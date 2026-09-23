"""Exact stabilizer equations for the stated one-background covariance theorem.

The group-transitivity step is proved in ONE_BACKGROUND.md. This script
checks the finite linear algebra; it does not assert the theorem's physical
premises for the complete TFPT source.
"""
from pathlib import Path
import json
import sympy as s

HERE = Path(__file__).resolve().parent
checks = {}

def require(condition, label):
    checks[label] = bool(condition)
    if not condition:
        raise RuntimeError(label)

z = s.symbols('z0:9')
F = s.Matrix(3, 3, z)
eps = s.Matrix([[0, 1], [-1, 0]])
# Two genuine SU(2) matrices already force the claimed invariant subspace.
generators = [s.diag(s.I, -s.I, 1), s.diag(eps, 1)]
equations = []
for g in generators:
    require(g.det() == 1 and g.conjugate().T*g == s.eye(3), 'stabilizer unitary determinant one '+str(len(equations)))
    require(g*s.Matrix([0, 0, 1]) == s.Matrix([0, 0, 1]), 'stabilizer fixes e3 '+str(len(equations)))
    equations.extend(list(g.conjugate()*F*g.conjugate().T-F))
solution = list(s.linsolve(equations, z))
expected = (0, -z[3], 0, z[3], 0, 0, 0, 0, z[8])
require(solution == [expected], 'stabilizer leaves exactly epsilon2 and singlet scalar')
restricted = F.subs(dict(zip(z, expected)))
# t=pi/2 suffices to force the singlet coefficient to zero.
u = (1-s.I)/s.sqrt(2)
g = s.diag(u, u, s.I)
require(s.simplify(g.det()) == 1 and s.simplify(g.conjugate().T*g) == s.eye(3), 'phase compensating matrix is SU3')
require(g*s.Matrix([0, 0, 1]) == s.I*s.Matrix([0, 0, 1]), 'phase compensating matrix sends h to i h')
phase_residual = s.simplify(g.conjugate()*restricted*g.conjugate().T-s.I*restricted)
require(phase_residual == s.diag(0, 0, -(1+s.I)*z[8]), 'correct degree eliminates the singlet block')

h = s.Matrix(s.symbols('h1:4'))
A = s.Matrix([[0,h[2],-h[1]],[-h[2],0,h[0]],[h[1],-h[0],0]])
require(A*h == s.zeros(3,1) and A.det() == 0, 'family kernel and determinant exactly zero')
require(A.rank() == 2, 'generic nonzero coefficient has rank two')
conj_h = s.Matrix(s.symbols('barh1:4'))
R = conj_h*conj_h.T
require((-s.I*conj_h)*(-s.I*conj_h).T == -R, 'conjugate rank one covariant has phase degree minus two')
require(-R != s.I*R, 'rank one complement violates required Higgs phase degree')

result = {
    'status': 'PASS_EXACT_STABILIZER_ALGEBRA',
    'research_verdict': 'CONDITIONAL',
    'checks': checks, 'passed': sum(checks.values()), 'total':len(checks),
    'theorem': 'F(h)=f(h_dagger_h)*epsilon*h under SU3 covariance and phase degree +1; rank at most two',
    'premises': ['one nonzero family vector h only', 'exact SU3 covariance with two conjugate fundamental coefficient indices', 'Higgs U1 degree +1', 'no additional tensor or oriented background'],
    'analyticity_required': False,
    'complete_source_satisfies_premises': 'NOT_ASSERTED',
    'full_TFPT_no_go': False,
    'physical_gates_closed': []
}
(HERE/'one_background.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':result['status'],'passed':result['passed'],'total':result['total']}))
