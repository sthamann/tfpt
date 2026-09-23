"""Read-only source audit; run frozen copies and retain reproducible receipts."""
from pathlib import Path
import ast
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
SOURCE = REPO / 'experiments/theory-contracts/universalraum-native-ground-response-20260915'
FROZEN_ROOT = HERE / 'frozen'
FROZEN = FROZEN_ROOT / 'experiments/theory-contracts/universalraum-native-ground-response-20260915'
NAMES = ['operation_symmetry', 'symmetry_availability', 'lorentz_types']
TENSOR = SOURCE / 'ground_replay/outputs/simple_core/spinor_tensors.npz'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def copy(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    if digest(source) != digest(target):
        raise RuntimeError(f'Copy hash differs: {source}')

receipt = {'source_before': {}, 'replays': [], 'literal_true_guards': {}}
for name in NAMES:
    source = SOURCE / (name + '.py')
    receipt['source_before'][str(source)] = digest(source)
    copy(source, FROZEN / source.name)
    tree = ast.parse(source.read_text())
    receipt['literal_true_guards'][name] = [
        {'line': node.lineno, 'label': ast.literal_eval(node.args[1])}
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        and node.func.id == 'need' and len(node.args) > 1
        and isinstance(node.args[0], ast.Constant) and node.args[0].value is True
    ]
    for mode in ['normal', 'optimized']:
        original = SOURCE / f'{name}_{mode}.json'
        receipt['source_before'][str(original)] = digest(original)
        copy(original, HERE / 'original_reports' / original.name)
receipt['source_before'][str(TENSOR)] = digest(TENSOR)
copy(TENSOR, FROZEN / 'ground_replay/outputs/simple_core/spinor_tensors.npz')
copy(TENSOR, FROZEN_ROOT / 'experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz')

for name in NAMES:
    results = {}
    for mode, flags in [('normal', ['-B']), ('optimized', ['-B', '-OO'])]:
        completed = subprocess.run([sys.executable, *flags, str(FROZEN / (name + '.py'))],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        (HERE / f'{name}_{mode}.json').write_bytes(completed.stdout)
        (HERE / f'{name}_{mode}.stderr.txt').write_bytes(completed.stderr)
        if completed.returncode:
            raise RuntimeError(f'{name} {mode} failed: {completed.stderr.decode()}')
        data = json.loads(completed.stdout)
        entry = {'name': name, 'mode': mode, 'checks': data['checks'],
                 'status': data['status'], 'stdout_sha256': hashlib.sha256(completed.stdout).hexdigest(),
                 'stderr_empty': not completed.stderr,
                 'identical_to_supplied_report': completed.stdout == (HERE / 'original_reports' / f'{name}_{mode}.json').read_bytes()}
        receipt['replays'].append(entry)
        results[mode] = completed.stdout
        print(json.dumps(entry), flush=True)
    if results['normal'] != results['optimized']:
        raise RuntimeError(f'{name}: normal and optimized differ')

receipt['all_sources_unchanged'] = all(digest(Path(path)) == pin for path, pin in receipt['source_before'].items())
if not receipt['all_sources_unchanged']:
    raise RuntimeError('Concurrent source drift detected')
scope_results=[]
for mode,flags in [('normal',['-B']),('optimized',['-B','-OO'])]:
    completed=subprocess.run([sys.executable,*flags,str(HERE/'check_scope.py')],
                             stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
    (HERE/f'check_scope_{mode}.json').write_bytes(completed.stdout)
    if completed.stderr:
        raise RuntimeError(completed.stderr.decode())
    scope_results.append(completed.stdout)
if scope_results[0]!=scope_results[1]:
    raise RuntimeError('Scope check normal and optimized differ')
receipt['scope_checks']=json.loads(scope_results[0])
receipt['status'] = 'PASS'
(HERE / 'replay_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'total_checks': sum(entry['checks'] for entry in receipt['replays'] if entry['mode'] == 'normal')}))
