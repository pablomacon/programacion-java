# Verificación de la fase 2B

## Comprobaciones realizadas

- El servidor `127.0.0.1:8766` respondió con HTTP 200 para la portada y las unidades 1, 5 y 7.
- `python -m unittest discover -s tests -p "test_*.py"`: 10 pruebas aprobadas. Se verificaron hashes de las siete fuentes, texto y estructura del capítulo, bloques de código, actividades, índices, IDs únicos, anclas, enlaces entre unidades y la estabilidad de los 23 registros de recursos.
- `node --test tests/simuladores.test.cjs`: 3 pruebas aprobadas del código heredado, que permanece fuera de las páginas canónicas.
- Las pruebas inspeccionan la estructura de las siete páginas: un logotipo en la cabecera, índice con `details`/`summary`, enlace para saltar al contenido, destinos internos y etiquetas de código reconocidas únicamente por señales explícitas.
- La regla que oculta el checklist se ejecuta únicamente para U5; se comprobó que mantiene el párrafo «Próxima clase». Las otras seis fuentes pasan intactas al procesador.
- Se revisaron las reglas CSS de foco, anchos, desplazamiento y medios de impresión. Esto es análisis estático, no una prueba visual ni una auditoría WCAG.

## Correcciones aplicadas

- Se declaró `@page { size: A4; }` en impresión.
- Los bloques de código con líneas de más de 25 caracteres pueden recibir foco para facilitar su desplazamiento mediante teclado en pantallas estrechas. El texto y la indentación del código no cambiaron.
- Se añadieron pruebas de navegación, etiquetas y configuración de impresión en `tests/test_navegacion.py`.

## Pendiente

El servicio de acceso a navegadores devolvió «browser access host is unavailable»; por ello no se pudo inspeccionar visualmente escritorio, móvil, zoom, foco real ni la paginación. Tampoco se generaron ni revisaron PDF o capturas. El funcionamiento real del desplazamiento con teclado y la impresión A4 necesitan confirmarse en un navegador. **La fase 2 sigue pendiente de esas verificaciones**, antes de pasar a la fase 3.
