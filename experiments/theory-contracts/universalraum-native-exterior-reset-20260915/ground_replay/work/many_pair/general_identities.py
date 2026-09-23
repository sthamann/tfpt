"""Exact identities valid on the full native fermion/boson Fock space."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
import json,hashlib,sys,math
import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix,csr_matrix,eye
sys.path.insert(0,str(Path(__file__).parent.resolve()))
import full_n4 as m
checks=[]
def need(c,s):
    if not c:raise RuntimeError(s)
    checks.append(s)
def spin_generators(n):
    dim=2**n;ann=[]
    for j in range(n):
        a=np.zeros((dim,dim),complex)
        for mask in range(dim):
            if mask>>j&1:a[mask^(1<<j),mask]=(-1)**((mask&((1<<j)-1)).bit_count())
        ann.append(a)
    gam=[a+a.T for a in ann]+[1j*(a.T-a) for a in ann]
    even=[i for i in range(dim) if i.bit_count()%2==0]
    # These are twice the anti-Hermitian Lie generators.
    return [(gam[a]@gam[b])[np.ix_(even,even)] for a,b in combinations(range(2*n),2)]
Gs=spin_generators(5);Gc=spin_generators(3)
need(np.array_equal(-sum(x@x for x in Gs),45*np.eye(16)),'single spinor Casimir 45/4')
need(np.array_equal(-sum(x@x for x in Gc),15*np.eye(4)),'single color Casimir 15/4')
pairs=list(combinations(range(64),2));pair_index={p:i for i,p in enumerate(pairs)}
def exterior_square(X):
    entries=[];lookup=[[(int(i),X[i,j]) for i in np.flatnonzero(X[:,j])] for j in range(64)]
    for k,(u,v) in enumerate(pairs):
        for i,x in lookup[u]:
            if i!=v:entries.append((pair_index[tuple(sorted((i,v)))],k,x*(1 if i<v else -1)))
        for i,x in lookup[v]:
            if i!=u:entries.append((pair_index[tuple(sorted((u,i)))],k,x*(1 if u<i else -1)))
    return coo_matrix(([v for i,j,v in entries],([i for i,j,v in entries],[j for i,j,v in entries])),shape=(2016,2016)).tocsr()
casimirs=[]
for generators in [[np.kron(x,np.eye(4)) for x in Gs],[np.kron(np.eye(16),x) for x in Gc]]:
    total=csr_matrix((2016,2016),dtype=complex)
    for X in generators:
        L=exterior_square(X);total=total-L@L
    total.eliminate_zeros();casimirs.append(total)
W=csr_matrix(m.m.W);residual=8*(W.T@W)+sum(casimirs)-120*eye(2016);residual.eliminate_zeros()
need(residual.nnz==0,'complete exact two-body Casimir identity, not merely selected irreps')

# Complete additive number-conservation space, not guessed local charges.
equations=[]
for pair,(a,sign) in m.m.couple.items():
    row=np.zeros(124,dtype=np.int64);row[pair[0]]=row[pair[1]]=1;row[64+a]=-1;equations.append(row)
A=np.array(equations);Q=np.vstack([np.column_stack([m.roots.T,m.broot.T]),np.r_[np.ones(64,dtype=int),2*np.ones(60,dtype=int)]])
need(np.array_equal(A@Q.T,np.zeros((480,9))), 'eight Cartan charges and total pair number conserved')
need(sp.Matrix(Q).rank()==9,'nine explicit rational conserved charges independent')
binary=(A%2).astype(np.uint8);rank=0;pivots=[]
for col in range(124):
    found=np.flatnonzero(binary[rank:,col])
    if not len(found):continue
    j=rank+int(found[0]);binary[[rank,j]]=binary[[j,rank]]
    for j in range(rank+1,len(binary)):
        if binary[j,col]:binary[j]^=binary[rank]
    rank+=1;pivots.append(col)
need(rank==115,'mod-two lower rank plus nine rational nullvectors proves exact rational rank 115')
not_local=[]
for s in range(16):
    desired=[int(u//4==s) for u in range(64)]
    added=sp.Matrix(np.vstack([Q[:,:64],desired])).rank()
    need(added==10,'one spinor-place occupation cannot extend to an additive native conserved charge')
    not_local.append(s)

# All numbers of identical mediators: native Cartan extremality isolates an
# eight-pair quasispin system, with no imposed vertex Gauss charges.
root_channels=[]
for a in range(60):
    occupied=set(x for u,v,s in m.m.decay[a] for x in (u,v))
    need(len(occupied)==16 and len(m.m.decay[a])==8,'eight disjoint fermion pairs per mediator')
    allowed=[(u,v,r) for (u,v),(r,s) in m.m.couple.items() if u in occupied and v in occupied]
    need(len(allowed)==8 and all(r==a for u,v,r in allowed),'no other mediator channel acts within extremal fermion support')
    fcharges=m.roots@m.broot[a];bcharges=m.broot@m.broot[a]
    need(max(fcharges)==4 and max(bcharges)==8,'Cartan bounds per fermion and mediator')
    need(set(np.flatnonzero(fcharges==4))==occupied and list(np.flatnonzero(bcharges==8))==[a],'equality selects exactly the extremal native channel')
    root_channels.append({'mediator':a,'pair_slots':8})

# Exact verification that the five two-mediator seeds occupy the claimed
# irreducible summands of Sym^2(C10 tensor C6).
J10=np.block([[np.zeros((5,5)),np.eye(5)],[np.eye(5),np.zeros((5,5))]])
J6=np.zeros((6,6))
for a,s in enumerate([1,-1,1,1,-1,1]):J6[a,5-a]=s
seeds={'54_20':{(0,0):1},'54_1':{(a,5-a):s for a,s in enumerate([1,-1,1])},'1_20':{(6*j,6*(j+5)):1 for j in range(5)},'1_1':{(6*j+a,6*(j+5)+5-a):[1,-1,1,1,-1,1][a] for j in range(5) for a in range(6)},'45_15':{(0,7):1,(1,6):-1}}
for name,seed in seeds.items():
    T=np.zeros((60,60))
    for (a,b),c in seed.items():
        if a==b:T[a,a]+=c
        else:T[a,b]+=c/2;T[b,a]+=c/2
    T=T.reshape(10,6,10,6);swapped=T.transpose(2,1,0,3)
    need(np.array_equal(swapped,(-1 if name=='45_15' else 1)*T),'exact spin/color exchange irrep sign')
    ts=np.einsum('ij,iajb->ab',J10,T);tc=np.einsum('ab,iajb->ij',J6,T)
    if name.startswith('1_'):need(np.array_equal(10*T,np.einsum('ij,ab->iajb',J10,ts)),'pure spin trace')
    else:need(np.count_nonzero(ts)==0,'spin tracelessness')
    if name.endswith('_1'):need(np.array_equal(6*T,np.einsum('ij,ab->iajb',tc,J6)),'pure color trace')
    else:need(np.count_nonzero(tc)==0,'color tracelessness')

result={'checks_passed':len(checks),'checks':checks,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'full_Fock_Casimir_identity':{'formula':'sum_A P_A†P_A = (15 N_f - C_Spin10 - C_SU4)/2','normalization':{'Spin10_fundamental_vector':9,'Spin10_spinor':str(F(45,4)),'SU4_fundamental':str(F(15,4)),'SU4_antisymmetric_six':5},'proof':'exact identity on all 2016 two-fermion states, then second quantization of a two-body operator; holds in every fermion-number sector','operator_norm':480,'norm_attained':'unique completely occupied 64-fermion state','leading_effective_Hamiltonian':'-g^2/(2 Delta) (15 N_f - C_Spin10 - C_SU4); this expression is second order, not the exact eliminated microscopic dynamics'},
 'linear_conservation':{'reaction_matrix_shape':[480,124],'exact_rational_rank':115,'dimension':9,'basis':'eight Cartan charges and N_f+2 N_b','all_sixteen_vertex_number_extensions_fail':True,'scope':'charges linear in number operators; no assertion that all nonlinear conserved observables have been classified'},
 'identical_mediator_all_n':{'proved_for_all_root_channels':60,'basis':'k converted pairs, k=0,...,min(n,8)','matrix_dimension':'min(n,8)+1','diagonal':'Delta (n-k)','offdiagonal':'g sqrt((n-k)(k+1)(8-k))','proof':'Cartan extremality restricts to one mediator and sixteen fermion modes; eight disjoint pair slots form quasispin j=4; initial all-mediator state selects the symmetric j=4 ladder','scope':'all numbers n in the cyclic space from n identical root mediators, not all states at total pair number n'},
 'stability':{'one_cell_lower_bound':'H >= -480 g^2/Delta','n_local_banks_lower_bound':'H >= -480 L g^2/delta if the bosonic one-particle operator is >= delta I','proof':'complete the positive boson square and use the exact fermionic Casimir norm 480; each bank has 64 fermionic modes','self_adjointness':'finite-mode bosons with bounded fermion coefficients give relative bound zero with respect to positive harmonic-oscillator energy; finite-particle core is essentially self-adjoint','not_proved':'a selected infinite spatial geometry or a uniform interacting relativistic limit'}}
Path('outputs/many_pair/general_identities.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['checks_passed','full_Fock_Casimir_identity','linear_conservation']},indent=2))
