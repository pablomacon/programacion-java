# Ajustes editoriales y de anchura — fase 2C

Las fuentes se verificaron contra sus hashes vigentes antes de editarlas. El único cambio en cada una de las dos unidades es el número del encabezado indicado; las pruebas revierten ese cambio en memoria y comprueban el hash anterior. Los documentos del respaldo y `documentacion/VERIFICACION.json` permanecen como registro histórico del paquete anterior.

| Fuente | Cambio | SHA-256 anterior | SHA-256 vigente |
|---|---|---|---|
| Unidad 1 | `15.8` → `15.7`, taller de transferencia | `9ba6176cb3be42789da866ec380c5b20f916a1fd0e0582a92037ac12dd081fb6` | `330926b02a175d3cfd305c87900f4bea71913e0bc79543e5b3b205da96ba1d10` |
| Unidad 5 | Segunda sección `11.12` → `11.13`, transferencia | `8b4c2863601bcdcff55f396c5c45521a96f5d83cc928c42e7a833a6244bd4649` | `75686428c11a88ca5ba51c899554b2c2367588e6a6884bcea09262827a5ad6a3` |

Los hashes de las unidades 2, 3, 4, 6 y 7 no cambiaron. `verificacion-fuentes.json` registra únicamente los dos hashes nuevos. El generador conserva alias para los identificadores anteriores de ambos encabezados y comprueba los 23 IDs de recurso.

La columna del capítulo tiene un máximo de 82 rem (1.312 px con tamaño raíz de 16 px); la lectura se limita a 90 caracteres CSS (`ch`). Código, tablas y recursos utilizan las tres columnas disponibles. La impresión vuelve al flujo normal y mantiene las reglas A4.

## Predicciones

En U5, apartado 1.2, la consigna «Antes de ejecutarlo, predice la salida» y su respuesta inmediata se identificaron mediante el texto completo exacto de la fuente. La página presenta la explicación en un `details` nativo; existe una copia exclusiva para impresión. La fuente permanece intacta. Si cambia ese párrafo, la generación se detiene para revisión.

Otros casos requieren delimitación editorial explícita antes de ocultar contenido: U1, sección 3.6 (predicción y desarrollo en apartados siguientes); U5, sección 10 (el error, su explicación y la solución ocupan varios bloques); y U5, sección 11.13 (las dos pistas comparten un párrafo). Conviene marcar por separado consigna, pista, respuesta y fin de respuesta en los Markdown; no se infieren automáticamente.

## Verificación y límites

El acceso al navegador del entorno respondió «browser access host is unavailable». Por tanto no se pudieron verificar visualmente 1366, 1440, 1920 px ni móvil, ni comprobar un PDF nuevo. La presentación de la respuesta impresa y los posibles desbordamientos se comprobaron por estructura y reglas CSS, no mediante renderizado. Permanecen pendientes esas revisiones visuales y de teclado real.
