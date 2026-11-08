from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import json
import hashlib
import re
import sys
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import generar


class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids=[]; self.links=[]; self.headings={}; self.stack=[]; self.toc=[]
        self.header_images=[]; self.header=False; self.in_toc=False; self.pre=[]

    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        if tag=='header' and attrs.get('class')=='site-header': self.header=True
        if tag=='img' and self.header: self.header_images.append(attrs)
        if tag=='details' and attrs.get('class')=='contents': self.in_toc=True
        if tag=='a':
            self.links.append(attrs)
            if self.in_toc: self.toc.append([attrs.get('href',''), ''])
        if tag in ('h1','h2','h3','h4','h5','h6'):
            self.stack.append([tag,attrs.get('id'), ''])
        if tag=='pre': self.pre.append(attrs)

    def handle_data(self, data):
        if self.stack: self.stack[-1][2]+=data
        if self.in_toc and self.toc: self.toc[-1][1]+=data

    def handle_endtag(self,tag):
        if tag=='header': self.header=False
        if tag=='details': self.in_toc=False
        if self.stack and tag==self.stack[-1][0]:
            _, ident, text=self.stack.pop(); self.headings[ident]=text


class NavegacionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs={}
        for name in ['index.html']+[f'unidad-{i:02}.html' for i in range(1,8)]:
            p=Document(); p.feed((ROOT/name).read_text(encoding='utf8')); cls.docs[name]=p

    def test_ids_y_destinos(self):
        for name, doc in self.docs.items():
            duplicates=[key for key,count in Counter(doc.ids).items() if count>1]
            self.assertEqual(duplicates,[],name)
            for link in doc.links:
                ref=link.get('href',''); parsed=urlsplit(ref)
                if parsed.scheme or parsed.netloc: continue
                filename=parsed.path or name
                if filename in self.docs and parsed.fragment:
                    self.assertIn(unquote(parsed.fragment),self.docs[filename].ids,f'{name}: {ref}')

    def test_indice_y_navegacion_entre_unidades(self):
        for n in range(1,8):
            doc=self.docs[f'unidad-{n:02}.html']
            self.assertGreater(len(doc.toc),10)
            for href,label in doc.toc:
                self.assertIn(href[1:],doc.headings)
                self.assertEqual(label.strip(),doc.headings[href[1:]].strip())
            refs=[a.get('href') for a in doc.links]
            self.assertIn('index.html#unidades',refs)
            self.assertIn('#top',refs)
            self.assertEqual([a.get('href') for a in doc.links if a.get('rel')=='prev'],[f'unidad-{n-1:02}.html'] if n>1 else [])
            self.assertEqual([a.get('href') for a in doc.links if a.get('rel')=='next'],[f'unidad-{n+1:02}.html'] if n<7 else [])
        self.assertEqual(len([a for a in self.docs['index.html'].links if re.fullmatch(r'unidad-\d\d\.html',a.get('href',''))]),7)

    def test_cabecera_y_accesibilidad_estructural(self):
        for name,doc in self.docs.items():
            self.assertEqual(len(doc.header_images),1,name)
            self.assertEqual(doc.header_images[0].get('src'),'assets/logo-profe-macon.png')
            self.assertEqual(doc.header_images[0].get('alt'),'Profe Macón')
            html=(ROOT/name).read_text(encoding='utf8')
            self.assertIn('href="#contenido"',html)
            if name!='index.html':
                self.assertIn('<summary>Índice de la unidad</summary>',html)
                self.assertIn('aria-label="Tabla: desplazar horizontalmente si es necesario"',html)
                for block in doc.pre:
                    self.assertTrue(block.get('data-etiqueta'))

    def test_impresion_y_fuente_docente(self):
        css=(ROOT/'assets/style.css').read_text(encoding='utf8')
        self.assertRegex(css,r'@page\s*\{\s*size\s*:\s*A4')
        self.assertIn('white-space:pre-wrap',css)
        self.assertIn(':focus-visible',css)
        for n in range(1,8):
            source=(ROOT/f'contenido/unidad-{n:02}.md').read_text(encoding='utf8')
            public=generar.public_source(source,n)
            if n==7:
                title='## Guía breve para la docencia: secuencia de cuatro módulos'
                self.assertEqual(source.count(title),1)
                self.assertEqual(public,source.split(title,1)[0])
                self.assertIn('## 15.9. Cierre del recorrido anual',public)
                self.assertNotIn('Checklist docente de cierre',public)
                html=(ROOT/'unidad-07.html').read_text(encoding='utf8')
                self.assertNotIn('Checklist docente de cierre',html)
                self.assertNotIn(title,html)
                self.assertIn('15.9. Cierre del recorrido anual',html)
            elif n!=5: self.assertEqual(public,source)
            else:
                self.assertNotIn('# Checklist docente y continuidad',public)
                self.assertIn('**Próxima clase:**',public)
                self.assertEqual(public, re.sub(r'(?m)^# Checklist docente y continuidad\s*\n(?:\s*\n)?(?:- [^\n]*\n)+','',source))

    def test_etiquetas_de_codigo_solo_con_indicios_explicitos(self):
        examples=[
            ('**Programa completo:**\n\n```java\nclass Main {}\n```','Programa Java completo'),
            ('**Fragmento para analizar:**\n\n```java\nint x = 1;\n```','Fragmento Java'),
            ('**Ejemplo incorrecto:**\n\n```java\nint x = ;\n```','Java · ejemplo incorrecto'),
            ('Pseudocódigo:\n\n```text\nLEER valor\n```','Pseudocódigo'),
            ('Salida esperada:\n\n```text\n42\n```','Salida esperada'),
            ('Un fragmento puede tener errores.\n\n```java\nint x = 1;\n```','Java'),
        ]
        for source,label in examples:
            rendered=generar.MARKDOWN.render(source)
            self.assertIn(f'data-etiqueta="{label}"',rendered)

    def test_registro_no_cambia_al_generar(self):
        registry=json.loads((ROOT/'registro-recursos.json').read_text(encoding='utf8'))
        before=(ROOT/'registro-recursos.json').read_bytes()
        self.assertEqual(len({x['id'] for x in registry}),23)
        generar.build()
        self.assertEqual((ROOT/'registro-recursos.json').read_bytes(),before)

    def test_correcciones_editoriales_exactas(self):
        revisions={1:('## 15.8. Taller de transferencia: diseñar el estado antes de actuar','## 15.7. Taller de transferencia: diseñar el estado antes de actuar'),5:('## 11.12. Transferencia: decidir qué necesitamos conservar','## 11.13. Transferencia: decidir qué necesitamos conservar')}
        original_hashes={1:'9ba6176cb3be42789da866ec380c5b20f916a1fd0e0582a92037ac12dd081fb6',5:'8b4c2863601bcdcff55f396c5c45521a96f5d83cc928c42e7a833a6244bd4649'}
        for n in range(1,8):
            actual=(ROOT/f'contenido/unidad-{n:02}.md').read_bytes()
            if n in revisions:
                old,new=(s.encode('utf-8') for s in revisions[n])
                self.assertEqual(actual.count(new),1)
                self.assertEqual(hashlib.sha256(actual.replace(new,old,1)).hexdigest(),original_hashes[n])
        for n,alias in [(1,'seccion-15-8-taller-de-transferencia-disenar-el-estado-antes-de-actuar'),(5,'seccion-11-12-transferencia-decidir-que-necesitamos-conservar')]:
            self.assertIn(alias,self.docs[f'unidad-{n:02}.html'].ids)

    def test_respuesta_voluntaria_y_recursos(self):
        html=(ROOT/'unidad-05.html').read_text(encoding='utf8')
        self.assertIn('Antes de ejecutarlo, predice la salida:</p><details class="respuesta"><summary>Ver explicación</summary>',html)
        self.assertIn('es <strong>9</strong>',html)
        self.assertIn('<div class="respuesta-impresa" aria-hidden="true"><p>es <strong>9</strong>',html)
        css=(ROOT/'assets/style.css').read_text(encoding='utf8')
        self.assertIn('.respuesta-impresa{display:none}',css)
        self.assertIn('.respuesta-impresa{display:block;break-inside:avoid}',css)
        for n in range(1,8):
            html=(ROOT/f'unidad-{n:02}.html').read_text(encoding='utf8')
            self.assertNotIn('Podés estudiar este concepto',html)
            self.assertNotIn('Recurso interactivo o visual en preparación.',html)

if __name__=='__main__': unittest.main()
