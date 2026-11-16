# Orienta: construcción E3

Proyecto independiente, raíz /home/ben/orienta-proyecto. Origen y SHA en PROCEDENCIA.md. No editar el checkout histórico para desarrollar este proyecto.

Instalar con python -m venv .venv y .venv/bin/pip install -r requirements-lock.txt. Ejecutar herramientas/inicializar.py, migrate, importar_catalogo.py --aplicar y enriquecer_catalogo.py. Solo loopback y datos de prueba; gates para usuarios reales en docs/E3/Validacion_Usuarios.md.

Pruebas: coverage run --branch --source=orienta manage.py test tests. Navegador: herramientas/e2e_navegadores.py contra puerto19039. Carga: herramientas/medir_carga.py --segundos600 crea runtime propio y usa19040. No confundir sus datos con usuarios ni sus tiempos con HH humanas.

La cobertura académica se audita en docs/E3/Cobertura_R3.md. No inventar actas, firmas, comentarios ni validaciones. No marcar la rúbrica al100% mientras falte evidencia humana. Documentos editables y PDF se exportan con herramientas/exportar_documentos.py.
