"""NON-RH source-pinned parallel replay for uniform-chain work."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
LANES = ('bond_algebra.py','operator_structure.py','hierarchy_source.py',
         'dimer_parent.py','trimer_variational.py','dimer_filter.py')


def hashes():
    return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(HERE.glob('*.py'))}


def run(name):
    def execute(options):
        done = subprocess.run([sys.executable,'-B',*options,str(HERE/name)],cwd=HERE,
                              capture_output=True,text=True,timeout=180)
        if done.returncode:
            raise RuntimeError(name+': '+done.stderr[-4000:])
        return done.stdout
    with ThreadPoolExecutor(max_workers=2) as pool:
        outputs = list(pool.map(execute,([],['-OO'])))
    if outputs[0] != outputs[1]:
        raise ValueError(name+': optimized replay differs')
    result = json.loads(outputs[0])
    if result.get('T1_T8_closed') != []:
        raise ValueError(name+': invalid promotion')
    return name, {'normal_optimized_identical':True,'result':result}


def main():
    before = hashes()
    with ThreadPoolExecutor(max_workers=3) as pool:
        lanes = dict(pool.map(run,LANES))
    if hashes() != before:
        raise ValueError('local Python source changed during replay')
    print(json.dumps({'scope':'NON-RH uniform primitive-chain algebra, variational obstruction and dimer comparison',
        'all_replays_pass':True,'execution_count':2*len(LANES),'source_sha256':before,
        'lanes':lanes,'T1_T8_closed':[]},indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
