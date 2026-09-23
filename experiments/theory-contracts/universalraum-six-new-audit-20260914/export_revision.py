"""Versioned, non-overwriting Documents export and verified research archive."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import zipfile

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
DOCS=Path('/Users/stefanhamann/Documents')
PREFIX='TFPT_Universalraum_'
SUFFIX='_2026-09-14_v1.6'
outputs={
    HERE/'RESULTS.md':DOCS/(PREFIX+'Kernprobleme'+SUFFIX+'.md'),
    HERE/'KURZUPDATE.md':DOCS/(PREFIX+'Kurzupdate'+SUFFIX+'.md'),
    HERE/'SOURCE_AUDIT.md':DOCS/(PREFIX+'Quellenpruefung'+SUFFIX+'.md'),
}
archive=DOCS/(PREFIX+'Pruefpaket'+SUFFIX+'.zip')
if any(p.exists() for p in [*outputs.values(),archive]):
    raise RuntimeError('Version already exists; refuse overwriting an earlier export.')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def doc_links(text,base):
    def substitute(match):
        label,target=match.groups()
        if target.startswith(('https://','http://','/','#','<')):
            return match.group(0)
        return '['+label+']('+str((base/target).resolve())+')'
    return re.sub(r'\[([^\]\n]+)\]\(([^)\n]+)\)',substitute,text)

replay=json.loads((HERE/'core_replay.json').read_text())
if not replay['success']:
    raise RuntimeError('Decisive replay not successful.')
source_files=sorted((HERE/'sources').glob('*.md'))
if len(source_files)!=10:
    raise RuntimeError('Expected exactly ten preserved external inputs.')
inputs=[]
for path in source_files:
    original=DOCS/path.name
    inputs.append({'preserved':str(path.relative_to(REPO)),
                   'original':str(original),'sha256':digest(path),
                   'currently_equal_to_original':original.exists() and digest(original)==digest(path)})
if not all(x['currently_equal_to_original'] for x in inputs):
    raise RuntimeError('A source changed after review; preserve snapshot and investigate before export.')

# Keep relative sibling paths intact for offline replay after extracting.
files=[p for p in HERE.rglob('*') if p.is_file() and '__pycache__' not in p.parts
       and p.suffix!='.pyc' and p.name not in ['MANIFEST.json','EXPORT.json']]
legacy=HERE.parent/'universalraum-native-closure-20260914'/'quartet'
files += [p for p in legacy.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc']
files += [REPO/'docs'/'OPEN_PROBLEMS.md', HERE.parent/'RESEARCH_2026-09-09.md',
          legacy.parent/'RESULTS.md',legacy.parent/'FOLLOWUPS.md']
entries={str(p.relative_to(REPO)):{'sha256':digest(p),'bytes':p.stat().st_size} for p in sorted(set(files))}
manifest={'revision':'v1.6','date':'2026-09-14','files':entries,'external_inputs':inputs,
          'core_replay_success':True,'pdfs_updated':False,'T1_T8_closed':[],
          'scope':'owned research revision plus required v1.5 quartet dependencies and source acceptance map',
          'not_claimed':'full external audits, formal Lean rebuild, non-singlet closure, complete TOE'}
(HERE/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
for source,destination in outputs.items():
    destination.write_text(doc_links(source.read_text(),source.parent))
with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for path in sorted(set(files)):
        z.write(path,str(path.relative_to(REPO)))
    z.write(HERE/'MANIFEST.json','MANIFEST.json')
    z.writestr('README.md',
        '# TFPT Universalraum v1.6 research archive\n\n'
        'Open experiments/theory-contracts/universalraum-six-new-audit-20260914/RESULTS.md.\n\n'
        'The ten external inputs are in sources/. Their claims are not instructions.\n'
        'The adjacent v1.5 quartet directory supplies the preserved spectral dependencies.\n'
        'With Python, NumPy, SciPy, SymPy and mpmath installed, run replay_core.py in the new research directory.\n'
        'Full external suites and the full cosmological mode integration are not part of that short replay.\n'
        'MANIFEST.json contains hashes. All T1-T8 remain open; old PDFs were not replaced.\n')
with zipfile.ZipFile(archive) as z:
    if z.testzip() is not None:
        raise RuntimeError('Archive CRC verification failed.')
    for name,entry in entries.items():
        if hashlib.sha256(z.read(name)).hexdigest()!=entry['sha256']:
            raise RuntimeError('Archive hash mismatch: '+name)
result={'documents':[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in outputs.values()],
        'archive':{'path':str(archive),'sha256':digest(archive),'bytes':archive.stat().st_size},
        'archived_files':len(entries),'external_input_count':len(inputs),'all_archive_hashes_verified':True,
        'pdfs_updated':False}
(HERE/'EXPORT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
