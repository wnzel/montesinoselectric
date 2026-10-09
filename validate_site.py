"""Check generated routes, local assets, page semantics, and structured data."""
import json,re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote

ROOT=Path(__file__).parent;DIST=ROOT/'dist';errors=[];checked=0
class Document(HTMLParser):
    def __init__(self):
        super().__init__();self.tags=[];self.ids=[];self.h1=0;self.in_ld=False;self.ld=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs);self.tags.append((tag,a))
        if 'id' in a:self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='script' and a.get('type')=='application/ld+json':self.in_ld=True
    def handle_endtag(self,tag):
        if tag=='script':self.in_ld=False
    def handle_data(self,data):
        if self.in_ld:self.ld.append(data)
for page in DIST.rglob('*.html'):
    doc=Document();doc.feed(page.read_text(encoding='utf-8'));checked+=1
    redirect=any(t=='meta' and a.get('http-equiv')=='refresh' for t,a in doc.tags)
    if not redirect:
        if doc.h1!=1:errors.append(f'{page}: expected one h1, got {doc.h1}')
        if len(doc.ids)!=len(set(doc.ids)):errors.append(f'{page}: duplicate element ids')
        for block in doc.ld:
            try:json.loads(block)
            except json.JSONDecodeError as ex:errors.append(f'{page}: JSON-LD {ex}')
    for tag,attrs in doc.tags:
        if tag=='img' and 'src' in attrs and 'alt' not in attrs:errors.append(f'{page}: image missing alt')
        if tag=='label' and attrs.get('for') not in doc.ids:errors.append(f'{page}: label has no field')
        for key in ('src','href'):
            value=attrs.get(key,'');parts=urlsplit(value)
            if parts.scheme or parts.netloc or not value or value.startswith('#'):continue
            target=DIST/unquote(parts.path).lstrip('/') if value.startswith('/') else page.parent/unquote(parts.path)
            if not target.exists():errors.append(f'{page.relative_to(DIST)}: missing {value}')
            if parts.fragment and target.is_file() and target==page and parts.fragment not in doc.ids:errors.append(f'{page}: missing anchor {parts.fragment}')
for css in DIST.glob('*.css'):
    for url in re.findall(r'url\([\'\"]?([^\)\'\"]+)',css.read_text(encoding='utf-8')):
        if url.startswith('/') and not (DIST/url.lstrip('/')).exists():errors.append(f'{css}: missing {url}')
config=json.loads((ROOT/'site-content.json').read_text(encoding='utf-8'))
if config['business']['email'] or config['business']['quoteEndpoint']:errors.append('Email delivery must remain unconfigured')
if len(config['projects'])!=20:errors.append('Expected 20 original project entries')
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {checked} HTML files; internal routes, assets, headings, labels, image alt text and JSON-LD checked. Email stays empty.')
