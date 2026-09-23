"""Replay four finite conditional checks; emit a hash-bound JSON receipt."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
LANES = ('tl_clock.py', 'leaf_information.py', 'ternary.py', 'commutant.py')


def lane(name):
    path = HERE/name
    pin = hashlib.sha256(path.read_bytes()).hexdigest()
    outputs = []
    for options in ([], ['-OO']):
        result = subprocess.run([sys.executable, '-B', *options, str(path)],
            cwd=HERE, capture_output=True, text=True, timeout=120)
        if result.returncode:
            raise RuntimeError(name+': '+result.stderr[-4000:])
        outputs.append(result.stdout)
    if outputs[0] != outputs[1]:
        raise ValueError(name+': optimized replay differs')
    if hashlib.sha256(path.read_bytes()).hexdigest() != pin:
        raise ValueError(name+': source changed during replay')
    payload = json.loads(outputs[0])
    if payload.get('T1_T8_closed') != []:
        raise ValueError(name+': finite audit must not close physical gates')
    return name, {'checker_sha256': pin, 'normal_optimized_identical': True,
                  'result': payload}


def main():
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = dict(pool.map(lane, LANES))
    print(json.dumps({'scope': 'NON-RH conditional composition/refinement/information',
        'all_replays_pass': True, 'lane_count': len(LANES), 'execution_count': 2*len(LANES),
        'T1_T8_closed': [], 'lanes': results}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
