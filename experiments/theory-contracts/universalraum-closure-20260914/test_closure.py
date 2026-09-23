"""Guard tests for closure_checks.py (cheap pieces only; heavy runs are validated via their JSON)."""
import itertools
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import closure_checks as cc  # noqa: E402
from clebsch_su4 import clebsch_edges, young_orthogonal_sparse  # noqa: E402


def test_graph_matches_fugen_contract():
    data = cc.clebsch_data()
    assert data["edges"] == clebsch_edges()
    labs = set(data["labels"])
    assert len(labs) == 10 and all(data["labels"].count(l) == 4 for l in labs)


def test_automorphism_group_order_and_translations():
    data = cc.clebsch_data()
    perms, extra = cc.automorphisms(data)
    assert len(perms) == 1920 and len(extra["translation"]) == 16
    assert tuple(range(16)) in perms


def test_representation_is_a_homomorphism_on_small_irrep():
    # shape (2,1,1): S4 irrep of dim 3 on 4 sites; check rho(pi) rho(sigma) = rho(pi sigma) up to inverse convention
    d, mats = young_orthogonal_sparse((2, 1, 1))
    eye = np.eye(d)
    reps = {}
    for pi in itertools.permutations(range(4)):
        reps[pi] = cc.represent(mats, pi, eye)
        assert np.allclose(reps[pi].T @ reps[pi], eye, atol=1e-12)
    chi2 = sum(np.trace(R) ** 2 for R in reps.values()) / 24
    assert abs(chi2 - 1.0) < 1e-10  # irreducible


def test_e8_cocycle_properties():
    coc = cc.E8Cocycle()
    n = coc.self_test(samples=200)
    assert n > 0


def test_native_edge_map_is_antisymmetriser_and_f2_solver():
    data = cc.clebsch_data()
    coc = cc.E8Cocycle()
    sites, colours, orig_of = data["sites"], data["colours"], data["orig_of"]
    (i, j) = data["edges"][0]
    s, t = sites[orig_of[i]], sites[orig_of[j]]
    K = np.zeros((6, 16))
    med = {}
    for a, b in itertools.permutations(range(4), 2):
        alpha, beta = s + colours[a], t + colours[b]
        gamma = cc.add(alpha, beta)
        mu = med.setdefault(gamma, len(med))
        K[mu, 4 * a + b] = coc.eps(alpha, beta)
    S = np.zeros((16, 16))
    for a in range(4):
        for b in range(4):
            S[4 * a + b, 4 * b + a] = 1
    assert np.allclose(K.T @ K, np.eye(16) - S)
    A = np.array([[1, 1, 0], [0, 1, 1], [1, 0, 1]], dtype=np.uint8)
    assert cc.f2_solve(A, np.array([0, 0, 0], dtype=np.uint8))["consistent"]
    assert not cc.f2_solve(A, np.array([1, 0, 0], dtype=np.uint8))["consistent"]


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
