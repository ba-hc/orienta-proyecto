# Respuesta docente e iteraciones verificadas

Corte: 16/11/2026. Base: orienta-grupo9 main a 92f1fd3cfea061543cf14557320120793b32eb1. Fuente de observaciones: transcripción del usuario en docs/fuentes/Comentarios_Docentes.md. El escrito y la PDR se distinguen: el oral 1 aportó puntajes, sin comentario cualitativo adicional. No se atribuyen estas correcciones a una observación oral que no fue aportada.

## Respuesta una a una al escrito (intento 2)

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

## Respuesta a la PDR / oral 1

Puntajes aportados: C1 = 3,00; C2 = 3,50; C3 = 3,00; C4 = 3,50; C5 = 3,50; C6 = 3,00; C7 = 2,50; P = 3,19; nota 5,4. Se conserva el dato tal como se recibió, sin recalcularlo con redondeos de la tabla visible. Acciones para E3: elegir el problema y límites en 60 s, mostrar el sistema real, respaldar arquitectura con CI1/CI2 y mediciones, reemplazar láminas densas por resultados verificables, ensayar con cinco voces y demo acotada. Son decisiones del equipo asistidas por IA; no son citas de la profesora. Falta adjuntar cualquier comentario cualitativo adicional de la PDR si existiera.

## Iteración I1 · Del blob PoC al modelo relacional integrado

Disparador: revisión docente C3 y evidencia de PoC con guardados/par en un único JSON; no podía verificar importación ni supresión del producto. Alternativas: conservar todo en JSON; usar modelo relacional normalizado; separar microservicios. Decisión: Django con claves, FK, UNIQUE, CHECK y transacciones. Se mantienen el monolito y el recorrido de E2 por su tamaño/costo; se descartan microservicios por complejidad operativa.

Efecto verificado: lote repetido mantiene número de ofertas; lote duplicado falla sin efectos; guardado repetido no duplica; autocomparación falla en BD; supresión del titular elimina dependencias y conserva catálogo. Evidencia: la suite tests/test_workflow.py y migración 0001. Esta es una iteración estructural de diseño, no solo avance de implementación.

## Iteración I2 · Procedencia por campo y faltantes seguros

Disparador: catálogo 2027 era precondición sin proceso de carga; páginas públicas mezclan admisión 2027 con arancel 2026/indicadores sin cohorte. Alternativas: rellenar con estimación; incorporar todas las cifras como 2027; publicar únicamente campos verificables y señalar faltantes. Decisión: snapshot de 91 ofertas con código, campus, ciclo, fuente, página y hash; 3 duraciones de páginas oficiales con límite de vigencia; sin arancel/empleabilidad cuando período no es comprobable. Se conserva comparación sin ganador.

Efecto verificado: 91 códigos/ciclo únicos y 3 campus; importador valida dominio, fecha, hash, código, ciclo y duplicados antes de la transacción; comparación no convierte NULL en 0 y rechaza períodos incompatibles. Evidencia: data/catalogo_udec_2027.json, datos curados y pruebas RF05/06/09/10/18. Sacrificio: menos cifras; beneficio: no presentar datos incompatibles como comparables.

## Iteración I3 · Integración real de formularios y CSRF

Disparador: backend pasaba, pero Chromium devolvió 403 al crear la cuenta. Inspección del POST: Origin:null con Referrer-Policy:no-referrer; Django rechazó el origen. Alternativas: excluir CSRF o aceptar origen nulo; conservar validación y usar política same-origin. Decisión: política same-origin, sin modificar CsrfViewMiddleware ni decoradores de mutación.

Efecto inicial observado: el mismo alta cambió de 403 a 302 y llegó al proceso. Verificación posterior: E2E completo en dos navegadores y suite CSRF con token ausente 403. La evidencia negativa se registra en Defectos.csv. No se califica como explotación: fue un fallo de compatibilidad que bloqueaba una acción legítima.

## Tres intercambios defendibles

1. Se sacrifica completitud numérica para conservar procedencia/período y evitar inferencias falsas.
2. Se sacrifica escalado multiinstancia inmediato para lograr instalación local, control de datos y demo sin terceros; SQLite se evalúa con carga, PostgreSQL queda condicionado.
3. Se sacrifica un puntaje vocacional atractivo para proteger agencia del estudiante: ficha autodescriptiva sin baremos, diagnóstico ni ranking.
