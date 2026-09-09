#!/usr/bin/env python3
"""Check saved exact geometry witness without its formula/nullspace search.

Shares the existing compiler source extractor. Checks its raw matrix, source
hashes, marked-triangle obstruction, boundary cyclic span and cubic directly.
Separately builds a symbolic QWZ cylinder by local edges at general seam phase.
"""
import hashlib
import json
from pathlib import Path

import sympy as s

from seam_source import construct

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
r = json.loads((HERE/'seam_geometry_results.json').read_text())


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


for rel, sha in r['source_hashes'].items():
    need(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest() == sha, 'changed source: '+rel)
src = construct()
need(src['provenance']['source_sha256'] == r['provenance']['source_sha256'], 'changed compiler source')
A = s.Matrix(src['A16_dep'])
B = s.Matrix(src['A_int'])
O = s.zeros(16)
for i, j in enumerate(src['img']):
    O[j, i] = 1
U = s.Matrix([[s.Rational(x) for x in row] for row in r['data']['reflection']['U']])
I = s.eye(16)
P3, P2, PB = [s.diag(*[int(a <= i < b) for i in range(16)])
              for a, b in ((0, 6), (6, 10), (10, 16))]
need(U.T == U and U**2 == I, 'reflection not orthogonal involution')
need(U*A*U == -A and U*B*U == -B, 'source reversal')
need(U*O*U == O.T and U*PB == PB*U, 'clock/boundary law')
need(U*P3 != P3*U and U*P2 != P2*U, 'marked mixing')
need(s.trace(P3*B*P2*B*PB*B) == -36, 'triangle invariant')
need(s.trace(O**2*B) == 6 and s.trace(O**2*A) == 0, 'family invariant')
print('PASS saved rational U and marked/family trace obstructions')

Pi = sum((O**j for j in range(6)), s.zeros(16))/6
Krylov = s.Matrix.hstack(*[(B**k)[:, 10:] for k in range(5)])
need(Pi.rank() == 10 and Pi*PB == PB, 'clock fixed projector')
need(Krylov.rank() == 10 and Pi*Krylov == Krylov, 'boundary cyclic span')
active = s.diag(s.ones(3)/3, s.ones(2)/2, s.ones(3)/3)
active = s.kronecker_product(active, s.eye(2))
plus = (I-s.I*A)/2
L = -s.I*B
Q = L**3-L**2-21*L+9*I
need(active.rank() == 6 and (active*plus).rank() == 3, 'active ranks')
need((Q*active*plus).applyfunc(s.expand) == s.zeros(16), 'raw source cubic')
need(A*B == B*A and A*active == active*A and B*active == active*B, 'active invariance')
print('PASS boundary observability and cubic on raw source matrices')

X = s.Matrix([[0,1],[1,0]])
Y = s.Matrix([[0,-s.I],[s.I,0]])
Z = s.diag(1,-1)
Tx = X/(2*s.I)-Z/2
Ty = Y/(2*s.I)-Z/2
z, mass = s.symbols('z mass', nonzero=True)
nx, ny = 3, 2


def local_cylinder(phase):
    H = s.zeros(2*nx*ny)
    for x in range(nx):
        for y in range(ny):
            a = 2*(x*ny+y)
            H[a:a+2,a:a+2] += mass*Z
            b = 2*(((x+1)%nx)*ny+y)
            f = phase if x == nx-1 else 1
            H[b:b+2,a:a+2] += f*Tx
            H[a:a+2,b:b+2] += (1/f)*Tx.conjugate().T
            if y+1 < ny:
                b = a+2
                H[b:b+2,a:a+2] += Ty
                H[a:a+2,b:b+2] += Ty.conjugate().T
    return H


Rx = s.zeros(nx)
for j in range(nx):
    Rx[j,nx-1-j] = 1
V = s.kronecker_product(Rx,s.kronecker_product(s.eye(ny),X))
need(s.simplify(V*local_cylinder(z)*V+local_cylinder(1/z)) == s.zeros(12), 'general phase reflection')
need(V**2 == s.eye(12), 'general phase involution')
print('PASS independently assembled symbolic QWZ cylinder with general seam phase')
print('CERTIFICATE VALID: finite source identities; no physical/global identification.')
