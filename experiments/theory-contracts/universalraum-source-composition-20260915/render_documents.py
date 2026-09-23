"""Render every final page and contact sheets for human visual inspection."""
from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageDraw
import json
import subprocess

HERE=Path(__file__).resolve().parent
def main():
    docs=json.loads((HERE/'documents_manifest.json').read_text());out={}
    for kind,r in docs.items():
        folder=HERE/'tmp/pdfs/render'/kind;folder.mkdir(parents=True,exist_ok=True)
        subprocess.run(['pdftoppm','-r','65','-png',str(HERE/r['pdf']),str(folder/'page')],check=True)
        pages=sorted(folder.glob('page-*.png'))
        if not pages:raise RuntimeError('No rendered pages')
        sheets=[]
        for start in range(0,len(pages),12):
            batch=pages[start:start+12]
            sheet=Image.new('RGB',(1200,4*575),'#dce1e6');draw=ImageDraw.Draw(sheet)
            for j,p in enumerate(batch):
                im=Image.open(p).convert('RGB');im.thumbnail((380,540))
                x=(j%3)*400+(400-im.width)//2;y=(j//3)*575+25
                sheet.paste(im,(x,y));draw.text(((j%3)*400+10,(j//3)*575+5),f'{kind} / {start+j+1}',fill='black')
            target=folder/f'contact-{start//12+1:02d}.png';sheet.save(target);sheets.append(str(target))
        out[kind]={'pdf_sha256':r['pdf_sha256'],'rendered_pages':len(pages),'contact_sheets':sheets}
    (HERE/'render_manifest.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
