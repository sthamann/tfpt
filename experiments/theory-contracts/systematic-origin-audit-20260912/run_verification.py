"""Replay the integrated bounded audit, without modifying physical status.

Eight isolated finite checks, each normal and optimized. Not a full TFPT suite,
microscopic continuum replay, proof-assistant certification or empirical test.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREVIOUS = HERE.parent / 'primitive-transfer-selection-20260912'
LANES = {
    'coherent_record': PREVIOUS / 'coherent_compiler_record.py',
    'logical_selection': PREVIOUS / 'coherent_record_selection.py',
    'clock_origin': HERE / 'clock-origin/checker.py',
    'interaction': HERE / 'interaction/checker.py',
    'independent_redteam': HERE / 'redteam/independent_check.py',
    'charge_clock_bridge': HERE / 'charge_clock_bridge.py',
    'composition': HERE / 'interaction/composition.py',
    'composition_direct': HERE / 'redteam/composition_direct.py',
}


def run_lane(item):
    name, path = item
    digest_before = hashlib.sha256(path.read_bytes()).hexdigest()
    outputs = []
    try:
        for optimized in (False, True):
            args = [sys.executable, '-B'] + (['-OO'] if optimized else []) + [str(path)]
            result = subprocess.run(args, cwd=ROOT, capture_output=True, timeout=120)
            if result.returncode:
                raise RuntimeError(result.stderr.decode(errors='replace')[-4000:])
            outputs.append(result.stdout)
        if outputs[0] != outputs[1]:
            raise RuntimeError('normal and optimized outputs differ')
        payload = json.loads(outputs[0])
        gate_key = ('physical_gates_closed' if name in ('independent_redteam', 'composition_direct')
                    else 'T1_T8_closed')
        if payload.get(gate_key) != []:
            raise RuntimeError('bounded audit must not promote a physical acceptance gate')
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest_before:
            raise RuntimeError('checker changed during replay')
        return name, {'verification': 'pass', 'normal_optimized_byte_identical': True,
                      'checker_sha256': digest_before, 'result': payload}
    except (RuntimeError, subprocess.TimeoutExpired, ValueError) as error:
        return name, {'verification': 'failed', 'error': str(error), 'checker_sha256': digest_before}


def main():
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = dict(pool.map(run_lane, LANES.items()))
    passed = all(result['verification'] == 'pass' for result in results.values())
    print(json.dumps({'scope': 'NON-RH bounded source and finite algebra audit',
        'all_replays_pass': passed, 'lane_count': len(LANES), 'normal_and_optimized_per_lane': True,
        'physical_completion_proved': False, 'physical_gates_closed': [],
        'not_replayed': ['full TFPT suite', 'microscopic continuum estimates',
                         'rotor infinite-volume proofs', 'independent physical holdouts'],
        'lanes': results}, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
