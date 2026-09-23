"""Execute the contract checker twice (normal and -OO).

Byte-identity is required after removing runtime fields from the JSON
report. Status starts at RUNNING; any failure sets FAIL; only a full
successful pass sets PASS. No prior research report is changed by this.
"""
from pathlib import Path
from hashlib import sha256
import subprocess
import sys
import json

here = Path(__file__).resolve().parent
CHECKER = 'seam_reflection_operator.py'

manifest_path = here / 'replay_manifest.json'
runs = []


def progress(status, **extra):
    manifest_path.write_text(json.dumps({'status': status, 'runs': runs, **extra},
                                        indent=2) + '\n')


def canonical(raw):
    data = json.loads(raw)
    data.pop('runtime_seconds', None)
    return json.dumps(data, sort_keys=True)


progress('RUNNING')
outputs = []
for mode, flags in [('normal', []), ('optimized', ['-B', '-OO'])]:
    p = subprocess.run([sys.executable, *flags, str(here / CHECKER)],
                       capture_output=True, cwd=here)
    (here / f'seam_reflection_{mode}.json').write_bytes(p.stdout)
    (here / f'seam_reflection_{mode}.stderr.txt').write_bytes(p.stderr)
    if p.returncode:
        runs.append({'checker': CHECKER, 'mode': mode, 'exit_code': p.returncode})
        progress('FAIL', reason='checker returned a nonzero exit code')
        print(p.stderr.decode(), file=sys.stderr)
        raise SystemExit(p.returncode)
    data = json.loads(p.stdout)
    if data.get('status') != 'PASS':
        progress('FAIL', reason='checker status is not PASS', mode=mode)
        raise RuntimeError('checker did not pass: ' + CHECKER)
    outputs.append(canonical(p.stdout))
    runs.append({'checker': CHECKER, 'mode': mode, 'exit_code': p.returncode,
                 'sha256': sha256(p.stdout).hexdigest()})
if outputs[0] != outputs[1]:
    progress('FAIL', reason='normal and optimized output differ')
    raise RuntimeError('normal and optimized output differ: ' + CHECKER)

manifest = {'status': 'PASS', 'runs': runs,
            'exact_checks': data.get('exact_checks'),
            'identity': 'normal vs -OO byte-identical after removing runtime fields',
            'scope': 'counts are guards, not independent new theorems or '
                     'physical closure; theory contract, no verification claim'}
manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps(manifest, indent=2))
