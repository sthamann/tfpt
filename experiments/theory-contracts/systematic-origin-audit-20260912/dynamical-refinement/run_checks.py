"""Replay finite dynamical repair checks; exact and numerical scopes separated."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
LANES = ('hull.py','weights.py','recovery.py','filter.py','boundary_access.py')


def run(name):
    path = HERE/name
    pin = hashlib.sha256(path.read_bytes()).hexdigest()
    outputs = []
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
    for options in ([], ['-OO']):
        result = subprocess.run([sys.executable,'-B',*options,str(path)],cwd=HERE,
            env=env,capture_output=True,text=True,timeout=180)
        if result.returncode:
            raise RuntimeError(name+': '+result.stderr[-3000:])
        outputs.append(result.stdout)
    if outputs[0] != outputs[1]:
        raise ValueError(name+': replay changed under optimization')
    if hashlib.sha256(path.read_bytes()).hexdigest() != pin:
        raise ValueError(name+': file changed during replay')
    payload = json.loads(outputs[0])
    if payload.get('T1_T8_closed') != []:
        raise ValueError(name+': no physical gate promotion permitted')
    return name, {'checker_sha256':pin,'normal_optimized_identical':True,
        'evidence_class':('exact sector formulas plus floating full-space diagnostic'
                          if name=='filter.py' else 'exact finite algebra'),
        'result':payload}


def main():
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = dict(pool.map(run, LANES))
    print(json.dumps({'scope':'NON-RH conditional finite dynamical refinement',
        'all_replays_pass':True,'execution_count':10,'lane_count':5,
        'full_spectrum_rigorous_certificate':False,'T1_T8_closed':[],
        'lanes':results},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
