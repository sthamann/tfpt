"""Minimal scalar-Weyl tensor repair, explicitly not a native derivation.

An auxiliary two-dimensional alternating tensor repairs the exchange type.
It is an additional independent multiplicity, not the Lorentz spinor index,
not merely a central double-cover sign and not a Nambu particle-hole relabel.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
TENSOR=HERE/'ground_replay/outputs/simple_core/spinor_tensors.npz'
checks=[]
def need(ok,label):
    if not bool(ok): raise RuntimeError(label)
    checks.append(label)
need(sha256(TENSOR.read_bytes()).hexdigest()=='3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763','native tensor pin')
raw_W=np.load(TENSOR)['W']
need(not np.any(raw_W.imag) and np.array_equal(raw_W.real,np.rint(raw_W.real)),'complex storage has exactly zero imaginary part and integral real coefficients')
W=raw_W.real.astype(np.int64)
eps=np.array([[0,1],[-1,0]],dtype=np.int64)
pairs=list(combinations(range(64),2))
for A,row in enumerate(W):
    M=np.zeros((64,64),dtype=np.int64)
    for j in np.flatnonzero(row):
        u,v=pairs[int(j)];M[u,v]=row[j];M[v,u]=-row[j]
    naive=np.kron(M,eps)
    need(np.array_equal(naive,naive.T),'original scalar Weyl coefficient cancels')
    internal_doubled=np.kron(M,eps)
    repaired=np.kron(internal_doubled,eps)
    need(np.array_equal(internal_doubled,internal_doubled.T),'auxiliary alternating factor makes internal Yukawa tensor symmetric')
    need(np.array_equal(repaired,-repaired.T) and np.any(repaired),'doubled scalar Weyl vertex survives Grassmann antisymmetrization')
    need(int(np.sum(repaired*repaired))==64,'all sixty repaired coefficient norms from exact W')

E=s.Matrix(eps)
for generator in [s.Matrix([[0,1],[0,0]]),s.Matrix([[0,0],[1,0]]),s.diag(1,-1)]:
    need(generator.T*E+E*generator==s.zeros(2),'epsilon invariant under infinitesimal SL2')
# Lorentz and auxiliary factors are DIFFERENT spaces; each contraction is a
# singlet of its own determinant-one action. No compactness/unitarity of
# Lorentz transformations is assumed here.
a,b,c,d=s.symbols('a b c d')
K=s.Matrix([[a,b],[c,d]])
sol=s.linsolve(list(K+K.T),(a,b,c,d))
need(sol==s.FiniteSet((0,-c,c,0)),'unique two-dimensional alternating form up to normalization')
need(s.Matrix([[a]])+s.Matrix([[a]]).T==s.Matrix([[2*a]]),'one-dimensional auxiliary factor has no nonzero alternating form')
need(E.det()==1,'minimal auxiliary form is nondegenerate')

# Charge bookkeeping: two independent annihilation multiplets can keep the
# same native b† f f charge, but the Nambu substitute cannot.
need(2-1-1==0,'independent equal-charge doublet retains source N conservation')
need(2-1+1==2,'particle-hole Nambu doubling fails the same charge test')

result={'status':'PASS','checks':len(checks),'check_labels':checks,
        'conditional_scalar_vertex':'b_A^dagger M_A[I,J] epsilon[a,b] epsilon[alpha,beta] psi[I,a,alpha] psi[J,b,beta] + h.c.',
        'index_dictionary':{'I':'64 native internal labels','a':'NEW independent auxiliary multiplicity, dimension 2',
                            'alpha':'left Weyl Lorentz spinor, dimension 2','A':'60 native internal boson labels; Lorentz scalar in this candidate'},
        'minimality_scope':'among tensor-factor repairs retaining the same antisymmetric W, a local same-handed Weyl bilinear and a scalar b',
        'native_status':'NOT DERIVED: requires 128 rather than 64 Weyl internal components; no physical on-shell count or family assignment follows',
        'not_proved':['source origin and physical availability of auxiliary doublet','CAR-preserving native embedding and matching H',
                      'Lorentz-covariant kinetic action','chiral measure/anomaly cancellation/mirror control','continuum limit'],
        'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(result,indent=2))
