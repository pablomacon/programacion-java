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

class Recursos3C(unittest.TestCase):
    def test_seis_montajes_sin_pendientes(self):
        ids={k for k in generar.INTERACTIVOS if k.startswith(('u06-','u07-'))}
        self.assertEqual(len(ids),6)
        mounts=[]
        for n in range(1,8):
            p=Scanner();p.feed((ROOT/f'unidad-{n:02}.html').read_text(encoding='utf8'))
            mounts+=p.mounts
            self.assertEqual(p.pending,0)
            if n in (6,7):
                self.assertEqual(len(p.mounts),3);self.assertEqual(p.fallbacks,3)
                self.assertEqual(p.scripts[-2:],['assets/recursos-3c-modelos.js','assets/recursos-3c.js'])
        for ident in ids:self.assertEqual(mounts.count(ident),1,ident)
        self.assertEqual(len(mounts),22)
        registry=json.loads((ROOT/'registro-recursos.json').read_text(encoding='utf8'))
        self.assertEqual(len(registry),23)
        self.assertEqual(sum(r['estado'].startswith('implementado') for r in registry),22)

if __name__=='__main__':unittest.main()
