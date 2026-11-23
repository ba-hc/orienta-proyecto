# Orienta · Hito 1: regularización documental y procedencia

Corte de referencia: `e04eb2d252ba7a9e047cdc40723191b4cd0ea9f4` (E3). Fecha de trabajo: 23/11/2026. Este hito solo modifica documentación Markdown actual de la raíz y agrega este directorio; no cambia código, pruebas, datos, configuración, CI ni el paquete E3.

## 1. Qué es actual y qué es antecedente

| Entrega | Qué contiene | Uso válido | Límite que no se debe borrar |
| --- | --- | --- | --- |
| E1 | SRS v1.8 del 08/10/2026, problema, 17 RF, 21 RNF, restricciones, riesgos, presupuesto y encuesta de conveniencia | Línea base de requisitos y evidencia histórica del problema | No es el producto actual; la encuesta no es validación de uso de E3 |
| E2 | Dossier de diseño, tres alternativas, matriz ponderada, C4/modelos, mockups y PoC | Antecedente de diseño y decisiones; matriz de referencia | No es un MVP ni acredita uso real; la copia local tiene enlaces y activos faltantes |
| E3 | Producto Django, SRS v2.0, pruebas, mediciones, riesgos, protocolo de validación y paquete | Producto actual en el corte `e04eb2d`; evidencia técnica local | La validación con personas sigue pendiente; el paquete no es aprobación docente |
| H1 | Este índice, inventario, matriz de requisitos, auditoría de exposición y diagnóstico | Regularización documental y mapa para E4 | No inicia H2, no redacta E4 y no crea evidencia humana |

El repositorio figura como **público** en GitHub y **sin licencia declarada** (comprobado por API el 23/11/2026; detalle en [Exposición y licencias](Exposicion_y_Licencias.md)). Público no significa permiso de reutilización, y la visibilidad solo la decide el propietario.

## 2. Índice

- [Inventario de antecedentes y mapa E4](Inventario_Antecedentes.md): actividades E1/E2/E3, fuente → archivo local → capítulo/artefacto, enlaces rotos de E2 y obsolescencias.
- [Matriz vigente de requisitos](Matriz_Requisitos.md): RF, RNF, RB y CI con estado, prueba/evidencia y brecha.
- [Exposición, licencias y decisiones](Exposicion_y_Licencias.md): categorías de material, metadatos, terceros y decisiones humanas.
- [Diagnóstico de entrada a H2](Diagnostico_H2.md): brechas de H1 y posteriores, priorizadas, sin ejecutar H2.
- Documentos canónicos: [README](../../README.md), [PRODUCT](../../PRODUCT.md), [PROCEDENCIA](../../PROCEDENCIA.md), [DESIGN](../../DESIGN.md).
- Producto y evidencia E3: [SRS](../E3/SRS_IEEE830_E3.md), [trazabilidad](../E3/Trazabilidad_RF_RB.md), [RNF](../E3/RNF_Mediciones.md), [validación](../E3/Validacion_Usuarios.md), [ciencias](../E3/Ciencias_Ingenieria.md), [costos y riesgos](../E3/Costos_Riesgos_Plan.md), [dossier](../E3/Dossier_E3.md).

## 3. Ejecución local reproducible

Requisitos: Python 3.13 o 3.14 y las dependencias del lockfile. La instalación y el arranque base están en [README](../../README.md#ejecutar-en-localhost); no se duplican aquí. Para verificar sin tocar el runtime del checkout, usar un directorio único fuera de Git:

```bash
RT="$(mktemp -d /tmp/orienta-h1.XXXXXX)"
export ORIENTA_RUNTIME_DIR="$RT"
.venv/bin/python herramientas/inicializar.py
.venv/bin/python manage.py migrate --noinput
.venv/bin/python herramientas/importar_catalogo.py data/catalogo_udec_2027.json
.venv/bin/python herramientas/importar_catalogo.py data/catalogo_udec_2027.json --aplicar
.venv/bin/python herramientas/enriquecer_catalogo.py
.venv/bin/gunicorn orienta.wsgi:application --bind 127.0.0.1:19039 --workers 1 --threads 8
```

Abrir `http://127.0.0.1:19039/acceso/`. Los datos de la demo son sintéticos. La base, las claves y el runtime quedan fuera de Git; sin la clave original no se recuperan las respuestas cifradas. El catálogo contiene 91 ofertas, 3 campus y 3 duraciones con extracto curado; arancel y empleabilidad sin período comprobable permanecen ausentes.

Verificación local ejecutada en H1:

| Comando | Resultado | Salida |
| --- | --- | --- |
| `.venv/bin/ruff check orienta tests herramientas manage.py` | pasa | `All checks passed!`; exit 0 |
| `.venv/bin/ruff format --check orienta tests herramientas manage.py` | pasa | `28 files already formatted`; exit 0 |
| `.venv/bin/python manage.py check` | pasa | `System check identified no issues (0 silenced).`; exit 0 |
| `.venv/bin/python manage.py makemigrations --check --dry-run` | pasa | `No changes detected`; exit 0 |
| `.venv/bin/coverage run --branch --source=orienta manage.py test tests --noinput` | pasa | 24 tests; exit 0 |
| `.venv/bin/coverage report` | informa | 414/421 líneas (98,34 %), 89/92 ramas (96,74 %); reporte combinado 98 %; exit 0 |
| Instalación limpia en venv temporal fuera del checkout | pasa | 26 dependencias del lockfile; `manage.py check`, migraciones, Ruff y 24 tests; exit 0 |
| Importación en runtime descartable | pasa | secado: 91 ofertas; aplicación: 91; enriquecimiento: 3 duraciones; 91 ofertas, 3 campus, 273 datos; reaplicación: 91 ofertas, sin duplicados |
| `git diff --check` | pasa | sin errores; exit 0 |
| `git diff --name-only` / `git status --porcelain` | acotado | solo `README.md`, `PRODUCT.md`, `PROCEDENCIA.md` y `docs/H1/`; código, pruebas y E3 sin cambios |
| Verificador de enlaces Markdown | sin enlaces nuevos rotos | 31 rotos preexistentes en 3 documentos E2; se resuelven rutas relativas, anclas `.md` y `#page=N` de PDF |

Los resultados crudos se conservan fuera del repositorio, en un archivo privado del responsable; no se versionan. **No se ejecutó una CI nueva de H1**: la CI pública del SHA base `e04eb2d` existe y pasó (run [45168123412](https://github.com/ba-hc/orienta-proyecto/actions/runs/45168123412), job `verificar`), pero no cubre la rama/diff de H1. Tampoco se repitieron el E2E de Playwright, axe, la carga de 600 s ni la restauración: siguen siendo evidencias históricas de E3 y no se presentan como ejecuciones de H1.

## 4. Paquete E3, manifest y ZIP

Comprobaciones realizadas en el corte `e04eb2d`:

- Los **189 blobs** listados en [manifest.json](../../entrega/manifest.json) coinciden en bytes y SHA-256 con los archivos de ese corte; entre ellos están `README.md`, `PRODUCT.md` y `PROCEDENCIA.md`. No falta ningún path del manifiesto ni hay paths del árbol fuera de él, salvo el propio manifiesto y el ZIP.
- El ZIP histórico [Orienta_E3_Completo.zip](../../entrega/Orienta_E3_Completo.zip) tiene 190 entradas: 189 archivos del manifiesto más el manifiesto. Las 189 huellas coinciden; `testzip` no reporta errores; no contiene el directorio `.git/`, `.venv`, `.runtime`, `node_modules`; no se listan bases, claves ni `.env` (comprobación por nombres).
- El ZIP no está listado dentro del manifiesto y el manifiesto no se lista a sí mismo; por eso la comprobación del ZIP se hizo comparando su contenido contra las 189 huellas.

**Por qué el manifiesto no valida el checkout H1:** el manifiesto certifica integridad de contenido respecto de un corte E3, no autoría ni aprobación. H1 modifica `README.md`, `PRODUCT.md` y `PROCEDENCIA.md` y agrega `docs/H1/`; esos cambios no están en el manifiesto y romperían sus hashes. Además, el campo `application_commit` del manifiesto es `a845244…`, no `e04eb2d…`, y el manifiesto no tiene firma. No se regenera en H1: el ZIP debe seguir siendo el corte E3 verificable, no una mezcla con documentación posterior.

## 5. Límites de H1

H1 deja el repositorio mejor documentado, pero no cierra estas condiciones:

- La copia local de E2 no contiene todos los activos que su dossier referencia; el árbol antecedente los conserva, pero no se descargaron ni se incorporaron, y no se declara autosuficiencia de E2.
- La consulta no autenticada al antecedente devuelve `404`; con acceso autenticado de solo lectura se cotejaron los blob IDs de SRS E1, dossier E2 y matriz. No se descargaron contenidos ni se enlaza el árbol como dependencia de evaluación.
- No hay licencia de repositorio ni permisos verificados para material de terceros.
- Hay decisiones humanas pendientes sobre visibilidad, RF-02 ([SRS E1 p. 11](../fuentes/SRS_E1_original.pdf#page=11)), metadatos y una exposición concreta de terceros.
- La validación con personas, la instalación por un segundo integrante, TLS/cifrado integral y la aprobación docente siguen fuera del alcance de H1.

Estado de H1: **PARTIAL**. No se declara E4, H2 ni uso real.
