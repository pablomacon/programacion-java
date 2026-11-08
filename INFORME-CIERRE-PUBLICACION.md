# Cierre editorial y validación para publicación

**Dictamen: PUBLICACIÓN CONDICIONADA.** No se conocen defectos críticos o altos pendientes en los casos examinados, pero siguen pendientes pruebas relevantes de accesibilidad y revisión docente. Este dictamen no acredita conformidad WCAG.

## Estado inicial y alcance

Se partió de la auditoría anterior, con 15 pruebas Python y 33 Node aprobadas, 23 IDs y las correcciones previas conservadas. Se trabajó sobre el generador existente, sin rediseño, simuladores nuevos, commit ni despliegue. La fuente de cada capítulo es `contenido/unidad-01.md` a `contenido/unidad-07.md` respectivamente.

## Correcciones editoriales

Los únicos cambios de Markdown fueron estos números de encabezados; el contenido anterior y posterior permanece intacto. Se conservan anclas anteriores para los títulos afectados.

| Unidad | Encabezado anterior | Encabezado corregido |
|---|---|---|
| 2 | 13.8. Nota técnica: cerrar Scanner cuando utiliza System.in | 13.10. Nota técnica: cerrar Scanner cuando utiliza System.in |
| 2 | 13.9. Ruta de recuperación: del error a la causa | 13.11. Ruta de recuperación: del error a la causa |
| 3 | 10.9. Estrategia general para convertir una regla en una condición | 10.12. Estrategia general para convertir una regla en una condición |
| 7 | 13.18. Laboratorio guiado de modelado sin clase predeterminada | 13.19. Laboratorio guiado de modelado sin clase predeterminada |
| 7 | 13.19. Pistas y soluciones en capas para las actividades A–W | 13.20. Pistas y soluciones en capas para las actividades A–W |

El análisis automático de encabezados no detectó números duplicados, números fuera de orden ni títulos duplicados después del cambio. No constituye una revisión semántica exhaustiva de todos los apartados.

## Respuestas voluntarias

Hay 12 respuestas identificadas mediante coincidencia exacta de la fuente o límites explícitos de sección en `generar.py`, sin reglas basadas en palabras genéricas. Se usa `details`/`summary`, cerrado inicialmente y sin dependencia de JavaScript; se conserva una copia para impresión. Si cambia el texto delimitador, el generador falla en lugar de ocultar otro contenido. La fuente conserva íntegra cada respuesta.

- U3: predicción de salida de `switch`.
- U4: salida y explicación del primer `while`; valor final al reemplazar asignaciones.
- U5: valor de la última asignación (ya existía); valor inicial del arreglo; promedio calculado antes de modificar el arreglo; máximo inicializado en cero.
- U6: invocaciones con 16 y 20; copia de un `int` en un método; división entera y de punto flotante entre cero.
- U7: estado inicial de otro objeto y argumento faltante del constructor.

No se crearon pistas ni soluciones. Las explicaciones conceptuales posteriores y los ejemplos resueltos permanecen visibles. Pendiente de decisión docente: la secuencia sobre división y `NaN` en U6 ya explica el comportamiento antes de formular su predicción; determinar si conviene mover esa consigna. Revisar igualmente la presentación de pistas y soluciones agrupadas de U7 y otras consignas cuyo alcance no se puede delimitar sin interpretación pedagógica.

## Teclado, accesibilidad y contraste

En Chrome se abrió el índice con Espacio en las siete unidades, se comprobó Tab hacia el primer enlace y Shift+Tab de regreso, y se activó con Espacio un botón representativo por unidad con foco visible. En U3–U7 se abrieron y cerraron los primeros desplegables con Espacio; en U5 se probó también el índice con Enter y la apertura de una respuesta con JavaScript desactivado. Los escenarios automatizados anteriores volvieron a ejercitar avance, retroceso y reinicio mediante interacción de navegador. No se ha probado manualmente cada control, orden completo, ausencia de trampas en todos los componentes ni activación de cada variante mediante teclado.

No se utilizó lector de pantalla real. Los 22 componentes se montaron, los controles examinados tenían etiquetas y los botones tenían nombres; esto no verifica anuncios de `aria-live`, lectura de diagramas ni experiencia real de lector de pantalla.

La medición calculada para siete pares concretos del CSS dio: texto principal 15,65:1; secundario 7,02:1; enlace/botón sobre blanco 6,04:1; acento sobre fondo de recurso 5,57:1; código 15,32:1; foco sobre blanco 6,04:1 y borde de campo sobre blanco 3,69:1. Los pares elegidos cumplen sus umbrales de 4,5:1 para texto o 3:1 para componentes. Es una muestra, no un análisis automático completo de estados, mensajes y fondos compuestos. Detalles: `evidencias-cierre/contraste.json`.

Chrome comprobó ausencia de desbordamiento horizontal global en las siete unidades a 320, 341, 375, 683, 768, 1366, 1440 y 1920 px. Los 341 y 683 px son pruebas de anchura, **no zoom real** al 400 % o 200 %. El zoom real y la ejecución completa de simuladores ampliados quedan pendientes.

## Impresión y PDF

Se regeneraron PDF A4 de U1, U5 y U7: 46, 48 y 37 páginas. La extracción de todas las páginas detectó las alternativas impresas de los recursos, la explicación de U5, ninguna página con menos de 80 caracteres, ningún glifo fuera de la página y ninguna guía docente detectada. Se renderizaron primera, central y última página de cada PDF; se examinaron visualmente muestras, incluidas la central de U5 y el cierre de U7. Se comprobó visualmente la última página final de U5: contiene el cierre completo y el PDF tiene 48 páginas. No se ha examinado visualmente cada tabla, salto, título o bloque de los 131 folios.

## Integridad y regresión

- `python -m unittest discover -s tests -p 'test_*.py'`: **17 aprobadas**. Incluyen comparación del texto, encabezados, listas, tablas, código y 23 IDs, así como reversión en memoria de los cambios de numeración para recuperar hashes anteriores.
- `node --test tests\\recursos-3c.test.cjs tests\\recursos-3b.test.cjs tests\\recursos-3a.test.cjs tests\\interfaz-3a.test.cjs tests\\simuladores.test.cjs`: **33 aprobadas**, incluida compilación y ejecución de cinco programas Java completos.
- Chrome/CDP: 22 recursos montados y siete escenarios representativos aprobados; alternativas textuales 22/22 sin JavaScript; ninguna imagen rota ni error de consola detectado. Esto no implica prueba exhaustiva de todas las entradas.
- Los 23 IDs siguen siendo únicos: 22 componentes interactivos y la imagen canónica de bidones. Se conservan los respaldos de simuladores. La guía docente de U7 y el checklist docente de U5 siguen excluidos de la vista estudiantil; el contenido fuente permanece.

### SHA-256 modificados

| Fuente | Antes de este cierre | Después |
|---|---|---|
| U2 | `6ec409b0ac1449d8a28ae6069adb22bb65d0b4f5f6b9d27fd701cf32318a1891` | `34e08b125c5cab2321566993746d31c5fc8d854eb2792bd83f45d28d6344d72e` |
| U3 | `deed3272b7ceef51ce50a7ef1035c72dc53c12056d4ca3dfe97c224466d26241` | `81fd1dc0e3284dc6bce06a10374969e0df8481914686781790e2aeca715fd435` |
| U7 | `d80562656b01651a99dd7beaeb0cef603a8e86cda935db00e8fa938e752de85b` | `d5ea8ba6cb0a01f510c7d67e0b62ef72cfa425bd70c4950fe5cddb8d0bc65e6a` |

U1, U4, U5 y U6 mantienen los hashes previos registrados en `verificacion-fuentes.json`. `documentacion/VERIFICACION.json` se conserva como inventario histórico; U1 y U5 ya tenían las correcciones autorizadas de fase 2C.

## Archivos y evidencias

Modificados en este cierre: `contenido/unidad-02.md`, `contenido/unidad-03.md`, `contenido/unidad-07.md`, `generar.py`, `verificacion-fuentes.json`, `tests/test_integridad.py` y los HTML regenerados. Añadidos: `tests/test_cierre_editorial.py`, `tests/cierre-cdp.cjs`, `tests/cierre-pdf.py`, `tests/cierre-contraste.py`, este informe y `evidencias-cierre/`. El directorio `evidencias-auditoria/` anterior se conservó. El resultado detallado de navegador está en `evidencias-cierre/resultado.json`; PDF y rasterizaciones en el mismo directorio; análisis en `pdf-resultado.json`.

## Pendientes y severidad

- **Medio:** evaluación práctica con lector de pantalla y revisión completa de teclado, anuncios, foco y contrastes en todos los estados; no se puede descartar que aparezcan barreras altas.
- **Medio:** comprobar zoom real al 200 % y 400 %, incluidos controles en funcionamiento; revisar visualmente las páginas PDF restantes.
- **Medio:** revisión docente de secuenciación de pistas y soluciones, exactitud pedagógica completa y funcionamiento autónomo con estudiantes.
- **Medio:** comprobar rutas y recursos en la ubicación definitiva antes de publicar.

No se conocen defectos críticos o altos pendientes entre los casos comprobados. Las verificaciones no realizadas no se cuentan como satisfactorias.
