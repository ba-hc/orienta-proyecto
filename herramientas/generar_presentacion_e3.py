"""Presentación académica editable; copia y dirección visual definidas por el principal."""

import json
import re
from pathlib import Path
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "entrega"
OUT.mkdir(exist_ok=True)
BLUE, GOLD, INK, MUTED, PALE, GREEN = "223C6A", "E69B0A", "142840", "53677B", "F3F6F9", "087F7C"
load = json.loads((ROOT / "evidencia/carga.json").read_text())
coverage = json.loads((ROOT / "evidencia/cobertura.json").read_text())["totals"]
study = json.loads((ROOT / "evidencia/encuestas_reanalisis.json").read_text())["aggregates"]
restore = json.loads((ROOT / "evidencia/restauracion.json").read_text())
notes_source = (ROOT / "docs/E3/Guion_Oral_10_Minutos.md").read_text()
notes = re.split(r"\n## \d+ [·–] ", notes_source)[1:]


def text(slide, value, x, y, w, h, size=22, color=INK, bold=False, font="Roboto"):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    for index, line in enumerate(value.split("\n")):
        p = tf.paragraphs[0] if index == 0 else tf.add_paragraph()
        p.text = line
        p.font.name, p.font.size, p.font.bold = font, Pt(size), bold
        p.font.color.rgb = RGBColor.from_string(color)
        p.space_after = Pt(12)
    return shape


def rect(slide, x, y, w, h, fill, border=None):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    s.fill.solid()
    s.fill.fore_color.rgb = RGBColor.from_string(fill)
    s.line.fill.background() if not border else None
    if border:
        s.line.color.rgb = RGBColor.from_string(border)
    return s


def slide(prs, title, source="", notes_text=""):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = RGBColor(255, 255, 255)
    text(s, title, 0.65, 0.48, 12.0, 0.95, 31, BLUE, True, "Poppins")
    rect(s, 0.65, 1.56, 12.0, 0.035, GOLD)
    text(s, "Orienta · Grupo 9 · Revisión crítica de diseño", 0.65, 7.08, 9.5, 0.2, 10, MUTED)
    text(s, str(len(prs.slides)), 12.05, 7.04, 0.4, 0.25, 11, MUTED)
    if source:
        text(s, source, 0.65, 6.65, 11.9, 0.33, 10, MUTED)
    s.notes_slide.notes_text_frame.text = notes_text + "\n\nFuentes y límites: " + source
    return s


def table(slide_obj, headers, rows, y=2.0, h=4.2, widths=None, size=17):
    shape = slide_obj.shapes.add_table(
        len(rows) + 1, len(headers), Inches(0.65), Inches(y), Inches(12), Inches(h)
    )
    t = shape.table
    if widths:
        for column, width in zip(t.columns, widths):
            column.width = Inches(width)
    for row_idx, values in enumerate([headers, *rows]):
        for col_idx, value in enumerate(values):
            cell = t.cell(row_idx, col_idx)
            cell.text = str(value)
            cell.margin_left = cell.margin_right = Inches(0.12)
            cell.margin_top = Inches(0.1)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor.from_string(
                BLUE if row_idx == 0 else (PALE if row_idx % 2 else "FFFFFF")
            )
            for p in cell.text_frame.paragraphs:
                p.font.name, p.font.size = "Roboto", Pt(size)
                p.font.bold = row_idx == 0
                p.font.color.rgb = RGBColor.from_string("FFFFFF" if row_idx == 0 else INK)
    return shape


prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)

s = slide(
    prs,
    "Orienta · Revisión crítica de diseño",
    "E3 / Avance oral 2 · 16 de noviembre de 2026 · DIICC, Universidad de Concepción",
    notes[0] if notes else "",
)
s.shapes.add_picture(
    str(ROOT / "docs/identidad/UdeC_horizontal.png"), Inches(9.8), Inches(2.02), width=Inches(2.75)
)
text(
    s,
    "Un recorrido construido.\nDecisiones que se pueden comprobar.",
    0.65,
    2.0,
    8.8,
    1.65,
    33,
    BLUE,
    True,
    "Poppins",
)
text(
    s,
    "Intereses → prioridades → dos ofertas → comparación → recuperación",
    0.65,
    4.0,
    11.8,
    0.7,
    23,
    INK,
)
text(
    s,
    "Jorge Alejandro Slimming Lagos · Benjamín Alonso Henríquez Cid\nDiego Alejandro Gutiérrez Mendoza · Mauro Sebastián Muñoz González\nLucas Daniel Morales Oyanedel",
    0.65,
    5.1,
    12,
    1.1,
    16,
    MUTED,
)

s = slide(
    prs,
    "La necesidad local y sus límites",
    "SRS E1, instrumento y apéndice; reanálisis de 192 registros. SIES 2026: retención cohorte 2025. Ver Fuentes_Publicas.md.",
    notes[1] if len(notes) > 1 else "",
)
for i, (key, label) in enumerate(
    [("Q4", "Indecisión"), ("Q5", "Varias opciones"), ("Q7", "Temor a equivocarse")]
):
    count = study["estudiantes"]["items"][key]["agreement_4_5"]
    yy = 2.05 + i * 1.13
    text(s, label, 0.65, yy, 3, 0.35, 20, INK)
    rect(s, 3.9, yy, 3.2, 0.37, PALE)
    rect(s, 3.9, yy, 3.2 * count / 156, 0.37, GREEN)
    text(s, f"{count}/156", 7.25, yy, 1.3, 0.4, 20, BLUE, True)
text(
    s,
    "Muestra de conveniencia; respuestas 4–5.\nNo es prevalencia nacional ni prueba de uso.",
    0.65,
    5.7,
    8.1,
    0.7,
    17,
    MUTED,
)
text(s, "77,9 % de retención", 9.0, 2.05, 3.6, 0.7, 25, BLUE, True)
text(
    s,
    "Contexto público SIES.\nLa no continuidad tiene múltiples causas.\n\nLa utilidad de Orienta sigue siendo una hipótesis a validar.",
    9.0,
    2.95,
    3.6,
    2.9,
    20,
    INK,
)

s = slide(
    prs,
    "Tres iteraciones con efecto verificado",
    "Comentarios aportados del escrito; puntajes PDR sin comentarios cualitativos adicionales. Respuesta_Docente_Iteraciones.md.",
    notes[2] if len(notes) > 2 else "",
)
table(
    s,
    ["Disparador", "Decisión", "Efecto comprobado"],
    [
        [
            "PoC en JSON; importación y supresión sin contrato",
            "Modelo relacional, RF18 y RF19",
            "Lote inválido sin efectos; guardado único; borrado en cascada",
        ],
        [
            "Fuentes con ciclos/períodos mezclados",
            "Snapshot y procedencia por campo",
            "91 ofertas 2027; faltantes explícitos; sin diferencia inválida",
        ],
        [
            "Alta de navegador devuelve 403",
            "Referrer-Policy: same-origin, conservando CSRF",
            "Alta 302; flujo completo en Chromium y Firefox",
        ],
    ],
    h=4.5,
    size=19,
)

s = slide(
    prs,
    "CI1 · Las claves gobiernan el diseño",
    "E1 comprometió dependencias funcionales y 3FN. Migraciones 0001/0002, Ciencias_Ingenieria.md y pruebasCI1/RF18/RF19.",
    notes[3] if len(notes) > 3 else "",
)
for x, title, body in [
    (0.65, "Fuente", "URL + hash\nIdentidad de snapshot"),
    (4.75, "Oferta", "Código + ciclo\nCarrera · campus · fuente"),
    (8.85, "Dato", "Oferta + dimensión\nValor · unidad · período"),
]:
    rect(s, x, 2.0, 3.8, 1.65, PALE)
    text(s, title, x + 0.18, 2.15, 3.4, 0.35, 23, BLUE, True)
    text(s, body, x + 0.18, 2.65, 3.4, 0.85, 19, INK)
text(
    s,
    "Una revisión nueva conserva la fuente anterior.\nUNIQUE evita duplicados; CHECK impide el mismo par; CASCADE borra el proceso propio.\nLa prueba verifica integridad; la 3FN se justifica con dependencias.",
    0.65,
    4.1,
    11.9,
    1.85,
    23,
    INK,
)

s = slide(
    prs,
    "CI2 · Integridad y acceso con controles negativos",
    "Django 5.2; AESGCM de cryptography; NIST SP800-38D. Pruebas de credenciales, caducidad, propiedad, CSRF y alteración.",
    notes[4] if len(notes) > 4 else "",
)
text(
    s,
    "Credencial adaptativa → sesión de 30 min → consulta por propietario",
    0.65,
    2.05,
    12,
    0.65,
    25,
    BLUE,
    True,
)
text(
    s,
    "AES-256-GCM: nonce de 96 bits + respuesta + UUID/ítem/versión como datos asociados.\n\nCambiar etiqueta, ítem o proceso invalida la respuesta.\nLeer, editar o suprimir el proceso ajeno no está permitido.",
    0.65,
    3.05,
    11.9,
    2.35,
    23,
    INK,
)
text(
    s,
    "Límite: cifrado de respuestas ≠ cifrado de todo el almacenamiento. Demo local con datos ficticios.",
    0.65,
    5.82,
    11.9,
    0.6,
    18,
    MUTED,
)

s = slide(
    prs,
    "Demostración en vivo · el estado persiste",
    "Captura real del sistema; la exposición debe abrir el navegador y ejecutar el flujo. Guion_Demo.md; respuestas de prueba.",
    notes[5] if len(notes) > 5 else "",
)
text(
    s,
    "Entrar → intereses → prioridades → catálogo → guardar → comparar → salir y retomar",
    0.65,
    1.86,
    12,
    0.65,
    21,
    BLUE,
    True,
)
pic = s.shapes.add_picture(
    str(ROOT / "evidencia/navegador/chromium-1440-comparacion.png"),
    Inches(0.65),
    Inches(2.7),
    width=Inches(8.3),
    height=Inches(3.65),
)
pic.crop_top, pic.crop_bottom = 0.27, 0.19
text(
    s,
    "91 ofertas oficiales\nPar distinto\nPrioridad declarada\nFuente y faltantes\nRecuperación propia\nSupresión confirmada",
    9.4,
    2.75,
    3.15,
    3.6,
    20,
    INK,
)

s = slide(
    prs,
    "Verificación reproducible en cuatro niveles",
    "evidencia/pruebas.log, cobertura.json, e2e.json, auditoria_web.json; CI vinculada alSHA publicado. Versiones y límites en losJSON.",
    notes[6] if len(notes) > 6 else "",
)
table(
    s,
    ["Nivel", "Resultado observado", "Qué acredita"],
    [
        [
            "Dominio e integración",
            "24 pruebas; contratos positivos y negativos",
            "RF/RB, claves, importación, integridad y permisos",
        ],
        [
            "Cobertura",
            f"{coverage['covered_lines']}/{coverage['num_statements']} líneas; {coverage['covered_branches']}/{coverage['num_branches']} ramas",
            "Ramas críticas por encima de 80 %; no porcentaje de MVP",
        ],
        [
            "Extremo a extremo",
            "Chromium  + Firefox;360 y 1440 px",
            "4 recorridos con recuperación y supresión",
        ],
        [
            "Accesibilidad automática",
            "Axe: 0 incidencias en 12 pantallas",
            "Alcance automático; lector/criterios manuales pendientes",
        ],
    ],
    h=4.4,
    size=18,
)

s = slide(
    prs,
    "RNF · valores y límites del resultado",
    "Carga: 50 VU, 360 procesos, 70/30, host compartido, runtime aislado. Datos sintéticos. RNF_Mediciones.md reporta los 21 RNF.",
    notes[7] if len(notes) > 7 else "",
)
table(
    s,
    ["Contrato", "Objetivo", "Resultado / veredicto"],
    [
        ["Consulta / guardado", "p95≤1000ms", f"{load['p95_ms']:.0f}ms · cumple local"],
        [
            "Fallos",
            "≤1% con 50 sesiones",
            f"0/{load['operations']:,} · {load['wall_seconds']:.1f}s · cumple local",
        ],
        [
            "Restauración",
            "RTO≤4h",
            f"{restore['restoration_seconds']:.2f}s ejercicio · RPO periódico sin acreditar",
        ],
        [
            "Entorno para personas reales",
            "TLS+cifrado integral",
            "Pendiente; el cifrado de campo no cierra este RNF",
        ],
        [
            "Disponibilidad / WebVitals",
            "Ventana real / p75 de campo",
            "Sin período o muestra de campo; no se declara cumplido",
        ],
    ],
    h=4.3,
    size=18,
)

s = slide(
    prs,
    "Validación: necesidades reales, uso por comprobar",
    "Encuestas_Reanalisis.md; Validacion_Usuarios.md; CSV sin filas ficticias. La encuesta no sustituye tareas de uso de E3.",
    notes[8] if len(notes) > 8 else "",
)
text(s, "156 estudiantes  + 36 apoderados", 0.65, 2.05, 12, 0.65, 29, BLUE, True)
text(
    s,
    "Reanálisis descriptivo del apéndice E1, con instrumento y frecuencias.\nSin extrapolación ni recodificación monetaria de Q13A.",
    0.65,
    3.0,
    11.8,
    1.2,
    23,
    INK,
)
text(s, "Preparado para el estudio de uso", 0.65, 4.5, 11.8, 0.45, 24, BLUE, True)
text(
    s,
    "5 tareas · éxito sin ayuda · tiempos · errores · comprensión de límites.\nMeta ≥4/5; requiere participantes externos y registros reales.",
    0.65,
    5.1,
    11.8,
    1.05,
    22,
    INK,
)

s = slide(
    prs,
    "Costos · estimación, caja y esfuerzo separados",
    "E1, tabla de presupuesto; referencia pública UdeC/MiFuturo +DT 42 h. Costos_Riesgos_Plan.md; sin compras ni contratación nuevas.",
    notes[9] if len(notes) > 9 else "",
)
table(
    s,
    ["Dimensión", "Línea base", "Corte E3"],
    [
        [
            "Esfuerzo planificado",
            "400 HH +100 HH reserva",
            "HH humanas ejecutadas sin bitácora aportada",
        ],
        ["Caja", "Techo interno CLP 100.000", "CLP 0 de nuevos desembolsos; hardware existente"],
        [
            "Costo de oportunidad",
            "Tarifas por rol sin fuente",
            "Rango uniforme CLP 13.736–16.484/h; sensibilidad",
        ],
        [
            "Continuidad",
            "Proyección académica",
            "Sin servicio permanente contratado ni aceptación de responsable",
        ],
    ],
    h=4.3,
    size=18,
)

s = slide(
    prs,
    "Replanificar a partir de los riesgos",
    "Corte S15 posterior a E3/S14; sin prórroga inventada. Registro de 10 riesgos con disparador, gestión, residual y rol propuesto.",
    notes[10] if len(notes) > 10 else "",
)
table(
    s,
    ["Ventana", "Prioridad", "Criterio para continuar"],
    [
        ["S15", "Cerrar construcción y evidenciaE3", "Must, catálogo, CI y medición verificables"],
        [
            "S15–16",
            "Usuarios y controles operativos",
            "Datos reales y segundo operador; sin simular aceptación",
        ],
        [
            "S17",
            "InformeE4 y continuidad",
            "Evidencias consolidadas, responsable y costos acreditados",
        ],
        ["S17–18", "Ensayo ydemoE5", "Participación real de todos y contingencia probada"],
    ],
    h=3.8,
    size=19,
)
text(
    s,
    "Fuera del corte: exportación, panel, chat IA yranking. Se priorizan derechos, verificación y comprensión.",
    0.65,
    6.0,
    12,
    0.5,
    18,
    MUTED,
)

s = slide(
    prs,
    "Lo construido se sostiene con evidencia",
    "Repositorio independiente ypaquete reproducible. La exposición, la validación externa y la aceptación docente requieren ejecución real.",
    notes[11] if len(notes) > 11 else "",
)
text(
    s,
    "Recorrido persistente con catálogo oficial.\nTres iteraciones con disparador y comprobación.\nDos aplicaciones de ingeniería integradas.\nPruebas y RNF con valores, denominadores y límites.",
    0.65,
    2.1,
    11.8,
    2.6,
    27,
    BLUE,
    True,
)
text(
    s,
    "La decisión sigue siendo del estudiante.\nLas brechas humanas y operativas quedan declaradas.",
    0.65,
    5.15,
    12,
    1.0,
    23,
    INK,
)

s = slide(
    prs,
    "Referencias de la exposición",
    "Las fuentes completas, fechas, hashes yrestricciones de uso se conservan en el repositorio.",
)
text(
    s,
    "Rúbrica R3 pp6–7; enunciadoE3 p8; SRS E1 v1.8 y plantilla IEEE830.\nDEMRE/Mineduc · Oferta Definitiva 2027, páginas 294–300.\nSIES · Informe de retención de primer año, cohorte 2025.\nAdmisión UdeC · Informática, Medicina yPsicología.\nDjango 5.2 · auth, CSRF yORM; cryptography · AESGCM; NIST SP800-38D.\nDT · jornada de 42 horas; BCN · Decreto 8144, Leyes 19.628 y21.719.\nArtefactos propios: pruebas, coverage, Playwright, axe, carga yrestauración.",
    0.65,
    2.0,
    12,
    4.3,
    22,
    INK,
)
prs.save(OUT / "Orienta_E3_Exposicion.pptx")

s = slide(
    prs,
    "Respaldo · frontera del sistema y operación",
    "Diagramas editables DOT y SVG/PNG en docs/modelos. HTTP loopback es el entorno de demostración, no despliegue real.",
)
s.shapes.add_picture(
    str(ROOT / "docs/modelos/C4_Contenedores.png"), Inches(0.75), Inches(2.05), width=Inches(11.8)
)

s = slide(
    prs,
    "Respaldo · el escenario de carga es explícito",
    "evidencia/carga.json y 30.000 eventosJSONL; entorno y comando reproducible. Sin usuarios reales ni tráfico escolar.",
)
table(
    s,
    ["Configuración", "Valor"],
    [
        ["Carga", "50 sesiones, 360 procesos, 91 ofertas,70/30"],
        ["Ejecución", f"{load['wall_seconds']:.2f}s;30.000 operaciones"],
        ["Servidor", "Gunicorn 1 worker/16 threads; SQLite IMMEDIATE; loopback"],
        [
            "Latencia",
            f"p50 {load['p50_ms']:.1f}ms /p95 {load['p95_ms']:.1f}ms /p99 {load['p99_ms']:.1f}ms",
        ],
        ["Fallos", "0 HTTP 5xx y0 errores decontrato funcional"],
    ],
    h=4.3,
    widths=[3.3, 8.7],
    size=19,
)

s = slide(
    prs,
    "Respaldo · los datos no publicados no se inventan",
    "data/catalogo_udec_2027.json, data/atributos_verificados.json y PDF original. Hash dePDF distinto dehash deextracto curado.",
)
text(
    s,
    "Oferta: código, campus, ciclo, fuente y página.\nDato: dimensión, valor, unidad, período y fuente.\nFuente: URL, fecha y hash de snapshot.\n\n3 duraciones verificadas con límite de vigencia.\nAranceles/empleabilidad sin año o cohorte: información no disponible.\nUna nueva revisión conserva la fuente anterior.",
    0.65,
    2.0,
    12,
    4.4,
    24,
    INK,
)

s = slide(
    prs,
    "Respaldo · preguntas que debemos poder responder",
    "Preguntas_Defensa.md desarrolla respuestas con evidencia y límites.",
)
text(
    s,
    "¿Por qué SQLite aquí y cuándo migrar a PostgreSQL?\n¿Qué prueba la 3FN yqué prueban los tests?\n¿Qué impide trasplantar una respuesta cifrada?\n¿Qué mide exactamente el p95 y cuál es el denominador de fallos?\n¿Por qué la encuesta no demuestra usabilidad?\n¿Qué falta antes de operar con personas reales?",
    0.65,
    2.0,
    12,
    4.4,
    24,
    INK,
)
prs.save(OUT / "Orienta_E3_Entrega.pptx")
print("Presentaciones editables:13 láminas de exposición y17 deentrega.")
