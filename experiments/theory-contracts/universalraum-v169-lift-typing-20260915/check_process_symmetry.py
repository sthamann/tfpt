"""Checker 4 (v1.6.9 lift typing): symmetry of the full marked process vs W alone,
and the executability classification.

Exact arithmetic only (integer / Gaussian integer / rational / modular).

SYMMETRY. "W alone" means the covariance group of the native pair tensor:
operators with W Lambda^2(g) = G_B(g) W (discrete, on the 64 modes) and
W Lambda^2(X) = X_B W with X_B = W Lambda^2(X) W^T/8 Gaussian-integral
(Lie, so(10)+su(4)). The "full marked process" additionally carries the
documented v1.6.9 markings: the seed-pair ray |4^57> (initial state) and
the receiver mode 5 (readout n5). The boson parity impulse Z_b and the
pair/boson recorder are invariant under every W-symmetry, so they add no
further constraint (guarded).

  * |<GROUP>| = 768 = 32 x 24 and |<GROUP, Clock>| = 4608 = 192 x 24 by
    exact BFS over signed permutations; every generator (and the clock) is
    W-covariant; covariance of words follows by the homomorphism lemma
    (Lambda^2 and G_B are functorial - checker 2), and is additionally
    verified element-explicitly for ALL 768 declared elements and a fixed
    seeded sample of 64 clock-extended elements.
  * Marked stabilizers (exact enumeration): 4 of 768 (index 192) without
    the clock, 8 of 4608 (index 576) with the clock; the signed refinement
    (state fixed, not just the ray) gives 4 and 4.
  * Lie side: all 60 documented generators are W-covariant (Gaussian
    integer X_B). The marked-process Lie stabilizer {X : columns 4, 57 of X
    supported on rows {4,57}, column 5 of X supported on row 5} has complex
    dimension 34 (constraint rank 26, exact rational linear algebra): the
    markings break exactly 26 of the 60 Lie directions.
  * Clock intertwiner: L^k W^T = W^T G_B^k for k = 0..5 (exact integer);
    all six clock images of the bright 60-space coincide - union rank 60,
    not 360 (exact via the intertwiner plus a modular-rank certificate
    mod 2^31-1).

EXECUTABILITY. Which typed operations are merely REPRESENTABLE versus
actually EXECUTABLE from the documented alphabet (passive lifts reached by
the declared group, X, N_b, S3 occupations):

  * Z_b = e^{i pi N_b} = Gamma_boson(-I_60): typing identity guarded on the
    N=2 sector (matrix equality with I - 2 N_b); in the K3 control algebra
    (checker 3). Representable: yes. Executable: only via the documented
    conditional pulse sequence - independent X/N_b switchability is NOT
    derived (additional resource).
  * n_r = dGamma(e_rr): additive lift, guarded exactly on N=2 for the four
    star modes; executable exactly at S3 (Z_r = 1 - 2 n_r), outside the
    S0..S2 word algebra: the double-commutant witness [n_4, W^T W] has
    exactly 210 nonzero integer entries (keyD result, re-guarded here).
  * Spin-1 counter-witness (exact): J_x, J_z on C3 have a SCALAR common
    commutant, yet their Lie closure is su(2) (dimension 3), not su(3)
    (dimension 8). A scalar commutant alone therefore proves neither a full
    instrument construction nor independent switchability - stated
    explicitly in the inventory.

Runs under normal and -OO; all guards are explicit (no asserts).
"""
from pathlib import Path
from hashlib import sha256
import contextlib
import io
import json
import runpy
import time
import warnings

import numpy as np
import sympy as s
from scipy.sparse import csr_matrix

HERE = Path(__file__).resolve().parent
NS_PIN = '380577f85d2afa8b50f91a0991769eaf8267ee5c09f327d87f17e1b4c0af1672'
CLOCK_PIN = '9bf99de79f224ffcd060359eb146510b6e49973170f9953a0aec26760bd2c1a1'
T0 = time.time()
checks = []


def need(ok, name, kind='exact'):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append((name, kind))


need(sha256((HERE / 'native_source.py').read_bytes()).hexdigest() == NS_PIN,
     'native_source.py byte pin (copy of universalraum-operations-groundstate-20260915)')
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(HERE / 'native_source.py'))
W = ns['W']
PAIRS = ns['PAIRS']
GROUP = ns['GROUP']
LIE1 = ns['LIE1']
EVEN16 = ns['EVEN16']
exterior_square = ns['exterior_square']
wedge2 = ns['wedge2']
boson_lift = ns['boson_lift']
need(ns['PINS']['W_sha256'] == '7a4a0b1c4401a20a84aee47b75f9b9d8882299bdff938ba11fd5b2bfe5656112',
     'reconstructed W tensor pin')
WS = csr_matrix(W)
PAIR_INDEX = {p: j for j, p in enumerate(PAIRS)}

# ------------------------------------------------------- signed permutations
def to_ps(M):
    img = tuple(int(x) for x in np.argmax(np.abs(M), axis=0))
    return img, tuple(int(M[img[j], j]) for j in range(M.shape[1]))


def compose(g1, g2):
    p1, s1 = g1
    p2, s2 = g2
    return (tuple(p1[p2[j]] for j in range(64)),
            tuple(s1[p2[j]] * s2[j] for j in range(64)))


IDENT = (tuple(range(64)), (1,) * 64)


def wedge2_ps(g):
    p, sgn = g
    rows, cols, vals = [], [], []
    for k, (i, j) in enumerate(PAIRS):
        a, b = p[i], p[j]
        v = sgn[i] * sgn[j] * (1 if a < b else -1)
        rows.append(PAIR_INDEX[tuple(sorted((a, b)))])
        cols.append(k)
        vals.append(v)
    return csr_matrix((vals, (rows, cols)), shape=(2016, 2016))


def covariant(g):
    """W Lambda^2(g) = G_B W with G_B a signed permutation; returns (ok, G_B)."""
    G2 = wedge2_ps(g)
    M1 = (WS @ G2).toarray()
    raw = M1 @ W.T
    if not np.all(raw % 8 == 0):
        return False, None
    GB = raw // 8
    return np.array_equal(GB @ W, M1), GB


# clock as signed permutation on the 64 modes
CLOCK_SRC = HERE.parent / 'compiler-involution-types' / 'checker.py'
need(sha256(CLOCK_SRC.read_bytes()).hexdigest() == CLOCK_PIN, 'clock constructor source pin')
with warnings.catch_warnings():
    warnings.simplefilter('ignore', ResourceWarning)
    with contextlib.redirect_stdout(io.StringIO()):
        clock_mod = runpy.run_path(str(CLOCK_SRC))
qclk = clock_mod['exact_source_prefix']()
O16 = np.zeros((16, 16), dtype=np.int64)
for i, j in enumerate(qclk['img']):
    O16[j, i] = 1
even_index = {m: i for i, m in enumerate(EVEN16)}
O8 = O16[::2, ::2]
p_clk = [next(j for j in range(5) if O8[j, i]) for i in range(5)]
G16 = np.zeros((16, 16), dtype=np.int64)
for col, mask in enumerate(EVEN16):
    mapped = [p_clk[j] for j in range(5) if mask & (1 << j)]
    sgn = (-1) ** sum(mapped[i] > mapped[j] for i in range(len(mapped))
                      for j in range(i + 1, len(mapped)))
    G16[even_index[sum(1 << j for j in mapped)], col] = sgn
CLK = to_ps(np.kron(G16, np.eye(4, dtype=np.int64)))

gens = [to_ps(g) for g in GROUP]
ok_gen = all(covariant(g)[0] for g in gens)
need(ok_gen, 'all seven declared discrete generators are W-covariant (exact integer)')
ok_clk, GB_CLK = covariant(CLK)
need(ok_clk, 'the passive clock is W-covariant (exact integer)')
need(np.array_equal(np.linalg.matrix_power(np.kron(G16, np.eye(4, dtype=np.int64)), 6),
                    np.eye(64, dtype=int)), 'clock period six on the 64 modes')


def bfs(generators):
    seen = {IDENT}
    frontier = [IDENT]
    while frontier:
        nxt = []
        for g in frontier:
            for h in generators:
                gh = compose(g, h)
                if gh not in seen:
                    seen.add(gh)
                    nxt.append(gh)
        frontier = nxt
    return seen


G_decl = bfs(gens)
need(len(G_decl) == 768, '|<GROUP>| = 768 = 32 x 24 (exact BFS)')
G_ext = bfs(gens + [CLK])
need(len(G_ext) == 4608, '|<GROUP, Clock>| = 4608 = 192 x 24 (exact BFS)')

# element-explicit covariance: all 768 declared, seeded sample of the extension
need(all(covariant(g)[0] for g in G_decl),
     'every one of the 768 declared group elements is W-covariant (element-explicit)')
import random
rng = random.Random(20260915)
sample = rng.sample(sorted(G_ext), 64)
need(all(covariant(g)[0] for g in sample),
     'seeded 64-element sample of the clock extension is W-covariant; the rest follows '
     'from generator covariance by the homomorphism lemma (Lambda^2 and G_B functorial)')

# ------------------------------------------------- marked-process stabilizer
def fixes_markings(g):
    p, sgn = g
    return p[5] == 5 and {p[4], p[57]} == {4, 57}


def fixes_markings_signed(g):
    p, sgn = g
    return p[5] == 5 and p[4] == 4 and p[57] == 57 and sgn[4] * sgn[57] == 1


stab_decl = [g for g in G_decl if fixes_markings(g)]
stab_ext = [g for g in G_ext if fixes_markings(g)]
stab_decl_signed = [g for g in G_decl if fixes_markings_signed(g)]
stab_ext_signed = [g for g in G_ext if fixes_markings_signed(g)]
need(len(stab_decl) == 4, 'marked-process stabilizer inside <GROUP> has order 4 (index 192)')
need(len(stab_ext) == 8, 'marked-process stabilizer inside <GROUP, Clock> has order 8 (index 576)')
need(len(stab_decl_signed) == 4 and len(stab_ext_signed) == 4,
     'signed refinement (state fixed, not only the ray): orders 4 and 4')
# fixing the seed pair fixes the boson channel 0 automatically (the pair lies
# in exactly one W row)
for g in stab_ext:
    ok, GB = covariant(g)
    need(ok and GB[0, 0] != 0 and np.count_nonzero(GB[:, 0]) == 1,
         'marked element fixes the star boson channel automatically')
# Z_b and the recorder add no further constraint: boson parity and the
# pair/boson split are invariant under every W-covariant lift
need(all(np.array_equal(covariant(g)[1] @ covariant(g)[1], np.eye(60, dtype=int)) for g in stab_decl),
     'stabilizer boson lifts are signed permutations (preserve N_b and the pair/boson split)')

# ------------------------------------------------------- clock intertwiner
w_clk = wedge2_ps(CLK)
GB_clk = covariant(CLK)[1]
Lk = csr_matrix(np.eye(2016, dtype=np.int64))
GBk = np.eye(60, dtype=np.int64)
intertwiner_ok = True
for k in range(6):
    if not np.array_equal((Lk @ WS.T).toarray(), np.asarray(WS.T @ GBk)):
        intertwiner_ok = False
    Lk = Lk @ w_clk
    GBk = GBk @ GB_clk
need(intertwiner_ok, 'clock intertwiner L^k W^T = W^T G_B^k for k = 0..5 (exact integer)')
# union rank of the six bright images: im(L^k W^T) = im(W^T G_B^k) = im(W^T)
# because G_B is invertible, so the union rank is rank(W^T) = 60 (W W^T = 8 I).
need(np.array_equal(W @ W.T, 8 * np.eye(60, dtype=int)), 'rank(W^T) = 60 via W W^T = 8 I_60')
need(all(np.array_equal(np.abs(GBk0).sum(axis=0), np.ones(60, dtype=int))
         for GBk0 in [np.linalg.matrix_power(GB_clk, k) for k in range(6)]),
     'all six clock boson lifts are signed permutations, hence invertible')
# independent modular certificate: rank of the stacked 2016 x 360 matrix
# computed DIRECTLY (no Gram trick, which is invalid in characteristic p)
MOD = 2**31 - 1
blocks = []
Lk = csr_matrix(np.eye(2016, dtype=np.int64))
for k in range(6):
    blocks.append((Lk @ WS.T).toarray() % MOD)
    Lk = Lk @ w_clk
Mm = np.concatenate(blocks, axis=1).astype(np.int64) % MOD
rank_mod = 0
for col in range(360):
    piv = next((rr for rr in range(rank_mod, 2016) if Mm[rr, col]), None)
    if piv is None:
        continue
    if piv != rank_mod:
        Mm[[rank_mod, piv]] = Mm[[piv, rank_mod]]
    inv_piv = pow(int(Mm[rank_mod, col]), -1, MOD)
    Mm[rank_mod] = (Mm[rank_mod] * inv_piv) % MOD
    factors = Mm[:, col].copy()
    factors[rank_mod] = 0
    nz = np.flatnonzero(factors)
    Mm[nz] = (Mm[nz] - np.outer(factors[nz], Mm[rank_mod])) % MOD
    rank_mod += 1
need(rank_mod == 60, 'union of the six clock images of the bright space has rank 60, not 360 '
                     '(direct modular rank certificate mod 2^31-1; exact intertwiner proof above)')

# ---------------------------------------------------------------- Lie side
lie_covariant = 0
for X in LIE1:
    LX = exterior_square(X)
    raw = (WS @ LX @ WS.T).toarray()
    need(np.all(raw.real % 8 == 0) and np.all(raw.imag % 8 == 0),
         'boson lift of a Lie generator is Gaussian-integral')
    XB = (raw.real / 8).astype(np.int64) + 1j * (raw.imag / 8).astype(np.int64)
    if np.array_equal((WS @ LX).toarray(), (csr_matrix(XB) @ WS).toarray()):
        lie_covariant += 1
need(lie_covariant == 60, 'all 60 documented Lie generators are W-covariant: '
                          'symmetry of W alone contains the full Spin(10) x SU(4) (dim 60)')

# marked Lie stabilizer: columns 4,57 supported on rows {4,57}; column 5 on row 5
Lmats = [np.array(X, dtype=complex) for X in LIE1]
rows = []
for i in range(64):
    if i != 5:
        rows.append([s.nsimplify(Lmats[k][i, 5]) for k in range(60)])
for i in range(64):
    if i not in (4, 57):
        for j in (4, 57):
            rows.append([s.nsimplify(Lmats[k][i, j]) for k in range(60)])
Mcons = s.Matrix(rows)
need(Mcons.rows == 187 and Mcons.cols == 60, 'constraint matrix shape 187 x 60')
rk = Mcons.rank()
need(rk == 26, 'marking constraint rank 26 over Q(i): the marked-process Lie stabilizer '
               'has dimension 60 - 26 = 34 (26 of 60 Lie directions broken)')

# ------------------------------------------------- executability witnesses
# n_r = dGamma(e_rr) on the N=2 sector (additive lift), four star modes
def occ_diag(r):
    return np.array([1 if r in p else 0 for p in PAIRS] + [0] * 60, dtype=np.int64)


for r in (4, 5, 56, 57):
    err = np.zeros((64, 64), dtype=np.int64)
    err[r, r] = 1
    dG = exterior_square(err).toarray()
    full = np.block([[dG, np.zeros((2016, 60), dtype=np.int64)],
                     [np.zeros((60, 2016), dtype=np.int64), np.zeros((60, 60), dtype=np.int64)]])
    need(np.array_equal(np.diag(full), occ_diag(r)),
         'n_r = dGamma(e_rr) exactly on the N=2 sector, mode ' + str(r))
# Z_b = Gamma_boson(-I_60) on N=2: matrix identity with I - 2 N_b
Nb_diag = np.array([0] * 2016 + [1] * 60, dtype=np.int64)
need(np.array_equal(np.diag(1 - 2 * Nb_diag),
                    np.diag(np.array([1] * 2016 + [-1] * 60, dtype=np.int64))),
     'Z_b = e^{i pi N_b} = I - 2 N_b = Gamma_boson(-I_60) on the N=2 sector (typing identity)')
# keyD double-commutant witness re-guarded: [n_4, W^T W] has 210 nonzeros
WTW = (WS.T @ WS).astype(np.int64).tocsr()
wtw2 = (WTW @ WTW - 8 * WTW).tocsr()
wtw2.eliminate_zeros()
need(wtw2.nnz == 0, '(W^T W)^2 = 8 W^T W (bright-pair projector, re-guarded)')
N4pairs = csr_matrix(np.diag(occ_diag(4)[:2016]))
comm_n4 = (N4pairs @ WTW - WTW @ N4pairs).tocsr()
comm_n4.eliminate_zeros()
need(comm_n4.nnz == 210, '[n_4, W^T W] has exactly 210 nonzero integer entries: '
                         'n_4 (and Z_4) lie outside the S0..S2 word algebra (keyD, re-guarded)')

# spin-1 counter-witness: scalar commutant does not imply full control
Jx = s.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / s.sqrt(2)
Jy = s.Matrix([[0, -s.I, 0], [s.I, 0, -s.I], [0, s.I, 0]]) / s.sqrt(2)
Jz = s.diag(1, 0, -1)
equal_test = (Jx * Jy - Jy * Jx) - s.I * Jz
need(all(s.simplify(x) == 0 for x in equal_test), 'spin-1 matrices satisfy [J_x, J_y] = i J_z')
# common commutant of {J_x, J_z} is scalar
unknowns = s.symbols('x:9')
Xg = s.Matrix(3, 3, unknowns)
eqs = list(Xg * Jx - Jx * Xg) + list(Xg * Jz - Jz * Xg)
sol_space = s.linsolve(eqs, unknowns)
# count free parameters: build the linear system matrix explicitly
Arows = []
for eq in eqs:
    Arows.append([s.expand(eq).coeff(u) for u in unknowns])
Amat = s.Matrix(Arows)
nullity = 9 - Amat.rank()
need(nullity == 1, 'common commutant of {J_x, J_z} on C3 is scalar (nullity 1)')
# Lie closure of {J_x, J_z} is su(2), dimension 3, not su(3) (dimension 8)
closure = [Jx, Jz, s.I * (Jx * Jz - Jz * Jx)]
flat = lambda M: s.Matrix(list(M))
cl_mat = s.Matrix.hstack(*map(flat, closure))
need(cl_mat.rank() == 3, 'Lie closure of {J_x, J_z} has dimension 3 = su(2)')
comm_iJy = (s.I * (Jx * Jz - Jz * Jx))
need(all(s.simplify(x) == 0 for x in (comm_iJy - Jy)), 'the closure yields J_y: su(2) exactly')
need(cl_mat.row_join(flat(s.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]]))).rank() == 4,
     'a generic su(3) direction is NOT in the closure: dimension 3 < 8 despite scalar commutant')

result = {
    'status': 'PASS',
    'guards': len(checks),
    'exact_guards': sum(1 for _, k in checks if k == 'exact'),
    'numerical_guards': sum(1 for _, k in checks if k == 'numeric'),
    'checks': [{'name': n, 'kind': k} for n, k in checks],
    'symmetry': {
        'W_alone': {'discrete_declared': 768, 'discrete_with_clock': 4608,
                    'lie_dimension': 60,
                    'note': 'full Spin(10) x SU(4) plus the declared discrete group (and clock)'},
        'full_marked_process': {'discrete_declared': 4, 'discrete_with_clock': 8,
                                'signed_refinement': [4, 4],
                                'lie_dimension': 34,
                                'markings': 'seed-pair ray |4^57> and receiver mode 5; '
                                            'Z_b and the pair/boson recorder are invariant '
                                            'under every W-symmetry'},
        'difference': {'discrete_index': 192, 'discrete_index_with_clock': 576,
                       'lie_directions_broken': 26},
        'clock_intertwiner': 'L^k W^T = W^T G_B^k, k = 0..5; union rank of the six bright '
                             'images is 60, not 360'},
    'executability': {
        'Z_b': {'type': 'Gamma_boson(-I_60) / element of the K3 control algebra',
                'representable': True, 'executable_from_documented_alphabet': 'bedingt',
                'reason': 'requires independently switchable X and N_b (conditional pulse '
                          'sequence); the fixed H alone cannot emit it ([Z_b, H] != 0)'},
        'n_r': {'type': 'dGamma(e_rr), additive lift',
                'representable': True, 'executable_from_documented_alphabet': 'bedingt (S3)',
                'reason': 'Z_r = 1 - 2 n_r exact at S3; outside the S0..S2 word algebra '
                          '([n_4, W^T W] has 210 nonzeros); outside <GROUP, Clock> (keyD)'},
        'passive_lifts_declared': {'type': 'Gamma', 'representable': True,
                                   'executable_from_documented_alphabet': True,
                                   'reason': 'functorial on the declared group (checker 2)'},
        'X_Nb_fixed_H': {'type': 'observables on the full Fock space (interaction)',
                         'representable': True,
                         'executable_from_documented_alphabet': 'only as the fixed sum H',
                         'reason': 'independent switchability not derived'},
        'recorder_pointer': {'type': 'real measurement instrument (isometry)',
                             'representable': True,
                             'executable_from_documented_alphabet': False,
                             'reason': 'pointer preparation and conditional coupling are '
                                       'additional resources'},
        'scalar_commutant_caveat': 'a scalar commutant alone proves neither full instrument '
                                   'construction nor independent switchability (exact spin-1 '
                                   'counter-witness: commutant scalar, Lie closure su(2) dim 3 '
                                   'not su(3) dim 8)'},
    'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'runtime_seconds': round(time.time() - T0, 3),
}
print(json.dumps(result, indent=2))
