from pathlib import Path
from html.parser import HTMLParser
import json
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import generar

class Scanner(HTMLParser):
    def __init__(self):super().__init__();self.mounts=[];self.fallbacks=0;self.pending=0;self.scripts=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'data-componente-interactivo' in a:self.mounts.append(a['data-componente-interactivo'])
        if 'data-alternativa' in a:self.fallbacks+=1
        if a.get('class')=='recurso-pendiente':self.pending+=1
        if tag=='script':self.scripts.append(a.get('src'))

class Recursos3B(unittest.TestCase):
    def test_ocho_montajes_y_seis_pendientes(self):
        ids={key for key in generar.INTERACTIVOS if key.startswith(('u04-','u05-'))}
        self.assertEqual(len(ids),8)
        all_mounts=[];pending=0
        for n in range(1,8):
            p=Scanner();p.feed((ROOT/f'unidad-{n:02}.html').read_text(encoding='utf8'))
            all_mounts+=p.mounts;pending+=p.pending
            if n in (4,5):
                self.assertEqual(len(p.mounts),4)
                self.assertEqual(p.fallbacks,4)
                self.assertEqual(p.scripts[-2:],['assets/recursos-3b-modelos.js','assets/recursos-3b.js'])
            if n>=6:self.assertEqual(p.pending,0)
        for ident in ids:self.assertEqual(all_mounts.count(ident),1,ident)
        self.assertEqual(len(all_mounts),22);self.assertEqual(pending,0)
        registry=json.loads((ROOT/'registro-recursos.json').read_text(encoding='utf8'))
        self.assertEqual(len(registry),23)
        self.assertEqual(sum(x['estado'].startswith('implementado') for x in registry),22)

if __name__=='__main__':unittest.main()
