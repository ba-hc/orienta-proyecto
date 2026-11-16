# Exportar los documentos E3

```bash
/home/ben/orienta-proyecto/.venv/bin/python herramientas/exportar_documentos.py entrega.md
/home/ben/orienta-proyecto/.venv/bin/python herramientas/exportar_documentos.py entrega.md anexo.md --pdf
```

El intérprete necesita `python-docx`. `--pdf` necesita `libreoffice` o `soffice`
en el PATH. El exportador no instala dependencias, fuentes ni recursos remotos.

Cada salida queda junto al Markdown, con su mismo nombre base: `entrega.docx`
y, al pedirlo, `entrega.pdf`. Una salida existente se reemplaza únicamente al
terminar su generación. Si el PDF falla, se conserva el DOCX generado y el PDF
anterior, si lo había. Los errores se informan por archivo; el proceso continúa
con los restantes y termina con código 1 si alguno falló.

## Markdown admitido

- `#` es el título; `##`, `###` y `####` son los tres niveles de encabezado.
- Párrafos en varias líneas, listas con `-`, `+`, `*` y numeración `1.` o `1)`;
  las listas pueden anidarse mediante indentación.
- `**Negrita**`, código entre backticks y enlaces `[texto](URL)`, que se muestran
  como `texto (URL)` para conservar la dirección también al imprimir.
- Tablas con pipes y fila separadora; se admiten alineaciones `:---`, `:---:`
  y `---:`. Para pipes literales, usa `\|` o código inline. Las filas con menos
  celdas se completan vacías; las que exceden la cabecera producen un error con
  número de línea para evitar pérdida de contenido.
- Bloques de código delimitados por tres o más backticks o tildes; se conservan
  literalmente, sin ejecutar su contenido.
- Una línea `---` añade una línea divisoria y espacio.

La entrada debe estar codificada en UTF-8 (se admite BOM). Los acentos, eñes y
signos españoles se conservan. Es un subconjunto de Markdown: no se procesan
HTML, imágenes, fórmulas, notas al pie, enlaces por referencia ni extensiones
de diagramas. No se descargan imágenes ni se abren enlaces.

## Presentación y conversión

A4, márgenes de 2 cm, cuerpo Roboto 10.5 pt y fallback declarado Aptos si
Fontconfig no detecta Roboto. El título usa Poppins 22 pt y azul `223C6A`;
los encabezados usan Poppins 18/14/12 pt. Los encabezados se mantienen junto al
contenido siguiente y los párrafos tienen control de líneas viudas.

La cabecera dice «Orienta · Grupo 9 · E3» y el pie contiene un campo de número
de página. Las tablas usan 8.5 pt, cabecera azul con texto blanco repetida en
cada página y ancho fijo dentro de los márgenes. Las filas pueden continuar en
otra página, incluso cuando una celda supera una página. El código en bloque
usa Liberation Mono 9 pt.

Las fuentes no se incrustan: el procesador de textos puede sustituir Poppins,
Roboto o Aptos si no están instaladas. Para una tipografía idéntica entre equipos,
instala previamente las fuentes correspondientes por los medios habituales.

Cada PDF usa un perfil temporal de LibreOffice independiente de la sesión de
escritorio y de otras conversiones, que se elimina al terminar. El límite es
120 segundos por archivo; al excederse se detiene el grupo del conversor en
POSIX y se informa un error. El contenido Markdown nunca se ejecuta y las
llamadas externas se realizan sin intérprete de shell.
