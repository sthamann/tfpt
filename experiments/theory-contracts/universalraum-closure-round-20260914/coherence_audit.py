"""Global vertex coherence audit for the repaired Universalraum exchange vertex.

Exact (integer / sympy) checks of the claims in Konsolidierte_Fortsetzung.md
sections 4 and 9 and the Clebsch label structure used in section 5:

 1. K^dagger K = I - S on the full 16-dim pair space (unrecorded vertex)
 2. ordered history destroys it: K~^dagger K~ = I - D_diag (orthonormal records)
 3. interpolation: record overlap eta gives I - D_diag - eta*(S - D_diag)
 4. U_W = [[P_+, -W^dag],[W, 0]] is unitary (W = K/sqrt(2)), symbolic in sqrt(2)
 5. H_22 antisymmetric band shift equals -j(g,Delta) exactly
 6. H_bad ground spaces: K4 -> dim 24 at -6 kappa; star -> dim 108 at -3 kappa
 7. Clebsch mediator labels: 40 edges, 10 vector labels, each exactly 4 edges;
    alternate present pairings of any 4-cycle never share a label multiset
    (the F4 completeness argument of section 5.3)
 8. local symmetry mechanism: [sum_s h_s, H_exchange] = 0 on two adjacent
    edges forces h1 = h2 = h3 (exact 64-dim nullspace computation)

No external research code imported; all objects rebuilt here.
"""
import numpy as np
import sympy as sp
from itertools import product, combinations
from collections import Counter, defaultdict
from math import prod
import json, time, hashlib
from pathlib import Path

start = time.time()
CHECKS = []

def require(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append(name)
    print("PASS:", name, flush=True)

# ---------- 1. unrecorded vertex Gram operator ----------
wedge = [(a, b) for a in range(4) for b in range(a + 1, 4)]  # 6
K = np.zeros((6, 16), dtype=int)
for a in range(4):
    for b in range(4):
        if a < b:
            K[wedge.index((a, b)), 4 * a + b] = 1
        elif a > b:
            K[wedge.index((b, a)), 4 * a + b] = -1
S16 = np.zeros((16, 16), dtype=int)
for a in range(4):
    for b in range(4):
        S16[4 * b + a, 4 * a + b] = 1
I16 = np.eye(16, dtype=int)
D_diag = np.zeros((16, 16), dtype=int)
for a in range(4):
    D_diag[4 * a + a, 4 * a + a] = 1

require(np.array_equal(K.T @ K, I16 - S16), "1: K^dag K = I - S (unrecorded vertex)")
require(np.linalg.matrix_rank(K) == 6, "1b: rank K = 6")

# ---------- 2./3. recorded vertex with overlap eta ----------
def recorded_gram(eta):
    # record space: for each unordered pair {a,b} a 2-dim space with
    # h_ab = e1, h_ba = eta*e1 + sqrt(1-eta^2)*e2 (sympy exact)
    G = sp.zeros(16)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    i, j = 4 * a + b, 4 * c + d
                    if a == b or c == d:
                        continue
                    if frozenset((a, b)) != frozenset((c, d)):
                        continue
                    s1 = 1 if a < b else -1
                    s2 = 1 if c < d else -1
                    ov = 1 if (a < b) == (c < d) else eta
                    G[i, j] = s1 * s2 * ov
    return G

for eta_val, label in [(sp.Integer(0), "0 (orthonormal)"),
                       (sp.Rational(1, 2), "1/2"),
                       (sp.Integer(1), "1 (coherent)")]:
    G = recorded_gram(eta_val)
    target = sp.Matrix(I16 - D_diag - eta_val * (S16 - D_diag))
    require(sp.simplify(G - target) == sp.zeros(16),
            f"3: recorded Gram = I - D - eta(S - D), eta={label}")

G0 = np.array(recorded_gram(sp.Integer(0))).astype(float)
require(np.linalg.matrix_rank(G0) == 12,
        "2: orthonormal ordered history raises Gram rank 6 -> 12")

# ---------- 4. U_W unitary, symbolic ----------
sq2 = sp.sqrt(2)
I16s = sp.Matrix(I16)
S16s = sp.Matrix(S16)
Ws = sp.Matrix(K) / sq2
Pp = (I16s + S16s) / 2  # sympy Rational entries, exact
U_W = sp.Matrix.vstack(
    sp.Matrix.hstack(Pp, -Ws.T),
    sp.Matrix.hstack(Ws, sp.zeros(6)))
Uerr = (U_W.T * U_W - sp.eye(22)).applyfunc(sp.simplify)
require(Uerr == sp.zeros(22), "4: U_W unitary (22-dim, symbolic)")

# ---------- 5. H_22 exact antisymmetric shift ----------
g, Delta = sp.symbols("g Delta", positive=True)
j_exact = (sp.sqrt(Delta**2 + 4 * g**2) - Delta) / 2
lam_low = (Delta - sp.sqrt(Delta**2 + 4 * g**2)) / 2
require(sp.simplify(lam_low + j_exact) == 0,
        "5: antisymmetric band shift = -j(g,Delta), j = (sqrt(D^2+4g^2)-D)/2")
Hn = np.zeros((22, 22))
gv, Dv = 0.1, 1.0
Hn[:16, 16:] = gv * (K / np.sqrt(2)).T
Hn[16:, :16] = gv * (K / np.sqrt(2))
Hn[16:, 16:] = Dv * np.eye(6)
ev = np.sort(np.linalg.eigvalsh(Hn))
jnum = (np.sqrt(1 + 4 * gv**2) - 1) / 2
expect = sorted([0.0] * 10 + [-jnum] * 6 + [Dv + jnum] * 6)
require(np.max(np.abs(ev - np.array(expect))) < 1e-14,
        "5b: H_22 spectrum = 0(x10), -j(x6), D+j(x6)")

# ---------- 6. H_bad ground spaces ----------
def bad_spectrum(edge_list, n_sites=4):
    cnt = Counter()
    for word in product(range(4), repeat=n_sites):
        e = -sum(1 for (i, j) in edge_list if word[i] != word[j])
        cnt[e] += 1
    return cnt

ck4 = bad_spectrum(list(combinations(range(4), 2)))
cstar = bad_spectrum([(0, 1), (0, 2), (0, 3)])
require(min(ck4) == -6 and ck4[-6] == 24,
        "6: H_bad on K4: ground -6 kappa, dim 24 (Omega uniqueness destroyed)")
require(min(cstar) == -3 and cstar[-3] == 108,
        "6b: H_bad on star: ground -3 kappa, dim 108 = 4*3^3")

# ---------- 7. Clebsch mediator labels ----------
vertices = [x for x in product((-1, 1), repeat=5) if prod(x) == 1]
edges = [(i, j) for i, j in combinations(range(16), 2)
         if sum(a != b for a, b in zip(vertices[i], vertices[j])) == 4]
labels = [tuple(a + b for a, b in zip(vertices[i], vertices[j])) for i, j in edges]
lc = Counter(labels)
require(len(edges) == 40 and len(lc) == 10 and set(lc.values()) == {4},
        "7: 40 edges, 10 vector labels, each shared by exactly 4 edges")

adj = defaultdict(set)
for i, j in edges:
    adj[i].add(j)
    adj[j].add(i)

def is_edge(a, b):
    return sum(u != v for u, v in zip(vertices[a], vertices[b])) == 4

ok, n4 = True, 0
for i, j in edges:
    for k in adj[j] - {i}:
        for l in adj[k] - {j}:
            if l != i and i in adj[l] and i < l:
                n4 += 1
                cyc = [i, j, k, l]
                pairings = [[(0, 1), (2, 3)], [(0, 2), (1, 3)], [(0, 3), (1, 2)]]
                present = []
                for p in pairings:
                    if all(is_edge(cyc[x], cyc[y]) for (x, y) in p):
                        ms = sorted(
                            tuple(u + v for u, v in zip(vertices[cyc[x]], vertices[cyc[y]]))
                            for (x, y) in p)
                        present.append(tuple(ms))
                if len(present) != len(set(present)):
                    ok = False
require(ok, "7b: distinct present pairings of any 4-cycle have distinct label multisets")
require(n4 > 0, "7c: 4-cycles enumerated")

# ---------- 8. local symmetry mechanism (3 sites, exact nullspace) ----------
H_params = []
for s in range(3):
    for a in range(4):
        H_params.append((s, a, a, "re"))
        for b in range(a + 1, 4):
            H_params.append((s, a, b, "re"))
            H_params.append((s, a, b, "im"))
npar = len(H_params)  # 3 * 16 = 48
pindex = {p: i for i, p in enumerate(H_params)}

def build_h(s, vec):
    h = np.zeros((4, 4), dtype=complex)
    for a in range(4):
        h[a, a] = vec[pindex[(s, a, a, "re")]]
        for b in range(a + 1, 4):
            re = vec[pindex[(s, a, b, "re")]]
            im = vec[pindex[(s, a, b, "im")]]
            h[a, b] = re + 1j * im
            h[b, a] = re - 1j * im
    return h

S2 = np.zeros((16, 16))
for a in range(4):
    for b in range(4):
        S2[4 * b + a, 4 * a + b] = 1
I4 = np.eye(4)
S12 = np.kron(S2, I4)
S23 = np.kron(I4, S2)

cols = []
for p in range(npar):
    vec = np.zeros(npar)
    vec[p] = 1.0
    h1, h2, h3 = build_h(0, vec), build_h(1, vec), build_h(2, vec)
    H1 = np.kron(h1, np.kron(I4, I4))
    H2 = np.kron(I4, np.kron(h2, I4))
    H3 = np.kron(I4, np.kron(I4, h3))
    C = (H1 + H2) @ S12 - S12 @ (H1 + H2) + (H2 + H3) @ S23 - S23 @ (H2 + H3)
    cols.append(C.reshape(-1))
M = np.column_stack(cols)
Mr = np.vstack([M.real, M.imag])
_, sv, vt = np.linalg.svd(Mr)
nullity = int(np.sum(sv < 1e-10))
# mechanism: each edge forces h_i = h_j + c I (traceless scalar = 0 kills the
# antihermitian term), so nullspace = shared hermitian (16) + one scalar per
# edge (2) = 18; after quotienting scalar phases: collective su(4) only.
require(nullity == 18,
        "8: two-edge commutator nullspace = 16 (shared h) + 2 edge scalars")
ok_struct = True
for vnull in vt[-nullity:]:
    h1, h2, h3 = build_h(0, vnull), build_h(1, vnull), build_h(2, vnull)
    for da, db in ((h1, h2), (h3, h2)):
        diff = da - db
        if not np.allclose(diff, np.trace(diff) / 4 * np.eye(4), atol=1e-9):
            ok_struct = False
require(ok_struct,
        "8b: every null vector has h_i - h_j scalar (collective su(4) after phase quotient)")

result = {
    "checks": CHECKS,
    "count": len(CHECKS),
    "scope": "exact finite vertex/label/symmetry audit; no thermodynamic or CAR claim",
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "seconds": time.time() - start,
}
Path(__file__).with_name("coherence_audit.json").write_text(
    json.dumps(result, indent=2) + "\n")
print(json.dumps({"count": len(CHECKS), "seconds": result["seconds"]}, indent=2))
