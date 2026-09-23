"""Checker 2 (v1.6.9 lift typing): exact multiparticle distinctions on the native carrier.

On the native 64-fermion carrier (byte-pinned in-repo source, no npz) with
its two-particle space Lambda^2(C64) (2016 dimensions) and the boson lift
G_B on C60:

  (M1) dGamma is NOT multiplicative: dGamma(AB) != dGamma(A)dGamma(B) in
       general. Exact counterexample with matrix units A = e_01, B = e_10 on
       the native carrier: the difference has exactly ONE nonzero entry,
       [dGamma(AB) - dGamma(A)dGamma(B)]_{(0,1),(0,1)} = +1 (integer).
       Native witness with two documented Spin(10) Lie generators L0, L1:
       the difference has exactly 3968 nonzero Gaussian-integer entries.
       The general identity is guarded exactly:
           dGamma(A)dGamma(B) - dGamma(AB) = cross(A, B),
           cross(A, B)(v^w) = Av^Bw + Bv^Aw.
       The PRESERVED relation is the Lie homomorphism
       [dGamma(A), dGamma(B)] = dGamma([A, B]), guarded exactly for L0, L1.

  (M2) Pi^2 = Pi does NOT imply dGamma(Pi) is a projector. Exact
       counterexample on the native carrier with the seed-pair mode
       projector Pi = e_44 + e_5757 of the marked v1.6.9 process:
       dGamma(Pi)|4^57> = 2|4^57> but dGamma(Pi)^2|4^57> = 4|4^57>;
       dGamma(Pi)^2 - dGamma(Pi) has exactly one nonzero entry.
       Negative control: a rank-ONE projector does not discriminate on
       Lambda^2 (a wedge pair contains a fixed mode at most once, so the
       eigenvalues stay in {0,1}); the distinction needs rank >= 2.

  (M3) The unitary Fock lift IS functorial: Gamma(UV) = Gamma(U)Gamma(V),
       proved exactly on the carrier for all 49 pairs of the seven declared
       discrete source-symmetry generators, on Lambda^2 AND on the boson
       lift G_B, plus all six powers of the passive clock. Since every group
       element is a word in the generators, pairwise functoriality on the
       generators implies functoriality on the whole generated group by
       induction on word length (stated and used, not sampled).

Typing consequence recorded for the inventory: dGamma is a Lie-algebra
representation (additive second quantization), Gamma is a group
homomorphism (unitary Fock lift); confusing the two is exactly the
multiparticle error excluded here.

Runs under normal and -OO; all guards are explicit (no asserts).
"""
from pathlib import Path
from hashlib import sha256
import contextlib
import io
import json
import runpy
import time

import numpy as np
from scipy.sparse import csr_matrix

HERE = Path(__file__).resolve().parent
NS_PIN = '380577f85d2afa8b50f91a0991769eaf8267ee5c09f327d87f17e1b4c0af1672'
W_NPZ_PIN = '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763'
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
exterior_square = ns['exterior_square']
wedge2 = ns['wedge2']
boson_lift = ns['boson_lift']
need(ns['PINS']['W_sha256'] == '7a4a0b1c4401a20a84aee47b75f9b9d8882299bdff938ba11fd5b2bfe5656112',
     'reconstructed W tensor pin (npz archive pin 3f00a089... verified byte-exactly in earlier rounds)')
need(np.array_equal(W @ W.T, 8 * np.eye(60, dtype=int)), 'native row Gram W W^T = 8 I_60 (re-guarded)')
PAIR_INDEX = {p: j for j, p in enumerate(PAIRS)}

# --------------------------------------------------------------------- (M1)
A = np.zeros((64, 64), dtype=np.int64)
A[0, 1] = 1                      # A e_1 = e_0
B = np.zeros((64, 64), dtype=np.int64)
B[1, 0] = 1                      # B e_0 = e_1
AB = A @ B                       # = e_00
need(np.array_equal(AB, np.diag([1] + [0] * 63)), 'A B = e_00 exactly')
dA, dB, dAB = exterior_square(A), exterior_square(B), exterior_square(AB)
diff = (dAB - dA @ dB).tocsr()
diff.eliminate_zeros()
need(diff.nnz == 1, 'dGamma(AB) - dGamma(A)dGamma(B) has exactly one nonzero entry')
k01 = PAIR_INDEX[(0, 1)]
need(int(diff[k01, k01]) == 1,
     'the single discriminating entry is [dG(AB)-dG(A)dG(B)]_{(0,1),(0,1)} = +1')

# general cross-term identity dG(A)dG(B) - dG(AB) = cross(A,B)
def cross(A, B):
    rows, cols, data = [], [], []
    la = [[(int(i), int(A[i, j])) for i in np.flatnonzero(A[:, j])] for j in range(64)]
    lb = [[(int(i), int(B[i, j])) for i in np.flatnonzero(B[:, j])] for j in range(64)]
    for k, (v, w) in enumerate(PAIRS):
        for i, x in la[v]:
            for j, y in lb[w]:
                if i != j:
                    rows.append(PAIR_INDEX[tuple(sorted((i, j)))])
                    cols.append(k)
                    data.append(x * y * (1 if i < j else -1))
        for i, x in lb[v]:
            for j, y in la[w]:
                if i != j:
                    rows.append(PAIR_INDEX[tuple(sorted((i, j)))])
                    cols.append(k)
                    data.append(x * y * (1 if i < j else -1))
    return csr_matrix((data, (rows, cols)), shape=(2016, 2016))


resid = (dA @ dB - dAB - cross(A, B)).tocsr()
resid.eliminate_zeros()
need(resid.nnz == 0, 'exact identity dG(A)dG(B) - dG(AB) = cross(A,B) on Lambda^2')

# native witness with two documented Spin(10) Lie generators (Gaussian integer)
L0, L1 = LIE1[0], LIE1[1]
dL0, dL1 = exterior_square(L0), exterior_square(L1)
dL01 = exterior_square(L0 @ L1)
difL = (dL01 - dL0 @ dL1).tocsr()
difL.eliminate_zeros()
need(difL.nnz == 3968, 'native Lie witness: dG(L0 L1) - dG(L0)dG(L1) has exactly 3968 nonzeros')
need(not np.array_equal(np.array(L0 @ L1), np.array(L1 @ L0)),
     'the two native Lie generators do not commute (context for the cross term)')
# the PRESERVED relation: dGamma is a Lie-algebra homomorphism
comm1 = (dL0 @ dL1 - dL1 @ dL0).tocsr()
dcomm = exterior_square(L0 @ L1 - L1 @ L0)
lie_resid = (comm1 - dcomm).tocsr()
lie_resid.eliminate_zeros()
need(lie_resid.nnz == 0, 'PRESERVED: [dG(L0), dG(L1)] = dG([L0, L1]) exactly (Lie homomorphism)')

# --------------------------------------------------------------------- (M2)
Pi = np.zeros((64, 64), dtype=np.int64)
Pi[4, 4] = 1
Pi[57, 57] = 1                   # seed-pair mode projector of the marked process
need(np.array_equal(Pi @ Pi, Pi), 'Pi = e_44 + e_5757 is a projector (Pi^2 = Pi)')
dPi = exterior_square(Pi)
kseed = PAIR_INDEX[(4, 57)]
need(int(dPi[kseed, kseed]) == 2, 'dG(Pi)|4^57> = 2|4^57> (eigenvalue TWO on the seed pair)')
need(int((dPi @ dPi)[kseed, kseed]) == 4, 'dG(Pi)^2|4^57> = 4|4^57> != 2|4^57>')
d2 = (dPi @ dPi - dPi).tocsr()
d2.eliminate_zeros()
need(d2.nnz == 1 and int(d2[kseed, kseed]) == 2,
     'dG(Pi)^2 - dG(Pi) has exactly one nonzero entry, value +2 at the seed pair: '
     'Pi^2=Pi does NOT imply dG(Pi) is a projector')
P1 = np.zeros((64, 64), dtype=np.int64)
P1[4, 4] = 1
dP1 = exterior_square(P1)
d1 = (dP1 @ dP1 - dP1).tocsr()
d1.eliminate_zeros()
need(d1.nnz == 0, 'negative control: rank-ONE projector stays a projector on Lambda^2 '
                  '(a wedge pair contains a fixed mode at most once); rank >= 2 is needed')

# --------------------------------------------------------------------- (M3)
ok_w = True
ok_b = True
for U in GROUP:
    for V in GROUP:
        UV = U @ V
        if not np.array_equal(wedge2(UV).toarray(), (wedge2(U) @ wedge2(V)).toarray()):
            ok_w = False
        if not np.array_equal(boson_lift(UV), boson_lift(U) @ boson_lift(V)):
            ok_b = False
need(ok_w, 'Gamma(UV) = Gamma(U)Gamma(V) on Lambda^2 for all 49 generator pairs (exact integer)')
need(ok_b, 'Gamma(UV) = Gamma(U)Gamma(V) on the boson lift G_B for all 49 generator pairs (exact integer)')

# clock powers: Gamma(L^k) = Gamma(L)^k on Lambda^2 and on G_B, k = 0..5
CLOCK_SRC = HERE.parent / 'compiler-involution-types' / 'checker.py'
import warnings
CLOCK_PIN = '9bf99de79f224ffcd060359eb146510b6e49973170f9953a0aec26760bd2c1a1'
need(sha256(CLOCK_SRC.read_bytes()).hexdigest() == CLOCK_PIN, 'clock constructor source pin')
with warnings.catch_warnings():
    warnings.simplefilter('ignore', ResourceWarning)
    with contextlib.redirect_stdout(io.StringIO()):
        clock_mod = runpy.run_path(str(CLOCK_SRC))
qclk = clock_mod['exact_source_prefix']()
EVEN16 = ns['EVEN16']
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
CLK64 = np.kron(G16, np.eye(4, dtype=np.int64))
need(np.array_equal(np.linalg.matrix_power(CLK64, 6), np.eye(64, dtype=int)),
     'passive clock has period six on the 64 modes')
w_clk = wedge2(CLK64)
b_clk = boson_lift(CLK64)
w_pow = csr_matrix(np.eye(2016, dtype=np.int64))
b_pow = np.eye(60, dtype=np.int64)
clk_ok = True
for k in range(6):
    Lk = np.linalg.matrix_power(CLK64, k)
    if not np.array_equal(wedge2(Lk).toarray(), w_pow.toarray()):
        clk_ok = False
    if not np.array_equal(boson_lift(Lk), b_pow):
        clk_ok = False
    w_pow = w_pow @ w_clk
    b_pow = b_pow @ b_clk
need(clk_ok, 'Gamma(L^k) = Gamma(L)^k for all six clock powers on Lambda^2 and G_B (exact)')

# Z_r typing identity on the N=2 sector: Gamma(u_r) = Lambda^2(u_r) (+) I_60
# equals the occupation parity 1 - 2 n_r (passive-lift class of the phase).
def occ_diag(r):
    return np.array([1 if r in p else 0 for p in PAIRS] + [0] * 60, dtype=np.int64)


for r in (4, 5):
    u = np.eye(64, dtype=np.int64)
    u[r, r] = -1
    w2 = np.diag(wedge2(u).toarray())
    need(np.array_equal(w2, np.array([-1 if r in p else 1 for p in PAIRS], dtype=np.int64)),
         'Lambda^2(u_r) diagonal is (-1)^{n_r} on every pair')
    full = np.block([[np.diag(w2), np.zeros((2016, 60), dtype=np.int64)],
                     [np.zeros((60, 2016), dtype=np.int64), np.eye(60, dtype=np.int64)]])
    need(np.array_equal(full, np.diag(1 - 2 * occ_diag(r))),
         'Z_r = Gamma(u_r): the phase is the passive Fock lift of the sign flip (typing identity)')

result = {
    'status': 'PASS',
    'guards': len(checks),
    'exact_guards': sum(1 for _, k in checks if k == 'exact'),
    'numerical_guards': sum(1 for _, k in checks if k == 'numeric'),
    'checks': [{'name': n, 'kind': k} for n, k in checks],
    'multiparticle_verdicts': {
        'dGamma_not_multiplicative': {
            'counterexample': 'A = e_01, B = e_10 matrix units on the native C64 carrier',
            'discriminating_number': '[dG(AB)-dG(A)dG(B)]_{(0^1),(0^1)} = +1 (single nonzero entry)',
            'native_lie_witness_nnz': 3968,
            'cross_term_identity': 'dG(A)dG(B) - dG(AB) = cross(A,B), cross(A,B)(v^w)=Av^Bw+Bv^Aw',
            'preserved_relation': '[dG(A), dG(B)] = dG([A,B]) (Lie homomorphism)'},
        'projector_not_lifted': {
            'counterexample': 'Pi = e_44 + e_5757 (seed-pair modes of the marked process)',
            'discriminating_number': 'dG(Pi)|4^57> = 2|4^57>, dG(Pi)^2|4^57> = 4|4^57>; '
                                     'dG(Pi)^2 - dG(Pi) has one nonzero entry (+2)',
            'negative_control': 'rank-1 projector: dG(e_44)^2 = dG(e_44) on Lambda^2 '
                                '(eigenvalues in {0,1}); rank >= 2 needed'},
        'gamma_functorial': {
            'proved': 'Gamma(UV) = Gamma(U)Gamma(V) on Lambda^2 and on G_B',
            'scope': 'all 49 declared-generator pairs plus all six clock powers; '
                     'whole generated group by word-length induction'}},
    'typing_consequence': 'dGamma = additive second quantization (Lie-algebra representation, '
                          'NOT multiplicative); Gamma = unitary Fock lift (group homomorphism, '
                          'functorial); Z_r = Gamma(u_r) is a passive lift, n_r = dG(e_rr) is an '
                          'additive lift; the two types must not be identified',
    'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'runtime_seconds': round(time.time() - T0, 3),
}
print(json.dumps(result, indent=2))
