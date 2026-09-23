"""PDF text/glyph checks and small contact sheets; visual review remains required."""
from pathlib import Path
import json
import os
import re
from PIL import Image, ImageOps, ImageDraw
from pypdf import PdfReader
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parents[3]
DATE='2026-09-14'
if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',DATE):
    raise ValueError('invalid paper date')
TMP=ROOT/f'tmp/pdfs/tfpt_compiler_universalraum_20260914_v1_2'
PDF=ROOT/f'output/pdf/tfpt_compiler_universalraum_2026-09-14_v1.2.pdf'
SOURCE=ROOT/'docs/TFPT_COMPILER_UNIVERSALRAUM_PAPER_2026-09-14_v1.2.md'


def main():
    reader=PdfReader(PDF)
    fonts=json.loads((TMP/'fonts.json').read_text())
    font=TTFont('Audit',fonts['body'])
    chars=set(SOURCE.read_text())
    missing=[c for c in chars if not c.isspace() and ord(c) not in font.face.charToGlyph]
    if missing:
        raise ValueError('missing body-font glyphs: '+repr(missing))
    pages=[]
    for i,p in enumerate(reader.pages,1):
        text=p.extract_text() or ''
        if '\ufffd' in text:
            raise ValueError('replacement character in PDF')
        pages.append({'page':i,'text_characters':len(text)})
    for start in range(0,len(pages),6):
        canvas=Image.new('RGB',(1000,1440),'#d5dce0')
        draw=ImageDraw.Draw(canvas)
        for offset,item in enumerate(pages[start:start+6]):
            n=item['page']
            path=TMP/f'page-{n:02}.png'
            with Image.open(path) as im:
                im=ImageOps.contain(im.convert('RGB'),(480,440))
                col,row=offset%2,offset//2
                x=col*500+(500-im.width)//2
                y=row*480+25
                canvas.paste(im,(x,y))
                draw.text((col*500+15,row*480+6),f'Page {n}',fill='black')
        canvas.save(TMP/f'contact-{start//6+1}.jpg',quality=90)
    print(json.dumps({'pages':pages,'missing_glyphs':missing,'contact_sheets':(len(pages)+5)//6}))


if __name__=='__main__':
    main()
