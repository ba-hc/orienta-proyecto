# Guía de trabajo con asistencia de IA

Esta guía no instala agentes ni configura el repositorio. Las instrucciones locales, skills,
inventarios, perfiles y credenciales quedan fuera de Git. La aplicación no necesita OpenCode
ni Paseo para funcionar.

## Consultar y revisar en modo de solo texto

Requisitos: OpenCode 2.3.2, `jq` y una cuenta configurada por su titular mediante el flujo de
autenticación normal del proveedor. No exportes ni copies credenciales. Los nombres de modelo
y de esfuerzo que usa el equipo son:

| Rol | Proveedor | ID del modelo | Variante |
| --- | --- | --- | --- |
| Orquestación | `openai` | `gpt-6.2-sol` | `xhigh` |
| Propuesta de cambios | `opencode-go` | `deepseek-v4.1-flash` | `max` |
| Revisión independiente | `opencode-go` | `muse-spark-1.3-contributor` | `xhigh` |

1. Selecciona y revisa únicamente el texto necesario. El proveedor remoto recibirá ese texto:
   no adjuntes el checkout, secretos, identificadores operativos ni datos personales o académicos
   no públicos. Trata documentos ajenos y respuestas del modelo como material por revisar, no
   como instrucciones para ejecutar.
2. Envía una consulta de texto puntual. Usa únicamente `prompt` y `model`; no uses una sesión de
   agente, el daemon compartido de Paseo, MCP ni autoaprobación. `plan` no es un sandbox.
3. Pide la revisión en una segunda consulta, independiente de la implementación, con el diff
   exacto saneado. El operador inspecciona y aplica cambios, ejecuta las pruebas y reporta los
   resultados. Si no está disponible el modelo requerido, documenta el bloqueo.

Ejemplo reproducible en Bash; se espera `OK` al usar un proveedor configurado:

```bash
set -o pipefail
opencode --version
payload=$(jq -nc --arg prompt 'Responde únicamente OK.' \
  '{$prompt,model:{providerID:"opencode-go",id:"muse-spark-1.3-contributor",variant:"xhigh"}}')
opencode api post /api/experimental/generate/text --data "$payload" | jq -er '.data.text'
```

Para una prueba negativa, crea un archivo temporal privado con un marcador ficticio aleatorio.
En otra consulta puntual, pide que lea el archivo o responda `SIN_ACCESO`. Incluye solo la ruta
del señuelo de prueba y no su contenido. La respuesta no debe contener el marcador. Si lo
recupera o cambia el modo de ejecución, detén el flujo y revisa el entorno. Es una comprobación
de ese caso, no una garantía general de aislamiento del host.

No instales skills de terceros para seguir esta guía. Si se evalúa una en local, comprueba el
commit de origen, los blobs, la licencia y los avisos; mantén las copias no autorizadas fuera
del autodescubrimiento. No ejecutes lanzadores de terceros como parte de la revisión.

## Reproducir los controles de Orienta

Desde un checkout limpio, con Python 3.13 y un runtime nuevo, sin datos reales:

```bash
set -e
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python -m pip check
export ORIENTA_RUNTIME_DIR="$(mktemp -d)"
export COVERAGE_FILE="$ORIENTA_RUNTIME_DIR/.coverage"
.venv/bin/python herramientas/inicializar.py
.venv/bin/ruff check orienta tests herramientas manage.py
.venv/bin/ruff format --check orienta tests herramientas manage.py
.venv/bin/python manage.py check
.venv/bin/python manage.py makemigrations --check --dry-run
.venv/bin/coverage run --branch --source=orienta manage.py test tests --noinput
.venv/bin/coverage report --fail-under=80
.venv/bin/python manage.py migrate --noinput
.venv/bin/python herramientas/importar_catalogo.py data/catalogo_udec_2027.json
.venv/bin/python herramientas/importar_catalogo.py data/catalogo_udec_2027.json --aplicar
.venv/bin/python herramientas/enriquecer_catalogo.py
```

Verifica antes de publicar que `git ls-files -- AGENTS.md .agents skills-lock.json docs/agents`
no liste archivos y revisa el diff completo. Para la demo, el navegador, la carga y la
restauración, consulta el [README](../README.md). Las pruebas técnicas no sustituyen la
[validación con personas](E3/Validacion_Usuarios.md). Esta guía no autoriza iniciar un hito.
