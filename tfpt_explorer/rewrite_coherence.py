"""Source-derived coherence constraints on a future TFPT graph execution.

This is the existing SU(5)_1 current-block connection, not a new rewrite
model.  Its curvature vanishes although overlapping residues do not
commute.  The physical block is a line in two invariant tensor coordinates;
its fractional collision phases cancel against the existing E8 partner.
Neither that line nor the fixed finite trimer carrier is the whole affine
state space, and insertion positions do not acquire a physical-time meaning.
"""

from __future__ import annotations

from functools import lru_cache
from fractions import Fraction
import itertools
from typing import Any

import sympy as sp

from .current_block_geometry import build_current_block_geometry_data
from .cartan_source import _lattice_data
from .hecke_source import build_hecke_source_data


def _phase_bracket_certificate(phases: dict[tuple[int, ...], Fraction]) -> dict[str, Any]:
    """Check phases against every nonzero root bracket of the actual source.

    Values are turns modulo one. Cartan currents have phase zero. The fixed
    nonzero Chevalley/cocycle constants cancel from the homomorphism test.
    This also detects arbitrary root phases that are not lattice characters.
    """
    root_set = set(phases)
    brackets = mismatches = opposite_mismatches = 0
    for alpha, phase in phases.items():
        if (phase + phases[tuple(-a for a in alpha)]) % 1:
            opposite_mismatches += 1
        for beta, other_phase in phases.items():
            total = tuple(a + b for a, b in zip(alpha, beta))
            if total in root_set:
                brackets += 1
                mismatches += bool((phase + other_phase - phases[total]) % 1)
    return {"root_sum_brackets": brackets, "root_sum_mismatches": mismatches,
            "opposite_root_pairs": len(phases),
            "opposite_root_mismatches": opposite_mismatches,
            "exact": mismatches == opposite_mismatches == 0}


def _phase_ward_compatibility() -> dict[str, Any]:
    """Connect the actual Hecke character extensions to the current source.

    This is diagonal automorphism covariance of the full E8 current algebra,
    not an identification of a Hecke inclusion with KZ parallel transport.
    """
    roots = _lattice_data()["root_coordinates"]
    rows = []
    example_phases = None
    for example in build_hecke_source_data()["data"]["general_phase_extension"]["examples"]:
        theta = tuple(Fraction(value) for value in example["theta"])
        phases = {root: sum((t * a / 2 for t, a in zip(theta, root)), Fraction()) % 1
                  for root in roots}
        certificate = _phase_bracket_certificate(phases)
        rows.append({"depth": example["depth"], "phase_order": example["phase_order"],
                     **certificate,
                     "root_phase_turns": sorted({str(value) for value in phases.values()}),
                     "cartan_directions_fixed": 8,
                     "diagonal_casimir_invariant": certificate["opposite_root_mismatches"] == 0})
        if example["depth"] == 2:
            example_phases = phases
    assert example_phases is not None
    root = next(root for root, phase in example_phases.items() if phase)
    broken_phases = dict(example_phases)
    broken_phases[root] = (broken_phases[root] + Fraction(1, 2)) % 1
    broken = _phase_bracket_certificate(broken_phases)
    return {
        "formula": "U_theta e_alpha U_theta^(-1)=exp(pi*i*theta.alpha)e_alpha; U_theta H_i U_theta^(-1)=H_i",
        "all_depth_proof": "A lattice character obeys chi(alpha+beta)=chi(alpha)chi(beta) and chi(alpha)chi(-alpha)=1. Thus every nonzero root bracket and the invariant form are preserved. The same multiplicativity preserves the lattice-VOA cocycle OPE, with unchanged Heisenberg oscillators and conformal vector.",
        "casimir": "Omega=sum_i H_i tensor H^i + sum_alpha e_alpha tensor e^alpha; (U tensor U) Omega (U tensor U)^(-1)=Omega",
        "kz_implication": "Diagonal U on all legs preserves the full E8 Casimir. For a Casimir-built KZ connection on modules where that equation applies, this implies covariance of parallel transport. The actual E8 current correlators instead obey their Ward recursion; their weight-one adjoint currents are vacuum descendants, not integrable E8 level-one primaries. The independently verified SU5 primary-factor KZ connection above is kept separate. No Hecke inclusion is identified with KZ transport.",
        "ward_implication": "Every nonzero vacuum current correlator has total lattice charge zero, so the product of all insertion phases is one. For a noninvariant state the state must also be transformed.",
        "examples": rows,
        "single_leg_control": {"root_simple_coordinates": list(root),
                               "phase_turns": str(example_phases[root]),
                               "diagonal_phase_turns": "0",
                               "meaning": "Changing one insertion alone changes this Casimir term. Only simultaneous diagonal transport cancels opposite-root phases."},
        "noncharacter_control": broken,
        "scope": "Exact charged-source automorphism compatibility for every rational phase extension. A proper Hecke projection is not an algebra homomorphism; its missing charged sectors must remain active for full-source Ward identities. Ordinary homogeneous primary KZ equations are not imposed on E8 current correlators. No participant, event rate, physical time, or spacetime is selected. The 2x2 SU5 tensor-coordinate residues are not identified with this 248-dimensional current action.",
    }


def _matrix_strings(matrix: sp.MatrixBase) -> list[list[str]]:
    return [[str(sp.factor(value)) for value in row] for row in matrix.tolist()]


def _commutator(left: sp.MatrixBase, right: sp.MatrixBase) -> sp.Matrix:
    return sp.simplify(left * right - right * left)


def _connection(
    residues: dict[tuple[int, int], sp.Matrix],
    positions: tuple[sp.Symbol, ...],
) -> list[sp.Matrix]:
    return [
        sum(
            (
                residues[tuple(sorted((i, j)))] / (6 * (positions[i] - positions[j]))
                for j in range(len(positions)) if i != j
            ),
            sp.zeros(2),
        )
        for i in range(len(positions))
    ]


def _curvature(
    residues: dict[tuple[int, int], sp.Matrix],
    positions: tuple[sp.Symbol, ...],
) -> dict[str, sp.Matrix]:
    """Compute [partial_i-Gamma_i, partial_j-Gamma_j] exactly."""
    connection = _connection(residues, positions)
    return {
        f"{i + 1}{j + 1}": (
            -connection[j].diff(positions[i])
            + connection[i].diff(positions[j])
            + _commutator(connection[i], connection[j])
        ).applyfunc(sp.factor)
        for i, j in itertools.combinations(range(len(positions)), 2)
    }


@lru_cache(maxsize=1)
def build_rewrite_coherence_data() -> dict[str, Any]:
    """Return exact, JSON-safe coherence data from the existing source."""
    current = build_current_block_geometry_data()["data"]
    kz = current["correlator"]["KZ"]
    residues = {
        (0, 1): sp.Matrix(kz["omega12"]),
        (1, 2): sp.Matrix(kz["omega23"]),
        (0, 2): sp.Matrix(kz["omega13"]),
    }
    a, b, c = residues[0, 1], residues[1, 2], residues[0, 2]
    positions = sp.symbols("z1 z2 z3", nonzero=True)
    z1, z2, z3 = positions
    differences = {(0, 1): z1 - z2, (0, 2): z1 - z3, (1, 2): z2 - z3}
    ratio = (z1 - z2) / (z2 - z3)
    vector = sp.Matrix([1, ratio])

    # Exponents of the already verified source factorization.  Powers are
    # handled through logarithmic derivatives and integer exponent addition,
    # avoiding any false globally single-valued fractional-power identity.
    su5_exponents = {(0, 1): -sp.Rational(4, 5), (0, 2): -sp.Rational(1, 5), (1, 2): sp.Rational(1, 5)}
    partner_exponents = {(0, 1): -sp.Rational(6, 5), (0, 2): sp.Rational(6, 5), (1, 2): -sp.Rational(6, 5)}
    connection = _connection(residues, positions)
    horizontal_residuals = [
        (
            vector.diff(position)
            + sum(exponent * sp.diff(differences[pair], position) / differences[pair]
                  for pair, exponent in su5_exponents.items()) * vector
            - connection[index] * vector
        ).applyfunc(sp.factor)
        for index, position in enumerate(positions)
    ]
    curvature = _curvature(residues, positions)
    braid_relations = {
        "[Omega12,Omega13+Omega23]": _commutator(a, b + c),
        "[Omega23,Omega12+Omega13]": _commutator(b, a + c),
        "[Omega13,Omega12+Omega23]": _commutator(c, a + b),
    }
    overlapping = _commutator(a, b)
    # A meaningful negative control: omit a genuine source channel.  Merely
    # demanding commuting overlapping updates does not reproduce this source.
    omitted = dict(residues)
    omitted[0, 2] = sp.zeros(2)
    omitted_curvature = _curvature(omitted, positions)
    negative_witness = omitted_curvature["12"].subs({z1: -1, z2: 0, z3: 1})

    full_coefficient_a = sp.prod(
        differences[pair] ** (su5_exponents[pair] + partner_exponents[pair])
        for pair in differences
    )
    expected_a = (z1 - z3) / ((z1 - z2) ** 2 * (z2 - z3))
    full_factorization_exact = sp.factor(full_coefficient_a - expected_a) == 0
    collisions = []
    for pair in ((0, 1), (1, 2), (0, 2)):
        su5 = su5_exponents[pair]
        partner = partner_exponents[pair]
        # In the 23 collision, the second tensor coordinate has a simple
        # pole.  Integer shifts change leading powers but not loop phases.
        coordinate_shift = -1 if pair == (1, 2) else 0
        collisions.append({
            "pair": f"{pair[0] + 1}{pair[1] + 1}",
            "orientation": "opposite" if pair != (0, 2) else "same",
            "su5_scalar_exponent": str(su5),
            "su5_leading_exponent": str(su5 + coordinate_shift),
            "partner_exponent": str(partner),
            "full_leading_exponent": str(su5 + partner + coordinate_shift),
            "su5_phase_turns_mod_one": str(su5 % 1),
            "partner_phase_turns_mod_one": str(partner % 1),
            "full_phase_turns_mod_one": str((su5 + partner) % 1),
            "su5_phase": f"exp(2*pi*i*({su5}))",
            "partner_phase": f"exp(2*pi*i*({partner}))",
            "full_phase": "1" if (su5 + partner).is_integer else "nontrivial",
        })

    # The integrable highest weights of su(5) at level 1 have Dynkin-label
    # sum <= 1.  In the A4 lattice VOA, fusion preserves its Z5 center charge.
    # Only the vacuum has charge zero, hence 5 x bar5 has one physical
    # fusion channel; the classical adjoint is nonintegrable at this level.
    integrable_weights = [weight for weight in itertools.product(range(2), repeat=4) if sum(weight) <= 1]
    charge_zero = [weight for weight in integrable_weights if sum((i + 1) * value for i, value in enumerate(weight)) % 5 == 0]

    s = sp.symbols("s", real=True)
    moved_ratio = (1 + s) / (1 - s)
    w_coefficient = sp.sqrt(3) * (1 + moved_ratio)
    z_coefficient = sp.sqrt(2) * (1 - moved_ratio)
    z_weight = sp.factor(z_coefficient**2 / (w_coefficient**2 + z_coefficient**2))
    sample_matches = all(
        sp.factor(z_weight.subs(s, sp.Rational(str(sample["s"]))) - sp.Rational(sample["Z_probability_exact"])) == 0
        for sample in current["position_samples"]
    )
    six = current["six_current_cluster_test"]
    sectors = six["local_sector_decomposition"]
    rank_certificate = sectors["fundamental_multiplicity_rank"]
    phase_ward = _phase_ward_compatibility()
    checks = [
        {"name": "Originale KZ-Reste sind auf der physikalischen Linie exakt null", "ok": all(value == sp.zeros(2, 1) for value in horizontal_residuals), "actual": [_matrix_strings(value) for value in horizontal_residuals], "expected": "three zero 2x1 residuals", "method": "exact source residues and logarithmic derivatives"},
        {"name": "Ueberlappende Schritte kommutieren nicht, erfuellen aber die infinitesimale Zopfrelation", "ok": overlapping != sp.zeros(2) and all(value == sp.zeros(2) for value in braid_relations.values()), "actual": _matrix_strings(overlapping), "expected": "nonzero commutator, zero three-term relations", "method": "exact rational matrix multiplication"},
        {"name": "Die vollstaendige Quellverbindung hat exakt verschwindende Kruemmung", "ok": all(value == sp.zeros(2) for value in curvature.values()), "actual": {key: _matrix_strings(value) for key, value in curvature.items()}, "expected": "all three curvature matrices zero", "method": "symbolic derivatives and commutators"},
        {"name": "Weglassen eines Quellkanals zerstoert die Koharenz", "ok": negative_witness != sp.zeros(2), "actual": _matrix_strings(negative_witness), "expected": "nonzero curvature after deleting Omega13", "method": "negative control at (-1,0,1)"},
        {"name": "Gebrochene SU5-Phasen werden vom E8-Partner exakt kompensiert", "ok": full_factorization_exact and all(row["full_phase"] == "1" for row in collisions) and all(row["su5_phase_turns_mod_one"] != "0" for row in collisions), "actual": [{"pair": row["pair"], "su5_turns": row["su5_phase_turns_mod_one"], "partner_turns": row["partner_phase_turns_mod_one"], "full_phase": row["full_phase"]} for row in collisions], "expected": "rational full Ward block with trivial pure-loop phase", "method": "exact exponent sums and existing Ward tensor"},
        {"name": "Zwei Tensorkoordinaten bedeuten einen physikalischen SU5-Level-1-Fusionsblock", "ok": len(integrable_weights) == 5 and charge_zero == [(0, 0, 0, 0)], "actual": [list(weight) for weight in charge_zero], "expected": [[0, 0, 0, 0]], "method": "integrable A4 level-one weights and conserved Z5 fusion charge"},
        {"name": "Bewegte Marken erzeugen den bereits gemessenen Z-Anteil", "ok": sample_matches and z_weight != 0, "actual": str(z_weight), "expected": "2*s^2/(3+2*s^2), agrees with all 17 original samples", "method": "exact W/Z decomposition using their inherited tensor Gram form"},
        {"name": "Endliche Rekursion erhaelt den vollstaendigen lokalen 125-Traeger", "ok": rank_certificate["rank_for_0_lt_t_lt_1"] == 2 and six["direct_Ward_pattern_mismatches"] == 0 and six["affine_carry_grading"]["dimension"] == 125, "actual": rank_certificate["local_schmidt_support"], "expected": "2*5+45+70=125 at every finite 0<t<1", "method": "reuse exact six-current Ward/rank certificate, not a new truncation"},
        {"name": "Hecke-Phasen erhalten die geladenen Quellklammern und den diagonalen Casimir", "ok": all(row["exact"] and row["diagonal_casimir_invariant"] and row["root_sum_brackets"] == 13440 for row in phase_ward["examples"]), "actual": phase_ward["examples"], "expected": "all 13440 nonzero root-sum brackets and 240 opposite pairs at each illustrated depth", "method": "actual E8 root action plus all-depth character multiplicativity proof"},
        {"name": "Einseitige oder frei geaenderte Feldphasen bestehen den Quellenvergleich nicht", "ok": phase_ward["single_leg_control"]["phase_turns"] != "0" and not phase_ward["noncharacter_control"]["exact"], "actual": phase_ward["noncharacter_control"], "expected": "nonzero bracket defects after a single field phase is changed", "method": "negative source-algebra control; diagonal transport and single-leg change kept distinct"},
    ]
    return {
        "data": {
            "verdict": "EXACT_SOURCE_COHERENCE; PHYSICAL_REWRITE_RULE_NOT_SELECTED",
            "title": "Reihenfolge ohne Informationsverlust",
            "plain_language": "Die Quellgleichungen erlauben verschiedene Rechenwege fuer denselben Vorgang. Die Zwischeninformationen muessen mitgehen: Einzelne Schritte duerfen nicht beliebig vertauscht und Teilphasen nicht als neue Weltgesetze behandelt werden.",
            "connection": {
                "formula": "nabla_i=partial_i-sum_(j!=i) Omega_ij/[6(z_i-z_j)]",
                "residue_sum": _matrix_strings(a + b + c),
                "overlap_commutator": _matrix_strings(overlapping),
                "infinitesimal_braid_relations": {key: _matrix_strings(value) for key, value in braid_relations.items()},
                "curvature": {key: _matrix_strings(value) for key, value in curvature.items()},
                "flat": all(value == sp.zeros(2) for value in curvature.values()),
                "missing_channel_control": {"deleted": "Omega13", "positions": [-1, 0, 1], "curvature12": _matrix_strings(negative_witness)},
                "meaning": "Parallel transport agrees along homotopic collision-free paths. Overlapping residue operations themselves do not commute.",
            },
            "physical_block": {
                "invariant_tensor_coordinate_dimension": 2,
                "physical_level_one_fusion_block_dimension": len(charge_zero),
                "integrable_dynkin_labels": [list(weight) for weight in integrable_weights],
                "excluded_classical_adjoint": {"dynkin_labels": [1, 0, 0, 1], "required_level": 2},
                "horizontal_line": "P_SU5*(1,z12/z23)",
                "SU5_factor": current["correlator"]["SU5_factor"],
                "partner_factor": current["correlator"]["full_E8_partner_factor"],
                "full_Ward_coefficients": [str(sp.factor(full_coefficient_a)), str(sp.factor(full_coefficient_a * ratio))],
                "collisions": collisions,
                "loop_scope": "A positive full winding of one marked insertion around another, with labels restored; not a half-exchange formula.",
                "full_current_monodromy": "identity on this rational four-current Ward tensor",
            },
            "carry_requirements": {
                "four_point": {"Z_weight": str(z_weight), "samples_agree": sample_matches, "source_sample_count": len(current["position_samples"]), "meaning": "The unique physical horizontal line moves in the two tensor coordinates. Fixed W-only projection is not closed away from the harmonic marks."},
                "six_point": {"split": sectors["representation_split"], "rank": 125, "domain": "0<epsilon/L<1", "certificate": rank_certificate["local_schmidt_support"], "finite_leakage_samples": [{"epsilon_over_L": row["epsilon_over_L"], "leakage_fraction": row["leakage_fraction"]} for row in six["finite_separation_samples"]]},
                "affine": "Finite 125-dimensional trimer support does not truncate the unbounded affine descendant tower.",
                "distinct_carries": "KZ collision phases, affine descendants and the separate 8-bit Cartan-lift characters have different definitions. No identification between them is used.",
            },
            "phase_ward_compatibility": phase_ward,
            "graph_implication": {
                "positive": "A source-respecting rewrite can use coherent OPE/parallel-transport identities instead of falsely demanding pairwise commutation of overlapping updates.",
                "required_data": ["ordered charged field labels and partner sector", "amplitudes and relative phases", "positions or their relational moduli and allowed paths", "all local source sectors needed at finite separation"],
                "not_selected": ["which insertions or participants exist next", "a graph growth or event-selection rule", "a common physical state and physical time", "a 3+1-dimensional spacetime interpretation"],
                "scope": "Source consistency on an already supplied configuration space; not Wolfram causal invariance, a universal rewrite confluence proof, or a derivation of spacetime.",
            },
        },
        "checks": checks,
        "sources": [
            "tfpt_explorer/current_block_geometry.py::_kz_certificate (actual SU5_1 residues)",
            "tfpt_explorer/current_block_geometry.py::build_current_block_geometry_data (actual E8_1 Ward tensor and finite carry)",
            "https://arxiv.org/abs/hep-th/0012099 (Todorov and Hadjiivanov, equations 2.2-2.9: flat KZ transport)",
            "https://aif.centre-mersenne.org/item/AIF_1987__37_4_139_0/ (Kohno, braid monodromy and Yang-Baxter relations)",
        ],
    }
