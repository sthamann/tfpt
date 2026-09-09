"""Exact countermodels for screenshot claims; no physical or RH construction."""
import hashlib
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
checks = {}


def need(name, condition):
    if not bool(condition):
        raise RuntimeError(name)
    checks[name] = True


I = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -s.I], [s.I, 0]])
Z = s.diag(1, -1)
J = s.Matrix([[0, -1], [1, 0]])
a, b, c, d, t = s.symbols('a b c d t', real=True)
H = s.Matrix([[a, c+s.I*d], [c-s.I*d, b]])
# Actual sheet swap is X, whereas parity grading is Z.
odd_swap = s.simplify(X*H*X+H)
need('swap_odd_general_solution', s.solve(list(odd_swap), [b, c]) == {b: -a, c: 0})
need('diagonal_H_is_swap_odd', X*Z*X == -Z)
evolution = s.diag(s.exp(-s.I*t), s.exp(s.I*t))
need('no_inter_sheet_transition', evolution[1, 0] == 0)
F = s.Matrix([[1, 1], [1, -1]])/s.sqrt(2)
need('parity_basis_diagonalizes_swap', F.T*X*F == Z)
need('same_diagonal_H_is_offdiagonal_in_parity_basis', F.T*Z*F == X)
need('pure_hopping_can_be_swap_even', X*X*X == X)
need('holomorphic_minus_identity_commutes_J', (-I)*J*(-I) == J)
need('antiholomorphic_reflection_reverses_J', Z*J*Z == -J)
need('J_squared_minus_identity', J**2 == -I)
Q = Z*J
need('Clifford_product_is_symmetric', Q.T == Q)
need('Clifford_product_square_is_trivial', Q**2 == I)
need('Clifford_product_is_odd', Z*Q*Z == -Q)
# A scalar complex phase is not this real complex structure.
need('linear_operator_cannot_reverse_central_i', Z*(s.I*I)*Z == s.I*I)
need('complex_conjugation_reverses_central_i', (s.I*I).conjugate() == -s.I*I)

# Exact partner spectra, including the missing zero eigenvalue.
A = s.Matrix([[1, 0], [0, 2], [0, 0]])
D = s.BlockMatrix([[s.zeros(3), A], [A.T, s.zeros(2)]]).as_explicit()
G = s.diag(1, 1, 1, -1, -1)
need('rectangular_selfadjoint_odd', D.T == D and G*D*G == -D)
need('square_block_formula', D**2 == s.diag(A*A.T, A.T*A))
need('partners_differ_at_zero', (A*A.T).eigenvals() == {1: 1, 4: 1, 0: 1} and (A.T*A).eigenvals() == {1: 1, 4: 1})
need('square_not_probability', (D**2).trace() == 10)
need('different_roots_same_square', X**2 == Y**2 and X != Y and X != -Y)

# Sharp finite imbalance bound and its consequence for a compact RH readout.
A16 = s.zeros(12, 4)
for k in range(4):
    A16[k, k] = k+1
D16 = s.BlockMatrix([[s.zeros(12), A16], [A16.T, s.zeros(4)]]).as_explicit()
G16 = s.diag(*([1]*12+[-1]*4))
need('12_4_odd_rank_bound_sharp', G16*D16*G16 == -D16 and D16.rank() == 8)
need('12_4_at_least_eight_zero_modes', len(D16.nullspace()) == 8)
T = (s.eye(16)+D16**2/4).inv()
need('compact_readout_eight_unit_eigenvalues', T.eigenvals()[s.Integer(1)] == 8)
need('zero_modes_can_be_invisible_to_selected_vector', (T**3)[0, 0] == s.Rational(4, 5)**3)
# If an invertible J anticommutes with G then J bijects the two eigenspaces.
# This rank obstruction excludes J^2=-I on the entire 12+4 carrier.
need('involution_imbalance', s.trace(G16) == 8)

z = s.symbols('z')
need('even_determinant_can_have_off_line_roots', (I+z*X).det() == 1-z**2)
root = s.Rational(1, 4)
need('scaled_even_pencil_counterexample', (I+4*root*X).det() == 0)

out = {
    'scope': 'Exact finite countermodels and identities; no TFPT dynamics, RH proof or factorization advantage',
    'checks': checks,
    'passed': len(checks),
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'sympy_version': s.__version__,
}
(HERE/'results.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
