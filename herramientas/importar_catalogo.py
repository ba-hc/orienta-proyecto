"""RF-18: validación en seco por defecto, importación transaccional explícita."""

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orienta.settings")
import django

django.setup()
from orienta.catalogue import import_catalogue, validate_catalogue

parser = argparse.ArgumentParser()
parser.add_argument("snapshot", type=Path)
parser.add_argument("--aplicar", action="store_true")
args = parser.parse_args()
payload = json.loads(args.snapshot.read_text(encoding="utf8"))
source, rows = validate_catalogue(payload)
pdf = ROOT / "docs/fuentes/oferta_definitiva_2027.pdf"
if pdf.exists():
    import hashlib

    if hashlib.sha256(pdf.read_bytes()).hexdigest() != source["sha256"]:
        raise SystemExit("El hash de la fuente no coincide con el PDF conservado")
if args.aplicar:
    print(f"Importación atómica: {import_catalogue(payload)} ofertas verificadas por esquema.")
else:
    print(f"Validación en seco: {len(rows)} ofertas; no se modificó la base.")
