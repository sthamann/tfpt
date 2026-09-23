"""Exact independent E8 sign audit and all-order CAR/tensor matching-sector adapter.
This constructs a standard ordered lattice cocycle, NOT a proven native clock lift.
"""
from itertools import product, combinations, permutations
from fractions import Fraction as F
from collections import deque
from pathlib import Path
import sympy as s
import numpy as np
import json,hashlib
HERE=Path(__file__).resolve().parent
checks=[]
def need(ok,name):
    if not bool(ok):raise RuntimeError(name)
    checks.append(name)
def solve(rows,n):
    piv={}
    for bits,b in rows:
        while bits:
            p=bits.bit_length()-1
            if p in piv:bits^=piv[p][0];b^=piv[p][1]
            else:piv[p]=(bits,b);break
        if not bits and b:return False,len(piv),None
    x=0
    for p,(bits,b) in sorted(piv.items()):
        if (bits&x).bit_count()%2!=b:x|=1<<p
    need(all(((bits&x).bit_count()%2)==b for bits,b in rows),'solution verifies every sign equation')
    return True,len(piv),x
def lattice():
    halves=[tuple(F(x,2) for x in z) for z in product((-1,1),repeat=8) if np.prod(z)==1]
    ints=[]
    for i,j in combinations(range(8),2):
        for a,b in product((-1,1),repeat=2):
            v=[F(0)]*8;v[i]=a;v[j]=b;ints.append(tuple(v))
    roots=sorted(halves+ints)
    simple=[tuple(F(x,2) for x in (1,-1,-1,-1,-1,-1,-1,1)),(1,1,0,0,0,0,0,0)]
    for i in range(6):
        v=[0]*8;v[i]=-1;v[i+1]=1;simple.append(tuple(v))
    A=s.Matrix(simple);G=A*A.T;Ai=A.T.inv()
    need(G.det()==1,'E8 determinant one')
    coords={r:tuple(Ai*s.Matrix(r)) for r in roots}
    need(all(all(x.q==1 for x in v) for v in coords.values()),'240 integral root coordinates')
    B=s.zeros(8)
    for i in range(8):
        for j in range(8):B[i,j]=1 if i==j else G[i,j] if i>j else 0
    need(all((B[i,j]+B[j,i]-G[i,j])%2==0 for i in range(8) for j in range(8)),'cocycle commutator identity modulo two')
    # Bilinearity proves the cocycle identity for arbitrary lattice vectors.
    B=np.array(B,dtype=int);coords={r:np.array(v,dtype=int) for r,v in coords.items()}
    def eps(a,b):return int(coords[a]@B@coords[b])%2
    sites=sorted({r[:5] for r in halves if np.prod(r[:5])<0})
    colours=sorted({r[5:] for r in halves if np.prod(r[:5])<0})
    need(len(sites)==16 and len(colours)==4,'D5 A3 positive spinor grade')
    edges=[(i,j) for i,j in combinations(range(16),2) if sum(a!=b for a,b in zip(sites[i],sites[j]))==4]
    labels=[tuple(a+b for a,b in zip(sites[i],sites[j])) for i,j in edges]
    mus=sorted({(lab,tuple(a+b for a,b in zip(ca,cb))) for lab in labels for ca,cb in permutations(colours,2)})
    med={m:i for i,m in enumerate(mus)};pairs=list(combinations(range(4),2))
    anti=[];glob=[];loc=[]
    for k,(i,j) in enumerate(edges):
        for a,b in permutations(range(4),2):
            bit=eps(sites[i]+colours[a],sites[j]+colours[b])^(int(a>b))
            site=(1<<(4*i+a))^(1<<(4*j+b))
            mu=med[(labels[k],tuple(x+y for x,y in zip(colours[a],colours[b])))]
            glob.append((site^(1<<(64+mu)),bit))
            loc.append((site^(1<<(64+6*k+pairs.index(tuple(sorted((a,b)))))),bit))
        for a,b in pairs:
            bit=eps(sites[i]+colours[a],sites[j]+colours[b])^eps(sites[i]+colours[b],sites[j]+colours[a])^1
            anti.append((sum(1<<(4*p+c) for p,c in [(i,a),(i,b),(j,a),(j,b)]),bit))
    ans1=solve(anti,64);ansg=solve(glob,124);ansl=solve(loc,304)
    need(ans1[:2]==(True,45),'site-colour antisymmetry rank 45')
    need(not ansg[0],'shared-mode sign obstruction')
    need(ansl[:2]==(True,285),'edge-local sign adapter rank 285')
    return {'site_colour_rank':ans1[1],'edge_local_rank':ansl[1],
            'shared_diagonal_sign_gauge_exists':ansg[0],
            'standard_lattice_cocycle_only':True,'native_clock_lift_identified':False}

def car():
    # Per-edge bosons in Q_v=n_f(v)+sum_{e contains v}n_e=1. All occupied
    # bosons form a matching; every pair colour state has two orientations.
    n=4;edges=list(combinations(range(n),2));pairs=list(combinations(range(4),2))
    states=[]
    for nm in range(3):
        for es in combinations(range(len(edges)),nm):
            ends=[v for k in es for v in edges[k]]
            if len(set(ends))!=len(ends):continue
            free=[v for v in range(n) if v not in ends]
            for cs in product(pairs,repeat=nm):
                bos=tuple(zip(es,cs))
                for cols in product(range(4),repeat=len(free)):
                    m=[-1]*n
                    for v,c in zip(free,cols):m[v]=c
                    states.append((tuple(m),bos))
    need(len(states)==940,'full K4 matching-sector dimension 940')
    index=set(states)
    def gauge(bos):
        es=[edges[k] for k,c in bos]
        nc=sum(i<k<j<l or k<i<l<j for (i,j),(k,l) in combinations(es,2))
        return (-1)**nc
    transitions=0;neg=0
    for m,bos in states:
        for v in range(n):need((m[v]>=0)+sum(v in edges[k] for k,c in bos)==1,'local conserved charge on enumerated state')
        for k,(i,j) in enumerate(edges):
            if m[i]<0 or m[j]<0 or m[i]==m[j]:continue
            mm=list(m);mm[i]=mm[j]=-1
            bb=tuple(sorted(bos+((k,tuple(sorted((m[i],m[j])))),)))
            dest=(tuple(mm),bb);need(dest in index,'matching sector closed under pair removal')
            sign_car=(-1)**sum(m[v]>=0 for v in range(i+1,j))
            base=(-1)**(j-i-1)
            relative=sign_car*base
            need(relative==gauge(bb)*gauge(bos),'CAR sign equals crossing-gauge coboundary')
            transitions+=1;neg+=relative<0
    need(neg>0,'crossing pairs exercise nontrivial fermionic signs')
    return {'dimension':len(states),'creation_transitions':transitions,'nontrivial_relative_signs':neg,
            'all_orders_scope':'per-edge mediator, Q_v=1, no mediator hopping, fixed site order, edge base phases',
            'CAR_tensor_unitary_gauge_exists':True,'shared_mode_extension':False}
def run():
    result={'lattice':lattice(),'car':car(),'checks':checks,'count':len(checks),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'T1_T8_closed':[]}
    return result
if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(HERE/'phase_car.json'));a=ap.parse_args()
    result=run();Path(a.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
