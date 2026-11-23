# Exposición, licencias y decisiones humanas

Auditoría documental mínima, no un dictamen legal. No se copian nombres, tokens, credenciales ni microdatos; cuando hay una exposición concreta se informa por ruta y categoría para que el responsable decida. H1 no cambió visibilidad, licencias ni permisos.

## 1. Estado del repositorio

| Dato | Resultado | Fecha / método |
| --- | --- | --- |
| Visibilidad | `public` | API de GitHub, 23/11/2026 19:52 UTC; `private: false` |
| Licencia detectada | Ninguna (`license: null`) | API de GitHub y ausencia de `LICENSE`/`COPYING` versionado |
| Rama por defecto | `main` | API de GitHub |
| Repositorio antecedente | `404` sin autenticación; árbol del SHA cotejado con acceso autenticado de solo lectura | API de GitHub, 23/11/2026 |

**Público no es permiso.** Que el repositorio sea visible no autoriza reutilizar el SRS, los documentos del curso, la marca UdeC, el PDF DEMRE, las fuentes tipográficas ni el material de E2. La licencia y la visibilidad las decide el propietario, no la implementación automatizada.

## 2. Inventario de exposición por categoría

| Categoría | Archivos / ruta | Hallazgo | Riesgo | Decisión |
| --- | --- | --- | --- | --- |
| Registros y apéndice E1 | [SRS_E1_original.pdf](../fuentes/SRS_E1_original.pdf); [Encuestas_Reanalisis](../E3/Encuestas_Reanalisis.md); [JSON](../../evidencia/encuestas_reanalisis.json) | 49 páginas; apéndice desidentificado y agregados de 156 estudiantes + 36 apoderados; no hay filas crudas nuevas en el repo | Material histórico de personas; el PDF puede contener nombres de autores y datos agregados | Decidir si el apéndice y los agregados se mantienen públicos; no se copian aquí |
| PDF E3 y entrega | 17 PDF en `docs/E3/`, 2 en `entrega/` | 19 PDF con metadatos de autor no vacíos | Los metadatos pueden identificar a quien exportó | Decidir sanitización antes de una publicación definitiva; no se imprimen valores |
| DOCX/PPTX | 16 DOCX E3, 1 plantilla, 2 PPTX | 16 DOCX E3 y la plantilla con `creator`; los PPTX con `lastModifiedBy` | Metadatos de autoría/edición | Misma decisión de sanitización; no se reescriben en H1 |
| ZIP histórico | [Orienta_E3_Completo.zip](../../entrega/Orienta_E3_Completo.zip) | 190 entradas, 12,6 MB; 23 PDF; 4 CSV; 2 JSONL; sin el directorio `.git/`, `.venv`, `.runtime`, `node_modules`; no se listan bases, claves ni `.env` (comprobación por nombres) | Publica el paquete completo, incluidos documentos y evidencia | Decidir si el ZIP sigue público; no se regenera |
| Nombres y metadatos | Documentos académicos y de identidad | Nombres de integrantes en documentos de autoría; una tercera persona y calificaciones en [Comentarios_Docentes.md](../fuentes/Comentarios_Docentes.md) | Exposición de un tercero y de evaluaciones | **Decisión humana prioritaria**; no se reproduce el nombre ni la nota |
| Datos de ejemplo vs. estudio | [validacion_usuarios.csv](../../data/validacion_usuarios.csv); [carga_operaciones.jsonl](../../evidencia/carga_operaciones.jsonl); [inicial_carga_operaciones.jsonl](../../evidencia/inicial_carga_operaciones.jsonl) | CSV solo con encabezados; JSONL de operaciones sintéticas de carga; no son estudiantes | Bajo si se mantiene la naturaleza sintética; el CSV vacío no es un estudio | Mantener etiquetado como sintético; no presentar como participantes |
| Assets UdeC | [docs/identidad](../identidad/README.md): 2 logos, 8 archivos de fuentes/licencias, README y JSON | Marca y tipografías; uso académico, sin patrocinio | La marca no tiene licencia abierta verificada; las fuentes sí conservan OFL | Decidir permiso de la marca; conservar textos OFL |
| PDF DEMRE | [oferta_definitiva_2027.pdf](../fuentes/oferta_definitiva_2027.pdf) | 577 páginas, 3,9 MB; fuente oficial; SHA-256 `ca161a…98067` | Documento público; la licencia de redistribución no está verificada | Confirmar condiciones de publicación; citar fuente y hash |
| Documentos del curso | Enunciado (12 pp.), rúbricas (13 pp.), plantilla DOCX | Material aportado para el curso | No hay licencia de redistribución verificada | Confirmar con el curso antes de publicar fuera del contexto académico |
| Fuentes OFL | `docs/identidad/fuentes/Poppins_OFL.txt`, `Roboto_OFL.txt` | Textos de licencia conservados junto a las fuentes | Licencia de fuentes cubierta; no cubre la marca | Mantener los textos; no confundir OFL con licencia del logo |
| Historia y duplicados | Dossier E2, Cobertura R2, Dossier E3 y formatos PDF/DOCX/MD | Enlaces E2 rotos y documentos duplicados en tres formatos | Un lector puede confundir antecedente con producto o citar un activo ausente | Ver [inventario](Inventario_Antecedentes.md); no reparar originales en H1 |

En la revisión acotada no se encontraron credenciales, bases de ejecución ni microdatos de estudiantes; sí se identificó una exposición de una tercera persona en los comentarios docentes. Esa afirmación no es una auditoría exhaustiva de cada PDF, DOCX o imagen. La búsqueda de secretos de E3 cubrió 80 archivos y no halló patrones; no sustituye una revisión de seguridad.

## 3. Licencias y procedencia

| Material | Licencia / permiso | Estado |
| --- | --- | --- |
| Código y documentos del repositorio | Sin licencia declarada | No se puede afirmar reutilización libre; decisión del propietario |
| SRS E1, documentos del curso y comentarios | Sin licencia de redistribución verificada | Se conservan como material académico aportado; no se impone una licencia abierta |
| Dossier E2, matriz y artefactos de diseño | Sin licencia verificada | Antecedente; su publicación no concede permiso |
| Ficha original de 12 ítems | CC BY 4.0 **propuesta** | No consta concesión formal; no se presenta como licencia vigente |
| Marca UdeC | Derechos de la universidad; uso académico | No implica patrocinio ni aprobación; permiso no verificado |
| PDF DEMRE/Mineduc | Documento público | Licencia de redistribución no verificada |
| Poppins/Roboto | SIL OFL 1.1, textos incluidos | Cubre las fuentes; no la marca |
| Dependencias Python/navegador | Declaradas en [Declaracion_IA_Licencias](../E3/Declaracion_IA_Licencias.md) | No es una auditoría legal exhaustiva; el lockfile fija versiones |

La declaración de IA de E3 es histórica. H1 no la reescribe ni le atribuye autoría humana. La ausencia de licencia del repositorio no anula las licencias OFL de las fuentes, que se conservan; tampoco se extrapola OFL al código, la marca o los documentos académicos. Cualquier cambio de licencia o de visibilidad requiere decisión del propietario y no se ejecuta en este hito.

## 4. Decisiones humanas pendientes

| ID | Decisión | Por qué | Estado | Efecto si no se resuelve |
| --- | --- | --- | --- | --- |
| D1 | Mantener público o volver privado | El repositorio expone material histórico y de terceros | Pendiente | No se puede afirmar que la exposición sea aceptada |
| D2 | Añadir licencia o declaración de derechos | Hoy no hay licencia detectada | Pendiente | Público seguiría sin permiso de reutilización |
| D3 | RF-02: instrumento autorizado vs. ficha original | E1 p. 11: «Presenta y registra ítems de instrumento autorizado»; precondición «instrumento seleccionado legalmente» ([PDF](../fuentes/SRS_E1_original.pdf#page=11)); E3 usa 12 ítems originales no validados | Pendiente | No se puede declarar equivalencia ni cierre del requisito; decisión previa al congelamiento de requisitos |
| D4 | CC BY 4.0 de la ficha | Es una propuesta, no una concesión | Pendiente | No se puede citar como licencia vigente |
| D5 | Nombre/calificaciones de tercero en comentarios docentes | Exposición concreta en archivo público | Pendiente | Riesgo de privacidad y de tratamiento no autorizado |
| D6 | Sanitizar metadatos de PDF/DOCX/PPTX | Pueden identificar a autores/exportadores | Pendiente | Exposición de nombres en metadatos |
| D7 | Permisos UdeC, DEMRE y documentos del curso | No hay licencia de redistribución verificada | Pendiente | Publicación sin base verificada |
| D8 | Recuperar o aceptar ausencia de activos E2 | Faltan diagramas, mockups y evidencias de la PoC | Pendiente | E2 no es autosuficiente; E4 debe declararlo |
| D9 | Datos reales y validación con personas | No hay protocolo ejecutado ni consentimientos | Pendiente | El piloto real sigue bloqueado; encuestas E1 no sustituyen |
| D10 | Fuente canónica de documentos E3 | Hay Markdown, DOCX y PDF duplicados | Pendiente | Correcciones divergentes o citas a versiones distintas |

Estas decisiones no las puede tomar la implementación automatizada. H1 solo las hace visibles y evita que una omisión se lea como aprobación.

## 5. Qué no se hizo

No se cambió la visibilidad ni la licencia; no se redactaron ni eliminaron datos; no se copiaron nombres, notas, tokens o microdatos; no se repararon los originales E2; no se regeneró el ZIP ni el manifiesto; no se publicó una conclusión legal. Si el propietario decide sanitizar o retirar material, será un cambio posterior y trazable.
