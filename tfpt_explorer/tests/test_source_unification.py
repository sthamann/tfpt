from __future__ import annotations

import json

import sympy as sp

from tfpt_explorer.current_block_geometry import _actual_current_source
from tfpt_explorer.source_unification import build_source_unification_data


def test_native_a8_extension_and_original_c4_complete_one_e8_source() -> None:
    result = build_source_unification_data()
    assert result is build_source_unification_data()
    assert all(check["ok"] for check in result["checks"])
    json.dumps(result)
    extension = result["data"]["a8_extension"]
    assert extension["lattice_index"] == 3
    assert extension["determinant"] == 9
    assert extension["E8_determinant"] == 1
    assert extension["X20_root_closure"] == [40, 72]
    assert extension["full24_root_closure"] == [48, 140, 240]
    assert [row["root_count"] for row in extension["sectors"]] == [72, 84, 84]
    assert [row["weight_one_dimension"] for row in extension["sectors"]] == [80, 84, 84]
    assert extension["C4_sector"] == "Lambda6"


def test_charged_C_is_outside_a8_and_has_exact_order_three_lattice_carry() -> None:
    source = _actual_current_source()
    extension = build_source_unification_data()["data"]["a8_extension"]
    basis = sp.Matrix(extension["simple_roots_doubled"]).T
    c0 = sp.Matrix([-1]*8)
    assert tuple(c0) in source["chevalley"].ridx
    coordinates = basis.inv()*c0
    assert not all(value.is_Integer for value in coordinates)
    assert not all(value.is_Integer for value in 2*coordinates)
    assert all(value.is_Integer for value in 3*coordinates)
    assert list(basis.T*c0/4) == [0, 0, 0, 0, 0, 1, 0, 0]


def test_same_virasoro_vector_needs_the_u1_piece_for_both_actual_field_types() -> None:
    data = build_source_unification_data()["data"]["shared_stress_tensor"]
    p4, p3, p1, p5 = [sp.Matrix(data["projectors"][key]) for key in ("A4", "A3", "u1", "D5")]
    assert p4+p3+p1 == sp.eye(8)
    assert p4+p1 == p5
    source = _actual_current_source()
    x = sp.Matrix(source["w20"][0, 0])/2
    c = sp.Matrix([-1]*8)/2
    # Dropping the shared scalar current is an actual wrong-weight control,
    # not simply a different way to write the same c=8 stress tensor.
    assert (x.T*(p4+p3)*x)[0]/2 == sp.Rational(31, 40)
    assert (c.T*(p4+p3)*c)[0]/2 == sp.Rational(3, 8)
    assert (x.T*(p4+p3+p1)*x)[0]/2 == 1
    assert (c.T*(p4+p3+p1)*c)[0]/2 == 1


def test_complementary_u1_is_not_the_original_p2_charge() -> None:
    data = build_source_unification_data()["data"]["shared_stress_tensor"]
    h = sp.Matrix(data["u1_direction"])
    y = sp.Matrix([sp.Rational(-1, 3)]*3+[sp.Rational(1, 2)]*2+[0]*3)
    source = _actual_current_source()
    assert h.dot(y) == 0
    assert {sp.simplify(h.dot(sp.Matrix(root)/2)) for root in source["w20"].values()} == {3/(2*sp.sqrt(5))}
    assert {y.dot(sp.Matrix(root)/2) for root in source["w20"].values()} == {sp.Rational(1, 3), sp.Rational(-1, 2)}
    assert h.dot(sp.Matrix([-1]*8)/2) == -sp.sqrt(5)/2
    assert y.dot(sp.Matrix([-1]*8)/2) == 0
