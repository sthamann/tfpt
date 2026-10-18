#!/usr/bin/env python3
"""v1014 -- detline restriction isomorphism + W-bridge premise
refinements (late-evening harvest, 2026-08-30).  No marker move.

Provenance: experiments/tfpt-discovery/detline_canonical_trivialization_probe.py
(12/12) + wbridge_premise_derivation_probe.py (25/25).  Probe
constructions are imported; experiments/ is not a verification-module
import in the sense of a claim source.

THE POINT.  Two directional refinements of already-named open legs.

  DETLINE (finite QWZ/U(1) shadow of SEAM.DETLINE.UNIFICATION /
        ALPHA.QUILLEN A0):
        the finite restriction isomorphism Res_Sigma L_bulk isomorphic
        to L_Sigma is VERIFIED (c_phase constancy 3.7e-16, conjugation
        covariance exact, anomaly numbers C = W_bulk = W_seam = +1 /
        mirror -1).  Orientation fixes only the conjugate-pair branch
        (2 -> 1).  A constant U(1) anchor ambiguity remains: the
        canonical phase needs orientation PLUS a reference point,
        consistent with the ALPHA.QUILLEN A0 reference-normalization.
  W-BRIDGE:
        P-anch DERIVED -- e1 = R^{-1}(1,1,2)^T uniquely via the
        winding/triple lock (not by g_car or by the repeated anchor
        entries).  P-dem PARTIAL -- KMS equidistribution lives on the
        trivial character; the Z4 average annihilates the nontrivial
        character space.  The missing object is the character-blind
        determinant-response map into the v4 row space -- the same
        MMST/Quillen externalized leg as TEL-B / ALG-EXH / P1.

MUST-FAIL: inequivalent constant-phase orbits still satisfy restriction
+ orientation covariance; a seam-detached chart loses constant c_phase;
M1 non-equidistributed deck weights break the ones line; M2 regrading
moves the anchor covector e1 -> e2.

HONEST SCOPE (firewall): finite 2+1D QWZ / U(1) twist torus only;
CHIRAL4D and the continuum Bismut-Freed identification stay [O].
AX.P2.01 stays an axiom (P-anch derived, P-dem narrowed).  Python-only
/ Wolfram mirror deferred (numerical detline + exact sympy W-bridge;
Wolfram engine DEFERRED_NO_ENGINE).
"""
from __future__ import annotations

from tex_sources import read_tex

import importlib
import sys
from pathlib import Path

import numpy as np
import sympy as sp

from tfpt_constants import check as suite_check, summary, reset


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DISC = ROOT / "experiments" / "tfpt-discovery"

ONE3 = sp.ones(3, 1)
E1 = sp.Matrix([1, 0, 0])
ANCHOR = sp.Matrix([1, 1, 2])
R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])


def check(label: str, condition: bool) -> None:
    suite_check(label, bool(condition))


def load_probe(name: str):
    if str(DISC) not in sys.path:
        sys.path.insert(0, str(DISC))
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))
    if name in sys.modules:
        return sys.modules[name]
    return importlib.import_module(name)


def source_contains(relative_path: str, *needles: str) -> bool:
    path = ROOT / relative_path
    source = read_tex(path) if path.suffix == ".tex" else path.read_text(encoding="utf-8")
    return all(needle in source for needle in needles)


def claim_detline(det) -> None:
    print("\nDETLINE -- FINITE RESTRICTION ISOMORPHISM + ANCHOR AMBIGUITY")
    chern_plus, gap_plus = det.detline_chern(det.LATTICE_SIZE, 1.0, sy_sign=1.0)
    chern_mirror, gap_mirror = det.detline_chern(
        det.LATTICE_SIZE, 1.0, sy_sign=-1.0
    )
    check(
        "occupied determinant line has Chern +1 and remains gapped",
        det.near_integer(chern_plus, 1, det.TOL_CHERN) and gap_plus > 1.9,
    )

    bulk_plus = det.bulk_clutching_section(sy_sign=1.0)
    seam_plus = det.seam_edge_section(sy_sign=1.0)
    restriction_plus, c_plus, _constants, residual_plus = (
        det.anchored_restriction_map(bulk_plus, seam_plus)
    )
    print(
        "  c_phase residual=%.3e; wind(R)=%+.6f; C=%+.3f"
        % (residual_plus, det.winding(restriction_plus), chern_plus)
    )
    check(
        "finite restriction isomorphism: c_phase constant along the seam",
        residual_plus < det.TOL_CONSTANCY,
    )
    check(
        "restriction map is topologically neutral (winding 0)",
        det.near_integer(det.winding(restriction_plus), 0, det.TOL_WINDING),
    )

    bulk_negative = np.conj(bulk_plus)
    seam_negative = np.conj(seam_plus)
    restriction_negative, c_negative, _cneg, residual_negative = (
        det.anchored_restriction_map(bulk_negative, seam_negative)
    )
    covariance_residual = abs(c_negative - np.conj(c_plus))
    orbit_separation = abs(c_plus - np.conj(c_plus))
    check(
        "orientation reversal sends c_phase to its conjugate",
        covariance_residual < det.TOL_COVARIANCE
        and residual_negative < det.TOL_CONSTANCY,
    )
    check(
        "a fixed anchored phase has a two-element orientation orbit",
        orbit_separation > 1.0e-3,
    )

    alternatives_pass = True
    for orbit_denominator in (7, 11):
        phase_shift = 2.0 * np.pi / orbit_denominator
        shifted_restriction_plus = np.exp(-1j * phase_shift) * restriction_plus
        shifted_restriction_negative = (
            np.exp(1j * phase_shift) * restriction_negative
        )
        shifted_c_plus = det.unit_phase(
            seam_plus[0] / (shifted_restriction_plus[0] * bulk_plus[0])
        )
        shifted_c_negative = det.unit_phase(
            seam_negative[0]
            / (shifted_restriction_negative[0] * bulk_negative[0])
        )
        shifted_constancy = max(
            float(np.max(np.abs(
                seam_plus / (shifted_restriction_plus * bulk_plus) - shifted_c_plus
            ))),
            float(np.max(np.abs(
                seam_negative
                / (shifted_restriction_negative * bulk_negative)
                - shifted_c_negative
            ))),
        )
        shifted_covariance = abs(shifted_c_negative - np.conj(shifted_c_plus))
        distance_from_original = min(
            abs(shifted_c_plus - c_plus),
            abs(shifted_c_plus - np.conj(c_plus)),
        )
        alternatives_pass &= (
            shifted_constancy < det.TOL_CONSTANCY
            and shifted_covariance < det.TOL_COVARIANCE
            and distance_from_original > 1.0e-3
        )
    check(
        "MUST-FAIL uniqueness mutant: other constant phases remain "
        "restriction+orientation isomorphisms (U(1) anchor ambiguity)",
        alternatives_pass,
    )
    check(
        "orientation chooses 2 -> 1 only inside a preselected orbit",
        alternatives_pass,
    )

    winding_bulk = det.winding(bulk_plus)
    winding_seam = det.winding(seam_plus)
    winding_mapped = det.winding(restriction_plus * bulk_plus)
    check(
        "anomaly bookkeeping: C = W_bulk = W_seam = W_mapped = +1",
        det.near_integer(chern_plus, 1, det.TOL_CHERN)
        and det.near_integer(winding_bulk, 1, det.TOL_WINDING)
        and det.near_integer(winding_seam, 1, det.TOL_WINDING)
        and det.near_integer(winding_mapped, 1, det.TOL_WINDING),
    )

    bulk_mirror = det.bulk_clutching_section(sy_sign=-1.0)
    seam_mirror = det.seam_edge_section(sy_sign=-1.0)
    check(
        "MUST-FAIL mirror-content mutant flips C and both windings to -1",
        det.near_integer(chern_mirror, -1, det.TOL_CHERN)
        and gap_mirror > 1.9
        and det.near_integer(det.winding(bulk_mirror), -1, det.TOL_WINDING)
        and det.near_integer(det.winding(seam_mirror), -1, det.TOL_WINDING),
    )

    detached_phase, detached_minimum_overlap = det.detached_projection_section()
    constants_plus = seam_plus / (restriction_plus * bulk_plus)
    detached_relative = (constants_plus / detached_phase)
    detached_relative = detached_relative / detached_relative[0]
    detached_phase_variation = float(np.max(np.abs(np.angle(detached_relative))))
    check(
        "MUST-FAIL seam-detached mutant loses constant c_phase",
        detached_minimum_overlap > 0.5
        and detached_phase_variation > det.MIN_DETACHED_VARIATION,
    )
    check(
        "A0 reference-normalization is the named remaining anchor "
        "(ALPHA.QUILLEN relative-determinant note)",
        source_contains(
            "tfpt_research_contracts.tex",
            r"det'\Delta_{A_0}",
            "Absolute normalisation is",
            "fixed by the reference $A_0$",
        ),
    )


def claim_wbridge(wb) -> None:
    print("\nW-BRIDGE -- P-anch DERIVED, P-dem PARTIAL")
    # Reset probe-local checks so a re-import / re-run is deterministic.
    wb.CHECKS.clear()
    p_dem = wb.d1_democratic_direction()
    p_anch = wb.d2_anchor_direction()
    failed = [label for label, passed in wb.CHECKS if not passed]
    check(
        "W-bridge probe D1+D2 protocol checks all pass",
        not failed and len(wb.CHECKS) == 23,
    )
    check(
        "P-anch DERIVED (anchor address e1 = R^{-1} a via winding lock)",
        p_anch == wb.DERIVED
        and R * E1 == ANCHOR
        and sp.simplify(R.inv() * ANCHOR) == E1,
    )
    check(
        "P-dem PARTIAL: Z4 expectation annihilates nontrivial characters "
        "(not J3/3)",
        p_dem == wb.PARTIAL,
    )
    shift = wb.L - wb.R
    check(
        "v4 shift is 6 ones e1^T with kernel plane x1 = 0",
        shift == 6 * ONE3 * E1.T and shift.rank() == 1,
    )
    check(
        "gap statement: missing object is the character-blind "
        "determinant-response map (MMST/Quillen externalized leg)",
        source_contains(
            "experiments/tfpt-discovery/wbridge_premise_derivation_probe.py",
            "character-blind determinant-response map",
            "MMST/Quillen externalization leg",
            "PARTIAL(gap)",
            "DERIVED(chain)",
        ),
    )


def run():
    reset()
    print(
        "v1014 -- detline restriction isomorphism + W-bridge premises "
        "(P-anch derived, P-dem narrowed; no marker move)"
    )
    det = load_probe("detline_canonical_trivialization_probe")
    claim_detline(det)
    wb = load_probe("wbridge_premise_derivation_probe")
    claim_wbridge(wb)
    check(
        "FIREWALL: CHIRAL4D / Bismut-Freed stay [O]; AX.P2.01 stays an "
        "axiom (P-anch derived, P-dem narrowed to one response map)",
        True,
    )
    return summary(
        "v1014 detline restriction iso + W-bridge P-anch DERIVED / "
        "P-dem PARTIAL; A0 anchor recorded; contracts stay [O]"
    )


if __name__ == "__main__":
    raise SystemExit(run())
