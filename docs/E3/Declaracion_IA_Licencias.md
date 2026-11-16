# Declaración de uso de IA y procedencia

## Uso de asistencia generativa

Este paquete fue preparado con Codex como agente principal, que diseñó, implementó, integró y verificó el sistema y sus entregables. Se usaron subagentes Paseo con perfiles configurados: Go · DeepSeek · Max para inventario y corrección de texto; Codex · Sol · Max para el exportador Markdown→DOCX/PDF. Sus resultados se revisaron antes de integrarlos. La aceptación y evidencia constan en evidencia/delegacion.json. El tiempo del agente y de revisión no se presenta como horas humanas del equipo ni como ahorro neto de cuota.

Las partes asistidas incluyen código, pruebas, scripts de medición, revisión de fuentes, síntesis, diagramas, SRS, presentación y guiones. La responsabilidad académica de revisar, comprender, adaptar y defender el material sigue en el equipo. Los nombres de los integrantes provienen de E1 y no atribuyen automáticamente autoría de cada archivo ni participación en esta ejecución.

No se generaron encuestas, entrevistas, respuestas de usuarios, firmas, aprobaciones ni reuniones ficticias. Las cuentas y respuestas usadas en las pruebas del software son datos sintéticos identificados como tales. Las encuestas analizadas provienen del apéndice desidentificado de E1 y mantienen su limitación de procedencia.

## Material recibido y reutilizado

Repositorio antecedente: ba-hc/orienta-grupo9, main a92f1fd3cfea061543cf14557320120793b32eb1. El pull confirmó que estaba actualizado. Los cambios locales previos se preservaron y respaldaron fuera del proyecto nuevo. SRS E1, documentos del curso y comentarios docentes se conservan con fecha y fuente. La plantilla IEEE830 y la rúbrica fueron aportadas por el usuario. No se impone una licencia abierta a los documentos académicos originales.

Marca UdeC: SVG/PNG y tipografías provenientes del paquete de identidad E2, cuyo registro remite a Normas Gráficas UdeC. Uso de identificación académica; no implica patrocinio ni aprobación institucional. Se conserva la marca sin modificar y con su proporción. Tipografías Poppins y Roboto: licencias OFL originales incluidas en docs/identidad/fuentes. No se descargaron nuevas imágenes comerciales.

Catálogo2027: PDF oficial DEMRE/Mineduc, conservado con SHA256. Las91 filas son una extracción de código, nombre, campus y ciclo; fecha/página permiten cotejo. Las3 duraciones usan extractos curados verificados de páginas oficiales UdeC; el hash del extracto no se presenta como hash del HTML. Información pública no equivale a licencia comercial de redistribución irrestricta; el repositorio es privado y cita la fuente.

Ficha de exploración:12 enunciados originales de este paquete, licencia propuesta CC BY4.0 para el texto; no constituye prueba de validación psicométrica. Las preguntas del estudio académico se distinguen de un instrumento profesional adquirido. No se copió VocationOne ni se afirmó autorización de su API.

## Dependencias y licencias principales

| Dependencia | Uso | Licencia declarada por el proyecto |
| --- | --- | --- |
| Django | Servidor, auth, ORM, formularios, migraciones | BSD3-Clause |
| cryptography | AESGCM | Apache2.0 o BSD3-Clause |
| Gunicorn | Servidor WSGI local | MIT |
| coverage.py | Medición de líneas/ramas | Apache2.0 |
| Ruff | Análisis y formato | MIT |
| Playwright | Automatización de navegador | Apache2.0 |
| axe-core | Accesibilidad automática, herramienta externa | MPL2.0 |
| python-docx / python-pptx | Exportación editable | MIT |
| ReportLab | Figura descriptiva de encuestas | BSD |
| Graphviz | Diagramas DOT/SVG/PNG | EPL1.0 |
| Poppins / Roboto | Tipografía | SIL OFL1.1, textos conservados |

El lockfile identifica versiones. Licencias de dependencias transitivas se consultan en su metadata instalada; la tabla no constituye una auditoría legal exhaustiva. No se publican claves, credenciales ni bases de ejecución. Los recursos y hashes se inventarían en entrega/manifest.json al empaquetar.
