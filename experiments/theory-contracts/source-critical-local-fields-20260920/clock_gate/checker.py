"""Exact gate for the existing critical n/z candidate and fixed clock lifts.

No new Hamiltonian is fitted. Tests concern fixed Y and the previously chosen
10D lifts, not every possible physical implementation of the native clocks.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
BASE = Path('/Users/stefanhamann/Documents/Codex/2026-09-19/h')
REPO = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
PINS = HERE / 'source_pins.json'
if not PINS.exists():
    raise RuntimeError('source_pins.json must be frozen before replay')
pins = json.loads(PINS.read_text())
for name, expected in pins.items():
    if hashlib.sha256(Path(name).read_bytes()).hexdigest() != expected:
        raise RuntimeError('source changed: ' + name)
prior = json.loads((BASE / 'outputs/TFPT_Gemeinsame_Quelle_Fortsetzung_2026-09-20/joint/gauge_section.json').read_text())
checks = {}

def require(condition, name):
    checks[name] = bool(condition)
    if not condition:
        raise RuntimeError(name)

def scalar(x):
    return x[0]

K = s.diag(*([1] * 9 + [-1]))
n = s.Matrix([1, 1, 1, -1, -1, -1, -1, -1, -1, 3])
z = s.eye(10)[:, 8] - s.eye(10)[:, 9]
a = n[:8, 0]
u, v = (n + z) / 2, (n - z) / 2
Y = s.Matrix([s.Rational(-1, 3)] * 3 + [s.Rational(1, 2)] * 2 + [0] * 3 + [1, 1])
q = s.ones(10, 1)
Vc = K + 2 * K * v * v.T * K
eR, m = -s.eye(10)[:, 8], n + s.eye(10)[:, 8]

def T(p):
    k = scalar(a.T * p) / 2
    return s.Matrix(list(p) + [-k, k])

def F(p):
    return T(p) - scalar(a.T * p) * n / 2

require(scalar(n.T*K*n) == scalar(z.T*K*z) == 0, 'two self-null competitors')
require(scalar(n.T*K*z) == 2, 'noncommuting null competitors')
require(scalar(Y.T*n) == scalar(Y.T*z) == scalar(q.T*n) == scalar(q.T*z) == 0, 'original q and Y neutral competitors')
require(scalar(u.T*K*u) == 1 and scalar(v.T*K*v) == -1 and scalar(u.T*K*v) == 0, 'neutral chiral coordinates')
require(Vc.eigenvals() == {s.Integer(1): 8, 7-4*s.sqrt(3): 1, 7+4*s.sqrt(3): 1}, 'positive selected critical metric')
require(scalar(n.T*Vc*n)/2 == scalar(z.T*Vc*z)/2 == 1, 'two dimension-one cosines')
require(z == F(-a) - eR - 3*m, 'competitor in prior E8 coframe')

native_path = REPO / 'experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json'
native = json.loads(native_path.read_text())['clock_matrices']
results = {}
for name, order in [('C', 30), ('J', 4)]:
    S = s.Matrix(prior['new_full_clock_lifts'][name])
    A = s.Matrix(native[name]['vector'])
    require(S**order == s.eye(10), name + ' fixed lift order')
    require(S*n == n and S*eR == eR and S*m == m and S.T*K*S == K, name + ' fixed pair and statistic metric')
    require(all(S*F(s.eye(8)[:, i]) == F(A*s.eye(8)[:, i]) for i in range(8)), name + ' actual native action intertwines')
    xs = [S**k*z for k in range(order)]
    require(len({tuple(x) for x in xs}) == order, name + ' full oriented competitor orbit')
    require(all(x != -z for x in xs), name + ' orbit has no minus original competitor')
    metric_powers = [k for k in range(order) if (S**k).T*Vc*S**k == Vc]
    cosine_powers = [k for k, x in enumerate(xs) if x == z or x == -z]
    q_values = [scalar(q.T*x) for x in xs]
    y_values = [scalar(Y.T*x) for x in xs]
    require(metric_powers == [0], name + ' only identity power preserves selected energy')
    require(cosine_powers == [0], name + ' only identity power preserves z cosine')
    require([k for k, y in enumerate(y_values) if y == 0] == [0], name + ' every other orbit vertex has nonzero fixed hypercharge')
    pairings = set()
    for k in range(order):
        require(xs[k] == F(-A**k*a) - eR - 3*m, name + ' orbit coframe formula ' + str(k))
        require(scalar(xs[k].T*K*xs[k]) == 0, name + ' self-null orbit ' + str(k))
        for ell in range(k+1, order):
            dot = scalar(xs[k].T*K*xs[ell])
            difference = A**k*a - A**ell*a
            require(dot == -scalar(difference.T*difference)/2 and dot < 0,
                    name + ' distinct orbit not mutually null ' + str(k) + ' ' + str(ell))
            pairings.add(dot)
    results[name] = {
        'order': order, 'q_by_power': [str(t) for t in q_values],
        'Y_by_power': [str(t) for t in y_values],
        'energy_preserving_powers': metric_powers,
        'z_cosine_preserving_powers': cosine_powers,
        'distinct_off_diagonal_K_pairings': [str(t) for t in sorted(pairings)]}

# This is a pair-only dressing statement; it is NOT a no-go for odd neutral
# operators elsewhere in the full lattice (the family vector supplies some).
Aaux, Baux = s.symbols('Aaux Baux', integer=True)
pair = Aaux*eR + Baux*m
require(scalar(Y.T*pair) == Baux-Aaux, 'pair-only hypercharge')
require(s.simplify(scalar(q.T*pair) - (Baux-Aaux)) == 0, 'pair-only microscopic number')
require(scalar(q.T*pair).subs(Baux, Aaux) == 0, 'Y-neutral pair-only dress is parity even')

# Actual charge Cartans in the common T embedding and their difference from
# the native F embedding on the complete lattice.
y8 = Y[:8, 0]
require(K*T(s.ones(8, 1)) == q, 'q is common T Cartan')
require(K*T(y8) == Y, 'Y is common T Cartan')
require(F(y8) == T(y8)+n, 'native F Cartan differs on nonzero n pairing')

result = {
    'research_verdict': 'PARTIAL',
    'mathematical_verdict': 'EXACT_FIXED_LIFT_CRITICAL_COMPATIBILITY_TEST',
    'checks': checks, 'passed': sum(checks.values()), 'total': len(checks),
    'clock_results': results,
    'neutral_pair_only_odd_dressing_exists': False,
    'source_derived_critical_selection': False,
    'complete_TFPT_solution': False,
    'scope': 'Existing selected Vc, n/z, original fixed Y, and previous 10D clock lifts. All-pair orbit check is finite and exact. No conclusion against a different physical realization or clocks that are not symmetries of this selected Hamiltonian.',
    'source_pins': pins}
(HERE / 'certificate.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
print(json.dumps({k: result[k] for k in ['mathematical_verdict', 'passed', 'total']}))
