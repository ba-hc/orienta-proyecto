# Costos, riesgos y replanificación E3

Corte: 16/11/2026, semana de referencia S15. La línea base del curso fijaba E3 en S14. El presente trabajo documenta el atraso; no supone una prórroga ni una nueva fecha oficial de entrega.

## Presupuesto estimado y ejecución acreditada

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

## Corrección de la valorización horaria

Se retira el diferencial no fundamentado de CLP 20.000–27.500 por rol. Referencia: Admisión UdeC cita MiFuturo para Informática y publica un rango de ingreso al 4.º año de CLP 2,5–3,0 millones mensuales. DT documenta jornada de 42 h/semana desde el 26/04/2026. Se adopta 182 h/mes = 42 × 52 / 12 solo como conversión de sensibilidad.

Tarifa referencial = ingreso mensual / 182: CLP 13.736–16.484 por hora (redondeo al peso). Para 400 HH: CLP 5.494.400–6.593.600, más desembolsos que se acrediten. Todos los roles usan el mismo rango para evitar aparentar salarios de mercado por especialidad sin fuente. La referencia es un ingreso de egresados, no honorario cotizado; no incluye impuestos/costos de contratación. No se usa como remuneración pagada ni compromiso comercial.

Costo futuro: no hay operación contratada ni responsable aceptado. Alternativa A, mantener demo local: recursos existentes y horas que el responsable debe acordar. Alternativa B, servicio público: cotizar infraestructura, TLS/almacenamiento cifrado, respaldo, monitoreo y mantención antes de asumir caja mensual. La proyección E1 de CLP 123.250/mes no se presenta como precio confirmado. Los beneficios potenciales de claridad/tiempo se validan con personas; no se monetiza retención evitada sin evidencia causal.

## Riesgos actualizados

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

## Replanificación y criterio de recorte

| Ventana de referencia | Compromiso propuesto | Dependencia | Coordinación propuesta | Criterio de salida / holgura |
| --- | --- | --- | --- | --- |
| S15, corte actual | Código, RF18/19, catálogo, 2+ iteraciones, pruebas/RNF y paquete E3 | Fuentes y comentarios ya aportados | Benjamín + QA | Flujo local y CI verificados; margen para defectos bloqueantes |
| S15–16 | Validación externa con instrumento; control de entorno y protocolo | Usuarios/consentimiento y responsable real | Diego + Mauro | Evidencia real y conclusiones; si falta, no declarar éxito |
| S16 | Cerrar Must y defectos; verificar accesibilidad manual y segundo operador | Pruebas y hallazgos | Equipo | Sin bloqueantes; repetir solo lo afectado |
| S17 | Informe E4, proveniencia, costos ejecutados y continuidad | Evidencias consolidadas | Jorge + Lucas | Revisión cruzada y entrega oficial |
| S17–18 | Ensayo cinco voces y demo E5 | Must estable, respaldo, comprensión | Todos | 15 min E5 + preguntas según guía; E3 se mantiene 10 + 5 |

Son propuestas de coordinación, no horas ya trabajadas ni tareas aceptadas por personas. Se deja fuera RF14 (exportación), panel institucional, chat IA, ranking y expansión a otras instituciones. Criterio: priorizar recorrido verificable, derechos y calidad antes de nuevas funciones. Si no hay responsables para un piloto, se entrega demo local y plan de retiro; no se improvisa operación con datos reales.
