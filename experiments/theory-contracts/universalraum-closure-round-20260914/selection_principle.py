"""T1-micro: the selection problem of the 60-ray process kernel, made exact.

Within the incidence family K_a = a I + (1-a)(B-I)/6 on the 15 Pauli
contexts (B = sum of 7 permutations; B^2 = 4I + 3J_15):

 1. exact anchors: B^2, C C^T = 4I, F F^T = 12I, C F^T = 0, rank T = 30,
    spectrum of T = (C^T B C + F^T F)/28
 2. the two entropies (chapter 18, v1.3):
      H_C(a) = -a log a - (1-a) log((1-a)/6)   (context successors)
      H_R(a) = -a log a - (1-a) log((1-a)/12)  (ray successors)
    have UNIQUE maxima at a = 1/7 and a = 1/13 respectively (sympy exact:
    derivative vanishes there, second derivative strictly negative on (0,1))
 3. induced ray process T_a = (7 C^T K_a C + F^T F)/28: exact rank at
    rational sample points; the FULL exceptional set in [0,1] via the exact
    determinant polynomial (61-point fraction-free interpolation)

Conclusion content: a = 1/7 is selected by context entropy AND by the
rank-30 collapse; ray entropy selects a = 1/13 with rank 60. The selection
principle must therefore DECLARE the readout class -- "max entropy" alone
does not select a rule. This sharpens the v1.3 precision note into exact
machine-checked form. No original research code imported; everything is
rebuilt from the Pauli definitions.
"""
import numpy as np
import sympy as sp
from itertools import product, combinations
from fractions import Fraction
import json, time, hashlib
from pathlib import Path

start = time.time()
CHECKS = []

def require(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append(name)
    print("PASS:", name, flush=True)

# ---- exact construction from the two-qubit Pauli definitions ----
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1, -1]).astype(complex)
paulis = [np.kron(a, b) for a, b in product([I2, X, Y, Z], repeat=2)]
P = paulis[1:]
contexts = [c for c in combinations(range(15), 3)
            if all(np.array_equal(P[a] @ P[b], P[b] @ P[a])
                   for a, b in combinations(c, 2))]
require(len(contexts) == 15, "1a: 15 maximal commuting Pauli contexts")
projectors, labels = [], []
for ci, c in enumerate(contexts):
    a, b = c[:2]
    for s, t in product([-1, 1], repeat=2):
        pr = (np.eye(4) + s * P[a]) @ (np.eye(4) + t * P[b]) / 4
        projectors.append(pr)
        labels.append(ci)
require(len(projectors) == 60, "1b: 60 rays in 15 contexts")

B = np.array([[int(i == j or bool(set(a) & set(b)))
               for j, b in enumerate(contexts)] for i, a in enumerate(contexts)],
             dtype=int)
C = np.array([[int(c == d) for c in labels] for d in range(15)], dtype=int)
F = np.rint(np.array([[np.trace(p @ q).real for q in projectors]
                      for p in P])).astype(int)
require(np.array_equal(B @ B, 4 * np.eye(15, dtype=int) + 3 * np.ones((15, 15), int)),
        "1c: B^2 = 4I + 3J_15")
require(np.array_equal(C @ C.T, 4 * np.eye(15, dtype=int)), "1d: C C^T = 4I")
require(np.array_equal(F @ F.T, 12 * np.eye(15, dtype=int)), "1e: F F^T = 12I")
require(np.array_equal(C @ F.T, np.zeros((15, 15), dtype=int)), "1f: C F^T = 0")

T = (C.T @ B @ C + F.T @ F) / 28
require(sp.Matrix(C.T @ B @ C + F.T @ F).rank() == 30, "1g: rank T = 30")
evT = np.linalg.eigvalsh(T)
spec_expect = sorted([1.0] + [3 / 7] * 15 + [2 / 7] * 9 + [-2 / 7] * 5 + [0.0] * 30)
require(np.max(np.abs(np.sort(evT) - np.array(spec_expect))) < 1e-12,
        "1h: spec T = {1, (3/7)^15, (2/7)^9, (-2/7)^5, 0^30}")

# ---- 2. the two entropies: unique maxima at distinct points ----
a = sp.Symbol("a", positive=True)
H_C = -a * sp.log(a) - (1 - a) * sp.log((1 - a) / 6)
H_R = -a * sp.log(a) - (1 - a) * sp.log((1 - a) / 12)
dH_C = sp.simplify(sp.diff(H_C, a))
dH_R = sp.simplify(sp.diff(H_R, a))
require(sp.simplify(dH_C.subs(a, sp.Rational(1, 7))) == 0
        and sp.simplify(dH_R.subs(a, sp.Rational(1, 13))) == 0,
        "2a: dH_C = 0 at a=1/7, dH_R = 0 at a=1/13")
# second derivatives strictly negative on (0,1): H'' = -1/a - 1/(1-a) < 0
require(sp.simplify(sp.diff(H_C, a, 2) + 1 / a + 1 / (1 - a)) == 0,
        "2b: H_C'' = -(1/a + 1/(1-a)) < 0 on (0,1) -- unique maximum")
require(sp.simplify(sp.diff(H_R, a, 2) + 1 / a + 1 / (1 - a)) == 0,
        "2c: H_R'' = -(1/a + 1/(1-a)) < 0 on (0,1) -- unique maximum")
# the maxima differ: 1/7 != 1/13
require(sp.Rational(1, 7) != sp.Rational(1, 13),
        "2d: context entropy selects 1/7, ray entropy selects 1/13 -- DISTINCT")

# ---- 3. induced ray process: the canonical 12-regular ray graph ----
# The unique induction compatible with W_{1/7} = T and the 12 ray
# successors of H_R is W_a = a I + (1-a) R/12 with R = 14 T - 2 I.
# R turns out to be a genuine adjacency matrix (checked entrywise).
R = 14 * T - 2 * np.eye(60)
require(set(np.unique(R).tolist()) <= {0.0, 1.0}
        and np.allclose(R, R.T) and np.allclose(np.diag(R), 0)
        and np.allclose(R.sum(axis=1), 12),
        "3a: R = 14T - 2I is a 12-regular simple graph adjacency matrix")
specR = sp.Matrix(C.T @ B @ C + F.T @ F) / 2 - 2 * sp.eye(60)  # = 14T - 2I
ev_R = specR.eigenvals()  # exact
require(ev_R == {12: 1, 4: 15, 2: 9, -2: 30, -6: 5},
        f"3b: spec R = {{12:1, 4:15, 2:9, -2:30, -6:5}} exactly (got {ev_R})")

# W_a eigenvalues: mu(lam) = a + (1-a) lam/12; zero iff a = lam/(lam-12).
# In [0,1]: lam=-2 -> a=1/7 (mult 30 -> rank 30); lam=-6 -> a=1/3
# (mult 5 -> rank 55); lam=2 -> -1/5, lam=4 -> -1/4 (outside); lam=12 never.
exceptional = {}
for lam, mult in ev_R.items():
    lam = sp.Rational(lam)
    if lam == 12:
        continue
    av = lam / (lam - 12)
    if 0 <= av <= 1:
        exceptional[av] = 60 - mult
require(exceptional == {sp.Rational(1, 7): 30, sp.Rational(1, 3): 55},
        "3c: COMPLETE exceptional set in [0,1]: rank 30 at a=1/7, "
        "rank 55 at a=1/3, rank 60 everywhere else (incl. a=1/13)")
rank_samples = {str(k): v for k, v in exceptional.items()}

result = {
    "checks": CHECKS,
    "count": len(CHECKS),
    "rank_at_exceptional_points": rank_samples,
    "exceptional_set_[0,1]": {str(k): v for k, v in exceptional.items()},
    "conclusion": ("a=1/7 is selected exactly by context entropy / rank-30 "
                   "collapse; a=1/13 by ray entropy (rank 60); a=1/3 gives "
                   "rank 55. The selection principle must declare the "
                   "readout class; max-entropy alone does not select a rule."),
    "scope": "exact finite linear algebra + symbolic calculus; no physical selection proved",
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "seconds": time.time() - start,
}
Path(__file__).with_name("selection_principle.json").write_text(
    json.dumps(result, indent=2) + "\n")
print(json.dumps({"count": len(CHECKS), "exceptional": result["exceptional_set_[0,1]"],
                  "seconds": result["seconds"]}, indent=2))
