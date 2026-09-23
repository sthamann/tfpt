#!/usr/bin/env python3
"""Exact smallest-current test for the root-diagonal adjoint/dual encoding.

Every E8 root supplies an sl2 triple (e, h, f).  The test works entirely
inside that mandatory subalgebra, so leakage here rules out invariance under
the full E8 current zero-mode algebra.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def subtract(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[x - y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def require(ok: bool, name: str) -> None:
    if not ok:
        raise RuntimeError(name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    # Ordered adjoint basis (e, h, f), with [e,h]=-2e and [e,f]=h.
    ad_e = [
        [0, -2, 0],
        [0, 0, 1],
        [0, 0, 0],
    ]
    p_f = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1],
    ]
    identity = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]

    current_on_p_f = subtract(matmul(ad_e, p_f), matmul(p_f, ad_e))
    current_on_identity = subtract(matmul(ad_e, identity), matmul(identity, ad_e))

    # A linear combination of the two root projectors P_e,P_f is diagonal
    # and therefore has no h<-f matrix element.  The current action has one.
    require(current_on_p_f[1][2] == 1, "Cartan leakage is nonzero")
    require(
        current_on_identity == [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        "full identity is current invariant",
    )

    result = {
        "status": "EXACT_ROOT_DIAGONAL_CURRENT_CLOSURE_FAIL",
        "scope": "the sl2 root triple contained in the E8 weight-one current algebra",
        "basis": ["E_alpha", "H_alpha", "E_minus_alpha"],
        "ad_E_alpha": ad_e,
        "root_projector_P_minus_alpha": p_f,
        "diagonal_current_action_commutator": current_on_p_f,
        "decisive_leakage": {
            "matrix_entry": "H_alpha <- E_minus_alpha",
            "value": 1,
            "reason": "[E_alpha,E_minus_alpha]=H_alpha",
        },
        "root_diagonal_subspace_invariant": False,
        "full_identity_operator_invariant": True,
        "full_identity_commutator": current_on_identity,
        "phase_pairing_lemma": "For |eta|=1, eta*conjugate(eta)=1 on each E_alpha tensor conjugate(E_alpha).",
        "interpretation": "Finite root-monomial lift phases cancel on paired root labels, but that 240-dimensional diagonal root space is not a representation of the full current algebra.",
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
