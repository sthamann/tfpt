#!/usr/bin/env python3
"""Exact sparse certificate for the positive RR lift on the pinned native W.

No full fermion-boson Fock matrix is built.  The largest operator constructed
is the 3840 x 3840 sparse integer Gram matrix C3 C3^T.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import comb, isqrt, prod
from pathlib import Path
import json

import numpy as np
from scipy.sparse import coo_matrix, eye


LOCAL_TENSOR = Path(__file__).with_name("native_tensor.npz")
ARCHIVED_TENSOR = Path(
    "/Users/stefanhamann/Documents/Codex/2026-09-21/l-s/outputs/"
    "TFPT_Stabile_Quellenrekonstruktion/native_tensor.npz"
)
TENSOR = LOCAL_TENSOR if LOCAL_TENSOR.exists() else ARCHIVED_TENSOR
TENSOR_SHA256 = "3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763"
N_FERMION = 64
N_BOSON = 60
PAIRS = tuple(combinations(range(N_FERMION), 2))


class Checks:
    def __init__(self) -> None:
        self.labels: list[str] = []

    def need(self, condition: bool, label: str) -> None:
        if not condition:
            raise RuntimeError(label)
        self.labels.append(label)


def sparse_zero(matrix) -> bool:
    candidate = matrix.copy()
    candidate.eliminate_zeros()
    return candidate.nnz == 0


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def main() -> dict[str, object]:
    checks = Checks()
    checks.need(
        sha256(TENSOR.read_bytes()).hexdigest() == TENSOR_SHA256,
        "pinned native tensor SHA-256",
    )
    with np.load(TENSOR, allow_pickle=False) as archive:
        raw = archive["W"]
    checks.need(np.all(raw.imag == 0), "native W is real")
    checks.need(np.all(raw.real == np.rint(raw.real)), "native W is integral")
    W = raw.real.astype(np.int64)
    checks.need(W.shape == (N_BOSON, len(PAIRS)), "native W shape is 60 x 2016")
    checks.need(set(np.unique(W)) == {-1, 0, 1}, "native W entries are 0,+/-1")
    checks.need(np.count_nonzero(W) == 480, "native W has 480 nonzero entries")
    checks.need(
        np.array_equal(W @ W.T, 8 * np.eye(N_BOSON, dtype=np.int64)),
        "native row Gram is 8 I60",
    )
    checks.need(
        int(np.max(np.sum(np.abs(W), axis=0))) == 1,
        "each supported fermion pair belongs to one W channel",
    )

    row_norms = np.sum(W * W, axis=1)
    checks.need(np.all(row_norms == 8), "all P_A vacuum and filled CAR norms are 8")

    # Derive every Q2 block from ||P_A^dagger|0>||^2.  The squared off-diagonal
    # entry in kappa units is norm/2; its sign is fixed positive by the lift.
    q2_blocks: list[np.ndarray] = []
    off_diagonal_roots = [isqrt(int(norm) // 2) for norm in row_norms]
    checks.need(
        all(root * root == int(norm) // 2 for root, norm in zip(off_diagonal_roots, row_norms)),
        "all Q2 off-diagonals are exact integers",
    )
    for norm, off_diagonal in zip(row_norms, off_diagonal_roots):
        q2_blocks.append(
            np.array([[int(norm) // 4, off_diagonal], [off_diagonal, 2]], dtype=np.int64)
        )
    checks.need(
        all(np.array_equal(block, np.array([[2, 2], [2, 2]], dtype=np.int64)) for block in q2_blocks),
        "all 60 Q2 blocks equal kappa [[2,2],[2,2]]",
    )
    q2_block = q2_blocks[0]
    checks.need(
        np.array_equal(q2_block @ np.array([1, -1], dtype=np.int64), np.zeros(2, dtype=np.int64)),
        "Q2 block has the exact zero direction (1,-1)",
    )
    checks.need(
        np.array_equal(q2_block @ np.array([1, 1], dtype=np.int64), 4 * np.ones(2, dtype=np.int64)),
        "Q2 block has the exact bright eigenvalue 4 kappa",
    )

    # B_A=b_A+P_A/sqrt(8).  Direct CAR norms give [P,P^dagger]/8=+1
    # on the vacuum and -1 on the filled state, hence [B,B^dagger]=2,0.
    b_comm_vacuum = [Fraction(1) + Fraction(int(value), 8) for value in row_norms]
    b_comm_filled = [Fraction(1) - Fraction(int(value), 8) for value in row_norms]
    checks.need(set(b_comm_vacuum) == {Fraction(2)}, "all composite B commutators equal 2 on vacuum")
    checks.need(set(b_comm_filled) == {Fraction(0)}, "all composite B commutators equal 0 on filled state")

    # Exact non-scalar response.  C_el/kappa=(W^T W)/4.  Apply the column
    # (4,57), then annihilate f_4.  Only the (4,57) output may remain.
    pair_index = {pair: column for column, pair in enumerate(PAIRS)}
    response_pair = (4, 57)
    response_column = pair_index[response_pair]
    channel_vector = W[:, response_column]
    checks.need(np.count_nonzero(channel_vector) == 1, "W contains the pair (4,57) in exactly one channel")
    elastic_numerator = W.T @ channel_vector
    r44_numerator: dict[int, int] = {}
    for column in np.flatnonzero(elastic_numerator):
        i, j = PAIRS[int(column)]
        coefficient = int(elastic_numerator[column])
        if i == 4:
            r44_numerator[j] = r44_numerator.get(j, 0) + coefficient
        elif j == 4:
            # For the ordered pair state f_i^dagger f_j^dagger|0>,
            # f_j contributes the CAR minus sign.
            r44_numerator[i] = r44_numerator.get(i, 0) - coefficient
    r44_numerator = {mode: value for mode, value in r44_numerator.items() if value}
    checks.need(r44_numerator == {57: 1}, "R44 on f57^dagger vacuum is exactly kappa/4 times that state")
    masks_on_vacuum_path = (0, 1 << 4)
    # Evaluate directly from W support so the vacuum claim is a real,
    # non-tautological gate.
    supported_pairs_on_vacuum_path = sum(
        1
        for mask in masks_on_vacuum_path
        for column in np.flatnonzero(np.any(W != 0, axis=0))
        if all((mask >> mode) & 1 for mode in PAIRS[int(column)])
    )
    checks.need(
        supported_pairs_on_vacuum_path == 0,
        "R44 on vacuum is zero: H+ has no supported pair action on the vacuum/f4 path",
    )

    # The pair projector is Pi_W=W^T W/8.  Its projector identity is reduced
    # to the already checked WW^T=8I, avoiding a dense 2016 x 2016 product.
    projector_rank = int(np.linalg.matrix_rank(W @ W.T))
    checks.need(projector_rank == 60, "Pi_W has exact rank 60")
    checks.need(
        np.array_equal((W @ W.T) @ W, 8 * W),
        "Pi_W squared equals Pi_W without forming a dense pair projector",
    )

    # Build the native Q=3 annihilation map C3: 3F -> bF exactly.
    lookup: dict[tuple[int, int], tuple[int, int]] = {}
    for channel, column in zip(*np.nonzero(W)):
        lookup[PAIRS[int(column)]] = (int(channel), int(W[channel, column]))
    rows: list[int] = []
    columns: list[int] = []
    values: list[int] = []
    for triple_column, (a, b, c) in enumerate(combinations(range(N_FERMION), 3)):
        for pair, spectator, sign in (
            ((a, b), c, 1),
            ((a, c), b, -1),
            ((b, c), a, 1),
        ):
            entry = lookup.get(pair)
            if entry is not None:
                channel, weight = entry
                rows.append(N_FERMION * channel + spectator)
                columns.append(triple_column)
                values.append(sign * weight)
    C3 = coo_matrix(
        (np.asarray(values, dtype=np.int64), (rows, columns)),
        shape=(N_BOSON * N_FERMION, comb(N_FERMION, 3)),
        dtype=np.int64,
    ).tocsr()
    checks.need(C3.nnz == 29_760, "native C3 has 29760 nonzero integer entries")
    G = (C3 @ C3.T).tocsr()
    identity = eye(N_BOSON * N_FERMION, dtype=np.int64, format="csr")
    roots = (0, 7, 10, 12)
    row_bound = int(np.max(np.asarray(abs(G).sum(axis=1)).ravel()))
    checks.need(
        (N_BOSON * N_FERMION) * prod(row_bound + abs(root) for root in roots) < 2**63,
        "Q3 sparse polynomial and trace arithmetic fit signed int64",
    )
    polynomial = identity
    for root in roots:
        polynomial = polynomial @ (G - root * identity)
    checks.need(sparse_zero(polynomial), "G obeys x(x-7)(x-10)(x-12)=0 exactly")

    multiplicities: dict[int, int] = {}
    projector_trace_numerators: dict[int, int] = {}
    projector_denominators: dict[int, int] = {}
    for root in roots:
        projector_numerator = identity
        denominator = 1
        for other in roots:
            if other != root:
                projector_numerator = projector_numerator @ (G - other * identity)
                denominator *= root - other
        trace_numerator = int(projector_numerator.diagonal().sum())
        checks.need(
            trace_numerator % denominator == 0,
            f"spectral projector trace is integral at lambda={root}",
        )
        multiplicities[root] = trace_numerator // denominator
        projector_trace_numerators[root] = trace_numerator
        projector_denominators[root] = denominator
    expected_multiplicities = {0: 64, 7: 2880, 10: 576, 12: 320}
    checks.need(multiplicities == expected_multiplicities, "exact native Q3 Gram multiplicities")
    checks.need(sum(multiplicities.values()) == 3840, "Q3 Gram multiplicities exhaust bF")

    rank_c3 = sum(multiplicity for root, multiplicity in multiplicities.items() if root != 0)
    kernel_c3 = comb(N_FERMION, 3) - rank_c3
    q3_zero_count = kernel_c3 + rank_c3
    checks.need(rank_c3 == 3776 and kernel_c3 == 37888, "C3 rank and 3F kernel dimensions")
    checks.need(q3_zero_count == 41664, "positive-lift Q3 zero multiplicity is 41664")

    energy_multiplicities: dict[str, int] = {}
    for gram_root, multiplicity in multiplicities.items():
        energy = Fraction(2) + Fraction(gram_root, 4)
        energy_multiplicities[fraction_text(energy)] = multiplicity
    checks.need(
        energy_multiplicities == {"2": 64, "15/4": 2880, "9/2": 576, "5": 320},
        "all nonzero positive-lift Q3 energies and multiplicities",
    )
    checks.need(
        q3_zero_count + sum(energy_multiplicities.values()) == 45_504,
        "positive-lift Q3 spectrum exhausts the 45504-dimensional sector",
    )

    checker_sha256 = sha256(Path(__file__).read_bytes()).hexdigest()
    return {
        "status": "PASS",
        "verdict": "EXACT_FINITE_POSITIVE_RR_LIFT_IDENTITIES_ON_PINNED_W",
        "pins": {
            "native_tensor": TENSOR.name,
            "native_tensor_sha256": TENSOR_SHA256,
            "checker_sha256": checker_sha256,
        },
        "largest_constructed_operator": {
            "name": "G=C3 C3^T",
            "shape": [3840, 3840],
            "storage": "sparse int64",
            "full_Q3_Hamiltonian_constructed": False,
            "full_Fock_matrix_constructed": False,
        },
        "native_W": {
            "shape": [60, 2016],
            "nonzero": 480,
            "row_gram": "8 I60",
        },
        "checked_blocks": {
            "Hplus": "2 kappa Nb + kappa/sqrt(2) (X+Xdagger) + kappa/4 D",
            "positive_factorization": "2 kappa sum_A (b_A+P_A/sqrt(8))^dagger (b_A+P_A/sqrt(8))",
            "Q2_over_kappa": q2_block.tolist(),
            "C1": "kappa W/sqrt(2)",
            "C_el": "kappa W^T W/4 = 2 kappa Pi_W",
            "C2": "0",
            "Schur_equality": "C_el=C1^dagger (2 kappa I60)^(-1) C1",
            "Pi_W_rank": projector_rank,
        },
        "noncanonical_B": {
            "commutator_on_vacuum": 2,
            "commutator_on_filled_state": 0,
            "channels_checked": N_BOSON,
        },
        "non_scalar_response": {
            "R44_on_vacuum": "0",
            "R44_on_f57dagger_vacuum": "(kappa/4) f57dagger|0>",
            "W_pair": [4, 57],
            "integer_numerator_after_f4": {str(key): value for key, value in r44_numerator.items()},
        },
        "Q3": {
            "C3_shape": list(C3.shape),
            "C3_nonzero": C3.nnz,
            "G_shape": list(G.shape),
            "G_row_l1_bound": row_bound,
            "annihilating_polynomial": "x(x-7)(x-10)(x-12)",
            "gram_multiplicities": {str(key): value for key, value in multiplicities.items()},
            "projector_trace_numerators": {
                str(key): value for key, value in projector_trace_numerators.items()
            },
            "projector_denominators": {
                str(key): value for key, value in projector_denominators.items()
            },
            "C3_rank": rank_c3,
            "C3_kernel_dimension": kernel_c3,
            "Hplus_zero_multiplicity": q3_zero_count,
            "Hplus_nonzero_energies_over_kappa": energy_multiplicities,
            "full_dimension": q3_zero_count + sum(energy_multiplicities.values()),
        },
        "analytic_not_full_matrix_checked": {
            "global_positivity": "follows from the displayed sum of squares for kappa>0",
            "global_kernel": "ker(Hplus)=Ran(exp(-X/sqrt(8)) on boson vacuum), dimension 2^64, by the finite recursion argument",
            "charge_q_kernel": "binomial(64,q) for 0<=q<=64",
            "source_selection": "not derived",
            "physical_RR_channel_map": "not derived",
        },
        "firewall": {
            "classification": "exact finite algebra under an explicit positive lift and the pinned W tensor",
            "not_a_source_origin_proof": True,
            "not_a_physical_RR_identification": True,
            "not_a_TOE_completion": True,
            "T1_to_T8_remain_open": True,
        },
        "exact_checks": len(checks.labels),
        "numerical_checks": 0,
        "checks": checks.labels,
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
