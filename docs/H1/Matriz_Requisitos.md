# Matriz vigente de requisitos · RF, RNF, RB y CI

Corte: `e04eb2d`, contrastado con la suite ejecutada en H1 (24 tests) y con la evidencia histórica E3. **Un vínculo o una tabla de trazabilidad no son un PASS.** Los estados describen qué se observó, no una aprobación docente ni una validación con estudiantes.

## 1. Cómo leer los estados

| Estado | Significado |
| --- | --- |
| Probado | Una prueba nombrada de la suite pasó en H1 y cubre el contrato indicado; no cubre personas ni producción |
| Verificación no versionada | Se comprobó con un script descartable de H1, no incorporado a la suite; no es una prueba de regresión |
| Parcial | Hay implementación o evidencia, pero falta un caso, una medición o una condición humana |
| No acreditado | No hay evidencia suficiente; no se rellena con una inferencia |
| No cumple | La evidencia contradice el objetivo en el entorno declarado |
| Fuera / excluido | El alcance E3 lo deja fuera; no se contabiliza como implementación |

### Archivos base de la matriz

| Tipo | Archivos de referencia |
| --- | --- |
| Implementación | [orienta/views.py](../../orienta/views.py), [orienta/models.py](../../orienta/models.py), [orienta/domain.py](../../orienta/domain.py), [orienta/catalogue.py](../../orienta/catalogue.py), [templates/orienta](../../templates/orienta/interests.html) |
| Pruebas | [tests/test_workflow.py](../../tests/test_workflow.py) |
| Evidencia | [carga.json](../../evidencia/carga.json), [e2e.json](../../evidencia/e2e.json), [auditoria_web.json](../../evidencia/auditoria_web.json), [restauracion.json](../../evidencia/restauracion.json), [pruebas.log](../../evidencia/pruebas.log), [cobertura.json](../../evidencia/cobertura.json) |
| Datos | [catalogo_udec_2027.json](../../data/catalogo_udec_2027.json), [atributos_verificados.json](../../data/atributos_verificados.json), [validacion_usuarios.csv](../../data/validacion_usuarios.csv) |

## 2. Requisitos funcionales

| RF | Prio | Estado H1 | Implementación y prueba / evidencia | Brecha explícita |
| --- | --- | --- | --- | --- |
| RF01 Crear y acceder | M | Probado | `test_RF01_create_return_without_civil_identifier`, `test_RF01_invalid_duplicate_and_wrong_credentials`, `test_account_protocol_and_session_attempt_limit`; `views.account`, `Process` | No hay prueba de usabilidad del alta ni de recuperación por una persona real |
| RF02 Registrar respuestas | M | **Implementado; no conforme a E1** | `test_RF02_RF03_complete_versioned_interests_survive_logout`, `test_RF02_invalid_incomplete_submission_does_not_persist`; ficha original de 12 ítems y AES-GCM | El SRS E1, p. 11, exige «Presenta y registra ítems de instrumento autorizado» y «instrumento seleccionado legalmente» ([PDF](../fuentes/SRS_E1_original.pdf#page=11)). La ficha de 12 ítems es original y no validada psicométricamente; CC BY 4.0 es una propuesta. Decisión humana pendiente |
| RF03 Mostrar resumen | M | Probado parcial | El mismo test verifica seis promedios y el texto de límites; `domain.summarize` | La prueba no demuestra que un estudiante comprenda el resumen ni que no lo lea como diagnóstico |
| RF04 Prioridad por dimensión | M | Probado | `test_RF04_priorities_remain_undefined_until_declared`; `Priority` | La comprensión de “prioridad” no se validó con personas |
| RF05 Filtrar catálogo | M | Probado | `test_RF05_RF06_catalogue_filters_and_provenance`; catálogo 91 ofertas, 3 campus | No hay prueba con todos los filtros ni con una escuela real |
| RF06 Ficha y procedencia | M | Probado parcial | Mismo test: fuente y “Información no disponible”; 273 filas de datos, 3 duraciones con valor; arancel/empleabilidad sin valor | Faltan valores y períodos verificados para la mayoría de los campos; las 91 ofertas están cargadas. El contrato de metadatos no equivale a completitud de valores |
| RF07a Incorporar guardado | M | Probado | `test_RF07a_RF07b_idempotent_save_and_remove`; `SavedOffer` | — |
| RF07b Retirar guardado | M | Probado | El mismo test | — |
| RF08 Elegir par distinto | M | Probado parcial | `test_RF08_duplicate_or_missing_pair_cannot_replace_valid_pair`; formulario y CHECK | La prueba rechaza entrada inválida, pero no demuestra que un par válido anterior se conserve tras un intento inválido |
| RF09 Comparación factual | M | Probado | `test_RF09_RF10_missing_fields_and_priorities_without_winner`, `test_RF09_compatible_values_and_nonhomologous_periods`; `domain.compare` | Solo unidades/períodos de fixture; no homologación de datos reales |
| RF10 Razones y faltantes | M | Probado | Los dos tests anteriores: faltante, no cero, sin ganador | La prueba no mide comprensión ni evita una lectura prescriptiva |
| RF11 Recuperación propia | M | Probado | `test_RF11_no_cross_owner_read_or_delete`, `test_RF11_edit_uses_authenticated_owner_even_with_foreign_identifier` | No hay prueba con sesión real de una persona ni auditoría de todas las rutas |
| RF12a Editar prioridad | S | Verificación no versionada | `views.priorities` actualiza una fila; comprobación H1 no versionada: `RF12a=update_unique_ok` | No tiene prueba versionada; la trazabilidad lo asocia a `test_RF04`, que no edita una prioridad existente |
| RF12b Recalcular comparación | S | Verificación no versionada | La comparación lee prioridades actuales; comprobación H1 no versionada: `RF12b=recalculate_keeps_pair_ok` | No tiene prueba versionada ni cubre cambios de par/estado |
| RF13 Estado de avance | S | Verificación no versionada | `views.dashboard`; comprobación H1 no versionada: `RF13=dashboard_counts_ok` | No tiene prueba versionada; no se validó con usuarios |
| RF14 Exportar resumen | C | Fuera de alcance | SRS §3.1 lo declara pendiente; no hay código | Decisión de alcance; no es un fallo oculto |
| RF15 Panel institucional | W | Excluido | No hay panel ni acceso agregado en `orienta/` | Debe seguir excluido salvo decisión de alcance |
| RF16 Chat IA | W | Excluido | No hay chat ni envío a proveedores de IA | Debe seguir excluido |
| RF17 Ranking global | W | Excluido | No hay puntaje global ni carrera ganadora | La ausencia de ranking es un invariante, no una función pendiente |
| RF18 Importar catálogo | M | Probado | `test_RF18_catalogue_atomic_rejection_and_repeatable_import`, `test_RF18_rejects_invalid_source_schema_fields`, `test_RF18_source_revisions_do_not_overwrite_existing_provenance`; CLI de secado y aplicación | El catálogo sigue siendo 91 ofertas y 3 duraciones; actualización periódica no está operada |
| RF19 Suprimir cuenta y proceso | M | Probado | `test_RF19_own_confirmed_deletion_cascades`; borrado de usuario y CASCADE | No se afirma purga de respaldos ni recuperación tras restauración |

**RF-02 no se resuelve en H1 y no bloquea por sí solo el inventario documental.** El SRS E1, p. 11, describe RF-02 como «Presenta y registra ítems de instrumento autorizado» y fija la precondición «instrumento seleccionado legalmente» ([SRS E1, p. 11](../fuentes/SRS_E1_original.pdf#page=11)). E3 implementa una ficha original de 12 ítems; no es equivalente al instrumento autorizado de E1. El [dossier E2 §2.6](../antecedentes/Dossier_E2_Completo.md) documenta la ruta pública y la ausencia de una licencia cerrada, pero no convierte esa ruta en aprobación. La decisión es previa al congelamiento de requisitos en H2; son decisiones distintas: (a) el equipo decide si mantiene la ficha o busca el instrumento autorizado; (b) el docente/curso decide si acepta el alcance; (c) la licencia CC BY 4.0 de la ficha sigue siendo una propuesta; (d) la validación con personas y el tratamiento de datos requieren protocolo y consentimiento. Ninguna de esas decisiones cambia el contrato E3 ni se toma por inferencia.

## 3. Requisitos no funcionales

| RNF | Objetivo resumido | Estado H1 | Evidencia y resultado | Límite |
| --- | --- | --- | --- | --- |
| RNF-R01 | LCP/INP/CLS de campo | Parcial | `auditoria_web.json`: 12 pantallas, LCP máximo 48 ms, CLS máximo 0,0126 | Laboratorio local n=1; sin INP ni p75 de campo |
| RNF-R02 | p95 ≤ 1000 ms, 50 sesiones, 10 min | Cumple local | `carga.json`: 50 VU, 600,31 s, 30.000 operaciones, p95 697,2 ms | No mide red escolar ni experiencia real |
| RNF-R03 | 360 procesos y catálogo 2027 | Cumple local | `carga.json`, catálogo: 360 procesos sintéticos, 91 ofertas, 3 campus | Escenario supuesto; no matrícula real |
| RNF-R04 | Fallos ≤ 1 %, 50 sesiones | Cumple local | `carga.json`: 0/30.000 fallos, 0 HTTP 5xx | Mismo límite de escenario |
| RNF-D01 | ≥ 99 % en ventana piloto | No acreditado | No hay ventana publicada ni monitor continuo | `health` 200 no es disponibilidad mensual |
| RNF-D02 | RPO ≤ 24 h, RTO ≤ 4 h | Parcial | `restauracion.json`: RTO 0,496 s, 91 ofertas, integridad OK | RPO operativo y periodicidad no demostrados |
| RNF-S01 | Auth y sesión vencida | Probado | `test_RNFS01_authentication_expiry_and_csrf` | Contratos locales, no auditoría exhaustiva |
| RNF-S02 | 0 accesos cruzados | Probado | `test_RF11_*`; lectura, edición y borrado ajenos | No cubre todas las rutas futuras |
| RNF-S03 | TLS y cifrado en reposo | **No cumple para datos reales** | HTTP loopback; AES-GCM solo de respuestas; SQLite/prioridades/respaldos sin cifrado integral | No habilitar datos reales; decisión y controles pendientes |
| RNF-S04 | 0 secretos versionados | Parcial | `revision_secretos.json`: 80 archivos, 0 hallazgos; claves fuera de Git | Revisión de patrones, no garantía universal |
| RNF-S05 | Finalidad, retención y supresión | Parcial | Protocolo y RF19; borrado activo probado | Sin estudio real ni purga operativa de respaldos |
| RNF-U01 | WCAG aplicable | Parcial | `auditoria_web.json`: axe 4.14.1, 12 pantallas, 0 violaciones | Lector de pantalla y revisión manual pendientes |
| RNF-U02 | ≥ 80 % completan comparación sin ayuda | No acreditado | `Validacion_Usuarios.md`; CSV solo con encabezados | No hay participantes; la encuesta E1 no sustituye |
| RNF-U03 | Español y 360–1440 px | Cumple en lo probado | `e2e.json`: 4 recorridos, 360 y 1440 px; sin overflow | Zoom y lector manual pendientes |
| RNF-C01 | Chromium y Firefox | Cumple en lo probado | `e2e.json`: 4 recorridos PASS en dos familias | Versiones concretas; no otros navegadores |
| RNF-C02 | URL, ciclo, fecha y unidad | Parcial | 273 filas base con metadatos; 3 duraciones con valor; 0 arancel/empleabilidad; `test_RF18_*` | Metadatos al alcance revisado; completitud de valores es un eje distinto (3/273). No se declara PASS universal ni se afirma que falten ofertas |
| RNF-M01 | RB críticas y ramas ≥ 80 % | Cumple local | 24 tests; 414/421 líneas (98,34 %), 89/92 ramas (96,74 %); E3 reporta dominio 91,67 % de ramas e importador 100 % | Cobertura no prueba 3FN ni comprensión |
| RNF-M02 | CI con lint/formato/tests | Cumple para el SHA base; no para H1 | CI pública de `e04eb2d`: dos runs `success`, run [45168123412](https://github.com/ba-hc/orienta-proyecto/actions/runs/45168123412) con job `verificar` e instalación/formato/migraciones/tests/importación; `ci_codigo.json` conserva una corrida anterior `a845244…` | No se ejecutó una CI nueva de la rama/diff H1; no es universal ni cubre el diff |
| RNF-M03 | Errores con correlación sin datos | Probado | `test_RNFS04_headers_and_error_correlation`: 404, cabeceras, ID de 32 caracteres | Sin observabilidad centralizada |
| RNF-P01 | Reproducible por segundo integrante | Parcial | CI limpia y comandos H1 | No hay instalación registrada por otra persona |
| RNF-P02 | Despliegue ≤ 30 min y rollback | Parcial | Pipeline y restauración local | Sin cronometraje humano ni operador externo |

## 4. Reglas de negocio y ciencias

| ID | Estado | Evidencia | Brecha |
| --- | --- | --- | --- |
| RB-01 Apoyar sin decidir | Parcial | RF09/10; comparación sin ganador | La interpretación humana no está validada |
| RB-02 Intereses no son diagnóstico | Parcial: regla visible; sin prueba versionada | [interests.html](../../templates/orienta/interests.html) muestra «No es un test psicométrico», «no tiene baremos» y «no asigna carreras»; comprobación H1 no versionada: GET `/intereses/` 200 con esos textos | La regla de no diagnóstico no acredita que la ficha sea el instrumento autorizado; son ejes distintos. El desvío RF02 se trata en la fila RF02 |
| RB-03 Carrera ≠ oferta | Probado | RF05/18; `Offer` con código/campus/ciclo | Catálogo limitado a UdeC 2027 |
| RB-04 Procedencia y NULL ≠ 0 | Probado parcial | RF06/09/10; 273 filas, 3 valores | Faltan períodos y valores para la mayoría |
| RB-05 Par exactamente dos | Probado parcial | RF08; formulario y CHECK | Falta prueba de conservación del par válido |
| RB-06 Prioridades explícitas | Probado + verificación no versionada | RF04; RF12a/b comprobados sin prueba versionada | Sin regresión versionada de RF12 |
| RB-07 Indicadores contextuales | Parcial | RF06/10 | No hay datos de empleabilidad con período |
| RB-08 Persistencia aislada | Probado | RF11; accesos ajenos 404 | Sin auditoría de todas las rutas |
| RB-09 Sin match global | Parcial | RF03/10; no hay ranking | Comprensión humana pendiente |
| RB-10 Supresión y seguridad | Probado | RF19; CASCADE; evento sin identidad | Purga de respaldos no ejecutada |
| CI1 Normalización/3FN | Implementado; razonamiento | [Ciencias](../E3/Ciencias_Ingenieria.md); `test_CI1_database_blocks_duplicates_and_self_comparison` | La prueba verifica restricciones, no demuestra 3FN ni portabilidad PostgreSQL |
| CI2 AES-256-GCM | Implementado; probado local | `test_CI2_random_nonces_tamper_and_binding`, `test_CI2_corrupt_payload_fails_closed_in_interface` | Sin TLS, KMS ni cifrado integral de la base |

## 5. Contraste entre SRS E3 e implementación

- **RF02:** el SRS E3 describe la ficha original, pero E1 exigía un instrumento autorizado (p. 11: «Presenta y registra ítems de instrumento autorizado»; «instrumento seleccionado legalmente», [PDF](../fuentes/SRS_E1_original.pdf#page=11)). La implementación cumple el contrato de software; no cumple el compromiso E1 ni acredita validez psicométrica.
- **RF12a/RF12b/RF13:** el SRS y la trazabilidad los presentan como disponibles, pero no tienen prueba nombrada. La verificación H1 no versionada los comprobó; la trazabilidad los asocia a `test_RF04`, que no edita una prioridad existente. No se eleva ese vínculo a PASS.
- **RF08:** el test cubre el rechazo de un par inválido, no la conservación de un par válido anterior. La implementación usa `update_or_create` solo con formulario válido, pero falta la prueba de regresión.
- **RNF-M02:** la CI pública de `e04eb2d` pasó (run 45168123412); `ci_codigo.json` es de `a845244…` y el SRS cita `471dc2c`. La evidencia cubre el SHA base, no la rama/diff H1 ni un resultado universal.
- **RNF-C02:** “273 campos con metadatos” no significa 273 valores. La ejecución H1 confirma 273 filas de datos, 3 duraciones con valor y 0 valores de arancel/empleabilidad; las 91 ofertas existen.
- **Visibilidad:** el SRS, el dossier y la bitácora E3 dicen “privado”; el repositorio figura público en la observación del 23/11/2026. Es una obsolescencia documental, no una autorización.
- **Manifiesto:** `application_commit` es `a845244…`; los 189 blobs sí coinciden en `e04eb2d`. El manifiesto certifica contenido, no el commit de aplicación ni H1.

## 6. Brechas que no se cierran con documentación

No hay evidencia de: sesiones de uso con estudiantes, instalación por un segundo integrante, verificación manual de accesibilidad, TLS/cifrado integral, RPO operativo, purga de respaldos, horas humanas, aprobación docente ni entrega E4. Estas brechas se registran; no se simulan.
