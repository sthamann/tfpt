"""Evaluate the existing Spin4 x v252 branch; does not identify it with full S_adm."""
import importlib.util
import json
import sys
from pathlib import Path
import sympy as s

repo=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(repo/'verification'))
spec=importlib.util.spec_from_file_location('original_v252',repo/'verification/v252_full_finite_triple.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
KF=s.Matrix(v.Kswap()).applyfunc(lambda x:s.Integer(int(x)))
gF=s.Matrix(v.grading()).applyfunc(lambda x:s.Integer(int(x)))
I2=s.eye(2); I4=s.eye(4)
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
gam=[s.kronecker_product(pauli[0],q) for q in pauli]+[s.kronecker_product(pauli[1],I2)]
g5=gam[0]*gam[1]*gam[2]*gam[3]
C=gam[0]*gam[2]
checks={}
def zero(M):return all(s.simplify(x)==0 for x in M)
def ck(name,val):
 if not val:raise RuntimeError(name)
 checks[name]=True

ck('original_internal_dimension_96',KF.shape==(96,96))
ck('original_JF_square_plus',zero(KF*KF-s.eye(96)))
ck('original_JF_flips_internal_grading',zero(KF*gF+gF*KF))
ck('Spin4_J_square_minus',zero(C*C.conjugate()+I4))
ck('Spin4_J_preserves_spin_grading',zero(C*g5.conjugate()-g5*C))
ck('Spin4_conjugation_of_clifford',all(zero(C*q.conjugate()+q*C) for q in gam))
ck('spin_derivative_pairing_symmetric',all(zero((C.H*q).T-C.H*q) for q in gam))
ck('spin_mass_pairing_skew',zero((C.H*g5).T+C.H*g5))
ck('original_KF_symmetric',zero(KF.T-KF))

# No special Yukawa value is supplied. The full-family mass result follows
# from the original relations Phi*=Phi and KF bar(Phi)=Phi KF:
# (KF Phi)^T=bar(Phi) KF=KF Phi, hence the spin product is skew.
Gamma_diag=[int(g5[i,i]*gF[j,j]) for i in range(4) for j in range(96)]
ranks={str(e):sum(x==e for x in Gamma_diag) for e in [-1,1]}
ck('both_total_chiral_fibers_rank192',ranks=={'-1':192,'1':192})

# Symbolic whole original Yukawa/Majorana family, with the v252 index and
# constructor pattern. These are indeterminates, not newly fitted couplings.
Ys={}
for f in ['u','d','e','nu']:
 Ys[f]=s.Matrix(3,3,lambda i,j:s.Symbol(f'{f}r{i}{j}',real=True)+s.I*s.Symbol(f'{f}i{i}{j}',real=True))
MR=s.zeros(3)
for i in range(3):
 for j in range(i,3):
  MR[i,j]=MR[j,i]=s.Symbol(f'Mr{i}{j}',real=True)+s.I*s.Symbol(f'Mi{i}{j}',real=True)
S=s.MutableSparseMatrix(48,48,{})
for name,ch,c,g in v.P:
 if ch=='L':
  for gj in range(3):
   i,j=v.IDX[(name,'L',c,g)],v.IDX[(name,'R',c,gj)]
   S[i,j]=Ys[name][g,gj];S[j,i]=s.conjugate(S[i,j])
T=s.MutableSparseMatrix(48,48,{})
for i in range(3):
 for j in range(3):T[v.IDX[('nu','R',0,i)],v.IDX[('nu','R',0,j)]]=MR[i,j]
Phi=s.SparseMatrix.vstack(s.SparseMatrix.hstack(S,T),s.SparseMatrix.hstack(T.H,S.conjugate()))
ck('whole_symbolic_v252_Phi_hermitian',zero(Phi.H-Phi))
ck('whole_symbolic_v252_Phi_odd',zero(gF*Phi+Phi*gF))
ck('whole_symbolic_v252_reality',zero(KF*Phi.conjugate()-Phi*KF))
ck('finite_isolated_mass_pairing_symmetric',zero((KF*Phi).T-KF*Phi))
Mass=s.kronecker_product(s.SparseMatrix(C.H*g5),s.SparseMatrix(KF)*Phi)
for e in [-1,1]:
 inds=[i for i,x in enumerate(Gamma_diag) if x==e]
 Me=Mass.extract(inds,inds)
 ck(f'whole_product_mass_pairing_skew_{e}',zero(Me.T+Me))
 # Exact norm formula establishes nonzero mass action for every nonzero Phi,
 # rather than checking a specially chosen mass matrix.
 norm=s.expand(sum(s.conjugate(x)*x for x in Me.todok().values()))
 target=s.expand(2*s.trace(Phi*Phi))
 ck(f'whole_product_mass_norm_identity_{e}',s.expand(norm-target)==0)

# Actual free Craig Eq16, same momentum convention for the traditional
# Euclidean kinetic term i gamma.p on the flat product branch.
p=s.pi/2;G=gam[0]
Ktrad=s.I*G*p
D=I4+s.I*G
A=I4-D/2
Kreq=s.simplify(D*A.inv())
Phat=(I4-g5*(I4-D))/2
Pminus=(I4-g5)/2
Pplus=(I4+g5)/2
ck('Craig_GW_exact',zero(g5*D+D*g5-D*g5*D))
ck('Craig_maps_allowed_chirality',zero(D*Phat-Pplus*D))
ck('ordinary_kernel_maps_ordinary_chirality',zero(Ktrad*Pminus-Pplus*Ktrad))
ck('Craig_chiral_singular_value_sqrt2',zero(Phat*D.H*D*Phat-2*Phat))
ck('product_chiral_singular_value_pi_over2',zero(Pminus*Ktrad.H*Ktrad*Pminus-p**2*Pminus))
ck('required_kernel_is_2i_gamma1',zero(Kreq-2*s.I*G))
ck('product_kernel_not_required_kernel',not zero(Ktrad-Kreq))
ck('fieldmap_chiral_A_singular_value_one_over_sqrt2',zero(Phat*A.H*A*Phat-Phat/2))

out={'result_id':'CRAIG20261103B','scope':'Existing ordinary Spin4 product consumer with actual v252 JF and gammaF; its fermionic spectral-triple action is conditional and is not a proven full original S_adm identity.',
 'passed':len(checks),'checks':checks,'physical_fiber_ranks':ranks,
 'kernel':'D_product=-i gamma^mu nabla_mu tensor1 + gamma5 tensor Phi',
 'skew_kernel':'M_epsilon=E_epsilon^T (C4 tensor KF)^dagger D_product E_epsilon; transpose includes spacetime integration by parts',
 'free_charged_comparison':{'p':'pi/2','original_traditional_kinetic':'i gamma1 pi/2','Craig_D':'1+i gamma1','Cayley_required_K':'2 i gamma1','ordinary_chiral_singular_value':'pi/2','Craig_chiral_singular_value':'sqrt(2)','squared_singular_value_defect':str(s.pi**2/4-2),'kernel_norm_defect':str(2-s.pi/2)},
 'source_status':{'primitive_bosonic_trace_hessian_wrt_independent_fermions':0,'full_original_Sadm_Hessian':'not_computed','full_original_Craig_measure_equality':'not_proved'}}
Path(__file__).with_name('actual-product-results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
