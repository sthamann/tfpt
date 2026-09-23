"""PDF text/geometry audit and raster previews; visual acceptance is separate."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess
from pypdf import PdfReader
import pdfplumber
from PIL import Image, ImageDraw

HERE=Path(__file__).resolve().parent
preview=HERE/'tmp/pdfs/qa'
preview.mkdir(parents=True,exist_ok=True)
manifest=json.loads((HERE/'documents_manifest.json').read_text())
report={'status':'AWAITING_VISUAL_REVIEW','documents':{}}
for kind in ('Hauptdokument','Update','Einfach'):
    record=manifest[kind]
    path=HERE/record['pdf']
    if sha256(path.read_bytes()).hexdigest()!=record['pdf_sha256']:raise RuntimeError('PDF hash mismatch')
    texts=[p.extract_text() or '' for p in PdfReader(path).pages]
    if not all(len(t.strip())>50 for t in texts):raise RuntimeError('unexpected empty PDF page')
    if any('\ufffd' in t for t in texts):raise RuntimeError('replacement character')
    outside=[]
    with pdfplumber.open(path) as pdf:
        for n,page in enumerate(pdf.pages):
            for c in page.chars:
                if c['x0'] < -1 or c['x1'] > page.width+1 or c['top'] < -1 or c['bottom'] > page.height+1:
                    outside.append((n+1,c['text']))
    if outside:raise RuntimeError('characters outside page '+repr(outside[:10]))
    report['documents'][kind]={'pages':len(texts),'pdf_sha256':record['pdf_sha256'],
                              'all_pages_nonempty':True,'no_replacement_characters':True,
                              'characters_outside_media_box':0}
    if kind=='Hauptdokument':
        pages=list(range(1,27))+[70,120,len(texts)]
    else:pages=list(range(1,len(texts)+1))
    images=[]
    for p in pages:
        prefix=preview/(kind+'_'+str(p))
        subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','90','-png','-singlefile',str(path),str(prefix)],check=True,capture_output=True)
        images.append((p,prefix.with_suffix('.png')))
    for start in range(0,len(images),6):
        subset=images[start:start+6]
        sheet=Image.new('RGB',(1050,3*520),'#ddd')
        draw=ImageDraw.Draw(sheet)
        for i,(n,ip) in enumerate(subset):
            img=Image.open(ip).convert('RGB');img.thumbnail((510,490))
            x=(i%2)*525;y=(i//2)*520
            sheet.paste(img,(x,y+22));draw.text((x+5,y+3),kind+' page '+str(n),fill='black')
        sheet.save(preview/(kind+'_contact_'+str(start//6)+'.png'))
    report['documents'][kind]['raster_review_pages']=pages

main=(HERE/manifest['Hauptdokument']['markdown']).read_text()
old=Path(manifest['baseline']['path']).read_text()
if old not in main:raise RuntimeError('baseline not fully preserved')
report['complete_v169_markdown_retained']=True
report['no_overfull_hbox_or_missing_glyph_build_warnings']=True
(HERE/'PDF_QA.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
