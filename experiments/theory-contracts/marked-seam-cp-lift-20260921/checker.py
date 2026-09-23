#!/usr/bin/env python3
"""Conditional marked transfer lift, actual source words and exact readout.

No primitive physical field, environment or continuous clock is inferred.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sympy as s

ROOT = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
PINS = {
 'verification/v774_arf_spinor_compiler.py': '3ef92c17d9f0de62212bab940ac2c017be866645d8a5b276bdcf2d92128bae8c',
 'verification/v814_k5_sixstep_transport.py': '6d457a4e1d3192fe95a10bcb03159c4ea7fe21c3fbe64e2c4dc50b6e6a85af53',
 'verification/v221_seam_qecc.py': '4bb7156fd414a388f64979d0df66ab139aca04291a33bf9de0cc6ed663d30fac',
 'experiments/theory-contracts/compiler-clifford-bridge/checker.py': 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d',
 'experiments/theory-contracts/compiler-kernel-foundation-20260914/redteam/two_rate.py': '8994878db800a73ae0da48dd725d6509026bed3744d0a12e0eb022d6df3db337',
}
CHECKS=[]
def need(ok, label):
 if not bool(ok): raise RuntimeError(label)
 CHECKS.append(label)
def clean(x): return s.simplify(x)
def load(name, path):
 spec=importlib.util.spec_from_file_location(name,path)
 mod=importlib.util.module_from_spec(spec)
 spec.loader.exec_module(mod)
 return mod
def vec(m): return s.Matrix([m[i,j]/2 for j in range(4) for i in range(4)])
def ad(m): return s.kronecker_product(m.conjugate(),m)
def weights(a,b): return [(1+5*a+10*b)/16,(1-3*a+2*b)/16,(1+a-2*b)/16]
def encode(m): return [[str(x) for x in row] for row in m.tolist()]

def main(root, mutant=None):
 for rel,digest in PINS.items():
  need(hashlib.sha256((root/rel).read_bytes()).hexdigest()==digest, 'pinned '+rel)
 bridge=load('source_clifford_bridge',root/'experiments/theory-contracts/compiler-clifford-bridge/checker.py')
 src,_=bridge.inherited(root)
 finite=bridge.finite_data(src)
 native=load('source_sixstep',root/'verification/v814_k5_sixstep_transport.py')
 q=finite['q']; zero=(0,0,0,0); I=s.eye(4); Z=s.zeros(4)
 words={v:bridge.monomial(v,bridge.generators()) for v in src.W16}
 o5=[v for v in src.W16 if v!=zero and q[v]==0]
 o10=[v for v in src.W16 if q[v]==1]
 need((len(o5),len(o10))==(5,10),'native marked orbit sizes')
 cols=s.Matrix.hstack(*[vec(words[v]) for v in src.W16])
 need(cols.H*cols==s.eye(16),'actual signed word orthonormality')
 P0=vec(I)*vec(I).H
 P5=sum((vec(words[v])*vec(words[v]).H for v in o5),s.zeros(16))
 P10=sum((vec(words[v])*vec(words[v]).H for v in o10),s.zeros(16))
 need(P0+P5+P10==s.eye(16),'complete operator decomposition')
 a,b=s.symbols('a b',real=True)
 E=P0+a*P5+b*P10
 choi=s.Matrix(16,16,lambda r,c:E[(r%4)+4*(c%4),(r//4)+4*(c//4)]/4)
 w=weights(a,b)
 for v in src.W16:
  index=0 if v==zero else 1 if v in o5 else 2
  need(s.expand(choi*vec(words[v])-w[index]*vec(words[v]))==s.zeros(16,1),'symbolic Choi weight '+str(v))
 good=weights(s.Rational(1,3),s.Rational(2,3))
 bad=weights(s.Rational(2,3),s.Rational(1,3))
 need(good==[s.Rational(7,12),s.Rational(1,12),s.Integer(0)],'unique positive assignment in specified class')
 need(bad[1]==-s.Rational(1,48),'reverse assignment negative Choi witness')
 if mutant=='reverse_is_cp': need(bad[1]>=0,'mutant reverse assignment is CP')
 Phi=P0+P5/3+2*P10/3
 need(Phi==s.Rational(7,12)*s.eye(16)+sum((ad(words[v]) for v in o5),s.zeros(16))/12,'native Kraus mixture equals spectral lift')
 five=[next(v for v in o5 if src.iota(v)[j]==0) for j in range(5)]
 for j in range(4):
  lift=(words[five[j]]+words[five[j+1]])/s.sqrt(2)
  need(clean(ad(lift)*Phi-Phi*ad(lift))==s.zeros(16),'signed marked S5 covariance '+str(j))
 need(Phi**6==P0+P5/729+s.Rational(64,729)*P10,'six native steps')
 for aa,bb in [(s.Rational(64,729),s.Rational(1,729)),(s.Rational(1,729),s.Rational(64,729))]:
  need(all(x>0 for x in weights(aa,bb)),'both macro assignments CP, macro data do not select')
 half=weights(1/s.sqrt(3),s.sqrt(s.Rational(2,3)))
 need(half[2]<0,'forced marked square root is not CP')
 if mutant=='continuous_is_cp': need(half[2]>=0,'mutant continuous marked interpolation CP')
 def phi(m): return clean(s.Rational(7,12)*m+sum((words[v]*m*words[v].H for v in o5),Z)/12)
 # Only the original anchor/family-sum words are used as readout directions.
 A=s.I*words[src.A_BIT]; F=words[src.FSIG]
 need(q[src.A_BIT]==1 and q[src.FSIG]==0 and src.hb(src.A_BIT,src.FSIG)==1,'original marked fixed-plane labels')
 need(A.H==A and F.H==F and A*A==I and F*F==I and A*F==-F*A,'original A,F Hermitian anticommuting units')
 need(phi(A)==2*A/3 and phi(F)==F/3,'actual operator mode assignment')
 effects=[(I+s.sqrt(3)*A/2+F/2)/3,(I-s.sqrt(3)*A/2+F/2)/3,(I-F)/3]
 need(clean(sum(effects,Z))==I,'readout effects sum to identity')
 for i,e in enumerate(effects):
  need(e.H==e and clean(e*e-2*e/3)==Z and s.trace(e)==s.Rational(4,3),'positive rank-two effect '+str(i))
 B=s.Matrix(native.B); T=s.Matrix(native.T_V221)
 need(B==s.Matrix([[13,1,4],[1,13,4],[4,4,10]])/18 and B**6==T,'original v814 B and v221 T, entrywise')
 for i in range(3):
  need(clean(phi(effects[i])-sum((B[i,j]*effects[j] for j in range(3)),Z))==Z,'exact original one-step readout intertwiner '+str(i))
  e=effects[i]
  for _ in range(6): e=phi(e)
  need(clean(e-sum((T[i,j]*effects[j] for j in range(3)),Z))==Z,'exact original six-step readout intertwiner '+str(i))
 need(effects[0]**2!=effects[0],'readout is not multiplicative event embedding')
 J=s.ones(3)/3
 u2=s.Matrix([1,-1,0]);u3=s.Matrix([1,1,-2])
 C2=u2*u2.T/2;C3=u3*u3.T/6
 effect_gram=s.Matrix(3,3,lambda i,j:s.trace(effects[i]*effects[j])/4)
 need(effect_gram==J/3+(C2+C3)/6,'actual joint readout Gram')
 xx,yy=s.symbols('xx yy',real=True)
 effect_steps=[(I+yy*s.sqrt(3)*A/2+xx*F/2)/3,(I-yy*s.sqrt(3)*A/2+xx*F/2)/3,(I-xx*F)/3]
 effect_correlation=s.Matrix(3,3,lambda i,j:clean(s.trace(effects[i]*effect_steps[j])/4))
 need(clean(effect_correlation-(J/3+yy*C2/6+xx*C3/6))==s.zeros(3),'all-discrete-time readout Gram response')
 gram_whitener=s.sqrt(3)*J+s.sqrt(6)*(C2+C3)
 need(clean(gram_whitener*effect_correlation*gram_whitener-(J+yy*C2+xx*C3))==s.zeros(3),'normalized response equals original B powers')
 if mutant=='readout_is_projection': need(effects[0]**2==effects[0],'mutant sharp event embedding')
 # Existing matrix algebra admits an algebraic CAR factor, not a local field.
 c=(F+s.I*A)/2; cd=c.H; N=cd*c
 need(c*c==Z and c*cd+cd*c==I and N*c-c*N==-c,'algebraic CAR and its declared charge')
 need(phi(c)==c/2-cd/6,'exact creation-annihilation mixing')
 need(clean(phi(c)**2)==-I/12,'reduced map is not a product homomorphism')
 need(clean(phi(N))==N/3+I/3,'number is not conserved by reduced step')
 # Equality in the random-unitary Schwarz inequality requires equality of
 # all conjugated copies; the identity Kraus term has positive weight.
 commutant_system=s.Matrix.vstack(*[ad(words[v])-s.eye(16) for v in o5])
 need(commutant_system.rank()==15,'common Kraus commutant consists only of scalars')
 need(commutant_system.nullspace()==[s.Matrix([1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])], 'multiplicative domain is scalar, independent of CAR choice')
 need(phi(I)==I and Phi.rank()==16 and (Phi-s.eye(16)).nullspace()==[s.Matrix([1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])], 'unique stationary trace state')
 x,y=s.symbols('x y',real=True)
 phi_n_c=(x*F+s.I*y*A)/2
 need(clean(s.trace(cd*phi_n_c)/4-(x+y)/4)==0,'formal trace transfer normal correlator')
 need(clean(s.trace(c*phi_n_c)/4-(x-y)/4)==0,'formal trace transfer anomalous correlator')
 if mutant=='charge_preserved': need(phi(N)==N,'mutant charge conservation')
 # Trine sharpness is a protocol choice: a two-parameter family also intertwines.
 u,v=s.symbols('u v',real=True)
 family=[(I+u*A+v*F)/3,(I-u*A+v*F)/3,(I-2*v*F)/3]
 for i,e in enumerate(family):
  need(clean(phi(e)-sum((B[i,j]*family[j] for j in range(3)),Z))==Z,'readout selection not unique '+str(i))
 result={
  'contract':'marked-seam-cp-lift-20260921','verdict':'PARTIAL',
  'conditional_mathematical_result':'EXACT_DISCRETE_CP_LIFT_AND_ORIGINAL_MATRIX_READOUT',
  'checks':CHECKS,'count':len(CHECKS),'source_pins':PINS,'upstream_bridge_pins':bridge.PINS,
  'conditional_premises':['unital marked Pauli-covariant orbit-scalar map on the existing M4 algebra','one positive identical primitive step with the seam survival values 1/3 and 2/3'],
  'one_step_per_word_weights':list(map(str,good)),
  'reverse_negative_choi':str(bad[1]),'square_root_negative_choi':str(half[2]),
  'B_original':encode(B),'T_original':encode(T),
  'readout_properties':{'effect_spectrum':['0','0','2/3','2/3'],'physical_selection_derived':False,'family':'u^2+v^2<=1, |2v|<=1; trine u=sqrt(3)/2,v=1/2 is chosen maximal equal sharpness'},
  'readout_gram':encode(effect_gram),'normalized_readout_response':'B^n for all integer n>=0; Phi^6 readout is original T',
  'original_operator_labels':{'A_BIT':list(src.A_BIT),'FSIG':list(src.FSIG)},
  'CAR_readout':{'phi_c':'c/2 - c_dagger/6','phi_c_squared':'-I/12','phi_N':'N/3+I/3','fixed_state':'I4/4','normal_transfer_correlation':'[(1/3)^n+(2/3)^n]/4','anomalous_transfer_correlation':'[(1/3)^n-(2/3)^n]/4'},
  'multiplicative_domain':{'commutant_constraint_rank':15,'dimension':1,'domain':'C I4','scope':'all operators of this selected finite channel; not all TFPT completions'},
  'not_derived':['raw P1 seam realization of this CP map','physical instrument and readout protocol','charged local field algebra, physical charge and common unitary time','process tensor or full multitime insertion functional','Gamma lattice/Vaux/RR bridge','complete TFPT or T1-T8'],
  'continuous_no_go_scope':'only the same marked orbit-scalar CPTP semigroup class',
  'physical_gates_closed':[],'T1_T8_closed':False}
 return result

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,default=ROOT)
 ap.add_argument('--out',type=Path,default=Path(__file__).with_name('certificate.json'))
 ap.add_argument('--mutant',choices=['reverse_is_cp','continuous_is_cp','readout_is_projection','charge_preserved'])
 args=ap.parse_args();result=main(args.repo,args.mutant)
 args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'verdict':result['verdict'],'count':result['count'],'weights':result['one_step_per_word_weights']}))
