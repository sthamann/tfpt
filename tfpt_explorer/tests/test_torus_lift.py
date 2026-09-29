import sympy as sp

from tfpt_explorer.torus_lift import (
    _integer_left_obstruction, build_torus_lift_data,
)


def test_continuous_characters_can_repair_a_sign_only_obstruction():
    # 2t=1 mod2 has the real solution t=1/2, but no sign-bit solution.
    assert _integer_left_obstruction([[2]], [1]) is None
    assert _integer_left_obstruction([[2], [2]], [0, 1]) is not None


def test_full_group_witness_contradicts_even_continuous_characters():
    result = build_torus_lift_data()
    assert result['global_section_excluded']
    rows = result['witness_equations']
    coefficients = sp.Matrix([row['coefficients'] for row in rows])
    multipliers = sp.Matrix([[row['multiplier'] for row in rows]])
    rhs = sp.Matrix([row['rhs'] for row in rows])
    assert multipliers * coefficients == sp.zeros(1, 40)
    assert int((multipliers * rhs)[0]) % 2 == 1
    assert result['processed_Cayley_nodes'] <= 100


def test_braid_pair_has_no_continuous_character_obstruction():
    result = build_torus_lift_data((13, 0))
    assert result['generated_Cayley_nodes'] == 6
    assert not result['global_section_excluded']
