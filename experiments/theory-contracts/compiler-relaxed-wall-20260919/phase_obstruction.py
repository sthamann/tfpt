"""Native central-character obstruction; no energy ordering is inferred."""
from pathlib import Path
import hashlib, importlib.util, json
import numpy as np
ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
p=ROOT/'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
checks=[]
def req(x,n):
 if not bool(x):raise RuntimeError(n)
 checks.append(n)
req(hashlib.sha256(p.read_bytes()).hexdigest()=='3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593','native source pin')
spec=importlib.util.spec_from_file_location('source',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
z=m.source_rays();r=[np.eye(4)-np.outer(v,v.conj())/2 for v in z]
def swap(i,j,c=1):
 a=np.eye(4,dtype=complex);a[i,i]=a[j,j]=0;a[i,j]=c;a[j,i]=c.conjugate() if hasattr(c,'conjugate') else c;return a
factors=[swap(0,1),swap(1,2),swap(2,3),swap(1,3,1j),swap(1,3),np.diag([1,1,-1,1])]
for a in factors:req(any(np.array_equal(a,b) for b in r),'factor is native reflection')
X=factors[0]@factors[1]@factors[2];Z=factors[3]@factors[4]@factors[5]
req(np.array_equal(X@Z@X.conj().T@Z.conj().T,-1j*np.eye(4)),'matter Weyl commutator minus i')
def key(a):return tuple((int(v.real),int(v.imag)) for v in a)
lookup={key(1j**q*v):(i,q) for i,v in enumerate(z) for q in range(4)}
def source(g,k):
 M=np.zeros((60,60),complex)
 for i,v in enumerate(z):
  j,q=lookup[key(g@v)];M[j,i]=1j**(-k*q)
 return M
for k in range(4):
 A=source(X,k);B=source(Z,k)
 req(np.array_equal(A@B@A.conj().T@B.conj().T,1j**k*np.eye(60)),'source Weyl character q'+str(k))
characters={str(K):str(1j**K*(-1j)**5) for K in range(4)}
req(1j**3*(-1j)**5==-1,'K3 joint action anticommutes for five matter registers')
req(1j*(-1j)**5==1,'K1 has trivial joint Weyl commutator')
res={'status':'PASS','checks':len(checks),'matter_vertices':5,'joint_commutator':'(-i)^(5-K) I','characters':characters,
 'energy_multiplicity_divisor_by_K':{'0':4,'1':1,'2':4,'3':2},
 'premise':'Full H retains simultaneous native X and Z covariance, as do H0, HE, and V.',
 'conclusion':'Every K3 energy eigenspace is even-dimensional; this is NOT an energy bound or its exclusion as the vacuum.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
print(json.dumps(res,indent=2))
