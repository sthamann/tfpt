#!/usr/bin/env python3
"""Exact checks for the finite CAR/CCR mixed-response reconstruction result.

The finite rank calculation uses integer operator matrices for CAR(4), exact
normal-order multiplication for one CCR mode, and sparse Gaussian elimination
modulo a prime.  A rank-325 minor modulo a prime is an exact certificate that
the integer response matrix has rational rank at least 325; the identity
column is identically zero, so its rank is exactly 325.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np


NATIVE_TENSOR = Path(
    "/Users/stefanhamann/Documents/Codex/2026-09-21/l-s/outputs/"
    "TFPT_RR_Quellenbruecke/native_tensor.npz"
)
EXPECTED_SHA256 = "3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763"
PRIME = 2_147_483_647


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def car_generators(nf: int) -> tuple[list[np.ndarray], list[np.ndarray]]:
    """Return annihilation and creation matrices in the occupation basis."""
    dim = 1 << nf
    annihilators: list[np.ndarray] = []
    creators: list[np.ndarray] = []
    for i in range(nf):
        f = np.zeros((dim, dim), dtype=np.int64)
        bit = 1 << i
        lower = bit - 1
        for state in range(dim):
            if state & bit:
                sign = -1 if ((state & lower).bit_count() & 1) else 1
                f[state ^ bit, state] = sign
        annihilators.append(f)
        creators.append(f.T.copy())
    return annihilators, creators


def fermion_monomial(
    creators: list[np.ndarray], annihilators: list[np.ndarray], imask: int, jmask: int
) -> np.ndarray:
    """f^dagger_I f_J with creators ascending and annihilators descending."""
    out = np.eye(creators[0].shape[0], dtype=np.int64)
    for i in range(len(creators)):
        if imask & (1 << i):
            out = out @ creators[i]
    for j in reversed(range(len(annihilators))):
        if jmask & (1 << j):
            out = out @ annihilators[j]
    return out


# An operator is {(number of b^dagger, number of b): CAR matrix}.
Operator = dict[tuple[int, int], np.ndarray]


def op_add(left: Operator, right: Operator, scale: int = 1) -> Operator:
    out = {key: value.copy() for key, value in left.items()}
    for key, value in right.items():
        if key in out:
            out[key] = out[key] + scale * value
            if not np.any(out[key]):
                del out[key]
        elif scale:
            candidate = scale * value
            if np.any(candidate):
                out[key] = candidate
    return out


def op_mul(left: Operator, right: Operator) -> Operator:
    """Multiply using b^c (b^dagger)^d normal ordering, exactly over Z."""
    out: Operator = {}
    for (a, c), lmat in left.items():
        for (d, e), rmat in right.items():
            matrix = lmat @ rmat
            if not np.any(matrix):
                continue
            for k in range(min(c, d) + 1):
                coefficient = math.comb(c, k) * math.factorial(d) // math.factorial(d - k)
                key = (a + d - k, c + e - k)
                term = coefficient * matrix
                out[key] = out.get(key, np.zeros_like(term)) + term
                if not np.any(out[key]):
                    del out[key]
    return out


def comm(left: Operator, right: Operator) -> Operator:
    return op_add(op_mul(left, right), op_mul(right, left), scale=-1)


def anti(left: Operator, right: Operator) -> Operator:
    return op_add(op_mul(left, right), op_mul(right, left), scale=1)


def singleton(matrix: np.ndarray, a: int = 0, c: int = 0) -> Operator:
    return {(a, c): matrix}


def enumerate_neutral_monomials(nf: int, max_degree: int) -> list[tuple[int, int, int, int]]:
    monomials = []
    for a in range(max_degree + 1):
        for c in range(max_degree + 1):
            for imask in range(1 << nf):
                ni = imask.bit_count()
                for jmask in range(1 << nf):
                    nj = jmask.bit_count()
                    degree = a + c + ni + nj
                    charge = ni - nj + 2 * (a - c)
                    if degree <= max_degree and charge == 0:
                        monomials.append((a, c, imask, jmask))
    return monomials


def append_output(
    vector: dict[tuple[int, ...], int], prefix: tuple[int, ...], operator: Operator
) -> None:
    for (a, c), matrix in operator.items():
        rows, cols = np.nonzero(matrix)
        for row, col in zip(rows.tolist(), cols.tolist()):
            value = int(matrix[row, col])
            key = prefix + (a, c, row, col)
            vector[key] = vector.get(key, 0) + value
            if vector[key] == 0:
                del vector[key]


def response_columns(
    nf: int, monomials: list[tuple[int, int, int, int]]
) -> list[dict[tuple[int, ...], int]]:
    annihilators, creators = car_generators(nf)
    identity = np.eye(1 << nf, dtype=np.int64)
    b = singleton(identity, c=1)
    bdag = singleton(identity, a=1)
    fs = [singleton(matrix) for matrix in annihilators]
    fds = [singleton(matrix) for matrix in creators]

    columns: list[dict[tuple[int, ...], int]] = []
    for a, c, imask, jmask in monomials:
        h = singleton(fermion_monomial(creators, annihilators, imask, jmask), a=a, c=c)
        vector: dict[tuple[int, ...], int] = {}

        # R^f_ij = { [f_i,H], f_j^dagger }.
        for i in range(nf):
            first = comm(fs[i], h)
            for j in range(nf):
                append_output(vector, (0, i, j), anti(first, fds[j]))

        # R^b = [[b,H],b^dagger].
        bh = comm(b, h)
        append_output(vector, (1,), comm(bh, bdag))

        # Gamma_ij and its adjoint response.  The latter is necessary before
        # imposing self-adjointness on coefficient vectors.
        for i in range(nf):
            middle = comm(bh, fds[i])
            middle_adj = comm(comm(bdag, h), fs[i])
            for j in range(nf):
                append_output(vector, (2, i, j), anti(middle, fds[j]))
                append_output(vector, (3, i, j), anti(middle_adj, fs[j]))
        columns.append(vector)
    return columns


def sparse_rank_mod_prime(
    columns: list[dict[tuple[int, ...], int]], prime: int
) -> tuple[int, list[int], str]:
    pivots: dict[tuple[int, ...], dict[tuple[int, ...], int]] = {}
    pivot_columns: list[int] = []
    digest = hashlib.sha256()
    for column_index, raw in enumerate(columns):
        vector = {row: value % prime for row, value in raw.items() if value % prime}
        while vector:
            row = min(vector)
            if row not in pivots:
                inverse = pow(vector[row], prime - 2, prime)
                vector = {key: (value * inverse) % prime for key, value in vector.items()}
                pivots[row] = vector
                pivot_columns.append(column_index)
                digest.update(repr((column_index, row, sorted(vector.items()))).encode("ascii"))
                break
            factor = vector[row]
            pivot = pivots[row]
            for key, value in pivot.items():
                updated = (vector.get(key, 0) - factor * value) % prime
                if updated:
                    vector[key] = updated
                else:
                    vector.pop(key, None)
    return len(pivots), pivot_columns, digest.hexdigest()


def finite_rank_check() -> dict[str, object]:
    nf = 4
    max_degree = 8
    monomials = enumerate_neutral_monomials(nf, max_degree)
    degree_counts: dict[str, int] = {}
    for a, c, imask, jmask in monomials:
        degree = a + c + imask.bit_count() + jmask.bit_count()
        degree_counts[str(degree)] = degree_counts.get(str(degree), 0) + 1
    require(len(monomials) == 326, f"expected 326 monomials, got {len(monomials)}")
    require(monomials[0] == (0, 0, 0, 0), "identity is not the first monomial")

    columns = response_columns(nf, monomials)
    require(columns[0] == {}, "identity must lie in the response kernel")
    rank, pivot_columns, pivot_digest = sparse_rank_mod_prime(columns, PRIME)
    require(rank == 325, f"expected modular rank 325, got {rank}")
    require(0 not in pivot_columns, "identity unexpectedly chosen as a pivot")
    return {
        "degree_counts": dict(sorted(degree_counts.items(), key=lambda item: int(item[0]))),
        "kernel": "span{identity}",
        "max_total_degree": max_degree,
        "modes": {"boson": 1, "fermion": nf},
        "monomial_count": len(monomials),
        "pivot_certificate_sha256": pivot_digest,
        "prime": PRIME,
        "rank_mod_prime": rank,
    }


def native_tensor_check() -> dict[str, object]:
    payload = NATIVE_TENSOR.read_bytes()
    sha256 = hashlib.sha256(payload).hexdigest()
    require(sha256 == EXPECTED_SHA256, f"native tensor SHA-256 mismatch: {sha256}")
    archive = np.load(NATIVE_TENSOR, allow_pickle=False)
    w = archive["W"]
    require(w.shape == (60, 2016), f"unexpected W shape {w.shape}")
    require(np.all(np.isin(w, (-1, 0, 1))), "W is not exactly {-1,0,1}-valued")
    require(int(np.count_nonzero(w)) == 480, "W must have exactly 480 nonzero entries")
    gram = w @ w.conj().T
    require(np.array_equal(gram, 8 * np.eye(60)), "W W* is not exactly 8 I_60")

    pairs = list(itertools.combinations(range(64), 2))
    require(len(pairs) == 2016, "pair-column count mismatch")

    # Independent 4-mode CAR-matrix ward for the sign used below.
    small_f, small_fd = car_generators(4)
    sign_cases = 0
    for i, j in itertools.combinations(range(4), 2):
        pair_operator = small_f[j] @ small_f[i]
        for k in range(4):
            left = pair_operator @ small_fd[k] - small_fd[k] @ pair_operator
            right = np.zeros_like(left)
            if k == i:
                right += small_f[j]
            if k == j:
                right -= small_f[i]
            require(np.array_equal(left, right), f"CAR sign ward failed at {(i, j, k)}")
            sign_cases += 1

    # Directly assemble [P_A,f_k^dagger] from
    # [f_j f_i,f_k^dagger] = delta_ik f_j - delta_jk f_i,
    # then apply {f_l,f_m^dagger}=delta_lm to all ordered components.
    gamma = np.zeros((60, 64, 64), dtype=np.complex128)
    for column, (i, j) in enumerate(pairs):
        coefficients = w[:, column]
        gamma[:, i, j] += coefficients
        gamma[:, j, i] -= coefficients
    require(np.all(gamma + np.swapaxes(gamma, 1, 2) == 0), "Gamma is not antisymmetric")
    require(int(np.count_nonzero(gamma)) == 960, "ordered Gamma support must have 960 entries")

    upper = np.stack([gamma[:, i, j] for i, j in pairs], axis=1)
    require(np.array_equal(upper, w), "Gamma upper triangle does not reproduce W")
    projected_g = np.vdot(w, upper) / np.vdot(w, w)
    require(projected_g == 1, "unit-coupling projection did not return g=1")
    require(np.vdot(w, w) == 480, "native W norm-square must be 480")
    return {
        "Gamma_components_checked": int(gamma.size),
        "Gamma_nonzero_ordered": int(np.count_nonzero(gamma)),
        "CAR_pair_sign_cases": sign_cases,
        "W_nonzero_upper": int(np.count_nonzero(w)),
        "W_norm_squared": int(np.vdot(w, w).real),
        "WW_star": "8 I_60 exact",
        "g_projection_at_unit_coupling": int(projected_g.real),
        "sha256": sha256,
        "shape": list(w.shape),
        "sign_convention": "[f_j f_i,f_k^dagger]=delta_ik f_j-delta_jk f_i for i<j",
    }


def theorem_scope_check() -> dict[str, object]:
    # Q preservation bounds pure conversion order independently of an a priori
    # polynomial cutoff: 2m distinct CAR annihilators imply m <= nf/2.
    nf = 64
    maximum_m = nf // 2
    require(maximum_m == 32, "unexpected conversion-order bound")
    sector_dimensions = {}
    nb = 60
    for q in (0, 1, 2, 32, 64):
        dimension = 0
        for fermions in range(min(nf, q) + 1):
            if (q - fermions) % 2 == 0:
                bosons = (q - fermions) // 2
                dimension += math.comb(nf, fermions) * math.comb(nb + bosons - 1, bosons)
        sector_dimensions[str(q)] = dimension
    return {
        "finite_Q_sector_examples": sector_dimensions,
        "maximum_conversion_order_m": maximum_m,
        "maximum_fermion_degree_2m": 2 * maximum_m,
        "operator_extension_conditions": [
            "finite numbers of CAR and CCR modes",
            "irreducible Fock representation",
            "self-adjoint H strongly commuting with Q",
            "finite-particle core contained in Dom(H) and invariant under H",
            "all nested response identities hold as operator identities on that core",
        ],
    }


def weak_compositions(total: int, slots: int) -> list[tuple[int, ...]]:
    if slots == 1:
        return [(total,)]
    out = []
    for first in range(total + 1):
        for tail in weak_compositions(total - first, slots - 1):
            out.append((first,) + tail)
    return out


def filled_state_weight_check() -> dict[str, object]:
    """Small exact ward for the filled-state separation and norm formula."""
    nf = 4
    nb = 3
    annihilators, creators = car_generators(nf)
    full_state = np.zeros(1 << nf, dtype=np.int64)
    full_state[-1] = 1
    checked_basis_terms = 0
    checked_nonzero_images = 0
    image_sources: dict[tuple[object, ...], tuple[tuple[int, ...], int]] = {}

    for m in (1, 2):
        for alpha in weak_compositions(m, nb):
            alpha_factorial = math.prod(math.factorial(value) for value in alpha)
            for occupied in itertools.combinations(range(nf), 2 * m):
                imask = sum(1 << i for i in occupied)
                pair_operator = fermion_monomial(creators, annihilators, 0, imask)
                fermion_pair_norm_sum = 0
                for i, j in itertools.combinations(range(nf), 2):
                    nested = pair_operator @ creators[i] - creators[i] @ pair_operator
                    nested = nested @ creators[j] + creators[j] @ nested
                    image = nested @ full_state
                    norm_squared = int(image @ image)
                    expected = int(i in occupied and j in occupied)
                    require(norm_squared == expected, f"filled-state CAR ward failed at {(m, occupied, i, j)}")
                    fermion_pair_norm_sum += norm_squared
                    if not expected:
                        continue
                    holes = tuple(k for k in occupied if k not in (i, j))
                    for mode, exponent in enumerate(alpha):
                        if exponent == 0:
                            continue
                        beta = list(alpha)
                        beta[mode] -= 1
                        key = (mode, i, j, tuple(beta), holes)
                        source = (alpha, imask)
                        require(key not in image_sources, f"filled-state images collided: {key}")
                        image_sources[key] = source
                        checked_nonzero_images += 1

                require(
                    fermion_pair_norm_sum == m * (2 * m - 1),
                    "fermion-pair count does not equal binomial(2m,2)",
                )
                boson_sum = 0
                for mode, exponent in enumerate(alpha):
                    if exponent:
                        beta_factorial = math.prod(
                            math.factorial(value - (1 if index == mode else 0))
                            for index, value in enumerate(alpha)
                        )
                        boson_sum += exponent * exponent * beta_factorial
                require(boson_sum == m * alpha_factorial, "boson factorial identity failed")
                total_weight = boson_sum * fermion_pair_norm_sum
                expected_weight = m * m * (2 * m - 1) * alpha_factorial
                require(total_weight == expected_weight, "filled-state total weight failed")
                checked_basis_terms += 1

    return {
        "checked_basis_terms": checked_basis_terms,
        "checked_nonzero_response_images": checked_nonzero_images,
        "formula": "m^2 (2m-1) alpha!",
        "modes": {"boson": nb, "fermion": nf},
        "orders_checked_by_exact_CAR_matrices": [1, 2],
        "orthogonal_image_labels": "(A,i,j,alpha-e_A,I\\{i,j}) are collision-free",
    }


def main() -> None:
    result = {
        "filled_state_weight_check": filled_state_weight_check(),
        "finite_rank_check": finite_rank_check(),
        "native_tensor_check": native_tensor_check(),
        "status": "PASS",
        "theorem_scope_check": theorem_scope_check(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
