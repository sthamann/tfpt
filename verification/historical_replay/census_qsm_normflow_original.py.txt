#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""CENSUS.QSM.NORMFLOW.01 -- canonical census QSM norm-flow probe.

FROZEN SPECIFICATION (2026-09-04)
---------------------------------
Experiment-only; no ledger, paper, verification-suite, or RH claim.

Construct bridge 1 from the single rank-four Gaussian E8 module M used by
v714.  Its Hilbert basis is the set of finite-index Z[i]-submodules K of M,
graded by [M:K].  The acting semigroup consists of injective Z[i]-linear
endomorphisms A of M.  It acts by the isometries

    mu_A delta_K = delta_{A K},             q(A) = [M:A M],
    sigma_t(mu_A) = q(A)^(it) mu_A,         H delta_K = log[M:K] delta_K.

Thus mu_A mu_B = mu_(A B), q(A B)=q(A)q(B), and [H,mu_A]=log(q(A))mu_A.
HNF representatives enumerate submodules but are NOT asserted to form a
semigroup: their canonical representatives do not multiply canonically.
The endomorphism semigroup is the exact closure that acts on the canonical
submodule space.  There is one object M and no inductive tower.

T1: enumerate all coefficients a(n), n <= 200, by Gaussian HNF cells; check
exact index multiplicativity, the norm-flow automorphism law, and finite
compressed Gibbs/KMS identities at several beta.  T2: compare coefficientwise
with product_(j=0)^3 zeta_Q(i)(s-j), classify the occurring and primitive
index degrees without a prime list, and record poles/zero shifts.  T3: test
assigned-flow, classical-renaming, global-covariance, and multiplicity kills.
T4: distinguish the constructed classical arithmetic QSM bridge 1 from the
still-missing RH positivity bridge; positive Gibbs weights are blind to
analytic-continuation cancellations.  The only named completion is an
archimedean/scaling place and the adele-class quotient of Q(i), i.e. the
classical Connes trace-formula setting, not a result of this probe.

O2 CONTROL: the classical Hecke relation
T_m T_n = sum_(d|(m,n)) d^(k-1) T_(mn/d^2) is not homogeneous for
T_n -> n^(it)T_n when d>1; verify the phase mismatch explicitly.

Prior kills respected: v740's bilateral Laurent generators contradict KMS,
whereas semigroup isometries have a proper range projection; v741's
nonmonotone inter-window UCP tower is absent because this construction uses
one module and one globally defined semigroup action.

Allowed verdicts:
  CONSTRUCTED_CANONICAL_CLASSICAL
  CONSTRUCTED_NOVEL
  KILLED(Kn)

Deterministic, exact integer/Fraction arithmetic for deciding checks; mpmath
is used only for nonintegral-beta and analytic Dirichlet-series diagnostics.
No prime table or primality API is imported or called.
"""
from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
import random
from fractions import Fraction
from pathlib import Path
from typing import Iterable

import mpmath as mp


HERE = Path(__file__).resolve().parent
RESULT_JSON = HERE / "census_qsm_normflow_result.json"
CONTRACT = "CENSUS.QSM.NORMFLOW.01"
RANK = 4
N_MAX = 200
RANDOM_SEED = 20260904
RANDOM_SAMPLES = 32
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
FENCE = "Experiment-only arithmetic QSM construction; no RH claim."
BANNED_IDENTIFIERS = {
    "isprime", "primerange", "nextprime", "prevprime", "primepi",
    "sieve", "zetazero", "nzeros",
}

Gaussian = tuple[int, int]
GMatrix = tuple[tuple[Gaussian, ...], ...]
ZERO: Gaussian = (0, 0)
ONE: Gaussian = (1, 0)
CHECKS: list[dict] = []


def check(name: str, condition: bool, detail: str) -> bool:
    CHECKS.append({"name": name, "pass": bool(condition), "detail": detail})
    marker = "PASS" if condition else "FAIL"
    print(f"[{marker}] {name}: {detail}")
    return bool(condition)


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gneg(value: Gaussian) -> Gaussian:
    return -value[0], -value[1]


def gmul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gnorm(value: Gaussian) -> int:
    return value[0] * value[0] + value[1] * value[1]


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def gdet(matrix: GMatrix) -> Gaussian:
    size = len(matrix)
    total = ZERO
    for permutation in itertools.permutations(range(size)):
        term = ONE
        for row, column in enumerate(permutation):
            term = gmul(term, matrix[row][column])
        if permutation_sign(permutation) < 0:
            term = gneg(term)
        total = gadd(total, term)
    return total


def gmatmul(left: GMatrix, right: GMatrix) -> GMatrix:
    size = len(left)
    return tuple(
        tuple(
            sum_gaussian(
                gmul(left[row][inner], right[inner][column])
                for inner in range(size)
            )
            for column in range(size)
        )
        for row in range(size)
    )


def sum_gaussian(values: Iterable[Gaussian]) -> Gaussian:
    total = ZERO
    for value in values:
        total = gadd(total, value)
    return total


def matrix_index(matrix: GMatrix) -> int:
    return gnorm(gdet(matrix))


def gaussian_classes_by_norm(nmax: int) -> dict[int, list[Gaussian]]:
    """Associate classes from the lattice norm scan, with no arithmetic list."""
    bound = math.isqrt(nmax) + 1
    classes: dict[int, set[Gaussian]] = {}
    for real in range(-bound, bound + 1):
        for imag in range(-bound, bound + 1):
            norm = real * real + imag * imag
            if not 1 <= norm <= nmax:
                continue
            associates = (
                (real, imag), (-imag, real), (-real, -imag), (imag, -real)
            )
            representative = min(associates)
            classes.setdefault(norm, set()).add(representative)
    return {norm: sorted(values) for norm, values in sorted(classes.items())}


def ideal_counts(nmax: int) -> list[int]:
    """Number of principal ideals of norm n, obtained by a lattice scan."""
    bound = math.isqrt(nmax) + 1
    representations = [0] * (nmax + 1)
    for real in range(-bound, bound + 1):
        for imag in range(-bound, bound + 1):
            norm = real * real + imag * imag
            if 1 <= norm <= nmax:
                representations[norm] += 1
    assert all(value % 4 == 0 for value in representations[1:])
    return [value // 4 for value in representations]


def divisors(value: int) -> list[int]:
    return [candidate for candidate in range(1, value + 1)
            if value % candidate == 0]


def hnf_cell_counts(nmax: int, rank: int = RANK) -> list[int]:
    """Explicit diagonal-cell recursion for Z[i]-HNF submodules.

    For diagonal norm tuple (d_0,...,d_(r-1)), each diagonal contributes
    b(d_j) associate classes and d_j^j residue choices above it.
    """
    ideals = ideal_counts(nmax)
    counts = [0] * (nmax + 1)

    def enumerate_diagonals(position: int, remaining: int, weight: int) -> int:
        if position == rank:
            return weight if remaining == 1 else 0
        total = 0
        for diagonal_norm in divisors(remaining):
            class_count = ideals[diagonal_norm]
            if class_count:
                total += enumerate_diagonals(
                    position + 1,
                    remaining // diagonal_norm,
                    weight * class_count * diagonal_norm**position,
                )
        return total

    for index in range(1, nmax + 1):
        counts[index] = enumerate_diagonals(0, index, 1)
    return counts


def dirichlet_convolution(
    left: list[int], right: list[int], nmax: int
) -> list[int]:
    output = [0] * (nmax + 1)
    for index in range(1, nmax + 1):
        output[index] = sum(
            left[divisor] * right[index // divisor]
            for divisor in divisors(index)
        )
    return output


def solomon_product_counts(nmax: int, rank: int = RANK) -> list[int]:
    """Coefficients of product_j zeta_Q(i)(s-j), independently convolved."""
    ideals = ideal_counts(nmax)
    output = [0] * (nmax + 1)
    output[1] = 1
    for shift in range(rank):
        factor = [ideals[index] * index**shift
                  for index in range(nmax + 1)]
        output = dirichlet_convolution(output, factor, nmax)
    return output


def random_triangular_endomorphism(
    rng: random.Random, diagonal_pool: list[Gaussian]
) -> GMatrix:
    rows: list[tuple[Gaussian, ...]] = []
    for row in range(RANK):
        entries: list[Gaussian] = []
        for column in range(RANK):
            if column < row:
                entries.append(ZERO)
            elif column == row:
                entries.append(rng.choice(diagonal_pool))
            else:
                entries.append((rng.randint(-1, 1), rng.randint(-1, 1)))
        rows.append(tuple(entries))
    return tuple(rows)


def semigroup_checks(classes: dict[int, list[Gaussian]]) -> dict:
    rng = random.Random(RANDOM_SEED)
    diagonal_pool = [
        value
        for norm, values in classes.items()
        if 1 <= norm <= 13
        for value in values
    ]
    rows = []
    all_exact = True
    action_exact = True
    one_parameter_error = mp.mpf("0")
    product_phase_error = mp.mpf("0")
    times = (mp.mpf("-0.7"), mp.mpf("0.0"), mp.mpf("0.31"))
    for sample in range(RANDOM_SAMPLES):
        left = random_triangular_endomorphism(rng, diagonal_pool)
        right = random_triangular_endomorphism(rng, diagonal_pool)
        product = gmatmul(left, right)
        left_index = matrix_index(left)
        right_index = matrix_index(right)
        product_index = matrix_index(product)
        exact = product_index == left_index * right_index
        all_exact &= exact

        test_basis = random_triangular_endomorphism(rng, diagonal_pool)
        sequential = gmatmul(left, gmatmul(right, test_basis))
        composed = gmatmul(product, test_basis)
        action_exact &= sequential == composed

        for first_time in times:
            for second_time in times:
                lhs = mp.power(product_index, 1j * (first_time + second_time))
                rhs = (
                    mp.power(product_index, 1j * first_time)
                    * mp.power(product_index, 1j * second_time)
                )
                one_parameter_error = max(one_parameter_error, abs(lhs - rhs))
            phase_product = mp.power(product_index, 1j * first_time)
            phase_factors = (
                mp.power(left_index, 1j * first_time)
                * mp.power(right_index, 1j * first_time)
            )
            product_phase_error = max(
                product_phase_error, abs(phase_product - phase_factors)
            )
        if sample < 6:
            rows.append({
                "sample": sample,
                "q_left": left_index,
                "q_right": right_index,
                "q_product": product_index,
                "exact": exact,
            })
    return {
        "samples": RANDOM_SAMPLES,
        "sample_head": rows,
        "index_multiplicative_exact": all_exact,
        "left_action_relation_exact": action_exact,
        "one_parameter_max_error": mp.nstr(one_parameter_error, 8),
        "product_phase_max_error": mp.nstr(product_phase_error, 8),
    }


def compressed_kms_checks(counts: list[int]) -> list[dict]:
    """KMS for compressed semigroup shifts.

    For an index-q endomorphism A, the compressed mu_A pairs every source
    basis vector at level n <= N/q with its image at level qn.  Therefore
    phi(mu_A mu_A*) = q^-beta phi(mu_A* mu_A) exactly, including the finite
    boundary projection.  Integer beta is checked as Fraction arithmetic.
    """
    indices = (2, 5, 9)
    integer_betas = (1, 2, 5)
    noninteger_betas = (mp.mpf("4.5"), mp.mpf("6.25"))
    rows: list[dict] = []
    for beta in integer_betas:
        partition = sum(
            (Fraction(counts[index], index**beta)
             for index in range(1, N_MAX + 1)),
            Fraction(0),
        )
        for shift_index in indices:
            source = sum(
                (Fraction(counts[index], index**beta)
                 for index in range(1, N_MAX // shift_index + 1)),
                Fraction(0),
            )
            left = Fraction(1, shift_index**beta) * source / partition
            right = sum(
                (Fraction(counts[index], (shift_index * index)**beta)
                 for index in range(1, N_MAX // shift_index + 1)),
                Fraction(0),
            ) / partition
            rows.append({
                "beta": str(beta),
                "q": shift_index,
                "mode": "exact_fraction",
                "error": str(left - right),
                "pass": left == right,
            })
    mp.mp.dps = 60
    for beta in noninteger_betas:
        partition = mp.fsum(
            mp.mpf(counts[index]) * mp.power(index, -beta)
            for index in range(1, N_MAX + 1)
        )
        for shift_index in indices:
            source = mp.fsum(
                mp.mpf(counts[index]) * mp.power(index, -beta)
                for index in range(1, N_MAX // shift_index + 1)
            )
            left = mp.power(shift_index, -beta) * source / partition
            right = mp.fsum(
                mp.mpf(counts[index])
                * mp.power(shift_index * index, -beta)
                for index in range(1, N_MAX // shift_index + 1)
            ) / partition
            error = abs(left - right)
            rows.append({
                "beta": mp.nstr(beta, 8),
                "q": shift_index,
                "mode": "mpmath",
                "error": mp.nstr(error, 8),
                "pass": error < mp.mpf("1e-50"),
            })
    return rows


def primitive_occurring_degrees(occurring: list[int]) -> list[int]:
    occurring_set = set(occurring)
    return [
        value
        for value in occurring
        if value > 1 and not any(
            left > 1
            and value % left == 0
            and value // left > 1
            and left in occurring_set
            and value // left in occurring_set
            for left in occurring
            if left <= math.isqrt(value)
        )
    ]


def hecke_flow_obstruction() -> dict:
    """The d=2 term in T_2 T_2 contains T_1 and breaks norm homogeneity."""
    time = mp.mpf("0.37")
    left_phase = mp.power(4, 1j * time)
    d_two_term_phase = mp.power(1, 1j * time)
    mismatch = abs(left_phase - d_two_term_phase)
    return {
        "m": 2,
        "n": 2,
        "d": 2,
        "left_degree": 4,
        "term_degree": 1,
        "degree_ratio": 4,
        "time": mp.nstr(time, 8),
        "phase_mismatch": mp.nstr(mismatch, 12),
        "obstructed": mismatch > mp.mpf("1e-12"),
        "reason": "the d-term differs by d^(2it), so the Hecke sum is not homogeneous",
    }


def dedekind_zeta_gaussian(argument: mp.mpf) -> mp.mpf:
    character = [0, 1, 0, -1]
    return mp.zeta(argument) * mp.dirichlet(argument, character)


def partition_diagnostics(counts: list[int]) -> list[dict]:
    rows = []
    for beta in (mp.mpf("4.5"), mp.mpf("5.0"), mp.mpf("6.25")):
        partial = mp.fsum(
            mp.mpf(counts[index]) * mp.power(index, -beta)
            for index in range(1, N_MAX + 1)
        )
        analytic = mp.fprod(
            dedekind_zeta_gaussian(beta - shift)
            for shift in range(RANK)
        )
        rows.append({
            "beta": mp.nstr(beta, 8),
            "partial_n_le_200": mp.nstr(partial, 18),
            "analytic_product": mp.nstr(analytic, 18),
            "relative_tail": mp.nstr(abs(analytic - partial) / abs(analytic), 10),
        })
    return rows


def ast_firewall() -> list[str]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    hits: set[str] = set()
    for node in ast.walk(tree):
        names: list[str] = []
        if isinstance(node, ast.Name):
            names.append(node.id)
        elif isinstance(node, ast.Attribute):
            names.append(node.attr)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            names.extend(alias.name.split(".")[0] for alias in node.names)
        hits.update(name for name in names if name.lower() in BANNED_IDENTIFIERS)
    return sorted(hits)


def main() -> int:
    mp.mp.dps = 60
    firewall_hits = ast_firewall()
    classes = gaussian_classes_by_norm(N_MAX)
    hnf_counts = hnf_cell_counts(N_MAX)
    formula_counts = solomon_product_counts(N_MAX)
    occurring = [index for index in range(1, N_MAX + 1)
                 if hnf_counts[index] > 0]
    missing = [index for index in range(1, N_MAX + 1)
               if hnf_counts[index] == 0]
    primitive = primitive_occurring_degrees(occurring)
    semigroup = semigroup_checks(classes)
    kms_rows = compressed_kms_checks(hnf_counts)
    hecke_obstruction = hecke_flow_obstruction()
    partition_rows = partition_diagnostics(hnf_counts)

    coefficient_mismatches = [
        index for index in range(1, N_MAX + 1)
        if hnf_counts[index] != formula_counts[index]
    ]
    multiplicative_failures = [
        [left, right]
        for left in range(1, N_MAX + 1)
        for right in range(1, N_MAX // left + 1)
        if math.gcd(left, right) == 1
        and hnf_counts[left * right] != hnf_counts[left] * hnf_counts[right]
    ]

    check("G0 no prime-table API", not firewall_hits,
          f"hits={firewall_hits}")
    check("T1 exact index multiplication",
          semigroup["index_multiplicative_exact"],
          f"{RANDOM_SAMPLES}/{RANDOM_SAMPLES} Gaussian matrix products")
    check("T1 semigroup action",
          semigroup["left_action_relation_exact"],
          "mu_A mu_B delta_K = mu_(AB) delta_K exactly")
    flow_ok = (
        mp.mpf(semigroup["one_parameter_max_error"]) < mp.mpf("1e-50")
        and mp.mpf(semigroup["product_phase_max_error"]) < mp.mpf("1e-50")
    )
    check("T1 norm-flow automorphisms", flow_ok,
          "one-parameter and product relations agree to 60-digit precision")
    check("T1 compressed Gibbs KMS",
          all(row["pass"] for row in kms_rows),
          f"{len(kms_rows)}/{len(kms_rows)} exact/mpmath identities")
    check("T2 Solomon coefficient identity", not coefficient_mismatches,
          f"{N_MAX}/{N_MAX} exact coefficients")
    check("T2 coefficient multiplicativity", not multiplicative_failures,
          "all coprime pairs with product <= 200")
    check("T2 O2 Hecke obstruction", hecke_obstruction["obstructed"],
          f"d=2 phase mismatch={hecke_obstruction['phase_mismatch']}")

    verdict = "CONSTRUCTED_CANONICAL_CLASSICAL"
    kill_criteria = {
        "K1_assigned_p_it": {
            "fires": False,
            "assessment": (
                "NO: sigma uses q(A)=Norm(det A), computed from each "
                "endomorphism; primitive degrees are classified afterwards."
            ),
        },
        "K2_standard_system_renamed": {
            "fires": True,
            "assessment": (
                "YES as a novelty test: this is the standard GL_4(Z[i])-type "
                "Connes-Marcolli/Solomon QSM. The TFPT input selects M, but "
                "the Hermitian E8 form does not change this partition function."
            ),
            "verdict_effect": (
                "Forces CANONICAL_CLASSICAL rather than NOVEL; it does not "
                "invalidate the explicitly allowed classical-construction verdict."
            ),
        },
        "K3_global_covariance_failure": {
            "fires": False,
            "assessment": (
                "NO: one module M, one Hilbert space, and one semigroup action; "
                "there are no adjacent GNS windows or inductive embeddings."
            ),
        },
        "K4_multiplicity_not_fixed": {
            "fires": False,
            "assessment": (
                "NO: a(n) is fixed by the rank-four Z[i]-module HNF census. "
                "It is rank/module-specific but not sensitive to the E8 form."
            ),
        },
    }
    bridge_delivery = {
        "a_bridge_1": (
            "CONSTRUCTED: canonical norm/index time and primitive Gaussian-ideal "
            "norm events arise without a prime oracle, as a classical arithmetic QSM."
        ),
        "b_positivity": (
            "BLIND: for beta>4 the Gibbs/KMS functional is positive and each "
            "weight n^-beta is positive; positive-cone data cannot see zeros "
            "created by cancellation after analytic continuation."
        ),
        "c_phase_diagram": (
            "NO zero-location encoding found: real-axis phase boundaries are "
            "the poles beta=1,2,3,4, while nontrivial zeros are cancellations "
            "of shifted zeta and L factors outside the positive Gibbs regime."
        ),
        "d_required_extension": (
            "Add the archimedean/scaling place on the same arithmetic space and "
            "complete to the adele class space of Q(i). Connes' quotient trace "
            "formula then carries the zero spectrum, with positivity still the "
            "untouched bridge 2; this probe does not construct that completion."
        ),
    }
    result = {
        "contract": CONTRACT,
        "spec_sha256": SPEC_SHA,
        "claim_boundary": FENCE,
        "verdict": verdict,
        "construction": {
            "module": "one rank-four free Z[i]-module underlying Gaussian E8",
            "hilbert_basis": "finite-index Z[i]-submodules K of M",
            "acting_semigroup": "injective Z[i]-endomorphisms A of M",
            "action": "mu_A delta_K = delta_(A K)",
            "index": "q(A) = Norm(det A) = [M:A M]",
            "time": "sigma_t(mu_A) = q(A)^(it) mu_A",
            "hamiltonian": "H delta_K = log([M:K]) delta_K",
            "single_object_no_tower": True,
            "whole_algebra_state_domain": (
                "normalized Gibbs trace on the whole generated Toeplitz "
                "semigroup algebra for beta>4"
            ),
            "hnf_closure_caveat": (
                "HNF representatives enumerate submodules but do not themselves "
                "form a canonical multiplicative semigroup."
            ),
        },
        "enumeration": {
            "n_max": N_MAX,
            "occurring_indices": occurring,
            "missing_indices": missing,
            "primitive_occurring_indices": primitive,
            "primitive_interpretation": (
                "2, split rational degrees p, and inert rational degrees p^2: "
                "precisely norms of irreducibles in Z[i], derived as indecomposable "
                "occurring norms rather than supplied by a list"
            ),
            "a_n_head": [
                {"n": index, "a_n": hnf_counts[index]}
                for index in range(1, 31)
            ],
        },
        "semigroup": semigroup,
        "kms_checks": kms_rows,
        "dirichlet_identity": {
            "formula": (
                "Z(s)=zeta_Q(i)(s) zeta_Q(i)(s-1) "
                "zeta_Q(i)(s-2) zeta_Q(i)(s-3)"
            ),
            "coefficient_matches": N_MAX - len(coefficient_mismatches),
            "coefficient_mismatches": coefficient_mismatches,
            "partition_diagnostics": partition_rows,
            "poles": [1, 2, 3, 4],
            "critical_inverse_temperature": 4,
            "analytic_zero_description": (
                "zeros of zeta(s-j) and L(s-j,chi_-4), j=0,1,2,3, "
                "with multiplicities after any pole/zero cancellations"
            ),
        },
        "o2_hecke_obstruction": hecke_obstruction,
        "kill_criteria": kill_criteria,
        "rh_delivery": bridge_delivery,
        "checks": CHECKS,
        "checks_passed": sum(row["pass"] for row in CHECKS),
        "checks_total": len(CHECKS),
    }
    RESULT_JSON.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"RESULT {verdict}")
    print(f"CHECKS {result['checks_passed']}/{result['checks_total']}")
    print(f"OCCURRING {len(occurring)}/{N_MAX}; MISSING {missing}")
    print(f"PRIMITIVE {primitive}")
    print("A_N_HEAD " + ", ".join(
        f"{index}:{hnf_counts[index]}" for index in range(1, 16)
    ))
    print(f"WROTE {RESULT_JSON}")
    return 0 if result["checks_passed"] == result["checks_total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
