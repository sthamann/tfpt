"""Scoped package, extraction replay, and non-overwriting Documents delivery."""
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile, ZIP_DEFLATED
import json
import shutil
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent
DEST=Path('/Users/stefanhamann/Documents')
ARCHIVE='TFPT_Universalraum_Quellkomposition_Pruefpaket_2026-09-15_v1.6.9.zip'
TOP='universalraum-v1.6.9'
def digest(p):return sha256(p.read_bytes()).hexdigest()

def main():
 replay=json.loads((HERE/'replay_manifest.json').read_text())
 docs=json.loads((HERE/'documents_manifest.json').read_text())
 qa=json.loads((HERE/'pdf_qa.json').read_text())
 visual=json.loads((HERE/'visual_qa.json').read_text())
 if any(x['status']!='PASS' for x in (replay,qa,visual)):raise RuntimeError('Unfinished verification')
 for name,rec in {**replay['reports'],'independent_review':replay['independent_crosscheck_not_counted_in_own_total']}.items():
  if digest(HERE/rec['script'])!=rec['checker_sha256']:raise RuntimeError('Changed verifier '+name)
  for mode in ('normal','optimized'):
   if digest(HERE/'replay_outputs'/(name+'_'+mode+'.json'))!=rec['result_sha256']:
    raise RuntimeError('Changed result '+name)
 for name,rec in docs.items():
  if digest(HERE/rec['markdown'])!=rec['md_sha256']:raise RuntimeError('Changed Markdown '+name)
  if digest(HERE/rec['pdf'])!=rec['pdf_sha256']:raise RuntimeError('Changed PDF '+name)
  if any(x['documents'][name]['pdf_sha256']!=rec['pdf_sha256'] for x in (qa,visual)):
   raise RuntimeError('Stale PDF verification '+name)
 excluded={'tmp','__pycache__','.DS_Store','package_files.json','delivery_manifest.json',ARCHIVE}
 files=sorted(p for p in HERE.rglob('*') if p.is_file()
              and not any(x in excluded for x in p.relative_to(HERE).parts)
              and not p.name.endswith('.pyc'))
 records={str(p.relative_to(HERE)):digest(p) for p in files}
 receipt=HERE/'package_files.json';receipt.write_text(json.dumps(records,indent=2,sort_keys=True)+'\n')
 archive=HERE/ARCHIVE
 with ZipFile(archive,'w',ZIP_DEFLATED) as z:
  for p in files+[receipt]:z.write(p,TOP+'/'+str(p.relative_to(HERE)))
 with tempfile.TemporaryDirectory(prefix='tfpt-v169-package-replay-') as td:
  with ZipFile(archive) as z:z.extractall(td)
  root=Path(td)/TOP
  for name,h in records.items():
   if digest(root/name)!=h:raise RuntimeError('Extraction hash failure '+name)
  proc=subprocess.run([sys.executable,'-B','replay.py'],cwd=root,capture_output=True,timeout=360)
  if proc.returncode:raise RuntimeError('Extraction replay failed: '+proc.stderr.decode())
  if json.loads((root/'replay_manifest.json').read_text())!=replay:
   raise RuntimeError('Extraction replay manifest differs')
 selected=[]
 for rec in docs.values():selected.extend([HERE/rec['markdown'],HERE/rec['pdf']])
 selected.append(archive)
 for p in selected:
  target=DEST/p.name
  if target.exists() and digest(target)!=digest(p):raise RuntimeError('Different existing version '+str(target))
 delivered={}
 for p in selected:
  target=DEST/p.name
  if not target.exists():shutil.copy2(p,target)
  if digest(target)!=digest(p):raise RuntimeError('Delivery mismatch')
  delivered[str(target)]={'sha256':digest(target),'bytes':target.stat().st_size}
 result={'status':'PASS','package_extracted_and_replayed':True,
     'own_exact_checks_per_variant':replay['own_exact_checks_per_variant'],
     'own_numerical_checks_per_variant':replay['own_numerical_checks_per_variant'],
     'separate_crosscheck_exact_conditions':13,
     'supplied_and_inherited_checks_reported_separately':True,
     'existing_different_versions_overwritten':False,'commit_or_push':False,'files':delivered}
 (HERE/'delivery_manifest.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()

