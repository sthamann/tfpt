"""Exact CAR/boson dynamics beyond the single-pair sector.

The boson basis is unnormalized: creation has coefficient 1, annihilation
coefficient n, and its Gram weight is product n!. Thus every Hamilton entry
is integral at L=20 H/Delta and g/Delta=1/20. No tensor hard-core rule is added.
"""
from pathlib import Path
from itertools import combinations
from collections import deque
from fractions import Fraction as F
import numpy as np
import sympy as sp
import json,math,hashlib,time

OUT=Path('outputs/many_pair');OUT.mkdir(parents=True,exist_ok=True)
W=np.load('outputs/simple_core/spinor_tensors.npz')['W'].real.astype(int)
pairs=list(combinations(range(64),2));couple={};decay={i:[] for i in range(60)}
for col,pair in enumerate(pairs):
    rows=np.flatnonzero(W[:,col])
    if len(rows):
        r=int(rows[0]);s=int(W[r,col]);couple[pair]=(r,s);decay[r].append((*pair,s))
def parity(mask,j):return -1 if (mask&((1<<j)-1)).bit_count()%2 else 1
def transitions(state):
    mask,bosons=state;answer={state:20*len(bosons)}
    occupied=[i for i in range(64) if mask>>i&1]
    for u,v in combinations(occupied,2):
        link=couple.get((u,v))
        if link is None:continue
        r,s=link;left=mask^(1<<u);coef=s*parity(mask,u)*parity(left,v)
        dest=(left^(1<<v),tuple(sorted((*bosons,r))))
        answer[dest]=answer.get(dest,0)+coef
    for r in set(bosons):
        remaining=list(bosons);remaining.remove(r);multiplicity=bosons.count(r)
        for u,v,s in decay[r]:
            if mask>>u&1 or mask>>v&1:continue
            coef=s*multiplicity*parity(mask,v)*parity(mask,u)
            dest=(mask|(1<<u)|(1<<v),tuple(remaining))
            answer[dest]=answer.get(dest,0)+coef
    return {k:v for k,v in answer.items() if v}
def build(seed):
    states=list(seed);index={s:i for i,s in enumerate(states)};edges=[];start=time.time()
    for state in states:
        row=transitions(state);edges.append(row)
        for dest in row:
            if dest not in index:index[dest]=len(states);states.append(dest)
    columns=[[(index[s],v) for s,v in r.items()] for r in edges]
    metric=[math.prod(math.factorial(state[1].count(b)) for b in set(state[1])) for state in states]
    for j,column in enumerate(columns):
        for i,value in column:
            back=edges[i].get(states[j],0)
            if metric[i]*value!=metric[j]*back:raise RuntimeError('exact weighted self-adjointness failed')
    print('reachable graph',len(states),'edges',sum(map(len,columns)),'seconds',time.time()-start,flush=True)
    v=[F(0)]*len(states)
    for s,a in seed.items():v[index[s]]=F(a)
    return states,columns,metric,v
def dot(a,b,metric):return sum((x*y*m for x,y,m in zip(a,b,metric)),F(0))
def action(v,columns):
    out=[F(0)]*len(v)
    for j,x in enumerate(v):
        if x:
            for i,a in columns[j]:out[i]+=a*x
    return out
def lanczos(v,columns,metric,states,cap=60):
    previous=[F(0)]*len(v);lastnorm=None;records=[]
    for n in range(cap):
        norm=dot(v,v,metric);hv=action(v,columns);alpha=dot(v,hv,metric)/norm
        beta=norm/lastnorm if lastnorm is not None else F(0)
        w=[x-alpha*y-beta*z for x,y,z in zip(hv,v,previous)]
        nextnorm=dot(w,w,metric)
        occupancies=sorted({len(states[i][1]) for i,x in enumerate(v) if x})
        if len(occupancies)!=1 or alpha!=20*occupancies[0]:raise RuntimeError('basis fails occupation-purity needed for arbitrary Delta and g')
        row={'n':n,'norm':str(norm),'alpha':str(alpha),'beta':str(beta),'nextnorm':str(nextnorm),'boson_occupation':occupancies[0]}
        records.append(row);print('Lanczos',n,'a',alpha,'b',beta,'closed',nextnorm==0,flush=True)
        if nextnorm==0:return records
        previous,v,lastnorm=v,w,norm
    raise RuntimeError('Krylov space did not close within declared cap')
def solve(seed,name):
    states,columns,metric,v=build(seed);records=lanczos(v,columns,metric,states)
    z=sp.Symbol('z');prev=sp.Integer(1);poly=z-sp.Rational(records[0]['alpha'])
    for row in records[1:]:prev,poly=poly,sp.expand((z-sp.Rational(row['alpha']))*poly-sp.Rational(row['beta'])*prev)
    p=sp.Poly(poly,z)
    result={'seed':name,'scope':'complete exact cyclic Hamiltonian space reached from the declared two-mediator seed, not the whole N=4 sector','reachable_basis_states':len(states),'occupation_counts':{str(b):sum(len(s[1])==b for s in states) for b in [0,1,2]},'integer_operator':'L=20H/Delta, g/Delta=1/20','exact_weighted_self_adjointness':True,'Krylov_dimension':len(records),'Lanczos':records,'minimal_polynomial':str(p.as_expr()),'factorization':str(sp.factor(p.as_expr())),'root_intervals':[([str(a),str(b)],m) for (a,b),m in sp.polys.polytools.intervals(p,eps=sp.Rational(1,10**10))],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (OUT/f'{name}.json').write_text(json.dumps(result,indent=2)+'\n');return result
if __name__=='__main__':
    seeds={'54_20':{(0,(0,0)):1},
      '54_1':{(0,tuple(sorted((a,5-a)))):s for a,s in enumerate([1,-1,1])},
      '1_20':{(0,(6*j,6*(j+5))):1 for j in range(5)},
      '1_1':{(0,(6*j+a,6*(j+5)+5-a)):([1,-1,1,1,-1,1][a]) for j in range(5) for a in range(6)},
      '45_15':{(0,(0,7)):1,(0,(1,6)):-1}}
    for name,seed in seeds.items():
        print('SEED',name,flush=True);solve(seed,name)
