"""Exact replay of the original fixed-background clock/time comparison."""
import ast
import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
M_PATH = ROOT / "experiments/theory-contracts/v16-operator-pullback-20261014/fold-results.json"
SIGMA_PATH = ROOT / "verification/v634_st31_structure.py"
checks = []


def require(name, condition):
    if condition is not True and condition != sp.true:
        raise ArithmeticError(name)
    checks.append(name)


module = ast.parse(SIGMA_PATH.read_text())
sigma_assignments = [node.value for node in module.body if isinstance(node, ast.Assign)
                     and any(isinstance(t, ast.Name) and t.id == "SIGMA_IDX"
                             for t in node.targets)]
require("one original sigma literal", len(sigma_assignments) == 1)
idx = ast.literal_eval(sigma_assignments[0])
M = sp.Matrix(json.loads(M_PATH.read_text())["explicit_Weyl_matrix"])
R = M.T * sp.eye(8)[idx, :] * M
require("orthogonal original map", R.T * R == sp.eye(8))
require("original order three", R**3 == sp.eye(8) and R != sp.eye(8))
p = sp.eye(8)[:, 0] + sp.eye(8)[:, 2]
orbit = [R**k * p for k in range(3)]
require("actual marked root orbit", orbit == [p, sp.Matrix([1, 1, -1, 1, -1, 1, 1, 1])/2,
                                            sp.eye(8)[:, 1]-sp.eye(8)[:, 5]])
require("three norm-two roots", all(v.dot(v) == 2 for v in orbit))
variables = sp.Matrix(sp.symbols("p0:8"))
cases = []
for alpha in [sp.Rational(1, 4), sp.Rational(3, 4)]:
    delta = sp.Matrix([(k+alpha)/8-sp.Rational(1, 2) for k in range(8)])
    K = lambda v, d: v.dot(v)/2+d.dot(v)
    energies = [8*K(v, delta) for v in orbit]
    require(f"alpha {alpha}: exact source energies", energies == [2+2*alpha, 8+2*alpha, 4])
    require(f"alpha {alpha}: source cost six", energies[1]-energies[0] == 6)
    require(f"alpha {alpha}: quotient cost 3/4", (energies[1]-energies[0])/8 == sp.Rational(3, 4))
    b = R*delta-delta
    require(f"alpha {alpha}: full affine polynomial identity",
            sp.expand(K(R*variables+b, delta)-K(variables, delta)) == 0)
    require(f"alpha {alpha}: unique affine coefficient",
            R.T*(b+delta) == delta)
    require(f"alpha {alpha}: original lattice pairing nonintegral", b.dot(p).q != 1)
    require(f"alpha {alpha}: full transported-background identity",
            sp.expand(K(R*variables, R*delta)-K(variables, delta)) == 0)
    require(f"alpha {alpha}: full fixed-background energy response",
            sp.expand(K(R*variables, delta)-K(variables, delta)
                      -(R.T*delta-delta).dot(variables)) == 0)
    cases.append({"alpha": str(alpha), "source_H_energies": list(map(str, energies)),
                  "quotient_K_energies": [str(v/8) for v in energies],
                  "forced_affine_b": list(map(str, b)), "b_squared": str(b.dot(b)),
                  "b_dot_original_root": str(b.dot(p)),
                  "normalized_root_return_ratio": "exp(-3*t/4), t in original K units"})
result = {"verdict": "PASS_SCOPED_FIXED_SOURCE_TIME_TEST", "checks_passed": len(checks),
          "checks": checks, "cases": cases,
          "source_sha256": {str(f.relative_to(ROOT)): hashlib.sha256(f.read_bytes()).hexdigest()
                            for f in [M_PATH, SIGMA_PATH]},
          "scope": "Given source K and actual R; excludes only fixed-background energy-preserving affine charge maps with unchanged oscillator number. Not an exclusion of driven clocks or transported backgrounds, and not a primitive P1 realization."}
(HERE / "actual-clock-time-results.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
