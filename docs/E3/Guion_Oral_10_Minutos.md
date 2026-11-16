# Guion de exposición E3 · 10 minutos + 5 de preguntas

El enunciado fija 10 + 5; la rúbrica menciona 12. Se usa el límite más estricto de 10. La distribución es una propuesta de preparación por los roles originales, no una constancia de ensayo. Todos deben comprender el sistema completo. No mostrar nombres de cuentas, claves, consolas de secretos ni datos personales reales.

| Lámina | Intervalo | Voz propuesta | Mensaje / transición |
| --- | --- | --- | --- |
| 1 | 00:00–00:35 | Jorge | Problema, alcance y pregunta de E3 |
| 2 | 00:35–01:20 | Jorge | Evidencia local, fuentes públicas y corrección docente |
| 3 | 01:20–02:20 | Benjamín | Iteraciones con disparador y efecto |
| 4 | 02:20–03:00 | Mauro | CI1: modelo y anomalías evitadas |
| 5 | 03:00–03:40 | Mauro | CI2: credenciales, cifrado, permisos y límites |
| 6 / navegador | 03:40–06:10 | Benjamín | Demostración real con persistencia |
| 7 | 06:10–07:00 | Diego | Pruebas, cobertura, defectos y CI |
| 8 | 07:00–07:40 | Diego | RNF medidos y desviaciones |
| 9 | 07:40–08:20 | Diego | Validación: datos reales existentes y límites |
| 10 | 08:20–09:00 | Lucas | Presupuesto estimado/ejecutado |
| 11 | 09:00–09:35 | Lucas | Riesgos y replanificación |
| 12 | 09:35–10:00 | Jorge | Estado y compromisos verificables |

## 1 · Apertura (35 segundos)

«Orienta ayuda a un estudiante a revisar dos ofertas de educación superior con sus prioridades y con información que puede comprobar. La decisión sigue siendo del estudiante: no hay diagnóstico ni carrera ganadora. En esta revisión mostramos qué cambió desde el diseño, qué funciona y qué evidencia tenemos. La demostración es local y usa respuestas inventadas; el catálogo proviene de la publicación oficial 2027».

## 2 · Problema y respuesta docente (45 segundos)

«La encuesta original describe una necesidad de nuestra muestra, no una prevalencia nacional. Reanalizamos sus 156 registros estudiantiles y 36 de apoderados sin inventar respuestas. Como contexto público, SIES informa 77,9 % de retención en la cohorte 2025; la no continuidad no equivale automáticamente a indecisión. También contrastamos MiFuturo, Acceso, EligeCarrera y VocationOne. Corregimos los requisitos de importación y supresión, los costos y los supuestos del escenario. Las cifras de capacidad siguen declaradas como supuestos».

## 3 · Iteraciones (60 segundos)

«La primera iteración respondió a una limitación real de la PoC: el estado estaba en un JSON y no existía importación del catálogo ni supresión verificable. Consideramos conservarlo, separar servicios o normalizar en el monolito. Elegimos claves, restricciones y transacciones; las pruebas muestran rechazo de duplicados y borrado en cascada sin eliminar el catálogo.

La segunda surgió al revisar fuentes: una página puede mezclar ofertas 2027 con cifras sin período. Elegimos publicar solo valores verificables y mostrar lo que falta, en vez de rellenarlo. El snapshot contiene 91 códigos con campus, ciclo y fuente.

La tercera vino del navegador: el alta legítima recibía 403. Identificamos un Origin nulo por la política de referencias; usamos same-origin manteniendo CSRF. El mismo alta funcionó después».

## 4 · CI1 (40 segundos)

«La normalización fue una decisión de diseño aplicada. Código y ciclo identifican una oferta; oferta y dimensión identifican un dato; proceso y oferta identifican un guardado. Las fuentes tienen identidad por URL y hash, de modo que una nueva revisión no borra la anterior. Las dependencias declaradas justifican la descomposición en 3FN. Las pruebas no demuestran por sí solas la normalización: verifican sus consecuencias, como unicidad, integridad y supresión sin perder datos públicos».

## 5 · CI2 (40 segundos)

«Las contraseñas usan el hasher adaptativo de Django y las consultas usan siempre el propietario autenticado. Las respuestas se protegen con AES-256-GCM, nonce aleatorio y datos asociados al proceso, ítem y versión. Probamos alteración de etiqueta y traslado entre procesos: ambos se rechazan. También credenciales incorrectas, caducidad y CSRF. Este cifrado de campo no es cifrado integral de SQLite; TLS y controles operativos siguen siendo condiciones para usar datos reales».

## 6 · Demostración (150 segundos)

Aplicar el runbook de Guion_Demo.md. No improvisar explicación técnica mientras se teclean valores.

«Entramos con un alias de prueba. Aquí están nuestras 12 respuestas y el resumen: es una descripción de actividades, no un test psicológico. Marcamos una prioridad; lo no indicado queda sin definir. Buscamos dos códigos del catálogo 2027 y revisamos su fuente. Guardamos ambas ofertas. Elegimos exactamente dos distintas. La comparación muestra duración, prioridad, procedencia y faltantes; no se calcula un ganador. Salimos y retomamos para mostrar persistencia. El control de supresión pertenece solo a esta cuenta».

Si crear cuenta/responder consume más de 35 s, usar el proceso de prueba ya preparado y decir que estaba precargado; no fingir que se creó en vivo. La prueba automatizada cubre alta y persistencia, pero la demo debe mostrar la acción real que se está ejecutando.

## 7 · Verificación (50 segundos)

«La suite ejecuta contratos de entrada, permisos, persistencia, comparación, supresión e importación. Coverage reporta líneas y ramas; los resultados exactos están en el paquete y corresponden al código probado. El flujo se ejecutó en Chromium y Firefox, a 360 y 1440 píxeles, con recuperación y borrado. Axe detectó una etiqueta cuyo nombre accesible no incluía el texto visible; la corregimos y repetimos las pantallas afectadas. La CI remota se identifica por SHA y URL; no se confunde con un check local».

## 8 · RNF (40 segundos)

«La carga usa 50 sesiones autenticadas y 360 procesos sintéticos, con 70 % lecturas y 30 % guardados, durante 10 minutos. Presentamos el p95 y los errores obtenidos, junto al entorno y los 30.000 eventos. La restauración verifica integridad y recuperación sobre una copia cifrada. Estos resultados son locales: no prueban latencia escolar, 99 % mensual, Web Vitals de campo o WCAG completa. Los veredictos parciales quedan marcados y condicionan el piloto».

## 9 · Validación (40 segundos)

«Tenemos evidencia humana histórica de necesidades: los 192 registros desidentificados del E1, recalculados con instrumento y frecuencias. Esa encuesta no es una prueba de usabilidad de E3. El protocolo de uso ya define cinco tareas y criterios de éxito sin ayuda, tiempos, errores y comprensión de faltantes/sin ganadora. No presentamos sesiones ni resultados inexistentes. El análisis rechaza una planilla vacía. Si aún no fueron ejecutadas, esa es una brecha real del criterio, no un porcentaje cubierto por bots».

## 10 · Costos (40 segundos)

«La línea base era 400 horas planificadas y CLP 100.000 de provisión. Las HH humanas ejecutadas no recibieron bitácoras y no las inventamos. Este trabajo no efectuó compras nuevas: usó el equipo existente. Eso no significa costo total cero. Para la valorización retiramos el diferencial sin fuente por rol y usamos una sensibilidad basada en ingreso publicado y jornada de 42 horas. Es un costo de oportunidad referencial, no un honorario cotizado ni un gasto pagado».

## 11 · Riesgos y plan (35 segundos)

«Los riesgos que se materializaron incluyen faltantes de vigencia, descarga 403, el problema CSRF y el nombre accesible. Cada uno tiene acción y prueba posterior. El corte llega después de la S14 del calendario: no reescribimos el plazo. Priorizamos Must, validación y controles; quedan fuera exportación, chat, panel y ranking. Para E4/E5 hacen falta usuarios reales, segundo operador, ensayo compartido y decisión de continuidad».

## 12 · Cierre (25 segundos)

«Hoy existe un recorrido persistente con catálogo oficial y verificación reproducible. Las decisiones están ligadas a observaciones y pruebas, con sus límites. El repositorio separa lo construido, lo medido y lo que requiere evidencia humana. Podemos mostrar el flujo y explicar por qué su diseño cambió. Quedamos atentos a las preguntas».

## Ensayo y preguntas

Hacer un ensayo real con cronómetro, registrar tiempos observados y ajustes sin rellenar datos ficticios. Si se excede 10 min, recortar ejemplos antes que la evidencia. Todos deben responder al menos una pregunta de otro rol usando Preguntas_Defensa.md. La exposición humana y su fluidez no se acreditan mediante este archivo.
