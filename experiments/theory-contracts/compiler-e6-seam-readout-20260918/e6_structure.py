import ast,json,itertools,hashlib
from pathlib import Path
from fractions import Fraction as F
from collections import Counter,deque
import sympy as s
import numpy as np
from common import ROOT,OUT,PINS
PARENT=ROOT/'experiments/theory-contracts/compiler-native-root-dictionary-20260918/certificate.json'
parent=json.loads(PARENT.read_text())
for p,h in parent['source_pins'].items():
 if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h:raise RuntimeError('source drift '+p)
D=json.loads((ROOT/'experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json').read_text());R=s.Matrix(D['integral_triality']['vector_basis']);Ri=R.inv();checks=[]
def ck(ok,msg):
 if not bool(ok):raise RuntimeError(msg)
 checks.append(msg)
class On(ast.NodeTransformer):
 def visit_Assert(self,n):return ast.copy_location(ast.Expr(ast.Call(ast.Name('ck',ast.Load()),[n.test,ast.Constant('legacy assertion')],[])),n)
def select(path,name,env):
 node=next(n for n in ast.parse((ROOT/path).read_text()).body if isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name==name)
 env['ck']=ck;exec(compile(ast.fix_missing_locations(On().visit(ast.Module(body=[node],type_ignores=[]))),str(ROOT/path),'exec'),env);return env[name]
raw=select('verification/v1_e8_glue.py','e8_roots',{'np':np,'itertools':itertools})();ck(all(float(2*x).is_integer() for v in raw for x in v),'exact dyadic conversion')
roots=[tuple(int(2*x) for x in v) for v in raw];rs=set(roots);coords={v:tuple(F(x) for x in Ri*s.Matrix(v)/2) for v in roots}
class RS:
 n=8
 def __init__(self):self.roots=roots;self.simple=[tuple(int(x) for x in 2*R[:,i]) for i in range(8)]
 def alpha_coords(self,v):return coords[v]
Chevalley=select('verification/v498_celestial_wp5b_singular_vector.py','Chevalley',{'F':F,'ip':lambda a,b:sum(x*y for x,y in zip(a,b)),'vadd':lambda a,b:tuple(x+y for x,y in zip(a,b))});lie=Chevalley(RS())
def ip(a,b):return sum(x*y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def q(a):return sum(a[5:])
a2={v for v in roots if v[:5]==(0,)*5 and sum(v[5:])==0}
e6={v for v in roots if all(ip(v,a)==0 for a in a2)}
d5={v for v in roots if v[5:]==(0,)*3}
ck(len(a2)==6 and len(e6)==72 and len(d5)==40,'root counts A2 E6 D5')
ck(s.Matrix(list(e6)).rank()==6 and s.Matrix(list(a2)).rank()==2,'ranks E6 and A2')
# Positive system from the original E8 chamber, then intrinsic simple roots.
e6pos={v for v in e6 if all(c>=0 for c in coords[v])}
simples=sorted(v for v in e6pos if not any(add(a,b)==v for a in e6pos for b in e6pos))
cartan=s.Matrix([[s.Rational(ip(a,b),4) for b in simples] for a in simples])
ck(len(simples)==6 and cartan.det()==3,'E6 simple root Cartan determinant 3')
# Full complex centralizer of A2: weight centralizer has 72 roots and six Cartan axes;
# every such root commutes with every A2 root under the original source bracket.
for a,b in itertools.product(e6,a2):ck(not lie.bracket(lie.ridx[a],lie.ridx[b]),'source E6 and A2 root generators commute')
for subset in [e6,a2]:
 for a,b in itertools.product(subset,repeat=2):
  out=lie.bracket(lie.ridx[a],lie.ridx[b]);ck(all(i>=240 or lie.roots[i] in subset for i in out),'source subalgebra root closure')
# Family weight in A2 Cartan: three times orthogonal projection of doubled root.
def fw(v):return tuple(3*x-sum(v[5:]) for x in v[5:])
weights=[tuple(-4 if k==j else 2 for k in range(3)) for j in range(3)]
blocks=[{v for v in roots if fw(v)==w} for w in weights]
plus=set().union(*blocks);minus={neg(v) for v in plus}
ck(all(len(b)==27 for b in blocks) and len(plus)==81,'three 27 dimensional family weight blocks')
ck(rs==e6|a2|plus|minus and sum(map(len,[e6,a2,plus,minus]))==240,'complete disjoint E8 root decomposition')
transitions=[]
for ib,block in enumerate(blocks):
 ck(Counter(q(v) for v in block)=={1:16,-2:10,4:1},'27 decomposes as 16_1 plus 10_-2 plus 1_4')
 for a,b in itertools.product(e6,block):
  out=lie.bracket(lie.ridx[a],lie.ridx[b])
  ck(all(i<240 and lie.roots[i] in block for i in out),'all E6 root operators preserve each native 27 block')
  for i,c in out.items():
   z=lie.roots[i]
   if ib==0 and q(b)!=q(z):transitions.append({'generator':a,'input':b,'output':z,'coefficient':str(c),'from_grade':q(b),'to_grade':q(z)})
 # Cartan weights are one dimensional; connected root-action graph implies irreducibility.
 seen={next(iter(block))}
 while True:
  more=seen|{add(a,b) for a in e6 for b in seen if add(a,b) in block}
  if more==seen:break
  seen=more
 ck(seen==block,'27 block connected under E6 operator action')
 ck(len({tuple(ip(v,a) for a in simples) for v in block})==27,'27 distinct E6 Cartan weights')
for a,b in itertools.product(a2,plus):
 out=lie.bracket(lie.ridx[a],lie.ridx[b]);ck(all(i<240 and lie.roots[i] in plus for i in out),'A2 family operators preserve all three 27 blocks jointly')
# Exact envelope of old marked 48 under the source E6 action.
old48={v for v in plus if q(v)==1};env=set(old48);history=[48]
while True:
 more=env|{add(a,b) for a in e6 for b in env if add(a,b) in rs}
 if more==env:break
 env=more;history.append(len(env))
ck(env==plus,'minimal E6 module containing old 48 has dimension 81')
singlets=e6-d5;ck(Counter(q(v) for v in singlets)=={-3:16,3:16},'former fourth carrier weights become E6 off-diagonal generators')
ck(Counter(q(v) for v in roots)=={-4:3,-3:16,-2:30,-1:48,0:46,1:48,2:30,3:16,4:3},'complete marked integer grading')
# The old 16+16 singlet sectors, D5 and the family charge Cartan close to E6.
# All three marked 16 spectra must remain exactly the original hypercharges.
y=[s.Rational(-1,3)]*3+[s.Rational(1,2)]*2
charges=[]
for b in blocks:
 count=Counter(str(sum(y[i]*s.Rational(v[i],2) for i in range(5))) for v in b if q(v)==1)
 ck(count=={'0':1,'-2/3':3,'1/6':6,'1':1,'1/3':3,'-1/2':2},'all three old 16 blocks preserve source hypercharges');charges.append(dict(count))
# Independent original clocks: the new 81 sector is also not generally a fixed-time sector.
clock={}
for name,data in D['clock_matrices'].items():
 M=s.Matrix(data['vector']);image={tuple(M*s.Matrix(v)) for v in plus};clock[name]={'retained_in_81':len(image&plus),'to_conjugate_81':len(image&minus),'to_E6_roots':len(image&e6),'to_A2_roots':len(image&a2)}
# Keep one nonzero source bracket for each pair of distinct D5 grading blocks.
witness={}
for t in transitions:witness.setdefault(str((t['from_grade'],t['to_grade'])),t)
out={'research_id':'UR.COMPILER.E6_READOUT_CLOSURE.04','verdict':'EXACT_MARKED_E6_A2_OPERATOR_REPACKING; PHYSICAL_SELECTION_OPEN','source_pins':PINS,'parent_certificate_sha256':hashlib.sha256(PARENT.read_bytes()).hexdigest(),'checks':len(checks),'e6_cartan':[[str(x) for x in row] for row in cartan.tolist()],'e6_simple_roots_doubled':simples,'root_sectors':{'E6':len(e6),'A2':len(a2),'27x3':len(plus),'conjugate':len(minus)},'lie_dimensions':[78,8,81,81],'marked_grade_dimensions_including_cartan':{'-4':3,'-3':16,'-2':30,'-1':48,'0':54,'1':48,'2':30,'3':16,'4':3},'family_weights_tripled_doubled':weights,'three_27_blocks':[[list(v) for v in sorted(b)] for b in blocks],'closure_history':history,'source_bracket_witnesses':witness,'hypercharges':charges,'clock_sector_transport':clock,'premises':['Existing coordinate D5+D3 marking and its complex family polarization','Family A2 chosen as number-preserving difference roots in last three coordinates; its selection from P1 is not derived here'],'scope':'Lie algebra modules only, not spacetime fermions or a selected vacuum. E6 and A2 factor names identify exact roots/actions, not newly derived physical gauge groups. Conjugate 81 remains present.'}
(OUT/'e6.json').write_text(json.dumps(out,indent=2)+'\n')
