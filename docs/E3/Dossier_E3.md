# Orienta · Dossier E3

Revisión Crítica de Diseño / Avance oral 2 · Grupo 9 · DIICC, UdeC. Corte: 16/11/2026.

Este documento reúne la respuesta docente, las iteraciones, el estado construido, las ciencias de la ingeniería, la verificación, los datos de necesidades, costos, riesgos y defensa. El sistema es ejecutable y la evidencia técnica está en el repositorio. Las condiciones humanas pendientes se mantienen visibles; no se atribuye una nota ni un cumplimiento total ficticio.

## Lectura de la entrega

Presentación principal: 13 láminas (12 de exposición y referencias), guion de 10 minutos +5 de preguntas. Entrega extendida: 17 láminas. SRS actualizado: 14 secciones de plantilla y 21 RNF. Software: Django, 91 ofertas oficiales, recorrido persistente. Pruebas: 24 tests, 4 recorridos navegador ymediciones con denominadores.

El detalle de cada prueba se conserva en JSON/logs. Para evaluar un RNF hay que leer objetivo, método, valor y veredicto; un resultado de laboratorio no se extiende a una escuela real ni a una población de usuarios.


---

## Respuesta docente e iteraciones verificadas

Corte: 16/11/2026. Base: orienta-grupo9 main a 92f1fd3cfea061543cf14557320120793b32eb1. Fuente de observaciones: transcripción del usuario en docs/fuentes/Comentarios_Docentes.md. El escrito y la PDR se distinguen: el oral 1 aportó puntajes, sin comentario cualitativo adicional. No se atribuyen estas correcciones a una observación oral que no fue aportada.

### Respuesta una a una al escrito (intento 2)

| Observación recibida | Qué cambió | Qué se mantiene y por qué | Evidencia / límite |
| --- | --- | --- | --- |
| C1: encuesta no probabilística; magnitud sin dato público | Se incorpora SIES 2026: retención 1.er año cohorte 2025 de 77,9 %; complemento 22,1 % no retenido en el mismo programa. Se agrega contraste concreto de MiFuturo, Acceso, EligeCarrera y VocationOne. | La encuesta sigue como necesidad local; nunca como prevalencia nacional. La no retención tiene causas múltiples y no prueba indecisión ni eficacia de Orienta. | SRS §2.3, Fuentes_Publicas.md. La brecha de utilidad sigue siendo hipótesis sometida a validación. |
| C2: cifras «5 guardados» y «22×12» sin fuente; TI no descrita | «5 guardados» se reclasifica como estimación de dimensionamiento, no límite implementado; «22×12» se retira como horario real. Se caracteriza un escenario de TI y se adjunta ficha para verificar una escuela concreta. | 360 = 8 × 45 y 50 = 45 + 5 siguen como escenarios de capacidad; 45 se referencia al Decreto 8144. No se presenta 8 cursos como matrícula observada. | SRS §2.3–2.5 y carga 360/50. Recursos supuestos: PC con navegador, red estable, responsable TI; falta inspección de establecimiento real. |
| C3: importación sin RF; supresión mal trazada; RF07/12 compuestos | Se agregan RF18 importación controlada y RF19 supresión; RF07a guardar/RF07b retirar; RF12a editar prioridades/RF12b recalcular comparación. RB10 → RF19. | Se conservan IDs originales para rastrear E1; los sufijos delimitan contratos, no borran la historia. | catalogue.py, importar_catalogo.py; rutas y pruebas RF07a/b, RF18, RF19. |
| C4: umbrales arbitrarios | R04 ≤ 1 % se deriva de presupuesto de 1 operación fallida por 100 en sesión; D01 se redefine para ventana publicada de demostración/piloto; M01 exige 100 % de reglas críticas y 80 % de ramas por riesgo; P02 ≤ 30 min se deriva de bloque de preparación de clase. | Los valores siguen siendo presupuestos de diseño, no leyes ni observaciones de una escuela. Se exige medición y ajuste si hay desvíos. | Tabla RNF objetivo/método/resultado/veredicto. Se conserva E1 inmutable. |
| C5: origen techo RC01; calendario RC02 | RC01: límite interno de caja del equipo, no financiamiento aprobado por colegio. RC02: MVP objetivo S13, E3 S14 y cierre E5 S17–18. El corte actual S15 documenta atraso. | 400 HH + 100 de reserva se mantiene como plan, no horas trabajadas. | SRS §2.6, costos y replanificación. |
| C7: valores hora y hosting sin fuente | Se elimina diferencia salarial arbitraria por rol. Costo de oportunidad referencial uniforme: rango público UdeC/MiFuturo 2,5–3,0 MM mensuales / 182 h = 13.736–16.484 CLP/h. Caja incremental de esta ejecución: 0, hardware existente; no se contrata hosting. | El techo de 100.000 y presupuesto original se preservan como línea base; no se confunden con gasto. El rango es sensibilidad académica, no cotización profesional. | Costos_Riesgos_Plan.md; UdeC y DT 42 h. Historial HH humano no aportado. |
| C8: Anexo F equivocado | El nuevo Anexo F identifica la propuesta aprobada como evidencia no recibida, y conserva la fundamentación como documento distinto. | No se fabrica firma/constancia docente. | SRS §13–14: aprobación pendiente de adjunto real. |
| C8: remisión C02 a §2.4 | La remisión se corrige a §1.2 Alcance y exclusiones. | Se conserva la numeración IEEE 830. | SRS actualizado. |
| C8: diccionario Q13 apoderados | Se corrige la semántica: Q13A es disposición monetaria declarada, no escala ordinal 1–5. Se conservan los 8 códigos históricos y se marca solapamiento/ambigüedad de respuestas exactas/rangos. | No se recodifican las 36 respuestas sin formulario original; no se obtiene precio ni promedio de esta variable. | Anexo A del SRS: 0 = 15–30 mil, 1 = $0, 2 = 30–50 mil, 3 = $15 mil, 4 = 5–15 mil, 5 = $30 mil, 6 = $5 mil, 7 = > $50 mil. |

### Respuesta a la PDR / oral 1

Puntajes aportados: C1 = 3,00; C2 = 3,50; C3 = 3,00; C4 = 3,50; C5 = 3,50; C6 = 3,00; C7 = 2,50; P = 3,19; nota 5,4. Se conserva el dato tal como se recibió, sin recalcularlo con redondeos de la tabla visible. Acciones para E3: elegir el problema y límites en 60 s, mostrar el sistema real, respaldar arquitectura con CI1/CI2 y mediciones, reemplazar láminas densas por resultados verificables, ensayar con cinco voces y demo acotada. Son decisiones del equipo asistidas por IA; no son citas de la profesora. Falta adjuntar cualquier comentario cualitativo adicional de la PDR si existiera.

### Iteración I1 · Del blob PoC al modelo relacional integrado

Disparador: revisión docente C3 y evidencia de PoC con guardados/par en un único JSON; no podía verificar importación ni supresión del producto. Alternativas: conservar todo en JSON; usar modelo relacional normalizado; separar microservicios. Decisión: Django con claves, FK, UNIQUE, CHECK y transacciones. Se mantienen el monolito y el recorrido de E2 por su tamaño/costo; se descartan microservicios por complejidad operativa.

Efecto verificado: lote repetido mantiene número de ofertas; lote duplicado falla sin efectos; guardado repetido no duplica; autocomparación falla en BD; supresión del titular elimina dependencias y conserva catálogo. Evidencia: la suite tests/test_workflow.py y migración 0001. Esta es una iteración estructural de diseño, no solo avance de implementación.

### Iteración I2 · Procedencia por campo y faltantes seguros

Disparador: catálogo 2027 era precondición sin proceso de carga; páginas públicas mezclan admisión 2027 con arancel 2026/indicadores sin cohorte. Alternativas: rellenar con estimación; incorporar todas las cifras como 2027; publicar únicamente campos verificables y señalar faltantes. Decisión: snapshot de 91 ofertas con código, campus, ciclo, fuente, página y hash; 3 duraciones de páginas oficiales con límite de vigencia; sin arancel/empleabilidad cuando período no es comprobable. Se conserva comparación sin ganador.

Efecto verificado: 91 códigos/ciclo únicos y 3 campus; importador valida dominio, fecha, hash, código, ciclo y duplicados antes de la transacción; comparación no convierte NULL en 0 y rechaza períodos incompatibles. Evidencia: data/catalogo_udec_2027.json, datos curados y pruebas RF05/06/09/10/18. Sacrificio: menos cifras; beneficio: no presentar datos incompatibles como comparables.

### Iteración I3 · Integración real de formularios y CSRF

Disparador: backend pasaba, pero Chromium devolvió 403 al crear la cuenta. Inspección del POST: Origin:null con Referrer-Policy:no-referrer; Django rechazó el origen. Alternativas: excluir CSRF o aceptar origen nulo; conservar validación y usar política same-origin. Decisión: política same-origin, sin modificar CsrfViewMiddleware ni decoradores de mutación.

Efecto inicial observado: el mismo alta cambió de 403 a 302 y llegó al proceso. Verificación posterior: E2E completo en dos navegadores y suite CSRF con token ausente 403. La evidencia negativa se registra en Defectos.csv. No se califica como explotación: fue un fallo de compatibilidad que bloqueaba una acción legítima.

### Tres intercambios defendibles

1. Se sacrifica completitud numérica para conservar procedencia/período y evitar inferencias falsas.
2. Se sacrifica escalado multiinstancia inmediato para lograr instalación local, control de datos y demo sin terceros; SQLite se evalúa con carga, PostgreSQL queda condicionado.
3. Se sacrifica un puntaje vocacional atractivo para proteger agencia del estudiante: ficha autodescriptiva sin baremos, diagnóstico ni ranking.

---

## Trazabilidad del sistema E3

Problema y evidencia: SRS §2.3, encuesta E1 reanalizada y fuentes públicas. Los RF01–11 originales tienen recorrido funcional; RF07 se dividió; RF18/19 agregan los contratos faltantes. RF12a/b y RF13 están disponibles; RF14 queda fuera y RF15–17 se mantienen excluidos. Implementado no significa validado con usuarios.

| RF | RB | RNF asociados | Componente | Prueba propietaria ejecutada |
| --- | --- | --- | --- | --- |
| RF01 | RB08 | S01, S02 | views.account / Process | test_RF01_create_return_without_civil_identifier |
| RF02/03 | RB02, RB09 | S01, U02, M01 | InterestResponse / domain.summarize | test_RF02_RF03_complete_versioned_interests_survive_logout |
| RF04/12a/12b | RB06 | S02, U02 | Priority / comparison | test_RF04_priorities_remain_undefined_until_declared |
| RF05/06 | RB03, RB04 | R01, R03, C02 | Offer / Datum / Source | test_RF05_RF06_catalogue_filters_and_provenance |
| RF07a/07b | RB08 | S02, R02 | SavedOffer | test_RF07a_RF07b_idempotent_save_and_remove |
| RF08 | RB05 | M01 | PairForm / Comparison | test_RF08_duplicate_or_missing_pair_cannot_replace_valid_pair |
| RF09/10 | RB01, RB04, RB07, RB09 | U01, M01 | domain.compare / comparison.html | test_RF09_RF10_missing_fields_and_priorities_without_winner |
| RF11 | RB08 | S01, S02, D02 | own_process / sesiones | test_RF11_no_cross_owner_read_or_delete; test_RF11_edit_uses_authenticated_owner_even_with_foreign_identifier |
| RF18 | RB03, RB04 | C02, M01 | catalogue.import_catalogue | test_RF18_catalogue_atomic_rejection_and_repeatable_import; test_RF18_source_revisions_do_not_overwrite_existing_provenance |
| RF19 | RB10 | S02, S05 | delete_process / CASCADE | test_RF19_own_confirmed_deletion_cascades |

RB01/02/09 también requieren revisión de contenido y comprensión humana: la ausencia de un ganador no demuestra que un estudiante interprete correctamente la ficha. El E2E cubre transporte, navegación, persistencia y borrado en dos familias, sin duplicar los invariantes de BD que pertenecen a la suite de integración. Los casos de nonces/AAD/integridad pertenecen a CI2; las restricciones de claves/foreign keys a CI1. Cobertura de ramas se mide con coverage, no se infiere del número de requisitos.

### Matriz de siete artefactos de diseño

| Artefacto exigido | Ubicación sustantiva |
| --- | --- |
| Problema y stakeholders | SRS §2.3–2.4; Fuentes_Publicas; Encuestas_Reanalisis |
| Especificación y priorización | SRS §3–4 y §9.1 |
| Modelos, cálculos y ciencias | docs/modelos DOT/SVG/PNG; Ciencias_Ingenieria |
| Tres alternativas | SRS §8 y antecedente Dossier_E2_Completo |
| Matriz ponderada | docs/antecedentes/Matriz_Decision_E2.csv; fundamento E2 conservado |
| Riesgos actualizados | Costos_Riesgos_Plan, 10 riesgos con disparador/gestión |
| Tres intercambios | Respuesta_Docente_Iteraciones, beneficio/sacrificio/condición |

---

## Modelo de datos y ciencias de la ingeniería

### CI-1 · Dependencias funcionales y 3FN

Compromiso E1, tabla 8, p. 9: modelar entidades, claves, dependencias y normalizar; verificar anomalías en el sistema construido.

La relación universal U(código, ciclo, carrera, campus, URL, fecha, hash, página, dimensión, valor, unidad, período, proceso, titular, ítem, respuesta, prioridad, guardado) duplicaría fuentes e identidad en cada respuesta y dato. Produce anomalías: corregir una URL exige modificar muchas filas; no se puede registrar una fuente sin inventar una respuesta; borrar el último guardado podría borrar información académica. Se descompone en las relaciones siguientes, implementadas por migración real.

| Relación | Clave candidata | Dependencia no trivial |
| --- | --- | --- |
| Campus | id; nombre | id → nombre |
| Career | id; nombre | id → nombre |
| Source | id; (URL, hash) | id → URL, título, fecha, hash |
| Offer | id; (código, ciclo) | id → carrera, campus, fuente, página, activo |
| Datum | id; (oferta, dimensión) | oferta, dimensión → valor, unidad, período, fuente |
| Process | UUID; propietario | UUID → propietario, versión, fechas |
| InterestResponse | id; (proceso, ítem) | proceso, ítem → valor_cifrado |
| Priority | id; (proceso, dimensión) | proceso, dimensión → nivel |
| SavedOffer | id; (proceso, oferta) | proceso, oferta → asociación |
| Comparison | id; proceso | proceso → ofertaA, ofertaB |
| AuditEvent | id | id → tipo, fecha, correlación |

Bajo estas dependencias declaradas, todo determinante no trivial es una superclave: las relaciones cumplen BCNF y, por implicación, 3FN. No se afirma que una prueba automática demuestre normalización. El razonamiento depende de que nombre sea único en el catálogo acotado UdeC; otra universidad exigiría una clave institución + código de carrera. El valor cifrado es un atributo atómico del almacenamiento lógico; no se consulta internamente con SQL.

Descomposición sin pérdida: cada unión con tabla maestra comparte su clave, por ejemplo Offer ∩ Source = {source_id}, que determina Source; en ese paso se satisface el criterio de unión sin pérdida. Todas las dependencias declaradas quedan dentro de una tabla. Las restricciones UNIQUE impiden asociación y respuesta duplicadas; CHECK impide la autocomparación; FK PROTECT conserva fuentes y carreras referidas; CASCADE elimina datos dependientes del titular.

Resultado observado: pruebas test_CI1_database_blocks_duplicates_and_self_comparison, test_RF18_catalogue_atomic_rejection_and_repeatable_import y test_RF19_own_confirmed_deletion_cascades. La misma migración crea el esquema usado por el navegador. Efecto: importación repetible sin duplicados, rechazo completo de lotes corruptos, supresión sin borrar el catálogo público.

### CI-2 · Autenticidad e integridad

Compromiso E1: credenciales, acceso y cifrado. Modelo: atacante conoce UUID ajeno, manipula token/respuesta o recupera una copia del archivo de respuestas; no controla el sistema operativo ni la clave privada del servidor. Las contraseñas usan el hasher adaptativo PBKDF2 de Django; no se cifran reversiblemente. La sesión de 30 min se valida en servidor; la identidad autenticada se usa en todas las consultas al proceso. CSRF verifica las mutaciones desde navegador.

Para cada respuesta se calcula (C, T) = AES-256-GCM(K, N, M, A), K privada de 32 bytes, N aleatorio de 12 bytes, M = respuesta 1..5 y A = UUID:ítem:versión. El almacenamiento es N||C||T. Cambiar C, T o A invalida la etiqueta y produce un fallo cerrado. Asociar A evita transplantar una respuesta válida a otro titular/ítem. Para n respuestas con nonce aleatorio de 96 bits, la cota de colisión aproximada es n(n−1)/2^97: con 360 × 12 = 4320 respuestas es aproximadamente 1,18 × 10^-22 por clave. La cota no justifica reutilizar nonce ni operar indefinidamente con una misma clave.

Pruebas: credencial válida/incorrecta/caducada; lectura y supresión ajena; nonces distintos con igual mensaje; manipulación de etiqueta; cambio de UUID e ítem; contenido alterado devuelve 503 sin resultado; CSRF ausente devuelve 403. La suite y el E2E son evidencia reproducible, no certificación criptográfica.

Aprendizaje: se contrastaron documentación oficial de Django 5.2, API AESGCM de cryptography y NIST SP 800-38D. La comprensión se verificó con controles negativos (cambio de AAD e integridad), no solo con un roundtrip cifrar/descifrar. Persisten límites: el cifrado de respuestas no cifra todo SQLite, prioridades ni respaldos; no hay TLS público ni KMS. Este entorno admite únicamente datos de prueba. RNF-S03 requiere cierre antes de datos reales.

### Dimensionamiento y complejidad

Escenario declarado: 8 cursos × 45 = 360 procesos; clase 45 + 5 de margen = 50 sesiones. 45 se contrasta con el límite reglamentario del Decreto 8144; no demuestra matrícula de un establecimiento. El 8 es un supuesto del escenario. El snapshot del catálogo contiene 91 códigos distintos con campus/ciclo; se cotejan contra las páginas 294–300 del PDF 2027. Se generaron 360 procesos sintéticos para carga, no estudiantes reales.

La comparación recorre un conjunto fijo de 3 dimensiones numéricas más ubicación: O(d) en tiempo y memoria, sin suma de conveniencia. La restricción UNIQUE(proceso, oferta) en Guardados evita la duplicación; la búsqueda usa el catálogo acotado de 91, por lo que no se justifica Elasticsearch. La base SQLite simplifica el entorno local; la carga decide si satisface el escenario limitado. Escalar a varios servidores o escrituras intensivas implica evaluar PostgreSQL, no afirmar equivalencia de motores.

Fuentes técnicas: https://docs.djangoproject.com/en/5.2/topics/auth/passwords/; https://docs.djangoproject.com/en/5.2/ref/csrf/; https://cryptography.io/en/latest/hazmat/primitives/aead/#cryptography.hazmat.primitives.ciphers.aead.AESGCM; https://csrc.nist.gov/pubs/sp/800/38/d/final.

---

## RNF: objetivos, métodos, resultados y veredictos

Corte 16/11/2026. Se preservan los 21 IDs de E1 y se reportan todos, no solo los favorables. Los objetivos son presupuestos de diseño justificados/revisables, no requisitos impuestos por una escuela no inspeccionada. Carga, navegador, CI y validación humana son evidencias distintas. Ver JSON originales para denominadores y versiones.

| ID | Objetivo | Justificación contextual | Método ejecutado / requerido | Valor obtenido | Veredicto y decisión |
| --- | --- | --- | --- | --- | --- |
| RNF-R01 | LCP ≤ 2,5 s; INP ≤ 200 ms; CLS ≤ 0,1, p75 de campo | Web Vitals; objetivo de experiencia, no SLA de servidor | PerformanceObserver en 12 pantallas; laboratorio local, n = 1/ruta/ancho | LCP máximo 48 ms; CLS máximo 0.0126; INP/campo sin muestra | Parcial: no afirmar p75 ni INP |
| RNF-R02 | p95 ≤ 1000 ms, 50 sesiones, 10 min | Presupuesto de 1 s por consulta/guardado repetido en clase de 45+5 | 50 VU autenticados, 70/30, 1 operación/s/VU, runtime aislado | p95 = 697.2 ms; 30000 operaciones | Cumple en local; ver duración exacta en JSON |
| RNF-R03 | 360 procesos y catálogo 2027 completo | 8 × 45 supuesto; snapshot oficial, no 91 carreras asumidas | Creación de 360 procesos; extracción y validación de 91 códigos/campus/ciclo | 360 procesos sintéticos, 91 ofertas, 3 campus | Cumple la capacidad local; pertinencia de atributos limitada |
| RNF-R04 | Fallos ≤ 1 % con 50 sesiones, 70/30, 10 min | Presupuesto máximo 1 fallo/100 operaciones; ajustar tras estudio | Estados HTTP y contrato funcional por operación; sin redirects contados como lecturas nuevas | 0/30000 fallos; 0 HTTP 5xx | Cumple en escenario local |
| RNF-D01 | ≥ 99 % en ventana piloto declarada | No hay horario real de escuela; se retira 22 × 12 como hecho | Requiere monitor continuo y denominador de ventana publicada | No hay período de piloto publicado/observado | No acreditado: una respuesta health 200 no es disponibilidad mensual |
| RNF-D02 | RPO ≤ 24 h; RTO ≤ 4 h | Progreso no transaccional crítico; recuperación en jornada de uso | Snapshot SQLite consistente, AES-GCM, restauración, integrity/FK/check | RTO ejercicio = 0.496 s; snapshot de 0.488 s; 91 ofertas recuperadas | Parcial: RTO local cumple; periodicidad RPO 24 h sin operación |
| RNF-S01 | 100 % de los procesos con auth; caducados denegados | Aislamiento de proceso, potencial NNA | Casos de sesión válida/incorrecta/caducada y logout/login | Suite RF01/RNF-S01; redirige a auth sin revelar proceso | Cumple los contratos probados, no auditoría exhaustiva |
| RNF-S02 | 0 accesos cruzados en lectura/edición/supresión | Cada cuenta solo su proceso | UUID ajeno GET/DELETE; POST con ID ajeno actualiza solo al propietario autenticado | 0 lecturas/borrados cruzados; edición no altera dueño ajeno | Cumple la suite negativa local |
| RNF-S03 | TLS en 100 % y repositorios cifrados antes de datos reales | Privacidad de historial; potencial NNA | Inspección de configuración; pruebas AES-GCM; revisión BD/runtime | HTTP loopback; respuestas cifradas, SQLite/prioridades no cifrados integralmente | No cumple en entorno real: demo solo datos ficticios |
| RNF-S04 | 0 secretos versionados/logs; eventos sin respuestas | Minimización y prevención de exposición | Revisión de archivos Git; runtime ignorado; logs de error con correlación | Claves fuera de Git; no respuestas ni credenciales en eventos; revisión estática | Cumple el alcance revisado; no garantía universal de ausencia |
| RNF-S05 | Finalidad, acceso, retención y supresión de datos reales | Normativa aplicable y derechos | Protocolo, RF19, custodia y purga de respaldos del piloto | Finalidad/minimización/consentimiento propuestos; supresión activa probada | Parcial: sin estudio real ni purga operativa acreditada |
| RNF-U01 | Criterios WCAG 2.1 AA aplicables; analizar 2.2 | Acceso de usuarios heterogéneos | Axe 4.14.1, 12 pantallas, teclado, enlace salta-contenido | 0 violaciones automáticas; incompletos se conservan en JSON | Parcial: lector de pantalla y criterios manuales no acreditados |
| RNF-U02 | ≥ 80 % de participantes completan la comparación sin ayuda | Umbral de la guía del curso; con 5, 4/5 | Protocolo 5 tareas; CSV real y análisis rechaza vacíos | Sin observaciones de usabilidad de E3; encuesta E1 no es sustituto | Pendiente de usuarios externos reales |
| RNF-U03 | Español chileno; 360–1440 px | Dispositivos heterogéneos; caso móvil mínimo | E2E Chromium/Firefox, anchos 360/1440; axe y overflow | 4 recorridos PASS; 0 desbordes generales | Cumple en los anchos probados; zoom/lector manual pendientes |
| RNF-C01 | Flujo en dos familias de navegadores | Evitar dependencia de una familia escolar | Playwright Chromium y Firefox; alta → supresión | 4 recorridos completos PASS; versiones en e2e.json | Cumple en versiones/entorno probados |
| RNF-C02 | URL, ciclo, fecha y unidad en 100 % de los campos externos | Comparación trazable y homologable | Validación snapshot y Datum; PDF 91 ofertas; 3 extractos curados | 273 campos base con metadatos; 3 duraciones, resto NULL; hash scope explícito | Cumple el contrato de metadatos; faltantes se muestran |
| RNF-M01 | 100 % de las RB críticas con caso; ≥ 80 % de ramas críticas | 10 reglas sensibles: integridad, agencia, permisos, datos | Coverage --branch y matriz RB → prueba | 24 tests; líneas 98.34 %; ramas 96.74 %; dominio 91,67 %, importador 100 % | Cumple en módulos críticos y trazabilidad definida |
| RNF-M02 | Cambios integrados con lint/formato/tests | Control de defectos al integrar cinco roles | GitHub Actions por push/PR y checks locales | CI remota 471dc2c success; SHA final se archiva aparte | Cumple con SHA verificado; no inferir futuros SHA |
| RNF-M03 | Errores con fecha/tipo/correlación sin datos | Depurar con privacidad | Fallo 404/503 inducido; header X-Request-ID y log | Correlación 32 caracteres; eventos DB con fecha/tipo; logs de servidor con fecha | Cumple el contrato observado; no observabilidad centralizada |
| RNF-P01 | Entorno reproducible por segundo integrante | Continuidad colaborativa | Runbook + CI limpia; reproducción humana independiente | Instalación CI automatizada pasa; otro integrante no ha registrado instalación | Parcial: CI no equivale a segundo integrante |
| RNF-P02 | Despliegue ≤ 30 min y rollback | Bloque de preparación antes de una sesión de 45 min; no normativa | CI instala, migra, importa, prueba; cronometraje humano/runbook | Pipeline y restauración ejecutados; sin instalación humana cronometrada | Parcial: método listo, segundo operador pendiente |

Los RNF-D01, S03, U02 y P01 no se cierran con simulaciones. Decisión: mantener el entorno académico con datos ficticios y no declarar piloto real autorizado. Los controles automatizados y las mediciones sirven para detectar desvíos, no para sustituir las condiciones humanas/operativas. La carga inicial abarcó 599,78 s de operaciones programadas; se conserva íntegra; la ejecución final sostuvo 600,31 s con 30.000 operaciones para resolver el límite temporal. El reporte final reemplaza solo la tabla de valores, manteniendo la evidencia inicial.

---

## Reanálisis de evidencia real de necesidades

Se reanalizaron los registros desidentificados ya aportados en el SRS E1: 156 estudiantes y 36 apoderados. No se reclutaron nuevos participantes ni se imputaron respuestas. La fuente es el apéndice del informe, no la exportación original; esta limitación permanece.

| Ítem | Interpretación descriptiva | Conteo | Proporción muestral |
| --- | --- | --- | --- |
| Q4 | Indecisión de carrera | 45/156 | 28,8 % |
| Q5 | Varias opciones sin convicción | 50/156 | 32,1 % |
| Q6 | Sensación de decidir a ciegas | 43/156 | 27,6 % |
| Q7 | Temor a equivocarse | 82/156 | 52,6 % |
| Q8 | Autoconocimiento insuficiente | 41/156 | 26,3 % |
| Q9 | Desacuerdo con herramientas suficientes | 52/156 | 33,3 % |

El instrumento contiene escalas ordinales 1–5; se reportan conteos por categorías sin sumar un diagnóstico. Se distinguió la polaridad de Q9. Los códigos monetarios Q13A se conservaron como categorías con solapamientos; no se calculó promedio ni precio. El JSON incluye frecuencias completas y permite contrastar los conteos.

Conclusión de alcance: los datos justifican contrastar necesidades de claridad, información y autoconocimiento en la muestra. No establecen adopción, efectividad, causalidad ni éxito de tareas de la aplicación. Tampoco prueban que otras plataformas sean insuficientes. Para E3 se añade esta auditoría como evidencia histórica de necesidades; la validación de uso de la versión construida requiere sesiones reales con su instrumento, éxito/ayuda/errores/tiempos.

Consecuencia de diseño: mantener agencia del estudiante; no declarar una ganadora; explicar fuentes/faltantes y límites; permitir guardar/retomar. Estos vínculos son hipótesis de requisitos, no preferencias de interfaz demostradas. Ver instrumento y protocolo en Validacion_Usuarios.md.

---

## Validación con usuarios · protocolo listo para ejecución

**Estado: no se aportaron resultados de sesiones reales.** Las encuestas de E1 describen el problema; las pruebas de software, bots y evaluadores de IA no son validación con estudiantes. Este documento prepara el estudio y el análisis sin completar filas ficticias.

### Objetivo y muestra

Establecer si estudiantes del perfil comprenden el propósito, encuentran información y completan la comparación sin ayuda. Muestra intencional de 5 personas ajenas al equipo, preferentemente mayores de 18 años en transición a educación superior. Registrar criterios de inclusión y dispositivo, sin nombre, RUT, correo ni datos sensibles en la planilla. Si solo se consiguen 3 participantes se informa n = 3, sin cambiar el denominador para alcanzar el objetivo. No demuestra representatividad ni reducción de cambios/abandono de carrera.

### Preparación y consentimiento

Antes de contactar: designar responsable humano, habilitar un entorno adecuado al régimen de datos y acordar custodia/retención. La demo actual usa loopback y datos inventados; una prueba local supervisada puede pedir que la persona use una identidad ficticia y respuestas ficticias, pero el registro del estudio sigue requiriendo consentimiento. No usar este entorno para información personal real de menores. Para NNA se revisarán autorización, consentimiento/asentimiento y protocolo institucional antes de la sesión.

Texto propuesto: «Te invitamos a probar una aplicación académica durante 15–20 minutos. Participar es voluntario; puedes omitir preguntas o retirarte. Usarás un alias y respuestas inventadas. Registraremos éxito, tiempo, errores y comentarios anonimizados. No es un test psicológico ni una asesoría de admisión. No grabaremos audio/video ni datos sensibles sin permiso separado. Los datos identificables se eliminarán 30 días después del cierre académico; puedes solicitar el retiro de tu registro mediante el código que recibirás». Completar responsable/canal/fechas reales antes de usar; no inventar firma o aceptación.

### Parte 1 · Concepto y requisitos (5 minutos)

Preguntar, sin inducir respuesta: ¿cómo comparas hoy dos alternativas? ¿Qué información buscas y dónde? ¿Qué entiendes que hará esta aplicación? ¿Qué te preocuparía al guardar tu avance? ¿Qué otra herramienta usarías? Clasificar necesidades, expectativas y malentendidos; contrastar con RF y con soluciones existentes. Registrar verbatim breve con permiso y sin identidad. Separar este estudio de concepto del estudio de tareas, aunque una persona participe en ambos.

### Parte 2 · Tareas de uso (máximo 10 minutos)

T1. Crear un proceso con identidad inventada y completar la ficha con valores de prueba.

T2. Marcar duración como alta y ubicación como media; explicar qué crees que cambia.

T3. Encontrar Informática 13073 y Medicina 13086, revisar fuente/ciclo y guardarlas.

T4. Compararlas. Identificar la diferencia de duración, un dato no disponible y si existe una ganadora.

T5. Salir, retomar con la misma cuenta y comprobar estado. Finalmente localizar la opción de eliminación; ejecutarla solo en la cuenta ficticia propia.

Facilitador: leer la tarea sin indicar qué control usar; iniciar reloj al terminar de leer; parar al criterio de aceptación; registrar ayuda solicitada o entregada. Si intervienes para completar, la tarea no cuenta como éxito sin ayuda. Un error corregido por el propio participante se registra y puede coexistir con éxito sin ayuda. Corte a 10 min; tarea abandonada cuenta como no completada.

### Instrumento de observación

Archivo data/validacion_usuarios.csv, una fila por participante y tarea. Campos: participant_id (P01..P05), perfil, mayor18 (si/no), consentimiento_registrado (si/no), dispositivo, tarea (T1..T5), completada (si/no), ayuda (si/no), segundos, errores, comentario. El CSV entregado solo tiene encabezados. Custodia de consentimientos fuera de Git, con responsable humano. No se recogen contraseñas ni respuestas personales.

### Preguntas finales

¿La ficha te dijo qué carrera elegir? ¿Qué significa un dato no disponible? ¿Cuál es la fuente de la duración? ¿Qué cambiarías primero? ¿En qué parte necesitarías ayuda? Valorar confianza de 1 a 5 solo como descripción, sin convertirla en prueba de precisión del sistema.

### Análisis previsto y regla de decisión

Éxito principal por persona: T4 completada sin ayuda y explicación correcta de ausencia de ganador/faltantes. RNF-U02: al menos 80 %; con n = 5 requiere 4/5, con n = 3 requiere 3/3. Informar numerador, denominador y límites. Por tarea: éxitos, ayudas, errores; tiempos con mediana y rango. Si hay menos de 3 registros externos válidos, el estudio no acredita el criterio. No reemplazar faltantes por éxitos ni excluir abandonos del denominador sin justificarlo.

El análisis se genera con herramientas/analizar_validacion.py, que rehúsa producir resultados si solo hay encabezados. Las conclusiones deben separar observación, interpretación y cambio de diseño. Un comentario aislado orienta una hipótesis; no se generaliza a toda la población. Si menos de 4/5 completan T4 sin ayuda o alguien interpreta el resultado como diagnóstico, se reabre el diseño y se vuelve a probar lo afectado.

### Ficha de infraestructura del escenario

Registrar establecimiento o tipo anónimo, responsable de TI, cantidad de equipos disponibles/simultáneos, navegadores/versiones, conectividad medida en el horario, política de cuentas, disponibilidad de asistencia y ventana real de uso. Anexar método/fecha/autorización. Hasta obtener esta ficha, 8 cursos, 50 sesiones y horario del piloto son supuestos de capacidad, no hechos de un colegio.

### Cierre pendiente

Adjuntar registros reales anonimizados, análisis, decisiones y consentimiento custodiado; revisar entorno y retención; ejecutar ensayo con cinco voces. El agente no puede producir estas evidencias humanas por sustitución.

---

## Costos, riesgos y replanificación E3

Corte: 16/11/2026, semana de referencia S15. La línea base del curso fijaba E3 en S14. El presente trabajo documenta el atraso; no supone una prórroga ni una nueva fecha oficial de entrega.

### Presupuesto estimado y ejecución acreditada

| Partida | Estimado E1 | Ejecutado acreditado en este trabajo | Desvío / interpretación |
| --- | --- | --- | --- |
| Horas del equipo | 400 HH + 100 HH de reserva | Historial humano no aportado | No es posible calcular variación de HH sin bitácoras reales; el tiempo del agente no es HH de cinco personas |
| Valorización del esfuerzo | CLP 9.240.000, tarifas diferenciadas sin fuente | No es gasto pagado | Se reemplaza como estimación defendible por sensibilidad uniforme con fuente pública |
| Hosting/BD | Provisión CLP 30.000 | CLP 0 incremental nuevo | Se usó hardware existente y ejecución local; no se contrató hosting |
| Dominio/DNS opcional | Provisión CLP 15.000 | CLP 0 | Se conserva fuera del alcance; localhost no lo requiere |
| Logística de validación | Provisión CLP 20.000 | No se aportaron gastos históricos; ninguna compra nueva | No se contabiliza una validación no realizada |
| Contingencia/licencias | Provisión CLP 35.000 | CLP 0 incremental nuevo | Dependencias libres; no se compró instrumento propietario ni servicio |
| Caja máxima | CLP 100.000 | CLP 0 de desembolsos nuevos por estas acciones | El techo es un acuerdo/presupuesto interno de E1, no financiamiento institucional demostrado |

La ejecución local consume equipo, energía y acceso ya disponibles; no se declara costo económico total cero. No se compraron productos ni se amplió ningún plan. El uso de herramientas del agente no acredita la ausencia de un costo de suscripción preexistente, que no se asigna al proyecto sin respaldo.

### Corrección de la valorización horaria

Se retira el diferencial no fundamentado de CLP 20.000–27.500 por rol. Referencia: Admisión UdeC cita MiFuturo para Informática y publica un rango de ingreso al 4.º año de CLP 2,5–3,0 millones mensuales. DT documenta jornada de 42 h/semana desde el 26/04/2026. Se adopta 182 h/mes = 42 × 52 / 12 solo como conversión de sensibilidad.

Tarifa referencial = ingreso mensual / 182: CLP 13.736–16.484 por hora (redondeo al peso). Para 400 HH: CLP 5.494.400–6.593.600, más desembolsos que se acrediten. Todos los roles usan el mismo rango para evitar aparentar salarios de mercado por especialidad sin fuente. La referencia es un ingreso de egresados, no honorario cotizado; no incluye impuestos/costos de contratación. No se usa como remuneración pagada ni compromiso comercial.

Costo futuro: no hay operación contratada ni responsable aceptado. Alternativa A, mantener demo local: recursos existentes y horas que el responsable debe acordar. Alternativa B, servicio público: cotizar infraestructura, TLS/almacenamiento cifrado, respaldo, monitoreo y mantención antes de asumir caja mensual. La proyección E1 de CLP 123.250/mes no se presenta como precio confirmado. Los beneficios potenciales de claridad/tiempo se validan con personas; no se monetiza retención evitada sin evidencia causal.

### Riesgos actualizados

La probabilidad y el impacto A/M/B son juicios de diseño, no frecuencias observadas. El campo «Responsable» indica el rol que debería coordinar la respuesta, no una aceptación personal inventada.

| ID / categoría | Riesgo y disparador | P / I | Gestión aplicada o acción | Estado y residual | Rol |
| --- | --- | --- | --- | --- | --- |
| R01 datos | Catálogo o atributos mezclan períodos; aparece dato sin ciclo/cohorte | A/A | Snapshot 2027, 91 códigos; campos no verificados quedan ausentes; fuente por campo | Materializado: páginas sin vigencia explícita. Residual: 3 planes requieren confirmación 2027 | Datos |
| R02 validación | No hay sesiones externas de uso al corte | A/A | Reanálisis real de encuestas E1; protocolo/planilla/análisis preparados para uso | Abierto: encuesta no demuestra usabilidad/adopción | QA / gestión |
| R03 legal/ética | Se pretende usar datos de menores sin protocolo/entorno cerrado | M/A | Demo sintética, sin RUT; gates de TLS/cifrado/consentimiento | Abierto: no habilitar el piloto por existir una demo | Datos/privacidad |
| R04 técnica | SQLite bajo 50 sesiones presenta bloqueos o p95 > 1 s | M/A | Transacciones, índices/constraints; carga 50/360/70-30 durante 10 min | Medición local archivada; si falla, reducir escritura o evaluar PostgreSQL y repetir | Arquitectura |
| R05 seguridad funcional | Formulario legítimo devuelve 403 | M/A | Se reprodujo Origin:null; política same-origin conserva CSRF | Materializado y corregido; E2E/CSRF negativos posteriores | Arquitectura/QA |
| R06 terceros | Páginas oficiales rechazan descarga o cambian | A/M | Fuente PDF descargada y hash; lectura alternativa de extractos verificables | Materializado 403 en HTML; no depender de red durante demo | Operación/datos |
| R07 equipo | Contribución/HH/actas distribuidas sin evidencia | M/A | Separar asignación de autoría; guion por roles; plantillas sin firmas falsas | Abierto: no se crean commits a nombre de otros | Gestión |
| R08 calendario | E3 llega después de S14 o demo consume el tiempo | A/A | Guion 10 min, reserva técnica, excluir Could/Won't, recuperación local | Atraso documental materializado; fecha oficial debe constar en LMS | Gestión |
| R09 accesibilidad | Etiqueta visible no coincide con nombre accesible | M/M | Axe detectó label-content-name-mismatch; se conserva texto visible en aria-label | Materializado y corregido; 0 hallazgos automáticos en 12 pantallas, manual pendiente | QA |
| R10 continuidad/costo | No se acuerda responsable/postsemestre | M/A | No contratar; runbook local, retiro/eliminación y cotización previa | Abierto: demo académica no acredita operación permanente | Operación |

### Replanificación y criterio de recorte

| Ventana de referencia | Compromiso propuesto | Dependencia | Coordinación propuesta | Criterio de salida / holgura |
| --- | --- | --- | --- | --- |
| S15, corte actual | Código, RF18/19, catálogo, 2+ iteraciones, pruebas/RNF y paquete E3 | Fuentes y comentarios ya aportados | Benjamín + QA | Flujo local y CI verificados; margen para defectos bloqueantes |
| S15–16 | Validación externa con instrumento; control de entorno y protocolo | Usuarios/consentimiento y responsable real | Diego + Mauro | Evidencia real y conclusiones; si falta, no declarar éxito |
| S16 | Cerrar Must y defectos; verificar accesibilidad manual y segundo operador | Pruebas y hallazgos | Equipo | Sin bloqueantes; repetir solo lo afectado |
| S17 | Informe E4, proveniencia, costos ejecutados y continuidad | Evidencias consolidadas | Jorge + Lucas | Revisión cruzada y entrega oficial |
| S17–18 | Ensayo cinco voces y demo E5 | Must estable, respaldo, comprensión | Todos | 15 min E5 + preguntas según guía; E3 se mantiene 10 + 5 |

Son propuestas de coordinación, no horas ya trabajadas ni tareas aceptadas por personas. Se deja fuera RF14 (exportación), panel institucional, chat IA, ranking y expansión a otras instituciones. Criterio: priorizar recorrido verificable, derechos y calidad antes de nuevas funciones. Si no hay responsables para un piloto, se entrega demo local y plan de retiro; no se improvisa operación con datos reales.

---

## Guion de demostración en vivo · 2 minutos 30 segundos

### Preparación antes de la exposición

1. Ejecutar instalación, migraciones, importación y enriquecimiento según README. Verificar /health/ y abrir http://127.0.0.1:19039/acceso/. Utilizar una cuenta ficticia y una contraseña distinta de las personales.
2. Dejar disponible una segunda ventana para comprobar retorno. Si se precargan las 12 respuestas, declararlo al comenzar. Conservar las credenciales solo en almacenamiento privado local, nunca en las diapositivas ni en Git.
3. Verificar filtros 13073 y 13086, prioridad de duración, comparación y página del PDF. Mantener descargada la fuente para no depender de internet.
4. Probar el proyector, tamaño del texto y foco de teclado. Cerrar pestañas ajenas y consolas con información privada. Abrir la presentación y tener el dossier como respaldo.

### Ejecución cronometrada

| Intervalo | Acción real | Qué decir y comprobar |
| --- | --- | --- |
| 00:00–00:20 | Entrar o retomar cuenta ficticia | Alias sin RUT; proceso propio. Si está precargado, decirlo |
| 00:20–00:40 | Abrir intereses y resumen | Ficha original v1, 12 ítems; promedio autodescriptivo y límites |
| 00:40–01:00 | Guardar duración alta y ubicación media | Prioridades explícitas; las restantes siguen sin definir |
| 01:00–01:25 | Filtrar 13073 y 13086; revisar fuente y guardar | Código, campus, ciclo y procedencia; guardar no duplica |
| 01:25–01:55 | Elegir par distinto y comparar | Duraciones 10/14; diferencia 4 semestres; faltantes no son 0; sin ganadora |
| 01:55–02:15 | Salir, retomar y volver a comparación | Persistencia real de par y prioridades |
| 02:15–02:30 | Mostrar supresión; cancelar o confirmar cuenta propia | Control del titular; nunca borrar cuentas ajenas |

Las credenciales, claves y tablas privadas no forman parte de la presentación. Las pruebas de manipulación y permisos están archivadas; no hace falta improvisarlas durante la exposición. La demostración usa el servicio local y el catálogo descargado.

### Contingencias

Si aparece un error de campo, corregirlo sin reiniciar todo el proceso y explicar la validación. Si se olvida la contraseña ficticia, usar una cuenta de respaldo comprobada o crear otra y declarar la contingencia. Si cae el servidor, ejecutar el script local y verificar /health/. Si la recuperación consume el tiempo, continuar la explicación y aplicar la contingencia que autorice la docente: una captura o video no sustituye por defecto el software en ejecución. Si una fuente remota falla, abrir el PDF conservado y su página; el catálogo local sigue funcionando.

### Respaldo y restauración

El ejercicio herramientas/medir_restauracion.py trabaja sobre una copia temporal consistente, verifica integridad del cifrado, integrity_check, foreign keys y Django.check. No restaura sobre cuentas vivas. No demuestra periodicidad de 24 horas: para un piloto se debe implementar y probar retención, supresión tras restauración y custodia de claves.

### Registro de ensayo

Completar solo después de un ensayo real: fecha, participantes, duración observada, incidencias, recortes y responsable. El E2E automático demuestra funcionamiento, no fluidez de una exposición humana.

---

## Declaración de uso de IA y procedencia

### Uso de asistencia generativa

Este paquete fue preparado con Codex como agente principal, que diseñó, implementó, integró y verificó el sistema y sus entregables. Se usaron subagentes Paseo con perfiles configurados: Go · DeepSeek · Max para inventario y corrección de texto; Codex · Sol · Max para el exportador Markdown→DOCX/PDF. Sus resultados se revisaron antes de integrarlos. La aceptación y evidencia constan en evidencia/delegacion.json. El tiempo del agente y de revisión no se presenta como horas humanas del equipo ni como ahorro neto de cuota.

Las partes asistidas incluyen código, pruebas, scripts de medición, revisión de fuentes, síntesis, diagramas, SRS, presentación y guiones. La responsabilidad académica de revisar, comprender, adaptar y defender el material sigue en el equipo. Los nombres de los integrantes provienen de E1 y no atribuyen automáticamente autoría de cada archivo ni participación en esta ejecución.

No se generaron encuestas, entrevistas, respuestas de usuarios, firmas, aprobaciones ni reuniones ficticias. Las cuentas y respuestas usadas en las pruebas del software son datos sintéticos identificados como tales. Las encuestas analizadas provienen del apéndice desidentificado de E1 y mantienen su limitación de procedencia.

### Material recibido y reutilizado

Repositorio antecedente: ba-hc/orienta-grupo9, main a92f1fd3cfea061543cf14557320120793b32eb1. El pull confirmó que estaba actualizado. Los cambios locales previos se preservaron y respaldaron fuera del proyecto nuevo. SRS E1, documentos del curso y comentarios docentes se conservan con fecha y fuente. La plantilla IEEE830 y la rúbrica fueron aportadas por el usuario. No se impone una licencia abierta a los documentos académicos originales.

Marca UdeC: SVG/PNG y tipografías provenientes del paquete de identidad E2, cuyo registro remite a Normas Gráficas UdeC. Uso de identificación académica; no implica patrocinio ni aprobación institucional. Se conserva la marca sin modificar y con su proporción. Tipografías Poppins y Roboto: licencias OFL originales incluidas en docs/identidad/fuentes. No se descargaron nuevas imágenes comerciales.

Catálogo2027: PDF oficial DEMRE/Mineduc, conservado con SHA256. Las91 filas son una extracción de código, nombre, campus y ciclo; fecha/página permiten cotejo. Las3 duraciones usan extractos curados verificados de páginas oficiales UdeC; el hash del extracto no se presenta como hash del HTML. Información pública no equivale a licencia comercial de redistribución irrestricta; el repositorio es privado y cita la fuente.

Ficha de exploración:12 enunciados originales de este paquete, licencia propuesta CC BY4.0 para el texto; no constituye prueba de validación psicométrica. Las preguntas del estudio académico se distinguen de un instrumento profesional adquirido. No se copió VocationOne ni se afirmó autorización de su API.

### Dependencias y licencias principales

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
