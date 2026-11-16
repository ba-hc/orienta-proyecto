"""Carga únicamente el extracto revisado de duraciones, con límite de vigencia."""

import json
import os
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orienta.settings")
import django

django.setup()
from django.db import transaction
from orienta.models import Datum, Offer, Source

with transaction.atomic():
    rows = json.loads((ROOT / "data/atributos_verificados.json").read_text())
    for row in rows:
        if (
            urlparse(row["url"]).hostname != "admision.udec.cl"
            or urlparse(row["url"]).scheme != "https"
            or row["dimension"] != "duracion"
            or not 1 <= row["value"] <= 30
        ):
            raise ValueError("Extracto fuera del contrato de duraciones verificadas")
        source, _ = Source.objects.get_or_create(
            url=row["url"],
            sha256=row["sha256"],
            defaults={
                "title": row["title"],
                "retrieved": row["retrieved"],
            },
        )
        offer = Offer.objects.get(code=row["code"], cycle=2027)
        Datum.objects.update_or_create(
            offer=offer,
            dimension="duracion",
            defaults={
                "source": source,
                "value": row["value"],
                "unit": row["unit"],
                "period": row["period"],
            },
        )
print(
    f"{len(rows)} duraciones publicadas cargadas. Aranceles y cohortes sin vigencia permanecen ausentes."
)
