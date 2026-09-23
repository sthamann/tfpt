"""Replay the exact local-block and frame checks without physical promotion."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
LANES=('block_family.py','encoding_response.py','observer_form.py')


def run(name):
    path=HERE/name
    pin=hashlib.sha256(path.read_bytes()).hexdigest()
    def execute(options):
        done=subprocess.run([sys.executable,'-B',*options,str(path)],cwd=HERE,
                            capture_output=True,text=True,timeout=180)
        if done.returncode:
            raise RuntimeError(name+': '+done.stderr[-4000:])
        return done.stdout
    with ThreadPoolExecutor(max_workers=2) as replays:
        outputs=list(replays.map(execute,([],['-OO'])))
    if outputs[0]!=outputs[1]:
        raise ValueError(name+': replay differs')
    if hashlib.sha256(path.read_bytes()).hexdigest()!=pin:
        raise ValueError(name+': source drift')
    result=json.loads(outputs[0])
    if result.get('T1_T8_closed')!=[]:
        raise ValueError(name+': no TOE promotion allowed')
    return name,{'checker_sha256':pin,'normal_optimized_identical':True,'result':result}


def main():
    with ThreadPoolExecutor(max_workers=3) as pool:
        lanes=dict(pool.map(run,LANES))
    print(json.dumps({'scope':'NON-RH exact local-family response and finite frame audit',
        'all_replays_pass':True,'execution_count':6,'lanes':lanes,
        'controlled_iterated_RG_proved':False,'T1_T8_closed':[]},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
