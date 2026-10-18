#!/usr/bin/env python3
"""v1013 -- thermodynamic-dynamics theorem + Lieb-Robinson numeric twin
(late-evening harvest, 2026-08-30).  No marker move.

Provenance: articles/2026-08-30/tfpt_thermodynamic_dynamics_en.tex (FULLY
PROVED at Hamiltonian-class level) + experiments/tfpt-discovery/
lieb_robinson_witness_probe.py (8/8).  The probe is the numeric twin;
the theorem document carries the proof.  experiments/ is not a
verification-module import in the sense of a claim source.

THE POINT.  The MANDATORY-DYNAMICS LEG of QFT4D.LATTICE.FUNDAMENTAL.01
is CLOSED at Hamiltonian-class level:

  [E-class] uniform Lieb-Robinson bound with frozen assembled constants
        J = 12/5, R = 2, z = 4, kappa = 16043/450,
        v_LR = 2 e kappa R = 32086 e / 225 ~ 387.639.
  [E-class] norm-convergent thermodynamic-limit dynamics tau_t on every
        local observable (explicit Cauchy bound).
  [E-class] gauge-invariant quasilocal algebra (Gauss caveat resolved
        on the invariant subalgebra A^G, not a naive Hilbert embedding).
  [E-class] existence of at least one ground state and, for every
        beta > 0, at least one KMS state.
  [N]   numeric twin: measured cone v = 2.0 << proved class bound;
        analytic finite-volume bound dominates nested differences at
        buffers 8/16/32; 1/r mutant violates the inapplicable
        finite-range line; Gauss-positive control commutes, the
        constraint-violating embedding has commutator norm 1.

MUST-FAIL: the 1/r all-to-all mutant (outside the finite-range
hypothesis) violates the inapplicable bound; a constraint-violating
embedding fails to commute with the Gauss projector.

HONEST SCOPE (firewall / BOUNDARY BOX): no uniqueness / phase
structure, no thermodynamic-limit gap, no IR universality / common
light cone / continuum.  Those remain the T3/T5 contents.
QFT4D.LATTICE.FUNDAMENTAL.01 Decision typing UNCHANGED.  Python-only /
Wolfram mirror deferred (numerical twin + analytic memorandum).
"""
from __future__ import annotations

from tex_sources import read_tex

import importlib
import math
import sys
from fractions import Fraction
from pathlib import Path

from tfpt_constants import check as suite_check, summary, reset


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DISC = ROOT / "experiments" / "tfpt-discovery"

THEOREM_TEX = Path("articles/2026-08-30/tfpt_thermodynamic_dynamics_en.tex")
THEOREM_PDF = Path("articles/2026-08-30/tfpt_thermodynamic_dynamics_en.pdf")

J_EXACT = Fraction(12, 5)
KAPPA_EXACT = Fraction(16043, 450)
V_LR_PREFACTOR = Fraction(32086, 225)


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


def run():
    reset()
    print(
        "v1013 -- thermodynamic-dynamics class theorem + LR numeric twin "
        "(mandatory-dynamics leg closed at class level; Decision unmoved)"
    )
    lr = load_probe("lieb_robinson_witness_probe")

    print("\nS0  FROZEN CLASS CONSTANTS vs THEOREM")
    print(
        "  J=%.12f R=%d z=%d kappa=%.12f v_LR=%.12f"
        % (lr.J_MAX, lr.RANGE, lr.COORDINATION, lr.INTERACTION_MOMENT, lr.V_LR_PROVED)
    )
    check(
        "class J = 12/5, R = 2, z = 4 match the frozen assembled ledger",
        abs(lr.J_MAX - float(J_EXACT)) < 1.0e-14
        and lr.RANGE == 2
        and lr.COORDINATION == 4
        and abs(lr.J_MAX - 2.4) < 1.0e-14,
    )
    check(
        "interaction moment kappa = 16043/450",
        abs(lr.INTERACTION_MOMENT - float(KAPPA_EXACT)) < 1.0e-12
        and abs(lr.INTERACTION_MOMENT - 35.65111111111111) < 1.0e-12,
    )
    check(
        "proved v_LR = 2 e kappa R = 32086 e / 225",
        abs(lr.V_LR_PROVED - 2.0 * math.e * lr.INTERACTION_MOMENT * lr.RANGE) < 1.0e-12
        and abs(lr.V_LR_PROVED - float(V_LR_PREFACTOR) * math.e) < 1.0e-10
        and abs(lr.V_LR_PROVED - 387.639069990831) < 1.0e-12,
    )
    check(
        "theorem memorandum carries the class constants and the combined theorem",
        (ROOT / THEOREM_TEX).is_file()
        and (ROOT / THEOREM_PDF).is_file()
        and source_contains(
            str(THEOREM_TEX),
            r"\kappa",
            "16043",
            "32086",
            "Mandatory thermodynamic-dynamics leg",
            "BOUNDARY BOX",
        ),
    )

    print("\nS1  COMMUTATOR-NORM CONE (measured vs proved)")
    cone = lr.cone_witness()
    print(
        "  fronts=%s measured v=%.12f leakage=%.3e"
        % (cone.fronts, cone.velocity, cone.outside_leakage)
    )
    check(
        "measured cone sits strictly below the proved class velocity",
        cone.velocity <= lr.V_LR_PROVED
        and abs(cone.velocity - 2.0) < 1.0e-12
        and cone.outside_leakage < lr.LR_THRESHOLD,
    )

    print("\nS2  NESTED-VOLUME NORM CONVERGENCE")
    finite_range_rows = []
    for radius in lr.CONVERGENCE_RADII:
        difference = lr.embedded_projector_distance(radius, lr.LARGE_RADIUS)
        bound = lr.convergence_bound(radius)
        finite_range_rows.append((radius, difference, bound))
        print(
            "  buffer=%2d  difference=%.12e  bound=%.12e"
            % (radius, difference, bound)
        )
    check(
        "analytic finite-volume bound dominates nested differences at 8/16/32",
        all(
            difference <= bound + lr.NUMERIC_TOLERANCE
            for _radius, difference, bound in finite_range_rows
        ),
    )
    check(
        "nested differences are Cauchy (nonincreasing)",
        all(
            right[1] <= left[1] + lr.NUMERIC_TOLERANCE
            for left, right in zip(finite_range_rows[:-1], finite_range_rows[1:])
        ),
    )

    print("\nS3  DESTRUCTIVE MUTANTS + GAUSS COMPATIBILITY")
    long_range_difference = lr.embedded_projector_distance(
        lr.CONVERGENCE_RADII[-1], lr.LARGE_RADIUS, long_range=True
    )
    false_finite_range_bound = lr.convergence_bound(lr.CONVERGENCE_RADII[-1])
    mutant_ratio = long_range_difference / false_finite_range_bound
    print(
        "  1/r mutant difference=%.12e; inapplicable bound=%.12e; ratio=%.6e"
        % (long_range_difference, false_finite_range_bound, mutant_ratio)
    )
    check(
        "MUST-FAIL: 1/r mutant violates the inapplicable finite-range bound",
        long_range_difference > 4.0 * false_finite_range_bound,
    )
    good_commutator, restriction_defect, bad_commutator = lr.gauss_compatibility()
    check(
        "gauge-invariant embedding commutes with Gauss projection",
        good_commutator < 1.0e-14 and restriction_defect < 1.0e-14,
    )
    check(
        "MUST-FAIL: constraint-violating embedding fails Gauss compatibility",
        bad_commutator > 0.9,
    )
    check(
        "theorem document records the Gauss-subalgebra resolution "
        "and the existence (not uniqueness) of equilibrium states",
        source_contains(
            str(THEOREM_TEX),
            r"\A^G",
            "Compatible constrained dynamics",
            "Ground and KMS states",
            "does \\emph{not} give uniqueness",
        ),
    )
    check(
        "FIREWALL: Decision typing UNCHANGED; uniqueness / limit gap / "
        "IR universality remain open (mandatory-dynamics leg only)",
        source_contains(
            str(THEOREM_TEX),
            "phase structure",
            "spectral gap survives",
            "IR universality",
        ),
    )
    return summary(
        "v1013 thermodynamic-dynamics: class LR + tau_t + A^G + state "
        "existence proved; numeric twin 8/8; Decision unmoved"
    )


if __name__ == "__main__":
    raise SystemExit(run())
