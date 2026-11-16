"""Axe y métricas de laboratorio; no acredita WCAG integral ni Web Vitals de campo."""

import argparse
import json
import secrets
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument(
    "--axe", type=Path, default=ROOT / ".runtime/qa/node_modules/axe-core/axe.min.js"
)
args = parser.parse_args()
axe = args.axe.read_text()
results = []
with sync_playwright() as p:
    browser = p.chromium.launch()
    for width in (360, 1440):
        context = browser.new_context(
            viewport={"width": width, "height": 1000}, reduced_motion="reduce"
        )
        context.add_init_script(
            """window.lab={lcp:0,cls:0};new PerformanceObserver(l=>{for(const e of l.getEntries())window.lab.lcp=e.startTime}).observe({type:'largest-contentful-paint',buffered:true});new PerformanceObserver(l=>{for(const e of l.getEntries())if(!e.hadRecentInput)window.lab.cls+=e.value}).observe({type:'layout-shift',buffered:true});"""
        )
        page = context.new_page()
        page.goto("http://127.0.0.1:19039/acceso/")
        page.keyboard.press("Tab")
        keyboard_skip = page.evaluate("document.activeElement.textContent")
        assert keyboard_skip == "Saltar al contenido"
        page.locator("#id_alias").fill("axe_" + secrets.token_hex(6))
        page.locator("#id_password").fill(secrets.token_urlsafe(20))
        page.get_by_role("button", name="Crear mi proceso", exact=True).click()
        for route in (
            "/",
            "/intereses/",
            "/prioridades/",
            "/catalogo/",
            "/guardados/",
            "/comparar/",
        ):
            page.goto("http://127.0.0.1:19039" + route)
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(400)
            lab = page.evaluate("window.lab")
            page.evaluate(axe)
            result = page.evaluate(
                "async()=>await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']}})"
            )
            violations = [
                {
                    "id": v["id"],
                    "impact": v["impact"],
                    "help": v["help"],
                    "targets": [n["target"] for n in v["nodes"]],
                }
                for v in result["violations"]
            ]
            overflow = page.evaluate("document.documentElement.scrollWidth>innerWidth")
            results.append(
                {
                    "width": width,
                    "route": route,
                    "axe_version": result["testEngine"]["version"],
                    "violations": violations,
                    "incomplete_checks": len(result["incomplete"]),
                    "passes": len(result["passes"]),
                    "lcp_lab_ms": lab["lcp"],
                    "cls_lab": lab["cls"],
                    "page_overflow": overflow,
                    "keyboard_skip": keyboard_skip,
                }
            )
        page.goto("http://127.0.0.1:19039/")
        page.get_by_role("link", name="Eliminar mi proceso y cuenta").click()
        page.locator("#confirm").fill("ELIMINAR")
        page.get_by_role("button", name="Eliminar definitivamente").click()
        context.close()
    browser.close()
(ROOT / "evidencia/auditoria_web.json").write_text(
    json.dumps(
        {
            "results": results,
            "limits": "Axe automático no sustituye lector de pantalla/inspección de todos los criterios. LCP/CLS son laboratorio local n=1 por ruta/ancho; no INP ni p75 de campo.",
        },
        ensure_ascii=False,
        indent=2,
    )
    + "\n"
)
violations = sum(len(r["violations"]) for r in results)
print(
    f"{len(results)} pantallas: {violations} violaciones axe; {sum(r['page_overflow'] for r in results)} desbordes de página."
)
raise SystemExit(1 if violations else 0)
