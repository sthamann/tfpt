#!/usr/bin/env python3
"""Exact countermodels and bounded regressions for the ten-image proposal.

This audits implications, not RH, autonomous prime generation, or factoring speed.
Run with experiments/tfpt-discovery/.venv/bin/python. Writes only beside this file.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
checks = []
details = {}


def check(name, condition):
    checks.append({"name": name, "passed": bool(condition)})
    print(f"{'PASS' if condition else 'FAIL'} {name}")


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


z, x, y, c, w, u = sp.symbols("z x y c w u")
I5 = sp.eye(5)
Y = sp.diag(*([sp.Rational(-1, 3)] * 3 + [sp.Rational(1, 2)] * 2))
J = (12 * Y - I5) / 5
check("carrier_involution_exact", J**2 == I5)
check("carrier_projector_ranks_3_and_2", ((I5-J)/2).rank() == 3 and ((I5+J)/2).rank() == 2)
check("carrier_polynomial_exact", 6*Y**2-Y-I5 == sp.zeros(5))
details["carrier"] = {"Y": str(Y), "iota": str(J), "polynomial": "6Y^2-Y-I=0"}

# The induced exterior action is not the same as applying the affine formula
# to the total hypercharge on a many-particle state (already false on vacuum).
even_masks = [m for m in range(32) if m.bit_count() % 2 == 0]
lift = [(-1)**sum((m >> k) & 1 for k in range(3)) for m in even_masks]
check("exterior_lift_has_8_plus_8_sectors", lift.count(1) == lift.count(-1) == 8)
check("affine_hypercharge_formula_does_not_extend_to_vacuum", sp.Rational(-1, 5)**2 != 1)

# Every polynomial in Y commutes with J. Odd dynamics needs additional data.
a0, a1 = sp.symbols("a0 a1")
fY = a0*I5+a1*Y  # every polynomial reduces to this via the quadratic relation
check("entire_polynomial_Y_algebra_is_even", J*fY*J == fY)
entries = sp.symbols("b0:25")
B = sp.Matrix(5, 5, entries)
constraints = list(J*B+B*J)
cmat, _ = sp.linear_eq_to_matrix(constraints, entries)
check("odd_operator_space_has_dimension_12", 25-cmat.rank() == 12)
# Odd blocks are 3x2 and 2x3, hence rank <= 4; construct maximal rank witness.
Bmax = sp.zeros(5)
for i, j, val in ((0, 3, 1), (1, 4, 2)):
    Bmax[i, j] = Bmax[j, i] = val
check("odd_carrier_max_rank_witness_4", J*Bmax*J == -Bmax and Bmax.rank() == 4)

# Direct counterexample to K1+K2 => critical-line confinement, on actual 3+2 J.
Boff = sp.zeros(5)
Boff[0, 3] = Boff[3, 0] = 4
Dz = I5+z*Boff
detz = sp.factor(Dz.det())
check("countermodel_passes_screenshot_K1", J*Dz*J == Dz.subs(z, -z))
check("countermodel_passes_screenshot_K2", sp.expand(detz-detz.subs(z, -z)) == 0)
roots = sp.solve(detz, z)
check("countermodel_has_off_line_strip_roots", roots == [sp.Rational(-1, 4), sp.Rational(1, 4)])
details["countermodel"] = {"D": str(Dz), "det": str(detz), "z_roots": list(map(str, roots)),
                          "s_roots": [str(sp.Rational(1, 2)+r) for r in roots]}

# For a standard chiral spectral pencil the transformation includes a minus.
Pz = Bmax-z*I5
check("standard_spectral_pencil_has_minus_sign", J*Pz*J == -Pz.subs(z, -z))
check("odd_dimension_spectral_determinant_is_odd", sp.expand(Pz.det()+Pz.subs(z, -z).det()) == 0)

# Weighted inversion on log coordinate t: R_w f(t)=exp(-wt) f(-t).
t = sp.symbols("t", real=True)
f = sp.Function("f")
R = lambda h: sp.exp(-w*t)*h.subs(t, -t)
Theta = lambda h: -sp.diff(h, t)
check("weighted_reflection_is_involution_for_every_w", sp.simplify(R(R(f(t)))-f(t)) == 0)
check("weighted_reflection_generator_center_is_w_over_2", sp.simplify(R(Theta(R(f(t))))-(w*f(t)-Theta(f(t)))) == 0)
details["mellin"] = {"identity": "M[R_w f](s)=M[f](w-s)", "center": "w/2; w=1 needs an independently fixed measure"}

# A monodromy that exchanges the sheets removes odd repetitions in full trace.
Swap = sp.Matrix([[0, 1], [1, 0]])
check("sheet_swap_local_determinant_is_1_minus_x_squared", (sp.eye(2)-x*Swap).det() == 1-x*x)
trace_pattern = [int(sp.trace(Swap**k)) for k in range(1, 7)]
check("sheet_swap_full_trace_loses_odd_repetitions", trace_pattern == [0, 2, 0, 2, 0, 2])
details["sheet_swap"] = {"traces_k_1_to_6": trace_pattern,
                         "inverse_local_determinant": "1/(1-x^2), not 1/(1-x)"}

# log(product Euler factors) has no mixed pq orbit; a coupled graph does.
L = sp.Matrix([[x, c*x], [c*y, y]])
qdet = sp.expand((sp.eye(2)-L).det())
mixed = sp.diff(-sp.log(qdet), x, y).subs({x: 0, y: 0})
check("connected_two_orbit_graph_creates_mixed_term", sp.simplify(mixed-c*c) == 0)
check("disconnected_product_has_no_mixed_log_term", mixed.subs(c, 0) == 0)
details["mixed_orbits"] = {"det": str(qdet), "log_inverse_xy_coefficient": str(mixed)}

# Standard modular geodesic l=2log(epsilon), epsilon+1/epsilon integer.
# l=log(p) would require integer trace squared = p+2+1/p, impossible p>1.
p = sp.symbols("p", positive=True, integer=True)
check("modular_prime_length_obstruction_identity", sp.simplify((sp.sqrt(p)+1/sp.sqrt(p))**2-(p+2+1/p)) == 0)
details["modular_length"] = "For every integer p>1, p+2+1/p is not an integer, so l=log(p) is not a standard modular closed-geodesic length. No assertion about a new time-changed flow."

# Finite multiplicative shifts: exact symbolic determinant, primes supplied
# as fixtures. This is an audit of a failure, not a source-only prime mechanism.
shift_results = []
for N in (8, 16, 32):
    Lshift = sp.zeros(N)
    for pp in (2, 3, 5):
        for n in range(1, N+1):
            if pp*n <= N:
                Lshift[pp*n-1, n-1] += sp.Rational(1, pp**2)
    check(f"finite_shift_det_is_one_N{N}", (sp.eye(N)-Lshift).det() == 1)
    shift_results.append({"N": N, "det": "1", "traces_1_to_4": [str(sp.trace(Lshift**k)) for k in range(1,5)]})
details["finite_shifts"] = shift_results

# Re-use current v258 modular functions on a declared witness/control, not
# an assertion that this J is the deployed D_rel grading on its larger space.
sys.path.insert(0, str(ROOT/"verification"))
modular = load_module("audit_v258", ROOT/"verification/v258_dirac_covariance_induction.py")
Jn = np.array(J).astype(float)
H = np.array(Bmax).astype(float)
C = modular.kms_cov(H)
Hrec = modular.induce(C)
comp_res = float(np.max(np.abs(Jn@C@Jn-(np.eye(5)-C))))
odd_res = float(np.max(np.abs(Jn@Hrec@Jn+Hrec)))
control = np.diag([.2, .3, .4, .6, .7])
control_res = float(np.max(np.abs(Jn@control@Jn-(np.eye(5)-control))))
check("conditional_modular_complement_symmetry_numeric", comp_res < 1e-12 and odd_res < 1e-12)
check("legal_covariance_control_does_not_force_complement_symmetry", control_res > .1)
details["modular"] = {"complement_residual": comp_res, "odd_residual": odd_res,
                      "control_residual": control_res, "status": "constructed witness/control only; source derivation OPEN"}

source_paths = ["tfpt_1_architecture_e8.tex", "tfpt_2_standard_model.tex",
                "verification/v258_dirac_covariance_induction.py", "verification/v1021_all_place_tate_rank_audit.py",
                "experiments/tfpt-discovery/hecke_orbit_transfer_probe.py", "experiments/tfpt-discovery/seam_geodesic_factor.py",
                "experiments/tfpt-discovery/regulator_jump_probe.py", "rh/catalog/analysis/all_place_tate_audit.md"]
result = {"claim_boundary": "NO RH CLAIM; no factoring speedup; countermodels and finite regression only",
          "passed": sum(q["passed"] for q in checks), "total": len(checks), "checks": checks,
          "details": details, "versions": {"sympy": sp.__version__, "numpy": np.__version__},
          "source_sha256": {q: hashlib.sha256((ROOT/q).read_bytes()).hexdigest() for q in source_paths}}
(HERE/"results.json").write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n")
print(f"{result['passed']}/{result['total']} checks passed; NO RH CLAIM")
raise SystemExit(0 if result["passed"] == result["total"] else 1)
