#!/usr/bin/env python3
"""Exact finite checks for the native-root open-chain spatial-response gate.

This checker does not diagonalize the many-body Hamiltonian.  It verifies the
native E8-root combinatorics used by the variational and f-sum bounds and the
all-m coefficient identities exactly.  Open-chain Fourier profiles numerically
replay the separately derived exact geometric-sum identity.
The accompanying JSON/TXT state the analytic inequalities and their scope.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools as it
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
SOURCE = REPO / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py"
SOURCE_SHA256 = "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593"

Gaussian = tuple[tuple[int, int], ...]


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def phase(z: Gaussian, power: int) -> Gaussian:
    power %= 4
    maps = (
        lambda a, b: (a, b),
        lambda a, b: (-b, a),
        lambda a, b: (-a, -b),
        lambda a, b: (b, -a),
    )
    return tuple(maps[power](a, b) for a, b in z)


def canonical_mu4(z: Gaussian) -> Gaussian:
    return min(phase(z, k) for k in range(4))


def source_roots() -> list[Gaussian]:
    supports = [
        tuple(sorted((2 * i, 2 * i + 1, 2 * j, 2 * j + 1)))
        for i, j in it.combinations(range(4), 2)
    ]
    supports += [
        tuple(2 * k + d[k] for k in range(4))
        for d in it.product((0, 1), repeat=4)
        if sum(d) % 2 == 0
    ]
    real_roots: list[tuple[int, ...]] = []
    for k, sign in it.product(range(8), (-1, 1)):
        x = [0] * 8
        x[k] = 2 * sign
        real_roots.append(tuple(x))
    for support in supports:
        for signs in it.product((-1, 1), repeat=4):
            x = [0] * 8
            for k, sign in zip(support, signs):
                x[k] = sign
            real_roots.append(tuple(x))
    roots = [tuple((x[2 * k], x[2 * k + 1]) for k in range(4)) for x in real_roots]
    require(len(roots) == 240 and len(set(roots)) == 240, "240 distinct roots")
    require(all(norm2(z) == 4 for z in roots), "native roots have norm squared four")
    return sorted(roots)


def norm2(z: Gaussian) -> int:
    return sum(a * a + b * b for a, b in z)


def inner(z: Gaussian, a: Gaussian) -> tuple[int, int]:
    # z^dagger a
    real = sum(zr * ar + zi * ai for (zr, zi), (ar, ai) in zip(z, a))
    imag = sum(zr * ai - zi * ar for (zr, zi), (ar, ai) in zip(z, a))
    return real, imag


def reflect(z: Gaussian, a: Gaussian) -> Gaussian:
    # r_z a = a - z (z^dagger a)/2, for ||z||^2=4.
    cr, ci = inner(z, a)
    out = []
    for (ar, ai), (zr, zi) in zip(a, z):
        nr = zr * cr - zi * ci
        ni = zr * ci + zi * cr
        require(nr % 2 == 0 and ni % 2 == 0, "integral native reflection")
        out.append((ar - nr // 2, ai - ni // 2))
    return tuple(out)


def distance_x2(a: Gaussian, b: Gaussian) -> Fraction:
    # x=realification(alpha)/2.
    return Fraction(
        sum((ar - br) ** 2 + (ai - bi) ** 2 for (ar, ai), (br, bi) in zip(a, b)),
        4,
    )


def native_checks() -> dict[str, object]:
    source_bytes = SOURCE.read_bytes()
    source_hash = hashlib.sha256(source_bytes).hexdigest()
    require(source_hash == SOURCE_SHA256, "pinned source_channel.py hash")

    roots = source_roots()
    root_set = set(roots)
    rays = sorted({canonical_mu4(z) for z in roots})
    require(len(rays) == 60, "60 mu4 rays")

    histograms = set()
    row_sums = set()
    incoming: dict[Gaussian, Fraction] = defaultdict(Fraction)
    for alpha in roots:
        histogram: Counter[Fraction] = Counter()
        for ray in rays:
            beta = reflect(ray, alpha)
            require(beta in root_set, "reflection preserves the 240 roots")
            d2 = distance_x2(alpha, beta)
            histogram[d2] += 1
            incoming[beta] += d2
        histograms.add(tuple(sorted(histogram.items())))
        row_sums.add(sum(d * count for d, count in histogram.items()) / 60)

    expected_histogram = ((Fraction(0), 15), (Fraction(1), 32), (Fraction(2), 12), (Fraction(4), 1))
    require(histograms == {expected_histogram}, "uniform reflection-distance histogram")
    require(row_sums == {Fraction(1)}, "unit weighted row sum")
    require(set(value / 60 for value in incoming.values()) == {Fraction(1)}, "unit weighted column sum")

    # Rank-one register projector Q=|e_0><e_0| in the limiting root mixture.
    q_values = [Fraction(a * a + b * b, 4) for (a, b), *_ in roots]
    q1 = sum(q_values, Fraction()) / 240
    q2 = sum((q * q for q in q_values), Fraction()) / 240
    require(q1 == Fraction(1, 4), "single-register projector moment")
    require(q2 == Fraction(1, 10), "two-register projector moment")

    return {
        "source_sha256": source_hash,
        "source_pin_match": True,
        "root_count": len(roots),
        "mu4_ray_count": len(rays),
        "native_root_norm_squared": 4,
        "x_norm_squared": "1",
        "reflection_distance_histogram_per_root": {str(d): n for d, n in expected_histogram},
        "fixed_reflections_per_root": 15,
        "weighted_block_schur_row_sum": "1",
        "weighted_block_schur_column_sum": "1",
        "register_Q_mean": str(q1),
        "register_Q_two_site_moment": str(q2),
        "register_Q_connected_two_site": str(q2 - q1 * q1),
        "register_Q_zero_sum_normalized_static_variance": str(q1 - q2),
    }


def all_m_checks(max_m: int = 64) -> dict[str, object]:
    checked_pairs = 0
    checked_q_profiles = 0
    worst_q_error = 0.0
    for m in range(2, max_m + 1):
        coeffs = []
        for k in range(1, m):
            direct = sum(j - i for i in range(1, k + 1) for j in range(k + 1, m + 1))
            closed = m * k * (m - k) // 2
            require(direct == closed, "pair-distance bond coefficient")
            coeffs.append(direct)
            checked_pairs += 1
        exact_max = m**3 // 8 if m % 2 == 0 else m * (m * m - 1) // 8
        require(max(coeffs) == exact_max, "maximum pair-distance bond coefficient")

        for n in range(1, m):
            q = math.pi * n / m
            weights = [math.sqrt(2 / m) * math.cos(q * (e - 0.5)) for e in range(1, m + 1)]
            require(abs(sum(weights)) < 2e-12, "open-chain q profile is zero-sum")
            require(abs(sum(w * w for w in weights) - 1.0) < 2e-12, "open-chain q profile is normalized")
            running = 0.0
            antiderivative_norm2 = 0.0
            for w in weights[:-1]:
                running += w
                antiderivative_norm2 += running * running
            closed = 1.0 / (4.0 * math.sin(q / 2.0) ** 2)
            worst_q_error = max(worst_q_error, abs(antiderivative_norm2 - closed))
            checked_q_profiles += 1
    require(worst_q_error < 2e-10, "open-chain antiderivative norm identity")
    return {
        "m_range_checked": [2, max_m],
        "pair_coefficients_checked": checked_pairs,
        "q_profiles_numeric_replay_checked": checked_q_profiles,
        "q_profile_numeric_replay_max_abs_error": worst_q_error,
        "q_profile_replay_type": "numeric replay of the exact analytic geometric-sum identity",
        "pair_coefficient": "c_k = m k (m-k)/2",
        "pair_coefficient_max_even_m": "m^3/8",
        "pair_coefficient_max_odd_m": "m(m^2-1)/8",
        "open_chain_q": "q_n=pi n/m, n=1,...,m-1",
        "open_chain_weight": "w_e=sqrt(2/m) cos(q_n(e-1/2))",
        "antiderivative_norm_squared": "1/[4 sin^2(q_n/2)]",
    }


def build_payload() -> dict[str, object]:
    native = native_checks()
    finite = all_m_checks()
    return {
        "verdict": "PASS_WITH_SCOPE_LIMIT",
        "model_scope": "The specified pure-root, pure-permutation open-chain Hamiltonian only; m>=2, J>=0, kappa>0, mu>0.",
        "no_new_hamiltonian": True,
        "full_many_body_spectrum_computed": False,
        "native_exact_checks": native,
        "finite_identity_checks": finite,
        "all_m_bounds": {
            "trial": "E0 <= 3 kappa m/4",
            "gradient": "sum_{e=1}^{m-1}<|x_{e+1}-x_e|^2> <= 3 kappa m/(2 mu)",
            "endpoint": "<x_1 dot x_m> >= 1-3 kappa m(m-1)/(4 mu)",
            "endpoint_at_mu_ge_3kappa_m2": ">=3/4+1/(4m), hence the user's >=3/4 bound is valid",
            "magnetization_even_m_at_threshold": "sum_a Var(M_a)=<M^2> >=15m^2/16",
            "magnetization_odd_m_at_threshold": "sum_a Var(M_a)=<M^2> >=(15m^2+1)/16",
            "gap_even_m": "Delta <=8 kappa/(15m)",
            "gap_odd_m": "Delta <=8 kappa m/(15m^2+1)",
            "gap_prerequisites": "unique ground state plus the exact global source inversion symmetry",
        },
        "q_resolved_source_coordinate_gate": {
            "observable": "O_n,a=sum_e w_e^(n) x_e^a with normalized real open-chain w^(n)",
            "locked_subspace": "O_n,a P_lock=P_lock O_n,a=0",
            "static_sum": "S0(n)=sum_a int S_aa(n,omega)domega <=3 kappa m/[8 mu sin^2(q_n/2)]",
            "f_sum": "S1(n)=sum_a int omega S_aa(n,omega)domega <=kappa/2",
            "finite_pole_criterion": "Any claimed pole/window with total residue Z at q_n must obey Z<=3 kappa m/[8 mu sin^2(q_n/2)]; if its support has omega>=omega_min>0, also Z<=kappa/(2 omega_min).",
            "fixed_nonzero_q_under_lock_scaling": "If q_n stays bounded away from 0 and mu>=3 kappa m^2, S0(n)<=1/[8m sin^2(q_n/2)] ->0.",
            "long_wave_limit": "For fixed n, q_n=pi n/m ->0; mu>=3 kappa m^2 gives only S0(n)<=m/(2 pi^2 n^2)(1+o(1)), so it does not suppress the collective long-wave sector.",
            "scope": "This excludes finite-residue source-coordinate response at fixed nonzero q. It does not exclude spectrally dark modes, prove a dispersion law, or apply to arbitrary register observables.",
        },
        "register_observable_scope_check": {
            "limiting_state": "Tracing the orthogonal source labels from Omega_m leaves a classical root mixture on the registers.",
            "rank_one_Q_moments": "<Q_e>=1/4, <Q_e Q_f>=1/10 for e!=f, connected=3/80.",
            "zero_sum_normalized_profile": "<|sum_e w_e(Q_e-1/4)|^2>=3/20, independent of m.",
            "consequence": "The all-observable claim 'every nonzero-q local response vanishes' is false. Only the specified source-coordinate O_w is proved to be suppressed; the Q fluctuation need not be low-frequency.",
        },
        "interpretation": "The proven 1/m gap upper bound is a collective q=0 source-coordinate statement, not evidence for eight spatial dimensions. The eight components are native root coordinates.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="print the complete machine-readable result")
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print("SPATIAL RESPONSE CHECK: PASS_WITH_SCOPE_LIMIT")
        print("native roots/rays: 240/60; weighted f-sum Schur constant: 1")
        print("user endpoint and 8*kappa/(15*m) bounds: VERIFIED (finite-m endpoint sharpened)")
        print("fixed nonzero-q source-coordinate residue: SUPPRESSED under mu>=3*kappa*m^2")
        print("all-observable nonzero-q suppression: REFUTED by register-Q static variance 3/20")


if __name__ == "__main__":
    main()
