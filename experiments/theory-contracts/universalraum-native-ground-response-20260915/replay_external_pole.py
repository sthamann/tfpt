"""Frozen audit of the newly supplied v1.6.3 pole result, in our own directory."""
from pathlib import Path
from hashlib import sha256
import shutil
import subprocess
import json
import sys

HERE=Path(__file__).resolve().parent
SOURCE=Path('/Users/stefanhamann/Documents/Codex/2026-09-15/der-n-chste-entscheidende-schritt-ist/outputs')
PINS={'verify_native_pole.py':'fdbcabd244450c302182086d67c68284634c994e3fee026200c42c508f731654',
      'TFPT_Universalraum_Nativer_Pol_2026-09-15_v1.6.3.md':'77828b122446decd55b89708fe801934f31402e5398ad813aa35a5f5ce6b0d10',
      'verification_native_pole.json':'da21c77bcbd3af97b9f340968ada181f4df40efd491f3de617291aef84047309',
      'TFPT_Universalraum_Nativer_Pol_Pruefpaket_2026-09-15_v1.6.3.zip':'be77d03684de854fb55c637d6e856ff80cfbb9c4ad1b66994146a6e132cd1038'}
state={'status':'RUNNING','source_pins':PINS,'runs':[]}
def save(): (HERE/'external_pole_replay_manifest.json').write_text(json.dumps(state,indent=2)+'\n')
try:
    save()
    (HERE/'sources').mkdir(exist_ok=True)
    for name,pin in PINS.items():
        src=SOURCE/name
        if sha256(src.read_bytes()).hexdigest()!=pin: raise RuntimeError('changed source '+name)
        shutil.copy2(src,HERE/'sources'/name)
    digests=[]
    for mode,flags in [('normal',[]),('optimized',['-OO'])]:
        run=subprocess.run([sys.executable,*flags,str(HERE/'sources/verify_native_pole.py')],cwd=HERE,capture_output=True,text=True)
        (HERE/('external_pole_'+mode+'.stderr.txt')).write_text(run.stderr)
        (HERE/('external_pole_'+mode+'.json')).write_text(run.stdout)
        state['runs'].append({'mode':mode,'exit_code':run.returncode})
        save()
        if run.returncode: raise RuntimeError(run.stderr[-2000:])
        result=json.loads(run.stdout)
        if result['status']!='PASS' or result['checks']!=317: raise RuntimeError('unexpected certificate status')
        digests.append(sha256(run.stdout.encode()).hexdigest())
        state['runs'][-1].update({'checks':result['checks'],'sha256':digests[-1]})
        print(mode,result['status'],result['checks'],flush=True)
    if digests[0]!=digests[1] or digests[0]!=PINS['verification_native_pole.json']:
        raise RuntimeError('replay differs from original or under optimization')
    state['status']='PASS';save()
except BaseException as error:
    state['status']='FAIL';state['error']=repr(error);save();raise
