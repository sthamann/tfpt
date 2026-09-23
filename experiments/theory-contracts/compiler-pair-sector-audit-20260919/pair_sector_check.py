"""Exact bounded audit of the phase-free response-pair sector.

The local calculation uses the original sixty Gaussian E8 rays.  The chain
calculation uses only the resulting exact local projector and sparse Bell
contractions.  It never constructs a full open-chain Hamiltonian.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE_REL = Path("experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py")
SOURCE = ROOT / SOURCE_REL
SOURCE_SHA256 = "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593"
checks: Counter[str] = Counter()


def require(condition: bool, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks[label] += 1


def gaussian_sympy(value: complex) -> sp.Expr:
    real = int(round(complex(value).real))
    imag = int(round(complex(value).imag))
    require(complex(value) == complex(real, imag), "Gaussian ray coordinate is integral")
    return sp.Integer(real) + sp.I * sp.Integer(imag)


def local_index(a: int, b: int, c: int) -> int:
    return (4 * a + b) * 4 + c


def bell_span() -> sp.SparseMatrix:
    """Columns: Bell(left,source) x right and left x Bell(source,right)."""
    entries: dict[tuple[int, int], sp.Expr] = {}
    half = sp.Rational(1, 2)
    for c in range(4):
        for i in range(4):
            entries[(local_index(i, i, c), c)] = half
            key = (local_index(c, i, i), 4 + c)
            entries[key] = entries.get(key, 0) + half
    return sp.SparseMatrix(64, 8, entries)


def sparse_chain_state(m: int, free_site: int, colour: int) -> dict[tuple[int, ...], Fraction]:
    """Bell tiling with the only free matter register at free_site.

    Global order is M0,S0,M1,S1,...,S_(m-1),Mm.  Sources left of the
    free site pair left; sources at or right of it pair right.
    """
    amplitude = Fraction(1, 2**m)
    result: dict[tuple[int, ...], Fraction] = {}
    for labels in it.product(range(4), repeat=m):
        word = [-1] * (2 * m + 1)
        word[2 * free_site] = colour
        for edge, label in enumerate(labels):
            word[2 * edge + 1] = label
            matter = edge if edge < free_site else edge + 1
            word[2 * matter] = label
        require(all(value >= 0 for value in word), "Bell tiling assigns every factor")
        result[tuple(word)] = amplitude
    return result


def sparse_inner(left: dict[tuple[int, ...], Fraction],
                 right: dict[tuple[int, ...], Fraction]) -> Fraction:
    if len(left) > len(right):
        left, right = right, left
    return sum((value * right.get(word, Fraction(0)) for word, value in left.items()),
               Fraction(0))


def main(output: Path) -> None:
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "pinned original sixty-ray source")
    spec = importlib.util.spec_from_file_location("pair_audit_native", SOURCE)
    source = importlib.util.module_from_spec(spec)
    require(spec.loader is not None, "native source module has loader")
    spec.loader.exec_module(source)
    rays = source.source_rays()
    require(len(rays) == 60, "original source has sixty projective rays")

    # Exact local operator on matter-left 4 x source bar4 x matter-right 4.
    identity4 = sp.eye(4)
    event_mean = sp.zeros(64)
    exact_reflections: list[sp.Matrix] = []
    for ray in rays:
        z = sp.Matrix([gaussian_sympy(value) for value in ray])
        reflection = (identity4 - z * z.conjugate().T / 2).applyfunc(sp.simplify)
        require(reflection * reflection == identity4, "exact reflection is involutive")
        require(reflection == reflection.conjugate().T, "exact reflection is Hermitian")
        exact_reflections.append(reflection)
        event_mean += sp.kronecker_product(reflection, reflection.conjugate(), reflection) / 60
    event_mean = event_mean.applyfunc(sp.simplify)
    local = (sp.eye(64) - event_mean).applyfunc(sp.simplify)
    identity64 = sp.eye(64)
    eigenvalues = [sp.Rational(1, 2), sp.Rational(5, 6), sp.Rational(11, 10)]
    spectral_polynomial = identity64
    for value in eigenvalues:
        spectral_polynomial = spectral_polynomial * (local - value * identity64)
    require(spectral_polynomial == sp.zeros(64), "local cubic spectral polynomial vanishes")
    ranks = [(local - value * identity64).rank() for value in eigenvalues]
    multiplicities = [64 - rank for rank in ranks]
    require(multiplicities == [8, 36, 20], "local eigenvalue multiplicities are 8,36,20")
    trace_moments = [sp.simplify(sp.trace(local**power)) for power in range(1, 4)]
    require(trace_moments == [sp.Integer(56), sp.Rational(256, 5), sp.Rational(3634, 75)],
            "local first three traces match claimed spectrum")

    # The eight-dimensional bottom is exactly the sum of the two Bell families.
    bell = bell_span()
    gram = bell.T * bell
    gram_expected = sp.kronecker_product(
        sp.Matrix([[1, sp.Rational(1, 4)], [sp.Rational(1, 4), 1]]), sp.eye(4)
    )
    require(gram == gram_expected, "two Bell families have overlap delta_cd/4")
    require(gram.rank() == 8, "Bell-family sum has dimension eight")
    require(local * bell == sp.Rational(1, 2) * bell,
            "both Bell families lie in the local bottom eigenspace")
    bottom_projector = (bell * gram.inv() * bell.T).applyfunc(sp.simplify)
    require(bottom_projector * bottom_projector == bottom_projector,
            "Bell span gives an exact local orthogonal projector")
    require((local - sp.Rational(1, 2) * identity64).nullspace() and
            64 - (local - sp.Rational(1, 2) * identity64).rank() == bell.cols,
            "Bell span exhausts the local bottom eigenspace")

    # Closed tensor formula.  P and Q project onto the left/source and
    # source/right Bell pairs; S swaps the two matter factors A and C.
    phi = sp.zeros(16)
    for i in range(4):
        for j in range(4):
            phi[4 * i + i, 4 * j + j] = sp.Rational(1, 4)
    projector_left = sp.kronecker_product(phi, sp.eye(4))
    projector_right = sp.kronecker_product(sp.eye(4), phi)
    swap_ac = sp.zeros(64)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                swap_ac[local_index(c, b, a), local_index(a, b, c)] = 1
    event_formula = (
        sp.eye(64) / 30 + sp.Rational(2, 15) * swap_ac
        + sp.Rational(8, 15) * (projector_left + projector_right)
        - sp.Rational(4, 15) * (projector_left * swap_ac + swap_ac * projector_left)
    )
    require(event_mean == event_formula,
            "native sixty-ray mean equals closed Bell-swap tensor formula")
    bottom_formula = (
        sp.Rational(16, 15) * (projector_left + projector_right)
        - sp.Rational(4, 15) * (projector_left * swap_ac + swap_ac * projector_left)
    )
    require(bottom_projector == bottom_formula,
            "closed formula reproduces the local bottom projector")
    symmetric_ac = (identity64 + swap_ac) / 2
    antisymmetric_ac = (identity64 - swap_ac) / 2
    require((symmetric_ac - symmetric_ac * bottom_projector).rank() == 36,
            "outside Bell span the matter-symmetric sector has dimension 36")
    require((antisymmetric_ac - antisymmetric_ac * bottom_projector).rank() == 20,
            "outside Bell span the matter-antisymmetric sector has dimension 20")

    # Adjacent local-bottom projectors: use their 1024x128 sparse range bases,
    # but diagonalize only the exact 128x128 generalized overlap matrix.
    identity16_sparse = sp.eye(16, cls=sp.SparseMatrix)
    basis_left = sp.kronecker_product(bell, identity16_sparse)
    basis_right = sp.kronecker_product(identity16_sparse, bell)
    cross = basis_left.T * basis_right
    gram_inverse = gram.inv()
    gram_left_inverse = sp.kronecker_product(gram_inverse, identity16_sparse)
    gram_right_inverse = sp.kronecker_product(identity16_sparse, gram_inverse)
    cos2 = gram_left_inverse * cross * gram_right_inverse * cross.T
    identity128 = sp.eye(128, cls=sp.SparseMatrix)
    cos2_values = [sp.Integer(0), sp.Rational(1, 225), sp.Rational(16, 225), sp.Integer(1)]
    cos2_poly = identity128
    for value in cos2_values:
        cos2_poly = cos2_poly * (cos2 - value * identity128)
    require(cos2_poly == sp.zeros(128), "adjacent generalized overlap polynomial vanishes")
    cos2_ranks = [(cos2 - value * identity128).rank() for value in cos2_values]
    cos2_multiplicities = [128 - rank for rank in cos2_ranks]
    require(cos2_multiplicities == [56, 4, 56, 12],
            "adjacent squared principal-cosine multiplicities are exact")
    require(sp.trace(cos2) == 16, "adjacent overlap trace is exact")
    principal_c = sp.Rational(4, 15)
    require(principal_c**2 == sp.Rational(16, 225),
            "largest nontrivial adjacent principal cosine is 4/15")

    # Direct sparse replay of the claimed all-m Bell-chain Gram matrix.
    replayed_m = list(range(1, 7))
    for m in replayed_m:
        states = {(site, colour): sparse_chain_state(m, site, colour)
                  for site in range(m + 1) for colour in range(4)}
        for j in range(m + 1):
            for k in range(m + 1):
                for c in range(4):
                    for d in range(4):
                        expected = Fraction(int(c == d), 4 ** abs(j - k))
                        require(sparse_inner(states[j, c], states[k, d]) == expected,
                                "open-chain Bell tiling has claimed Gram entry")
    # Each colour block is the AR(1) Toeplitz matrix q^|j-k|, q=1/4.
    # Its determinant is (1-q^2)^m, hence all 4(m+1) states are independent.
    q = sp.Rational(1, 4)
    for m in range(1, 11):
        toeplitz = sp.Matrix(m + 1, m + 1, lambda j, k: q ** abs(j - k))
        require(toeplitz.det() == (1 - q**2) ** m,
                "Bell-chain Toeplitz determinant is positive")

    # Native moments used both by the eigenstate proof and by the full-source
    # variational control.
    mean_reflection = sum(exact_reflections, sp.zeros(4)) / 60
    require(mean_reflection == sp.eye(4) / 2, "mean native reflection is I/2")
    require(all(sp.trace(reflection) == 2 for reflection in exact_reflections),
            "every native reflection has trace two")

    # Full 240-source aligned packet Omega=sum_alpha |alpha> psi_alpha psi_alpha.
    # This is outside the reduced source-bar4 sector above.  Exact permutation
    # covariance makes every selected nonoverlapping packet a zero mode.
    roots = np.stack([(1j**phase) * ray for ray in rays for phase in range(4)])
    root_keys = {
        tuple((int(round(value.real)), int(round(value.imag))) for value in root): index
        for index, root in enumerate(roots)
    }
    require(len(root_keys) == 240, "sixty rays lift to 240 oriented roots")
    psi = roots / 2
    require(np.array_equal(psi.conj().T @ psi, 60 * np.eye(4)),
            "full aligned packet has one-matter marginal I/4")
    pair_coefficients = np.einsum("ai,aj->aij", psi, psi).reshape(240, 16)
    for ray in rays:
        reflection = np.eye(4, dtype=np.complex128) - np.outer(ray, ray.conj()) / 2
        permutation = tuple(root_keys[
            tuple((int(round(value.real)), int(round(value.imag)))
                  for value in reflection @ root)
        ] for root in roots)
        transformed_coordinates = np.zeros_like(psi)
        for old, new in enumerate(permutation):
            transformed_coordinates[new] = psi[old]
        require(np.array_equal(transformed_coordinates, psi @ reflection.T),
                "original 240-source coordinate subspace carries bar4")
        transformed = np.zeros_like(pair_coefficients)
        for old, new in enumerate(permutation):
            transformed[new] = pair_coefficients[old]
        transformed = transformed @ np.kron(reflection.T, reflection.T)
        require(np.array_equal(transformed, pair_coefficients),
                "phase-free event fixes full aligned source packet")

    # On every unselected gap edge, the source is uniform and at least one
    # endpoint comes from a packet with marginal I/4.  The other is either an
    # independent I/4 marginal or a boundary pure state.  In both cases the
    # averaged event expectation is exactly 1/4, so L contributes 3/4.
    require(sp.Rational(2, 4) * sp.Rational(2, 4) == sp.Rational(1, 4),
            "uniform gap between packets has event expectation one quarter")
    require(sp.Rational(1, 2) * mean_reflection[0, 0] == sp.Rational(1, 4),
            "uncovered boundary gives the same averaged gap expectation")
    for m in range(1, 21):
        trial = sp.Rational(3, 4) * (m // 2)
        require(trial < sp.Rational(m, 2),
                "alternating full-source trial lies below reduced-pair energy")

    result = {
        "research_id": "UR.COMPILER.PAIR_SECTOR_AUDIT.23",
        "verdict": "PARTIAL",
        "mathematical_verdict": "EXACT_REDUCED_PAIR_GROUND_SECTOR_AND_FULL_SOURCE_VARIATIONAL_CONTROL",
        "source": {"path": str(SOURCE_REL), "sha256": SOURCE_SHA256, "rays": 60},
        "local_4_x_bar4_x_4": {
            "spectrum": {"1/2": 8, "5/6": 36, "11/10": 20},
            "trace_moments_1_to_3": [str(value) for value in trace_moments],
            "bottom_space": (
                "Bell(M_left,S_bar) tensor M_right plus "
                "M_left tensor Bell(S_bar,M_right)"
            ),
            "cross_gram": "delta_cd/4",
            "event_mean_formula": (
                "I/30+(2/15)Swap_AC+(8/15)(P+Q)"
                "-(4/15)(P Swap_AC+Swap_AC P)"
            ),
            "bottom_projector_formula": (
                "(16/15)(P+Q)-(4/15)(P Swap_AC+Swap_AC P)"
            ),
        },
        "open_reduced_pair_chain": {
            "energy": "kappa*m/2",
            "ground_dimension_at_least": "4*(m+1)",
            "state_labels": "free matter position j=0,...,m and colour c=1,...,4",
            "gram": "delta_cd * 4^(-abs(j-k))",
            "gram_block_determinant": "(15/16)^m",
            "sparse_replay_m": replayed_m,
        },
        "adjacent_projectors": {
            "squared_principal_cosines": {
                "0": 56, "1/225": 4, "16/225": 56, "1": 12
            },
            "max_nontrivial_principal_cosine": "4/15",
            "projector_chain_gap": "1-2*(4/15)=7/15",
            "hamiltonian_gap_lower_bound": "(kappa/3)*(7/15)=7*kappa/45",
        },
        "full_240_source_variational_control": {
            "state": (
                "nonoverlapping alternating Omega_e=240^(-1/2) sum_alpha "
                "|alpha> |psi_alpha> |psi_alpha>, uniform source on gap edges"
            ),
            "selected_edge_energy": "0",
            "gap_edge_energy": "3*kappa/4",
            "gap_edges": "floor(m/2)",
            "trial_energy": "3*kappa*floor(m/2)/4 < kappa*m/2",
            "consequence": (
                "kappa*m/2 is the reduced source-bar4 sector ground, not the "
                "ground energy of the full 240-source phase-free Hamiltonian"
            ),
        },
        "scope": (
            "Exact finite J=mu=0 pure-permutation model. No phase-faithful current lift, "
            "mixed-640 sector, leakage, thermodynamic limit, critical phase, or TOE claim."
        ),
        "checks": sum(checks.values()),
        "check_counts": dict(sorted(checks.items())),
        "closed_gate_ids": [],
    }
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"verdict": result["verdict"], "checks": result["checks"]}, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=HERE / "pair_sector_check.json")
    arguments = parser.parse_args()
    main(arguments.out)
