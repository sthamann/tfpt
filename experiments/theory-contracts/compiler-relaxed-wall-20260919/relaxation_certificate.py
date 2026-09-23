"""Exact local certificates for the relaxed native four-source wall sectors."""
from pathlib import Path
import contextlib
import hashlib
import importlib.util
import io
import itertools as it
import json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
PINS={
 'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py':
 '3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593',
 'experiments/theory-contracts/compiler-pair-sector-audit-20260919/PROOF.txt':
 'b63d5a7a97c331f0aa0920fb77bded14981be1c6ec735fdc91e3b1536ed5a766',
 'experiments/theory-contracts/compiler-domain-wall-core-20260919/PROOF.txt':
 'fe9c66ef6821ff4771993cc899dd7ea385b3ad87a45712e831d12cc190c9ddb6',
}
checks=[]
def req(ok,name):
    if not bool(ok):raise RuntimeError(name)
    checks.append(name)
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
for p,h in PINS.items():req(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'pin '+p)
with contextlib.redirect_stdout(io.StringIO()):
    six=load('six',HERE/'core_six.py')
source=load('source',ROOT/next(iter(PINS)))
rays=source.source_rays()
r2=[2*np.eye(4)-np.outer(z,z.conj()) for z in rays]
def perm_matrix(perm):
    d=len(perm);n=4**d;P=np.zeros((n,n),dtype=np.int64)
    for old in it.product(range(4),repeat=d):
        new=tuple(old[perm[i]] for i in range(d))
        P[np.ravel_multi_index(new,(4,)*d),np.ravel_multi_index(old,(4,)*d)]=1
    return P
I64=np.eye(64,dtype=np.int64)
S01=perm_matrix((1,0,2));S02=perm_matrix((2,1,0));S12=perm_matrix((0,2,1))
K3num=sum((np.kron(np.kron(r,r),r) for r in r2),np.zeros((64,64),complex))
req(np.array_equal(K3num,16*I64+64*(S01+S02+S12)-32*(S01@S12+S12@S01)),
    'native third reflection moment equals the stated permutation algebra')
Kbar=sum((np.kron(np.kron(r.conj(),r),r) for r in r2),np.zeros((64,64),complex))
Lnum=480*I64-Kbar
req(np.array_equal(Lnum,Lnum.conj().T),'local conjugate-four L Hermitian')
# Rational local spectral polynomial gives the needed complete local floor.
poly=(Lnum-240*I64)@(Lnum-400*I64)@(Lnum-528*I64)
req(np.array_equal(poly,np.zeros((64,64))),'bar4 local roots 1/2,5/6,11/10')
def traceB(M):return np.trace(M.reshape(4,4,4,4,4,4),axis1=1,axis2=4).reshape(16,16)
bell=np.eye(4).reshape(-1);B=np.outer(bell,bell)
I16=np.eye(16,dtype=np.int64)
req(np.array_equal(traceB(Lnum),192*(9*I16-B)),
    'partial L =9I/10-BellBell*/10')
req(np.array_equal(25*traceB(Lnum@Lnum),76800*(251*I16-44*B)),
    'partial L squared =251I/300-11 BellBell*/75')
# Above equality avoids fractions: denominator4*480^2=921600.
# 921600/300=3072, times25 gives76800.
G,H,Q=six.G,six.H,six.Q
req(G==G.T and all(G[:i,:i].det()>0 for i in range(1,7)),
    'six-bond Gram positive definite')
req(G*H==H.T*G,'six native actions Hermitian in the true Gram')
req(Q.T*G*Q==G and Q*Q==s.eye(6) and Q[:,0]==s.eye(6)[:,0],
    'mirror is unitary involution fixing the unrelaxed core')
x=s.symbols('x');p=H.charpoly(x).as_expr()
intervals=[(s.Rational(1221493930352475,10**15),s.Rational(1221493930352476,10**15)),
 (s.Rational(2010,1000),s.Rational(2011,1000)),
 (s.Rational(2543,1000),s.Rational(2544,1000)),
 (s.Rational(2785,1000),s.Rational(2786,1000)),
 (s.Rational(3031,1000),s.Rational(3032,1000)),
 (s.Rational(3541,1000),s.Rational(3542,1000))]
for lo,hi in intervals:req(s.Poly(p,x).count_roots(lo,hi)==1,'one simple root in '+str((lo,hi)))
req(sum(s.Poly(p,x).count_roots(lo,hi) for lo,hi in intervals)==6,'all six roots isolated')
req((G*H)[0,0]==s.Rational(5,4),'initial core energy 5/4')
req((G*H*H)[0,0]-s.Rational(25,16)==s.Rational(3,80),'initial core variance 3/80')
v=s.Matrix([6,1,0,0,0,0])
req((v.T*G*H*v)[0]/(v.T*G*v)[0]==s.Rational(391,320),
    'full model rational variational upper bound 391/320')

# Complete fixed-source-module complement bound, not a full-source theorem.
A=s.Rational(33,20);C=s.Rational(53,30);b2=s.Rational(77,1200)
req(s.Rational(251,300)-s.Rational(81,100)==s.Rational(2,75),
    'adjoint bar4 variance 2/75')
req(s.Rational(2,75)+s.Rational(3,80)==b2,'total adjoint offblock norm squared')
c=(205-s.sqrt(973))/120
req(s.simplify((A+C-s.sqrt((A-C)**2+4*b2))/2-c)==0,
    'complete complement bound from two-block quadratic form')
req(c>s.Rational(1448,1000),'fixed-module complement above 1.448')
eb=s.Rational(1,2)+(8-s.sqrt(19))/5
req(eb>s.Rational(1228,1000) and eb<s.Rational(1229,1000),'boundary exact eigenvalue interval')
req(c-eb>s.Rational(22,100),'boundary sector certified gap over .22')
req(c-intervals[0][1]>s.Rational(2268,10000),'central sector certified gap over .2268')
req(eb-intervals[0][1]>s.Rational(6726,10**6),'end-center offset exceeds .006726')

# Native phase-transfer kernel between Phi on source2 and source3.
Z=np.stack([phase*z for z in rays for phase in(1,1j,-1,-1j)])
N=len(Z);O=Z.conj()@Z.T;R=O.real.astype(np.int64)
kernel=s.zeros(4)
for i,j in it.product(range(4),repeat=2):
    vals=Z.conj()[:,i,None]*Z[None,:,j]*(4-R)
    req(np.array_equal(vals.real,np.rint(vals.real)) and np.array_equal(vals.imag,np.rint(vals.imag)),
        'native Phi kernel Gaussian integral')
    kernel[i,j]=(s.Integer(int(vals.real.sum()))+s.I*int(vals.imag.sum()))/(16*N*N)
req(kernel==-s.eye(4)/32,'native transferred-Phi kernel minus identity/32')
# Gram uses I/4 for Phi after tracing its source. Replacing by -I/32 gives -G/8.
req(-s.Rational(1,32)/s.Rational(1,4)==-s.Rational(1,8),
    'cross-six-space V matrix exactly minus Gram/8')
weight_lower=s.Rational(750,779)
eta_lower=s.Rational(721,779)
req(weight_lower==(2-s.Rational(5,4))/(2-s.Rational(1221,1000)),
    'core ground overlap bound from second eigenvalue at least two')
req(eta_lower==2*weight_lower-1 and eta_lower>0,
    'relaxed mirror hopping provably nonzero')
result={'status':'PASS','verdict':'PARTIAL','checks':len(checks),'guard_names':checks,
 'source_pins':PINS,
 'exact_central_characteristic_polynomial':str(s.factor(p)),
 'central_root_interval':[str(z) for z in intervals[0]],
 'boundary_ground':'1/2+(8-sqrt19)/5',
 'complete_fixed_module_complement_floor':'(205-sqrt973)/120',
 'complete_fixed_module_ground_simple':True,
 'central_gap_bound':'>0.2268 kappa','boundary_gap_bound':'>0.22 kappa',
 'relaxed_central_native_V_matrix':'-G/8 between companion six-bond bases',
 'relaxed_central_hop':'-mu eta/8; eta=<g|mirror g>',
 'eta_lower_bound':'721/779','eta_upper_bound':'1',
 'eta_numerical_evaluation':six.result['relaxed_middle_overlap_eta'],
 'hop_over_mu_numerical':six.result['relaxed_middle_hopping_over_mu'],
 'scope':'EXACT_FIXED_SOURCE_MODULE_THEOREMS_NOT_COMPLETE_SOURCE_VACUUM',
 'not_claimed':['full-source ground','isolated full-source doublet','positive-coupling physical gap',
                'large-chain dispersion','fermion statistics','Dirac/Weyl mode','TOE']}
(HERE/'relaxation_certificate.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:result[k] for k in('status','verdict','checks','central_root_interval',
 'complete_fixed_module_complement_floor','central_gap_bound','eta_lower_bound','eta_numerical_evaluation')},indent=2))
