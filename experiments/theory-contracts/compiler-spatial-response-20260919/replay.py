"""Bounded contract replay with unconditional normal/-OO checks."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

HERE=Path(__file__).resolve().parent
JOBS=[
 ('chain_order_check.py','chain_order_certificate.json',[]),
 ('spatial_response_check.py','spatial_response_check.json',['--json']),
 ('neutral_current_bridge_check.py','neutral_current_bridge_check.json',['--out','neutral_current_bridge_check.json']),
 ('current_response_check.py','current_response_check.json',[]),
]
if (HERE/'completion24_check.py').exists():
    JOBS.append(('completion24_check.py','completion24_check.json',['--out','completion24_check.json']))


def main():
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    rows=[]
    for script,cert,extra in JOBS:
        outputs=[]
        for flags in [('-B',),('-B','-OO')]:
            run=subprocess.run([sys.executable,*flags,str(HERE/script),*extra],cwd=HERE,
                               env=env,text=True,capture_output=True)
            if run.returncode:
                raise RuntimeError(f'{script} {flags}\n{run.stderr}\n{run.stdout[-1000:]}')
            if script=='spatial_response_check.py':
                # This checker emits its certificate to stdout by design.
                json.loads(run.stdout)
                (HERE/cert).write_text(run.stdout)
            outputs.append((HERE/cert).read_bytes())
        if outputs[0]!=outputs[1]:
            raise RuntimeError(f'normal/-OO certificate mismatch: {script}')
        row={'checker':script,'certificate':cert,'normal_and_OO_identical':True,
             'sha256':hashlib.sha256(outputs[0]).hexdigest()}
        rows.append(row)
        print(json.dumps(row),flush=True)
    result={'research_id':'UR.COMPILER.SPATIAL_RESPONSE.20','verdict':'PASS_SCOPED_REPLAY',
            'runs':rows,'scope':'Finite checks, numeric profile replay and written conditional proofs only; no physical gate closed'}
    (HERE/'replay_certificate.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
