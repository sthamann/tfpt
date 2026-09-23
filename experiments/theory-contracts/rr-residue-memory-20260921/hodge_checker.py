#!/usr/bin/env python3
"""Exact smallest-gate test for the RR family Hodge/source bridge.

The test keeps the marked D5+A3 discriminant glue explicit, distinguishes
the RR boson-basis Hodge map from an active source symmetry, and checks the
finite Pin(6) lift that would be available only after restoring both family
chiral blocks.  It makes no physical field, locality, or time-selection claim.
"""

from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
RR_CHECKER = Path(
    "/Users/stefanhamann/Documents/Codex/2026-09-21/l-s/outputs/"
    "TFPT_RR_Quellenbruecke/RR_W_CHECK.py"
)
TENSOR = ROOT / (
    "experiments/theory-contracts/universalraum-v16-integrated-20260915/"
    "sources/native_tensor.npz"
)

PINS = {
    ROOT / "verification/v92_glue_uniqueness.py":
        "bafe88d89cfab2125e205dfed56ddddbb4d3a23cb623582e6f173acdc497d1c5",
    ROOT / "verification/v154_simple_current_theorem.py":
        "928aff32e0e5d9d440d326cb6f8a12dbb119d7cf86ccf6c2ea95a469f185e4c5",
    ROOT / (
        "experiments/theory-contracts/source-operator-origin-20260920/"
        "family_intertwiner/PROOF.md"
    ): "ef5d0278862523d27ba23e9b8fbf4e91e604c888923befb4378d71fc9c6cdffa",
    ROOT / (
        "experiments/theory-contracts/source-charged-extension-selection-20260921/"
        "PROOF.txt"
    ): "6bb8cb37f1461d76d9371c813e7e883d142fb27f5066591d37753b9c396d6e9a",
    ROOT / (
        "experiments/theory-contracts/universalraum-keyD-native-instruments-20260915/"
        "native_source.py"
    ): "380577f85d2afa8b50f91a0991769eaf8267ee5c09f327d87f17e1b4c0af1672",
    RR_CHECKER:
        "16fdfc6a8f1dab3fa09f5d0ab1a019abbd930c17553b0e5d4cddcb7e8376c4b4",
    TENSOR:
        "3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763",
}


class Failure(RuntimeError):
    pass


def need(condition: bool, label: str) -> None:
    if not bool(condition):
        raise Failure(label)


def subgroup(generator: tuple[int, int]) -> frozenset[tuple[int, int]]:
    return frozenset(((k * generator[0]) % 4, (k * generator[1]) % 4)
                     for k in range(4))


def q_form(value: tuple[int, int]) -> F:
    x, y = value
    return F(5 * x * x + 3 * y * y, 8) % 1


def hodge_six() -> sp.Matrix:
    pairs = list(combinations(range(4), 2))
    index = {pair: j for j, pair in enumerate(pairs)}
    K = sp.zeros(6)
    for column, (a, b) in enumerate(pairs):
        complement = tuple(j for j in range(4) if j not in (a, b))
        permutation = (a, b, *complement)
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(4) for j in range(i + 1, 4))
        K[index[complement], column] = (-1) ** inversions
    return K


def wedge2(matrix: sp.Matrix) -> sp.Matrix:
    pairs = list(combinations(range(4), 2))
    result = sp.zeros(6)
    for column, (i, j) in enumerate(pairs):
        vi = matrix[:, i]
        vj = matrix[:, j]
        for row, (a, b) in enumerate(pairs):
            result[row, column] = vi[a] * vj[b] - vi[b] * vj[a]
    return result


def jw(n: int) -> list[sp.Matrix]:
    result = []
    for j in range(n):
        matrix = sp.zeros(2**n)
        for mask in range(2**n):
            if (mask >> j) & 1:
                sign = (-1) ** ((mask & ((1 << j) - 1)).bit_count())
                matrix[mask ^ (1 << j), mask] = sign
        result.append(matrix)
    return result


def exact_run() -> dict:
    checks: list[dict] = []

    def record(identifier: str, details: dict) -> None:
        checks.append({"id": identifier, "status": "PASS", "details": details})

    for path, wanted in PINS.items():
        need(sha256(path.read_bytes()).hexdigest() == wanted,
             f"source pin changed: {path}")
    record("source_pins", {"count": len(PINS)})

    # Primitive marked D5+A3 glue gate.
    H_plus = subgroup((1, 1))
    H_minus = subgroup((1, 3))
    all_order4_cyclic = {subgroup((x, y)) for x in range(4) for y in range(4)
                         if len(subgroup((x, y))) == 4}
    isotropic = {H for H in all_order4_cyclic
                 if all(q_form(element) == 0 for element in H)}
    need(isotropic == {H_plus, H_minus}, "exactly two Lagrangian Z4 glues")
    record("primitive_glue_classification", {
        "q": "(5*x^2+3*y^2)/8 mod 1",
        "lagrangian_glues": ["<(1,1)>", "<(1,3)>"]
    })

    family_conj = lambda value: (value[0], (-value[1]) % 4)
    carrier_conj = lambda value: ((-value[0]) % 4, value[1])
    both_conj = lambda value: ((-value[0]) % 4, (-value[1]) % 4)
    need(frozenset(map(family_conj, H_plus)) == H_minus,
         "family conjugation must swap the marked glue")
    need(frozenset(map(carrier_conj, H_plus)) == H_minus,
         "carrier conjugation must swap the marked glue")
    need(frozenset(map(both_conj, H_plus)) == H_plus,
         "simultaneous conjugation must preserve the marked glue")
    record("marked_glue_automorphisms", {
        "family_only": "H_plus -> H_minus",
        "carrier_only": "H_plus -> H_minus",
        "simultaneous": "H_plus -> H_plus"
    })

    need((1, 1) in H_plus and (3, 3) in H_plus and
         (1, 3) in H_minus and (3, 1) in H_minus,
         "oriented odd-sector labels")
    record("oriented_representation_content", {
        "H_plus_odd": ["(16,4)", "(bar16,bar4)"],
        "H_minus_odd": ["(16,bar4)", "(bar16,4)"],
        "decision": "desired crossed family chirality requires the other marked glue"
    })

    # RR Hodge map and the natural SU(4) real six.
    K = hodge_six()
    need(K * K == sp.eye(6) and K.T * K == sp.eye(6) and K.det() == -1,
         "Hodge is an orientation-reversing O(6) involution")
    record("hodge_orientation", {
        "K_squared": "I6", "det_K": -1,
        "real_structure": "J(x)=K*conjugate(x)"
    })

    # A raw odd mark permutation is not an SU(4)-real O(6) action.  Its
    # determinant-normalized lift is: choose c=e^{-i*pi/4}, so wedge2(cP)
    # is -i*wedge2(P) and det(cP)=1.
    P = sp.zeros(4)
    for j in range(4):
        P[(j + 1) % 4, j] = 1
    A = wedge2(P)
    A_su = -sp.I * A
    need(P.det() == -1 and A.det() == -1, "raw D4 mark lift orientation")
    need(K * A == -A * K, "raw determinant-minus-one lift anticommutes with J")
    need(A_su * K == K * A_su.conjugate(),
         "SU4-normalized lift preserves the natural real structure")
    need(A_su.det() == 1,
         "SU4-normalized six-dimensional action is orientation preserving")
    record("d4_su4_normalization", {
        "raw": "Lambda2(P), det=-1, not J-real",
        "normalized": "-i Lambda2(P), det=+1, J-real SO(6)",
        "consequence": "D4 covariance alone supplies no Pin block exchange"
    })

    # The Hodge reflection itself has an algebraic odd Pin lift on the full
    # precompression Cl6 module.  This only proves existence in M8.
    annihilators = jw(3)
    gammas = [a + a.T for a in annihilators]
    gammas += [sp.I * (a.T - a) for a in annihilators]
    positive_vectors = []
    for first, second, sign in ((0, 5, 1), (1, 4, -1), (2, 3, 1)):
        vector = sp.zeros(6, 1)
        vector[first] = 1 / sp.sqrt(2)
        vector[second] = sign / sp.sqrt(2)
        positive_vectors.append(vector)
    C = sp.eye(8)
    for vector in positive_vectors:
        C *= sum((vector[a] * gammas[a] for a in range(6)), sp.zeros(8))
    Cinv = C.inv()
    pin_covariance = []
    for a in range(6):
        target = sum((K[b, a] * gammas[b] for b in range(6)), sp.zeros(8))
        pin_covariance.append(sp.simplify(C * gammas[a] * Cinv - target) == sp.zeros(8))
    even = [mask for mask in range(8) if mask.bit_count() % 2 == 0]
    P_plus = sp.diag(*[1 if mask in even else 0 for mask in range(8)])
    need(all(pin_covariance) and
         sp.simplify(C.conjugate().T * C - sp.eye(8)) == sp.zeros(8) and
         sp.simplify(C * C + sp.eye(8)) == sp.zeros(8),
         "exact Pin lift of K")
    need(sp.simplify(C * P_plus * Cinv) == sp.eye(8) - P_plus,
         "Pin lift exchanges the two chiral blocks")
    record("conditional_pin_lift", {
        "exists_in": "full precompression Cl6(C)=M8",
        "C_squared": "-I8",
        "block_action": "Pplus <-> Pminus",
        "scope": "algebraic existence only; no sourced Hamiltonian symmetry"
    })

    # The actual RR construction postcomposes the 60 boson rows by K.  It is
    # not an active invariance of the fixed native tensor.
    with np.load(TENSOR, allow_pickle=False) as source:
        W_complex = source["W"]
    need(np.array_equal(W_complex.imag, np.zeros_like(W_complex.imag)),
         "native W real")
    W = np.rint(W_complex.real).astype(np.int64)
    K_np = np.asarray(K.tolist(), dtype=np.int64)
    W_sharp = np.kron(np.eye(10, dtype=np.int64), K_np) @ W
    need(not np.array_equal(W_sharp, W), "K is not a fixed-W symmetry")
    need(np.count_nonzero(W_sharp - W) == 960 and
         np.count_nonzero((W_sharp == W) & (W != 0)) == 0,
         "every supported W coefficient is moved to a distinct boson row")
    need(np.array_equal(W_sharp @ W_sharp.T, W @ W.T),
         "Hodge postcomposition preserves the boson row Gram")
    record("rr_hodge_role", {
        "operation": "Wsharp=(I10 tensor K)W",
        "Wsharp_equals_W": False,
        "difference_nonzeros": 960,
        "unchanged_supported_coefficients": 0,
        "interpretation": "isometric boson-basis transport, not fixed-source symmetry"
    })

    return {
        "schema_version": 1,
        "status": "PASS_EXACT_SCOPED",
        "verdict": (
            "FIXED_MARKED_GLUE_REJECTS_FAMILY_ONLY_TWIST; "
            "RR_HODGE_IS_BOSON_BASIS_TRANSPORT_NOT_A_SOURCED_BLOCK_EXCHANGE; "
            "AN_ALGEBRAIC_PIN_LIFT_EXISTS_ONLY_ON_THE_RESTORED_M8"
        ),
        "scope": (
            "Exact discriminant-form, finite Hodge/Pin, and native-W tests. "
            "No field localization, common time, or physical source-selection claim."
        ),
        "checks": checks,
        "summary": {
            "pass_count": len(checks),
            "fail_count": 0,
            "fixed_marked_source_bridge": "REJECTED",
            "explicit_sheet_reinterpretation": "ALGEBRAICALLY_ALLOWED_BUT_CHANGES_MARKED_GLUE",
            "delta_offset_selected": False,
            "physical_gate_closed": False,
        },
    }


def main() -> int:
    output = HERE / "certificate.json"
    try:
        result = exact_run()
        exit_code = 0
    except Exception as exc:
        result = {
            "schema_version": 1,
            "status": "FAIL",
            "failure": f"{type(exc).__name__}: {exc}",
            "summary": {"pass_count": 0, "fail_count": 1},
        }
        exit_code = 1
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
