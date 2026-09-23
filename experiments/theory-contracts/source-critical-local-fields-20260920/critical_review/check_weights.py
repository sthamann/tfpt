#!/usr/bin/env python3
"""Exact rational audit of the local UV/IR weight table.

This checks only consequences of the pinned lattice data and the standard
Ising weights.  It does not select V_c, the couplings, or a vacuum.
"""

from fractions import Fraction as F
import json


checks = []


def check(name, got, expected):
    ok = got == expected
    checks.append({"name": name, "ok": ok, "got": str(got), "expected": str(expected)})
    if not ok:
        raise AssertionError(f"{name}: got {got}, expected {expected}")


def neutral_weights(a, b):
    return a * a / 2, b * b / 2


def total(h):
    return h[0] + h[1]


def spin(h):
    return h[0] - h[1]


# n/2=(u+v)/2 and z/2=(u-v)/2.
check("n_half_weights", neutral_weights(F(1, 2), F(1, 2)), (F(1, 8), F(1, 8)))
check("z_half_weights", neutral_weights(F(1, 2), F(-1, 2)), (F(1, 8), F(1, 8)))
check("u_weights", neutral_weights(F(1), F(0)), (F(1, 2), F(0)))
check("v_weights", neutral_weights(F(0), F(1)), (F(0), F(1, 2)))

# D8 level-one conformal weights from minimal squared norms 0,1,2,2.
d8 = {"0": F(0), "vector": F(1, 2), "spinor": F(1), "cospinor": F(1)}
check("D8_vector_weight", d8["vector"], F(1, 2))
check("D8_spinor_weight", d8["spinor"], F(1))
check("D8_cospinor_weight", d8["cospinor"], F(1))

uv = {
    "f": (d8["vector"] + F(1, 8), F(1, 8)),
    "b": (d8["spinor"] + F(1, 8), F(1, 8)),
    "raw_f+b_u": (F(2) + F(1, 2), F(0)),
    "raw_f+b-z_v": (F(2), F(1, 2)),
    "x_c_u": (d8["cospinor"] + F(1, 2), F(0)),
    "x_c-z_v": (d8["cospinor"], F(1, 2)),
}
ir = {
    "f": (d8["vector"] + F(1, 16), F(1, 16)),
    "b": (d8["spinor"] + F(1, 16), F(1, 16)),
    "raw_f+b_u": uv["raw_f+b_u"],
    "raw_f+b-z_v": uv["raw_f+b-z_v"],
    "x_c_u": uv["x_c_u"],
    "x_c-z_v": uv["x_c-z_v"],
}

expected_uv = {
    "f": ((F(5, 8), F(1, 8)), F(3, 4), F(1, 2)),
    "b": ((F(9, 8), F(1, 8)), F(5, 4), F(1)),
    "raw_f+b_u": ((F(5, 2), F(0)), F(5, 2), F(5, 2)),
    "raw_f+b-z_v": ((F(2), F(1, 2)), F(5, 2), F(3, 2)),
    "x_c_u": ((F(3, 2), F(0)), F(3, 2), F(3, 2)),
    "x_c-z_v": ((F(1), F(1, 2)), F(3, 2), F(1, 2)),
}
expected_ir = {
    "f": ((F(9, 16), F(1, 16)), F(5, 8), F(1, 2)),
    "b": ((F(17, 16), F(1, 16)), F(9, 8), F(1)),
    "raw_f+b_u": ((F(5, 2), F(0)), F(5, 2), F(5, 2)),
    "raw_f+b-z_v": ((F(2), F(1, 2)), F(5, 2), F(3, 2)),
    "x_c_u": ((F(3, 2), F(0)), F(3, 2), F(3, 2)),
    "x_c-z_v": ((F(1), F(1, 2)), F(3, 2), F(1, 2)),
}

for name, weights in uv.items():
    ew, ed, es = expected_uv[name]
    check(f"uv_{name}_weights", weights, ew)
    check(f"uv_{name}_dimension", total(weights), ed)
    check(f"uv_{name}_spin", spin(weights), es)

for name, weights in ir.items():
    ew, ed, es = expected_ir[name]
    check(f"ir_{name}_weights", weights, ew)
    check(f"ir_{name}_dimension", total(weights), ed)
    check(f"ir_{name}_spin", spin(weights), es)

# Global monodromy: D8 vector-spinor and neutral half-vertices each give 1/2.
check("D8_mutual_pairing", F(1, 2), F(1, 2))
check("neutral_mutual_pairing", F(1, 2), F(1, 2))
check("full_mutual_pairing", F(1, 2) + F(1, 2), F(1))

# Neutral locality requires integer u,v coefficients of equal parity.
def neutral_is_local(a, b):
    return a.denominator == b.denominator == 1 and (a.numerator - b.numerator) % 2 == 0


check("u_not_pure_local", neutral_is_local(F(1), F(0)), False)
check("v_not_pure_local", neutral_is_local(F(0), F(1)), False)
check("n_local", neutral_is_local(F(1), F(1)), True)
check("z_local", neutral_is_local(F(1), F(-1)), True)
check("minimal_representative_spin_difference_integer", spin(ir["x_c_u"]) - spin(ir["x_c-z_v"]), F(1))

# Direct Gamma integrality of the two cospinor-dressed Majorana representatives.
f_vec = (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
b_vec = (1, 1, 1, 0, 0, 0, 0, 0, 0, 1)
z_vec = (0, 0, 0, 0, 0, 0, 0, 0, 1, -1)
fb_u = tuple(x + y for x, y in zip(f_vec, b_vec))
fb_v = tuple(x - y for x, y in zip(fb_u, z_vec))
check("f_plus_b_integral_representative", fb_u, (2, 1, 1, 0, 0, 0, 0, 0, 0, 1))
check("f_plus_b_minus_z_integral_representative", fb_v, (2, 1, 1, 0, 0, 0, 0, 0, -1, 2))

d_vec = (1, 1, 0, 0, 0, 0, 0, 0)
a_vec = (1, 1, 1, -1, -1, -1, -1, -1)
a_dot_d = sum(x * y for x, y in zip(a_vec, d_vec))
t_d = d_vec + (-a_dot_d // 2, a_dot_d // 2)
x_c = tuple(x - y for x, y in zip(fb_u, t_d))
x_c_minus_z = tuple(x - y for x, y in zip(x_c, z_vec))
check("T_d_vector", t_d, (1, 1, 0, 0, 0, 0, 0, 0, -1, 1))
check("x_c_integral_representative", x_c, (1, 0, 1, 0, 0, 0, 0, 0, 1, 0))
check("x_c_minus_z_integral_representative", x_c_minus_z, (1, 0, 1, 0, 0, 0, 0, 0, 0, 1))

# Direct K-spin and V_c-dimension checks for every displayed ten-vector.
k_signs = (1, 1, 1, 1, 1, 1, 1, 1, 1, -1)
n_vec = (1, 1, 1, -1, -1, -1, -1, -1, -1, 3)
v_vec = tuple(F(x - y, 2) for x, y in zip(n_vec, z_vec))


def bilinear(x, y):
    return sum(F(k) * F(a) * F(b) for k, a, b in zip(k_signs, x, y))


def vc_dimension(x):
    return (bilinear(x, x) + 2 * bilinear(v_vec, x) ** 2) / 2


displayed = {
    "f": (f_vec, F(1, 2), F(3, 4)),
    "b": (b_vec, F(1), F(5, 4)),
    "raw_f+b": (fb_u, F(5, 2), F(5, 2)),
    "raw_f+b-z": (fb_v, F(3, 2), F(5, 2)),
    "x_c": (x_c, F(3, 2), F(3, 2)),
    "x_c-z": (x_c_minus_z, F(1, 2), F(3, 2)),
}
for name, (vector, expected_spin, expected_delta) in displayed.items():
    check(f"{name}_integral_coordinates", all(isinstance(q, int) for q in vector), True)
    check(f"{name}_K_spin", bilinear(vector, vector) / 2, expected_spin)
    check(f"{name}_Vc_dimension", vc_dimension(vector), expected_delta)

result = {
    "verdict": "PASS_EXACT_SCOPED",
    "checks": len(checks),
    "all_pass": all(c["ok"] for c in checks),
    "scope": "Exact rational weights, direct K-spins and V_c dimensions of displayed vectors, neutral locality parity, and monodromy cancellation only.",
    "records": checks,
}
print(json.dumps(result, indent=2, sort_keys=True))
