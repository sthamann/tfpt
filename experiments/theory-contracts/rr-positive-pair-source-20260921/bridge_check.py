import json
from math import comb
import sympy as s

checks=[]
def need(v,label):
    if not v:
        raise RuntimeError(label)
    checks.append(label)
I=s.eye(5); R=s.diag(1,s.I,-1,-s.I,1); h=s.diag(0,1,2,3,4)
S=s.zeros(5)
for j in range(5): S[4-j,j]=-1
P=(I+R+R**2+R**3)/4
need(P==s.diag(1,0,0,0,1),'active_projector_is_rotation_fixed_space')
need(P*P==P and P.conjugate().T==P,'active_orthogonal_projector')
need(P*S==S*P and P*h==h*P,'active_projection_preserves_D4_and_clock')
need(S*h*S==4*I-h,'full_RR_affine_reflection')
need(set(h.diagonal())-{0,4}=={1,2,3},'missing_three_frequencies_for_same_Q2_time_intertwiner')
z,k=s.symbols('z k',nonzero=True)
H=k*s.Matrix([[2,2],[2,2]])
r=(z*s.eye(2)-H).inv()[0,0]
need(s.simplify(r-(z-2*k)/(z*(z-4*k)))==0,'bright_pair_resolvent')
eff=2*k+4*k*k/(z-2*k)
need(s.simplify(eff-2*k*z/(z-2*k))==0,'Schur_saturated_energy_response')
need(eff.subs(z,0)==0,'static_pair_response_cancels')
need(s.limit(z*r,z,0)==s.Rational(1,2),'zero_energy_bright_residue')
need(s.limit((z-4*k)*r,z,4*k)==s.Rational(1,2),'four_kappa_bright_residue')
need(sum(comb(64,q) for q in range(4))==43745,'positivity_protected_low_sector_kernel_count')
print(json.dumps({'status':'PASS','scope':'exact symbolic finite RR projection, bright resolvent and binomial count; general theorems require written proofs','checks':checks},indent=2))
