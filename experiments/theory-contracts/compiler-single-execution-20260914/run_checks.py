"""Normal/-OO replay and in-memory mutations, without editing any source."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CHECKER = HERE/'check.py'
env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')


def run(args, code=None):
    p = subprocess.run([sys.executable, *args], input=code, text=True,
                       capture_output=True, env=env, cwd=HERE, timeout=120)
    return p


normal = run([str(CHECKER)])
optimized = run(['-OO', str(CHECKER)])
if normal.returncode or optimized.returncode:
    raise RuntimeError(normal.stderr + optimized.stderr)
if normal.stdout != optimized.stdout:
    raise ValueError('normal and optimized reports differ')
report = json.loads(normal.stdout)
source = CHECKER.read_text()
mutants = [
    ('record-one Kraus operator equals antisymmetric projector',
     "block1 = R.extract(list(range(1, 32, 2)), list(range(0, 32, 2)))",
     "block1 = s.zeros(16)"),
    ('source reset trace preserving target=0',
     "kraus.append(k)", "kraus.append(k/2)"),
    ('strict contraction off target',
     "q2 = max(e for e in eigs if e != 1)", "q2 = s.Integer(1)"),
    ('same finite experiment fresh limit five two-hundred-sixteenths',
     "limit_fresh = sum(norm2(target*branch*target*input0) for branch in (B0, B1))",
     "limit_fresh = limit_retained"),
    ('unread star channel has nontrivial fixed algebra',
     "fixed_algebra_dimension = sum(4**(2*cycles(w)) for w in words)//24",
     "fixed_algebra_dimension = 1"),
]
caught = []
for expected, old, new in mutants:
    if source.count(old) != 1:
        raise ValueError('mutation target not unique: '+old)
    changed = source.replace(old, new)
    wrapper = "__file__ = " + repr(str(CHECKER)) + "\nexec(compile(" + repr(changed) + ", __file__, 'exec'))"
    result = run(['-'], wrapper)
    if result.returncode == 0 or ('ValueError: '+expected) not in result.stderr:
        raise ValueError('mutant did not fail at intended guard: '+expected+'\n'+result.stderr)
    caught.append(expected)
(HERE/'verification.json').write_text(normal.stdout)
receipt = {'normal_OO_byte_identical': True,
           'own_exact_checks': report['own_exact_checks'],
           'inherited_source_prefix_checks': report['source_prefix_checks'],
           'mutants_caught': caught,
           'checker_sha256': hashlib.sha256(CHECKER.read_bytes()).hexdigest(),
           'T1_T8_closed': []}
(HERE/'replay.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt, indent=2))
