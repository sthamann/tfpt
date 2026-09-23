"""Independent exact power-law and background-identity normalization controls."""
from pathlib import Path
import json
import math
import sympy as s
from mode_transfer import observables


class PowerLaw:
    end=100.
    def at(self,n):
        eps=.01
        p=-math.sqrt(2*eps)
        H=1e-5*math.exp(-eps*(n-46.))
        return p*(n-46.),p,eps,H,0.,0.


def main():
    p,u,w=s.symbols('p u w')
    eps=p*p/2
    F=-(3-eps)*(p+u)
    Fphi=-(3-eps)*(w-u*u)
    m=-(Fphi*p+s.diff(F,p)*F+(3-eps)*F)/p
    expected=(3-eps)*w-p**4/2+2*p*(3-eps)*u+3*p*p
    if s.factor(m-expected)!=0:
        raise RuntimeError('mass term is inconsistent with exact curvature equation')
    got=observables(PowerLaw(),54.,start_ratio=3000.,rtol=2e-12,atol=2e-14)
    epsilon=.01
    nu=(3-epsilon)/(2*(1-epsilon))
    correction=2**(2*nu-1)*math.gamma(nu)**2/math.pi*(1-epsilon)**(2*nu-1)
    targetAs=1e-10/(8*math.pi**2*epsilon)*correction
    targetNs=1-2*epsilon/(1-epsilon)
    errors={'As_relative':got['As']/targetAs-1,
            'ns_absolute':got['ns']-targetNs,'r_absolute':got['r']-16*epsilon}
    if abs(errors['As_relative'])>3e-7 or abs(errors['ns_absolute'])>1e-7 or abs(errors['r_absolute'])>1e-10:
        raise RuntimeError(str(errors))
    # A missing polarization or using the horizon amplitude fails the controls.
    if abs(got['r']/2-16*epsilon)<.07:
        raise RuntimeError('missing tensor polarization was not detected')
    ratio=got['central_mode']['scalar_horizon_amplitude_over_final']
    if ratio<1.8:
        raise RuntimeError('premature horizon evaluation was not detected')
    out={'status':'PASS','power_law_epsilon':epsilon,'H_at_pivot':1e-5,
         'closed_hankel_solution':{'As':targetAs,'ns':targetNs,'r':16*epsilon},
         'computed':got,'errors':errors,'exact_effective_mass_identity':True,
         'negative_missing_tensor_polarization_detected':True,
         'negative_horizon_readout_detected':True}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':'PASS','errors':errors},indent=2))


if __name__=='__main__':
    main()
