# Auditoría integral — Programación I 2026

**Dictamen: PUBLICACIÓN CONDICIONADA.** No quedan defectos críticos o altos conocidos entre los casos examinados. Antes de publicar faltan verificaciones importantes de accesibilidad real, zoom, contraste y cobertura visual completa. Las pruebas de modelos y los escenarios automatizados no demuestran por sí solos ausencia de defectos.

## Integridad editorial

Los siete hashes coinciden con `verificacion-fuentes.json`. Las pruebas comparan encabezados, texto, listas, tablas y bloques de código generados con las fuentes públicas, y comprueban los 23 IDs, enlaces y las actividades A–S de U5. Los hashes históricos de U1 y U5 difieren únicamente por las correcciones de numeración autorizadas en 2C; las pruebas revierten esos cambios en memoria y comparan sus hashes originales.

Se excluyó de la vista pública la sección de U7 titulada «Guía breve para la docencia: secuencia de cuatro módulos», que se había filtrado en HTML y PDF. El Markdown completo permanece intacto; una prueba comprueba que el cierre estudiantil anterior se conserva. La regla existente de U5 sigue excluyendo únicamente su checklist docente.

## Matriz de recursos

Todos los interactivos se montaron en Chrome en su marcador y tienen alternativa textual sin JavaScript. **B**: interacción real automatizada representativa en navegador; **M**: reglas comprobadas con pruebas Node; **I**: posición, ID y alternativa verificados por Python. No implica que cada combinación de entradas ni cada aspecto de accesibilidad haya sido probado.

| ID | Estado | Evidencia y observación |
|---|---|---|
| `u01-bidones-problema` | Imagen cargada | I, carga natural en Chrome; texto alternativo presente. |
| `u01-bidones-simulador` | Implementado | B/M/I: rutas de 6 y 8 pasos, retroceso, límites y operaciones sin cambio. |
| `u01-programa-cpu-ram` | Implementado | B/M/I: avance y retroceso; modelo conceptual simplificado. |
| `u02-estructura-java` | Implementado | B/M/I: botones de partes y orden; programa Java compilado. |
| `u02-variables-asignacion` | Implementado | B/M/I: 450 permanece tras cambio de precio; copia de primitivos. |
| `u03-if-else` | Implementado | B/M/I: igualdad y valores inferiores; una sola rama. |
| `u03-else-if` | Implementado | B/M/I: nota 10, orden incorrecto y condición no evaluada. |
| `u03-condiciones-compuestas` | Implementado | B/M/I: cortocircuito y negación; agrupaciones en modelos. |
| `u03-switch` | Implementado | B/M/I: default y caída entre casos sin `break`. |
| `u04-while-trazado` | Implementado | B/M/I: 3 iteraciones, 4 evaluaciones, inicio falso y protección sin progreso. |
| `u04-acumuladores-contadores` | Implementado | B/M/I: suma 35, contador 4, límites y estados parciales. |
| `u04-for-esquema` | Implementado | B/M/I: inicialización, condición, actualización y caso sin iteraciones. |
| `u04-do-while-esquema` | Implementado | B/M/I: comparación con `while` y condición inicial falsa. |
| `u05-arreglo-indices` | Implementado | B/M/I: índices válidos e inválidos y modificación sin cambiar longitud. |
| `u05-recorrido-arreglo` | Implementado | B/M/I: vacío, evaluación final y acceso inválido con `<=`. |
| `u05-busqueda-lineal` | Implementado | B/M/I: búsqueda repetida, primera coincidencia y detención anticipada. |
| `u05-string-vs-array` | Implementado | B/M/I: acceso, longitud e inmutabilidad; `toUpperCase()`. |
| `u06-flujo-metodos` | Implementado | B/M/I: llamadas y retornos; salida C, B, A, D compilada en Java. |
| `u06-parametros-retorno` | Implementado | B/M/I: argumento, retorno y resultado 13; Java compilado. |
| `u06-alcance-referencias` | Implementado | B/M/I: copia por valor, elemento compartido y reasignación local. |
| `u07-abstraccion-modelado` | Implementado | B/M/I: propuesta libre y comparación orientativa, sin respuesta única. |
| `u07-clase-instancias` | Implementado | B/M/I: `new`, alias, cambio de estado y deshacer. |
| `u07-encapsulamiento` | Implementado | B/M/I: rechazo de retiro inválido, asignación directa y reinicio. |

## Pruebas y evidencia

- Python: **15 pruebas aprobadas**. Node: **33 pruebas aprobadas**, incluidas pruebas de DOM simulado y compilación/ejecución de cinco programas Java mostrados.
- Chrome headless y CDP: siete unidades, 22 montajes, escenarios de las siete unidades y barrido de controles visibles; sin errores de consola ni imágenes rotas detectados. Se verificaron anchos solicitados 375, 768, 1366, 1440 y 1920 px sin desbordamiento horizontal del documento después de corregir U3.
- Las 22 alternativas textuales permanecen visibles en Chrome con JavaScript desactivado. Los controles examinados disponen de etiqueta y los botones de nombre; regiones de estado usan `aria-live`. Se comprobó Tab, Shift+Tab, Espacio y Enter en el índice de U5 y foco visible en ese recorrido. No es una auditoría completa de teclado o WCAG.
- Se inspeccionaron capturas del inicio de las unidades 1, 5 y 7 a 375 y 1440 px, y muestras de recursos. Los resultados y capturas están en `evidencias-auditoria/` y el procedimiento en `tests/auditoria-cdp.cjs`.
- Se generaron PDF A4 de U1, U5 y U7. Se extrajo texto de todas las páginas, se comprobó presencia de las 2, 4 y 3 alternativas respectivas, la respuesta de U5, ausencia de nota docente y glifos fuera del tamaño de página. Se renderizaron páginas de inicio, mitad y final y se examinaron muestras; no se revisaron visualmente todas las páginas. Los PDF tienen 46, 48 y 37 páginas respectivamente.

## Hallazgos y correcciones

| Severidad | Hallazgo | Resultado |
|---|---|---|
| Crítico | Los trazados de ciclos mostraban `2147483648` como valor `int` tras desbordamiento, lo que no corresponde a Java. | Corregida la aritmética de 32 bits y la pausa de seguridad; prueba de regresión añadida. |
| Alto | La guía dirigida a docentes de U7 aparecía en la página pública y en el PDF. | Se excluye de la salida pública sin alterar la fuente; prueba de regresión añadida. |
| Medio | Un selector de U3 expandía la página a 417 px en una ventana de 375 px. | Corregidos los límites de anchura; Chrome volvió a comprobar 375 px. |
| Medio | El PDF inicial de U5 terminaba con una página casi vacía. | Reducido el margen entre párrafos solo en impresión; el PDF regenerado tiene 48 páginas y su última página contiene el cierre completo. |
| Bajo | Numeración duplicada: U2 `13.8` y `13.9`; U3 `10.9`; U7 `13.18`. | Pendiente de revisión editorial; no se cambiaron los Markdown por tratarse de numeración cosmética. |
| Medio | Algunas explicaciones y pistas siguen visibles junto a consignas sin delimitación editorial inequívoca. | Pendiente de marcación y revisión docente; no se ocultó contenido de forma automática. |

Archivos de producto corregidos: `generar.py`, `assets/style.css`, `assets/recursos-3b-modelos.js` y los HTML regenerados. Se añadieron o ampliaron las pruebas `tests/recursos-3b.test.cjs`, `tests/test_navegacion.py`, `tests/auditoria-cdp.cjs`, `tests/auditoria-editorial.py` y `tests/auditoria-pdf.py`. Los resultados de navegador y PDF están en `evidencias-auditoria/resultado.json` y `pdf-resultado.json`.

## Pendiente antes de publicar

1. Probar con lector de pantalla, medir contraste y verificar teclado y foco de todos los controles; no se afirma conformidad WCAG 2.2 AA. No se verificó zoom real del navegador al 200 %.
2. Revisar visualmente el resto de los recursos y páginas PDF, especialmente saltos de tablas y bloques largos; el análisis de coordenadas no demuestra que toda la composición sea óptima.
3. Resolver las numeraciones duplicadas y acordar marcadores editoriales para pistas y soluciones que aún se muestran inmediatamente.
4. Probar la publicación en la ruta relativa definitiva y realizar una revisión pedagógica docente de las interacciones con estudiantes.

No se realizó commit ni despliegue.
