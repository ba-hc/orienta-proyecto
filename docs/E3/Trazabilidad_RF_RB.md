# Trazabilidad del sistema E3

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

## Matriz de siete artefactos de diseño

| Artefacto exigido | Ubicación sustantiva |
| --- | --- |
| Problema y stakeholders | SRS §2.3–2.4; Fuentes_Publicas; Encuestas_Reanalisis |
| Especificación y priorización | SRS §3–4 y §9.1 |
| Modelos, cálculos y ciencias | docs/modelos DOT/SVG/PNG; Ciencias_Ingenieria |
| Tres alternativas | SRS §8 y antecedente Dossier_E2_Completo |
| Matriz ponderada | docs/antecedentes/Matriz_Decision_E2.csv; fundamento E2 conservado |
| Riesgos actualizados | Costos_Riesgos_Plan, 10 riesgos con disparador/gestión |
| Tres intercambios | Respuesta_Docente_Iteraciones, beneficio/sacrificio/condición |
