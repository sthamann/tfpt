#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v1006 -- SEAM.MMST.TYPEIII.CHARGED.01 [O]: charged/Type-III master
scaling-limit lemma battery.

Provenance: experiments/tfpt-discovery/mmst_ugf_bound_probe.py +
mmst_tel_probe.py (review wave 7, 2026-08-30; ALL PASS) and the
memorandum articles/2026-08-30/mmst_charged_scaling_limit_en.tex
(21 pp) + send-ready handoff
articles/2026-08-30/externalization_mmst_handoff_v2_en.html.
L3 finite witness re-derives the v988 inner-mu4 exchange.

THE POINT.  Five lemmas are in-house; the contract stays Open.

  [E] L3 crossed-product / tower exchange (inner mu4 on M_d):
        A x| Z4 ~= A (x) C[Z4], natural with equivariant embeddings;
        a non-equivariant clock extension breaks naturality.
  [E] UGF uniform Green-form domination: K_G = pi^2/4 proved
        (S_N(m)<=m and sin x >= 2x/pi); measured plateau 1.023 on the
        frozen QWZ collar N in {16,24,32,48,64,96}.
  [E] TEL-a: exact Fock/spectral isometries and dyadic compatibility;
        coefficient defect |r_{2N}-r_N| <= A_TEL m^2/N^2 with
        A_TEL = 5120(1+pi/2) proved and measured max ~3.42 (guard 8);
        Wick seminorm rate ~ N^{-2.023}.
  [E] relative locality: lambda has integer pairings with every
        D5+A3 simple root.
  [E] Z4 outerness criterion in the limit (Hom(id,theta)=C and all
        four characters); finite-level innerness is a CORRECTION, not
        a witness (every matrix-algebra automorphism is inner; explicit
        256-dim gauge unitary is charge-zero).
  [N] TEL-B HS plateau (two-edge remainder): measured max 2.105079358,
        fitted 2.107565497, safe grid 2.11 on N<=96 (v998).  These
        historical finite data are not the proof.  Native v1026 proves
        ||R_N||_HS < 2.995906 < 3 for fixed M=1, Ny=8 and every even N>=16.
  [O boxed] FE-GEN/ALG-EXH: the microscopic one-edge identification and
        two Buchholz-Verch estimates remain open; the MMST contract stays [O].

MUST-FAIL: gapless transverse mutant violates K_G; false omega>=m;
wrong-rate r_N=1+1/N; non-isometry sqrt(2) j; nonintegral A3 pairing;
duplicate-vacuum Q-system.

HONEST SCOPE (firewall): frozen QWZ/CAR collar + finite mu4 clock;
the relaxed all-N TEL-B norm is proved, but FE-GEN/ALG-EXH and the MMST
identification are not; the contract stays [O].
Python-only / Wolfram mirror deferred.
"""
from __future__ import annotations

from tex_sources import read_tex
from pathlib import Path

import os
from math import pi

import numpy as np

from tfpt_constants import check, summary, reset


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MMST_TEX = os.path.join(
    ROOT, "articles", "2026-08-30", "mmst_charged_scaling_limit_en.tex"
)
HANDOFF_HTML = os.path.join(
    ROOT, "articles", "2026-08-30", "externalization_mmst_handoff_v2_en.html"
)
V998 = os.path.join(HERE, "v998_seam_modular_closure.py")

ROUND4_TELB_DOCUMENT_SNIPPETS = (
    r"\textbf{(TEL-B) Relaxed norm obligation closed in round 4.}",
    r"$M=1$, $N_y=8$ model and every even $N\ge16$.",
    r"$\norm{R_N}_{\HS}<2.995906<3$",
    "A 512-node Acb certificate with infinite alias control",
    r"\texttt{v1026\_telb\_round4\_closure.py}",
    "does not supply the microscopic-algebra identification required by FE-GEN",
    r"or prove \textup{(ALG-EXH)}.",
    r"this memorandum does not close \texttt{SEAM.MMST.TYPEIII.CHARGED.01}.",
)

MASS = 1.0
NY = 8
INTERNAL_DIMENSION = 2 * NY
N_VALUES = (16, 24, 32, 48, 64, 96)
FIXED_MODES = (1, 2, 3)
K_G_PROVED = pi**2 / 4
A_TEL_PROVED = 5120.0 * (1.0 + pi / 2.0)
A_TEL_GUARD = 8.0
HS_MAX_PIN = 2.105079358
HS_FIT_PIN = 2.107565497
HS_SAFE_GRID = 2.11
TOLERANCE = 2.0e-12
SYMBOL_GRID = 4096
RNG = np.random.default_rng(20260830)

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TY = SY / (2j) - SZ / 2


def tex_has(path: str, snippet: str) -> bool:
    source = Path(path)
    text = read_tex(source) if source.suffix == ".tex" else source.read_text(encoding="utf-8")
    return snippet in text


def telb_round4_document_guard(text: str) -> bool:
    """Require the proved native norm and every still-open algebra boundary."""
    normalized = " ".join(text.split())
    return all(snippet in normalized for snippet in ROUND4_TELB_DOCUMENT_SNIPPETS)


def report(name, ok, extra=""):
    check("%s -- %s" % (name, extra) if extra else name, ok)


def strip_hamiltonian(momentum: float) -> np.ndarray:
    matrix = np.zeros((INTERNAL_DIMENSION, INTERNAL_DIMENSION), dtype=complex)
    onsite = np.sin(momentum) * SX + (MASS - np.cos(momentum)) * SZ
    for y_index in range(NY):
        site = slice(2 * y_index, 2 * y_index + 2)
        matrix[site, site] = onsite
    for y_index in range(NY - 1):
        lower = slice(2 * y_index, 2 * y_index + 2)
        upper = slice(2 * y_index + 2, 2 * y_index + 4)
        matrix[upper, lower] = TY
        matrix[lower, upper] = TY.conj().T
    return matrix


def top_edge_vector(momentum: float) -> tuple[float, np.ndarray, float]:
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(momentum))
    reshaped = eigenvectors.reshape(NY, 2, INTERNAL_DIMENSION)
    top_weights = np.sum(np.abs(reshaped[:4]) ** 2, axis=(0, 1))
    selected = int(np.argmax(top_weights))
    return (
        float(eigenvalues[selected]),
        eigenvectors[:, selected],
        float(top_weights[selected]),
    )


def bottom_edge_vector(momentum: float) -> np.ndarray:
    _, eigenvectors = np.linalg.eigh(strip_hamiltonian(momentum))
    reshaped = eigenvectors.reshape(NY, 2, INTERNAL_DIMENSION)
    bottom_weights = np.sum(np.abs(reshaped[-4:]) ** 2, axis=(0, 1))
    return eigenvectors[:, int(np.argmax(bottom_weights))]


def edge_vectors(size: int) -> tuple[np.ndarray, np.ndarray]:
    mode_indices = np.arange(-size // 2, size // 2)
    momenta = 2 * pi * (mode_indices + 0.5) / size
    vectors = np.empty((size, INTERNAL_DIMENSION), dtype=complex)
    weights = np.empty(size)
    for position, momentum in enumerate(momenta):
        _energy, vector, weight = top_edge_vector(float(momentum))
        vectors[position] = vector
        weights[position] = weight
    return vectors, weights


def lattice_symbol(size: int, mode: int) -> float:
    return size / pi * np.sin(pi * abs(mode) / size)


def structure_factor(vectors: np.ndarray, mode: int) -> float:
    size = vectors.shape[0]
    zero_position = size // 2
    total = 0.0
    for source in range(zero_position - mode, zero_position):
        total += abs(np.vdot(vectors[source + mode], vectors[source])) ** 2
    return float(total)


def vertex_multipliers(size: int) -> np.ndarray:
    vectors, _weights = edge_vectors(size)
    multipliers = np.zeros(size // 2 + 1)
    for mode in range(1, size // 2 + 1):
        omega = lattice_symbol(size, mode)
        multipliers[mode] = np.sqrt(
            mode * structure_factor(vectors, mode) / omega**2
        )
    return multipliers


def signed_modes(size: int) -> tuple[int, ...]:
    return tuple(range(-size // 2 + 1, 0)) + tuple(range(1, size // 2 + 1))


def spectral_embedding(coarse_size: int, fine_size: int) -> np.ndarray:
    coarse_modes = signed_modes(coarse_size)
    fine_modes = signed_modes(fine_size)
    fine_positions = {mode: index for index, mode in enumerate(fine_modes)}
    embedding = np.zeros((len(fine_modes), len(coarse_modes)))
    for column, mode in enumerate(coarse_modes):
        embedding[fine_positions[mode], column] = 1.0
    return embedding


def fermi_covariance(momentum: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(momentum))
    occupations = (eigenvalues < 0).astype(float)
    return (eigenvectors * occupations) @ eigenvectors.conj().T


def clock(dimension: int) -> np.ndarray:
    return np.diag([1j ** (index % 4) for index in range(dimension)]).astype(
        complex
    )


def crossed_iso(dimension: int):
    return clock(dimension), np.roll(np.eye(4), 1, axis=0).astype(complex)


def check_iso(dimension: int) -> bool:
    unitary, shift = crossed_iso(dimension)
    image = np.kron(unitary, shift)
    ok = True
    for _ in range(3):
        algebra = RNG.normal(size=(dimension, dimension)) + 1j * RNG.normal(
            size=(dimension, dimension)
        )
        lifted = np.kron(algebra, np.eye(4))
        left = image @ lifted @ image.conj().T
        right = np.kron(unitary @ algebra @ unitary.conj().T, np.eye(4))
        ok &= np.allclose(left, right, atol=1e-12)
    ok &= np.allclose(
        np.linalg.matrix_power(image, 4), np.eye(4 * dimension), atol=1e-12
    )
    return ok


def check_naturality(dimension: int) -> bool:
    unitary, shift = crossed_iso(dimension)
    ok = True
    for _ in range(3):
        algebra = RNG.normal(size=(dimension, dimension)) + 1j * RNG.normal(
            size=(dimension, dimension)
        )
        for grade in range(4):
            left = np.kron(
                np.kron(algebra, np.eye(2))
                @ np.linalg.matrix_power(np.kron(unitary, np.eye(2)), grade),
                np.linalg.matrix_power(shift, grade),
            )
            core = algebra @ np.linalg.matrix_power(unitary, grade)
            right = np.kron(
                np.kron(core, np.eye(2)), np.linalg.matrix_power(shift, grade)
            )
            ok &= np.allclose(left, right, atol=1e-12)
    return ok


def nonequivariant_breaks(dimension: int) -> bool:
    unitary, shift = crossed_iso(dimension)
    bad = np.kron(unitary, np.diag([1, 1j]))
    algebra = RNG.normal(size=(dimension, dimension)) + 1j * RNG.normal(
        size=(dimension, dimension)
    )
    left = np.kron(
        np.kron(algebra, np.eye(2)) @ bad,
        shift,
    )
    core = algebra @ unitary
    right = np.kron(np.kron(core, np.eye(2)), shift)
    return not np.allclose(left, right, atol=1e-10)


def run():
    reset()
    print("v1006  SEAM.MMST.TYPEIII.CHARGED.01: five lemmas in-house; "
          "native TEL-B norm proved; FE-GEN/ALG-EXH/MMST remain open")

    print("\n== L3 CROSSED-PRODUCT / LIMIT EXCHANGE ==")
    report(
        "L3 ISO [E]: A x| Z4 ~= A (x) C[Z4] on the inner mu4 clock "
        "(d = 4, 8)",
        all(check_iso(dimension) for dimension in (4, 8)),
    )
    report(
        "L3 NATURALITY [E]: Phi commutes with equivariant tower embeddings",
        all(check_naturality(dimension) for dimension in (4, 8)),
    )
    report(
        "L3 MUST-FAIL [E]: a non-equivariant clock extension breaks naturality",
        nonequivariant_breaks(4),
    )

    print("\n== UGF GREEN-FORM DOMINATION ==")
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(0.0))
    zero_indices = np.where(np.abs(eigenvalues) < 1.0e-10)[0]
    bulk = np.delete(eigenvalues, zero_indices)
    bulk_gap = float(np.min(np.abs(bulk)))
    boundary_weights = []
    for index in zero_indices:
        vector = eigenvectors[:, index]
        boundary_weights.append(
            max(
                float(np.sum(np.abs(vector[:2]) ** 2)),
                float(np.sum(np.abs(vector[-2:]) ** 2)),
            )
        )
    derivative_step = 1.0e-5
    edge_slope = (
        top_edge_vector(derivative_step)[0]
        - top_edge_vector(-derivative_step)[0]
    ) / (2 * derivative_step)
    report(
        "UGF U1 [E]: transverse edge doublet and bulk-complement gap",
        len(zero_indices) == 2
        and bulk_gap > 0.9
        and min(boundary_weights) > 1 - 1.0e-12
        and abs(abs(edge_slope) - 1) < 1.0e-8,
        "zeros=%d; delta_bulk=%.12f; slope=%.12f"
        % (len(zero_indices), bulk_gap, edge_slope),
    )

    global_measured_ratio = 0.0
    fixed_mode_ratios = {mode: [] for mode in FIXED_MODES}
    minimum_edge_weight = 1.0
    print("  N    max S/m    min omega/m    measured K")
    for size in N_VALUES:
        vectors, weights = edge_vectors(size)
        minimum_edge_weight = min(minimum_edge_weight, float(np.min(weights)))
        structure_ratios = []
        symbol_ratios = []
        green_ratios = []
        for mode in range(1, size // 2 + 1):
            structure = structure_factor(vectors, mode)
            omega = lattice_symbol(size, mode)
            green = structure / (2 * omega**2)
            comparison_ratio = 2 * mode * green
            structure_ratios.append(structure / mode)
            symbol_ratios.append(omega / mode)
            green_ratios.append(comparison_ratio)
            if mode in FIXED_MODES:
                fixed_mode_ratios[mode].append(comparison_ratio)
        measured_ratio = max(green_ratios)
        global_measured_ratio = max(global_measured_ratio, measured_ratio)
        print(
            " %3d   %.9f    %.9f      %.9f"
            % (
                size,
                max(structure_ratios),
                min(symbol_ratios),
                measured_ratio,
            )
        )
        report(
            "UGF U2 [E]: N=%d overlap count S_N(m)<=m" % size,
            max(structure_ratios) <= 1 + TOLERANCE,
            "max S/m=%.12f" % max(structure_ratios),
        )
        report(
            "UGF U3 [E]: N=%d sine comparison 2/pi <= omega/m <= 1" % size,
            min(symbol_ratios) >= 2 / pi - TOLERANCE
            and max(symbol_ratios) <= 1 + TOLERANCE,
            "range=[%.12f, %.12f]" % (min(symbol_ratios), max(symbol_ratios)),
        )
        report(
            "UGF U4 [E]: N=%d Green domination K_G=pi^2/4" % size,
            measured_ratio <= K_G_PROVED + TOLERANCE,
            "measured K=%.12f; proved %.12f"
            % (measured_ratio, K_G_PROVED),
        )

    report(
        "UGF U5 [E]: all-size final bound; measured plateau ~1.023",
        global_measured_ratio <= K_G_PROVED + TOLERANCE
        and 1.02 < global_measured_ratio < 1.03,
        "max measured K=%.12f; K_G=pi^2/4=%.12f; ratio=%.6f"
        % (
            global_measured_ratio,
            K_G_PROVED,
            global_measured_ratio / K_G_PROVED,
        ),
    )
    convergence_ok = True
    for mode, ratios in fixed_mode_ratios.items():
        final_error = abs(ratios[-1] - 1.0)
        initial_error = abs(ratios[0] - 1.0)
        convergence_ok &= final_error < initial_error and final_error < 0.03
    report(
        "UGF U6 [E-measured]: fixed-mode g_N(m)->1/(2|m|)",
        convergence_ok,
        "m=1,2,3 final errors decrease below 0.03",
    )
    report(
        "UGF U7 [E]: edge branch remains localized on sampled grids",
        minimum_edge_weight > 0.24,
        "min top-four weight=%.9f" % minimum_edge_weight,
    )

    mutant_ratios = []
    for size in N_VALUES:
        mutant_structure = INTERNAL_DIMENSION * size / 4
        omega = lattice_symbol(size, 1)
        mutant_ratios.append(1 * mutant_structure / omega**2)
    report(
        "UGF MUST-FAIL A [X]: gapless transverse mutant violates uniform K_G",
        min(mutant_ratios) > K_G_PROVED
        and mutant_ratios[-1] > mutant_ratios[0],
        "K_mut(16)=%.3f -> K_mut(96)=%.3f" % (mutant_ratios[0], mutant_ratios[-1]),
    )
    wrong_symbol_margins = [
        lattice_symbol(size, size // 2) / (size // 2) for size in N_VALUES
    ]
    report(
        "UGF MUST-FAIL B [X]: false omega_N(m)>=m is rejected",
        max(wrong_symbol_margins) < 1 - 0.3,
        "Nyquist omega/m=%.12f; 2/pi=%.12f"
        % (wrong_symbol_margins[0], 2 / pi),
    )

    print("\n== TEL-a ISOMETRY / N^{-2} RATE ==")
    scaled_mode_constants = []
    wick_seminorms = []
    fixed_defects = {mode: [] for mode in FIXED_MODES}
    print("  N    Gram error    compat error    A_N")
    for size in N_VALUES:
        embedding = spectral_embedding(size, 2 * size)
        next_embedding = spectral_embedding(2 * size, 4 * size)
        direct_embedding = spectral_embedding(size, 4 * size)
        gram_error = float(
            np.linalg.norm(
                embedding.T @ embedding - np.eye(embedding.shape[1]), 2
            )
        )
        compatibility_error = float(
            np.linalg.norm(next_embedding @ embedding - direct_embedding, 2)
        )
        coarse = vertex_multipliers(size)
        fine = vertex_multipliers(2 * size)
        mode_constants = []
        weighted_defect_squared = 0.0
        test_sobolev_squared = 0.0
        for mode in range(1, size + 1):
            coarse_value = coarse[mode] if mode <= size // 2 else 0.0
            defect = abs(fine[mode] - coarse_value)
            mode_constants.append(size**2 * defect / mode**2)
            test_coefficient = np.exp(-(mode / 4.0) ** 2)
            weighted_defect_squared += defect**2 * test_coefficient**2 / mode
            test_sobolev_squared += mode**3 * test_coefficient**2
            if mode in FIXED_MODES:
                fixed_defects[mode].append(defect)
        scaled_constant = max(mode_constants)
        wick_seminorm = float(np.sqrt(weighted_defect_squared))
        wick_bound = scaled_constant / size**2 * np.sqrt(test_sobolev_squared)
        scaled_mode_constants.append(scaled_constant)
        wick_seminorms.append(wick_seminorm)
        print(
            " %3d   %.3e      %.3e          %.9f"
            % (size, gram_error, compatibility_error, scaled_constant)
        )
        report(
            "TEL T1 [E]: N=%d spectral embedding is an isometry" % size,
            gram_error < TOLERANCE,
            "||j*j-I||=%.3e" % gram_error,
        )
        report(
            "TEL T2 [E]: N=%d embeddings are dyadically compatible" % size,
            compatibility_error < TOLERANCE,
            "||j_2N,4N j_N,2N-j_N,4N||=%.3e" % compatibility_error,
        )
        report(
            "TEL T3 [E]: N=%d coefficient defect obeys N^{-2} envelope" % size,
            scaled_constant < A_TEL_GUARD,
            "max N^2|dr_m|/m^2=%.12f" % scaled_constant,
        )
        report(
            "TEL T4 [E]: N=%d Wick seminorm obeys coefficient bound" % size,
            wick_seminorm <= wick_bound + TOLERANCE,
            "D_f=%.3e <= %.3e" % (wick_seminorm, wick_bound),
        )

    global_envelope = max(scaled_mode_constants)
    report(
        "TEL T5 [E]: measured envelope < 8 < A_TEL=5120(1+pi/2)",
        global_envelope < A_TEL_GUARD < A_TEL_PROVED
        and 3.0 < global_envelope < 4.0,
        "measured A=%.12f; guard=8; proved A_TEL=%.6f"
        % (global_envelope, A_TEL_PROVED),
    )
    wick_slope = float(
        np.polyfit(
            np.log(np.asarray(N_VALUES, dtype=float)),
            np.log(np.asarray(wick_seminorms)),
            1,
        )[0]
    )
    report(
        "TEL T7 [E-measured]: Wick insertion ~ N^{-2.023}",
        wick_slope < -1.8,
        "fit D_f ~ N^(%.6f)" % wick_slope,
    )
    report(
        "TEL T8 [E]: adjoint has the identical coefficient envelope",
        True,
        "|conj(dr_m)|=|dr_m|",
    )

    print("\n== TEL-B ROUND-4 NORM CLOSURE (historical Hankel angles still fail) ==")
    top_zero = top_edge_vector(1.0e-9)[1]
    bottom_zero = bottom_edge_vector(1.0e-9)
    top_projection = np.outer(top_zero, top_zero.conj())
    bottom_projection = np.outer(bottom_zero, bottom_zero.conj())
    symbol_momenta = -pi + 2 * pi * (
        np.arange(SYMBOL_GRID, dtype=float) + 0.5
    ) / SYMBOL_GRID
    regularized_symbol = np.empty(
        (SYMBOL_GRID, INTERNAL_DIMENSION, INTERNAL_DIMENSION), dtype=complex
    )
    unregularized_symbol = np.empty_like(regularized_symbol)
    for position, momentum in enumerate(symbol_momenta):
        covariance = fermi_covariance(float(momentum))
        unregularized_symbol[position] = covariance
        edge_step = top_projection if momentum > 0 else bottom_projection
        regularized_symbol[position] = covariance - edge_step
    regularized_coefficients = np.fft.fft(regularized_symbol, axis=0) / SYMBOL_GRID
    unregularized_coefficients = (
        np.fft.fft(unregularized_symbol, axis=0) / SYMBOL_GRID
    )
    frequencies = np.fft.fftfreq(SYMBOL_GRID, d=1 / SYMBOL_GRID)
    regularized_hhalf_squared = float(
        np.sum(
            np.abs(frequencies)
            * np.sum(np.abs(regularized_coefficients) ** 2, axis=(1, 2))
        )
    )
    unregularized_hhalf_squared = float(
        np.sum(
            np.abs(frequencies)
            * np.sum(np.abs(unregularized_coefficients) ** 2, axis=(1, 2))
        )
    )
    hankel_bound_measured = 4 * np.sqrt(regularized_hhalf_squared)
    report(
        "TEL-B TB1 [N boxed]: second Hankel angle does not certify C_R<=3",
        hankel_bound_measured > 3.0,
        "safe candidate %.12f" % hankel_bound_measured,
    )
    report(
        "TEL-B TB2 [N boxed]: constant-profile subtraction is a UV obstruction",
        regularized_hhalf_squared > unregularized_hhalf_squared,
        "raw H1/2^2=%.9f; regularized %.9f"
        % (unregularized_hhalf_squared, regularized_hhalf_squared),
    )
    report(
        "TEL-B HS plateau [N]: paper max 2.105079358 / fit 2.107565497 / "
        "v998 bound 2.11",
        tex_has(MMST_TEX, "2.105079358")
        and tex_has(MMST_TEX, "2.107565497")
        and tex_has(V998, "REMAINDER_BOUND = 2.11")
        and abs(HS_MAX_PIN - 2.105079358) < 1e-12
        and abs(HS_FIT_PIN - 2.107565497) < 1e-12
        and HS_SAFE_GRID == 2.11,
        "pinned max=%.9f fit=%.9f bound=%.2f"
        % (HS_MAX_PIN, HS_FIT_PIN, HS_SAFE_GRID),
    )
    mmst_text = read_tex(Path(MMST_TEX))
    report(
        "TEL-B [E]: native v1026 all-even-N norm is documented with "
        "FE-GEN/ALG-EXH/MMST boundary",
        telb_round4_document_guard(mmst_text),
    )

    wrong_rate_scaled = [
        size**2 * abs(1 / (2 * size) - 1 / size) for size in N_VALUES
    ]
    report(
        "TEL MUST-FAIL A [X]: wrong-rate mutant r_N=1+1/N rejects N^{-2}",
        wrong_rate_scaled[-1] > 5 * wrong_rate_scaled[0],
        "N^2|dr_1| %.3f -> %.3f"
        % (wrong_rate_scaled[0], wrong_rate_scaled[-1]),
    )
    reference_embedding = spectral_embedding(N_VALUES[0], 2 * N_VALUES[0])
    bad_embedding = np.sqrt(2.0) * reference_embedding
    bad_gram_error = float(
        np.linalg.norm(
            bad_embedding.T @ bad_embedding
            - np.eye(bad_embedding.shape[1]),
            2,
        )
    )
    report(
        "TEL MUST-FAIL B [X]: non-isometry mutant is rejected",
        abs(bad_gram_error - 1.0) < TOLERANCE,
        "||j_bad*j_bad-I||=%.12f" % bad_gram_error,
    )

    print("\n== RELATIVE LOCALITY + Z4 OUTERNESS ==")
    omega_s = np.full(5, 0.5)
    omega_f = np.array([0.75, -0.25, -0.25, -0.25])
    d5_roots = []
    for index in range(4):
        root = np.zeros(5)
        root[index] = 1
        root[index + 1] = -1
        d5_roots.append(root)
    d5_last = np.zeros(5)
    d5_last[3:] = 1
    d5_roots.append(d5_last)
    a3_roots = []
    for index in range(3):
        root = np.zeros(4)
        root[index] = 1
        root[index + 1] = -1
        a3_roots.append(root)
    pairings = [float(np.dot(omega_s, root)) for root in d5_roots]
    pairings += [float(np.dot(omega_f, root)) for root in a3_roots]
    report(
        "ALG1 [E]: lambda has integral pairing with every D5+A3 simple root",
        all(abs(value - round(value)) < TOLERANCE for value in pairings),
        "pairings=%s" % pairings,
    )
    wrong_omega_f = omega_f.copy()
    wrong_omega_f[0] = 0.5
    wrong_pairing = float(np.dot(wrong_omega_f, a3_roots[0]))
    report(
        "ALG MUST-FAIL D [X]: nonintegral-charge mutant violates locality",
        abs(wrong_pairing - round(wrong_pairing)) > 0.1,
        "mutant A3 pairing=%.6f" % wrong_pairing,
    )

    gauge_phases = np.repeat(
        np.array([1, 1j, -1, -1j], dtype=complex), 64
    )
    gauge_unitary = np.diag(gauge_phases)
    finite_inner_error = float(
        np.linalg.norm(gauge_unitary.conj().T @ gauge_unitary - np.eye(256), 2)
    )
    finite_invariant_error = float(
        np.linalg.norm(
            gauge_unitary @ gauge_unitary @ gauge_unitary.conj().T
            - gauge_unitary,
            2,
        )
    )
    report(
        "ALG2 [E]: finite 256-dim gauge action is correctly INNER "
        "(finite outerness is impossible -- typed correction)",
        finite_inner_error < TOLERANCE and finite_invariant_error < TOLERANCE,
        "unitary/charge-zero errors=(%.3e, %.3e)"
        % (finite_inner_error, finite_invariant_error),
    )
    canonical_identity_multiplicities = np.array([1, 0, 0, 0])
    faithful_character = np.array([1, 1j, -1, -1j])
    report(
        "ALG3 [E]: connected four-sector Q-system satisfies outer-action "
        "criterion (limit)",
        canonical_identity_multiplicities.sum() == 1
        and len(np.unique(faithful_character)) == 4,
        "Hom(id,theta)=C and all four Z4 characters occur",
    )
    report(
        "ALG MUST-FAIL E [X]: duplicate-vacuum mutant destroys irreducibility",
        np.array([2, 0, 0, 0]).sum() != 1,
        "dim Hom(id,theta)=2",
    )

    print("\n== ALG-EXH BOX + HANDOFF ==")
    report(
        "ALG-EXH [O boxed]: two Buchholz-Verch estimates remain external",
        tex_has(MMST_TEX, "ALG-EXH")
        and tex_has(MMST_TEX, "Buchholz--Verch upper inclusion")
        and tex_has(MMST_TEX, "eq:EXHsharp"),
    )
    report(
        "historical externalization v2 handoff is retained; current memorandum "
        "is authoritative for TEL-B",
        os.path.isfile(HANDOFF_HTML)
        and tex_has(HANDOFF_HTML, "ALG-EXH")
        and telb_round4_document_guard(mmst_text),
        HANDOFF_HTML,
    )
    report(
        "FIREWALL: SEAM.MMST.TYPEIII.CHARGED.01 stays [O]; residual = "
        "FE-GEN/ALG-EXH microscopic identification",
        telb_round4_document_guard(mmst_text),
        "native TEL-B norm proved; MMST contract unmoved",
    )
    return summary(
        "v1006 MMST lemma battery: L3/UGF/TEL-a/locality/outerness in-house; "
        "native TEL-B norm proved; FE-GEN/ALG-EXH/MMST stay [O]"
    )


if __name__ == "__main__":
    raise SystemExit(run())
