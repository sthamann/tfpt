"""The original determinant carry lifts to the marked E8/D8 source grading.

This is an internal group and source-field dictionary. The exterior-slot
grading, CAR field parity, bosonic E8 glue grading, and four-dimensional
spin-charge postulate are explicitly different objects.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from typing import Any

import sympy as sp

from .current_block_geometry import _actual_current_source
from .flavor_path_transport import exact_clock_dictionary, integrate_path_transport
from .neutral_source_response import exact_joint_flavor_response


_A3_TO_D3 = sp.Rational(1, 2) * sp.Matrix([
    [1, 1, -1, -1],
    [1, -1, 1, -1],
    [1, -1, -1, 1],
])


def a3_sumzero_to_d3(weight: tuple[Any, Any, Any, Any]) -> tuple[sp.Expr, ...]:
    """Map the redundant sum-zero A3 coordinates to three orthogonal D3 axes."""
    vector = sp.Matrix(weight)
    if vector.shape != (4, 1) or sp.simplify(sum(vector)) != 0:
        raise ValueError("an A3 weight needs four coordinates with sum zero")
    return tuple(sp.simplify(value) for value in _A3_TO_D3 * vector)


def d3_to_a3_sumzero(weight: tuple[Any, Any, Any]) -> tuple[sp.Expr, ...]:
    """Inverse of :func:`a3_sumzero_to_d3` on the A3 sum-zero hyperplane."""
    vector = sp.Matrix(weight)
    if vector.shape != (3, 1):
        raise ValueError("a D3 weight needs three orthogonal coordinates")
    return tuple(sp.simplify(value) for value in _A3_TO_D3.T * vector)


def spinor_pair_kernel_coefficients(weights: tuple[Any, ...]) -> tuple[sp.Expr, ...]:
    """Coefficients of exp(2 sum_k w_k z**k/k), through the supplied order.

    This computes the neutral eight-copy current reference.  It neither
    constructs microscopic charged fields nor supplies the eight copies.
    For Gaussian weights, each coefficient needs only finitely many w_k.
    """
    exact_weights = tuple(sp.sympify(value) for value in weights)
    if any(value.is_real is not True or value.is_finite is not True
           or value.is_nonnegative is not True
           or (1-value).is_nonnegative is not True
           for value in exact_weights):
        raise ValueError("pair-kernel filter weights must be real and lie in [0, 1]")
    coefficients = [sp.Integer(1)]
    for degree in range(1, len(exact_weights) + 1):
        coefficients.append(sp.simplify(
            sp.Rational(2, degree) * sum(exact_weights[k-1] * coefficients[degree-k]
                                        for k in range(1, degree+1))
        ))
    return tuple(coefficients)


def _double_twist_dictionary(source: dict[str, Any]) -> dict[str, Any]:
    """Exact charge dictionary for the conditional eight-channel CAR source.

    The finite order-four flux-register square and the internal D5+D3 glue
    grade are deliberately kept separate.  The former does not by itself
    construct the latter as a support-localized microscopic field.
    """
    chevalley = source["chevalley"]
    roots = tuple(chevalley.roots)
    d8_roots = tuple(root for root in roots if all(value % 2 == 0 for value in root))
    spinor_roots = tuple(root for root in roots if all(abs(value) == 1 for value in root))
    block_roots = tuple(
        root for root in d8_roots
        if all(value == 0 for value in root[:5]) or all(value == 0 for value in root[5:])
    )
    mixed_roots = tuple(root for root in d8_roots if root not in block_roots)

    # The table stores doubled orthogonal charges.  Thus q=lambda/2=(1/4)^8
    # and lambda=(1/2)^8 is represented by the actual E8 root (1,...,1).
    lambda_root = (1,) * 8
    lambda_adjoint = (-1,) * 8
    lambda_vector = sp.Matrix(lambda_root) / 2
    q_vector = lambda_vector / 2
    q_norm2 = q_vector.dot(q_vector)
    lambda_norm2 = lambda_vector.dot(lambda_vector)
    fusion_exponent = lambda_norm2 / 2 - q_norm2
    q_pairings = [sp.Rational(sum(root), 8) for root in d8_roots]
    lambda_pairings = [sp.Rational(sum(root), 4) for root in d8_roots]
    q_local_count = sum(value.q == 1 for value in q_pairings)
    lambda_local_count = sum(value.q == 1 for value in lambda_pairings)
    glue_grades = Counter((-sum(root[5:])) % 4 for root in spinor_roots)
    even_spinor_chirality = all(sum(value < 0 for value in root) % 2 == 0
                                for root in spinor_roots)

    # Generate with nonzero brackets of the original Chevalley algebra, not
    # by a dimension count or by adding formal charges without coefficients.
    generated = {chevalley.ridx[root] for root in (*block_roots, lambda_root, lambda_adjoint)}
    closure_counts = [len(generated)]
    nonzero_new_brackets = []
    while True:
        new_roots: set[int] = set()
        witnessed = 0
        for left in generated:
            for right in generated:
                for output, coefficient in chevalley.bracket(left, right).items():
                    if coefficient and output < chevalley.nR and output not in generated:
                        new_roots.add(output)
                        witnessed += 1
        if not new_roots:
            break
        generated.update(new_roots)
        closure_counts.append(len(generated))
        nonzero_new_brackets.append(witnessed)

    cartan_rows = []
    for index in generated:
        bracket = chevalley.bracket(index, chevalley.opp[index])
        cartan_rows.append([bracket.get(chevalley.nR + axis, 0)
                            for axis in range(chevalley.rank)])
    cartan_rank = int(sp.Matrix(cartan_rows).rank())
    generated_roots = {roots[index] for index in generated}
    generated_spinors = generated_roots.intersection(spinor_roots)
    generated_mixed = generated_roots.intersection(mixed_roots)

    omega_f = (sp.Rational(3, 4),) + (sp.Rational(-1, 4),) * 3
    mapped_omega_f = a3_sumzero_to_d3(omega_f)
    return {
        "status": "EXACT_CHARGE_AND_CHEVALLEY_CLOSURE_CONDITIONAL_ON_EIGHT_CAR_CHANNELS",
        "source_assumption": (
            "Die MMST-Quellenpraemisse deklariert 16 unabhaengige Majorana-Kopien, also acht "
            "orthogonale komplexe CAR-Kanaele. Die 10+6-Blockwirkung ist die gewaehlte "
            "D5+D3-Zielmarkierung; die Kopienzahl leitet diese Wirkung nicht her. Der unveraenderte "
            "einzelne Ny=8-QWZ-Streifen hat dagegen pro Kante genau einen komplexen chiralen Kanal "
            "und leitet die acht Kanaele nicht her. Hier wird kein neuer Quellenoperator erzeugt."
        ),
        "coordinate_map": {
            "A3_sumzero_to_D3": [[str(value) for value in row] for row in _A3_TO_D3.tolist()],
            "omega_f_A3": [str(value) for value in omega_f],
            "omega_f_D3": [str(value) for value in mapped_omega_f],
            "inverse_roundtrip": [str(value) for value in d3_to_a3_sumzero(mapped_omega_f)],
        },
        "charges": {
            "quarter_twist_q": [str(x) for x in q_vector],
            "double_twist_lambda": [str(x) for x in lambda_vector],
            "chevalley_root_doubled_lambda": list(lambda_root),
            "chevalley_root_doubled_adjoint": list(lambda_adjoint),
            "q_norm_squared": str(q_norm2), "q_conformal_weight": str(q_norm2 / 2),
            "lambda_norm_squared": str(lambda_norm2), "lambda_conformal_weight": str(lambda_norm2 / 2),
        },
        "renormalized_fusion": {
            "exponent_from_weights": str(fusion_exponent),
            "exponent_from_pairing": str(q_norm2),
            "ope": "V_{lambda/2}(z+epsilon)V_{lambda/2}(z) = epsilon^(1/2) epsilon_cocycle V_lambda(z) + ...",
            "formal_leading_coefficient": "V_lambda = formal-lim epsilon^(-1/2) epsilon_cocycle^(-1) V_{lambda/2}(z+epsilon)V_{lambda/2}(z)",
            "literal_unitary_square": False,
            "meaning": (
                "Dies ist nur der formale fuehrende OPE-Koeffizient fuer vorausgesetzte freie "
                "Boson-Intertwiner. Er ist kein stark bewiesener mikroskopischer Operatorlimes "
                "und kein Quadrat eines beschraenkten unitaeren Operators."
            ),
        },
        "locality": {
            "actual_D8_root_count": len(d8_roots),
            "q_integral_pairings": q_local_count,
            "lambda_integral_pairings": lambda_local_count,
            "q_local_to_all_even_CAR_observables": q_local_count == len(d8_roots),
            "lambda_local_to_all_even_CAR_observables": lambda_local_count == len(d8_roots),
            "lambda_local_to_full_CAR_field_algebra": False,
            "witness": {
                "even_root_e1_plus_e2": {"q_pairing": "1/2", "lambda_pairing": "1"},
                "odd_CAR_weight_e1": {"lambda_pairing": "1/2"},
            },
            "bosonic_self_statistics": True,
            "self_statistics_phase": "+1",
            "cocycle_scope": (
                "Die integralen Paarungen und h=1 erlauben die lokale bosonische Erweiterung. "
                "Ein kohaerenter D8-Gitter-2-Kozykel/Klein-Faktor und eine GSO-Chiralitaet "
                "muessen fuer einen konkreten Feldoperator dennoch gewaehlt und mikroskopisch identifiziert werden."
            ),
        },
        "grading": {
            "flux_register_square_charge_mod4": 2,
            "internal_glue_grade_lambda_mod4": (-sum(lambda_root[5:])) % 4,
            "internal_glue_grade_adjoint_mod4": (-sum(lambda_adjoint[5:])) % 4,
            "spinor_grade_counts": {str(grade): count for grade, count in sorted(glue_grades.items())},
            "CAR_parity": (
                "lambda ist ein Ramond/DHR-Intertwiner relativ zum geraden CAR-Netz, "
                "kein lokales Polynom der vollen NS-CAR-Feldalgebra mit ungeraden Feldern; Gluegrad, "
                "Fluxladung und Fermionparitaet sind verschiedene Gradierungen."
            ),
        },
        "chirality": {
            "actual_spinor_root_count": len(spinor_roots),
            "all_have_even_number_of_minus_signs": even_spinor_chirality,
            "selected_D8_half_spinor": "one of S/C, fixed here by the original E8 root table",
            "both_chiralities_may_be_adjoined": False,
        },
        "chevalley_closure": {
            "initial_D5_plus_D3_roots": len(block_roots),
            "initial_with_lambda_and_adjoint": len(block_roots) + 2,
            "root_counts_by_round": closure_counts,
            "nonzero_new_bracket_witnesses_by_round": nonzero_new_brackets,
            "generated_D5_plus_D3_roots": len(generated_roots.intersection(block_roots)),
            "generated_mixed_D8_roots": len(generated_mixed),
            "generated_spinor_roots": len(generated_spinors),
            "generated_total_roots": len(generated_roots),
            "generated_Cartan_rank": cartan_rank,
            "generated_Lie_dimension": len(generated_roots) + cartan_rank,
            "uses_actual_nonzero_brackets": True,
        },
        "microscopic_pair": {
            "status": "ANALYTIC_NEUTRAL_DISTRIBUTION_LIMIT_CONDITIONAL_ON_EIGHT_IDENTICAL_COPIES",
            "construction": "Z_t^16 [C_N^circ(a,b)]^8; every determinant uses the full occupied QWZ source",
            "limit_kernel": "(1-exp(2*pi*i*(b-a)-0))^(-2)",
            "limit_fourier_coefficients": [str(value) for value in
                                            spinor_pair_kernel_coefficients((1,) * 12)],
            "lattice_to_smoothed_error_rate": "O(N^(-3/8) (log N)^3)",
            "endpoint_grid_error_rate": "O(N^(-1/4))",
            "convergence": "distributions on T^2, including endpoint collisions; not an L1 power limit",
            "positive_pair_form": True,
            "copies_are_an_explicit_premise": True,
            "charged_local_spinor_field_constructed": False,
            "source": "tfpt_explorer/docs/session-2026-09-28/TFPT_Gesamtsynthese_2026-09-28.tex",
            "section_label": "sec:microscopicpairbridge",
            "scope": (
                "Der analytische Satz gewinnt den Gewicht-1-Paarkern aus den vollstaendigen "
                "acht Quelldeterminanten. Nullmodenladung, lokale Austauschprodukte, "
                "GSO/Kokzyklus und der Ursprung der acht Kanaele sind damit nicht bewiesen."
            ),
        },
        "microscopic_identification_remaining": (
            "Zu beweisen bleibt, dass die punktgetrennte, renormierte Fusion des originalen "
            "QWZ/CAR-Vierteltwist-Implementierers im Skalierungslimes genau den hier gewaehlten "
            "lambda-DHR-Intertwiner samt Adjungiertem, GSO-Chiralitaet, Kozykel und lokaler "
            "Traegerkontrolle ergibt. Die endliche Fluxregisterrelation D_q^2 hat diese "
            "Operatoridentitaet noch nicht bewiesen."
        ),
    }


def exterior_power(matrix: sp.Matrix, degree: int) -> sp.Matrix:
    """Exterior power in increasing lexicographic wedge order."""
    if matrix.rows != matrix.cols or not 0 <= degree <= matrix.rows:
        raise ValueError("a square matrix and an allowed exterior degree are required")
    subsets = list(combinations(range(matrix.rows), degree))
    return sp.Matrix([[matrix.extract(a, b).det() for b in subsets] for a in subsets])


def even_spin_lift_endpoint(matrix: sp.Matrix, determinant_winding: int) -> sp.Matrix:
    """Lift a U(3) path ending in SU(3), retaining its determinant winding.

    The lifted action is det(u)^(-1/2) Lambda^even(u). Only the endpoint
    and integer relative winding enter this endpoint formula; the function
    does not manufacture a path or an invariant positive source metric.
    """
    if (matrix.shape != (3, 3) or sp.simplify(matrix.det()) != 1
            or sp.simplify(matrix.H*matrix) != sp.eye(3)):
        raise ValueError("the endpoint must be a unitary determinant-one matrix in three dimensions")
    if not isinstance(determinant_winding, int):
        raise ValueError("the determinant winding must be an integer")
    return (1 if determinant_winding % 2 == 0 else -1) * sp.diag(1, exterior_power(matrix, 2))


def _matrix_json(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(sp.simplify(value)) for value in row] for row in matrix.tolist()]


@lru_cache(maxsize=1)
def build_source_spin_lift_data() -> dict[str, Any]:
    source = _actual_current_source()
    roots = tuple(source["chevalley"].roots)
    root_set = set(roots)
    records = []
    for root in roots:
        xd, xf = -sum(root[:5]), -sum(root[5:])
        records.append({"root_doubled": list(root), "X_D5": xd, "X_A3": xf,
                        "D5_phase_mod4": xd % 4, "A3_phase_mod4": xf % 4,
                        "diagonal_phase_mod4": (xd+xf) % 4,
                        "deck_sign": 1 if xd % 2 == 0 else -1})
    # All roots have either integer or half-integer coordinates. This tests
    # the whole original root table, not just the dimensions of its branches.
    central_match = all((r["X_D5"]-r["X_A3"]) % 2 == 0 for r in records)
    diagonal_trivial = all(r["diagonal_phase_mod4"] == 0 for r in records)
    deck_counts = Counter(r["deck_sign"] for r in records)
    bracket_count = 0
    bracket_preserved = True
    for left in roots:
        for right in roots:
            target = tuple(a+b for a, b in zip(left, right))
            if target in root_set:
                bracket_count += 1
                bracket_preserved &= ((-sum(left[:5])-sum(right[:5])+sum(target[:5])) % 2 == 0)
    opposite_preserved = all((sum(root[:5])+sum(-x for x in root[:5])) % 2 == 0
                             for root in roots)
    # Vector weights of SO(10) + SO(6), not E8 roots or Spin(10) spinor states.
    car_vectors = []
    for axis in range(8):
        for sign in (-1, 1):
            vector = [0]*8
            vector[axis] = 2*sign
            phase = (-sum(vector[:5])-sum(vector[5:])) % 4
            car_vectors.append({"weight_doubled": vector, "block": "10" if axis < 5 else "6",
                                "diagonal_phase_mod4": phase,
                                "generator_sign": -1 if phase == 2 else 1,
                                "square_sign": 1 if phase % 2 == 0 else -1})
    car_match = all(row["diagonal_phase_mod4"] == 2 for row in car_vectors)

    packet = []
    for bits in product((0, 1), repeat=5):
        degree = sum(bits)
        if degree % 2:
            continue
        nc, nw = sum(bits[:3]), sum(bits[3:])
        hypercharge = -sp.Rational(nc, 3)+sp.Rational(nw, 2)
        # Original left-chiral assignments in the exterior packet.
        bl = {(0, 0): 1, (2, 0): -sp.Rational(1, 3),
              (1, 1): sp.Rational(1, 3), (0, 2): 1,
              (3, 1): -1, (2, 2): -sp.Rational(1, 3)}[nc, nw]
        packet.append({"occupation": list(bits), "N": degree, "X": 5-2*degree,
                       "Y": str(hypercharge), "B_minus_L": str(bl),
                       "X_from_B_minus_L_Y": str(5*bl-4*hypercharge),
                       "omega_phase_mod4": (5-2*degree) % 4,
                       "slot_parity": 1, "omega_square": -1})

    joint = exact_joint_flavor_response()
    z, connection = joint["z"], joint["connection"]
    residues = [connection.applyfunc(lambda x: sp.limit((z-p)*x, z, p))
                for p in (1, sp.I, -1, -sp.I)]
    residue_spectrum = {sp.Rational(0): 1, sp.Rational(1, 3): 1, sp.Rational(2, 3): 1}
    residue_match = all(residue.eigenvals() == residue_spectrum for residue in residues)
    determinant = 1-z**4
    determinant_identity = sp.simplify(sp.diff(determinant, z)/determinant-sp.trace(connection)) == 0
    path = integrate_path_transport()
    winding = path["determinant_character"]["integrated_phase_winding"]

    m = exact_clock_dictionary()["M"]
    u = sp.diag(1, sp.I, -sp.I)
    lifted = even_spin_lift_endpoint(m, 1)
    minimal = even_spin_lift_endpoint(m, 0)
    lifted_product = sp.eye(4)
    for k in range(4):
        lifted_product = sp.simplify(lifted_product*even_spin_lift_endpoint(u**k*m*u**(-k), 1))
    lift_checks = {
        "unitary": sp.simplify(lifted.H*lifted) == sp.eye(4),
        "determinant_one": sp.simplify(lifted.det()) == 1,
        "relative_spin_sign": lifted == -minimal,
        "cube_is_family_centre": sp.simplify(lifted**3) == -sp.eye(4),
        "sixth_power_identity": sp.simplify(lifted**6) == sp.eye(4),
        "four_original_matrix_generators_product_identity": lifted_product == sp.eye(4),
        "vector_six_sees_no_relative_sign": exterior_power(lifted, 2) == exterior_power(minimal, 2),
    }

    # This tests the actual scalar-spinor-Higgs route of v488 against the
    # NEW Lorentz/Z4 quotient, not against the ordinary internal centre.
    fields = [
        {"field": "nu^c in 16_F", "X": 5, "lorentz_2pi_sign": -1, "statistics": "Weyl-Fermion"},
        {"field": "nu^c-conjugate direction in 16bar_H", "X": -5,
         "lorentz_2pi_sign": 1, "statistics": "Skalares Higgsfeld der Originalroute"},
        {"field": "10_H direction", "X": 2, "lorentz_2pi_sign": 1, "statistics": "Skalar im internen 10-Träger"},
    ]
    for field in fields:
        field["omega_square"] = 1 if field["X"] % 2 == 0 else -1
        field["quotient_kernel_action"] = field["lorentz_2pi_sign"]*field["omega_square"]
        field["descends_to_spin_Z4_quotient"] = field["quotient_kernel_action"] == 1

    double_twist = _double_twist_dictionary(source)
    double_closure = double_twist["chevalley_closure"]

    def check(name: str, ok: bool, actual: Any, expected: Any, method: str) -> dict[str, Any]:
        return {"name": name, "ok": bool(ok), "actual": actual, "expected": expected, "method": method}

    checks = [
        check("Das diagonale Originalzentrum ist auf allen E8-Feldern trivial",
              len(roots) == 240 and diagonal_trivial and central_match and car_match,
              {"roots": len(roots), "diagonal_trivial": diagonal_trivial},
              {"roots": 240, "diagonal_trivial": True}, "Exakte Phasen aus allen ursprünglichen verdoppelten Wurzeln"),
        check("Der relative Familien-Spinlift ist der ursprüngliche D8-Deckcharakter",
              deck_counts == {1: 112, -1: 128} and bracket_count == 13440
              and bracket_preserved and opposite_preserved,
              {"even_with_Cartan": deck_counts[1]+8, "odd": deck_counts[-1], "root_brackets": bracket_count},
              {"even_with_Cartan": 120, "odd": 128, "root_brackets": 13440},
              "Zentrale Charaktergleichheit auf jeder Wurzel, allen Wurzelsummen und gegenüberliegenden Klammern"),
        check("Die ursprünglichen 16 Ladungen tragen X, aber keine hergeleitete Feldstatistik",
              all(str(row["X"]) == row["X_from_B_minus_L_Y"] and row["omega_phase_mod4"] == 1 for row in packet),
              {"states": len(packet), "omega": "i", "omega_square": -1, "slot_parity": 1},
              {"states": 16, "omega": "i", "omega_square": -1, "slot_parity": 1},
              "Alle ursprünglichen Außenmonome und unabhängigen Standardmodell-B−L-Zuweisungen"),
        check("Die Originalresiduen und ihre Determinante behalten die Einheitswindung",
              residue_match and determinant_identity and abs(winding-1) < 2e-8,
              {"residue_spectrum": ["0", "1/3", "2/3"], "determinant_winding": winding},
              {"residue_spectrum": ["0", "1/3", "2/3"], "determinant_winding": 1},
              "Symbolische originale Fuchsverbindung und separat integrierter Originalpfad"),
        check("Der ursprüngliche Spinlift gibt eine Sechserwirkung mit geladenem Deck-Cube",
              all(lift_checks.values()), lift_checks, True,
              "Exakte Minorenwirkung auf Lambda-even C3; algebraische Produktrelation der vier vorgegebenen v117-Matrizengeneratoren"),
        check("Die neue Spin-Ladungsforderung kollidiert mit der alten skalaren Spinor-Higgs-Route",
              [row["descends_to_spin_Z4_quotient"] for row in fields] == [True, False, True],
              [row["quotient_kernel_action"] for row in fields], [1, -1, 1],
              "Der Quotientenkern muss auf jedem einzelnen ursprünglichen Feld trivial wirken; Operatorneutralität allein genügt nicht"),
        check("Halbtwist und Adjungierter erzeugen die ganze E8-Algebra durch echte Klammern",
              double_closure["generated_total_roots"] == 240
              and double_closure["generated_Cartan_rank"] == 8
              and double_closure["generated_Lie_dimension"] == 248
              and all(double_closure["nonzero_new_bracket_witnesses_by_round"]),
              {"roots": double_closure["generated_total_roots"],
               "Cartan_rank": double_closure["generated_Cartan_rank"],
               "dimension": double_closure["generated_Lie_dimension"],
               "rounds": double_closure["root_counts_by_round"]},
              {"roots": 240, "Cartan_rank": 8, "dimension": 248,
               "rounds": [54, 80, 150, 240]},
              "Nichtverschwindende Klammern der originalen Chevalley-Tabelle ab D5+D3 und +/-lambda"),
    ]
    data = {
        "title": "Die Originalwindung wird zum geladenen Spinlift derselben Quelle",
        "status": "EXACT_INTERNAL_LIFT_WITH_NUMERIC_PATH_CHECK",
        "formula": "det-Windung 1 → relatives Spinzeichen −1 → E8/D8-Deckcharakter η",
        "root_characters": {"records": records, "X_D5": "−sum(r[:5])", "X_A3": "−sum(r[5:])",
                            "coordinate_convention": "r=2 alpha in the original E8 Chevalley table",
                            "even_roots": deck_counts[1], "odd_roots": deck_counts[-1],
                            "even_with_Cartan": deck_counts[1]+8,
                            "bracket_count_ordered": bracket_count},
        "group_quotient": {
            "group": "(Spin(10) × SU(4))/⟨(omega10,−i I4)⟩",
            "central_identity": "[(1,−I4)]=[(-1_Spin10,1)]=eta_D8",
            "diagonal_generator_on_E8": "+I248",
            "diagonal_square_on_E8": "+I248",
            "D5_centre_square_on_E8": "+I120 ⊕ (−I128)",
            "current_weights": {"(16,4)": "5/8+3/8=1", "(10,6)": "1/2+1/2=1"},
            "meaning": "Die vollständigen geladenen E8-Felder sind bosonische Gewicht-1-Ströme. Ihre Deckgraduierung ist keine Fermionparität.",
        },
        "exterior_packet": {"formula": "X=5−2N=5(B−L)−4Y", "records": packet,
                            "full_exterior_identity": "omega=exp(i pi X/2)=i (−1)^N",
                            "distinction": "Auf Lambda-even C5 ist die Slotparität +1, während omega²=−1. Eine zusätzliche physische Fermionparität ist damit nicht hergeleitet."},
        "parent_CAR": {
            "one_particle_representation": "V16=(10,1) ⊕ (1,6)",
            "vector_weights": car_vectors,
            "diagonal_generator_actions": [-1, -1], "diagonal_square_actions": [1, 1],
            "scope": "Bei der vorhandenen chiralen CAR-Quantisierung wirkt der diagonale Generator als Fermionparität. Das setzt diese CAR-Feldalgebra voraus; ihr Einteilchenraum ist nicht der Spin(10)-Halbspinor 16.",
        },
        "fuchs_lift": {
            "original_logs": ["0", "1/3", "2/3"], "minimal_logs": ["0", "1/3", "−1/3"],
            "formula": "S(u)=det(u)^(−1/2) Lambda-even(u)",
            "original_endpoint": "−Lambda-even(M)", "minimal_endpoint": "+Lambda-even(M)",
            "matrix": _matrix_json(lifted), "checks": lift_checks,
            "determinant": "det Psi(z)=1−z⁴, Psi(0)=I", "measured_winding": winding,
            "source_action": "g³=eta_D8; g⁶=I on the original E8 source",
            "basis": "Lambda^0 C3 ⊕ Lambda^2 C3; pair basis (12),(13),(23)",
            "matrix_relation_scope": "Die Produktidentität betrifft die vier vorgegebenen Generatoren U^k M U^(−k). Sie beweist für sich nicht deren simultane Identifikation mit Monodromien aus gemeinsamen basierten ODE-Pfaden. Der separat integrierte Einpunkturpfad trägt den hier verwendeten lokalen Windungs- und Spinliftanschluss.",
            "framework_scope": "Die positive flache Metrik oder polare Retraktion überführt den nichtunitären Rohpfad in seine U3-Homotopieklasse. Die logarithmischen Erweiterungen unterscheiden sich tatsächlich; gleiche Endmonodromie löscht ihre Windung nicht.",
            "not_identified": "Dieser interne SU4-Spinlift ist weder der räumliche NS-Vierteldrehungslift noch ohne zusätzliches Wörterbuch der Sechser-Faseroperator U6=M⊕(−M).",
        },
        "spin_charge_scope": {
            "new_postulate": "omega10² = (−1)^F_4D",
            "fields": fields,
            "original_majorana_operator": "(16_F 16bar_H)^2 / Lambda",
            "operator_X_charge": 2*(5-5), "bare_nu_pair_X": 10,
            "required_compensating_charge_mod4": 2,
            "verdict": "Die neue Spin-Z4-Identifikation ist mit dem skalaren 16bar_H der bestehenden Majorana-Route unverträglich. Das ist kein allgemeiner TFPT-Ausschluss.",
            "remaining": "Die gewöhnliche interne Z4-Symmetrie erlaubt die Originalroute. Eine andere physische Statistik-/Higgsrealisierung müsste aus derselben Quelle hergeleitet werden; ein neutrales R-Feld kompensiert die Ladung des nackten Majorana-Paares nicht.",
        },
        "double_twist": double_twist,
    }
    return {"data": data, "checks": checks, "sources": [
        "tfpt_1_architecture_e8.tex:5325-5347",
        "tfpt_1_architecture_e8.tex:1615-1636",
        "_archive/tfpt-45/source_extracts/02_carrier_source.tex:573-668",
        "verification/v117_monodromy_weyl_a3.py:51-88",
        "verification/v148_fock_census.py:19-43",
        "verification/v154_simple_current_theorem.py:13-42",
        "verification/v242_spin_statistics_modular.py:8-28",
        "verification/v522_woit_beta1_gso_gauge.py:1",
        "verification/v983_simple_current_generator.py:11-52",
        "verification/v988_psi_lambda_reduction.py:1-42",
        "verification/v1033_charged_disorder.py:191-295",
        "articles/2026-08-30/mmst_charged_scaling_limit_en.tex:243-312",
        "experiments/theory-contracts/half-twist-grade-carry/README.md:21-97",
        "experiments/theory-contracts/half-twist-grade-carry/checker.py:98-128",
        "experiments/theory-contracts/source-rg-clock-bridge-20260920/PROOF.txt:26-119",
        "experiments/theory-contracts/microscopic-neutral-limit/README.md:43-60",
        "experiments/theory-contracts/microscopic-fourpoint-limit/README.md:165-232",
        "experiments/theory-contracts/microscopic-charged-car-limit/README.md:165-226",
        "tfpt_2_standard_model.tex:2001-2015",
        "verification/v488_majorana_clebsch_door.py:9-18",
        "experiments/theory-contracts/source-local-time-origin-20260921/PROOF.md:117-178",
        "tfpt_explorer/flavor_path_transport.py:1",
        "tfpt_explorer/hecke_source.py:313-329",
    ]}
