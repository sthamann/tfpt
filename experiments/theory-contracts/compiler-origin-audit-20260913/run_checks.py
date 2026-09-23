"""Replay the four finite audits and reject scoped in-memory mutations. NON-RH."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def main():
    results = {}
    for name in ('label_lift.py', 'spinor_symmetry.py', 'context_instrument.py', 'record_composition.py'):
        path = HERE / name
        runs = []
        for flags in (['-B'], ['-B', '-OO']):
            run = subprocess.run([sys.executable, *flags, str(path)],
                                 capture_output=True, text=True, timeout=60, check=True)
            if run.stderr:
                raise ValueError('unexpected stderr: ' + run.stderr)
            runs.append(run.stdout)
        if runs[0] != runs[1]:
            raise ValueError('optimization-mode mismatch: ' + name)
        results[name] = {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                         'normal_OO_byte_identical': True, 'result': json.loads(runs[0])}

    mutations = [
        ('label_lift.py', "    require(n == 15,", "    b[0][0] ^= 1\n    require(n == 15,",
         'B regular degree seven'),
        ('label_lift.py', 'F(counts[i][j], 720 * 7)', 'F(counts[i][j], 720 * 6)',
         'fully covariant lift has source populations'),
        ('label_lift.py', 'plus[j][i] * plus[i][j]', 'plus[j][i] * eb_output[i][j]',
         'same interference measurement separates lifts'),
        ('label_lift.py', '(x + 2)**5', '(x - 2)**5',
         'source spectrum reconstructed, including five NEGATIVE modes'),
        ('spinor_symmetry.py', 's.zeros(16))/len(orbit)', 's.zeros(16))/(len(orbit)+1)',
         'exact orbit twirl band multiplier'),
        ('context_instrument.py', 'b[i//4,j//4]*gram[i,j]/7', 'b[i//4,j//4]*gram[i,j]/6',
         'conditional transition stochastic'),
        ('context_instrument.py', 'depol = 3*s.eye(16)/7', 'depol = 2*s.eye(16)/7',
         'quantum shadow closes EXACTLY'),
        ('context_instrument.py', 'record_rotation[j,k]*kraus_random[k]', 'int(j == k)*kraus_random[k]',
         'source record rotation turns reflection Kraus operators into projectors'),
        ('record_composition.py', 'branches = [clean(d[k]*c[j])', 'branches = [clean(c[j]*d[k])',
         'two actual unitary couplings produce the ordered selective branches'),
        ('record_composition.py', 'twice = u*once', 'twice = once',
         'coherent register reuse undoes instead of repeating the channel'),
        ('record_composition.py', 'crossed = phase_gate((0,3))*phase_gate((1,2))', 'crossed = phase_gate((0,3))',
         'equality coupling is two crossed CZ gates plus local Clifford phases'),
    ]
    rejected = []
    for name, old, new, error in mutations:
        path = HERE / name
        raw = path.read_text()
        if raw.count(old) != 1:
            raise ValueError('mutation is not narrowly targeted: ' + old)
        mutant = '__file__ = ' + repr(str(path)) + '\n' + raw.replace(old, new)
        run = subprocess.run([sys.executable, '-B', '-OO', '-c', mutant],
                             capture_output=True, text=True, timeout=60)
        if run.returncode == 0 or error not in run.stderr:
            raise ValueError('mutation failed to trigger expected guard: ' + error)
        rejected.append({'script': name, 'guard': error, 'exit_code': run.returncode})
    print(json.dumps({'scope': 'NON-RH finite compiler-origin audit',
                      'audits': results, 'rejected_mutations': rejected,
                      'total_checks_per_mode': sum(r['result']['checks'] for r in results.values()),
                      'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
