"""Crea un runtime local privado, sin sobreescribir claves existentes."""

import os
import secrets
from pathlib import Path

root = Path(__file__).resolve().parents[1]
runtime = Path(os.environ.get("ORIENTA_RUNTIME_DIR", root / ".runtime"))
runtime.mkdir(parents=True, exist_ok=True, mode=0o700)
os.chmod(runtime, 0o700)
for name, data in [
    ("django.key", secrets.token_urlsafe(64).encode()),
    ("payload.key", secrets.token_bytes(32)),
]:
    path = runtime / name
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        continue
    with os.fdopen(fd, "wb") as handle:
        handle.write(data)
print("Runtime inicializado. Claves existentes preservadas; ningún secreto se imprime.")
