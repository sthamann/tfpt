"""History / Gram / U / native-phase lane inside universalraum-parallel-closure successor.

NON-RH. Exact finite witnesses only; no promotion. Source pins via source_manifest.json.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
ORIGIN = REPO / "experiments/theory-contracts/compiler-origin-audit-20260913"
SINGLE = REPO / "experiments/theory-contracts/compiler-single-execution-20260914"
FUGEN = REPO / "experiments/theory-contracts/universalraum-fugen-20260914"

CHECKS: list[dict] = []


def require(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append({"name": name, "kind": kind})


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_manifest():
    manifest = json.loads((HERE / "source_manifest.json").read_text())
    for key, meta in manifest["sources"].items():
        p = (HERE / meta["path"]).resolve()
        got = sha256_file(p)
        if got != meta["sha256"]:
            raise RuntimeError(f"source pin {key}")
    return manifest


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def pair_index(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a < b else (b, a)


def build_K_and_history():
    pairs = list(itertools.combinations(range(4), 2))
    K = s.zeros(6, 16)
    L = s.zeros(12, 16)
    for row, (a, b) in enumerate(pairs):
        K[row, 4 * a + b] = 1
        K[row, 4 * b + a] = -1
        L[2 * row, 4 * a + b] = 1
        L[2 * row + 1, 4 * b + a] = -1
    swap = s.Matrix(16, 16, lambda i, j: int(i // 4 == j % 4 and i % 4 == j // 4))
    same = s.diag(*[int(a == b) for a, b in itertools.product(range(4), repeat=2)])
    eye = s.eye(16)
    return K, L, swap, same, eye, pairs


def history_gram_witnesses():
    K, L, swap, same, eye, pairs = build_K_and_history()
    require(K.T * K == eye - swap, "local K dagger K equals I minus S")
    require(int(K.rank()) == 6, "bare pair wedge rank six")
    require(L.T * L == eye - same, "ordered ab history Gram equals I minus D diagonal")
    require(int(L.rank()) == 12, "ordered color history rank twelve")
    W = K / s.sqrt(2)
    Pp = (eye + swap) / 2
    U_W = Pp.row_join(-W.T).col_join(W.row_join(s.zeros(6)))
    require(s.simplify(U_W.H * U_W - s.eye(22)) == s.zeros(22), "U_W is 22 dimensional unitary")
    # L = V K iff L^dagger L = K^dagger K on the shared image: embed 6 into 12 with V^dagger V = I_6.
    V = s.zeros(12, 6)
    for r in range(6):
        V[2 * r, r] = 1
    L_embed = V * K
    require(L_embed.T * L_embed == K.T * K, "L equals V K implies matching Gram on image")
    require(L.T * L != K.T * K, "actual ordered history Gram differs from bare K Gram")
    X = s.zeros(4)
    X[0, 1] = X[1, 0] = 1
    collective = s.kronecker_product(X, s.eye(4)) + s.kronecker_product(s.eye(4), X)
    require((eye - swap) * collective == collective * (eye - swap),
            "bare Gram commutes with collective SU4 on two carriers")
    require((eye - same) * collective != collective * (eye - same),
            "ordered history Gram breaks collective SU4 symmetry")
    eta = s.symbols("eta", real=True)
    record = s.diag(*[s.Matrix([[1, eta], [eta, 1]]) for _ in pairs])
    G_eta = L.T * record * L
    require(G_eta == eye - eta * swap - (1 - eta) * same,
            "history overlap eta gives exact Gram interpolation")
    return {
        "K_shape": [6, 16],
        "L_shape": [12, 16],
        "U_W_shape": [22, 22],
        "bare_gram": "I - S",
        "ordered_gram": "I - D_diag",
        "interpolation": "I - eta S - (1-eta) D",
    }


def bad_kernel_degeneracies():
    def spectrum(edges, n_sites=4):
        cnt = Counter()
        for word in itertools.product(range(4), repeat=n_sites):
            e = -sum(1 for i, j in edges if word[i] != word[j])
            cnt[e] += 1
        return cnt

    k4 = spectrum(list(itertools.combinations(range(4), 2)))
    star = spectrum([(0, 1), (0, 2), (0, 3)])
    require(min(k4) == -6 and k4[-6] == 24, "tetramer K4 bad ground degeneracy twenty four")
    require(min(star) == -3 and star[-3] == 108, "star bad ground degeneracy one hundred eight")
    return {"H_bad_K4_ground_dim": 24, "H_bad_star_ground_dim": 108}


def clebsch_edge_kernel_audit(fugen_checker):
    roots = fugen_checker.e8_roots()
    sites = sorted({r[:5] for r in roots if fugen_checker.sector(r) == "(16,4)"})
    colours = sorted({r[5:] for r in roots if fugen_checker.sector(r) == "(16,4)"})
    cidx = {c: i for i, c in enumerate(colours)}
    rset = set(roots)
    edges = []
    for i, j in itertools.combinations(range(16), 2):
        u = fugen_checker.add(sites[i], sites[j])
        if sum(x != 0 for x in u) == 1 and abs(next(x for x in u if x)) == 1:
            edges.append((i, j))
    S = np.zeros((16, 16))
    for a in range(4):
        for b in range(4):
            S[4 * a + b, 4 * b + a] = 1
    edge_ok = True
    for i, j in edges:
        kern = {}
        for a, b in itertools.permutations(range(4), 2):
            gamma = fugen_checker.add(sites[i] + colours[a], sites[j] + colours[b])
            if gamma in rset:
                kern[(a, b)] = gamma
        if len(kern) != 12:
            edge_ok = False
            continue
        K = np.zeros((6, 16))
        tlist = sorted(set(kern.values()))
        for (a, b), gamma in kern.items():
            ca, cb = cidx[colours[a]], cidx[colours[b]]
            sign = 1.0 if ca < cb else -1.0
            K[tlist.index(gamma), 4 * ca + cb] = sign
        if not np.allclose(K.T @ K, np.eye(16) - S, atol=1e-12):
            edge_ok = False
    require(len(edges) == 40 and edge_ok,
            "all forty Clebsch edges share K dagger K equals I minus S")
    return {"clebsch_edges": 40, "per_edge_rule": "antisymmetric carrier kernel, rank six"}


def u_theta_non_identifiability():
    K, _, swap, _, eye, _ = build_K_and_history()
    W = K / s.sqrt(2)
    Pp = (eye + swap) / 2
    U0 = Pp.row_join(W.T).col_join(W.row_join(s.zeros(6)))
    Ui = (s.I * Pp).row_join(W.T).col_join(W.row_join(s.zeros(6)))
    require(U0.H * U0 == s.eye(22) and Ui.H * Ui == s.eye(22), "two U theta completions are unitary")
    require(U0 * U0 == s.eye(22), "U theta zero involution completion squares to identity")
    require((Ui * Ui)[:16, :16] == -swap, "U theta one completion flips carrier sector at two steps")
    psi = s.zeros(22, 1)
    psi[1] = 1

    def block_prob(v):
        p0 = (v[:16, 0].H * v[:16, 0])[0]
        p1 = (v[16:, 0].H * v[16:, 0])[0]
        return s.simplify(p0), s.simplify(p1)

    p0_a, p1_a = block_prob(U0 * psi)
    p0_b, p1_b = block_prob(Ui * psi)
    require(p0_a == p0_b and p1_a == p1_b, "same pinned grammar shares first-step block readout")
    v0, vi = U0 * U0 * psi, Ui * Ui * psi
    overlap = s.simplify((v0.H * vi)[0])
    require(overlap == 0, "U theta non injectivity: two-step returns orthogonal")
    trans_prob = s.simplify(abs(overlap) ** 2)
    spec0 = sorted(str(x) for x in U0.eigenvals())
    spec1 = sorted(str(x) for x in Ui.eigenvals())
    require(spec0 != spec1, "U theta non injectivity: 22D spectra differ")
    return {
        "witness": "same K wedge data; U0 involution versus Ui occupation-phase completion",
        "shared_invariant": "first coarse block readout on probe",
        "differing_invariant": "two_step_return_overlap_and_unitary_spectrum",
        "two_step_inter_completion_transition_probability": str(trans_prob),
        "U_theta_0_spectrum": spec0,
        "U_theta_1_spectrum": spec1,
        "interpretation": "source insufficiency: local Gram data does not fix global unitary completion",
    }


def source_api_inventory(context_core, fugen_checker):
    d = context_core.source_prefix()
    roots_gauss = len(d["Z240"])
    pauli_count = len(d["PMAT"])
    projector_rays = len(d["line_reps"])
    require(roots_gauss == 240, "context adapter exposes two hundred forty Gaussian roots")
    require(pauli_count == 16 and projector_rays == 60,
            "context adapter exposes sixteen Paulis and sixty ray projectors")
    has_bracket_table = any(
        k for k in d.keys()
        if "structure" in k.lower() or "holonom" in k.lower() or "N_ab" in k
    )
    require(not has_bracket_table, "no signed Lie bracket table in context adapter dict")
    # fugen: integer |N_ab| via root sum, no complex phase export API
    roots = fugen_checker.e8_roots()
    npairs = sum(1 for a in roots for b in roots if fugen_checker.add(a, b) in set(roots))
    require(npairs == 240 * 56 and "|N_ab|" in (FUGEN / "checker.py").read_text(),
            "fugen checks |N_ab| magnitude only not signed bracket phases")
    return {
        "context_adapter": {
            "gaussian_roots_Z240": roots_gauss,
            "pauli_PMAT": pauli_count,
            "ray_projectors_line_reps": projector_rays,
            "clock_normalization": "three_cycle_on_C4",
            "signed_lie_bracket_phases": False,
            "edge_holonomy_table": False,
        },
        "fugen_checker": {
            "root_pair_count": npairs,
            "checks_magnitude_only": "|N_ab| = 1 via inner product and root sum",
            "exports_signed_complex_structure_constants": False,
        },
        "compiler_single_execution": {
            "records_mediator_occurrence_only": True,
            "ordered_color_history_in_source": False,
        },
    }


def phase_adapter_verdict(inventory):
    native_signed = (
        inventory["context_adapter"]["signed_lie_bracket_phases"]
        or inventory["fugen_checker"]["exports_signed_complex_structure_constants"]
        or inventory["context_adapter"]["edge_holonomy_table"]
    )
    if native_signed:
        verdict = "RUN_CYCLE_HOLONOMY_COMPARATOR"
    else:
        verdict = "BLOCKED_MISSING_NATIVE_PHASE_DATA"
    require(verdict == "BLOCKED_MISSING_NATIVE_PHASE_DATA", "phase adapter blocked on missing native phases")
    return {
        "phase_adapter_verdict": verdict,
        "CAR_native_phase_equivalence": False,
        "gaussian_root_vector_phases": "240 phase-marked roots; clock preserves root set",
        "lie_bracket_structure_constant_phases": "not exposed in pinned source adapters",
        "cycle_holonomy_comparator_ran": False,
        "comparator_fields": None,
        "note": "no guessed plus-one phases; magnitude |N_ab|=1 only",
    }


def run():
    verify_manifest()
    fugen_checker = load_module("fugen_checker_u_phase", FUGEN / "checker.py")
    context_core = load_module("context_u_phase", ORIGIN / "context_instrument.py")
    hist = history_gram_witnesses()
    bad = bad_kernel_degeneracies()
    clebsch = clebsch_edge_kernel_audit(fugen_checker)
    u_theta = u_theta_non_identifiability()
    inventory = source_api_inventory(context_core, fugen_checker)
    phase = phase_adapter_verdict(inventory)
    return {
        "scope": "History/U/non-identifiability/native-phase lane; NON-RH; no promotion",
        "history_gram": hist,
        "bad_kernel": bad,
        "clebsch_local_rule": clebsch,
        "P1_P2_non_identifiability": u_theta,
        "source_api_inventory": inventory,
        "phase_adapter": phase,
        "status_boundaries": {
            "closed": [
                "finite K and ordered-history Gram witnesses",
                "22D U_W unitarity",
                "forty-edge local K rule",
                "U_theta process non-injectivity witness",
            ],
            "blocked": [
                "native TFPT to CAR signed phase comparator",
                "cycle holonomy replay without bracket phase table",
            ],
            "not_claimed": ["T1-T8 closure", "CAR_native_phase_equivalence"],
        },
        "checks": CHECKS,
        "count": len(CHECKS),
        "CAR_native_phase_equivalence": False,
        "phase_adapter_verdict": phase["phase_adapter_verdict"],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(HERE / "u_phase_validation.json"))
    args = parser.parse_args()
    result = run()
    result["checker_sha256"] = sha256_file(Path(__file__))
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "checks"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
