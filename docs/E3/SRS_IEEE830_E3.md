# Orienta · Especificación de requisitos IEEE 830

Grupo 9 · Proyecto Informático · DIICC · Universidad de Concepción. Versión 2.0 para E3, 16 de noviembre de 2026. Autoría: equipo definido en E1; elaboración de este paquete con asistencia de IA. El SRS v1.8 original permanece inmutable en docs/fuentes/SRS_E1_original.pdf. La presente versión corrige las observaciones aportadas, sin afirmar aprobación docente ni validación humana no recibida.

## Control de cambios

| Versión | Fecha | Cambio y fuente |
| --- | --- | --- |
| 1.8 | 08/10/2026 | Línea base E1, 17 RF y 21 RNF; documento original preservado |
| 2.0 | 16/11/2026 | RF atómicos, importación y supresión, construcción E3, fuentes públicas, CI1/CI2 y mediciones; comentarios del escrito del 06/11 y puntajes PDR del 16/11 |

## Resumen ejecutivo

Orienta ayuda a un estudiante a expresar sus intereses y prioridades y a revisar dos ofertas de educación superior con datos que puede comprobar. No elige una carrera por la persona. El problema local se documentó mediante una encuesta de conveniencia; no representa a todos los estudiantes de Chile. SIES aporta contexto de continuidad de estudios, sin identificar por sí solo la causa de las decisiones.

La versión E3 funciona en un equipo local y conserva respuestas, prioridades, ofertas y comparación. Incluye 91 ofertas UdeC de la publicación oficial de Admisión 2027. Los valores sin fuente o período comprobable se muestran como información no disponible. La exploración de intereses utiliza textos originales y no constituye un test psicológico. Las pruebas técnicas y sus límites figuran en el dossier. Para autorizar un piloto con personas reales faltan las validaciones humanas, el protocolo efectivo y el cierre de los controles del entorno operativo.

## 1. Introducción

### 1.1 Propósito

Especificar el contrato funcional, de datos y de calidad del sistema construido para E3 y su continuidad hacia E4/E5. Audiencia: equipo, docente y eventual responsable técnico. La plantilla IEEE 830 aportada es la estructura canónica de las secciones 1 a 14.

### 1.2 Alcance y exclusiones

Incluye acceso por alias; ficha original de intereses; prioridades; catálogo UdeC 2027; detalle con procedencia; incorporación y retiro de guardados; par distinto; comparación factual; recuperación y supresión; importación operada por responsable técnico. Excluye RUT, diagnóstico, ranking, porcentaje global de compatibilidad, panel de terceros, chat IA y postulación oficial. RF-14 exportación queda fuera del corte. El sistema no representa aprobación ni patrocinio UdeC. La ficha C-02 y cualquier remisión a alcance deben apuntar a esta sección, corrigiendo la remisión errónea a §2.4.

### 1.3 Definiciones

Proceso: estado privado asociado a un titular lógico. Oferta: carrera en campus y ciclo, identificada por código oficial. PDR: revisión preliminar E2. CDR: revisión crítica E3. RF/RNF: requisitos funcionales/no funcionales. Must: imprescindible para MVP; Should: siguiente prioridad; Could: opcional; Won't: excluido. Dato faltante: ausencia que no se transforma en cero. Validación: comprobar utilidad/comprensión con personas; verificación: comprobar contratos del sistema.

### 1.4 Referencias

SRS E1 original; rúbrica R3 páginas 6–7; enunciado E3 página 8; plantilla IEEE 830; comentarios aportados por el usuario; Fuentes_Publicas.md; Respuesta_Docente_Iteraciones.md; Ciencias_Ingenieria.md. Los antecedentes E2 y su matriz se conservan en docs/antecedentes. Las referencias públicas completas y límites de descarga se mantienen en Fuentes_Publicas.md.

## 2. Descripción general

### 2.1 Perspectiva y funciones

Aplicación web monolítica Django, navegación HTML del servidor y persistencia relacional. Se mantiene la dirección ALT1 de E2 por su bajo costo de operación y tamaño de equipo. Se distingue el prototipo académico del servicio operativo: la ejecución E3 usa datos personales sintéticos y catálogo público.

### 2.2 Contexto del sistema

Actor directo: estudiante con alias. Operador técnico: prepara e importa snapshot revisado; no puede consultar respuestas a través de un panel de producto. Sistemas externos: DEMRE/Mineduc y Admisión UdeC como fuentes públicas descargadas previamente; navegador como cliente. Durante el flujo principal no se consulta un proveedor externo. Figuras C4 L1/L2 y modelo lógico en docs/modelos. La red escolar, correo y LMS están fuera de la frontera del sistema.

### 2.3 Problema, oportunidad y escenario

La necesidad local es hacer explícitos intereses y prioridades al revisar información dispersa. E1 reporta 156 respuestas estudiantiles y 36 de apoderados, de conveniencia, sin inferencia poblacional. SIES informó 77,9 % de retención de primer año para la cohorte 2025; 22,1 % es el complemento de continuidad en el mismo programa y no una medida de indecisión o fracaso de orientación. Las consecuencias potenciales incluyen tiempo, gasto y frustración; no se estima ahorro causal atribuible a Orienta sin estudio.

MiFuturo permite revisar oferta e indicadores; Acceso/DEMRE informa códigos y reglas; EligeCarrera aporta recursos; Vocation One ofrece evaluación e informes profesionales. Orienta propone conservar prioridades y una comparación acotada con faltantes visibles. No se afirma que estas plataformas sean inadecuadas ni que carezcan de toda comparación: la necesidad diferencial es una hipótesis a contrastar con usuarios.

Escenario supuesto: establecimiento de enseñanza media con 8 cursos de hasta 45 estudiantes, 360 procesos y una clase de 45 más 5 sesiones de margen. La referencia reglamentaria de 45 no acredita matrícula real. Cinco guardados por persona fue una hipótesis de capacidad, no resultado de encuesta ni límite implementado. La ventana 22 × 12 horas se retira como hecho: el piloto debe publicar su horario real.

Recursos supuestos: navegador actual en PC o teléfono, red con acceso al servidor, responsable de coordinación TI y espacio para una sesión de 45 minutos. Madurez tecnológica supuesta básica: uso de navegador y formularios, sin administración propia de nube. No existe inspección de un establecimiento específico. Antes del piloto se medirá velocidad/estabilidad, número de equipos simultáneos, navegadores, responsable y horario usando la ficha del Anexo B. Conectividad para la Educación y Aulas Conectadas aportan un marco público, sin probar la infraestructura del escenario.

### 2.4 Perfiles y validación prevista

| Perfil | Tipo y tarea | Contexto / alfabetización | Influencia y acceso |
| --- | --- | --- | --- |
| Estudiante de 3.º–4.º medio | Directo; explorar, guardar, comparar y retomar | Teléfono/PC, experiencia básica de formularios; posible discapacidad o conectividad limitada | Alta en aceptación; solo su proceso |
| Orientador/a | Indirecto; acompañar conversación y explicar límites | Contexto escolar; experiencia media, no administra infraestructura | Alta en pertinencia; sin panel ni acceso a procesos ajenos |
| Apoderado/a | Afectado; conversar sobre costos y opciones | Recursos y alfabetización variables | Media; no accede a cuenta del estudiante |
| Coordinador/a TI | Operador; instalar, importar snapshot y recuperar servicio | Experiencia técnica suficiente para runbook; disponibilidad por confirmar | Alta en viabilidad; tareas técnicas con mínimo privilegio |

Validación de concepto y uso con personas ajenas al equipo según Validacion_Usuarios.md. Prioridad inicial: 5 participantes de 18 años que correspondan a transición escolar, sin recolectar nombres. Si se incluyen menores se exige protocolo y autorizaciones aplicables antes de comenzar. Ninguna sesión se declara realizada sin registro real.

### 2.5 Suposiciones, dependencias y restricciones de contexto

Dependencias: Python/Django, cryptography, navegador y SQLite; sin API pagada para el flujo. Supuestos revisables: catálogo oficial disponible; capacidad de instalar el entorno; usuarios representativos accesibles; ficha autodescriptiva pertinente. Riesgos que invalidan el diseño: ausencia de responsable de operación, datos oficiales incompatibles, utilidad no observada o controles de privacidad incompletos. Se preserva independencia entre datos sintéticos de pruebas y cualquier estudio real.

### 2.6 Registro de restricciones de diseño

| ID / ABET | Enunciado y origen | Métrica / gestión | Alternativa descartada |
| --- | --- | --- | --- |
| RC-01 cost | Equipo propone caja máxima CLP 100.000/semestre; no es financiamiento externo aprobado | Gasto incremental nuevo documentado; no contratar sin responsable | Servicio vocacional comercial sin licencia/cotización disponible |
| RC-02 schedule | SRS: MVP S13, E3 S14, cierre E5 S17–18 | Corte actual S15; replanificar sin inventar prórroga | Microservicios o recomendador ML antes del MVP |
| RC-03 legal considerations | Privacidad, licencias y reglas de NNA, normativa vigente al ejecutar estudio | Datos sintéticos en demo; gate previo a reales; derecho de supresión | Ingreso de RUT, datos sensibles innecesarios o instrumento propietario copiado |
| RC-04 usability | Uso en clase y móvil, recursos heterogéneos | Flujo legible 360–1440 px, teclado y errores concretos | Tabla fija que desborde toda la página |
| RC-05 maintainability | Cinco roles académicos; continuidad no contratada | Monolito, migraciones, tests, runbook y CI | Stack distribuida con múltiples servicios de operación |
| RC-06 interoperability | Datos de distintas fuentes/ciclos | Fuente, fecha, unidad y período; bloquear homologación inválida | Mezclar arancel 2026 con etiqueta 2027 sin advertencia |
| RC-07 sustainability | Presupuesto y mantención posterior no garantizados | Demo local, sin inferencia IA; plan de retiro si no hay responsable | Servicio permanente dependiente de cómputo pagado sin continuidad |

### 2.7 Aplicaciones de ciencias de la ingeniería

CI1: dependencias funcionales y normalización; CI2: autenticidad, autorización y cifrado. Se desarrollan con formulación, supuestos, procedimiento, pruebas y efectos en Ciencias_Ingenieria.md. Dimensionamiento y complejidad apoyan estas decisiones; no sustituyen las dos aplicaciones comprometidas en E1.

## 3. Requisitos funcionales

### 3.1 Lista resumida, prioridad y aceptación

Convención: RF-01 es el identificador formal de E1; los nombres de tests y código pueden omitir el guion (RF01) sin cambiar la trazabilidad.

| ID | Requisito atómico | Prioridad | Dado / Cuando / Entonces |
| --- | --- | --- | --- |
| RF-01 | Crear y acceder a proceso propio | M | Dado un alias nuevo, cuando confirma credencial válida, obtiene proceso propio sin RUT; credencial incorrecta no da acceso |
| RF-02 | Registrar respuestas versionadas | M | Dada ficha original v1, cuando envía 12 valores 1–5 válidos, se guardan por ítem/versión; inválidos no generan resultado |
| RF-03 | Mostrar resumen de intereses con límites | M | Dada ficha completa, cuando consulta, ve seis promedios autodescriptivos y límites sin diagnóstico ni carrera sugerida |
| RF-04 | Registrar prioridad por dimensión | M | Dada ubicación alta, cuando guarda, persiste y se resalta en comparación; campos vacíos quedan sin definir |
| RF-05 | Filtrar catálogo UdeC 2027 | M | Dado snapshot cargado, cuando filtra campus/código/nombre, ve solo ofertas coincidentes con ciclo |
| RF-06 | Mostrar ficha y procedencia | M | Dada oferta, cuando consulta detalle, ve fuente, fecha, ciclo y faltantes; ausencia no se transforma en 0 |
| RF-07a | Incorporar oferta guardada | M | Dada oferta ya guardada, cuando repite incorporación, existe una sola asociación |
| RF-07b | Retirar oferta guardada | M | Dado guardado propio, cuando retira, desaparece solo esa asociación |
| RF-08 | Seleccionar par distinto | M | Dadas dos ofertas distintas, cuando confirma, conserva par; selección incompleta/igual se rechaza |
| RF-09 | Mostrar comparación factual | M | Dado par y prioridades, cuando consulta, muestra valores/unidades/fuentes y bloquea diferencias no homologables |
| RF-10 | Explicar diferencias y faltantes | M | Dado campo ausente o período incompatible, cuando compara, comunica límite sin ganador ni ranking |
| RF-11 | Recuperar estado propio | M | Dado proceso guardado, cuando sale/vuelve, recupera estado; otro titular no lee ni elimina por UUID |
| RF-12a | Editar prioridad existente | S | Dada prioridad guardada, cuando cambia nivel, queda un único nivel actualizado |
| RF-12b | Recalcular comparación al editar | S | Dado par existente, cuando vuelve tras editar prioridad, ve nuevo resalte sin reconstruir el par |
| RF-13 | Mostrar estado de avance | S | Dado proceso, cuando abre inicio, ve respuestas, dimensiones y guardados persistidos |
| RF-14 | Exportar resumen local | C | Pendiente; futura exportación solo del estado propio, sin terceros |
| RF-15 | Panel institucional | W | Excluido del MVP; no se habilita consulta agregada/individual |
| RF-16 | Chat IA | W | Excluido; no se transmiten respuestas a proveedores de IA |
| RF-17 | Ranking global | W | Excluido; no existe carrera ganadora ni porcentaje de compatibilidad |
| RF-18 | Importar catálogo controlado | M nuevo | Dado snapshot local, cuando valida y aplica, inserta en transacción; duplicado/ciclo inválido rechaza todo; repetición es idempotente |
| RF-19 | Suprimir cuenta y proceso | M nuevo | Dado titular autenticado, cuando confirma ELIMINAR, se borran sus dependencias y acceso; catálogo y otros titulares permanecen |

La división de RF-07 mantiene su trazabilidad al RF-07 original. Los 11 Must originales se rastrean con RF-07a/b; RF-18/19 son correcciones añadidas. Estado funcional y límites: Trazabilidad_RF_RB.md. No se contabilizan Won't como implementaciones.

### 3.2 Detalle de los requisitos críticos

Actor: estudiante para RF-01–11/19, operador técnico para RF-18. Precondición general: entorno local preparado y catálogo revisado; operaciones personales requieren sesión propia. El alta crea usuario + proceso en transacción. Flujo: acceder → responder → revisar resumen → declarar prioridades → buscar catálogo → revisar ficha → guardar/retirar → elegir par → comparar → salir/retomar → suprimir si decide.

RF-02–03: instrucciones visibles y escala; 12 respuestas obligatorias y originales; error por campo; guardado atómico; ciphertext asociado a UUID/ítem/versión; fallo de integridad no produce resultado. El promedio por par se explica y no se normaliza contra población. Datos: InterestResponse y versión del proceso; RB-02/06/09; RNF-S01/02 y RNF-U01/U02.

RF-04 y 12: una fila por dimensión; niveles 1–3 o ausencia; actualización transaccional; no existe prioridad por defecto. Comparación lee prioridades actuales; RB-06, RNF-M01/U02.

RF-05–06: datos públicos, búsqueda/campus/código; catálogo vacío o sin coincidencias ofrece limpiar filtros. Detalle distingue plan publicado sin año explícito y arancel/empleabilidad sin vigencia. Cada campo conserva Source; RB-03/04/07; RNF-R01/03 y RNF-C02.

RF-07a/b–08: incorporación idempotente; retiro solo de asociaciones del proceso autenticado; par válido se puede elegir entre ofertas activas y no depende de guardar exactamente dos. Selección igual/incompleta no sobreescribe el par anterior. RB-05/08, RNF-S02/R02.

RF-09–10: estructura de tres dimensiones numéricas más ubicación. Se calculan diferencias absolutas solo con mismo ciclo, unidad y período. Falta de valor genera mensaje, nunca 0. La prioridad resalta información y las preguntas guían conversación sin ordenar carreras. RB-01/04/07/09, RNF-U01/M01.

RF-11: consultas filtran propietario; UUID opaco no reemplaza permiso. Sesión expirada redirige a reautenticación; acceso ajeno devuelve 404 sin confirmar existencia. Guardados y comparación permanecen al salir. RB-08, RNF-S01/02/D02.

RF-18: CLI con validación en seco por defecto, archivo local, fuente permitida, fecha, ciclo 2027, código 13xxx, página y SHA; validación completa antes de escritura; transacción atómica; UNIQUE(código, ciclo); lote repetido actualiza sin duplicar. Actualización desactiva ofertas que salen del snapshot sin borrarlas. Fuente original y registro de importación se conservan. RB-03/04, RNF-C02/M01.

RF-19: página de consecuencias; confirmación literal; POST + CSRF; borrado del usuario en transacción con CASCADE del proceso; evento sin identidad. No se afirma purga retroactiva de todos los respaldos sin ejecución; política de retención 7 días del piloto debe implementarse antes de uso real. RB-10, RNF-S02/05.

## 4. Requisitos no funcionales

Se conservan los21 objetivos de E1 y se actualiza su justificación y medición. La tabla distingue cumplimiento local, evidencia parcial y condiciones pendientes. Los valores no son promesas de un establecimiento no inspeccionado.

### 4.1 Rendimiento y capacidad

| ID | Objetivo | Justificación | Método | Resultado | Veredicto |
| --- | --- | --- | --- | --- | --- |
| RNF-R01 | LCP ≤ 2,5 s; INP ≤ 200 ms; CLS ≤ 0,1, p75 de campo | Web Vitals; objetivo de experiencia, no SLA de servidor | PerformanceObserver en 12 pantallas; laboratorio local, n = 1/ruta/ancho | LCP máximo 48 ms; CLS máximo 0.0126; INP/campo sin muestra | Parcial: no afirmar p75 ni INP |
| RNF-R02 | p95 ≤ 1000 ms, 50 sesiones, 10 min | Presupuesto de 1 s por consulta/guardado repetido en clase de 45+5 | 50 VU autenticados, 70/30, 1 operación/s/VU, runtime aislado | p95 = 697.2 ms; 30000 operaciones | Cumple en local; ver duración exacta en JSON |
| RNF-R03 | 360 procesos y catálogo 2027 completo | 8 × 45 supuesto; snapshot oficial, no 91 carreras asumidas | Creación de 360 procesos; extracción y validación de 91 códigos/campus/ciclo | 360 procesos sintéticos, 91 ofertas, 3 campus | Cumple la capacidad local; pertinencia de atributos limitada |
| RNF-R04 | Fallos ≤ 1 % con 50 sesiones, 70/30, 10 min | Presupuesto máximo 1 fallo/100 operaciones; ajustar tras estudio | Estados HTTP y contrato funcional por operación; sin redirects contados como lecturas nuevas | 0/30000 fallos; 0 HTTP 5xx | Cumple en escenario local |

### 4.2 Disponibilidad y continuidad

| ID | Objetivo | Justificación | Método | Resultado | Veredicto |
| --- | --- | --- | --- | --- | --- |
| RNF-D01 | ≥ 99 % en ventana piloto declarada | No hay horario real de escuela; se retira 22 × 12 como hecho | Requiere monitor continuo y denominador de ventana publicada | No hay período de piloto publicado/observado | No acreditado: una respuesta health 200 no es disponibilidad mensual |
| RNF-D02 | RPO ≤ 24 h; RTO ≤ 4 h | Progreso no transaccional crítico; recuperación en jornada de uso | Snapshot SQLite consistente, AES-GCM, restauración, integrity/FK/check | RTO ejercicio = 0.496 s; snapshot de 0.488 s; 91 ofertas recuperadas | Parcial: RTO local cumple; periodicidad RPO 24 h sin operación |

### 4.3 Seguridad

| ID | Objetivo | Justificación | Método | Resultado | Veredicto |
| --- | --- | --- | --- | --- | --- |
| RNF-S01 | 100 % de los procesos con auth; caducados denegados | Aislamiento de proceso, potencial NNA | Casos de sesión válida/incorrecta/caducada y logout/login | Suite RF-01/RNF-S01; redirige a auth sin revelar proceso | Cumple los contratos probados, no auditoría exhaustiva |
| RNF-S02 | 0 accesos cruzados en lectura/edición/supresión | Cada cuenta solo su proceso | UUID ajeno GET/DELETE; POST con ID ajeno actualiza solo al propietario autenticado | 0 lecturas/borrados cruzados; edición no altera dueño ajeno | Cumple la suite negativa local |
| RNF-S03 | TLS en 100 % y repositorios cifrados antes de datos reales | Privacidad de historial; potencial NNA | Inspección de configuración; pruebas AES-GCM; revisión BD/runtime | HTTP loopback; respuestas cifradas, SQLite/prioridades no cifrados integralmente | No cumple en entorno real: demo solo datos ficticios |
| RNF-S04 | 0 secretos versionados/logs; eventos sin respuestas | Minimización y prevención de exposición | Revisión de archivos Git; runtime ignorado; logs de error con correlación | Claves fuera de Git; no respuestas ni credenciales en eventos; revisión estática | Cumple el alcance revisado; no garantía universal de ausencia |
| RNF-S05 | Finalidad, acceso, retención y supresión de datos reales | Normativa aplicable y derechos | Protocolo, RF-19, custodia y purga de respaldos del piloto | Finalidad/minimización/consentimiento propuestos; supresión activa probada | Parcial: sin estudio real ni purga operativa acreditada |

### 4.4 Usabilidad y accesibilidad

| ID | Objetivo | Justificación | Método | Resultado | Veredicto |
| --- | --- | --- | --- | --- | --- |
| RNF-U01 | Criterios WCAG 2.1 AA aplicables; analizar 2.2 | Acceso de usuarios heterogéneos | Axe 4.14.1, 12 pantallas, teclado, enlace salta-contenido | 0 violaciones automáticas; incompletos se conservan en JSON | Parcial: lector de pantalla y criterios manuales no acreditados |
| RNF-U02 | ≥ 80 % de participantes completan la comparación sin ayuda | Umbral de la guía del curso; con 5, 4/5 | Protocolo 5 tareas; CSV real y análisis rechaza vacíos | Sin observaciones de usabilidad de E3; encuesta E1 no es sustituto | Pendiente de usuarios externos reales |
| RNF-U03 | Español chileno; 360–1440 px | Dispositivos heterogéneos; caso móvil mínimo | E2E Chromium/Firefox, anchos 360/1440; axe y overflow | 4 recorridos PASS; 0 desbordes generales | Cumple en los anchos probados; zoom/lector manual pendientes |

### 4.5 Compatibilidad e interoperabilidad

| ID | Objetivo | Justificación | Método | Resultado | Veredicto |
| --- | --- | --- | --- | --- | --- |
| RNF-C01 | Flujo en dos familias de navegadores | Evitar dependencia de una familia escolar | Playwright Chromium y Firefox; alta → supresión | 4 recorridos completos PASS; versiones en e2e.json | Cumple en versiones/entorno probados |
| RNF-C02 | URL, ciclo, fecha y unidad en 100 % de los campos externos | Comparación trazable y homologable | Validación snapshot y Datum; PDF 91 ofertas; 3 extractos curados | 273 campos base con metadatos; 3 duraciones, resto NULL; hash scope explícito | Cumple el contrato de metadatos; faltantes se muestran |

### 4.6 Mantenibilidad y calidad interna

| ID | Objetivo | Justificación | Método | Resultado | Veredicto |
| --- | --- | --- | --- | --- | --- |
| RNF-M01 | 100 % de las RB críticas con caso; ≥ 80 % de ramas críticas | 10 reglas sensibles: integridad, agencia, permisos, datos | Coverage --branch y matriz RB → prueba | 24 tests; líneas 98.34 %; ramas 96.74 %; dominio 91,67 %, importador 100 % | Cumple en módulos críticos y trazabilidad definida |
| RNF-M02 | Cambios integrados con lint/formato/tests | Control de defectos al integrar cinco roles | GitHub Actions por push/PR y checks locales | CI remota 471dc2c success; SHA final se archiva aparte | Cumple con SHA verificado; no inferir futuros SHA |
| RNF-M03 | Errores con fecha/tipo/correlación sin datos | Depurar con privacidad | Fallo 404/503 inducido; header X-Request-ID y log | Correlación 32 caracteres; eventos DB con fecha/tipo; logs de servidor con fecha | Cumple el contrato observado; no observabilidad centralizada |

### 4.7 Portabilidad y despliegue

| ID | Objetivo | Justificación | Método | Resultado | Veredicto |
| --- | --- | --- | --- | --- | --- |
| RNF-P01 | Entorno reproducible por segundo integrante | Continuidad colaborativa | Runbook + CI limpia; reproducción humana independiente | Instalación CI automatizada pasa; otro integrante no ha registrado instalación | Parcial: CI no equivale a segundo integrante |
| RNF-P02 | Despliegue ≤ 30 min y rollback | Bloque de preparación antes de una sesión de 45 min; no normativa | CI instala, migra, importa, prueba; cronometraje humano/runbook | Pipeline y restauración ejecutados; sin instalación humana cronometrada | Parcial: método listo, segundo operador pendiente |

## 5. Requisitos de datos

### 5.1 Modelo de información

Campus, Career, Source, Offer, Datum, Process, InterestResponse, Priority, SavedOffer, Comparison, AuditEvent. Claves, dependencias, 3FN, integridad y diagrama en Ciencias_Ingenieria.md y docs/modelos. Catálogo: 91 ofertas, 3 campus, ciclo 2027; procesos de carga: 360 sintéticos; 12 respuestas por proceso. Crecimiento estimado lineal; las 5 alternativas por usuario son supuesto de dimensionamiento sin límite del producto. Calidad: unidades y períodos explícitos, NULL diferenciado, procedencia estable, validación atómica. Datos de desarrollo/demostración: cuentas y respuestas sintéticas; no se importan respuestas de encuesta como usuarios de producto.

### 5.2 Interfaces externas

Entrada: JSON local revisado schema 1, RF-18; sin subida pública ni URL que el servidor descargue a pedido. Campos de oferta: código, nombre, campus, ciclo, página; fuente: URL, título, fecha, SHA256. Datos adicionales curados en atributos_verificados.json con unidad, período y limitación. Salida: HTML por HTTPS en futuro piloto; HTTP loopback en demo; JSON de estado solo para propietario, sin respuestas en claro. No hay API de recomendación ni envío de datos a terceros.

### 5.3 Protección de datos y normativa

Incluso un alias puede ser dato personal si permite identificar a alguien. Finalidad: retomar exploración propia. La demo usa identidades inventadas. Se minimiza: no RUT, nombre, correo, fecha de nacimiento ni preguntas de salud. Si se ejecuta estudio real, consentimiento informado y protocolo aplicable se verifican previamente; el código local no constituye por sí solo una base de licitud.

Medidas implementadas: hasher Django, CSRF, propiedad de proceso, sesión 30 min, claves fuera de Git, permisos privados de runtime, cifrado AES-GCM de respuestas, logs mínimos, supresión propia. Medidas pendientes para datos reales: HTTPS, cifrado integral de almacenamiento/respaldos, gestión de claves, control operativo de acceso, retención y purga probada. El cifrado del campo no se presenta como cifrado de toda SQLite.

Retención de estudio propuesta: eliminar registros de contacto/consentimiento del sistema de análisis y datos identificables 30 días después del cierre académico; custodiar consentimientos por responsable definido fuera de Git; respaldos de piloto máximo 7 días. Al solicitar supresión se elimina estado activo y se aplica lista de borrados después de cualquier restauración. No hay despliegue real que acredite esa operación aún.

Derechos: consulta/rectificación por cuenta; supresión RF-19; canal al responsable a designar para oposición/portabilidad/acceso asistido. Ley 19.628 y reforma 21.719 se revisan al momento de actividad; texto BCN consultado indica vigencia diferida 01/12/2026, sin tratar proyectos de aplazamiento como ley. No se recolectan datos de NNA hasta aprobar el protocolo.

Licencias: Django BSD-3, cryptography Apache 2/BSD, fuentes OFL; marca UdeC con sus derechos originales, uso académico, no patrocinio; catálogo público citado, sin atribuir licencia abierta no verificada. Ficha original de 12 ítems puede reutilizarse bajo CC BY 4.0 por disposición del autor de este paquete; no hereda validez psicométrica. Registro de assets y dependencias adjunto.

## 6. Reglas de negocio

| ID | Regla | RF / prueba propietaria |
| --- | --- | --- |
| RB-01 | Apoya, sin decidir | RF-10; comparación sin veredicto |
| RB-02 | Intereses no son diagnóstico | RF-02/03; resumen original con límites |
| RB-03 | Carrera distinta de oferta por campus/ciclo | RF-05/18; código/ciclo único |
| RB-04 | Proveniencia verificable; NULL ≠ 0 | RF-06/09/10; faltantes y fuentes |
| RB-05 | Par exactamente dos distintas | RF-08; formulario y CHECK |
| RB-06 | Prioridades explícitas, sin valor inventado | RF-04/12; ausencia permanece NULL lógico |
| RB-07 | Indicadores contextuales no garantizan futuro | RF-06/10; período/compatibilidad |
| RB-08 | Persistencia aislada por titular | RF-11; acceso cruzado denegado |
| RB-09 | Sin match numérico global | RF-03/10; dimensiones separadas, sin ranking |
| RB-10 | Supresión y seguridad | RF-19; eliminación en cascada |

## 7. Ética, contexto social y sostenibilidad

### 7.1 Salud, seguridad y bienestar

El riesgo es influir indebidamente en una decisión con efectos personales/económicos. Mitigación: sin diagnóstico ni ganadora, limitaciones visibles, fuentes, faltantes y supervisión humana. Riesgo residual: malinterpretar un promedio autodescriptivo o indicador histórico; se evalúa comprensión en la validación y se elimina cualquier texto prescriptivo.

### 7.2 Factores sociales, culturales y globales

Puede excluir a quien no dispone de conectividad, navegador, lectoescritura o apoyo accesible. Español chileno, etiquetas, teclado, móvil y sesión facilitada sin hacer la tarea por el participante. No se extrapola muestra local ni se infiere preferencia por género, origen o nivel socioeconómico. La orientación humana se complementa, no se automatiza su función.

### 7.3 Factores ambientales y sostenibilidad

Monolito local, 91 registros, sin modelo IA ni entrenamiento; evitar servicios encendidos innecesarios. No se cuantifica ahorro de CO2 sin medición. Continuidad requiere responsable, catálogo actualizado y presupuesto acordado; en su ausencia, se archiva la versión académica y se eliminan datos.

### 7.4 Factores económicos

Caja incremental nueva 0 CLP, hardware existente; no significa costo total 0. Costo de oportunidad y estimación original se distinguen de HH humanas y gasto pagado. No se atribuyen ingresos, ahorros de abandono ni disposición de compra desde encuesta. Costos_Riesgos_Plan.md mantiene fórmulas y sensibilidad.

## 8. Espacio de soluciones y decisión

ALT1: monolito Django, catálogo y estado propios; operación integrada con control local; menor complejidad para 5 roles. ALT2: frontend/backend/BD separados; mayor independencia y costo de integración. ALT3: integrar proveedor vocacional y datos oficiales; licencia, API, consentimiento y costos externos por verificar. La matriz ponderada E2, sus pesos, notas y sensibilidad permanecen en docs/antecedentes/Dossier_E2_Completo.md, con 70/100 h de escenarios y restricciones originales, no cotizaciones.

Se mantiene ALT1 por alcance/control, cambiando la persistencia en blob PoC a modelo relacional. La incertidumbre que decide E3 es el recorrido integrado, importación, supresión, carga y utilidad. Las iteraciones I1–I3 describen alternativas actuales y efectos. No se declara una nueva votación del equipo ni adquisición de un proveedor.

## 9. Priorización, plan, presupuesto y equipo

### 9.1 MoSCoW y MVP

Must: RF-01–11 (07a/b), 18, 19. Should: 12a/b, 13; implementados al compartir estado y diseño del recorrido. Could: 14; fuera del corte. Won't: 15–17. Justificación: Must cubre decisión informada y derechos; Should mejora revisión sin sistema adicional; Could/Won't no condicionan E3. MVP demostrable: acceso → intereses → prioridades → catálogo → par → comparación → recuperación y supresión.

### 9.2 Hitos y carta Gantt

Línea base: E1 S9, E2 S11, MVP S13, E3 S14, E4 S17, E5 S17–18. Corte 16/11 S15 posterior a la S14: se reporta retraso, no prórroga. Replanificación: cerrar técnica local y respuesta docente S15; validar usuarios/cerrar controles S15–16; congelar Must y redactar E4 S17; ensayar y demostrar E5 S17–18. Responsables sugeridos por rol, falta confirmación de compromisos reales. Gantt y dependencias en Costos_Riesgos_Plan.md.

### 9.3 Presupuesto y recursos

Original: 400 HH plan + 100 holgura; 9.240.000 CLP valorizados + 100.000 caja. Corrección: tarifa uniforme referencial 13.736–16.484 CLP/h derivada de fuente pública y 182 h/mes; 400 h = 5.494.400–6.593.600 CLP. No es sueldo ni contratación. Esta ejecución no efectuó compras ni contrató hosting; 0 CLP incremental. HH históricas ejecutadas no aportadas; no se calcula desvío humano ni saldo de plan inventado. Registro actual: commits, comandos y evidencia técnica, distintos de tiempo académico humano.

### 9.4 Equipo y roles

Jorge Alejandro Slimming Lagos: gestión/contexto; Benjamín Alonso Henríquez Cid: arquitectura/integración; Diego Alejandro Gutiérrez Mendoza: calidad; Mauro Sebastián Muñoz González: datos/privacidad; Lucas Daniel Morales Oyanedel: operación/costos. Nombres completos y responsabilidades históricas en SRS original. Las asignaciones de guion E3 son propuestas; no acreditan autoría de commits, asistencia a reuniones ni HH. Conducción de reuniones y contribución distribuida requieren registros reales.

## 10. Aceptación y validación

DoD técnico: contratos Must automatizados; flujo navegador con persistencia; catálogo con fuente; pruebas negativas de permisos/CSRF/cifrado/supresión; medición RNF y defectos registrados; CI verde del SHA publicado; instrucciones reproducibles. DoD académico adicional: validación externa real, comprensión del material, ensayo cinco voces y entrega oficial. No se marca DoD humano desde un render.

Pruebas de alto nivel: alta/retorno; 12 respuestas válidas; prioridad vacía/alta; catálogo filtrado/fuente; guardado duplicado/retiro; par igual rechazado; faltante o período incompatible; recuperación; supresión y acceso ajeno. Herramientas: unittest Django, coverage, Playwright, axe y prueba de carga HTTP. Validación: instrumento de tareas, consentimiento, CSV y análisis descritos por separado.

## 11. Trazabilidad

Necesidad → RF → RNF → RB → componente → prueba → resultado en Trazabilidad_RF_RB.md. Problema con fuentes en §2.3; requisitos §3–4; implementación orienta/; pruebas tests/ y herramientas/; evidencia en JSON/logs/navegador; estado R3 en Cobertura_R3.md. Los archivos de resultados identifican método/entorno/denominador; no equivalen a CI remota o validación humana.

## 12. Riesgos y supuestos

Registro actualizado con 10 riesgos en Costos_Riesgos_Plan.md: catálogo/períodos; utilidad; privacidad/NNA; disponibilidad de usuarios; concurrencia SQLite; dependencias; disponibilidad del equipo; aprobación/formato; costos/continuidad; tiempo de demo. Cada caso tiene probabilidad, impacto, disparador, mitigación, estado y residual. Riesgos materializados verificables: ausencia E3 en origen; CSRF legítimo rechazado; descarga páginas 403; faltantes de período; error accesibilidad detectado por axe. No se atribuyen incidentes no observados.

## 13. Aprobaciones

| Rol | Nombre/constancia | Estado |
| --- | --- | --- |
| Gestión del equipo | Jorge Alejandro Slimming Lagos, según asignación E1 | Revisión y firma real no aportadas |
| Líder técnico | Benjamín Alonso Henríquez Cid, según asignación E1 | Paquete preparado con IA; aceptación grupal pendiente |
| Docente / alcance | No se adjuntó propuesta aprobada | Evidencia necesaria; no se reemplaza con admisibilidad |

## 14. Anexos

A: instrumentos y datos originales en SRS E1, con limitaciones de muestra y corrección Q13A. Q13A mide disposición monetaria declarada; códigos históricos 0 = 15–30 mil, 1 = $0, 2 = 30–50 mil, 3 = $15 mil, 4 = 5–15 mil, 5 = $30 mil, 6 = $5 mil, 7 = >50 mil. Rangos/puntos exactos se solapan; sin formulario original no se recodifica ni se estima promedio/precio. El diccionario tipado corregido está en data/diccionario_Q13A_corregido.csv: distingue categorías de rango, punto y no pago, sin tratarlas como una escala ordinal.

B: Validacion_Usuarios.md e instrumentos/CSV sin filas inventadas; ficha TI y consentimiento. C: Bitacora.md: hechos de esta ejecución y plantilla de actas reales; no asistencias ficticias. D: Gantt en Costos_Riesgos_Plan.md. E: Declaracion_IA_Licencias.md. F: propuesta aprobada/constancia no aportada; fundamentación de admisibilidad queda como antecedente distinto. G: diagramas C4, ER, secuencia y capturas reales. H: consentimientos reales, en custodia fuera del repo, pendientes si hay validación. I: interfaz JSON documentada y CLI, no API pública general. J: glosario §1.3.

Checklist de consistencia: 14 secciones presentes; fuentes con fecha/límite; 4 perfiles; 7 restricciones con alternativa; 2 ciencias desarrolladas; RF atómicos e importación/supresión; 21 RNF con estado; MoSCoW real; 10 riesgos; aprobaciones y validaciones sin fabricar.
