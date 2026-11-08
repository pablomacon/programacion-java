# Integridad editorial: fuentes y discrepancias

La fuente de cada página es `contenido/unidad-NN.md`. En la auditoría inicial los siete SHA-256 coincidían con `documentacion/VERIFICACION.json` y las copias del respaldo. Posteriormente se autorizaron dos correcciones de numeración en U1 y U5: consultar `INFORME-FASE-2C.md` y los hashes vigentes en `verificacion-fuentes.json`. Las otras cinco unidades siguen coincidiendo con el paquete revisado. El estado histórico del respaldo describe reconstrucciones anteriores y no identifica el contenido actualmente presente en esas rutas.

| Unidad | Bytes | Encabezados | Encabezados con «Actividad» | Recursos |
|---|---:|---:|---:|---:|
| 01 | 72.357 | 124 | 10 | 3 |
| 02 | 79.230 | 148 | 14 | 2 |
| 03 | 88.047 | 153 | 17 | 4 |
| 04 | 66.444 | 133 | 18 | 4 |
| 05 | 77.914 | 151 | 19 | 4 |
| 06 | 81.649 | 165 | 23 | 3 |
| 07 | 71.628 | 131 | 26 | 3 |

Las cifras de encabezados con «Actividad» incluyen todas las coincidencias y no pretenden contar actividades independientes. La U5 contiene 14 apartados principales y actividades A–S. La fuente y la página anteriores tenían 12 apartados, una nota de reconstrucción y burbuja; se preserva la fuente antigua en `referencias/` y el código de sus tres simuladores en `assets/simuladores.js`. No se montan en las páginas canónicas porque sus contratos difieren; burbuja no es uno de los cuatro recursos actuales de U5.

Cada marcador canónico se registra en `registro-recursos.json` y se inserta en su ubicación. La imagen de los bidones se copió del respaldo y se verificó visualmente. Los otros 22 recursos se muestran como pendientes con orientación textual; no se declaran implementados. Los comentarios técnicos y el checklist docente de U5 se omiten de la vista estudiantil, manteniendo el párrafo posterior y el archivo fuente íntegro.

La documentación también identifica diferencias para los ejemplos antiguos de U6 y U7: prevalecen los marcadores y ejemplos revisados, sin integrar todavía simuladores incompatibles. La infografía de ciclos de U4 sigue sin verificarse. Quedan pendientes implementación y pruebas de los recursos, revisión visual y accesibilidad en navegadores y cotejo con cualquier versión histórica anterior al paquete revisado.
