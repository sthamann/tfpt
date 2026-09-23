"""Exact quartic-coordinate test; affine-current embedding audited separately."""
from pathlib import Path
import importlib.util
import itertools as it
import hashlib
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module
def require(ok,label):
    if not bool(ok):raise RuntimeError(label)
def simp(x):return s.simplify(x)
PINS={
 'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py':'3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593',
 'experiments/theory-contracts/compiler-spatial-response-20260919/completion24_check.py':'2f75bdf053e75e6a16919762ae8e8ce34471248729c336d57580fce81fece6ea',
}
for path,digest in PINS.items():
    require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,'source pin '+path)
source=load('product_source','experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py')
completion=load('product_completion','experiments/theory-contracts/compiler-spatial-response-20260919/completion24_check.py')
psis=[completion.exact_ray(z) for z in source.source_rays()]
def symmetric_basis(n):
    words=list(it.product(range(4),repeat=n)); idx={v:i for i,v in enumerate(words)}
    columns=list(it.combinations_with_replacement(range(4),n)); B=s.zeros(4**n,len(columns))
    for j,col in enumerate(columns):
        perms=set(it.permutations(col))
        for p in perms:B[idx[p],j]=1/s.sqrt(len(perms))
    return B
B2=symmetric_basis(2);B3=symmetric_basis(3)
Q=s.zeros(256,5)
for i,word in enumerate(it.product(range(4),repeat=4)):
    count=tuple(word.count(j) for j in range(4))
    if 4 in count:Q[i,0]=1
    elif count in ((2,2,0,0),(0,0,2,2)):Q[i,1]=1
    elif count in ((2,0,2,0),(0,2,0,2)):Q[i,2]=1
    elif count in ((2,0,0,2),(0,2,2,0)):Q[i,3]=1
    elif count==(1,1,1,1):Q[i,4]=1
norms=(4,12,12,12,24)
F20=s.Matrix.vstack(*[2*Q[:,a].reshape(4,64)*B3/s.sqrt(norms[a]) for a in range(5)])
F10=s.Matrix.vstack(*[s.sqrt(s.Rational(2,norms[a]))*B2.T*Q[:,a].reshape(16,16)*B2 for a in range(5)])
require(simp(F20.H*F20)==s.eye(20),'F20 isometry')
require(simp(F10.H*F10)==s.eye(10),'F10 isometry')
# Explicitly transport to the original Pauli Bell basis of contract .18.
def exact_entry(z):
    c=complex(z)
    require(c.real==round(c.real) and c.imag==round(c.imag),'Gaussian Pauli entry')
    return s.Integer(round(c.real))+s.I*s.Integer(round(c.imag))
Bbell=s.Matrix.hstack(*[s.Matrix([exact_entry(z)/2 for row in p for z in row])
                            for p in source.SYMMETRIC_PAULIS])
U=simp(Bbell.H*B2)
require(simp(U.H*U)==s.eye(10),'unitary monomial to original Bell basis')
Fbell=s.Matrix.vstack(*[s.sqrt(s.Rational(2,norms[a]))*Bbell.H*Q[:,a].reshape(16,16)*Bbell.conjugate() for a in range(5)])
require(simp(Fbell*U.conjugate()-s.kronecker_product(s.eye(5),U)*F10)==s.zeros(50,10),'phase faithful original .18 F10 basis conversion')
products=[]; overlaps=[]; factor_ranks=[]
for psi in psis:
    cube=B3.T*completion.tensor_power(psi,3)
    w20=simp(F20*cube.conjugate()); M=w20.reshape(5,4)
    q=simp(M*psi.conjugate())
    require(simp(M-q*psi.T)==s.zeros(5,4),'native cubic ray factorization')
    require(simp((q.H*q)[0])==1,'unit W5 factor')
    v=simp(B2.T*completion.tensor_power(psi,2))
    r=s.kronecker_product(q,v)
    require(simp((r.H*r)[0])==1,'unit product')
    image=simp(F10.H*r)
    require(simp(image-v.conjugate()/s.sqrt(2))==s.zeros(10,1),'product projection to old Bell readout')
    products.append(r);overlaps.append(str(simp((image.H*image)[0])))
R=s.Matrix.hstack(*products);G=simp(R*R.H);P=simp(F10*F10.H)
require(simp(G*P-3*P)==s.zeros(50),'Bell source subspace eigenvalue3')
require(simp(G-s.Rational(3,4)*s.eye(50)-s.Rational(9,4)*P)==s.zeros(50),'full exact product frame identity')
# Minimal polynomial and exact trace determine the remaining spectrum.
remaining=simp(G-3*P)
eigen=remaining.eigenvals()
result={'status':'PASS_COORDINATE_IDENTITIES','rays':len(psis),
 'source_pins':PINS,
 'factorization':'F20 conjugate(psi^3)=q_l tensor psi_l; ||q_l||=1',
 'projection':'F10^dagger(q_l tensor psi_l^2)=conjugate(psi_l^2)/sqrt(2)',
 'projection_norm_squared':sorted(set(overlaps)),
 'frame_eigenvalues':{str(k):int(v) for k,v in G.eigenvals().items()},
 'residual_eigenvalues':{str(k):int(v) for k,v in eigen.items()},
 'frame_identity':'G=(3/4) I50+(9/4) F10 F10^dagger; P_F=(4G-3I50)/9',
 'basis_conversion':'Exact unitary U from symmetric monomials to original Pauli Bell basis: F_Bell conjugate(U)=(I5 tensor U)F10',
 'affine_embedding':'Not established by this coordinate checker; requires explicit current-product dictionary.',
 'physical_gate_closed':False}
(HERE/'current_product_readout_check.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,sort_keys=True))
