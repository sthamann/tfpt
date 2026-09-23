"""Exact finite spectrum audit for the 240-root dynamical source.

This verifies only the stated 3840-dimensional model.  It does not select the
Hamiltonian, its couplings, a local net, physical time, or a continuum limit.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import reduce
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
SOURCE = REPO / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py"
SUBMISSION = HERE / "submitted_text.txt"
SOURCE_SHA = "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593"
SUBMISSION_SHA = "2e2fcde0dbab0015db9c63b5cf91a27f1587894bf9a9b4c3448ad075fd1e456b"
checks: list[str] = []


def require(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append(name)


def encode_half_gaussian(a: np.ndarray) -> bytes:
    """Exact key for a 4x4 matrix whose entries are Gaussian half-integers."""
    b = 2*a
    require(np.array_equal(b.real, np.rint(b.real)) and
            np.array_equal(b.imag, np.rint(b.imag)), "exact dyadic group matrix")
    out = np.empty((4, 4, 2), dtype=np.int8)
    out[:, :, 0] = np.rint(b.real).astype(np.int8)
    out[:, :, 1] = np.rint(b.imag).astype(np.int8)
    return out.tobytes()


def polynomial_coefficients(roots: list[int]) -> list[int]:
    """Low-to-high coefficients of product (x-root)."""
    coefficients = [1]
    for root in roots:
        new = [0]*(len(coefficients)+1)
        for k, c in enumerate(coefficients):
            new[k] -= root*c
            new[k+1] += c
        coefficients = new
    return coefficients


def modular_solve(a, b, prime):
    aug = [[int(x) % prime for x in row] + [int(y) % prime]
           for row, y in zip(a, b)]
    n = len(aug)
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        inv = pow(aug[col][col], -1, prime)
        aug[col] = [(x*inv) % prime for x in aug[col]]
        for row in range(n):
            if row != col and aug[row][col]:
                factor = aug[row][col]
                aug[row] = [(x-factor*y) % prime for x, y in zip(aug[row], aug[col])]
    return [aug[k][-1] for k in range(n)]


def main():
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA, "pinned .13 source")
    require(hashlib.sha256(SUBMISSION.read_bytes()).hexdigest() == SUBMISSION_SHA, "pinned submitted text")
    spec = importlib.util.spec_from_file_location("native_source", SOURCE)
    src = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(src)
    rays = src.source_rays()
    reflections = [np.eye(4)-np.outer(z, z.conj())/2 for z in rays]
    require(len(rays) == 60, "sixty native rays")

    # Full 240-root phase fibre and exact reflection action.
    root_dictionary = {}
    for ell, z in enumerate(rays):
        for phase in range(4):
            w = (1j**phase)*z
            key = tuple((int(x.real), int(x.imag)) for x in w)
            require(key not in root_dictionary, "distinct full root")
            root_dictionary[key] = (ell, phase)
    require(len(root_dictionary) == 240, "full 240-root register")
    actions = []
    for r in reflections:
        row = []
        for z in rays:
            w = r@z
            require(np.array_equal(w.real, np.rint(w.real)) and
                    np.array_equal(w.imag, np.rint(w.imag)), "reflection preserves Gaussian roots")
            row.append(root_dictionary[tuple((int(x.real), int(x.imag)) for x in w)])
        require(len({ell for ell, phase in row}) == 60, "reflection permutes rays")
        actions.append(row)

    # Generate the phase-faithful order-46080 reflection group exactly.
    generator_indices = [0, 13, 2, 3, 1]
    generators = [reflections[k] for k in generator_indices]
    identity = np.eye(4, dtype=complex)
    group = [identity]
    group_keys = {encode_half_gaussian(identity): 0}
    cursor = 0
    while cursor < len(group):
        g = group[cursor]
        cursor += 1
        for generator in generators:
            h = g@generator
            key = encode_half_gaussian(h)
            if key not in group_keys:
                group_keys[key] = len(group)
                group.append(h)
    require(len(group) == 46080, "phase-faithful reflection group order 46080")
    group_array = np.stack(group)
    group_order = len(group)

    # Right multiplication by the reflection class on the regular group algebra.
    transitions = np.empty((60, group_order), dtype=np.int32)
    for m, reflection in enumerate(reflections):
        products = group_array@reflection
        encoded = np.empty((group_order, 4, 4, 2), dtype=np.int8)
        twice = 2*products
        require(np.array_equal(twice.real, np.rint(twice.real)) and
                np.array_equal(twice.imag, np.rint(twice.imag)), "exact class transition matrices")
        encoded[:, :, :, 0] = np.rint(twice.real).astype(np.int8)
        encoded[:, :, :, 1] = np.rint(twice.imag).astype(np.int8)
        transitions[m] = [group_keys[row.tobytes()] for row in encoded]
        require(len(set(map(int, transitions[m]))) == group_order, "each class transition is a permutation")

    # An exact regular-algebra polynomial for S=sum_m reflection_m.  Modular
    # zero plus a CRT product larger than twice the elementary word-count
    # bound is an integer proof, not a probabilistic modular test.
    universal_roots = [-60, -36, -30, -24, -20, -18, -12, -10, -6, -4,
                       0, 4, 6, 10, 12, 18, 20, 24, 30, 36, 60]
    coefficients = polynomial_coefficients(universal_roots)
    coefficient_bound = sum(abs(c)*60**k for k, c in enumerate(coefficients))
    primes = [1000000007, 1000000009, 1000000033, 1000000087, 1000000093]
    require(all(sp.isprime(p) for p in primes), "CRT moduli are prime")
    modulus_product = 1
    for prime in primes:
        power = np.zeros(group_order, dtype=np.int64)
        power[0] = 1
        value = (coefficients[0] % prime)*power % prime
        for degree in range(1, len(coefficients)):
            next_power = np.zeros(group_order, dtype=np.int64)
            for transition in transitions:
                next_power[transition] += power
            power = next_power % prime
            value = (value + (coefficients[degree] % prime)*power) % prime
        require(not np.any(value), f"class polynomial vanishes modulo {prime}")
        modulus_product *= prime
    require(modulus_product > 2*coefficient_bound, "CRT lift proves exact integer class polynomial")

    # Exact characters of the four source phase sectors tensor V tensor V.
    twice_trace = 2*np.trace(group_array, axis1=1, axis2=2)
    require(np.array_equal(twice_trace.real, np.rint(twice_trace.real)) and
            np.array_equal(twice_trace.imag, np.rint(twice_trace.imag)), "exact group traces")
    twice_trace = np.rint(twice_trace.real) + 1j*np.rint(twice_trace.imag)
    phase_characters = []
    fixed_phase_data = []
    for ell, z in enumerate(rays):
        images = group_array@z
        phases = np.zeros(group_order, dtype=complex)
        fixed = np.zeros(group_order, dtype=bool)
        for phase in (1, 1j, -1, -1j):
            hits = np.all(images == phase*z, axis=1)
            require(not np.any(fixed & hits), "unique fixed-ray phase")
            fixed |= hits
            phases[hits] = phase
        fixed_phase_data.append((fixed, phases))
    for q in range(4):
        source_character = np.zeros(group_order, dtype=complex)
        for fixed, phases in fixed_phase_data:
            # With |ell;q> = 1/2 sum_k i^(kq)|i^k z_ell>, an action
            # g z_ell = phase*z_ell contributes phase^(-q).
            source_character += phases**((-q) % 4) if q else fixed.astype(float)
        numerator = source_character*twice_trace**2
        require(np.array_equal(numerator.real, np.rint(numerator.real)) and
                np.array_equal(numerator.imag, np.rint(numerator.imag)), "Gaussian character numerator")
        real = np.rint(numerator.real).astype(np.int64)
        imag = np.rint(numerator.imag).astype(np.int64)
        require(np.all(real % 4 == 0) and np.all(imag % 4 == 0), "integral phase-block character")
        phase_characters.append((real//4, imag//4))
        require(phase_characters[-1][0][0] == 960 and phase_characters[-1][1][0] == 0,
                "each phase block has dimension 960")

    # H_E/2 is the block projector onto the -1 eigenspace of r_l tensor r_l.
    # Compute exact characters of its kernel and range, both invariant under S.
    joint_characters = []
    for q in range(4):
        numerator_kernel = np.zeros(group_order, dtype=complex)
        numerator_total = np.zeros(group_order, dtype=complex)
        for (fixed, phases), reflection in zip(fixed_phase_data, reflections):
            weight = phases**((-q) % 4) if q else fixed.astype(float)
            trace_reflection_g = 2*np.einsum("ij,nji->n", reflection, group_array)
            require(np.array_equal(trace_reflection_g.real, np.rint(trace_reflection_g.real)) and
                    np.array_equal(trace_reflection_g.imag, np.rint(trace_reflection_g.imag)),
                    "exact reflected group traces")
            trace_reflection_g = (np.rint(trace_reflection_g.real) +
                                  1j*np.rint(trace_reflection_g.imag))
            numerator_total += weight*twice_trace**2
            numerator_kernel += weight*(twice_trace**2 + trace_reflection_g**2)
        def divide_gaussian(values, denominator, name):
            require(np.array_equal(values.real, np.rint(values.real)) and
                    np.array_equal(values.imag, np.rint(values.imag)), name+" integer numerator")
            real = np.rint(values.real).astype(np.int64)
            imag = np.rint(values.imag).astype(np.int64)
            require(np.all(real % denominator == 0) and np.all(imag % denominator == 0),
                    name+" exact division")
            return real//denominator, imag//denominator
        total_character = divide_gaussian(numerator_total, 4, "total character")
        kernel_character = divide_gaussian(numerator_kernel, 8, "HE-kernel character")
        range_character = (total_character[0]-kernel_character[0],
                           total_character[1]-kernel_character[1])
        require(kernel_character[0][0] == 600 and range_character[0][0] == 360,
                "HE zero/range dimensions 600 plus 360")
        joint_characters.append((kernel_character, range_character))

    # Exact traces of S^k followed by Vandermonde inversion modulo a prime.
    # The exact class polynomial gives the support. Multiplicities are integers
    # in [0,960], so their residues modulo a prime >960 determine them uniquely.
    prime = primes[0]
    count = np.zeros(group_order, dtype=np.int64)
    count[0] = 1
    phase_moments = np.zeros((4, len(universal_roots)), dtype=np.int64)
    joint_moments = np.zeros((4, 2, len(universal_roots)), dtype=np.int64)
    for degree in range(len(universal_roots)):
        for q in range(4):
            real, imag = phase_characters[q]
            phase_moments[q, degree] = sum((int(a)*int(b)) % prime for a, b in zip(count, real)) % prime
            require(sum((int(a)*int(b)) % prime for a, b in zip(count, imag)) % prime == 0,
                    "phase trace moment is real")
            for sector in range(2):
                real, imag = joint_characters[q][sector]
                joint_moments[q, sector, degree] = sum(
                    (int(a)*int(b)) % prime for a, b in zip(count, real)) % prime
                require(sum((int(a)*int(b)) % prime for a, b in zip(count, imag)) % prime == 0,
                        "joint trace moment is real")
        next_count = np.zeros(group_order, dtype=np.int64)
        for transition in transitions:
            next_count[transition] += count
        count = next_count % prime
    vandermonde = [[pow(root, degree, prime) for root in universal_roots]
                   for degree in range(len(universal_roots))]

    phase_multiplicities = []
    joint_multiplicities = []
    for q in range(4):
        multiplicities = modular_solve(vandermonde, phase_moments[q], prime)
        require(all(0 <= m <= 960 for m in multiplicities) and sum(multiplicities) == 960,
                "unique exact phase multiplicities")
        phase_multiplicities.append({root: m for root, m in zip(universal_roots, multiplicities) if m})
        split = []
        for sector, dimension in ((0, 600), (1, 360)):
            multiplicities = modular_solve(vandermonde, joint_moments[q, sector], prime)
            require(all(0 <= m <= 960 for m in multiplicities) and sum(multiplicities) == dimension,
                    "unique exact joint multiplicities")
            split.append({root: m for root, m in zip(universal_roots, multiplicities) if m})
        joint_multiplicities.append(split)
        require(Counter(phase_multiplicities[q]) == Counter(split[0]) + Counter(split[1]),
                "HE split recombines phase spectrum")

    expected_phase = [
        {-24: 10, -12: 40, 0: 600, 12: 240, 24: 70},
        {-18: 20, -10: 36, -6: 140, 0: 320, 6: 100, 10: 252, 18: 80, 30: 12},
        {-12: 45, -4: 225, 0: 16, 4: 405, 12: 240, 20: 18, 36: 10, 60: 1},
        {-30: 4, -18: 20, -10: 108, 0: 320, 6: 260, 10: 144, 18: 100, 30: 4},
    ]
    require(phase_multiplicities == expected_phase, "exact four-block spectrum")
    require(joint_multiplicities[2][0].get(60) == 1 and
            all(split[sector].get(60, 0) == 0
                for q, split in enumerate(joint_multiplicities)
                for sector in range(2) if not (q == 2 and sector == 0)),
            "unique common ground lies in phase2 HE kernel")
    require(joint_multiplicities[2][0].get(36) == 10,
            "ten exact gap modes at A=3/5 lie in HE kernel")

    # Exact common vector and its reduced register state.
    omega_blocks = np.array([np.kron(z, z)/4 for z in rays])
    for m, reflection in enumerate(reflections):
        for ell, z in enumerate(rays):
            target, phase = actions[m][ell]
            require(np.array_equal(np.kron(reflection, reflection)@omega_blocks[ell],
                                   ((-1)**phase)*omega_blocks[target]),
                    "aligned root-pair covariance")
    swap = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for j in range(4):
            swap[4*j+i, 4*i+j] = 1
    plus = (np.eye(16)+swap)/2
    register_moment = sum((np.outer(v, v.conj()) for v in omega_blocks), np.zeros((16, 16), complex))
    require(np.array_equal(10*register_moment, 60*plus), "reduced AB state is Psym/10")

    # Convert S spectrum to A=S/60 and L=I-A, including full multiplicities.
    l_spectrum = Counter()
    for spectrum in phase_multiplicities:
        for root, multiplicity in spectrum.items():
            l_spectrum[Fraction(1)-Fraction(root, 60)] += multiplicity
    require(sum(l_spectrum.values()) == 3840 and l_spectrum[Fraction(0)] == 1 and
            l_spectrum[Fraction(2, 5)] == 10, "unique ground and LR gap two-fifths")
    nonzero = [value for value in l_spectrum if value]
    require(min(nonzero) == Fraction(2, 5), "exact LR spectral gap")
    numerators_over_30 = [value.numerator*(30//value.denominator) for value in l_spectrum]
    require(reduce(math.gcd, numerators_over_30) == 1, "LR spectrum has primitive denominator thirty")
    revival_parameter = "60*pi"

    # Since HE has eigenvalues 0,2 and commutes with LR, the ten LR-gap modes
    # in ker HE prove both the lower bound and attainment for every J>=0.
    require(all(root <= 36 for q, split in enumerate(joint_multiplicities)
                for root in split[0] if not (q == 2 and root == 60)),
            "all non-ground HE-zero modes have LR energy at least two-fifths")
    require(all(Fraction(1)-Fraction(root, 60) >= Fraction(2, 5)
                for split in joint_multiplicities for root in split[1]),
            "all HE-range modes already have LR energy at least two-fifths")

    result = {
        "research_id": "UR.COMPILER.ROOT_SOURCE_AUDIT.17-INDEPENDENT",
        "verdict": "EXACT_FINITE_PASS_WITH_PHYSICAL_SELECTION_OPEN",
        "source_sha256": SOURCE_SHA,
        "submission_sha256": SUBMISSION_SHA,
        "phase_faithful_group_order": 46080,
        "class_polynomial_degree": len(universal_roots),
        "class_sum_integer_roots": universal_roots,
        "class_polynomial_exact_certificate": {
            "crt_primes": primes,
            "crt_product_bits": modulus_product.bit_length(),
            "coefficient_word_bound_bits": coefficient_bound.bit_length(),
            "lift_is_exact": modulus_product > 2*coefficient_bound,
        },
        "A_phase_spectra": [
            {str(Fraction(root, 60)): multiplicity for root, multiplicity in spectrum.items()}
            for spectrum in phase_multiplicities
        ],
        "source_fourier_convention": "|ell;q>=(1/2) sum_k i^(kq)|i^k z_ell>; fixed-ray phase contributes phase^(-q)",
        "LR_full_spectrum": {str(value): multiplicity for value, multiplicity in sorted(l_spectrum.items())},
        "HE_LR_joint_spectra": [
            {
                "HE=0": {str(Fraction(root, 60)): multiplicity for root, multiplicity in split[0].items()},
                "HE=2": {str(Fraction(root, 60)): multiplicity for root, multiplicity in split[1].items()},
            }
            for split in joint_multiplicities
        ],
        "ground": "unique; phase sector2, HE=0, A=1",
        "gap_for_all_J_nonnegative": "2*kappa/5",
        "gap_multiplicity": 10,
        "gap_modes": "phase sector2, HE=0, A=3/5",
        "reduced_AB": "P_sym/10",
        "single_register_reduction": "I4/4",
        "Schmidt_weights_source_vs_AB": "1/10 with multiplicity10",
        "minimal_positive_LR_revival_parameter": revival_parameter,
        "old_event_exact_revival_condition": "for J>0, t*=pi/(2J) and kappa/J=120*n; minimal positive ratio120",
        "artifact_availability": "submitted chatgpt-content-reference artifacts were not locally available; this is an independent reconstruction",
        "scope": "specified finite 240x4x4 Hilbert space only; no preparation, locality, graph, continuum, physical time, coupling ratio, or TOE selection",
        "checks": len(checks),
    }
    (HERE/"spectrum_certificate.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({key: result[key] for key in
          ("verdict", "phase_faithful_group_order", "ground", "gap_for_all_J_nonnegative",
           "minimal_positive_LR_revival_parameter", "old_event_exact_revival_condition", "checks")}, indent=2))


if __name__ == "__main__":
    main()
