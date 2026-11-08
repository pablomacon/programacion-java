"""Inspección opcional de PDF de auditoría con dependencias temporales."""
from pathlib import Path
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'auditoria-pdf-deps'))
from pypdf import PdfReader
import pypdfium2 as pdfium

output=ROOT/'evidencias-cierre'
report=[]
for n in (1,5,7):
    file=output/f'unidad-{n}.pdf'
    reader=PdfReader(file)
    texts=[re.sub(r'\s+', ' ',p.extract_text() or '').strip() for p in reader.pages]
    pages=[0,len(texts)//2,len(texts)-1]
    if n==5:
        pages.extend(i for i,t in enumerate(texts) if 'predice la salida' in t.lower() and 'Cada asignación' in t)
    pdf=pdfium.PdfDocument(str(file))
    for page_number in sorted(set(pages)):
        bitmap=pdf[page_number].render(scale=1.25)
        bitmap.to_pil().save(output/f'pdf-u{n}-p{page_number+1}.png')
    outside=[]
    for page_number in range(len(pdf)):
        page=pdf[page_number];textpage=page.get_textpage();width,height=page.get_size()
        for char in range(textpage.count_chars()):
            left,bottom,right,top=textpage.get_charbox(char)
            if right>width+1 or left< -1 or top>height+1 or bottom< -1:
                outside.append(page_number+1);break
    details={'unidad':n,'paginas':len(texts),'a4':all(abs(float(p.mediabox.width)-595.28)<3 and abs(float(p.mediabox.height)-841.89)<3 for p in reader.pages),
             'paginas_con_poco_texto':[i+1 for i,t in enumerate(texts) if len(t.strip())<80],
             'fallback_impreso':sum(t.count('Predice el resultado y contrástalo') for t in texts),
             'paginas_con_glifos_fuera_de_pagina':outside,
             'nota_interna_visible':any(any(s in t for s in ('PM-PROTOCOLO-DIDACTICO','PM-RECURSO','Checklist docente de cierre','Guía breve para la docencia')) for t in texts),
             'u5_respuesta_impresa':any('Cada asignación reemplaza' in t for t in texts) if n==5 else None,
             'paginas_renderizadas':[x+1 for x in sorted(set(pages))]}
    report.append(details)
(output/'pdf-resultado.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))
