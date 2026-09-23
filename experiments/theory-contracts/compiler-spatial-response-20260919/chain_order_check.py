"""Exact bounded audit of the fixed-length open-chain strong-lock coefficient.

This checker does not construct a new physical model.  It audits the natural
open-chain repetition of the pure-permutation packet and adjacent overlap lock
that were certified for two packets in
compiler-overlap-phase-lock-20260919.  The all-m statement proved here is a
fixed-m strong-lock asymptotic statement; no m-uniform finite-lock threshold is
claimed.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
SOURCE = REPO / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py"
SOURCE_SHA256 = "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593"
M2_CERT = REPO / "experiments/theory-contracts/compiler-overlap-phase-lock-20260919/effective_check.json"
M2_CERT_SHA256 = "11dcef3e223b0c5a6ea05354a7fc098eb2d2e06b1db9d9e13f54c8c4dc30f699"


checks: Counter[str] = Counter()


def require(condition: bool, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks[label] += 1


def gaussian_key(vector: np.ndarray) -> tuple[tuple[int, int], ...]:
    require(
        np.array_equal(vector.real, np.rint(vector.real))
        and np.array_equal(vector.imag, np.rint(vector.imag)),
        "Gaussian root coordinates remain integral",
    )
    return tuple(
        (int(round(value.real)), int(round(value.imag))) for value in vector
    )


def polynomial_coefficients(roots: tuple[int, ...]) -> list[int]:
    """Coefficients low-to-high of the monic polynomial with these roots."""
    coefficients = [1]
    for root in roots:
        updated = [0] * (len(coefficients) + 1)
        for degree, coefficient in enumerate(coefficients):
            updated[degree] -= root * coefficient
            updated[degree + 1] += coefficient
        coefficients = updated
    return coefficients


def exact_integer_spectrum(
    matrix: np.ndarray,
    eigenvalues: tuple[int, ...],
    multiplicities: tuple[int, ...],
    label: str,
) -> None:
    """Certify an integer symmetric spectrum without a numerical eigensolve."""
    require(
        np.array_equal(matrix, matrix.T)
        and np.issubdtype(matrix.dtype, np.integer),
        f"{label} is an exact symmetric integer matrix",
    )
    coefficients = polynomial_coefficients(eigenvalues)
    value = np.eye(len(matrix), dtype=np.int64)
    for coefficient in reversed(coefficients[:-1]):
        value = value @ matrix
        value[np.diag_indices_from(value)] += coefficient
    require(not np.any(value), f"{label} exact spectral polynomial")

    power = np.eye(len(matrix), dtype=np.int64)
    moments: list[int] = []
    for _ in eigenvalues:
        moments.append(int(np.trace(power)))
        power = power @ matrix
    vandermonde = sp.Matrix(
        [[sp.Integer(root) ** degree for root in eigenvalues]
         for degree in range(len(eigenvalues))]
    )
    recovered = tuple(int(value) for value in vandermonde.inv() * sp.Matrix(moments))
    require(recovered == multiplicities, f"{label} exact spectral multiplicities")


def boundary(mask: int, length: int) -> int:
    return sum(
        ((mask >> site) & 1) != ((mask >> (site + 1)) & 1)
        for site in range(length - 1)
    )


def ordered_path_sum(length: int) -> Fraction:
    """Subset DP for sum_sigma prod_{k=1}^{m-1} 1/|d S_k|."""
    full = (1 << length) - 1
    dynamic = [Fraction(0) for _ in range(1 << length)]
    dynamic[0] = Fraction(1)
    for mask in range(1 << length):
        if dynamic[mask] == 0:
            continue
        for site in range(length):
            if mask & (1 << site):
                continue
            enlarged = mask | (1 << site)
            divisor = 1 if enlarged == full else boundary(enlarged, length)
            require(divisor > 0, f"m={length}: every proper nonempty cut has boundary")
            dynamic[enlarged] += dynamic[mask] / divisor
    return dynamic[full]


def main() -> None:
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "pinned native sixty-ray source")
    require(hashlib.sha256(M2_CERT.read_bytes()).hexdigest() == M2_CERT_SHA256,
            "pinned independent m=2 effective certificate")
    module_spec = importlib.util.spec_from_file_location("chain_native_source", SOURCE)
    source = importlib.util.module_from_spec(module_spec)
    require(module_spec.loader is not None, "native source module has a loader")
    module_spec.loader.exec_module(source)

    rays = source.source_rays()
    require(len(rays) == 60, "sixty native Gaussian rays loaded")
    roots = np.stack([(1j ** phase) * ray for ray in rays for phase in range(4)])
    root_index = {gaussian_key(root): index for index, root in enumerate(roots)}
    require(len(root_index) == 240, "two hundred forty oriented roots")

    gram = roots.conj() @ roots.T
    require(
        np.array_equal(gram.real, np.rint(gram.real))
        and np.array_equal(gram.imag, np.rint(gram.imag)),
        "oriented-root Gram matrix is Gaussian integral",
    )
    gram_real = np.rint(gram.real).astype(np.int64)
    gram_imag = np.rint(gram.imag).astype(np.int64)
    adjacency = ((gram_real == 2) & (gram_imag == 0)).astype(np.int64)
    antipode_index = np.array(
        [root_index[gaussian_key(-root)] for root in roots], dtype=np.int64
    )
    antipode = np.eye(240, dtype=np.int64)[antipode_index]
    require(np.array_equal(adjacency.sum(axis=1), 32 * np.ones(240, dtype=np.int64)),
            "A32 is regular of degree thirty-two")
    require(np.array_equal(antipode @ antipode, np.eye(240, dtype=np.int64)),
            "F is the exact antipodal involution")
    require(np.array_equal(adjacency @ antipode, antipode @ adjacency),
            "A32 and F commute exactly")

    # Joint A32/F spectrum.  Representatives of antipodal pairs give exact
    # integer matrices on the F=+1 and F=-1 subspaces.
    seen: set[int] = set()
    representatives: list[int] = []
    for alpha, beta in enumerate(antipode_index):
        if alpha in seen:
            continue
        representatives.append(alpha)
        seen.update((alpha, int(beta)))
    require(len(representatives) == 120, "one hundred twenty antipodal pairs")
    a_plus = np.array(
        [[adjacency[alpha, beta] + adjacency[alpha, antipode_index[beta]]
          for beta in representatives] for alpha in representatives],
        dtype=np.int64,
    )
    a_minus = np.array(
        [[adjacency[alpha, beta] - adjacency[alpha, antipode_index[beta]]
          for beta in representatives] for alpha in representatives],
        dtype=np.int64,
    )
    plus_values = (-8, -4, 0, 8, 32)
    plus_mults = (9, 40, 45, 25, 1)
    minus_values = (-4, 4, 16)
    minus_mults = (72, 40, 8)
    exact_integer_spectrum(a_plus, plus_values, plus_mults, "A32 on F=+1")
    exact_integer_spectrum(a_minus, minus_values, minus_mults, "A32 on F=-1")

    # Reconstruct the native event action and its complete transition profile.
    reflections = [np.eye(4) - np.outer(ray, ray.conj()) / 2 for ray in rays]
    profiles: Counter[tuple[int, int, int, int]] = Counter()
    for alpha, root in enumerate(roots):
        target_counts: Counter[int] = Counter()
        for reflection in reflections:
            target_counts[root_index[gaussian_key(reflection @ root)]] += 1
        fixed = target_counts[alpha]
        half = sum(count for beta, count in target_counts.items()
                   if beta != alpha and gram_real[alpha, beta] == 2
                   and gram_imag[alpha, beta] == 0)
        zero = sum(count for beta, count in target_counts.items()
                   if beta != alpha and gram_real[alpha, beta] == 0
                   and gram_imag[alpha, beta] == 0)
        opposite = target_counts[int(antipode_index[alpha])]
        require(all(count == 1 for beta, count in target_counts.items() if beta != alpha),
                "every nonfixed reflected target is reached uniquely")
        profiles[(fixed, half, zero, opposite)] += 1
    require(profiles == Counter({(15, 32, 12, 1): 240}),
            "all roots have transition profile 15/32/12/1")

    # The local first-order matter edge.  Its unique bottom vector is
    # psi_alpha tensor psi_alpha, which makes the open chain frustration-free.
    alpha = rays[0]
    fixed_reflections = [reflection for reflection in reflections
                         if np.array_equal(reflection @ alpha, alpha)]
    require(len(fixed_reflections) == 15,
            "fifteen native events fix the pinned oriented root")
    edge60_complex = 60 * np.eye(16, dtype=np.complex128) - sum(
        (np.kron(reflection, reflection) for reflection in fixed_reflections),
        np.zeros((16, 16), dtype=np.complex128),
    )
    require(
        np.array_equal(edge60_complex.real, np.rint(edge60_complex.real))
        and not np.any(edge60_complex.imag),
        "sixty times the one-edge matter operator is exact real integral",
    )
    edge60 = np.rint(edge60_complex.real).astype(np.int64)
    exact_integer_spectrum(
        edge60,
        (45, 53, 55, 57, 65),
        (1, 3, 6, 3, 3),
        "one-edge first-order matter operator 60h",
    )
    psi = alpha / 2
    require(np.array_equal(edge60 @ np.kron(psi, psi),
                           45 * np.kron(psi, psi)),
            "psi tensor psi spans the one-edge bottom eigenspace")

    # Exact subset-DP replay of the ordered denominators, and coefficient/gap
    # replay through m=10.  This is exponential in m, not factorial.
    path_sums: dict[str, str] = {}
    coefficient_replay: dict[str, dict[str, object]] = {}
    for length in range(2, 11):
        path_sum = ordered_path_sum(length)
        require(path_sum == 2 ** (length - 1),
                f"m={length}: ordered cut-denominator sum is 2^(m-1)")
        path_sums[str(length)] = str(path_sum)

        base = Fraction(1, 60) * Fraction(1, 30) ** (length - 1)
        coefficients: dict[str, str] = {}
        for name, overlap in (
            ("half", Fraction(1, 2)),
            ("orthogonal", Fraction(0)),
            ("antipode", Fraction(-1)),
        ):
            raw = (
                path_sum * overlap ** (length - 1)
                / (1 - overlap) ** (length - 1)
                / 60 ** length
            )
            coefficients[name] = str(raw)
        require(Fraction(coefficients["half"]) == base,
                f"m={length}: half-overlap coefficient equals a_m")
        require(Fraction(coefficients["orthogonal"]) == 0,
                f"m={length}: orthogonal transition vanishes")
        c = Fraction(-1, 2) ** (length - 1)
        require(Fraction(coefficients["antipode"]) == base * c,
                f"m={length}: antipode coefficient equals c_m a_m")

        levels = (
            [(Fraction(value) + c, mult, "+")
             for value, mult in zip(plus_values, plus_mults)]
            + [(Fraction(value) - c, mult, "-")
               for value, mult in zip(minus_values, minus_mults)]
        )
        levels.sort(reverse=True, key=lambda item: item[0])
        require(levels[0] == (32 + c, 1, "+"),
                f"m={length}: effective top level is simple")
        require(levels[1] == (16 - c, 8, "-"),
                f"m={length}: coordinate level is exactly second")
        gap = levels[0][0] - levels[1][0]
        require(gap == 16 + 2 * c,
                f"m={length}: exact dimensionless first gap")
        resolvent_sign = -1 if (length - 1) % 2 else 1
        event_sign = -1 if length % 2 else 1
        require(resolvent_sign * event_sign == -1,
                f"m={length}: Feshbach and event signs give -B_m")
        coefficient_replay[str(length)] = {
            "c_m": str(c),
            "a_m_without_kappa_mu": str(base),
            "transition_coefficients_without_kappa_mu": coefficients,
            "B_m_top": str(levels[0][0]),
            "B_m_top_multiplicity": levels[0][1],
            "B_m_next": str(levels[1][0]),
            "B_m_next_multiplicity": levels[1][1],
            "dimensionless_gap": str(gap),
        }

    require(
        Fraction(coefficient_replay["2"]["a_m_without_kappa_mu"]) == Fraction(1, 1800)
        and Fraction(coefficient_replay["2"]["c_m"]) == Fraction(-1, 2),
        "m=2 reduces to (2 A32-F)/3600",
    )

    result = {
        "research_id": "UR.COMPILER.OPEN_CHAIN.ORDER_AUDIT.20260919",
        "verdict": "PASS_FIXED_M_LEADING_ORDER__NO_UNIFORM_FINITE_LOCK_CLAIM",
        "defined_scope": {
            "sources": "m oriented-root sources on an open path",
            "registers": "m+1 C4 registers, packet i acting on registers i-1 and i",
            "lock": "mu sum_i [1-Re<psi_(alpha_i),psi_(alpha_(i+1))>]",
            "events": "pure root permutation R_r with register reflection r tensor r, averaged over sixty native rays",
            "matter": "the certified positive controlled edge terms repeated along the path",
        },
        "theorem": {
            "first_nonscalar_order": "m",
            "a_m": "kappa/60 * (kappa/(30 mu))^(m-1)",
            "c_m": "(-1/2)^(m-1)",
            "effective_operator": "scalar*I - a_m [A32+c_m F] + O_m(mu^(-m)) for fixed kappa,J,m",
            "leading_ground": "uniform coherent sum over the 240 aligned roots; multiplicity 1",
            "leading_first_excited": "eight real E8 coordinate columns; multiplicity 8",
            "gap": "a_m [16+2 c_m] + O_m(mu^(-m))",
            "fixed_m_consequence": "for every fixed finite m there exists a sufficiently large lock for a unique ground state",
        },
        "matter_first_order": {
            "edge_spectrum_of_60h": {"45": 1, "53": 3, "55": 6, "57": 3, "65": 3},
            "edge_bottom": "3/4, simple, vector psi_alpha tensor psi_alpha",
            "chain_bottom": "3m/4, simple for each alpha, vector psi_alpha^(m+1)",
            "positive_controlled_matter_terms": "annihilate the same product and cannot lower it",
        },
        "joint_spectrum": {
            "F=+1": {str(value): mult for value, mult in zip(plus_values, plus_mults)},
            "F=-1": {str(value): mult for value, mult in zip(minus_values, minus_mults)},
        },
        "ordered_path_identity": {
            "formula": "sum_sigma prod_(k=1..m-1) 1/boundary(S_k)=2^(m-1)",
            "independent_proof": "partition integral over R^(m-1) of exp(-sum_edges |t_i-t_j|), with t_1=0; tree edge differences are independent and each integrates to 2",
            "subset_dp_replay": path_sums,
        },
        "coefficient_and_gap_replay": coefficient_replay,
        "transition_profile_per_root": {
            "fixed": 15,
            "half_overlap": 32,
            "orthogonal": 12,
            "antipode": 1,
            "nonfixed_target_multiplicity": 1,
        },
        "folded_term_audit": (
            "At orders below m an off-diagonal aligned-root matrix element is impossible, "
            "because every one of the m source labels must change and one packet event changes "
            "only one source. Root transitivity makes all surviving diagonal terms scalar. "
            "Consequently folded terms built from lower orders are scalar. At order m every "
            "source is hit exactly once, every proper intermediate subset is off-lock, and the "
            "displayed irreducible path sum is the complete nonscalar term."
        ),
        "boundaries": [
            "The all-m result is for the explicitly defined repeated open-chain operator; the m=2 contract alone did not prove it.",
            "The result is an exact leading fixed-m strong-lock asymptotic, not an explicit finite-mu remainder bound.",
            "No threshold uniform in m is proved; a_m decays with m at fixed couplings.",
            "No thermodynamic, propagating-mode, continuum, preparation, current-lift, physical-origin, or TOE claim follows.",
        ],
        "source_sha256": {
            str(SOURCE): SOURCE_SHA256,
            str(M2_CERT): M2_CERT_SHA256,
        },
        "check_evaluations": sum(checks.values()),
        "distinct_checks": len(checks),
        "checks": dict(sorted(checks.items())),
    }
    (HERE / "chain_order_certificate.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "verdict": result["verdict"],
        "check_evaluations": result["check_evaluations"],
        "distinct_checks": result["distinct_checks"],
        "m_replayed": list(path_sums),
        "joint_spectrum": result["joint_spectrum"],
        "m2": coefficient_replay["2"],
        "m10": coefficient_replay["10"],
    }, indent=2))


if __name__ == "__main__":
    main()
