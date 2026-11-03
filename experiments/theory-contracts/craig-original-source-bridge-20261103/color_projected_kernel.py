"""Original center selector on the existing CAR chart; no primitive-source claim."""
import importlib.util
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
import numpy as np
import sympy as s

repo=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(repo/'verification'))
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path)
 out=importlib.util.module_from_spec(spec);sys.modules[name]=out;spec.loader.exec_module(out)
 return out
v=module('original_v1002',repo/'verification/v1002_spin10_mirror_projector.py')
d=module('original_v252',repo/'verification/v252_full_finite_triple.py')
weights=v.spin10_chiral_weights_doubled()
charges=[]
for w in weights:
 q=Fraction(w[0]+w[1]-2*w[2],2)
 if q.denominator!=1:raise RuntimeError('color weight')
 charges.append(int(q)%3)
checks={}
def ck(name,val):
 if not val:raise RuntimeError(name)
 checks[name]=True
ck('actual_carrier_center_multiplicities',Counter(charges)=={0:4,1:6,2:6})
n=len(charges);dim=1<<n
trial=np.zeros(dim,dtype=np.int8)
degree=np.zeros(dim,dtype=np.int8)
for state in range(1,dim):
 bit=state&-state;i=bit.bit_length()-1;prev=state^bit
 trial[state]=(int(trial[prev])+charges[i])%3
 degree[state]=degree[prev]+1
neutral=(trial==0)
ranks={str(q):int(np.sum(trial==q)) for q in range(3)}
bydegree={str(k):int(np.sum(neutral&(degree==k))) for k in range(n+1)}
ck('whole_color_sector_ranks',ranks=={'0':21856,'1':21840,'2':21840})
ck('degree_one_neutral_rank4',bydegree['1']==4)
ck('degree_two_neutral_rank42',bydegree['2']==42)
ck('exterior_oneparticle_neutral_rank16',2**charges.count(0)==16)
colored=[i for i,q in enumerate(charges) if q]
Gamma_p=np.ones(dim,dtype=bool)
for i in colored:Gamma_p &= ((np.arange(dim)&(1<<i))==0)
ck('center_projector_is_not_exterior_of_degree_one',not np.array_equal(neutral,Gamma_p))
i=charges.index(1);j=charges.index(2);pair=(1<<i)|(1<<j)
ck('charged_neutral_pair_retained',bool(neutral[pair]) and not bool(Gamma_p[pair]))
ann=v.mode_operator(n,i,False).tocoo()
ck('compressed_charged_field_is_zero',not np.any(neutral[ann.row]&neutral[ann.col]))

# Whole original 96 coefficient family. This is a matrix charge check,
# never quantization of its particle/antiparticle bookkeeping twice.
q=np.array([1 if name in ['u','d'] else 0 for name,ch,c,g in d.P])
q=np.concatenate([q,-q])
res=0.0;directions=0
for f in range(4):
 for a in range(3):
  for b in range(3):
   for value in [1,1j]:
    args=[np.zeros((3,3),complex) for _ in range(5)]
    args[f][a,b]=value
    D=d.full_D(*args)
    res=max(res,float(np.max(np.abs(D*(q[:,None]-q[None,:])))))
    directions+=1
for a in range(3):
 for b in range(a,3):
  for value in [1,1j]:
   args=[np.zeros((3,3),complex) for _ in range(5)]
   args[4][a,b]=args[4][b,a]=value
   D=d.full_D(*args)
   res=max(res,float(np.max(np.abs(D*(q[:,None]-q[None,:])))))
   directions+=1
ck('all84_original_directions_preserve_color_center',directions==84 and res==0)

# One actual color triplet: root-of-unity filter of its exact coherent
# exterior kernel and twisted trace. Variables are formal propagation
# coefficients, not newly chosen physical energies.
z=(-1+s.sqrt(3)*s.I)/2
r=s.symbols('r1:4',positive=True)
filtered=s.simplify(sum(s.prod(1+z**k*x for x in r) for k in range(3))/3)
ck('triplet_projected_trace',s.expand(filtered-(1+s.prod(r)))==0)
ck('degree1_filter_zero',s.simplify(sum(z**k for k in range(3)))==0)
ck('degree2_filter_zero',s.simplify(sum(z**(2*k) for k in range(3)))==0)
ck('baryon_degree3_filter_one',s.simplify(sum(z**(3*k) for k in range(3))/3)==1)
rr=s.symbols('r',positive=True)
for k in range(3):
 t=z**k
 C=s.simplify(t/(1+t*rr))
 ck(f'actual_twisted_Green_boundary_{k}',s.simplify(1-rr*C-t**(-1)*C)==0)

# Actual Craig Eq16 on the flat one-site periodic four-torus. The temporal
# SU3-center holonomy is embedded as diag(z,z,z,1,1) in SU5. Work on one
# actual triality-one field block; the opposite block conjugates it.
sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-s.I],[s.I,0]])
sz=s.diag(1,-1);I4=s.eye(4)
gam=[s.kronecker_product(sx,p) for p in [sx,sy,sz]]+[s.kronecker_product(sy,s.eye(2))]
g5=gam[0]*gam[1]*gam[2]*gam[3]
Ds=[];Ps=[]
def iszero(M):return all(s.simplify(x)==0 for x in M)
for k in range(3):
 theta=2*s.pi*k/3
 DW=(1-s.cos(theta))*I4+s.I*s.sin(theta)*gam[3]
 HW=g5*(DW-I4)
 ck(f'Craig_center_sector_Hsquare_{k}',iszero(HW*HW-I4))
 D=I4+g5*HW  # sign(HW)=HW exactly, including the k=0 zero-D sector.
 ck(f'Craig_center_sector_GW_{k}',iszero(g5*D+D*g5-D*g5*D))
 Phat=(I4-g5*(I4-D))/2
 ck(f'Craig_center_sector_chiral_projector_{k}',iszero(Phat*Phat-Phat))
 Ds.append(D);Ps.append(Phat)
Davg=s.simplify(sum(Ds,s.zeros(4))/3)
Pavg=s.simplify(sum(Ps,s.zeros(4))/3)
ck('averaged_Craig_operator_is_I',iszero(Davg-I4))
ck('averaged_Craig_operator_violates_GW',iszero(g5*Davg+Davg*g5-Davg*g5*Davg-g5))
ck('averaged_chiral_spaces_give_half_I',iszero(Pavg-I4/2))
ck('averaged_chirality_is_not_a_projector',iszero(Pavg*Pavg-Pavg+I4/4))

out={'result_id':'CRAIG20261103C','checks':checks,'passed':len(checks),
 'actual_spinor_weights_doubled':[list(w) for w in weights],
 'actual_color_trialities':charges,'fock_dimension':dim,
 'triality_sector_ranks':ranks,'neutral_rank_by_degree':bydegree,
 'original96_coefficient_directions':directions,'original96_commutator_max_residual':res,
 'scope':'Exact original color-center selector applied to its stated existing CAR realization. Not a proof that this is the complete original Padm/source map; other selectors and dynamic boson weights are retained as unresolved inputs.',
 'projected_coherent_kernel':'K_color(barv,u)=1/3 sum_(k=0)^2 exp(barv z^k R u)',
 'twisted_boundary':'psi(beta)=-z^(-k)psi(0)',
 'twisted_inverse':'Gk(t,s)=1_(t>s)R(t,s)-R(t,0)(I+z^k R(beta,0))^-1 z^k R(beta,s)',
 'actual_Craig_flat_center_test':{'spin_structure':'periodic','lattice':'one-site four-torus','plaquettes':'all identity','HW_squared':'I in all sectors','D0':'0','D1':'3I/2+i sqrt(3) gamma4/2','D2':'3I/2-i sqrt(3) gamma4/2','average_D':'I','average_GW_residual':'gamma5','average_Phat':'I/2','average_projector_defect':'-I/4'},
 'full_primitive_Sadm_kernel':'not_computed'}
Path(__file__).with_name('color-projected-kernel-results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
