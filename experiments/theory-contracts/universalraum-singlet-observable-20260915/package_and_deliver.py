"""Package only this contract, replay it after extraction, then deliver safely.

Never overwrites a different previously delivered version. Source locations
are recorded but the scientific replay only uses frozen package inputs.
"""
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile,ZIP_DEFLATED
import json
import subprocess
import tempfile
import shutil
import sys

HERE=Path(__file__).resolve().parent
DEST=Path('/Users/stefanhamann/Documents')
ARCHIVE='TFPT_Universalraum_Richtige_Kette_Pruefpaket_2026-09-15_v1.6.7.zip'
TOP='universalraum-v1.6.7'
def digest(p):return sha256(p.read_bytes()).hexdigest()

def main():
    replay=json.loads((HERE/'replay_manifest.json').read_text())
    docs=json.loads((HERE/'documents_manifest.json').read_text())
    qa=json.loads((HERE/'pdf_qa.json').read_text())
    visual=json.loads((HERE/'visual_qa.json').read_text())
    if replay['status']!='PASS' or qa['status']!='PASS' or visual['status']!='PASS':
        raise RuntimeError('Unfinished scientific or document verification')
    for name,rec in replay['reports'].items():
        if digest(HERE/('verify_'+name+'.py'))!=rec['checker_sha256']:raise RuntimeError('Changed checker '+name)
        for mode in ('normal','optimized'):
            if digest(HERE/'replay_outputs'/(name+'_'+mode+'.json'))!=rec['sha256']:raise RuntimeError('Changed replay output')
    for name,rec in docs.items():
        if digest(HERE/rec['markdown'])!=rec['md_sha256']:raise RuntimeError('Changed Markdown '+name)
        if digest(HERE/rec['pdf'])!=rec['pdf_sha256']:raise RuntimeError('Changed PDF '+name)
        if qa['documents'][name]['pdf_sha256']!=rec['pdf_sha256']:raise RuntimeError('Stale PDF QA')
        if visual['documents'][name]['pdf_sha256']!=rec['pdf_sha256']:raise RuntimeError('Stale visual QA')
    # Only explicitly scoped contract content, not the repo or transient tools.
    excluded={'tmp','__pycache__','.DS_Store','package_files.json','delivery_manifest.json',ARCHIVE}
    files=sorted(p for p in HERE.rglob('*') if p.is_file()
                 and not any(part in excluded for part in p.relative_to(HERE).parts)
                 and not p.name.endswith('.pyc'))
    records={str(p.relative_to(HERE)):digest(p) for p in files}
    receipt=HERE/'package_files.json'
    receipt.write_text(json.dumps(records,indent=2,sort_keys=True)+'\n')
    archive=HERE/ARCHIVE
    with ZipFile(archive,'w',ZIP_DEFLATED) as z:
        for p in files+[receipt]:z.write(p,TOP+'/'+str(p.relative_to(HERE)))
    with tempfile.TemporaryDirectory(prefix='tfpt-v167-delivery-replay-') as tmp:
        with ZipFile(archive) as z:z.extractall(tmp)
        root=Path(tmp)/TOP
        for name,h in records.items():
            if digest(root/name)!=h:raise RuntimeError('Extraction changed file '+name)
        proc=subprocess.run([sys.executable,'-B','replay.py'],cwd=root,capture_output=True,timeout=300)
        if proc.returncode:raise RuntimeError('Extracted replay failed: '+proc.stderr.decode())
        if json.loads((root/'replay_manifest.json').read_text())!=replay:raise RuntimeError('Extracted replay manifest differs')
    selected=[]
    for rec in docs.values():selected.extend([HERE/rec['markdown'],HERE/rec['pdf']])
    selected.append(archive)
    # Check all destinations before writing any of them.
    for source in selected:
        target=DEST/source.name
        if target.exists() and digest(target)!=digest(source):raise RuntimeError('Refusing to overwrite different version '+str(target))
    deliveries={}
    for source in selected:
        target=DEST/source.name
        if not target.exists():shutil.copy2(source,target)
        if digest(target)!=digest(source):raise RuntimeError('Delivery copy mismatch')
        deliveries[str(target)]={'sha256':digest(target),'bytes':target.stat().st_size}
    final={'status':'PASS','package_extracted_and_replayed':True,
           'exact_checks_per_variant':replay['exact_checks_per_python_variant'],
           'input_count':replay['input_count'],'files':deliveries,
           'existing_different_versions_overwritten':False,'commit_or_push':False}
    (HERE/'delivery_manifest.json').write_text(json.dumps(final,indent=2,sort_keys=True)+'\n')
    print(json.dumps(final,indent=2,sort_keys=True))

if __name__=='__main__':main()
