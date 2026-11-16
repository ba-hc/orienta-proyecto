# Inventario de fuentes — Avance oral 2 (E3)

**Checkout revisado:** `/home/ben/Paseo/Chats/.orienta-ao2-work/revision-fuentes`
**Rama:** `main`
**SHA completo:** `a92f1fd3cfea061543cf14557320120793b32eb1`
**SHA corto:** `a92f1fd`
**Estado del checkout:** limpio; solo lectura. No se modificó ningún archivo del proyecto.
**Único archivo escrito por este trabajo:** `/home/ben/Paseo/Chats/.orienta-ao2-work/inventario-srs.md`

**Fuentes principales y abreviaturas**

| Abreviatura | Fuente | Extensión |
|---|---|---|
| **SRS** | `entregas/E1/Orienta_E1_Grupo9_Informe_SRS.pdf` | 49 páginas; v1.8, 08/10/2026 |
| **EN** | `docs/curso/Enunciado_Proyecto_Semestral.pdf` | 12 páginas |
| **RB** | `docs/curso/Rubricas_Proyecto_Semestral.pdf` | 13 páginas; R3 en pp. 6–7 |
| **SYL** | `docs/curso/Syllabus_Proyecto_Informatico.pdf` | calendario en «IX.- Planificación» |
| **E2D** | `entregas/E2/Dossier_E2_Completo.md` | dossier técnico E2 |
| **E3R** | `entregas/E3/README.md` | único archivo de E3 |

**Método.** `pdftotext -layout` a `/tmp/ao2src`, separación por saltos de página y cotejo de la página impresa de cada PDF. Las páginas citadas son las impresas en el pie («Página X de Y» / «| X»), no el índice del visor. Se revisaron además `README.md`, `ROADMAP.md`, `VERIFICACION.md`, `entregas/E1/README.md`, `entregas/E2/README.md`, `entregas/E2/Revision_Rubrica_R2_2026-10-27.md`, la PoC en `integrantes/benjamin-henriquez/04_PoC/` y el historial git. `docs/identidad/README.md` se leyó como referencia de identidad gráfica; no aporta requisitos ni calendario.

**Límite de lectura.** «No encontrado en el checkout» significa ausencia de evidencia en este corte, no prueba de que el hecho no haya ocurrido. No se inventan observaciones de la PDR, resultados con usuarios, contribuciones, horas ejecutadas ni autorizaciones. No se analizan algoritmos de seguridad ni datos personales crudos.

---

## 0. Hallazgos que condicionan la preparación de E3

1. **E1 contiene los artefactos que este inventario necesitaba:** 17 RF (11 Must), 21 RNF, dos aplicaciones CI, siete restricciones, diez riesgos y cinco roles. Los RNF son metas y métodos, no mediciones.
2. **E3 está casi vacío en el checkout:** `entregas/E3/` solo contiene un README que dice «por preparar» y «todavía no contiene una entrega de esta fase».
3. **E2 aporta diseño y PoC, no MVP:** hay modelos, mockups y una PoC Django con 15/15 contratos y 23/23 comprobaciones de modelo, pero el propio paquete declara que no es el MVP, no mide carga y no acredita validación con estudiantes.
4. **La brecha de mayor peso está en C1 y C2:** suman 36 % de R3; ambas dependen de evidencia que no aparece en el checkout (respuesta a la PDR, iteraciones, software parcial vivo).
5. **Hay un conflicto de tiempo que debe resolverse antes de exponer:** EN fija 10 minutos de exposición + 5 de preguntas; RB R3-C7 habla de «dentro de los 12 minutos».

---

## 1. Requisitos funcionales RF-01…RF-17

**Prioridad:** M = Must, S = Should, C = Could, W = Won't. La tabla resumen está en SRS pp. 9–10; el detalle Dado/Cuando/Entonces de los Must está en SRS pp. 10–13.

| ID | Título | Prioridad | Aceptación sustantiva | Pág. |
|---|---|---|---|---|
| RF-01 | Crear proceso y acceso | M | Dado un estudiante sin proceso, cuando inicia y confirma, entonces obtiene un proceso asociado a su credencial; **no se solicita RUT**. El acceso queda aislado. | 9–11 |
| RF-02 | Administrar intereses | M | Dado un formulario con una respuesta inválida, cuando se intenta finalizar, entonces se indica el ítem y no se genera resultado; con respuestas válidas se registra una **aplicación versionada**. | 10–11 |
| RF-03 | Presentar intereses | M | Dado un instrumento completado, cuando se consulta el resultado, entonces se muestran dimensiones y **límites de interpretación**; no se diagnostica ni se prescribe una carrera. | 10–11 |
| RF-04 | Gestionar prioridades | M | Dado un estudiante que marca ubicación como alta prioridad, cuando guarda, entonces la prioridad aparece **persistida y resaltada** en la comparación posterior; si falta, queda «sin definir». | 10–12 |
| RF-05 | Explorar catálogo | M | Dado el catálogo UdeC 2027, cuando se filtra por campus, entonces solo aparecen ofertas del campus indicado; cada tarjeta identifica su **ciclo**. | 10, 12 |
| RF-06 | Detalle y origen | M | Dado un indicador de empleabilidad ausente, cuando se abre el detalle, entonces se muestra «información no disponible» y **no 0 %**; se muestran fuente y vigencia. | 10, 12 |
| RF-07 | Guardar alternativas | M | Dado que una oferta ya está guardada, cuando se intenta guardarla otra vez, entonces **no aparecen duplicados**; se puede retirar. | 10, 12 |
| RF-08 | Elegir par | M | Dado solo una alternativa seleccionada, cuando se solicita comparar, entonces el sistema pide **exactamente dos**; con dos distintas continúa. | 10, 12–13 |
| RF-09 | Comparación factual | M | Dadas dos ofertas con duraciones diferentes y prioridad alta en duración, cuando compara, entonces ambas duraciones se muestran con **unidades consistentes** y se destaca la prioridad. | 10, 13 |
| RF-10 | Razones y faltantes | M | Dado que una dimensión carece de dato confiable, cuando se muestran razones, entonces se presenta como **dato faltante** y no se declara una opción ganadora. | 10, 13 |
| RF-11 | Persistencia del proceso | M | Dado el proceso de A guardado, cuando B intenta abrirlo con el identificador de A, entonces se deniega y no se revelan datos; cuando A regresa, recupera su estado. | 10, 13 |
| RF-12 | Modificar contexto | S | Permite editar prioridades y recalcular la vista comparativa; los cambios se reflejan en la comparación. Solo resumen, sin D/C/T. | 10 |
| RF-13 | Resumen de avance | S | Presenta el estado actual de exploración y las tareas pendientes. Solo resumen, sin D/C/T. | 10 |
| RF-14 | Exportar resumen | C | Genera un resumen local opcional **sin revelar datos de terceros**. Solo resumen, sin D/C/T. | 10 |
| RF-15 | Panel institucional | W | Acceso de orientador a procesos individuales o agregados; **excluido del MVP**. Sin D/C/T. | 10 |
| RF-16 | Chat conversacional IA | W | Orientador automatizado conversacional; **excluido del MVP**. Sin D/C/T. | 10 |
| RF-17 | Ranking global | W | Porcentaje global de compatibilidad y carrera ganadora; **excluido: no match global**. Sin D/C/T. | 10 |

**Observación de completitud:** solo RF-01…RF-11 tienen flujo principal, alternos/excepciones y D/C/T en §3.2. RF-12…RF-17 quedan en la tabla resumen de p. 10, sin flujo ni criterio detallado. No es una invención de este informe: el SRS no desarrolla esos seis requisitos Should/Could/Won't.

**MoSCoW y MVP (SRS p. 22):** Must = RF-01 a RF-11; Should = RF-12, RF-13; Could = RF-14; Won't = RF-15, RF-16, RF-17. El MVP comprometido es el recorrido Must completo, mostrable de extremo a extremo en hasta 15 minutos con datos sintéticos.

---

## 2. Requisitos no funcionales: los 21 RNF

Los valores son **objetivos de diseño** y métodos previstos, no mediciones de E1 (SRS p. 14). La tabla siguiente reproduce el objetivo literal y resume el método de verificación; la página remite a la tabla original.

| ID | Objetivo literal (SRS) | Método de verificación (SRS) | Pág. |
|---|---|---|---|
| RNF-R01 | «LCP ≤2,5 s, INP ≤200 ms y CLS ≤0,1; objetivo p75 cuando exista muestra de campo suficiente.» | Lighthouse para laboratorio (LCP/CLS y trazas); RUM/telemetría de navegador para p75 de campo si hay muestra; informar n y dispositivo. | 14 |
| RNF-R02 | «p95 de consulta y guardado ordinarios ≤1.000 ms con 50 usuarios concurrentes.» | Prueba con 50 usuarios virtuales, lectura y guardado mixtos, 10 min estables; reportar p95, tasa de error y entorno. | 14 |
| RNF-R03 | «Soportar 360 procesos y catálogo UdeC 2027 completo; validar cantidad de registros por código/sede.» | Carga de datos semilla + consulta integral y capacidad. | 14 |
| RNF-R04 | «En 50 sesiones concurrentes, tasa de fallos ≤1 % en flujo de lectura/guardado.» | Carga de 50 usuarios virtuales durante 10 min, escenario 70 % lectura y 30 % guardado; reportar errores funcionales y HTTP 5xx por separado. | 14 |
| RNF-D01 | «Disponibilidad ≥99 % de disponibilidad objetivo en horario de uso piloto declarado.» | Monitorizar ventana horaria publicada y registrar caídas. | 14 |
| RNF-D02 | «Meta preliminar RPO ≤24 h y RTO ≤4 h; se revisará en E2.» | Ejercicio de restauración con registro de tiempos; revisar tras E2. | 14 |
| RNF-S01 | «100 % de accesos a procesos personales requieren autenticación; sesiones expiradas denegadas.» | Pruebas positivas y negativas de autenticación y vencimiento. | 15 |
| RNF-S02 | «0 accesos cruzados en suite de autorización de lectura, edición y eliminación.» | Pruebas de IDs ajenos / roles / permisos. | 15 |
| RNF-S03 | «100 % del tráfico con datos personales protegido mediante HTTPS; 100 % de repositorios persistentes que almacenan datos personales con cifrado en reposo activo y verificable antes de pruebas reales.» | Inspección de configuración TLS; revisión documental y comprobación de configuración efectiva de cifrado en almacenamiento y respaldos antes del piloto. | 15 |
| RNF-S04 | «0 credenciales/secretos en logs o archivos versionados; registro de eventos críticos sin respuestas de intereses.» | Revisión de logs, búsqueda automatizada de secretos y checklist. | 15 |
| RNF-S05 | «100 % de datos identificables de pruebas reales sujetos a finalidad, acceso, retención y eliminación declarados.» | Matriz de cumplimiento con muestreo documental. | 15 |
| RNF-U01 | «Cumplir criterios aplicables WCAG 2.1 AA; analizar además mejoras pertinentes de WCAG 2.2.» | Inspección por criterio; axe + pruebas manuales teclado/lector. | 15 |
| RNF-U02 | «≥80 % de participantes completan comparación sin ayuda (por ejemplo, ≥4/5).» | Protocolo de tareas con ayuda, tiempo y errores observados. | 15 |
| RNF-U03 | «Interfaz en español chileno, responsiva en ancho 360–1440 px.» | Pruebas viewport, zoom y lectura en teléfonos. | 15 |
| RNF-C01 | «Flujo crítico en dos familias de navegador (Chromium y Firefox), versiones estables vigentes.» | Prueba E2E en ambas familias. | 16 |
| RNF-C02 | «100 % de campos externos publicados mantienen URL, ciclo, fecha y unidad; formato de importación documentado.» | Validación de esquema y muestreo de fuentes. | 16 |
| RNF-M01 | «100 % de reglas RB críticas vinculadas a al menos un caso automatizado; cobertura de ramas ≥80 % de módulos de lógica crítica.» | Reporte de trazabilidad y cobertura de tests. | 16 |
| RNF-M02 | «100 % de cambios integrados pasan formateo/lint y pruebas automáticas.» | Registro CI y control de merges. | 16 |
| RNF-M03 | «Eventos de error técnicos registran fecha/tipo y correlación sin datos de intereses.» | Revisión de registros sobre errores inducidos. | 16 |
| RNF-P01 | «Ambiente de desarrollo y prueba reproducibles mediante instrucciones verificables por segundo integrante.» | Instalación limpia por persona no autora. | 16 |
| RNF-P02 | «Despliegue reproducible ≤30 min y recuperación/rollback documentados.» | Cronometrar despliegue a partir de instrucciones. | 16 |

**Cobertura de categorías:** rendimiento/capacidad (4), disponibilidad/continuidad (2), seguridad (5), usabilidad/accesibilidad (3), compatibilidad/interoperabilidad (2), mantenibilidad/calidad interna (3), portabilidad/despliegue (2). Total: **21**.

**Estado real en el checkout:** no hay tabla de valores obtenidos ni veredictos. E2D declara expresamente que RNF-R02 y RNF-R04 «no se han medido» en E2. `VERIFICACION.md` lista como no acreditados: carga con 50 usuarios, catálogo 2027 completo, WCAG completa, HTTPS productivo, restauración del MVP, despliegue y validación con estudiantes. Los 15 contratos de la PoC y los 23 del modelo no son porcentaje de cobertura del MVP.

---

## 3. Aplicaciones de ingeniería CI-1 y CI-2

**Texto exacto de la Tabla 8 (SRS p. 9):**

| ID | Aplicación prevista | Ubicación e impacto en decisión | Validación futura |
|---|---|---|---|
| **CI-1** | «Modelo formal y normalización de datos: entidades, claves, dependencias funcionales, 3FN donde corresponda.» | «Persistencia de procesos, ofertas y fuentes; decisión sobre integridad y eliminación de anomalías.» | «Modelo formal, razonamiento sobre claves y pruebas de actualización/anomalías.» |
| **CI-2** | «Criptografía aplicada: autenticidad/integridad de credenciales y cifrado para datos personales.» | «Acceso y recuperación del proceso; sustenta selección del esquema de seguridad.» | «Modelo de amenazas y pruebas con credenciales válidas, manipuladas, vencidas y acceso cruzado.» |

**Compromiso E1, literal (SRS p. 9):**

> «Ambas aplicaciones se comprometen como trabajo de ingeniería a desarrollar y medir posteriormente; E1 no declara algoritmos criptográficos específicos ni que la normalización ya esté implementada.»

**Lectura de estado:** en E1 son aplicaciones **comprometidas**, no ejecutadas. E2 contiene material parcial: CI-1 tiene descomposición funcional y 23/23 comprobaciones de integridad en SQLite; CI-2 tiene modelo de amenazas y una PoC con pruebas de credenciales/manipulación/acceso cruzado. El propio E2D advierte que CI-1 no demuestra 3FN mediante tests ni portabilidad al motor objetivo, y que la PoC de CI-2 no cubre el almacenamiento completo, HTTPS ni respaldos. Para E3 falta la integración de ambas en el sistema construido y el efecto verificado, no solo el artefacto de diseño.

---

## 4. Presupuesto, hitos y roles: texto y límites

### 4.1 Presupuesto (SRS pp. 23–24)

**Límite de caja:** «Límite aprobado para desembolso directo: CLP 100.000 por semestre.»

**Horas:** «Para semanas 9–18 se considera un techo teórico de 10 semanas × 10 h × 5 personas = 500 HH; 400 HH planificadas y 100 HH de holgura (20 %).»

| Rol | Integrante | HH plan | CLP/h | Subtotal CLP |
|---|---|---:|---:|---:|
| Jefe de proyecto / Product Owner | Jorge Alejandro Slimming Lagos | 80 | 20.000 | 1.600.000 |
| Líder técnico | Benjamín Alonso Henríquez Cid | 80 | 20.000 | 1.600.000 |
| Líder de calidad | Diego Alejandro Gutiérrez Mendoza | 80 | 23.000 | 1.840.000 |
| Líder de datos y seguridad | Mauro Sebastián Muñoz González | 80 | 25.000 | 2.000.000 |
| Líder de operación | Lucas Daniel Morales Oyanedel | 80 | 27.500 | 2.200.000 |
| **Total** |  | **400** |  | **9.240.000** |

| Gasto directo | Provisión CLP | Condición de control |
|---|---:|---|
| Infraestructura/hosting y BD | 30.000 | Estimación presupuestaria, no contratación ni precio cotizado |
| Dominio / DNS opcional | 15.000 | No obligatorio; usar recurso gratuito si conviene |
| Materiales y validación con usuarios | 20.000 | Logística básica, según consentimiento y disponibilidad |
| Contingencia / licencias | 35.000 | Licencias/servicios eventuales; solo con aprobación y registro |
| **Total máximo** | **100.000** | Límite de desembolso directo |

**Costo valorizado:** «Costo valorizado del proyecto (400 HH planificadas + desembolso directo máximo): CLP 9.340.000. Esta cifra no corresponde a una factura, sueldo pagado ni gasto efectivo.»

**Continuidad posterior (proyección, no cotización):** infraestructura y BD hasta CLP 12.000/mes; dominio opcional CLP 1.250/mes; mantención referencial 4 HH/mes × CLP 27.500 = CLP 110.000/mes. Total referencial **CLP 123.250/mes** si se contrata o valoriza la mantención; sin mantención remunerada, **CLP 13.250/mes**. «El presupuesto de CLP 100.000 aplica al semestre, no autoriza continuidad posterior.»

**Límites explícitos:**
- El establecimiento supuesto **no financia una operación permanente**; la continuidad exigirá responsable, aprobación del costo mensual y mantenimiento del catálogo, no comprometidos por E1 (SRS p. 8).
- Las HH son valorización académica de esfuerzo, **no salarios pagados**; el desembolso de caja está topado a CLP 100.000 (SRS p. 23).
- No hay horas ejecutadas acreditadas en el checkout; el CSV de costos E2 dice «no horas ejecutadas».

### 4.2 Hitos (SRS pp. 22–23)

| Hito | Semana | Entregable o condición | Responsable principal | Dependencia / holgura |
|---|---|---:|---|---|
| E1 — Avance escrito | 9 | SRS, anexos y baseline de alcance | Jorge (con aportes de todos) | SRS desde semana 8; revisión del equipo |
| Exploración de alternativas / PoC | 10 | Protocolo y evidencia para evaluar arquitecturas | Benjamín | E1 aprobado internamente; 0–1 semana holgura |
| E2 — PDR | 11 | Selección fundamentada, matriz y primeros modelos | Benjamín/Jorge | PoC; observaciones del docente |
| Construcción inicial | 12–13 | Flujo E2E parcial y datos de catálogo | Benjamín/Mauro/Lucas | Diseño E2; integración antes de E3 |
| MVP demostrable | 13 | Primer recorrido integrado con datos representativos | Equipo | RF Must prioritarios; no incluir Should/Could |
| E3 — CDR | 14 | Software parcial operativo, pruebas y mediciones | Diego | MVP parcial, observaciones E2 |
| Cierre Must / verificación | 15–16 | Ajustes, privacidad, pruebas, validación de uso | Diego y equipo | Reserva para correcciones |
| E4 — Informe final | 17 | Informe, evidencia, costos y continuidad | Jorge | Pruebas y mediciones cerradas |
| E5 — Defensa | 17–18 | Demo real en vivo y defensa compartida | Todos / Lucas (operación) | Contingencia de despliegue, semana 18 |

**Límites:** el SRS dice que «El Gantt del Anexo D muestra compromisos de planificación, no certificaciones de tareas ejecutadas» y que «La planificación es estimativa, no una afirmación de ejecución pasada». La numeración oficial es E1 S9, E2 S11, E3 S14, E4 S17, E5 S17–18; E1 se fecha el 8 de octubre. El Anexo C registra retrospectivamente actividades desde la semana 5 y aclara que el encargo E1 se habilitó el 22 de septiembre (semana 7).

### 4.3 Roles (SRS p. 24)

| Integrante | Rol | Entregables que coordina | Secciones SRS que lidera |
|---|---|---|---|
| Jorge Alejandro Slimming Lagos | Jefe de proyecto / Product Owner | Alcance, seguimiento, planificación, bitácora y coherencia editorial | §1, §2.3, §9, §13 |
| Benjamín Alonso Henríquez Cid | Líder técnico | Alternativas, modelos de contexto y diseño, criterios de ingeniería | §2.2, §2.7, §8 |
| Diego Alejandro Gutiérrez Mendoza | Líder de calidad | Aceptación, RNF, plan de pruebas y trazabilidad | §3, §4, §10–11 |
| Mauro Sebastián Muñoz González | Líder de datos y seguridad | Modelo de información, privacidad, licencias y seguridad | §5–7 |
| Lucas Daniel Morales Oyanedel | Líder de operación | Plan de entornos, continuidad, costos y riesgos operativos | §9.2–9.3, §12 |

**Límites:** la asignación «refleja responsabilidades principales y no exime de revisión colectiva de requisitos ni participación en diseño, pruebas y defensa». La conducción de reuniones «se registrará por acta real» y se planificará rotación para que cada integrante dirija al menos dos; «no se atribuyen conducciones retrospectivas sin respaldo». Los nombres y HH de esta tabla son asignaciones/estimaciones del SRS: **no acreditan autoría, horas ejecutadas ni contribuciones individuales**.

---

## 5. Discrepancias de tiempos, semanas y alcance

No se encontró una plantilla separada de calendario en el checkout; el SRS fija las semanas en §9.2. Las discrepancias verificables están entre EN, RB, SYL y el propio SRS.

| # | Fuente A | Fuente B | Discrepancia y efecto práctico |
|---|---|---|---|
| 1 | **EN p. 7** (tabla de entregables): E3 = «10 y 5 minutos, con software en ejecución»; **EN p. 8** desarrolla E3 sin cambiar el formato. | **RB R3-C7, p. 7:** «Exposición fluida y estructurada dentro de los **12 minutos**». **RB R2-C7, p. 5** repite «12 minutos» para E2. | 12 ≠ 10. El formato oficial es 10 min de exposición + 5 de preguntas. El equipo ya detectó el mismo conflicto para E2 en `entregas/E2/Revision_Rubrica_R2_2026-10-27.md` («La guía del curso asigna 10 minutos de exposición y 5 de preguntas; la rúbrica menciona un máximo de 12 minutos»). Para E3 debe prepararse un guion de **10 min** y no asumir 12; si se usa el margen de 12, se recorta contenido o se explicita que es holgura interna, no tiempo oficial. |
| 2 | **EN p. 8 (E3):** «Diferencias respecto del diseño presentado en la **semana 8**.» | **EN p. 7:** E2 = semana 11; **SRS p. 22:** E2 — PDR = semana 11; **SYL:** E2 = semana del 19/10 (S11). | La semana 8 (28/09) es anterior a E1 (S9) y a E2 (S11). La línea base real del diseño presentado es **E2/S11**, no S8. Usar «semana 8» lleva a comparar contra un diseño que no fue la primera revisión oral. |
| 3 | **EN p. 8 (E3):** «Medición de **cada** requisito no funcional: objetivo, método y valor obtenido.» | **RB R3-C4, p. 6 (nivel Destacado):** «Cada **RNF crítico** medido: valor objetivo, método de medición reproducible, valor obtenido y veredicto.» | El enunciado pide todos; la rúbrica acota el nivel Destacado a los críticos (el nivel Competente habla de «RNF principales»). Para cubrir ambos, medir los 21 RNF o justificar explícitamente cuáles son críticos y por qué el resto no se mide. |
| 4 | **EN p. 8 (E3):** «Software en ejecución, **aun parcial**. Estado de los requisitos imprescindibles.» | **RB R3-C2, p. 6 (nivel Destacado):** «La **mayoría de los RF Must** está implementada.» El nivel Competente pide «una parte significativa del flujo principal, con errores no bloqueantes». | «Parcial» y «mayoría de 11 Must» no son el mismo umbral: mayoría de Must es el listón de Destacado; Competente admite una parte significativa. Una demo mínima puede quedar en «En desarrollo». Conviene declarar el subconjunto Must realmente operativo y su porcentaje. |
| 5 | **RB R3-C1, p. 6:** «Responde una a una las observaciones de la **PDR**.» | **EN p. 7:** E2 se llama «Primera revisión oral: revisión preliminar de diseño»; **SRS p. 22** usa «E2 — PDR». | No hay una instancia PDR separada: PDR = E2. La rúbrica asume la sigla; el enunciado no la usa. Para E3, el cuadro de observaciones debe referirse a E2, no a una reunión distinta. |
| 6 | **EN p. 3, condición 5:** «un equipo de **tres o seis** integrantes». | **EN p. 10:** «En equipos de **3-4** integrantes, los dos últimos roles pueden fusionarse»; **SRS p. 1 y p. 23:** cinco integrantes y cinco roles. | Ambigüedad de plantilla: «tres o seis» no aclara si es una enumeración (3 o 6) o un rango (3 a 6); el SRS usa 5, que solo encaja si es rango, y «3-4» no cubre 5. No se resuelve aquí; conviene confirmar con el docente y no cambiar el presupuesto ni los roles sin esa confirmación. |
| 7 | **EN p. 7:** «Registro de las **seis** restricciones». | **SRS pp. 8–9:** RC-01 a RC-07 (siete); **RB R1-C5, p. 3:** «seis o más». | No es una contradicción: el SRS supera el mínimo. Se registra para evitar que alguien «corrija» el SRS a seis por error. |

**Coincidencias de calendario:** E1 S9, E2 S11, E3 S14, E4 S17 y E5 S17–18 aparecen alineados en EN p. 7, SRS p. 22 y SYL. La fractura concreta es «semana 8» en la descripción de E3; el resto de las semanas no presenta contradicción documental.

**Otras tensiones de alcance, no de tiempo:**
- **RF-12…RF-17 sin D/C/T:** el SRS solo desarrolla los 11 Must; los Should/Could/Won't quedan como resumen. Si E3 quiere demostrar «estado de los requisitos imprescindibles», el universo defendible es RF-01…RF-11.
- **E3 pide «software parcial»; R3-C2 (Destacado) pide «mayoría de Must»:** ver fila 4.
- **E3 pide «medición de cada RNF»; R3-C4 (Destacado) pide «cada RNF crítico»:** ver fila 3.

---

## 6. R3 — C1…C7: peso y evidencia faltante real

**R3 = Avance oral 2: Revisión Crítica de Diseño (E3), 10 % del proyecto (RB p. 6).** Pesos: C1 18 %, C2 18 %, C3 14 %, C4 16 %, C5 12 %, C6 10 %, C7 12 %; suman 100 %. C1+C2 concentran 36 %.

La columna «Lo que exige R3» resume el nivel **Destacado**; el nivel **Competente** admite una versión más simple. La columna de faltantes señala lo que no está acreditado para sostener el nivel alto y, cuando corresponde, el mínimo de Competente.

| Criterio y peso | Lo que exige R3 | Evidencia presente en el checkout | Evidencia faltante real |
|---|---|---|---|
| **C1. Respuesta a la PDR e iteración del diseño — 18 %** | Responder una a una las observaciones de la PDR, indicando qué cambió y qué se mantuvo y por qué. Documentar **al menos dos iteraciones** con disparador (medición, prueba, retroalimentación, riesgo materializado), alternativas consideradas, decisión y efecto verificado. | El paquete E2 contiene selección ALT-1, matriz, riesgos, C4 y PoC. E2D registra decisiones de diseño y límites. | No hay archivo con observaciones de la PDR ni cuadro observación→acción→fundamento. No hay bitácora de dos iteraciones con disparador, alternativas, decisión y efecto verificado. `ROADMAP.md` marca como pendiente «Incorporar observaciones reales de E1/E2 ... cuando existan» y «Al menos 2 iteraciones reales de diseño». No se infiere el contenido de esas observaciones. |
| **C2. Estado de la construcción y demostración parcial en vivo — 18 %** | Ejecutar en vivo el flujo principal de forma sustantiva, con datos representativos y persistencia real. La mayoría de los RF Must implementada. Historial del repositorio con contribución distribuida e integración continua. | PoC Django con 15/15 contratos, fixture sintética, evidencia de navegador y mockups navegables sin backend. E2D y `VERIFICACION.md` describen la PoC y sus límites. | `entregas/E3/` solo tiene README: no hay MVP ni flujo parcial del producto, ni tabla de estado de los 11 Must. La PoC se declara «no es el MVP» y no cubre persistencia del producto, catálogo real ni despliegue; el único backend encontrado es esa PoC. No hay artefacto de CI ni historial de construcción del MVP: `git log` tiene 6 commits, todos de documentación/recursos de E1–E2; ninguno incorpora el MVP. No se afirma que no exista trabajo fuera del checkout; se afirma que **no está acreditado aquí**. |
| **C3. Aplicación de ciencias de la ingeniería y sus resultados — 14 %** | Desarrollar las dos aplicaciones declaradas en E1 con formulación, supuestos, procedimiento y resultados, y mostrar cómo influyeron en el sistema construido. Si exigió teoría nueva, explicar cómo se adquirió y validó. | CI-1: descomposición 3FN, supuestos y 23/23 comprobaciones de integridad en SQLite. CI-2: modelo de amenazas y PoC con pruebas de credenciales/manipulación/acceso cruzado. E2D explicita límites: CI-1 no demuestra 3FN por tests ni PostgreSQL; CI-2 no cubre almacenamiento completo/HTTPS/respaldos. | Falta la integración de ambas en el **sistema construido** y el efecto verificado en E3. Los resultados actuales son de modelo/PoC, no del MVP. No hay nueva medición E3 ni migración al motor objetivo. |
| **C4. Verificación: pruebas y medición de los requisitos no funcionales — 16 %** | Plan de pruebas ejecutado con tipos apropiados (unitarias, integración, E2E y específicas del dominio), cobertura reportada con herramienta, defectos con estado. Cada RNF crítico medido: objetivo, método reproducible, valor obtenido y veredicto. Interpretar desviaciones y decidir. | 15 contratos de PoC, 23 comprobaciones de modelo y QA documental 51/51 (este último no es cobertura de código). SRS pp. 14–16 fija objetivos y métodos. | No hay suite del MVP, cobertura con herramienta ni registro de defectos. No hay tabla RNF con valor obtenido/veredicto. RNF-R02 y RNF-R04 no se midieron en E2. `VERIFICACION.md` declara no acreditados carga 50, WCAG completa, restauración, HTTPS productivo y despliegue; E2D añade Firefox. Los 15+23 contratos no son cobertura del MVP. |
| **C5. Validación con usuarios y análisis de datos — 12 %** | Diseñar la validación según objetivo (a quiénes, cuántos, instrumento, qué se busca establecer), presentar datos, analizarlos con método adecuado y concluir reconociendo límites. | SRS pp. 33–34 tienen el protocolo B.3 (3–5 participantes, consentimiento, tareas) y la ficha B.4 **en blanco** («A completar en sesión»). E1 p. 32 dice que la validación está «programada»/«prevista», no ejecutada. | No hay registros de la validación de concepto/uso: participantes, consentimientos/asentimientos ejecutados, observaciones, análisis ni conclusiones. El SRS solo declara el requisito de consentimiento (Anexo H, p. 41) y no presume autorización para instancias no realizadas. `entregas/E2/README.md` dice que «la defensa, evaluación y validaciones humanas no se acreditan mediante archivos». Las encuestas de mayo son evidencia del problema, no validación de uso del producto. No se inventan resultados. |
| **C6. Costos, riesgos y replanificación — 10 %** | Costo estimado vs ejecutado con desglose y causas de desviación; riesgos materializados con gestión aplicada; replanificación explícita de semanas restantes con compromisos, exclusiones y criterio. | SRS pp. 23–24: 400 HH + 100 holgura, CLP 100.000, roles y provisión. E1 registra diez riesgos; E2 prioriza cinco y tiene CSV de costos por alternativa. | No hay costo ejecutado ni desglose estimado-vs-real: el CSV E2 dice «no horas ejecutadas». No hay riesgos materializados con gestión aplicada. No hay una replanificación **post-E2** que declare compromisos, exclusiones y criterio; el ROADMAP es un plan general. Los riesgos siguen «Abiertos» o con controles parciales; eso no es materialización. |
| **C7. Comunicación oral, uso del tiempo y respuesta a preguntas — 12 %** | Exposición fluida y estructurada dentro de 12 min (rúbrica) / 10+5 (enunciado), lenguaje técnico correcto, apoyo visual informativo, todos los integrantes con dominio, demostración con guion y sin improvisación, respuestas precisas. | Existe presentación/guion E2 de 10 min y una revisión que detecta el conflicto 10 vs 12. | No hay presentación, guion ni guion de demo de E3 en el checkout; `entregas/E3/README.md` dice «por preparar». No hay registro de cronometraje ni de ensayo E3. No se afirma que no se haya ensayado: se afirma que no hay evidencia en este corte. Resolver el 10 vs 12 antes de exponer. |

**Brecha priorizada por peso y evidencia:** C2 y C1 (36 %) son las brechas mayores; C4 (16 %) es la siguiente; C5 y C7 (24 %) dependen de ejecución y registro; C3 (14 %) tiene base E2 pero no integración en el sistema; C6 (10 %) tiene estimaciones pero no ejecución. Esta priorización es de inventario, no una decisión de arquitectura ni de alcance.

---

## 7. Fuentes, comandos y trazabilidad

**Verificación de fuentes**
- `git rev-parse HEAD` → `a92f1fd3cfea061543cf14557320120793b32eb1`; `git branch --show-current` → `main`; `git status --porcelain` sin salida.
- `pdfinfo` confirmó: SRS 49 páginas; RB 13; EN 12.
- `pdftotext -layout` generó `/tmp/ao2src/{srs,rubricas,enunciado,syllabus}.txt`; la separación por `\f` permitió citar la página impresa.
- `grep`/`find` sobre el checkout para localizar RF, RNF, CI, hitos, roles, evidencias E2/E3, archivos de validación, CI y cobertura.
- `git log --oneline` → 6 commits: `ec11cce`, `0a4b2b5`, `91cb1ae`, `7701572`, `65e20fc`, `a92f1fd`; el más reciente es «Audita rubrica R2 y revalida evidencia del diseno».

**Archivos adicionales consultados**
- `README.md`, `ROADMAP.md`, `VERIFICACION.md`, `COMO_COLABORAR.md`, `FUENTES_Y_USO_IA.md`.
- `entregas/E1/README.md`, `entregas/E2/README.md`, `entregas/E3/README.md`.
- `entregas/E2/Dossier_E2_Completo.md`, `entregas/E2/Revision_Rubrica_R2_2026-10-27.md`, `entregas/E2/Guion_E2_Equipo.md`.
- `integrantes/benjamin-henriquez/04_PoC/README.txt`, `registro_pruebas.txt`, `resultados_poc.json`; `entregas/E2/evidencia/poc_contracts.json`, `modelo_integridad.json`.
- `docs/identidad/README.md`: identidad gráfica UdeC, Poppins/Roboto y paleta; aclara que el uso identifica un trabajo académico del Grupo 9 y **no representa una aprobación institucional**. No incide en requisitos, calendario ni evaluación E3.

**Límites del informe**
- No se examinaron datos personales crudos ni se analizaron algoritmos de seguridad; solo se inventarió el estado y el alcance declarado de CI-1/CI-2.
- No se atribuyen observaciones de la PDR, resultados de usuarios, horas ejecutadas, contribuciones individuales ni autorizaciones. Donde no hay archivo, se dice «no encontrado/acreditado en el checkout». El SRS declara en p. 1 «REVISADO POR EL EQUIPO / EN REVISIÓN DOCENTE»; no hay aprobación docente acreditada.
- La evaluación docente, la defensa oral y la calificación no están acreditadas por los PDF ni por este inventario.

**touched_paths**
- `/home/ben/Paseo/Chats/.orienta-ao2-work/inventario-srs.md` (único archivo escrito).
- Checkout del proyecto: sin cambios.
