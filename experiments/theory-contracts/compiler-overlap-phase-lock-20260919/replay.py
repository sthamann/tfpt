"""Replay the six bounded certificates with and without optimization."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
HERE=Path(__file__).resolve().parent
JOBS=[('phase_balance_check.py', 'phase_balance_certificate.json'), ('effective_check.py', 'effective_check.json'), ('schur_check.py', 'schur_check.json'), ('overlap_lift_check.py', 'overlap_lift_certificate.json'), ('standard_lift_lock_check.py', 'standard_lift_lock_certificate.json'), ('quartic_1plus3_check.py', 'quartic_1plus3_check.json')]
def main():
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    result=[]
    for script,cert in JOBS:
        data=[]
        for flags in [('-B',),('-B','-OO')]:
            proc=subprocess.run([sys.executable,*flags,str(HERE/script)],cwd=HERE,env=env,text=True,capture_output=True)
            if proc.returncode:
                raise RuntimeError(f'{script} {flags} failed\n{proc.stderr}\n{proc.stdout[-2000:]}')
            data.append((HERE/cert).read_bytes())
        if data[0]!=data[1]: raise RuntimeError(f'normal/-OO mismatch: {script}')
        d=json.loads(data[0]); row={'checker':script,'certificate':cert,'normal_and_OO_identical':True,'sha256':hashlib.sha256(data[0]).hexdigest(),'checks':d.get('check_evaluations',d.get('finite_checks',d.get('checks')))}
        if isinstance(row['checks'],list): row['checks']=len(row['checks'])
        result.append(row); print(json.dumps(row),flush=True)
    out={'research_id':'UR.COMPILER.OVERLAP_PHASE_LOCK.19','status':'PASS_SCOPED_REPLAY','claim_scope':'Exact finite certificates and specified obstructions only; no TOE completion','runs':result}
    (HERE/'replay_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__': main()
