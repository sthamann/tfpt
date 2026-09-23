"""Independent exact audit of definitions, kernel boundary, marked current."""
import json
from pathlib import Path
import sympy as s

checks=[]
def ck(name,value):
    assert bool(value),name
    checks.append({'name':name,'pass':True})
def norm2(v):return s.simplify((v.H*v)[0])
q=4;I=s.eye(q);m=s.zeros(q,q*q);eta=s.eye(q)[:,0]
for a in range(q):
    for b in range(q):m[(a+b)%q,a*q+b]=1
u=s.kronecker_product(eta,eta);v=m.H*eta
ck('Native specialness',m*m.H==4*I)
ck('Native unit',m*s.kronecker_product(eta,I)==I)
ck('Cap norm four',norm2(v)==4)
ck('Cap marked unit amplitude one',(u.H*v)[0]==1)
ck('Cap orthogonal complement norm three',norm2(v-u)==3)
ck('m adjoint over two is isometry',(m.H/2).H*(m.H/2)==I)
ck('m over two is coisometry',(m/2)*(m/2).H==I)
ck('m over two is not isometry on tensor domain',(m/2).H*(m/2)!=s.eye(16))
L=s.zeros(4)
for a in range(4):L[(a+1)%4,a]=1
S=s.kronecker_product(L,L.H)
R=s.diag(1,s.I,-1,-s.I);grade=s.kronecker_product(R,R)
swap=s.zeros(16)
for a in range(4):
    for b in range(4):swap[b*4+a,a*4+b]=1
w=s.zeros(16,1)
for a in range(4):w[a*4+(-a)%4]=(-1)**a
ck('Both currents total Z4 neutral',grade*v==v and grade*w==w)
ck('Both currents swap invariant',swap*v==v and swap*w==w)
ck('Alternative norm and unit marker preserved',norm2(w)==4 and (u.H*w)[0]==1)
ck('Native cap balanced',S*v==v)
ck('Alternative current anti-balanced',S*w==-w)
ck('Marked cap balance distinguishes exact responses',norm2(S*w-w)==16)
Y=(S+S.H)/2
ck('Hermitian process reader distinguishes plus/minus one',
   (v.H*Y*v)[0]/4==1 and (w.H*Y*w)[0]/4==-1)
neutral=s.zeros(16,4)
for a in range(4):neutral[a*4+(-a)%4,a]=1
ck('Balanced neutral subspace is one-dimensional',4-((S-s.eye(16))*neutral).rank()==1)
a=s.Rational(1,12);A=s.Matrix([[0,a],[a,0]]);id2=s.eye(2)
Cl=s.kronecker_product(u,A/2)
W=Cl.row_join(s.kronecker_product(v,id2))
Walt=Cl.row_join(s.kronecker_product(w,id2))
h=s.diag(A,s.zeros(2))+W.H*W
target=(A+A*A/4).row_join(A/2).col_join((A/2).row_join(4*id2))
ck('Cap gives full declared parent',h==target)
ck('Changed marked current gives exactly same full parent',Walt.H*Walt==W.H*W)
wrong=Cl.row_join(s.kronecker_product(v/2,id2))
ck('Normalized cap changes HH to one', (wrong.H*wrong)[2:4,2:4]==id2)
ck('Normalized cap changes cross normalization', (wrong.H*wrong)[0:2,2:4]==A/4)
v13=2*v-u
W13=Cl.row_join(s.kronecker_product(v13,id2))
ck('Earlier HH13 mutant independently reproduced',
   W13.H*W13-W.H*W==s.diag(s.zeros(2),9*id2))

cycle=s.Matrix([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
Ac=a*cycle;P=cycle*cycle/4;D=3*I+2*P
B=(Ac*Ac/4).row_join(Ac/2).col_join((Ac/2).row_join(D-3*I))
Wc=(Ac/2).row_join(P)
ck('Singular test uses orthogonal range projection',P*P==P and P.H==P and P*Ac==Ac and P.rank()==2)
ck('Singular case exactly factors at generalized bound',B==Wc.H*Wc+s.diag(s.zeros(4),P))
ck('All local HH budgets still four with singular A',all(D[i,i]==4 for i in range(4)))
ck('Singular A defeats unsafeguarded D>=4I',min((D-4*I).eigenvals())==-1)
ck('Singular fixed ring remains within norm bound',max(abs(x) for x in Ac.eigenvals())==s.Rational(1,6))

beta,et=s.symbols('beta et',positive=True)
M=4*et**2/beta
ck('Cap scales obey relation M beta=4 eta squared',s.simplify(M*beta-4*et**2)==0)
ck('Native scaling reproduces M4',M.subs({beta:s.Rational(1,4),et:s.Rational(1,2)})==4)
ck('Full hopping coefficient relation',4*s.Rational(1,576)==4*s.Rational(1,24)**2)
dimensions=[4+2*s.cos(s.pi*c/2) for c in range(4)]
ck('Native second rung unequal sector dimensions',dimensions==[6,4,2,4])
result={'status':'PASS','count':len(checks),'checks':checks,
  'singular_example':{'A':str(Ac),'D':str(D),'eigen_D_minus_4':str((D-4*I).eigenvals())},
  'same_parent_different_current':{'native_coefficients':[1,1,1,1],
    'alternative_coefficients':[1,-1,1,-1],
    'unit_amplitude':1,'norm_squared':4,'balanced_reader_responses':[1,-1]},
  'scope':'Exact finite review and own countermodels. No primitive-to-physical CAR/rotor intertwiner, no new physics prediction, no native suite run.'}
Path(__file__).with_name('cap-review-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','count':len(checks)}))
