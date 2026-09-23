"""Extract every PDF page and validate content, source retention and typography."""
from pathlib import Path
from hashlib import sha256
import json
import re
import pdfplumber

HERE=Path(__file__).resolve().parent

def inspect(path):
 texts=[];bad=[]
 with pdfplumber.open(path) as doc:
  for i,p in enumerate(doc.pages):
   text=p.extract_text() or '';texts.append(text)
   if not text.strip():bad.append([i+1,'empty'])
   if '\ufffd' in text:bad.append([i+1,'replacement character'])
   for c in p.chars:
    if c['x0']<15 or c['x1']>p.width-15 or c['top']<10 or c['bottom']>p.height-10:
     bad.append([i+1,'page edge']);break
 if bad:raise RuntimeError(str(path)+str(bad))
 return texts

def main():
 manifest=json.loads((HERE/'documents_manifest.json').read_text());result={}
 for name,r in manifest.items():
  pdf=HERE/r['pdf'];md=(HERE/r['markdown']).read_text()
  if sha256(pdf.read_bytes()).hexdigest()!=r['pdf_sha256']:raise RuntimeError('Changed PDF')
  texts=inspect(pdf);text='\n'.join(texts)
  if name=='Konsolidierung':
   for source in ['sources/baseline_v168.md','COMPOSITION.md','agents/source/REPORT.md',
                  'agents/protocol/REPORT.md','agents/field/REPORT.md','RESULTS.md']:
    if (HERE/source).read_text() not in md:raise RuntimeError('Lost complete source '+source)
   count=str(json.loads((HERE/'replay_manifest.json').read_text())['own_exact_checks_per_variant'])
   for token in [count,'960','349056','8068','0.000310417','Takagi','T1','T8']:
    if token not in text:raise RuntimeError('Missing rendered token '+token)
  logs=sorted((HERE/'tmp/pdfs').glob(name+'_xelatex_*.log'),key=lambda p:p.stat().st_mtime)
  log=logs[-1].read_text(errors='replace')
  for item in ['Missing character:','Label(s) may have changed','Column widths have changed']:
   if item in log:raise RuntimeError('Unresolved typography '+name+' '+item)
  widths=[float(v) for v in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',log)]
  if max(widths,default=0)>3:raise RuntimeError('Overfull text '+name+str(widths))
  result[name]={'pages':len(texts),'all_pages_text_extracted':True,'characters':len(text),
    'no_empty_pages':True,'no_page_edge_overflow':True,'no_missing_glyphs':True,
    'maximum_minor_overfull_pt':max(widths,default=0),'pdf_sha256':r['pdf_sha256'],
    'landmark_pages':{word:[i+1 for i,t in enumerate(texts) if word in t][:4]
                      for word in ['960','349056','Clockbilder','Takagi','0.000310417','Nullimpuls','Kinetiktest','Historischer Teil']}}
 output={'status':'PASS','documents':result}
 (HERE/'pdf_qa.json').write_text(json.dumps(output,indent=2)+'\n')
 print(json.dumps(output,indent=2))

if __name__=='__main__':main()

