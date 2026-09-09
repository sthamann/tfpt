#!/usr/bin/env python3
"""Independent exact checks of the saved witness; no nullspace search or KMS.

Rebuild integer source using the pinned source constructor; verify the reported
M directly. The polar-reflection conclusion then follows by functional calculus.
"""
import hashlib
import json
from pathlib import Path

import sympy as sp

from seam_source import construct

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
r=json.loads((HERE/'seam_covariance_results.json').read_text())
d=r['data']
for rel, expected in d['external_source_hashes'].items():
    assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==expected, rel
s=construct()
assert s['provenance']['source_sha256']==d['provenance']['source_sha256']
A=sp.Matrix(s['A16_dep']); B=sp.Matrix(s['A_int']); O=sp.zeros(16)
for i,j in enumerate(s['img']): O[j,i]=1
M=sp.Matrix([[sp.Rational(v) for v in row] for row in d['nonlocal_witness']['exact_M']])
assert M.T==M
assert M.det()==sp.Integer(d['nonlocal_witness']['det_M'])!=0
assert M*A+A*M==sp.zeros(16)
assert M*B+B*M==sp.zeros(16)
assert M*O==O.T*M
assert O.T*O==sp.eye(16)
assert M**2*A==A*M**2 and M**2*B==B*M**2 and M**2*O==O*M**2
print('PASS exact saved nonlocal witness; invertible, symmetric, both anticommutators, reversed clock, polar-square compatibility')
assert sp.trace(O*A)==0 and sp.trace(O*B)==-6
print('PASS exact clock obstruction Tr(O H)=6 i t')

# Independent symbolic finite strip assembly. Arbitrary real onsite sin(p)
# and M-cos(p) stand in for momentum and mass; local proof valid every width.
a,b=sp.symbols('a b',real=True)
X=sp.Matrix([[0,1],[1,0]])
Y=sp.Matrix([[0,-sp.I],[sp.I,0]])
Z=sp.diag(1,-1)
T=Y/(2*sp.I)-Z/2
for ny in (2,3,5):
    H=sp.Matrix(sp.kronecker_product(sp.eye(ny),a*X+b*Z))
    for j in range(ny-1):
        H[2*j+2:2*j+4,2*j:2*j+2]=T
        H[2*j:2*j+2,2*j+2:2*j+4]=T.conjugate().T
    R=sp.zeros(ny)
    for j in range(ny):R[j,ny-1-j]=1
    U=sp.kronecker_product(R,Y)
    assert U**2==sp.eye(2*ny)
    assert U.conjugate().T==U
    assert U*H*U==-H
print('PASS symbolic independently assembled QWZ strips, arbitrary onsite parameters')
print('CERTIFICATE VALID: finite identities only; source locality/physical identification/global RH not asserted')
