from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parent
source = (ROOT / 'contenido/unidad-05.md').read_text(encoding='utf-8')

def inline(text):
    parts = re.split(r'(`[^`]+`)', text)
    for i, part in enumerate(parts):
        if part.startswith('`') and part.endswith('`'):
            parts[i] = '<code>' + escape(part[1:-1]) + '</code>'
        else:
            parts[i] = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escape(part))
    return ''.join(parts)

def render(markdown):
    lines = markdown.splitlines()
    result, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif line.startswith('```'):
            lang = line[3:].strip(); i += 1; block = []
            while i < len(lines) and not lines[i].startswith('```'):
                block.append(lines[i]); i += 1
            if i == len(lines): raise ValueError('Bloque de código sin cerrar')
            result.append('<pre><code class="language-' + escape(lang) + '">' + escape('\n'.join(block)) + '</code></pre>')
            i += 1
        elif line.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|\-]+\|$', lines[i+1]):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([inline(x.strip()) for x in lines[i].strip('|').split('|')]); i += 1
            head = ''.join('<th scope="col">'+cell+'</th>' for cell in rows[0])
            body = ''.join('<tr>'+''.join('<td>'+cell+'</td>' for cell in row)+'</tr>' for row in rows[2:])
            result.append('<div class="table-wrap"><table><thead><tr>'+head+'</tr></thead><tbody>'+body+'</tbody></table></div>')
        elif re.match(r'^#{1,3} ', line):
            match = re.match(r'^(#{1,3}) (.*)', line); level = len(match[1]); title = match[2]
            if level == 1: result.append('<h1>'+inline(title)+'</h1>')
            else:
                n = re.match(r'(\d+)\.', title)
                id_attr = ' id="seccion-'+n[1]+'"' if n else ''
                result.append(f'<h{level}{id_attr}>'+inline(title)+f'</h{level}>')
                if level == 2 and n and n[1] in ('2','7','8'):
                    result.append('<div data-simulador="'+{'2':'indices','7':'busqueda','8':'burbuja'}[n[1]]+'"></div>')
            i += 1
        else:
            paragraph = []
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(('```', '#', '|')):
                paragraph.append(lines[i].rstrip()); i += 1
            result.append('<p>'+'<br>'.join(inline(x) for x in paragraph)+'</p>')
    return '\n'.join(result)

header = '''<header class="site-header"><div class="header-inner"><a class="brand" href="index.html"><img class="brand-pm" src="assets/logo-pm.png" alt="PM"><img src="assets/logo-profe-macon.png" alt="Profe Macón"><span><strong>Programación I</strong><small>1.º BT Informática · DGETP / UTU</small></span></a><nav aria-label="Navegación principal"><a href="index.html">Inicio</a><a href="index.html#unidades">Unidades</a><a href="unidad-05.html">Unidad 5</a></nav></div></header>'''
footer = '''<footer><div class="footer-inner"><img src="assets/logo-pm.png" alt="PM"><span><strong>Programación I · 2026</strong><br>Profe Macón · DGETP / UTU</span></div></footer>'''
def page(title, main, script=''):
    return '<!doctype html>\n<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>'+escape(title)+' · Programación I</title><link rel="icon" href="assets/logo-pm.png"><link rel="stylesheet" href="assets/style.css"></head><body id="top">'+header+main+footer+script+'</body></html>\n'

units = [('Pensar como programadores','Problemas, algoritmos y primeras soluciones.'),('Nuestros primeros programas en Java','Variables, tipos de datos y operaciones.'),('Estructuras condicionales','Decisiones y alternativas.'),('Estructuras iterativas','Repetición, contadores y acumuladores.'),('Arreglos y cadenas de caracteres','Conservar, recorrer y organizar datos.'),('Métodos en Java','Organizar y reutilizar soluciones.'),('Clases y objetos','Representar problemas con objetos.')]
cards = []
for n,(name, desc) in enumerate(units,1):
    content=f'<span class="unit-number">UNIDAD {n:02}</span><h3>{escape(name)}</h3><p>{escape(desc)}</p>'
    cards.append('<a class="unit-card available" href="unidad-05.html">'+content+'<span class="card-link">Explorar unidad <span aria-hidden="true">→</span></span></a>' if n==5 else '<article class="unit-card">'+content+'<span class="pending">Próximamente</span></article>')
home = '''<main><section class="hero"><div class="container"><p class="eyebrow">1.º Bachillerato Tecnológico en Informática · 2026</p><h1>Programación I</h1><p class="lead">Aprender a pensar, construir y comprender programas, paso a paso.</p><a class="button primary" href="#unidades">Explorar las unidades <span aria-hidden="true">→</span></a></div></section><section class="container unit-section" id="unidades"><p class="eyebrow">Recorrido del curso</p><h2>Unidades de aprendizaje</h2><p class="intro">Un recorrido desde los primeros algoritmos hasta las clases y los objetos en Java.</p><div class="units">'''+''.join(cards)+'''</div></section></main>'''
lesson = '<main class="lesson"><a class="back" href="index.html#unidades">← Volver a las unidades</a><p class="eyebrow">Programación I · Unidad 05</p><article class="prose">'+render(source)+'</article><nav class="lesson-bottom" aria-label="Navegación de la unidad"><a href="index.html#unidades">← Todas las unidades</a><a href="#top">Volver arriba ↑</a></nav></main>'
(ROOT/'index.html').write_text(page('Inicio',home),encoding='utf-8')
(ROOT/'unidad-05.html').write_text(page('Unidad 5',lesson,'<script src="assets/simuladores.js" defer></script>'),encoding='utf-8')
