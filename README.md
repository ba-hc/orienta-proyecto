# Orienta · Grupo 9 · Proyecto y Avance oral 2

Aplicación Django ejecutable y paquete de revisión crítica E3. Proyecto Informático, DIICC, Universidad de Concepción. Corte E3: 16 de noviembre de 2026; regularización documental H1: 23 de noviembre de 2026. Repositorio público en GitHub (verificado el 23/11/2026; sin licencia detectada), independiente del antecedente [orienta-grupo9](https://github.com/ba-hc/orienta-grupo9); [procedencia](PROCEDENCIA.md). La visibilidad pública no concede permiso de reutilización.

## Estado y alcance

- **Actual:** producto Django de E3 en el corte `e04eb2d` y documentación H1 que lo describe; demo local con datos sintéticos.
- **Antecedentes:** E1 (SRS y problema) y E2 (diseño, mockups y PoC) se conservan como historia; no son el producto actual ni una validación de uso.
- **No realizado:** no hay piloto con estudiantes, validación de usabilidad, aprobación docente, licencia de reutilización ni entrega E4. H1 no inicia H2 ni redacta E4.

El índice de la regularización, el mapa de evidencias E1/E2/E3, la matriz RF/RNF y las decisiones pendientes están en [docs/H1](docs/H1/README.md).

## Abrir la entrega

[Paquete descargable completo](https://github.com/ba-hc/orienta-proyecto/blob/main/entrega/Orienta_E3_Completo.zip).

El ZIP es un corte E3 (`e04eb2d`); no incluye `docs/H1` y no se regenera en H1.

- [Presentación de exposición](entrega/Orienta_E3_Exposicion.pdf) · [PowerPoint editable](entrega/Orienta_E3_Exposicion.pptx):12 láminas principales + referencias, con guion de 10 minutos.
- [Presentación con respaldo](entrega/Orienta_E3_Entrega.pdf) · [PowerPoint](entrega/Orienta_E3_Entrega.pptx).
- [SRS actualizado](docs/E3/SRS_IEEE830_E3.pdf) · [DOCX](docs/E3/SRS_IEEE830_E3.docx) · [Markdown](docs/E3/SRS_IEEE830_E3.md), con las 14 secciones de la plantilla.
- [Dossier E3](docs/E3/Dossier_E3.pdf), [guion de cinco voces](docs/E3/Guion_Oral_10_Minutos.pdf), [demo](docs/E3/Guion_Demo.pdf) y [preguntas de defensa](docs/E3/Preguntas_Defensa.pdf).
- [Cobertura R3](docs/E3/Cobertura_R3.md), [mediciones RNF](docs/E3/RNF_Mediciones.pdf), [trazabilidad](docs/E3/Trazabilidad_RF_RB.pdf) y [evidencia](evidencia/).

## Ejecutar en localhost

Requiere Python 3.13 o 3.14. Ejecutar desde este directorio. El entorno académico local admite cuentas y respuestas ficticias; no ingresar datos personales reales de estudiantes.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-lock.txt
.venv/bin/python herramientas/inicializar.py
.venv/bin/python manage.py migrate --noinput
.venv/bin/python herramientas/importar_catalogo.py data/catalogo_udec_2027.json
.venv/bin/python herramientas/importar_catalogo.py data/catalogo_udec_2027.json --aplicar
.venv/bin/python herramientas/enriquecer_catalogo.py
.venv/bin/gunicorn orienta.wsgi:application --bind 127.0.0.1:19039 --workers 1 --threads 8
```

Abrir http://127.0.0.1:19039/acceso/ y crear un alias de prueba. Las claves del servicio se generan fuera de Git y no se sobrescriben. La base y el runtime se ignoran en Git. Sin las claves originales las respuestas cifradas no se recuperan: conservarlas con respaldo privado, sin compartirlas ni versionarlas. Para una verificación descartable, exportar `ORIENTA_RUNTIME_DIR="$(mktemp -d /tmp/orienta.XXXXXX)"` antes de inicializar y usar solo datos sintéticos.

Recorrido: acceso → intereses → prioridades → catálogo → guardados → comparación → salir/retomar → supresión. Catálogo: 91 ofertas oficiales 2027; 3 duraciones de páginas UdeC con vigencia a confirmar. Arancel y empleabilidad sin período comprobable permanecen ausentes. La ficha de 12 ítems es original y no psicométrica.

## Verificación reproducible

```bash
.venv/bin/ruff check orienta tests herramientas manage.py
.venv/bin/ruff format --check orienta tests herramientas manage.py
.venv/bin/python manage.py check
.venv/bin/python manage.py makemigrations --check --dry-run
.venv/bin/coverage run --branch --source=orienta manage.py test tests --noinput
.venv/bin/coverage report
.venv/bin/python -m playwright install chromium firefox
.venv/bin/python herramientas/e2e_navegadores.py
.venv/bin/python herramientas/medir_carga.py --segundos 600
.venv/bin/python herramientas/medir_restauracion.py
.venv/bin/python herramientas/reanalizar_encuestas.py
```

La carga crea un runtime separado y usa el puerto 19040; no prueba cuentas humanas. El E2E usa 19039 y elimina sus cuentas al terminar. Axe requiere `npm install --prefix .runtime/qa axe-core@4.14.1`, luego `.venv/bin/python herramientas/auditar_web.py`. Los scripts permiten reproducir resultados técnicos; no rellenan evidencia humana.

La [CI remota](https://github.com/ba-hc/orienta-proyecto/actions) ejecuta formato, análisis, migraciones, suite y catálogo por push/PR. Local, CI, navegador, carga y despliegue son evidencias distintas. Los resultados incluyen denominador y límites.

En H1 se ejecutaron Ruff, `manage.py check`, migraciones, 24 tests con coverage e importación del catálogo. No se ejecutó una CI nueva de H1: la CI pública del SHA base `e04eb2d` está verificada como `success` (run [45168123412](https://github.com/ba-hc/orienta-proyecto/actions/runs/45168123412)), pero no cubre la rama/diff H1. Tampoco se repitieron el E2E, la carga ni la restauración; esas siguen siendo evidencias históricas de E3. El resumen y los límites están en [docs/H1](docs/H1/README.md).

## Documentos y alcance real

La respuesta docente, tres iteraciones, ciencias, costos/riesgos, plan, bitácora, uso de IA y fuentes están en [docs/E3](docs/E3/). Los originales están en [docs/fuentes](docs/fuentes/). E2 y su matriz se conservan como antecedentes, sin atribuir una nueva aprobación grupal. La documentación H1 ordena procedencia, requisitos, exposición y pendientes en [docs/H1](docs/H1/README.md); no reescribe los documentos E3 que aún declaran el repositorio como privado.

La cobertura documental de los siete criterios no garantiza el 100 % de nota: la validación de uso con personas externas, contribución distribuida auténtica, instalación por otro integrante, ensayo y exposición requieren evidencia humana real. No se generaron respuestas, firmas, HH o commits ficticios. El reanálisis de 192 registros de E1 es evidencia de necesidades, no de usabilidad de E3.

Antes de un piloto real faltan TLS, cifrado integral, protocolo efectivo, responsables y controles operativos. La demo local y el cifrado de respuestas no equivalen a un despliegue autorizado con datos de menores.
