"""Contraste relativo WCAG para combinaciones concretas del CSS; no analiza toda la página."""
import json
from pathlib import Path

def luminance(value):
    channels = [int(value[i:i+2], 16)/255 for i in (1, 3, 5)]
    linear = [x/12.92 if x <= .04045 else ((x+.055)/1.055)**2.4 for x in channels]
    return sum(a*b for a, b in zip(linear, (.2126, .7152, .0722)))

samples = [
    ('texto principal', '#202426', '#ffffff', 4.5),
    ('texto secundario', '#505b5c', '#ffffff', 4.5),
    ('enlaces y botones', '#006f69', '#ffffff', 4.5),
    ('enlaces sobre recurso', '#006f69', '#f1f7f6', 4.5),
    ('texto de código', '#f4f8f7', '#182123', 4.5),
    ('foco sobre blanco', '#006f69', '#ffffff', 3),
    ('borde de campo', '#758987', '#ffffff', 3),
]
report=[]
for name, foreground, background, minimum in samples:
    x,y=sorted((luminance(foreground),luminance(background)), reverse=True)
    contrast=(x+.05)/(y+.05)
    report.append(dict(elemento=name, primer_plano=foreground, fondo=background,
                       relacion=round(contrast,2), minimo=minimum, cumple=contrast>=minimum))
out=Path(__file__).resolve().parents[1]/'evidencias-cierre'/'contraste.json'
out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf8')
print(json.dumps(report, ensure_ascii=False, indent=2))
