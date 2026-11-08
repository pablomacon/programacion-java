# Recursos interactivos — fase 3A

La integración usa un mapa de IDs canónicos en `generar.py`, funciones deterministas en `assets/recursos-modelos.js` y montaje progresivo en `assets/recursos-interactivos.js`. Cada recurso conserva una alternativa textual que permanece disponible si no carga JavaScript y se muestra al imprimir. Los 14 recursos de U4–U7 permanecen pendientes; la imagen de bidones original no se modificó.

| ID | Implementación |
|---|---|
| `u01-bidones-simulador` | Operaciones regladas, pares de estado, contador efectivo, historial, predicción opcional, retroceso y guías de 8 y 6 operaciones. |
| `u01-programa-cpu-ram` | Modelo conceptual por pasos del cálculo de total, memoria, procesamiento y salida; distingue el código Java del entorno de ejecución. |
| `u02-estructura-java` | Código seleccionable y explicaciones de clase, main, llaves, instrucción y recorrido. |
| `u02-variables-asignacion` | Trazado de precio y total y ejemplo separado de copia de primitivos; anterior, siguiente y reinicio. |
| `u03-if-else` | Saldo y precio modificables, predicción opcional, límites y explicación de la rama elegida. |
| `u03-else-if` | Nota de 1 a 10, predicción, orden correcto o incorrecto y distinción entre falso y no evaluado. |
| `u03-condiciones-compuestas` | AND, OR, negación y dos agrupaciones; muestra estados individuales y cortocircuito. |
| `u03-switch` | Menú con break, sin break y con flechas, incluyendo default y ejecución sucesiva sin break. |

Los recursos están implementados y cuentan con pruebas automatizadas, pero no se declaran validados visualmente ni en accesibilidad real. Las dos modalidades adicionales de switch están expresamente presentes en el marcador canónico, aunque el enunciado general pide evitar sintaxis que aún no se enseñe. La copia de primitivos es un segundo ejemplo y no altera la secuencia canónica de precio y total.

Las pruebas de modelos abarcan las rutas completas de bidones, capacidades y operaciones sin cambio; estados del cálculo y copias; límites; condiciones no evaluadas; agrupaciones y switch. Las pruebas de interfaz usan un DOM simulado, no un navegador real. Las pruebas Python comprueban ubicación única, alternativas, 14 recursos pendientes, imagen, registro, contenido, hashes y navegación. El programa `Main` usado en el esquema se compiló y ejecutó con salida `Hola`.

El servicio de navegador devolvió `browser access host is unavailable`. Quedan pendientes revisión de escritorio y móvil, operación con teclado y lector de pantalla reales, impresión/PDF y contraste medido. La base de modelos, registro y alternativas puede extenderse en 3B y 3C conservando esas mismas pruebas por recurso.
