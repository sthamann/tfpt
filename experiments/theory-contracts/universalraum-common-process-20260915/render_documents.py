"""Render every delivered PDF page and produce compact review contact sheets."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess
from PIL import Image, ImageDraw

HERE=Path(__file__).resolve().parent
POPPLER=Path('/Users/stefanhamann/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm')

def main():
    docs=json.loads((HERE/'documents_manifest.json').read_text())
    qa=json.loads((HERE/'pdf_qa.json').read_text())
    root=HERE/'tmp/rendered';root.mkdir(parents=True,exist_ok=True)
    result={}
    for name,rec in docs.items():
        pdf=HERE/rec['pdf'];folder=root/name;folder.mkdir(exist_ok=True)
        if sha256(pdf.read_bytes()).hexdigest()!=rec['pdf_sha256']:
            raise RuntimeError('Changed PDF '+name)
        count=qa['documents'][name]['pages']
        prefix=folder/'page'
        subprocess.run([str(POPPLER),'-r','80','-png',str(pdf),str(prefix)],check=True,timeout=180,capture_output=True)
        pages=sorted(folder.glob('page-*.png'))
        # A folder may contain an earlier render; fail instead of hiding it.
        if len(pages)!=count:raise RuntimeError('Unexpected rendered page count '+name)
        contacts=[]
        for start in range(0,count,20):
            canvas=Image.new('RGB',(1200,1440),'#cbd5e1');draw=ImageDraw.Draw(canvas)
            for k,path in enumerate(pages[start:start+20]):
                with Image.open(path) as source:
                    source.thumbnail((228,325))
                    x=(k%5)*240+(240-source.width)//2;y=(k//5)*360+24
                    canvas.paste(source,(x,y))
                draw.text(((k%5)*240+8,(k//5)*360+6),f'{name} / {start+k+1}',fill='black')
            target=folder/f'contact-{start//20+1:02}.png';canvas.save(target)
            contacts.append(str(target))
        landmarks=qa['documents'][name]['landmark_pages']
        result[name]={'pdf_sha256':rec['pdf_sha256'],'pages':count,'contact_sheets':contacts,
                      'rendered_pages':[str(p) for p in pages],'landmarks':landmarks}
    target=HERE/'render_manifest.json';target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:{'pages':v['pages'],'contact_sheets':v['contact_sheets'],'landmarks':v['landmarks']}
                      for k,v in result.items()},indent=2))

if __name__=='__main__':main()
