#!/usr/bin/env python3
"""Independent checks of saved normalized readout and positivity counterexample.

Rebuilds compiler source; verifies the saved W and reduced matrices without
repeating their construction or the source graph-function AST extraction.
"""
import hashlib
import json
from pathlib import Path

import sympy as s

from seam_source import construct

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
r = json.loads((HERE/'clock_readout_results.json').read_text())


def need(ok, msg):
    if not ok:
        raise RuntimeError(msg)


def matrix(name):
    return s.Matrix([[s.sympify(v) for v in row] for row in r['data'][name]])


def zero(M):
    return M.applyfunc(s.simplify) == s.zeros(*M.shape)


for rel, sha in r['source_hashes'].items():
    need(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==sha, 'source hash: '+rel)
src = construct()
need(src['provenance']['source_sha256']==r['provenance']['source_sha256'], 'compiler hash')
A, B = s.Matrix(src['A16_dep']), s.Matrix(src['A_int'])
O = s.zeros(16)
for i,j in enumerate(src['img']):
    O[j,i] = 1
W, P = matrix('W'), matrix('P')
Ar, Br, Or, Ur = [matrix(k) for k in ('A12','B12','O12','U12')]
need(zero(W.T*W-s.eye(12)) and zero(W*W.T-P), 'saved isometry/projector')
need(zero(P*P-P) and P.rank()==12, 'rank twelve')
need(zero(B*(s.eye(16)-P)), 'discarded modes')
for full, red in ((A,Ar),(B,Br),(O,Or)):
    need(zero(full*W-W*red), 'source intertwiner')
need(zero(Ur.T-Ur) and zero(Ur**2-s.eye(12)), 'saved reflection')
need(zero(Ur*Ar*Ur+Ar) and zero(Ur*Br*Ur+Br), 'source reversal')
need(zero(Ur*Or*Ur-Or.T), 'clock reversal')
need(s.Matrix.hstack(s.eye(16)[:,:10],B[:,:10]).rank()==12, 'minimal carrier-generated closure')
print('PASS saved isometry, reducing source intertwiners, reflection and minimality')

z = s.symbols('z')
need(s.expand(Or.charpoly(z).as_expr()-(z-1)**6*(z+1)**2*(z*z+z+1)**2)==0, 'clock character polynomial')
P0 = sum((Or**k for k in range(6)),s.zeros(12))/6
Pm = sum(((-1)**k*Or**k for k in range(6)),s.zeros(12))/6
Pt = s.eye(12)-P0-Pm
need([p.rank() for p in (P0,Pm,Pt)]==[6,2,4], 'clock ranks')
need(zero(Br*Pm+Ar*Pm) and zero(Br*Pt-(Or-Or.T)*Pt), 'clock energy blocks')
need(s.simplify(s.trace(Or*(-s.I*Br)))==6*s.I, 'clock-sensitive trace')
print('PASS full source clock sectors and exact energy dependence')

# An exact three-pair core suffices for the graph-map counterexample.
# The source extractor retains cross-channel blocks and removes diagonal ones.
# Input covariance eigenvalues are exactly 1/20 and 19/20; output has -1/10.
J = s.Matrix([[0,1],[-1,0]])
R = s.eye(3)-2*s.ones(3)/3
Ac = s.Rational(9,10)*s.kronecker_product(R,J)
need(Ac**2==-s.Rational(81,100)*s.eye(6), 'faithful input control')
Cin = (s.eye(6)+s.I*Ac)/2
need(set(Cin.eigenvals())=={s.Rational(1,20),s.Rational(19,20)}, 'input spectrum')
Ag = s.zeros(6)
for i in range(3):
    for j in range(3):
        if i!=j:
            Ag[2*i:2*i+2,2*j:2*j+2]=Ac[2*i:2*i+2,2*j:2*j+2]
Cg = (s.eye(6)+s.I*Ag)/2
eg = Cg.eigenvals()
need(s.Rational(-1,10) in eg and s.Rational(11,10) in eg, 'graph positivity failure')
print('PASS exact faithful-input / negative-output graph counterexample')
print('CERTIFICATE VALID: finite normalized readout, not a global or physical identification.')
