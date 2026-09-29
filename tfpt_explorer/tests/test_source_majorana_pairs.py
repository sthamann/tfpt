from __future__ import annotations

import json
from fractions import Fraction

from tfpt_explorer.source_majorana_pairs import (
    _inner, _native_pairs, build_source_majorana_pairs_data,
)


def test_original_level_one_pair_channel_and_highest_weights() -> None:
    result = build_source_majorana_pairs_data()
    assert all(check["ok"] for check in result["checks"])
    json.dumps(result)
    assert result is build_source_majorana_pairs_data()
    data = result["data"]
    for grade, family_dimension in ((3, 6), (4, 10)):
        highest = data[f"grade_{'three' if grade == 3 else 'four'}"]["highest_weight"]
        assert highest["norm_squared"] == "1"
        assert highest["lattice_weight"] == str(grade)
        assert highest["chiral_weight"] == grade
        assert highest["X"] == 10
        assert (highest["D5_dimension"], highest["A3_dimension"]) == (126, family_dimension)


def test_null_pair_is_specific_to_level_one_and_not_a_deleted_pbw_word() -> None:
    for level in (1, 2):
        native = _native_pairs(level)
        for a in range(4):
            for b in range(4):
                state = native["grade2"][a][b]
                assert state  # The simple quotient, not an empty PBW word, kills it.
                expected = (2 if a == b else 1) * level * (level - 1)
                assert _inner(native["affine"], state, state) == expected


def test_charge_conjugate_pair_exists_with_the_same_positive_norms() -> None:
    native = _native_pairs(dagger=True)
    for a, b in native["grade4"]:
        state = native["grade4"][a, b]
        assert _inner(native["affine"], state, state) == (1 if a == b else 2)
        weights = {native["affine"].weight(key) for key in state}
        assert len(weights) == 1
        doubled = next(iter(weights))
        assert sum(doubled[:5]) == 10
    for state in native["grade3"].values():
        assert _inner(native["affine"], state, state) == 1


def test_symmetric_grade_four_is_not_just_the_grade_three_derivative() -> None:
    native = _native_pairs()
    affine, pair = native["affine"], native["pair"]
    for a, b in native["grade3"]:
        forward, reverse = pair(a, b, 3), pair(b, a, 3)
        # Norms 2,-1,2 give norm2 for the symmetric field and norm6 for the
        # antisymmetric derivative. The latter equals 2h for h=3, as required.
        assert _inner(affine, forward, forward) == 2
        assert _inner(affine, reverse, reverse) == 2
        assert _inner(affine, forward, reverse) == -1
        assert _inner(affine, native["grade4"][a, b], native["grade4"][a, b]) == Fraction(2)


def test_other_native_yukawa_pair_channels_survive_at_grade_two() -> None:
    channels = build_source_majorana_pairs_data()["data"]["other_grade_two_channels"]
    for name, labels, charge in (("10x10", [1, 0, 0, 0, 0], 2),
                                  ("120x6", [0, 0, 1, 0, 0], 6)):
        highest = channels["witnesses"][name]["highest_weight"]
        assert highest["D5_dynkin"] == labels
        assert highest["X"] == charge
        assert highest["norm_squared"] == "1"
        assert highest["lattice_weight"] == "2"
    assert channels["image_dimension"] + channels["kernel_dimension"] == 64 * 65 // 2


def test_wound_family_pair_carry_has_original_discrete_intertwiner() -> None:
    import sympy as sp
    from tfpt_explorer.flavor_path_transport import exact_clock_dictionary
    from tfpt_explorer.source_majorana_pairs import _symmetric_square
    from tfpt_explorer.source_spin_lift import exterior_power

    data = build_source_majorana_pairs_data()["data"]["family_transport"]
    j = sp.Matrix(data["C_to_original_discrete_family"])
    p = sp.Matrix(data["C_to_exterior"])
    m = exact_clock_dictionary()["M"]
    retained = -p.T * exterior_power(m, 2) * p
    assert sp.simplify(j * retained + m * j) == sp.zeros(3)
    assert sp.simplify(j * retained - m * j) != sp.zeros(3)
    assert sp.simplify(_symmetric_square(j) * _symmetric_square(retained)
                       - _symmetric_square(m) * _symmetric_square(j)) == sp.zeros(6)
    # The same B is NOT a continuous SU3 intertwiner: a generic torus element
    # distinguishes the fundamental and its conjugate, as representation theory requires.
    generic = sp.diag(sp.I, 1, -sp.I)
    b = sp.Matrix(data["B"])
    assert generic * b != b * sp.conjugate(generic)


def test_source_pair_coupling_keeps_cocycle_adjoint_and_separation_factors() -> None:
    data = build_source_majorana_pairs_data()["data"]
    pair = data["native_three_point"]["grade4_126x10"]
    assert pair["lattice_phase"] == pair["adjoint_phase"] == "-1"
    assert pair["coefficient"] == "1"
    assert pair["exponents_z12_z13_z23"] == [2, -4, -4]
    for channel in data["other_grade_two_channels"]["witnesses"].values():
        assert channel["three_point"]["coefficient"] == "1"
        assert channel["three_point"]["exponents_z12_z13_z23"] == [0, -2, -2]


def test_neutral_pair_ward_keeps_the_offdiagonal_oscillator_and_same_family_corner() -> None:
    data = build_source_majorana_pairs_data()["data"]["joint_neutral_pair"]
    for row in data["symmetric_retained_six"]:
        a, b = row["family_pair"]
        assert row["eigenvector_checked"]
        assert Fraction(row["charge_R0"]) + Fraction(row["oscillator_R0"]) == 4
        if a != b:
            assert row["charge_R0"] == "0"  # Dropping the oscillator gives the wrong answer.
            assert row["oscillator_R0"] == "4"
    assert all(row["R0_eigenvalue"] == "0" for row in data["antisymmetric_retained_three"])
    assert data["omitted_diagonal_R0"] == "-12"  # No false SU4-invariant response.


def test_explicit_car_cocycle_matches_original_on_all_d8_roots_against_generators() -> None:
    import sympy as sp
    import pytest
    from functools import lru_cache
    from tfpt_explorer.source_majorana_pairs import _d8_car_cocycle, _d8_car_phase

    native = _native_pairs()
    algebra = native["algebra"]
    dictionary = _d8_car_cocycle()
    basis = [tuple(int(x) for x in dictionary["basis"][:, i]) for i in range(8)]
    roots = [tuple(x // 2 for x in root) for root in algebra.roots
             if all(x % 2 == 0 for x in root)]
    assert len(roots) == 112
    assert dictionary["symmetric_ratio"]

    @lru_cache(maxsize=None)
    def phase(momentum):
        return _d8_car_phase(sp.Matrix(momentum))

    for p in roots:
        for q in basis:
            i = algebra.ridx[tuple(2*x for x in p)]
            j = algebra.ridx[tuple(2*x for x in q)]
            original = algebra.eps(i, j)
            car = (-1)**sum(p[a]*q[b] for a in range(8) for b in range(a))
            summed = tuple(a+b for a, b in zip(p, q))
            assert original*phase(summed) == phase(p)*phase(q)*car
    # The overlap is D8, not the whole spinor source or the odd NS sector.
    with pytest.raises(ValueError):
        _d8_car_phase(sp.Matrix([sp.Rational(1, 2)]*8))
    with pytest.raises(ValueError):
        _d8_car_phase(sp.Matrix([1]+[0]*7))


def test_ten_pair_car_fields_retain_the_exact_lattice_ope_and_canonical_order() -> None:
    import sympy as sp
    from tfpt_explorer.source_majorana_pairs import _d8_car_phase

    rows = build_source_majorana_pairs_data()["data"]["CAR_pair_dictionary"]["rows"]
    native = _native_pairs()
    algebra = native["algebra"]
    assert len(rows) == 10
    for row in rows:
        a, b = row["family_pair"]
        ia, pa = native["currents"][a]
        ib, pb = native["currents"][b]
        momentum = sp.Matrix(row["momentum"])
        oscillator = sp.Matrix(row["oscillator"])
        # Distinct, increasingly ordered complex CAR components produce e^lambda
        # with no additional sign in the explicitly chosen CAR cocycle.
        assert [x["direction"] for x in row["CAR_factors"]] == sorted(x["direction"] for x in row["CAR_factors"])
        assert all(x["charge"] in (-1, 1) for x in row["CAR_factors"])
        assert row["CAR_composite_phase"] == pa*pb*algebra.eps(ia, ib)*_d8_car_phase(momentum)
        assert row["chiral_weight"] == 4
        assert row["X"] == 10 and row["Y"] == "0" and row["CAR_parity"] == 1
        if a == b:
            assert len(row["CAR_factors"]) == 8
            assert momentum.dot(momentum) == 8 and oscillator == sp.zeros(8, 1)
            assert row["norm_squared"] == "1"
        else:
            assert len(row["CAR_factors"]) == 6
            assert momentum.dot(momentum) == 6 and oscillator.dot(oscillator) == 2
            assert all(momentum[i]*oscillator[i] == 0 for i in range(8))
            assert row["norm_squared"] == "2"


def test_mixed_pair_ward_reports_actual_leakage_instead_of_inventing_eigenvalue() -> None:
    import sympy as sp
    from tfpt_explorer.neutral_source_response import _native_neutral_branch

    rows = build_source_majorana_pairs_data()["data"]["CAR_pair_dictionary"]["rows"]
    ar = _native_neutral_branch(0)["R_matrix"]
    for row in rows:
        a, b = row["family_pair"]
        ward = row["ward"]
        if a == 0 and b != 0:
            oscillator = sp.Matrix(row["oscillator"])
            # Exact orthogonal remainder; normalized variance is 64/2=32.
            residual = ar*oscillator + 4*oscillator
            assert residual != sp.zeros(8, 1)
            assert oscillator.dot(residual) == 0
            assert residual.dot(residual) == 64
            assert ward["R0_mean"] == "-4" and ward["normalized_variance"] == "32"
            assert not ward["is_eigenstate"]
        else:
            assert ward["is_eigenstate"] and ward["normalized_variance"] == "0"
            assert ward["R0_mean"] == ("-12" if a == b == 0 else "4")
