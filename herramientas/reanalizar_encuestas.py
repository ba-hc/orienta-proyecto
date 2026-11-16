"""Recalcula agregados del apéndice desidentificado de E1, sin exportar filas."""

import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from reportlab.lib import colors
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
pdf = ROOT / "docs/fuentes/SRS_E1_original.pdf"
text = subprocess.check_output(["pdftotext", "-layout", str(pdf), "-"], text=True)
columns = ["curso", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10", "TL", "Q11", "Q12", "Q13"]
groups = {"estudiantes": [], "apoderados": []}
ids = set()
for line in text.splitlines():
    match = re.match(r"^\s*([EA]-\d{3})\s+([0-9\s]+)$", line)
    if not match:
        continue
    identifier, values = match[1], [int(x) for x in match[2].split()]
    if identifier in ids:
        raise ValueError("Código duplicado en extracción")
    ids.add(identifier)
    names = columns + (["Q14"] if identifier.startswith("A-") else [])
    if len(values) != len(names):
        raise ValueError(f"Fila incompleta: {identifier}")
    groups["apoderados" if identifier.startswith("A-") else "estudiantes"].append(
        dict(zip(names, values))
    )
assert len(groups["estudiantes"]) == 156 and len(groups["apoderados"]) == 36
aggregates = {}
for name, rows in groups.items():
    stats = {}
    for key in ["Q4", "Q5", "Q6", "Q7", "Q8", "Q9"] + (["Q14"] if name == "apoderados" else []):
        values = [r[key] for r in rows]
        assert all(1 <= v <= 5 for v in values)
        stats[key] = {
            "n": len(values),
            "frequencies": dict(sorted(Counter(values).items())),
            "agreement_4_5": sum(v >= 4 for v in values),
            "disagreement_1_2": sum(v <= 2 for v in values),
        }
    stats["Q11_no_test"] = sum(r["Q11"] == 0 for r in rows)
    stats["Q13_categories"] = dict(sorted(Counter(r["Q13"] for r in rows).items()))
    aggregates[name] = {"n": len(rows), "items": stats}
report = {
    "source": str(pdf.relative_to(ROOT)),
    "source_pages": "Apéndice A-Datos, pp41–49; instrumento pp29–31",
    "method": "Extracción de filas tabulares desidentificadas de PDF; conteos ordinales4/5 y1/2; sin media monetariaQ13A ni estimación poblacional",
    "aggregates": aggregates,
    "limits": "Fuente secundaria del equipo: se audita la transcripción E1, no exportación original del formulario. Muestra de conveniencia de mayo2026. Necesidades declaradas, no prueba de uso/utilidad de la versiónE3. Consentimiento reportado enE1, sin nueva atribución de sesiones.",
}
(ROOT / "evidencia/encuestas_reanalisis.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n"
)
labels = [
    ("Q4", "Indecisión de carrera", "agreement_4_5"),
    ("Q5", "Varias opciones sin convicción", "agreement_4_5"),
    ("Q6", "Sensación de decidir a ciegas", "agreement_4_5"),
    ("Q7", "Temor a equivocarse", "agreement_4_5"),
    ("Q8", "Autoconocimiento insuficiente", "agreement_4_5"),
    ("Q9", "Desacuerdo con herramientas suficientes", "disagreement_1_2"),
]
c = canvas.Canvas(str(ROOT / "docs/E3/Encuestas_Resultados.pdf"), pagesize=(842, 595))
c.setTitle("Orienta · Reanálisis descriptivo de necesidades")
c.setFillColor(colors.HexColor("#223C6A"))
c.setFont("Helvetica-Bold", 24)
c.drawString(44, 546, "Qué declararon los estudiantes")
c.setFillColor(colors.HexColor("#53677B"))
c.setFont("Helvetica", 12)
c.drawString(
    44, 518, "156 registros de E1 · muestra de conveniencia · no valida el uso del producto"
)
lines = []
for index, (key, label, metric) in enumerate(labels):
    n = aggregates["estudiantes"]["items"][key][metric]
    y = 455 - index * 57
    c.setFillColor(colors.HexColor("#142840"))
    c.setFont("Helvetica", 11)
    c.drawString(44, y + 9, label)
    c.setFillColor(colors.HexColor("#EDF2F6"))
    c.rect(335, y, 355, 28, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#087F7C"))
    c.rect(335, y, 355 * n / 156, 28, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#142840"))
    c.setFont("Helvetica-Bold", 11)
    c.drawString(704, y + 9, f"{n}/156 ({n / 156:.1%})")
    lines.append(f"| {key} | {label} | {n}/156 | {n / 156:.1%} |")
c.setFont("Helvetica", 10)
c.setFillColor(colors.HexColor("#53677B"))
c.drawString(
    44,
    72,
    "Q4–Q8: respuestas4–5; Q9: respuestas1–2 a enunciado positivo. No son prevalencias nacionales.",
)
c.drawString(
    44,
    54,
    "Fuente: SRS E1 v1.8, apéndice desidentificado. Reproducción: herramientas/reanalizar_encuestas.py.",
)
c.save()
md = (
    """# Reanálisis de evidencia real de necesidades

Se reanalizaron los registros desidentificados ya aportados en el SRS E1:156 estudiantes y36 apoderados. No se reclutaron nuevos participantes ni se imputaron respuestas. La fuente es el apéndice del informe, no la exportación original; esta limitación permanece.

| Ítem | Interpretación descriptiva | Conteo | Proporción muestral |
| --- | --- | --- | --- |
"""
    + "\n".join(lines)
    + "\n\n"
)
md += "El instrumento contiene escalas ordinales1–5; se reportan conteos por categorías sin sumar un diagnóstico. Se distinguió la polaridad deQ9. Los códigos monetariosQ13A se conservaron como categorías con solapamientos; no se calculó promedio ni precio. El JSON incluye frecuencias completas y permite contrastar los conteos.\n\n"
md += "Conclusión de alcance: los datos justifican contrastar necesidades de claridad, información y autoconocimiento en la muestra. No establecen adopción, efectividad, causalidad ni éxito de tareas de la aplicación. Tampoco prueban que otras plataformas sean insuficientes. ParaE3 se añade esta auditoría como evidencia histórica de necesidades; la validación de uso de la versión construida requiere sesiones reales con su instrumento, éxito/ayuda/errores/tiempos.\n\n"
md += "Consecuencia de diseño: mantener agencia del estudiante; no emitir ganadora; explicar fuentes/faltantes y límites; permitir guardar/retomar. Estos vínculos son hipótesis de requisitos, no preferencias de interfaz demostradas. Ver instrumento y protocolo en Validacion_Usuarios.md.\n"
(ROOT / "docs/E3/Encuestas_Reanalisis.md").write_text(md)
print(json.dumps({name: values["n"] for name, values in aggregates.items()}))
