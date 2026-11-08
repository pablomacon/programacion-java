"""Genera el sitio estático a partir de los siete capítulos revisados."""
from pathlib import Path
from html import escape
import hashlib
import json
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'vendor'))
from markdown_it import MarkdownIt
from markdown_it.token import Token

VERIFICACION = json.loads((ROOT / 'verificacion-fuentes.json').read_text(encoding='utf-8'))
MARKDOWN = MarkdownIt('commonmark', {'html': True}).enable('table')
UNIDADES = [
    ('Pensar como programadores', 'Problemas, algoritmos y primeras soluciones.'),
    ('Nuestros primeros programas en Java', 'Variables, tipos de datos y operaciones.'),
    ('Estructuras condicionales', 'Decisiones y alternativas.'),
    ('Estructuras iterativas', 'Repetición, contadores y acumuladores.'),
    ('Arreglos y cadenas de caracteres', 'Conservar, recorrer y buscar información.'),
    ('Métodos en Java', 'Organizar y reutilizar soluciones.'),
    ('Clases y objetos', 'Representar problemas con objetos.'),
]

# Vinculaciones editoriales explícitas: texto exacto de la fuente revisada.
# No se infieren respuestas a partir de la proximidad de un encabezado.
PREDICCION_U05 = ('Antes de ejecutarlo, predice la salida: es **9**. Cada asignación reemplaza el valor anterior; '
                  'la variable no conserva un historial. **¿En qué lugar quedó guardada la tercera nota, 8?** '
                  'En ninguno que podamos consultar con este fragmento.')
ANTIGUAS_ANCLAS = {
    '15.7. Taller de transferencia: diseñar el estado antes de actuar': 'seccion-15-8-taller-de-transferencia-disenar-el-estado-antes-de-actuar',
    '11.13. Transferencia: decidir qué necesitamos conservar': 'seccion-11-12-transferencia-decidir-que-necesitamos-conservar',
    '13.10. Nota técnica: cerrar Scanner cuando utiliza System.in': 'seccion-13-8-nota-tecnica-cerrar-scanner-cuando-utiliza-system-in',
    '13.11. Ruta de recuperación: del error a la causa': 'seccion-13-9-ruta-de-recuperacion-del-error-a-la-causa',
    '10.12. Estrategia general para convertir una regla en una condición': 'seccion-10-9-estrategia-general-para-convertir-una-regla-en-una-condicion',
    '13.19. Laboratorio guiado de modelado sin clase predeterminada': 'seccion-13-18-laboratorio-guiado-de-modelado-sin-clase-predeterminada',
    '13.20. Pistas y soluciones en capas para las actividades A–W': 'seccion-13-19-pistas-y-soluciones-en-capas-para-las-actividades-a-w',
}

# Delimitaciones editoriales explícitas, verificadas contra el texto íntegro.
# La pregunta y su respuesta deben coincidir exactamente: nunca se infieren.
RESPUESTAS = {
    4: [('**Predice el valor final antes de continuar.** ¿Vale 20 porque ingresaron 7, 5 y 8?', 'No. Vale **8**. Cada asignación sustituye el valor anterior. La variable no recuerda las cifras que recibió antes.')],
    5: [('¿Qué mostrará?', '**0**. No lo introdujo ningún estudiante: es el valor predeterminado de un elemento `int` recién creado. No debemos interpretar automáticamente cada cero como una nota registrada. El arreglo tiene **cinco posiciones disponibles**, pero todavía no hemos cargado cinco calificaciones.'),
        ('¿Qué muestra?', '**7.0**. Aunque ahora la tercera nota vale 10, el promedio quedó calculado con la suma anterior. Para obtener el promedio actualizado, debemos recorrer y volver a sumar los valores: `7 + 5 + 10 + 6 + 9 = 37`, y entonces `37 / 5.0 = 7.4`.'),
        ('¿Qué muestra?', '**0**, aunque no aparece en el arreglo. Todos los números son menores que cero y el supuesto máximo no se actualiza. Así descubrimos por qué conviene comenzar con `mayor = numeros[0]` cuando el arreglo no está vacío. Luego podemos recorrer desde el índice 1: el primero ya fue considerado.')],
    6: [('**Predicción breve antes de probar:** ¿qué ocurrirá con `int a = 0 / 0;` y con `double b = 0.0 / 0.0;`?', 'En el primer caso no hay un resultado entero válido y la operación de división por cero provoca una excepción; en el segundo, `b` recibe `NaN`. La decisión pedagógica sigue siendo comprobar que hay al menos un dato antes de calcular el promedio.')],
    7: [('**Predicción:** si creas otro `Producto` con `new`, ¿tendrá automáticamente el nombre «Cuaderno»?', 'No: tendrá su propio estado inicial, hasta que le asignemos datos.'), ('**Ejercicio de predicción:** identifica por qué `new Producto(101, "Cuaderno", 120)` no coincide con el constructor que escribimos.', 'Le falta el cuarto argumento, `stock`.')],
}
# Respuestas de varios bloques: límites definidos por la consigna y el siguiente
# título exactos, no por palabras sueltas ni por heurísticas de proximidad.
RESPUESTAS_BLOQUE = {
    3: [('Antes de continuar, predice la salida.', '10.2. ¿Qué hace switch?')],
    4: [('**Antes de continuar, predice:** ¿qué números se mostrarán?, ¿qué valor tendrá `numero` al terminar?, ¿cuántas veces se comprobará la condición?', '3.2. Trazado completo')],
    6: [('Antes de ejecutar, predice la salida.', '4.7. Trazado de argumentos'), ('Antes de ejecutarlo, predice la salida.', '6.7. ¿Por qué no cambió valor?')],
}
INTERACTIVOS = {
    'u01-bidones-simulador': 'Dos recipientes vacíos, A de 5 litros y B de 3. Llena o vacía por completo y trasvasa hasta llenar el destino o vaciar el origen. Objetivo: 4 litros en A. Predice el estado después de llenar B y pasarlo a A.',
    'u01-programa-cpu-ram': 'Modelo conceptual: programa con instrucciones → procesamiento → datos temporales en RAM → salida. Por ejemplo, precio 150 y cantidad 3 producen total 450. Java necesita compilación y un entorno de ejecución.',
    'u02-estructura-java': 'En Main.java, la clase Main contiene el método main. La ejecución entra en main y sigue sus instrucciones. Las llaves delimitan cada bloque; println muestra información.',
    'u02-variables-asignacion': 'Traza: precio 150, cantidad 3, total 450; después precio cambia a 200 y total permanece en 450 hasta volver a calcularlo, cuando pasa a 600. En una copia de primitivos, cambiar b no cambia a.',
    'u03-if-else': 'Si saldo >= precio se ejecuta «Compra autorizada»; en caso contrario, «Saldo insuficiente». Con saldo y precio iguales se ejecuta la primera alternativa.',
    'u03-else-if': 'Para el ejemplo, nota >= 9 produce Excelente; si no, nota >= 6 produce Aprobado; en otro caso, Debe mejorar. Después de una condición verdadera, las posteriores no se evalúan.',
    'u03-condiciones-compuestas': 'En puntos >= 10 && vidas > 0, si la primera condición es falsa no se evalúa la segunda. En puntos >= 10 || permisoEspecial, si la primera es verdadera tampoco se evalúa la segunda. ! invierte un booleano.',
    'u03-switch': 'En el menú, 1 consulta saldo, 2 indica depósito, 3 sale y cualquier otro valor ejecuta default. En el switch tradicional, break evita continuar hacia los casos siguientes.'
}
INTERACTIVOS.update({
    'u04-while-trazado': 'Con numero = 1, while (numero <= 3) muestra 1, 2 y 3. Al llegar a 4 se comprueba una cuarta vez la condición, que es falsa: tres iteraciones y cuatro evaluaciones.',
    'u04-acumuladores-contadores': 'Con las notas 7, 5, 8, 6, 9, la suma pasa por 7, 12, 20, 26 y 35. Contar notas >= 6 produce 1, 1, 2, 3 y 4 aprobados. Ambos comienzan en cero.',
    'u04-for-esquema': 'for (int i = 1; i <= 5; i++) inicializa una vez, evalúa, ejecuta el cuerpo y actualiza; al evaluar 6 <= 5 termina sin ejecutar otra iteración.',
    'u04-do-while-esquema': 'Con numero = 5 y condicion numero <= 3, while ejecuta el cuerpo cero veces; do...while lo ejecuta una vez antes de evaluar la condición falsa.',
    'u05-arreglo-indices': 'Para notas = {7, 5, 8, 6, 9}, el tercer elemento tiene índice 2 y valor 8. length es 5; los índices -1 y 5 producirían un error de límites.',
    'u05-recorrido-arreglo': 'Con notas = {7, 5, 8, 6, 9}, for recorre índices 0 a 4. Con i = 5, i < notas.length es falsa y no se accede a notas[5].',
    'u05-busqueda-lineal': 'Buscar 8 en {7, 5, 8, 6, 9}: se comparan índices 0, 1 y 2; la primera posición es 2. Buscar 4 recorre las cinco posiciones y comunica que no está.',
    'u05-string-vs-array': 'Para numeros = {3, 5, 8} y palabra = "Java", numeros.length es 3 y palabra.length() es 4. numeros[1] es 5 y palabra.charAt(1) es a. Un elemento del arreglo puede cambiar; String es inmutable y palabra[0] = \'L\' no compila.'
})
INTERACTIVOS.update({
    'u06-flujo-metodos': 'En el programa, main muestra C y llama a segundo; segundo muestra B y llama a primero, que muestra A. Luego se retorna y main muestra D. Salida: C, B, A, D.',
    'u06-parametros-retorno': 'calcularDoble(5) recibe numero = 5 y devuelve 10; main continúa con 10 + 3 y obtiene 13. return devuelve un valor y finaliza el método; void puede mostrar sin devolver un valor utilizable.',
    'u06-alcance-referencias': 'Java pasa argumentos por valor. Cambiar un parámetro int no cambia el original; en un arreglo se copia la referencia y un cambio de elemento afecta al mismo arreglo. Reasignar el parámetro no cambia la referencia de main.',
    'u07-abstraccion-modelado': 'La finalidad determina qué datos representar. Para alquiler de bicicletas pueden importar identificador y disponibilidad; para mantenimiento, kilómetros y estado de frenos. Propón comportamientos y justifica qué dejas fuera.',
    'u07-clase-instancias': 'Producto define código, nombre, precio y stock. Dos expresiones new crean objetos independientes; c = a copia una referencia, por lo que c y a observan el mismo objeto.',
    'u07-encapsulamiento': 'Un Producto con stock 15 acepta agregarStock(5) y queda en 20; desde el estado inicial, retirarStock(20) se rechaza y conserva 15. private limita el acceso; las operaciones y el constructor necesitan validar sus reglas.'
})

HEADER = '''<a class="skip-link" href="#contenido">Saltar al contenido</a><header class="site-header"><div class="header-inner"><a class="brand" href="index.html"><img src="assets/logo-profe-macon.png" alt="Profe Macón"><span><strong>Programación I</strong><small>1.º BT Informática · DGETP / UTU</small></span></a><nav aria-label="Navegación principal"><a href="index.html">Inicio</a><a href="index.html#unidades">Unidades</a>{current}</nav></div></header>'''
FOOTER = '''<footer><div class="footer-inner"><img src="assets/logo-PM-opcional.png" alt=""><span><strong>Programación I · 2026</strong><br>Profe Macón · DGETP / UTU</span></div></footer>'''

def page(title, main, unit=None):
    return ('<!doctype html>\n<html lang="es"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{escape(title)} · Programación I</title>'
            '<link rel="icon" href="assets/logo-PM-opcional.png">'
            '<link rel="stylesheet" href="assets/style.css"></head><body id="top">'
            + HEADER.format(current=f'<span class="current-unit" aria-current="page">Unidad {unit}</span>' if unit else '') + main + FOOTER
            + ('<script defer src="assets/recursos-modelos.js"></script><script defer src="assets/recursos-interactivos.js"></script>' if unit in (1, 2, 3, 4, 5, 6, 7) else '')
            + ('<script defer src="assets/recursos-3b-modelos.js"></script><script defer src="assets/recursos-3b.js"></script>' if unit in (4, 5, 6, 7) else '')
            + ('<script defer src="assets/recursos-3c-modelos.js"></script><script defer src="assets/recursos-3c.js"></script>' if unit in (6, 7) else '') + '</body></html>\n')

def heading_text(inline):
    return ''.join(child.content for child in inline.children or []
                   if child.type in ('text', 'code_inline', 'softbreak', 'hardbreak'))

def heading_slug(text):
    plain = unicodedata.normalize('NFKD', text.casefold())
    plain = ''.join(c for c in plain if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '-', plain).strip('-')[:100].rstrip('-') or 'apartado'

def table_open(self, tokens, idx, options, env):
    return ('<div class="table-scroll" role="region" tabindex="0" '
            'aria-label="Tabla: desplazar horizontalmente si es necesario">\n<table>\n')

def table_close(self, tokens, idx, options, env):
    return '</table>\n</div>\n'

def fence(self, tokens, idx, options, env):
    token = tokens[idx]
    language = token.info.strip().split()[0] if token.info.strip() else ''
    previous = tokens[idx-2].content.strip() if idx >= 2 and tokens[idx-1].type == 'paragraph_close' and tokens[idx-2].type == 'inline' else ''
    label = 'Java' if language == 'java' else 'Texto'
    if language == 'java':
        if re.fullmatch(r'\*\*(?:Código|Ejemplo|Fragmento) (?:intencionalmente )?incorrecto:?\*\*:?|(?:Código|Ejemplo|Fragmento) (?:intencionalmente )?incorrecto:', previous, re.I):
            label = 'Java · ejemplo incorrecto'
        elif re.fullmatch(r'\*\*Programa (?:Java )?completo:?\*\*:?|Programa (?:Java )?completo:', previous, re.I):
            label = 'Programa Java completo'
        elif re.fullmatch(r'\*\*Fragmento(?: para analizar)?:?\*\*:?|Fragmento:', previous, re.I):
            label = 'Fragmento Java'
    elif language in ('text', ''):
        if re.fullmatch(r'\*\*Pseudocódigo:?\*\*:?|Pseudocódigo:', previous, re.I): label = 'Pseudocódigo'
        elif re.fullmatch(r'\*\*Salida esperada:?\*\*:?|Salida esperada:', previous, re.I): label = 'Salida esperada'
    elif language == 'bash':
        label = 'Consola'
    focus = ' role="region" tabindex="0" aria-label="' + escape(label) + ': bloque de código desplazable"' if any(len(line) > 25 for line in token.content.splitlines()) else ''
    return (f'<pre class="codigo-bloque" data-etiqueta="{escape(label)}"{focus}>'
            f'<code class="language-{escape(language)}">{escape(token.content)}</code></pre>\n')

MARKDOWN.add_render_rule('table_open', table_open)
MARKDOWN.add_render_rule('table_close', table_close)
MARKDOWN.add_render_rule('fence', fence)

def public_source(source, unit):
    # La lista es una instrucción de planificación docente, no teoría ni actividad.
    # El párrafo posterior «Próxima clase» sí se conserva.
    if unit == 5:
        source, count = re.subn(r'(?m)^# Checklist docente y continuidad\s*\n(?:\s*\n)?(?:- [^\n]*\n)+', '', source)
        if count != 1:
            raise ValueError('No se identificó exactamente el checklist docente de U5')
    if unit == 7:
        teacher_section = '## Guía breve para la docencia: secuencia de cuatro módulos'
        if source.count(teacher_section) != 1:
            raise ValueError('No se identificó exactamente la guía docente de U7')
        source = source.split(teacher_section, 1)[0]
    return source

def process_unit(unit, source, expected_ids):
    tokens = MARKDOWN.parse(public_source(source, unit))
    resources, found, heading, contents = [], [], '', []
    slugs = {}
    heading_number = 0
    for pos, token in enumerate(tokens):
        if token.type == 'heading_open':
            heading_number += 1
            inline = tokens[pos + 1]
            label = heading_text(inline)
            slug = heading_slug(label)
            slugs[slug] = slugs.get(slug, 0) + 1
            heading_id = 'seccion-' + slug + (f'-{slugs[slug]}' if slugs[slug] > 1 else '')
            token.attrSet('id', heading_id)
            # Mantener operativos enlaces creados antes de esta versión.
            alias = Token('html_inline', '', 0)
            alias.content = f'<span id="apartado-{heading_number}" class="legacy-anchor" aria-hidden="true"></span>'
            inline.children.insert(0, alias)
            if label in ANTIGUAS_ANCLAS:
                previous_alias = Token('html_inline', '', 0)
                previous_alias.content = f'<span id="{ANTIGUAS_ANCLAS[label]}" class="legacy-anchor" aria-hidden="true"></span>'
                inline.children.insert(1, previous_alias)
            if token.tag == 'h1' and heading_number > 1:
                contents.append((heading_id, label))
            heading = tokens[pos + 1].content
        if token.type == 'inline':
            for child in token.children or []:
                if child.type == 'html_inline' and not re.fullmatch(r'<span id="(?:apartado-\d+|seccion-[a-z0-9-]+)" class="legacy-anchor" aria-hidden="true"></span>', child.content):
                    child.type = 'text'
        if token.type != 'html_block':
            continue
        content = token.content.strip()
        if re.match(r'^<!--\s*PM-RECURSO\b', content):
            if not content.endswith('-->'):
                raise ValueError(f'Comentario de recurso sin cerrar en U{unit}')
            attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', content))
            resource_id = attrs.get('id', '')
            if not re.fullmatch(r'u\d{2}-[a-z0-9-]+', resource_id):
                raise ValueError(f'ID de recurso inválido: {resource_id!r}')
            found.append(resource_id)
            status = 'pendiente'
            if resource_id == 'u01-bidones-problema':
                status = 'imagen disponible'
                body = ('<figure class="recurso-imagen"><img src="assets/bidones-problema.png" '
                        'alt="Dos bidones vacíos: A de cinco litros y B de tres, sin marcas. '
                        'Se pueden llenar, vaciar o trasvasar hasta vaciar el origen o llenar el destino; '
                        'el objetivo es obtener cuatro litros en A."></figure>')
            elif resource_id in INTERACTIVOS:
                status = 'implementado; verificación visual pendiente'
                body = (f'<div data-componente-interactivo="{resource_id}"><div data-montaje></div>'
                        f'<aside data-alternativa class="recurso-alternativo"><p>{escape(INTERACTIVOS[resource_id])}</p>'
                        '<p>Predice el resultado y contrástalo con los ejemplos del capítulo.</p></aside></div>')
            else:
                body = ('<aside class="recurso-pendiente" aria-label="Recurso en preparación">'
                        '<p>Recurso interactivo o visual en preparación. '
                        'Puedes estudiar este concepto con la explicación y los ejemplos de esta sección.</p></aside>')
            token.content = f'<div id="{resource_id}" data-recurso="{resource_id}">{body}</div>\n'
            resources.append({'id': resource_id, 'unidad': unit, 'seccion': heading,
                              'ubicacion': attrs.get('ubicacion', ''), 'tipo': attrs.get('tipo', ''),
                              'componente': attrs.get('componente', ''), 'estado': status,
                              'fuente': f'contenido/unidad-{unit:02}.md', 'pagina': f'unidad-{unit:02}.html'})
        elif content.startswith('<!--'):
            token.content = ''
        else:
            # Nunca ejecutar HTML crudo proporcionado por un capítulo.
            token.content = '<pre>' + escape(token.content) + '</pre>\n'
    if found != expected_ids:
        raise ValueError(f'Marcadores de unidad {unit}: {found!r}; esperados {expected_ids!r}')
    rendered = MARKDOWN.renderer.render(tokens, MARKDOWN.options, {})
    for question, next_heading in RESPUESTAS_BLOQUE.get(unit, []):
        marker = '<p>' + MARKDOWN.renderInline(question) + '</p>\n'
        end_marker = '<h2 id="seccion-' + heading_slug(next_heading) + '">'
        if rendered.count(marker) != 1 or rendered.count(end_marker) != 1:
            raise ValueError(f'Límites de predicción no identificados de manera única en U{unit}: {question}')
        start = rendered.index(marker) + len(marker)
        end = rendered.index(end_marker)
        if end <= start:
            raise ValueError(f'Orden de predicción inválido en U{unit}')
        answer = rendered[start:end]
        rendered = (rendered[:start] + '<details class="respuesta"><summary>Ver explicación</summary>'
                    + answer + '</details><div class="respuesta-impresa" aria-hidden="true">'
                    + answer + '</div>\n' + rendered[end:])
    for question, answer in RESPUESTAS.get(unit, []):
        inline = MARKDOWN.renderInline(question + ' ' + answer)
        separate = MARKDOWN.renderInline(question) + '</p>\n<p>' + MARKDOWN.renderInline(answer)
        original_inline, original_separate = '<p>' + inline + '</p>', '<p>' + separate + '</p>'
        original = original_inline if rendered.count(original_inline) == 1 else original_separate
        if rendered.count(original) != 1:
            raise ValueError(f'Predicción no identificada de manera única en U{unit}: {question}')
        solution = '<p>' + MARKDOWN.renderInline(answer) + '</p>'
        replacement = ('<p>' + MARKDOWN.renderInline(question) + '</p>'
                       '<details class="respuesta"><summary>Ver explicación</summary>' + solution + '</details>'
                       '<div class="respuesta-impresa" aria-hidden="true">' + solution + '</div>')
        rendered = rendered.replace(original, replacement, 1)
    if unit == 5:
        question, answer = PREDICCION_U05.split(': ', 1)
        original = '<p>' + MARKDOWN.renderInline(PREDICCION_U05) + '</p>'
        replacement = ('<p>' + MARKDOWN.renderInline(question + ':') + '</p>'
                       '<details class="respuesta"><summary>Ver explicación</summary><p>'
                       + MARKDOWN.renderInline(answer) + '</p></details>'
                       '<div class="respuesta-impresa" aria-hidden="true"><p>'
                       + MARKDOWN.renderInline(answer) + '</p></div>')
        if rendered.count(original) != 1:
            raise ValueError('La predicción U5 no coincide exactamente con la fuente revisada')
        rendered = rendered.replace(original, replacement, 1)
    return rendered, resources, contents

def build():
    cards = []
    for n, (name, desc) in enumerate(UNIDADES, 1):
        cards.append(f'<a class="unit-card available" href="unidad-{n:02}.html"><span class="unit-number">UNIDAD {n:02}</span><h3>{escape(name)}</h3><p>{escape(desc)}</p><span class="card-link">Explorar unidad →</span></a>')
    home = ('<main id="contenido"><section class="hero"><div class="container"><p class="eyebrow">1.º Bachillerato Tecnológico en Informática · 2026</p><h1>Programación I</h1><p class="lead">Aprender a pensar, construir y comprender programas, paso a paso.</p><a class="button primary" href="#unidades">Explorar las unidades →</a></div></section><section class="container unit-section" id="unidades"><p class="eyebrow">Recorrido del curso</p><h2>Unidades de aprendizaje</h2><p class="intro">Un recorrido desde los primeros algoritmos hasta las clases y los objetos en Java.</p><div class="units">' + ''.join(cards) + '</div></section></main>')
    output = {'index.html': page('Inicio', home)}
    all_resources = []
    for entry in VERIFICACION['unidades']:
        n = entry['unidad']
        path = ROOT / f'contenido/unidad-{n:02}.md'
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if digest != entry['sha256']:
            raise ValueError(f'{path}: hash no coincide con la fuente revisada; revisar cambios editoriales antes de generar')
        rendered, resources, contents = process_unit(n, raw.decode('utf-8'), entry['marcadores'])
        all_resources.extend(resources)
        links = ''.join(f'<li><a href="#{section_id}">{escape(label)}</a></li>' for section_id, label in contents)
        toc = f'<details class="contents"><summary>Índice de la unidad</summary><nav aria-label="Apartados de la unidad"><ol>{links}</ol></nav></details>'
        previous = f'<a rel="prev" href="unidad-{n-1:02}.html">← Unidad {n-1}: {escape(UNIDADES[n-2][0])}</a>' if n > 1 else '<span></span>'
        following = f'<a rel="next" href="unidad-{n+1:02}.html">Unidad {n+1}: {escape(UNIDADES[n][0])} →</a>' if n < len(UNIDADES) else '<span></span>'
        lesson = (f'<main class="lesson" id="contenido"><a class="back" href="index.html#unidades">← Volver a las unidades</a><p class="eyebrow">Programación I · Unidad {n:02}</p>{toc}<article class="prose">{rendered}</article><nav class="lesson-bottom" aria-label="Navegación entre unidades">{previous}{following}</nav><p class="return-top"><a href="#top">Volver arriba ↑</a></p></main>')
        output[f'unidad-{n:02}.html'] = page(f'Unidad {n}', lesson, n)
    ids = [resource['id'] for resource in all_resources]
    if len(ids) != 23 or len(set(ids)) != 23:
        raise ValueError('Se esperaban 23 marcadores únicos')
    output['registro-recursos.json'] = json.dumps(all_resources, ensure_ascii=False, indent=2) + '\n'
    for filename, contents in output.items():
        (ROOT / filename).write_text(contents, encoding='utf-8', newline='\n')
    print('Generadas siete unidades y registrados 23 recursos.')

if __name__ == '__main__':
    build()
