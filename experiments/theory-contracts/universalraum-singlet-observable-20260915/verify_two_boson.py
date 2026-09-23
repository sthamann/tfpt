"""Fresh two-boson source amplitudes and invariant projection weights.

Integer polynomial boson convention: ||(b_A^dagger)^2|0>||^2=2.
R is sqrt(2) times its ordered symmetric two-boson tensor, hence ||R||^2=2||v2||^2.
No ground-state approximation is called the true vacuum.
"""
from pathlib import Path
from collections import defaultdict
from itertools import combinations, permutations
from fractions import Fraction as F
from hashlib import sha256
import json
import numpy as np

HERE=Path(__file__).resolve().parent
checks=[]
def need(ok,name):
    if not ok: raise RuntimeError(name)
    checks.append(name)
def clean(d): return {k:v for k,v in d.items() if v}
def sign(mask,i): return (-1)**((mask&((1<<i)-1)).bit_count())

def main():
    path=HERE/'sources/spinor_tensors.npz'
    need(sha256(path.read_bytes()).hexdigest()=='3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763','native W archive pin')
    with np.load(path) as archive: W=archive['W']
    need(np.count_nonzero(W.imag)==0 and np.array_equal(W.real,np.rint(W.real)),
         'native W has exactly zero imaginary part and integral real entries')
    W=W.real.astype(np.int64)
    pairs=list(combinations(range(64),2))
    support=[(int(A),*pairs[int(c)],int(W[A,c])) for A,c in zip(*np.nonzero(W))]
    need(len(support)==480,'480 native creation vertices')
    v2=defaultdict(int)
    for A,i,j,w in support:
        mask=(1<<i)|(1<<j)
        for B,k,l,z in support:
            if mask&((1<<k)|(1<<l)): continue
            s=sign(mask,l)*sign(mask|(1<<l),k)
            v2[(mask|(1<<k)|(1<<l),min(A,B),max(A,B))]+=w*z*s
    v2=clean(v2)
    norm2=sum(c*c*(2 if A==B else 1) for (mask,A,B),c in v2.items())
    need(len(v2)==108240 and norm2==439680,'fresh complete v2 enumeration')
    R={}
    for (mask,A,B),c in v2.items():
        if A==B: R[(mask,A,B)]=2*c
        else: R[(mask,A,B)]=R[(mask,B,A)]=c
    nr=sum(c*c for c in R.values())
    need(nr==2*norm2,'ordered-tensor factorial normalization')
    colors=list(combinations(range(4),2))
    eps={p:(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)) for p in permutations(range(4))}
    cb=[];ce=[]
    for c,(a,b) in enumerate(colors):
        other=tuple(i for i in range(4) if i not in (a,b))
        cb.append(colors.index(other));ce.append(eps[(a,b,*other)])
    need(all(cb[cb[c]]==c and ce[cb[c]]==ce[c] for c in range(6)),'color metric involution')
    spin_trace=defaultdict(int);color_trace=defaultdict(int);both_trace=defaultdict(int)
    rf=0
    for (mask,A,B),amp in R.items():
        k,c=divmod(A,6);l,d=divmod(B,6)
        rf+=amp*R.get((mask,6*l+c,6*k+d),0)
        if l==(k+5)%10: spin_trace[(mask,c,d)]+=amp
        if d==cb[c]: color_trace[(mask,k,l)]+=ce[c]*amp
        if l==(k+5)%10 and d==cb[c]: both_trace[mask]+=ce[c]*amp
    ps=F(sum(a*a for a in spin_trace.values()),10)
    pc=F(sum(a*a for a in color_trace.values()),6)
    p00=F(sum(a*a for a in both_trace.values()),60)
    pplus=F(nr+rf,2);pminus=F(nr-rf,2)
    norms={'(1,1)':p00/2,'(54,1)':(pc-p00)/2,'(1,20prime)':(ps-p00)/2,
           '(54,20prime)':(pplus-pc-ps+p00)/2,'(45,15)':pminus/2}
    need(p00==0,'Fierz scalar-scalar projection of v2 vanishes')
    need(all(x>=0 for x in norms.values()),'nonnegative orthogonal projections')
    need(sum(norms.values())==norm2,'all five orthogonal projections exhaust v2')
    need(all(v>0 for k,v in norms.items() if k!='(1,1)'), 'native v2 populates all four singlet directions')
    # Complete compressed H up through boson level two. Three dark directions
    # at level two have diagonal 2 Delta; the sole bright direction couples sqrt(916).
    couplings={key:val/480 for key,val in norms.items() if val}
    need(sum(couplings.values())==916,'four squared source couplings add to 916')
    out={'status':'PASS','exact_checks':len(checks),'checks':checks,
         'v2_entries':len(v2),'v2_norm_squared':norm2,'ordered_tensor_norm_squared':nr,
         'spin_swap_overlap':rf,'orthogonal_v2_norms':{k:str(v) for k,v in norms.items()},
         'squared_couplings_from_normalized_v1':{k:str(v) for k,v in couplings.items()},
         'complete_k_le_2_singlet_dimension':6,
         'exact_compressed_H':'bright 3x3 diag(0,Delta,2Delta), offdiag(g sqrt(480),g sqrt(916)); plus 2Delta I3',
         'scope':{'compression_not_invariant':True,'full_ground_state_solved':False}}
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
