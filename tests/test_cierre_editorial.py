import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CAMBIOS = {
    2: ('6ec409b0ac1449d8a28ae6069adb22bb65d0b4f5f6b9d27fd701cf32318a1891', [
        ('13.8. Nota técnica: cerrar Scanner cuando utiliza System.in', '13.10. Nota técnica: cerrar Scanner cuando utiliza System.in'),
        ('13.9. Ruta de recuperación: del error a la causa', '13.11. Ruta de recuperación: del error a la causa')]),
    3: ('deed3272b7ceef51ce50a7ef1035c72dc53c12056d4ca3dfe97c224466d26241', [
        ('10.9. Estrategia general para convertir una regla en una condición', '10.12. Estrategia general para convertir una regla en una condición')]),
    7: ('d80562656b01651a99dd7beaeb0cef603a8e86cda935db00e8fa938e752de85b', [
        ('13.18. Laboratorio guiado de modelado sin clase predeterminada', '13.19. Laboratorio guiado de modelado sin clase predeterminada'),
        ('13.19. Pistas y soluciones en capas para las actividades A–W', '13.20. Pistas y soluciones en capas para las actividades A–W')]),
}

class CierreEditorial(unittest.TestCase):
    def test_cambios_exactos_y_hashes_anteriores(self):
        manifest = json.loads((ROOT/'verificacion-fuentes.json').read_text(encoding='utf8'))
        for n, (before, changes) in CAMBIOS.items():
            data = (ROOT/f'contenido/unidad-{n:02}.md').read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), manifest['unidades'][n-1]['sha256'])
            for old, new in changes:
                old, new = old.encode(), new.encode()
                self.assertEqual(data.count(new), 1)
                data = data.replace(new, old, 1)
            self.assertEqual(hashlib.sha256(data).hexdigest(), before)

    def test_respuestas_cerradas_y_con_copia_impresa(self):
        for n, count in ((3,1),(4,2),(5,4),(6,3),(7,2)):
            page=(ROOT/f'unidad-{n:02}.html').read_text(encoding='utf8')
            self.assertEqual(page.count('<details class="respuesta"><summary>Ver explicación</summary>'),count)
            self.assertEqual(page.count('<div class="respuesta-impresa" aria-hidden="true">'),count)

if __name__ == '__main__': unittest.main()
