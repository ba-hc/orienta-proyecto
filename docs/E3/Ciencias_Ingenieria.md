# Modelo de datos y ciencias de la ingeniería

## CI-1 · Dependencias funcionales y 3FN

Compromiso E1, tabla 8, p. 9: modelar entidades, claves, dependencias y normalizar; verificar anomalías en el sistema construido.

La relación universal U(código, ciclo, carrera, campus, URL, fecha, hash, página, dimensión, valor, unidad, período, proceso, titular, ítem, respuesta, prioridad, guardado) duplicaría fuentes e identidad en cada respuesta y dato. Produce anomalías: corregir una URL exige modificar muchas filas; no se puede registrar una fuente sin inventar una respuesta; borrar el último guardado podría borrar información académica. Se descompone en las relaciones siguientes, implementadas por migración real.

| Relación | Clave candidata | Dependencia no trivial |
| --- | --- | --- |
| Campus | id; nombre | id → nombre |
| Career | id; nombre | id → nombre |
| Source | id; (URL, hash) | id → URL, título, fecha, hash |
| Offer | id; (código, ciclo) | id → carrera, campus, fuente, página, activo |
| Datum | id; (oferta, dimensión) | oferta, dimensión → valor, unidad, período, fuente |
| Process | UUID; propietario | UUID → propietario, versión, fechas |
| InterestResponse | id; (proceso, ítem) | proceso, ítem → valor_cifrado |
| Priority | id; (proceso, dimensión) | proceso, dimensión → nivel |
| SavedOffer | id; (proceso, oferta) | proceso, oferta → asociación |
| Comparison | id; proceso | proceso → ofertaA, ofertaB |
| AuditEvent | id | id → tipo, fecha, correlación |

Bajo estas dependencias declaradas, todo determinante no trivial es una superclave: las relaciones cumplen BCNF y, por implicación, 3FN. No se afirma que una prueba automática demuestre normalización. El razonamiento depende de que nombre sea único en el catálogo acotado UdeC; otra universidad exigiría una clave institución + código de carrera. El valor cifrado es un atributo atómico del almacenamiento lógico; no se consulta internamente con SQL.

Descomposición sin pérdida: cada unión con tabla maestra comparte su clave, por ejemplo Offer ∩ Source = {source_id}, que determina Source; en ese paso se satisface el criterio de unión sin pérdida. Todas las dependencias declaradas quedan dentro de una tabla. Las restricciones UNIQUE impiden asociación y respuesta duplicadas; CHECK impide la autocomparación; FK PROTECT conserva fuentes y carreras referidas; CASCADE elimina datos dependientes del titular.

Resultado observado: pruebas test_CI1_database_blocks_duplicates_and_self_comparison, test_RF18_catalogue_atomic_rejection_and_repeatable_import y test_RF19_own_confirmed_deletion_cascades. La misma migración crea el esquema usado por el navegador. Efecto: importación repetible sin duplicados, rechazo completo de lotes corruptos, supresión sin borrar el catálogo público.

## CI-2 · Autenticidad e integridad

Compromiso E1: credenciales, acceso y cifrado. Modelo: atacante conoce UUID ajeno, manipula token/respuesta o recupera una copia del archivo de respuestas; no controla el sistema operativo ni la clave privada del servidor. Las contraseñas usan el hasher adaptativo PBKDF2 de Django; no se cifran reversiblemente. La sesión de 30 min se valida en servidor; la identidad autenticada se usa en todas las consultas al proceso. CSRF verifica las mutaciones desde navegador.

Para cada respuesta se calcula (C, T) = AES-256-GCM(K, N, M, A), K privada de 32 bytes, N aleatorio de 12 bytes, M = respuesta 1..5 y A = UUID:ítem:versión. El almacenamiento es N||C||T. Cambiar C, T o A invalida la etiqueta y produce un fallo cerrado. Asociar A evita transplantar una respuesta válida a otro titular/ítem. Para n respuestas con nonce aleatorio de 96 bits, la cota de colisión aproximada es n(n−1)/2^97: con 360 × 12 = 4320 respuestas es aproximadamente 1,18 × 10^-22 por clave. La cota no justifica reutilizar nonce ni operar indefinidamente con una misma clave.

Pruebas: credencial válida/incorrecta/caducada; lectura y supresión ajena; nonces distintos con igual mensaje; manipulación de etiqueta; cambio de UUID e ítem; contenido alterado devuelve 503 sin resultado; CSRF ausente devuelve 403. La suite y el E2E son evidencia reproducible, no certificación criptográfica.

Aprendizaje: se contrastaron documentación oficial de Django 5.2, API AESGCM de cryptography y NIST SP 800-38D. La comprensión se verificó con controles negativos (cambio de AAD e integridad), no solo con un roundtrip cifrar/descifrar. Persisten límites: el cifrado de respuestas no cifra todo SQLite, prioridades ni respaldos; no hay TLS público ni KMS. Este entorno admite únicamente datos de prueba. RNF-S03 requiere cierre antes de datos reales.

## Dimensionamiento y complejidad

Escenario declarado: 8 cursos × 45 = 360 procesos; clase 45 + 5 de margen = 50 sesiones. 45 se contrasta con el límite reglamentario del Decreto 8144; no demuestra matrícula de un establecimiento. El 8 es un supuesto del escenario. El snapshot del catálogo contiene 91 códigos distintos con campus/ciclo; se cotejan contra las páginas 294–300 del PDF 2027. Se generaron 360 procesos sintéticos para carga, no estudiantes reales.

La comparación recorre un conjunto fijo de 3 dimensiones numéricas más ubicación: O(d) en tiempo y memoria, sin suma de conveniencia. La restricción UNIQUE(proceso, oferta) en Guardados evita la duplicación; la búsqueda usa el catálogo acotado de 91, por lo que no se justifica Elasticsearch. La base SQLite simplifica el entorno local; la carga decide si satisface el escenario limitado. Escalar a varios servidores o escrituras intensivas implica evaluar PostgreSQL, no afirmar equivalencia de motores.

Fuentes técnicas: https://docs.djangoproject.com/en/5.2/topics/auth/passwords/; https://docs.djangoproject.com/en/5.2/ref/csrf/; https://cryptography.io/en/latest/hazmat/primitives/aead/#cryptography.hazmat.primitives.ciphers.aead.AESGCM; https://csrc.nist.gov/pubs/sp/800/38/d/final.
