"""Importación explícita de un snapshot local; sin requests ni URLs ejecutables."""

import datetime
import re
from urllib.parse import urlparse
from django.core.exceptions import ValidationError
from django.db import transaction
from .domain import DIMENSIONS
from .models import Campus, Career, Datum, Offer, Source


def validate_catalogue(payload):
    if not isinstance(payload, dict) or payload.get("schema") != 1:
        raise ValidationError("Esquema de catálogo inválido")
    source = payload.get("source", {})
    if urlparse(source.get("url", "")).scheme != "https" or urlparse(
        source.get("url", "")
    ).hostname not in {"acceso.mineduc.cl", "admision.udec.cl"}:
        raise ValidationError("Fuente fuera de los dominios oficiales permitidos")
    if not re.fullmatch(r"[0-9a-f]{64}", source.get("sha256", "")):
        raise ValidationError("El snapshot debe declarar SHA-256")
    try:
        datetime.date.fromisoformat(source["retrieved"])
    except (KeyError, ValueError, TypeError) as error:
        raise ValidationError("Fecha de consulta inválida") from error
    if not source.get("title") or len(source["title"]) > 180:
        raise ValidationError("Título de fuente inválido")
    offers = payload.get("offers", [])
    if not isinstance(offers, list) or not 1 <= len(offers) <= 1000:
        raise ValidationError("Se esperan entre 1 y 1000 ofertas")
    keys = set()
    for row in offers:
        if (
            not isinstance(row, dict)
            or not re.fullmatch(r"13\d{3}", str(row.get("code", "")))
            or row.get("cycle") != 2027
        ):
            raise ValidationError("Código o ciclo inválidos")
        if (
            not isinstance(row.get("name"), str)
            or not 1 <= len(row["name"]) <= 180
            or row.get("campus") not in {"Concepción", "Chillán", "Los Ángeles"}
        ):
            raise ValidationError("Carrera o campus inválidos")
        if type(row.get("source_page")) is not int or not 1 <= row["source_page"] <= 1000:
            raise ValidationError("Página inválida")
        key = row["code"], row["cycle"]
        if key in keys:
            raise ValidationError("Código/ciclo duplicado: se rechaza el lote completo")
        keys.add(key)
    return source, offers


@transaction.atomic
def import_catalogue(payload):
    source_data, rows = validate_catalogue(payload)
    source, _ = Source.objects.update_or_create(
        url=source_data["url"],
        defaults={k: source_data[k] for k in ("title", "retrieved", "sha256")},
    )
    for row in rows:
        campus, _ = Campus.objects.get_or_create(name=row["campus"])
        career, _ = Career.objects.get_or_create(name=row["name"])
        offer, _ = Offer.objects.update_or_create(
            code=row["code"],
            cycle=2027,
            defaults={
                "career": career,
                "campus": campus,
                "source": source,
                "source_page": row["source_page"],
                "active": True,
            },
        )
        for key, _ in DIMENSIONS:
            Datum.objects.get_or_create(
                offer=offer,
                dimension=key,
                defaults={
                    "value": None,
                    "unit": {"duracion": "semestres", "arancel": "CLP/año", "empleabilidad": "%"}[
                        key
                    ],
                    "period": "No publicado",
                    "source": source,
                },
            )
    Offer.objects.filter(cycle=2027).exclude(code__in=[r["code"] for r in rows]).update(
        active=False
    )
    return len(rows)
