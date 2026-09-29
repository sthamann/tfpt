"""Public exact evaluations of the single original E8_1 current source.

The program evaluates field correlation functions, not detector histories.
Positions are arguments of that source law. No event probabilities, elapsed
physical times, Hamiltonians, or graph measures are supplied by this API.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
import itertools as it
from typing import Any

import sympy as sp

from .current_block_geometry import (
    AFFINE_SOURCE, CURRENT_PROOF, PHASE_SOURCE,
    _actual_current_source, _bracket, _check, _current, _kappa, _ward,
    _ward_at_infinity,
)


@lru_cache(maxsize=1)
def _c_currents() -> tuple[dict[int, Fraction], ...]:
    """The original C phases, fixed by the same SU4 root transport as X."""
    source = _actual_current_source()
    algebra = source["chevalley"]
    roots = [(-1,) * 5 + weight for weight in
             [(-1, -1, -1), (-1, 1, 1), (1, -1, 1), (1, 1, -1)]]
    phases = [Fraction(1)]
    for a in range(3):
        simple = tuple(x - y for x, y in zip(roots[a + 1], roots[a]))
        phases.append(phases[-1] * algebra.bracket(
            algebra.ridx[simple], algebra.ridx[roots[a]])[algebra.ridx[roots[a + 1]]])
    return tuple({algebra.ridx[root]: phase} for root, phase in zip(roots, phases))


def _field(specification: dict[str, Any]) -> tuple[dict[str, Any], dict[int, Fraction]]:
    if not isinstance(specification, dict):
        raise ValueError("each field must be a dictionary with kind C or X")
    kind = specification.get("kind")
    if kind not in ("C", "X"):
        raise ValueError("field kind must be C or X")
    allowed = {"kind", "a", "dagger"} | ({"i"} if kind == "X" else set())
    if set(specification) - allowed:
        raise ValueError("unknown field keys: " + ", ".join(sorted(set(specification) - allowed)))
    a = specification.get("a")
    if type(a) is not int or not 0 <= a < 4:
        raise ValueError("a must be an integer in 0..3")
    dagger = specification.get("dagger", False)
    if type(dagger) is not bool:
        raise ValueError("dagger must be boolean")
    clean: dict[str, Any] = {"kind": kind, "a": a, "dagger": dagger}
    source = _actual_current_source()
    if kind == "X":
        i = specification.get("i")
        if type(i) is not int or not 0 <= i < 5:
            raise ValueError("i must be an integer in 0..4")
        clean["i"] = i
        vector = _current(source, i, a, dagger)
    else:
        vector = dict(_c_currents()[a])
        if dagger:
            vector = {source["chevalley"].opp[index]: -coefficient
                      for index, coefficient in vector.items()}
    return clean, vector


def _position(value: Any) -> Fraction:
    if type(value) not in (int, str, Fraction):
        raise ValueError("positions must be exact integers, Fraction values, or rational strings")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError("invalid rational position") from error


def _numeric_display(value: Fraction) -> float | None:
    """Keep exact results usable when their optional float display overflows."""
    try:
        return float(value)
    except OverflowError:
        return None


def _bracket_description(vector: dict[int, Fraction]) -> list[dict[str, Any]]:
    algebra = _actual_current_source()["chevalley"]
    return [
        {"basis_index": index, "coefficient": str(coefficient),
         "basis_kind": "root" if index < algebra.nR else "simple_coroot",
         "root_doubled": list(algebra.roots[index]) if index < algebra.nR else None}
        for index, coefficient in sorted(vector.items())
    ]


def evaluate_source_word(word: list[dict[str, Any]], positions: list[Any]) -> dict[str, Any]:
    """Evaluate any finite current word at distinct finite rational positions.

    ``{"kind":"X","i":0,"a":1,"dagger":True}`` and
    ``{"kind":"C","a":2}`` name the original fields. Complexity grows
    with word length; no truncation, Gaussian replacement or new dynamics
    is introduced. The trace contains only the first Ward expansion.
    """
    if not isinstance(word, (list, tuple)) or not isinstance(positions, (list, tuple)):
        raise ValueError("word and positions must be finite lists or tuples")
    if len(word) != len(positions):
        raise ValueError("one position is required for every field")
    clean_and_vectors = [_field(specification) for specification in word]
    clean = [entry[0] for entry in clean_and_vectors]
    vectors = tuple(entry[1] for entry in clean_and_vectors)
    points = tuple(_position(value) for value in positions)
    if len(set(points)) != len(points):
        raise ValueError("coincident positions require an OPE limit, not this finite-position evaluation")
    source = _actual_current_source()
    value = _ward(source, vectors, points)
    expansion = []
    for j in range(1, len(vectors)):
        separation = points[0] - points[j]
        pairing = _kappa(source, vectors[0], vectors[j])
        double_pole = pairing * _ward(
            source, vectors[1:j] + vectors[j + 1:], points[1:j] + points[j + 1:]
        ) / separation**2
        bracket = _bracket(source, vectors[0], vectors[j])
        replaced = list(vectors[1:])
        replaced[j - 1] = bracket
        simple_pole = _ward(source, tuple(replaced), points[1:]) / separation if bracket else Fraction(0)
        expansion.append({
            "pair": [0, j], "separation": str(separation), "kappa": str(pairing),
            "double_pole_contribution": str(double_pole),
            "bracket": _bracket_description(bracket),
            "simple_pole_contribution": str(simple_pole),
        })
    return {
        "word": clean, "positions": [str(point) for point in points],
        "value_exact": str(value), "value_numeric": _numeric_display(value),
        "first_expansion": expansion,
        "meaning": "E8_1 vacuum current correlation amplitude; not a probability or a sequence of detector outcomes",
    }


def _connected_ward(vectors: tuple[dict[int, Fraction], ...], points: tuple[Fraction, ...]) -> Fraction:
    """Finite subset recursion for the square-free coefficient of log Z."""
    source = _actual_current_source()

    @lru_cache(maxsize=None)
    def moment(subset: tuple[int, ...]) -> Fraction:
        return _ward(source, tuple(vectors[i] for i in subset), tuple(points[i] for i in subset))

    @lru_cache(maxsize=None)
    def cumulant(subset: tuple[int, ...]) -> Fraction:
        if not subset:
            return Fraction(0)
        value = moment(subset)
        anchor, *rest = subset
        # Every set partition has a unique block containing the anchor.
        # Summing the remaining blocks gives the complementary full moment.
        for size in range(len(rest)):
            for selected in it.combinations(rest, size):
                block = (anchor,) + selected
                complement = tuple(i for i in rest if i not in selected)
                value -= cumulant(block) * moment(complement)
        return value

    return cumulant(tuple(range(len(vectors))))


def connected_source_word(word: list[dict[str, Any]], positions: list[Any]) -> dict[str, Any]:
    """Return the connected coefficient in the finite formal source log Z.

    Here Z(t)=omega(product_i(1+t_i J_i(z_i))). Only the coefficient of
    t_1...t_n is requested; no infinite functional integral is assumed.
    """
    result = evaluate_source_word(word, positions)
    vectors = tuple(_field(field)[1] for field in result["word"])
    points = tuple(Fraction(point) for point in result["positions"])
    connected = _connected_ward(vectors, points)
    result.update({
        "connected_value_exact": str(connected), "connected_value_numeric": _numeric_display(connected),
        "generating_polynomial": "Z(t)=omega(product_i(1+t_i J_i(z_i))); connected=coefficient_(t1...tn) log Z(t)",
    })
    return result


@lru_cache(maxsize=1)
def build_source_program_data() -> dict[str, Any]:
    source = _actual_current_source()
    six_word = [
        {"kind": "X", "i": i, "a": a, "dagger": dagger}
        for i, a, dagger in [(0, 0, False), (1, 0, True), (1, 1, False),
                            (2, 1, True), (2, 2, False), (0, 2, True)]
    ]
    points = tuple(map(Fraction, (-5, -2, -1, 1, 3, 7)))
    vectors = tuple(_field(field)[1] for field in six_word)
    example = connected_source_word(six_word, list(points))
    pairing_zeros = sum(_kappa(source, vectors[a], vectors[b]) == 0
                        for a, b in it.combinations(range(6), 2))
    proper_subsets = [subset for size in range(1, 6) for subset in it.combinations(range(6), size)]
    vanishing_subsets = sum(_ward(source, tuple(vectors[i] for i in subset),
                                tuple(points[i] for i in subset)) == 0 for subset in proper_subsets)
    algebra = source["chevalley"]
    root_charges = [algebra.roots[next(iter(vector))] for vector in vectors]
    charged_proper_subsets = sum(
        any(sum(root_charges[i][axis] for i in subset) != 0 for axis in range(8))
        for subset in proper_subsets
    )
    total_root_charge = [sum(root[axis] for root in root_charges) for axis in range(8)]
    z = sp.symbols("z1:7")
    symbolic_formula = 1 / ((z[0] - z[1]) * (z[0] - z[5]) * (z[1] - z[2])
                            * (z[2] - z[3]) * (z[3] - z[4]) * (z[4] - z[5]))
    symbolic_exact = sp.factor(_ward(source, vectors, z) - symbolic_formula) == 0
    permutation_failures = sum(
        _ward(source, tuple(vectors[i] for i in permutation), tuple(points[i] for i in permutation))
        != Fraction(1, 576) for permutation in it.permutations(range(6))
    )

    # The original 8000 mixed brackets imply the complete four-index tensor.
    # This witness has no pair contractions at all and distinguishes the
    # joint carrier/register tensor from a naive single 20D W encoder.
    four_vectors = (_current(source, 0, 0), _current(source, 1, 0, True),
                    _current(source, 1, 1), _current(source, 0, 1, True))
    joint_value = _ward_at_infinity(source, four_vectors, tuple(map(Fraction, (-1, 0, 1))))
    full_signature_vectors = tuple(_field(field)[1] for field in [
        {"kind": "C", "a": 0}, {"kind": "X", "i": 0, "a": 0, "dagger": True},
        {"kind": "X", "i": 0, "a": 1}, {"kind": "C", "a": 1, "dagger": True},
    ])
    full_signature_value = _ward_at_infinity(source, full_signature_vectors, tuple(map(Fraction, (-1, 0, 1))))

    def encoder_gram(dimension: int) -> list[list[int]]:
        gram = [[0] * dimension for _ in range(dimension)]
        for a, b, c in it.product(range(dimension), repeat=3):
            row = [int(a == b and c == x) + int(a == x and b == c) for x in range(dimension)]
            for x, y in it.product(range(dimension), repeat=2):
                gram[x][y] += row[x] * row[y]
        return gram

    gram5, gram4 = encoder_gram(5), encoder_gram(4)
    joint_gram_exact = all(
        gram5[i][j] == 12 * int(i == j) for i, j in it.product(range(5), repeat=2)
    ) and all(gram4[a][b] == 10 * int(a == b) for a, b in it.product(range(4), repeat=2))
    coefficient_failures = 0
    indices = list(it.product(range(5), range(4)))
    # Each triple determines its full sparse current output, so this checks
    # the entire 20^4 tensor without 160000 repeated Ward recursions.
    for (i, a), (j, b), (k, c) in it.product(indices, repeat=3):
        first, second, third = _current(source, i, a), _current(source, j, b, True), _current(source, k, c)
        actual = dict(_bracket(source, _bracket(source, first, second), third))
        for factor, vector in [(_kappa(source, first, second), third),
                               (_kappa(source, second, third), first)]:
            for index, value in vector.items():
                actual[index] = actual.get(index, Fraction(0)) + factor * value
        expected: dict[int, Fraction] = {}
        for l, d in indices:
            coefficient = (int(i == j and k == l) + int(i == l and j == k)) * (
                int(a == b and c == d) + int(a == d and b == c))
            if coefficient:
                for index, value in _current(source, l, d).items():
                    expected[index] = expected.get(index, Fraction(0)) + coefficient * value
        actual = {index: value for index, value in actual.items() if value}
        coefficient_failures += actual != expected
    cartan = _bracket(source, _current(source, 0, 0), _current(source, 0, 0, True))
    control_points = tuple(map(Fraction, (-3, -1, 1, 3)))
    cartan_full = _ward(source, (cartan,) * 4, control_points)
    cartan_connected = _connected_ward((cartan,) * 4, control_points)
    checks = [
        _check("Volle gemischte Sechspunktantwort", example["value_exact"] == "1/576" and pairing_zeros == 15,
               [example["value_exact"], pairing_zeros], ["1/576", 15], "Originale Chevalley-Klammer und affine Ward-Rekursion, ohne Gaußersatz"),
        _check("Die Sechspunktantwort ist verbunden", vanishing_subsets == charged_proper_subsets == 62 and example["connected_value_exact"] == "1/576" and not any(total_root_charge) and symbolic_exact,
               {"vanishing": vanishing_subsets, "charged_subsets": charged_proper_subsets, "connected": example["connected_value_exact"]},
               {"vanishing": 62, "charged_subsets": 62, "connected": "1/576"},
               "Alle62 echten Teilmengen tragen nichtnull E8-Ladung: ihre Korrelatoren verschwinden für alle Positionen. Direkte Teilmengen-/logZ-Rekursion bestätigt den verbundenen Wert"),
        _check("Quellenwert unabhängig vom Ward-Rechenweg", permutation_failures == 0,
               permutation_failures, 0, "Alle720 gemeinsamen Permutationen von Feld-Positions-Paaren; keine Aussage über gemessene Ereignisreihenfolgen"),
        _check("Gemeinsame geladene Rekursion enthält beide Faktoren", coefficient_failures == 0 and joint_value == 1 and joint_gram_exact,
               [coefficient_failures, str(joint_value), joint_gram_exact], [0, "1", True], "Alle8000 Stromausgaben des harmonischen Vierpunkttensors; beide Gram-Matrizen direkt aus ganzzahligen Encodertensoren"),
        _check("Die volle24er-Signatur behält ihre gemischte Klammer", full_signature_value == Fraction(1, 2),
               str(full_signature_value), "1/2", "Originale C-X-Antwort; ein naiver W6 tensor W4-Ersatz würde an denselben Indizes1 liefern"),
        _check("Echte Cartan-Gaußkontrolle", cartan_full != 0 and cartan_connected == 0,
               [str(cartan_full), str(cartan_connected)], ["nonzero", "0"], "Derselbe E8-Cartan-Strom viermal: volle Antwort ungleichnull, verbundene Antwort null"),
    ]
    return {"data": {
        "title": "Die vollständige Quellenregel auswerten",
        "api": {"function": "evaluate_source_word(word, positions)", "X_example": six_word[0],
                "connected_function": "connected_source_word(word, positions)",
                "C_example": {"kind": "C", "a": 0, "dagger": False},
                "positions": "distinct finite rational numbers", "empty_word": "1", "one_current": "0"},
        "rule": "F_n=sum_(j>1) kappa(a1,aj)/(z1-zj)^2 F_(n-2)+1/(z1-zj) F_(n-1)(...,[a1,aj],...)",
        "source_signature": "The original C4+X20 currents and adjoints generate the full248-current E8 source; intermediate brackets retain its actual root/coroot basis.",
        "example": example,
        "connected_six_point": {"value_exact": "1/576", "pair_contractions_zero": pairing_zeros,
                                "symbolic_rule": "F6=1/[(z1-z2)(z1-z6)(z2-z3)(z3-z4)(z4-z5)(z5-z6)]",
                                "symbolic_rule_exact": symbolic_exact,
                                "symbolic_rule_origin": "Direct symbolic evaluation of the same original Chevalley/affine Ward recursion for these six labeled currents; all proper subcorrelators vanish by E8 charge conservation.",
                                "proper_subcorrelators_zero": vanishing_subsets, "proper_subcorrelators_tested": 62,
                                "proper_subsets_with_nonzero_E8_charge": charged_proper_subsets,
                                "total_E8_charge": total_root_charge,
                                "generating_polynomial": example["generating_polynomial"],
                                "simultaneous_permutations_tested": 720, "permutation_failures": permutation_failures,
                                "meaning": "A nonzero connected six-current response generated by the same bracket law; a computation hyperedge, not an extra fundamental interaction or outcome probability."},
        "gaussian_cartan_control": {"positions": list(map(str, control_points)),
                                    "full_value_exact": str(cartan_full), "connected_value_exact": str(cartan_connected)},
        "joint_recursion": {
            "tensor": "F_(ia,jb,kc,ld)(-1,0,1,infinity)=(delta_ij delta_kl+delta_il delta_jk)(delta_ab delta_cd+delta_ad delta_bc)",
            "normalized_encoder": "W_joint = W5 tensor W4, with the three carrier/register factors interleaved",
            "input_dimension": 20, "output_dimension": 8000, "gram": "N_joint^dagger N_joint=120 I20",
            "factor_grams_exact": joint_gram_exact,
            "coefficient_triples_checked": 8000, "coefficient_failures": coefficient_failures,
            "mixed_witness": {"fields": ["X(0,0)", "X(1,0)^dagger", "X(1,1)", "X(0,1)^dagger"],
                              "value_exact": str(joint_value), "naive_single20_W_value": "0"},
            "scope": "This is the full X20 harmonic block, with a conjugate middle leg, and its leading three-current OPE. It does not assert the same product encoder for the larger C4+X20 signature or discard finite-separation descendants.",
        },
        "full24_mixed_response": {
            "fields": ["C(0)", "X(0,0)^dagger", "X(0,1)", "C(1)^dagger"],
            "positions": ["-1", "0", "1", "infinity"], "value_exact": str(full_signature_value),
            "naive_W6_tensor_W4_value": "1",
            "meaning": "The same full Ward rule includes the actual C-X exterior-product bracket. The X20 factorization is a derived sector of that rule, not a replacement for the original24 fields.",
        },
        "source_scope": {
            "type": "fixed E8_1 chiral vacuum functional",
            "determined": "All finite current-insertion amplitudes at specified distinct rational positions follow from this one source rule. Coordinates and inserted fields are query arguments, not adjusted laws.",
            "computation_paths": "Alternative Ward/fusion trees evaluate the same source amplitude; they are not separate physical histories receiving additional arbitrary weights.",
            "not_identified": ["chiral insertion coordinate with physical3+1 time", "internal field labels with spatial points", "correlation amplitudes with detector probabilities"],
            "physical_extension": "A source-to-P1 collar field identification and any dynamical spacetime geometry measure remain separate physical realization requirements. No missing choice of measuring apparatus is claimed to make this already specified vacuum functional ambiguous.",
        },
    }, "checks": checks, "sources": [
        f"{AFFINE_SOURCE}:398-522", f"{PHASE_SOURCE}:176-236", f"{CURRENT_PROOF}:43-72",
        "tfpt_explorer/current_block_geometry.py::_ward (shared original affine recursion)",
    ]}
