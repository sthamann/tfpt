"""Independent complete norm sums through N4 representation traces.

R_k = sum_ordered P†...P† |0><0| P...P.
||Q_+^k F||² = k! Tr(R_k), and
Tr R_{k+1} = Tr[R_k (V_{2k}+480-30k)].
The full N4 decomposition fixes R2 on four invariant copies.
Only pair creation/annihilation on four/six-hole states is needed for n4.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations
import numpy as np
import json,math,hashlib
W=np.load('outputs/simple_core/spinor_tensors.npz')['W'].real.astype(int)
pairs=list(combinations(range(64),2))
channels=[[(pairs[j][0],pairs[j][1],int(row[j])) for j in np.flatnonzero(row)] for row in W]
checks=[]
def need(c,label):
    if not c:raise RuntimeError(label)
    checks.append(label)
need(all(len({u for a,b,c in channel for u in [a,b]})==16 for channel in channels),'every channel has eight disjoint pairs')
need(all(sum(u in [a,b] for channel in channels for a,b,c in channel)==15 for u in range(64)),'exact commutator contraction 480 minus 15 Nf')
def pair_action(v,a,creation):
    out=defaultdict(int)
    for mask,coef in v.items():
        for u,w,sign in channels[a]:
            both=(1<<u)|(1<<w)
            if creation:
                if mask&both:continue
                target=mask|both;empty=mask
            else:
                if mask&both!=both:continue
                target=mask^both;empty=target
            lower=((1<<u)-1)^((1<<w)-1)
            out[target]+=coef*sign*(-1)**((empty&lower).bit_count())
    return {a:b for a,b in out.items() if b}
def norm(v):return sum(a*a for a in v.values())
def add(out,v,factor=1):
    for a,b in v.items():out[a]+=factor*b
def v_action(v):
    out=defaultdict(int)
    for a in range(60):add(out,pair_action(pair_action(v,a,False),a,True))
    return {a:b for a,b in out.items() if b}
seeds=[
 ('54,20',1080,14,14,{(0,0):1}),
 ('54,1',54,20,20,{(a,5-a):sign for a,sign in enumerate([1,-1,1])}),
 ('1,20',20,24,24,{(6*j,6*(j+5)):1 for j in range(5)}),
 ('45,15',675,16,18,{(0,7):1,(1,6):-1})]
traceR2=F(0);traceR3=F(0);traceR3V6=F(0);records=[]
for label,dim,squared,V4,seed in seeds:
    v=defaultdict(int)
    for (a,b),coef in seed.items():add(v,pair_action(pair_action({0:1},a,True),b,True),coef)
    v={a:b for a,b in v.items() if b};nv=norm(v)
    need(nv>0,f'{label} nonzero seed')
    need(v_action(v)=={a:V4*b for a,b in v.items()},f'{label} full V4 eigenvector identity')
    trace_first=0;trace_second=0
    for a in range(60):
        w=pair_action(v,a,True);trace_first+=norm(w)
        for b in range(60):trace_second+=norm(pair_action(w,b,False))
    need(trace_first==(V4+420)*nv,f'{label} complete pair-commutator contraction')
    S=F(trace_second,nv);R2=8*squared
    traceR2+=dim*R2
    traceR3+=dim*R2*(V4+420)
    traceR3V6+=dim*R2*S
    record={'irrep':label,'dimension':dim,'R2_eigenvalue':R2,'V4_eigenvalue':V4,'seed_norm_squared':nv,'four_hole_basis_terms':len(v),'sum_A_P_A_V6_P_A_dagger_expectation':str(S)}
    records.append(record);print(record,flush=True)
mom=[1,480,2*traceR2,6*traceR3,24*(traceR3V6+390*traceR3)]
need(all(x.denominator==1 if isinstance(x,F) else True for x in mom),'all trace-derived moments integers')
mom=list(map(int,mom))
original=json.loads(Path('outputs/many_pair/vacuum_number_sector.json').read_text())['moments']
need(mom==original,'independent complete trace derivation agrees with every bosonic norm sum through order four')
result={'status':'PASS','scope':'independent complete symmetry-trace derivation of all five norm moments, not a sample of the boson configurations','moments':mom,'trace_R2':str(traceR2),'trace_R3':str(traceR3),'trace_R3_V6':str(traceR3V6),'irreducible_contractions':records,'checks':checks,'dependencies':['complete N4 irreducible block theorem and seed identities','exact native pair commutator sum P_A P_A† = V+480-15 Nf','Spin10 x SU4 covariance'],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path('outputs/many_pair/moment_trace_identity.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
