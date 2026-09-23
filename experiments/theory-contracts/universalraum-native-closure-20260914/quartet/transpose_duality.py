"""Exact hidden exchange-sign duality and an additional 80 -> 40 reduction.

This is a finite internal spectral reflection, NOT physical spacetime chirality.
The self-conjugate Specht shape (4^4) has a tableau-transpose involution J with
J S_ij J=-S_ij. Every graph automorphism is even, hence [J,G]=0. Moreover every
g in G has an explicit odd centralizer, which forces tr(J rho(g))=0. Therefore
all 18 multiplicity blocks split equally into J+ and J- and their off-diagonal
exchange operators are square, largest 131. Their squared singular-value
problems are at most 131x131; the leading H0 itself remains twice this size.
"""
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib, json, math
import numpy as np
import sympy as sy
from checker import tableaux, graph, Young

HERE=Path(__file__).resolve().parent
checks=0
def need(x,message):
    global checks
    checks+=1
    if not bool(x):
        raise RuntimeError(message)
def parity(pi):
    return (-1)**sum(pi[i]>pi[j] for i,j in combinations(range(len(pi)),2))
def cycles(pi):
    result=[];seen=set()
    for i in range(len(pi)):
        if i in seen:
            continue
        c=[];j=i
        while j not in seen:
            c.append(j);seen.add(j);j=pi[j]
        result.append(c)
    return result
def odd_centralizer(g):
    cs=cycles(g);h=list(range(len(g)))
    even=[c for c in cs if len(c)%2==0]
    if even:
        c=even[0]
        for i,x in enumerate(c):
            h[x]=c[(i+1)%len(c)]
    else:
        pair=next(((a,b) for a,b in combinations(cs,2) if len(a)==len(b)),None)
        need(pair is not None,'odd centralizer exists from repeated odd cycle')
        a,b=pair
        for x,y in zip(a,b):
            h[x]=y;h[y]=x
    return tuple(h)

tabs=tableaux();lookup={t:i for i,t in enumerate(tabs)}
trans=np.array([lookup[tuple((c,r) for r,c in t)] for t in tabs])
eta=np.array([parity([4*r+c for r,c in t]) for t in tabs],dtype=np.int64)
need(np.array_equal(trans[trans],np.arange(len(tabs))),'tableau transpose involution')
need(np.array_equal(eta*eta[trans],np.ones(len(tabs),dtype=np.int64)),'J squared is plus I')
for k in range(15):
    dist=np.array([t[k+1][1]-t[k+1][0]-t[k][1]+t[k][0] for t in tabs])
    need(np.array_equal(dist[trans],-dist),'diagonal part anticommutes with J')
    for i,t in enumerate(tabs):
        if abs(dist[i])==1:
            continue
        other=list(t);other[k],other[k+1]=other[k+1],other[k]
        j=lookup[tuple(other)]
        need(eta[i]==-eta[j],'off diagonal signs anticommute with J')
        tt=list(tabs[trans[i]]);tt[k],tt[k+1]=tt[k+1],tt[k]
        need(lookup[tuple(tt)]==trans[j],'transpose commutes with tableau relabelling')
_,_,aut=graph();all_even=0;centralizer_count=0
for sigma in permutations(range(5)):
    for flips in product((-1,1),repeat=5):
        if math.prod(flips)!=1:
            continue
        g=aut(sigma,flips);h=odd_centralizer(g)
        need(parity(g)==1,'graph automorphism lies in A16');all_even+=1
        need(parity(h)==-1,'constructed centralizer is odd')
        need(tuple(g[h[i]] for i in range(16))==tuple(h[g[i]] for i in range(16)),
             'constructed odd permutation centralizes graph automorphism')
        centralizer_count+=1
little=json.loads((HERE/'little_group_reduction.json').read_text())
halves=[]
for row in little['blocks']:
    n=row['multiplicity_block_dimension'];need(n%2==0,'equal multiplicities of J signs')
    halves.append(n//2)

saved=np.load(HERE/'basis_float.npz');basis=saved['basis'];H=saved['block']
JB=eta[:,None]*basis[trans]
J80=basis.T@JB
need(np.linalg.norm(JB-basis@J80)<1e-9,'numerical standard-space J invariance')
jv,jq=np.linalg.eigh((J80+J80.T)/2)
need(np.count_nonzero(jv<0)==40 and np.max(abs(abs(jv)-1))<1e-10,'standard split 40 plus 40')
Xm=jq.T@(2*H-40*np.eye(80))@jq
C=Xm[:40,40:]
diag_error=float(np.linalg.norm(Xm[:40,:40])+np.linalg.norm(Xm[40:,40:]))
need(diag_error<1e-9,'X is off diagonal in J basis')
singular=np.linalg.svd(C,compute_uv=False)
energies=np.sort(np.concatenate((20-singular/2,20+singular/2)))
need(np.max(abs(energies-np.linalg.eigvalsh(H)))<1e-10,'40 singular values recover 80 energies')
poly=json.loads((HERE/'exact_polynomial.json').read_text())
coefs=poly['integer_coefficients_descending'];need(all(c==0 for c in coefs[1::2]),'exact characteristic polynomial even')
qcoefs=coefs[::2];x=sy.Symbol('x');q=sy.Poly.from_list(qcoefs,x)
need(sy.gcd(q,q.diff()).degree()==0,'40-square polynomial simple')
need(q.count_roots(sy.S.NegativeInfinity,0)==0,'40-square polynomial has no nonpositive roots')
result={'checks':checks,'tableau_transpose_J_squared':1,
    'exact_anticommutation_all_adjacent_generators':True,
    'even_graph_automorphisms_verified':all_even,
    'explicit_odd_centralizers_verified':centralizer_count,
    'all_multiplicity_blocks_equal_J_sign_dimensions':True,
    'squared_block_dimensions':halves,'largest_squared_block_dimension':max(halves),
    'sum_squared_block_dimensions':sum(halves),
    'standard_off_diagonal_shape':[40,40],
    'standard_off_diagonal_C':C.tolist(),
    'standard_off_diagonal_error':diag_error,
    'standard_squared_characteristic_coefficients_descending':qcoefs,
    'spectral_reflection':'E maps to 40-E for H0 only',
    'physical_chirality_derived':False,'applies_unmodified_to_F4_corrected_H':False,
    'global_spectral_order_certified':False,
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'transpose_duality.json').write_text(json.dumps(result,indent=2)+'\n')
print('EXACT J DUALITY; largest squared singlet block',max(halves),'checks',checks)
