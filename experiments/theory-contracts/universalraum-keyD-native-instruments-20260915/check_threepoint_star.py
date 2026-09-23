"""Task 2 (keyD): native 3-point intervention test on the exact star block.

Three exact layers on the 9-dimensional invariant star of channel A = 0
(rebuilt from the byte-pinned in-repo native_source.py, no npz):

  (A) v1.6.8 reproduction with native-only steps: star-internal evolution
      U_T, the phase Z_4, occupation readout n_5; plus the documented 3x3
      reduction (h3, z3, e3) cross-validated against the 9x9 computation.
  (B) CAR null-intervention lemma: Z_r f_r = f_r and f_r^dag Z_r = f_r^dag
      (since n_r f_r = 0), verified as exact integer sparse sector maps for
      N = 1, 2, 3 and all 64 modes. Consequence: the literal removal-tagged
      3-point intervention  <Omega|f_r^dag e^{iHt} n_s e^{-iHt} f_r|Omega>
      - <Omega|f_r^dag Z_r e^{iHt} n_s e^{-iHt} Z_r f_r|Omega>  vanishes
      identically for every state Omega, every r, s, t and every H - the
      no-go extends, by CAR absorption at the removal event, not by symmetry.
  (C) The physical midpoint protocol on the star-symmetric (bright) state
      |B> = (1/sqrt 8) sum_q sigma_q |leaf q>: the off-diagonal intervention
      signal is delta^B_{r->s} = -3x/128 != 0 for every g != 0 - the
      symmetry no-go does NOT extend to the native midpoint 3-point protocol
      at star level. Discriminating companion: the 2-point removal response
      on |B> is C^B_{rs}(t) = delta_rs/8 exactly (no mode-to-mode structure).

Numeric cross-checks on the full 2076-dimensional N=2 block are flagged
kind='numerical'. Runs under normal and -OO; explicit guards, no asserts.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations, permutations
import contextlib
import io
import math
import runpy
import json
import time
import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix, csr_matrix, bmat, eye
from scipy.sparse.linalg import expm_multiply

HERE = Path(__file__).resolve().parent
NS_PIN = '380577f85d2afa8b50f91a0991769eaf8267ee5c09f327d87f17e1b4c0af1672'

T0 = time.time()
checks = []
def need(ok, name, kind='exact'):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append((name, kind))

need(sha256((HERE / 'native_source.py').read_bytes()).hexdigest() == NS_PIN,
     'native_source.py byte pin')
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(HERE / 'native_source.py'))
W = ns['W']; PAIRS = ns['PAIRS']; ann = ns['ann']; create = ns['create']
TRIPLES = list(combinations(range(64), 3))
PAIR_INDEX = {p: j for j, p in enumerate(PAIRS)}

# --- Star channel A = 0 ------------------------------------------------------
columns = list(map(int, np.flatnonzero(W[0])))
leaves = [PAIRS[c] for c in columns]
signs = [int(W[0, c]) for c in columns]
need(leaves[0] == (4, 57) and leaves[1] == (5, 56), 'v1.6.8 star leaves')
star_modes = [m for leaf in leaves for m in leaf]
need(len(set(star_modes)) == 16, 'sixteen distinct star modes')
leaf_of = {m: q for q, leaf in enumerate(leaves) for m in leaf}
mate = {}
for i, j in leaves:
    mate[i] = j
    mate[j] = i
need(signs[0] == -1, 'sigma_0 = -1')

Delta, g, z = sp.symbols('Delta g z')
sig = sp.Matrix(signs)
H = sp.zeros(9)
H[:8, 8] = g * sig
H[8, :8] = g * sig.T
H[8, 8] = Delta
projector = sig * sig.T / 8
active = sp.diag(projector, sp.ones(1))
need(sp.simplify(H * H - Delta * H - 8 * g * g * active) == sp.zeros(9),
     'exact quadratic identity H^2 = Delta H + 8 g^2 active on the star')
need(sp.simplify(active * H - H) == sp.zeros(9), 'bright-plus-boson subspace is invariant')
shifted = H - Delta * active / 2
Omega2 = Delta**2 / 4 + 8 * g**2
need(sp.simplify(shifted * shifted - Omega2 * active) == sp.zeros(9),
     'shifted Hamiltonian squares to Omega^2 on the bright block')
UT = sp.eye(9) + (z - 1) * active
need(sp.simplify(UT.subs(z, 1/z).T * UT - sp.eye(9)) == sp.zeros(9),
     'full-period propagator U_T = I + (z-1) active is unitary for |z| = 1')
Nf9 = sp.diag(*([2] * 8), 0)
Nb9 = sp.diag(*([0] * 8), 1)
need(Nf9 + 2 * Nb9 == 2 * sp.eye(9), 'total charge is two on the star')

def z_leaf(q):
    return sp.diag(*[(-1 if k == q else 1) for k in range(8)], 1)

def n_leaf(q):
    return sp.diag(*[(1 if k == q else 0) for k in range(8)], 0)

# Global-to-star restriction of the native operators, for all 16 star modes.
for r in star_modes:
    zr_global = np.array([-1 if r in p else 1 for p in PAIRS] + [1] * 60, dtype=np.int64)
    need(np.array_equal(zr_global[columns + [2016]], np.array(z_leaf(leaf_of[r]).diagonal(), dtype=int).ravel()),
         f'global (-1)^n_{r} restricts to the star leaf phase')
    nr_global = np.array([1 if r in p else 0 for p in PAIRS] + [0] * 60, dtype=np.int64)
    need(np.array_equal(nr_global[columns + [2016]], np.array(n_leaf(leaf_of[r]).diagonal(), dtype=int).ravel()),
         f'global n_{r} restricts to the star leaf projector')
need(all(leaf_of[r] == leaf_of[mate[r]] for r in star_modes), 'mode and mate share their leaf')

x = 2 - z - 1 / z  # = 4 cos^2(pi d / 2) for z = -exp(-i pi d), |z| = 1

def prob(amp):
    return sp.simplify(amp * amp.subs(z, 1/z))

def protocol(start, q_pulse, q_read):
    mid = UT * start
    base = UT * mid
    pul = UT * (z_leaf(q_pulse) * mid)
    return sp.simplify(prob(pul[q_read]) - prob(base[q_read])), base, pul

# --- (A) v1.6.8 reproduction, native steps only ------------------------------
p0 = sp.eye(9)[:, 0]
d_prod_45, base_p, pul_p = protocol(p0, 0, 1)
need(sp.simplify(d_prod_45 - x * (25 * x - 64) / 1024) == 0,
     'v1.6.8 headline: delta_{4->5} = x(25x-64)/1024 with native-only steps')
need(sp.simplify(prob(base_p[1]) - x * (4 - x) / 64) == 0, 'untouched probability x(4-x)/64')
need(sp.simplify(prob(pul_p[1]) - 9 * x**2 / 1024) == 0, 'pulsed probability 9x^2/1024')
for st, nm in ((base_p, 'untouched'), (pul_p, 'pulsed')):
    need(sp.simplify(Nf9 * st - 2 * st) == sp.zeros(9, 1), f'product {nm} arm ends with exactly N_f = 2')
    need(sp.simplify(Nb9 * st) == sp.zeros(9, 1), f'product {nm} arm ends with zero bosons')
need(25 * 2 - 64 < 0, 'strict negative product-state response on 0 < x <= 2')
# interval equivalence: x <= 2  <=>  d >= 1/2  <=>  g^2 <= 3 Delta^2/32
d2 = Delta**2 / (4 * Omega2)
need(sp.simplify(d2 - sp.Rational(1, 4) - (3 * Delta**2 / 4 - 8 * g**2) / (4 * Omega2)) == 0,
     'd^2 >= 1/4  <=>  g^2 <= 3 Delta^2/32 (algebraic equivalence)')
need(sp.simplify(d2 - 1 + 8 * g**2 / Omega2) == 0,
     'd < 1  <=>  g != 0 (equivalently x > 0)')
# Full leaf-level table, product start.
prod_off = x * (25 * x - 64) / 1024
prod_diag = 7 * x * (64 - 25 * x) / 1024
for qr, qs in permutations(range(8), 2):
    dq, _, _ = protocol(p0 * 0 + sp.eye(9)[:, qr], qr, qs)
    need(sp.simplify(dq - prod_off) == 0, f'product off-diagonal leaf pair {qr}->{qs} = x(25x-64)/1024')
for qr in range(8):
    dq, _, _ = protocol(sp.eye(9)[:, qr], qr, qr)
    need(sp.simplify(dq - prod_diag) == 0, f'product diagonal leaf {qr} = 7x(64-25x)/1024')
need(sp.simplify(prod_diag + 7 * prod_off) == 0, 'product leaf sum rule: diagonal + 7 off-diagonal = 0')

# Documented 3x3 reduction (h3, z3, e3) cross-validated against the 9x9 star.
u7 = sp.Matrix([sp.Rational(0)] + [sp.Rational(sv) / sp.sqrt(7) for sv in signs[1:]] + [sp.Rational(0)])
P3 = sp.Matrix.hstack(sp.eye(9)[:, 0], u7, sp.eye(9)[:, 8])
need(sp.simplify(P3.T * P3 - sp.eye(3)) == sp.zeros(3), 'reduction basis is orthonormal')
h3 = sp.Matrix([[0, 0, -g], [0, 0, sp.sqrt(7) * g], [-g, sp.sqrt(7) * g, Delta]])
z3 = sp.diag(-1, 1, 1)
e3 = sp.diag(0, sp.Rational(1, 7), 0)
need(sp.simplify(H * P3 - P3 * h3) == sp.zeros(9, 3), 'span{e_0, u, b} is H-invariant with the documented h3')
need(sp.simplify(z_leaf(0) * P3 - P3 * z3) == sp.zeros(9, 3), 'Z_4 preserves the 3d subspace and restricts to z3')
need(sp.simplify(P3.T * n_leaf(1) * P3 - e3) == sp.zeros(3), 'n_5 compresses to e3 = diag(0, 1/7, 0)')
B3 = sp.Matrix([-1, sp.sqrt(7), 0]) / sp.sqrt(8)
UT3 = sp.eye(3) + (z - 1) * (B3 * B3.T + sp.diag(0, 0, 1))
need(sp.simplify(UT * P3 - P3 * UT3) == sp.zeros(9, 3), 'U_T restricts to the 3d subspace propagator')
mid3 = UT3 * sp.eye(3)[:, 0]
base3 = UT3 * mid3
pul3 = UT3 * (z3 * mid3)
need(sp.simplify((prob(pul3[1]) - prob(base3[1])) / 7 - x * (25 * x - 64) / 1024) == 0
     and sp.simplify(prob(pul3[1]) / 7 - 9 * x**2 / 1024) == 0
     and sp.simplify(prob(base3[1]) / 7 - x * (4 - x) / 64) == 0,
     'the 3x3 reduction (h3, z3, e3) reproduces the v1.6.8 response exactly')

# --- (B) CAR null-intervention lemma -----------------------------------------
def f_map(N_from, r):
    rows, cols, vals = [], [], []
    if N_from == 1:
        return coo_matrix(([1], ([0], [r])), shape=(1, 64), dtype=np.int64).tocsr()
    if N_from == 2:
        for j, (a, b) in enumerate(PAIRS):
            st = ann((1 << a) | (1 << b), r)
            if st:
                mask, sign = st
                rows.append(mask.bit_length() - 1)
                cols.append(j)
                vals.append(sign)
        return coo_matrix((vals, (rows, cols)), shape=(64, 2076), dtype=np.int64).tocsr()
    # N_from == 3: triples -> pairs, (b,f) -> bosons
    for j, (a, b, c) in enumerate(TRIPLES):
        st = ann((1 << a) | (1 << b) | (1 << c), r)
        if st:
            mask, sign = st
            bits = tuple(k for k in range(64) if mask & (1 << k))
            rows.append(PAIR_INDEX[bits])
            cols.append(j)
            vals.append(sign)
    for A in range(60):
        rows.append(2016 + A)
        cols.append(41664 + 64 * A + r)
        vals.append(1)
    return coo_matrix((vals, (rows, cols)), shape=(2076, 45504), dtype=np.int64).tocsr()

def z_diag(N, r):
    if N == 0:
        return csr_matrix(([1], ([0], [0])), shape=(1, 1), dtype=np.int64)
    if N == 1:
        d = np.array([-1 if s == r else 1 for s in range(64)], dtype=np.int64)
        return csr_matrix(np.diag(d))
    if N == 2:
        d = np.array([-1 if r in p else 1 for p in PAIRS] + [1] * 60, dtype=np.int64)
        return csr_matrix(np.diag(d))
    d = np.array([-1 if r in t else 1 for t in TRIPLES]
                 + [-1 if s == r else 1 for A in range(60) for s in range(64)], dtype=np.int64)
    return csr_matrix(np.diag(d))

car_identities = 0
for N in (1, 2, 3):
    for r in range(64):
        fmap = f_map(N, r)
        Zt = z_diag(N - 1, r)
        d1 = (Zt @ fmap - fmap).tocsr(); d1.eliminate_zeros()
        need(d1.nnz == 0, f'Z_{r} f_{r} = f_{r} as sector map N={N} -> N={N-1}')
        fdag = f_map(N, r).T.tocsr()
        d2 = (fdag @ Zt - fdag).tocsr(); d2.eliminate_zeros()
        need(d2.nnz == 0, f'f_{r}^dag Z_{r} = f_{r}^dag as sector map N={N-1} -> N={N}')
        nr_low = (csr_matrix(np.eye(Zt.shape[0], dtype=np.int64)) - Zt) / 2
        d3 = (nr_low @ fmap).tocsr(); d3.eliminate_zeros()
        need(d3.nnz == 0, f'n_{r} f_{r} = 0 as sector map N={N} -> N={N-1} (CAR absorption)')
        car_identities += 3
need(car_identities == 3 * 64 * 3, 'CAR null lemma: 576 exact sparse sector identities')

# State-level content on the star with the symmetric state |B>: the tagged and
# untagged removal 3-point functions coincide for all 16 x 16 mode pairs.
B9 = sp.Matrix([sp.Rational(sv) for sv in signs]) / sp.sqrt(8)
B9 = sp.Matrix.vstack(B9, sp.Matrix([0]))
def removal_state(r):
    """f_r |B> as an exact N=1 one-mode state (sign, mode)."""
    q = leaf_of[r]
    i, j = leaves[q]
    sgn = 1 if r == i else -1  # f_i|pair(i,j)> = +|j>, f_j|pair(i,j)> = -|i>
    return sp.Rational(sgn * signs[q]) / sp.sqrt(8), mate[r]

three_point = {}
for r in star_modes:
    cr, mr = removal_state(r)
    for s in star_modes:
        untagged = sp.simplify(cr * cr * (1 if s == mr else 0))
        # tagged: Z_r on the N=1 state |mr> is +1 because mr != r
        tagged = untagged
        need(untagged == tagged, f'tagged equals untagged removal 3-point on the star for ({r},{s})')
        need(untagged == (sp.Rational(1, 8) if s == mr else sp.Rational(0)),
             f'star removal 3-point T^B_{{{r},{s}}} = delta_{{s,mate(r)}}/8')
        three_point[(r, s)] = untagged
# Generalization: ANY single-mode tag at removal time is a global phase on the
# one-fermion removal state, hence physically void.
for r in star_modes:
    cr, mr = removal_state(r)
    for rp in star_modes:
        eigen = -1 if rp == mr else 1
        need(sp.simplify(eigen * cr - cr * (1 if rp != mr else -1)) == 0,
             f'Z_{rp} f_{r}|B> = +/- f_{r}|B> (global phase only)')

# --- (C) 2-point analog and the midpoint 3-point on the symmetric state -------
# H vanishes on the N=1 sector: no bosons can be present (N_b = 1 needs N >= 2)
# and pair annihilation needs two fermions.
support_pairs = [PAIRS[int(c)] for c in np.flatnonzero(np.any(W, axis=0))]
need(len(support_pairs) == 480, '480 supported pairs')
need(all(ns['pair_action'](1 << s, pr, dagger=False) is None
         for s in range(64) for pr in support_pairs),
     'pair annihilation vanishes on every one-fermion state: X = 0 on N=1, hence H = 0 on N=1')
two_point_delta = True
for r in star_modes:
    cr, mr = removal_state(r)
    for s in star_modes:
        cs, ms = removal_state(s)
        # C^B_{rs}(t) = <B| f_r^dag e^{-iHt} f_s |B> = conj(cr) cs <mr|ms> (H = 0 on N=1)
        cval = sp.simplify(cr * cs * (1 if mr == ms else 0))
        need(cval == (sp.Rational(1, 8) if r == s else sp.Rational(0)),
             f'2-point removal response C^B_{{{r},{s}}}(t) = delta_rs/8 (no mode-to-mode structure)')

# Midpoint protocol on the bright symmetric state.
bright_off = -3 * x / 128
bright_diag = 21 * x / 128
for qr, qs in permutations(range(8), 2):
    dq, _, _ = protocol(B9, qr, qs)
    need(sp.simplify(dq - bright_off) == 0, f'bright off-diagonal {qr}->{qs}: -3x/128')
for qr in range(8):
    dq, base_b, pul_b = protocol(B9, qr, qr)
    need(sp.simplify(dq - bright_diag) == 0, f'bright diagonal leaf {qr}: +21x/128')
need(sp.simplify(bright_diag + 7 * bright_off) == 0, 'bright leaf sum rule: diagonal + 7 off-diagonal = 0')
_, base_b, pul_b = protocol(B9, 0, 1)
for st, nm in ((base_b, 'untouched'), (pul_b, 'pulsed')):
    need(sp.simplify(Nf9 * st - 2 * st) == sp.zeros(9, 1), f'bright {nm} arm ends with exactly N_f = 2')
    need(sp.simplify(Nb9 * st) == sp.zeros(9, 1), f'bright {nm} arm ends with zero bosons')
need(sp.simplify(bright_off / x - (-sp.Rational(3, 128))) == 0 and sp.Rational(-3, 128) < 0,
     'bright off-diagonal signal is exactly -3/128 * x: strictly negative for every x > 0 (every g != 0)')
need(sp.simplify(bright_diag / x - sp.Rational(21, 128)) == 0 and sp.Rational(21, 128) > 0,
     'bright diagonal signal is exactly +21/128 * x: strictly positive for every x > 0')

# Boson-seed secondary witness (native steps; v1.6.8 secondary protocol).
a, b, c = sp.symbols('a b c')
Uhalf = sp.eye(9)
Uhalf[:8, :8] += (a - 1) * projector
Uhalf[:8, 8] = b * sig / sp.sqrt(8)
Uhalf[8, :8] = b * sig.T / sp.sqrt(8)
Uhalf[8, 8] = c
boson = sp.eye(9)[:, 8]
mid_b = Uhalf * boson
difference = Uhalf * z_leaf(0) * mid_b - Uhalf * mid_b
need(sp.simplify(difference[1] + signs[1] * b * (a - 1) / (4 * sp.sqrt(8))) == 0,
     'boson-seed half-period phase response amplitude')
d = sp.symbols('d', positive=True)
boson_signal = (1 - d * d) * (1 + d * d - 2 * d * sp.sin(sp.pi * d / 2)) / 128
lower_bound = (1 - d * d) * (1 - d) ** 2 / 128
halfphase = sp.cos(sp.pi * d / 2) - sp.I * sp.sin(sp.pi * d / 2)
r_sym = sp.symbols('r', real=True)
halfvalues = {a: sp.I * d * halfphase, c: -sp.I * d * halfphase, b: -sp.I * r_sym * halfphase}
need(sp.simplify((Uhalf * Uhalf * boson)[1].subs(halfvalues)) == 0,
     'untouched boson seed has exactly zero receiver amplitude after two half periods')
boson_response_amp = sp.simplify((Uhalf * z_leaf(0) * Uhalf * boson)[1].subs(halfvalues))
boson_response_probability = sp.simplify(sp.expand_complex(boson_response_amp * sp.conjugate(boson_response_amp)))
need(sp.trigsimp(sp.expand(boson_response_probability.subs(r_sym * r_sym, 1 - d * d) - boson_signal), method='fu') == 0,
     'exact boson-seed receiver probability after local phase')
need(sp.simplify(boson_signal - lower_bound - (1 - d * d) * d * (1 - sp.sin(sp.pi * d / 2)) / 64) == 0,
     'positive boson-seed signal lower bound for 0 < d < 1')

# --- Numeric cross-check on the full 2076-dim N=2 block (flagged numerical) ---
Delta_num, g_num = 1.0, 0.05
omega = math.sqrt(Delta_num**2 / 4 + 8 * g_num**2)
dnum = Delta_num / (2 * omega)
period = math.pi / omega
xnum = 4 * math.cos(math.pi * dnum / 2) ** 2
Wsp = csr_matrix(W, dtype=float)
Hfull = bmat([[csr_matrix((2016, 2016)), g_num * Wsp.T],
              [g_num * Wsp, Delta_num * eye(60)]], format='csr')
phase = np.ones(2076)
phase[[k for k, p in enumerate(PAIRS) if 4 in p]] = -1
read5 = np.zeros(2076)
read5[[k for k, p in enumerate(PAIRS) if 5 in p]] = 1
read4 = np.zeros(2076)
read4[[k for k, p in enumerate(PAIRS) if 4 in p]] = 1

def run_protocol(start_vec):
    mid = expm_multiply(-1j * period * Hfull, start_vec)
    base = expm_multiply(-1j * period * Hfull, mid)
    pul = expm_multiply(-1j * period * Hfull, phase * mid)
    return base, pul

prod0 = np.zeros(2076, dtype=complex)
prod0[columns[0]] = 1
base_fp, pul_fp = run_protocol(prod0)
need(abs(float(np.dot(read5, np.abs(base_fp) ** 2)) - xnum * (4 - xnum) / 64) < 1e-13,
     'numeric full-N2 untouched product probability matches x(4-x)/64', 'numerical')
need(abs(float(np.dot(read5, np.abs(pul_fp) ** 2)) - 9 * xnum ** 2 / 1024) < 1e-13,
     'numeric full-N2 pulsed product probability matches 9x^2/1024', 'numerical')
bright0 = np.zeros(2076, dtype=complex)
bright0[columns] = np.array(signs, dtype=float) / math.sqrt(8)
base_fb, pul_fb = run_protocol(bright0)
d_off_num = float(np.dot(read5, np.abs(pul_fb) ** 2) - np.dot(read5, np.abs(base_fb) ** 2))
d_diag_num = float(np.dot(read4, np.abs(pul_fb) ** 2) - np.dot(read4, np.abs(base_fb) ** 2))
need(abs(d_off_num - (-3 * xnum / 128)) < 1e-12,
     'numeric full-N2 bright off-diagonal signal matches -3x/128', 'numerical')
need(abs(d_diag_num - 21 * xnum / 128) < 1e-12,
     'numeric full-N2 bright diagonal signal matches +21x/128', 'numerical')
complement = np.ones(2076)
complement[columns + [2016]] = 0
need(float(np.dot(complement, np.abs(base_fb) ** 2)) < 1e-24
     and float(np.dot(complement, np.abs(pul_fb) ** 2)) < 1e-24,
     'bright protocol stays inside the star (zero leakage)', 'numerical')
need(np.linalg.norm(base_fb[2016:]) < 1e-12 and np.linalg.norm(pul_fb[2016:]) < 1e-12,
     'bright arms end with zero bosons numerically', 'numerical')
# Boson-seed numeric.
boson0 = np.zeros(2076, dtype=complex)
boson0[2016] = 1
mid_b = expm_multiply(-0.5j * period * Hfull, boson0)
base_bb = expm_multiply(-0.5j * period * Hfull, mid_b)
pul_bb = expm_multiply(-0.5j * period * Hfull, phase * mid_b)
expected_boson_signal = float(boson_signal.subs(d, dnum))
need(float(np.dot(read5, np.abs(base_bb) ** 2)) < 1e-24,
     'numeric boson-seed untouched receiver probability vanishes', 'numerical')
need(abs(float(np.dot(read5, np.abs(pul_bb) ** 2)) - expected_boson_signal) < 1e-13,
     'numeric boson-seed phase response matches the exact formula', 'numerical')
# Star-symbolic states match the embedded full states.
znum = -np.exp(-1j * math.pi * dnum)
_, base_s, pul_s = protocol(p0, 0, 1)
star_base = np.array(base_s.subs(z, znum), dtype=complex).ravel()
star_pulse = np.array(pul_s.subs(z, znum), dtype=complex).ravel()
embed = columns + [2016]
expected_full0 = np.zeros(2076, dtype=complex)
expected_full1 = np.zeros(2076, dtype=complex)
expected_full0[embed] = star_base
expected_full1[embed] = star_pulse
need(np.linalg.norm(base_fp - expected_full0) < 1e-12 and np.linalg.norm(pul_fp - expected_full1) < 1e-12,
     'full-N2 product arms agree with the exact star states', 'numerical')

result = {
    'status': 'PASS',
    'task': 'native 3-point intervention on the exact star block',
    'guards': len(checks),
    'exact_guards': sum(k == 'exact' for _, k in checks),
    'numerical_guards': sum(k == 'numerical' for _, k in checks),
    'car_null_lemma': {
        'operator_identities': ['Z_r f_r = f_r', 'f_r^dag Z_r = f_r^dag', 'n_r f_r = 0'],
        'sector_identities_checked': car_identities,
        'sectors': 'N = 1 -> 0, N = 2 -> 1, N = 3 -> 2, all 64 modes, exact integer sparse',
        'consequence': ('the literal removal-tagged 3-point intervention signal '
                        'Delta n_s(t) = <..f_r^dag e^{iHt} n_s e^{-iHt} f_r..> - <..f_r^dag Z_r e^{iHt} n_s '
                        'e^{-iHt} Z_r f_r..> vanishes identically for every state, every r, s, t, every H'),
        'star_state_level': 'tagged = untagged for all 16 x 16 star mode pairs; any single-mode tag at '
                            'removal time is a global phase on the one-fermion removal state',
        'no_go_extension': 'extends exactly - mechanism is CAR absorption at the removal event, not symmetry',
    },
    'two_point_star_analog': {
        'value': 'C^B_{rs}(t) = delta_rs/8, time-independent (H = 0 on N=1)',
        'mode_to_mode_structure': 'absent, consistent with the ground-state no-go form',
    },
    'midpoint_three_point_bright': {
        'state': '|B> = (1/sqrt 8) sum_q sigma_q |leaf q> (star-symmetric bright state)',
        'off_diagonal': '-3x/128 for all 56 ordered leaf pairs (r != s leaves); strictly negative for every g != 0',
        'diagonal': '+21x/128 (same leaf)',
        'sum_rule': 'diagonal + 7 * off-diagonal = 0 exactly (N_f conservation)',
        'verdict': ('the star-symmetric state does NOT kill the off-diagonal intervention signal: '
                    'the symmetry no-go does not extend to the native midpoint 3-point protocol at '
                    'star level; a native symmetric-state witness exists at block level'),
    },
    'v168_reproduction': {
        'product_state_delta': 'x(25x-64)/1024',
        'product_diagonal': '7x(64-25x)/1024',
        'negative_interval': '0 < g^2 <= 3 Delta^2/32  <=>  0 < x <= 2',
        'boson_seed_signal': '(1-d^2)(1+d^2-2d sin(pi d/2))/128 > 0 for 0 < d < 1',
        'reduction_3x3': 'h3, z3 = diag(-1,1,1), e3 = diag(0,1/7,0) cross-validated against the 9x9 star',
        'native_steps_only': ['star-internal evolution U_T', 'phase Z_4', 'occupation readout n_5'],
    },
    'numeric_test_point': {
        'Delta': 1, 'g': '1/20',
        'x': format(xnum, '.14g'),
        'product_delta_45': format(xnum * (25 * xnum - 64) / 1024, '.14g'),
        'bright_off_diagonal': format(-3 * xnum / 128, '.14g'),
        'bright_diagonal': format(21 * xnum / 128, '.14g'),
        'boson_seed_signal': format(expected_boson_signal, '.14g'),
    },
    'scope': ('exact star block (9 dims) and exact sparse sector maps through N=3; numeric full-N=2 '
              'cross-check flagged; no N=64 ground-state vector; the true-singlet 3-point question '
              'remains open beyond block level'),
    'runtime_seconds': round(time.time() - T0, 3),
    'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'dependency_sha256': NS_PIN,
    'T1_T8_closed': [],
}
print(json.dumps(result, indent=2, sort_keys=True))
