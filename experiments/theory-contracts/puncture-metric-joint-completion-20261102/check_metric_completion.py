"""Whole-cone conditional metric selection for the original D5+A3 glue.

No physical source, square selection, or spacetime reconstruction is claimed.
The original W(D5) and square C4 actions, additive charge lattice,
specified index-four extension and integral-unimodular closure are hypotheses.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
checks=[]
def need(value,label):
    if not value: raise RuntimeError(label)
    checks.append(label)

I=s.eye(4); one=s.ones(4,1); P=I-one*one.T/4
v=s.Matrix([1,-1,1,-1])/2
R=s.zeros(4); S=s.zeros(4)
for j in range(4):
    R[(j+1)%4,j]=1
    S[(-j)%4,j]=1
B=s.Matrix.hstack(I[:,0]-I[:,1],I[:,1]-I[:,2],I[:,2]-I[:,3])
need(B.T*B==s.Matrix([[2,-1,0],[-1,2,-1],[0,-1,2]]),'actual puncture differences give A3 root Gram')
need((B.T*B).det()==4,'root determinant four')
M=P[:,:3]
need((M.T*M).det()==s.Rational(1,4),'meridian weight determinant one quarter')
need(P*one==s.zeros(4,1),'meridian relation is retained')
need((P-I).rank()==1,'four by four identity does not descend to puncture quotient')
need(sum((P[:,j] for j in range(4)),s.zeros(4,1))==s.zeros(4,1),'all four meridian weights sum to zero')
need(all(P[:,j]-P[:,0]==I[:,j]-I[:,0] for j in range(4)),'all marks have the same discriminant class')

x,a,b=s.symbols('x a b',positive=True)
Q=a*(P-v*v.T)+b*v*v.T
need(s.simplify(Q*R-R*Q)==s.zeros(4) and s.simplify(Q*S-S*Q)==s.zeros(4),'whole proposed metric cone has the actual D4 action')
# All symmetric quotient forms: solve before restricting to the proposed cone.
xs=s.symbols('x:10'); Z=s.zeros(4); k=0
for i in range(4):
    for j in range(i,4): Z[i,j]=Z[j,i]=xs[k]; k+=1
equations=list(Z*one)+list(Z*R-R*Z)+list(Z*S-S*Z)
linear,_=s.linear_eq_to_matrix(equations,xs)
need(10-linear.rank()==2,'D4 invariant positive quotient metrics have exactly two parameters')
quarter_linear,_=s.linear_eq_to_matrix(list(Z*one)+list(Z*R-R*Z),xs)
need(10-quarter_linear.rank()==2,'reflection is unnecessary: square C4 already gives this whole symmetric cone')
need((P-v*v.T).rank()==2 and (v*v.T).rank()==1,'two metric coefficients act on ranks two and one')
G=s.simplify(B.T*Q*B)
need(s.factor(G.det())==4*a*a*b,'entire root metric determinant is four a squared b')
r_opposite=I[:,0]-I[:,2]; r_adjacent=I[:,0]-I[:,1]
need(s.expand((r_opposite.T*Q*r_opposite)[0])==2*a,'opposite root norm is two a')
need(s.expand((r_adjacent.T*Q*r_adjacent)[0])==a+b,'adjacent root norm is a plus b')
need(G[0,1]==-b and G[0,0]==a+b,'integrality of the root pairing forces both a and b integral')
weyl=[]
for i in range(4):
    w=s.eye(5); w.row_swap(i,i+1); weyl.append(w)
weyl.append(s.diag(-1,-1,1,1,1))
yx=s.symbols('y:15'); A=s.zeros(5); k=0
for i in range(5):
    for j in range(i,5): A[i,j]=A[j,i]=yx[k]; k+=1
L,_=s.linear_eq_to_matrix([e for w in weyl for e in list(A*w-w*A)],yx)
need(15-L.rank()==1,'whole W(D5) invariant symmetric carrier metric has exactly one scale')
no_fixed=s.Matrix.vstack(*(w-s.eye(5) for w in weyl))
need(no_fixed.rank()==5,'W(D5) invariance forces every mixed carrier-family metric block to zero')
d0=s.Matrix([1,-1,0,0,0]); d1=s.Matrix([0,1,-1,0,0])
need((d0.T*(x*s.eye(5))*d1)[0]==-x,'D5 root pairing integrality forces carrier scale x integral')
need(s.factor((4*x**5)*G.det()/16)==x**5*a*a*b,'whole glued metric determinant is x to five times a squared b')
need(s.simplify(G.subs({a:1,b:1})-B.T*B)==s.zeros(3),'unique candidate recovers original root metric')
# Analytic whole-cone proof, no bounded parameter search:
# Integrality implies x,a,b are positive integers. Unimodularity gives
# x^5 a^2 b=1. Thus x=a=b=1. Evenness is a conclusion after the explicit
# identification below, not a premise of metric uniqueness.
m0=P[:,0]; spin=s.ones(5,1)/2
need((m0.T*m0)[0]==s.Rational(3,4) and (spin.T*spin)[0]==s.Rational(5,4),'original complementary norms are recovered')
O=s.Matrix([[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])/2
need(O.T*O==P and O*O.T==s.eye(3),'explicit family map is an isometry of sum zero')
need(O*m0==s.ones(3,1)/2,'actual puncture maps to original D3 spinor weight')
need(abs((O*B).det())==2,'family root lattice maps onto integral even-sum D3')
need(all(sum((O*B)[:,j])%2==0 for j in range(3)),'transformed family basis has even integer coordinate sum')
need(sum(2*spin)%2==1 and sum(2*O*m0)%2==1,'twice glue joins odd-odd block coset into D8')
need((spin.T*spin)[0]+(m0.T*m0)[0]==2,'original diagonal generator has even root norm')
need(all((B.T*m0)[j].is_integer for j in range(3)),'family glue has integral pairing with every root generator')
need(all(all(z.is_integer for z in w*spin-spin) and sum(w*spin-spin)%2==0 for w in weyl),'actual W(D5) generators preserve original spinor discriminant class')
need(R*m0-m0==I[:,1]-I[:,0],'actual quarter action preserves original meridian discriminant class')

out={
 'status':'PASS_EXACT_CONDITIONAL_WHOLE_CONE',
 'checks':len(checks), 'check_names':checks,
 'metric_cone':'carrier x I5 plus Q=a(P-vv^T)+b vv^T, x,a,b>0; P=I-J/4; v=(1,-1,1,-1)/2; cross block vanishes by W(D5)',
 'root_gram':[[str(x) for x in G.row(i)] for i in range(3)],
 'glued_lattice_determinant':'x^5 a^2 b',
 'whole_cone_proof':'Integral root pairings imply x,a,b are positive integers. Unimodularity implies x^5 a^2 b=1. Thus x=a=b=1. Explicit lattice identification then gives evenness.',
 'sufficient_lattice_identification':'O(A3)=D3, O(m0)=(1/2)^3. Adding 2 lambda joins D5+D3 to D8. Adding lambda gives D8 union (D8+(1/2)^8), the explicit standard E8 lattice.',
 'first_extra_premises':['given W(D5) carrier action and square C4 mark action','fixed additive D5 plus puncture difference lattice','original diagonal spinor-meridian index four extension','invariant positive real symmetric metric','integral and unimodular joint lattice'],
 'not_derived':['four marks or square arrangement','carrier D5 and choice of spinor-meridian extension','physical justification of integral unimodular closure','P1 source or state','physical clock and locality','3+1 spacetime or complete TFPT'],
 'original_sources':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [
   'documents/tfpt_1_architecture_e8/sections/011-source.tex',
   'verification/v983_simple_current_generator.py']},
 'scope':'Reconstruction of the family metric from explicitly supplied joint completion requirements; no use of the conclusion E8 as an independent origin premise.'
}
dest=Path(__file__).with_name('metric_completion_results.json')
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,sort_keys=True))
