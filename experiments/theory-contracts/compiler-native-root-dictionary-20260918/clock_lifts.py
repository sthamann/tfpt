from common import ROOT,D,OUT
import json,itertools
from pathlib import Path
import sympy as s
R=s.Matrix(D['integral_triality']['vector_basis']);Ri=R.inv();G=R.T*R
B=s.zeros(8)
for i in range(8):
 B[i,i]=1
 for j in range(i):B[i,j]=G[i,j]
roots=set()
for i,j in itertools.combinations(range(8),2):
 for a,b in itertools.product([-2,2],repeat=2):
  v=[0]*8;v[i]=a;v[j]=b;roots.add(tuple(v))
roots|={v for v in itertools.product([-1,1],repeat=8) if v.count(-1)%2==0}
roots=sorted(roots);ix={v:i for i,v in enumerate(roots)};coords=[tuple(int(x) for x in Ri*s.Matrix(v)/2) for v in roots]
def ck(b,msg):
 if not b:raise RuntimeError(msg)
def eps(m,n):return (-1)**sum(m[i]*int(B[i,j])*n[j] for i in range(8) for j in range(i+1))
epsdict={(a,b):eps(coords[a],coords[b]) for a in range(240) for b in range(240) if tuple(x+y for x,y in zip(roots[a],roots[b])) in ix}
half={i for i,v in enumerate(roots) if all(abs(x)==1 for x in v)};carrier={i for i in half if sum(x==1 for x in roots[i][:5])%2==0};triplet={i for i in carrier if sum(x==1 for x in roots[i][5:])==2}
res={};perms={}
for name,item in D['clock_matrices'].items():
 M=s.Matrix(item['vector']);T=Ri*M*R
 ck(all(x.q==1 for x in T),'integer root coordinate action')
 delta=T.T*B*T-B
 ck(all(int(delta[i,i])%2==0 for i in range(8)) and all(int(delta[i,j]-delta[j,i])%2==0 for i in range(8) for j in range(8)),'cocycle difference has quadratic refinement')
 signs=[(-1)**sum(int(delta[i,j])*m[i]*m[j] for i in range(8) for j in range(i+1,8)) for m in coords]
 perm=[ix[tuple(M*s.Matrix(v))] for v in roots];perms[name]=perm
 ck(len(set(perm))==240,'bijective root action')
 for (a,b),ep in epsdict.items():
  c=ix[tuple(x+y for x,y in zip(roots[a],roots[b]))]
  ck(ep*signs[c]==signs[a]*signs[b]*epsdict[perm[a],perm[b]],'all nonzero root-sum brackets preserved')
 for a,v in enumerate(roots):
  neg=ix[tuple(-x for x in v)]
  ck(signs[a]*signs[neg]==1,'opposite-root Cartan bracket preserved')
 order={'C':30,'J':4,'sigma':3,'c':12}[name];finalsign=[]
 for a in range(240):
  z=1;b=a
  for k in range(order):z*=signs[b];b=perm[b]
  ck(b==a,'base clock order');finalsign.append(z)
 sectors={}
 for label,A in [('spinor128',half),('carrier64',carrier),('triplet48',triplet)]:
  image={perm[i] for i in A};sectors[label]={'size':len(A),'retained':len(image&A),'to_integer_root':len(image-half)}
 res[name]={'root_order':order,'lift_returns_plus':finalsign.count(1),'lift_returns_minus':finalsign.count(-1),'sectors':sectors,'root_permutation':perm,'root_signs':signs}
seen=set(triplet)
while True:
 more=seen|{perms[k][i] for k in ['C','J'] for i in seen}
 if more==seen:break
 seen=more
ck(len(seen)==240,'joint clocks generate all root directions from marked 48')
# Individual quadratic refinements need not respect the compiler power relations.
# Use the already verified order-12 lift of c to realize sigma=c^4 and J=c^9 coherently.
def power_lift(p,z,n):
 outp=[];outz=[]
 for a in range(240):
  b=a;w=1
  for _ in range(n):w*=z[b];b=p[b]
  outp.append(b);outz.append(w)
 return outp,outz
coherent={}
cp,cz=res['c']['root_permutation'],res['c']['root_signs']
for label,power,order in [('sigma',4,3),('J',9,4)]:
 p,z=power_lift(cp,cz,power)
 ck(p==res[label]['root_permutation'],'compiler power matches original coordinate clock')
 pp,zz=power_lift(p,z,order)
 ck(pp==list(range(240)) and zz==[1]*240,'coherent compiler lift has original order')
 for (a,b),ep in epsdict.items():
  c=ix[tuple(x+y for x,y in zip(roots[a],roots[b]))]
  ck(ep*z[c]==z[a]*z[b]*epsdict[p[a],p[b]],'coherent lift preserves all root-sum brackets')
 coherent[label]={'from_c_power':power,'order':order,'root_permutation':p,'root_signs':z,'changed_signs_from_independent_refinement':sum(a!=b for a,b in zip(z,res[label]['root_signs']))}
pj,zj=coherent['J']['root_permutation'],coherent['J']['root_signs'];ps,zs=coherent['sigma']['root_permutation'],coherent['sigma']['root_signs']
ck([pj[ps[i]] for i in range(240)]==cp and [zs[i]*zj[ps[i]] for i in range(240)]==cz,'coherent J sigma equals c including cocycle signs')
out={'verdict':'EXACT_COCYCLE_CLOCK_LIFTS_AND_MARKED_SECTOR_TRANSPORT','roots':roots,'clocks':res,'coherent_compiler_lifts':coherent,'nonzero_root_sum_pairs_checked_per_clock':len(epsdict),'joint_C_J_orbit_of_marked_48':len(seen),'scope':'Deterministic cocycle lift, not a proof of canonical group splitting or physical time. Fixed coordinate 5+3 and 1+3 marks; non-invariance is not a gauge or particle no-go.'}
(OUT/'clocks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**{k:v for k,v in out.items() if k!='coherent_compiler_lifts'},'roots':'240 exact roots','clocks':{k:{a:b for a,b in v.items() if a not in ['root_permutation','root_signs']} for k,v in res.items()}},indent=2))
