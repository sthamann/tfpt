from common import ROOT,D,OUT
import ast,json,itertools,hashlib
from pathlib import Path
from fractions import Fraction as F
from collections import deque,Counter
import sympy as s
import numpy as np
R=s.Matrix(D['integral_triality']['vector_basis']);Ri=R.inv();checks=[]
def ck(ok,label):
 if not bool(ok):raise RuntimeError(label)
 checks.append(label)
class On(ast.NodeTransformer):
 def visit_Assert(self,n):return ast.copy_location(ast.Expr(ast.Call(ast.Name('ck',ast.Load()),[n.test,ast.Constant('original source assertion line '+str(n.lineno))],[])),n)
def select(path,name,env):
 t=ast.parse((ROOT/path).read_text());node=next(n for n in t.body if isinstance(n,(ast.ClassDef,ast.FunctionDef)) and n.name==name)
 env['ck']=ck;exec(compile(ast.fix_missing_locations(On().visit(ast.Module(body=[node],type_ignores=[]))),str(ROOT/path),'exec'),env);return env[name]
raw=select('verification/v1_e8_glue.py','e8_roots',{'np':np,'itertools':itertools})()
ck(all(float(2*x).is_integer() for v in raw for x in v),'dyadic source conversion is exact')
roots=[tuple(int(2*x) for x in v) for v in raw]
ck(all(s.Matrix(v).dot(s.Matrix(v))==8 for v in roots) and len(set(roots))==240,'all 240 exact doubled source roots')
coords={v:tuple(F(x) for x in Ri*s.Matrix(v)/2) for v in roots}
ck(all(x.denominator==1 for v in coords.values() for x in v),'all root basis coordinates integral')
class RS:
 n=8
 def __init__(self):self.roots=roots;self.simple=[tuple(int(x) for x in 2*R[:,i]) for i in range(8)]
 def alpha_coords(self,v):return coords[v]
Chevalley=select('verification/v498_celestial_wp5b_singular_vector.py','Chevalley',{'F':F,'ip':lambda a,b:sum(x*y for x,y in zip(a,b)),'vadd':lambda a,b:tuple(x+y for x,y in zip(a,b))})
lie=Chevalley(RS());ck(lie.sgn==-1,'source cocycle opposite-root convention')
# Direct source Chevalley-Serre relations on its full 248-dimensional adjoint.
def adroot(index):
 return s.SparseMatrix(248,248,{(i,j):s.Rational(v.numerator,v.denominator) for j in range(248) for i,v in lie.bracket(index,j).items()})
Es=[adroot(lie.ridx[v]) for v in lie.rs.simple];Fs=[-adroot(lie.ridx[tuple(-x for x in v)]) for v in lie.rs.simple];Hs=[adroot(240+i) for i in range(8)]
def comm(a,b):return a*b-b*a
zero=s.zeros(248);cartan=R.T*R
for i,j in itertools.product(range(8),repeat=2):
 ck(comm(Hs[i],Es[j])==cartan[i,j]*Es[j],'Cartan raising relation '+str((i,j)))
 ck(comm(Hs[i],Fs[j])==-cartan[i,j]*Fs[j],'Cartan lowering relation '+str((i,j)))
 ck(comm(Es[i],Fs[j])==(Hs[i] if i==j else zero),'raising lowering relation '+str((i,j)))
 if i!=j:
  ep=comm(Es[i],Es[j]);fp=comm(Fs[i],Fs[j])
  if cartan[i,j]==-1:ep=comm(Es[i],ep);fp=comm(Fs[i],fp)
  ck(ep==zero and fp==zero,'both Serre relations '+str((i,j)))
print('original E8 Chevalley-Serre action checked',flush=True)
# 8 complex slots = 16 Majorana directions. Reuse the source creation rule.
SUBSETS=[frozenset(t) for k in range(9) for t in itertools.combinations(range(8),k)];IDX={t:i for i,t in enumerate(SUBSETS)}
adag=select('verification/v474_entropic_hodge_carrier.py','adag',{'np':np,'DIM':256,'SUBSETS':SUBSETS,'IDX':IDX})
ads=[]
for k in range(8):
 A=adag(k);ck(np.all(A.imag==0) and np.all(np.isin(A.real,[-1,0,1])),'exact source creation entries '+str(k));rows,cols=np.nonzero(A);ads.append(s.SparseMatrix(256,256,{(int(i),int(j)):int(A[i,j].real) for i,j in zip(rows,cols)}))
Id=s.eye(256);z=s.zeros(256)
for i,j in itertools.product(range(8),repeat=2):
 ck(ads[i]*ads[j]+ads[j]*ads[i]==z and ads[i].T*ads[j]+ads[j]*ads[i].T==(Id if i==j else z),'native CAR '+str((i,j)))
even=[i for i,t in enumerate(SUBSETS) if len(t)%2==0];sets=[SUBSETS[i] for i in even];spinroots=[tuple(1 if k in t else -1 for k in range(8)) for t in sets]
ck(set(spinroots)=={v for v in roots if all(abs(x)==1 for x in v)},'native even-eight spinor weights are exactly all 128 E8 half-roots')
ix={v:i for i,v in enumerate(spinroots)}
def native_op(alpha):
 pos=[i for i,x in enumerate(alpha) if x==2];neg=[i for i,x in enumerate(alpha) if x==-2]
 if len(pos)==2:i,j=pos;B=ads[i]*ads[j]
 elif len(neg)==2:i,j=neg;B=ads[j].T*ads[i].T
 else:i=pos[0];j=neg[0];B=ads[i]*ads[j].T
 return B.extract(even,even)
def root_op(alpha):
 ai=lie.ridx[alpha];entries={}
 for j,b in enumerate(spinroots):
  for k,value in lie.bracket(ai,lie.ridx[b]).items():
   ck(k<240 and lie.roots[k] in ix,'D8 preserves the spinor root sector')
   entries[ix[lie.roots[k]],j]=s.Rational(value.numerator,value.denominator)
 return s.SparseMatrix(128,128,entries)
simple=[]
for i in range(7):a=[0]*8;a[i]=2;a[i+1]=-2;simple.append(tuple(a))
a=[0]*8;a[6]=a[7]=2;simple.append(tuple(a))
edges=[]
for a in simple:
 N=native_op(a);T=root_op(a)
 for (i,j),nv in N.todok().items():
  ck(T[i,j] in [-1,1],'source and native root supports match');ratio=T[i,j]/nv;edges.extend([(j,i,ratio),(i,j,ratio)])
phase={0:s.Integer(1)};queue=deque([0]);adj={i:[] for i in range(128)}
for j,i,r in edges:adj[j].append((i,r))
while queue:
 j=queue.popleft()
 for i,r in adj[j]:
  v=phase[j]*r
  if i in phase:ck(phase[i]==v,'root phase transport path independent')
  else:phase[i]=v;queue.append(i)
ck(len(phase)==128,'all spinor root phases fixed up to one global sign')
S=s.diag(*[phase[i] for i in range(128)]);etas={}
d8roots=[a for a in roots if all(x%2==0 for x in a)]
for a in d8roots:
 N=native_op(a);T=S*root_op(a)*S
 entry=next(iter(N.todok()));eta=T[entry]/N[entry]
 ck(eta in [-1,1] and T==eta*N,'full D8 root operator dictionary '+str(a));etas[str(a)]=int(eta)
# Cartan charges retain the native occupation action.
for i in range(8):
 H=s.diag(*[s.Rational(v[i],2) for v in spinroots]);N=(ads[i]*ads[i].T).extract(even,even)-s.eye(128)/2
 ck(H==N,'source Cartan equals native occupation minus one half '+str(i))
# Source D5+D3 decomposition, with D3=A3.
sectors=Counter((len(t&set(range(5)))%2,len(t&{5,6,7})%2) for t in sets)
ck(sectors=={(0,0):64,(1,1):64},'128 = even5 tensor even3 plus odd5 tensor odd3')
sector=[i for i,t in enumerate(sets) if len(t&set(range(5)))%2==0]
y=[s.Rational(-1,3)]*3+[s.Rational(1,2)]*2
per_family={}
for f in [frozenset(),frozenset({5,6}),frozenset({5,7}),frozenset({6,7})]:
 counts=Counter(str(sum(y[k] for k in sets[i] if k<5)) for i in sector if sets[i]&{5,6,7}==f)
 ck(counts=={'0':1,'-2/3':3,'1/6':6,'1':1,'-1/2':2,'1/3':3},'all original hypercharges in family weight '+str(sorted(f)));per_family[str(sorted(f))]=dict(counts)
# Original D5 Weyl word now acts via original root raising/lowering operators.
a,b=simple[0],simple[1];E1=native_op(a);E2=native_op(b);I128=s.eye(128)
n1=(I128+E1)*(I128-E1.T)*(I128+E1);n2=(I128+E2)*(I128-E2.T)*(I128+E2);weyl=n1*n2
traces=[]
for f in [frozenset(),frozenset({5,6}),frozenset({5,7}),frozenset({6,7})]:
 inds=[i for i in sector if sets[i]&{5,6,7}==f];traces.append(int(s.trace(weyl.extract(inds,inds))))
ck(traces==[4]*4,'native D5 Weyl trace restored on every family weight')
# Root-sector Lie brackets close back into D8 adjoint (112 roots + 8 Cartan).
nonzero=0
for a,b in itertools.product(spinroots,repeat=2):
 out=lie.bracket(lie.ridx[a],lie.ridx[b]);nonzero+=bool(out)
 ck(all(k>=240 or lie.roots[k] in d8roots for k in out),'spinor bracket lands in the native 120-dimensional D8 sector')
print('128 source root weights, all 112 root operators, and all charges matched',flush=True)
out={'verdict':'EXACT_NATIVE_E8_ROOT_TO_CAR_OPERATOR_DICTIONARY','checks':checks,'native_modes':{'complex':8,'majorana':16,'full_fock':256,'even_spinor':128},'e8_adjoint_split':[120,128],'source_subgroup_split':'D5 + D3 (D3 is A3)','source_halfroot_sectors':{'even5_even3':64,'odd5_odd3':64},'root_operator_signs':etas,'basis_phases':[int(phase[i]) for i in range(128)],'spinor_root_order':[list(v) for v in spinroots],'family_charge_multiplicities':per_family,'native_weyl_traces':traces,'nonzero_spinor_root_brackets':nonzero,'scope':'Exact source-compatible algebraic dictionary; no canonical physical vacuum, interacting dynamics or spacetime. The family fundamental has four weights; retaining its triplet is a marked readout, not newly derived three-generation selection.'}
(OUT/'native.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['checks','root_operator_signs','basis_phases','spinor_root_order']},indent=2));print('checks',len(checks))
