"""Owned deterministic replay and targeted negative controls; no external writes."""
import json
import hashlib
import os
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'check.py'


def main():
    initial_hash=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'}
    outputs=[]
    for flags in (['-B'],['-B','-OO']):
        print('Running full audit '+str(flags),flush=True)
        result=subprocess.run([sys.executable,*flags,str(SOURCE)],capture_output=True,text=True,
                              timeout=360,env=env,check=True)
        if result.stderr: raise ValueError(result.stderr)
        outputs.append(result.stdout)
    if outputs[0]!=outputs[1]: raise ValueError('normal and optimized replay differ')
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest()!=initial_hash:
        raise ValueError('checker changed during replay; rerun frozen version')
    raw=SOURCE.read_text()
    mutations=[
        ('tagged.T*tagged == eye-same','tagged.T*tagged == eye-swap',
         'history_and_completion()', 'ordered-color history destroys exchange interference'),
        ('np.count_nonzero(np.diag(collisions)==0) == 24','np.count_nonzero(np.diag(collisions)==0) == 1',
         'history_and_completion()', 'fully colored history gives 24 ground states'),
        ('(Ui*Ui)[:16,:16] == -swap','(Ui*Ui)[:16,:16] == eye',
         'history_and_completion()', 'same vertex different two-step physics'),
        ('s.Rational(1,2):1,s.Rational(5,8):4','s.Rational(1,3):1,s.Rational(5,8):4',
         'two_cell_exact()', 'adjoint compression half five-eighths three-quarters'),
        ('series_s=-2*g*g/Delta+4*g**6/Delta**5','series_s=-2*g*g/Delta+g**4/Delta**3+4*g**6/Delta**5',
         "star_and_mediator(load_module('compiler-extension-audit-20260914/check_extension.py','mutant_source'))",
         'symmetric mediator branch has no fourth-order term'),
    ]
    caught=[]
    for old,new,call,guard in mutations:
        if raw.count(old)!=1: raise ValueError('ambiguous mutation '+old)
        code='__file__='+repr(str(SOURCE))+'\n__name__="mutation_probe"\n'+raw.replace(old,new)+'\n'+call
        result=subprocess.run([sys.executable,'-B','-OO','-c',code],capture_output=True,text=True,
                              timeout=90,env=env)
        if result.returncode==0 or guard not in result.stderr:
            raise ValueError('mutation failed to hit intended guard '+guard+'\n'+result.stderr)
        caught.append(guard)
    (HERE/'verification.json').write_text(outputs[0])
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest()!=initial_hash:
        raise ValueError('checker changed during negative controls')
    report={'normal_OO_byte_identical':True,'negative_controls_caught':caught,'checker_sha256':initial_hash,
            'counts_per_mode':json.loads(outputs[0])['counts'],'T1_T8_closed':[]}
    (HERE/'replay.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2),flush=True)


if __name__=='__main__': main()
