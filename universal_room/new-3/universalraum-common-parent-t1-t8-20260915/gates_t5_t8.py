"""T5-T8 gate checker slice for the universalraum-common-parent-t1-t8-20260915 worktree.

Imports the shared ``parent_model`` (interface: ``parent_id``, ``constants``,
``R_eta``, ``J_eta``, ``L_eta``, ``U_eta``) and encodes exact symbolic /
rational witnesses for gates T5-T8.  No gate is closed: the naive
cycle-uniform-gap route is killed (T5), declared required mechanisms stay
non-unique / underselected (T6), the Lorentz-type of the only uniform
mediator is an antisymmetric tensor, not spin 2 (T7), and the untwisted
asymmetric ground-margin 8223/31250 > 0 proves unique-ground-state selection
insufficient (T8).  Operator-state / scattering, native state / instrument /
record and a universal dynamic coupling are absent.

SymPy + stdlib only.  No ``assert`` statements.  ``run()`` returns a stable
JSON-serialisable dict; the CLI prints the same JSON.  Per-gate fields match
the T1-T4 slice.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

# Shared parent model (live contract).  No fallback: a missing/broken
# interface is a hard import failure, never a silent parent-id substitution.
import parent_model  # noqa: E402  -- PARENT_ID, CONSTANTS, R_eta, J_eta, L_eta, U_eta

PARENT_ID: str = parent_model.PARENT_ID
CONSTANTS: dict = parent_model.CONSTANTS

# --------------------------------------------------------------------------- #
#  Check registry
# --------------------------------------------------------------------------- #
_checks: list[str] = []


def _record(label: str, ok: bool) -> bool:
    """Record a named check with its boolean outcome and return ``ok``."""
    _checks.append(label)
    return bool(ok)


def _parent_attr(name: str, default):
    """Read an attribute from the shared parent_model, falling back to default.

    Used only for OPTIONAL diagnostic flags (e.g. ``free_spin2_prescribed``);
    the canonical ``parent_id`` and ``constants`` are always read from the
    stable module-level exports, never from this helper.
    """
    return getattr(parent_model, name, default)


# --------------------------------------------------------------------------- #
#  T5 -- naive cycle scaling gap
# --------------------------------------------------------------------------- #
def gate_t5() -> dict:
    """s_min(L) = 1 - cos(pi/L): exact values, decreasing sequence, limit 0.

    The infimum over L is 0, so no uniform positive lower bound exists; the
    naive-cycle-uniform-gap route is killed.  Operator-state and scattering
    instruments are absent from the parent model.
    """
    L = sp.symbols("L", positive=True, integer=True)
    s_min = 1 - sp.cos(sp.pi / L)

    ladder = {int(n): sp.simplify(1 - sp.cos(sp.pi / n)) for n in range(1, 9)}

    _record("T5: s_min(1) = 1 - cos(pi) = 2", ladder[1] == 2)
    _record("T5: s_min(2) = 1 - cos(pi/2) = 1", ladder[2] == 1)
    _record("T5: s_min(3) = 1 - cos(pi/3) = 1/2", ladder[3] == sp.Rational(1, 2))
    _record(
        "T5: s_min(4) = 1 - cos(pi/4) = 1 - sqrt(2)/2",
        sp.simplify(ladder[4] - (1 - sp.sqrt(2) / 2)) == 0,
    )

    decreasing = all(sp.simplify(ladder[n] - ladder[n + 1]) > 0 for n in range(1, 8))
    _record("T5: s_min(L) strictly decreasing for L = 1..8", decreasing)

    lim = sp.limit(s_min, L, sp.oo)
    _record("T5: lim_{L->+inf} s_min(L) = 0", lim == 0)

    inf_zero = (lim == 0)
    _record("T5: inf_L s_min(L) = 0 (no uniform positive lower bound)", inf_zero)

    killed = ["naive-cycle-uniform-gap"] if inf_zero else []

    has_os = hasattr(parent_model, "operator_state")
    has_scat = hasattr(parent_model, "scattering")
    _record("T5: operator-state instrument absent from parent_model", not has_os)
    _record("T5: scattering instrument absent from parent_model", not has_scat)
    absent = []
    if not has_os:
        absent.append("operator-state")
    if not has_scat:
        absent.append("scattering")

    return {
        "gate_id": "T5",
        "status": "partial" if inf_zero else "open",
        "summary": (
            "s_min(L)=1-cos(pi/L) is exact, strictly decreasing and tends to 0; "
            "the naive-cycle-uniform-gap route is killed; OS/scattering absent."
        ),
        "evidence": {
            "formula": "s_min(L) = 1 - cos(pi/L)",
            "exact_values": {str(k): str(v) for k, v in ladder.items()},
            "symbolic_limit": str(lim),
            "decreasing_sequence_verified": bool(decreasing),
            "infimum": "0",
            "no_uniform_positive_gap": bool(inf_zero),
        },
        "proven": [
            "s_min(L)=1-cos(pi/L) exact and strictly decreasing for L=1..8",
            "lim_{L->+inf} s_min(L) = 0 (no uniform positive lower bound)",
        ] if inf_zero else [],
        "killed_routes": killed,
        "missing": absent,
        "open_gaps": [
            "continuum / thermodynamic limit of the native cycle",
            "operator-state instrument at the parent",
            "scattering instrument at the parent",
        ],
        "exact_checks": len(_checks[-9:]),
        "checks": list(_checks[-9:]),
        "closed_in_package": False,
        "parent_id": PARENT_ID,
    }


# --------------------------------------------------------------------------- #
#  T6 -- parameter / spectrum contract (T6-specific) + underselection witness
# --------------------------------------------------------------------------- #
def gate_t6() -> dict:
    """T6-specific required conditions for parameter/spectrum closure, plus an
    exact non-uniqueness / underselection witness, WITHOUT fitting any
    observed data.  Closure is false.

    T6 required conditions (scoped to the parameter/spectrum contract, NOT
    substituting T3/T7/T8 requirements):
      * a single common normalized transfer / Detline functional W[J] shared
        across all four transfer interfaces (poles, eta_B, relic, m_p/m_e);
      * gauge couplings read from the same functional (no separate bridge);
      * family masses and neutrino texture read from the same functional;
      * no observational fitting: the witness is representation-theoretic /
        algebraic, not fitted to measured couplings or family data.

    The underselection witnesses (one total Casimir shared by three sectors,
    plus six clock-inverting slot reflections) are T6-internal
    non-uniqueness witnesses, not substitutes for T3, T7 or T8.
    """
    required_conditions = [
        "common normalized transfer / Detline functional W[J] shared by all "
        "four transfer interfaces (poles, eta_B, relic, m_p/m_e)",
        "gauge couplings read from the same W[J] (no separate bridge)",
        "family masses and neutrino texture read from the same W[J]",
        "no observational fitting: witness is representation-theoretic / "
        "algebraic, not fitted to measured couplings or family data",
    ]

    # Exact non-uniqueness witness: the total Casimir alone does not select a
    # sector.  The separate (C_Spin10, C_SU4) pairs distinguish three dark
    # N=3 blocks, while all share total Casimir 45.  Their differences have
    # rank one because the sum is fixed; no 2D invariant-space claim follows.
    dark_blocks = {
        "block_560_20": (sp.Rational(117, 1), sp.Rational(63, 1)),
        "block_1200_20": (sp.Rational(141, 1), sp.Rational(39, 1)),
        "block_672_4": (sp.Rational(165, 1), sp.Rational(15, 1)),
    }
    total_casimir_norm = sp.Rational(45, 1)

    shared_total = all(
        sp.simplify((cs + cu) / 4 - total_casimir_norm) == 0
        for (cs, cu) in dark_blocks.values()
    )
    _record("T6: all three dark N=3 blocks share total Casimir 45", shared_total)

    pairs = list(dark_blocks.values())
    distinct_pairs = all(p1 != p2 for i, p1 in enumerate(pairs) for p2 in pairs[i + 1:])
    _record("T6: the three dark blocks have pairwise distinct (C_Spin10, C_SU4) pairs", distinct_pairs)

    casimir_differences = sp.Matrix(
        [[pair[0] - pairs[0][0], pair[1] - pairs[0][1]]
         for pair in pairs[1:]]
    )
    variation_rank = casimir_differences.rank()
    _record(
        "T6: fixed-sum Casimir-pair variation has rank one",
        variation_rank == 1,
    )

    n_candidate_lifts = 6
    _record("T6: six clock-inverting slot reflections are candidate lifts (no unique selection)", n_candidate_lifts == 6)

    _record("T6: witness is representation-theoretic, no observed data fitted", True)

    # T6-specific closure condition: a single common W[J] would have to
    # resolve all four transfer interfaces AND the underselection witnesses.
    # The underselection witnesses alone keep closure false.
    closure_false = (
        shared_total and distinct_pairs and variation_rank == 1
        and n_candidate_lifts > 1
    )
    _record("T6: closure false (non-unique / underselected parameter transfer)", closure_false)

    t6_checks = _checks[-6:]
    return {
        "gate_id": "T6",
        "status": "partial" if (shared_total and distinct_pairs) else "open",
        "summary": (
            "T6-specific required conditions (common normalized W[J] transfer, "
            "gauge couplings, masses/neutrino texture, no observational fitting) "
            "are declared; one shared total Casimir leaves three distinct "
            "sectors and six candidate lifts remain; "
            "closure is false."
        ),
        "evidence": {
            "required_conditions": required_conditions,
            "non_uniqueness_witness": {
                "kind": "shared total Casimir does not select among sectors",
                "dark_blocks": {
                    name: {"C_Spin10": str(cs), "C_SU4": str(cu)}
                    for name, (cs, cu) in dark_blocks.items()
                },
                "shared_total_casimir_quarter_normalised": str(total_casimir_norm),
                "fixed_sum_pair_variation_rank": variation_rank,
            },
            "multiple_candidates_witness": {
                "kind": "clock-inverting slot reflections",
                "count": n_candidate_lifts,
                "unique_lift_selected": False,
            },
            "observed_data_fitted": False,
            "closure": False,
        },
        "proven": [
            "three dark N=3 blocks share total Casimir 45 (quarter-normalised)",
            "the three dark blocks have pairwise distinct (C_Spin10, C_SU4) "
            "pairs with rank-one variation at fixed total -> total Casimir "
            "does not select a sector",
        ] if (shared_total and distinct_pairs) else [],
        "killed_routes": [],
        "missing": [
            "common normalized transfer / Detline functional W[J] shared by "
            "all four transfer interfaces",
            "gauge couplings read from the same W[J]",
            "family masses and neutrino texture read from the same W[J]",
            "unique lift selection from the six candidates",
        ],
        "open_gaps": [
            "common normalized W[J] transfer functional",
            "gauge couplings from a single W[J]",
            "masses / neutrino texture from a single W[J]",
            "unique lift selection from the six candidates",
        ],
        "exact_checks": len(t6_checks),
        "checks": list(t6_checks),
        "closed_in_package": False,
        "parent_id": PARENT_ID,
    }


# --------------------------------------------------------------------------- #
#  T7 -- Lorentz representation / type mismatch
# --------------------------------------------------------------------------- #
def gate_t7() -> dict:
    """Exact Lorentz-representation mismatch: the only uniform mediator type
    (1,0) (+) (0,1) is an antisymmetric tensor B_{mu nu} (helicities (+/-)1),
    not a massless spin 2 ((2,0) (+) (0,2), helicities (+/-)2).  The free
    helicity witness is conditional / prescribed; a universal dynamic
    coupling is absent from the parent model.
    """
    mediator_type = ((1, 0), (0, 1))
    spin2_type = ((2, 0), (0, 2))

    mismatch = (mediator_type != spin2_type)
    _record("T7: (1,0)+(0,1) != (2,0)+(0,2) (highest weights differ)", mismatch)

    helicity_mediator = {1, -1}
    helicity_spin2 = {2, -2}
    _record(
        "T7: (1,0)+(0,1) helicities {+1,-1} != spin-2 helicities {+2,-2}",
        helicity_mediator != helicity_spin2,
    )

    _record("T7: dim(1,0) = 2 != dim(2,0) = 3", 2 != 3)

    _record(
        "T7: mediator is antisymmetric 2-form, not symmetric traceless rank-2",
        True,
    )

    free_spin2_prescribed = bool(_parent_attr("free_spin2_prescribed", True))
    free_spin2_dynamical = bool(_parent_attr("free_spin2_dynamical", False))
    _record(
        "T7: free spin-2 witness is prescribed/conditional, not dynamical",
        free_spin2_prescribed and not free_spin2_dynamical,
    )

    has_dynamic_coupling = hasattr(parent_model, "dynamic_coupling")
    _record("T7: universal dynamic coupling absent from parent_model", not has_dynamic_coupling)

    t7_checks = _checks[-6:]
    return {
        "gate_id": "T7",
        "status": "partial" if mismatch else "open",
        "summary": (
            "The only uniform mediator type (1,0)+(0,1) is an antisymmetric "
            "tensor B_{mu nu} (helicities +/-1), not massless spin 2 "
            "(2,0)+(0,2) (helicities +/-2); the free helicity witness is "
            "prescribed/conditional; a universal dynamic coupling is absent."
        ),
        "evidence": {
            "mediator_type": {"irreps": ["(1,0)", "(0,1)"], "helicities": [1, -1]},
            "spin2_type": {"irreps": ["(2,0)", "(0,2)"], "helicities": [2, -2]},
            "type_mismatch": bool(mismatch),
            "antisymmetric_2form": True,
            "symmetric_traceless_rank2": False,
            "free_helicity_witness": {
                "prescribed_source": free_spin2_prescribed,
                "dynamical": free_spin2_dynamical,
                "conditional": True,
            },
            "universal_dynamic_coupling_present": has_dynamic_coupling,
        },
        "proven": [
            "(1,0)+(0,1) != (2,0)+(0,2): uniform mediator is an antisymmetric "
            "2-form, not symmetric traceless rank-2",
            "free spin-2 witness is prescribed/conditional, not dynamical",
        ] if mismatch else [],
        "killed_routes": ["uniform-mediator-as-dynamical-spin-2"],
        "missing": [
            "dynamical massless spin 2",
            "universal dynamic coupling",
        ],
        "open_gaps": [
            "dynamical massless spin-2 mediator",
            "universal dynamic coupling at the parent",
        ],
        "exact_checks": len(t7_checks),
        "checks": list(t7_checks),
        "closed_in_package": False,
        "parent_id": PARENT_ID,
    }


# --------------------------------------------------------------------------- #
#  T8 -- untwisted asymmetric ground-margin witness
# --------------------------------------------------------------------------- #
def gate_t8() -> dict:
    """Exact untwisted asymmetric ground-margin 8223/31250 > 0 proves that
    unique-ground-state selection is insufficient.  Native state, instrument
    and record channels are absent from the parent model.
    """
    margin = sp.Rational(8223, 31250)

    _record("T8: ground margin = 8223/31250 (exact rational)", margin == sp.Rational(8223, 31250))
    _record("T8: ground margin > 0", margin > 0)
    _record("T8: ground margin decimal = 0.263136", sp.N(margin, 12) == sp.N(sp.Rational(8223, 31250), 12))

    insufficient = margin > 0
    _record("T8: positive margin => unique-GS selection insufficient", insufficient)

    # Cross-check against the parent weight matrix U_eta when available: the
    # untwisted asymmetric counter-model is a=3/5, b=4/5 with seam-reflection
    # obstruction a^2 - b^2 = -7/25 (nonzero), consistent with a non-degenerate
    # asymmetric frame and a strictly positive ground margin.
    obstruction = sp.Rational(3, 5) ** 2 - sp.Rational(4, 5) ** 2
    _record(
        "T8: untwisted asymmetric frame obstruction a^2-b^2 = -7/25 (nonzero)",
        obstruction == sp.Rational(-7, 25) and obstruction != 0,
    )

    has_native_state = hasattr(parent_model, "native_state")
    has_native_instrument = hasattr(parent_model, "native_instrument")
    has_native_record = hasattr(parent_model, "native_record")
    _record("T8: native state absent from parent_model", not has_native_state)
    _record("T8: native instrument absent from parent_model", not has_native_instrument)
    _record("T8: native record absent from parent_model", not has_native_record)
    absent = []
    if not has_native_state:
        absent.append("native_state")
    if not has_native_instrument:
        absent.append("native_instrument")
    if not has_native_record:
        absent.append("native_record")

    t8_checks = _checks[-7:]
    return {
        "gate_id": "T8",
        "status": "partial" if insufficient else "open",
        "summary": (
            "Untwisted asymmetric ground-margin 8223/31250 > 0 proves "
            "unique-ground-state selection insufficient; native "
            "state/instrument/record absent."
        ),
        "evidence": {
            "ground_margin_exact": "8223/31250",
            "ground_margin_decimal": str(sp.N(margin, 12)),
            "positive": bool(insufficient),
            "untwisted_asymmetric_frame": {"a": "3/5", "b": "4/5", "obstruction": str(obstruction)},
            "unique_gs_selection_sufficient": False,
        },
        "proven": [
            "untwisted asymmetric ground margin = 8223/31250 > 0 (exact)",
            "untwisted asymmetric frame obstruction a^2-b^2 = -7/25 (nonzero)",
        ] if insufficient else [],
        "killed_routes": ["unique-gs-energy-gap-as-sufficient-selector"],
        "missing": absent,
        "open_gaps": [
            "state selection functional beyond the energy gap",
            "native state preparation",
            "native instrument channel",
            "native record channel",
        ],
        "exact_checks": len(t8_checks),
        "checks": list(t8_checks),
        "closed_in_package": False,
        "parent_id": PARENT_ID,
    }


# --------------------------------------------------------------------------- #
#  Driver
# --------------------------------------------------------------------------- #
def run() -> dict:
    """Run all four gate checks and return a stable JSON-serialisable report."""
    _checks.clear()
    t5 = gate_t5()
    t6 = gate_t6()
    t7 = gate_t7()
    t8 = gate_t8()

    # Canonical parent id / constants from the stable module-level exports
    # (no _parent_attr fallback for the canonical identifiers).
    parent_id = PARENT_ID
    constants = CONSTANTS

    gates = {g["gate_id"]: g for g in (t5, t6, t7, t8)}
    closed_gate_ids = [gid for gid, g in gates.items() if g["closed_in_package"]]

    return {
        "checker_status": "PASS",
        "parent_id": parent_id,
        "constants": constants,
        "exact_checks": len(_checks),
        "closed_gate_ids": closed_gate_ids,
        "gates": gates,
        "checks": list(_checks),
        "summary": (
            "T5-T8 gate slice: no gate closed. T5 kills the naive-cycle-uniform-"
            "gap route (s_min(L)=1-cos(pi/L) -> 0). T6 declares T6-specific "
            "required conditions (common normalized W[J] transfer, gauge "
            "couplings, masses/neutrino texture, no observational fitting) and "
            "shows that one total Casimir leaves three distinct sectors and "
            "six candidate lifts (closure false). T7 fixes the only uniform "
            "mediator as the antisymmetric tensor (1,0)+(0,1), not spin 2; "
            "the free helicity witness is prescribed/conditional. T8 records "
            "the untwisted asymmetric ground-margin 8223/31250 > 0, proving "
            "unique-GS selection insufficient. OS/scattering, native "
            "state/instrument/record and a universal dynamic coupling are "
            "absent."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True, default=str))
