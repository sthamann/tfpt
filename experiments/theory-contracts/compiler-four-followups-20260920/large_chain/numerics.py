#!/usr/bin/env python3
"""Finite-size controls of the exact packet COMPRESSION, not the full H."""
import json
import numpy as np
from scipy.sparse import coo_matrix,diags
from scipy.sparse.linalg import LinearOperator,eigsh

kappa=1.;J=.01;mu=(kappa+9*J)/2
out=[]
for n in(4,6,8,10,12):
    dim=2**n;s=4.**(1-n)
    a=np.arange(dim,dtype=np.int64)
    nw=np.zeros(dim,dtype=np.int64)
    for e in range(n):nw+=((a>>e)&1)==((a>>((e+1)%n))&1)
    diag=3*n*(kappa+J)/8+mu*n+(kappa+9*J)*nw/8
    row=np.repeat(a,n);col=(a[:,None]^(1<<np.arange(n))).ravel()
    H=diags(diag)+coo_matrix((np.full(len(row),-mu/8),(row,col)),shape=(dim,dim)).tocsr()
    rr=[0,dim-1];cc=[dim-1,0]
    vv=[s*n*(kappa/2+mu)]*2
    for e in range(n):
        for root,leaf in((0,(dim-1)^(1<<e)),(dim-1,1<<e)):
            rr.extend((root,leaf));cc.extend((leaf,root));vv.extend((-s*mu/2,)*2)
    K=H+coo_matrix((vv,(rr,cc)),shape=(dim,dim)).tocsr()
    ap=(1+s)**(-.5);am=(1-s)**(-.5)
    aa=(ap+am)/2;bb=(ap-am)/2
    def A(v):
        w=v.copy();w[0]=aa*v[0]+bb*v[-1];w[-1]=bb*v[0]+aa*v[-1];return w
    C=LinearOperator((dim,dim),matvec=lambda v:A(K@A(v)),dtype=float)
    # Fixed full-support seed has no exact parity restriction.
    v0=np.random.default_rng(193+n).normal(size=dim)
    ec,vc=eigsh(C,k=4,which='SA',tol=2e-12,v0=v0)
    order=np.argsort(ec);ec=ec[order];vc=vc[:,order]
    ei=np.sort(eigsh(H,k=4,which='SA',tol=2e-12,v0=v0,return_eigenvectors=False))
    residual=max(np.linalg.norm(C@vc[:,i]-ec[i]*vc[:,i]) for i in range(4))
    bound=n*s/(1-s)*(kappa+1.5*J+21*mu/8)
    if residual>1e-9 or np.max(np.abs(ec-ei))>bound+1e-9:
        raise RuntimeError((n,residual,bound,ec,ei))
    exact_ising_gap=2*((kappa+9*J)/16)*np.tan(np.pi/(4*n))
    if abs(ei[1]-ei[0]-exact_ising_gap)>1e-9:raise RuntimeError('finite Ising gap')
    out.append({'N':n,'compression_E0':float(ec[0]),'compression_gap':float(ec[1]-ec[0]),
       'N_times_compression_gap':float(n*(ec[1]-ec[0])),
       'Ising_gap':float(ei[1]-ei[0]),'Ising_exact_finite_gap':float(exact_ising_gap),
       'ring_correction_norm_bound':float(bound),'max_compression_residual':float(residual)})
print(json.dumps({'status':'PASS_NUMERICAL_COMPRESSION_ONLY','couplings':{'kappa':kappa,'J':J,'mu':mu},
  'expected_limit_N_gap':float(np.pi*(kappa+9*J)/32),'rows':out,
  'full_vacuum_or_critical_point_proved':False},indent=2,sort_keys=True))
