"""Exact bounded forward tests; no H70 target coefficients are inputs.

Run: python3 -B check.py (also under -OO). No file writes.
Source: compiler-cone-object-audit/ORDER_PROOF.md, sections 1 and 3.
These tests concern a declared two-dimensional representation, not all TFPT.
"""
import json
from pathlib import Path
import hashlib
import sympy as s

checks = []


def equal(name, actual, expected):
    delta = actual - expected
    ok = all(s.simplify(x) == 0 for x in delta) if isinstance(delta, s.MatrixBase) else s.simplify(delta) == 0
    if not ok:
        raise RuntimeError(name)
    checks.append(name)


I = s.eye(2)
u1 = s.diag(s.I, -s.I)
u2 = s.Matrix([[0, 1], [-1, 0]])
u3 = u1 * u2
w = (I + u1 + u2 + u3) / 2


def defect(U, phase=1):
    R = U - phase * I
    return s.simplify(R.H * R)


for j, u in enumerate([u1, u2, u3], 1):
    equal(f'u{j}_unitarity', u.H * u, I)
    equal(f'u{j}_square', u * u, -I)
    equal(f'u{j}_identity_defect', defect(u), 2 * I)
    equal(f'u{j}_minus_identity_defect', defect(u, -1), 2 * I)
equal('w_unitarity', w.H * w, I)
equal('w_cubic_lift', w**3, -I)
equal('quaternion_commutator_central_minus', u1*u2*u1.H*u2.H, -I)
equal('w_identity_defect', defect(w), I)
equal('w_minus_identity_defect', defect(w, -1), 3 * I)
equal('four_equal_defects', sum((defect(u) for u in [u1, u2, u3, w]), s.zeros(2)), 7 * I)

# A non-real character selects a direction but is extra declared input.
equal('phase_i_u1_selects_first_axis', defect(u1, s.I), s.diag(0, 4))
equal('phase_i_u2_nonidentical', defect(u2, s.I), 2 * I + 2 * s.I * u2)
equal('distinct_selected_projectors', s.trace(((I - s.I*u1)/2) * ((I - s.I*u2)/2)), s.Rational(1, 2))

# Exact commutant: preserving both primitive actions leaves only scalars.
basis = [s.Matrix([[1,0],[0,0]]), s.Matrix([[0,1],[0,0]]),
         s.Matrix([[0,0],[1,0]]), s.Matrix([[0,0],[0,1]])]
columns = []
for B in basis:
    columns.append(s.Matrix(list(B*u1-u1*B) + list(B*u2-u2*B)))
comm = s.Matrix.hstack(*columns)
equal('commutant_rank_three', comm.rank(), 3)
equal('identity_in_commutant', comm*s.Matrix([1,0,0,1]), s.zeros(8,1))

# Independently declared two-rule control from the ChatGPT research reports.
C = s.diag(1, s.I)
X = s.Matrix([[0, 1], [1, 0]])
d = (I-C).col_join(I-X)
Q = s.simplify(d.H*d)
equal('two_rule_positive_control', Q, s.Matrix([[2,-2],[-2,4]]))
equal('positive_control_determinant', Q.det(), 4)

# Whitening removes dependence on row redundancy, but all singular values.
equal('canonical_gram_normalization', s.simplify(d.H*(d*d.H).pinv()*d), I)
duplicate = d.col_join(I-C)
equal('duplicate_changes_raw_form', duplicate.H*duplicate, s.Matrix([[2,-2],[-2,6]]))
equal('duplicate_whitened_form', s.simplify(duplicate.H*(duplicate*duplicate.H).pinv()*duplicate), I)
rank_one = s.Matrix([[1, 0], [2, 0]])
equal('rank_deficient_control', rank_one.H*(rank_one*rank_one.H).pinv()*rank_one, s.diag(1,0))

# Regularization preserves a selected direction, but restores a free scale.
for lam in [s.Rational(1, 2), s.Integer(1), s.Integer(2)]:
    left = s.simplify(d.H*(d*d.H+lam*s.eye(d.rows)).inv()*d)
    right = s.simplify(Q*(Q+lam*I).inv())
    equal(f'regularized_identity_{lam}', left, right)

source = Path(__file__).resolve().parents[1]/'compiler-cone-object-audit'/'ORDER_PROOF.md'
print(json.dumps({
    'status': 'BOUNDED_FORWARD_CANDIDATES_REJECTED',
    'checks_passed': len(checks), 'checks': checks,
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'target_couplings_used': False,
    'primitive_measure_derived': False,
    'H70_forward_reconstruction_performed': False,
    'all_TFPT_selection_mechanisms_excluded': False,
}, sort_keys=True, indent=2))
