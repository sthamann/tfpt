"""Exact comparison of the existing v395 family transfer, not a cosmic model."""
import json
from pathlib import Path
import sympy as s

# Exact rational expression printed by the original _family_M constructor.
M=s.Matrix([[1,0,0],[0,s.Rational(1,2),s.Rational(1,6)],
            [0,s.Rational(1,6),s.Rational(1,2)]])
checks={
    'original_family_eigenvalues': M.eigenvals()=={s.Integer(1):1,s.Rational(2,3):1,s.Rational(1,3):1},
    'transfer_is_not_unitary': M.T*M != s.eye(3),
    'determinant_two_ninths': M.det()==s.Rational(2,9),
    'symmetric_eigenline_two_thirds':M*s.Matrix([0,1,1])==s.Rational(2,3)*s.Matrix([0,1,1]),
    'antisymmetric_eigenline_one_third':M*s.Matrix([0,1,-1])==s.Rational(1,3)*s.Matrix([0,1,-1]),
}
if not all(checks.values()):raise RuntimeError(checks)
out={
 'result_id':'GENESIS20261103', 'checks':checks,
 'spectrum':['1','2/3','1/3'],
 'conditional_Euclidean_log_spectrum':['0','log(3/2)/tau','log(3)/tau'],
 'exact_period_obstruction':'If log(3/2)/log(3)=m/n with n>0, then 3**(n-m)=2**n, impossible by unique prime factorization. This is an analytic proof, not a numeric irrationality test.',
 'scope':'Only the supplied original v395 family transfer. No identification with the full physical TFPT Hamiltonian and no exclusion of general cyclic cosmology.',
}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
