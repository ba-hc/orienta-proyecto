#!/usr/bin/env python3
"""Exporta Markdown de Orienta E3 a DOCX y, opcionalmente, PDF.

Uso: python herramientas/exportar_documentos.py archivo.md [otro.md ...] [--pdf]
Solo requiere python-docx; PDF requiere LibreOffice instalado localmente.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import tempfile

try:
    from docx import Document
    from docx.enum.style import WD_STYLE_TYPE
    from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt, RGBColor
except ImportError as exc:
    raise SystemExit(
        "Falta python-docx en este intérprete. Instálalo con "
        f"'python -m pip install python-docx'. Detalle: {exc}"
    ) from exc


BLUE = "223C6A"
MONO = "Liberation Mono"
PDF_TIMEOUT = 120
HEADING = re.compile(r"^ {0,3}(#{1,4})[ \t]+(.*)$")
LIST_ITEM = re.compile(r"^([ \t]*)([-+*]|[0-9]+[.)])[ \t]+(.*)$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
SEPARATOR = re.compile(r":?-+:?")


class ExportError(Exception):
    """Error de entrada o conversión que puede mostrarse sin traceback."""


def xml_value(tag, value):
    element = OxmlElement(tag)
    element.set(qn("w:val"), str(value))
    return element


def set_font(font, name, size=None, *, color=None, bold=None):
    font.name = name
    # Word y LibreOffice usan también estos atributos al resolver Unicode.
    fonts = font._element.get_or_add_rPr().get_or_add_rFonts()
    for attribute in ("ascii", "hAnsi", "eastAsia", "cs"):
        fonts.set(qn(f"w:{attribute}"), name)
    if size is not None:
        font.size = Pt(size)
    if color is not None:
        font.color.rgb = RGBColor.from_string(color)
    if bold is not None:
        font.bold = bold


def body_font():
    """Consulta fuentes locales, sin instalar ni descargar nada."""
    executable = shutil.which("fc-list")
    if executable:
        try:
            result = subprocess.run(
                [executable, "--format=%{family}\n"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=10,
                check=False,
            )
            families = {
                name.strip().casefold()
                for line in result.stdout.splitlines()
                for name in line.split(",")
            }
            if result.returncode == 0 and "roboto" in families:
                return "Roboto"
        except (OSError, subprocess.TimeoutExpired):
            pass
    return "Aptos"


def new_document(font_name):
    document = Document()
    section = document.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.top_margin = section.bottom_margin = Cm(2)
    section.left_margin = section.right_margin = Cm(2)
    section.header_distance = section.footer_distance = Cm(0.8)

    normal = document.styles["Normal"]
    set_font(normal.font, font_name, 10.5, color="222222")
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.12
    normal.paragraph_format.widow_control = True
    normal.element.get_or_add_rPr().append(xml_value("w:lang", "es-CL"))

    for style_name, size in (
        ("Title", 22),
        ("Heading 1", 18),
        ("Heading 2", 14),
        ("Heading 3", 12),
    ):
        style = document.styles[style_name]
        set_font(style.font, "Poppins", size, color=BLUE, bold=True)
        style.paragraph_format.keep_with_next = True
        style.paragraph_format.keep_together = True
        style.paragraph_format.widow_control = True
        style.paragraph_format.space_before = Pt(14 if style_name != "Title" else 0)
        style.paragraph_format.space_after = Pt(6)

    for name, size, family in (("Orienta Code", 9, MONO), ("Orienta Table", 8.5, font_name)):
        style = document.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        style.base_style = normal
        set_font(style.font, family, size)
        style.paragraph_format.space_before = Pt(0)
        style.paragraph_format.space_after = Pt(2)
        style.paragraph_format.line_spacing = 1.05
        style.paragraph_format.keep_with_next = False
        style.paragraph_format.keep_together = False

    header = section.header.paragraphs[0]
    set_font(header.add_run("Orienta · Grupo 9 · E3").font, font_name, 8, color=BLUE)
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = footer.add_run()
    set_font(run.font, font_name, 8, color=BLUE)
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    field.set(qn("w:dirty"), "true")
    value = OxmlElement("w:r")
    text = OxmlElement("w:t")
    text.text = "1"
    value.append(text)
    field.append(value)
    run._r.addnext(field)
    document.settings.element.append(xml_value("w:updateFields", "true"))
    document.core_properties.author = "Orienta · Grupo 9"
    return document


def link_at(text, start):
    """Lee un enlace inline, incluyendo paréntesis balanceados de la URL."""
    close = text.find("](", start + 1)
    if close < 0:
        return None
    cursor, depth = close + 2, 1
    while cursor < len(text):
        char = text[cursor]
        if char == "\\" and cursor + 1 < len(text):
            cursor += 2
            continue
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return text[start + 1 : close], text[close + 2 : cursor], cursor + 1
        cursor += 1
    return None


def add_inline(paragraph, text, *, bold=False, links=True):
    """Interpreta solo formato textual: nunca abre URLs ni inserta recursos."""
    cursor, plain = 0, []

    def flush():
        if plain:
            run = paragraph.add_run("".join(plain))
            if bold:
                run.bold = True
            plain.clear()

    while cursor < len(text):
        if text[cursor] == "\\" and cursor + 1 < len(text):
            if text[cursor + 1] in r"\`*_{}[]()#+-.!|":
                plain.append(text[cursor + 1])
                cursor += 2
                continue
        if text[cursor] == "`":
            end = cursor + 1
            while end < len(text) and text[end] == "`":
                end += 1
            closing = text.find(text[cursor:end], end)
            if closing >= 0:
                flush()
                run = paragraph.add_run(text[end:closing])
                set_font(run.font, MONO)
                if bold:
                    run.bold = True
                cursor = closing + end - cursor
                continue
        if not bold and text.startswith("**", cursor):
            closing = text.find("**", cursor + 2)
            if closing > cursor + 2:
                flush()
                add_inline(paragraph, text[cursor + 2 : closing], bold=True, links=links)
                cursor = closing + 2
                continue
        if links and text[cursor] == "[" and (cursor == 0 or text[cursor - 1] != "!"):
            link = link_at(text, cursor)
            if link:
                flush()
                label, url, cursor = link
                url = url.strip()
                if url.startswith("<") and url.endswith(">"):
                    url = url[1:-1]
                add_inline(paragraph, label, bold=bold, links=False)
                if url and label != url:
                    run = paragraph.add_run(f" ({url})")
                    if bold:
                        run.bold = True
                continue
        plain.append(text[cursor])
        cursor += 1
    flush()


def table_cells(line):
    """Separa pipes fuera de código; conserva pipes escapados como texto."""
    cells, cell, cursor, code_fence = [], [], 0, 0
    line = line.strip()
    while cursor < len(line):
        char = line[cursor]
        if char == "\\" and cursor + 1 < len(line):
            cell.extend(line[cursor : cursor + 2])
            cursor += 2
            continue
        if char == "`":
            end = cursor + 1
            while end < len(line) and line[end] == "`":
                end += 1
            count = end - cursor
            if code_fence == 0:
                code_fence = count
            elif code_fence == count:
                code_fence = 0
            cell.append(line[cursor:end])
            cursor = end
            continue
        if char == "|" and not code_fence:
            cells.append("".join(cell).strip())
            cell.clear()
        else:
            cell.append(char)
        cursor += 1
    cells.append("".join(cell).strip())
    if line.startswith("|"):
        cells.pop(0)
    if line.endswith("|") and cells and cells[-1] == "":
        cells.pop()
    return cells


def table_start(lines, index):
    if index + 1 >= len(lines) or "|" not in lines[index]:
        return False
    header, separator = table_cells(lines[index]), table_cells(lines[index + 1])
    return (
        bool(header)
        and len(header) == len(separator)
        and all(SEPARATOR.fullmatch(cell) for cell in separator)
    )


def add_table(document, rows, separator):
    columns = len(rows[0])
    table = document.add_table(rows=0, cols=columns)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"
    table.autofit = False
    width = Cm(17 / columns)
    for column in table.columns:
        column.width = width
    for index, values in enumerate(rows):
        row = table.add_row()
        # Sin cantSplit: una fila más alta que la página puede continuar.
        if index == 0:
            row._tr.get_or_add_trPr().append(xml_value("w:tblHeader", "true"))
        for number, (cell, value) in enumerate(zip(row.cells, values)):
            cell.width = width
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
            paragraph = cell.paragraphs[0]
            paragraph.style = document.styles["Orienta Table"]
            if separator[number].endswith(":"):
                paragraph.alignment = (
                    WD_ALIGN_PARAGRAPH.CENTER
                    if separator[number].startswith(":")
                    else WD_ALIGN_PARAGRAPH.RIGHT
                )
            add_inline(paragraph, value)
            if index == 0:
                shade = OxmlElement("w:shd")
                shade.set(qn("w:fill"), BLUE)
                cell._tc.get_or_add_tcPr().append(shade)
                paragraph.paragraph_format.keep_with_next = True
                paragraph.paragraph_format.keep_together = True
                for run in paragraph.runs:
                    run.font.color.rgb = RGBColor(255, 255, 255)
                    run.bold = True


def list_numbering(document, ordered, start, level, font_name):
    root = document.part.numbering_part.element
    abstract_id = (
        max(
            (int(item.get(qn("w:abstractNumId"))) for item in root.findall(qn("w:abstractNum"))),
            default=-1,
        )
        + 1
    )
    abstract = OxmlElement("w:abstractNum")
    abstract.set(qn("w:abstractNumId"), str(abstract_id))
    abstract.append(xml_value("w:multiLevelType", "singleLevel"))
    lvl = OxmlElement("w:lvl")
    lvl.set(qn("w:ilvl"), "0")
    for tag, value in (
        ("w:start", start),
        ("w:numFmt", "decimal" if ordered else "bullet"),
        ("w:lvlText", "%1." if ordered else "•"),
        ("w:lvlJc", "left"),
    ):
        lvl.append(xml_value(tag, value))
    properties = OxmlElement("w:pPr")
    indent = OxmlElement("w:ind")
    indent.set(qn("w:left"), str(Cm(0.6 * (level + 1)).twips))
    indent.set(qn("w:hanging"), str(Cm(0.4).twips))
    properties.append(indent)
    lvl.append(properties)
    run_properties = OxmlElement("w:rPr")
    fonts = OxmlElement("w:rFonts")
    fonts.set(qn("w:ascii"), font_name)
    fonts.set(qn("w:hAnsi"), font_name)
    run_properties.append(fonts)
    lvl.append(run_properties)
    abstract.append(lvl)
    root.insert(0, abstract)
    return root.add_num(abstract_id).numId


def is_block(lines, index):
    line = lines[index]
    return bool(
        HEADING.match(line)
        or LIST_ITEM.match(line)
        or FENCE.match(line)
        or line.strip() == "---"
        or table_start(lines, index)
    )


def render_markdown(document, markdown, font_name):
    lines, cursor, list_stack = markdown.splitlines(), 0, []
    while cursor < len(lines):
        line = lines[cursor]
        if not line.strip():
            cursor += 1
            continue
        fence = FENCE.match(line)
        heading = HEADING.match(line)
        item = LIST_ITEM.match(line)
        if not item:
            list_stack.clear()
        if fence:
            delimiter = fence.group(1)
            end = cursor + 1
            while end < len(lines):
                candidate = lines[end].strip()
                if len(candidate) >= len(delimiter) and set(candidate) == {delimiter[0]}:
                    break
                end += 1
            paragraph = document.add_paragraph(style="Orienta Code")
            paragraph.add_run("\n".join(lines[cursor + 1 : end]))
            cursor = min(end + 1, len(lines))
        elif heading:
            level = len(heading.group(1))
            text = re.sub(r"[ \t]+#+[ \t]*$", "", heading.group(2))
            paragraph = document.add_paragraph(
                style="Title" if level == 1 else f"Heading {level - 1}"
            )
            add_inline(paragraph, text)
            if level == 1 and not document.core_properties.title:
                document.core_properties.title = text
            cursor += 1
        elif line.strip() == "---":
            paragraph = document.add_paragraph()
            paragraph.paragraph_format.space_after = Pt(6)
            paragraph.paragraph_format.space_before = Pt(3)
            paragraph.paragraph_format.line_spacing = Pt(2)
            border = OxmlElement("w:pBdr")
            bottom = xml_value("w:bottom", "single")
            bottom.set(qn("w:sz"), "4")
            bottom.set(qn("w:color"), BLUE)
            border.append(bottom)
            paragraph._p.get_or_add_pPr().append(border)
            cursor += 1
        elif table_start(lines, cursor):
            rows, separator = [table_cells(line)], table_cells(lines[cursor + 1])
            cursor += 2
            while cursor < len(lines) and lines[cursor].strip() and "|" in lines[cursor]:
                if (
                    HEADING.match(lines[cursor])
                    or FENCE.match(lines[cursor])
                    or LIST_ITEM.match(lines[cursor])
                ):
                    break
                cells = table_cells(lines[cursor])
                if len(cells) > len(rows[0]):
                    raise ExportError(
                        f"Tabla, línea {cursor + 1}: {len(cells)} celdas; "
                        f"la cabecera tiene {len(rows[0])}. Escapa los pipes literales con \\|."
                    )
                rows.append(cells + [""] * (len(rows[0]) - len(cells)))
                cursor += 1
            add_table(document, rows, separator)
        elif item:
            indent = len(item.group(1).expandtabs(4))
            ordered = item.group(2)[0].isdigit()
            while list_stack and list_stack[-1][0] > indent:
                list_stack.pop()
            if list_stack and list_stack[-1][0] == indent and list_stack[-1][1] != ordered:
                list_stack.pop()
            if not list_stack or list_stack[-1][0] != indent:
                level = min(len(list_stack), 8)
                start = int(item.group(2)[:-1]) if ordered else 1
                if not 1 <= start <= 2147483647:
                    raise ExportError(f"Numeración fuera de rango en la línea {cursor + 1}.")
                num_id = list_numbering(document, ordered, start, level, font_name)
                list_stack.append((indent, ordered, num_id, level))
            _, _, num_id, level = list_stack[-1]
            paragraph = document.add_paragraph()
            paragraph.paragraph_format.left_indent = Cm(0.6 * (level + 1))
            paragraph.paragraph_format.first_line_indent = -Cm(0.4)
            numbering = paragraph._p.get_or_add_pPr().get_or_add_numPr()
            numbering.get_or_add_ilvl().val = 0
            numbering.get_or_add_numId().val = num_id
            parts = [item.group(3)]
            cursor += 1
            while cursor < len(lines) and lines[cursor].strip() and not is_block(lines, cursor):
                parts.append(lines[cursor].strip())
                cursor += 1
            add_inline(paragraph, " ".join(parts))
        else:
            parts = [line.strip()]
            cursor += 1
            while cursor < len(lines) and lines[cursor].strip() and not is_block(lines, cursor):
                parts.append(lines[cursor].strip())
                cursor += 1
            add_inline(document.add_paragraph(), " ".join(parts))


def save_docx(document, destination):
    """Publica el archivo completo; conserva la salida previa si guardar falla."""
    descriptor, name = tempfile.mkstemp(prefix=".orienta-", suffix=".docx", dir=destination.parent)
    os.close(descriptor)
    temporary = Path(name)
    try:
        document.save(temporary)
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)


def convert_pdf(docx_path):
    executable = shutil.which("libreoffice") or shutil.which("soffice")
    if not executable:
        raise ExportError(
            "No se encontró LibreOffice/soffice; instala LibreOffice para usar --pdf."
        )
    destination = docx_path.with_suffix(".pdf")
    with tempfile.TemporaryDirectory(prefix="orienta-pdf-") as temporary:
        work = Path(temporary)
        profile = (work / "profile").as_uri()
        command = [
            executable,
            f"-env:UserInstallation={profile}",
            "--headless",
            "--nologo",
            "--nodefault",
            "--nofirststartwizard",
            "--convert-to",
            "pdf:writer_pdf_Export",
            "--outdir",
            str(work),
            str(docx_path),
        ]
        with subprocess.Popen(
            command,
            cwd=work,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            start_new_session=(os.name == "posix"),
        ) as process:
            try:
                output, _ = process.communicate(timeout=PDF_TIMEOUT)
            except subprocess.TimeoutExpired as exc:
                if os.name == "posix":
                    try:
                        os.killpg(process.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                else:
                    process.kill()
                process.communicate()
                raise ExportError(
                    f"LibreOffice excedió el límite de {PDF_TIMEOUT} s para {docx_path.name}; "
                    "se conserva el DOCX."
                ) from exc
        generated = work / destination.name
        if process.returncode != 0 or not generated.is_file():
            detail = output.strip()[-2000:] or "sin detalles del conversor"
            raise ExportError(
                f"LibreOffice no generó el PDF (salida {process.returncode}): {detail}"
            )
        with generated.open("rb") as stream:
            if stream.read(5) != b"%PDF-":
                raise ExportError("LibreOffice produjo una salida que no es un PDF válido.")
        descriptor, name = tempfile.mkstemp(
            prefix=".orienta-", suffix=".pdf", dir=destination.parent
        )
        os.close(descriptor)
        staging = Path(name)
        try:
            shutil.copyfile(generated, staging)
            os.replace(staging, destination)
        finally:
            staging.unlink(missing_ok=True)
    return destination


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archivos", nargs="+", type=Path, metavar="archivo.md")
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="Generar también PDF con LibreOffice (límite: 120 s/archivo).",
    )
    args = parser.parse_args(argv)
    font_name = body_font()
    if font_name == "Aptos":
        print("Aviso: Roboto no detectada; el cuerpo se declara en Aptos.", file=sys.stderr)
    failures, seen = 0, set()
    for argument in args.archivos:
        source = argument.expanduser().absolute()
        if source in seen:
            continue
        seen.add(source)
        try:
            if source.suffix.casefold() not in {".md", ".markdown"}:
                raise ExportError("Se esperaba un archivo .md o .markdown.")
            if not source.is_file():
                raise ExportError("El archivo Markdown no existe o no es un archivo regular.")
            markdown = source.read_text(encoding="utf-8-sig")
            document = new_document(font_name)
            render_markdown(document, markdown, font_name)
            destination = source.with_suffix(".docx")
            save_docx(document, destination)
            print(f"DOCX: {destination}", flush=True)
            if args.pdf:
                print(f"PDF: {convert_pdf(destination)}", flush=True)
        except (OSError, UnicodeError, ValueError, ExportError) as exc:
            failures += 1
            print(f"ERROR: {source}: {exc}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
