"""Replay: run every KeyC checker normal and -OO, demand byte-identical JSON.

Theory contract, experiments only. No paper/ledger/website edits, no commits.
Expected wall time: keyc_localize builds the 15.25M-entry v3 twice
(several minutes, ~5 GB peak); the other two checkers are fast.
"""
from pathlib import Path
from hashlib import sha256
import subprocess
import sys
import json

here = Path(__file__).resolve().parent
manifest_path = here / 'replay_manifest.json'
runs = []
totals = {'guards': 0}

def progress(status, **extra):
    manifest_path.write_text(json.dumps({'status': status, 'runs': runs, **extra}, indent=2) + '\n')

def guard_count(data):
    for key in ('guards_count', 'guards'):
        if key in data:
            value = data[key]
            return len(value) if isinstance(value, list) else int(value)
    return 0

progress('RUNNING')
CHECKERS = [('keyc_localize.py', 'localize_'), ('keyc_copysym.py', 'copysym_'),
            ('keyc_staterule.py', 'staterule_')]
for checker, prefix in CHECKERS:
    if not (here / checker).exists():
        progress('FAIL', reason='missing checker', checker=checker)
        raise SystemExit('missing checker ' + checker)
    outputs = []
    for mode, flags in [('normal', []), ('optimized', ['-OO'])]:
        p = subprocess.run([sys.executable, *flags, str(here / checker)],
                           capture_output=True, cwd=here)
        (here / f'{prefix}{mode}.json').write_bytes(p.stdout)
        (here / f'{prefix}{mode}.stderr.txt').write_bytes(p.stderr)
        if p.returncode:
            runs.append({'checker': checker, 'mode': mode, 'exit_code': p.returncode})
            progress('FAIL', reason='checker returned nonzero exit code', checker=checker, mode=mode)
            print(p.stderr.decode()[-4000:], file=sys.stderr)
            raise SystemExit(p.returncode)
        try:
            data = json.loads(p.stdout)
        except (ValueError, TypeError):
            progress('FAIL', reason='invalid checker JSON', checker=checker, mode=mode)
            raise
        if data.get('status') != 'PASS':
            progress('FAIL', reason='checker status is not PASS', checker=checker, mode=mode)
            raise RuntimeError('checker did not pass: ' + checker)
        digest = sha256(p.stdout).hexdigest()
        outputs.append(digest)
        runs.append({'checker': checker, 'mode': mode, 'exit_code': 0, 'sha256': digest})
    if outputs[0] != outputs[1]:
        progress('FAIL', reason='normal and optimized output differ', checker=checker)
        raise RuntimeError('normal and optimized output differ: ' + checker)
    totals['guards'] += guard_count(data)

manifest = {'status': 'PASS', 'runs': runs, **totals,
            'scope': 'guard counts are check conditions, not independent theorems or physical closure'}
manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps(manifest, indent=2))
