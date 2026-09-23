"""Read-only independent reconstruction of the other session's small core.

No importing/running the worker's programs and no writing its artifacts.
The source tensor is rebuilt from exterior-algebra signs before comparison.
Integer identities are exact; the result does not prove a physical source.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import numpy as np
import sympy as sp

SOURCE = Path('/Users/stefanhamann/Documents/Codex/2026-09-14/scha-3/outputs/simple_core/spinor_tensors.npz')
checks = []

def require(ok, name):
    if not ok:
        raise RuntimeError(name)
    checks.append(name)

def same(a, b, name):
    require(np.array_equal(a, b), name)

even = [m for m in range(32) if m.bit_count() % 2 == 0]
ann = []
for j in range(5):
    a = np.zeros((32, 32), dtype=np.int64)
    for m in range(32):
        occupied = [k for k in range(5) if (m >> k) & 1]
        if j in occupied:
            a[m ^ (1 << j), m] = (-1) ** occupied.index(j)
    ann.append(a)
C = np.eye(32, dtype=np.int64)
for a in ann:
    C = C @ (a + a.T)
beta = [(C @ a)[np.ix_(even, even)] for a in ann + [a.T for a in ann]]
D = [beta[j] + beta[j + 5] for j in range(5)]
for i, j in product(range(5), repeat=2):
    same(D[i] @ D[j] + D[j] @ D[i],
         (2 if i == j else 0) * np.eye(16, dtype=np.int64), f'CAR bilinear {i},{j}')

pairs = list(combinations(range(64), 2))
colors = list(combinations(range(4), 2))
W = np.zeros((60, len(pairs)), dtype=np.int64)
Wplus = np.zeros_like(W)
for k, b in enumerate(beta):
    for c, (a, d) in enumerate(colors):
        for j, (u, v) in enumerate(pairs):
            s, x = divmod(u, 4)
            t, y = divmod(v, 4)
            wedge = int(x == a and y == d) - int(x == d and y == a)
            W[6*k+c, j] = b[s, t] * wedge
            Wplus[6*k+c, j] = abs(b[s, t]) * wedge
with np.load(SOURCE, allow_pickle=False) as source:
    same(W, source['W'], 'reconstructed native tensor matches independent-session artifact')
    same(Wplus, source['Wflat'], 'positive replacement has same declared input basis')
same(W @ W.T, 8*np.eye(60, dtype=np.int64), 'native row Gram')
same(Wplus @ Wplus.T, 8*np.eye(60, dtype=np.int64), 'positive row Gram')
same(Wplus @ W.T, np.zeros((60,60),dtype=np.int64), 'orthogonal bright subspaces')
require(np.count_nonzero(W) == 480, '480 unordered nonzero root pairs')

# All additive conserved charges: reconstruct rather than trusting report.
cw = np.array([[(1 if not (m >> j) & 1 else -1) for j in range(3)]
               for m in range(8) if m.bit_count() % 2 == 0], dtype=np.int64)
roots = np.array([[1-2*((m>>j)&1) for j in range(5)] + list(c)
                  for m in even for c in cw], dtype=np.int64)  # twice roots
broots = []
for j in range(10):
    v = [0]*5
    v[j%5] = -2 if j < 5 else 2
    for a,b in colors:
        broots.append(v + list(cw[a] + cw[b]))
broots = np.array(broots,dtype=np.int64)
equations = []
for row,col in zip(*np.nonzero(W)):
    u,v = pairs[col]
    same(roots[u]+roots[v], broots[row], 'weight conservation on coupling')
    eq = np.zeros(124,dtype=np.int64)
    eq[u] = eq[v] = 1
    eq[64+row] = -1
    equations.append(eq)
A = np.array(equations)
Q = np.vstack([np.column_stack([roots.T,broots.T]),
               np.r_[np.ones(64,dtype=int),2*np.ones(60,dtype=int)]])
same(A @ Q.T, np.zeros((480,9),dtype=np.int64), 'eight weights and pair number conserved')
require(sp.Matrix(Q).rank() == 9, 'nine rational independent nullvectors')
F = (A % 2).astype(np.uint8)
rank = 0
for col in range(F.shape[1]):
    idx = np.flatnonzero(F[rank:,col])
    if not len(idx):
        continue
    p = rank + int(idx[0])
    F[[rank,p]] = F[[p,rank]]
    for r in range(rank+1,len(F)):
        if F[r,col]:
            F[r] ^= F[rank]
    rank += 1
require(rank == 115, 'rational rank at least115 modulo2 and at most115 by nine nullvectors')
for s in range(16):
    desired = [int(u//4 == s) for u in range(64)]
    require(sp.Matrix(np.vstack([Q[:,:64],desired])).rank() == 10,
            f'no additive charge extends spinor-place occupancy {s}')

# Verify the decisive non-diagonal-adapter obstruction on its exact line.
t = sp.Symbol('t')
T = [sp.Matrix(abs(d)) for d in D]
detline = (t*T[0]+2*T[1]+4*T[2]+8*T[3]+16*T[4]).det(method='domain-ge')
target = sp.prod(t*t-r*r for r in [2,6,10,14,18,22,26,30])
require(sp.expand(detline-target) == 0, 'positive determinant line')
require(sp.gcd(detline,sp.diff(detline,t)) == 1, 'simple roots cannot be eighth-power quadratic')

eps = Fraction(1,20)
maximum = 32*eps*eps/(1+32*eps*eps)
require(maximum == Fraction(2,27), 'native weak-coupling conversion maximum')
require(32*Fraction(1,10)**2/(1+32*Fraction(1,10)**2) == Fraction(8,33),
        'symmetry leaves observable dimensionless coupling choice')
print(json.dumps({
    'status':'PASS', 'exact_checks':len(checks),
    'source':str(SOURCE), 'source_sha256':sha256(SOURCE.read_bytes()).hexdigest(),
    'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'native_row_gram':'8 I60', 'positive_cross_gram':'0',
    'one_pair_characteristic_polynomial':'E^1956 (E^2-Delta E-8g^2)^60',
    'same_input_maximum_native':str(maximum), 'same_input_maximum_positive':'0',
    'additive_charge_dimension':9,
    'additive_charge_basis':'eight E8 Cartan weights plus Nf+2Nb',
    'sixteen_vertex_number_extensions':False,
    'scope':'finite signed coupling, charge classification and one-pair sector',
    'not_independently_recomputed':['full-Fock ground-state moment certificate',
        '960 cocycle phase equations','continuum','physical parameter selection'],
    'full_T1_T8_closed':False},indent=2))
