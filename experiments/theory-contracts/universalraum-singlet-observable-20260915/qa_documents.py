"""Read every PDF page and check delivery coverage/geometry before visual QA."""
from pathlib import Path
from hashlib import sha256
import json
import re
import pdfplumber

HERE=Path(__file__).resolve().parent
def main():
    manifest=json.loads((HERE/'documents_manifest.json').read_text())
    results={}
    for name,record in manifest.items():
        md=(HERE/record['markdown']).read_text()
        if sha256((HERE/record['pdf']).read_bytes()).hexdigest()!=record['pdf_sha256']:
            raise RuntimeError('PDF changed after build')
        pages=[];bad=[]
        with pdfplumber.open(HERE/record['pdf']) as doc:
            for i,p in enumerate(doc.pages):
                text=p.extract_text() or ''
                pages.append(text)
                if not text.strip():bad.append([i+1,'empty page'])
                for c in p.chars:
                    if c['x0']<15 or c['x1']>p.width-15 or c['top']<10 or c['bottom']>p.height-10:
                        bad.append([i+1,'near/outside physical page edge']);break
        if bad:raise RuntimeError(str((name,bad)))
        text='\n'.join(pages)
        if name=='Konsolidierung':
            for source in ['historical_v1.6.6.md','attachment_round.txt','attachment_correction.txt']:
                if (HERE/'sources'/source).read_text() not in md:raise RuntimeError('Lost full source '+source)
            for source in ['multiplicity_z4.txt','fundamental_reduction.txt','runtime_synthesis.txt','operations_ground_field_v163.txt']:
                if (HERE/'late_sources'/source).read_text() not in md:raise RuntimeError('Lost full late source '+source)
            for token in ['78877653','105168998','4035','T1','T8','Nutzerquelle A','Nutzerquelle B']:
                if token not in text:raise RuntimeError('Missing rendered text '+token)
            for token in ['Nutzerquelle C','Nutzerquelle D','Nutzerquelle E','Bogoliubov','1956','Holografie']:
                if token not in text:raise RuntimeError('Missing late rendered text '+token)
        if name=='Update':
            for token in ['0.00773911','4035','822','Kodierer']:
                if token not in text:raise RuntimeError('Missing update token '+token)
        logs=sorted((HERE/'tmp/pdfs').glob(name+'_xelatex_*.log'))
        # Last iteration of the current build is recorded by successful stable
        # compilation. All glyph errors in any latest log are forbidden.
        relevant=max(logs,key=lambda p:p.stat().st_mtime)
        log=relevant.read_text(errors='replace')
        if 'Missing character:' in log or 'Label(s) may have changed' in log or 'Column widths have changed' in log:
            raise RuntimeError('Unresolved PDF rendering/cross-reference warning '+name)
        widths=[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',log)]
        if widths and max(widths)>3:raise RuntimeError('Substantial overfull text '+name)
        results[name]={'pages':len(pages),'text_characters':len(text),
                       'all_pages_read':True,'no_empty_pages':True,'no_page_edge_overflow':True,
                       'no_missing_glyphs':True,'stable_cross_references':True,
                       'maximum_minor_overfull_pt':max(widths,default=0),
                       'pdf_sha256':record['pdf_sha256']}
    (HERE/'pdf_qa.json').write_text(json.dumps({'status':'PASS','documents':results},indent=2)+'\n')
    print(json.dumps(results,indent=2))

if __name__=='__main__':main()
