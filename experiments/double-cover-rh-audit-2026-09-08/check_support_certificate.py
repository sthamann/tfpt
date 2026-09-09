#!/usr/bin/env python3
"""Independent exact support projector and response-premise certificate.

Uses the shared compiler extractor. Identifies the support from the exact
nullspace rather than from the main probe's spectral polynomial construction.
"""
import hashlib
import json
from pathlib import Path

import sympy as s

from seam_source import construct

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
r=json.loads((HERE/'interaction_support_results.json').read_text())


def need(ok,msg):
    if not ok:
        raise RuntimeError(msg)


for rel,sha in r['source_hashes'].items():
    need(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==sha,'source hash: '+rel)
src=construct()
need(src['provenance']['source_sha256']==r['provenance']['source_sha256'],'compiler source hash')
A,B=s.Matrix(src['A16_dep']),s.Matrix(src['A_int'])
I=s.eye(16)
K=s.Matrix.hstack(*B.nullspace())
need(K.cols==4,'kernel dimension')
P=I-K*(K.T*K).inv()*K.T
need(P**2==P and P.T==P and P*B==B and P.rank()==12,'support from nullspace')
old=json.loads((HERE/'clock_readout_results.json').read_text())
Pold=s.Matrix([[s.sympify(v) for v in row] for row in old['data']['P']])
need(P==Pold,'same previously normalized readout')
poly=B**10+47*B**8+634*B**6+2046*B**4+1701*B**2
need(P==-poly/243,'polynomial projector')
need((P*B).rank()==P.rank() and (I-P)*B==s.zeros(16),'no null modes on selected support')
print('PASS support from exact kernel equals prior readout and polynomial')

# Response proof hypotheses and its algebraic prefactor at the bare axis.
need(A.T==-A and B.T==-B and A**2==-I and A*B==B*A,'commuting normal source')
a=s.symbols('a',real=True)
C0=(I+s.I*a*A)/2
need((C0*(I-C0)-(1-a*a)*I/4).applyfunc(s.expand)==s.zeros(16),'Fermi response prefactor')
need(B.rank()==12 and (A+B/8).rank()==16,'interaction versus Hamiltonian support')
print('PASS source hypotheses and exact linear-response prefactor identity')

# Verify the proposed small input port generates the same support; use B only,
# whereas the main probe closes under A,B,O,O^T. Both source pair components
# are included in this real CAR port.
seed=s.Matrix.hstack(I[:,:2],I[:,6:8])
span=s.Matrix.hstack(*[B**k*seed for k in range(6)])
need(span.rank()==12 and P*span==span,'two-orbit seed support')
print('PASS two source channel pairs generate the interaction support')

t=s.symbols('t')
gap=s.Poly(1+t-21*t*t-9*t**3,t)
need(gap.count_roots(0,s.oo)==1 and gap.count_roots(s.Rational(23,100),s.Rational(24,100))==1,'first gap interval')
print('PASS exact positive-gap root interval')
print('CERTIFICATE VALID: finite candidate-source interaction support; physical parent not established.')
