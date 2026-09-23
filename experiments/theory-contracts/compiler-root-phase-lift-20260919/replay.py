"""Replay the six bounded certificates with and without optimization."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
HERE=Path(__file__).resolve().parent
JOBS=[('checker.py','certificate.json'),('origin_obstructions.py','origin_obstruction_certificate.json'),('lift12_character_check.py','lift12_character_certificate.json'),('grade2_character_check.py','grade2_character_certificate.json'),('quartic_state_check.py','quartic_state_certificate.json'),('readout_intertwiner_check.py','readout_intertwiner_certificate.json')]
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
        result.append(row); print(json.dumps(row),flush=True)
    out={'research_id':'UR.COMPILER.ROOT_PHASE_LIFT.18','status':'PASS_SCOPED_REPLAY','claim_scope':'Exact finite certificates and specified obstructions only; no TOE completion','runs':result}
    (HERE/'replay_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__': main()
