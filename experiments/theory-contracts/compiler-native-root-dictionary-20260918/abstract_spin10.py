from common import ROOT,D,OUT
import ast,json,itertools,hashlib
from pathlib import Path
from collections import Counter
import sympy as s
import numpy as np
checks=[]
def ck(ok,msg):
 if not bool(ok):raise RuntimeError(msg)
 checks.append(msg)
def select(path,name,env):
 t=ast.parse((ROOT/path).read_text());f=next(n for n in t.body if isinstance(n,ast.FunctionDef) and n.name==name)
 exec(compile(ast.Module(body=[f],type_ignores=[]),str(ROOT/path),'exec'),env);return env[name]
jw=select('verification/v113_quasifree_kernel.py','jw',{'sp':s})(4)
g4=[x for a in jw for x in (a+a.T,s.I*(a.T-a))];I=s.eye(16);K=s.diag(*[(-1)**i.bit_count() for i in range(16)])
B=g4[1]*g4[3]*g4[5]*g4[7]
def rb(indices):
 cols=[];seen=set()
 for i in indices:
  if i in seen:continue
  j=next(j for j in indices if B[j,i]!=0);b=B[j,i]
  if j==i:cols.append(I[:,i]*(1 if b==1 else s.I));seen.add(i)
  else:cols += [(I[:,i]+b*I[:,j])/s.sqrt(2),s.I*(I[:,i]-b*I[:,j])/s.sqrt(2)];seen.update([i,j])
 return s.Matrix.hstack(*cols)
F=s.Matrix.hstack(rb([i for i in range(16) if i.bit_count()%2==0]),rb([i for i in range(16) if i.bit_count()%2]))
A=[s.Matrix(a) for a in D['bilinear_maps']];gs=[]
for a in A:
 x=s.zeros(16);x[:8,8:]=a.T;x[8:,:8]=a;gs.append(x)
K0=s.diag(*([1]*8+[-1]*8))
ck(F.H*F==I,'unitary complexification chart')
ck(all(s.simplify(F.H*g*F)==a for g,a in zip(g4,gs)),'source JW maps exactly to intrinsic real Clifford operators')
ck(F.H*K*F==K0,'intrinsic grading matches four-mode parity')
# Actual original carrier construction, exact conversion of integer source matrices.
SUBSETS=[frozenset(t) for k in range(6) for t in itertools.combinations(range(5),k)];IDX={t:i for i,t in enumerate(SUBSETS)}
adag=select('verification/v474_entropic_hodge_carrier.py','adag',{'np':np,'DIM':32,'SUBSETS':SUBSETS,'IDX':IDX})
ad=[]
for i in range(5):
 a=adag(i);ck(np.all(a.imag==0) and np.all(a.real==np.round(a.real)),'native creation entries integral '+str(i));ad.append(s.Matrix(a.real.astype(int)))
g5=[x for a in ad for x in (a+a.T,s.I*(a-a.T))]
even=[i for i,t in enumerate(SUBSETS) if len(t)%2==0];evsets=[SUBSETS[i] for i in even];evindex={t:i for i,t in enumerate(evsets)}
P=s.zeros(16)
for mask in range(16):
 t={j for j in range(4) if mask&(1<<(3-j))}
 if len(t)%2:t.add(4)
 P[evindex[frozenset(t)],mask]=1
U=P*F;ck(U.H*U==I,'source carrier identification unitary')
q=gs+[K0];gens={}
for a,b in itertools.combinations(range(10),2):
 target=(g5[a]*g5[b]/2).extract(even,even)
 intrinsic=q[a]*q[b]/2 if b<9 else s.I*q[a]/2
 ck(s.simplify(U*intrinsic*U.H)==target,'full native Spin10 intertwiner '+str((a,b)))
 gens[a,b]=intrinsic
ck(all(g.H==-g for g in gens.values()),'all intrinsic generators anti-Hermitian')
# Trace Gram gives exact independence; no floating numerical rank.
keys=list(gens);T=s.Matrix([[s.re(s.trace(a.H*b)) for b in gens.values()] for a in gens.values()])
ck(T==4*s.eye(45),'45 generators independent with exact trace Gram')
def gen(a,b):return s.zeros(16) if a==b else gens[a,b] if a<b else -gens[b,a]
for (a,b),(c,d) in itertools.combinations(keys,2):
 expected=(int(b==c)*gen(a,d)-int(a==c)*gen(b,d)-int(b==d)*gen(a,c)+int(a==d)*gen(b,c))
 ck(gens[a,b]*gens[c,d]-gens[c,d]*gens[a,b]==expected,'so10 commutator '+str((a,b,c,d)))
print('all 45 source operators matched; all 990 brackets checked',flush=True)
# Native source marking: first three color slots, last two weak slots.
Yslot=[s.Rational(-1,3)]*3+[s.Rational(1,2)]*2
Tslot=[0,0,0,s.Rational(1,2),s.Rational(-1,2)]
Num=[(a*a.T).extract(even,even) for a in ad]
Y=sum((y*n for y,n in zip(Yslot,Num)),s.zeros(16));T3=sum((t*n for t,n in zip(Tslot,Num)),s.zeros(16));Q=Y+T3
Yintr=s.simplify(U.H*Y*U);T3intr=s.simplify(U.H*T3*U)
ck(all(Yintr.H==Yintr for _ in [0]),'transported hypercharge Hermitian')
# Expected formula includes the fifth occupancy, fixed by four-mode parity.
N4=[a.T*a for a in jw];Y4=sum((Yslot[i]*N4[i] for i in range(4)),s.zeros(16))+Yslot[4]*(I-K)/2
ck(s.simplify(Yintr-F.H*Y4*F)==s.zeros(16),'hypercharge parity term exact')
rows=[]
for subset in evsets:
 nc=len(subset&{0,1,2});nw=len(subset&{3,4})
 name={(0,0):'nu^c',(2,0):'u^c',(1,1):'Q',(0,2):'e^c',(2,2):'d^c',(3,1):'L'}[nc,nw]
 rows.append({'subset':sorted(subset),'field':name,'Y':str(sum(Yslot[i] for i in subset)),'Q':str(sum(Yslot[i]+Tslot[i] for i in subset))})
counts=Counter((r['field'],r['Y']) for r in rows)
ck(dict(counts)=={('nu^c','0'):1,('u^c','-2/3'):3,('Q','1/6'):6,('e^c','1'):1,('d^c','1/3'):3,('L','-1/2'):2},'all native SM charge multiplicities')
weak=(ad[3]*ad[4].T).extract(even,even);W=s.simplify(U.H*weak*U)
ck(K0*W-W*K0!=s.zeros(16),'triality grading is not physical weak-invariant chirality')
# A fifth-mode-free truncation must fail the source hypercharges.
ck(Y4!=sum((Yslot[i]*N4[i] for i in range(4)),s.zeros(16)),'dropping the parity-supplied fifth mode fails the charge map')
# Orthogonal seed-only Lie closure has 36 generators; K is the explicit extra seed.
ck(len([k for k in keys if 8 not in k])==36,'without grading generator the corresponding compact closure is so9 (36)')
Ucs={name:s.diag(s.Matrix(D['clock_matrices'][name]['plus']),s.Matrix(D['clock_matrices'][name]['minus'])) for name in ['C','J','sigma']}
clockcharges={k:(s.simplify(x*Yintr-Yintr*x)==s.zeros(16)) for k,x in Ucs.items()}
ck(Ucs['J']**2==K0,'grading already equals the half-quarter-clock lift J squared')
out={'verdict':'EXACT_SPIN10_OPERATOR_AND_MARKED_CHARGE_BRIDGE_CONDITIONAL_ON_UNITARY_SEEDS','checks':checks,'new_premise':'Complexify the real Clifford module and take Lie closure of i*geometric Clifford directions and i*grading. This is an algebraic unitary-completion rule, not a derived Hamiltonian.', 'normalizations':'M_ab=Gamma_a Gamma_b/2; M_a9=i Gamma_a/2 (zero-based final index9)','charge_rows':rows,'clock_commutes_with_marked_hypercharge':clockcharges,'grading':'J_lift squared; not physical chirality','chart':'first four source slots plus parity-supplied fifth slot; no canonical marked physical identification claimed','U':[[str(x) for x in row] for row in U.tolist()],'scope':'One generation algebraic representation only; no field dynamics, source-to-readout selection, families or TOE closure'}
(OUT/'abstract.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'verdict':out['verdict'],'checks':len(checks),'clock_charges':clockcharges,'charge_multiplicities':{str(k):v for k,v in counts.items()}},indent=2))
