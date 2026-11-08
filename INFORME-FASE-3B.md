# Recursos de ciclos, arreglos y cadenas — fase 3B

Se conserva la infraestructura de 3A: `generar.py` registra los 23 IDs y monta progresivamente los componentes; `assets/recursos-interactivos.js` comparte controles y montaje. `assets/recursos-3b-modelos.js` contiene trazados deterministas separados del DOM y `assets/recursos-3b.js` presenta los controles. Las 16 alternativas de U1–U5 siguen disponibles sin JavaScript e impresas. Las seis de U6–U7 permanecen pendientes.

| ID | Comportamiento implementado |
|---|---|
| `u04-while-trazado` | Condición, cuerpo, actualización, salida, iteraciones y evaluaciones; inicio e incremento ajustables y pausa de seguridad sin afirmar terminación. |
| `u04-acumuladores-contadores` | Notas editables, suma y conteo antes/después, límite 6, trazado acumulativo y promedio. |
| `u04-for-esquema` | Inicialización única, condición, cuerpo, actualización y salida; variación de inicio, paso y dirección. |
| `u04-do-while-esquema` | Comparación de orden de ejecución con `while`, incluido valor inicial 5 y referencia al menú. |
| `u05-arreglo-indices` | Cinco celdas etiquetadas, consulta, modificación, índice ordinal y errores de límites. |
| `u05-recorrido-arreglo` | Recorrido, condición final falsa, arreglo vacío, variante inversa y demostración del acceso inválido con `<=`. |
| `u05-busqueda-lineal` | Existencia, primera posición, búsqueda anticipada y conteo, con repetidos y arreglo vacío. |
| `u05-string-vs-array` | Consulta y modificación de arreglo frente a `String` inmutable, `length`/`length()`, `charAt()` y `toUpperCase()`. |

La instrucción de esta fase pide inicialmente `{3, 5, 8}` para la comparación, mientras el marcador incluye `{7, 5, 8}`. La interfaz inicia con el ejemplo solicitado y permite seleccionar el del marcador, sin alterar ninguna fuente. El `while` predeterminado utiliza exactamente `numero = 1` a `3`, no cinco iteraciones: cinco iteraciones corresponden al ejemplo canónico de `for`. Los modos de búsqueda de existencia y primera posición no se detienen anticipadamente; el modo `while` sí lo hace.

Las pruebas de modelos cubren las condiciones finales, casos vacíos, valores límite y repetidos. La integración comprueba los ocho montajes en sus marcadores, 16 recursos con alternativa, seis pendientes e integridad de las siete fuentes. Las pruebas de interfaz se ejecutan sobre un DOM simulado y no equivalen a una prueba en navegador.

El servicio de acceso a navegador devolvió `browser access host is unavailable`. Quedan pendientes inspección visual en escritorio/móvil, uso real con teclado y lector de pantalla, contraste y PDF/impresión. No se modificaron los Markdown canónicos. Para 3C, conservar los modelos separados, los controles semánticos y las alternativas de impresión, y añadir pruebas de casos y de montaje para los seis marcadores de U6 y U7.
