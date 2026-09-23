"""Exact algebra controls for the source-derived joint pair/mediator response.

Analytic infinite-dimensional statements are proved in the accompanying note.
This checker does not infer CAR/CCR or physical source selection.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sympy as s

CHECKS = []

def equal(name, lhs, rhs):
    diff = lhs-rhs
    values = list(diff) if isinstance(diff, s.MatrixBase) else [diff]
    if any(s.simplify(v) != 0 for v in values):
        raise RuntimeError(name)
    CHECKS.append(name)

rho, x, lam = s.symbols('rho x lambda', positive=True)
nu, a, b = s.symbols('nu a b', real=True)
xi = a+s.I*b
d = rho**2*(2-rho)/(2*(1-rho)**3)
o = (2-rho)/(2*(1-rho)**2)
gb = s.factor(d+8*o)
pb = 8/gb
q1 = s.factor(12*rho/(gb-8))
qd = s.factor(rho**2/d)

equal('pasted_mobius_8_over_27', s.Rational(8,27)-2*x*(1-x)**2,
      s.Rational(2,27)*(3*x-1)**2*(4-3*x))
HM = s.Matrix([[nu,s.sqrt(2)*s.conjugate(xi),0],
               [s.sqrt(2)*xi,2*nu,s.sqrt(6)*s.conjugate(xi)],
               [0,s.sqrt(6)*xi,3*nu]])
equal('pasted_mobius_second_jet', (HM*HM)[:2,:2]-HM[:2,:2]**2,
      s.diag(0,6*(a*a+b*b)))
equal('bright_gram_factor',gb,(2-rho)*(rho**2-8*rho+8)/(2*(1-rho)**3))
equal('tail_lowest_grade_weight',q1,24*(1-rho)**3/((4-3*rho)*(6-5*rho)))
equal('tail_error_positive_remainder',2*rho-(1-q1),
      rho*(2-rho)*(7-6*rho)/((4-3*rho)*(6-5*rho)))
equal('dark_error_positive_remainder',s.Rational(5,2)*rho-(1-qd),
      rho**2*(7-4*rho)/(2*(2-rho)))
equal('bright_error_positive_remainder',s.Rational(3,2)*rho-(1-pb),
      rho**2*(4-3*rho**2)/(2*(2-rho)*(rho**2-8*rho+8)))
equal('new_tail_limit',s.limit(q1,rho,0),1)
equal('dark_limit',s.limit(qd,rho,0),1)
equal('overlap_limit',s.limit(pb,rho,0),1)

c = s.symbols('c',positive=True)
u,v=s.symbols('u v',real=True)
# Rotation from normalized visible plus/minus to primary/orthogonal-tail.
rotation=s.Matrix([[u,-v],[v,u]])
gram_rotation=rotation.T*rotation
equal('rotation_norm',gram_rotation,(u*u+v*v)*s.eye(2))
Kpm=s.diag(3,4)
had=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
K=had*Kpm*had
equal('derived_bright_collision_block',K,s.Matrix([[s.Rational(7,2),-s.Rational(1,2)],[-s.Rational(1,2),s.Rational(7,2)]]))
equal('relative_block_saturation',(K-3*s.eye(2)).det(),0)
equal('absolute_block_positive_determinant',K.det(),12)
equal('collision_exchange_at_pi',had*s.diag(-1,1)*had,s.Matrix([[0,-1],[-1,0]]))

vlam=s.Matrix([lam,1])/s.sqrt(1+lam**2)
Klam=4*s.eye(2)-vlam*vlam.T
equal('rescaled_block_lambda_one',Klam.subs(lam,1),K)
prob=4*lam**2/(1+lam**2)**2
equal('normalization_loss_factorization',1-prob,(lam**2-1)**2/(lam**2+1)**2)
equal('lambda_two_transfer_probability',prob.subs(lam,2),s.Rational(16,25))
equal('source_spectral_rank',60+60+1956,2076)

# The full CAR pair answer from the source is not asserted by this checker.
# These are exact checks on the existing rational spectral response.
for n in range(8):
    coeff=s.expand(s.series(gb,rho,0,8).removeO()).coeff(rho,n)
    target=s.Integer(8) if n==0 else s.Rational((n+2)*(n+15),4)
    equal(f'bright_spectral_weight_{n}',coeff,target)

parser=argparse.ArgumentParser()
parser.add_argument('--out',type=Path,default=Path(__file__).with_name('joint_response_certificate.json'))
args=parser.parse_args()
repo=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
inputs=['experiments/theory-contracts/source-pair-transfer-20260920/PROOF.md',
        'experiments/theory-contracts/source-pair-transfer-20260920/certificate.json',
        'experiments/theory-contracts/source-dressed-native-20260920/PROOF.md']
pins={p:hashlib.sha256((repo/p).read_bytes()).hexdigest() for p in inputs}
data={'research_id':'UR.SOURCE.JOINT_RESPONSE.01','verdict':'PARTIAL',
      'scope':'Exact algebra of conditional source response; no full Fock or physical theory reconstruction.',
      'exact_checks':len(CHECKS),'checks':CHECKS,'source_sha256':pins,
      'new_joint_collision_spectrum':{'3':60,'4':60,'5':1956},
      'normalization_control_lambda_2_max_transfer':'16/25',
      'uniform_realtime_bound':'min(2, 4*rho+sqrt(3*rho)), 0<rho<1',
      't1_t8_closed':False,'full_car_ccr_intertwiner':False,
      'infinite_theorems_basis':'Analytic source series and proof, not finite coefficient samples.'}
args.out.parent.mkdir(parents=True,exist_ok=True)
args.out.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
print(json.dumps({'verdict':data['verdict'],'exact_checks':len(CHECKS)},sort_keys=True))
