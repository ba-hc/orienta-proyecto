# Validación con usuarios · protocolo listo para ejecución

**Estado: no se aportaron resultados de sesiones reales.** Las encuestas de E1 describen el problema; las pruebas de software, bots y evaluadores de IA no son validación con estudiantes. Este documento prepara el estudio y el análisis sin completar filas ficticias.

## Objetivo y muestra

Establecer si estudiantes del perfil comprenden el propósito, encuentran información y completan la comparación sin ayuda. Muestra intencional de 5 personas ajenas al equipo, preferentemente mayores de 18 años en transición a educación superior. Registrar criterios de inclusión y dispositivo, sin nombre, RUT, correo ni datos sensibles en la planilla. Si solo se consiguen 3 participantes se informa n = 3, sin cambiar el denominador para alcanzar el objetivo. No demuestra representatividad ni reducción de cambios/abandono de carrera.

## Preparación y consentimiento

Antes de contactar: designar responsable humano, habilitar un entorno adecuado al régimen de datos y acordar custodia/retención. La demo actual usa loopback y datos inventados; una prueba local supervisada puede pedir que la persona use una identidad ficticia y respuestas ficticias, pero el registro del estudio sigue requiriendo consentimiento. No usar este entorno para información personal real de menores. Para NNA se revisarán autorización, consentimiento/asentimiento y protocolo institucional antes de la sesión.

Texto propuesto: «Te invitamos a probar una aplicación académica durante 15–20 minutos. Participar es voluntario; puedes omitir preguntas o retirarte. Usarás un alias y respuestas inventadas. Registraremos éxito, tiempo, errores y comentarios anonimizados. No es un test psicológico ni una asesoría de admisión. No grabaremos audio/video ni datos sensibles sin permiso separado. Los datos identificables se eliminarán 30 días después del cierre académico; puedes solicitar el retiro de tu registro mediante el código que recibirás». Completar responsable/canal/fechas reales antes de usar; no inventar firma o aceptación.

## Parte 1 · Concepto y requisitos (5 minutos)

Preguntar, sin inducir respuesta: ¿cómo comparas hoy dos alternativas? ¿Qué información buscas y dónde? ¿Qué entiendes que hará esta aplicación? ¿Qué te preocuparía al guardar tu avance? ¿Qué otra herramienta usarías? Clasificar necesidades, expectativas y malentendidos; contrastar con RF y con soluciones existentes. Registrar verbatim breve con permiso y sin identidad. Separar este estudio de concepto del estudio de tareas, aunque una persona participe en ambos.

## Parte 2 · Tareas de uso (máximo 10 minutos)

T1. Crear un proceso con identidad inventada y completar la ficha con valores de prueba.

T2. Marcar duración como alta y ubicación como media; explicar qué crees que cambia.

T3. Encontrar Informática 13073 y Medicina 13086, revisar fuente/ciclo y guardarlas.

T4. Compararlas. Identificar la diferencia de duración, un dato no disponible y si existe una ganadora.

T5. Salir, retomar con la misma cuenta y comprobar estado. Finalmente localizar la opción de eliminación; ejecutarla solo en la cuenta ficticia propia.

Facilitador: leer la tarea sin indicar qué control usar; iniciar reloj al terminar de leer; parar al criterio de aceptación; registrar ayuda solicitada o entregada. Si intervienes para completar, la tarea no cuenta como éxito sin ayuda. Un error corregido por el propio participante se registra y puede coexistir con éxito sin ayuda. Corte a 10 min; tarea abandonada cuenta como no completada.

## Instrumento de observación

Archivo data/validacion_usuarios.csv, una fila por participante y tarea. Campos: participant_id (P01..P05), perfil, mayor18 (si/no), consentimiento_registrado (si/no), dispositivo, tarea (T1..T5), completada (si/no), ayuda (si/no), segundos, errores, comentario. El CSV entregado solo tiene encabezados. Custodia de consentimientos fuera de Git, con responsable humano. No se recogen contraseñas ni respuestas personales.

## Preguntas finales

¿La ficha te dijo qué carrera elegir? ¿Qué significa un dato no disponible? ¿Cuál es la fuente de la duración? ¿Qué cambiarías primero? ¿En qué parte necesitarías ayuda? Valorar confianza de 1 a 5 solo como descripción, sin convertirla en prueba de precisión del sistema.

## Análisis previsto y regla de decisión

Éxito principal por persona: T4 completada sin ayuda y explicación correcta de ausencia de ganador/faltantes. RNF-U02: al menos 80 %; con n = 5 requiere 4/5, con n = 3 requiere 3/3. Informar numerador, denominador y límites. Por tarea: éxitos, ayudas, errores; tiempos con mediana y rango. Si hay menos de 3 registros externos válidos, el estudio no acredita el criterio. No reemplazar faltantes por éxitos ni excluir abandonos del denominador sin justificarlo.

El análisis se genera con herramientas/analizar_validacion.py, que rehúsa producir resultados si solo hay encabezados. Las conclusiones deben separar observación, interpretación y cambio de diseño. Un comentario aislado orienta una hipótesis; no se generaliza a toda la población. Si menos de 4/5 completan T4 sin ayuda o alguien interpreta el resultado como diagnóstico, se reabre el diseño y se vuelve a probar lo afectado.

## Ficha de infraestructura del escenario

Registrar establecimiento o tipo anónimo, responsable de TI, cantidad de equipos disponibles/simultáneos, navegadores/versiones, conectividad medida en el horario, política de cuentas, disponibilidad de asistencia y ventana real de uso. Anexar método/fecha/autorización. Hasta obtener esta ficha, 8 cursos, 50 sesiones y horario del piloto son supuestos de capacidad, no hechos de un colegio.

## Cierre pendiente

Adjuntar registros reales anonimizados, análisis, decisiones y consentimiento custodiado; revisar entorno y retención; ejecutar ensayo con cinco voces. El agente no puede producir estas evidencias humanas por sustitución.
