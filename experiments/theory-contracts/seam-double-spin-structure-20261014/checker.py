"""Spin structure of the 16-Majorana seam double and the E8 class of the clock.

Standalone checks; no paper/ledger promotion.  Scope: PROOF.md.
Operators are those of verification/v506_seam_clock_rigidity.py (Part B):
16 real Majorana sites, deck D = half shift, clock C = quarter shift, wrap sign
-1 (NS, v506) or +1 (R).

P1  one-particle data reproduce v506: NS C^2 = D, D^2 = -1, C^8 = 1,
    charpoly(C) = (x^4+1)^4; R: D^2 = +1, charpoly(C) = (x^4-1)^4.
P2  Fock lifts in Cl(16) (256-dim): NS deck lift squares to the chirality
    gamma_1..gamma_16 (nonsplit, U^2 = (-1)^F); R deck lift squares to a scalar.
P3  E8 class of the clock (rotation angles read from the 16x16 matrix, both
    spin lifts): NS -> A1+D6 / A1+A7, never A3+D5; R -> A3+D5 for both lifts.
    Deck: NS -> A1+E7 / D8; R -> D8.
P4  pullback: NS on a base circle of L sites lifts to the connected double
    (2L sites) as R; the deck splits the R double into base-NS (deck = -1) and
    base-R (deck = +1) sectors.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json
import numpy as np
from scipy.linalg import expm, schur

checks = {}
def require(name, cond):
    if not bool(cond):
        raise RuntimeError(name)
    checks[name] = True

def shift_matrix(n, k, ws):          # gamma_j -> ws^(#wraps) gamma_{j+k}  (v506 convention)
    M = np.zeros((n, n))
    for a in range(n):
        M[(a + k) % n, a] = ws if a + k >= n else 1
    return M

n = 16
I16 = np.eye(n)
C_ns, D_ns = shift_matrix(n, 4, -1), shift_matrix(n, 8, -1)
C_r, D_r = shift_matrix(n, 4, 1), shift_matrix(n, 8, 1)
mp = np.linalg.matrix_power
# P1
require("P1_ns_C2_is_D", np.allclose(mp(C_ns, 2), D_ns))
require("P1_ns_D2_minus1", np.allclose(mp(D_ns, 2), -I16))
require("P1_ns_C8_is_1", np.allclose(mp(C_ns, 8), I16) and not np.allclose(mp(C_ns, 4), I16))
require("P1_ns_charpoly", np.allclose(np.poly(C_ns), np.poly(np.kron(np.eye(4), np.array([[0, 0, 0, -1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])))))
require("P1_r_D2_plus1", np.allclose(mp(D_r, 2), I16) and np.allclose(mp(C_r, 4), I16))

# P2: Cl(16) via Jordan-Wigner on 8 qubits
X = np.array([[0, 1], [1, 0]]); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]); I2 = np.eye(2)
def kron_all(ms):
    out = np.array([[1.0]])
    for m in ms: out = np.kron(out, m)
    return out
gam = []
for j in range(8):
    gam.append(kron_all([Z] * j + [X] + [I2] * (7 - j)))
    gam.append(kron_all([Z] * j + [Y] + [I2] * (7 - j)))
for a in range(n):
    for b in range(n):
        require_ok = np.allclose(gam[a] @ gam[b] + gam[b] @ gam[a], 2 * (a == b) * np.eye(256))
        if not require_ok: raise RuntimeError("clifford")
checks["P2_clifford_relations"] = True
chir = np.eye(256)
for g in gam: chir = chir @ g
def implementer(O):
    T, Q = schur(O, output="real")            # O = Q T Q^T, T block diagonal
    AT = np.zeros_like(T); i = 0; neg = []
    while i < len(T):
        if i + 1 < len(T) and abs(T[i + 1, i]) > 1e-9:
            th = np.arctan2(T[i + 1, i], T[i, i]); AT[i + 1, i], AT[i, i + 1] = th, -th; i += 2
        else:
            if T[i, i] < 0: neg.append(i)
            i += 1
    require("P2_even_reflection_count", len(neg) % 2 == 0)
    for a, b in zip(neg[0::2], neg[1::2]):     # pair -1 eigenvalues into pi-rotations
        AT[b, a], AT[a, b] = np.pi, -np.pi
    A = Q @ AT @ Q.T
    require("P2_log_reproduces", np.allclose(expm(A), O, atol=1e-9))
    G = sum(A[a, b] * gam[a] @ gam[b] for a in range(n) for b in range(n)) / 4.0
    U = expm(G)
    # check U gamma_a U^-1 = sum_b O[b,a] gamma_b
    Ui = np.linalg.inv(U)
    for a in range(n):
        if not np.allclose(U @ gam[a] @ Ui, sum(O[b, a] * gam[b] for b in range(n)), atol=1e-8):
            raise RuntimeError("implementer")
    return U
def is_scalar(M):
    return np.allclose(M, M[0, 0] * np.eye(M.shape[0]), atol=1e-8)
def prop_to(M, N):
    k = np.vdot(N.ravel(), M.ravel()) / np.vdot(N.ravel(), N.ravel())
    return abs(k) > 1e-8 and np.allclose(M, k * N, atol=1e-8)
U_ns = implementer(D_ns)
U_r = implementer(D_r)
require("P2_ns_deck_nonsplit_U2_chirality", prop_to(U_ns @ U_ns, chir) and not is_scalar(U_ns @ U_ns))
require("P2_r_deck_split_U2_scalar", is_scalar(U_r @ U_r))

# P3: E8 classes
roots = []
for i, j in combinations(range(8), 2):
    for s1, s2 in product((1, -1), repeat=2):
        v = [F(0)] * 8; v[i] = F(s1); v[j] = F(s2); roots.append(tuple(v))
for sg in product((1, -1), repeat=8):
    if sg.count(-1) % 2 == 0: roots.append(tuple(F(t, 2) for t in sg))
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
def in_e8(v):
    if all(x.denominator == 1 for x in v) or all(x.denominator == 2 for x in v): return sum(v) % 2 == 0
    return False
def order(mu): return next(k for k in range(1, 200) if in_e8(tuple(k * x for x in mu)))
NAMES = {(12, 3): "A3", (40, 5): "D5", (112, 8): "D8", (60, 6): "D6", (2, 1): "A1", (126, 7): "E7", (56, 7): "A7"}
def cls(mu):
    R = [r for r in roots if dot(r, mu).denominator == 1]
    seen, out = set(), []
    for i in range(len(R)):
        if i in seen: continue
        st, c = [i], []; seen.add(i)
        while st:
            a = st.pop(); c.append(R[a])
            for b in range(len(R)):
                if b not in seen and dot(R[a], R[b]) != 0: seen.add(b); st.append(b)
        rk = np.linalg.matrix_rank(np.array([[float(x) for x in r] for r in c]))
        out.append(NAMES.get((len(c), rk), f"?{len(c)},{rk}"))
    return order(mu), tuple(sorted(out))
def angles(M):
    th = np.angle(np.linalg.eigvals(M))
    comp = sorted(t for t in th if 1e-9 < t < np.pi - 1e-9)
    nneg = sum(1 for t in th if abs(abs(t) - np.pi) < 1e-9)
    mu = [F(round(t / (2 * np.pi) * 64), 64) for t in comp] + [F(1, 2)] * (nneg // 2)
    return tuple(mu + [F(0)] * (8 - len(mu)))
e1 = tuple([F(1)] + [F(0)] * 7)
both = lambda mu: {cls(mu), cls(tuple(a + b for a, b in zip(mu, e1)))}
table = {k: both(angles(M)) for k, M in (("NS_clock", C_ns), ("NS_deck", D_ns), ("R_clock", C_r), ("R_deck", D_r))}
require("P3_ns_clock_not_glue", table["NS_clock"] == {(4, ("A1", "D6")), (4, ("A1", "A7"))})
require("P3_r_clock_is_glue_both_lifts", table["R_clock"] == {(4, ("A3", "D5"))})
require("P3_ns_deck", table["NS_deck"] == {(2, ("A1", "E7")), (2, ("D8",))})
require("P3_r_deck", table["R_deck"] == {(2, ("D8",))})
mu_glue = tuple([F(1, 2)] * 5 + [F(0)] * 3)
require("P3_glue_reference", cls(mu_glue) == (4, ("A3", "D5")))

# P4: pullback of NS along the connected double cover
for L in (4, 6, 8):
    base_turn = -1                                  # NS holonomy of the base circle
    require(f"P4_double_holonomy_L{L}", base_turn ** 2 == 1)
    T = shift_matrix(2 * L, 1, 1)                   # R double, unit shift
    Dk = mp(T, L)                                   # deck = half shift
    for sgn, base_hol in ((-1, -1), (1, 1)):
        w, V = np.linalg.eig(Dk)
        Vs = V[:, np.isclose(w, sgn)]
        Q, _ = np.linalg.qr(Vs)
        Tb = Q.conj().T @ T @ Q                      # unit shift restricted to sector
        require(f"P4_sector_{'NS' if sgn < 0 else 'R'}_L{L}",
                np.allclose(mp(Tb, L), base_hol * np.eye(L), atol=1e-9))

results = {"contract": "seam-double-spin-structure-20261014",
           "e8_classes": {k: sorted(map(list, v)) for k, v in table.items()},
           "checks": checks, "n_checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2, default=str) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
