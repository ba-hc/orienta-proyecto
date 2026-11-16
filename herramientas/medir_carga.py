"""RNF-R02/R04: 50 sesiones, 70/30 lectura/escritura, 10 min estables.

Crea un runtime aislado y 360 procesos sintéticos. Nunca mide cuentas humanas.
"""

import argparse
import concurrent.futures
import json
import os
import platform
import secrets
import statistics
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--segundos", type=int, default=600)
args = parser.parse_args()
runtime = ROOT / ".runtime" / ("carga-" + str(int(time.time())))
runtime.mkdir(parents=True, mode=0o700)
env = {**os.environ, "ORIENTA_RUNTIME_DIR": str(runtime)}
os.environ["ORIENTA_RUNTIME_DIR"] = str(runtime)
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orienta.settings")
python = str(ROOT / ".venv/bin/python")
for command in [
    [python, "herramientas/inicializar.py"],
    [python, "manage.py", "migrate", "--noinput"],
    [python, "herramientas/importar_catalogo.py", "data/catalogo_udec_2027.json", "--aplicar"],
]:
    subprocess.run(command, cwd=ROOT, env=env, check=True, stdout=subprocess.DEVNULL)
import django

django.setup()
import requests
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.sessions.backends.db import SessionStore
from orienta.models import Offer, Process

# Una contraseña aleatoria compartida solo para fixtures; jamás se imprime.
hashed = make_password(secrets.token_urlsafe(32))
users = User.objects.bulk_create(
    [User(username=f"carga_{i:03}", password=hashed) for i in range(360)]
)
Process.objects.bulk_create([Process(owner=u) for u in users])
cookies = []
for user in users[:50]:
    session = SessionStore()
    session["_auth_user_id"] = str(user.pk)
    session["_auth_user_backend"] = "django.contrib.auth.backends.ModelBackend"
    session["_auth_user_hash"] = user.get_session_auth_hash()
    session.create()
    cookies.append(session.session_key)
log = (runtime / "server.log").open("w")
server = subprocess.Popen(
    [
        str(ROOT / ".venv/bin/gunicorn"),
        "orienta.wsgi:application",
        "--bind",
        "127.0.0.1:19040",
        "--workers",
        "1",
        "--threads",
        "16",
        "--access-logfile",
        "/dev/null",
    ],
    cwd=ROOT,
    env=env,
    stdout=log,
    stderr=log,
)
base = "http://127.0.0.1:19040"
results = []
barrier = threading.Barrier(50)
raw_path = ROOT / "evidencia/carga_operaciones.jsonl"
try:
    for _ in range(100):
        try:
            if requests.get(base + "/health/", timeout=1).status_code == 200:
                break
        except requests.RequestException:
            time.sleep(0.1)
    else:
        raise RuntimeError("No inició el servidor de carga")

    def worker(index):
        session = requests.Session()
        session.cookies.set("sessionid", cookies[index], domain="127.0.0.1", path="/")
        warm = session.get(base + "/prioridades/", timeout=15)
        if warm.status_code != 200:
            raise RuntimeError("No autenticó la sesión sintética")
        token = session.cookies.get("csrftoken")
        barrier.wait(timeout=30)
        start = time.perf_counter()
        operations = []
        for iteration in range(args.segundos):
            target = start + iteration
            if target > time.perf_counter():
                time.sleep(target - time.perf_counter())
            write = (iteration + index) % 10 >= 7
            began = time.perf_counter()
            error = ""
            try:
                if write:
                    response = session.post(
                        base + "/prioridades/",
                        data={
                            "duracion": 3,
                            "arancel": 2,
                            "empleabilidad": "",
                            "csrfmiddlewaretoken": token,
                        },
                        headers={"Referer": base + "/prioridades/"},
                        timeout=15,
                        allow_redirects=False,
                    )
                    valid = response.status_code == 302 and response.headers.get("Location") == "/"
                else:
                    response = session.get(
                        base + "/catalogo/?campus=Chill%C3%A1n", timeout=15, allow_redirects=False
                    )
                    valid = response.status_code == 200 and "Catálogo UdeC" in response.text
                status = response.status_code
            except requests.RequestException as exc:
                status, valid, error = 0, False, type(exc).__name__
            operations.append(
                {
                    "vu": index,
                    "iteration": iteration,
                    "kind": "write" if write else "read",
                    "ms": (time.perf_counter() - began) * 1000,
                    "status": status,
                    "valid": valid,
                    "error": error,
                }
            )
        return operations, time.perf_counter() - start

    began = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        for operations, elapsed in executor.map(worker, range(50)):
            results.extend(operations)
    wall = time.perf_counter() - began
    raw_path.write_text("".join(json.dumps(r) + "\n" for r in results))
    durations = sorted(r["ms"] for r in results)
    failures = sum(not r["valid"] for r in results)

    def percentile(data, p):
        return data[min(len(data) - 1, int((len(data) - 1) * p))]

    report = {
        "method": "50 sesiones autenticadas persistentes; 1 operación/s/VU; cada bloque de 10 contiene 7 lecturas/3 guardados; sin redirecciones; calentamiento excluido",
        "runtime": str(runtime.relative_to(ROOT)),
        "platform": platform.platform(),
        "python": platform.python_version(),
        "server": "gunicorn 1 worker, 16 threads; SQLite IMMEDIATE; loopback; sin tráfico de otros entornos",
        "duration_requested_seconds": args.segundos,
        "wall_seconds": wall,
        "virtual_users": 50,
        "processes": Process.objects.count(),
        "offers": Offer.objects.filter(active=True).count(),
        "operations": len(results),
        "reads": sum(r["kind"] == "read" for r in results),
        "writes": sum(r["kind"] == "write" for r in results),
        "http_5xx": sum(r["status"] >= 500 for r in results),
        "functional_or_http_failures": failures,
        "failure_percent": failures / len(results) * 100,
        "p50_ms": statistics.median(durations),
        "p95_ms": percentile(durations, 0.95),
        "p99_ms": percentile(durations, 0.99),
        "RNF_R02_pass": percentile(durations, 0.95) <= 1000 and args.segundos >= 600,
        "RNF_R04_pass": failures / len(results) <= 0.01 and args.segundos >= 600,
        "limits": "Capacidad local con datos sintéticos; no demuestra latencia de red escolar, 99% mensual, experiencia real ni aceptación de usuarios.",
    }
    (ROOT / "evidencia/carga.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    )
    print(json.dumps(report, ensure_ascii=False), flush=True)
finally:
    server.terminate()
    try:
        server.wait(timeout=15)
    except subprocess.TimeoutExpired:
        server.kill()
        server.wait()
    log.close()
