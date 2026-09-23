"""Independent C16 quartet reduction in characteristic zero and a finite field.

The exact target space is Im P_T(P_{S4}-P_{S5}) in S^(4,4,4,4).
It contains one copy of each S5-standard multiplicity, dimension 80.
No 24024-square matrix is constructed. No full physical spectral claim.
"""
from __future__ import annotations
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import argparse, hashlib, json, math, time
import numpy as np
import sympy as sy
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import reverse_cuthill_mckee

HERE = Path(__file__).resolve().parent
START = time.time()
CHECKS = 0

def require(test, message):
    global CHECKS
    CHECKS += 1
    if not bool(test):
        raise RuntimeError(message)

@lru_cache(None)
def partitions(n, maximum=16):
    if n == 0:
        return ((),)
    return tuple((k,) + p for k in range(min(n, maximum), 0, -1)
                 for p in partitions(n-k, k))

@lru_cache(None)
def char(shape, cycles):
    if not cycles:
        return int(not shape)
    k, rest = cycles[0], cycles[1:]
    answer = 0
    for mu in partitions(sum(shape)-k):
        if len(mu)>len(shape) or any(x>shape[i] for i,x in enumerate(mu)):
            continue
        cells = {(r,c) for r,a in enumerate(shape)
                 for c in range(mu[r] if r<len(mu) else 0, a)}
        if not cells:
            continue
        reached = {next(iter(cells))}
        while True:
            grow = reached | {z for r,c in reached
                for z in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)) if z in cells}
            if grow == reached:
                break
            reached = grow
        if reached != cells:
            continue
        if any({(r,c),(r+1,c),(r,c+1),(r+1,c+1)}<=cells for r,c in cells):
            continue
        answer += (-1)**(len({r for r,c in cells})-1)*char(mu,rest)
    return answer

def cycle_type(pi):
    seen=set(); lengths=[]
    for i in range(len(pi)):
        if i in seen:
            continue
        j=i; n=0
        while j not in seen:
            seen.add(j); n+=1; j=pi[j]
        lengths.append(n)
    return tuple(sorted(lengths,reverse=True))

def graph():
    raw_vertices = [x for x in product((-1,1),repeat=5) if math.prod(x)==1]
    raw_edges = [(i,j) for i,j in combinations(range(16),2)
                 if sum(a!=b for a,b in zip(raw_vertices[i],raw_vertices[j]))==4]
    adj=np.zeros((16,16),dtype=int)
    for i,j in raw_edges:
        adj[i,j]=adj[j,i]=1
    rcm=reverse_cuthill_mckee(csr_matrix(adj),symmetric_mode=True)
    vertices=[raw_vertices[int(i)] for i in rcm]
    index={x:i for i,x in enumerate(vertices)}
    edges=[(i,j) for i,j in combinations(range(16),2)
           if sum(a!=b for a,b in zip(vertices[i],vertices[j]))==4]
    def aut(sigma=tuple(range(5)), flips=(1,)*5):
        return tuple(index[tuple(flips[m]*v[sigma[m]] for m in range(5))] for v in vertices)
    return vertices,edges,aut

def exact_characters(aut):
    flips=[x for x in product((-1,1),repeat=5) if math.prod(x)==1]
    totals=Counter(); classes=Counter()
    for sigma in permutations(range(5)):
        for f in flips:
            c=cycle_type(aut(sigma,f)); value=char((4,4,4,4),c)
            totals['S5']+=value; classes[str(c)]+=1
            if sigma[4]==4:
                totals['S4']+=value
            if sigma==tuple(range(5)):
                totals['T']+=value
    require(totals['T']%16==0,'translation character integrality')
    require(totals['S4']%384==0,'S4 character integrality')
    require(totals['S5']%1920==0,'S5 character integrality')
    dT=totals['T']//16; d4=totals['S4']//384; d5=totals['S5']//1920
    require(dT==1764 and d4-d5==80,'exact character dimensions')
    require(char((4,4,4,4),(1,)*16)==24024,'identity character')
    return {'translation_dimension':dT,'translation_S4_fixed_dimension':d4,
            'translation_S5_fixed_dimension':d5,'standard_multiplicity':d4-d5,
            'automorphism_cycle_census':dict(classes)}

def tableaux():
    tabs=[]; counts=[0]*4; cur=[]
    def rec():
        if len(cur)==16:
            tabs.append(tuple(cur)); return
        for r in range(4):
            c=counts[r]
            if c<4 and (r==0 or counts[r-1]>c):
                counts[r]+=1;cur.append((r,c));rec();cur.pop();counts[r]-=1
    rec()
    return tabs

def word(pi):
    """Adjacent swaps acting in written order; the final permutation is pi."""
    current=list(range(len(pi))); ans=[]
    inverse=[pi.index(i) for i in range(len(pi))]
    for i in range(len(pi)):
        j=current.index(inverse[i])
        while j>i:
            current[j-1],current[j]=current[j],current[j-1]
            ans.append(j-1);j-=1
    check=list(range(len(pi)))
    for k in ans:
        check=[k+1 if z==k else k if z==k+1 else z for z in check]
    require(check==list(pi),'permutation word convention')
    return ans

class Young:
    def __init__(self,tabs,prime):
        self.prime=prime;self.d=len(tabs);self.diag=[];self.off=[];self.indices=[]
        self.operations=0
        lookup={x:i for i,x in enumerate(tabs)}
        for k in range(15):
            dist=[];partner=[]
            for i,tab in enumerate(tabs):
                r,c=tab[k];R,C=tab[k+1]; z=C-R-c+r;dist.append(z)
                if abs(z)==1:
                    partner.append(i)
                else:
                    swapped=list(tab);swapped[k],swapped[k+1]=swapped[k+1],swapped[k]
                    partner.append(lookup[tuple(swapped)])
            dist=np.array(dist,dtype=np.int64); partner=np.array(partner)
            if prime:
                diagonal=np.array([pow(int(z)%prime,-1,prime) for z in dist],dtype=np.int64)
                # Output row receives coefficient 1 - 1/d from the swapped column.
                off=(1-diagonal)%prime;off[abs(dist)==1]=0
            else:
                diagonal=1/dist.astype(float);off=np.sqrt(1-diagonal**2)
            self.diag.append(diagonal);self.off.append(off);self.indices.append(partner)
    def adjacent(self,v,k):
        self.operations+=1
        out=self.diag[k][:,None]*v+self.off[k][:,None]*v[self.indices[k]]
        return out%self.prime if self.prime else out
    def apply(self,v,w):
        for k in w:
            v=self.adjacent(v,k)
        return v
    def divide(self,v,n):
        return v*pow(n,-1,self.prime)%self.prime if self.prime else v/n

def projectors(young,aut):
    translation=[]
    for k in range(4):
        f=[1]*5;f[k]=f[4]=-1;translation.append(word(aut(flips=tuple(f))))
    swaps={}
    for i,j in combinations(range(5),2):
        sigma=list(range(5));sigma[i],sigma[j]=sigma[j],sigma[i]
        swaps[i,j]=word(aut(tuple(sigma)))
    def PT(v):
        for w in translation:
            v=young.divide(v+young.apply(v,w),2)
        return v
    def extend(v,n):
        out=v.copy()
        for i in range(n-1):
            out+=young.apply(v,swaps[i,n-1])
        return young.divide(out,n)
    def P4(v):
        for n in (2,3,4):
            v=extend(v,n)
        return v
    def target(v):
        v=P4(PT(v))
        v=v-extend(v,5)
        return v%young.prime if young.prime else v
    return target,PT,P4,lambda v:extend(v,5),translation,swaps

def modular_inverse(matrix,p):
    n=matrix.shape[0];a=np.concatenate((matrix.copy()%p,np.eye(n,dtype=np.int64)),axis=1)
    for k in range(n):
        candidates=np.flatnonzero(a[k:,k]);require(len(candidates)>0,'invertible pivot')
        j=k+int(candidates[0]);a[[k,j]]=a[[j,k]]
        a[k]=a[k]*pow(int(a[k,k]),-1,p)%p
        factors=a[:,k].copy();factors[k]=0
        a=(a-factors[:,None]*a[k])%p
    require(np.array_equal(a[:,:n],np.eye(n,dtype=np.int64)),'modular inverse')
    return a[:,n:]

def pivot_rows(w,p):
    # Rank-revealing column elimination on W^T. All arithmetic exact modulo p.
    a=w.T.copy(); n=a.shape[0]; pivots=[];row=0
    for j in range(a.shape[1]):
        ix=np.flatnonzero(a[row:,j])
        if not len(ix):
            continue
        k=row+int(ix[0]);a[[row,k]]=a[[k,row]]
        a[row]=a[row]*pow(int(a[row,j]),-1,p)%p
        factors=a[:,j].copy();factors[row]=0
        a=(a-factors[:,None]*a[row])%p
        pivots.append(j);row+=1
        if row==n:
            return pivots
    raise RuntimeError('projected random vectors did not have full rank')

def characteristic_mod(a,p):
    # Newton identities use traces and division only by 1,...,80; p>80.
    n=len(a); power=np.eye(n,dtype=np.int64);traces=[];coefs=[1]
    for k in range(1,n+1):
        power=power@a%p;traces.append(int(np.trace(power)%p))
        value=-sum(coefs[k-i]*traces[i-1] for i in range(1,k+1))
        coefs.append(value*pow(k,-1,p)%p)
    x=sy.Symbol('x');poly=sy.Poly.from_list(coefs,x,modulus=p)
    gcd=sy.gcd(poly,poly.diff())
    # Independent Cayley-Hamilton and determinant evaluations.
    value=np.eye(n,dtype=np.int64)
    for c in coefs[1:]:
        value=(value@a+c*np.eye(n,dtype=np.int64))%p
    require(np.count_nonzero(value)==0,'Cayley-Hamilton residue')
    return {'coefficients_descending':coefs,'gcd_with_derivative_degree':gcd.degree(),
            'gcd_coefficients_descending':[int(x)%p for x in gcd.all_coeffs()],
            'factor_degrees_and_multiplicities':[(f.degree(),int(e)) for f,e in sy.factor_list(poly)[1]]}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--prime',type=int,default=65521)
    parser.add_argument('--floating',action='store_true');parser.add_argument('--characters-only',action='store_true')
    parser.add_argument('--no-basis',action='store_true')
    args=parser.parse_args()
    vertices,edges,aut=graph();exact=exact_characters(aut)
    print('exact character reduction',exact,flush=True)
    if args.characters_only:
        (HERE/'characters.json').write_text(json.dumps(exact,indent=2)+'\n');return
    p=None if args.floating else args.prime
    if p:
        require(sy.isprime(p) and 80<p<100000000,'safe modulus; 80*(p-1)^2 < 8e17')
    young=Young(tableaux(),p);require(young.d==24024,'tableaux dimension')
    target,PT,P4,P5step,translation,swaps=projectors(young,aut)
    rng=np.random.default_rng(202609141)
    probe=rng.integers(0,p,size=(young.d,2),dtype=np.int64) if p else rng.normal(size=(young.d,2))
    def eq(a,b):
        return np.array_equal(a%p,b%p) if p else np.linalg.norm(a-b)<1e-9
    for i in range(15):
        require(eq(young.adjacent(young.adjacent(probe,i),i),probe),'Coxeter involution')
    for i in range(14):
        require(eq(young.apply(probe,[i,i+1,i]),young.apply(probe,[i+1,i,i+1])),'Coxeter braid')
    for i,j in combinations(range(15),2):
        if j-i>1:
            require(eq(young.apply(probe,[i,j]),young.apply(probe,[j,i])),'Coxeter distant')
    print('Young matrices and Coxeter checks ready',time.time()-START,flush=True)
    raw=rng.integers(0,p,size=(young.d,80),dtype=np.int64) if p else rng.normal(size=(young.d,84))
    w=target(raw)
    print('projected random range',time.time()-START,flush=True)
    if p:
        pivots=pivot_rows(w,p);inv=modular_inverse(w[pivots],p)
        require(len(pivots)==80,'80 independent exact projected columns')
        basis=w
    else:
        q,s,_=np.linalg.svd(w,full_matrices=False)
        require(s[79]>1e-4 and s[80]<1e-10,'numerical projector rank is 80')
        basis=q[:,:80];pivots=None
    # Exact fixed-vector and standard-subtraction membership on the entire basis.
    for tw in translation:
        require(eq(young.apply(basis,tw),basis),'translation invariance of all basis vectors')
    for i in range(3):
        require(eq(young.apply(basis,swaps[i,i+1]),basis),'S4 invariance of all basis vectors')
    require(eq(P5step(basis),np.zeros_like(basis)),'zero S5-invariant component')
    print('full basis symmetry certified',time.time()-START,flush=True)
    def exchange(v):
        out=np.zeros_like(v)
        for i,j in edges:
            pi=list(range(16));pi[i],pi[j]=pi[j],pi[i]
            out+=young.apply(v,word(tuple(pi)))
        return out%p if p else out
    hb=exchange(basis)
    if p:
        a=inv@hb[pivots]%p
        # 80 term products < 8e17 safely fit signed int64.
        defect=(hb-basis@a)%p
        require(np.count_nonzero(defect)==0,'exact invariant block intertwining')
        poly=characteristic_mod(a,p)
        result={'prime':p,'exact_character_dimensions':exact,'block_shape':[80,80],
                'operator':'X=sum_40_edges S_e; H0=(40 I+X)/2',
                'full_exact_intertwining_nonzero_entries':int(np.count_nonzero(defect)),
                'pivot_rows':pivots,'X80_mod_p':a.tolist(),'characteristic':poly,
                'eigenvalues_simple_inside_standard_block':poly['gcd_with_derivative_degree']==0,
                'global_spectral_order_certified':False}
        if not args.no_basis:
            np.savez_compressed(HERE/f'basis_mod_{p}.npz',basis=basis,pivot_rows=np.array(pivots),block=a)
        out=HERE/f'modular_{p}.json'
    else:
        a=basis.T@hb
        symmetric_error=float(np.linalg.norm(a-a.T));a=(a+a.T)/2
        values,z=np.linalg.eigh((40*np.eye(80)+a)/2)
        block_defect=hb-basis@a
        individual=np.linalg.norm(block_defect@z/2,axis=0)
        require(np.max(individual)<1e-8,'80 block residuals')
        result={'exact_character_dimensions':exact,'block_shape':[80,80],
                'operator':'H0=sum_40_edges (I+S_e)/2','H80':((40*np.eye(80)+a)/2).tolist(),
                'all_80_eigenvalues':values.tolist(),'all_80_residuals':individual.tolist(),
                'block_intertwining_frobenius':float(np.linalg.norm(block_defect)),
                'symmetry_error':symmetric_error,'projector_singular_values':s.tolist(),
                'global_spectral_order_certified':False}
        np.savez_compressed(HERE/'basis_float.npz',basis=basis,block=(40*np.eye(80)+a)/2)
        out=HERE/'floating.json'
    result.update({'checks':CHECKS,'seconds':time.time()-START,'adjacent_applications':young.operations,
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('complete',out,'seconds',result['seconds'],flush=True)
    if p:
        print('gcd degree',result['characteristic']['gcd_with_derivative_degree'],flush=True)
    else:
        print('lowest block eigenvalues',values[:12],flush=True)

if __name__=='__main__':
    main()
