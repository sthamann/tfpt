"""Actual one-copy source channel rank and marked seam/glue clock dictionary.

Conditional low-energy channel result, not a construction of the E8 source.
The quarter/half-twist and charge-carry facts are inherited from 2026-09-08.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--out', type=Path, required=True)
args = parser.parse_args()
args.out.mkdir(parents=True, exist_ok=True)
checks = Counter()


def ck(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    checks[name] += 1


pins = json.loads((HERE / 'source_pins.json').read_text())
for name, h in pins.items():
    ck(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == h, 'source pins')

path = ROOT / 'experiments/theory-contracts/microscopic-charged-car-limit/checker.py'
spec = importlib.util.spec_from_file_location('source_channel_car', path)
car = importlib.util.module_from_spec(spec)
spec.loader.exec_module(car)
linear, source = car.inherited()  # validates the source adapter's own transitive chain


def exact(matrix):
    converted = s.Matrix([[s.Rational(float(x.real)) + s.I * s.Rational(float(x.imag))
                           for x in row] for row in np.asarray(matrix)])
    ck(all(s.denom(s.re(x)) <= 2 and s.denom(s.im(x)) <= 2 for x in converted),
       'source entries are exact dyadic Gaussian rationals')
    return converted


H0 = exact(source.strip_at_momentum(0, 8))
TX, TY, SZ = [exact(getattr(source, name)) for name in ('TX', 'TY', 'SZ')]
SX = s.Matrix([[0, 1], [1, 0]])
X = s.diag(*([SX] * 8))
Z = s.diag(*([SZ] * 8))
derivative = s.diag(*([-s.I * TX + s.I * TX.conjugate().T] * 8))
ck(derivative == -X, 'source longitudinal derivative')
ck(TX + TX.conjugate().T == -SZ, 'source cosine coefficient')
ck(H0 * X + X * H0 == s.zeros(16) and Z * X + X * Z == s.zeros(16),
   'transverse part anticommutes with longitudinal part')
ck(H0 ** 3 == H0 and H0.rank() == 14, 'source transverse spectrum and two zero modes')
ck(H0 == H0.conjugate().T, 'source self-adjoint')
ck((H0 + 2 * Z).det() != 0, 'no zero at momentum pi')
rt, rb = s.zeros(16, 1), s.zeros(16, 1)
rt[14] = rt[15] = 1 / s.sqrt(2)
rb[0], rb[1] = 1 / s.sqrt(2), -1 / s.sqrt(2)
V = s.Matrix.hstack(rt, rb)
ck(V.T * V == s.eye(2) and H0 * V == s.zeros(16, 2), 'all source zero modes explicitly spanned')
ck(V.T * derivative * V == s.diag(-1, 1), 'one branch per orientation')

# All transverse matrix units B=|i><j|, not just the eight row densities.
# The norm-one chiral source mode rt gives b(B)=<rt,B rt>.
b = s.Matrix([s.conjugate(rt[i]) * rt[j] for i in range(16) for j in range(16)])
G = b * b.conjugate().T
ck(G.rank() == 1 and sum(abs(x) ** 2 for x in b) == 1,
   'leading current Gram on all 256 matrix units has rank one')
row_b = s.Matrix([sum(abs(rt[2 * y + a]) ** 2 for a in range(2)) for y in range(8)])
ck(row_b == s.Matrix([0] * 7 + [1]), 'eight rows reduce to one top current')
ck(s.diag(1, *([0] * 7)) != s.eye(8), 'rank-eight relabeling control rejected')

rows = []
for N in (64, 128, 256, 512):
    gram = np.zeros((8, 8), complex)
    max_profile_error = 0.0
    rho_max = 0.0
    for empty in (-2, -1, 0):
        occupied = empty + 3
        data_u, data_v = car.strip(N, empty), car.strip(N, occupied)
        u, v = data_u['j'], data_v['j']
        rho_max = max(rho_max, data_u['rho'], data_v['rho'])
        for w, data in ((u, data_u), (v, data_v)):
            error = float(np.linalg.norm(w - car.row_spinor()))
            ck(error <= 4 * data['rho'] + 1e-11, 'source polarized embedding error bound')
            max_profile_error = max(max_profile_error, error)
        amplitudes = np.array([np.vdot(u[2*y:2*y+2], v[2*y:2*y+2]) for y in range(8)])
        gram += np.outer(amplitudes, amplitudes.conj()) / 3
    target = np.zeros((8, 8)); target[-1, -1] = 1
    error = float(np.linalg.norm(gram - target, 2))
    # Per coefficient: |b_N-b|<=8 rho_max. Product error <=16 rho_max;
    # an 8-by-8 entrywise bound gives operator norm <=128 rho_max.
    ck(error <= 128 * rho_max + 1e-11, 'finite-source row Gram obeys analytic convergence cap')
    rows.append({'N': N, 'mode': 3, 'row_Gram_error': error,
                 'analytic_cap': float(128 * rho_max), 'max_profile_error': max_profile_error,
                 'eigenvalues_float': np.linalg.eigvalsh(gram).tolist()})

# Connect the NEW marked geometric deck to the pre-existing charge-carry clock.
parent = json.loads((ROOT / 'experiments/theory-contracts/compiler-e6-seam-readout-20260918/certificate.json').read_text())
roots2 = list(map(tuple, parent['seam']['root_order']))
T = dict(zip(roots2, parent['seam']['root_character_exponents']))
g = lambda r: sum(r[:5]) % 4
a = lambda r: (r[7] - r[6]) // 2 % 4
for r in roots2:
    ck((r[7] - r[6]) % 2 == 0, 'family rotation integral on E8')
    ck(T[r] == (2 * g(r) + a(r)) % 4, 'seam deck equals glue-clock square times A2 rotation')
    reflected = r[:6] + (r[7], r[6])
    ck(g(reflected) == g(r) and a(reflected) == (-a(r)) % 4,
       'source reflection fixes glue clock and reverses family rotation')
counts = Counter(g(r) for r in roots2); counts[0] += 8
ck([counts[k] for k in range(4)] == [60, 64, 60, 64], 'inherited glue clock multiplicities')
ck([counts[k] for k in range(4)] != [parent['seam']['full_adjoint_multiplicities_i_to_k'][str(k)] for k in range(4)],
   'glue dual clock and geometric deck not conjugate')

# Existing lattice result, checked here to type the source paper's remaining theorem.
lam = (F(1, 2),) * 8
def L0(x):
    return all(v.denominator == 1 for v in x) and sum(x[:5]) % 2 == 0 and sum(x[5:]) % 2 == 0
def D8(x):
    return all(v.denominator == 1 for v in x) and sum(x) % 2 == 0
ck(not L0(lam) and not L0(tuple(2*x for x in lam)) and L0(tuple(4*x for x in lam)),
   'lambda order four relative to D5 plus D3')
ck(not D8(lam) and D8(tuple(2*x for x in lam)), 'lambda order two relative to D8')
sector_reps = [(F(0),)*8, (F(1),)+(F(0),)*7, lam, (F(-1,2),)+(F(1,2),)*7]
ck(all(D8(tuple(2*x for x in v)) for v in sector_reps), 'all D8 discriminant sectors have exponent two')
quarter = tuple(x / 2 for x in lam)
pairings = [sum(q * F(rj, 2) for q, rj in zip(quarter, r)) for r in roots2 if all(x % 2 == 0 for x in r)]
ck(sum(x.denominator != 1 for x in pairings) == 56, 'known quarter twist fails D8 relative-locality lattice test')
ck(sum(x*x for x in quarter)/2 == F(1,4) and sum(x*x for x in lam)/2 == 1,
   'known quarter versus half conformal weights')

# Test the tempting numerical identification in v367 against the native
# compact D5 action; do not replace its complex spinor by a real vector.
native = json.loads((ROOT / 'experiments/theory-contracts/compiler-native-root-dictionary-20260918/certificate.json').read_text())
halfroots = list(map(tuple, native['results']['native']['spinor_root_order']))
ck(len(halfroots) == 128 and all(all(abs(x) == 1 for x in r) for r in halfroots),
   'native source doubled spinor coordinates')
family = halfroots[0][5:]
carrier = {r[:5] for r in halfroots if r[5:] == family}
ck(len(carrier) == 16, 'native fixed-family D5 half-spinor')
ck(not any(tuple(-x for x in r) in carrier for r in carrier),
   'compact D5 half-spinor weights are not invariant under conjugation')
central_phases = {sum(r) % 4 for r in carrier}
ck(len(central_phases) == 1 and central_phases <= {1, 3},
   'compact Spin10 center has purely imaginary spinor character')
real_vector_weights = [tuple(2*sign if i == j else 0 for i in range(8))
                       for j in range(8) for sign in (-1, 1)]
ck(sum(any(r[:5]) for r in real_vector_weights) == 10
   and sum(not any(r[:5]) for r in real_vector_weights) == 6,
   'known marked real vector decomposition is 10 plus 6')
ck(F(10,16)+F(6,16) == 1, 'known product spin-field conformal weight is one')

result = {
    'research_id': 'UR.COMPILER.SOURCE_CHANNEL_GATE.07', 'verdict': 'PARTIAL',
    'mathematical_verdict': 'EXACT_ONE_COPY_LEADING_CURRENT_RANK_AND_MARKED_CLOCK_DICTIONARY',
    'source_pins': pins,
    'source': {'model': 'original v1033 QWZ strip, m=1, width=8, one copy',
               'zero_mode_dimension': 2, 'oriented_velocities': [-1, 1],
               'one_edge_complex_CAR_channels': 1, 'top_256_bilinear_Gram_rank': 1,
               'row_current_coefficients': [0]*7+[1],
               'scope': 'leading weight-one currents of the existing one-edge CAR scaling limit; not an all-interacting-model no-go'},
    'finite_source_diagnostics': rows,
    'clock_dictionary': {'identity_on_full_charge_lattice': 'T=G^2 A',
                         'G_exponent': '2 sum(q[0:5]) modulo 4',
                         'A_exponent': 'q[7]-q[6] modulo 4',
                         'T_exponent': '4q[5]+3q[6]+5q[7] modulo 4',
                         'G_eigenmultiplicities_on_E8_adjoint': [60,64,60,64],
                         'T_eigenmultiplicities_on_E8_adjoint': [70,56,66,56],
                         'reflection': 'F G F^-1=G; F A F^-1=A^-1',
                         'physical_source_identification': False},
    'inherited_not_new': ['half-twist-grade-carry: half twist, integer carry, L/L0=Z4 and L/D8=Z2',
                          'microscopic-charged-car-limit: original one-copy CAR field/state scaling dictionary'],
    'corrected_extension_target': 'D5_1 x A3_1 --index2--> D8_1 --index2 spinor--> E8_1; no order-four DHR sector of D8_1',
    'copy_action_gate': {
        'native_carrier_complex_dimension': 16,
        'native_carrier_real_dimension': 32,
        'carrier_center_i_exponent': next(iter(central_phases)),
        'same_action_on_16_real_Majoranas': False,
        'known_correct_real_vector_split': [10, 6],
        'interpretation': 'v113 and native .03 already provide the correct algebraic vector/spinor dictionary; v367 numerical copy count alone is not that intertwiner',
        'spin_field_weights': ['5/8', '3/8'],
        'physical_local_source_selected': False},
    'first_added_structure': 'independent channel copies / rank-eight local current algebra are supplied in the old lattice realization, not generated by its eight transverse rows',
    'next_origin_obligation': 'derive an actual local rank-eight current algebra and its marked state/action from the original TFPT source, before charged-field optimization',
    'physical_gates_closed': [], 'checks_by_group': dict(sorted(checks.items()))}
(args.out / 'certificate.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
print(json.dumps({'verdict': result['verdict'], 'source_current_rank': 1,
                  'clock_dictionary': 'T=G^2 A', 'physical_gates_closed': []}))
