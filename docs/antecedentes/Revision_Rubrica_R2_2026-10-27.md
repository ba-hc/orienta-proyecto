# Revisión de la rúbrica R2 · Orienta E2

**Fecha:** 27 de octubre de 2026. **Fuentes:** [rúbrica R2, páginas 4–5](../../docs/curso/Rubricas_Proyecto_Semestral.pdf), [enunciado E2, páginas 7–8](../../docs/curso/Enunciado_Proyecto_Semestral.pdf) y [SRS E1](../E1/Orienta_E1_Grupo9_Informe_SRS.pdf). Se revisaron el PPT de entrega de 22 láminas, el PPT de exposición de 15 y los guiones de los cinco integrantes.

| Criterio | Peso | Evidencia y localización | Resultado de la revisión |
| --- | --- | --- | --- |
| C1 · Problema, requisitos y restricciones | 10 % | Lámina 2; SRS pp. 6–10. Cinco RF conectados al diseño, restricciones, escenario y encuesta. | Cubierto en el material. Las cifras se presentan como alta identificación en escala 4–5, con muestra no probabilística. |
| C2 · Análisis, datos y ciencias de ingeniería | 18 % | Láminas 3–4 y respaldo 15; modelo lógico y reporte de integridad. | Cubierto en el material: dominio, claves y normalización; volumen y concurrencia con supuestos; ley de Little y criptografía con límites. Los 23 contratos se repitieron con SQLite en memoria. |
| C3 · Múltiples soluciones | 18 % | Lámina 5 y dossier, sección 3. | Cubierto en el material: tres opciones distintas, comparables en arquitectura, tecnología, operación, esfuerzo y costo estimado. La licencia y el acceso del tercero están sin verificar. |
| C4 · Evaluación y decisión | 20 % | Láminas 6–7 y respaldos 16–18; CSV/XLSX y dossier, sección 4. | Cubierto en el material: requisitos, pesos y su fundamento, 21 notas justificadas, descartes y sensibilidad. Totales 3,95 / 3,60 / 2,20 y cuatro escenarios recalculados. |
| C5 · Arquitectura y rigor de modelos | 12 % | Láminas 8–9; dossier, sección 5. | Cubierto en el material y en la exposición: C4 L1/L2/L3, fronteras y tecnologías, UML de secuencia y vínculo con RNF. El UML muestra el diseño previsto, no una traza medida. |
| C6 · Riesgos e intercambios | 10 % | Láminas 11–13 y respaldo 21; dossier, secciones 7–8. | Cubierto en el material: tres sacrificios con beneficio y restricción; cinco riesgos priorizados con disparadores y mitigaciones; PoC local revalidada 15/15. |
| C7 · Exposición y preguntas | 12 % | Láminas 1–14 de exposición, referencias, [guion del equipo](Guion_E2_Equipo.pdf) y [preguntas](Preguntas_Defensa_E2.pdf). | Material preparado para cinco integrantes y 600 segundos planificados. **Falta demostrarlo en un ensayo y en la defensa:** fluidez, tiempo efectivo, dominio y respuestas no pueden acreditarse solo con archivos. |

## Comprobaciones realizadas

- Las 15 pruebas HTTP/criptográficas de la PoC se ejecutaron nuevamente en un entorno aislado, con datos sintéticos: [reporte 15/15](evidencia/poc_revalidacion_2026-10-27.json). El código y la evidencia anterior se conservaron.
- Los 23 contratos del modelo se reejecutaron en SQLite en memoria: [reporte 23/23](evidencia/modelo_revalidacion_2026-10-27.json). No constituyen una prueba de PostgreSQL ni del MVP completo.
- Se recalcularon los totales y los cuatro escenarios de la matriz; se comprobó que las notas visibles coincidan con sus fundamentos. Los pesos y puntajes siguen siendo juicios de ingeniería, no mediciones comparativas de rendimiento.
- Se revisaron la lectura y geometría del PDF, los siete paneles de mockup, el logo UdeC, los guiones y las referencias. [Control de artefactos](evidencia/QA_Paquete_E2.json): 51/51 comprobaciones aprobadas.

## Correcciones de esta revisión

El UML pasó a la secuencia de exposición, se tiparon explícitamente la aplicación web y la base de datos dentro de la frontera C4, se precisó el requisito RF-09 y la interpretación de la encuesta, y se cambió la afirmación de que la PoC «elimina» incertidumbre por la conclusión respaldada: la reduce para el flujo sintético. Se actualizaron la matriz, sus fuentes y los guiones.

La guía del curso asigna 10 minutos de exposición y 5 de preguntas; la rúbrica menciona un máximo de 12 minutos. El guion se planifica para 10, pero se debe cronometrar al equipo y ensayar preguntas cruzadas. La cobertura documental de los siete criterios no garantiza una nota de 100 %.
