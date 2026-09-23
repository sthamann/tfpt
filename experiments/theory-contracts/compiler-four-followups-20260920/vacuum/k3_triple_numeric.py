#!/usr/bin/env python3
from __future__ import annotations
import hashlib, importlib.util, json
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
SOURCE=ROOT/'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
PIN='3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593'
HERE=Path(__file__).resolve().parent
checks=[]
def req(c,n):
 if not bool(c): raise RuntimeError(n)
 checks.append(n)
req(hashlib.sha256(SOURCE.read_bytes()).hexdigest()==PIN,'native source pin')
spec=importlib.util.spec_from_file_location('k3_source',SOURCE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
rays=m.source_rays();req(len(rays)==60,'sixty rays')
pairs=[(a,b) for a in range(4) for b in range(a,4)]
bplus=np.zeros((16,10),complex)
for j,(a,b) in enumerate(pairs):
 if a==b:bplus[4*a+b,j]=1
 else:bplus[4*a+b,j]=bplus[4*b+a,j]=1/np.sqrt(2)
refl=[]; actions={1:[],2:[]}
for ray in rays:
 r=np.eye(4)-np.outer(ray,ray.conj())/2;refl.append(r)
 actions[1].append(r.conj())
 actions[2].append((bplus.conj().T@np.kron(r,r)@bplus).conj())
local={}
for q,d in [(1,4),(2,10)]:
 k=sum(np.kron(a,np.kron(r,r)) for a,r in zip(actions[q],refl))/60
 local[q]=np.eye(16*d)-k
 req(np.linalg.norm(local[q]-local[q].conj().T)<4e-14,f'local q{q} Hermitian')

class Chain(LinearOperator):
 def __init__(self,charges):
  self.charges=tuple(charges);self.sd=tuple(4 if q==1 else 10 for q in charges)
  self.dims=self.sd+(4,)*(len(charges)+1)
  super().__init__(dtype=np.complex128,shape=(int(np.prod(self.dims)),)*2)
 def _matvec(self,x):
  t=np.asarray(x,complex).reshape(self.dims);out=np.zeros_like(t);n=len(self.charges);N=len(self.dims)
  for e,q in enumerate(self.charges):
   axes=(e,n+e,n+e+1);rest=tuple(a for a in range(N) if a not in axes);p=axes+rest;inv=np.argsort(p)
   moved=t.transpose(p); rows=moved.reshape(self.sd[e]*16,-1)
   out+=(local[q]@rows).reshape(moved.shape).transpose(inv)
  return out.reshape(-1)

def solve(charges,seed):
 op=Chain(charges);rng=np.random.default_rng(seed);v=rng.normal(size=op.shape[0])+1j*rng.normal(size=op.shape[0]);v/=np.linalg.norm(v)
 vals,vecs=eigsh(op,k=6,which='SA',v0=v,tol=2e-12,maxiter=2000,ncv=40)
 ix=np.argsort(vals);vals=vals[ix];vecs=vecs[:,ix]
 res=[float(np.linalg.norm(op@vecs[:,j]-vals[j]*vecs[:,j])) for j in range(6)]
 return {'charges':list(charges),'dimension':op.shape[0],'lowest_six':[float(x) for x in vals],'residuals':res,'max_residual':max(res),'orthogonality_error':float(np.max(abs(vecs.conj().T@vecs-np.eye(6))))}

results=[solve((1,2,2),20260920),solve((2,1,2),20260921)]
out={'status':'NUMERICAL_GUIDANCE','checks':len(checks),'results':results,'k1_reference':1.221493930352475,'not_a_lower_bound':True}
(HERE/'k3_triple_numeric.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
