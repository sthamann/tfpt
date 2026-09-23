"""Hash-bound normal/-OO replay of the source-selection exact checkers."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
LANES = ('synchronization.py', 'primitive_chain.py', 'operator_meaning.py')


def run(name):
    path = HERE / name
    pin = hashlib.sha256(path.read_bytes()).hexdigest()
    outputs = []
    for options in ([], ['-OO']):
        done = subprocess.run([sys.executable, '-B', *options, str(path)],
                              cwd=HERE, capture_output=True, text=True, timeout=180)
        if done.returncode:
            raise RuntimeError(name + ': ' + done.stderr[-4000:])
        outputs.append(done.stdout)
    if outputs[0] != outputs[1]:
        raise ValueError(name + ': optimized replay differs')
    if hashlib.sha256(path.read_bytes()).hexdigest() != pin:
        raise ValueError(name + ': checker changed during replay')
    result = json.loads(outputs[0])
    if result.get('T1_T8_closed') != []:
        raise ValueError(name + ': unsupported physical status promotion')
    return name, {'checker_sha256': pin, 'normal_optimized_identical': True,
                  'result': result}


def main():
    with ThreadPoolExecutor(max_workers=3) as pool:
        lanes = dict(pool.map(run, LANES))
    print(json.dumps({'scope': 'NON-RH source selection and representation distinctions',
                      'all_replays_pass': True, 'lane_count': 3, 'execution_count': 6,
                      'lanes': lanes, 'infinite_limit_machine_proved_here': False,
                      'T1_T8_closed': []}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
