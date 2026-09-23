#!/usr/bin/env python3
from __future__ import annotations
import hashlib,importlib.util,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import eigvalsh
from scipy.sparse.linalg import LinearOperator,eigsh
ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4');BASE=ROOT/'experiments/theory-contracts/compiler-relaxed-wall-20260919';HERE=Path(__file__).resolve().parent
p=BASE/'sector_numeric.py';assert hashlib.sha256(p.read_bytes()).hexdigest()=='fc20412835ba4b5e4436a0e7d24c9405485fc36b97e99eaded789e326145bd04'
s=importlib.util.spec_from_file_location('mom_sn',p);m=importlib.util.module_from_spec(s);sys.modules['mom_sn']=m;s.loader.exec_module(m)
checks=[];n=m.build_native(checks);LB=n.local_laplacians[2];LO=n.local_laplacians[1]
# q21 ground Omega(s1,A,B) Phi(s2,C), left dims s1,s2,A,B,C.
pair=np.einsum('xAB,yC->xyABC',n.omega,n.phi).reshape(-1);pair/=np.linalg.norm(pair)
leftdims=(10,4,4,4,4);rdims=(10,4);right=40

def apply_local(t,op,axes):
 N=t.ndim;rest=tuple(i for i in range(N) if i not in axes);perm=tuple(axes)+rest;inv=np.argsort(perm);z=t.transpose(perm);d=int(np.prod([t.shape[i] for i in axes]));return (op@z.reshape(d,-1)).reshape(z.shape).transpose(inv)
def H12(t):return apply_local(t,LB,(0,2,3))+apply_local(t,LO,(1,3,4))
pt=pair.reshape(leftdims)
hp=H12(pt)
assert np.linalg.norm(hp-.5*pt)<2e-14
# T_B partial C trace acts on s3,D.
A=LB.reshape(10,4,4,10,4,4);T=np.zeros((10,4,10,4),complex);L2=(LB@LB).reshape(10,4,4,10,4,4);T2=np.zeros_like(T)
for c in range(4):T+=A[:,c,:,:,c,:]/4;T2+=L2[:,c,:,:,c,:]/4
T=T.reshape(40,40);V0=T2.reshape(40,40)-T@T
# J output dims left,s3,D,input
I=np.eye(right).reshape(10,4,right);J=np.einsum('xyABC,zdj->xyABCzdj',pt,I)
LJ=apply_local(J,LB,(5,4,6));JT=np.einsum('xyABCzdi,ij->xyABCzdj',J,T)
W=LJ-JT
# verify orthogonal to p on left
ov=np.einsum('xyABC,xyABCzdj->zdj',pt.conj(),W).reshape(right,right)
assert np.linalg.norm(ov)<2e-13
HW=H12(W)
Wm=W.reshape(-1,right);HWm=HW.reshape(-1,right)
V=Wm.conj().T@Wm;M=Wm.conj().T@HWm
assert np.linalg.norm(V-V0)<3e-13
# generalized mean on support
vv,UU=np.linalg.eigh(V);keep=vv>1e-11;S=UU[:,keep]/np.sqrt(vv[keep]);gen=S.conj().T@M@S;ge=np.linalg.eigvalsh(gen)
# chord f(t)=1/(t+3/5-U), t in[c,23/10]
U0=391/320;c=(31-2*np.sqrt(10))/30;hi=23/10;shift=.6-U0
fl=1/(c+shift);fr=1/(hi+shift);slope=(fr-fl)/(hi-c);inter=fl-slope*c
Rbound=inter*V+slope*M
class Effective(LinearOperator):
 def __init__(self):super().__init__(dtype=np.complex128,shape=(1600,1600))
 def _matvec(self,x):
  q=np.asarray(x,complex).reshape(10,10,4,4);out=np.zeros_like(q)
  p=(0,2,1,3);inv=np.argsort(p);z=q.transpose(p);out+=((T-Rbound)@z.reshape(40,-1)).reshape(z.shape).transpose(inv)
  p=(1,2,3,0);inv=np.argsort(p);z=q.transpose(p);out+=(LB@z.reshape(160,-1)).reshape(z.shape).transpose(inv)
  out+=(.5-U0)*q
  return out.reshape(-1)
ev=eigsh(Effective(),k=4,which='SA',tol=1e-13,maxiter=1000,ncv=30,return_eigenvectors=False);ev=np.sort(ev)
print(json.dumps({'V_spectrum':[float(x) for x in eigvalsh(V)],'generalized_mean':[float(x) for x in ge],'chord_intercept':inter,'chord_slope':slope,'Rbound_max':float(eigvalsh(Rbound)[-1]),'certified_operator_margin_numeric':[float(x) for x in ev],'checks':len(checks)},indent=2))
np.savez_compressed(HERE/'k3_offblock_moments.npz',V=V,M=M,Rbound=Rbound,T=T,V0=V0)
