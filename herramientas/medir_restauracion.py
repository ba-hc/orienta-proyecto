"""Ejercicio local de respaldo cifrado, alteración negativa y restauración."""

import hashlib
import json
import os
import secrets
import shutil
import sqlite3
import subprocess
import tempfile
import time
from pathlib import Path
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

ROOT = Path(__file__).resolve().parents[1]
runtime = ROOT / ".runtime"
started = time.perf_counter()
with tempfile.TemporaryDirectory(dir=runtime, prefix="restore-") as temp:
    work = Path(temp)
    snapshot = work / "snapshot.sqlite3"
    with (
        sqlite3.connect(runtime / "orienta.sqlite3") as source,
        sqlite3.connect(snapshot) as destination,
    ):
        source.backup(destination)
    snapshot_time = time.time()
    raw = snapshot.read_bytes()
    key, nonce = secrets.token_bytes(32), secrets.token_bytes(12)
    cipher = AESGCM(key).encrypt(nonce, raw, b"Orienta-local-backup-v1")
    key_path = work / "backup.key"
    key_path.write_bytes(key)
    os.chmod(key_path, 0o600)
    tampered = cipher[:-1] + bytes([cipher[-1] ^ 1])
    try:
        AESGCM(key).decrypt(nonce, tampered, b"Orienta-local-backup-v1")
    except InvalidTag:
        tamper_denied = True
    else:
        raise RuntimeError("El respaldo alterado no fue rechazado")
    recovered = AESGCM(key).decrypt(nonce, cipher, b"Orienta-local-backup-v1")
    restored_dir = work / "restored"
    restored_dir.mkdir(mode=0o700)
    restored = restored_dir / "orienta.sqlite3"
    restored.write_bytes(recovered)
    os.chmod(restored, 0o600)
    for name in ("django.key", "payload.key"):
        shutil.copy2(runtime / name, restored_dir / name)
    with sqlite3.connect(restored) as db:
        integrity = db.execute("PRAGMA integrity_check").fetchone()[0]
        foreign_errors = db.execute("PRAGMA foreign_key_check").fetchall()
        offers = db.execute("SELECT COUNT(*) FROM orienta_offer WHERE active=1").fetchone()[0]
    env = {**os.environ, "ORIENTA_RUNTIME_DIR": str(restored_dir)}
    result = subprocess.run(
        [str(ROOT / ".venv/bin/python"), "manage.py", "check"],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        check=True,
    )
    assert integrity == "ok" and not foreign_errors and offers == 91
    report = {
        "mode": "ejercicio local sobre copia consistente SQLite de datos sintéticos",
        "restoration_seconds": time.perf_counter() - started,
        "snapshot_age_seconds_at_restore": time.time() - snapshot_time,
        "source_bytes": len(raw),
        "restored_sha256_equals_snapshot": hashlib.sha256(raw).digest()
        == hashlib.sha256(recovered).digest(),
        "integrity_check": integrity,
        "foreign_key_errors": len(foreign_errors),
        "active_offers_recovered": offers,
        "tampered_ciphertext_rejected": tamper_denied,
        "django_check_exit": result.returncode,
        "rto_target_seconds": 14400,
        "rpo_target_seconds": 86400,
        "limits": "RTO de ejercicio medido. RPO observado solo para este snapshot; no demuestra periodicidad de backup de24h ni operación escolar. Respaldo/key/restaurado temporales se eliminan al terminar. No certifica cifrado integral de la base activa.",
    }
(ROOT / "evidencia/restauracion.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n"
)
print(json.dumps(report, ensure_ascii=False))
