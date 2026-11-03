"""Independent exterior-algebra mixed CAR words on an actual singular component."""
from pathlib import Path
from itertools import combinations,product
import json
import numpy as np
from scipy.linalg import expm
from scipy.special import expit
rng=np.random.default_rng(252)
Yu=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
s=float(np.linalg.svd(Yu,compute_uv=False)[0]);p=.25
z=np.diag([1,-1]);x=np.array([[0,1],[1,0]])
h=p*z+s*x;F=.13*s*x
e,R=np.linalg.eigh(h);U=R.conj().T@(expm(.4j*h)@expm(-.4j*(h+F)))@R
c=expit(-2*e);E=np.vstack([np.diag(np.sqrt(1-c)),np.diag(np.sqrt(c))])
U4=np.block([[U,np.zeros_like(U)],[np.zeros_like(U),U]])
ann=[]
for i in range(4):
 a=np.zeros((16,16))
 for st in range(16):
  if st>>i&1:a[st^(1<<i),st]=(-1)**((st&((1<<i)-1)).bit_count())
 ann.append(a)
omega=np.zeros(16,dtype=complex)
for ix in combinations(range(4),2):omega[sum(1<<i for i in ix)]=np.linalg.det(E[list(ix),:])
G=np.zeros((16,16),complex)
for st in range(16):
 rows=[i for i in range(4) if st>>i&1]
 for col in range(16):
  cols=[j for j in range(4) if col>>j&1]
  if len(rows)==len(cols):G[st,col]=np.linalg.det(U4[np.ix_(rows,cols)]) if rows else 1
amplitude=omega.conj()@G@omega
Q=U4@E@np.linalg.inv(E.conj().T@U4@E)@E.conj().T
errors=[]
for i,j in product(range(4),repeat=2):
 direct=omega.conj()@ann[j].T@ann[i]@G@omega/amplitude
 errors.append(abs(direct-Q[i,j]))
four=[]
for i,j,k,l in product(range(4),repeat=4):
 direct=omega.conj()@ann[i].T@ann[j].T@ann[l]@ann[k]@G@omega/amplitude
 expected=Q[k,i]*Q[l,j]-Q[l,i]*Q[k,j]
 four.append(abs(direct-expected))
out={'all_passed':bool(max(errors+four)<1e-11),'two_field_words':len(errors),'four_field_words':len(four),'max_error':float(max(errors+four)),'scope':'Actual original seed252 Yukawa singular component and its coherent two-face Slater state. Independent sixteen-state exterior-algebra evaluation, not full physical source matching.'}
if not out['all_passed']:raise RuntimeError(out)
Path(__file__).with_name('transition-word-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
