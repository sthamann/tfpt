"""One exact implication test on the existing TFPT source and native clock.

Question: if the actual native sigma is an active operation on the SAME
local source fibre, does closing the original D8 source under it force the
marked extension? No primitive source realization of sigma is assumed proven.
"""

import ast
import hashlib
import json
from pathlib import Path
import sys

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

REPO = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
HERE = Path(__file__).resolve().parent
FOLD = REPO / 'experiments/theory-contracts/v16-operator-pullback-20261014/fold-results.json'
NATIVE = REPO / 'verification/v634_st31_structure.py'
CURRENT = REPO / 'tfpt_explorer/current_block_geometry.py'
sys.path.insert(0, str(REPO))
from tfpt_explorer.current_block_geometry import _actual_current_source


def ints(matrix):
    assert all(x.q == 1 for x in matrix)
    return sp.Matrix(matrix.rows, matrix.cols, [sp.Integer(x) for x in matrix])


def vector(values):
    return [str(x) for x in values]


native_ast = ast.parse(NATIVE.read_text())
sigma_idx = next(ast.literal_eval(n.value) for n in native_ast.body
                 if isinstance(n, ast.Assign)
                 and any(isinstance(t, ast.Name) and t.id == 'SIGMA_IDX'
                         for t in n.targets))
assert sigma_idx == [4, 5, 0, 1, 2, 3, 6, 7]
M = sp.Matrix(json.loads(FOLD.read_text())['explicit_Weyl_matrix'])
Sigma = sp.eye(8)[sigma_idx, :]
R = M.T * Sigma * M
assert M.T*M == sp.eye(8)
assert R.T*R == sp.eye(8) and R**3 == sp.eye(8)

# A standard source D8 basis, with determinant two in the ORIGINAL source
# Euclidean pairing. No E8 root list is used in this lattice calculation.
B = sp.zeros(8)
for j in range(7):
    B[j, j] = 1
    B[j+1, j] = -1
B[6, 7] = B[7, 7] = 1
assert B.det() == 2
H = hermite_normal_form(ints((2*B).row_join(2*R*B)))
Basis = H/2
Gram = Basis.T * Basis
assert all(x.q == 1 for x in Gram)
assert all(Gram[i, i] % 2 == 0 for i in range(8))
assert Gram.det() == 1
assert all(x.q == 1 for x in H.inv()*R*H)
assert abs(B.det()/Basis.det()) == 2

s = sp.ones(8, 1)/2
assert s.dot(s) == 2
assert all(x.q == 1 for x in Basis.inv()*s)
# Identify the lattice directly with D8 + Zs, avoiding even-unimodular
# classification as an additional input.
Hmarked = hermite_normal_form(ints((2*B).row_join(2*s)))
assert Hmarked == H

# The shortest explicit source-relative generation word is one clock
# action followed by one existing D8-current bracket.
p = sp.eye(8)[:, 0] + sp.eye(8)[:, 2]
delta = sp.eye(8)[:, 2] + sp.eye(8)[:, 4]
charged = R*p
assert all(x.q == 1 for x in B.inv()*p)
assert all(x.q == 1 for x in B.inv()*delta)
assert charged + delta == s and charged.dot(delta) == -1
assert charged.dot(charged) == delta.dot(delta) == 2

# Check the nonzero signed OPE in the ACTUAL original Chevalley code;
# this is separate from, and unnecessary for, the lattice identification.
source = _actual_current_source()
alg = source['chevalley']
target_p = tuple(int(x) for x in 2*M*p)
target_charged = tuple(int(x) for x in 2*M*charged)
target_delta = tuple(int(x) for x in 2*M*delta)
target_s = tuple(int(x) for x in 2*M*s)
bracket = alg.bracket(alg.ridx[target_delta], alg.ridx[target_charged])
assert set(bracket) == {alg.ridx[target_s]}
coefficient = bracket[alg.ridx[target_s]]
assert coefficient in (-1, 1)

result = {
    'verdict': 'PASS_CONDITIONAL_ACTIVE_COMMON_FIBRE_CLOCK_COMPLETION',
    'first_unproved_bridge': (
        'An active operation on the same original local source field fibre '
        'implements the actual native sigma through R=M^T sigma M, with '
        'the required conformal, state, reflection and physical-time dictionary. '
        'Passive chart/background transport alone does not imply closure.'
    ),
    'source_clock_R': [[str(x) for x in row] for row in R.tolist()],
    'native_sigma_indices': sigma_idx,
    'source_clock_order': 3,
    'source_clock_is_orthogonal': True,
    'twice_completion_HNF_basis': [[int(x) for x in row] for row in H.tolist()],
    'D8_Gram_determinant': int((B.T*B).det()),
    'completion_Gram_determinant': int(Gram.det()),
    'completion_is_integral_even': True,
    'completion_index_over_D8': 2,
    'completion_R_stable': True,
    'exact_lattice_identification': 'D8 + Z*(q/2), q=(1,1,1,1,1,1,1,1)',
    'q_half_HNF_coordinates': vector(Basis.inv()*s),
    'explicit_generation_word': {
        'source_even_p': vector(p),
        'source_Rp': vector(charged),
        'source_even_delta': vector(delta),
        'source_Rp_plus_delta': vector(s),
        'inner_product_Rp_delta': str(charged.dot(delta)),
        'target_p_doubled': list(target_p),
        'target_sigma_p_doubled': list(target_charged),
        'target_delta_doubled': list(target_delta),
        'target_q_half_doubled': list(target_s),
        'actual_Chevalley_bracket_coefficient': str(coefficient),
    },
    'marking_changes_under_R': vector(R*sp.ones(8, 1)),
    'fixed_background_symmetry_not_asserted': True,
    'neutral_fixed_point_escape': (
        'B^Z2=A and omega_B=omega_A o E reproduce every complete even '
        'word already identified in B, including charged intermediates. '
        'No demand that individual charged fields be A observables follows.'
    ),
    'originality': (
        'General active-clock forces current completion principle reused from '
        'compiler-clock-current-closure-20260919/PROOF.txt and its source audit; '
        'extension/OPE completion machinery reused. New exact source-relative '
        'synthesis is the original-M native-clock HNF computation and the '
        'one-clock one-bracket word producing the marked q/2 current. '
        'It is not an original primitive P1 sigma derivation.'
    ),
    'sources': {
        str(path.relative_to(REPO)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in (FOLD, NATIVE, CURRENT,
                     REPO/'experiments/theory-contracts/compiler-clock-current-closure-20260919/PROOF.txt',
                     REPO/'experiments/theory-contracts/compiler-clock-current-closure-20260919/source_origin_audit.txt')
    },
}
(HERE/'actual-clock-completion-results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
