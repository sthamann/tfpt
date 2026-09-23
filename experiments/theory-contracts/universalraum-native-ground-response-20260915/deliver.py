"""Versioned delivery, without overwriting a different prior Documents file."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import zipfile

HERE=Path(__file__).resolve().parent
DOCUMENTS=Path('/Users/stefanhamann/Documents')
report={'status':'RUNNING','scope':'v1.6.4 research continuation, not a replacement of the main PDF','files':[]}
def save(): (HERE/'delivery_manifest.json').write_text(json.dumps(report,indent=2)+'\n')
def publish(src,name):
    dst=DOCUMENTS/name
    digest=sha256(src.read_bytes()).hexdigest()
    if dst.exists() and sha256(dst.read_bytes()).hexdigest()!=digest:
        raise RuntimeError('different existing delivery: '+str(dst))
    shutil.copy2(src,dst)
    if sha256(dst.read_bytes()).hexdigest()!=digest: raise RuntimeError('copy hash mismatch')
    report['files'].append({'path':str(dst),'sha256':digest,'bytes':dst.stat().st_size})
    save()
try:
    save()
    for name in ['ground_replay_manifest.json','external_pole_replay_manifest.json','response_replay_manifest.json']:
        data=json.loads((HERE/name).read_text())
        if data['status']!='PASS': raise RuntimeError('incomplete verification: '+name)
    # Recheck all original read-only inputs after the work, not just before it.
    for modname in ['replay_ground','replay_external_pole']:
        if modname=='replay_external_pole':
            data=json.loads((HERE/'external_pole_replay_manifest.json').read_text())
            origin=Path('/Users/stefanhamann/Documents/Codex/2026-09-15/der-n-chste-entscheidende-schritt-ist/outputs')
        else:
            data=json.loads((HERE/'ground_replay_manifest.json').read_text())
            origin=Path('/Users/stefanhamann/Documents/Codex/2026-09-14/scha-3')
        for name,digest in data['source_pins'].items():
            if sha256((origin/name).read_bytes()).hexdigest()!=digest: raise RuntimeError('source changed after replay: '+name)
    report['all_pinned_inputs_unchanged']=True
    publish(HERE/'RESULTS.md','TFPT_Universalraum_Native_Antwort_Konsolidierung_2026-09-15_v1.6.4.md')
    publish(HERE/'EINFACH_ERKLAERT.md','TFPT_Universalraum_Native_Antwort_Einfach_2026-09-15_v1.6.4.md')
    archive=HERE/'TFPT_Universalraum_Native_Antwort_Pruefpaket_2026-09-15_v1.6.4.zip'
    entries=[]
    for path in sorted(HERE.rglob('*')):
        if not path.is_file() or '__pycache__' in path.parts: continue
        if path==archive or path.name=='delivery_manifest.json' or path.name=='vacuum_moments': continue
        entries.append(path)
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for path in entries: z.write(path,Path('TFPT_Native_Antwort_v1.6.4')/path.relative_to(HERE))
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None: raise RuntimeError('zip integrity failed')
    report['archive_file_count']=len(entries)
    publish(archive,archive.name)
    report['status']='PASS';save()
    print(json.dumps(report,indent=2))
except BaseException as error:
    report['status']='FAIL';report['error']=repr(error);save();raise
