"""Recorrido real Chromium/Firefox, escritorio/móvil, persistencia y supresión."""

import json
import secrets
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
BASE = "http://127.0.0.1:19039"
out = ROOT / "evidencia/navegador"
out.mkdir(exist_ok=True)
results = []
with sync_playwright() as p:
    for engine in ("chromium", "firefox"):
        browser = getattr(p, engine).launch(headless=True)
        for width in (1440, 360):
            context = browser.new_context(viewport={"width": width, "height": 1000})
            page = context.new_page()
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            alias = "e2e_" + secrets.token_hex(6)
            password = secrets.token_urlsafe(20)
            began = time.perf_counter()
            page.goto(BASE + "/acceso/")
            page.screenshot(path=str(out / f"{engine}-{width}-acceso.png"), full_page=True)
            page.get_by_label("Alias", exact=False).fill(alias)
            page.get_by_label("Contraseña", exact=False).fill(password)
            page.get_by_role("button", name="Crear mi proceso", exact=True).click()
            page.wait_for_url(BASE + "/")
            page.goto(BASE + "/intereses/")
            for i in range(1, 13):
                page.locator(f"#id_q{i}").select_option("4" if i % 2 else "2")
            page.get_by_role("button", name="Guardar respuestas y ver resumen").click()
            page.get_by_role("heading", name="Lo que expresaste").wait_for()
            page.screenshot(path=str(out / f"{engine}-{width}-intereses.png"), full_page=True)
            page.goto(BASE + "/prioridades/")
            page.get_by_label("Duración", exact=False).select_option("3")
            page.get_by_label("Arancel anual", exact=False).select_option("2")
            page.get_by_role("button", name="Guardar prioridades").click()
            page.goto(BASE + "/catalogo/")
            assert page.locator("article.offer").count() == 91
            page.get_by_label("Carrera o código").fill("13073")
            page.get_by_role("button", name="Filtrar", exact=True).click()
            page.locator("article.offer form button").click()
            page.goto(BASE + "/catalogo/?q=13086")
            page.locator("article.offer form button").click()
            assert page.locator("article.offer").count() == 2
            page.goto(BASE + "/comparar/")
            options = page.locator("#id_offer_a option").evaluate_all(
                "els => els.map(x => ({value:x.value,text:x.textContent}))"
            )
            a = next(x["value"] for x in options if "(13073)" in x["text"])
            b = next(x["value"] for x in options if "(13086)" in x["text"])
            page.locator("#id_offer_a").select_option(a)
            page.locator("#id_offer_b").select_option(b)
            page.get_by_role("button", name="Guardar y comparar").click()
            page.get_by_role("heading", name="Tu comparación guardada").wait_for()
            assert "Prioridad alta" in page.locator("main").inner_text()
            assert "Información no disponible" in page.locator("main").inner_text()
            page.screenshot(path=str(out / f"{engine}-{width}-comparacion.png"), full_page=True)
            overflow = page.evaluate("document.documentElement.scrollWidth > innerWidth")
            assert not overflow, "Desborde de página fuera de la tabla desplazable"
            page.get_by_role("button", name="Salir", exact=True).click()
            page.get_by_label("Alias", exact=False).fill(alias)
            page.get_by_label("Contraseña", exact=False).fill(password)
            page.get_by_role("button", name="Retomar proceso", exact=True).click()
            page.goto(BASE + "/comparar/")
            assert page.locator("#id_offer_b").input_value() == b
            page.goto(BASE + "/")
            page.get_by_role("link", name="Eliminar mi proceso y cuenta").click()
            page.get_by_label("Escribe ELIMINAR para confirmar").fill("ELIMINAR")
            page.get_by_role("button", name="Eliminar definitivamente").click()
            page.wait_for_url(BASE + "/acceso/")
            assert not errors, errors
            results.append(
                {
                    "engine": engine,
                    "version": browser.version,
                    "width": width,
                    "status": "pass",
                    "seconds": round(time.perf_counter() - began, 2),
                    "page_errors": errors,
                    "horizontal_page_overflow": overflow,
                    "steps": "alta,12 respuestas,prioridades,91 ofertas,filtro,2 guardados,comparación,logout/login,recuperación,supresión",
                }
            )
            print(engine, width, "PASS", flush=True)
            context.close()
        browser.close()
(ROOT / "evidencia/e2e.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
