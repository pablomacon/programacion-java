# Programación I 2026

Abrir `index.html` o ejecutar `python -m http.server 8000` en esta carpeta y visitar `http://localhost:8000/`.

Para regenerar las siete páginas: `python generar.py`. El generador usa las siete fuentes revisadas en `contenido/`, valida sus hashes e IDs contra `verificacion-fuentes.json` y registra cada inserción en `registro-recursos.json`. Usa markdown-it-py 3.0.0 y mdurl 0.1.2 incluidos en `vendor/` con sus licencias. Un cambio editorial autorizado requiere actualizar expresamente el hash correspondiente; el generador se detiene ante diferencias o marcadores inesperados.

Pruebas: `python -m unittest discover -s tests -p "test_*.py"` y `node --test tests/simuladores.test.cjs`.

Los capítulos proceden del paquete revisado. En U1 y U5 se corrigió únicamente la numeración de un encabezado; el detalle y los hashes anteriores están en `INFORME-FASE-2C.md`. Las otras cinco fuentes siguen idénticas al paquete. Esto no certifica una comparación literal con todos los borradores históricos. Se ocultan comentarios técnicos y el checklist destinado al docente en U5; se conserva el párrafo «Próxima clase». Los marcadores se conservan sin editar.

La imagen de bidones y los 22 recursos interactivos están integrados en sus marcadores; cada recurso tiene una alternativa textual para ausencia de JavaScript e impresión. Las reglas y controles compartidos están en `assets/recursos-modelos.js` y `assets/recursos-interactivos.js`; las fases 3B y 3C agregan sus propios módulos de modelos y presentación. La verificación visual está pendiente. Los simuladores anteriores siguen en `assets/simuladores.js` con sus pruebas, sin montarse en el sitio. El simulador de burbuja queda preservado como legado, sin incorporarlo a la U5 revisada. La fuente anterior de U5 está en `referencias/`.

Pruebas de los recursos nuevos: `node --test tests/recursos-3a.test.cjs tests/interfaz-3a.test.cjs`.

Pruebas de trazados de U4–U5: `node --test tests/recursos-3b.test.cjs tests/interfaz-3a.test.cjs`.

Pruebas de U6–U7: `node --test tests/recursos-3c.test.cjs tests/interfaz-3a.test.cjs` (requieren `javac` y `java` para compilar los ejemplos completos mostrados).
