"""Exact marked response of the original EM005 C6 Green operator.

No physical H_adm identification, fitted parameters or new source model.
"""
import json
import sympy as s

a, b = s.symbols("a b", positive=True)
u = s.zeros(6)
for j in range(6):
    u[(j + 1) % 6, j] = 1
r = (a - 2*b) * (a*s.eye(6) - b*(u + u.T)).inv()
e = s.ones(6, 1)
o = s.diag(1, 0, 0, 0, 0, 0) - s.eye(6)/6
rates = [(a-2*b)/(a-b), (a-2*b)/(a+b), (a-2*b)/(a+2*b)]
moments = []
residuals = []
for k in range(3):
    actual = s.factor((e.T * o * r**k * o * e)[0]/6)
    expected = (2*rates[0]**k + 2*rates[1]**k + rates[2]**k)/36
    residual = s.factor(actual - expected)
    assert residual == 0
    moments.append(actual)
    residuals.append(str(residual))
defect = s.factor(moments[0]*moments[2] - moments[1]**2)
expected_defect = b**2*(a-2*b)**2*(3*a**2+8*a*b+7*b**2)/(108*(a-b)**2*(a+b)**2*(a+2*b)**2)
assert s.factor(defect - expected_defect) == 0
print(json.dumps({"verdict": "PASS_SCOPED_ORIGINAL_RESPONSE", "exact_identities": 4,
                  "response_residuals": residuals, "defect_identity_residual": "0",
                  "moments": [str(x) for x in moments], "positive_defect": str(defect),
                  "positivity_domain": "a>2*b>0", "physical_source_identified": False,
                  "primitive_generator": None, "joint_physical_spectrum": None}, indent=2))
