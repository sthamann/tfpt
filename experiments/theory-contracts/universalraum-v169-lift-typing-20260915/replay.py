"""Execute all four checkers of this contract twice (normal and -OO).

Byte-identity is required after removing runtime fields from the JSON
reports. Status starts at RUNNING; any failure sets FAIL; only a full
successful pass sets PASS. No prior research report is changed by this.
"""
from pathlib import Path
from hashlib import sha256
import subprocess
import sys
import json

here = Path(__file__).resolve().parent
CHECKERS = [('check_source_side.py', 'source_'),
            ('check_multiparticle.py', 'multiparticle_'),
            ('check_recorded_experiment.py', 'experiment_'),
            ('check_process_symmetry.py', 'symmetry_')]

manifest_path = here / 'replay_manifest.json'
runs = []
totals = {'guards': 0, 'exact_guards': 0, 'numerical_guards': 0}


def progress(status, **extra):
    manifest_path.write_text(json.dumps({'status': status, 'runs': runs, **extra}, indent=2) + '\n')


def canonical(raw):
    data = json.loads(raw)
    data.pop('runtime_seconds', None)
    return json.dumps(data, sort_keys=True)


progress('RUNNING')
for checker, prefix in CHECKERS:
    outputs = []
    for mode, flags in [('normal', []), ('optimized', ['-B', '-OO'])]:
        p = subprocess.run([sys.executable, *flags, str(here / checker)], capture_output=True, cwd=here)
        (here / f'{prefix}{mode}.json').write_bytes(p.stdout)
        (here / f'{prefix}{mode}.stderr.txt').write_bytes(p.stderr)
        if p.returncode:
            runs.append({'checker': checker, 'mode': mode, 'exit_code': p.returncode})
            progress('FAIL', reason='checker returned a nonzero exit code', checker=checker)
            print(p.stderr.decode(), file=sys.stderr)
            raise SystemExit(p.returncode)
        try:
            data = json.loads(p.stdout)
        except (ValueError, TypeError):
            progress('FAIL', reason='invalid checker JSON', checker=checker, mode=mode)
            raise
        if data.get('status') != 'PASS':
            progress('FAIL', reason='checker status is not PASS', checker=checker, mode=mode)
            raise RuntimeError('checker did not pass: ' + checker)
        outputs.append(canonical(p.stdout))
        runs.append({'checker': checker, 'mode': mode, 'exit_code': p.returncode,
                     'sha256': sha256(p.stdout).hexdigest()})
    if outputs[0] != outputs[1]:
        progress('FAIL', reason='normal and optimized output differ', checker=checker)
        raise RuntimeError('normal and optimized output differ: ' + checker)
    for key in totals:
        totals[key] += data.get(key, 0)

manifest = {'status': 'PASS', 'runs': runs, **totals,
            'identity': 'normal vs -OO byte-identical after removing runtime fields',
            'scope': 'counts are guards, not independent new theorems or physical closure; '
                     'theory contract only - no paper, ledger or website claim'}
manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps(manifest, indent=2))
