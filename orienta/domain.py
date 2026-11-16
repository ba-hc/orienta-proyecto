"""Reglas del dominio: sin ranking ni inferencias psicométricas."""

import os
from decimal import Decimal
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from django.conf import settings

DIMENSIONS = [
    ("duracion", "Duración"),
    ("arancel", "Arancel anual"),
    ("empleabilidad", "Empleabilidad histórica"),
]
INTERESTS = [
    (
        "Investigar",
        "Me interesa observar fenómenos y buscar explicaciones.",
        "Me interesa analizar datos para responder preguntas.",
    ),
    (
        "Construir",
        "Me interesa diseñar y probar soluciones prácticas.",
        "Me interesa comprender cómo funcionan herramientas y sistemas.",
    ),
    (
        "Crear",
        "Me interesa expresar ideas mediante textos, imágenes o música.",
        "Me interesa proponer formas nuevas de comunicar una idea.",
    ),
    (
        "Acompañar",
        "Me interesa escuchar y apoyar el aprendizaje de otras personas.",
        "Me interesa colaborar para mejorar el bienestar de mi comunidad.",
    ),
    (
        "Organizar",
        "Me interesa planificar actividades y coordinar recursos.",
        "Me interesa revisar detalles y mantener información ordenada.",
    ),
    (
        "Participar",
        "Me interesa conversar y construir acuerdos con otras personas.",
        "Me interesa impulsar proyectos colectivos.",
    ),
]
ITEMS = [
    (i * 2 + j + 1, label, text)
    for i, (label, *texts) in enumerate(INTERESTS)
    for j, text in enumerate(texts)
]


def encrypt_response(process_id, item, value):
    nonce = os.urandom(12)
    aad = f"{process_id}:{item}:ORIENTA-EXPLORA-1".encode()
    return nonce + AESGCM(settings.PAYLOAD_KEY).encrypt(nonce, str(value).encode(), aad)


def decrypt_response(response):
    blob = bytes(response.encrypted_value)
    aad = f"{response.process_id}:{response.item}:ORIENTA-EXPLORA-1".encode()
    value = int(AESGCM(settings.PAYLOAD_KEY).decrypt(blob[:12], blob[12:], aad))
    if not 1 <= value <= 5:
        raise ValueError("Respuesta fuera de escala")
    return value


def summarize(values):
    if set(values) != set(range(1, 13)) or any(
        type(v) is not int or not 1 <= v <= 5 for v in values.values()
    ):
        raise ValueError("Completa los doce ítems con valores de 1 a 5.")
    return [
        {"label": label, "mean": (values[i * 2 + 1] + values[i * 2 + 2]) / 2}
        for i, (label, *_rest) in enumerate(INTERESTS)
    ]


def compare(offer_a, offer_b, priorities):
    if offer_a.pk == offer_b.pk:
        raise ValueError("Elige exactamente dos ofertas distintas.")
    maps = [{d.dimension: d for d in offer.data.all()} for offer in (offer_a, offer_b)]
    rows = []
    for key, label in DIMENSIONS:
        a, b = [m.get(key) for m in maps]
        missing = a is None or b is None or a.value is None or b.value is None
        compatible = (
            not missing
            and offer_a.cycle == offer_b.cycle
            and (a.unit, a.period) == (b.unit, b.period)
        )
        if missing:
            reason = "Falta información publicada. No se reemplaza por cero ni se infiere una diferencia."
        elif not compatible:
            reason = "Unidad, período o ciclo diferentes: estos datos no son homologables."
        else:
            delta = abs(Decimal(a.value) - Decimal(b.value))
            reason = (
                f"Diferencia factual: {delta:g} {a.unit}. Es un dato para conversar, sin veredicto."
            )
        rows.append(
            {"label": label, "priority": priorities.get(key), "a": a, "b": b, "reason": reason}
        )
    return rows
