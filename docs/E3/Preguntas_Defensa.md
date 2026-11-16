# Preguntas de defensa E3

## Diseño y respuesta docente

**¿Qué cambió por evidencia?** El estado monolítico en JSON se convirtió en relaciones con claves y transacciones; se incorporaron contratos de importación y supresión; se separó procedencia por campo y revisión; el alta de navegador obligó a corregir la política de referencias manteniendo CSRF. Cada iteración tiene disparador, alternativas, decisión y efecto en Respuesta_Docente_Iteraciones.md.

**¿Todas estas observaciones fueron del oral 1?** No. El usuario aportó comentarios cualitativos del escrito, intento 2, y puntajes del oral 1. Se conservan por separado. Las acciones inferidas por el equipo no se atribuyen a la profesora.

**¿Por qué SQLite si E2 consideraba PostgreSQL?** E3 prioriza una ejecución académica local, independiente y de bajo costo. La prueba de carga del escenario local cumple el presupuesto. SQLite no se presenta como equivalente para operación multiinstancia o mayor concurrencia de escrituras; ese crecimiento activa una evaluación de PostgreSQL y su migración. La elección y su sacrificio están documentados.

**¿No bastaba con configurar otra plataforma?** Se evaluaron tres alternativas en E2: monolito propio, separación cliente/API y adquisición/integración. La última mantiene incertidumbres de licencia/API/costo. Orienta conserva reglas propias de procedencia, comparación y privacidad; no copia un instrumento profesional ni pretende sustituir la orientación.

## Ciencias y datos

**¿Las pruebas demuestran 3FN?** No. Las dependencias funcionales y las claves justifican la descomposición. Las pruebas verifican consecuencias: duplicados, referencias, actualizaciones y borrados consistentes. El razonamiento depende del dominio UdeC acotado y debe revisarse si cambia.

**¿Qué evita perder procedencia al actualizar una URL?** Source tiene identidad por URL y hash del snapshot. Una revisión nueva crea otra fuente, preservando la anterior. Oferta y cada dato apuntan a su fuente concreta. Existe una prueba de que una importación nueva no sobrescribe el hash anterior.

**¿Qué protege AES-GCM?** Confidencialidad e integridad de la respuesta bajo una clave privada, nonce aleatorio y datos asociados al UUID, ítem y versión. El cambio de contenido o contexto invalida la etiqueta. No protege un host comprometido que controla las claves ni cifra todo SQLite.

**¿Por qué no se puede copiar un ciphertext entre estudiantes?** La etiqueta autentica datos asociados que incluyen proceso e ítem. El mismo ciphertext con otro contexto no valida. Ese control negativo está ejecutado; no se confía únicamente en que cifrar y descifrar devuelvan el mismo valor.

**¿La ficha es un test validado?** No. Son 12 textos originales de exploración de actividades, con promedios autodescriptivos de dos respuestas. No hay baremos, precisión diagnóstica ni asignación de carreras. La licencia del texto no demuestra validez psicológica. La pertinencia y comprensión requieren validación humana.

**¿Por qué hay tantos faltantes?** La oferta oficial 2027 no contiene todos los costos ni indicadores. Algunas páginas muestran cifras sin cohorte o año. Es preferible mostrar el límite a mezclar períodos o convertir ausencia en cero. Las 3 duraciones publicadas se marcan con vigencia por confirmar.

## Verificación

**¿Qué mide el p95?** El percentil 95 de duración por operación HTTP medida con reloj monotónico en un host local, 50 sesiones autenticadas, 70 % lectura y 30 % guardado, 1 operación por segundo por sesión. Se excluyó calentamiento y no se contaron redirecciones como lecturas nuevas. No es el tiempo que demora una persona en decidir ni latencia de una red escolar.

**¿Cuál es el denominador de errores?** 30.000 operaciones: 21.000 lecturas y 9.000 guardados. Se verifica estado HTTP y contrato funcional de respuesta. Se reportan 5xx y fallos de contrato por separado. Los JSONL conservan una fila por operación, sin credenciales.

**¿Por qué repetir la carga?** La primera programación terminó la última operación alrededor de 599,78 segundos. Se conservó esa evidencia, se completó explícitamente la ventana a 600 segundos y se repitió el protocolo. La repetición final pasó; no se descartó un resultado malo para aparentar éxito.

**¿98 % de cobertura significa 98 % de requisitos?** No. Se reportan líneas y ramas de código con coverage. La trazabilidad de requisitos y reglas es una matriz distinta. El objetivo de 80 % se verifica en los módulos críticos, no con conteo de archivos ni de documentos.

**¿Cero resultados de axe prueban WCAG AA?** No. Son criterios automatizables en pantallas y versiones concretas. Los incompletos y las pruebas manuales de lector, foco, zoom y comprensión tienen su propio estado. El paquete mantiene los límites.

**¿La restauración demuestra RPO 24 h?** Demuestra recuperación íntegra de un snapshot del ejercicio y su tiempo. No demuestra que exista un respaldo automático cada 24 horas durante una operación real. Ese control y la purga tras supresión deben ejecutarse en el piloto.

**¿Qué demuestra la CI?** Instalación, formato, análisis, migraciones, pruebas e importación del SHA identificado. No demuestra despliegue productivo, usabilidad humana ni que otros SHAs posteriores pasaron. Se incluye enlace y metadatos del commit publicado.

## Validación, costos y operación

**¿La encuesta de E1 valida la aplicación?** Aporta evidencia histórica de necesidades de una muestra de conveniencia. Recalculamos 156 registros de estudiantes y 36 de apoderados del apéndice. No midió tareas de uso de E3, adopción ni eficacia. El estudio de uso necesita participantes externos y registros reales.

**¿Qué se corrigió en Q13A?** Es una categoría monetaria declarada, no una escala de 1 a 5. Los ocho códigos incluyen rangos y puntos exactos que se solapan. Se preservan sin promediar ni traducirlos en precio comercial; la recodificación definitiva requiere el formulario original.

**¿Cuánto costó realmente?** Estas acciones no hicieron compras nuevas: caja incremental 0 CLP y hardware existente. No significa costo económico total cero. Las HH humanas históricas no se aportaron y no se inventan. La valorización académica se separa de desembolso y de ingreso facturado.

**¿Por qué cambiaron los valores por rol?** No tenían fuente. Se reemplazan por una sensibilidad uniforme derivada de ingreso público y jornada de referencia, con fórmula y límites; no es una tarifa profesional cotizada.

**¿Qué falta para afirmar cumplimiento total?** Resultados reales de uso externo, evidencia auténtica de contribución distribuida, instalación por otro integrante, controles operativos del piloto, ensayo y exposición humana. El material técnico prepara esas actividades y no fabrica sus resultados.

**¿Qué se dejó fuera y por qué?** Exportación opcional, panel institucional, chat IA y ranking. Se priorizan recorrido Must, privacidad, procedencia y verificación dentro del plazo. Si no hay responsable ni presupuesto de continuidad, corresponde retiro controlado de datos y archivo académico.
