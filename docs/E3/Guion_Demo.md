# Guion de demostración en vivo · 2 minutos 30 segundos

## Preparación antes de la exposición

1. Ejecutar instalación, migraciones, importación y enriquecimiento según README. Verificar /health/ y abrir http://127.0.0.1:19039/acceso/. Utilizar una cuenta ficticia y una contraseña distinta de las personales.
2. Dejar disponible una segunda ventana para comprobar retorno. Si se precargan las 12 respuestas, declararlo al comenzar. Conservar las credenciales solo en almacenamiento privado local, nunca en las diapositivas ni en Git.
3. Verificar filtros 13073 y 13086, prioridad de duración, comparación y página del PDF. Mantener descargada la fuente para no depender de internet.
4. Probar el proyector, tamaño del texto y foco de teclado. Cerrar pestañas ajenas y consolas con información privada. Abrir la presentación y tener el dossier como respaldo.

## Ejecución cronometrada

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

## Contingencias

Si aparece un error de campo, corregirlo sin reiniciar todo el proceso y explicar la validación. Si se olvida la contraseña ficticia, usar una cuenta de respaldo comprobada o crear otra y declarar la contingencia. Si cae el servidor, ejecutar el script local y verificar /health/. Si la recuperación consume el tiempo, continuar la explicación y aplicar la contingencia que autorice la docente: una captura o video no sustituye por defecto el software en ejecución. Si una fuente remota falla, abrir el PDF conservado y su página; el catálogo local sigue funcionando.

## Respaldo y restauración

El ejercicio herramientas/medir_restauracion.py trabaja sobre una copia temporal consistente, verifica integridad del cifrado, integrity_check, foreign keys y Django.check. No restaura sobre cuentas vivas. No demuestra periodicidad de 24 horas: para un piloto se debe implementar y probar retención, supresión tras restauración y custodia de claves.

## Registro de ensayo

Completar solo después de un ensayo real: fecha, participantes, duración observada, incidencias, recortes y responsable. El E2E automático demuestra funcionamiento, no fluidez de una exposición humana.
