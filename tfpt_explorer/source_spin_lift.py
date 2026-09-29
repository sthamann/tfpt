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
        "tfpt_2_standard_model.tex:2001-2015",
        "verification/v488_majorana_clebsch_door.py:9-18",
        "experiments/theory-contracts/source-local-time-origin-20260921/PROOF.md:117-178",
        "tfpt_explorer/flavor_path_transport.py:1",
        "tfpt_explorer/hecke_source.py:313-329",
    ]}
