# Inventario de antecedentes y mapa hacia E4

Este documento ordena qué material de E1, E2 y E3 está en el repositorio oficial, qué se puede usar para evaluar y qué falta. No redacta E4 ni convierte un enlace en evidencia. Los capítulos y artefactos son destinos previstos, no texto ya escrito.

## 1. Método y límites de acceso

Se revisaron los archivos versionados del corte `e04eb2d`, el manifiesto y el ZIP de E3. Se cotejaron el SRS E1 original (49 páginas), el inventario E1 y el dossier E2 local. No se clonó, movió ni editó el checkout histórico `orienta-grupo9`. La consulta no autenticada a la API devuelve `404`; con acceso autenticado de solo lectura al árbol del SHA se cotejaron los blob IDs de SRS E1, dossier E2 y matriz, y se confirmó la presencia de diagramas, DDL, mockups y archivos de evidencia de la PoC. No se descargaron contenidos. El cotejo se limita a lo declarado en [PROCEDENCIA](../../PROCEDENCIA.md) y a los archivos locales.

### Cotejo de procedencia

| Objeto | Registro / archivo | Resultado | Límite |
| --- | --- | --- | --- |
| E1 | SRS E1 v1.8 y [inventario E1](../fuentes/Inventario_SRS_E1.md) | 49 páginas; 17 RF, 21 RNF, 7 restricciones y 10 reglas; coincide con el inventario; blob Git `13a36d07c9069aac4872cf41daaa0b289fd723a1` | Sin descarga de contenido remoto; solo copia local y blob ID del árbol |
| E2 | [Dossier E2](../antecedentes/Dossier_E2_Completo.md) y [matriz](../antecedentes/Matriz_Decision_E2.csv) | 456 líneas; pesos 100; totales 3,95 / 3,60 / 2,20; blobs `fc96a0e7e0911377bfb2d2af1702509f93fe559c` y `ec059bad1399631669fadfb20084f9c18060b154` | Los activos están en el árbol antecedente, no en el checkout oficial; no se descargaron |
| E3 | [Manifiesto](../../entrega/manifest.json) y ZIP | 189/189 blobs coinciden en `e04eb2d`; ZIP de 190 entradas con las mismas huellas | El manifiesto no cubre H1 ni certifica autoría; `application_commit` es `a845244…` |

## 2. E1 · problema, requisitos y encuesta

| Actividad / fuente | Archivo local | Estado y límite |
| --- | --- | --- |
| Problema, usuarios, alcance y encuesta de conveniencia (156 estudiantes y 36 apoderados) | [SRS_E1_original.pdf](../fuentes/SRS_E1_original.pdf) | Original conservado; 49 páginas; 17 RF (11 Must), 21 RNF, 7 restricciones y 10 reglas de negocio. No es el producto actual ni validación de uso. |
| Inventario de requisitos y calendario E1 | [Inventario_SRS_E1.md](../fuentes/Inventario_SRS_E1.md) | Documento de análisis del antecedente; conserva rutas del checkout histórico y no acredita ejecución. |
| Reanálisis de la encuesta | [Encuestas_Reanalisis.md](../E3/Encuestas_Reanalisis.md), [encuestas_reanalisis.json](../../evidencia/encuestas_reanalisis.json) | Agregados de 192 registros históricos; no hay filas crudas nuevas ni participantes reclutados. Encuesta ≠ usabilidad. |
| Enunciado, rúbricas y plantilla del curso | [Enunciado](../fuentes/Enunciado_Proyecto_Semestral.pdf), [rúbricas](../fuentes/Rubricas_Proyecto_Semestral.pdf), `Plantilla_SRS_IEEE830_2026.docx` | Documentos aportados para el curso; su licencia de redistribución no está verificada. |
| Comentarios docentes y puntajes PDR | [Comentarios_Docentes.md](../fuentes/Comentarios_Docentes.md) | Transcripción aportada, no captura del LMS. Contiene una exposición de terceros que requiere decisión; no se reproduce aquí. |

E1 aporta la línea base, no el estado de implementación. El SRS E3 conserva los IDs y corrige la especificación; la fuente original no se reescribe.

## 3. E2 · diseño, alternativas y PoC

| Actividad / fuente | Archivo local | Estado y límite |
| --- | --- | --- |
| Dossier de diseño E2 | [Dossier_E2_Completo.md](../antecedentes/Dossier_E2_Completo.md) | Copia local de 456 líneas; problemas, dominio, CI1/CI2, tres alternativas, matriz, arquitectura, PoC, costos y riesgos. No es MVP. |
| Matriz ponderada | [Matriz_Decision_E2.csv](../antecedentes/Matriz_Decision_E2.csv) | Siete criterios, pesos que suman 100; totales 3,95 / 3,60 / 2,20. Son juicios de ingeniería, no mediciones. |
| Cobertura y revisión R2 | [Cobertura_Rubrica_R2.md](../antecedentes/Cobertura_Rubrica_R2.md), [Revisión_R2](../antecedentes/Revision_Rubrica_R2_2026-10-27.md) | Material histórico; contiene enlaces a archivos que no están en este repositorio. |
| Diagramas y modelos | [docs/modelos](../modelos/Modelo_Datos.png) | Diagramas E3 en DOT/SVG/PNG; no son los archivos E2 originales y no cubren todo lo que el dossier E2 promete. |
| Identidad y tipografías | [docs/identidad](../identidad/README.md) | Marca UdeC y fuentes OFL; uso académico, no patrocinio. La marca no tiene licencia abierta verificada. |
| Mockups y PoC E2 | No están en el checkout oficial | El árbol antecedente conserva diagramas, DDL, mockups y archivos de evidencia de su PoC; no se descargaron ni copiaron. No se verificó el contenido de los 15/23 contratos. |

E2 sigue siendo el antecedente de las tres alternativas y de la matriz. La implementación E3 se aparta de la PoC en persistencia y controles, por lo que no se debe presentar la PoC como el producto.

## 4. E3 · producto y evidencia

| Actividad / fuente | Archivo local | Estado y límite |
| --- | --- | --- |
| SRS v2.0 | [SRS_IEEE830_E3.md](../E3/SRS_IEEE830_E3.md) | 14 secciones; RF atómicos, RF18/19, 21 RNF y límites. No sustituye validación humana. |
| Trazabilidad | [Trazabilidad_RF_RB.md](../E3/Trazabilidad_RF_RB.md) | Mapa RF→RB→RNF→componente→prueba; algunos vínculos son más amplios que la prueba citada (ver [matriz](Matriz_Requisitos.md)). |
| RNF | [RNF_Mediciones.md](../E3/RNF_Mediciones.md) | 21 IDs con objetivo, método, resultado y veredicto; varios quedan parciales o no acreditados. |
| Ciencias | [Ciencias_Ingenieria.md](../E3/Ciencias_Ingenieria.md) | CI1 (normalización y 3FN) y CI2 (AES-256-GCM); límites de motor, TLS y KMS explícitos. |
| Validación | [Validacion_Usuarios.md](../E3/Validacion_Usuarios.md) | Protocolo y CSV sin filas; no hay sesiones reales de E3. |
| Costos y riesgos | [Costos_Riesgos_Plan.md](../E3/Costos_Riesgos_Plan.md) | Caja incremental 0; HH humanas no aportadas; 10 riesgos y replanificación. |
| Iteraciones y trade-offs | [Respuesta_Docente_Iteraciones.md](../E3/Respuesta_Docente_Iteraciones.md) | Tres iteraciones y tres intercambios; la respuesta docente depende de una transcripción, no de una captura. |
| Defectos | [Defectos.csv](../E3/Defectos.csv) | D01–D08; D06 (uso externo) y D07 (TLS/cifrado) siguen abiertos. |
| IA y licencias | [Declaracion_IA_Licencias.md](../E3/Declaracion_IA_Licencias.md) | Declaración histórica de E3; menciona el repositorio como privado, hoy desactualizado. No se reescribe en H1. |
| Paquete | [manifest.json](../../entrega/manifest.json), [ZIP](../../entrega/Orienta_E3_Completo.zip) | 189 blobs verificados en `e04eb2d`; ZIP de 190 entradas; no cubre H1. |

## 5. Fuente → archivo local → destino E4

Los capítulos se refieren a la estructura oficial de E4 (1 introducción; 2 problema/contexto; 3 requisitos/diseño; 4 ciencias/construcción; 5 verificación/validación; 6 economía/ética; 7 operación/continuidad; 8 conclusiones) y a los siete artefactos de la guía.

| Fuente o actividad | Archivo local | Destino E4 | Condición / límite |
| --- | --- | --- | --- |
| Problema, stakeholders y encuesta E1 | SRS E1; [Encuestas_Reanalisis](../E3/Encuestas_Reanalisis.md); [Fuentes_Publicas](../E3/Fuentes_Publicas.md) | Cap. 2; artefacto 1 | Muestra de conveniencia; no prevalencia ni uso |
| Requisitos priorizados | SRS E3 §3–4 y §9.1; [Trazabilidad](../E3/Trazabilidad_RF_RB.md) | Cap. 3; artefacto 2 | RF02 no conforme ([SRS E1 p. 11](../fuentes/SRS_E1_original.pdf#page=11)); RF12/13 sin prueba versionada |
| Modelos, cálculos y ciencias | [docs/modelos](../modelos/Modelo_Datos.png); [Ciencias](../E3/Ciencias_Ingenieria.md) | Cap. 4; artefacto 3 | Diagramas E3; el dominio E2 original no está |
| Tres alternativas | [Dossier E2 §3](../antecedentes/Dossier_E2_Completo.md); SRS E3 §8 | Cap. 3; artefacto 4 | Alternativas de diseño, no benchmark |
| Matriz ponderada | [CSV E2](../antecedentes/Matriz_Decision_E2.csv); Dossier §4 | Cap. 3; artefacto 5 | Pesos y notas E2; sensibilidad declarada |
| Riesgos actualizados | [Costos_Riesgos_Plan](../E3/Costos_Riesgos_Plan.md); Dossier §8.3 | Caps. 6–7; artefacto 6 | P/I ordinales; no frecuencias |
| Tres trade-offs | [Respuesta_Docente_Iteraciones](../E3/Respuesta_Docente_Iteraciones.md); Dossier §8.1 | Cap. 3; artefacto 7 | Tres formulados; efecto verificado solo donde hay prueba |
| Arquitectura y despliegue | SRS §2, §5; [C4_Contexto](../modelos/C4_Contexto.png), [C4_Contenedores](../modelos/C4_Contenedores.png) | Caps. 3–4 | Local; sin TLS ni operación real |
| Pruebas y RNF | [tests/test_workflow.py](../../tests/test_workflow.py); [RNF](../E3/RNF_Mediciones.md); [evidencia](../../evidencia/carga.json) | Cap. 5 | 24 tests, 414/421 líneas (98,34 %), 89/92 ramas (96,74 %); sin E2E/carga repetidos en H1 |
| Validación con usuarios | [Validacion_Usuarios](../E3/Validacion_Usuarios.md); [CSV](../../data/validacion_usuarios.csv) | Cap. 5 | Pendiente; no hay filas reales |
| Costos y continuidad | [Costos_Riesgos_Plan](../E3/Costos_Riesgos_Plan.md) | Caps. 6–7 | Sin HH humanas ni gasto nuevo |
| Ética, licencias e IA | [Declaracion_IA_Licencias](../E3/Declaracion_IA_Licencias.md); [Exposición](Exposicion_y_Licencias.md) | Caps. 6–7 y anexos | Decisiones humanas pendientes |
| Defensa y guiones | [Guion oral](../E3/Guion_Oral_10_Minutos.md); [demo](../E3/Guion_Demo.md); [entrega](../../entrega/LEEME.md) | Cap. 8 / E5 | No acredita ensayo ni exposición |
| Paquete E3 | [manifest](../../entrega/manifest.json); [ZIP](../../entrega/Orienta_E3_Completo.zip) | Anexo de reproducibilidad | Corte E3; no incluye H1 |

## 6. Siete artefactos: ubicación sustantiva

| Artefacto | Ubicación local | Fuerza | Límite |
| --- | --- | --- | --- |
| 1. Caso y stakeholders | SRS E3 §2.3–2.4; [Fuentes_Publicas](../E3/Fuentes_Publicas.md); [Encuestas](../E3/Encuestas_Reanalisis.md) | Problema y afectados con fuentes y límites | Encuesta local; no representa al país |
| 2. Requisitos priorizados | SRS §3–4, §9.1; [Trazabilidad](../E3/Trazabilidad_RF_RB.md) | IDs, MoSCoW y criterios | RF02 no conforme ([SRS E1 p. 11](../fuentes/SRS_E1_original.pdf#page=11)) y pruebas parciales |
| 3. Modelos y memoria de cálculos | [docs/modelos](../modelos/Modelo_Datos.png); [Ciencias](../E3/Ciencias_Ingenieria.md) | ER, C4, secuencia y fórmulas | No hay prueba formal de 3FN ni modelo de dominio E2 |
| 4. Tres soluciones | Dossier E2 §3; SRS §8 | Tres arquitecturas comparables | Sin benchmark ni cotización |
| 5. Matriz ponderada | CSV E2; Dossier §4 | Pesos, notas y sensibilidad | Juicios, no mediciones |
| 6. Riesgos | Costos_Riesgos_Plan; Dossier §8.3 | 10 riesgos con disparador y residual | Sin frecuencias ni materializaciones completas |
| 7. Trade-offs | Respuesta §Tres intercambios; Dossier §8.1 | Tres formulaciones X→Y→Z | Efecto verificado solo en algunos |

## 7. Enlaces E2 rotos y equivalencias E3

El verificador local encontró **31 enlaces locales rotos en 3 archivos de antecedentes** (14 en Cobertura R2, 9 en Dossier E2 y 8 en Revisión R2). No se reparan los originales: se indexan aquí para no confundir una referencia muerta con evidencia disponible.

| Referencia E2 | Estado local | Equivalente E3 | Nivel de sustitución |
| --- | --- | --- | --- |
| `modelos/Dominio.png` | falta | [Modelo_Datos.png](../modelos/Modelo_Datos.png) | Parcial: modelo lógico/ER, no el dominio E2 |
| `modelos/Modelo_Logico.png` | falta | Modelo_Datos + [Ciencias](../E3/Ciencias_Ingenieria.md) | Parcial: esquema implementado, no DDL E2 |
| `modelos/esquema_logico.sql` | falta | `orienta/migrations/0001_initial.py` | Implementación, no el DDL histórico |
| `modelos/C4_L2.png` | falta | [C4_Contenedores.png](../modelos/C4_Contenedores.png) | Equivalente de propósito |
| `modelos/C4_L3.png` | falta | ninguno exacto | Brecha: no hay C4 L3 E3 localizado |
| `modelos/Secuencia_Comparacion.png` | falta en esa ruta | [Secuencia_Comparacion.png](../modelos/Secuencia_Comparacion.png) | Diagrama E3 del mismo nombre; no se probó identidad |
| `integrantes/…/C4_L1_Contexto.png` | falta | [C4_Contexto.png](../modelos/C4_Contexto.png) | Equivalente de propósito |
| `mockups/capturas/*.jpg` | falta | [evidencia/navegador](../../evidencia/navegador/) | Distinto: capturas reales de E3, no mockups |
| `evidencia/modelo_integridad.json`, `poc_*` | falta | [tests/test_workflow.py](../../tests/test_workflow.py); [pruebas.log](../../evidencia/pruebas.log) | Distinto: suite E3, no los 15/23 contratos E2 |
| Paquete E2 (PPT/PDF/XLSX) | falta | [entrega](../../entrega/LEEME.md) | Distinto: entrega E3 |

Consecuencia: el repositorio **no es autosuficiente para reconstruir todo E2**. La evaluación puede usar E2 como antecedente y E3 como producto, pero debe declarar que los diagramas y evidencias E2 originales no están en el checkout oficial. Recuperarlos exige una decisión humana y acceso al checkout histórico; no se copian aquí.

### Recuperación mínima propuesta

Con permiso humano previo, el mínimo sería: (1) conservar los tres blobs ya cotejados —SRS E1, dossier E2 y matriz— con sus IDs; (2) incorporar los diagramas de dominio/lógico/C4 y el DDL necesarios para entender el diseño; (3) decidir por separado si se incorporan mockups y evidencia de la PoC; (4) no usar el árbol privado como dependencia de evaluación. H1 no ejecuta esta recuperación ni copia activos.

## 8. Obsolescencias y duplicados

- **Visibilidad:** [README](../../README.md) fue corregido en H1. El SRS, el dossier, la declaración de IA y la bitácora todavía describen el repositorio como privado; son afirmaciones históricas desactualizadas en la observación del 23/11/2026, cuando el repositorio figura público. No se editaron en H1.
- **CI:** la CI pública de `e04eb2d` tiene dos runs `success` (run [45168123412](https://github.com/ba-hc/orienta-proyecto/actions/runs/45168123412), job `verificar`); [ci_codigo.json](../../evidencia/ci_codigo.json) conserva una corrida anterior `a845244…`, y el SRS cita `471dc2c`. No hay contradicción, pero H1 no ejecutó una CI nueva ni cubre el diff.
- **Cobertura:** E3 y H1 comparten las mismas fracciones: 414/421 líneas (98,34 %) y 89/92 ramas (96,74 %); no hay diferencia entre corridas. El reporte combinado muestra 98 %, pero no se usa como porcentaje de líneas.
- **Formatos:** los documentos E3 existen en Markdown, DOCX y PDF. El Markdown es la fuente legible; DOCX/PDF son exportaciones. H1 no las regenera. Cualquier corrección futura debe decidir la fuente canónica y reexportar.
- **Duplicación:** el [Dossier_E3](../E3/Dossier_E3.md) reúne contenido de documentos individuales; para detalles se usan los documentos específicos. `Encuestas_Resultados.pdf` y `Encuestas_Reanalisis` describen los mismos 192 registros; no son dos estudios.
- **Rutas históricas:** `Inventario_SRS_E1.md` y `AGENT_SETUP.md` usan rutas de otros checkouts. Son registros de procedencia, no instrucciones vigentes.

## 9. Vías locales sustantivas para evaluación

Sin `orienta-grupo9`, un evaluador puede: leer el SRS E3 y la trazabilidad; instalar y ejecutar la app con el runtime descartable; correr los 24 tests y coverage; importar y enriquecer el catálogo; revisar las mediciones y límites en `evidencia/`; y contrastar el paquete E3 contra su manifiesto. No puede reconstruir los activos E2 faltantes ni acreditar uso real con estudiantes. Esa diferencia debe quedar visible en E4.
