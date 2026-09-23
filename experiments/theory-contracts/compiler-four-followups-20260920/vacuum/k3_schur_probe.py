#!/usr/bin/env python3
from __future__ import annotations
import hashlib,importlib.util,json
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator,eigsh
ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4');HERE=Path(__file__).resolve().parent
SOURCE=ROOT/'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593'
s=importlib.util.spec_from_file_location('probe_source',SOURCE);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);rays=m.source_rays()
def key(v):return tuple((int(round(z.real)),int(round(z.imag))) for z in v)
lookup={key(1j**q*v):(i,q) for i,v in enumerate(rays) for q in range(4)}
acts=[];refs=[]
for ray in rays:
 r=np.eye(4)-np.outer(ray,ray.conj())/2;refs.append(r);a=np.zeros((60,60),complex)
 for i,v in enumerate(rays):
  j,q=lookup[key(r@v)];a[j,i]=1j**(-2*q)
 acts.append(a)
D=np.empty((60,60),complex)
for l,u in enumerate(rays):
 for j,v in enumerate(rays):D[l,j]=np.vdot(v,u)**2
D=np.rint(D.real)+1j*np.rint(D.imag);P=D/96
w,U=np.linalg.eigh(P);X=U[:,:50];B=U[:,50:]
assert np.max(abs(w[:50]))<1e-12 and np.max(abs(w[50:]-1))<1e-12
mods={'B':B,'X':X};local={};T={};V={}
for name,U0 in mods.items():
 ar=[U0.conj().T@a@U0 for a in acts];d=U0.shape[1]
 K=sum(np.kron(a,np.kron(r,r)) for a,r in zip(ar,refs))/60
 L=np.eye(d*16)-K;local[name]=L
 A=L.reshape(d,4,4,d,4,4)
 # source,left,right, source',left',right' -> source,right,source',right'
 t=np.zeros((d,4,d,4),complex)
 L2=(L@L).reshape(d,4,4,d,4,4);t2=np.zeros_like(t)
 for c in range(4):
  t+=A[:,c,:,:,c,:]/4;t2+=L2[:,c,:,:,c,:]/4
 t=t.reshape(d*4,d*4);t2=t2.reshape(d*4,d*4)
 T[name]=t;V[name]=t2-t@t
 assert np.linalg.norm(t-t.conj().T)<1e-11 and np.linalg.norm(V[name]-V[name].conj().T)<1e-11
class Eff(LinearOperator):
 def __init__(self,a,b):
  self.a=a;self.b=b;self.da=mods[a].shape[1];self.db=mods[b].shape[1];self.dims=(self.da,self.db,4,4)
  super().__init__(dtype=np.complex128,shape=(self.da*self.db*16,)*2)
 def _matvec(self,x):
  q=np.asarray(x,complex).reshape(self.dims);out=np.zeros_like(q)
  # T_a on axes source a,D
  p=(0,2,1,3);inv=np.argsort(p);z=q.transpose(p);out+=(T[self.a]@z.reshape(self.da*4,-1)).reshape(z.shape).transpose(inv)
  # L_b on source b,D,E
  p=(1,2,3,0);inv=np.argsort(p);z=q.transpose(p);out+=(local[self.b]@z.reshape(self.db*16,-1)).reshape(z.shape).transpose(inv)
  return out.reshape(-1)
def solve(a,b,seed):
 op=Eff(a,b);rng=np.random.default_rng(seed);v=rng.normal(size=op.shape[0])+1j*rng.normal(size=op.shape[0]);
 vals,vecs=eigsh(op,k=10,which='SA',v0=v,tol=1e-12,maxiter=1000,ncv=40);vals=np.sort(vals)
 varmax=float(np.linalg.eigvalsh(V[a])[-1])
 return {'partial':a,'full':b,'dimension':op.shape[0],'lowest_ten':[float(z) for z in vals],'variance_norm':varmax}
res=[solve('B','B',1),solve('B','X',2),solve('X','B',3)]
c21=31/30-np.sqrt(10)/15;beta=17/15-np.sqrt(214)/30;U0=391/320
for x in res:
 A0=.5+x['lowest_ten'][0];C=c21+(.6 if x['partial']==x['full']=='B' else beta);b2=x['variance_norm']
 x.update(A=A0,C=C,b2=b2,schur=(A0+C-np.sqrt((A0-C)**2+4*b2))/2,threshold=U0)
out={'status':'NUMERICAL_GUIDANCE_NOT_PROOF','results':res}
(HERE/'k3_schur_probe.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
