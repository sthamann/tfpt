"""Hecke covering index == Jones-Longo index of the lattice subnet A_{A E8} c A_{E8} (exact check).

Uses only two facts the corpus already trusts:
  (1) hecke-index-theorem: the covering index of x -> A x on R^8/E8 is |det A| = [E8 : A E8].
  (2) Kawahigashi-Longo-Mueger: mu_A = [B:A]^2 mu_B for finite-index conformal subnets, and
      mu(A_L) = |L^*/L| = |disc L| for even lattice nets  (the repo uses (2) for [E8 : D5+A3] = 4).
Consequence: [A_{E8} : A_{A E8}] = sqrt(disc(A E8)/disc(E8)) = |det A| = Hecke index.
The Solomon zeta of E8 (sublattice count) is prod_{k=0..7} zeta(s-k); its zeros are zeta zeros and
translates -> RH-neutral, as recorded in the graph (e8-sublattice-rg-semigroup).  Pimsner-Popa turns
log|det A| into the conditional entropy H(B|A), not into a modular Hamiltonian: the vacuum is invariant
under the dual-group automorphisms implementing E8/AE8, so the Connes cocycle (D omega.E : D omega) is 1.
NO RH claim, NO status move.  Exploration in fable-runde3.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction as F
from itertools import product
from pathlib import Path

import numpy as np

E8_CARTAN = [  # Gram matrix of the E8 root basis (Bourbaki numbering), det = 1, even
    [2, -1, 0, 0, 0, 0, 0, 0],
    [-1, 2, -1, 0, 0, 0, 0, 0],
    [0, -1, 2, -1, 0, 0, 0, -1],
    [0, 0, -1, 2, -1, 0, 0, 0],
    [0, 0, 0, -1, 2, -1, 0, 0],
    [0, 0, 0, 0, -1, 2, -1, 0],
    [0, 0, 0, 0, 0, -1, 2, 0],
    [0, 0, -1, 0, 0, 0, 0, 2],
]


def det_exact(M):
    """Bareiss determinant over Fractions."""
    n = len(M)
    A = [[F(x) for x in row] for row in M]
    sign = 1
    for k in range(n):
        piv = next((i for i in range(k, n) if A[i][k] != 0), None)
        if piv is None:
            return F(0)
        if piv != k:
            A[k], A[piv] = A[piv], A[k]
            sign = -sign
        for i in range(k + 1, n):
            f = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= f * A[k][j]
    d = F(sign)
    for k in range(n):
        d *= A[k][k]
    return d


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(r) for r in zip(*A)]


def solomon_coefficients(nmax, rank=8):
    """a_n = #sublattices of index n in Z^rank = Dirichlet coefficients of prod_{k<rank} zeta(s-k)."""
    a = [0] * (nmax + 1)
    a[1] = 1
    for k in range(rank):
        b = [0] * (nmax + 1)
        for n in range(1, nmax + 1):
            for d in range(1, nmax // n + 1):
                b[n * d] += a[n] * d ** k
        a = b
    return a


def count_index_p_sublattices(p, rank=8):
    """Sublattices of index p in Z^rank <-> hyperplanes in F_p^rank: (p^rank - 1)/(p - 1)."""
    return (p ** rank - 1) // (p - 1)


def main():
    G = E8_CARTAN
    assert det_exact(G) == 1 and all(G[i][i] % 2 == 0 for i in range(8)), "E8 Gram: unimodular, even"
    rng = np.random.default_rng(2026)
    rows = []
    tested = 0
    while tested < 12:
        A = rng.integers(-2, 3, size=(8, 8)).tolist()
        dA = det_exact(A)
        if dA == 0:
            continue
        gram_sub = matmul(matmul(transpose(A), G), A)
        disc = det_exact(gram_sub)
        assert disc == dA * dA, "disc(A E8) = det(A)^2 * disc(E8)"
        # KLM: [A_E8 : A_{AE8}]^2 = mu(A_{AE8}) / mu(A_E8) = disc / 1
        jones_index_sq = disc
        hecke_index = abs(dA)
        assert jones_index_sq == hecke_index ** 2, "Jones index == Hecke covering index"
        rows.append({"det_A": int(dA), "disc_sublattice": int(disc), "hecke_index": int(hecke_index),
                     "jones_index_from_KLM": int(hecke_index), "scalar_A": all(A[i][j] == (A[0][0] if i == j else 0) for i in range(8) for j in range(8))})
        tested += 1
    assert any(not r["scalar_A"] for r in rows), "non-scalar endomorphisms tested"
    # composition law: index multiplicative (Hecke semigroup), matching [C:A] = [C:B][B:A] for subnets
    A1 = rng.integers(-2, 3, size=(8, 8)).tolist(); A2 = rng.integers(-2, 3, size=(8, 8)).tolist()
    while det_exact(A1) == 0: A1 = rng.integers(-2, 3, size=(8, 8)).tolist()
    while det_exact(A2) == 0: A2 = rng.integers(-2, 3, size=(8, 8)).tolist()
    assert abs(det_exact(matmul(A1, A2))) == abs(det_exact(A1)) * abs(det_exact(A2)), "index multiplicative"
    # Solomon zeta coefficients (sublattice census) and prime check
    a = solomon_coefficients(30)
    for p in (2, 3, 5, 7):
        assert a[p] == count_index_p_sublattices(p), f"a_{p} = (p^8-1)/(p-1)"
    out = {"claim_boundary": "exploration; no RH claim; no status move",
           "identity": "[A_E8 : A_{A E8}] = |det A| = Hecke covering index of x->Ax on R^8/E8 (KLM mu-formula + disc(AE8)=det(A)^2)",
           "examples": rows,
           "solomon_coefficients_n_le_30": a[1:],
           "solomon_zeta": "prod_{k=0}^{7} zeta(s-k); rightmost pole s=8=c; zeros = zeta zeros and translates (RH-neutral)",
           "what_it_does_not_give": "log|det A| is Pimsner-Popa conditional entropy H(B|A); vacuum invariant under dual-group automorphisms => Connes cocycle trivial => no modular Hamiltonian log(index) on the holomorphic seam in the vacuum (scoped negative for index-modular-state)."}
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("hecke_index_net.json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "examples"}, indent=1))
    print("examples:", [(r["det_A"], r["hecke_index"]) for r in rows])
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
