"""Decisive deck-to-trimer covariance checks.

This module does not add a deck identification.  It tests the actual tensor
and operator actions that a proposed identification has to respect:

* the four-leg event tensor ``G`` and all of its S4 leg permutations;
* the six permutations of the typed trimer ``U tensor Ubar tensor U``;
* covariance with the diagonal connection, both on the fixed typed bundle and
  after transporting the connection with the permutation;
* the absence of a complex-linear SU(5) adapter ``U -> Ubar``;
* the distinction between the 15-event covariance of ``G`` and the full
  SU(5)-covariance of the established path intertwiner ``W``.

The resulting statement is deliberately narrow: outer-leg exchange is the
unique nontrivial trimer permutation that is an endomorphism of the already
typed bundle, and it fixes both W and G.  Covariance under a transported
connection is natural for every permutation but does not select one as the
geometric P1 covering deck.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import permutations, product
import json
import math
from typing import Any

import numpy as np
import sympy as sp

from .composition import _su_generators
from .consolidation import _covariant_chain
from .process import _invariants


DIMENSION = 5
TRIMER_DIMENSION = DIMENSION**3


def _permutation_operator(permutation: tuple[int, int, int]) -> np.ndarray:
    """Return P with P vec(T) = vec(transpose(T, permutation))."""

    indices = np.arange(TRIMER_DIMENSION).reshape((DIMENSION,) * 3)
    source_indices = indices.transpose(permutation).reshape(-1)
    return np.eye(TRIMER_DIMENSION)[source_indices]


def _collective(generator: np.ndarray) -> np.ndarray:
    """Connection action on U tensor Ubar tensor U."""

    identity = np.eye(DIMENSION, dtype=complex)
    return (
        np.kron(np.kron(generator, identity), identity)
        - np.kron(np.kron(identity, generator.T), identity)
        + np.kron(np.kron(identity, identity), generator)
    )


def _sl5_basis() -> list[np.ndarray]:
    basis: list[np.ndarray] = []
    for row, column in product(range(DIMENSION), repeat=2):
        if row != column:
            matrix = np.zeros((DIMENSION, DIMENSION))
            matrix[row, column] = 1
            basis.append(matrix)
    for index in range(DIMENSION - 1):
        matrix = np.zeros((DIMENSION, DIMENSION))
        matrix[index, index] = 1
        matrix[index + 1, index + 1] = -1
        basis.append(matrix)
    return basis


def _linear_map_rank(dual_target: bool) -> int:
    """Rank of the equations for Hom_sl5(U,Ubar) or End_sl5(U)."""

    equations = []
    for generator in _sl5_basis():
        for out_row, out_column in product(range(DIMENSION), repeat=2):
            row = np.zeros(DIMENSION**2)
            for source_row, source_column in product(range(DIMENSION), repeat=2):
                variable = source_row * DIMENSION + source_column
                # target_action @ D - D @ source_action
                target_action = -generator.T if dual_target else generator
                coefficient = 0.0
                if source_column == out_column:
                    coefficient += target_action[out_row, source_row]
                if source_row == out_row:
                    coefficient -= generator[source_column, out_column]
                row[variable] = coefficient
            equations.append(row)
    # All coefficients are integers.  SymPy therefore decides the rank over Q
    # without a numerical tolerance.
    return int(sp.Matrix(np.asarray(equations, dtype=int)).rank())


def _tensor_g(invariants: dict[str, Any]) -> np.ndarray:
    identity = np.eye(DIMENSION)
    tensor_a = (
        np.einsum("ab,cd->abcd", identity, identity)
        + np.einsum("ac,bd->abcd", identity, identity)
        + np.einsum("ad,bc->abcd", identity, identity)
    )
    simplex = invariants["coordinate_map"]
    tensor_c = np.einsum("ia,ib,ic,id->abcd", simplex, simplex, simplex, simplex)
    return tensor_c + tensor_a / 6


@lru_cache(maxsize=1)
def build_deck_constraint_data() -> dict[str, Any]:
    invariants = _invariants()
    chain = _covariant_chain()
    tensor_g = _tensor_g(invariants)
    encoder_g = tensor_g.reshape(TRIMER_DIMENSION, DIMENSION) / math.sqrt(2)
    encoder_w = chain["w"].astype(complex)
    identity125 = np.eye(TRIMER_DIMENSION)

    four_leg_residuals = {}
    for permutation in permutations(range(4)):
        key = "".join(str(index + 1) for index in permutation)
        four_leg_residuals[key] = float(
            np.linalg.norm(tensor_g - tensor_g.transpose(permutation))
        )

    generators = [matrix.astype(complex) for matrix in _sl5_basis()]
    roles = ("U", "Ubar", "U")
    trimer_rows = []
    transported_covariance_max = 0.0
    fixed_connection_covariance_max_by_permutation: dict[str, float] = {}
    for permutation in permutations(range(3)):
        operator = _permutation_operator(permutation).astype(complex)
        permuted_w = operator @ encoder_w
        transported_residual = 0.0
        fixed_residual = 0.0
        commutator_residual = 0.0
        for generator in generators:
            connection = _collective(generator)
            transported_connection = operator @ connection @ operator.T.conj()
            transported_residual = max(
                transported_residual,
                float(
                    np.linalg.norm(
                        transported_connection @ permuted_w - permuted_w @ generator
                    )
                ),
            )
            fixed_residual = max(
                fixed_residual,
                float(np.linalg.norm(connection @ permuted_w - permuted_w @ generator)),
            )
            commutator_residual = max(
                commutator_residual,
                float(np.linalg.norm(connection @ operator - operator @ connection)),
            )
        key = "".join(str(index + 1) for index in permutation)
        transported_covariance_max = max(transported_covariance_max, transported_residual)
        fixed_connection_covariance_max_by_permutation[key] = fixed_residual
        trimer_rows.append(
            {
                "permutation": key,
                "roles_after_permutation": [roles[index] for index in permutation],
                "preserves_fixed_typing": tuple(roles[index] for index in permutation) == roles,
                "transported_connection_covariance_residual": transported_residual,
                "fixed_connection_covariance_residual": fixed_residual,
                "fixed_connection_commutator_norm": commutator_residual,
                "fixes_W": float(np.linalg.norm(permuted_w - encoder_w)) < 1e-12,
                "fixes_G": float(np.linalg.norm(operator @ encoder_g - encoder_g)) < 1e-12,
            }
        )

    outer_swap = _permutation_operator((2, 1, 0)).astype(complex)
    projector_g = encoder_g @ encoder_g.T.conj()
    projector_w = encoder_w @ encoder_w.T.conj()
    full_su5_g_leakage = 0.0
    full_su5_w_leakage = 0.0
    for generator in _su_generators():
        connection = _collective(generator.astype(complex))
        full_su5_g_leakage = max(
            full_su5_g_leakage,
            float(np.linalg.norm((identity125 - projector_g) @ connection @ encoder_g)),
        )
        full_su5_w_leakage = max(
            full_su5_w_leakage,
            float(np.linalg.norm((identity125 - projector_w) @ connection @ encoder_w)),
        )

    event_covariance = 0.0
    for event in invariants["transpositions"]:
        physical_event = np.kron(np.kron(event, event), event)
        event_covariance = max(
            event_covariance,
            float(np.linalg.norm(physical_event @ encoder_g - encoder_g @ event)),
        )

    dual_rank = _linear_map_rank(dual_target=True)
    end_rank = _linear_map_rank(dual_target=False)
    dual_nullity = DIMENSION**2 - dual_rank
    end_nullity = DIMENSION**2 - end_rank

    checks = [
        {
            "name": "G is invariant under all 24 S4 leg permutations",
            "ok": max(four_leg_residuals.values()) < 1e-12,
            "actual": max(four_leg_residuals.values()),
            "expected": 0,
        },
        {
            "name": "all six trimer permutations are covariant after transporting the connection",
            "ok": transported_covariance_max < 1e-12,
            "actual": transported_covariance_max,
            "expected": 0,
        },
        {
            "name": "only identity and outer swap preserve U-Ubar-U typing",
            "ok": [row["permutation"] for row in trimer_rows if row["preserves_fixed_typing"]]
            == ["123", "321"],
            "actual": [row["permutation"] for row in trimer_rows if row["preserves_fixed_typing"]],
            "expected": ["123", "321"],
        },
        {
            "name": "there is no nonzero complex-linear sl5 intertwiner U to Ubar",
            "ok": dual_nullity == 0 and end_nullity == 1,
            "actual": {"Hom(U,Ubar)": dual_nullity, "End(U)": end_nullity},
            "expected": {"Hom(U,Ubar)": 0, "End(U)": 1},
        },
        {
            "name": "outer swap fixes both covariant path W and quartic encoder G",
            "ok": bool(
                max(
                    np.linalg.norm(outer_swap @ encoder_w - encoder_w),
                    np.linalg.norm(outer_swap @ encoder_g - encoder_g),
                )
                < 1e-12
            ),
            "actual": {
                "W": float(np.linalg.norm(outer_swap @ encoder_w - encoder_w)),
                "G": float(np.linalg.norm(outer_swap @ encoder_g - encoder_g)),
            },
            "expected": 0,
        },
        {
            "name": "G closes on the 15 event generators but not on a five-dimensional full SU5 module",
            "ok": event_covariance < 1e-12 and full_su5_g_leakage > 1e-6,
            "actual": {
                "event_residual": event_covariance,
                "full_su5_leakage": full_su5_g_leakage,
                "W_full_su5_leakage_control": full_su5_w_leakage,
            },
            "expected": {
                "event_residual": 0,
                "full_su5_leakage": "nonzero",
                "W_full_su5_leakage_control": 0,
            },
        },
    ]

    return {
        "status": "PASS" if all(check["ok"] for check in checks) else "FAIL",
        "checks": checks,
        "four_leg_S4": {
            "permutations_tested": 24,
            "maximum_residual": max(four_leg_residuals.values()),
            "residuals": four_leg_residuals,
            "consequence": (
                "G alone does not distinguish a deck leg action; every leg permutation "
                "lies in its tensor stabilizer."
            ),
        },
        "typed_trimer": {
            "roles": list(roles),
            "permutations": trimer_rows,
            "complex_linear_duality_adapter": {
                "Hom_sl5_U_to_Ubar_dimension": dual_nullity,
                "End_sl5_U_dimension": end_nullity,
                "consequence": (
                    "the four permutations that move the conjugate leg need a change of "
                    "bundle typing or an antilinear structure; they are not internal linear "
                    "symmetries of the fixed U-Ubar-U trimer"
                ),
            },
        },
        "operator_scope": {
            "outer_swap_restriction_to_W": "plus identity",
            "outer_swap_restriction_to_G": "plus identity",
            "G_event_covariance_residual": event_covariance,
            "G_full_su5_five_space_leakage": full_su5_g_leakage,
            "W_full_su5_five_space_leakage_control": full_su5_w_leakage,
        },
        "verdict": {
            "derived": (
                "After the U-Ubar-U typing and its diagonal connection are fixed, outer "
                "exchange S13 is the unique nontrivial leg permutation that stays inside "
                "that same typed bundle.  It is connection-covariant and fixes W and G."
            ),
            "not_derived": (
                "Nothing in G, S4 covariance, or transported-connection naturality identifies "
                "S13 with the free P1 covering deck or its fermionic spin lift.  All S4 legs "
                "are symmetric in G, and transported covariance holds for every permutation."
            ),
            "smallest_missing_map": (
                "A source-level associated-bundle intertwiner must map the geometric P1 deck "
                "and spin lift to the typed trimer action while preserving the connection, "
                "CAR conjugation, state, and pair vertex."
            ),
        },
    }


if __name__ == "__main__":
    print(json.dumps(build_deck_constraint_data(), indent=2, sort_keys=True))
