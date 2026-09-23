"""Checker 3 (v1.6.9 lift typing): the complete small recorded experiment on one carrier.

The carrier is the native common three-state space K3 = span{p0, R7, b0}
inside the channel-0 star of the byte-pinned in-repo W (no npz):

  p0 = |4,57> (seed pair, leaf 0),  R7 = (1/sqrt7) Sum_{q=1..7} s_q |p_q>
  (the seven remaining leaves of the same star),  b0 = the star boson.

  H3 = Delta B + g X3,  X3 = [[0,0,-1],[0,0,sqrt7],[-1,sqrt7,0]],
  B = diag(0,0,1),  Z_b = I - 2B = e^{i pi N_b} on K3,  E = diag(0,1/7,0)
  (the n5 readout effect compressed to K3).

COMPLETE EXPERIMENT, all guarded exactly (sympy, formal d = Delta/(2 Omega)
and c = cos(pi d)) and at the documented test point Delta=1, g=1/20
(numerisch, float64, tolerance 1e-14 against the symbolic values):

  * initial state: p0 (both arms identical);
  * operation sequences: free U.I.U vs impulse U.Z_b.U, tau = pi/(2 Omega),
    Omega^2 = Delta^2/4 + 8 g^2;
  * admissible readout: n5 (effect E); ALL outcome probabilities:
    P(n5=1), P(n5=0) in both arms (they sum to 1), the endpoint boson
    probabilities P(N_b) in both arms, and the midpoint boson probability;
  * recording on the same carrier: the neutral two-state pointer isometry
    V psi = (I-B) psi x |0> + B psi x |1> on K3 x C2, with its explicit
    unitary coupler C_R = exp(-i pi/2 B x (I - X_R)); V preserves the full
    joint Gram kernel (V^dagger V = I) and ALL pair coherences
    (V^dagger (O x I) V = O for pair-block operators O, including the
    off-diagonal coherence |p0><R7| + h.c.);
  * ignoring the pointer gives the real CPTP update (rho + Z_b rho Z_b)/2
    and EXACTLY half the follow-up effect: p_rec = (p_free + p_pulse)/2;
    the soft-record overlap eta interpolates (1-eta)/2 of the impulse signal;
  * work deposits: the impulse deposits Delta(1-d^2)/4 = Delta/54 and the
    recorder Delta(1-d^2)/8 = Delta/108 at the test point (d^2 = 25/27
    exactly);
  * instrument boundary: the terminal n5 Lueders back-action does NOT
    preserve K3: (n5 J - J E)^dagger(n5 J - J E) = diag(0, 6/49, 0)
    (documented v1.6.8 boundary, re-guarded on the native star).

An independent float64 matrix-exponential replay on the NINE-dimensional
native star built directly from W (no symbolic half-period formula used to
form the evolution) reproduces both arm probabilities and the six-dimensional
recorded process.

Runs under normal and -OO; all guards are explicit (no asserts).
"""
from pathlib import Path
from hashlib import sha256
import contextlib
import io
import json
import math
import runpy
import time

import numpy as np
import sympy as s
from scipy.linalg import expm

HERE = Path(__file__).resolve().parent
NS_PIN = '380577f85d2afa8b50f91a0991769eaf8267ee5c09f327d87f17e1b4c0af1672'
T0 = time.time()
checks = []


def need(ok, name, kind='exact'):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append((name, kind))


def equal(A, B, name):
    difference = A - B
    if isinstance(difference, s.MatrixBase):
        ok = all(s.simplify(x) == 0 for x in difference)
    else:
        ok = s.simplify(difference) == 0
    need(ok, name)


# ------------------------------------------------------- native star from W
need(sha256((HERE / 'native_source.py').read_bytes()).hexdigest() == NS_PIN,
     'native_source.py byte pin (copy of universalraum-operations-groundstate-20260915)')
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(HERE / 'native_source.py'))
W = ns['W']
PAIRS = ns['PAIRS']
need(ns['PINS']['W_sha256'] == '7a4a0b1c4401a20a84aee47b75f9b9d8882299bdff938ba11fd5b2bfe5656112',
     'reconstructed W tensor pin')
cols = list(map(int, np.flatnonzero(W[0])))
leaves = [PAIRS[k] for k in cols]
signs = [int(W[0, k]) for k in cols]
need(len(cols) == 8 and np.count_nonzero(W[1:, cols]) == 0, 'closed native eight-leaf star')
need(leaves[0] == (4, 57) and leaves[1] == (5, 56), 'same seed pair and receiver leaf as documented')
need(len(set(i for pair in leaves for i in pair)) == 16, 'sixteen disjoint star modes')
need(signs[0] == -1, 'sender leaf sign -1 (documented h3 convention)')

# ----------------------------------------------------- K3 operators, exact
Delta, g = s.symbols('Delta g', real=True, positive=True)
X = s.Matrix([[0, 0, -1], [0, 0, s.sqrt(7)], [-1, s.sqrt(7), 0]])
B = s.diag(0, 0, 1)
I = s.eye(3)
H = Delta * B + g * X
Z = I - 2 * B
E = s.diag(0, s.Rational(1, 7), 0)

# the 9-dimensional native star and the isometric K3 adapter (symbolic)
H9 = s.zeros(9)
sgn = s.Matrix(signs)
H9[:8, 8] = g * sgn
H9[8, :8] = g * sgn.T
H9[8, 8] = Delta
J = s.zeros(9, 3)
J[0, 0] = 1
J[8, 2] = 1
for q in range(1, 8):
    J[q, 1] = sgn[q] / s.sqrt(7)
equal(J.T * J, I, 'K3 adapter is isometric')
equal(H9 * J, J * H, 'native star Hamiltonian preserves K3 exactly')
B9 = s.diag(*([0] * 8), 1)
equal(B9 * J, J * B, 'total boson number preserves K3')
equal((s.eye(9) - 2 * B9) * J, J * Z, 'boson parity e^{i pi N_b} preserves K3 and equals I-2B there')
n5_9 = s.zeros(9)
n5_9[1, 1] = 1                      # leaf 1 = pair (5,56) contains receiver mode 5
equal(J.T * n5_9 * J, E, 'terminal receiver effect compresses to E = diag(0,1/7,0)')
lueders = ((n5_9 * J - J * E).H * (n5_9 * J - J * E)).applyfunc(s.simplify)
equal(lueders, s.diag(0, s.Rational(6, 49), 0),
      'instrument boundary: terminal n5 Lueders back-action leaves K3 (diag(0,6/49,0))')

# Z_b inside, old Z_4 outside the documented K3 control algebra
dark = I - X * X / 8
equal(dark * dark, dark, 'dark projector idempotent')
equal(s.trace(dark).simplify(), s.Integer(1), 'dark subspace one-dimensional')
equal(dark * X, s.zeros(3), 'X annihilates the dark direction')
equal(dark * B, s.zeros(3), 'N_b annihilates the dark direction')
equal(dark * Z - Z * dark, s.zeros(3), 'Z_b stays in the documented block algebra')
oldZ = s.diag(-1, 1, 1)             # the old single-mode impulse Z4 on K3
need(oldZ * dark - dark * oldZ != s.zeros(3), 'old single-mode Z4 lies outside the X,N_b algebra')
algebra_basis = [I, B, X, s.I * (B * X - X * B), X * X]
flatten = lambda A: s.Matrix(list(A))
algebra_matrix = s.Matrix.hstack(*map(flatten, algebra_basis))
need(algebra_matrix.rank() == 5, 'documented K3 control algebra has complex dimension five')
for a, Amat in enumerate(algebra_basis):
    for b, Bmat in enumerate(algebra_basis):
        need(algebra_matrix.row_join(flatten(Amat * Bmat)).rank() == 5,
             'control algebra multiplication closure ' + str((a, b)))
equal(s.diag(1, 1, s.exp(s.I * s.pi)), Z, 'Z_b equals e^{i pi N_b} on K3')

# ------------------------------------------- exact half-period propagator
d, r = s.symbols('d r', real=True)
u = s.symbols('u', nonzero=True)
bright = s.Matrix([-1, s.sqrt(7), 0]) / s.sqrt(8)
boson = s.Matrix([0, 0, 1])
Pbright = bright * bright.T
equal(Pbright + B + dark, I, 'bright / boson / dark decomposition')
U = dark + u * (s.I * d * Pbright - s.I * r * (bright * boson.T + boson * bright.T) - s.I * d * B)


def reduce(expression):
    return s.simplify(s.expand(expression).subs(r * r, 1 - d * d))


def dagger(A):
    return A.conjugate().T.subs(s.conjugate(u), 1 / u)


equal((dagger(U) * U).applyfunc(reduce), I, 'exact half-period propagator unitarity')

# ------------------------------------------------------- the two sequences
seed = s.Matrix([1, 0, 0])
midpoint = U * seed
free = (U * midpoint).applyfunc(reduce)
pulse = (U * Z * midpoint).applyfunc(reduce)
prob = lambda state, O: reduce((dagger(state) * O * state)[0])
c = s.symbols('c', real=True)
cos_identity = (u**2 + u**-2) / 2
p0 = (1 + c) / 32
p1 = (1 + (1 - 2 * d * d)**2 - 2 * (1 - 2 * d * d) * c) / 64
delta = -(1 - d * d) * (d * d + c) / 16
equal(prob(free, E), p0.subs(c, cos_identity), 'free-arm n5=1 probability')
equal(prob(pulse, E), p1.subs(c, cos_identity), 'impulse-arm n5=1 probability')
equal(p1 - p0, delta, 'unconditional delayed response formula')
# ALL outcome probabilities
equal(prob(free, I - E) + prob(free, E), s.Integer(1), 'free arm: n5 outcomes sum to one')
equal(prob(pulse, I - E) + prob(pulse, E), s.Integer(1), 'impulse arm: n5 outcomes sum to one')
equal(prob(free, B), s.Integer(0), 'free arm ends boson-free exactly')
equal(prob(pulse, B), d * d * (1 - d * d) / 2, 'impulse arm endpoint boson probability d^2(1-d^2)/2')
equal(prob(pulse, I - B) + prob(pulse, B), s.Integer(1), 'impulse arm: boson outcomes sum to one')
equal(prob(midpoint, B), (1 - d * d) / 8, 'midpoint boson probability (1-d^2)/8')
equal(Z * seed, seed, 'impulse on the unprepared seed would have no effect')
equal(Z * E - E * Z, s.zeros(3), 'boson sender phase commutes with the fermion receiver effect')
equal(Z * H * Z, Delta * B - g * X, 'the impulse reverses the interaction, detuning intact')
need(H * Z - Z * H != s.zeros(3), 'Z_b does not commute with the fixed H (not a wait word)')

# ------------------------------------------------------------- the recorder
Q0, Q1 = I - B, B
pointer_x = s.Matrix([[0, 1], [1, 0]])
ptr0 = s.Matrix([1, 0])
ptr1 = s.Matrix([0, 1])
record_unitary = s.kronecker_product(Q0, s.eye(2)) + s.kronecker_product(Q1, pointer_x)
record = record_unitary * s.kronecker_product(I, ptr0)
record_generator = s.pi / 2 * s.kronecker_product(B, s.eye(2) - pointer_x)
equal((-s.I * record_generator).exp(), record_unitary,
      'explicit finite neutral pointer coupling implements the instrument')
equal(record_unitary.H * record_unitary, s.eye(6), 'neutral two-state pointer coupling is unitary')
equal(record.H * record, I, 'record isometry preserves the complete joint Gram kernel')
equal(record * s.Matrix([1, 0, 0]), s.kronecker_product(s.Matrix([1, 0, 0]), ptr0),
      'seed pair direction has pointer label 0')
equal(record * s.Matrix([0, 1, 0]), s.kronecker_product(s.Matrix([0, 1, 0]), ptr0),
      'coherent R7 direction has the SAME pointer label 0 (pairs not distinguished)')
equal(record * boson, s.kronecker_product(boson, ptr1), 'boson direction has pointer label 1')
# pair-coherence preservation: every operator on the pair block passes through
pair_ops = {
    'P_p0': s.diag(1, 0, 0),
    'P_R7': s.diag(0, 1, 0),
    'C_re': s.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    'C_im': s.Matrix([[0, -s.I, 0], [s.I, 0, 0], [0, 0, 0]]),
}
for name, O in pair_ops.items():
    equal(record.H * s.kronecker_product(O, s.eye(2)) * record, O,
          'pair coherence preserved by the record: ' + name)
equal(record.H * s.kronecker_product(E, s.eye(2)) * record, E,
      'recording has no immediate receiver effect for any state')
equal(Q0.H * Q0 + Q1.H * Q1, I, 'discarding the pointer is a complete trace-preserving instrument')
m = s.symbols('rho:9')
rho = s.Matrix(3, 3, m)
reduced_record = Q0 * rho * Q0 + Q1 * rho * Q1
equal(reduced_record, (rho + Z * rho * Z) / 2,
      'ignored pointer gives the real update (rho + Z_b rho Z_b)/2')
eta = s.symbols('eta', real=True)
soft_record = Q0 * rho * Q0 + Q1 * rho * Q1 + eta * (Q0 * rho * Q1 + Q1 * rho * Q0)
equal(soft_record, (1 + eta) * rho / 2 + (1 - eta) * Z * rho * Z / 2,
      'partial pointer overlap eta controls the pair-boson coherence exactly')

# recorded process: joint evolution and ALL joint outcome probabilities
joint_mid = record * midpoint
joint_end = s.kronecker_product(U, s.eye(2)) * joint_mid
joint_dag = joint_end.conjugate().T.subs(s.conjugate(u), 1 / u)
E0 = s.kronecker_product(E, s.diag(1, 0))
E1 = s.kronecker_product(E, s.diag(0, 1))
p_rec_0 = reduce((joint_dag * E0 * joint_end)[0])
p_rec_1 = reduce((joint_dag * E1 * joint_end)[0])
p_rec = reduce(p_rec_0 + p_rec_1)
equal(p_rec, ((p0 + p1) / 2).subs(c, cos_identity),
      'coherently evolved record yields the average unconditional receiver probability')
equal((p0 + p1) / 2 - p0, delta / 2,
      'HALF EFFECT: full composition recording causes exactly half the impulse signal')
ptr1_prob = reduce((joint_dag * s.kronecker_product(I, s.diag(0, 1)) * joint_end)[0])
equal(ptr1_prob, (1 - d * d) / 8, 'pointer branch weights equal the midpoint boson probability')
equal(reduce((joint_dag * joint_end)[0]), s.Integer(1), 'joint state normalised (all outcomes sum to one)')

# ------------------------------------------------------------- work deposits
H_in_omega_units = 2 * d * B + r * X / s.sqrt(8)
equal(prob(midpoint, H_in_omega_units), s.Integer(0), 'native midpoint has unchanged zero system energy')
equal(prob(Z * midpoint, H_in_omega_units), d * (1 - d * d) / 2,
      'impulse work in Omega units is d(1-d^2)/2 = Delta(1-d^2)/4 in absolute units')
record_mid_energy = (prob(midpoint, H_in_omega_units) + prob(Z * midpoint, H_in_omega_units)) / 2
equal(record_mid_energy, d * (1 - d * d) / 4, 'record work in Omega units is Delta(1-d^2)/8')
d2_test = s.Rational(25, 27)
equal((Delta**2 / (4 * (Delta**2 / 4 + 8 * g * g))).subs({Delta: 1, g: s.Rational(1, 20)}),
      d2_test, 'd^2 = 25/27 exactly at g/Delta = 1/20')
need(s.Rational(1, 4) * (1 - d2_test) == s.Rational(1, 54),
     'impulse deposits exactly Delta/54 at the test point')
need(s.Rational(1, 8) * (1 - d2_test) == s.Rational(1, 108),
     'recorder deposits exactly Delta/108 at the test point')

# ------------------------------------------- independent numeric replay
omega = math.sqrt(1 / 4 + 8 / 400)
tau = math.pi / (2 * omega)
dn = 1 / (2 * omega)
tol = 1e-14
hn = np.array(H.subs({Delta: 1, g: s.Rational(1, 20)}), dtype=float)
un = expm(-1j * tau * hn)
zn = np.diag([1.0, 1.0, -1.0])
en = np.diag([0.0, 1 / 7, 0.0])
sn = np.array([1, 0, 0], dtype=complex)
fn, pn = un @ un @ sn, un @ zn @ un @ sn
expected0 = float(p0.subs(c, math.cos(math.pi * dn)))
expected1 = float(p1.subs({c: math.cos(math.pi * dn), d: dn}))
need(abs(float(np.vdot(fn, en @ fn).real) - expected0) < tol, 'independent expm free-arm response', 'numeric')
need(abs(float(np.vdot(pn, en @ pn).real) - expected1) < tol, 'independent expm impulse-arm response', 'numeric')
need(abs(expected0 - 0.0002194998817122665) < 1e-16, 'documented free-arm value reproduced', 'numeric')
need(abs(expected1 - 0.0005299169088385700) < 1e-16, 'documented impulse-arm value reproduced', 'numeric')
rn = np.array(record, dtype=float)
jn = np.kron(un, np.eye(2)) @ rn @ (un @ sn)
prec_n = float(np.vdot(jn, np.kron(en, np.eye(2)) @ jn).real)
need(abs(prec_n - (expected0 + expected1) / 2) < tol, 'independent six-state record half effect', 'numeric')
need(abs(np.linalg.norm(fn) - 1) < tol and abs(np.linalg.norm(pn) - 1) < tol
     and abs(np.linalg.norm(jn) - 1) < tol, 'independent probability normalisation', 'numeric')

# nine-dimensional native star cross-check (evolution formed numerically)
h9n = np.array(H9.subs({Delta: 1, g: s.Rational(1, 20)}), dtype=float)
u9 = expm(-1j * tau * h9n)
seed9 = np.zeros(9, dtype=complex)
seed9[0] = 1
z9 = np.diag([1.0] * 8 + [-1.0])
e9 = np.diag([0.0, 1.0] + [0.0] * 7)
f9 = u9 @ u9 @ seed9
p9 = u9 @ z9 @ u9 @ seed9
need(abs(float(np.vdot(f9, e9 @ f9).real) - expected0) < tol,
     'native nine-star free arm matches K3 (expm, no symbolic formula)', 'numeric')
need(abs(float(np.vdot(p9, e9 @ p9).real) - expected1) < tol,
     'native nine-star impulse arm matches K3 (expm, no symbolic formula)', 'numeric')

result = {
    'status': 'PASS',
    'guards': len(checks),
    'exact_guards': sum(1 for _, k in checks if k == 'exact'),
    'numerical_guards': sum(1 for _, k in checks if k == 'numeric'),
    'checks': [{'name': n, 'kind': k} for n, k in checks],
    'experiment': {
        'carrier': 'native K3 = span{p0=|4,57>, R7, b0} inside the channel-0 star of W',
        'initial_state': 'p0 (both arms identical)',
        'sequences': {'free': 'U I U', 'impulse': 'U Z_b U', 'tau': 'pi/(2 Omega)',
                      'Omega_squared': 'Delta^2/4 + 8 g^2'},
        'readout': 'n5, effect E = diag(0,1/7,0) on K3 (admissible: compresses exactly; '
                   'Lueders back-action leaves K3, boundary diag(0,6/49,0))',
        'all_outcome_probabilities': {
            'free': {'n5_1': '(1+cos(pi d))/32', 'n5_0': '1 - (1+cos(pi d))/32', 'Nb_end_1': '0'},
            'impulse': {'n5_1': '[1+(1-2d^2)^2-2(1-2d^2)cos(pi d)]/64',
                        'n5_0': '1 - that', 'Nb_end_1': 'd^2(1-d^2)/2'},
            'midpoint_Nb_1': '(1-d^2)/8'},
        'test_point': {'Delta': '1', 'g': '1/20', 'd^2': '25/27',
                       'free_n5': repr(expected0), 'impulse_n5': repr(expected1),
                       'difference': repr(expected1 - expected0),
                       'record_n5': repr((expected0 + expected1) / 2),
                       'record_difference': repr((expected1 - expected0) / 2)},
        'recording': {'isometry': 'V psi = (I-B) psi x |0> + B psi x |1> on K3 x C2',
                      'coupler': 'C_R = exp(-i pi/2 B x (I - X_R))',
                      'all_pair_coherences_preserved': True,
                      'joint_Gram_preserved': True,
                      'ignored_pointer_update': '(rho + Z_b rho Z_b)/2',
                      'half_effect_exact': True,
                      'soft_overlap_eta_signal': '(1-eta)/2 of the impulse signal',
                      'postselection': False},
        'work': {'impulse_deposit': 'Delta(1-d^2)/4 = Delta/54 at the test point',
                 'recorder_deposit': 'Delta(1-d^2)/8 = Delta/108 at the test point'},
        'additional_resources_not_derived': ['independent X/N_b switchability',
                                             'pointer preparation and conditional coupling',
                                             'initial p0 preparation', 'terminal calibrated n5 detector']},
    'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'runtime_seconds': round(time.time() - T0, 3),
}
print(json.dumps(result, indent=2))
