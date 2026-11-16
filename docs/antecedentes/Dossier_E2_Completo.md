# Orienta · Dossier completo E2 / Avance oral 1

Proyecto Informático · Ingeniería Civil Informática · Universidad de Concepción · Grupo 9.

**Versión de diseño: 26/10/2026.** El paquete desarrolla los siete criterios R2 (rúbrica pp. 4–5), con una exposición propuesta de 10 minutos y material de respaldo. E2 es la revisión preliminar de diseño, llamada avance oral 1; E3 es el siguiente avance oral. Las dos denominaciones no son dos entregas distintas.

Se completa el material de los cinco roles por encargo de Benjamín. Los nombres indican quién lo presenta y coordina; no prueban autoría previa, aprobación conjunta ni reuniones realizadas. La selección ALT-1 corresponde al diseño de este paquete y puede revisarse con evidencia del equipo/docente. La fluidez, participación y duración reales dependen de la defensa humana y no se certifican con un PPT.

## 1. Problema, valor y escenario (C1)

Estudiantes de 3.º y 4.º medio enfrentan una decisión con intereses poco estructurados e información académica distribuida. En la encuesta inicial de mayo de 2026, 82 de 156 respuestas válidas (52,6 %) muestran alta identificación (4–5) con el miedo a equivocarse y 45 de 156 (28,8 %) con la frase «aún no sé qué carrera estudiar». Se documentaron además 36 respuestas de apoderados. La muestra es no probabilística; no estima prevalencia nacional, demanda comercial ni eficacia del software.

Orienta conecta exploración de intereses, prioridades personales y datos académicos verificables para guardar opciones, comparar exactamente dos ofertas distintas y recuperar el propio proceso. Apoya la reflexión y la conversación con familia/orientación. No entrega una carrera ganadora, un porcentaje de compatibilidad, un diagnóstico ni un chat generativo.

El piloto propuesto usa ofertas UdeC de admisión 2027. Carrera y oferta se separan: una carrera puede tener ofertas diferentes por campus, código oficial y ciclo. Las 91 carreras de la referencia no demuestran que existan exactamente 91 ofertas. Los 360 usuarios y 50 concurrentes son escenarios de diseño de E1, no matrícula ni tráfico observados.

### Cinco requisitos que gobiernan decisiones

| Requisito | Decisión derivada | Restricción / consecuencia |
| --- | --- | --- |
| RF-02: intereses con instrumento autorizado | Versionar instrumento/ítems y preservar condiciones de uso | RC-03: licencia y pertinencia se verifican antes de usar ítems reales |
| RF-06: detalle con origen y vigencia | Fuente, definición, unidad, período y revisión por dato | RC-07: carga revisada; no copiar cifras de otro ciclo |
| RF-09: comparación factual | Dos revisiones de ofertas distintas; validar compatibilidad | No restar unidades/períodos incompatibles ni reemplazar faltantes por cero |
| RF-10: explicación sin veredicto | Reglas deterministas y razones por campo/prioridad | Sin ranking global ni predicción individual |
| RF-11: recuperación propia | Titular lógico, sesión y autorización de cada proceso | RNF-S01/02/03: acceso y cifrado; un ID opaco no anonimiza |


RF-01…RF-11 continúan como Must. Seleccionar cinco para explicar el diseño no desprioriza el resto. RC-01 limita la caja a CLP 100.000; RC-02 el semestre; RC-06 la mantenibilidad por cinco personas. RC-04 (usabilidad) y RC-05 (accesibilidad) siguen vigentes: prototipo en español, teclado, estados explícitos y diseño móvil.

## 2. Dominio, datos y ciencias de la ingeniería (C2)

### 2.1 Modelo del dominio

El titular lógico posee procesos; cada proceso agrupa aplicaciones de instrumentos, prioridades, ofertas guardadas y comparaciones. Una aplicación referencia una versión de instrumento y sus respuestas. El catálogo distingue institución, campus, carrera y oferta. Las revisiones de oferta reúnen observaciones con procedencia; una comparación conserva dos revisiones para mantener el contexto del dato utilizado.

![Modelo del dominio, relaciones y multiplicidades](modelos/Dominio.png)

La cardinalidad 0..* permite procesos iniciados sin respuestas ni guardados. Una comparación contiene dos extremos obligatorios distintos. Un orientador y un apoderado son actores indirectos, sin cuenta o acceso al proceso por defecto. El mantenedor valida el catálogo por una herramienta interna; no se agrega un panel público no comprometido.

### 2.2 Modelo lógico y diccionario

![Modelo relacional, claves y relaciones](modelos/Modelo_Logico.png)

DDL reproducible: modelos/esquema_logico.sql. Es el modelo objetivo E2 comprobado en SQLite con claves foráneas activas; no es una migración PostgreSQL ejecutada. La PoC tiene una representación JSON simplificada distinta. La autenticación referencia el subsistema de credenciales, sin guardar contraseña en texto plano en titular.

| Relación | Clave primaria | Atributos / tipo de comprobación |
| --- | --- | --- |
| aplicacion | id | id:TEXT; proceso_id:TEXT; version_id:TEXT; estado:TEXT |
| campus | id | id:TEXT; institucion_id:TEXT; nombre:TEXT |
| carrera | id | id:TEXT; nombre:TEXT |
| catalogo_version | id | id:TEXT; etiqueta:TEXT; creado:TEXT |
| comparacion | id | id:TEXT; proceso_id:TEXT; revision_a:TEXT; revision_b:TEXT; creado:TEXT |
| criterio | codigo | codigo:TEXT; nombre:TEXT |
| dato | id | id:TEXT; revision_id:TEXT; definicion_codigo:TEXT; periodo:TEXT; unidad:TEXT; valor:NUMERIC; estado:TEXT; fuente_id:TEXT |
| definicion | codigo | codigo:TEXT; nombre:TEXT; significado:TEXT |
| fuente | id | id:TEXT; url:TEXT; titulo:TEXT; consultado:TEXT; hash_documento:TEXT |
| guardado | proceso_id, oferta_id | proceso_id:TEXT; oferta_id:TEXT; creado:TEXT |
| institucion | id | id:TEXT; nombre:TEXT |
| instrumento | id | id:TEXT; nombre:TEXT; fuente:TEXT |
| instrumento_version | id | id:TEXT; instrumento_id:TEXT; version:TEXT; idioma:TEXT; licencia_url:TEXT; permiso:TEXT |
| item | id | id:TEXT; version_id:TEXT; codigo:TEXT; minimo:INTEGER; maximo:INTEGER |
| oferta | id | id:TEXT; carrera_id:TEXT; campus_id:TEXT; codigo_oficial:TEXT; ciclo:INTEGER |
| oferta_revision | id | id:TEXT; oferta_id:TEXT; catalogo_id:TEXT |
| prioridad | proceso_id, criterio_codigo | proceso_id:TEXT; criterio_codigo:TEXT; nivel:INTEGER |
| proceso | id | id:TEXT; titular_id:TEXT; estado:TEXT; creado:TEXT |
| respuesta | aplicacion_id, item_id | aplicacion_id:TEXT; item_id:TEXT; valor:INTEGER |
| titular | id | id:TEXT; referencia_credencial:TEXT |


Todas las referencias declaradas son claves foráneas. Claves candidatas adicionales: referencia_credencial; (instrumento, versión, idioma); (versión, código de ítem); (institución, nombre de campus); (campus, código oficial, ciclo); etiqueta de catálogo; (oferta, catálogo); (revisión, definición, período). Ver DDL para CHECK y UNIQUE completos. Fechas se serializan ISO en la comprobación SQLite; en PostgreSQL se propone timestamp with time zone, UUID y numeric de precisión definida según el campo. Esta correspondencia requiere una migración propia en E3.

### 2.3 CI-1: dependencias funcionales y 3FN

Supuestos: un campus pertenece a una sola institución; el código de una oferta se interpreta dentro del campus/ciclo; cada observación tiene un significado explícito; un instrumento versionado conserva sus ítems. Se valida ese supuesto antes de cargar otra institución o régimen de códigos.

La forma inicial Oferta(campus_id, institución_id, institución_nombre, carrera, código, ciclo, valor, fuente, respuestas...) mezcla grupos repetidos y dependencias. Si cambia el nombre de institución habría que cambiar muchas filas, con riesgo de contradicción; no se podría registrar una institución sin crear una oferta. Las respuestas repetidas tampoco son un atributo atómico de una oferta.
| Dependencia funcional | Descomposición / efecto |
| --- | --- |
| campus_id → institución_id, nombre_campus; institución_id → nombre_institución | Institución y campus propios; oferta solo referencia campus. Elimina dependencia transitiva |
| (campus_id, código_oficial, ciclo) → oferta_id, carrera_id | Clave candidata UNIQUE de oferta; carrera separada del lugar/ciclo |
| (aplicación_id, ítem_id) → valor | Respuesta con clave compuesta; sin listas ni datos del instrumento repetidos |
| (proceso_id, criterio) → nivel; (proceso_id, oferta_id) → creado | Prioridad y guardado como relaciones distintas, sin duplicados |
| revisión_id → oferta_id, catálogo_id; fuente_id → URL, consulta, título | Valores y procedencia no se confunden con identidad de carrera |
| (revisión_id, definición, período) → unidad, valor, estado, fuente_id | Dato atómico contextualizado; el código del campo no determina por sí solo su unidad/período |


Primera forma normal: valores escalares y grupos repetidos extraídos. Segunda: en las relaciones de clave compuesta los atributos no clave dependen del conjunto, no solo de una parte. Tercera: con las dependencias declaradas, cada dependencia no trivial tiene una superclave como determinante o atributo primo; se extrajeron los determinantes transitivos (institución, fuente, definición e instrumento). Si el levantamiento revela nuevas dependencias se revisa el esquema; el nombre 3FN por sí solo no demuestra corrección del dominio.

Las descomposiciones se reúnen por PK/FK y claves candidatas, conservando identidad y relaciones. Fuente/definición separadas evitan reeditar todos los valores para cambiar una referencia. Los datos publicados no se sobrescriben: se crea otra revisión. Triggers impiden modificar revisiones, reinterpretar fuentes/definiciones utilizadas y añadir/eliminar datos de revisiones ya comparadas. La eliminación de un historial personal exige un flujo transaccional que primero retire comparaciones y datos personales conforme al protocolo; no basta borrar una fila de titular.

Resultado: 23/23 contratos de inserción/actualización/eliminación pasaron, incluyendo claves, escala, versión del instrumento, par distinto, NULL en faltantes y estabilidad de referencias. Evidencia: evidencia/modelo_integridad.json. Esto comprueba esas restricciones en SQLite; no demuestra 3FN mediante tests ni autorización HTTP ni portabilidad al motor objetivo.

### 2.4 Dimensionamiento con origen y cotas

| Magnitud | Cálculo / origen | Consecuencia para el diseño |
| --- | --- | --- |
| 360 procesos | 8 cursos × 45 alumnos (supuesto E1) | Índice por titular; recuperación de proceso propio |
| 50 usuarios simultáneos | 45 + 5 de holgura (E1) | Objetivo de prueba, no capacidad medida |
| 21.600 respuestas | 360 × 60 ítems (cota de almacenamiento, no test seleccionado) | Clave (aplicación, ítem); versionar escala y contenido |
| 2.880 prioridades / 1.800 guardados / 1.080 comparaciones | 360 × 8 / × 5 / × 3; supuestos explícitos de uso | Relaciones separadas e índices por proceso |
| 273 ofertas / 2.730 datos por revisión de catálogo | 91 carreras × hasta 3 campus × 10 campos; envolvente supuesta | Validar inventario por código/campus/ciclo; no se afirma recuento real |
| 5 solicitudes/s | 50 usuarios / 10 s entre acciones, aproximación conservadora de diseño | 70 % lectura = 3,5/s; 30 % guardado = 1,5/s |
| 5 solicitudes medias en curso | Ley de Little L = λW, λ=5/s y W medio supuesto=1s, régimen estable | No equivale a 50 conexiones activas ni usa p95 como media |
| 3.732 MiB lógicos (estimados) | 21.600×128 + 2.880×64 + 1.800×48 + 1.080×80 + 2.730×256 + 360×256 bytes | Cada tamaño por fila es una hipótesis; no es disco físico medido |
| 11.20 MiB con factor 3; reserva 256 MiB | Índices/serialización/margen; no incluye histórico ilimitado, WAL ni backups | Revisar con datos reales y retención; no es cuota contratada |


La teoría de colas se usa como comprobación de coherencia del escenario, sin prometer rendimiento: la tasa exacta de un sistema cerrado dependería de tiempo de pensamiento y respuesta. No se conocen aún tiempos de servicio ni distribución; no se infiere un tamaño de servidor ni p95 desde Little. La carga prevista para E3 mantiene 50 usuarios virtuales, 10 minutos estables y mezcla 70/30. RNF-R02 exige p95≤1.000 ms y RNF-R04 fallos≤1 %, separando errores funcionales/HTTP. En E2 esos dos RNF no se han medido.

### 2.5 CI-2: criptografía y modelo de amenazas

Bienes protegidos: respuestas de intereses, prioridades, guardados, comparación, credenciales y capacidad de recuperación. Adversarios considerados: usuario sin sesión, otro titular, sesión vencida/manipulada y alteración/copia de ciphertext. Un administrador que obtiene aplicación y claves queda fuera de la garantía de cifrado del payload; debe tratarse con controles de operación y mínimo acceso.

| Mecanismo y supuesto | Garantía / decisión | Evidencia y límite |
| --- | --- | --- |
| Hash de contraseña del framework Django; verificador con sal y costo | Comprobar una clave sin almacenar su texto original; usar la API del framework | Autenticación válida/inválida probada; no protege claves débiles ni sustituye limitación de intentos |
| Sesión aleatoria de servidor + caducidad + autorización por proceso | La identidad autenticada se contrasta con titular_id en cada lectura/escritura | Casos anónimo, ajeno, vencido y manipulado rechazados; ID opaco no basta |
| AES-256-GCM; clave aleatoria 32 bytes; nonce aleatorio 12 bytes por cifrado | C = Enc(K, nonce, contenido, AAD=id_proceso); autentica contenido y vinculación | Alterar un byte o usar otro id falla; nonce distinto probado; las claves locales no se publican |
| Etiqueta GCM de 128 bits y nonce de 96 bits | Nunca reutilizar nonce con la misma clave; ante n cifrados aleatorios, colisión aprox. n(n−1)/2^97 | Para n=100.000: ~6,3×10^-20 bajo aleatoriedad ideal. No es medición ni garantía total del sistema |
| CSRF en peticiones de escritura; ORM y escape de salida | Reducir solicitudes cruzadas y contenido inyectado | Pruebas HTTP de token y entrada inválida/escapada; no constituye auditoría completa |


GCM da confidencialidad e integridad bajo la seguridad de AES, claves secretas, nonces no repetidos y límites de uso. El identificador en AAD es público y no cifra por sí mismo. El ciphertext lleva nonce + contenido autenticado; la clave no se almacena en el repositorio. Al fallar la autenticación del ciphertext se rechaza la recuperación, sin devolver texto parcial ni inventar estado vacío. La PoC responde 503; ajeno recibe 404 y no autenticado 401.

La PoC cifra únicamente el contenido JSON del proceso. SQLite completo, identidades, sesiones y respaldos no quedan cifrados por ese mecanismo. El servidor local HTTP tampoco demuestra HTTPS. Para RNF-S03 se exige HTTPS y almacenamiento/backup cifrados antes de datos reales; secretos fuera del árbol de aplicación, control de permisos, rotación y recuperación probada. Cifrar sin conservar una clave recuperable causa pérdida del historial; por eso el diseño incluye copia segura de claves separada de los respaldos y acceso mínimo.

### 2.6 Instrumento, licitud y pertinencia

La ruta pública candidata es O*NET Interest Profiler: existen versiones de 30/60 ítems y recursos en español. Las páginas oficiales distinguen copia sin cambios (CC BY-ND) de adaptaciones sujetas a Developer License y sus condiciones; la documentación de widget/API solicita registro. Edumetrics sirve como referencia de adquisición externa, sin cotización, contrato ni API acreditados. Se revisaron las descripciones públicas; no se aceptaron acuerdos ni se obtuvieron permisos por actuar en el sitio.

Decisión operativa: continuar la evidencia técnica con SINTETICO-TECNICO-1. Antes de sustituirlo por un instrumento real, registrar nombre/versión/idioma, licencia exacta, atribución, permiso para traducción/adaptación e integración, población objetivo, límites de interpretación y revisión de pertinencia para adolescentes chilenos. No se ha acreditado validación psicométrica local; usar el nombre O*NET no la aporta. Si no se cierran condiciones, se bloquea el uso de ítems reales y se replanifica, sin generar un resultado vocacional con el ejemplo técnico.

Antes de un piloto con menores: revisar régimen aplicable a la fecha, finalidad, base de licitud, autorizaciones y asentimiento según protocolo, derechos, retención, supresión y terceros. E1 distingue Ley 19.628 y transición de Ley 21.719 (vigencia prevista 01/12/2026); confirmar aplicación con la fuente oficial y responsable institucional. Este documento no es aprobación jurídica ni permiso del establecimiento.


## 3. Tres soluciones comparables (C3)

Se mantiene el mismo alcance funcional: intereses autorizados, prioridades, catálogo con procedencia, dos ofertas, razones sin ganador y recuperación propia. El costo de un instrumento lícito debe analizarse en todas; ALT-3 agrega la dependencia del servicio externo. Ninguna arquitectura garantiza por sí sola privacidad o validez psicométrica.
| Dimensión | ALT-1 integrada | ALT-2 cliente/API | ALT-3 integrar/adquirir |
| --- | --- | --- | --- |
| Arquitectura | Monolito modular; pantallas y dominio en una app | Interfaz separada y API de dominio | Capa propia para proceso/catálogo/comparación; evaluación de tercero |
| Tecnología propuesta | Django + PostgreSQL + HTML/CSS | React + FastAPI + PostgreSQL + JSON/OpenAPI | Django/PostgreSQL + servicio Edumetrics de referencia; interfaz autorizada por confirmar |
| Límites del dato | Proceso y evaluación en infraestructura controlada | Mismo dominio propio; sesión, CORS y contrato a diseñar | El tercero recibe lo mínimo permitido; exportación y tratamiento requieren acuerdo |
| Operación | Una app propia + BD; importación interna revisada | Dos artefactos + BD; compatibilidad y releases coordinados | App + BD + disponibilidad y cambios del proveedor |
| Esfuerzo central / rango | 400 HH / 400 | 460 HH / 440–480 | 400 HH / 360–440 |
| Caja de referencia | 100.000 máximo provisionado | 100.000–130.000 según infraestructura | 100.000 + licencia L si reserva íntegra |
| Evidencia comparable | PoC sintética 15 contratos; no benchmark | Referencia técnica de separación/operación; sin PoC propia | Servicio comercial existente; precio/API/datos no verificados |
| Incertidumbre dominante | Liberación conjunta y cierre del instrumento real | Integración E2E y consumo de holgura | Licencia, interfaz, transferencias y control contractual |


ALT-2 es una opción real cuando se necesitan clientes o despliegues independientes; obtiene ventaja explícita de evolución en la matriz. ALT-3 no implica que el proveedor entregue todo Orienta: el comparador factual y la persistencia siguen requiriendo desarrollo. Un enlace o widget solo sería suficiente si satisface el recorrido y el control de información acordados. O*NET ofrece otra ruta pública de integración, pero requiere verificar condiciones y pertinencia; no se presume intercambiable con Edumetrics ni una licencia de costo L determinada.

Los rangos derivan de descomposición prospectiva por rol y complejidad de integración. Son comparables como planificación, no tiempos medidos de implementación de las tres opciones. El dato de que ALT-1 ya tenga PoC reduce cierta incertidumbre; no acredita que sea más rápida o segura en producción.

## 4. Matriz, decisión y sensibilidad (C4)

La decisión aplica suma ponderada S(a)=Σ(peso_i/100 × nota_ia). Escala común 1–5, mayor es mejor: 1 = incumplimiento o factibilidad no verificable; 2 = dependencia importante abierta; 3 = viable con costo/incertidumbre; 4 = adecuado al piloto con evidencia o estimación explícita; 5 = ventaja estructural fuerte en ese criterio. Las notas son juicios de ingeniería fundamentados; no mediciones ni calificaciones docentes. No se presenta una preferencia por marca como evidencia.

| Criterio / origen | Peso | ALT-1 | ALT-2 | ALT-3 |
| --- | --- | --- | --- | --- |
| Cobertura del recorrido Must · RF-01…11 | 25% | 4 | 4 | 2 |
| Calendario y constructibilidad · RC-02/06; 400 HH plan | 20% | 4 | 3 | 2 |
| Costo y control de caja · RC-01; ≤CLP100.000 | 15% | 4 | 3 | 1 |
| Privacidad y control de datos · RC-03; RNF-S01…05 | 15% | 4 | 4 | 2 |
| Explicabilidad y procedencia · RF-06/09/10; RB-01/04/09 | 10% | 4 | 4 | 3 |
| Operación inicial · RNF-P01/P02; D02 | 10% | 4 | 3 | 4 |
| Evolución independiente · RC-06; RNF-M | 5% | 3 | 5 | 3 |

| Resultado | ALT-1 | ALT-2 | ALT-3 |
| --- | --- | --- | --- |
| Suma ponderada / 5 | 3.95 | 3.60 | 2.20 |

### COV · Cobertura del recorrido Must (25 %)

Peso: El recorrido coherente es el propósito del MVP. Fuente de la necesidad: RF-01…11.

| Opción / nota | Fundamento y alcance |
| --- | --- |
| ALT-1 / 4 | Flujo propio y PoC sintética ejecutada; instrumento real y catálogo completo no acreditados. |
| ALT-2 / 4 | Mismo dominio implementable con cliente/API; no hay prueba E2E equivalente. |
| ALT-3 / 2 | Capa propia viable, pero exportación/API y cobertura del proveedor no verificadas. |

### CAL · Calendario y constructibilidad (20 %)

Peso: Cinco personas y plazo semestral; se necesita holgura para verificar. Fuente de la necesidad: RC-02/06; 400 HH plan.

| Opción / nota | Fundamento y alcance |
| --- | --- |
| ALT-1 / 4 | 400 HH: conserva 100 HH sobre capacidad500. La PoC reduce incertidumbre sobre el flujo sintético. |
| ALT-2 / 3 | 460 HH centrales (rango440–480): consume60 HH de holgura; más integración/contratos. |
| ALT-3 / 2 | 400 HH centrales (360–440), con acceso/licencia/plazo del tercero aún inciertos. |

### CST · Costo y control de caja (15 %)

Peso: No se autoriza gasto que exceda el techo; considerar costo futuro. Fuente de la necesidad: RC-01; ≤CLP100.000.

| Opción / nota | Fundamento y alcance |
| --- | --- |
| ALT-1 / 4 | Provisión E1:100.000. Licencia libre candidata sujeta a condiciones; sin contratación. |
| ALT-2 / 3 | 100.000–130.000 según compartir o separar infraestructura; extremo alto excede techo. |
| ALT-3 / 1 | 100.000+L con reserva íntegra; L y condiciones no cotizados. Nota1 significa no verificable. |

### PRI · Privacidad y control de datos (15 %)

Peso: Historial personal de potenciales menores exige control proporcional. Fuente de la necesidad: RC-03; RNF-S01…05.

| Opción / nota | Fundamento y alcance |
| --- | --- |
| ALT-1 / 4 | Propietario, sesión, CSRF y payload cifrado probados; TLS/cifrado integral pendientes de operación real. |
| ALT-2 / 4 | Propiedad controlable con API propia; diseño separa sesión/permisos. No garantiza más seguridad por estar separado. |
| ALT-3 / 2 | Tratamiento, región, contrato y exportación del tercero no verificados. |

### EXP · Explicabilidad y procedencia (10 %)

Peso: Toda diferencia debe ser interpretable y rastreable, sin ranking. Fuente de la necesidad: RF-06/09/10; RB-01/04/09.

| Opción / nota | Fundamento y alcance |
| --- | --- |
| ALT-1 / 4 | Reglas locales y fuentes de fixture verificadas; modelo incorpora definición, período, unidad y versión. |
| ALT-2 / 4 | Mismas reglas posibles como paquete de dominio; contrato debe preservar procedencia. |
| ALT-3 / 3 | Comparador propio conserva explicaciones; razones de resultados del servicio dependen del acceso permitido. |

### OPS · Operación inicial (10 %)

Peso: La defensa y el traspaso necesitan una operación reproducible. Fuente de la necesidad: RNF-P01/P02; D02.

| Opción / nota | Fundamento y alcance |
| --- | --- |
| ALT-1 / 4 | Una aplicación+BD; inicialización y pruebas locales reproducidas. Restauración y TLS del MVP aún no acreditados. |
| ALT-2 / 3 | Dos artefactos propios+BD; versiones cliente/API y contratos coordinados. |
| ALT-3 / 4 | Capa propia+BD y servicio administrado; reduce mantención del test pero agrega disponibilidad externa. |

### EVO · Evolución independiente (5 %)

Peso: Beneficio futuro real, menor prioridad que entregar el piloto acotado. Fuente de la necesidad: RC-06; RNF-M.

| Opción / nota | Fundamento y alcance |
| --- | --- |
| ALT-1 / 3 | Módulos separados internamente, pero liberación conjunta. |
| ALT-2 / 5 | Cliente y API pueden liberarse independientemente con contrato compatible; evidencia estructural, no medición. |
| ALT-3 / 3 | Comparador propio evoluciona; el instrumento depende del tercero. |


### Selección y descarte condicionado

Se selecciona ALT-1 para este diseño E2: 3,95/5 frente a 3,60 y 2,20, con 100 HH de holgura y operación inicial simple. La confianza es suficiente para preparar el piloto acotado, sujeta al instrumento/catálogo y controles operativos.

ALT-2 se descarta en el escenario semestral porque el beneficio de releases independientes no compensa 60 HH centrales adicionales y más contratos por mantener. Conserva valor si cambia la prioridad de evolución o aparece un segundo cliente.

ALT-3 se descarta ahora por factibilidad no demostrada de costo, transferencia y acceso/exportación. No se afirma que el producto sea técnicamente inferior: información contractual favorable obligaría a recalcular sus notas. Si las siete notas pasaran justificadamente a [4,4,4,4,4,4,3], empataría con ALT-1 en 3,95/5. Esa revisión requiere evidencia externa, no un supuesto presentado como resultado.

### Sensibilidad a pesos y a juicios
| Escenario | Pesos COV/CAL/CST/PRI/EXP/OPS/EVO | ALT-1 | ALT-2 | ALT-3 | Selección |
| --- | --- | --- | --- | --- | --- |
| Base | 25/20/15/15/10/10/5 | 3.95 | 3.6 | 2.2 | ALT-1 |
| Privacidad prioritaria | 20/15/10/30/10/10/5 | 3.95 | 3.7 | 2.25 | ALT-1 |
| Entrega corta | 25/30/15/10/10/8/2 | 3.98 | 3.49 | 2.13 | ALT-1 |
| Evolución futura dominante | 20/10/10/10/10/10/30 | 3.7 | 4.0 | 2.5 | ALT-2 |


Para variar solo evolución, sea w su peso como fracción; se reescalan proporcionalmente los otros seis desde su suma original 0,95. La ventaja media de ALT-1 en esos criterios es 0,45/0,95=0,473684. Diferencia S1−S2=0,473684(1−w)−2w. El empate ocurre en w=0,191489 (19,15 %). Por encima gana ALT-2 bajo esas notas; no es un umbral universal para cualquier vector de pesos.

La incertidumbre de notas también importa: reducir calendario de ALT-1 de 4 a 3 y elevar el de ALT-2 de 3 a 4 deja 3,75 contra 3,80, con el resto igual. Una variación individual cambia 0,20 puntos; la combinación invierte por 0,05. Por eso se conserva la evidencia y se pide revisar estimaciones con integración real en E3. La selección no es una verdad matemática independiente de los supuestos.

El CSV contiene cada fundamento. El libro Matriz_Decision_E2.xlsx permite editar pesos/notas y recalcula totales; no contiene macros ni enlaces externos. El JSON conserva valores de referencia y escenarios para comprobarlos por separado.


## 5. Arquitectura seleccionada y rigor (C5)

### C4 L1: contexto

![C4 L1: actores, sistema y fuentes externas](../../integrantes/benjamin-henriquez/03_Diagramas/C4_L1_Contexto.png)

### C4 L2: contenedores

![C4 L2: navegador, aplicación, base de datos, fuentes y respaldos](modelos/C4_L2.png)

En C4 un contenedor es una aplicación ejecutable o un almacén; no implica usar Docker. La aplicación integra presentación y dominio en un despliegue. El navegador ejecuta HTML/CSS y JS mínimo; la base objetivo es PostgreSQL. Un comando interno importa snapshots revisados desde fuentes oficiales. Los respaldos son privados y cifrados; no se suben al repositorio. El instrumento real se integra solo después de verificar condiciones; no hay dependencia de proveedor activa en ALT-1.

### C4 L3 y secuencia UML

![C4 L3: componentes de la aplicación](modelos/C4_L3.png)

Acceso establece sesión; Procesos verifica titular; Intereses valida versión/escala; Catálogo entrega revisiones con procedencia; Comparación comprueba par y compatibilidad, y explica diferencias; Persistencia usa transacciones. Las rutas de la PoC son una implementación simplificada y no se presentan como todos estos componentes terminados.

![UML de secuencia: recuperar y comparar un proceso propio](modelos/Secuencia_Comparacion.png)

La secuencia modela el comportamiento propuesto, con alternativas de autorización y dato ausente/incompatible; no es una traza de una ejecución. Las líneas de vida, mensajes numerados y retornos distinguen llamada y respuesta. Cada diagrama indica frontera, tipo de elemento, tecnología y leyenda; el detalle de relaciones está en DOT editable.
| Requisito crítico | Decisión visible | Verificación / estado |
| --- | --- | --- |
| RNF-S01/02: sesión y aislamiento | Acceso + autorización en Procesos antes de consultar; índice titular | Contratos de PoC local; revisar todas las rutas del MVP |
| RNF-S03/04: cifrado y secretos | HTTPS propuesto; payload AEAD; almacenamiento/backup cifrados y claves separadas | AEAD probado local; HTTPS/cifrado integral no acreditados |
| RNF-C02 / RF-06: procedencia | Importador interno → snapshots → dato/fuente/unidad/período | Modelo verificado; inventario completo 2027 pendiente de ejecución |
| RNF-M01: reglas comprobables | Comparación como lógica separada; cero ranking; NULL explícito | Casos factuales/faltantes/unidades en PoC; ramas ≥80 % no medidas |
| RNF-R02/R04: 50 usuarios, p95 y fallos | Lecturas indexadas y transacciones cortas; un despliegue inicial | Diseño y método; carga no ejecutada en E2 |
| RNF-D02: RPO≤24h / RTO≤4h | Copia diaria + plan de restauración + claves recuperables | Objetivos ratificados para piloto; ensayo del MVP por ejecutar |
| RNF-U01/U03: AA y 360–1440px | HTML semántico, teclado, foco visible y tabla deslizable | Revisión de mockups en Chromium escritorio/móvil; no certifica WCAG ni Firefox |


## 6. Mockups y recorrido de demostración

Prototipo navegable local en mockups/index.html, siete vistas: inicio, intereses, prioridades, catálogo, comparación, progreso y privacidad. Puede abrirse directamente o servirse en loopback con python3 -m http.server 8894 --bind 127.0.0.1 --directory entregas/E2/mockups desde la raíz. No usa un backend, analítica, almacenamiento persistente o cuentas. Su estado vive solo en la pestaña.

Recorrido propuesto para la exposición: mostrar inicio → intereses ilustrativos y error de incompletitud → prioridades → buscar/guardar dos ofertas → comparar con faltantes → progreso. El PPT conserva capturas para no depender de una demo de navegación dentro de los 10 minutos. La PoC ejecutable comprueba por separado el guardado y la recuperación reales.

Las fichas de ejemplo muestran nombres, campus y duración publicados: Ingeniería Civil Informática (10 semestres) y Psicología (5 años), campus Concepción. Los aranceles de páginas que indican otro año no se reutilizan como 2027. La conversión 2 semestres/año es una hipótesis de trabajo, no certificación de equivalencia académica. Empleabilidad sin definición/período compatible se marca como ausente o no homologable.

![Mockup: inicio del recorrido](mockups/capturas/01_inicio.jpg)

![Mockup: comparación y razones sin ganador](mockups/capturas/07_comparacion.jpg)

![Mockup: comparación en móvil](mockups/capturas/10_movil_comparacion.jpg)

La revisión funcional de interfaz se documenta en evidencia/mockups_navegador.json: respuesta incompleta, búsquedas vacías, selección, transición y marcado de comparación. Esta revisión técnica no sustituye usabilidad con estudiantes ni una evaluación de accesibilidad completa.

## 7. Prueba de concepto y alcance de la evidencia (C6)

La incertidumbre comprobada es si una aplicación integrada puede guardar un proceso, comparar información con procedencia y recuperar solo el estado del titular, rechazando entradas y accesos inválidos. Entorno: Python 3.12, Django 5.2.18, cryptography 50.0.2 y SQLite. Ofertas e instrumento de la PoC son sintéticos; las fichas UdeC de mockups son una pieza separada de diseño.

Resultado local: 15/15 contratos HTTP/criptográficos pasaron. Incluyen guardar/salir/reautenticar/recuperar, entradas incompletas/fuera de escala/par inválido sin sobrescritura, NULL/unidades, anónimo/ajeno/sesión vencida o manipulada, CSRF, clave incorrecta, ciphertext alterado/copiado a otro proceso, nonce distinto y escape de entrada. Ver integrantes/benjamin-henriquez/04_PoC/resultados_poc.json y README.txt.

El 27/10/2026 se reejecutaron en un entorno aislado los 15 contratos de la PoC y los 23 del modelo lógico, con resultados 15/15 y 23/23 respectivamente. Los reportes se conservan en entregas/E2/evidencia; no sustituyen una prueba de carga o una validación con usuarios.

El esquema lógico añade 23/23 comprobaciones diferentes en SQLite. No se suman 15+23 como porcentaje de cobertura: comprueban fronteras y artefactos distintos. No hay medición comparativa entre arquitecturas ni acreditación de carga50, catálogo completo, psicometría, WCAG, Firefox, despliegue productivo o aceptación de usuarios.

## 8. Sacrificios, costo y riesgos (C6)

### 8.1 Tres intercambios defendibles

1. Se sacrifica **liberación independiente de interfaz y dominio** para obtener **menos contratos y despliegues que coordinar**, por la restricción **RC-02/06: semestre y5integrantes**. Consecuencia: Módulos internos y revisiones cruzadas; API separada se reabre si surge un cliente independiente.

2. Se sacrifica **actualización automática inmediata de datos** para obtener **revisión humana y procedencia verificable**, por la restricción **RC-07: fuentes/ciclo; sin API oficial impuesta**. Consecuencia: Registrar consulta y fecha de revisión; indicar obsolescencia y bloquear inferencias no homologables.

3. Se sacrifica **escalamiento independiente del comparador** para obtener **operación y costo inicial acotados**, por la restricción **RC-01:≤100.000caja; escenario50concurrentes**. Consecuencia: Medir el objetivo de carga enE3 antes de afirmar capacidad y revisar si cambia el escenario.


### 8.2 Presupuesto y esfuerzo

Caja es dinero que se desembolsa; horas valorizadas representan costo de oportunidad. No hay gastos pagados, facturas ni HH ejecutadas documentadas en este paquete. Se conserva la provisión de E1 sin atribuir una compra: servicios 30.000 (aprox. 12.000/mes × 2,5), dominio opcional 15.000, validación 20.000 y contingencia 35.000 = máximo 100.000. No es una cotización vigente.
| Rol / valor hora (E1) | ALT-1 HH | ALT-2 HH | ALT-3 HH |
| --- | --- | --- | --- |
| Jorge / CLP 20.000 | 80 | 90 | 80 |
| Benjamín / CLP 20.000 | 80 | 100 | 75 |
| Diego / CLP 23.000 | 80 | 95 | 85 |
| Mauro / CLP 25.000 | 80 | 85 | 80 |
| Lucas / CLP 27.500 | 80 | 90 | 80 |

| Alternativa | HH centrales / holgura de 500 | Costo HH valorizado | Caja estimada |
| --- | --- | --- | --- |
| ALT-1 | 400 / 100 | CLP 9.240.000 | 100.000–100.000 |
| ALT-2 | 460 / 40 | CLP 10.585.000 | 100.000–130.000 |
| ALT-3 | 400 / 100 | CLP 9.255.000 | 100.000 + L |


La descomposición por rol es un escenario central prospectivo. ALT-2 añade integración interfaz/API y operación; rango 440–480 HH, holgura20–60. ALT-3 rango360–440 HH, depende del acceso externo. Si no hay cotización L no se puede asegurar que ALT-3 cumple el techo. Para encajar manteniendo el resto de partidas: L + contingencia remanente ≤35.000; se requiere revisar licencia y presupuesto antes de comprometer gasto.

ALT-1 valoriza 400 HH en CLP 9.240.000; al añadir la provisión máxima de caja, costo económico de referencia CLP 9.340.000. No se exige pagar a los estudiantes ese monto. E1 contempla continuidad de servicios CLP 13.250/mes y 4h de operación ×27.500 =110.000/mes; costo mensual valorizado123.250. Si ese régimen se mantuviera 12 meses, caja de servicios159.000 y trabajo1.320.000, total económico1.479.000. Es una proyección distinta del límite semestral de caja; no hay responsable ni presupuesto permanente aprobados. No se calcula retorno con beneficios monetarios inventados.

### 8.3 Registro vivo de riesgos

P e I son estimaciones ordinales1–5, no frecuencias observadas; P×I ordena atención y no equivale a pérdida esperada. Estado al26/10/2026; responsables indican coordinación del riesgo. Se reevalúa al cambiar catálogo, instrumento, entorno o disponibilidad de personas.

#### R03 · Datos · P4 × I4 = 16 · Mauro

Evento: Valores de años, unidades o definiciones incompatibles inducen una comparación engañosa.

Disparador: Dato sin ciclo/fuente/definición o discrepancia entre fuentes oficiales.

Mitigación: Snapshots; fuente por dato; validación previa; NULL explícito; bloquear diferencias incompatibles.

Estado: Abierto; controles sintéticos y esquema comprobados. Residual: Catálogo oficial completo y política de actualización requieren carga/revisión.

#### R04 · Licencia/instrumento · P3 × I5 = 15 · Mauro

Evento: No hay permiso o adaptación/pertinencia suficiente para el instrumento elegido.

Disparador: No se documentan versión, licencia y condiciones antes de usar ítems reales.

Mitigación: Mantener PoC sintética; elegir versión oficialmente autorizada; no traducir/adaptar sin régimen válido.

Estado: Abierto, ruta pública O*NET documentada; integración no contratada. Residual: Requiere revisión de pertinencia para adolescentes chilenos; sin validación psicométrica local acreditada.

#### R05 · Usuarios/validación · P3 × I5 = 15 · Jorge

Evento: No se consiguen participantes representativos y autorizaciones a tiempo.

Disparador: Menos de3 participantes confirmados una semana antes de la validación.

Mitigación: Convocar anticipadamente3–5 personas; ventana alternativa y protocolo de consentimiento/asentimiento.

Estado: Abierto; protocolo listo, ejecución sin evidencia. Residual: Disponibilidad y autorizaciones externas; no inventar resultados.

#### R09 · Operación/continuidad · P3 × I4 = 12 · Lucas

Evento: Fallo de entorno, pérdida de claves o ausencia de restauración impide mostrar/recuperar el flujo.

Disparador: Falla el ensayo de arranque/restauración o servicio excede provisión de costo.

Mitigación: Entorno local alterno, datos sintéticos, claves privadas separadas, copia diaria y ejercicio de restauración antes de uso real.

Estado: Abierto; arranque de PoC reproducido, restauración del MVP no acreditada. Residual: RPO/RTO son objetivos hasta ejecutar el ejercicio completo.

#### R07 · Privacidad/acceso · P2 × I5 = 10 · Mauro

Evento: Un usuario obtiene o modifica respuestas del proceso de otro.

Disparador: Cualquier prueba de lectura/escritura ajena o credencial vencida permite acceso.

Mitigación: Autorización por propietario, sesión caducable, CSRF y suite negativa; datos sintéticos hasta protocolo completo.

Estado: Reducido localmente por pruebas; permanece abierto para el MVP. Residual: TLS, cifrado integral, registro/rotación y configuración del piloto por verificar.


### 8.4 Operación y continuidad

RPO≤24h admite perder hasta un día de cambios; RTO≤4h fija el objetivo de recuperación. Son metas proporcionadas a un piloto no crítico y ratificadas como diseño, pendientes del ensayo completo. Copia diaria de BD, configuración y versiones; cifrado de copia, clave en resguardo separado y acceso mínimo. Verificar integridad, conservar política de retención del protocolo y caducar copias con datos personales. No publicar bases, claves o sesiones en Git.

Procedimiento de restauración previsto: detectar incidente y registrar hora → detener escrituras afectadas → seleccionar copia verificada y entorno aislado → recuperar claves por canal seguro → restaurar BD/configuración → ejecutar casos de autorización/recuperación/comparación → medir tiempo y punto recuperado → habilitar solo tras aceptar resultados. Si no se cumplen metas, se revisa frecuencia, costo y alcance. El repositorio tiene la PoC reproducible, no un ejercicio de restauración productivo realizado.

Para la defensa: PPT/PDF descargados, capturas incluidas y PoC local con datos sintéticos como respaldo. Verificar antes el puerto y arranque; no depender de internet o de una API con permisos pendientes. El presentador responde con el alcance de cada evidencia y deriva a respaldo sin consumir el turno de los demás.

## 9. Validación prevista y hoja de ruta

E3 debe responder observaciones reales de E2, construir flujo parcial vivo, medir RNF y registrar al menos dos iteraciones de diseño con desencadenante, alternativas, decisión y efecto verificado. El roadmap incluye E4/E5 y obligaciones del ramo. Los materiales de E2 no se marcan como un MVP entregado ni demo final.

Protocolo de usabilidad listo para ejecutar:3–5 estudiantes del perfil ajenos al equipo, autorizaciones según protocolo, alias y datos mínimos, moderador que no ayuda salvo bloqueo. Tareas: iniciar/retomar un proceso; completar intereses autorizados; declarar prioridad; guardar dos ofertas; comparar, identificar un faltante y explicar que no hay ganador; recuperar estado. Registrar por tarea éxito sin ayuda/con ayuda/fallo, tiempo, errores y comprensión. Con n=5, meta≥4/5 completan comparación sin ayuda; con n=3 la lectura es descriptiva y se informa denominador. No generalizar ni inventar participantes/tiempos. La encuesta inicial no reemplaza este estudio.

## 10. Defensa de 10 minutos (C7)

La versión académica breve de exposición tiene 14 láminas principales y una de referencias. La entrega contiene 22, incluidos siete respaldos técnicos y el fundamento de las 21 notas de la matriz; este dossier conserva el desarrollo extenso. El modelo UML también se expone. Los nombres aparecen solo en portada; los turnos y tiempos se mantienen en guiones separados. Las notas de exposición contienen texto oral sin nombres ni cronómetro. El total de preparación planificado es 600 s. La guía habla de 10 minutos más preguntas y la rúbrica de hasta 12 minutos; se adopta la versión más breve. No se acredita un ensayo humano por estimar palabras o duraciones.

Todos deben dominar problema, selección, dato ausente, privacidad y límites de PoC. En preguntas: responder el punto primero, mostrar la evidencia pertinente y reconocer lo que no se midió. No decir «100% de la rúbrica aprobado» ni atribuir a personas validaciones no realizadas. La cobertura documental de los siete criterios está en Cobertura_Rubrica_R2.md; la evaluación final depende de contenido y defensa.

## 11. Fuentes y autoría

Prioridad: enunciado y rúbrica oficiales sobre guías de preparación; E1 como baseline; nueva evidencia local como comprobación técnica. Los originales se preservan con SHA-256. La documentación explica dónde el análisis nuevo amplía E1, sin inventar feedback docente.

| ID | Referencia / acceso | Uso y límite |
| --- | --- | --- |
| E1-21 | SRS E1 v1.8, p.21: alternativas y protocolo de PoC · entregas/E1/Orienta_E1_Grupo9_Informe_SRS.pdf | documento aportado; planteamiento previo |
| E1-23 | SRS E1 v1.8, pp.8,21,23–24 · entregas/E1/Orienta_E1_Grupo9_Informe_SRS.pdf | documento aportado |
| P01 | PoC local:15contratos HTTP, SQLite, AESGCM y navegador · integrantes/benjamin-henriquez/04_PoC/resultados_poc.json | ejecución local |
| D01 | C4 y modelo lógico formal E2 · entregas/E2/modelos/esquema_logico.sql | diseño comprobado en SQLite |
| W-DJ | Django5.2: seguridad · https://docs.djangoproject.com/en/5.2/topics/security/ | documentación técnica |
| W-FAST | FastAPI: conceptos de despliegue · https://fastapi.tiangolo.com/deployment/concepts/ | documentación técnica |
| W-EDU | Edumetrics: descripción comercial del servicio · https://www.edumetrics.cl/test-vocacional | fuente del proveedor; no cotización/API verificada |
| W-ONET-L | O*NET: condiciones de copia/adaptación · https://www.onetcenter.org/license_tools.html | licencia publicada; no dictamen jurídico |
| W-ONET-IP | O*NET: versiones, idioma e integración · https://services.onetcenter.org/ip | documentación de integración; registro necesario para API/widget |
| W-UDEC-I | UdeC:Ingeniería Civil Informática,10semestres yConcepción · https://admision.udec.cl/ingenieria-civil-informatica/ | ficha consultada26/10; año/ciclo de cada dato debe verificarse |
| W-UDEC-P | UdeC:Psicología,5años yConcepción · https://admision.udec.cl/psicologia/ | ficha consultada26/10; no asumir arancel2027 |
| W-BCN | BCN:Ley21.719 y transición del régimen · https://www.bcn.cl/leychile/navegar?idNorma=1209272 | normativa; revisar régimen al operar |


Rúbrica R2: docs/curso/Rubricas_Proyecto_Semestral.pdf pp.4–5. Enunciado E2: pp.7–8. Baseline E1:49páginas v1.8 del08/10/2026. Guion original de Jorge conservado en su carpeta. Consultas públicas de instrumento, fichas y servicio al26/10/2026; no representan contratos. Los enlaces técnicos sirven de referencia de capacidades del framework, no resultados empíricos de Orienta.

Elaboración asistida por Codex: redacción nueva de todos los bloques, código/generadores/mockups, análisis de decisión, diagramas y pruebas locales por instrucción de Benjamín. El equipo debe comprender y revisar el material antes de defenderlo; no se fabrican actas, reuniones, tiempos de trabajo ni contribuciones individuales. Los datos sintéticos se identifican expresamente y no contienen respuestas reales de estudiantes.
