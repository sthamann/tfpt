"""Build complete v1.6 and short update; verify preservation and render all pages."""
from pathlib import Path
from collections import Counter
import subprocess,hashlib,json,re,shutil
from pypdf import PdfReader
from PIL import Image,ImageDraw

HERE=Path(__file__).resolve().parent
SRC=HERE/'main-v1.6'
BASE=HERE.parent/'universalraum-native-closure-20260914/main-v1.5'
QA=HERE/'qa'; QA.mkdir(exist_ok=True)
LATEX='/Library/TeX/texbin/lualatex'
POP='/Users/stefanhamann/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
heading=re.compile(r'\\(?:chapter|section|subsection)\*?\{([^\n]*)\}')
coverage=[]
for p in sorted((BASE/'chapters').glob('*.tex')):
    q=SRC/'chapters'/p.name
    old,new=p.read_text(),q.read_text()
    missing=list((Counter(heading.findall(old))-Counter(heading.findall(new))).elements())
    recovered=re.sub(r'\n\\input\{revisions/[^}]+\}\n','',new)
    expected=old
    for prefix in ['Aktueller Stand v','Aktueller Forschungsauftrag v']:
        expected=expected.replace(prefix,prefix.replace('Aktueller','Historischer'))
    if recovered!=expected or missing:
        raise RuntimeError('Baseline text not fully preserved: '+p.name)
    coverage.append({'file':p.name,'baseline_sha256':sha(p),'current_sha256':sha(q),
                     'all_baseline_text_preserved':True,'heading_count':len(heading.findall(old)),
                     'missing_headings':missing})
if len(coverage)!=25: raise RuntimeError('Incomplete baseline')
figures=[]
for p in sorted((BASE/'figures').rglob('*')):
    if p.is_file():
        q=SRC/'figures'/p.relative_to(BASE/'figures')
        if p.read_bytes()!=q.read_bytes(): raise RuntimeError('Figure changed: '+str(p))
        figures.append({'file':str(p.relative_to(BASE/'figures')),'sha256':sha(p)})
counts={}
for name in ['main','update']:
    for run in range(3):
        process=subprocess.run([LATEX,'-no-shell-escape','-interaction=nonstopmode',
                                '-halt-on-error',name+'.tex'],cwd=SRC,capture_output=True)
        (QA/f'{name}-build-{run}.log').write_bytes(process.stdout+process.stderr)
        if process.returncode: raise RuntimeError(name+' build failed; inspect qa log')
    log=(SRC/(name+'.log')).read_text()
    for marker in ['There were undefined references','Overfull \\hbox','Overfull \\vbox','Missing character:']:
        if marker in log: raise RuntimeError(name+': '+marker)
    reader=PdfReader(SRC/(name+'.pdf'))
    texts=[p.extract_text() or '' for p in reader.pages]
    if any('??' in t for t in texts) or any(len(t.strip())<15 for t in texts):
        raise RuntimeError(name+': blank or unresolved page')
    counts[name]=len(texts)
    (QA/(name+'_text.txt')).write_text('\n\n'.join(texts))
    render=QA/name; render.mkdir(exist_ok=True)
    # Only this builder's generated preview files, never document sources.
    for old in render.glob('page-*.png'): old.unlink()
    for old in QA.glob(name+'-contact-*.png'): old.unlink()
    subprocess.run([POP,'-r','65','-png',str(SRC/(name+'.pdf')),str(render/'page')],check=True)
    pages=sorted(render.glob('page-*.png'))
    if len(pages)!=len(texts): raise RuntimeError(name+': render page count mismatch')
    for offset in range(0,len(pages),12):
        sheet=Image.new('RGB',(1200,1760),'#dddddd'); draw=ImageDraw.Draw(sheet)
        for j,p in enumerate(pages[offset:offset+12]):
            im=Image.open(p).convert('RGB'); im.thumbnail((386,410))
            x=j%3*400+(400-im.width)//2; y=j//3*440+22
            sheet.paste(im,(x,y)); draw.text((j%3*400+12,j//3*440+4),p.stem,fill='black')
        sheet.save(QA/f'{name}-contact-{offset//12+1:02}.png')
    print(name,len(texts),'pages: compiled, text checked, all pages rendered',flush=True)
source_hashes={str(p.relative_to(SRC)):sha(p) for p in sorted(SRC.rglob('*.tex'))}
manifest={'version':'1.6','date':'2026-09-15',
 'baseline':'complete main v1.5','baseline_pdf_pages':len(PdfReader(BASE/'main.pdf').pages),
 'baseline_chapter_coverage':coverage,'baseline_figures':figures,'page_counts':counts,
 'new_chapter_files':6,'contextual_insertions':13,'source_tex_hashes':source_hashes,
 'input_manifest_sha256':sha(HERE/'sources.json'),
 'replay_manifest':json.loads((HERE/'replay_manifest.json').read_text()),
 'pdfs':{n:sha(SRC/(n+'.pdf')) for n in ['main','update']},
 'T1_T8_closed':[],'visual_review':'pending',
 'scope':'document QA and scoped exact research; no global physics closure'}
(HERE/'release_manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(counts))
