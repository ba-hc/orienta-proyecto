# Procedencia

## Estado del repositorio

`ba-hc/orienta-proyecto` figura como **público** en GitHub y **sin licencia declarada**. Comprobación por API: 23/11/2026 19:52 UTC; `private: false`, `visibility: public`, `license: null`. La visibilidad pública no concede permiso de reutilización y solo el propietario puede cambiarla. Ver [exposición y licencias](docs/H1/Exposicion_y_Licencias.md).

## Antecedente E1/E2

Antecedente histórico: `https://github.com/ba-hc/orienta-grupo9`, rama `main`, SHA `a92f1fd3cfea061543cf14557320120793b32eb1`. El registro de E3 indica que el pull del 16/11/2026 confirmó el checkout actualizado, sin cambios remotos. Los archivos previos permanecen en ese checkout histórico; no se clonaron, movieron ni editaron en este repositorio.

La consulta no autenticada a la API de GitHub devuelve `404` para ese repositorio; con acceso autenticado de solo lectura al árbol del SHA se comprobó la presencia y los blob IDs de tres archivos: SRS E1 (`13a36d07c9069aac4872cf41daaa0b289fd723a1`), dossier E2 (`fc96a0e7e0911377bfb2d2af1702509f93fe559c`) y matriz (`ec059bad1399631669fadfb20084f9c18060b154`), coincidentes con las copias locales. No se descargaron contenidos ni se clonó el antecedente; no se enlaza el árbol privado como dependencia de evaluación.

## Material local

- SRS E1 original: [docs/fuentes/SRS_E1_original.pdf](docs/fuentes/SRS_E1_original.pdf), 49 páginas, v1.8 del 08/10/2026; SHA-256 `b5ec2294…cab766f`. Conserva 17 RF, 21 RNF, 7 restricciones y 10 reglas de negocio.
- Inventario E1: [docs/fuentes/Inventario_SRS_E1.md](docs/fuentes/Inventario_SRS_E1.md). Es un análisis del antecedente, no una prueba de ejecución.
- Dossier E2: [docs/antecedentes/Dossier_E2_Completo.md](docs/antecedentes/Dossier_E2_Completo.md), copia local de 456 líneas; SHA-256 `7f61c8d5…eff62e19`.
- Matriz E2: [docs/antecedentes/Matriz_Decision_E2.csv](docs/antecedentes/Matriz_Decision_E2.csv); SHA-256 `4dfbc6c0…61d2e35`. Sus totales son 3,95 / 3,60 / 2,20.
- Identidad y fuentes: [docs/identidad](docs/identidad/README.md); incluye marca UdeC, tipografías y textos OFL. No se impone una licencia abierta a la marca.
- Enunciado, rúbricas y plantilla del curso: [docs/fuentes](docs/fuentes/). Son documentos aportados para el curso; su licencia de redistribución no está verificada.

El SRS E1 y el enunciado se conservan sin modificación. La rúbrica y la plantilla fueron aportadas para el curso. Se reutiliza la idea y el diseño del antecedente, con construcción trazable en este repositorio. No se atribuyen commits a personas que no los realizaron.

## Producto E3 y paquete

El producto actual es el corte `e04eb2d252ba7a9e047cdc40723191b4cd0ea9f4`. El [manifiesto](entrega/manifest.json) lista 189 archivos; en ese corte los 189 coinciden en bytes y SHA-256. El [ZIP](entrega/Orienta_E3_Completo.zip) tiene 190 entradas —los 189 archivos más el manifiesto—, con las mismas huellas y sin el directorio `.git/`, `.venv`, `.runtime`, `node_modules`; no se listan bases, claves ni `.env` (comprobación por nombres). El manifiesto no incluye el ZIP ni se incluye a sí mismo.

El campo `application_commit` del manifiesto es `a845244…`, no `e04eb2d…`. El manifiesto certifica integridad de contenido en el corte, no autoría, aprobación ni el commit de aplicación. La regularización H1 modifica `README.md`, `PRODUCT.md` y `PROCEDENCIA.md` y agrega `docs/H1/`; por eso el manifiesto y el ZIP **no validan el checkout H1** y no se regeneran en este hito.

## Reproducibilidad

Desde la raíz, con un runtime descartable fuera de Git:

```bash
RT="$(mktemp -d /tmp/orienta.XXXXXX)"
export ORIENTA_RUNTIME_DIR="$RT"
.venv/bin/python herramientas/inicializar.py
.venv/bin/python manage.py migrate --noinput
.venv/bin/ruff check orienta tests herramientas manage.py
.venv/bin/ruff format --check orienta tests herramientas manage.py
.venv/bin/python manage.py check
.venv/bin/python manage.py makemigrations --check --dry-run
.venv/bin/coverage run --branch --source=orienta manage.py test tests --noinput
.venv/bin/coverage report
```

Resultado H1: 24 tests, 414/421 líneas (98,34 %) y 89/92 ramas (96,74 %); catálogo de 91 ofertas, 3 campus y 3 duraciones. El detalle y los límites están en [docs/H1/README.md](docs/H1/README.md).

## Uso, IA y límites

El paquete E3 conserva su declaración histórica de uso de IA; H1 no la reescribe ni atribuye autoría humana que no corresponda. Los cambios de H1 quedan en el historial de Git. No se generaron participantes, consentimientos, firmas, horas, aprobaciones ni commits ficticios.

No se declara licencia, patrocinio UdeC, permiso sobre el PDF DEMRE, los documentos del curso o el material E2, ni autorización para datos reales. Esas decisiones son humanas y están listadas en [docs/H1/Exposicion_y_Licencias.md](docs/H1/Exposicion_y_Licencias.md).
