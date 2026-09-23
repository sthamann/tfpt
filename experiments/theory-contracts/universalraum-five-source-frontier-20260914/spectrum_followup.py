"""v1.4: independent C16 singlet, local F4 star-square factorization and genuine
rediagonalisation of the truncated local H2+H4. Derived from our v1.3 checker.
No exact eigenvalue enclosure and no full all-order microscopic spectrum.
"""
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import LinearOperator, eigsh
from scipy.sparse.csgraph import reverse_cuthill_mckee
from itertools import product, combinations
import json, time, hashlib
from pathlib import Path

start=time.time()
vertices=[x for x in product((-1,1),repeat=5) if np.prod(x)==1]
raw=[(i,j) for i,j in combinations(range(16),2) if sum(a!=b for a,b in zip(vertices[i],vertices[j]))==4]
adj=np.zeros((16,16))
for i,j in raw:adj[i,j]=adj[j,i]=1
perm=reverse_cuthill_mckee(csr_matrix(adj),symmetric_mode=True)
pos={int(p):k for k,p in enumerate(perm)}
paired=sorted((tuple(sorted((pos[i],pos[j]))),tuple(a+b for a,b in zip(vertices[i],vertices[j]))) for i,j in raw)
edges=[e for e,r in paired];labels=[r for e,r in paired]
tabs=[];fill=[0]*4;cur=[]
def rec():
    if len(cur)==16:tabs.append(tuple(cur));return
    for r in range(4):
        c=fill[r]
        if c<4 and (r==0 or fill[r-1]>c):
            fill[r]+=1;cur.append((r,c));rec();cur.pop();fill[r]-=1
rec()
d=len(tabs)
if d!=24024:raise RuntimeError("wrong Specht dimension")
index={x:i for i,x in enumerate(tabs)}
mats=[]
for k in range(15):
    rows=[];cols=[];data=[]
    for i,tab in enumerate(tabs):
        r1,c1=tab[k];r2,c2=tab[k+1];dist=c2-r2-c1+r1
        rows.append(i);cols.append(i);data.append(1/dist)
        if abs(dist)>1:
            other=list(tab);other[k],other[k+1]=other[k+1],other[k]
            rows.append(index[tuple(other)]);cols.append(i);data.append(np.sqrt(1-1/dist**2))
    mats.append(csr_matrix((data,(rows,cols)),shape=(d,d)))
def swap(v,e):
    i,j=sorted(e)
    chain=list(range(i,j-1))+[j-1]+list(range(i,j-1))[::-1]
    w=v
    for k in chain:w=mats[k]@w
    return w
def E(v,e):return v-swap(v,e)
def hv(v):
    v=np.asarray(v).reshape(d)
    out=20*v.copy()
    for e in edges:out+=.5*swap(v,e)
    return out
op=LinearOperator((d,d),matvec=hv,dtype=float)
print("constructed full 24024-dimensional singlet operator",flush=True)
vals,vec=eigsh(op,k=12,which="SA",ncv=80,tol=1e-12,maxiter=30000,
               v0=np.random.default_rng(20260914).normal(size=d))
order=np.argsort(vals);vals=vals[order];vec=vec[:,order]
res=[float(np.linalg.norm(hv(vec[:,i])-vals[i]*vec[:,i])) for i in range(12)]
if max(res)>1e-8:raise RuntimeError("singlet residual")
if np.count_nonzero(abs(vals-vals[1])<1e-8)!=4:raise RuntimeError("not four detected modes")
print("singlet levels obtained; applying all F4 path classes",flush=True)
v=vec[:,:5];out=np.zeros_like(v)
for e in edges:out+=2*E(v,e)
for k,e in enumerate(edges):
    for l in range(k+1,len(edges)):
        f=edges[l]
        if set(e)&set(f):out+=E(E(v,e),f)+E(E(v,f),e)
        elif labels[k]==labels[l]:
            w=swap(swap(v,(e[0],f[0])),(e[1],f[1]))
            out-=2*E(E(w,e),f)
proj=v.T@out
if np.linalg.norm(proj-proj.T)>1e-7:raise RuntimeError("F4 Hermiticity")
f0=float(proj[0,0]);exc=np.linalg.eigvalsh(proj[1:5,1:5])
coef=(exc-f0)/2
incident=[[e for e in edges if i in e] for i in range(16)]
def local_f4(v):
    w=np.asarray(v)
    out=np.zeros_like(w)
    for es in incident:
        a=sum((E(w,e) for e in es),np.zeros_like(w))
        out+=sum((E(a,e) for e in es),np.zeros_like(w))-a
    return out
local=local_f4(v)
direct=np.zeros_like(v)
for e in edges:direct+=2*E(v,e)
for e,f in combinations(edges,2):
    if set(e)&set(f):direct+=E(E(v,e),f)+E(E(v,f),e)
factor_error=float(np.linalg.norm(local-direct))
if factor_error>1e-9:raise RuntimeError("local star-square factorization")
pl=v.T@local;l0=float(pl[0,0]);le=np.linalg.eigvalsh(pl[1:,1:])
print("local F4 star-square factorization checked; diagonalising full truncated operator",flush=True)
def corrected(x):return hv(x)+.00125*local_f4(np.asarray(x).reshape(d))
lc,vc=eigsh(LinearOperator((d,d),matvec=corrected,dtype=float),k=8,which="SA",ncv=64,
             tol=1e-11,maxiter=10000,v0=np.random.default_rng(141414).normal(size=d))
idx=np.argsort(lc);lc=lc[idx];vc=vc[:,idx]
rc=[float(np.linalg.norm(corrected(vc[:,i])-lc[i]*vc[:,i])) for i in range(8)]
if max(rc)>1e-7:raise RuntimeError("corrected singlet residual")
ns=12.133537149348086
def bound(h):return h+.00125*(h*h-76*h+1440)
result={
 "dimension":d,"levels":vals.tolist(),"residuals":res,
 "F4_ground":f0,"F4_first_detected_four":exc.tolist(),
 "gap_epsilon2_coefficients":coef.tolist(),
 "gap_corrected_first_order_epsilon_1_20":(vals[1]-vals[0]+coef*.0025).tolist(),
 "comparison_ground_error":abs(f0-555.488500363836),
 "comparison_excited_max_error":float(np.max(abs(exc-583.29203866638))),
 "full_non_singlet_comparison":False,"exact_multiplicity_upper_bound":False,
 "higher_order_bound":False,"CAR_native_phase_equivalence":False,
 "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 "local_F4_ground":l0,"local_F4_first_detected_four":le.tolist(),
 "local_gap_epsilon2_coefficients":((le-l0)/2).tolist(),
 "local_factorization_error":factor_error,
 "local_truncated_rediagonalised_levels":lc.tolist(),"local_truncated_residuals":rc,
 "local_truncated_gap":float(lc[1]-lc[0]),
 "local_non_singlet_lower_bound_conditional_on_bare_minimum":bound(ns),
 "local_quartet_variational_upper_bound":float(vals[1]+.00125*max(le)),
 "bare_source_minimum_is_certified":False,
 "seconds":time.time()-start}
if result["comparison_ground_error"]>1e-6 or result["comparison_excited_max_error"]>1e-6:
    raise RuntimeError("submitted F4 spectrum not reproduced: "+str(result))
Path(__file__).with_name("spectrum_followup.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2),flush=True)
