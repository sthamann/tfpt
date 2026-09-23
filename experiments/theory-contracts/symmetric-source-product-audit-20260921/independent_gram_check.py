#!/usr/bin/env python3
"""Independent exact charge-block audit of the attached E8 symmetric product.

Column cocycle phases are removed unitarily for Gram spectra and weight
characters only. This does NOT check the archived tensor's signed dictionary.
"""
from itertools import product, combinations, combinations_with_replacement
from collections import Counter, defaultdict
from pathlib import Path
import hashlib
import json
import argparse
import sympy as s

def need(ok, message):
    if not ok:
        raise RuntimeError(message)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def pairs(weights, symmetric):
    it = combinations_with_replacement(weights,2) if symmetric else combinations(weights,2)
    return Counter(add(a,b) for a,b in it)
def tensor(a,b):
    out=Counter()
    for x,n in a.items():
        for y,m in b.items(): out[x+y]+=n*m
    return out

def main():
    spin5=[x for x in product((1,-1),repeat=5) if x.count(-1)%2==0]
    spin3=[x for x in product((1,-1),repeat=3) if x.count(-1)%2==0]
    roots=[a+b for a in spin5 for b in spin3]  # doubled source weights
    need(len(roots)==64,'64 marked roots')
    native=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-keyD-native-instruments-20260915/native_source.py')
    need(hashlib.sha256(native.read_bytes()).hexdigest()=='380577f85d2afa8b50f91a0991769eaf8267ee5c09f327d87f17e1b4c0af1672','archived native source pin')
    prefix,sep,_=native.read_text().partition('# --- Root-opposite boson pairing')
    need(bool(sep),'native source boundary')
    ns={'__file__':str(native),'__name__':'native_prefix_audit'}
    exec(compile(prefix,str(native),'exec',optimize=0),ns)
    need(set(roots)==set(map(tuple,ns['FW'].tolist())),'same marked weights as archived source')
    blocks=defaultdict(list); census=Counter()
    for i,j in combinations_with_replacement(range(64),2):
        r,t=roots[i],roots[j]; d=dot(r,t)//4
        need(dot(r,t)%4==0,'integral pair inner product')
        census[d]+=1
        blocks[add(r,t)].append((r,t,d))
    spectra=Counter(); chars={0:Counter(),4:Counter(),8:Counter()}
    image_by_dot=Counter(); blocktypes=Counter(); nnz=0
    for q,ps in blocks.items():
        n=len(ps); ds={p[2] for p in ps}
        need(len(ds)==1,'common charge determines pair type')
        d=next(iter(ds))
        if d==-1:
            # S column = (r-t)/sqrt(2), using undoubled roots.
            diffs=[tuple((a-b)//2 for a,b in zip(r,t)) for r,t,_ in ps]
            G=s.Matrix(n,n,lambda i,j:s.Rational(dot(diffs[i],diffs[j]),2))
            nnz+=sum(sum(x!=0 for x in v) for v in diffs)
        elif d==0:
            G=2*s.ones(n);nnz+=n
        else:
            need(d in (1,2),'only regular vanishing types remain')
            G=s.zeros(n)
        need(G*(G-4*s.eye(n))*(G-8*s.eye(n))==s.zeros(n),'exact Gram polynomial')
        eig=G.eigenvals()
        need(set(eig)<=set((0,4,8)),'exact allowed eigenvalues')
        need(all(v>=0 for v in eig),'positive Gram')
        p100=G*(G-4*s.eye(n))/32
        p720=G*(8*s.eye(n)-G)/16
        need(p100*p100==p100 and p720*p720==p720 and p100*p720==s.zeros(n),'orthogonal polynomial projectors')
        for ev,m in eig.items():
            spectra[int(ev)]+=m; chars[int(ev)][q]+=m
            if ev: image_by_dot[d]+=m
        blocktypes[(d,n)]+=1
    # Character comparison in doubled-weight coordinates, not dimensions alone.
    vector5=Counter()
    for i in range(5):
        for sg in (-1,1):
            v=[0]*5;v[i]=2*sg;vector5[tuple(v)]+=1
    symspin=pairs(spin5,True); antisymspin=pairs(spin5,False)
    char126=symspin.copy();char126.subtract(vector5)
    need(all(v>=0 for v in char126.values()),'126 character nonnegative')
    symfamily=pairs(spin3,True);antisymfamily=pairs(spin3,False)
    expected100=tensor(vector5,symfamily)
    expected720=tensor(antisymspin,antisymfamily)
    expected1260=tensor(char126,symfamily)
    need(chars[8]==expected100,'all 100 weights and multiplicities')
    need(chars[4]==expected720,'all 720 weights and multiplicities')
    need(chars[0]==expected1260,'all 1260 null weights and multiplicities')
    need(spectra=={0:1260,4:720,8:100},'claimed full spectrum')
    h1,h2,h3=s.symbols('h1 h2 h3',real=True)
    A=s.Matrix([[0,h3,-h2],[-h3,0,h1],[h2,-h1,0]])
    sigma=s.Matrix([[0,1,0],[0,0,1],[1,0,0]])
    Y=sigma.T*A-A*sigma
    det=-2*(h1+h2+h3)*(h1*h1+h2*h2+h3*h3-h1*h2-h1*h3-h2*h3)
    need(Y==Y.T and s.expand(Y.det()-det)==0,'relative-clock symmetric determinant')
    rp=tuple([1]*8);twor=add(rp,rp)
    min_degree=s.Rational(dot(twor,twor),8)
    need(min_degree==4,'highest weight of 126,10 first allowed grade four')
    result={
      'verdict':'PASS_SCOPED_INDEPENDENT_ALGEBRA_AUDIT',
      'source':str(native),'source_sha256':hashlib.sha256(native.read_bytes()).hexdigest(),
      'inputs':sum(census.values()),'charge_blocks':len(blocks),
      'input_inner_product_counts':dict(sorted(census.items())),
      'image_ranks_by_inner_product':dict(sorted(image_by_dot.items())),
      'spectrum':dict(sorted(spectra.items())),'image_rank':sum(image_by_dot.values()),
      'nonzero_coordinate_entries':nnz,
      'full_weight_character_match':{'8':'(10,10)','4':'(120,6)','0':'(126,10)'},
      'clock_determinant':str(s.factor(Y.det())),
      'highest_weight_minimum_degree':str(min_degree),
      'cocycle_scope':'Column phases removed for Gram spectra/weight characters; not the archived signed operator map.',
      'equivariance_scope':'Zero-mode derivation identity proves symmetrized product equivariance; all 52 signed matrices NOT independently replayed here.',
      'not_checked':['unavailable original reproduction package','claimed two-texture CP example','historical Bell10 signed operator identification','physical field/state/time selection','full TFPT suite'],
      'physical_gates_closed':[]}
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path(__file__).with_name('independent_certificate.json'))
    args=ap.parse_args();result=main()
    args.out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(result,indent=2,ensure_ascii=False))
