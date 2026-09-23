"""Freeze read inputs or create a bounded, independently replayable package."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import sys
from zipfile import ZipFile, ZIP_DEFLATED

HERE=Path(__file__).resolve().parent
ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')


def freeze():
    records={}
    result=json.loads((HERE/'verification_normal.json').read_text())
    paths=dict(result['source_hashes'])
    helper=ROOT/'verification/tfpt_constants.py'
    paths[str(helper)]=sha256(helper.read_bytes()).hexdigest()
    for name in ('v177_seam_marking_kernel.py','v180_clock_is_mobius.py'):
        p=ROOT/'verification'/name
        paths[str(p)]=sha256(p.read_bytes()).hexdigest()
    for i,(name,digest) in enumerate(paths.items()):
        source=Path(name)
        if sha256(source.read_bytes()).hexdigest()!=digest:raise RuntimeError('changed source '+name)
        if source.name in ('v480_multilocal_four_interval.py','tfpt_constants.py'):
            target=HERE/'sources/clock'/source.name
        else:target=HERE/'sources'/('input_'+str(i)+'_'+source.name)
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists() and target.read_bytes()!=source.read_bytes():raise RuntimeError('would overwrite different frozen file')
        shutil.copy2(source,target)
        records[name]={'local':str(target.relative_to(HERE)),'sha256':digest}
    (HERE/'frozen_sources.json').write_text(json.dumps(records,indent=2)+'\n')
    late=json.loads((HERE/'late_aspects_normal.json').read_text())
    for name,record in late['source_hashes'].items():
        source=Path(name)
        if sha256(source.read_bytes()).hexdigest()!=record['sha256']:raise RuntimeError('changed late source')
        target=HERE/record['local']
        if target.exists() and target.read_bytes()!=source.read_bytes():raise RuntimeError('changed frozen late source')
        shutil.copy2(source,target)
    print('Frozen '+str(len(records))+' unchanged input files')


def package():
    qa=json.loads((HERE/'PDF_QA.json').read_text())
    if qa['status']!='PASS':raise RuntimeError('PDF QA incomplete')
    replay=json.loads((HERE/'REPLAY.json').read_text())
    if replay['status']!='PASS':raise RuntimeError('replay incomplete')
    target=HERE/'TFPT_Universalraum_Spinlift_Pruefpaket_2026-09-15_v1.6.10.zip'
    files=[p for p in HERE.iterdir() if p.is_file() and p.suffix in ('.py','.md','.json','.txt','.stderr')]
    for folder in ('sources','deliverables','output/pdf'):
        files.extend(p for p in (HERE/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    with ZipFile(target,'w',ZIP_DEFLATED) as z:
        for p in sorted(set(files)):z.write(p,str(p.relative_to(HERE)))
    print(json.dumps({'path':str(target),'sha256':sha256(target.read_bytes()).hexdigest(),'files':len(set(files)),'bytes':target.stat().st_size}))


if __name__=='__main__':
    if sys.argv[1:] == ['package']:package()
    else:freeze()
