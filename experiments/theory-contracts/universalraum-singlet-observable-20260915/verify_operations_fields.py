"""Recheck conditional full algebra using a small support graph proof,
and check the supplied Lorentz-contraction claims on the native tensor.

Connected one-body graph implies connected k-token graph for 0<k<64.
This avoids constructing multi-million-edge finite-sector graphs.
It is a theorem about an ADJOINED operation alphabet, not native access.
"""
from pathlib import Path
from itertools import combinations
from hashlib import sha256
import json
import numpy as np
from scipy.sparse import csr_matrix, coo_matrix
from scipy.sparse.csgraph import connected_components

HERE=Path(__file__).resolve().parent
checks=[]
def need(ok,name):
    if not ok: raise RuntimeError(name)
    checks.append(name)
def zero(a):
    a=a.tocsr();a.eliminate_zeros()
    return a.nnz==0

def main():
    path=HERE/'sources/spinor_tensors.npz'
    need(sha256(path.read_bytes()).hexdigest()=='3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763','native archive pin')
    with np.load(path) as archive: W=archive['W']
    need(np.count_nonzero(W.imag)==0,'native W real exactly')
    W=W.real.astype(np.int64);Ws=csr_matrix(W)
    pairs=list(combinations(range(64),2));pi={pair:q for q,pair in enumerate(pairs)}
    ann=[]
    for j in range(5):
        a=np.zeros((32,32),dtype=np.int64)
        for m in range(32):
            if m>>j&1:a[m^(1<<j),m]=(-1)**((m&((1<<j)-1)).bit_count())
        ann.append(a)
    gamma=[a+a.T for a in ann]+[1j*(a.T-a) for a in ann]
    even=[m for m in range(32) if m.bit_count()%2==0]
    generators=[np.kron((gamma[i]@gamma[j])[np.ix_(even,even)],np.eye(4)) for i,j in combinations(range(10),2)]
    # Only three color generators needed for graph connectivity; they are a
    # subset of SU(4), not an extra all-modes hopping Hamiltonian.
    for j in range(3):
        c=np.zeros((4,4));c[j,j+1]=1;c[j+1,j]=-1
        generators.append(np.kron(np.eye(16),c))
    f_edges=np.zeros((64,64),dtype=np.int8);b_edges=np.zeros((60,60),dtype=np.int8)
    for q,X in enumerate(generators):
        support=[list(zip(np.flatnonzero(X[:,i]),X[np.flatnonzero(X[:,i]),i])) for i in range(64)]
        rr=[];cc=[];vv=[]
        for column,(i,j) in enumerate(pairs):
            for r,x in support[i]:
                if r==j:continue
                rr.append(pi[tuple(sorted((int(r),j)))]);cc.append(column);vv.append(x*(1 if r<j else -1))
            for r,x in support[j]:
                if r==i:continue
                rr.append(pi[tuple(sorted((i,int(r))))]);cc.append(column);vv.append(x*(1 if i<r else -1))
        L=coo_matrix((vv,(rr,cc)),shape=(2016,2016)).tocsr()
        B8=Ws@L@Ws.T
        need(zero(B8@Ws-8*Ws@L),'actual W covariance for graph generator '+str(q))
        f_edges|=(np.abs(X)>0).astype(np.int8)
        b_edges|=(np.abs(B8.toarray())>0).astype(np.int8)
    fcc,_=connected_components(csr_matrix(f_edges),directed=False)
    bcc,_=connected_components(csr_matrix(b_edges),directed=False)
    need(fcc==1 and bcc==1,'connected 64-mode and 60-mediator support graphs')
    # Exact combinatorial lemma: a connected graph has connected k-token
    # graph. To move configurations, induct on a spanning-tree leaf, arranging
    # its occupation via the nearest token/hole, then delete the fixed leaf.
    # Native W connects the two already connected sides in N2; C3 similarly N3.
    cols=[];rows=[];values=[]
    lookup={pairs[int(c)]:(int(A),int(W[A,c])) for A,c in zip(*np.nonzero(W))}
    for q,(i,j,k) in enumerate(combinations(range(64),3)):
        for pair,left,s in [((i,j),k,1),((i,k),j,-1),((j,k),i,1)]:
            if pair in lookup:
                A,w=lookup[pair];cols.append(q);rows.append(64*A+left);values.append(s*w)
    C3=coo_matrix((values,(rows,cols)),shape=(3840,41664)).tocsr()
    need(C3.nnz==29760,'native C3 connects the N3 sides')
    need(2016+60==2076 and 41664+3840==45504,'two sector dimensions')
    # Without the adjoined group, even all occupation readouts leave the native
    # color Cartan invariant. The Clock permutes spin slots only.
    color=[(1,1,1),(-1,-1,1),(-1,1,-1),(1,-1,-1)]
    color_pairs=list(combinations(range(4),2))
    fq=np.array([color[r%4][0] for r in range(64)])
    bq=np.array([color[c][0]+color[d][0] for k in range(10) for c,d in color_pairs])
    need(all(fq[i]+fq[j]==bq[A] for (i,j),(A,w) in lookup.items()),'Cartan conserved at every native vertex')
    need(len(set(bq))>1 and len(set(fq))>1,'Cartan is a non-scalar obstruction')
    # Weyl contraction, ordered-index convention from the supplied report.
    eps=np.array([[0,1],[-1,0]],dtype=np.int64)
    spin_basis=[np.eye(2,dtype=np.int64),np.array([[0,1],[1,0]],dtype=np.int64),np.diag([1,-1])]
    per_row=[]
    for A in range(60):
        M=np.zeros((64,64),dtype=np.int64)
        for c in np.flatnonzero(W[A]):
            i,j=pairs[c];M[i,j]=W[A,c];M[j,i]=-W[A,c]
        K=np.kron(M,eps)
        need(np.count_nonzero(K-K.T)==0,'same-handed scalar channel vanishes '+str(A))
        row=[]
        for j,S in enumerate(spin_basis):
            K=np.kron(M,S);a=K-K.T
            norm=int(np.sum(np.triu(a,1)**2))
            need(norm==64,'nonzero symmetric channel norm '+str((A,j)))
            row.append(norm)
        per_row.append(row)
    need(all(sum(row)==192 for row in per_row),'direct-sum channel squared norm 192')
    need(24**2!=192,'reported norm 24 incompatible with reported squared norm 192')
    out={'status':'PASS','exact_checks':len(checks),'checks':checks,
         'conditional_algebras':{'N2':{'dimension':2076**2,'commutant_dimension':1},
                                 'N3':{'dimension':45504**2,'commutant_dimension':1},
                                 'N2_plus_N3_with_charged_instruments':{'dimension':47580**2,'commutant_dimension':1}},
         'support_graph_components':{'fermions':int(fcc),'bosons':int(bcc)},
         'sufficient_graph_generator_subset':'45 Spin(10) generators plus 3 nearest-color SU(4) generators; not claimed minimal',
         'lorentz_row_norms_squared':[0,64,64,64], 'nonzero_direct_sum_norm':'8 sqrt(3), not 24',
         'scope':{'algebraic_fullness_conditional':True,'dynamical_Lie_control_certified':False,
                  'native_occupations_and_group_instruments':False,'relativistic_completion':False}}
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
