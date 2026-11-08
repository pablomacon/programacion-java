import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import generar


class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.article = False
        self.headings = []
        self.heading = None
        self.code = []
        self.pre = False
        self.current_code = ''
        self.resource_ids = []
        self.tags = {}
        self.text = []
        self.references = []
        self.print_copy = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.print_copy:
            if tag not in ('img','br','hr','input','meta','link'): self.print_copy += 1
            return
        if attrs.get('class') == 'respuesta-impresa': self.print_copy = 1; return
        if tag == 'article' and attrs.get('class') == 'prose': self.article = True
        if not self.article: return
        self.tags[tag] = self.tags.get(tag, 0) + 1
        if tag in ('h1','h2','h3','h4','h5','h6'): self.heading = [tag, '']
        if tag == 'pre': self.pre = True; self.current_code = ''
        if 'data-recurso' in attrs: self.resource_ids.append(attrs['data-recurso'])
        if tag in ('img','a'):
            value = attrs.get('src') or attrs.get('href')
            if value: self.references.append(value)

    def handle_endtag(self, tag):
        if self.print_copy: self.print_copy -= 1; return
        if not self.article: return
        if self.heading and tag == self.heading[0]:
            self.headings.append(tuple(self.heading)); self.heading = None
        if tag == 'pre': self.code.append(self.current_code); self.pre = False
        if tag == 'article': self.article = False

    def handle_data(self, data):
        if self.print_copy: return
        if not self.article: return
        self.text.append(data)
        if self.heading: self.heading[1] += data
        if self.pre: self.current_code += data


def plain_inline(token):
    # Los títulos son Markdown: eliminar sus marcas usando el mismo parser,
    # pero extraer el texto del HTML de forma independiente.
    class Text(HTMLParser):
        def __init__(self): super().__init__(); self.parts=[]
        def handle_data(self, data): self.parts.append(data)
    p=Text(); p.feed(generar.MARKDOWN.renderInline(token.content)); return ''.join(p.parts)


class TextWithoutResources(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True); self.skip=0; self.parts=[]; self.answer=False; self.summary=False
    def handle_starttag(self, tag, attrs):
        if tag == 'details' and dict(attrs).get('class') == 'respuesta': self.answer=True
        if tag == 'summary' and self.answer: self.summary=True
        if self.skip:
            if tag not in ('img','br','hr','input','meta','link'): self.skip += 1
        elif 'data-recurso' in dict(attrs) or dict(attrs).get('class') == 'respuesta-impresa': self.skip=1
        elif tag in ('p','li','tr','pre','h1','h2','h3','h4','h5','h6','br'): self.parts.append(' ')
    def handle_startendtag(self, tag, attrs):
        if not self.skip: self.parts.append(' ')
    def handle_endtag(self, tag):
        if tag == 'summary' and self.summary: self.summary=False
        if tag == 'details' and self.answer: self.answer=False
        if self.skip: self.skip -= 1
        elif tag in ('p','li','tr','pre','h1','h2','h3','h4','h5','h6'): self.parts.append(' ')
    def handle_data(self, data):
        if not self.skip and not self.summary: self.parts.append(data)


class EditorialTests(unittest.TestCase):
    def test_enlaces_y_recursos_locales(self):
        class Links(HTMLParser):
            def __init__(self): super().__init__(); self.refs=[]
            def handle_starttag(self,tag,attrs):
                a=dict(attrs)
                if tag in ('a','link','img','script'):
                    ref=a.get('href') or a.get('src')
                    if ref: self.refs.append(ref)
        for file in [ROOT/'index.html',*(ROOT/f'unidad-{n:02}.html' for n in range(1,8))]:
            parser=Links(); parser.feed(file.read_text(encoding='utf-8'))
            for ref in parser.refs:
                if not re.match(r'^(https?:|mailto:|#)',ref):
                    self.assertTrue((file.parent/ref.split('#')[0]).is_file(),f'{file.name}: {ref}')
        for name in ('inter-variable.woff2','montserrat-variable.woff2','fira-code-variable.woff2'):
            self.assertTrue((ROOT/'assets/fonts'/name).is_file())

    def test_contenido_y_estructura_de_las_siete_unidades(self):
        registry = json.loads((ROOT/'registro-recursos.json').read_text(encoding='utf-8'))
        seen = []
        for entry in generar.VERIFICACION['unidades']:
            n=entry['unidad']; raw=(ROOT/f'contenido/unidad-{n:02}.md').read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(),entry['sha256'])
            source=raw.decode('utf-8'); tokens=generar.MARKDOWN.parse(generar.public_source(source,n))
            page=(ROOT/f'unidad-{n:02}.html').read_text(encoding='utf-8')
            dom=ArticleParser(); dom.feed(page)
            headings=[(token.tag,plain_inline(tokens[i+1])) for i,token in enumerate(tokens) if token.type=='heading_open']
            self.assertEqual(dom.headings,headings, f'U{n}: encabezados')
            code=[t.content for t in tokens if t.type in ('fence','code_block')]
            self.assertEqual(dom.code,code, f'U{n}: bloques de código')
            for kind,tag in [('bullet_list_open','ul'),('ordered_list_open','ol'),('list_item_open','li'),('table_open','table'),('tr_open','tr')]:
                self.assertEqual(dom.tags.get(tag,0),sum(t.type==kind for t in tokens), f'U{n}: {tag}')
            # Comparar todo el texto visible del capítulo frente al Markdown,
            # excluyendo solo los componentes insertados y los comentarios HTML.
            reference=TextWithoutResources(); reference.feed(generar.MARKDOWN.render(generar.public_source(source,n)))
            student=TextWithoutResources()
            article=re.search(r'<article class="prose">(.*?)</article>',page,re.S).group(1)
            student.feed(article)
            normalize=lambda parts: re.sub(r'\s+',' ',''.join(parts)).strip()
            self.assertEqual(normalize(student.parts),normalize(reference.parts),f'U{n}: texto completo')
            self.assertEqual(dom.resource_ids,entry['marcadores'])
            self.assertNotIn('<!-- PM-',page)
            self.assertNotIn('Estado:</strong> reconstrucción editorial',page)
            for ref in dom.references:
                if not re.match(r'^(https?:|mailto:|#)',ref): self.assertTrue((ROOT/ref.split('#')[0]).exists(),ref)
            seen.extend(dom.resource_ids)
        self.assertEqual(len(seen),23)
        self.assertEqual(len(set(seen)),23)
        self.assertEqual([r['id'] for r in registry],seen)

    def test_u5_extensa_y_legado(self):
        source=(ROOT/'contenido/unidad-05.md').read_text(encoding='utf-8')
        self.assertEqual(len(re.findall(r'^# (?:[1-9]|1[0-4])\. ',source,re.M)),14)
        dom=ArticleParser(); dom.feed((ROOT/'unidad-05.html').read_text(encoding='utf-8'))
        headings=' '.join(x[1] for x in dom.headings)
        for letter in 'ABCDEFGHIJKLMNOPQRS':
            self.assertRegex(headings,rf'Actividad {letter}\b')
        self.assertIn('Problema integrador',headings)
        self.assertNotIn('Checklist docente y continuidad',headings)
        self.assertIn('Próxima clase',' '.join(dom.text))
        self.assertNotIn('data-simulador="burbuja"',(ROOT/'unidad-05.html').read_text(encoding='utf-8'))
        self.assertIn("mount('burbuja'",(ROOT/'assets/simuladores.js').read_text(encoding='utf-8'))
        self.assertTrue((ROOT/'referencias/unidad-05-piloto-reconstruccion.md').is_file())

    def test_insercion_falla_si_id_no_coincide(self):
        source=(ROOT/'contenido/unidad-05.md').read_text(encoding='utf-8')
        with self.assertRaises(ValueError): generar.process_unit(5,source.replace('id="u05-arreglo-indices"','id="u05-inventado"',1),generar.VERIFICACION['unidades'][4]['marcadores'])

if __name__=='__main__': unittest.main()
