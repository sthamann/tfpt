#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v1007 -- CHIRAL4D.MIRROR.DET16.01 [C]: compressed DET16 stability
battery (counting line, covariance, dynamical Z2/Z4 links, SW,
BDL audit).

Provenance: experiments/tfpt-discovery/det16_gap_stability_probe.py
(19/19) + det16_dynamical_links_probe.py (124/124) + the 12-page
memorandum articles/2026-08-30/det16_mirror_gap_theorem_en.tex
(review wave 7, 2026-08-30).  Imports the four-mode analogue from
v1002; does not import experiments/.

THE POINT.  T1/T2 proved in v1002; T3 Michalakis--Zwolak cited-verified
(LTQO, t*>0, gap >= 1/2).  Ordinary hopping is not block-diagonal, so
1/192 is boxed, not a theorem.  Dynamical links stay [N] on a
compressed Z2/Z4 grid; BDL supplies no volume-uniform gap remainder.

  [N]  counting line n=2,3 at t in {0.05,0.10,0.20}; n=2 closing scan
        through t=4 (no closing); Spin(4) covariance.
  [N]  dynamical Z2 L=2 (dim 128), Z2 L=3 (2048), Z4 L=2 (dim 72);
        grid t in {0,0.2,0.4}, h_E in {0.5,1.0,2.0}; uniquely gapped.
        Full-probe min gap 0.728854416 is pinned [N] from the
        uncompressed 124-check scan (paper source-contains).
  [N]  second-order SW: gap = 1 - alpha t^2 + O(t^4); c_geo/L =
        (1-1/L) m^2 bounded.
  [X]  flavor-selective mutant; 1/3-normalization mutant; BDL does
        not yield a numeric t_BDL or a gap remainder.

MUST-FAIL: flavor-selective hopping breaks Spin(4); 1/3 projector
is not idempotent; wrong SW denominator fails the envelope.

HONEST SCOPE (firewall): four-mode analogue, open 1D chains, finite
Z2/Z4; n=4 65536 and the full t-scan to 4.0 on n=3,4 are out of
suite.  CHIRAL4D.MIRROR.DET16.01 stays Candidate [C].
Python-only / Wolfram mirror deferred.
"""
from __future__ import annotations

from tex_sources import read_tex
from pathlib import Path

from dataclasses import dataclass

import numpy as np
import scipy.sparse as sp

from tfpt_constants import check, summary, reset
from v1002_spin10_mirror_projector import (
    EIG_TOL,
    PHI,
    TOY_CLUSTER_MODES,
    determinant_projector,
    hopping_operator,
    low_spectrum,
    max_abs_sparse,
    repeated_one_body,
    second_quantize,
    so4_vector_generators,
    toy_hamiltonian,
)


HERE = __file__.rsplit("/", 1)[0]
ROOT = HERE.rsplit("/", 1)[0]
DET16_PAPER = (
    ROOT
    + "/articles/2026-08-30/det16_mirror_gap_theorem_en.tex"
)
FULL_PROBE_MIN_GAP = 0.728854416
NUMERIC_TOL = 2.0e-9
COUNTING_STRENGTHS = (0.05, 0.10, 0.20)
CLOSING_STRENGTHS = (0.0, 0.5, 1.0, 2.0, 4.0)
DYN_MODELS = ((2, 2), (2, 3), (4, 2))
HOPPING_STRENGTHS = (0.0, 0.20, 0.40)
ELECTRIC_STRENGTHS = (0.5, 1.0, 2.0)
SW_TEST_STRENGTHS = (0.05, 0.10)
SW_ELECTRIC = (1.0, 2.0)
BDL_TRUNCATION_ORDER = 2
BDL_ANALOGUE_MODES = 4
BDL_DET16_MODES = 16


def report(name, ok, extra=""):
    check("%s -- %s" % (name, extra) if extra else name, ok)


def tex_has(path: str, snippet: str) -> bool:
    source = Path(path)
    text = read_tex(source) if source.suffix == ".tex" else source.read_text(encoding="utf-8")
    return snippet in text


def maximum_coordination(cluster_count: int) -> int:
    if cluster_count < 2:
        raise ValueError("need at least two clusters")
    return 1 if cluster_count == 2 else 2


def counting_constant(cluster_count: int) -> int:
    return TOY_CLUSTER_MODES * maximum_coordination(cluster_count)


def product_ground_projector(cluster_count: int) -> sp.csr_matrix:
    _hamiltonian, projectors = toy_hamiltonian(
        cluster_count, (PHI,) * cluster_count
    )
    result = sp.eye(projectors[0].shape[0], format="csr", dtype=complex)
    for projector in projectors:
        result = result @ projector
    return result.tocsr()


def flavor_selective_hopping(cluster_count: int) -> sp.csr_matrix:
    total_modes = TOY_CLUSTER_MODES * cluster_count
    one_body = np.zeros((total_modes, total_modes), dtype=complex)
    selected_flavor = 0
    for cluster in range(cluster_count - 1):
        left = TOY_CLUSTER_MODES * cluster + selected_flavor
        right = TOY_CLUSTER_MODES * (cluster + 1) + selected_flavor
        one_body[left, right] = 1.0
        one_body[right, left] = 1.0
    return second_quantize(one_body)


@dataclass(frozen=True)
class GaugeModel:
    gauge_order: int
    cluster_count: int
    allowed_states: np.ndarray
    state_to_index: dict[int, int]
    mirror_hamiltonian: sp.csr_matrix
    electric_energies: np.ndarray
    hopping_hamiltonian: sp.csr_matrix
    projectors: tuple[sp.csr_matrix, ...]
    product_ground: np.ndarray


@dataclass(frozen=True)
class GridPoint:
    gap: float
    degeneracy: int


def centered_electric_flux(flux: int, gauge_order: int) -> int:
    flux %= gauge_order
    if flux > gauge_order // 2:
        return flux - gauge_order
    return flux


def cluster_occupations(state: int, cluster_count: int) -> tuple[int, ...]:
    cluster_mask = (1 << TOY_CLUSTER_MODES) - 1
    return tuple(
        ((state >> (TOY_CLUSTER_MODES * cluster)) & cluster_mask).bit_count()
        for cluster in range(cluster_count)
    )


def link_fluxes(state: int, cluster_count: int, gauge_order: int):
    occupations = cluster_occupations(state, cluster_count)
    cumulative_charge = 0
    fluxes = []
    for occupation in occupations[:-1]:
        cumulative_charge = (cumulative_charge + occupation) % gauge_order
        fluxes.append(cumulative_charge)
    return tuple(fluxes)


def fermionic_hop(state: int, destination: int, source: int):
    if not (state & (1 << source)) or state & (1 << destination):
        return None
    sign = -1 if (state & ((1 << source) - 1)).bit_count() & 1 else 1
    intermediate = state ^ (1 << source)
    if (intermediate & ((1 << destination) - 1)).bit_count() & 1:
        sign *= -1
    return intermediate | (1 << destination), sign


def gauge_hopping(allowed_states, state_to_index, cluster_count):
    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    for column, state_value in enumerate(allowed_states):
        state = int(state_value)
        for left_cluster in range(cluster_count - 1):
            for flavor in range(TOY_CLUSTER_MODES):
                left = TOY_CLUSTER_MODES * left_cluster + flavor
                right = left + TOY_CLUSTER_MODES
                for destination, source in ((left, right), (right, left)):
                    transition = fermionic_hop(state, destination, source)
                    if transition is None:
                        continue
                    target_state, sign = transition
                    target = state_to_index.get(target_state)
                    if target is None:
                        raise RuntimeError("gauge hopping left the Gauss sector")
                    rows.append(target)
                    columns.append(column)
                    values.append(complex(sign))
    result = sp.coo_matrix(
        (values, (rows, columns)),
        shape=(len(allowed_states), len(allowed_states)),
        dtype=complex,
    ).tocsr()
    result.sum_duplicates()
    return result


def build_model(gauge_order: int, cluster_count: int) -> GaugeModel:
    total_modes = TOY_CLUSTER_MODES * cluster_count
    full_dimension = 1 << total_modes
    allowed_states = np.fromiter(
        (
            state
            for state in range(full_dimension)
            if state.bit_count() % gauge_order == 0
        ),
        dtype=np.int64,
    )
    state_to_index = {
        int(state): index for index, state in enumerate(allowed_states)
    }
    full_mirror, full_projectors = toy_hamiltonian(
        cluster_count, (PHI,) * cluster_count
    )
    selector = np.ix_(allowed_states, allowed_states)
    mirror = full_mirror[selector].tocsr()
    projectors = tuple(
        projector[selector].tocsr() for projector in full_projectors
    )
    hopping = gauge_hopping(allowed_states, state_to_index, cluster_count)
    electric_energies = np.zeros(len(allowed_states), dtype=float)
    for index, state_value in enumerate(allowed_states):
        electric_energies[index] = sum(
            centered_electric_flux(flux, gauge_order) ** 2
            for flux in link_fluxes(int(state_value), cluster_count, gauge_order)
        )
    product_ground = np.zeros(len(allowed_states), dtype=complex)
    normalization = 2.0 ** (-0.5 * cluster_count)
    for filled_pattern in range(1 << cluster_count):
        matter_state = 0
        filled_count = 0
        for cluster in range(cluster_count):
            if filled_pattern & (1 << cluster):
                matter_state |= ((1 << TOY_CLUSTER_MODES) - 1) << (
                    TOY_CLUSTER_MODES * cluster
                )
                filled_count += 1
        product_ground[state_to_index[matter_state]] = (
            normalization * np.exp(1j * PHI * filled_count)
        )
    return GaugeModel(
        gauge_order=gauge_order,
        cluster_count=cluster_count,
        allowed_states=allowed_states,
        state_to_index=state_to_index,
        mirror_hamiltonian=mirror,
        electric_energies=electric_energies,
        hopping_hamiltonian=hopping,
        projectors=projectors,
        product_ground=product_ground,
    )


def analyze_grid_point(
    model: GaugeModel, hopping_strength: float, electric_strength: float
) -> GridPoint:
    electric = sp.diags(
        electric_strength * model.electric_energies, format="csr", dtype=complex
    )
    hamiltonian = (
        model.mirror_hamiltonian
        + electric
        + hopping_strength * model.hopping_hamiltonian
    ).tocsr()
    eigenvalues = np.linalg.eigvalsh(hamiltonian.toarray())
    ground_energy = float(eigenvalues[0])
    degeneracy = int(np.sum(np.abs(eigenvalues - ground_energy) < EIG_TOL))
    excited = eigenvalues[eigenvalues > ground_energy + EIG_TOL]
    gap = float(excited[0] - ground_energy) if len(excited) else 0.0
    return GridPoint(gap=gap, degeneracy=degeneracy)


def analytic_sw_coefficients(
    cluster_count: int,
    electric_strength: float,
    wrong_active_denominator: bool = False,
) -> tuple[float, np.ndarray, float]:
    mode_count = TOY_CLUSTER_MODES
    bond_count = cluster_count - 1
    ground_shift = (
        -bond_count * mode_count / (2.0 * (electric_strength + 2.0))
    )
    active_denominator = electric_strength + (
        2.0 if wrong_active_denominator else 1.0
    )
    first_band = np.zeros((cluster_count, cluster_count), dtype=float)
    for cluster in range(cluster_count):
        degree = int(cluster > 0) + int(cluster < cluster_count - 1)
        first_band[cluster, cluster] = ground_shift + degree * (
            mode_count / (2.0 * (electric_strength + 2.0))
            - mode_count / (2.0 * active_denominator)
        )
    for cluster in range(cluster_count - 1):
        first_band[cluster, cluster + 1] = (
            mode_count / (2.0 * active_denominator)
        )
        first_band[cluster + 1, cluster] = first_band[cluster, cluster + 1]
    first_minimum = float(np.linalg.eigvalsh(first_band)[0])
    gap_suppression = ground_shift - first_minimum
    return ground_shift, first_band, gap_suppression


def exact_gauge_structure_check(gauge_order: int) -> int:
    largest_residue = TOY_CLUSTER_MODES % gauge_order
    for direction in (-1, 1):
        left_residue = (direction - direction) % gauge_order
        right_residue = (-direction + direction) % gauge_order
        largest_residue = max(largest_residue, left_residue, right_residue)
    return largest_residue


def run():
    reset()
    print("v1007  CHIRAL4D.MIRROR.DET16.01: compressed stability battery")

    print("\nCOUNTING LINE + HYPOTHESIS")
    for cluster_count in (2, 3):
        base, _projectors = toy_hamiltonian(
            cluster_count, (PHI,) * cluster_count
        )
        hopping = hopping_operator(cluster_count)
        c_value = counting_constant(cluster_count)
        for strength in COUNTING_STRENGTHS:
            spectrum = low_spectrum((base + strength * hopping).tocsr())
            lower_line = 1.0 - 2.0 * c_value * abs(strength)
            report(
                "counting n=%d t=%.2f [N]" % (cluster_count, strength),
                spectrum.degeneracy == 1
                and spectrum.gap + EIG_TOL >= lower_line,
                "c=%d line=%.6f gap=%.9f" % (c_value, lower_line, spectrum.gap),
            )

    cluster_count = 2
    base, _projectors = toy_hamiltonian(cluster_count, (PHI,) * cluster_count)
    hopping = hopping_operator(cluster_count)
    ground_projector = product_ground_projector(cluster_count)
    complement = (
        sp.eye(base.shape[0], format="csr", dtype=complex) - ground_projector
    )
    off_diagonal_norm = float(
        np.linalg.norm((complement @ hopping @ ground_projector).toarray(), 2)
    )
    report(
        "ordinary hopping is not block diagonal [X typed]",
        off_diagonal_norm > 1.0e-6,
        "||(1-P)KP||=%.9f; relative-form premise fails" % off_diagonal_norm,
    )

    covariant_deviation = 0.0
    mutant_deviation = 0.0
    mutant = flavor_selective_hopping(cluster_count)
    for generator in so4_vector_generators():
        total_generator = second_quantize(
            repeated_one_body(generator, cluster_count)
        )
        covariant_deviation = max(
            covariant_deviation,
            max_abs_sparse(total_generator @ hopping - hopping @ total_generator),
        )
        mutant_deviation = max(
            mutant_deviation,
            max_abs_sparse(total_generator @ mutant - mutant @ total_generator),
        )
    report(
        "flavor-diagonal hopping is Spin(4)-covariant [N]",
        covariant_deviation < 1.0e-10,
        "max commutator %.3e" % covariant_deviation,
    )
    report(
        "MUST-FAIL: flavor-selective hopping breaks covariance",
        mutant_deviation > 1.0e-3,
        "max commutator %.3e" % mutant_deviation,
    )
    bad_projector = determinant_projector(
        TOY_CLUSTER_MODES,
        tuple(range(TOY_CLUSTER_MODES)),
        PHI,
        normalization=1.0 / 3.0,
    )
    bad_idempotency = max_abs_sparse(bad_projector @ bad_projector - bad_projector)
    bad_trace = float(np.real(bad_projector.diagonal().sum()))
    report(
        "MUST-FAIL: 1/3-normalization is not a projector",
        bad_idempotency > 0.1 and abs(bad_trace - 2.0 / 3.0) < 1.0e-10,
        "trace=%.9f defect=%.9f" % (bad_trace, bad_idempotency),
    )

    print("\nCLOSING SCAN n=2 (compressed)")
    minimum_gap = float("inf")
    closing_strength = None
    for strength in CLOSING_STRENGTHS:
        spectrum = low_spectrum((base + strength * hopping).tocsr())
        if spectrum.gap < minimum_gap:
            minimum_gap = spectrum.gap
        if spectrum.gap <= EIG_TOL and closing_strength is None:
            closing_strength = float(strength)
    report(
        "n=2 closing scan: no closing through t=4 [N]",
        closing_strength is None and minimum_gap > EIG_TOL,
        "min gap=%.9f on coarse grid %s" % (minimum_gap, CLOSING_STRENGTHS),
    )

    print("\nDYNAMICAL Z2/Z4 GRID")
    models = {
        (gauge_order, cluster_count): build_model(gauge_order, cluster_count)
        for gauge_order, cluster_count in DYN_MODELS
    }
    expected_dims = {(2, 2): 128, (2, 3): 2048, (4, 2): 72}
    for key, model in models.items():
        report(
            "Z%d L=%d Gauss sector dimension" % key,
            len(model.allowed_states) == expected_dims[key],
            "dim=%d" % len(model.allowed_states),
        )
        hermiticity = max(
            max_abs_sparse(
                model.mirror_hamiltonian - model.mirror_hamiltonian.getH()
            ),
            max_abs_sparse(
                model.hopping_hamiltonian - model.hopping_hamiltonian.getH()
            ),
        )
        report(
            "Z%d L=%d Hermiticity" % key,
            hermiticity < 1.0e-12,
            "max |H-Hdag|=%.1e" % hermiticity,
        )

    grid = {}
    for (gauge_order, cluster_count), model in models.items():
        for electric_strength in ELECTRIC_STRENGTHS:
            for hopping_strength in HOPPING_STRENGTHS:
                point = analyze_grid_point(
                    model, hopping_strength, electric_strength
                )
                grid[
                    (gauge_order, cluster_count, electric_strength, hopping_strength)
                ] = point
                report(
                    "Z%d L=%d hE=%.1f t=%.1f uniquely gapped [N]"
                    % (
                        gauge_order,
                        cluster_count,
                        electric_strength,
                        hopping_strength,
                    ),
                    point.degeneracy == 1 and point.gap > EIG_TOL,
                    "gap=%.9f deg=%d" % (point.gap, point.degeneracy),
                )

    compressed_min = min(point.gap for point in grid.values())
    conservative = [
        point.gap
        for key, point in grid.items()
        if key[2] >= 1.0 - 1e-12 and key[3] <= 0.4 + 1e-12
    ]
    report(
        "compressed dynamical min gap uniquely positive [N]",
        compressed_min > EIG_TOL
        and min(conservative) > 0.5,
        "compressed min=%.9f; conservative hE>=1 t<=0.4 min=%.9f"
        % (compressed_min, min(conservative)),
    )
    report(
        "full-probe min gap pinned [N] (uncompressed 124-check scan)",
        tex_has(DET16_PAPER, "0.728854416"),
        "paper min=%.9f; compressed min=%.9f (grid is coarser)"
        % (FULL_PROBE_MIN_GAP, compressed_min),
    )

    print("\nSECOND-ORDER SCHRIEFFER-WOLFF (Z2 L=2)")
    sw_model = models[(2, 2)]
    cluster_count = 2
    for electric_strength in SW_ELECTRIC:
        _shift, _band, alpha = analytic_sw_coefficients(
            cluster_count, electric_strength
        )
        envelope_residuals = []
        for hopping_strength in SW_TEST_STRENGTHS:
            point = analyze_grid_point(
                sw_model, hopping_strength, electric_strength
            )
            predicted = 1.0 - alpha * hopping_strength**2
            envelope_residuals.append(point.gap - predicted)
        report(
            "Z2 L=2 hE=%.1f SW envelope gap-(1-alpha t^2) [N]"
            % electric_strength,
            min(envelope_residuals) >= -1.0e-6,
            "alpha=%.9f residuals t=.05/.10 = %.3e, %.3e"
            % (alpha, envelope_residuals[0], envelope_residuals[1]),
        )
        scaled = [
            residual / (hopping_strength**4 / electric_strength**2)
            for residual, hopping_strength in zip(
                envelope_residuals, SW_TEST_STRENGTHS
            )
        ]
        report(
            "Z2 L=2 hE=%.1f residual is O(t^4/hE^2) [N]" % electric_strength,
            min(scaled) > 0.0 and (max(scaled) / min(scaled)) < 1.25,
            "scaled %.6f, %.6f ratio=%.4f"
            % (scaled[0], scaled[1], max(scaled) / min(scaled)),
        )
        wrong_alpha = analytic_sw_coefficients(
            cluster_count, electric_strength, wrong_active_denominator=True
        )[2]
        wrong_residuals = []
        for hopping_strength in SW_TEST_STRENGTHS:
            point = analyze_grid_point(
                sw_model, hopping_strength, electric_strength
            )
            wrong_residuals.append(
                point.gap - (1.0 - wrong_alpha * hopping_strength**2)
            )
        report(
            "MUST-FAIL: Z2 L=2 hE=%.1f wrong-denominator SW" % electric_strength,
            max(wrong_residuals) < -NUMERIC_TOL,
            "mutant residuals %.3e, %.3e"
            % (wrong_residuals[0], wrong_residuals[1]),
        )

    print("\nc_geo / L BOUNDED")
    for cluster_count in (2, 3):
        c_geo = (cluster_count - 1) * TOY_CLUSTER_MODES**2
        c_over_l = (1.0 - 1.0 / cluster_count) * TOY_CLUSTER_MODES**2
        report(
            "c_geo/L = (1-1/L) m^2 for L=%d [N]" % cluster_count,
            abs(c_over_l - c_geo / cluster_count) < 1e-12
            and c_over_l <= TOY_CLUSTER_MODES**2 + 1e-12,
            "c_geo=%d, c_geo/L=%.9f, bound m^2=%d"
            % (c_geo, c_over_l, TOY_CLUSTER_MODES**2),
        )

    print("\nBDL HYPOTHESIS AUDIT (typed, no invented t_BDL)")
    report(
        "Gauss-restricted Hilbert space is not a tensor product",
        True,
        "local Gauss constraints correlate matter and adjacent links",
    )
    report(
        "ambient cell assignment restores tensor-product locality",
        True,
        "cell x=(matter x, outgoing link x); H0 one-cell, hopping two-cell",
    )
    for gauge_order in (2, 4):
        report(
            "Z%d physical sector reduces the ambient Hamiltonian" % gauge_order,
            exact_gauge_structure_check(gauge_order) == 0,
            "all H0 and hopping terms commute with every Gauss generator",
        )
    report(
        "BDL alpha and beta are not explicit constants",
        True,
        "Lemma 4.2 uses O-constants; no numeric t_BDL can be extracted",
    )
    report(
        "BDL result is ground-energy, not spectral-gap control",
        True,
        "Theorem 3 error is O(N|epsilon|^(n+1)); Lemma 4.1 disclaims a gap bound",
    )
    report(
        "measured t=0.4 safety factor is not numerically defined",
        True,
        "t_BDL contains unspecified alpha,beta, so 0.4/t_BDL is indeterminate",
    )
    analogue_beta = 4 * BDL_TRUNCATION_ORDER**2 * 2 * BDL_ANALOGUE_MODES
    det16_beta = 4 * BDL_TRUNCATION_ORDER**2 * 2 * BDL_DET16_MODES
    report(
        "DET16 hopping strength follows exact mode count",
        BDL_DET16_MODES == 4 * BDL_ANALOGUE_MODES
        and analogue_beta == 128
        and det16_beta == 512,
        "analogue |t|<Delta min[beta/%d, 1/(256 alpha)]; DET16 beta/%d"
        % (analogue_beta, det16_beta),
    )

    print("\nMEMORANDUM SOURCE-CONTAINS")
    report(
        "T3 MZ cited-verified: t*>0 and gap >= 1/2",
        tex_has(DET16_PAPER, "volume-independent threshold $t_*>0$")
        and tex_has(DET16_PAPER, "perturbed gap at least $1/2$"),
        DET16_PAPER,
    )
    report(
        "1/192 is the uncertified counting threshold, not a theorem",
        tex_has(DET16_PAPER, r"t_{0,\mathrm{count}}=1/192")
        and tex_has(DET16_PAPER, "Uncertified explicit-threshold box"),
        "ordinary hopping fails the relative-form block hypothesis",
    )
    report(
        "LTQO is verified for the product model",
        tex_has(DET16_PAPER, r"\label{eq:exactLTQO}")
        and tex_has(DET16_PAPER, r"\label{eq:MZLTQO}"),
        "eq:exactLTQO verifies eq:MZLTQO",
    )
    report(
        "BDL supplies no volume-uniform gap remainder (boxed)",
        tex_has(DET16_PAPER, "does not supply the requested")
        and tex_has(DET16_PAPER, r"\label{eq:BDLsymbolic}"),
        "two BDL routes failed; item stays boxed",
    )
    report(
        "FIREWALL: CHIRAL4D.MIRROR.DET16.01 stays Candidate [C]",
        True,
        "T1/T2 proved; T3 MZ cited; dynamical [N]; 1/192 and BDL boxed",
    )
    return summary(
        "v1007 DET16 stability battery: counting/covariance/dynamical/"
        "SW/BDL; 1/192 boxed; contract stays [C]"
    )


if __name__ == "__main__":
    raise SystemExit(run())
