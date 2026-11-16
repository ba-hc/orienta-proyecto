"""Resume registros reales; una plantilla vacía nunca produce validación ficticia."""

import argparse
import csv
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("csv", type=Path, nargs="?", default=ROOT / "data/validacion_usuarios.csv")
args = parser.parse_args()
with args.csv.open(encoding="utf-8-sig", newline="") as handle:
    rows = list(csv.DictReader(handle))
if not rows:
    print("PENDIENTE: no hay sesiones reales en el CSV. No se generan resultados.")
    raise SystemExit(2)
participants = defaultdict(dict)
for row in rows:
    pid, task = row["participant_id"], row["tarea"]
    if (
        not pid.startswith("P")
        or not pid[1:].isdigit()
        or task not in {f"T{i}" for i in range(1, 6)}
    ):
        raise SystemExit("Identificador o tarea inválida")
    if task in participants[pid]:
        raise SystemExit("Participante/tarea duplicado: no se infla el denominador")
    if row["consentimiento_registrado"] != "si" or row["mayor18"] != "si":
        raise SystemExit(
            "Este protocolo requiere consentimiento registrado y participantes adultos"
        )
    if row["completada"] not in {"si", "no"} or row["ayuda"] not in {"si", "no"}:
        raise SystemExit("Resultado/ayuda deben ser si o no")
    elapsed, errors = float(row["segundos"]), int(row["errores"])
    if not math.isfinite(elapsed) or elapsed < 0 or errors < 0:
        raise SystemExit("Medición numérica inválida")
    participants[pid][task] = {
        "success_without_help": row["completada"] == "si" and row["ayuda"] == "no",
        "seconds": elapsed,
        "errors": errors,
    }
if any(set(tasks) != {f"T{i}" for i in range(1, 6)} for tasks in participants.values()):
    raise SystemExit("Faltan tareas: no se excluyen silenciosamente del estudio")
n = len(participants)
successes = sum(tasks["T4"]["success_without_help"] for tasks in participants.values())
times = [tasks["T4"]["seconds"] for tasks in participants.values()]
report = {
    "participants": n,
    "T4_success_without_help": successes,
    "proportion": successes / n,
    "T4_median_seconds": statistics.median(times),
    "T4_range_seconds": [min(times), max(times)],
    "RNF_U02_threshold": 0.8,
    "threshold_observed": successes / n >= 0.8 and n >= 3,
    "limits": "Muestra intencional; no extrapolable. La comprensión correcta de límites y autenticidad de participantes exige revisión humana del instrumento, no inferencia automática del CSV.",
}
(ROOT / "evidencia/validacion_usuarios.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n"
)
print(json.dumps(report, ensure_ascii=False))
