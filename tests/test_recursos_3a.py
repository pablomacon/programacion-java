import json
from html.parser import HTMLParser
from pathlib import Path
import unittest
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import generar

class Resources(HTMLParser):
    def __init__(self): super().__init__(); self.ids=[]; self.mounts=[]; self.fallbacks=0; self.pending=0; self.images=[]; self.heading=''; self.reading_heading=False; self.at={}
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag in ('h1','h2','h3','h4','h5','h6'): self.reading_heading=True;self.heading=''
        if 'data-recurso' in a: self.ids.append(a['data-recurso']); self.at[a['data-recurso']]=self.heading
        if 'data-componente-interactivo' in a:self.mounts.append(a['data-componente-interactivo'])
        if 'data-alternativa' in a:self.fallbacks+=1
        if a.get('class')=='recurso-pendiente':self.pending+=1
        if tag=='img':self.images.append(a.get('src'))
    def handle_data(self,data):
        if self.reading_heading:self.heading+=data
    def handle_endtag(self,tag):
        if tag in ('h1','h2','h3','h4','h5','h6'):self.reading_heading=False

class Integracion(unittest.TestCase):
    def test_ocho_componentes_en_marcadores_y_respaldo(self):
        registry=json.loads((ROOT/'registro-recursos.json').read_text(encoding='utf8'))
        self.assertEqual(len(registry),23)
        targets={key for key in generar.INTERACTIVOS if key.startswith(('u01-', 'u02-', 'u03-'))}
        self.assertEqual(len(targets),8)
        found=[];pending=0;alternatives=0
        for n in range(1,8):
            content=(ROOT/f'unidad-{n:02}.html').read_text(encoding='utf8');p=Resources();p.feed(content)
            found.extend(p.mounts);pending+=p.pending;alternatives+=p.fallbacks
            for resource in (x for x in registry if x['unidad']==n):
                self.assertEqual(p.ids.count(resource['id']),1)
                self.assertEqual(p.at[resource['id']],resource['seccion'])
                if resource['id'] in targets:self.assertEqual(p.mounts.count(resource['id']),1)
            if n<=3:
                self.assertIn('assets/recursos-modelos.js',content);self.assertIn('assets/recursos-interactivos.js',content)
            if n==1:self.assertIn('assets/bidones-problema.png',p.images)
        self.assertEqual(set(found) & targets,targets);self.assertEqual(len(found),22)
        self.assertEqual(alternatives,22);self.assertEqual(pending,0)
        css=(ROOT/'assets/style.css').read_text(encoding='utf8')
        self.assertIn('.alternativa-impresa{display:none}',css)
        self.assertIn('.alternativa-impresa{display:block}',css)

if __name__=='__main__':unittest.main()
