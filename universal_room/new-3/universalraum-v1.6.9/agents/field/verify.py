"""Exact degree-one Lorentz readout for the mixed-handed six-dimensional carrier.

The momentum bispinor is an explicit additional input. No momentum,
spacetime, kinetic operator, or physical instrument is derived from W.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import json
import sympy as s

HERE=Path(__file__).resolve().parent
PINS={
 'sources/field_dictionary.py':'a581bacd17c08dd9a766ae439bfe1e8e35e6d30b9509cb9d98053b897d8ecc13',
 'sources/v167_BIG_PICTURE.md':'856079607a0c4071698f6bd1286c80df3a1d1bf66e8e4e77d5c3a9da943c651c',
 'sources/v168_late_field.json':'cfd9e15cec5c2b0ce3de9397614836b16b24b4adb8f6711eb704925589965774',
 'sources/v168_verify_late_field.py':'f18e6fd2af7c1a28a81e85654df68fe805e59b1d957801611d2668678550dfc2'}
checks=[]

def need(ok,name):
 if not bool(ok):raise RuntimeError(name)
 checks.append(name)

def eq(a,b,name):
 d=a-b
 need(all(s.simplify(x)==0 for x in d) if isinstance(d,s.MatrixBase) else s.simplify(d)==0,name)

def clean(a):return a.applyfunc(s.factor)
def mj(a):return [[str(x) for x in row] for row in a.tolist()]

def readout(p):
 a,b,c,d=p[0,0],p[0,1],p[1,0],p[1,1]
 return s.Matrix([[d,-c,-b,a,0,0],[0,0,d,-c,-b,a]])

def insertion(p):
 a,b,c,d=p[0,0],p[0,1],p[1,0],p[1,1]
 return s.Matrix([[2*a,0],[2*b,0],[c,a],[d,b],[0,2*c],[0,2*d]])

def sym2(m):
 a,b,c,d=m[0,0],m[0,1],m[1,0],m[1,1]
 return s.Matrix([[a*a,2*a*b,b*b],[a*c,a*d+b*c,b*d],[c*c,2*c*d,d*d]])

def hom_equations(incoming,outgoing):
 n=incoming[0].rows;k=outgoing[0].rows
 return s.Matrix.vstack(*[s.kronecker_product(b,s.eye(n))-s.kronecker_product(s.eye(k),a.T)
                          for a,b in zip(incoming,outgoing)])

def main():
 for name,digest in PINS.items():need(sha256((HERE/name).read_bytes()).hexdigest()==digest,'frozen pin '+name)
 previous=json.loads((HERE/'sources/v168_late_field.json').read_text())
 oldC=s.Matrix([[s.sympify(x) for x in row] for row in previous['epsilon_contraction_C']])
 oldR=s.Matrix([[s.sympify(x) for x in row] for row in previous['insertion_R']])
 eq(oldC*oldR,s.eye(2),'frozen same-handed comparison adapter')
 a,b,c,d=s.symbols('p00 p01 p10 p11');p=s.Matrix([[a,b],[c,d]])
 cp=readout(p);jp=insertion(p);det=p.det()
 eq(cp*jp,3*det*s.eye(2),'degree-one extraction insertion product equals three p-squared')
 # These four minors prove rank two for EVERY nonzero complex p, including null.
 minors=[]
 for cols,target in zip(((0,2),(1,3),(2,4),(3,5)),(d*d,c*c,b*b,a*a)):
  minor=cp[:,cols].det();eq(minor,target,'readout minor '+str(cols));minors.append(str(minor))
 for rows,target in zip(((0,2),(1,3),(2,4),(3,5)),(2*a*a,2*b*b,2*c*c,2*d*d)):
  eq(jp[rows,:].det(),target,'insertion minor '+str(rows))
 eq(readout(s.zeros(2)),s.zeros(2,6),'zero momentum gives zero derivative readout')
 # Complexified Lorentz Lie algebra sl2_L plus sl2_R.
 E=s.Matrix([[0,1],[0,0]]);F=E.T;H=s.diag(1,-1)
 E1=s.Matrix([[0,2,0],[0,0,1],[0,0,0]])
 F1=s.Matrix([[0,0,0],[1,0,0],[0,2,0]]);H1=s.diag(2,0,-2)
 # A literal derivative-free bdag ff scalar fixes which adjoint field is
 # left-handed; the internal mode symbol alone does not fix that choice.
 spin_one_pairing=s.Matrix([[0,0,1],[0,-2,0],[1,0,0]])
 for tag,y in zip(('E','F','H'),(E1,F1,H1)):
  eq(y.T*spin_one_pairing+spin_one_pairing*y,s.zeros(3),'left-left spin-one scalar pairing '+tag)
 mixed_boson=[s.kronecker_product(y,s.eye(3)) for y in (E1,F1,H1)]+[s.kronecker_product(s.eye(3),y) for y in (E1,F1,H1)]
 need(hom_equations(mixed_boson,[s.zeros(1)]*6).rank()==9,'opposite-handed spin-one product has no Lorentz scalar')
 tensor_gens=[];momentum_gens=[];output_gens=[]
 for side in ('L','R'):
  for x,y in zip((E,F,H),(E1,F1,H1)):
   tensor_gens.append(s.kronecker_product(y,s.eye(2)) if side=='L' else s.kronecker_product(s.eye(3),x))
   momentum_gens.append(s.kronecker_product(x,s.eye(2)) if side=='L' else s.kronecker_product(s.eye(2),x))
   output_gens.append(x if side=='L' else s.zeros(2))
 zero_eq=hom_equations(tensor_gens,output_gens)
 need(zero_eq.rank()==12,'no momentum-free mixed-handed to left-Weyl intertwiner')
 basis=[]
 for i in range(4):
  q=s.zeros(2);q[i//2,i%2]=1;basis.append(q)
 linear=s.Matrix.hstack(*[readout(q) for q in basis])
 joint_gens=[s.kronecker_product(x,s.eye(6))+s.kronecker_product(s.eye(4),y)
             for x,y in zip(momentum_gens,tensor_gens)]
 for i,(x,y) in enumerate(zip(joint_gens,output_gens)):
  eq(linear*x,y*linear,'full degree-one Lorentz intertwining '+str(i))
 one_eq=hom_equations(joint_gens,output_gens)
 need(one_eq.rank()==47,'degree-one equivariant readout space dimension one out of48 coefficients')
 # Finite transformations include boosts and complex null rotations.
 transformations=[s.diag(2,s.Rational(1,2)),s.Matrix([[1,1],[0,1]]),s.Matrix([[1,s.I],[0,1]]),
                  s.Matrix([[1,1+s.I],[1,2+s.I]])]
 for i,m in enumerate(transformations):
  eq(m.det(),1,'finite SL2 matrix determinant '+str(i))
  dp=s.kronecker_product(sym2(m),m.conjugate());pnew=m*p*m.H
  eq(readout(pnew)*dp,m*cp,'finite Lorentz readout covariance '+str(i))
  eq(insertion(pnew)*m,dp*jp,'finite Lorentz insertion covariance '+str(i))
 rp=jp/(3*det);projector=clean(rp*cp)
 epsilon=s.Matrix([[0,1],[-1,0]])
 handedness_adapter=s.kronecker_product(s.eye(3),p*epsilon.T)
 eq(oldC*handedness_adapter,cp,'new readout factors through old same-handed epsilon adapter')
 eq(handedness_adapter.inv()*oldR,rp,'non-null insertion transports old same-handed insertion')
 eq(handedness_adapter.inv()*(oldR*oldC)*handedness_adapter,projector,'non-null projector transports frozen same-handed projector')
 eq(cp*rp,s.eye(2),'non-null covariant right inverse')
 eq(projector*projector,projector,'non-null covariant projector idempotent')
 eq(s.trace(projector),2,'non-null covariant projector rank two')
 # Rest and null kernels, represented by independent exact columns.
 prest=s.eye(2);pnull=s.diag(1,0)
 cre=readout(prest);cnu=readout(pnull);jnu=insertion(pnull)
 kre=s.Matrix.hstack(s.eye(6)[:,1],s.eye(6)[:,4],s.eye(6)[:,0]-s.eye(6)[:,3],s.eye(6)[:,2]-s.eye(6)[:,5])
 knu=s.eye(6)[:,(0,1,2,4)]
 eq(cre*kre,s.zeros(2,4),'timelike-rest four-dimensional kernel')
 eq(cnu*knu,s.zeros(2,4),'null four-dimensional kernel')
 need(kre.rank()==4 and knu.rank()==4 and cre.rank()==cnu.rank()==2,'timelike and null exact ranks')
 nil=jnu*cnu
 eq(cnu*jnu,s.zeros(2),'null insertion image lies in readout kernel')
 eq(nil*nil,s.zeros(6),'null numerator is nilpotent rather than a projector')
 need(jnu.rank()==2 and nil.rank()==2,'null insertion and nilpotent numerator rank two')
 # Null little group forbids a p-only Lorentz-covariant right inverse.
 left=s.kronecker_product(E1,s.eye(2));right=s.kronecker_product(s.eye(3),E)
 nreal=left+right;nimag=s.I*(left-right)
 eq(E*pnull+pnull*E.T,s.zeros(2),'real null rotation fixes chosen null momentum')
 eq(s.I*E*pnull+pnull*(s.I*E).H,s.zeros(2),'imaginary null rotation fixes chosen null momentum')
 selector=s.Matrix.vstack(s.eye(6)[2,:],s.eye(6)[4,:])
 eq(cnu,selector*right,'readout factors through right null-rotation generator')
 unknown=s.Matrix(6,2,s.symbols('r0:12'))
 equations=list(nreal*unknown-unknown*E)+list(nimag*unknown-unknown*(s.I*E))+list(cnu*unknown-s.eye(2))
 lhs,rhs=s.linear_eq_to_matrix(equations,list(unknown))
 lr=lhs.rank();ar=lhs.row_join(rhs).rank()
 need(lr<ar,'exact inconsistent null right-inverse little-group system')
 # One extra covariant reference vector repairs the right inverse, not its origin.
 qa,qb,qc,qd=s.symbols('q00 q01 q10 q11');q=s.Matrix([[qa,qb],[qc,qd]])
 k=clean(cp*insertion(q));sigma=s.trace(q*p.adjugate())
 eq(k,sigma*s.eye(2)+q*p.adjugate(),'two-vector cross-contraction formula')
 eq(k.det(),2*sigma**2+p.det()*q.det(),'cross-contraction determinant')
 rn=insertion(prest)*(cnu*insertion(prest)).inv()
 eq(cnu*rn,s.eye(2),'null finite right inverse with timelike reference q')
 eq((rn*cnu)**2,rn*cnu,'reference-dependent null projector idempotent')
 need((rn*cnu).rank()==2,'reference-dependent null projector rank two')
 for i,m in enumerate(transformations):
  dp=s.kronecker_product(sym2(m),m.conjugate())
  pp=m*pnull*m.H;qq=m*prest*m.H
  rr=insertion(qq)*(readout(pp)*insertion(qq)).inv()
  eq(rr*m,dp*rn,'two-vector null inverse Lorentz covariance '+str(i))
 # A rank-two spinor readout does not by itself solve the massless Weyl equation.
 weyl_constraint=pnull.adjugate()*cnu
 need(weyl_constraint.rank()==1,'null Weyl equation imposes one additional independent constraint')
 allowed=s.Matrix.hstack(*weyl_constraint.nullspace())
 need(allowed.rank()==5 and (cnu*allowed).rank()==1,'null on-shell restriction leaves one Weyl polarization')
 need((pnull.adjugate()*cnu)!=s.zeros(2,6),'readout does not automatically enforce massless kinetics')
 # Early kinetic gate: on two free massless constituent fields the unique
 # derivative channel is an equation-of-motion divergence and vanishes.
 # Independent dotted spinors make this a complex polynomial identity;
 # physical real momenta follow by setting dotted partners to conjugates.
 l0,l1,L0,L1,u0,u1,U0,U1=s.symbols('l0 l1 L0 L1 u0 u1 U0 U1')
 lam=s.Matrix([l0,l1]);lbar=s.Matrix([L0,L1])
 mu=s.Matrix([u0,u1]);mbar=s.Matrix([U0,U1]);epsilon=s.Matrix([[0,1],[-1,0]])
 pf=lam*lbar.T;ppsi=mu*mbar.T;strength=lam*lam.T
 composed=s.Matrix([strength[i,j]*mbar[k] for i,j in ((0,0),(0,1),(1,1)) for k in range(2)])
 eq(pf.det(),0,'free field-strength constituent momentum null')
 eq(ppsi.det(),0,'free Weyl constituent momentum null')
 eq(strength*epsilon*pf,s.zeros(2),'free self-dual field-strength equation')
 eq(ppsi*epsilon*mbar,s.zeros(2,1),'free opposite-handed Weyl equation')
 eq(readout(pf+ppsi)*composed,s.zeros(2,1),'total derivative readout vanishes on free massless constituents')
 eq(readout(s.eye(2))*s.eye(6)[:,1],s.zeros(2,1),'noncollinear null constituents can have timelike total momentum but zero derivative readout')
 # Positive covariant fiber metric exists on a prescribed future-timelike orbit.
 embed=s.zeros(8,6)
 for col,(ab,dd) in enumerate((ab,dd) for ab in ((0,0),(0,1),(1,1)) for dd in range(2)):
  for aa,bb in set((ab,ab[::-1])):embed[4*aa+2*bb+dd,col]=1
 gram=embed.T*embed;pi0=insertion(prest)*readout(prest)/3
 eq(pi0.H*gram,gram*pi0,'massive rest projector orthogonal in correct tensor metric')
 for i,m in enumerate(transformations):
  pp=m*m.H;dp=s.kronecker_product(sym2(m),m.conjugate())
  metric=embed.H*s.kronecker_product(pp.inv(),pp.inv(),pp.conjugate().inv())*embed
  eq(metric,dp.inv().H*gram*dp.inv(),'positive timelike fiber metric covariance '+str(i))
  pi=insertion(pp)*readout(pp)/(3*pp.det())
  eq(pi.H*metric,metric*pi,'timelike projector metric self-adjointness '+str(i))
 # Neutral derivatives do not change exact native U(1) charges.
 qf,qfd,qb,qbd=-1,1,-2,2
 need(qb+qfd==-1 and qbd+qfd==3,'distinct native D and chi-dagger charges')
 need((qb+qfd)%4==(qbd+qfd)%4,'charge coincidence only modulo four')
 need((qb+qfd)+0==-1 and (qbd+qfd)+0==3,'neutral derivative cannot identify the two charges')
 result={'status':'PASS','exact_checks':len(checks),'numerical_checks':0,'checks':checks,'pins':PINS,
 'readout':{'C_p':mj(cp),'J_p':mj(jp),'C_p_J_p':'3 det(p) I2','minimal_momentum_degree':1,'equivariant_degree_one_dimension':1,
            'all_nonzero_momenta_rank':2,'all_nonzero_momenta_kernel_dimension':4,'rank_certifying_minors':minors},
 'timelike':{'rest_kernel':mj(kre),'right_inverse':'J_p/(3 det(p))','projector':'J_p C_p/(3 det(p))','positive_fiber_metric_conditional_on_future_timelike_p':True},
 'null':{'kernel':mj(knu),'numerator_rank':2,'numerator_square_zero':True,'p_only_covariant_right_inverse_exists':False,
         'inconsistent_system_ranks':[lr,ar],'with_q_rest_right_inverse':mj(rn),'with_q_rest_projector':mj(rn*cnu),
         'massless_Weyl_constraint_rank':1,'on_shell_allowed_T_dimension':5,'on_shell_readout_dimension':1},
 'extra_reference':{'cross_contraction':'C_p J_q = sigma I + q adj(p), sigma=tr(q adj(p))',
                    'determinant':'2 sigma^2 + det(p) det(q)','reference_needed_for_null_right_inverse':True},
 'charges':{'D_b_fdag':-1,'chi_dag_bdag_eta_fdag':3,'momentum_or_derivative':0},
 'literal_vertex_chirality':{'if_f_left_and_bdag_ff_scalar':'bdag is (1,0); b is (0,1); D is dotted same-handed; chi-dagger is mixed',
                             'if_b_itself_left_and_dagger_literal':'D is mixed; bare bdag ff has no Lorentz scalar',
                             'field_mode_adapter_can_change_literal_identification':True},
 'early_kinetic_gate':{'free_massless_constituents_divergence_identically_zero':True,
                       'zero_not_limited_to_collinear_momenta':True,
                       'nonzero_free_Weyl_pole_demonstrated':False},
 'scope':{'Lorentz_vector_p_added_as_input':True,'native_momentum_derived':False,'spacetime_derived':False,
          'positive_kinetic_theory_derived':False,'native_field_adapter_derived':False,'same_handed_alternative_excluded':False,
          'underlying_creation_mode_Lorentz_type_assumed_from_dagger':False,'no_commit_or_promotion':True}}
 print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
