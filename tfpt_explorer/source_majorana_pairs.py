"""Actual charged pair channels in the existing simple E8 level-one source.

The finite zero-mode (126,10) representation occurs at chiral weight four,
although its naive weight-two normal product is null. This is an operator
existence statement, not a four-dimensional Higgs field, condensate, mass
scale, or identification of chiral and four-dimensional engineering weights.
"""

from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, combinations_with_replacement
from typing import Any

import sympy as sp

from .current_block_geometry import _actual_current_source, _check
from .flavor_path_transport import exact_clock_dictionary
from .neutral_source_response import _native_neutral_branch
from .source_program import _field
from .source_spin_lift import even_spin_lift_endpoint, exterior_power


def _scale(state: dict, coefficient: F) -> dict:
    return {key: coefficient * value for key, value in state.items() if coefficient * value}


def _sum(*states: dict) -> dict:
    result: dict = {}
    for state in states:
        for key, value in state.items():
            result[key] = result.get(key, F(0)) + value
    return {key: value for key, value in result.items() if value}


def _inner(affine: Any, left: dict, right: dict) -> F:
    """Compact vacuum form in the ORIGINAL affine PBW implementation.

    Root adjoints are -E_{-alpha}; Cartan adjoints have no minus sign. A
    zero-norm universal PBW vector vanishes in the simple unitary quotient.
    """
    algebra = affine.ch
    result = F(0)
    for key, coefficient in left.items():
        state = right
        for mode, index in key:
            root = index < algebra.nR
            state = affine.act(algebra.opp[index] if root else index, -mode, state)
            if root:
                state = _scale(state, F(-1))
        result += coefficient * state.get((), F(0))
    return result


@lru_cache(maxsize=4)
def _native_pairs(level: int = 1, dagger: bool = False) -> dict[str, Any]:
    source = _actual_current_source()
    algebra = source["chevalley"]
    affine = source["affine"].Affine(algebra, F(level))
    currents = [next(iter(_field({"kind": "C", "a": a, "dagger": dagger})[1].items()))
                for a in range(4)]

    def pair(a: int, b: int, first_mode: int) -> dict:
        ia, pa = currents[a]
        ib, pb = currents[b]
        return _scale(affine.act(ia, -first_mode, affine.act(ib, -1, {(): F(1)})), pa * pb)

    grade2 = [[pair(a, b, 1) for b in range(4)] for a in range(4)]
    grade3 = {(a, b): pair(a, b, 2) for a, b in combinations(range(4), 2)}
    grade4 = {(a, b): (pair(a, a, 3) if a == b else
                      _sum(pair(a, b, 3), pair(b, a, 3)))
              for a, b in combinations_with_replacement(range(4), 2)}
    return {"algebra": algebra, "affine": affine, "currents": currents, "pair": pair,
            "grade2": grade2, "grade3": grade3, "grade4": grade4}


def _dot(left: tuple, right: tuple) -> F:
    return sum((F(a) * F(b) for a, b in zip(left, right)), F(0))


def _weyl_dimension(weight: tuple, positive_roots: list[tuple]) -> int:
    rho = tuple(sum(root[j] for root in positive_roots) / F(2) for j in range(len(weight)))
    shifted = tuple(a + b for a, b in zip(weight, rho))
    result = F(1)
    for root in positive_roots:
        result *= _dot(shifted, root) / _dot(rho, root)
    assert result.denominator == 1
    return result.numerator


def _highest_weight(native: dict, state: dict) -> dict[str, Any]:
    algebra, affine = native["algebra"], native["affine"]
    weights = {affine.weight(key) for key in state}
    assert len(weights) == 1
    doubled = next(iter(weights))
    charge = tuple(F(value, 2) for value in doubled)
    roots = [algebra.roots[index] for index, _ in native["currents"]]
    d5_simple = []
    for j in range(4):
        root = [0] * 8
        root[j], root[j + 1] = -2, 2
        d5_simple.append(tuple(root))
    d5_simple.append((0, 0, 0, -2, -2, 0, 0, 0))
    a3_simple = [tuple(x - y for x, y in zip(roots[a], roots[a + 1])) for a in range(3)]
    simple = d5_simple + a3_simple
    images = [affine.act(algebra.ridx[root], 0, state) for root in simple]
    labels = [int(_dot(doubled, root) / 4) for root in simple]
    d5_positive = []
    for i, j in combinations(range(5), 2):
        for sign in (1, -1):
            root = [F(0)] * 5
            root[i], root[j] = F(-1), F(sign)
            d5_positive.append(tuple(root))
    a3_positive = [tuple(F(roots[a][j] - roots[b][j], 2) for j in range(5, 8))
                   for a, b in combinations(range(4), 2)]
    return {
        "charge_doubled": list(doubled), "X": int(-2 * sum(charge[:5])),
        "lattice_weight": str(_dot(charge, charge) / 2),
        "chiral_weight": -sum(mode for mode, _ in next(iter(state))),
        "norm_squared": str(_inner(affine, state, state)),
        "D5_dynkin": labels[:5], "A3_dynkin": labels[5:],
        "D5_dimension": _weyl_dimension(charge[:5], d5_positive),
        "A3_dimension": _weyl_dimension(charge[5:], a3_positive),
        "raising_image_norms": [str(_inner(affine, image, image)) for image in images],
        "positive_simple_roots_doubled": [list(root) for root in simple],
    }


def _symmetric_square(matrix: sp.Matrix) -> sp.Matrix:
    """Action on the unnormalized basis aa and ab+ba, matching the pair Gram."""
    pairs = list(combinations_with_replacement(range(matrix.rows), 2))
    columns = []
    for a, b in pairs:
        tensor = sp.zeros(matrix.rows)
        tensor[a, b] = 1
        tensor[b, a] = 1
        image = matrix * tensor * matrix.T
        columns.append(sp.Matrix([image[i, j] for i, j in pairs]))
    return sp.Matrix.hstack(*columns)


def _three_point(algebra: Any, a: int, b: int, pa: F = F(1), pb: F = F(1)) -> dict:
    """The normalized first pair coefficient, with original lattice cocycle."""
    ma, mb = algebra.mvec[a], algebra.mvec[b]
    total = tuple(x + y for x, y in zip(ma, mb))
    negative = tuple(-x for x in total)

    def eps(left: tuple, right: tuple) -> int:
        exponent = sum(left[i] * algebra.B[i][j] * right[j]
                       for i in range(algebra.rank) for j in range(algebra.rank))
        return -1 if exponent % 2 else 1

    phase = pa * pb * eps(ma, mb)
    adjoint_phase = phase * eps(total, negative)
    coefficient = pa * pb * adjoint_phase * eps(ma, mb) * eps(ma, negative) * eps(mb, negative)
    h = 2 + algebra.rip(a, b)
    return {"coefficient": str(coefficient), "lattice_phase": str(phase),
            "adjoint_phase": str(adjoint_phase), "pair_weight": h,
            "exponents_z12_z13_z23": [h - 2, -h, -h],
            "formula": "<B†(z3) A(z1) D(z2)> = z12^(h-2)/(z13^h z23^h)",
            "normalization": "B is the norm-one leading pair state with the displayed original cocycle phase."}


def _family_transport(native: dict) -> dict[str, Any]:
    """The same omitted C0 corner, including the actual current-basis phases."""
    algebra, currents = native["algebra"], native["currents"][1:]
    m, u = exact_clock_dictionary()["M"], sp.diag(1, sp.I, -sp.I)
    b = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, -1, 0]])
    hodge = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
    # Columns C1,C2,C3 correspond to wedge23,wedge13,wedge12. The already
    # transported C phases are checked below against the actual root action.
    permutation = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    intertwiner = b * hodge * permutation
    generator_checks = []
    parameter = sp.Symbol("t")
    for a, c in ((0, 1), (1, 2), (1, 0), (2, 1)):
        root = [0] * 8
        root[5 + a], root[5 + c] = 2, -2
        index = algebra.ridx[tuple(root)]
        sign = 1 if a < c else -1  # compact adjoint in original Chevalley basis
        actual = sp.zeros(3)
        for j, (source_index, source_phase) in enumerate(currents):
            action = algebra.bracket(index, source_index)
            for i, (target_index, target_phase) in enumerate(currents):
                actual[i, j] = sign * source_phase * action.get(target_index, F(0)) / target_phase
        elementary = sp.zeros(3)
        elementary[a, c] = 1
        exterior = exterior_power(sp.eye(3) + parameter * elementary, 2).diff(parameter).subs(parameter, 0)
        generator_checks.append(actual == permutation.T * exterior * permutation)
    lifted = even_spin_lift_endpoint(m, 1)
    retained = -permutation.T * exterior_power(m, 2) * permutation
    retained_u = permutation.T * exterior_power(u, 2) * permutation
    pair_intertwiner = _symmetric_square(intertwiner)
    square = _symmetric_square(lifted)
    checks = {
        "native_current_and_exterior_bases_match": all(generator_checks),
        "M_real_intertwiner": sp.simplify(m * b - b * sp.conjugate(m)) == sp.zeros(3),
        "U_real_intertwiner": sp.simplify(u * b - b * sp.conjugate(u)) == sp.zeros(3),
        "single_field_carry_kept": sp.simplify(intertwiner * retained + m * intertwiner) == sp.zeros(3),
        "pair_M_intertwining": sp.simplify(pair_intertwiner * _symmetric_square(retained)
                                            - _symmetric_square(m) * pair_intertwiner) == sp.zeros(6),
        "pair_U_intertwining": sp.simplify(pair_intertwiner * _symmetric_square(retained_u)
                                            - _symmetric_square(u) * pair_intertwiner) == sp.zeros(6),
        "full_symmetric_pair_cube_identity": sp.simplify(square ** 3) == sp.eye(10),
    }
    encode = lambda matrix: [[str(value) for value in row] for row in matrix.tolist()]
    return {
        "omitted_family": 0, "retained_families": [1, 2, 3],
        "native_basis": "C0 is wedge0; (C1,C2,C3)=(wedge23,wedge13,wedge12) after the original transported current phases.",
        "exterior_basis": "wedge12,wedge13,wedge23",
        "C_to_exterior": encode(permutation), "Hodge": encode(hodge), "B": encode(b),
        "C_to_original_discrete_family": encode(intertwiner),
        "pair_intertwiner": encode(pair_intertwiner), "checks": checks,
        "continuous_branching": "4 = 1 + bar3; Sym²4 = 1 + bar3 + bar6 relative to the original SU3 action M. The conjugate source gives 1+3+6.",
        "discrete_bridge": "For the original M,U, B intertwines bar3 with3. J=B H P intertwines the retained wound spin lift with -M; Sym²J intertwines its pair action with Sym²M. The genuine single-field minus sign is retained before taking pairs.",
        "majorana_form": "The six retained symmetric pairs form the space of symmetric 3x3 family tensors. Their conjugates can contract invariantly with nu^c nu^c from that same carrier; the actual mass matrix or vacuum expectation value is not selected.",
        "scope": "B is an intertwiner for the original discrete M,U subgroup, not for all SU3. The internal marked-matrix relation does not by itself identify every matrix generator with one jointly based raw-ODE monodromy representation.",
    }


def _joint_neutral_pair(native: dict) -> dict[str, Any]:
    """R0 on the same actual lattice pair states, including their oscillators."""
    ar = _native_neutral_branch(0)["R_matrix"]
    roots = [sp.Matrix(native["algebra"].roots[index]) / 2 for index, _ in native["currents"]]
    symmetric, antisymmetric = [], []
    for a, b in combinations_with_replacement((1, 2, 3), 2):
        momentum = roots[a] + roots[b]
        zero_mode = (momentum.T * ar * momentum)[0] / 2
        oscillator = sp.zeros(8, 1) if a == b else roots[a] - roots[b]
        # A symmetric off-diagonal pair is h_(alpha_a-alpha_b)(-1)|alpha_a+alpha_b>.
        # Its lattice contribution is zero, but its one oscillator contributes4.
        exact = (zero_mode == 4 if a == b else
                 ar * oscillator == (4 - zero_mode) * oscillator)
        symmetric.append({"family_pair": [a, b], "charge_R0": str(zero_mode),
                          "oscillator_R0": "0" if a == b else str(4 - zero_mode),
                          "R0_eigenvalue": "4", "eigenvector_checked": bool(exact),
                          "norm_squared": "1" if a == b else "2"})
    for a, b in combinations((1, 2, 3), 2):
        momentum = roots[a] + roots[b]
        zero_mode = (momentum.T * ar * momentum)[0] / 2
        antisymmetric.append({"family_pair": [a, b], "R0_eigenvalue": str(zero_mode)})
    omitted = ((2 * roots[0]).T * ar * (2 * roots[0]))[0] / 2
    return {
        "operator": "R=4T_A2-8T_U1 from the SAME original 48-current branch with omitted family0",
        "symmetric_retained_six": symmetric, "antisymmetric_retained_three": antisymmetric,
        "omitted_diagonal_R0": str(omitted),
        "ward_identity": "<B†(infinity) R(z) B(0)> / ||B||² = 4/z² for every retained symmetric family pair",
        "scope": "This is a fixed same-source neutral/charged-pair response. R is SU3-corner invariant, not SU4 invariant; the omitted diagonal pair instead has eigenvalue-12. No Majorana condensate, alpha-dependent mass, or physical coupling follows without the corresponding source-to-physics map.",
    }


@lru_cache(maxsize=1)
def build_source_majorana_pairs_data() -> dict[str, Any]:
    native = _native_pairs()
    algebra, affine, pair = native["algebra"], native["affine"], native["pair"]
    roots = [algebra.roots[index] for index, _ in native["currents"]]
    dot_matrix = [[algebra.rip(i, j) for j, _ in native["currents"]]
                  for i, _ in native["currents"]]
    norms2 = [[str(_inner(affine, state, state)) for state in row] for row in native["grade2"]]
    gram3 = [[str(_inner(affine, left, right)) for right in native["grade3"].values()]
             for left in native["grade3"].values()]
    gram4 = [[str(_inner(affine, left, right)) for right in native["grade4"].values()]
             for left in native["grade4"].values()]
    symmetric3 = [_sum(pair(a, b, 2), pair(b, a, 2)) for a, b in native["grade3"]]
    symmetric3_norms = [str(_inner(affine, state, state)) for state in symmetric3]
    diagonal3_norms = [str(_inner(affine, pair(a, a, 2), pair(a, a, 2))) for a in range(4)]
    derivative_cross = []
    for a, b in native["grade3"]:
        # Difference is the L_-1 descendant of the antisymmetric weight-three
        # field. The symmetric state is a separate, orthogonal weight-four state.
        derivative = _sum(pair(a, b, 3), _scale(pair(b, a, 3), F(-1)))
        derivative_cross.append(str(_inner(affine, native["grade4"][a, b], derivative)))
    highest3 = _highest_weight(native, native["grade3"][0, 1])
    highest4 = _highest_weight(native, native["grade4"][0, 0])
    other_pairs = {}
    first = native["currents"][0][0]
    for name, root in (("10x10", (-1, 1, 1, 1, 1, -1, -1, -1)),
                       ("120x6", (-1, -1, -1, 1, 1, -1, 1, 1))):
        second = algebra.ridx[root]
        state = affine.act(first, -1, affine.act(second, -1, {(): F(1)}))
        other_pairs[name] = {"roots_doubled": [list(algebra.roots[first]), list(root)],
                             "highest_weight": _highest_weight(native, state),
                             "three_point": _three_point(algebra, first, second)}
    family_transport = _family_transport(native)
    neutral_pair = _joint_neutral_pair(native)
    three_points = {
        "grade3_126x6": _three_point(algebra, *[native["currents"][a][0] for a in (0, 1)],
                                    *[native["currents"][a][1] for a in (0, 1)]),
        "grade4_126x10": _three_point(algebra, first, first),
    }
    expected3 = [[str(int(i == j)) for j in range(6)] for i in range(6)]
    diagonal4 = [1 if a == b else 2 for a, b in native["grade4"]]
    expected4 = [[str(diagonal4[i] if i == j else 0) for j in range(10)] for i in range(10)]
    checks = [
        _check("native_nuc_pair_dots", dot_matrix == [[2 if a == b else 1 for b in range(4)] for a in range(4)],
               dot_matrix, "2 on diagonal, 1 otherwise", "Inner products of the actual C-current roots"),
        _check("level_one_grade_two_null", norms2 == [["0"] * 4 for _ in range(4)],
               norms2, "all sixteen norms zero", "Original affine compact vacuum Gram form"),
        _check("grade_three_antisymmetric", gram3 == expected3 and symmetric3_norms == ["0"] * 6 and diagonal3_norms == ["0"] * 4,
               {"Gram": gram3, "symmetric_norms": symmetric3_norms, "diagonal_norms": diagonal3_norms},
               "six orthonormal antisymmetric states", "Original modes C_a(-2)C_b(-1)Omega"),
        _check("grade_four_symmetric", gram4 == expected4 and derivative_cross == ["0"] * 6,
               {"Gram": gram4, "derivative_cross": derivative_cross},
               "ten positive symmetric states, orthogonal to the weight-three derivatives", "Original modes C_a(-3)C_b(-1)Omega and exchanged pair"),
        _check("actual_highest_weights", highest3["D5_dynkin"] == highest4["D5_dynkin"] == [0, 0, 0, 0, 2]
               and highest3["A3_dynkin"] == [0, 1, 0] and highest4["A3_dynkin"] == [2, 0, 0]
               and highest3["raising_image_norms"] == highest4["raising_image_norms"] == ["0"] * 8
               and (highest3["D5_dimension"], highest3["A3_dimension"], highest4["A3_dimension"]) == (126, 6, 10),
               {"grade3": highest3, "grade4": highest4}, "(126,6) at weight3; (126,10) at weight4",
               "Eight actual positive root zero modes, Cartan weights and Weyl dimension formula"),
        _check("other_grade_two_pair_channels", all(row["highest_weight"]["norm_squared"] == "1"
               and row["highest_weight"]["raising_image_norms"] == ["0"] * 8
               and row["highest_weight"]["chiral_weight"] == 2 for row in other_pairs.values())
               and [(row["highest_weight"]["D5_dimension"], row["highest_weight"]["A3_dimension"])
                    for row in other_pairs.values()] == [(10, 10), (120, 6)],
               other_pairs, "Nonzero (10,10) and (120,6) at weight2", "Actual roots and affine highest-weight Gram test"),
        _check("original_marked_family_pair_transport", all(family_transport["checks"].values()),
               family_transport["checks"], True, "Original M,U, wound exterior spin lift, and actual current-generator basis phases"),
        _check("native_pair_three_point_coefficients", all(row["coefficient"] == "1" for row in three_points.values())
               and all(row["three_point"]["coefficient"] == "1" for row in other_pairs.values()),
               three_points, "Unit normalized OPE coefficient, with weight-dependent separation factors",
               "Bimultiplicative original Chevalley cocycle extended to the actual summed lattice charges"),
        _check("same_source_neutral_pair_ward", all(row["eigenvector_checked"] for row in neutral_pair["symmetric_retained_six"])
               and all(row["R0_eigenvalue"] == "0" for row in neutral_pair["antisymmetric_retained_three"])
               and neutral_pair["omitted_diagonal_R0"] == "-12",
               neutral_pair, "R0=4 on retained symmetric6, 0 on retained antisymmetric3, -12 on omitted diagonal",
               "Original neutral A_R matrix on the actual lattice momenta AND one-oscillator pair states"),
    ]
    data = {
        "title": "Der Majorana-Paarkanal ist in der vollständigen Quelle vorhanden",
        "summary": "Die unmittelbare Paarung der geladenen Singletfelder ist bei Level 1 null. Die Quelle erzeugt zuerst einen antisymmetrischen Kanal bei Gewicht 3 und dann den symmetrischen 126×10-Kanal bei Gewicht 4. Damit existiert ein zulässiger zusammengesetzter Ladung-2-Kandidat; seine physische Kopplung und Kondensation sind noch auszuwählen.",
        "status": "EXACT_SOURCE_OPERATOR_EXISTENCE",
        "source_currents": {"roots_doubled": [list(root) for root in roots],
                            "phases": [str(phase) for _, phase in native["currents"]],
                            "physical_coordinate": "alpha = root_doubled/2",
                            "X": [5] * 4, "adjoint_X": [-5] * 4,
                            "orientation": "X=-sum(root_doubled[:5])=5-2N, as in source_spin_lift: original C is the X=+5 nu^c singlet orientation; its adjoint has X=-5. The names 126 and conjugate reverse with Spin(10) chirality.",
                            "dot_matrix": dot_matrix},
        "ope": {
            "formula": "C_a(z)C_b(w) = p_a p_b epsilon(alpha_a,alpha_b) (z-w)^(alpha_a·alpha_b) [V_(alpha_a+alpha_b)(w)+...]",
            "cocycle": [[algebra.eps(i, j) for j, _ in native["currents"]] for i, _ in native["currents"]],
            "exchange": "epsilon(alpha,beta)/epsilon(beta,alpha)=(-1)^(alpha·beta)",
            "grade_two": ":C_a C_b: = 0 in the simple unitary level-one quotient",
            "grade_three": ":(partial C_a) C_b: = - :(partial C_b) C_a: for a!=b",
            "grade_four_diagonal": "(1/2) :(partial² C_a) C_a: = C_a(-3) C_a(-1)Omega",
            "explicit_lattice_vectors": "C_0(-2)C_1(-1)Omega = |alpha_0+alpha_1>; C_0(-3)C_0(-1)Omega = -|2alpha_0>, in the original cocycle convention",
        },
        "grade_two": {"pair_norms": norms2, "quotient_scope": "Zero norm, not an empty universal PBW expression; positivity kills it in the simple E8_1 quotient."},
        "grade_three": {"family_pairs": [list(pair) for pair in native["grade3"]], "gram": gram3,
                        "symmetric_norms": symmetric3_norms, "diagonal_norms": diagonal3_norms,
                        "highest_weight": highest3, "representation_dimension": 126 * 6},
        "grade_four": {"family_pairs": [list(pair) for pair in native["grade4"]], "gram": gram4,
                       "descendant_cross": derivative_cross,
                       "highest_weight": highest4, "representation_dimension": 126 * 10},
        "other_grade_two_channels": {
            "witnesses": other_pairs,
            "symmetric_tensor_decomposition": "Sym²(16 tensor4) = (10,10) + (126,10) + (120,6)",
            "image_dimension": 820, "kernel_dimension": 1260,
            "dimension_reason": "The symmetrized normal-product map is equivariant under D5+A3 zero modes. The domain decomposition is multiplicity-free. Its (126,10) highest vector is null; both other highest vectors are nonzero, so each other irreducible is injected.",
        },
        "native_three_point": three_points,
        "family_transport": family_transport,
        "joint_neutral_pair": neutral_pair,
        "charge_and_statistics": {
            "X": 10, "adjoint_X": -10, "Z4_charge": 2, "omega_eigenvalue": "-1", "omega_squared": "+1",
            "bosonic": "The even-lattice pair fields are bosonically local and their even internal X-charge is compatible with a scalar Spin×Z4/Z2 representation, if such a four-dimensional source dictionary is supplied.",
            "family_restriction": "In the same omitted-C0 spin-lift convention, Sym²(4)=bar6+bar3+1, with conjugate6+3+1. The original discrete real intertwiner connects the pair representation to Sym² of the original three-family M,U transport; no mass matrix is fixed.",
        },
        "first_occurrence_proof": "The highest (126,6) charge has squared length6, so no state with that weight exists below grade3. The highest (126,10) charge has squared length8, so none exists below grade4. The displayed nonzero lattice states attain both bounds. All X=±10 charges have squared length at least6 in the E8 lattice.",
        "physical_scope": {
            "positive_consequence": "The absence of 126 from the weight-one adjoint hull does not exclude a composite 126 from the full source. The symmetric charge-two channel is explicitly present.",
            "native_source_coupling": "The normalized three-point/OPE coefficients of the displayed pair operators are fixed by the same source, rather than free new chiral couplings. A four-dimensional Yukawa coefficient is a further identification.",
            "original_d5": "This does not make an elementary odd-X scalar 16_H a representation of Spin×Z4/Z2. A coupling to the composite conjugate (126,10) would be a different effective pair mechanism, unless an additional derivation relates it to the original d=5 formula.",
            "missing_maps": ["Which chiral source composite becomes a local four-dimensional scalar operator.",
                             "The invariant physical Yukawa or effective coupling to nu^c nu^c.",
                             "A state or dynamics giving the charged pair a nonzero expectation value, and its scale and family tensor."],
            "weight_warning": "Chiral source weight4 is not four-dimensional engineering dimension4. Operator existence is not condensation or the original Majorana mass derivation.",
        },
    }
    return {"data": data, "checks": checks, "sources": [
        "verification/v498_celestial_wp5b_singular_vector.py::Chevalley",
        "verification/v498_celestial_wp5b_singular_vector.py::Affine",
        "tfpt_explorer/source_program.py::_c_currents",
        "tfpt_explorer/source_spin_lift.py::even_spin_lift_endpoint",
        "tfpt_explorer/flavor_path_transport.py::exact_clock_dictionary",
        "tfpt_explorer/neutral_source_response.py::_native_neutral_branch",
        "experiments/theory-contracts/matter-geometry-round15/PROOF.md:126-179",
        "tfpt_2_standard_model.tex:2001-2018",
        "verification/v488_majorana_clebsch_door.py:9-17",
        "https://doi.org/10.1007/BF01391662",
    ]}
