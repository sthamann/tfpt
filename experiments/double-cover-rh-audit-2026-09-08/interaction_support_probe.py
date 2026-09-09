#!/usr/bin/env python3
"""Interaction support selects the earlier readout; finite-temperature response.

Exact finite source statements, not a derivation of the physical parent B or
an instruction to discard all uncoupled physical degrees of freedom.
"""
import hashlib
import json
from pathlib import Path

import numpy as np
import sympy as s

from seam_source import construct

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
CHECKS=[]
DATA={}


def check(name,ok):
    CHECKS.append({'name':name,'passed':bool(ok)})
    print(('PASS ' if ok else 'FAIL ')+name,flush=True)


def zero(M):
    return M.applyfunc(s.simplify)==s.zeros(*M.shape)


def err(M):
    return float(np.max(np.abs(M)))


def thermal(H,beta):
    e,V=np.linalg.eigh(H)
    return (V*(1/(1+np.exp(beta*e))))@V.conj().T


src=construct()
A,B=s.Matrix(src['A16_dep']),s.Matrix(src['A_int'])
I=s.eye(16)
O=s.zeros(16)
for i,j in enumerate(src['img']): O[j,i]=1
previous=json.loads((HERE/'clock_readout_results.json').read_text())
check('same_compiler_source',previous['provenance']['source_sha256']==src['provenance']['source_sha256'])
Pold=s.Matrix([[s.sympify(x) for x in row] for row in previous['data']['P']])
x=s.symbols('x')
p=s.Poly((x+1)*(x+3)*(x**3+43*x*x+459*x+81),x)
pB=s.zeros(16)
for (k,),c in p.terms(): pB+=c*B**(2*k)
P=I-pB/243
check('interaction_rank_twelve',B.rank()==12)
check('polynomial_support_equals_saved_readout',P==Pold)
check('support_projector_and_interaction_exact',P.T==P and P**2==P and P.rank()==12 and P*B==B and B*P==B)
check('kernel_polynomial_certificate',pB**2==243*pB and B*pB==s.zeros(16) and pB.rank()==4)
check('full_minimal_polynomial_B2',B**2*pB==s.zeros(16)
      and s.Matrix.hstack(*[(B**(2*k)).reshape(256,1) for k in range(6)]).rank()==6)
check('interaction_kernel_is_boundary_dark',all(all(v[i]==0 for i in range(10)) for v in B.nullspace())
      and all(sum(v[10+2*j+r] for j in range(3))==0 for v in B.nullspace() for r in range(2)))
check('support_does_not_need_clock_or_reflection_input',P*A==A*P and P*O==O*P)

# Full Hamiltonian support is a different selection: the uncoupled boundary
# modes have nonzero bare energy when u != 0.
H=s.Rational(1)*A+B/8
check('full_H_support_is_not_interaction_support',H.rank()==16 and A*(I-P)!=s.zeros(16))

# Port closures: source-generated, no spectral data. Closure under A,B,O,O^T
# is formed from exact column spans. U invariance of the resulting projectors
# is checked using the saved rational reflection, never imposed on the seeds.
g=json.loads((HERE/'seam_geometry_results.json').read_text())
U=s.Matrix([[s.Rational(x) for x in row] for row in g['data']['reflection']['U']])
bright=s.zeros(16,2)
for j in range(3):bright[10+2*j:12+2*j,:]=s.eye(2)
seeds={'bright_boundary':bright,'carrier_three_orbit_one_pair':I[:,:2],
       'carrier_two_orbit_one_pair':I[:,6:8],
       'one_pair_each_orbit':s.Matrix.hstack(I[:,:2],I[:,6:8]),
       'all_carrier':I[:,:10],'full_boundary':I[:,10:]}
expected={'bright_boundary':6,'carrier_three_orbit_one_pair':10,
          'carrier_two_orbit_one_pair':8,'one_pair_each_orbit':12,
          'all_carrier':12,'full_boundary':10}
ports={}
for name,seed in seeds.items():
    basis=s.Matrix.hstack(*seed.columnspace())
    while True:
        enlarged=s.Matrix.hstack(basis,*[M*basis for M in (A,B,O,O.T)])
        nxt=s.Matrix.hstack(*enlarged.columnspace())
        if nxt.cols==basis.cols:break
        basis=nxt
    Q=basis*(basis.T*basis).inv()*basis.T
    ports[name]={'rank':basis.cols,'clock_fixed_rank':int((sum((O**k for k in range(6)),s.zeros(16))/6*Q).rank()),
                 'reflection_preserved':zero(Q*U-U*Q)}
    check('port_closure_'+name,basis.cols==expected[name] and zero(Q*U-U*Q))
    if name in ('one_pair_each_orbit','all_carrier'):
        check('port_reconstructs_support_'+name,Q==P)
DATA['port_closures']=ports

# Two independent canonical blocks: boundary-reachable interaction support,
# and the nontrivial-clock support. Faithful C6 alone selects neither sum.
Pi0=sum((O**k for k in range(6)),s.zeros(16))/6
Pactive=P*Pi0
Pclock=P*(I-Pi0)
check('canonical_six_plus_six_split',Pactive.rank()==6 and Pclock.rank()==6
      and Pactive+Pclock==P and Pactive*Pclock==s.zeros(16)
      and zero(U*Pactive-Pactive*U) and zero(U*Pclock-Pclock*U))
check('clock_complete_sector_can_be_boundary_disjoint',Pclock[:,10:]==s.zeros(16,6)
      and all((O**k-I)*Pclock!=s.zeros(16) for k in (1,2,3)))

# Finite-beta proof: A and B commute, so simultaneous eigenvectors diagonalize
# H0 and Ht. Strict monotonicity of f_beta makes f(Ht)-f(H0) zero iff B=0
# on that eigenvector (t!=0). Therefore its support is exactly P.
check('joint_source_diagonalization_premise',A.T==-A and B.T==-B and A*B==B*A and A**2==-I)
An,Bn,Pn=[np.array(M,complex) for M in (A,B,P)]
rows=[]
for u,t,beta in ((1,.125,.5),(1,.125,1),(1,.125,2),(.5,.2,1),(1,-.125,1),(0,.2,1)):
    C0=thermal(-1j*u*An,beta)
    Ct=thermal(-1j*(u*An+t*Bn),beta)
    delta=Ct-C0
    e,V=np.linalg.eigh(delta)
    active=np.abs(e)>1e-10
    Pr=(V*active)@V.conj().T
    rows.append({'u':u,'t':t,'beta':beta,'rank':int(sum(active)),
        'support_error':err(Pr-Pn),'outside_support':err((np.eye(16)-Pn)@delta),
        'smallest_active_response':float(np.min(np.abs(e[active])))})
check('finite_temperature_response_support_six_samples',all(r['rank']==12 and r['support_error']<1e-10 and r['outside_support']<1e-12 for r in rows))
DATA['finite_response_samples']=rows

# At t=0, the scalar Fermi derivative gives dC/dt = i a(beta,u) B with
# a=beta/(4 cosh(beta u/2)^2). Numerical central differences only ward the
# analytic identity; halving the step checks truncation error decreases.
derivatives=[]
for u,beta in ((1,.5),(1,1),(.5,2)):
    scale=beta/(4*np.cosh(beta*u/2)**2)
    target=1j*scale*Bn
    errors=[]
    for h in (1e-3,5e-4):
        cp=thermal(-1j*(u*An+h*Bn),beta)
        cm=thermal(-1j*(u*An-h*Bn),beta)
        errors.append(err((cp-cm)/(2*h)-target))
    derivatives.append({'u':u,'beta':beta,'scale':float(scale),'errors':errors})
check('linear_response_identity_with_step_convergence',all(r['errors'][1]<.3*r['errors'][0] and r['errors'][1]<1e-6 for r in derivatives))
DATA['linear_response']=derivatives

# Zero-temperature limitation, not concealed by eigenvalue clipping.
# For u=1 the first positive crossing is the single positive root of
# 1+t-21t^2-9t^3. Below it all signs match the bare A sign sectors.
t=s.symbols('t')
gap=s.Poly(1+t-21*t*t-9*t**3,t)
check('first_gap_root_exact_interval',gap.count_roots(s.Rational(23,100),s.Rational(24,100))==1
      and gap.count_roots(0,s.oo)==1)


def ground(coupling):
    e,V=np.linalg.eigh(-1j*(An+coupling*Bn))
    return (V*(e<0))@V.conj().T


g0=ground(0)
ground_rows=[{'t':t,'difference':err(ground(t)-g0)} for t in (.125,.2,.3)]
check('ground_response_plateau_and_first_change',max(r['difference'] for r in ground_rows[:2])<1e-12 and ground_rows[2]['difference']>.1)
DATA['ground_control']={'samples':ground_rows,'first_positive_gap_t_u1':float([r for r in s.nroots(gap) if abs(s.im(r))<1e-12 and s.re(r)>0][0]),
    'scope':'finite-beta support theorem does not extend to the ground-state plateau'}

DATA['support_polynomial']={'variable':'x=B^2','annihilator_nonzero_spectrum':str(p.as_expr()),
    'projector':'P = I - p(B^2)/243','B_rank':12,'kernel_rank':4,
    'uniqueness':'P is the unique orthogonal projector satisfying B=PBP and ker(B restricted to im P)=0',
    'scope':'minimal complete interaction sector; not a proof that the physical parent discards bare spectators'}
result={'passed':sum(c['passed'] for c in CHECKS),'total':len(CHECKS),'checks':CHECKS,'data':DATA,
    'provenance':src['provenance'],
    'source_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in (Path(__file__),HERE/'seam_source.py',HERE/'clock_readout_results.json',HERE/'seam_geometry_results.json')}}
(HERE/'interaction_support_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(f"{result['passed']}/{result['total']} passed. FINITE INTERACTION SECTOR ONLY.")
raise SystemExit(0 if result['passed']==result['total'] else 1)
