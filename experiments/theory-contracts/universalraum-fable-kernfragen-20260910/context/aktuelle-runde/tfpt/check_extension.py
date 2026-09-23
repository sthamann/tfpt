"""Fresh exact path/CAR audit for the next Wilson-cap blocks; no prior outputs rewritten."""
from collections import Counter
from itertools import product
from pathlib import Path
from fractions import Fraction as F
import json
import sympy as s

tests=[]
def ck(name,p):
    assert bool(p),name
    tests.append({'name':name,'pass':True})
L=5;sites=list(product(range(L),repeat=3));N=len(sites)
a=s.Rational(1,12);b=s.Rational(1,24);c=s.Rational(1,576);kap=s.Rational(1,100)
def move(x,j,sg):
    y=list(x);y[j]=(y[j]+sg)%L;return tuple(y)
def hop(x,j,sg):
    y=move(x,j,sg);return y,(x,j) if sg==1 else (y,j),sg
def fkey(d):return tuple(sorted((e,v) for e,v in d.items() if v))
directions=list(product(range(3),(-1,1)))
walks=Counter();triangles=0
for x in sites:
    for word in product(directions,repeat=4):
        y=x;flux=Counter()
        for j,sg in word:
            y,e,k=hop(y,j,sg);flux[e]+=k
        if y==x:walks[fkey(flux)]+=1
    for word in product(directions,repeat=3):
        y=x
        for j,sg in word:y=move(y,j,sg)
        triangles+=y==x
ck('Native full torus closed-four-walk count',sum(walks.values())==90*N)
ck('Uncut zero-flux and actual plaquette decomposition',walks[()]==66*N and len(walks)-1==6*N and all(n==4 for p,n in walks.items() if p))
ck('No original three-step closed paths',triangles==0)
def plaq(z):return {((0,0,z),0):1,((1,0,z),1):1,((0,1,z),0):-1,((0,0,z),1):-1}
p1,p2=plaq(0),plaq(2)
code=[]
for r,t in product(range(4),repeat=2):
    f=Counter({e:r*k for e,k in p1.items()});f.update({e:t*k for e,k in p2.items()});code.append(f)
trace4=s.zeros(16)
for row,col in product(range(16),repeat=2):
    d=Counter(code[row]);d.subtract(code[col]);trace4[row,col]=walks[fkey(d)]
F4=s.zeros(4)
for j in range(3):F4[j+1,j]=1
K=s.kronecker_product(F4+F4.T,s.eye(4))+s.kronecker_product(s.eye(4),F4+F4.T)
ck('Whole Tr Q^4 compression keeps exactly two noncyclic Wilson readers',trace4==66*N*s.eye(16)+4*K)
g2=6*N*b*b
Gpair=s.simplify(b**4/g2*2*((6*N)**2*s.eye(16)-trace4))
ck('Exact next two-pair Gram',Gpair==s.Rational(739,288)*s.eye(16)-K/s.Integer(54000))
ck('Next two-pair channel injective without numeric eigensolver',all(Gpair[i,i]>sum(abs(Gpair[i,j]) for j in range(16) if j!=i) for i in range(16)))
h1shift=(4+kap/2)*s.eye(16)-c*trace4/(6*N)
ck('Actual first enlarged diagonal block',h1shift==s.Rational(57397,14400)*s.eye(16)-K/s.Integer(108000))

# Independent CAR sign of a low-hole return, with two occupied low modes.
def odd(mask,j,creation=False):
    occupied=(mask>>j)&1
    if occupied==creation:return None
    sign=(-1)**((mask&((1<<j)-1)).bit_count())
    return mask^(1<<j),sign
def word(mask,ops):
    amp=1
    for j,creation in reversed(ops):
        r=odd(mask,j,creation)
        if r is None:return None
        mask,sg=r;amp*=sg
    return mask,amp
# Modes l_x,d_x,l_y,d_y. T=d_x^* l_y; L=l_y^* l_x.
initial=(1<<0)|(1<<2)
first=word(initial,[(1,True),(2,False)])
second=word(first[0],[(2,True),(0,False)])
direct=word(initial,[(1,True),(0,False)])
ck('Native low-hole backtrack has minus CAR sign',second[0]==direct[0] and first[1]*second[1]==-direct[1])
ck('Coherent onsite next channel coupling',s.simplify((6*a*b*s.sqrt(N)/s.sqrt(g2))**2)==s.Rational(1,24))

# Two independent even LH monomials commute and add, rather than cancel.
full=sum(1<<(2*i) for i in range(4))
te=[(3,True),(0,False)];tf=[(7,True),(4,False)]
e=word(full,te);ef=word(e[0],tf)
f=word(full,tf);fe=word(f[0],te)
ck('Two true disjoint LH orders reinforce',ef[0]==fe[0] and e[1]*ef[1]==f[1]*fe[1])
ck('Explicit isolated two-pair amplitude squared',s.simplify(4*b**4/g2)==s.Rational(1,108000))
result={'status':'PASS','count':len(tests),'tests':tests,'L':L,'N':N,
 'first_coupling_squared':str(g2),'h1_minus_h0':'57397/14400 I - K/108000',
 'two_pair_Gram':'739/288 I - K/54000','onsite_next_coupling_squared':'1/24',
 'four_step_closed_walks':sum(walks.values()),'trivial_flux_four_walks':walks[()],
 'scope':'Exact original path/CAR identities and finite source-column actions, no electric cutoff or original module imports; first extension not claimed invariant.'}
Path(__file__).with_name('extension-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','count':len(tests),'walks':sum(walks.values())}))
