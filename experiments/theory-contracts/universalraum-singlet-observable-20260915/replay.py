"""Replay own programs normal/optimized; verify input pins and fresh contraction."""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import subprocess
import tempfile
import json
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
def digest(p):return sha256(p.read_bytes()).hexdigest()

def main():
    (HERE/'replay_manifest.json').write_text(json.dumps({'status':'RUNNING'})+'\n')
    manifest=json.loads((HERE/'sources_manifest.json').read_text())
    for name,record in manifest.items():
        if digest(HERE/'sources'/name)!=record['sha256']:raise RuntimeError('Input drift '+name)
    late=json.loads((HERE/'late_sources_manifest.json').read_text())
    for name,record in late.items():
        if digest(HERE/'late_sources'/name)!=record['sha256']:raise RuntimeError('Late input drift '+name)
    out=HERE/'replay_outputs';out.mkdir(exist_ok=True)
    reports={}
    for name in ['structure','two_boson','operations_fields','hamilton_chain','big_picture','shadows']:
        outputs=[]
        for label,flags in [('normal',[]),('optimized',['-OO'])]:
            proc=subprocess.run([sys.executable,'-B','-W','error',*flags,'verify_'+name+'.py'],
                cwd=HERE,capture_output=True,timeout=120)
            if proc.returncode:raise RuntimeError(name+' '+label+': '+proc.stderr.decode())
            if proc.stderr:raise RuntimeError('Unexpected warning '+proc.stderr.decode())
            data=json.loads(proc.stdout)
            if data['status']!='PASS':raise RuntimeError('Failed '+name)
            outputs.append(proc.stdout);(out/(name+'_'+label+'.json')).write_bytes(proc.stdout)
        if outputs[0]!=outputs[1]:raise RuntimeError('Normal/optimized mismatch '+name)
        reports[name]={'sha256':sha256(outputs[0]).hexdigest(),'exact_checks':data['exact_checks'],
                       'checker_sha256':digest(HERE/('verify_'+name+'.py'))}
    # The historical C++ contraction is small enough to replay directly. Its
    # result supplies u=TTdagger v2, including the off-ladder component.
    with np.load(HERE/'sources/spinor_tensors.npz') as archive:W=archive['W']
    if np.count_nonzero(W.imag):raise RuntimeError('Imaginary native source')
    pairs=list(combinations(range(64),2))
    text=''.join(f'{A} {pairs[c][0]} {pairs[c][1]} {int(W[A,c].real)}\n' for A,c in zip(*np.nonzero(W)))
    with tempfile.TemporaryDirectory(prefix='tfpt-krylov-replay-') as temp:
        exe=Path(temp)/'contracted_krylov'
        compiled=subprocess.run(['c++','-O2','-std=c++17',str(HERE/'sources/contracted_krylov.cpp'),'-o',str(exe)],capture_output=True,timeout=60)
        if compiled.returncode:raise RuntimeError(compiled.stderr.decode())
        run=subprocess.run([str(exe)],input=text.encode(),capture_output=True,timeout=120)
        if run.returncode:raise RuntimeError(run.stderr.decode())
        fresh=json.loads(run.stdout)
    expected=json.loads((HERE/'sources/old_contraction.json').read_text())
    if fresh!=expected:raise RuntimeError('Fresh contracted integers differ')
    (out/'fresh_contraction.json').write_text(json.dumps(fresh,indent=2,sort_keys=True)+'\n')
    summary={'status':'PASS','input_count':len(manifest)+len(late),'reports':reports,
             'exact_checks_per_python_variant':sum(r['exact_checks'] for r in reports.values()),
             'fresh_cpp_contraction_matches':True,'whole_foreign_programs_replayed':False}
    (HERE/'replay_manifest.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary,indent=2,sort_keys=True))

if __name__=='__main__':main()
