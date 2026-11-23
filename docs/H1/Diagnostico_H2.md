# Diagnóstico de entrada a H2

Este documento no inicia H2 ni modifica el producto. Ordena lo que H1 deja abierto para que una autorización posterior decida con alcance explícito. La prioridad combina impacto académico, privacidad/permisos y esfuerzo; no es una nota ni una promesa de cierre.

## 1. Brechas de H1

| Prioridad | Brecha | Evidencia | Por qué bloquea una afirmación fuerte |
| --- | --- | --- | --- |
| P0 | Visibilidad y licencia sin decisión | API pública, `license: null`, sin `LICENSE`; [Exposición](Exposicion_y_Licencias.md) | Público no es permiso; no se puede afirmar reutilización ni aceptación de exposición |
| P0 | Exposición de un tercero y metadatos | [Comentarios_Docentes.md](../fuentes/Comentarios_Docentes.md); 19 PDF y 19 DOCX/PPTX (17 DOCX y 2 PPTX) con metadatos | Debe decidirse retiro, redacción o aceptación; H1 no publica el contenido |
| P0 | RF-02 no conforme a E1 | E1 pide instrumento autorizado ([SRS E1 p. 11](../fuentes/SRS_E1_original.pdf#page=11): «Presenta y registra ítems de instrumento autorizado»; «instrumento seleccionado legalmente»); E3 usa ficha original de 12 ítems no validada; CC BY propuesta | Es una decisión previa al congelamiento de requisitos en H2, no un bloqueo autónomo del inventario documental H1; sin decisión no se puede declarar cierre ni equivalencia |
| P0 | E2 no autosuficiente | 31 enlaces locales rotos en tres documentos E2 (9 en el dossier); activos remotos no incorporados | E4 no puede citar E2 como si todos sus artefactos estuvieran en el checkout oficial |
| P1 | Procedencia remota E1/E2 | Consulta no autenticada `404`; con acceso de solo lectura se cotejaron los blob IDs de SRS E1, dossier y matriz, y la presencia de activos | El contenido de los activos no se descargó; la evaluación no debe depender del árbol privado |
| P1 | Manifiesto/ZIP no cubren H1 | 189 blobs válidos en `e04eb2d`; H1 cambia README/PRODUCT/PROCEDENCIA y agrega `docs/H1` | El paquete E3 no debe presentarse como validación del checkout actual |
| P2 | CI de la rama/diff H1 no ejecutada | CI pública del SHA base `e04eb2d` en `success` (run [45168123412](https://github.com/ba-hc/orienta-proyecto/actions/runs/45168123412)); H1 no ejecutó una nueva | RNF-M02 queda probada para el SHA base, no para el diff ni de forma universal |
| P1 | RF12/RF13 sin prueba versionada | Trazabilidad los asocia a `test_RF04`; H1 solo hizo verificación no versionada | Un vínculo no es regresión; falta prueba estable |
| P2 | Documentos E3 desactualizados | SRS/dossier/bitácora dicen “privado”; README ya corregido | Es una inconsistencia de exactitud, no una autorización |
| P2 | Formatos duplicados | Markdown, DOCX y PDF; el dossier compila otros documentos | Sin fuente canónica, una corrección puede divergir |
| P2 | Cobertura declarada | E3 y H1 comparten 414/421 líneas (98,34 %) y 89/92 ramas (96,74 %) | No hay diferencia; el reporte combinado muestra 98 % y no se usa como líneas |

H1 no cierra estas brechas: las hace explícitas. Un estado `PARTIAL` es el correcto mientras sigan abiertas.

## 2. Brechas posteriores a H2

| Prioridad | Brecha | Hito o decisión | Consecuencia |
| --- | --- | --- | --- |
| P0 | Validación de uso con 3–5 personas externas | H4, con reclutamiento y consentimiento humanos | RNF-U02 y R4-C7 no se acreditan con encuestas E1 ni tests |
| P0 | TLS, cifrado integral, KMS y retención | H3/H5 y decisión de datos | RNF-S03/S05 no habilitan datos reales |
| P1 | Cobertura de datos 2027: arancel, empleabilidad, períodos | H2/H3 con fuentes oficiales | RNF-C02 y RF06 quedan parciales; no rellenar con cero |
| P1 | Instalación por un segundo integrante y accesibilidad manual | H3 | RNF-P01/U01 siguen parciales |
| P1 | Pruebas de regresión RF08/RF12/RF13 y CI del SHA final | H2/H3 | La implementación existe, pero la evidencia estable es incompleta |
| P2 | HH humanas, reuniones, costos ejecutados y contribución distribuida | H6 | R4-C8/C11 y la declaración de autoría no se pueden completar con simulaciones |
| P2 | Ensayo, cinco voces y demo | H5/E5 | No se acredita con archivos |
| P3 | Redacción y auditoría E4 | H7/H8 | H1 no redacta E4 ni declara nota |

## 3. Qué puede hacer H2 sin ampliar alcance

H2 puede: congelar los RF/RNF realmente implementados; decidir el tratamiento de RF-02 con el equipo/docente; corregir la trazabilidad para que ningún vínculo débil se lea como PASS; agregar pruebas de regresión para RF08/RF12/RF13; reconciliar el estado de CI; y documentar faltantes de datos. No debería agregar funciones no comprometidas, cambiar la arquitectura ni abrir E4/E5.

## 4. Criterio de entrada

Para **iniciar** H2 basta una autorización escrita del responsable humano con alcance, exclusiones y criterio de cierre; las decisiones sensibles pueden seguir abiertas mientras H2 no las convierta en supuestos. Para **congelar requisitos** se necesita, además, la decisión sobre RF-02 y sobre cualquier reducción de alcance. Para **publicar o reutilizar** material se necesitan las decisiones de licencia, visibilidad y exposición de terceros. Para **incorporar activos E2** se requiere permiso y una decisión de recuperación. Ninguna de estas decisiones se declara aprobada en H1; si faltan, el estado correcto es `BLOCKED` para la afirmación afectada, no `PASS`.

H1 termina aquí. No se inició H2 ni se redactó E4.
