#!/usr/bin/env python3
from __future__ import annotations
import hashlib, importlib.util, json
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator,eigsh
ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
BASE=ROOT/'experiments/theory-contracts/compiler-relaxed-wall-20260919'
SOURCE=ROOT/'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
PINS={SOURCE:'3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593',BASE/'sector_numeric.py':'fc20412835ba4b5e4436a0e7d24c9405485fc36b97e99eaded789e326145bd04'}
for p,h in PINS.items():
 if hashlib.sha256(p.read_bytes()).hexdigest()!=h:raise RuntimeError('pin '+str(p))
def load(n,p):
 import sys
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
sn=load('k3sn',BASE/'sector_numeric.py');checks=[];native=sn.build_native(checks)
class Op(LinearOperator):
 def __init__(self,charges):
  self.charges=charges;self.sd=tuple(4 if q==1 else 10 for q in charges);self.dims=self.sd+(4,)*5
  super().__init__(dtype=np.complex128,shape=(int(np.prod(self.dims)),)*2)
 def _matvec(self,x):
  t=np.asarray(x,complex).reshape(self.dims);out=np.zeros_like(t);N=9
  for e,q in enumerate(self.charges):
   axes=(e,4+e,5+e);rest=tuple(a for a in range(N) if a not in axes);p=axes+rest;inv=np.argsort(p)
   m=t.transpose(p);rows=m.reshape(self.sd[e]*16,-1)
   out+=(native.local_laplacians[q]@rows).reshape(m.shape).transpose(inv)
  return out.reshape(-1)
def solve(charges,seed):
 op=Op(charges);rng=np.random.default_rng(seed);v=rng.normal(size=op.shape[0])+1j*rng.normal(size=op.shape[0]);v/=np.linalg.norm(v)
 vals,vecs=eigsh(op,k=4,which='SA',v0=v,tol=3e-10,maxiter=1000,ncv=16)
 ix=np.argsort(vals);vals=vals[ix];vecs=vecs[:,ix]
 res=[float(np.linalg.norm(op@vecs[:,i]-vals[i]*vecs[:,i])) for i in range(4)]
 return {'charges':list(charges),'dimension':op.shape[0],'lowest_four':[float(z) for z in vals],'residuals':res,'max_residual':max(res),'gram_error':float(np.max(abs(vecs.conj().T@vecs-np.eye(4))))}
import sys
charges=tuple(map(int,sys.argv[1])) if len(sys.argv)>1 else (2,1,2,2)
r=solve(charges,20260920+sum((i+1)*q for i,q in enumerate(charges)))
p=Path(__file__).with_name('k3_full_'+''.join(map(str,charges))+'.json');p.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps(r,indent=2,sort_keys=True))
