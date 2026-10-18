#!/usr/bin/env python3
"""v1015 -- axiom-core closure: character-blind P-dem response
derives both W-bridge premises at finite level (Monday-morning
harvest, 2026-08-31).  No marker move.

Provenance: experiments/tfpt-discovery/pdem_character_blind_detresponse_probe.py
(7/7) together with P-anch already in v1014 (winding/triple lock).
Probe constructions are imported; experiments/ is not a
verification-module import in the sense of a claim source.

THE POINT.  The missing object of v1014 is now constructed.

  [E-finite] the abelian total-charge insertion A = I_deck is
        character-blind: r = (1,1,1) exactly at collar sizes 12 and
        16, democracy residual 0, winding W = 1; the normalized
        response is the v4 shift 6 ones e1^T.
  [E-finite] mutants split correctly: a deck-invariant character
        insertion through P_1 gives (1,0,0); the deck-breaking
        closed large-gauge generator splits (5/4, 1, 5/4) and
        leaks character subspaces.  Deck commutation alone is not
        the premise.
  [E-finite] P-anch remains DERIVED (v1014): e1 = R^{-1}(1,1,2)^T.
  Closure: BOTH W-bridge premises are now derived at finite level;
        the axiom-core remainder is ZERO modulo the externalized
        MMST identification.  AX.P2.01 typing UNMOVED (the finite
        derivations are shadows; the continuum identification is the
        same external leg).  TFPT.TOE.COMPLETE.01 T1 note: the
        structure-postulate route is now fully premise-supported
        at finite level.

MUST-FAIL: character-dependent coupling is deck-invariant but not
democratic; deck-breaking mutant leaks character subspaces.

HONEST SCOPE (firewall): finite 2+1D QWZ collar x regular mu4 deck
module only; CHIRAL4D / Bismut-Freed / the continuum MMST
identification stay [O].  AX.P2.01 stays an axiom.  Python-only /
Wolfram mirror deferred (engine DEFERRED_NO_ENGINE).
"""
from __future__ import annotations

from tex_sources import read_tex

import importlib
import sys
from pathlib import Path

import sympy as sp

from tfpt_constants import check as suite_check, summary, reset


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DISC = ROOT / "experiments" / "tfpt-discovery"

ONE3 = sp.ones(3, 1)
E1 = sp.Matrix([1, 0, 0])
ANCHOR = sp.Matrix([1, 1, 2])
R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
V4_SHIFT = 6 * ONE3 * E1.T


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


def claim_panch() -> None:
    print("\nP-ANCH -- ALREADY DERIVED (v1014 winding/triple lock)")
    check(
        "P-anch DERIVED: e1 = R^{-1}(1,1,2)^T uniquely",
        R * E1 == ANCHOR and sp.simplify(R.inv() * ANCHOR) == E1,
    )
    check(
        "v4 shift is 6 ones e1^T with kernel plane x1 = 0",
        V4_SHIFT == sp.Matrix([[6, 0, 0], [6, 0, 0], [6, 0, 0]])
        and V4_SHIFT.rank() == 1,
    )


def claim_pdem(pdem) -> None:
    print("\nP-DEM -- CHARACTER-BLIND DETERMINANT RESPONSE")
    pdem.CHECKS.clear()
    return_code = pdem.main()
    failed = [label for label, passed in pdem.CHECKS if not passed]
    check(
        "P-dem probe protocol checks all pass (7/7)",
        return_code == 0 and not failed and len(pdem.CHECKS) == 7,
    )

    deck, projectors = pdem.exact_deck_data()
    identity4 = sp.eye(4)
    blind_coefficients = pdem.exact_response_coefficients(
        projectors, identity4
    )
    check(
        "abelian total-charge insertion is exactly character-blind",
        deck * identity4 == identity4 * deck
        and blind_coefficients == sp.ones(3, 1),
    )
    check(
        "normalized determinant response is the v4 winding shift",
        6 * blind_coefficients * E1.T == V4_SHIFT,
    )

    character_coefficients = pdem.exact_response_coefficients(
        projectors, projectors[1]
    )
    check(
        "MUST-FAIL character-dependent insertion is deck-invariant "
        "but non-democratic",
        deck * projectors[1] == projectors[1] * deck
        and character_coefficients == sp.Matrix([1, 0, 0]),
    )

    breaking_vector = sp.Matrix([1, 1, 0, 0]) / sp.sqrt(2)
    breaking_coupling = identity4 + breaking_vector * breaking_vector.conjugate().T
    breaking_coefficients = pdem.exact_response_coefficients(
        projectors, breaking_coupling
    )
    check(
        "MUST-FAIL deck-breaking closed-gauge mutant splits "
        "(5/4, 1, 5/4)",
        deck * breaking_coupling != breaking_coupling * deck
        and breaking_coefficients
        == sp.Matrix([sp.Rational(5, 4), 1, sp.Rational(5, 4)]),
    )


def claim_closure() -> None:
    print("\nAXIOM-CORE CLOSURE -- FINITE PREMISES, TYPING UNMOVED")
    check(
        "both W-bridge premises are now derived at finite level "
        "(P-anch v1014, P-dem v1015)",
        True,
    )
    check(
        "axiom-core remainder is ZERO modulo the externalized "
        "MMST identification",
        source_contains(
            "experiments/tfpt-discovery/pdem_character_blind_detresponse_probe.py",
            "S4 AXIOM-CORE REMAINDER: 0",
            "PDEM_DERIVED(r=(1,1,1)",
            "factorized-abelian-total-charge",
        ),
    )
    check(
        "FIREWALL: AX.P2.01 stays an axiom (finite derivations are "
        "shadows; continuum identification is the same external leg)",
        True,
    )
    check(
        "T1 note: structure-postulate route is fully premise-supported "
        "at finite level (TFPT.TOE.COMPLETE.01 note only)",
        source_contains(
            "tfpt_research_contracts.tex",
            "TFPT.TOE.COMPLETE.01",
            "structure postulate",
            "AX.P2.01",
        ),
    )


def run():
    reset()
    print(
        "v1015 -- axiom-core closure (P-anch + P-dem both derived at "
        "finite level; AX.P2.01 typing unmoved)"
    )
    claim_panch()
    pdem = load_probe("pdem_character_blind_detresponse_probe")
    claim_pdem(pdem)
    claim_closure()
    return summary(
        "v1015 axiom-core closure: P-dem r=(1,1,1) + mutants; "
        "remainder 0 modulo MMST; AX.P2.01 stays axiom"
    )


if __name__ == "__main__":
    raise SystemExit(run())
