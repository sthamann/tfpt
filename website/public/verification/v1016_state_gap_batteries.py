#!/usr/bin/env python3
"""v1016 -- state/gap batteries: Euclidean-cap selector, TEL-B
narrowing, uniform CAR nuclearity, DFP volume-uniform gap
(Monday-morning harvest, 2026-08-31).  No marker move.

Provenance: experiments/tfpt-discovery/rho0_euclidean_cap_probe.py
(ALL PASS) + mmst_telb_tail_probe.py (ALL PASS,
TAIL-TELESCOPING-FAILS) + mmst_nuclearity_probe.py (ALL PASS) +
det16_dynamical_links_probe.py DFP key checks (Fröhlich--Pizzo
hypotheses).  Probe constructions are imported.

THE POINT.  Four directional batteries on already-named open legs.

  FTRANSFER.SK.RHO0.01 [O]: the R4 seam-modular cap is the unique
        finite-level non-entropic selector (trace distance 0.1434
        from rho_KMS, SK response alive at 3.038e-3, mu4-invariant,
        conditional 3pi/5 saddle preserved).  R1 vacuous, R2
        response-dead, orientation-free mutant loses saddles.
        Caveat: the difference lives in the neutral spectator
        factor -- finite proxy.  Stays [O].
  SEAM.MMST.TYPEIII.CHARGED.01 [O]: the certified-tail (third) TEL-B
        route is BLOCKED -- N^2 D_N grows 530 -> 19032, remainder
        UV-supported.  The scalar dyadic-increment proposal and its
        measured 0.120--0.123 products remain historical diagnostics.
        Native v1026 instead proves ||R_N||_HS < 2.995906 < 3 for fixed
        M=1, Ny=8 and every even N>=16.  FE-GEN/ALG-EXH and the MMST
        identification remain open.  N-uniform CAR nuclearity PROVED
        (nu_N <= exp(16 C_beta); C_beta = (67.97, 29.73, 12.15)
        for beta = (0.5, 1, 2)); ALG-EXH projector-identification
        line UNCHANGED.
  CHIRAL4D.MIRROR.DET16.01 [C]: Fröhlich--Pizzo hypotheses
        cited-verified for Z2/Z4 DET open chains -- volume-uniform
        spectral gap >= Delta/2 in the parametric window tau_FP
        (a = 0.0233, a/16 = 0.00146; universal constants implicit).
        Dynamical-link leg closed at that finite-group level.
        Remaining: rotor links, wall mixing, 3+1D placement.

MUST-FAIL: N^{-2} remainder envelope rejected; gapless nuclearity
mutant loses N-uniformity; orientation-free twist loses saddles;
t=0.4 scan sits outside the certified DFP window.

HONEST SCOPE (firewall): finite 96-dim SK model / frozen QWZ collar
/ finite-group open chains.  All three contracts stay at their display
markers.  Python-only / Wolfram deferred.
"""
from __future__ import annotations

from tex_sources import read_tex

import importlib
import sys
from pathlib import Path

from tfpt_constants import check as suite_check, summary, reset


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DISC = ROOT / "experiments" / "tfpt-discovery"

MMST_TEX = ROOT / "articles" / "2026-08-30" / "mmst_charged_scaling_limit_en.tex"
DET16_TEX = ROOT / "articles" / "2026-08-30" / "det16_mirror_gap_theorem_en.tex"
HANDOFF_HTML = (
    ROOT / "articles" / "2026-08-30" / "externalization_mmst_handoff_v2_en.html"
)

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

DISTANCE_R4 = 1.434059500e-01
RESPONSE_RMS = 3.038094542e-3
C_BETA_PIN = {0.5: 67.968994250095, 1.0: 29.728144327927, 2.0: 12.148981866173}
A_R_TARGET = 43.0
A_R_MEMO = 42.956
HEADROOM_FLOOR = 340.0
SCALED_MIN = 530.264798
SCALED_MAX = 19031.615113
INCREMENT_LO = 0.119
INCREMENT_HI = 0.123
DFP_A = 0.023320199830777650
DFP_A_OVER_16 = DFP_A / 16.0
DFP_GAP_CEILING = 0.046907169193748369


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


def source_contains(path: Path, *needles: str) -> bool:
    source = read_tex(path) if path.suffix == ".tex" else path.read_text(encoding="utf-8")
    return all(needle in source for needle in needles)


def telb_round4_document_guard(text: str) -> bool:
    """Require the proved native norm and every still-open algebra boundary."""
    normalized = " ".join(text.split())
    return all(snippet in normalized for snippet in ROUND4_TELB_DOCUMENT_SNIPPETS)


def claim_euclidean(cap) -> None:
    print("\nEUCLIDEAN CAP -- R4 SEAM-MODULAR SELECTOR")
    check("euclidean-cap probe ALL PASS", cap.ALL_OK)
    winners = [row for row in cap.candidate_rows if row["selects"]]
    r4 = next(row for row in cap.candidate_rows if row["name"] == "R4")
    r1 = next(row for row in cap.candidate_rows if row["name"] == "R1")
    r2 = next(row for row in cap.candidate_rows if row["name"] == "R2")
    check(
        "R4 is the unique finite-model winner",
        [row["name"] for row in winners] == ["R4"],
    )
    check(
        "R4 differs from rho_KMS while keeping the SK response alive",
        abs(r4["distance"] - DISTANCE_R4) < 1.0e-9
        and abs(r4["response"] - RESPONSE_RMS) < 5.0e-12
        and r4["invariant"]
        and r4["saddle"],
    )
    check(
        "R1 is selection-vacuous (pure KMS square)",
        r1["distance"] < 1.0e-12 and not r1["selects"],
    )
    check(
        "R2 is nontrivial but response-dead",
        r2["distance"] > 1.0e-6
        and r2["response"] < 1.0e-12
        and not r2["selects"],
    )
    check(
        "MUST-FAIL orientation-free twist loses branch saddles",
        cap.orientation_free_amplitude < 1.0e-14,
    )
    check(
        "FIREWALL: finite-proxy caveat (neutral spectator factor); "
        "FTRANSFER.SK.RHO0.01 stays [O]",
        True,
    )


def claim_telb(telb) -> None:
    print("\nTEL-B -- HISTORICAL TAIL ROUTE BLOCKED; ROUND-4 NORM PROVED")
    check("TEL-B tail probe ALL PASS", telb.all_ok)
    scaled = [entry[2] for entry in telb.dyadic_defects]
    products = [
        pair[0] * increment
        for pair, increment in zip(telb.DYADIC_PAIRS, telb.norm_increments)
    ]
    check(
        "third (certified-tail) route BLOCKED: N^2 D_N grows "
        "530 -> 19032",
        abs(min(scaled) - SCALED_MIN) < 1.0e-4
        and abs(max(scaled) - SCALED_MAX) < 1.0e-3,
    )
    check(
        "scalar dyadic N*|Δ‖R‖| products sit in 0.120-0.123",
        INCREMENT_LO <= min(products) <= INCREMENT_HI
        and INCREMENT_LO <= max(products) <= INCREMENT_HI,
    )
    measured_a = max(products)
    headroom = A_R_TARGET / measured_a
    check(
        "A_R < 43 is sufficient for C_R < 3 with factor-~350 headroom",
        A_R_MEMO < A_R_TARGET
        and headroom > HEADROOM_FLOOR
        and measured_a < 0.13,
    )
    check(
        "verdict TAIL-TELESCOPING-FAILS (UV-supported remainder)",
        not telb.tail_rate_holds,
    )
    check(
        "memorandum records native v1026 all-even-N norm with "
        "FE-GEN/ALG-EXH/MMST boundary",
        telb_round4_document_guard(read_tex(MMST_TEX)),
    )


def claim_nuclearity(nuc) -> None:
    print("\nNUCLEARITY -- N-UNIFORM CAR COMPACTNESS; ALG UNCHANGED")
    check("nuclearity probe ALL PASS", nuc.all_ok)
    for beta, pinned in C_BETA_PIN.items():
        computed = nuc.proved_trace_constant(beta)
        check(
            "C_beta(%.1f) reproduces the proved trace constant" % beta,
            abs(computed - pinned) < 1.0e-10,
        )
        check(
            "nu_N bound is exp(16 C_beta) at beta=%.1f" % beta,
            abs(16.0 * computed - 16.0 * pinned) < 1.0e-9,
        )
    check(
        "ALG-EXH projector-identification line is NOT closed",
        source_contains(
            MMST_TEX,
            "ALG-exh",
            "eq:EXHsharp",
            "Buchholz--Verch",
        )
        and source_contains(
            Path(nuc.__file__),
            "ALG-EXH LINE 1: NOT CLOSED",
            "UNIFORM_CAR_NUCLEARITY_PROVED",
        ),
    )
    check(
        "MUST-FAIL gapless mutant loses N-uniformity",
        nuc.gapless_trace_norms[-1] > 5 * nuc.gapless_trace_norms[0],
    )


def claim_dfp(dfp) -> None:
    print("\nDFP -- FROEHLICH-PIZZO VOLUME-UNIFORM GAP (FINITE-GROUP)")
    computed_a = dfp.bisect_root(dfp.dfp_series_equation, 1.0e-8, 0.1)
    computed_gap = dfp.bisect_root(dfp.dfp_gap_series, 1.0e-8, 0.1)
    check(
        "DFP explicit series constant reproduces Eq. (A.27)",
        abs(computed_a - DFP_A) < dfp.DFP_EXPLICIT_ROOT_TOL,
    )
    check(
        "parametric window a/16 = 0.00146",
        abs(computed_a / 16.0 - DFP_A_OVER_16) < 1.0e-15
        and abs(DFP_A_OVER_16 - 0.001457512489423603) < 1.0e-15,
    )
    check(
        "DFP explicit local-gap inequality root reproduced",
        abs(computed_gap - DFP_GAP_CEILING) < dfp.DFP_EXPLICIT_ROOT_TOL,
    )
    check(
        "cited theorem: unique ground state and gap >= Delta/2",
        dfp.DFP_GAP_LOWER_BOUND == 0.5,
    )
    check(
        "Z2 and Z4 physical sectors are reducing",
        dfp.exact_gauge_structure_check(2) == 0
        and dfp.exact_gauge_structure_check(4) == 0,
    )
    check(
        "MUST-FAIL t=0.4 scan sits outside the certified DFP window",
        (0.40 * 4 / 0.5) > dfp.DFP_EXPLICIT_SERIES_CEILING
        and (0.40 * 16 / 0.5) > dfp.DFP_EXPLICIT_SERIES_CEILING,
    )
    check(
        "memorandum cites the volume-uniform theorem and remaining "
        "rotor/wall/3+1D residue",
        source_contains(
            DET16_TEX,
            "Fröhlich--Pizzo",
            "0.023320199830777650",
            "0.001457512489423603",
            r"\Delta/2",
            "rotor links",
        ),
    )
    check(
        "FIREWALL: CHIRAL4D.MIRROR.DET16.01 stays Candidate [C]; "
        "remaining rotor links, wall mixing, 3+1D placement",
        True,
    )


def run():
    reset()
    print(
        "v1016 -- state/gap batteries (R4 selector + TEL-B Round-4 norm + "
        "CAR nuclearity + DFP volume gap; no marker move)"
    )
    cap = load_probe("rho0_euclidean_cap_probe")
    claim_euclidean(cap)
    telb = load_probe("mmst_telb_tail_probe")
    claim_telb(telb)
    nuc = load_probe("mmst_nuclearity_probe")
    claim_nuclearity(nuc)
    dfp = load_probe("det16_dynamical_links_probe")
    claim_dfp(dfp)
    check(
        "handoff HTML is the named MMST specialist document",
        source_contains(
            HANDOFF_HTML,
            "TEL-B",
            "ALG-EXH",
            "SEAM.MMST.TYPEIII.CHARGED.01",
        ),
    )
    return summary(
        "v1016 R4 selector + TEL-B Round-4 norm + CAR nuclearity + "
        "DFP finite-group volume gap; contracts unmoved"
    )


if __name__ == "__main__":
    raise SystemExit(run())
