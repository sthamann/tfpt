"""Cartan/Weyl reduction of the complete four-charge Fock sector."""
from pathlib import Path
from itertools import combinations
from collections import defaultdict,Counter
import sys,json,math,time
import numpy as np
from scipy.sparse import coo_matrix
sys.path.insert(0,str(Path(__file__).parent.resolve()))
import two_pairs as m

even=[s for s in range(32) if s.bit_count()%2==0]
colors=[tuple(1-2*((s>>j)&1) for j in range(3)) for s in range(8) if s.bit_count()%2==0]
roots=np.array([tuple(1-2*((s>>j)&1) for j in range(5))+c for s in even for c in colors],dtype=np.int64)
colorpairs=list(combinations(range(4),2))
broot=[]
for r in range(10):
    spin=[0]*5;spin[r%5]=-2 if r<5 else 2
    for a,b in colorpairs:broot.append(spin+[colors[a][j]+colors[b][j] for j in range(3)])
broot=np.array(broot,dtype=np.int64)
def dominant(q):
    answer=[]
    for part in [q[:5],q[5:]]:
        c=sorted(map(abs,part),reverse=True)
        if 0 not in c and math.prod(1 if x>0 else -1 for x in part)<0:c[-1]*=-1
        answer+=c
    return tuple(answer)
def all_charges():
    seed=defaultdict(dict);fcounts=Counter()
    for (u,v) in combinations(range(64),2):
        pair=roots[u]+roots[v];mask=(1<<u)|(1<<v)
        for b in range(60):seed[tuple(pair+broot[b])][(mask,(b,))]=1
    for a in range(60):
        for b in range(a,60):seed[tuple(broot[a]+broot[b])][(0,(a,b))]=1
    for ids in combinations(range(64),4):fcounts[tuple(sum((roots[i] for i in ids),np.zeros(8,dtype=np.int64)))]+=1
    orbits=defaultdict(list)
    for q in set(seed)|set(fcounts):orbits[dominant(q)].append(q)
    return seed,fcounts,orbits
if __name__=='__main__':
    seed,fcounts,orbits=all_charges()
    print('weights',len(set(seed)|set(fcounts)),'Weyl orbits',len(orbits),'states',sum(map(len,seed.values()))+sum(fcounts.values()),flush=True)
    q=(0,)*8;states,columns,metric,v=m.build(seed[q])
    sectors={b:[i for i,s in enumerate(states) if len(s[1])==b] for b in [0,1,2]}
    i0={s:i for i,s in enumerate(sectors[0])};i1={s:i for i,s in enumerate(sectors[1])}
    entries=[(i1[i],i0[j],a) for j in sectors[0] for i,a in columns[j] if i in i1]
    A=coo_matrix(([a for i,j,a in entries],([i for i,j,a in entries],[j for i,j,a in entries])),shape=(len(i1),len(i0)),dtype=np.int64).tocsr()
    C=(A@A.T).toarray();values=np.linalg.eigvalsh(C)
    print('Gram eigs',[(float(x),int(n)) for x,n in zip(*np.unique(np.round(values,8),return_counts=True))],flush=True)
    np.savez_compressed('outputs/many_pair/zero_charge_gram.npz',C=C)
    summary={'weights':len(set(seed)|set(fcounts)),'weyl_orbits':len(orbits),'total_states':sum(map(len,seed.values()))+sum(fcounts.values()),'orbits':[{'representative':[int(x) for x in d],'weights':len(qs),'B_F2_B2_count':len(seed[qs[0]]),'F4_count':fcounts[qs[0]]} for d,qs in sorted(orbits.items())],'zero_charge_Gram_eigenvalue_candidates':[(float(x),int(n)) for x,n in zip(*np.unique(np.round(values,8),return_counts=True))]}
    Path('outputs/many_pair/N4_charge_decomposition.json').write_text(json.dumps(summary,indent=2)+'\n')
