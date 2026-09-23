"""Checker 1 (v169-controller): closed autonomous model structure.

Exact layer: native star (byte-pinned in-repo source) -> K3 reduction
(h3, B, Zb, E); Zb = I-2B inside the documented (X,Nb) algebra on K3 while
the outdated single-mode Z4 sits outside; recorder coupler C_R and the
dephasing identity D_B = (id + Zb . Zb)/2; pair-coherence preservation.

Numeric layer: the single time-independent H_tot (18-dim, block-diagonal
over the finite controller switch) is Hermitian, branch-preserving, and
reproduces the three v1.6.9 arm unitaries as full operators
(universal scope on K3, not state-specific).

Runs under normal and -OO; explicit guards, no asserts.
"""
from pathlib import Path
from hashlib import sha256
import contextlib
import io
import runpy
import json
import time
import numpy as np
import sympy as sp
from scipy.linalg import expm

import model_core as mc

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
MC_SHA = sha256((HERE / 'model_core.py').read_bytes()).hexdigest()
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(HERE / 'native_source.py'))
W = ns['W']
PAIRS = ns['PAIRS']
need(np.array_equal(W @ W.T, 8 * np.eye(60, dtype=int)), 'WW^T = 8 I_60')

# --- Native star A = 0 and the v1.6.8 interface ------------------------------
columns = list(map(int, np.flatnonzero(W[0])))
leaves = [PAIRS[c] for c in columns]
signs = [int(W[0, c]) for c in columns]
need(leaves[0] == (4, 57) and leaves[1] == (5, 56), 'v1.6.8 star leaves')
need(len({m for leaf in leaves for m in leaf}) == 16, 'sixteen distinct star modes')

Delta, g = sp.symbols('Delta g')
sig = sp.Matrix(signs)
H9 = sp.zeros(9)
H9[:8, 8] = g * sig
H9[8, :8] = g * sig.T
H9[8, 8] = Delta
Nb9 = sp.diag(*([0] * 8), 1)
Nf9 = sp.diag(*([2] * 8), 0)
need(Nf9 + 2 * Nb9 == 2 * sp.eye(9), 'total charge is two on the star')
Zb9 = sp.eye(9) - 2 * Nb9


def n_leaf(q):
    return sp.diag(*[(1 if k == q else 0) for k in range(8)], 0)


need(Zb9 * n_leaf(1) - n_leaf(1) * Zb9 == sp.zeros(9),
     'Zb commutes with n5 on the star: no immediate receiver effect')
need(Zb9 * Zb9 == sp.eye(9), 'Zb is an involution on N=2')

# --- Exact K3 reduction ------------------------------------------------------
u7 = sp.Matrix([sp.Rational(0)] + [sp.Rational(sv) / sp.sqrt(7) for sv in signs[1:]]
               + [sp.Rational(0)])
P3 = sp.Matrix.hstack(sp.eye(9)[:, 0], u7, sp.eye(9)[:, 8])
need(sp.simplify(P3.T * P3 - sp.eye(3)) == sp.zeros(3), 'reduction basis is orthonormal')
h3 = sp.Matrix([[0, 0, -g], [0, 0, sp.sqrt(7) * g], [-g, sp.sqrt(7) * g, Delta]])
B3s = sp.diag(0, 0, 1)
Zb3s = sp.diag(1, 1, -1)
E3s = sp.diag(0, sp.Rational(1, 7), 0)
need(sp.simplify(H9 * P3 - P3 * h3) == sp.zeros(9, 3), 'K3 is H-invariant with h3')
need(sp.simplify(Nb9 * P3 - P3 * B3s) == sp.zeros(9, 3), 'Nb restricts to B = diag(0,0,1)')
need(sp.simplify(Zb9 * P3 - P3 * Zb3s) == sp.zeros(9, 3), 'Zb restricts to diag(1,1,-1)')
need(sp.simplify(P3.T * n_leaf(1) * P3 - E3s) == sp.zeros(3), 'n5 compresses to diag(0,1/7,0)')
need(sp.simplify(Zb3s - (sp.eye(3) - 2 * B3s)) == sp.zeros(3),
     'Zb = I - 2B on K3: inside the documented (X,Nb) algebra')
X3s = (h3 - Delta * B3s) / g
need(sp.simplify(X3s - sp.Matrix([[0, 0, -1], [0, 0, sp.sqrt(7)], [-1, sp.sqrt(7), 0]]))
     == sp.zeros(3), 'X3 has the documented form')
PD = sp.eye(3) - X3s * X3s / 8
Z4old = sp.diag(-1, 1, 1)
comm_old = sp.simplify(Z4old * PD - PD * Z4old)
need(comm_old != sp.zeros(3), 'outdated single-mode Z4 lies outside the (X,Nb) algebra')
for M, nm in ((sp.eye(3), 'I'), (B3s, 'B'), (X3s, 'X3'),
              (sp.I * (B3s * X3s - X3s * B3s), 'i[B,X3]'), (X3s * X3s, 'X3^2')):
    need(sp.simplify(M * PD - PD * M) == sp.zeros(3),
         f'algebra basis element {nm} commutes with the dark projector')
comm_zb_h = sp.simplify(Zb3s * h3 - h3 * Zb3s)
need(comm_zb_h != sp.zeros(3), '[Zb,H3] != 0: the impulse is not time-covariant')
need(sp.simplify(comm_zb_h / g - sp.Matrix([[0, 0, -2], [0, 0, 2 * sp.sqrt(7)],
                                            [2, -2 * sp.sqrt(7), 0]])) == sp.zeros(3),
     'exact commutator [Zb,H3]/g')

# Float K3 cross-check against the exact reduction.
h3_num = np.array(h3.subs({Delta: 1, g: 0.05}).tolist(), dtype=float)
need(float(np.max(np.abs(mc.H3 - h3_num))) < 1e-15,
     'model_core h3 matches the exact star reduction', 'numerical')
need(float(np.max(np.abs(mc.X3 - np.array(X3s.subs({Delta: 1, g: 0.05}).tolist(),
                                                          dtype=float)))) < 1e-15,
     'model_core X3 matches the exact reduction', 'numerical')

# --- Recorder coupler C_R: exact integer layer -------------------------------
CR_int = (np.kron(np.eye(3, dtype=np.int64) - np.diag([0, 0, 1]),
                  np.eye(2, dtype=np.int64))
          + np.kron(np.diag([0, 0, 1]), np.array([[0, 1], [1, 0]], dtype=np.int64)))
need(np.array_equal(CR_int, mc.CR.astype(np.int64)), 'C_R matches model_core')
need(np.array_equal(CR_int @ CR_int, np.eye(6, dtype=np.int64)), 'C_R^2 = I (unitary involution)')
need(np.array_equal(CR_int, CR_int.T), 'C_R is Hermitian')
perm = [int(np.argmax(CR_int[:, j])) for j in range(6)]
need(sorted(perm) == [0, 1, 2, 3, 4, 5], 'C_R is a permutation matrix')
need(sum(1 for a in range(6) for b in range(a + 1, 6) if perm[a] > perm[b]) % 2 == 1,
     'C_R has determinant -1 (single transposition)')
Vrec = np.zeros((6, 3), dtype=np.int64)
Vrec[0, 0] = 1
Vrec[2, 1] = 1
Vrec[5, 2] = 1
need(np.array_equal(Vrec.T @ Vrec, np.eye(3, dtype=np.int64)),
     'V_rec is an isometry: all joint overlaps preserved')
B_int = np.diag([0, 0, 1])
ZB_int = np.diag([1, 1, -1])
for i in (0, 1):
    for j in (0, 1):
        Eij = np.zeros((3, 3), dtype=np.int64)
        Eij[i, j] = 1
        lhs = CR_int.T @ np.kron(Eij, np.eye(2, dtype=np.int64)) @ CR_int
        need(np.array_equal(lhs, np.kron(Eij, np.eye(2, dtype=np.int64))),
             f'pair coherence ({i},{j}) is preserved by C_R')
for i in range(3):
    for j in range(3):
        Eij = np.zeros((3, 3), dtype=np.int64)
        Eij[i, j] = 1
        IB = np.eye(3, dtype=np.int64) - B_int
        lhs = 2 * (IB @ Eij @ IB + B_int @ Eij @ B_int)
        rhs = Eij + ZB_int @ Eij @ ZB_int
        need(np.array_equal(lhs, rhs),
             f'D_B = (id + Zb . Zb)/2 on matrix unit ({i},{j})')
for i, j in ((0, 2), (1, 2), (2, 0), (2, 1)):
    Eij = np.zeros((3, 3), dtype=np.int64)
    Eij[i, j] = 1
    IB = np.eye(3, dtype=np.int64) - B_int
    need(np.array_equal(IB @ Eij @ IB + B_int @ Eij @ B_int, np.zeros((3, 3), dtype=np.int64))
         and np.array_equal(Eij + ZB_int @ Eij @ ZB_int, np.zeros((3, 3), dtype=np.int64)),
         f'pair-boson coherence ({i},{j}) is removed by the recorder step')
need(float(np.max(np.abs(mc.CR - expm(-0.5j * np.pi * np.kron(
    mc.B3, mc.I2 - mc.XR))))) < 1e-12,
     'C_R = exp(-i pi/2 B (x) (I-X))', 'numerical')

# --- H_tot: finite, time-independent, branch-preserving ----------------------
need(mc.H_TOT.shape == (18, 18), 'total dimension is 18 (3x3x2)')
need(float(np.max(np.abs(mc.H_TOT - mc.H_TOT.conj().T))) < 1e-12,
     'H_tot is Hermitian', 'numerical')
for a in range(3):
    for b in range(3):
        if a != b:
            need(np.array_equal(mc.H_TOT[a * 6:(a + 1) * 6, b * 6:(b + 1) * 6],
                                np.zeros((6, 6))),
                 f'off-branch block ({a},{b}) is exactly zero')
for c in range(3):
    Pc = mc.branch_projector(c)
    need(np.array_equal(mc.H_TOT @ Pc - Pc @ mc.H_TOT, np.zeros((18, 18))),
         f'branch {c} is exactly preserved by H_tot')
need(np.array_equal(mc.H_F, np.kron(mc.H3, mc.I2).astype(np.complex128)),
     'free branch is exactly h3 (x) I')
need(np.array_equal(mc.N_TOT, 2 * np.eye(18, dtype=np.int64)),
     'total charge is 2 on every arm')
rebuild_Z = mc.principal_log_hamiltonian(mc.W_Z, mc.T_TOT)
rebuild_R = mc.principal_log_hamiltonian(mc.W_R, mc.T_TOT)
need(np.array_equal(rebuild_Z, mc.H_Z) and np.array_equal(rebuild_R, mc.H_R),
     'H_tot build is deterministic (time-independent)')
for Wc, nm in ((mc.W_F, 'free'), (mc.W_Z, 'impulse'), (mc.W_R, 'recorder')):
    need(float(np.max(np.abs(Wc.conj().T @ Wc - np.eye(6)))) < 1e-12,
         f'{nm} arm target is unitary', 'numerical')
op_norms = {}
for Hc, Wc, nm in ((mc.H_F, mc.W_F, 'free'), (mc.H_Z, mc.W_Z, 'impulse'),
                   (mc.H_R, mc.W_R, 'recorder')):
    err = float(np.max(np.abs(expm(-1j * mc.T_TOT * Hc) - Wc)))
    op_norms[nm] = err
    need(err < 1e-9, f'{nm} branch reproduces its arm unitary as a full operator', 'numerical')

result = {
    'status': 'PASS',
    'task': 'closed-model structure: K3 reduction, Zb algebra, recorder, H_tot',
    'guards': len(checks),
    'exact_guards': sum(k == 'exact' for _, k in checks),
    'numerical_guards': sum(k == 'numerical' for _, k in checks),
    'model': {
        'hilbert_space': 'K3 (system) x C3 (controller: free/impulse/recorder) x R2 (pointer)',
        'total_dim': 18,
        'H_tot': 'block-diagonal H_F (+) H_Z (+) H_R, single time-independent operator',
        'controller_states': ['|F> free/no-op', '|Z> Zb impulse', '|R> neutral recorder'],
        'pointer': '|0> pair branch, |1> boson branch; C_R = (I-B)(x)I + B(x)X',
        'total_charge_per_arm': 2,
        'common_duration_T': mc.fmt(mc.T_TOT),
    },
    'operator_equality_maxabs': {k: mc.fmt(v) for k, v in op_norms.items()},
    'scope': 'universal on K3 (impulse) and K3xR2 (recorder): full-operator equality, not state-specific',
    'labels': 'structure exakt; time evolution numerisch; controller+pointer bedingt (origin unexplained)',
    'runtime_seconds': round(time.time() - T0, 3),
    'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'dependency_sha256': NS_PIN,
    'model_core_sha256': MC_SHA,
    'T1_T8_closed': [],
}
print(json.dumps(result, indent=2, sort_keys=True))
