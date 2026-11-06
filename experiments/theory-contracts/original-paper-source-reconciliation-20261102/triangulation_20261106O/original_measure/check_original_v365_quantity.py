"""Exact type check of the two nonzero energies already written in v365.

No new model, physical Hessian, measure or common field value is introduced.
The optional Gaussian interpretation M=H is explicitly conditional.
"""
from pathlib import Path
import json
import sympy as s

e1 = 6*s.log(s.Rational(3,2))
e2 = 6*s.log(3)
q1, q2 = s.Rational(2,3)**6, s.Rational(1,3)**6
energy_sum = e1+e2
det_h = e1*e2
stiffness = 8*s.pi
checks = {
    'source_energy_sum_is_6log9over2': s.simplify(energy_sum-6*s.log(s.Rational(9,2))) == 0,
    'sum_is_negative_log_transfer_determinant': s.simplify(energy_sum+s.log(q1*q2)) == 0,
    'conditional_H_determinant_is_product_of_energies': s.simplify(det_h-36*s.log(s.Rational(3,2))*s.log(3)) == 0,
    'conditional_8pi_H_gaussian_Z_squared': s.simplify(((2*s.pi)**2/(stiffness**2*det_h))-1/(16*det_h)) == 0,
    'source_susceptibility': 1/(1-q1) == s.Rational(729,665),
}
assert all(checks.values())
out = {
    'scope':'Original v365 finite two-energy diagnostic only; no physical Hessian identity or all-field integral asserted.',
    'checked':len(checks),'total':len(checks),'checks':checks,
    'source_sum':str(s.expand_log(energy_sum,force=True)),
    'source_sum_numeric':float(energy_sum),
    'conditional_logdet_H':str(s.log(det_h)),
    'conditional_logdet_H_numeric':float(s.log(det_h)),
    'conditional_flat_two_real_coordinate_Z_for_stiffness_8pi_H':str(1/(4*s.sqrt(det_h))),
    'primitive_common_value_computed':False,
    'canonical_files_changed':False,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
