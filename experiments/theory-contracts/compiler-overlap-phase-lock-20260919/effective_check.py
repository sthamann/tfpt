"""Exact audit of the reported two-source strong-lock overlap operator.

The finite claims are rebuilt from the pinned native 240 Gaussian E8 roots.
The perturbative derivation is conditional on the explicitly stated lock and
two averaged packet-event operators; no physical choice of that Hamiltonian is
inferred from the E8 root system alone.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import itertools as it
import json
from math import prod
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SOURCE = ROOT / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py"
SOURCE_SHA256 = "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593"
SPECTRUM_SOURCE = ROOT / "experiments/theory-contracts/compiler-root-source-backreaction-20260919/spectrum_check.py"
SPECTRUM_SHA256 = "c5bee13c426dec55d5d5a93f753cdbd7dd3947e22cf476451264907668e0db07"
check_counts: Counter[str] = Counter()


def require(ok, name: str) -> None:
    if not bool(ok):
        raise RuntimeError(name)
    check_counts[name] += 1


def key(z: np.ndarray) -> tuple[tuple[int, int], ...]:
    require(np.array_equal(z.real, np.rint(z.real)) and
            np.array_equal(z.imag, np.rint(z.imag)),
            "Gaussian root has exact integer coordinates")
    return tuple((int(round(x.real)), int(round(x.imag))) for x in z)


def polynomial_coefficients(roots: list[int]) -> list[int]:
    coefficients = [1]
    for root in roots:
        new = [0]*(len(coefficients)+1)
        for degree, value in enumerate(coefficients):
            new[degree] -= root*value
            new[degree+1] += value
        coefficients = new
    return coefficients


def modular_solve(a: list[list[int]], b: list[int], prime: int) -> list[int]:
    augmented = [[int(x) % prime for x in row] + [int(y) % prime]
                 for row, y in zip(a, b)]
    n = len(augmented)
    for column in range(n):
        pivot = next(row for row in range(column, n) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        inverse = pow(augmented[column][column], -1, prime)
        augmented[column] = [(x*inverse) % prime for x in augmented[column]]
        for row in range(n):
            if row != column and augmented[row][column]:
                factor = augmented[row][column]
                augmented[row] = [(x-factor*y) % prime
                                  for x, y in zip(augmented[row], augmented[column])]
    return [augmented[k][-1] for k in range(n)]


def main() -> None:
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "pinned native source")
    require(hashlib.sha256(SPECTRUM_SOURCE.read_bytes()).hexdigest() == SPECTRUM_SHA256,
            "pinned prior 240-root spectrum source")
    spec = importlib.util.spec_from_file_location("new_overlap_native_source", SOURCE)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)

    rays = source.source_rays()
    require(len(rays) == 60, "sixty native Gaussian rays")
    roots = np.stack([(1j**phase)*z for z in rays for phase in range(4)])
    root_index = {key(z): index for index, z in enumerate(roots)}
    require(len(root_index) == 240, "full oriented 240-root system")
    gram = roots.conj()@roots.T
    require(np.array_equal(gram.real, np.rint(gram.real)) and
            np.array_equal(gram.imag, np.rint(gram.imag)),
            "exact Gaussian root Gram matrix")
    gram_real = np.rint(gram.real).astype(np.int64)
    gram_imag = np.rint(gram.imag).astype(np.int64)
    require(np.array_equal(np.diag(gram_real), 4*np.ones(240, dtype=np.int64)) and
            not np.any(np.diag(gram_imag)), "all psi_alpha=z_alpha/2 are normalized")

    # A32 records the exact complex overlap <psi_alpha,psi_beta>=1/2.
    adjacency = ((gram_real == 2) & (gram_imag == 0)).astype(np.int64)
    antipode = ((gram_real == -4) & (gram_imag == 0)).astype(np.int64)
    require(np.array_equal(adjacency, adjacency.T) and not np.any(np.diag(adjacency)),
            "A32 is a simple symmetric graph")
    require(np.array_equal(adjacency.sum(axis=1), 32*np.ones(240, dtype=np.int64)),
            "A32 is exactly regular of degree 32")
    require(np.array_equal(antipode, antipode.T) and
            np.array_equal(antipode.sum(axis=1), np.ones(240, dtype=np.int64)) and
            not np.any(np.diag(antipode)) and
            np.array_equal(antipode@antipode, np.eye(240, dtype=np.int64)),
            "F is the fixed-point-free antipodal involution")
    for alpha, z in enumerate(roots):
        require(np.array_equal(antipode[alpha],
                               np.eye(240, dtype=np.int64)[root_index[key(-z)]]),
                "F maps each oriented root to its negative")
    require(np.array_equal(adjacency@antipode, antipode@adjacency),
            "A32 commutes exactly with F")

    # Rebuild all native reflections and their action on the oriented roots.
    reflections = [np.eye(4)-np.outer(z, z.conj())/2 for z in rays]
    transitions = np.empty((60, 240), dtype=np.int64)
    for m, reflection in enumerate(reflections):
        require(np.array_equal(reflection.conj().T, reflection) and
                np.array_equal(reflection@reflection, np.eye(4)) and
                np.trace(reflection) == 2,
                "native event is exact rank-one reflection")
        for alpha, z in enumerate(roots):
            transitions[m, alpha] = root_index[key(reflection@z)]
        require(len(set(map(int, transitions[m]))) == 240,
                "native reflection permutes all oriented roots")

    transition_counts = np.zeros((240, 240), dtype=np.int64)
    for alpha in range(240):
        for beta in transitions[:, alpha]:
            transition_counts[alpha, beta] += 1
    reached_orthogonal = (transition_counts -
                          15*np.eye(240, dtype=np.int64) - adjacency - antipode)
    require(np.all((reached_orthogonal == 0) | (reached_orthogonal == 1)) and
            np.array_equal(reached_orthogonal.sum(axis=1),
                           12*np.ones(240, dtype=np.int64)) and
            not np.any(reached_orthogonal*((gram_real != 0) | (gram_imag != 0))),
            "remaining twelve reached targets per root are exactly orthogonal")
    require(np.array_equal(transition_counts,
                           15*np.eye(240, dtype=np.int64) + adjacency +
                           reached_orthogonal + antipode),
            "transition relation splits as fixed, A32, reached-orthogonal and antipodal")
    require(np.array_equal(np.count_nonzero(transition_counts, axis=1),
                           46*np.ones(240, dtype=np.int64)),
            "every nonfixed target is reached by a unique native reflection")

    # Conditional second-order derivation.  Low basis vectors are
    # e_alpha=|alpha,alpha>_sources tensor |psi_alpha>_A|psi_alpha>_B|psi_alpha>_C.
    # The source lock assigns a one-mismatch intermediate energy
    # V(alpha,beta)=1-Re<psi_alpha,psi_beta>.
    # Two uses on the same packet return to e_alpha with amplitude 1.  The two
    # cross-packet orders land at e_beta with middle-register projection
    # <psi_beta,psi_alpha>.  Fixed events remain in P and give only a scalar
    # first-order term; all nonfixed images are unique as checked above.
    second_order_numerator = np.zeros((240, 240), dtype=np.int64)
    diagonal_self_energy = []
    transition_profile: Counter[str] = Counter()
    for alpha in range(240):
        diagonal = Fraction(0)
        cross: Counter[int] = Counter()
        fixed = 0
        for beta in transitions[:, alpha]:
            if beta == alpha:
                fixed += 1
                continue
            re = int(gram_real[alpha, beta])
            im = int(gram_imag[alpha, beta])
            require(im == 0 and re in (2, 0, -4),
                    "virtual reflection overlap is real half, zero or minus one")
            # V=(4-re)/4.  There are two same-side choices (left-left and
            # right-right), and two cross orders (left-right and right-left).
            diagonal += Fraction(8, 4-re)       # 2/V
            cross[int(beta)] += Fraction(2*re, 4-re)  # 2*<psi_a,psi_b>/V
            transition_profile[{2: "half", 0: "zero", -4: "antipode"}[re]] += 1
        require(fixed == 15, "fifteen fixed events per root and packet")
        require(diagonal == 153, "exact two-packet diagonal virtual self-energy 153")
        diagonal_self_energy.append(diagonal)
        second_order_numerator[alpha, alpha] = int(diagonal)
        for beta, value in cross.items():
            require(value.denominator == 1, "cross-packet virtual amplitude is integral")
            second_order_numerator[alpha, beta] = value.numerator

    matrix_m = 153*np.eye(240, dtype=np.int64) + 2*adjacency - antipode
    require(np.array_equal(second_order_numerator, matrix_m),
            "paired-reflection derivation gives M=153I+2A32-F")
    require(Fraction(2*15, 60) == Fraction(1, 2),
            "naked-permutation projected first-order event average is scalar one-half")

    # Exact spectrum without a large numerical eigensolve.  Verify the claimed
    # degree-eight annihilating polynomial modulo enough primes for a CRT lift;
    # the product exceeds twice a deterministic infinity-norm coefficient bound.
    eigenvalues = [136, 144, 146, 152, 162, 168, 186, 216]
    coefficients = polynomial_coefficients(eigenvalues)
    row_norm_bound = int(np.max(np.sum(np.abs(matrix_m), axis=1)))
    require(row_norm_bound == 218, "exact M infinity-norm bound 218")
    coefficient_bound = sum(abs(c)*row_norm_bound**degree
                            for degree, c in enumerate(coefficients))
    primes = [1000003, 1000033, 1000037, 1000039]
    require(all(sp.isprime(prime) for prime in primes), "CRT moduli are prime")
    for prime in primes:
        reduced = matrix_m % prime
        value = np.eye(240, dtype=np.int64)
        # Horner evaluation of the monic polynomial, high degree to constant.
        for coefficient in reversed(coefficients[:-1]):
            value = (value@reduced) % prime
            value[np.diag_indices(240)] = (value[np.diag_indices(240)] + coefficient) % prime
        require(not np.any(value), f"M spectral polynomial vanishes modulo {prime}")
    require(prod(primes) > 2*coefficient_bound,
            "CRT lift proves exact integer spectral polynomial")

    # Recover exact multiplicities from modular trace moments.  Since every
    # multiplicity is in [0,240] and prime>240, its residue is unique.
    prime = primes[0]
    reduced = matrix_m % prime
    power = np.eye(240, dtype=np.int64)
    moments = []
    for degree in range(len(eigenvalues)):
        moments.append(int(np.trace(power) % prime))
        power = (power@reduced) % prime
    vandermonde = [[pow(root, degree, prime) for root in eigenvalues]
                   for degree in range(len(eigenvalues))]
    multiplicities = modular_solve(vandermonde, moments, prime)
    require(all(0 <= value <= 240 for value in multiplicities) and
            sum(multiplicities) == 240,
            "unique exact spectral multiplicities")
    spectrum = dict(zip(eigenvalues, multiplicities))
    expected_spectrum = {136: 9, 144: 40, 146: 72, 152: 45,
                         162: 40, 168: 25, 186: 8, 216: 1}
    require(spectrum == expected_spectrum, "exact reported M spectrum")
    require(np.array_equal(matrix_m@np.ones(240, dtype=np.int64),
                           216*np.ones(240, dtype=np.int64)),
            "uniform aligned vector is the simple top eigenvector")

    # Standard real E8 normalization: X=(Re z,Im z)/sqrt(2), so every row has
    # norm squared two.  Work with the integral Y=sqrt(2)X.  Consequently
    # Y^T Y=120I in the native norm-four convention.  If one separately
    # rescales to norm-two roots X=Y/sqrt(2), then X^T X=60I.
    real_roots = np.concatenate((roots.real, roots.imag), axis=1).astype(np.int64)
    require(np.array_equal(real_roots@real_roots.T, gram_real),
            "realification reproduces real Hermitian overlaps")
    require(np.array_equal(real_roots.T@real_roots, 120*np.eye(8, dtype=np.int64)),
            "integral norm-four real roots have Y^T Y=120I")
    require(np.array_equal(matrix_m@real_roots, 186*real_roots),
            "all eight normalized E8 coordinates form the 186 eigenspace")

    # Exact third moment.  For psi=z/2, the density denominator is
    # 240*2^6=15360.  P_sym3/20=(sum_{pi in S3} U_pi)/120, hence it is enough
    # to prove sum z^tensor3 z^tensor3*=128 sum U_pi.
    triples = list(it.product(range(4), repeat=3))
    permutation_sum = np.zeros((64, 64), dtype=np.int64)
    for permutation in it.permutations(range(3)):
        for column, word in enumerate(triples):
            row_word = tuple(word[permutation[k]] for k in range(3))
            permutation_sum[triples.index(row_word), column] += 1
    third_moment = np.zeros((64, 64), dtype=complex)
    for z in roots:
        cube = np.kron(np.kron(z, z), z)
        third_moment += np.outer(cube, cube.conj())
    require(np.array_equal(third_moment.real, np.rint(third_moment.real)) and
            np.array_equal(third_moment.imag, np.rint(third_moment.imag)),
            "third root moment has exact Gaussian-integer entries")
    third_moment_integer = (np.rint(third_moment.real).astype(np.int64) +
                            1j*np.rint(third_moment.imag).astype(np.int64))
    require(np.array_equal(third_moment_integer, 128*permutation_sum),
            "rho_ABC equals P_sym3 divided by 20")

    result = {
        "research_id": "UR.COMPILER.NEW_OVERLAP.EFFECTIVE_CHECK.20260919",
        "verdict": "EXACT_CONDITIONAL_SECOND_ORDER_RESULT",
        "root_count": 240,
        "source_model": (
            "two oriented-root sources with low basis |alpha,alpha> tensor "
            "|psi_alpha>_A|psi_alpha>_B|psi_alpha>_C, one-source mismatch "
            "energy V=1-Re<psi_alpha,psi_beta>, and two native 60-event packet averages"
        ),
        "naked_permutation_first_order_projected_scalar": "1/2",
        "second_order_kernel": "D=(153 I + 2 A32 - F)/3600",
        "schrieffer_wolff_sign": (
            "For a positive lock Hamiltonian and perturbation epsilon W, the energy "
            "correction is -epsilon^2 D; D is the positive splitting kernel whose top "
            "eigenvector is selected at second order only if the first-order restriction "
            "remains scalar."
        ),
        "signed_lift_separation": (
            "D is unchanged for identical involutive sign lifts on both packet edges: "
            "same-side return phases multiply to 1 and cross-edge phases square to 1. "
            "The first-order PWP term need not remain scalar under such a lift, so D then "
            "need not be the leading selector. The signed first-order spectrum is not "
            "recomputed in this checker."
        ),
        "transition_counts_per_root": {
            "fixed": 15, "overlap_plus_one_half": 32,
            "overlap_zero": 12, "antipode": 1,
        },
        "A32_degree": 32,
        "F_commutes_with_A32": True,
        "M_spectrum": {str(value): multiplicity
                       for value, multiplicity in sorted(spectrum.items(), reverse=True)},
        "D_spectrum": {f"{value}/3600": multiplicity
                       for value, multiplicity in sorted(spectrum.items(), reverse=True)},
        "top_level": {"M_eigenvalue": 216, "multiplicity": 1,
                      "vector": "uniform coherent sum of the 240 aligned low-basis vectors"},
        "next_level": {"M_eigenvalue": 186, "multiplicity": 8,
                       "eigenspace": "eight normalized real E8 coordinate columns"},
        "real_root_frame_normalization": (
            "For the actual native matrix X_native=(Re z,Im z), row norm^2=4, "
            "X_native^T X_native=120 I8 and M X_native=186 X_native, exactly as reported. "
            "If one separately uses norm-two roots X=X_native/sqrt(2), then X^T X=60 I8."
        ),
        "native_third_moment": "rho_ABC=(1/240) sum_alpha |psi_alpha^3><psi_alpha^3|=P_sym3/20",
        "provenance_boundary": (
            "No URL or external checker package for the new report was supplied. "
            "All finite equalities were independently rebuilt from the pinned native source."
        ),
        "scope_boundary": (
            "Second-order strong-lock effective operator in the specified 240-dimensional "
            "aligned manifold only; no finite-lock all-orders spectrum, preparation, locality, "
            "continuum dynamics, or TOE selection is established."
        ),
        "source_sha256": {
            str(SOURCE.relative_to(ROOT)): SOURCE_SHA256,
            str(SPECTRUM_SOURCE.relative_to(ROOT)): SPECTRUM_SHA256,
        },
        "spectral_polynomial_coefficients_low_to_high": coefficients,
        "spectral_CRT_bound": coefficient_bound,
        "spectral_CRT_modulus": prod(primes),
        "check_evaluations": sum(check_counts.values()),
        "checks": dict(sorted(check_counts.items())),
    }
    (HERE / "effective_check.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: value for key, value in result.items() if key != "checks"}, indent=2))


if __name__ == "__main__":
    main()
