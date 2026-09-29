"""Typed continuation of the original three-channel seam transfer.

The original local rule is the symmetric *survival* operator

    M = 1/2 I + 1/6 sigma + 1/3 P0,

where ``sigma`` fixes the absorbing slot and swaps the remaining two
double-cover slots.  This module tests the corresponding continuation on the
existing ``U tensor Ubar tensor U`` trimer.  The continuation is conditional
on three explicit identifications: the original internal Z2 pair-swap is
represented by exchanging the two outer ``U`` legs, the absorbing slot is represented by
the established covariant trimer isometry ``W``, and the untouched complement
is assumed scalar on outer-swap parity sectors.

Under those identifications the continuation is forced inside the three-term
ansatz patterned on the original rule:

    C = 1/2 I + 1/6 S_13 + 1/3 W W^dagger.

Without the third identification, the compatible family
``C_eta=C+eta(P_minus-P_Z)`` proves that the 45-dimensional odd complement is
not fixed by the W/R/Z clock data.  ``C`` is a positive self-adjoint
amplitude/Euclidean-transfer contraction.  It is not, by this construction
alone, a CPTP density-matrix channel or a proof of a spatial RG coarse
graining.
"""

from __future__ import annotations

from functools import lru_cache
import math
from typing import Any

import numpy as np
import sympy as sp

from .composition import _su_generators
from .consolidation import _covariant_chain
from .process import _invariants


DIMENSION = 5
PHYSICAL_DIMENSION = DIMENSION**3


def _check(name: str, ok: bool, actual: Any, expected: Any, method: str) -> dict[str, Any]:
    return {
        "name": name,
        "ok": bool(ok),
        "actual": actual,
        "expected": expected,
        "method": method,
    }


def _outer_swap() -> np.ndarray:
    """Swap the two equally oriented outer factors in 5 x 5bar x 5."""

    swap = np.zeros((PHYSICAL_DIMENSION, PHYSICAL_DIMENSION))
    for first in range(DIMENSION):
        for middle in range(DIMENSION):
            for third in range(DIMENSION):
                source = DIMENSION**2 * first + DIMENSION * middle + third
                target = DIMENSION**2 * third + DIMENSION * middle + first
                swap[target, source] = 1
    return swap


def _second_intertwiner() -> np.ndarray:
    """The outer-antisymmetric fundamental copy Z=(A-B)/sqrt(8)."""

    left = np.zeros((PHYSICAL_DIMENSION, DIMENSION))
    right = np.zeros_like(left)
    for a in range(DIMENSION):
        for b in range(DIMENSION):
            for c in range(DIMENSION):
                row = DIMENSION**2 * a + DIMENSION * b + c
                if a == b:
                    left[row, c] = 1
                if b == c:
                    right[row, a] = 1
    return (left - right) / math.sqrt(8)


def _small_rules() -> dict[str, Any]:
    """Exact three-dimensional survival, Markov and readout operators."""

    half = sp.Rational(1, 2)
    sixth = sp.Rational(1, 6)
    third = sp.Rational(1, 3)
    survival = sp.Matrix(
        [[1, 0, 0], [0, half, sixth], [0, sixth, half]]
    )
    deck = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    p0 = sp.diag(1, 0, 0)

    # If the missing survival probability is explicitly routed into the
    # absorbing slot, the column-stochastic completion is different and has
    # an oblique Perron projector.  It is recorded to prevent conflation with
    # the symmetric survival operator used by the original clock calculation.
    absorbing_markov = sp.Matrix(
        [[1, third, third], [0, half, sixth], [0, sixth, half]]
    )
    oblique_pf = sp.Matrix([[1, 1, 1], [0, 0, 0], [0, 0, 0]])

    e0 = sp.Matrix([1, 0, 0])
    even = sp.Matrix([0, 1, 1]) / sp.sqrt(2)
    odd = sp.Matrix([0, 1, -1]) / sp.sqrt(2)
    survival_eigenbasis = sp.Matrix.hstack(e0, even, odd)

    fixed = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    recovery = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
    subdominant = sp.Matrix([1, 1, -2]) / sp.sqrt(6)
    symmetric_eigenbasis = sp.Matrix.hstack(fixed, recovery, subdominant)
    symmetric_clock = sp.Matrix(
        [[13, 1, 4], [1, 13, 4], [4, 4, 10]]
    ) / 18
    change_of_basis = symmetric_eigenbasis * survival_eigenbasis.T

    def zero_matrix(matrix: sp.Matrix) -> bool:
        return all(sp.simplify(value) == 0 for value in matrix)

    exact = {
        "survival_formula": survival == half * sp.eye(3) + sixth * deck + third * p0,
        "survival_is_symmetric": survival == survival.T,
        "survival_projector_is_orthogonal": p0 == p0.T and p0 * p0 == p0,
        "survival_row_sums": [sum(survival.row(i)) for i in range(3)],
        "markov_column_sums": [sum(absorbing_markov[:, j]) for j in range(3)],
        "markov_pf": absorbing_markov * oblique_pf == oblique_pf,
        "markov_pf_idempotent": oblique_pf * oblique_pf == oblique_pf,
        "markov_pf_is_oblique": oblique_pf != oblique_pf.T,
        "basis_is_orthogonal": zero_matrix(
            change_of_basis.T * change_of_basis - sp.eye(3)
        ),
        "symmetric_similarity": zero_matrix(
            symmetric_clock - change_of_basis * survival * change_of_basis.T
        ),
        "fixed_projector_similarity": zero_matrix(
            change_of_basis * p0 * change_of_basis.T - sp.ones(3, 3) / 3
        ),
    }
    return {
        "survival": survival,
        "deck": deck,
        "p0": p0,
        "absorbing_markov": absorbing_markov,
        "oblique_pf": oblique_pf,
        "survival_eigenbasis": survival_eigenbasis,
        "symmetric_eigenbasis": symmetric_eigenbasis,
        "symmetric_clock": symmetric_clock,
        "change_of_basis": change_of_basis,
        "exact": exact,
    }


def _rational_list(values: list[sp.Expr]) -> list[str]:
    return [str(sp.simplify(value)) for value in values]


@lru_cache(maxsize=1)
def build_origin_transfer_data() -> dict[str, Any]:
    """Return JSON-safe data and checks for the original-rule continuation."""

    small = _small_rules()
    invariants = _invariants()
    chain = _covariant_chain()
    identity = np.eye(PHYSICAL_DIMENSION)
    identity5 = np.eye(DIMENSION)
    w = chain["w"].astype(complex)
    g = invariants["v_triangle"].astype(complex)
    z = _second_intertwiner().astype(complex)
    remainder = (g - math.sqrt(2 / 3) * w) / math.sqrt(1 / 3)
    swap = _outer_swap().astype(complex)
    p_w = w @ w.T.conj()
    p_z = z @ z.T.conj()
    p_even = (identity + swap) / 2
    p_odd = (identity - swap) / 2
    p_45 = p_odd - p_z

    # Unique coefficients in a I+b S_13+c P_W with the inherited clock
    # eigenvalues on W, the even complement and the odd sector.
    a, b, c = sp.symbols("a b c")
    coefficient_solutions = sp.solve(
        [
            sp.Eq(a + b + c, 1),
            sp.Eq(a + b, sp.Rational(2, 3)),
            sp.Eq(a - b, sp.Rational(1, 3)),
        ],
        [a, b, c],
        dict=True,
    )
    coefficients = coefficient_solutions[0]
    transfer = (
        float(coefficients[a]) * identity
        + float(coefficients[b]) * swap
        + float(coefficients[c]) * p_w
    )

    projector_errors = {
        "W_isometry": float(np.linalg.norm(w.T.conj() @ w - identity5)),
        "PW_projector": float(np.linalg.norm(p_w @ p_w - p_w)),
        "swap_involution": float(np.linalg.norm(swap @ swap - identity)),
        "swap_PW_commutator": float(np.linalg.norm(swap @ p_w - p_w @ swap)),
        "W_even": float(np.linalg.norm(swap @ w - w)),
        "Z_odd": float(np.linalg.norm(swap @ z + z)),
        "R_even": float(np.linalg.norm(swap @ remainder - remainder)),
        "PZ_projector": float(np.linalg.norm(p_z @ p_z - p_z)),
        "P45_projector": float(np.linalg.norm(p_45 @ p_45 - p_45)),
    }
    p_45_rank = int(np.linalg.matrix_rank(p_45, tol=1e-10))

    eigenvalues = np.linalg.eigvalsh(transfer)
    spectrum = {
        "1": int(np.count_nonzero(np.isclose(eigenvalues, 1, atol=1e-11))),
        "2/3": int(np.count_nonzero(np.isclose(eigenvalues, 2 / 3, atol=1e-11))),
        "1/3": int(np.count_nonzero(np.isclose(eigenvalues, 1 / 3, atol=1e-11))),
    }
    lower_bound = float(eigenvalues[0])
    upper_bound = float(eigenvalues[-1])

    # Typed intertwiners.  J_eig orders the physical sectors as
    # fixed/even-recovery/odd-subdominant.  L uses the original absorbing
    # coordinates; K uses the symmetric cusp B coordinates.
    j_eigen = np.concatenate((w, remainder, z), axis=1)
    u_m = np.array(small["survival_eigenbasis"].evalf(), dtype=float)
    u_b = np.array(small["symmetric_eigenbasis"].evalf(), dtype=float)
    m = np.array(small["survival"], dtype=float)
    clock_b = np.array(small["symmetric_clock"], dtype=float)
    l_absorbing = j_eigen @ np.kron(u_m.T, identity5)
    k_symmetric = j_eigen @ np.kron(u_b.T, identity5)
    diagonal_clock = np.diag([1] * 5 + [2 / 3] * 5 + [1 / 3] * 5)
    intertwiner_errors = {
        "J_isometry": float(np.linalg.norm(j_eigen.T.conj() @ j_eigen - np.eye(15))),
        "CJ_equals_Jdiag": float(np.linalg.norm(transfer @ j_eigen - j_eigen @ diagonal_clock)),
        "CL_equals_LM": float(
            np.linalg.norm(transfer @ l_absorbing - l_absorbing @ np.kron(m, identity5))
        ),
        "CK_equals_KB": float(
            np.linalg.norm(
                transfer @ k_symmetric
                - k_symmetric @ np.kron(clock_b, identity5)
            )
        ),
    }

    iteration_rows = []
    iteration_error = 0.0
    for depth in (1, 2, 6, 12):
        power = np.linalg.matrix_power(transfer, depth)
        expected = (
            p_w
            + (2 / 3) ** depth * (p_even - p_w)
            + (1 / 3) ** depth * p_odd
        )
        formula_error = float(np.linalg.norm(power - expected))
        readout_error = float(np.linalg.norm(w.T.conj() @ power - w.T.conj()))
        convergence_norm = float(np.linalg.norm(power - p_w, ord=2))
        iteration_error = max(iteration_error, formula_error, readout_error)
        iteration_rows.append(
            {
                "depth": depth,
                "operator_norm_to_PW": convergence_norm,
                "bound": (2 / 3) ** depth,
                "formula_residual": formula_error,
                "readout_residual": readout_error,
            }
        )

    source_error = float(
        np.linalg.norm(
            transfer @ g
            - (
                math.sqrt(2 / 3) * w
                + (2 / 3) * math.sqrt(1 / 3) * remainder
            )
        )
    )
    source_power_error = float(
        np.linalg.norm(
            np.linalg.matrix_power(transfer, 6) @ g
            - (
                math.sqrt(2 / 3) * w
                + (2 / 3) ** 6 * math.sqrt(1 / 3) * remainder
            )
        )
    )

    path_commutator = float(
        np.linalg.norm(transfer @ chain["chain"] - chain["chain"] @ transfer)
    )
    # The three identified 5-dimensional modes do not fix the independent
    # outer-antisymmetric 45.  This explicit alternative proves that the full
    # 125-dimensional uniqueness needs the additional parity-only scalarity
    # assumption used by C.
    freedom_parameter = 1 / 12
    alternative_transfer = transfer + freedom_parameter * p_45
    freedom_clock_error = float(
        np.linalg.norm(alternative_transfer @ j_eigen - transfer @ j_eigen)
    )
    freedom_path_commutator = float(
        np.linalg.norm(
            alternative_transfer @ chain["chain"]
            - chain["chain"] @ alternative_transfer
        )
    )
    charge_commutator = 0.0
    freedom_charge_commutator = 0.0
    collective_generators = []
    for generator in _su_generators():
        collective = (
            np.kron(np.kron(generator, identity5), identity5)
            - np.kron(np.kron(identity5, generator.T), identity5)
            + np.kron(np.kron(identity5, identity5), generator)
        )
        collective_generators.append(collective)
        charge_commutator = max(
            charge_commutator,
            float(np.linalg.norm(transfer @ collective - collective @ transfer)),
        )
        freedom_charge_commutator = max(
            freedom_charge_commutator,
            float(
                np.linalg.norm(
                    alternative_transfer @ collective
                    - collective @ alternative_transfer
                )
            ),
        )
    event_commutator = 0.0
    freedom_event_commutator = 0.0
    event_intertwining = 0.0
    for event in invariants["transpositions"]:
        physical_event = np.kron(np.kron(event, event), event)
        event_commutator = max(
            event_commutator,
            float(np.linalg.norm(transfer @ physical_event - physical_event @ transfer)),
        )
        freedom_event_commutator = max(
            freedom_event_commutator,
            float(
                np.linalg.norm(
                    alternative_transfer @ physical_event
                    - physical_event @ alternative_transfer
                )
            ),
        )
        event_intertwining = max(
            event_intertwining,
            float(
                np.linalg.norm(
                    physical_event @ j_eigen
                    - j_eigen @ np.kron(np.eye(3), event)
                )
            ),
        )

    # Nine-port scaling.  One coarse link is completed by 3x3 microscopic
    # pairs.  Repeating this as a literal spatial refinement is exact at every
    # finite depth, but it increases degree by three per level.
    recursion_rows = []
    for depth in range(5):
        sites_per_parent_site = 3**depth
        pair_terms_per_parent_edge = 9**depth
        degree_factor = 3**depth
        recursion_rows.append(
            {
                "depth": depth,
                "sites_per_original_site": sites_per_parent_site,
                "pair_terms_per_original_edge": pair_terms_per_parent_edge,
                "degree_factor": degree_factor,
                "fixed_coupling_incident_weight_factor": degree_factor,
                "kac_weight_per_pair": f"1/{degree_factor}",
                "time_rescaling_for_same_compressed_link": degree_factor,
            }
        )
    recursion_exact = all(
        row["pair_terms_per_original_edge"]
        == row["sites_per_original_site"] * row["degree_factor"]
        for row in recursion_rows
    )

    small_exact = small["exact"]
    checks = [
        _check(
            "Originalregel ist ein symmetrischer Überlebensoperator mit orthogonalem P0",
            bool(
                small_exact["survival_formula"]
                and small_exact["survival_is_symmetric"]
                and small_exact["survival_projector_is_orthogonal"]
            ),
            {
                "row_sums": _rational_list(small_exact["survival_row_sums"]),
                "P0_orthogonal": bool(small_exact["survival_projector_is_orthogonal"]),
            },
            {"row_sums": ["1", "2/3", "2/3"], "P0_orthogonal": True},
            "exakte SymPy-Identität M=I/2+sigma/6+P0/3",
        ),
        _check(
            "Ein echter absorbierender Markov-Abschluss hat einen schiefen PF-Projektor",
            bool(
                small_exact["markov_pf"]
                and small_exact["markov_pf_idempotent"]
                and small_exact["markov_pf_is_oblique"]
            ),
            {
                "column_sums": _rational_list(small_exact["markov_column_sums"]),
                "orthogonal": not bool(small_exact["markov_pf_is_oblique"]),
            },
            {"column_sums": ["1", "1", "1"], "orthogonal": False},
            "fehlende Überlebensmasse wird ausdrücklich in den absorbierenden Slot geleitet",
        ),
        _check(
            "Symmetrischer Cusp-Clock B ist orthogonal ähnlich zu M",
            bool(
                small_exact["basis_is_orthogonal"]
                and small_exact["symmetric_similarity"]
                and small_exact["fixed_projector_similarity"]
            ),
            True,
            True,
            "exakte Radikalbasis; P0 wird auf J3/3 abgebildet",
        ),
        _check(
            "Die Fortsetzungskoeffizienten sind eindeutig",
            len(coefficient_solutions) == 1
            and coefficients
            == {a: sp.Rational(1, 2), b: sp.Rational(1, 6), c: sp.Rational(1, 3)},
            {str(key): str(value) for key, value in coefficients.items()},
            {"a": "1/2", "b": "1/6", "c": "1/3"},
            "W-, gerade Rest- und ungerade Eigenwerte 1,2/3,1/3",
        ),
        _check(
            "W, Z und R besitzen die benötigte Außentausch-Parität",
            max(projector_errors.values()) < 5e-12,
            projector_errors,
            0,
            "direkte Wirkung des Permutationsoperators S13 auf den nativen Tensoren",
        ),
        _check(
            "C ist eine positive Kontraktion mit vollständigem 125er Spektrum",
            spectrum == {"1": 5, "2/3": 70, "1/3": 50}
            and lower_bound > 1 / 3 - 1e-12
            and upper_bound < 1 + 1e-12,
            {"multiplicities": spectrum, "bounds": [lower_bound, upper_bound]},
            {"multiplicities": {"1": 5, "2/3": 70, "1/3": 50}, "bounds": [1 / 3, 1]},
            "Spektralzerlegung W5 + (Symmetrisch75-W5)70 + Antisymmetrisch50",
        ),
        _check(
            "Die 15D-Uhr lässt auf dem unberührten 45er eine Fortsetzungsfreiheit",
            p_45_rank == 45
            and freedom_clock_error < 5e-12
            and max(
                freedom_path_commutator,
                freedom_charge_commutator,
                freedom_event_commutator,
            )
            < 2e-11
            and np.linalg.eigvalsh(alternative_transfer)[0] > 0,
            {
                "P45_rank": p_45_rank,
                "eta": freedom_parameter,
                "clock_residual": freedom_clock_error,
                "path_commutator": freedom_path_commutator,
                "charge_commutator": freedom_charge_commutator,
                "event_commutator": freedom_event_commutator,
            },
            "C_eta=C+eta(Pminus-PZ) remains positive and compatible",
            "explicit counterfamily; full uniqueness requires parity-only scalarity",
        ),
        _check(
            "Typisierte Intertwiner reproduzieren M und den symmetrischen B-Clock",
            max(intertwiner_errors.values()) < 5e-12,
            intertwiner_errors,
            0,
            "L†L=K†K=I15, CL=L(M tensor I5), CK=K(B tensor I5)",
        ),
        _check(
            "Iteration konvergiert exakt auf den W-Träger und erhält den W†-Readout",
            iteration_error < 5e-12
            and all(
                abs(row["operator_norm_to_PW"] - row["bound"]) < 5e-12
                for row in iteration_rows
            ),
            {"maximum_residual": iteration_error, "rows": iteration_rows},
            "||C^n-PW||=(2/3)^n und W†C^n=W†",
            "orthogonale Spektralprojektoren von C",
        ),
        _check(
            "Der vorhandene Quellencoder liegt in Fix- plus Recovery-Sektor",
            max(source_error, source_power_error) < 5e-12,
            {"one_step": source_error, "six_steps": source_power_error},
            0,
            "G=sqrt(2/3)W+sqrt(1/3)R mit S13 R=R",
        ),
        _check(
            "Clock, Pfad, kollektive Ladung und native Ereignisse sind kompatibel",
            max(path_commutator, charge_commutator, event_commutator, event_intertwining)
            < 2e-11,
            {
                "path_commutator": path_commutator,
                "charge_commutator": charge_commutator,
                "event_commutator": event_commutator,
                "event_intertwining": event_intertwining,
            },
            0,
            "[C,Hpath]=[C,Qa]=[C,Tm^tensor3]=0; Ereignisse wirken als I3 tensor Tm",
        ),
        _check(
            "Wiederholte Neun-Port-Ersetzung ist endlich exakt, aber nicht gradbeschränkt",
            recursion_exact,
            recursion_rows,
            "N~3^n, E~9^n, Grad~3^n",
            "kombinatorische 3x3-Portrekursion; Kac-Skalierung 3^-n erfordert Zeitskalierung 3^n",
        ),
    ]

    return {
        "id": "origin_transfer",
        "title": "Originale Double-Cover-Uhr auf dem nativen Trimer",
        "status": "exact_minimal_continuation_under_three_typed_identifications",
        "checks": checks,
        "data": {
            "original_rule": {
                "survival_operator": [[str(value) for value in row] for row in small["survival"].tolist()],
                "formula": "M=(1/2)I+(1/6)sigma+(1/3)P0",
                "spectrum": ["1", "2/3", "1/3"],
                "row_sums": _rational_list(small_exact["survival_row_sums"]),
                "classification": "symmetric sub-Markov survival operator",
                "absorbing_markov_completion": {
                    "matrix": [
                        [str(value) for value in row]
                        for row in small["absorbing_markov"].tolist()
                    ],
                    "pf_projector": [
                        [str(value) for value in row]
                        for row in small["oblique_pf"].tolist()
                    ],
                    "scope": "distinct trace-preserving population completion; not the symmetric survival operator used below",
                },
                "symmetric_cusp_clock": [
                    [str(value) for value in row]
                    for row in small["symmetric_clock"].tolist()
                ],
                "basis_warning": (
                    "the orthogonal similarity preserves the Hilbert-space operator and spectrum, "
                    "but not the native positive population cone"
                ),
            },
            "typed_identification": {
                "z2_pair_swap": "sigma -> S13, exchange of the two outer U factors in U tensor Ubar tensor U",
                "absorbing_slot": "P0 -> PW=WW†, rank five",
                "assumptions": [
                    "the internal family/survival Z2 pair-swap is represented by the physical outer-leg exchange S13",
                    "the original fixed-law slot is represented by the covariant W code subspace",
                    "after removing W, the one-step survival rate depends only on outer-swap parity, with no separate 45-sector rate",
                ],
                "selection_status": (
                    "the third item is a new 125-dimensional continuation assumption. "
                    "The complete ladder in v487 quantifies only the three-dimensional family/cusp seed; "
                    "it neither selects nor reopens the already closed three-dimensional rule on the larger tensor space"
                ),
                "scope": (
                    "these are the three extra identifications; the tensor parities and all subsequent identities are computed. "
                    "The source calls the sigma eigenmodes even/odd deck parity, but does not identify sigma with the P1 sheet deck, v101 horizon swap, or trimer S13. "
                    "The frozen marked A3 cover does not settle the issue: simultaneous leaf swaps preserve its strong-edge trimers, but not its fixed full quotient-edge data"
                ),
                "missing_geometric_bridge": (
                    "construct an explicit D_deck on trimer states together with the connection/marking data, "
                    "then prove D_deck restricts locally to S13 and D_deck W=W"
                ),
            },
            "continuation": {
                "formula": "C=(1/2)I125+(1/6)S13+(1/3)PW",
                "unique_coefficients": {str(key): str(value) for key, value in coefficients.items()},
                "uniqueness_scope": "unique only in span{I,S13,PW}, equivalently under parity-only scalarity",
                "bounds": "(1/3)I <= C <= I",
                "spectrum": [
                    {"value": "1", "multiplicity": 5, "sector": "W"},
                    {
                        "value": "2/3",
                        "multiplicity": 70,
                        "sector": "outer-symmetric complement of W",
                    },
                    {
                        "value": "1/3",
                        "multiplicity": 50,
                        "sector": "outer-antisymmetric Z5 direct-sum 45",
                    },
                ],
                "six_step_spectrum": [
                    {"value": "1", "multiplicity": 5},
                    {"value": "64/729", "multiplicity": 70},
                    {"value": "1/729", "multiplicity": 50},
                ],
                "os_generator": (
                    "-6 log C has gaps 0, 6 log(3/2), 6 log(3); "
                    "it is the discrete seam-transfer generator, not H_path"
                ),
                "tensor_nature": (
                    "S13 is a factor permutation and PW is the covariant trimer-code projector; "
                    "C is defined on the full 5x5x5 tensor space"
                ),
            },
            "intertwiners": {
                "absorbing_coordinates": "CL=L(M tensor I5)",
                "symmetric_cusp_coordinates": "CK=K(B tensor I5)",
                "eigen_coordinates": "CJ=J diag(I5,(2/3)I5,(1/3)I5)",
                "residuals": intertwiner_errors,
                "typing": (
                    "L and K are Hilbert-space isometries; neither is by itself a stochastic coarse-graining map"
                ),
            },
            "iteration": {
                "identity": "C^n=PW+(2/3)^n(Pplus-PW)+(1/3)^n Pminus",
                "limit": "C^n -> PW in operator norm",
                "readout": "W†C^n=W†",
                "error_bound": "||C^n psi-PW psi|| <= (2/3)^n ||(I-PW)psi||",
                "rows": iteration_rows,
                "source": {
                    "identity": "C^n G=sqrt(2/3)W+(2/3)^n sqrt(1/3)R",
                    "meaning": "the native quartic source occupies only fixed and dominant recovery sectors",
                },
            },
            "joint_process_compatibility": {
                "path": "[C,H_path]=0, while C is not exp(-t(H_path-E0))",
                "charge": "[C,Q(X)]=0 for all 24 tested su(5) generators",
                "events": "rho(T_m)J=J(I3 tensor T_m), so all 15 native events preserve the three clock sectors",
                "nine_port": (
                    "a completed link is scalar plus (1/6) sum_a Q_A^a Q_B^a; "
                    "therefore it commutes with C on each incident block"
                ),
                "finite_graph": (
                    "clock layers, native-event layers and completed-link layers preserve the common carrier on every finite graph"
                ),
                "residuals": {
                    "path": path_commutator,
                    "charge": charge_commutator,
                    "events": event_commutator,
                },
            },
            "block_recursion": {
                "rows": recursion_rows,
                "verdict": (
                    "the nine-port replacement is an exact finite block isometry, but literal repetition is hierarchical/dense rather than bounded-degree local"
                ),
                "fixed_coupling": "logical link strength stays fixed while microscopic incident strength grows by 3 per level",
                "kac_option": (
                    "weight each microscopic pair by 1/3 per level to keep incident strength bounded; "
                    "the same logical evolution then needs a factor-3 time rescaling per level"
                ),
            },
            "e8_scale_grammar": {
                "carrier_counts": {
                    "D_start": "5*12=60",
                    "Omega_admissible": 48,
                    "E8_roots": "lcm(48,60)=240",
                },
                "exponent": "kappa_E=(5/6)/log(248/60)",
                "readout": (
                    "X(n,r,I1)=(Mbar/8) sin^2(theta13) "
                    "((60-2n)/60)^kappa_E exp(-(8-r)/64) exp(-12*pi*I1)"
                ),
                "typing": (
                    "this is the original downstream scale grammar. The W nine-port replacement "
                    "maps n to 3n combinatorially and preserves the compressed coupling J, but "
                    "does not by itself identify its depth, link count, or time rescaling with "
                    "the variables n, r, or I1 in X"
                ),
                "required_bridge": (
                    "a typed map from nine-port refinement depth and event data to (n,r,I1), "
                    "compatible with D_start=60 and Omega=48; no such map is derived here"
                ),
            },
            "scope": {
                "proved": (
                    "given the three typed identifications, the original lazy-rule coefficients have a unique positive continuation in span{I,S13,PW}, compatible with path, charge and native events"
                ),
                "not_proved": [
                    "that the internal family/survival pair-swap, P1 sheet deck, v101 horizon swap and outer-leg exchange S13 are the same typed operation",
                    "that the outer-antisymmetric 45 must share the Z-sector rate; C_eta=C+eta(Pminus-PZ), -1/3<=eta<=2/3, is a compatible positive counterfamily",
                    "that the amplitude contraction C is the uniquely selected CPTP instrument or spatial RG map",
                    "that literal nine-port iteration is a uniform finite-range continuum dynamics",
                    "a typed identification of nine-port refinement depth with the downstream E8 scale variables (n,r,I1)",
                    "selection of a state inside the rank-five W fixed sector",
                    "primitive future-distinguishability or a lossless causal quotient for arbitrary states",
                ],
                "cptp_boundary": (
                    "rho -> C rho C is completely positive but trace-decreasing; its sector survival "
                    "probabilities are 1,4/9,1/9, the squares of the amplitude eigenvalues, and therefore "
                    "are not automatically the original Markov population rates 1,2/3,1/3. A "
                    "trace-preserving completion needs additional Kraus data and is not selected here"
                ),
                "readout_boundary": (
                    "W† is an isometric inverse only on the W code. C^n removes generic even/odd "
                    "complement data as n grows, so convergence to PW is a cooling/survival filter, "
                    "not a lossless coarse graining of every input history"
                ),
                "process_boundary": (
                    "the primitive/future-closed full history process still requires a selected "
                    "instrument, record rule and state; it does not follow from this filter"
                ),
            },
            "sources": [
                {
                    "path": "origin_theory.tex",
                    "lines": "284-313",
                    "claim": "unique lazy double-cover rule, full clock spectrum and parity-to-rung assignment",
                },
                {
                    "path": "origin_theory.tex",
                    "lines": "315-324",
                    "claim": "original T_net tensor M coupled rewrite and E8 growth with attached fibre",
                },
                {
                    "path": "verification/v486_transfer_full_rule.py",
                    "lines": "68-123",
                    "claim": "exact survival matrix and its sub-stochastic classification",
                },
                {
                    "path": "verification/v487_transfer_clock_rungs.py",
                    "lines": "92-121",
                    "claim": "even recovery and odd subdominant deck-rung assignment",
                },
                {
                    "path": "verification/v160_seam_gaussianity_from_pf.py",
                    "lines": "16, 65-68, 248-263",
                    "claim": "the former PF uniqueness is only on the three-dimensional scalar transfer spectrum, not a larger cone",
                },
                {
                    "path": "verification/v161_one_particle_reduction.py",
                    "lines": "9-28, 165-172",
                    "claim": "the full cone is governed by a separate one-particle symbol and its exterior powers",
                },
                {
                    "path": "verification/v175_net_existence_full_cone.py",
                    "lines": "11-21, 103-107",
                    "claim": "Gamma(t) contains all subset-product eigenvalues; only contraction, fixed sector and the gap lift automatically",
                },
                {
                    "path": "verification/v814_k5_sixstep_transport.py",
                    "lines": "288-313",
                    "claim": "symmetric cusp B and its fixed eigenbasis",
                },
                {
                    "path": "tfpt_explorer/composition.py",
                    "lines": "359-448, 655-712, 721-744",
                    "claim": "W/R source split, outer-symmetric 70 orbit and completed-link covariance",
                },
                {
                    "path": "tfpt_1_architecture_e8.tex",
                    "lines": "4315-4325",
                    "claim": "E8 as downstream scale grammar with D_start=60, Omega=48, root count 240 and X(n,r,I1)",
                },
            ],
        },
    }
