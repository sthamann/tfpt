"""Export only a visually accepted release; never overwrite a different version."""
from pathlib import Path
import json,hashlib,shutil,zipfile
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
DOCS=Path('/Users/stefanhamann/Documents')
OUT=ROOT/'output/pdf'; OUT.mkdir(parents=True,exist_ok=True)
manifest=json.loads((HERE/'release_manifest.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
if manifest['visual_review']!='accepted':
    raise RuntimeError('Visual review is not accepted')
def preserve_copy(src,dst):
    if dst.exists() and dst.read_bytes()!=src.read_bytes():
        raise RuntimeError('Refusing overwrite of different existing release: '+str(dst))
    shutil.copy2(src,dst)
exports=[]
for stem,label in [('main','Hauptdokument'),('update','Update')]:
    src=HERE/'main-v1.6'/(stem+'.pdf')
    if sha(src)!=manifest['pdfs'][stem]: raise RuntimeError('PDF changed after QA')
    name=f'TFPT_Universalraum_{label}_2026-09-15_v1.6.pdf'
    preserve_copy(src,OUT/name); preserve_copy(src,DOCS/name)
    exports.append({'path':str(DOCS/name),'sha256':sha(src),'pages':manifest['page_counts'][stem]})
for src,name in [
    (HERE/'RESULTS.md','TFPT_Universalraum_Ergebnisse_2026-09-15_v1.6.md'),
    (HERE/'EINFACH_ERKLAERT.md','TFPT_Universalraum_Einfach_erklaert_2026-09-15_v1.6.md'),
]:
    preserve_copy(src,DOCS/name)
    exports.append({'path':str(DOCS/name),'sha256':sha(src)})
# Archive the exact replay programs and the pinned dependencies in addition to
# the authored sources; the README explicitly retains local-context requirements.
archived=HERE/'replayed_sources'; archived.mkdir(exist_ok=True)
replay=json.loads((HERE/'replay_manifest.json').read_text())
for label,row in replay.items():
    src=Path(row['script'])
    if sha(src)!=row['sha256']: raise RuntimeError('Replay source changed: '+str(src))
    shutil.copy2(src,archived/(label+'.py'))
for rel in [
    'experiments/theory-contracts/compiler-clifford-bridge/checker.py',
    'experiments/theory-contracts/compiler-involution-types/checker.py',
    'verification/v774_arf_spinor_compiler.py',
]:
    src=ROOT/rel; shutil.copy2(src,archived/(src.parent.name+'_'+src.name))
archive=HERE/'TFPT_Universalraum_Pruef_und_Quellenpaket_2026-09-15_v1.6.zip'
allowed={'.py','.json','.md','.txt','.tex','.npz','.pdf','.png','.jpg','.jpeg','.svg'}
files=[]
for p in sorted(HERE.rglob('*')):
    if not p.is_file() or p.suffix not in allowed: continue
    rel=p.relative_to(HERE)
    if 'qa' in rel.parts or '__pycache__' in rel.parts: continue
    if p.name in ['main.pdf','update.pdf']: continue
    files.append(p)
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for p in files: z.write(p,p.relative_to(HERE))
with zipfile.ZipFile(archive) as z:
    error=z.testzip()
    if error: raise RuntimeError('Archive integrity failed '+error)
preserve_copy(archive,DOCS/archive.name)
exports.append({'path':str(DOCS/archive.name),'sha256':sha(archive),'archived_files':len(files)})
(HERE/'delivery_manifest.json').write_text(json.dumps(exports,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(exports,indent=2,ensure_ascii=False))
