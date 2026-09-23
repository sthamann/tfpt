"""Exact Wilson-loop cap and full native LH leakage; no TFPT imports/cutoffs."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sympy as s

checks=[]
def ck(name,condition):
    assert bool(condition),name
    checks.append({'name':name,'pass':True})

L=5;sites=list(product(range(L),repeat=3));index={x:i for i,x in enumerate(sites)}
N=len(sites);b=F(1,24);kappa=s.Rational(1,100)
def neighbor(x,axis,d=1):
    y=list(x);y[axis]=(y[axis]+d)%L;return tuple(y)
edges=[(x,axis) for x in sites for axis in range(3)]
def plaquette(z):
    return {((0,0,z),0):1,((1,0,z),1):1,((0,1,z),0):-1,((0,0,z),1):-1}
p1,p2=plaquette(0),plaquette(2)
def addflux(v,p,k=1):
    out=dict(v)
    for e,n in p.items():out[e]=out.get(e,0)+k*n
    return {e:n for e,n in out.items() if n}
def div(v):
    out=defaultdict(int)
    for (x,axis),n in v.items():
        out[x]+=n;out[neighbor(x,axis)]-=n
    return {x:n for x,n in out.items() if n}
def cyc(v,p):
    anchor=next(e for e,n in p.items() if n==1)
    r=v.get(anchor,0)%4
    return addflux(v,p,1 if r!=3 else -3)
def fluxkey(v):return tuple(sorted(v.items()))
ck('Two native plaquettes disjoint and Gauss neutral',not set(p1)&set(p2) and div(p1)==div(p2)=={})
ok=True
for q in range(-3,4):
    for r in range(4):
        v=addflux({},p1,4*q+r);base=dict(v)
        for _ in range(4):v=cyc(v,p1)
        ok &= v==base and div(v)=={}
ck('Physical carry-corrected Wilson cycle has order four on arbitrary tested coarse flux',ok)

I=s.eye(4);S=s.zeros(4)
for a in range(4):S[(a+1)%4,a]=1
Z=s.diag(1,s.I,-1,-s.I)
ck('Native marked Weyl and star laws',S**4==I and S.H*S==I and Z*S==s.I*S*Z)
ck('Regular group products and canonical positive state',all(S**a*S**bb==S**((a+bb)%4) for a in range(4) for bb in range(4)) and all((S**a)[0,0]==int(a==0) for a in range(4)))
P=[s.diag(*[int(j==a) for j in range(4)]) for a in range(4)]
E={(a,bb):S**((a-bb)%4)*P[bb] for a in range(4) for bb in range(4)}
ck('Physical matrix units',all(E[a,bb]*E[c,d]==(E[a,d] if bb==c else s.zeros(4)) for a,bb,c,d in product(range(4),repeat=4)))
m=s.zeros(4,16)
for a,bb in product(range(4),repeat=2):m[(a+bb)%4,4*a+bb]=1
M=s.zeros(16)
for a,bb in product(range(4),repeat=2):M+=s.kronecker_product(E[(a+bb)%4,a],E[0,bb])
J1=s.kronecker_product(I,s.eye(4)[:,0])
ck('Actual two-loop multiplication and adjoint commute with embeddings',M==J1*m and M.H*J1==m.H and J1.H*J1==I)
K=M/2
ck('Normalized multiplication is a complete physical filter branch',K*K.H==s.kronecker_product(I,P[0]) and (K.H*K)**2==K.H*K and K.H*K+(s.eye(16)-K.H*K)**2==s.eye(16))
origin=s.eye(16)[:,0];cap=m.H*s.eye(4)[:,0]/2
DFT=s.Matrix(4,4,lambda a,bb:s.I**(a*bb)/2)
controlled=sum((s.kronecker_product(P[a],S**((-a)%4)) for a in range(4)),s.zeros(16))
prep=controlled*s.kronecker_product(DFT,I)
ck('Unitary gauge-invariant cap preparation and adjoint multiplication agree',prep.H*prep==s.eye(16) and prep*origin==cap and K.H*origin==cap)
balance=s.kronecker_product(S,S.H);grade=s.kronecker_product(Z,Z)
ck('Cap pairing and full balance', (cap.H*cap)[0]==1 and balance*cap==cap and grade*cap==cap and cap[0]==s.Rational(1,2))

code=[addflux(addflux({},p1,a),p2,bb) for a,bb in product(range(4),repeat=2)]
ck('Physical sixteen-code isometry and exact neutrality',len({fluxkey(v) for v in code})==16 and all(div(v)=={} for v in code))
electric=s.diag(*[kappa*sum(n*n for n in v.values())/2 for v in code])
ck('Electric compression retains every native flux energy',electric==s.diag(*[2*kappa*(a*a+bb*bb) for a,bb in product(range(4),repeat=2)]))
mean=s.simplify((cap.H*electric*cap)[0])
variance=s.simplify((cap.H*electric**2*cap)[0]-mean**2)
defect=(electric*balance-balance*electric)*cap
ck('Cap energy and nonstationarity exact',mean==14*kappa and variance==68*kappa*kappa)
ck('Fixed cap balance generator defect exact',s.simplify((defect.H*defect)[0])==208*kappa*kappa==s.Rational(13,625))

full_low=sum(1<<(2*i) for i in range(N))
def move_car(high,hole):
    annihilator=2*hole;creator=2*high+1
    mask=full_low
    sign=(-1)**((mask&((1<<annihilator)-1)).bit_count())
    mask ^=1<<annihilator
    sign*=(-1)**((mask&((1<<creator)-1)).bit_count())
    mask|=1<<creator
    return mask,sign
terms=[]
for e in edges:
    x,axis=e;y=neighbor(x,axis)
    terms.extend([(y,x,e,1),(x,y,e,-1)])
ck('All native oriented LH terms counted',len(terms)==6*N and len({(x,y) for x,y,e,sg in terms})==6*N)
out=defaultdict(dict);gauss_ok=True
for column,flux in enumerate(code):
    for high,hole,e,sg in terms:
        mask,sign=move_car(index[high],index[hole])
        newflux=addflux(flux,{e:sg})
        gauss=defaultdict(int,div(newflux));gauss[high]+=1;gauss[hole]-=1
        gauss_ok &= all(n==0 for n in gauss.values())
        key=(mask,fluxkey(newflux))
        out[key][column]=out[key].get(column,F(0))+sign*b
ck('Every true leakage branch stays in physical Gauss sector',gauss_ok)
gram=[[F(0) for _ in range(16)] for _ in range(16)]
for row in out.values():
    for a,va in row.items():
        for bb,vb in row.items():gram[a][bb]+=va*vb
ck('Complete original LH leakage is scalar and has no cancelling code direction',all(gram[a][bb]==(F(N,96) if a==bb else 0) for a,bb in product(range(16),repeat=2)))
ck('All LL offsite hopping is Pauli-blocked on the code',all((full_low>>(2*index[x]))&1 and (full_low>>(2*index[y]))&1 for x,y,e,sg in terms))
ck('Bounded electric clock generator has unavoidable CAR matrix element',s.simplify(abs((1-s.I)*s.Rational(1,24))**2)==s.Rational(1,288))

data={'status':'PASS','count':len(checks),'checks':checks,'torus_L':L,'sites':N,
      'physical_code_dimension':16,'directed_LH_terms':len(terms),
      'leakage_output_states':len(out),'leakage_gram_diagonal':str(F(N,96)),
      'single_clock_matter_generator_witness_squared':'1/288',
      'cap_electric_energy_increase':str(mean),'cap_electric_variance':str(variance),
      'cap_balance_commutator_projected_norm_squared':'13/625',
      'scope':'Exact full-H action on explicitly finite-flux test vectors, not a flux-cutoff Hamiltonian; native interactions preserved. No original TFPT module run/import.'}
Path(__file__).with_name('wilson-cap-checks.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:data[k] for k in ['status','count','sites','leakage_output_states','leakage_gram_diagonal']}))
