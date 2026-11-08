# Recursos de métodos, clases y objetos — fase 3C

Se extendieron el registro del generador y la infraestructura de montaje y trazado de 3A–3B. Las reglas están en `assets/recursos-3c-modelos.js`; la presentación y controles en `assets/recursos-3c.js`. Se modificaron `generar.py`, estilos, README, registro, HTML regenerados y pruebas de integración. No se modificaron los Markdown.

| Recurso | Estado y comportamiento |
|---|---|
| `u06-flujo-metodos` | Implementado: llamadas anidadas, instrucción actual, llamador, punto de retorno y salida C, B, A, D. |
| `u06-parametros-retorno` | Implementado: argumento literal o variable, copia al parámetro, cálculo, `return`, expresión y salida; contraste con `void`. |
| `u06-alcance-referencias` | Implementado: primitivo, modificación de arreglo compartido y reasignación local de la referencia, con estados de ámbito. |
| `u07-abstraccion-modelado` | Implementado: propuestas y justificación abiertas para alquiler o mantenimiento, con referencia opcional y sin respuesta única. |
| `u07-clase-instancias` | Implementado: creación de productos, operaciones, estado independiente y alias `c = a`. |
| `u07-encapsulamiento` | Implementado: comparación entre asignación directa y operaciones validadas, predicciones, estados, reinicio y deshacer. |

El flujo utiliza exactamente el ejemplo canónico con salida C, B, A, D. Se distingue que Java siempre pasa argumentos por valor y que una referencia copiada puede señalar el mismo arreglo. La actividad de abstracción no califica como incorrecta una alternativa defendible. En Producto se muestran los datos canónicos; los ejemplos secuenciales parten de stock 15 y pueden reiniciarse para ensayos aislados.

La versión esencial del capítulo valida cantidades positivas pero no evita el desbordamiento de `int`. El modelo reproduce la aritmética de Java y advierte ese límite; no afirma que `private` garantice validez completa. Los controles numéricos aceptan precios finitos, por lo que el caso especial `NaN` del capítulo queda fuera del simulador, sin modificar la teoría.

La regresión verifica reglas de 3A, 3B y 3C, montajes y controles con DOM simulado, siete hashes y capítulos, los 22 recursos y la imagen. Se compilaron y ejecutaron los programas Java completos mostrados: flujo, parámetros y tres variantes de alcance. Las alternativas textuales se conservan para ausencia de JavaScript e impresión. Las pruebas automatizadas no sustituyen pruebas de navegador real.

El servicio de navegador informó `browser access host is unavailable`. Quedan pendientes para la auditoría final: revisión visual y responsive, teclado y lector de pantalla reales, contraste y salida de impresión/PDF. No se ha realizado commit ni despliegue.
