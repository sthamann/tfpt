"""Replay finite corroboration of chain extension; not an external theorem prover."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
LANES=('diagrams.py','append.py','local_response.py')


def run(name):
    path=HERE/name
    pin=hashlib.sha256(path.read_bytes()).hexdigest()
    outputs=[]
    for options in ([],['-OO']):
        done=subprocess.run([sys.executable,'-B',*options,str(path)],cwd=HERE,
                            capture_output=True,text=True,timeout=180)
        if done.returncode:
            raise RuntimeError(name+': '+done.stderr[-3000:])
        outputs.append(done.stdout)
    if outputs[0]!=outputs[1]:
        raise ValueError(name+': optimization replay differs')
    if hashlib.sha256(path.read_bytes()).hexdigest()!=pin:
        raise ValueError(name+': source drift during replay')
    result=json.loads(outputs[0])
    if result.get('T1_T8_closed')!=[]:
        raise ValueError(name+': no physical status promotion')
    return name,{'checker_sha256':pin,'normal_optimized_identical':True,'result':result}


def main():
    with ThreadPoolExecutor(max_workers=3) as pool:
        lanes=dict(pool.map(run,LANES))
    print(json.dumps({'scope':'NON-RH finite checks plus separately documented all-length proofs',
        'all_replays_pass':True,'lane_count':3,'execution_count':6,'lanes':lanes,
        'external_thermodynamic_theorem_machine_proved_here':False,
        'thermodynamic_assumptions_checked_analytically_in':'README.md section 4',
        'T1_T8_closed':[]},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
