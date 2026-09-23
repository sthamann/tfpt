"""Exact finite field-adapter audit, separately frozen from the shadow suite.

This verifies conditional representation maps, not a native Lorentz adapter.
The dagger ambiguity is deliberately retained: a mode creation coefficient
alone is not an adjoint Weyl field with already assigned Lorentz indices.
"""
from pathlib import Path
from hashlib import sha256
from itertools import permutations
import json
import sympy as s

HERE=Path(__file__).resolve().parent
PINS={
 'late_sources/attachment_B.txt':'9aaf5e18cbc6a84d610b88429872df9b69e6078365bfdc8133c8f17e2c1c3801',
 'late_sources/field_dictionary.py':'a581bacd17c08dd9a766ae439bfe1e8e35e6d30b9509cb9d98053b897d8ecc13'}
checks=[]
def need(ok,name):
 if not bool(ok):raise RuntimeError(name)
 checks.append(name)
def eq(a,b,name):
 d=a-b
 need(all(s.simplify(x)==0 for x in d) if isinstance(d,s.MatrixBase) else s.simplify(d)==0,name)
def comm(a,b):return a*b-b*a
def commutant_dim(generators):
 n=generators[0].rows
 rows=s.Matrix.vstack(*[s.kronecker_product(s.eye(n),a)-s.kronecker_product(a.T,s.eye(n)) for a in generators])
 return n*n-rows.rank()
def matrix_json(a):return [[str(v) for v in row] for row in a.tolist()]

def main():
 for name,digest in PINS.items():need(sha256((HERE/name).read_bytes()).hexdigest()==digest,'frozen pin '+name)
 # Native supplied six-coordinate convention, independently reconstructed.
 pairs=[(0,0),(0,1),(1,1)]
 embed=s.zeros(8,6)
 for col,(pair,gamma) in enumerate((p,g) for p in pairs for g in range(2)):
  for a,b in set((pair,pair[::-1])):embed[4*a+2*b+gamma,col]=1
 metric=embed.T*embed
 eq(metric,s.diag(1,1,2,2,1,1),'actual nonorthonormal symmetric-pair metric')
 sym=s.zeros(8)
 for perm in permutations(range(3)):
  for old in range(8):
   bits=[(old>>2)&1,(old>>1)&1,old&1]
   new=sum(bits[perm[k]]<<(2-k) for k in range(3))
   sym[new,old]+=s.Rational(1,6)
 p32=metric.inv()*embed.T*sym*embed;p12=s.eye(6)-p32
 C=s.Matrix([[0,1,-1,0,0,0],[0,0,0,1,-1,0]])
 R=s.Rational(2,3)*metric.inv()*C.T
 eq(C*R,s.eye(2),'epsilon contraction has exact normalized right inverse')
 eq(R*C,p12,'independent epsilon projector matches supplied full symmetrizer')
 eq(p12*p12,p12,'spin one-half projector idempotent')
 eq(p32*p32,p32,'spin three-half projector idempotent')
 eq(p12*p32,s.zeros(6),'complementary projector images')
 eq(p12.T*metric,metric*p12,'projector self-adjoint in correct metric')
 need(p12.T!=p12,'unnormalized-coordinate projector is not Euclidean Hermitian')
 need(p12.rank()==2 and p32.rank()==4,'exact projector ranks two and four')
 eq(C*p32,s.zeros(2,6),'contraction annihilates spin three-half')
 eq(C*p12,C,'contraction retains complete spin one-half')
 # Fundamental sl2 and its actual symmetric square in the same coordinates.
 E=s.Matrix([[0,1],[0,0]]);F=E.T;H=s.diag(1,-1)
 E1=s.Matrix([[0,2,0],[0,0,1],[0,0,0]])
 F1=s.Matrix([[0,0,0],[1,0,0],[0,2,0]]);H1=s.diag(2,0,-2)
 same=[];opposite=[]
 for tag,a,b in zip(('E','F','H'),(E1,F1,H1),(E,F,H)):
  total=s.kronecker_product(a,s.eye(2))+s.kronecker_product(s.eye(3),b)
  difference=s.kronecker_product(a,s.eye(2))-s.kronecker_product(s.eye(3),b)
  same.append(total);opposite.append(difference)
  eq(comm(p12,total),s.zeros(6),'same-handed full sl2 covariance '+tag)
  eq(C*total,b*C,'epsilon extraction intertwines spinor '+tag)
  eq(total*R,R*b,'epsilon insertion intertwines spinor '+tag)
 need(commutant_dim(same)==2,'same-handed module has two irreducible summands')
 # Mixed handed module is sl2_L x sl2_R, not the diagonal sl2 alone.
 need(commutant_dim(same+opposite)==1,'mixed-handed full Lorentz module commutant scalar')
 Jz=same[2]/2;Kz=opposite[2]/2
 boost=comm(p12,Kz)
 eq(comm(p12,Jz),s.zeros(6),'rotational z projector covariance')
 need(boost.rank()==4,'mixed-handed boost breaks rotational spin projector with rank-four commutator')
 expected=s.zeros(6);expected[1,2]=s.Rational(4,3);expected[2,1]=-s.Rational(2,3)
 expected[3,4]=s.Rational(2,3);expected[4,3]=-s.Rational(4,3)
 eq(boost,expected,'explicit exact mixed-handed boost witness')
 # Dimension fraction is not a state-independent probability.
 v0=s.eye(6)[:,0];v1=R[:,0]
 weights=[]
 for v in (v0,v1):weights.append(s.factor((v.T*metric*p12*v)[0]/(v.T*metric*v)[0]))
 need(weights==[0,1],'positive pure vectors realize spin-half weights zero and one')
 eq(s.trace(p12)/6,s.Rational(1,3),'one-third is only the isotropic dimension fraction')
 # Exact counterexample to scalar commutant implying arbitrary unitary control.
 Jx=s.Matrix([[0,1,0],[1,0,1],[0,1,0]])/s.sqrt(2)
 Jy=s.Matrix([[0,-s.I,0],[s.I,0,-s.I],[0,s.I,0]])/s.sqrt(2)
 Jz3=s.diag(1,0,-1)
 for a,b,c in ((Jx,Jy,Jz3),(Jy,Jz3,Jx),(Jz3,Jx,Jy)):eq(comm(a,b),s.I*c,'spin-one su2 Lie closure '+str(len(checks)))
 need(commutant_dim([Jx,Jz3])==1,'spin-one controls have scalar commutant')
 need(s.Matrix.hstack(*[m.reshape(9,1) for m in (Jx,Jy,Jz3)]).rank()==3,'spin-one dynamical Lie dimension three not su3 dimension eight')
 # Necessary center rule does not eliminate lower degenerate nonsinglets.
 blockH=s.diag(0,-1,-1,-1,-1)
 center=s.diag(1,s.I,s.I,s.I,s.I)
 eq(comm(blockH,center),s.zeros(5),'invariant singlet-plus-fundamental countermodel')
 need(blockH.eigenvals()=={s.Integer(0):1,s.Integer(-1):4},'nonsinglet multiplet can lie below a singlet')
 out={'status':'PASS','exact_checks':len(checks),'checks':checks,'pins':PINS,
      'metric':matrix_json(metric),'epsilon_contraction_C':matrix_json(C),'insertion_R':matrix_json(R),
      'spin_half_projector':matrix_json(p12),'opposite_hand_boost_commutator':matrix_json(boost),
      'same_handed':{'module':'(1,0) tensor (1/2,0) = (3/2,0) plus (1/2,0)','commutant_dimension':2,'projector_ranks':[4,2]},
      'opposite_handed':{'module':'(1,0) tensor (0,1/2) = (1,1/2)','complex_dimension':6,'commutant_dimension':1,'rotation_projector_is_boost_invariant':False,'boost_commutator_rank':4},
      'scalar_commutant_control_counterexample':{'Hilbert_dimension':3,'commutant_dimension':1,'dynamic_Lie_dimension':3,'su3_dimension':8},
      'scope':{'literal_adjoint_field_flips_chirality':True,'native_creation_mode_has_Lorentz_type_from_dagger_alone':False,
               'independent_or_charge_conjugated_same_hand_dictionary_excluded':False,'native_field_adapter_derived':False,
               'same_hand_spin_half_fraction_for_native_state_derived':False,'Lorentz_covariant_particle_pole_derived':False}}
 print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
