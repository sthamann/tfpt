"""Independent finite/symbolic witnesses for the accompanying analytic proofs.

No RH proof, no factoring algorithm, no native spacetime derivation.
The general theorems are proved in the report, not by these finite tests.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from math import comb
from itertools import product
import json
import numpy as np
import sympy as s

ROOT = Path(__file__).resolve().parent
TENSOR = ROOT / 'TFPT_Universalraum_Native_Antwort_Pruefpaket_2026-09-15_v1.6.4/TFPT_Native_Antwort_v1.6.4/ground_replay/outputs/simple_core/spinor_tensors.npz'
checks=[]
def need(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    checks.append(label)

need(sha256(TENSOR.read_bytes()).hexdigest() == '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763', 'native W source pin')
raw=np.load(TENSOR)['W']
need(not np.any(raw.imag) and np.array_equal(raw.real,np.rint(raw.real)), 'W exactly real integral')
W=raw.real.astype(np.int64)
need(W.shape == (60,2016), 'sixty pair channels')
need(np.all(np.count_nonzero(W,axis=1)==8), 'eight terms per channel')
need(np.all(np.abs(W[W!=0])==1), 'all nonzero coefficients have modulus one')
need(sum(int(np.abs(row).sum())**2 for row in W)==3840, 'triangle bound sum norm(P_A)^2 <=3840')

# Exact finite counting witness; ln(2)<1 is proved by exp(1)>1+1.
C=F(96,5)  # 7680*(1/20)^2
cutoff=1024
boson_cutoff=int(2*(cutoff+C))
native_count_upper=2**64*comb(boson_cutoff+60,60)
need(boson_cutoff==2086,'outward spectral counting cutoff')
need(native_count_upper<2**455,'native states below 1024 Delta fewer than 2^455')
need(2**1024>native_count_upper,'logarithmic spectrum cannot fit in native energy window')
for m in range(1,7):
    for cutoff_small in range(7):
        need(sum(comb(k+m-1,m-1) for k in range(cutoff_small+1))==comb(cutoff_small+m,m), 'boson stars-and-bars cumulative count')

# Independent finite Fock witness (four fermions, two truncated bosons).
I2=s.eye(2); z=s.diag(1,-1); a=s.Matrix([[0,1],[0,0]])
def kron_all(xs):
    out=s.ones(1,1)
    for x in xs: out=s.kronecker_product(out,x)
    return out
fs=[]
for r in range(4):
    fs.append(s.kronecker_product(kron_all([z if j<r else a if j==r else I2 for j in range(4)]),s.eye(4)))
bs=[s.kronecker_product(s.eye(16),a,I2),s.kronecker_product(s.eye(16),I2,a)]
Ps=[fs[1]*fs[0],fs[3]*fs[2]]
Nb=sum((b.T*b for b in bs),s.zeros(64))
V=sum((b.T*p+p.T*b for b,p in zip(bs,Ps)),s.zeros(64))
g=s.Rational(1,20)
H=Nb+g*V
square=Nb/2+sum(((b+2*g*p).T*(b+2*g*p)/2-2*g*g*p.T*p for b,p in zip(bs,Ps)),s.zeros(64))
need(H==square,'square completion exact finite Fock matrix')
parity0=s.kronecker_product(z,z,I2,I2,s.eye(4))
parity1=s.kronecker_product(I2,I2,z,z,s.eye(4))
H_with_boson_hop=H+s.Rational(1,10)*(bs[0].T*bs[1]+bs[1].T*bs[0])
for parity in [parity0,parity1]:
    need(H_with_boson_hop*parity==parity*H_with_boson_hop,'pair vertices plus boson transfer preserve local fermion parity')
fermion_hop=fs[2].T*fs[0]+fs[0].T*fs[2]
need(fermion_hop*parity0!=parity0*fermion_hop,'single fermion exchange lies outside local even algebra')
vac=s.zeros(64,1);vac[0]=1
initial=fs[0].T*vac; final=fs[2].T*vac
state=initial
for k in range(9):
    need((final.T*state)[0]==0,'finite witness zero single-fermion transfer moment '+str(k))
    state=H_with_boson_hop*state
need((final.T*fermion_hop*initial)[0]==1,'added exchange really changes the transfer witness')

# Exact rational arithmetic for the analytically proved resolvent bound.
d=F(7737,10**6); cp=F(329636,10**6); c=F(379636,10**6)
eps_hi=F(2403745,61508688)
Zlo=F(40912436089,46487375000)
separation=min(cp+d,c-eps_hi)
radius=F(1,10)
rest_bound=(1-Zlo)/(separation-radius)
need(separation==F(337373,10**6),'minimum spectral distance to both remaining channels')
need(rest_bound<F(505213,10**6),'certified pole remainder <0.505213/Delta in radius 0.1 Delta')

# Twisted multiplicative semigroup: c(m,n)=(-1)^(v2(m)*v3(n)).
def valuation(n,p):
    k=0
    while n%p==0:
        n//=p;k+=1
    return k
def cocycle(m,n): return (-1)**(valuation(m,2)*valuation(n,3))
samples=[1,2,3,4,5,6,9,10,12,15]
for l,m,n in product(samples,repeat=3):
    need(cocycle(l,m)*cocycle(l*m,n)==cocycle(m,n)*cocycle(l,m*n),'associative twisted composition')
for n in range(1,25):
    need(cocycle(2,3*n)*cocycle(3,n)==-cocycle(3,2*n)*cocycle(2,n),'relative minus for multiplication by two and three')
for m,n in product(range(1,8),repeat=2):
    need(s.simplify(s.log(m*n)-s.log(m)-s.log(n))==0,'logarithmic generator shift identity')

limit=24
def truncated_shift(m,twisted):
    mat=s.zeros(limit)
    for n in range(1,limit+1):
        if m*n<=limit: mat[m*n-1,n-1]=cocycle(m,n) if twisted else 1
    return mat
S2=truncated_shift(2,False);T2=truncated_shift(2,True);T3=truncated_shift(3,True)
need(T2*T3==-T3*T2,'truncated anticommutation identity')
need(T2.T*T2==S2.T*S2,'twists leave occupation probabilities invariant')
need(T2.T*T2!=s.eye(limit),'finite truncated shift is not an isometry on entire window')
e1=s.eye(limit)[:,0]
w0=T2*T3*e1;w1=T3*T2*e1
need((w0+w1).dot(w0+w1)/4==0 and (w0-w1).dot(w0-w1)/4==1,'controlled path interference probabilities zero and one')

# A self-adjoint positive H does not force zeros of Tr exp(-s H) onto Re s=1/2.
zz=s.log(2)+s.I*s.pi
need(s.simplify(1+2*s.exp(-zz))==0,'positive H=diag(0,1,1) has partition zero at log(2)+i*pi')
need(s.log(2)!=s.Rational(1,2),'partition zero not on critical half line')
need((-1)**1==-1 and (-1)**2==1,'single phase cannot give minus for every repetition')

# Positive ground state does not determine excitation energies or a clock.
H1=s.diag(0,1,2);H2=s.diag(0,3,7);omega=s.Matrix([1,0,0])
need(H1*omega==H2*omega==s.zeros(3,1),'same pure ground state for different generators')
transition=s.zeros(3);transition[0,1]=1
need(H1*transition-transition*H1!=H2*transition-transition*H2,'same ground state different observable dynamics')

result={
 'status':'PASS','checks':len(checks),'check_labels':checks,
 'scope':'finite and symbolic witnesses accompanying analytic proofs; not formal proof assistant verification',
 'native_counting':{'crude_C_over_Delta':str(C),'energy_cutoff_Delta':cutoff,'boson_cutoff':boson_cutoff,'upper_count':str(native_count_upper),'upper_count_less_than_power_of_two':455,'required_log_spectrum_count_at_least_power_of_two':1024},
 'pole_remainder':{'distance_lower_bound_Delta':str(separation),'disk_radius_Delta':str(radius),'bound_times_Delta':str(rest_bound),'decimal':float(rest_bound)},
 'not_proved':['RH','efficient native factoring','native exchange operation','spacetime or gravity','origin of chosen cocycle','full native self-energy'],
 'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()
}
print(json.dumps(result,indent=2))
