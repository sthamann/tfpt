#!/usr/bin/env python3
"""Exact central source classes and certified local floors.

The native 240-root source is Fourier reduced to four 60-dimensional charge
representations.  For each charge this script forms the exact Gaussian-
integer class sum S_q=60 C_q, proves centrality, constructs polynomial
projectors, and certifies the allowed local K spectrum on every class.

The K-polynomial certificate is exact: it is checked in both embeddings of
Z[i] into several finite fields, with a CRT modulus larger than twice an
explicit integer entry bound.  Band multiplicities are retained as numerical
joint-diagonalization data and are not promoted to exact ranks.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sparse
import sympy as sp


HERE = Path(__file__).resolve().parent
REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
SOURCE_REL = Path(
    "experiments/theory-contracts/"
    "compiler-correlated-event-clock-20260919/source_channel.py"
)
GROUND_REL = Path(
    "experiments/theory-contracts/"
    "compiler-bond-response-20260919/ground_audit.py"
)
GROUND_JSON_REL = Path(
    "experiments/theory-contracts/"
    "compiler-bond-response-20260919/ground_audit.json"
)
PAIR_PROOF_REL = Path(
    "experiments/theory-contracts/"
    "compiler-pair-sector-audit-20260919/PROOF.txt"
)

PINS = {
    SOURCE_REL: "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
    GROUND_REL: "61980c8b830378f312ef6f81ad655574195e29c7287f5f14bc5aa0217f90b6e8",
    GROUND_JSON_REL: "f3e45d26034d42fdba0752d4844190221202e4e887ea411280d5ee558bf69886",
    PAIR_PROOF_REL: "b63d5a7a97c331f0aa0920fb77bded14981be1c6ec735fdc91e3b1536ed5a766",
}


def F(value: str) -> Fraction:
    return Fraction(value)


# s is the eigenvalue of S_q=60 C_q.  The K bands and their multiplicities
# below were discovered by joint Hermitian diagonalization.  Exact modular
# polynomial certificates independently establish the band SET and floor.
CLASS_DATA = {
    0: [
        {"s": 12, "dim": 45, "module": "unidentified invariant class",
         "K": [(F("-2/5"), 10), (F("-1/5"), 40), (F("0"), 470),
               (F("1/5"), 160), (F("2/5"), 40)]},
        {"s": 20, "dim": 9, "module": "unidentified invariant class",
         "K": [(F("0"), 94), (F("1/5"), 40), (F("2/5"), 10)]},
        {"s": 36, "dim": 5, "module": "unidentified invariant class",
         "K": [(F("0"), 30), (F("1/5"), 40), (F("2/5"), 10)]},
        {"s": 60, "dim": 1, "module": "1 (trivial source)",
         "K": [(F("0"), 6), (F("2/5"), 10)]},
    ],
    1: [
        {"s": 10, "dim": 36, "module": "unidentified invariant class",
         "K": [(F("-3/10"), 20), (F("-1/10"), 120), (F("0"), 192),
               (F("1/10"), 40), (F("1/6"), 180), (F("3/10"), 20),
               (F("1/2"), 4)]},
        {"s": 18, "dim": 20, "module": "unidentified invariant class",
         "K": [(F("-1/6"), 36), (F("0"), 128), (F("1/10"), 60),
               (F("1/6"), 36), (F("3/10"), 60)]},
        {"s": 30, "dim": 4, "module": "bar4 coordinate source",
         "K": [(F("-1/10"), 20), (F("1/6"), 36), (F("1/2"), 8)]},
    ],
    2: [
        {"s": 12, "dim": 40, "module": "unidentified invariant class",
         "K": [(F("-1/5"), 30), (F("-1/15"), 180), (F("0"), 16),
               (F("1/15"), 270), (F("1/5"), 130), (F("1/3"), 9),
               (F("3/5"), 5)]},
        {"s": 24, "dim": 20,
         "module": "Sym2(10) plus barSym2(10); reducible class containing Omega",
         "K": [(F("-1/5"), 15), (F("-1/15"), 45), (F("1/15"), 135),
               (F("1/5"), 110), (F("1/3"), 9), (F("3/5"), 5),
               (F("1"), 1)]},
    ],
    3: [
        {"s": 10, "dim": 36, "module": "unidentified invariant class",
         "K": [(F("-1/6"), 108), (F("0"), 192), (F("1/10"), 180),
               (F("1/6"), 36), (F("3/10"), 60)]},
        {"s": 18, "dim": 20, "module": "unidentified invariant class",
         "K": [(F("-3/10"), 20), (F("0"), 128), (F("1/10"), 40),
               (F("1/6"), 108), (F("3/10"), 20), (F("1/2"), 4)]},
        {"s": 30, "dim": 4, "module": "4 conjugate-coordinate source",
         "K": [(F("-1/2"), 4), (F("1/10"), 40), (F("3/10"), 20)]},
    ],
}


SINGLE_DATA = {
    0: {
        12: [(F("-1/10"), 20), (F("0"), 64), (F("1/6"), 72),
             (F("3/10"), 20), (F("1/2"), 4)],
        20: [(F("1/6"), 36)],
        36: [(F("3/10"), 20)],
        60: [(F("1/2"), 4)],
    },
    1: {
        10: [(F("-1/15"), 45), (F("1/15"), 45), (F("1/5"), 45),
             (F("1/3"), 9)],
        18: [(F("1/15"), 45), (F("1/5"), 30), (F("3/5"), 5)],
        30: [(F("1/5"), 15), (F("1"), 1)],
    },
    2: {
        12: [(F("0"), 64), (F("1/10"), 40), (F("1/6"), 36),
             (F("3/10"), 20)],
        24: [(F("1/10"), 20), (F("1/6"), 36), (F("3/10"), 20),
             (F("1/2"), 4)],
    },
    3: {
        10: [(F("0"), 94), (F("1/5"), 40), (F("2/5"), 10)],
        18: [(F("0"), 30), (F("1/5"), 40), (F("2/5"), 10)],
        30: [(F("0"), 6), (F("2/5"), 10)],
    },
}


checks: list[str] = []


def require(ok: bool, label: str) -> None:
    if not bool(ok):
        raise RuntimeError(label)
    checks.append(label)


def gaussian_int(matrix: np.ndarray, label: str) -> np.ndarray:
    real = np.rint(matrix.real)
    imag = np.rint(matrix.imag)
    require(np.array_equal(matrix.real, real) and np.array_equal(matrix.imag, imag), label)
    return real.astype(np.int64) + 1j * imag.astype(np.int64)


def gaussian_zero(matrix: np.ndarray) -> bool:
    return bool(np.count_nonzero(matrix.real) == 0 and np.count_nonzero(matrix.imag) == 0)


def gaussian_hash(matrix: np.ndarray) -> str:
    real = np.asarray(np.rint(matrix.real), dtype="<i8")
    imag = np.asarray(np.rint(matrix.imag), dtype="<i8")
    return hashlib.sha256(real.tobytes() + imag.tobytes()).hexdigest()


def source_module():
    path = REPO / SOURCE_REL
    spec = importlib.util.spec_from_file_location("source_classes_native", path)
    module = importlib.util.module_from_spec(spec)
    require(spec.loader is not None, "source loader exists")
    spec.loader.exec_module(module)
    return module


def key(vector: np.ndarray) -> tuple[tuple[int, int], ...]:
    return tuple((int(round(x.real)), int(round(x.imag))) for x in vector)


def build_actions(rays: list[np.ndarray]):
    root_index = {
        key((1j ** phase) * ray): (index, phase)
        for index, ray in enumerate(rays)
        for phase in range(4)
    }
    require(len(root_index) == 240, "sixty rays lift to 240 roots")
    actions = [[] for _ in range(4)]
    doubled_reflections = []
    for ray in rays:
        reflection = np.eye(4, dtype=np.complex128) - np.outer(ray, ray.conj()) / 2
        doubled = gaussian_int(2 * reflection, "doubled reflection is Gaussian integral")
        require(np.array_equal(doubled @ doubled, 4 * np.eye(4)),
                "doubled reflection squares to four")
        doubled_reflections.append(doubled)
        for charge in range(4):
            action = np.zeros((60, 60), dtype=np.complex128)
            for old, old_ray in enumerate(rays):
                new, phase = root_index[key(reflection @ old_ray)]
                action[new, old] = (1j) ** (-charge * phase)
            action = gaussian_int(action, "source action is Gaussian monomial")
            require(np.array_equal(action.conj().T @ action, np.eye(60)),
                    "source action is unitary")
            require(np.array_equal(action @ action, np.eye(60)),
                    "source action is involutive")
            actions[charge].append(action)
    return actions, doubled_reflections


def polynomial(matrix: np.ndarray, roots: list[int]) -> np.ndarray:
    answer = np.eye(matrix.shape[0], dtype=np.complex128)
    identity = np.eye(matrix.shape[0], dtype=np.complex128)
    for root in roots:
        answer = gaussian_int(answer @ (matrix - root * identity),
                              "Gaussian matrix polynomial remains integral")
    return answer


def determinant_mod(matrix: np.ndarray, prime: int) -> int:
    a = np.asarray(matrix % prime, dtype=np.int64).copy()
    det = 1
    for column in range(a.shape[0]):
        hits = np.flatnonzero(a[column:, column] % prime)
        if len(hits) == 0:
            return 0
        pivot = column + int(hits[0])
        if pivot != column:
            a[[column, pivot]] = a[[pivot, column]]
            det = -det
        value = int(a[column, column] % prime)
        det = det * value % prime
        inverse = pow(value, prime - 2, prime)
        a[column] = (a[column] * inverse) % prime
        if column + 1 < a.shape[0]:
            factors = a[column + 1:, column].copy()
            a[column + 1:] = (a[column + 1:] - factors[:, None] * a[column]) % prime
    return det % prime


def primes_one_mod_four(count: int) -> list[int]:
    answer = []
    candidate = 100_000
    while len(answer) < count:
        candidate = int(sp.nextprime(candidate))
        if candidate % 4 == 1:
            answer.append(candidate)
    return answer


PRIMES = primes_one_mod_four(8)


def embedding(matrix: np.ndarray, prime: int, root_i: int) -> np.ndarray:
    real = np.asarray(np.rint(matrix.real), dtype=np.int64)
    imag = np.asarray(np.rint(matrix.imag), dtype=np.int64)
    return (real + root_i * imag) % prime


def apply_factors(
    operator: sparse.csr_matrix,
    vectors: np.ndarray,
    factors: list[int],
    prime: int,
) -> np.ndarray:
    answer = vectors
    for value in factors:
        answer = (operator @ answer - value * answer) % prime
    return np.asarray(answer, dtype=np.int64)


def exact_band_certificate(
    operator_matrix: np.ndarray,
    exact_columns: np.ndarray,
    eigenvalues: list[Fraction],
    scale: int,
    charge: int,
    cache: dict,
    label: str,
) -> dict[str, object]:
    integer_roots = [int(scale * value) for value in eigenvalues]
    require(all(Fraction(root, scale) == value
                for root, value in zip(integer_roots, eigenvalues)),
            f"{label} scaled roots are integral")
    row_norm = int(np.max(np.sum(
        np.abs(operator_matrix.real) + np.abs(operator_matrix.imag), axis=1
    )))
    max_initial = int(np.max(
        np.abs(exact_columns.real) + np.abs(exact_columns.imag)
    ))
    bound = max_initial * math.prod(row_norm + abs(root) for root in integer_roots)
    modulus = 1
    used_primes = []
    for prime in PRIMES:
        roots_i = [int(value) for value in sp.sqrt_mod(-1, prime, all_roots=True)]
        require(len(roots_i) == 2, f"{label} prime has both Gaussian embeddings")
        for root_i in roots_i:
            cache_key = (label, charge, prime, root_i)
            if cache_key not in cache:
                cache[cache_key] = sparse.csr_matrix(
                    embedding(operator_matrix, prime, root_i)
                )
            operator_mod = cache[cache_key]
            columns_mod = embedding(exact_columns, prime, root_i)
            residual = apply_factors(
                operator_mod, columns_mod, integer_roots, prime
            )
            require(not np.any(residual),
                    f"{label} class polynomial vanishes in Gaussian embedding")
        modulus *= prime
        used_primes.append(prime)
        if modulus > 2 * bound:
            break
    require(modulus > 2 * bound,
            f"{label} CRT modulus exceeds twice entry bound")

    first_prime = used_primes[0]
    first_root = int(sp.sqrt_mod(-1, first_prime, all_roots=True)[0])
    operator_mod = cache[(label, charge, first_prime, first_root)]
    columns_mod = embedding(exact_columns, first_prime, first_root)
    witnesses = {}
    for target in integer_roots:
        component = apply_factors(
            operator_mod,
            columns_mod,
            [root for root in integer_roots if root != target],
            first_prime,
        )
        nonzero = int(np.count_nonzero(component))
        require(nonzero > 0, f"{label} each rational band is exactly present")
        witnesses[str(Fraction(target, scale))] = nonzero
    return {
        "scale": scale,
        "integer_roots": integer_roots,
        "primes": used_primes,
        "crt_modulus": str(modulus),
        "twice_entry_bound": str(2 * bound),
        "nonzero_witness_counts": witnesses,
    }


def independent_columns(
    numerator: np.ndarray, dimension: int, prime: int, root_i: int
) -> tuple[np.ndarray, np.ndarray]:
    _q, _r, column_pivots = sla.qr(numerator.astype(np.complex128),
                                    pivoting=True, mode="economic")
    columns = np.asarray(column_pivots[:dimension], dtype=int)
    chosen = numerator[:, columns]
    _q2, _r2, row_pivots = sla.qr(chosen.T, pivoting=True, mode="economic")
    rows = np.asarray(row_pivots[:dimension], dtype=int)
    minor = embedding(chosen[rows, :], prime, root_i)
    require(determinant_mod(minor, prime) != 0,
            "projector columns have an exact nonzero finite-field minor")
    return columns, rows


def group_numeric(values: np.ndarray, tolerance: float = 3e-8):
    groups: list[list[float | int]] = []
    for value in np.sort(np.real_if_close(values).real):
        if not groups or abs(value - float(groups[-1][0])) > tolerance:
            groups.append([float(value), 1])
        else:
            groups[-1][1] = int(groups[-1][1]) + 1
    return [(float(value), int(mult)) for value, mult in groups]


def module_identifications(rays, actions, class_sums, projectors):
    ray_rows = gaussian_int(np.stack(rays), "ray coordinate matrix is Gaussian integral")
    uniform = np.ones((60, 1), dtype=np.complex128)
    require(gaussian_zero(class_sums[0] @ uniform - 60 * uniform),
            "charge-zero uniform line is the trivial class")

    for action, doubled in zip(actions[1], doubled_reflections_global):
        # action*F = F*r^T and doubled=2r.
        require(gaussian_zero(2 * action @ ray_rows - ray_rows @ doubled.T),
                "charge-one coordinate subspace carries bar4 action")
    require(gaussian_zero(class_sums[1] @ ray_rows - 30 * ray_rows),
            "bar4 coordinates lie in charge-one central value one half")
    require(np.array_equal(ray_rows.conj().T @ ray_rows, 60 * np.eye(4)),
            "bar4 coordinate frame has exact rank four")

    conjugate_rows = ray_rows.conj()
    require(gaussian_zero(class_sums[3] @ conjugate_rows - 30 * conjugate_rows),
            "conjugate coordinates lie in charge-three central value one half")

    pairs = [(i, j) for i in range(4) for j in range(i, 4)]
    quadratic = gaussian_int(
        np.array([[ray[i] * ray[j] for i, j in pairs] for ray in rays]),
        "quadratic coordinates are Gaussian integral",
    )
    both = np.concatenate((quadratic, quadratic.conj()), axis=1)
    require(gaussian_zero(class_sums[2] @ both - 24 * both),
            "Sym2 and barSym2 coordinates share charge-two central value two fifths")
    prime = PRIMES[0]
    root_i = int(sp.sqrt_mod(-1, prime, all_roots=True)[0])
    _q, _r, cols = sla.qr(both.astype(np.complex128), pivoting=True, mode="economic")
    chosen_cols = np.asarray(cols[:20], dtype=int)
    _q2, _r2, rows = sla.qr(both[:, chosen_cols].T, pivoting=True, mode="economic")
    chosen_rows = np.asarray(rows[:20], dtype=int)
    minor = embedding(both[np.ix_(chosen_rows, chosen_cols)], prime, root_i)
    require(determinant_mod(minor, prime) != 0,
            "Sym2 plus barSym2 coordinates have exact combined rank twenty")
    require(projectors[(2, 24)]["dimension"] == 20,
            "quadratic coordinates exhaust the reducible charge-two class")
    return {
        "q0_s60": "1 (uniform trivial source)",
        "q1_s30": "bar4 coordinate source",
        "q2_s24": "Sym2(10) plus barSym2(10), not separated by C2",
        "q3_s30": "4 conjugate-coordinate source",
    }


def main(output_json: Path, output_text: Path) -> None:
    for relative, expected in PINS.items():
        observed = hashlib.sha256((REPO / relative).read_bytes()).hexdigest()
        require(observed == expected, f"pinned input {relative.name}")

    native = source_module()
    rays = native.source_rays()
    require(len(rays) == 60, "native source has sixty rays")
    global doubled_reflections_global
    actions, doubled_reflections_global = build_actions(rays)

    class_sums: dict[int, np.ndarray] = {}
    projectors: dict[tuple[int, int], dict[str, object]] = {}
    source_certificates = {}
    for charge in range(4):
        class_sum = gaussian_int(sum(actions[charge]), "class sum is Gaussian integral")
        class_sums[charge] = class_sum
        require(np.array_equal(class_sum, class_sum.conj().T),
                f"charge {charge} class sum is Hermitian")
        for action in actions[charge]:
            require(gaussian_zero(class_sum @ action - action @ class_sum),
                    f"charge {charge} class sum commutes with every reflection")
        roots = [entry["s"] for entry in CLASS_DATA[charge]]
        require(gaussian_zero(polynomial(class_sum, roots)),
                f"charge {charge} exact central minimal polynomial")

        common = 1
        numerators = []
        class_rows = []
        for entry in CLASS_DATA[charge]:
            central = int(entry["s"])
            other = [value for value in roots if value != central]
            numerator = polynomial(class_sum, other)
            denominator = math.prod(central - value for value in other)
            dimension = int(entry["dim"])
            require(gaussian_zero(numerator @ numerator - denominator * numerator),
                    "central polynomial projector is exactly idempotent")
            require(gaussian_zero(class_sum @ numerator - central * numerator),
                    "central polynomial projector has claimed eigenvalue")
            require(np.array_equal(numerator, numerator.conj().T),
                    "central polynomial projector is Hermitian")
            trace = complex(np.trace(numerator))
            require(trace.imag == 0 and int(trace.real) == denominator * dimension,
                    "central polynomial projector has exact trace/rank")
            common = math.lcm(common, abs(denominator))
            numerators.append((numerator, denominator))
            projectors[(charge, central)] = {
                "numerator": numerator,
                "denominator": denominator,
                "dimension": dimension,
            }
            class_rows.append({
                "central_sum_eigenvalue": central,
                "central_value": str(Fraction(central, 60)),
                "dimension": dimension,
                "module": entry["module"],
                "projector_denominator": denominator,
                "projector_numerator_sha256": gaussian_hash(numerator),
            })
        total = np.zeros((60, 60), dtype=np.complex128)
        for numerator, denominator in numerators:
            total += (common // denominator) * numerator
        require(gaussian_zero(total - common * np.eye(60)),
                f"charge {charge} exact projectors sum to identity")
        source_certificates[str(charge)] = {
            "class_sum_sha256": gaussian_hash(class_sum),
            "minimal_polynomial_roots_for_S_equals_60C": roots,
            "classes": class_rows,
        }

    identifications = module_identifications(rays, actions, class_sums, projectors)

    local_results = {}
    modular_cache = {}
    for charge in range(4):
        # B_q=240 K_q=sum_l R_l(q) tensor (2r_l) tensor (2r_l).
        b_matrix = gaussian_int(
            sum(np.kron(action, np.kron(doubled, doubled))
                for action, doubled in zip(actions[charge], doubled_reflections_global)),
            "scaled local operator B=240K is Gaussian integral",
        )
        b_row_norm = int(np.max(np.sum(np.abs(b_matrix.real) + np.abs(b_matrix.imag), axis=1)))
        c_float = class_sums[charge].astype(np.complex128) / 60
        central_values, central_vectors = np.linalg.eigh(c_float)
        charge_rows = []

        for entry in CLASS_DATA[charge]:
            central = int(entry["s"])
            dimension = int(entry["dim"])
            projector = projectors[(charge, central)]
            numerator = projector["numerator"]
            expected_k = entry["K"]
            b_values = [int(240 * value) for value, _mult in expected_k]
            require(all(Fraction(value, 240) == target
                        for value, (target, _mult) in zip(b_values, expected_k)),
                    "scaled K roots are integral")

            first_prime = PRIMES[0]
            first_root = int(sp.sqrt_mod(-1, first_prime, all_roots=True)[0])
            columns, _rows = independent_columns(numerator, dimension, first_prime, first_root)
            x_exact = np.kron(numerator[:, columns], np.eye(16, dtype=np.complex128))
            max_initial = int(np.max(np.abs(x_exact.real) + np.abs(x_exact.imag)))
            bound = max_initial * math.prod(b_row_norm + abs(value) for value in b_values)
            modulus = 1
            used_primes = []
            for prime in PRIMES:
                roots_i = [int(value) for value in sp.sqrt_mod(-1, prime, all_roots=True)]
                require(len(roots_i) == 2, "prime has both Gaussian embeddings")
                for root_i in roots_i:
                    cache_key = (charge, prime, root_i)
                    if cache_key not in modular_cache:
                        modular_cache[cache_key] = sparse.csr_matrix(
                            embedding(b_matrix, prime, root_i)
                        )
                    operator_mod = modular_cache[cache_key]
                    x_mod = embedding(x_exact, prime, root_i)
                    residual = apply_factors(operator_mod, x_mod, b_values, prime)
                    require(not np.any(residual),
                            "local K class polynomial vanishes in Gaussian finite-field embedding")
                modulus *= prime
                used_primes.append(prime)
                if modulus > 2 * bound:
                    break
            require(modulus > 2 * bound,
                    "CRT modulus exceeds twice exact local polynomial entry bound")

            # Every listed rational band, especially the top one determining
            # the floor, is present: the corresponding complementary product
            # is explicitly nonzero modulo a pinned prime.
            present_witnesses = {}
            operator_mod = modular_cache[(charge, first_prime, first_root)]
            x_mod = embedding(x_exact, first_prime, first_root)
            for target in b_values:
                component = apply_factors(
                    operator_mod, x_mod,
                    [value for value in b_values if value != target],
                    first_prime,
                )
                nonzero = int(np.count_nonzero(component))
                require(nonzero > 0, "each claimed rational local K band is exactly present")
                present_witnesses[str(Fraction(target, 240))] = nonzero

            # Numerical joint diagonalization is used only for multiplicities.
            indices = np.flatnonzero(np.abs(central_values - central / 60) < 2e-9)
            require(len(indices) == dimension, "numeric central multiplicity matches exact projector rank")
            basis = central_vectors[:, indices]
            lifted = np.kron(basis, np.eye(16))
            restricted = lifted.conj().T @ (b_matrix / 240) @ lifted
            observed = group_numeric(np.linalg.eigvalsh(restricted))
            expected_float = [(float(value), mult) for value, mult in expected_k]
            require(len(observed) == len(expected_float) and
                    all(abs(left[0] - right[0]) < 3e-9 and left[1] == right[1]
                        for left, right in zip(observed, expected_float)),
                    "numerical joint multiplicities match recorded table")

            maximum = max(value for value, _mult in expected_k)
            floor = Fraction(1) - maximum
            charge_rows.append({
                "central_value": str(Fraction(central, 60)),
                "dimension": dimension,
                "module": entry["module"],
                "K_spectrum": [
                    {
                        "eigenvalue": str(value),
                        "multiplicity": mult,
                        "multiplicity_evidence": "NUMERICAL_JOINT_DIAGONALIZATION",
                    }
                    for value, mult in expected_k
                ],
                "exact_band_set_certificate": {
                    "scaled_operator": "B=240K",
                    "scaled_integer_roots": b_values,
                    "annihilating_polynomial": "product_b (B-b I) on the exact central projector range",
                    "gaussian_embeddings_per_prime": 2,
                    "primes": used_primes,
                    "crt_modulus": str(modulus),
                    "twice_entry_bound": str(2 * bound),
                    "all_bands_nonzero_mod_prime": first_prime,
                    "nonzero_witness_counts": present_witnesses,
                },
                "local_L_minimum": str(floor),
                "floor_status": "EXACT_POLYNOMIAL_AND_NONZERO_TOP_BAND_CERTIFICATE",
            })
        local_results[str(charge)] = {
            "scaled_local_operator_sha256": gaussian_hash(b_matrix),
            "classes": charge_rows,
        }

    # Single-matter mean B_q=(1/60) sum_l R_l(q) tensor r_l.  The integral
    # scaling is A_q=120 B_q=sum_l R_l(q) tensor (2r_l).
    single_results = {}
    single_cache = {}
    q1_unique_rank = None
    for charge in range(4):
        single_matrix = gaussian_int(
            sum(np.kron(action, doubled)
                for action, doubled in zip(actions[charge], doubled_reflections_global)),
            "scaled single-matter operator A=120B is Gaussian integral",
        )
        central_values, central_vectors = np.linalg.eigh(
            class_sums[charge].astype(np.complex128) / 60
        )
        charge_rows = []
        for entry in CLASS_DATA[charge]:
            central = int(entry["s"])
            dimension = int(entry["dim"])
            expected = SINGLE_DATA[charge][central]
            numerator = projectors[(charge, central)]["numerator"]
            prime = PRIMES[0]
            root_i = int(sp.sqrt_mod(-1, prime, all_roots=True)[0])
            columns, _rows = independent_columns(numerator, dimension, prime, root_i)
            exact_columns = np.kron(numerator[:, columns], np.eye(4, dtype=np.complex128))
            certificate = exact_band_certificate(
                single_matrix,
                exact_columns,
                [value for value, _multiplicity in expected],
                120,
                charge,
                single_cache,
                "single-matter-B",
            )

            indices = np.flatnonzero(np.abs(central_values - central / 60) < 2e-9)
            require(len(indices) == dimension,
                    "single-matter numeric central dimension matches exact class")
            basis = central_vectors[:, indices]
            lifted = np.kron(basis, np.eye(4))
            restricted = lifted.conj().T @ (single_matrix / 120) @ lifted
            observed = group_numeric(np.linalg.eigvalsh(restricted))
            require(len(observed) == len(expected) and
                    all(abs(left[0] - float(right[0])) < 3e-9 and left[1] == right[1]
                        for left, right in zip(observed, expected)),
                    "single-matter numerical multiplicities match recorded table")

            # The decisive q=1 bar4 invariant is exactly one-dimensional.
            rank_status = "multiplicity numerical only"
            if charge == 1 and central == 30:
                component = gaussian_int(
                    (single_matrix - 24 * np.eye(240)) @ exact_columns,
                    "q1 bar4 eigenvalue-one spectral component is Gaussian integral",
                )
                hits = np.argwhere((component.real != 0) | (component.imag != 0))
                require(len(hits) > 0, "q1 bar4 invariant spectral component is nonzero")
                pivot_row, pivot_column = (int(hits[0, 0]), int(hits[0, 1]))
                pivot = component[pivot_row, pivot_column]
                rank_one_residual = (
                    pivot * component
                    - np.outer(component[:, pivot_column], component[pivot_row, :])
                )
                require(gaussian_zero(rank_one_residual),
                        "q1 bar4 eigenvalue-one component has exact rank at most one")
                q1_unique_rank = 1
                rank_status = "EXACT_RANK_ONE_GAUSSIAN_MINOR_IDENTITY"

            maximum = max(value for value, _multiplicity in expected)
            charge_rows.append({
                "central_value": str(Fraction(central, 60)),
                "dimension": dimension,
                "module": entry["module"],
                "B_spectrum": [
                    {
                        "eigenvalue": str(value),
                        "multiplicity": multiplicity,
                        "multiplicity_evidence": (
                            rank_status if value == maximum
                            else "NUMERICAL_JOINT_DIAGONALIZATION"
                        ),
                    }
                    for value, multiplicity in expected
                ],
                "exact_band_set_certificate": certificate,
                "B_maximum": str(maximum),
                "maximum_status": "EXACT_POLYNOMIAL_AND_NONZERO_TOP_BAND_CERTIFICATE",
            })
        single_results[str(charge)] = {
            "scaled_single_matter_operator_sha256": gaussian_hash(single_matrix),
            "classes": charge_rows,
        }

    require(q1_unique_rank == 1,
            "full q1 single-matter operator has a unique eigenvalue-one invariant")

    # Resolve the reducible q=2,C=2/5 class using the two explicit quadratic
    # coordinate modules.  Q is the barSym2 module in the pinned .23 convention.
    pairs = [(i, j) for i in range(4) for j in range(i, 4)]
    quadratic = gaussian_int(
        np.array([[ray[i] * ray[j] for i, j in pairs] for ray in rays]),
        "q2 quadratic coordinate module is Gaussian integral",
    )
    q2_single_matrix = gaussian_int(
        sum(np.kron(action, doubled)
            for action, doubled in zip(actions[2], doubled_reflections_global)),
        "q2 scaled single-matter operator is Gaussian integral",
    )
    quadratic_splits = {}
    for name, coordinates, expected in (
        ("barSym2(10)", quadratic, [(F("1/6"), 36), (F("1/2"), 4)]),
        ("Sym2(10)", quadratic.conj(), [(F("1/10"), 20), (F("3/10"), 20)]),
    ):
        exact_columns = np.kron(coordinates, np.eye(4, dtype=np.complex128))
        certificate = exact_band_certificate(
            q2_single_matrix,
            exact_columns,
            [value for value, _multiplicity in expected],
            120,
            2,
            single_cache,
            f"single-matter-q2-{name}",
        )
        normalized, _singular, _right = np.linalg.svd(
            coordinates.astype(np.complex128), full_matrices=False
        )
        lifted = np.kron(normalized[:, :10], np.eye(4))
        observed = group_numeric(np.linalg.eigvalsh(
            lifted.conj().T @ (q2_single_matrix / 120) @ lifted
        ))
        require(len(observed) == len(expected) and
                all(abs(left[0] - float(right[0])) < 3e-9 and left[1] == right[1]
                    for left, right in zip(observed, expected)),
                "quadratic single-matter numerical multiplicities match")
        quadratic_splits[name] = {
            "B_spectrum": [
                {
                    "eigenvalue": str(value),
                    "multiplicity": multiplicity,
                    "multiplicity_evidence": "NUMERICAL_JOINT_DIAGONALIZATION",
                }
                for value, multiplicity in expected
            ],
            "B_maximum": str(max(value for value, _multiplicity in expected)),
            "exact_band_set_certificate": certificate,
        }

    result = {
        "verdict": "EXACT_NATIVE_SOURCE_CLASSES_AND_LOCAL_FLOORS",
        "scope": (
            "One native source Fourier sector with one or two adjacent matter registers. "
            "No two-edge recoupling, four-source ground theorem, or physical-vacuum claim."
        ),
        "pins": {str(path): value for path, value in PINS.items()},
        "source_class_certificates": source_certificates,
        "module_identifications": identifications,
        "local_class_spectra": local_results,
        "single_matter_class_spectra": single_results,
        "single_matter_q2_quadratic_split": quadratic_splits,
        "decision": {
            "all_q0_q1_q3_classes_have_L_floor_at_least": "1/2",
            "only_nonpacket_coarse_class_below_one_half": (
                "q=2, C=1/5, dimension 40, exact L floor 2/5"
            ),
            "unresolved_reducible_packet_class": (
                "q=2, C=2/5, dimension 20 = Sym2(10)+barSym2(10); "
                "it contains the unique Omega K=1 state, so C alone gives floor 0"
            ),
            "m4_consequence": (
                "The local class floors refine source labels but do not by themselves prune "
                "the 106 overlapping-edge coarse masks to a certified handful. Exact recoupled "
                "two-edge class projectors/floors are still required, especially for 22, 21/12, "
                "and 23/32 patterns."
            ),
            "single_matter_consequence": (
                "B1 has a unique eigenvalue-one invariant, located in the q=1 bar4 "
                "class. Together with the established unique q=2 Omega and the "
                "compression I-(1/2)B1, this gives the 21/12 pair floor 1/2 with "
                "a unique saturating channel. B3 has exact maximum 2/5, so q1 and "
                "q3 are not interchangeable."
            ),
        },
        "evidence_boundary": {
            "exact": (
                "pins, Gaussian actions, centrality, central polynomials/projectors/ranks, "
                "module embeddings, rational K and B band sets, band presence, local floors, "
                "and the unique B1 eigenvalue-one invariant"
            ),
            "numerical_only": "multiplicity of each K band inside a central class",
        },
        "checks": len(checks),
    }
    output_json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    lines = [
        "NATIVE SOURCE CLASSES FOR THE RELAXED-WALL / FOUR-SOURCE AUDIT",
        "19 September 2026",
        "",
        "VERDICT: EXACT_NATIVE_SOURCE_CLASSES_AND_LOCAL_FLOORS",
        "",
        "Cq is the mean of the sixty native source reflection matrices in charge q.",
        "All commutators [Cq,R_l(q)] vanish exactly. Polynomial projectors in",
        "S_q=60 C_q give the invariant classes below. The rational K band sets and",
        "the top band determining each floor have exact Gaussian-integer/CRT",
        "certificates. Band multiplicities are numerical joint-diagonalization data.",
        "",
        " q   C value   dim   known module / class                         min(I-K)",
        "---  --------  ----  -------------------------------------------  --------",
    ]
    for charge in range(4):
        for row in local_results[str(charge)]["classes"]:
            lines.append(
                f" {charge}   {row['central_value']:<8}  {row['dimension']:>3}   "
                f"{row['module']:<43}  {row['local_L_minimum']}"
            )
    lines += [
        "",
        "Exact decision:",
        "* Every q=0,1,3 class has local L floor >=1/2.",
        "* The q=2, C=1/5, dim-40 nonpacket class has the lower floor 2/5.",
        "* C2 does not separate the two quadratic tens. Its C=2/5, dim-20 class is",
        "  Sym2(10)+barSym2(10) and contains Omega, hence its coarse floor is zero.",
        "* Therefore the class average exposes the only additional low coarse class",
        "  but does not by itself reduce the 106 overlapping-edge masks to a proved",
        "  handful. The next proof object is the recoupled two-edge class floor/projector",
        "  for 22, 21/12, and 23/32 patterns.",
        "",
        "Single-matter class average Bq=mean_l R_l(q) tensor r_l:",
        " q   C value   dim   known module / class                         max(Bq)",
        "---  --------  ----  -------------------------------------------  -------",
    ]
    for charge in range(4):
        for row in single_results[str(charge)]["classes"]:
            lines.append(
                f" {charge}   {row['central_value']:<8}  {row['dimension']:>3}   "
                f"{row['module']:<43}  {row['B_maximum']}"
            )
    lines += [
        "",
        "The q=1, C=1/2 bar4 class contains the unique B1=1 invariant; its",
        "rank-one property is exact. With the established unique q=2 Omega and",
        "the Omega compression I-(1/2)B1, the 21/12 pair has exact floor 1/2",
        "and a unique saturating channel. B3 has exact global maximum 2/5, so",
        "the q=1 and q=3 source representations do not give conjugate local B spectra.",
        "Within q=2,C=2/5, barSym2 has max(B2)=1/2 and its orthogonal Sym2",
        "partner has max(B2)=3/10; the class average C2 alone cannot see this split.",
        "",
        "No four-source global ground, full vacuum, current lift, or physical selection",
        "is inferred from these one-edge floors.",
    ]
    output_text.write_text("\n".join(lines) + "\n")
    print(json.dumps({"verdict": result["verdict"], "checks": result["checks"]}, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=HERE / "source_classes.json")
    parser.add_argument("--text", type=Path, default=HERE / "source_classes.txt")
    args = parser.parse_args()
    main(args.json, args.text)
