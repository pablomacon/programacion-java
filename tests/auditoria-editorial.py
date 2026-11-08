"""Inventario de numeración, títulos y notas para revisión editorial."""
from pathlib import Path
from collections import Counter,defaultdict
import re,json
ROOT=Path(__file__).resolve().parents[1]
result=[]
for p in sorted((ROOT/'contenido').glob('unidad-*.md')):
    text=p.read_text(encoding='utf8')
    headings=re.findall(r'^(#{1,6})\s+(.+)$',text,re.M)
    sections=defaultdict(list)
    for _,name in headings:
        m=re.match(r'(\d+)\.(\d+)\.',name)
        if m:sections[int(m[1])].append(int(m[2]))
    duplicates=[f'{group}.{num}' for group,nums in sections.items() for num,count in Counter(nums).items() if count>1]
    order=[{'grupo':group,'secuencia':nums} for group,nums in sections.items() if any(b<=a for a,b in zip(nums,nums[1:]))]
    titles=[title for title,count in Counter(name for _,name in headings).items() if count>1]
    result.append({'archivo':p.name,'titulos':len(headings),'numeros_duplicados':duplicates,'numeracion_fuera_de_orden':order,'titulos_duplicados':titles})
print(json.dumps(result,ensure_ascii=False,indent=2))
