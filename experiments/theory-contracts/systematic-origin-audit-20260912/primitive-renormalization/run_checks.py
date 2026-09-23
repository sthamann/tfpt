"""Hash-bound replay of NON-RH primitive renormalization exact checkers."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
LANES = ('frame_audit.py', 'block_link.py', 'second_order.py')


def run(name):
    path = HERE/name
    pin = hashlib.sha256(path.read_bytes()).hexdigest()
    def execute(options):
        done = subprocess.run([sys.executable, '-B', *options, str(path)],
                              cwd=HERE, capture_output=True, text=True, timeout=600)
        if done.returncode:
            raise RuntimeError(name+': '+done.stderr[-4000:])
        return done.stdout
    with ThreadPoolExecutor(max_workers=2) as replays:
        outputs = list(replays.map(execute, ([], ['-OO'])))
    if outputs[0] != outputs[1]:
        raise ValueError(name+': optimized replay differs')
    if hashlib.sha256(path.read_bytes()).hexdigest() != pin:
        raise ValueError(name+': checker drift during replay')
    result = json.loads(outputs[0])
    if result.get('T1_T8_closed') != []:
        raise ValueError(name+': no physical status promotion')
    return name, {'checker_sha256': pin, 'normal_optimized_identical': True, 'result': result}


def main():
    with ThreadPoolExecutor(max_workers=3) as pool:
        lanes = dict(pool.map(run, LANES))
    print(json.dumps({'scope': 'NON-RH exact finite primitive weak-link expansion and source audit',
        'all_replays_pass': True, 'lane_count': 3, 'execution_count': 6,
        'lanes': lanes, 'uniform_many_block_error_proved': False,
        'T1_T8_closed': []}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
