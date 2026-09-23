"""Checker 1 (v1.6.9 lift typing): source-side objects and regression anchors.

Rebuilds, with exact integer / Gaussian-integer / sympy rational arithmetic
only, the two documented source carriers WITHOUT importing the heavy original
verification files:

  (a) the seven early source words on the SAME C3 (v566 constants 111-121 /
      S1): Q = [[3,1,0],[3,2,0],[3,2,1]], U = Q diag(1,0,0),
      V = Q diag(0,1,1); the words I, U, V, UV, VU, V^2, VUV span a
      7-dimensional algebra closed under all 49 products; its minimal
      dagger completion is all of M3 (dimension 9), so the source algebra
      is NOT adjunction-closed.
  (b) the 60 original Gaussian root rays on the SAME C4 (v783 P0/P1):
      C* is the extended Hamming [8,4,4] code (14 weight-4 supports,
      W0246 a member), roots = {x in {-2..2}^8 : sum x^2 = 4, x mod 2 in C*},
      chart R^8 -> C^4, z_k = r_2k + i r_2k+1, J-lines = mu4 orbits,
      canonical Z[i]-primitive rays. Overlap squares are exactly
      {0, 1/4, 1/2, 1}; the projectors span the full M4 algebra.

Regression anchors guarded (not rediscovered; documented values):
  * ordered triple trace tr(Pi0 Pi1 Pi2) = (1-i)/4 for the documented
    ordering (Pi0, Pi1, Pi2) = (P_0, P_{+i}, P_+) of the source-ray
    projectors of a = (1,0,0,0), b = (1,0,1,0), c = (1,0,i,0);
    the reverse ordering gives (1+i)/4.
  * the reflection-word witness: R0 R+ Ri = diag(-i,1,-i,1),
    R0 Ri R+ = diag(i,1,i,1); with the internal source-ray probe
    (1,1,0,0) and readout (1,i,0,0) the Born probabilities are 1 and 0.

Every object is assigned its documented TYPE; no carrier identification
between these source spaces and the 64-fermion native carrier is claimed
(the typed assignment of the C4 rays to global CAR charts is missing).

Runs under normal and -OO; all guards are explicit (no asserts).
"""
from pathlib import Path
from hashlib import sha256
import itertools
import json
import time

import sympy as s

HERE = Path(__file__).resolve().parent
T0 = time.time()
checks = []


def need(ok, name, kind='exact'):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append((name, kind))


# ---------------------------------------------------------------- C3 words
Q = s.Matrix([[3, 1, 0], [3, 2, 0], [3, 2, 1]])
U = Q * s.diag(1, 0, 0)
V = Q * s.diag(0, 1, 1)
I3 = s.eye(3)
need(U.rank() == 1 and V.rank() == 2, 'source words U rank 1, V rank 2')
need(sorted(V.eigenvals().keys()) == [0, 1, 2], 'Spec(V) = {0,1,2}')

WORDS = [I3, U, V, U * V, V * U, V * V, V * U * V]
WORD_NAMES = ['I', 'U', 'V', 'UV', 'VU', 'V^2', 'VUV']
IDX = ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2))


def coord_vec(M):
    return [M[i, j] for (i, j) in IDX]


coords = s.Matrix([coord_vec(w) for w in WORDS])
need(coords.det() == -81 and coords.rank() == 7,
     'seven words independent on the same C3 (coordinate determinant -81)')


def in_span(M):
    return s.Matrix.vstack(coords, s.Matrix([coord_vec(M)])).rank() == 7


closed = all(in_span(w1 * w2) for w1 in WORDS for w2 in WORDS)
need(closed, 'all 49 word products close inside the 7-dimensional algebra')
units_in = True
for (i, j) in IDX:
    Eij = s.zeros(3, 3)
    Eij[i, j] = 1
    units_in = units_in and in_span(Eij)
need(units_in, 'the algebra contains all seven line-stabiliser matrix units '
               '(A = {[[*,*,0],[*,*,0],[*,*,*]]})')
need(all(w[0, 2] == 0 and w[1, 2] == 0 for w in WORDS),
     'every word stabilises the coordinate line e3 (parabolic shape)')
full_vec = lambda M: [M[i, j] for i in range(3) for j in range(3)]
dagger_completion = s.Matrix([full_vec(w) for w in WORDS] + [full_vec(w.H) for w in WORDS])
need(dagger_completion.rank() == 9,
     'minimal dagger completion of the word algebra is all of M3 (dim 9): '
     'the source algebra is NOT adjunction-closed')

# ------------------------------------------------------------- C4 Gauss rays
SUPPORTS = [(0, 1, 2, 3), (0, 1, 4, 5), (0, 1, 6, 7), (0, 2, 4, 6), (0, 2, 5, 7),
            (0, 3, 4, 7), (0, 3, 5, 6), (1, 2, 4, 7), (1, 2, 5, 6), (1, 3, 4, 6),
            (1, 3, 5, 7), (2, 3, 4, 5), (2, 3, 6, 7), (4, 5, 6, 7)]


def indicator(sup):
    return tuple(1 if i in sup else 0 for i in range(8))


code = {tuple([0] * 8)}
for sup in SUPPORTS:
    code.add(indicator(sup))
changed = True
while changed:
    changed = False
    for a, b in itertools.combinations(list(code), 2):
        c = tuple((x + y) % 2 for x, y in zip(a, b))
        if c not in code:
            code.add(c)
            changed = True
need(len(code) == 16 and sum(1 for w in code if sum(w) == 4) == 14,
     'C* is the extended Hamming [8,4,4] code (16 words, 14 of weight 4)')
W0246 = tuple(1 if i in (0, 2, 4, 6) else 0 for i in range(8))
need(W0246 in code, 'W0246 is a codeword (C* selection rule of the source)')

ROOTS = [x for x in itertools.product(range(-2, 3), repeat=8)
         if sum(v * v for v in x) == 4 and tuple(v % 2 for v in x) in code]
need(len(ROOTS) == 240, '240 Construction-A roots of C*')


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gconj(a):
    return (a[0], -a[1])


def gnorm(a):
    return a[0] * a[0] + a[1] * a[1]


def gdiv(a, b):
    n = gnorm(b)
    num = gmul(a, gconj(b))
    need(num[0] % n == 0 and num[1] % n == 0, 'Gaussian division exact')
    return (num[0] // n, num[1] // n)


def ggcd(a, b):
    while b != (0, 0):
        n = gnorm(b)
        num = gmul(a, gconj(b))
        q = ((2 * num[0] + n) // (2 * n), (2 * num[1] + n) // (2 * n))
        a, b = b, (a[0] - gmul(q, b)[0], a[1] - gmul(q, b)[1])
    return a


UNITS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def canonical_ray(z):
    g = (0, 0)
    for c in z:
        if c != (0, 0):
            g = c if g == (0, 0) else ggcd(g, c)
    w = tuple(gdiv(c, g) for c in z)
    first = next(c for c in w if c != (0, 0))
    for u in UNITS:
        f = gmul(u, first)
        if f[0] > 0 and f[1] >= 0:
            return tuple(gmul(u, c) for c in w)
    raise RuntimeError('no canonical unit')


def chart(r):
    return ((r[0], r[1]), (r[2], r[3]), (r[4], r[5]), (r[6], r[7]))


def J_vec(x):
    out = []
    for k in range(0, 8, 2):
        out += [-x[k + 1], x[k]]
    return tuple(out)


Z240 = [chart(r) for r in ROOTS]
need(all(sum(gnorm(c) for c in z) == 4 for z in Z240),
     'all 240 charted roots have squared norm 4')
ridx = {r: k for k, r in enumerate(ROOTS)}
line_of = {}
line_reps = []
for k, r in enumerate(ROOTS):
    if k in line_of:
        continue
    orb = [k]
    y = J_vec(r)
    while y != r:
        orb.append(ridx[y])
        y = J_vec(y)
    for j in orb:
        line_of[j] = len(line_reps)
    line_reps.append(k)
need(len(line_reps) == 60 and all(sum(1 for j in range(240) if line_of[j] == L) == 4
                                  for L in range(60)),
     '60 J-lines, each with exactly 4 = |mu4| roots')
RAYS = sorted({canonical_ray(Z240[i]) for i in line_reps})
need(len(RAYS) == 60, '60 distinct canonical Gaussian rays on the same C4')

I4 = s.eye(4)


def projector(z):
    v = s.Matrix([a + s.I * b for a, b in z])
    n = (v.H * v)[0]
    p = (v * v.H / n).applyfunc(s.expand)
    need(p * p == p and p.H == p and s.trace(p) == 1, 'rank-one source projector')
    return p


P = [projector(z) for z in RAYS]
gram = s.Matrix([[s.trace(p * q) for q in P] for p in P])
need(sorted(set(gram)) == [s.Integer(0), s.Rational(1, 4), s.Rational(1, 2), s.Integer(1)],
     'C4 source-ray overlap squares are exactly {0, 1/4, 1/2, 1}')
vec = lambda A: A.reshape(A.rows * A.cols, 1)
Bmat = s.Matrix.hstack(*map(vec, P))
need(Bmat.rank() == 16, 'the 60 source projectors span the full M4 algebra')
need(s.trace(gram) == 60, 'pair Gram trace normalization')

# reflections r_v = 1 - 2 P_v are unitary (the G31 generating set, source side)
need(all((I4 - 2 * p).H * (I4 - 2 * p) == I4 for p in P),
     'all 60 source reflections are unitary on C4')

# ------------------------------------------------- regression anchor 1: trace
a = s.Matrix([1, 0, 0, 0])
b = s.Matrix([1, 0, 1, 0])
c = s.Matrix([1, 0, s.I, 0])
Pa = a * a.H
Pb = b * b.H / 2
Pc = c * c.H / 2


def ray_of(v):
    z = tuple((int(s.re(x)), int(s.im(x))) for x in v)
    return canonical_ray(z)


need(all(ray_of(v) in RAYS for v in (a, b, c)),
     'the oriented triangle uses actual source rays')
need([s.trace(Pa * Pb), s.trace(Pb * Pc), s.trace(Pc * Pa)] == [s.Rational(1, 2)] * 3,
     'three pair overlaps all equal 1/2')
# Documented ordering of the anchor: (Pi0, Pi1, Pi2) = (P_0, P_{+i}, P_+).
Pi0, Pi1, Pi2 = Pa, Pc, Pb
need(s.expand(s.trace(Pi0 * Pi1 * Pi2)) == (1 - s.I) / 4,
     'REGRESSION: tr(Pi0 Pi1 Pi2) = (1-i)/4 (documented ordered triple)')
need(s.expand(s.trace(Pa * Pb * Pc)) == (1 + s.I) / 4,
     'reverse orientation tr(P0 P+ P+i) = (1+i)/4 (conjugate)')
need(s.expand(s.trace(Pi0 * Pi1 * Pi2)) != s.conjugate(s.expand(s.trace(Pi0 * Pi1 * Pi2))),
     'negative control: scalar pair data cannot choose an orientation')

# --------------------------------------- regression anchor 2: reflection words
R0 = I4 - 2 * Pa
Rplus = I4 - 2 * Pb
Ri = I4 - 2 * Pc
forward = (R0 * Rplus * Ri).applyfunc(s.expand)
reverse = (R0 * Ri * Rplus).applyfunc(s.expand)
need(forward == s.diag(-s.I, 1, -s.I, 1), 'REGRESSION: forward reflection word R0 R+ Ri = diag(-i,1,-i,1)')
need(reverse == s.diag(s.I, 1, s.I, 1), 'REGRESSION: reversed reflection word R0 Ri R+ = diag(i,1,i,1)')
probe = s.Matrix([1, 1, 0, 0])
readout = s.Matrix([1, s.I, 0, 0])
Pprobe = probe * probe.H / 2
Pread = readout * readout.H / 2
need(ray_of(probe) in RAYS and ray_of(readout) in RAYS,
     'internal reference and readout are original source rays')
p_forward = s.expand(s.trace(Pread * forward * Pprobe * forward.H))
p_reverse = s.expand(s.trace(Pread * reverse * Pprobe * reverse.H))
need(p_forward == 1 and p_reverse == 0,
     'REGRESSION: reflection-word witness answers are exactly 1 and 0')
need((forward * Pa * forward.H).applyfunc(s.expand) == Pa
     and (reverse * Pa * reverse.H).applyfunc(s.expand) == Pa,
     'without the cross-block reference the probe cannot see the phase')

result = {
    'status': 'PASS',
    'guards': len(checks),
    'exact_guards': sum(1 for _, k in checks if k == 'exact'),
    'numerical_guards': sum(1 for _, k in checks if k == 'numeric'),
    'checks': [{'name': n, 'kind': k} for n, k in checks],
    'source_objects': {
        'C3_word_algebra': {'words': WORD_NAMES, 'dimension': 7, 'products_closed': 49,
                            'coordinate_determinant': -81,
                            'dagger_completion_dimension': 9,
                            'adjunction_closed': False,
                            'type': 'Darstellung der Quellalgebra auf demselben C3; '
                                    'kein dokumentierter Lift auf den 64-Fermion-Traeger'},
        'C4_gauss_rays': {'rays': 60, 'roots': 240, 'mu4_lifts_per_ray': 4,
                          'overlap_squares': ['0', '1/4', '1/2', '1'],
                          'projector_span_dimension': 16,
                          'reflections_unitary': True,
                          'type': 'unitaere Quelloperationen auf demselben C4; '
                                  'Gamma-Lift-Kandidaten ohne dokumentierte CAR-Chart-Zuordnung'}},
    'regression_anchors': {
        'ordered_triple': {'ordering': ['P_0', 'P_+i', 'P_+'], 'value': '(1-i)/4',
                           'reverse_value': '(1+i)/4'},
        'reflection_word_witness': {'forward': 'diag(-i,1,-i,1)', 'reverse': 'diag(i,1,i,1)',
                                    'born_forward': 1, 'born_reverse': 0,
                                    'note': 'Artefakte der separaten Reflexionswort-Transferaufgabe '
                                            '(TFPT-Universalraum-Forschungspaper) bleiben pending; '
                                    'hier nur die dokumentierten Werte als Wachen'}},
    'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'runtime_seconds': round(time.time() - T0, 3),
}
print(json.dumps(result, indent=2))
