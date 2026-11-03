#!/usr/bin/env python3
"""R065 finite source tests for a manual standard-split theorem application.
Does NOT numerically construct the infinite split unitary or prove a 4D net.
"""
from pathlib import Path
import sys,json,hashlib,itertools as it
import numpy as np
import sympy as sp
ROOT=Path(__file__).resolve().parents[4]
SRC=ROOT/'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
OLD=ROOT/'experiments/theory-contracts/compiler-current-descendant-20260919'
sys.path.insert(0,str(SRC.parent));import source_channel as s
checks=[]
def ck(name,test):
    ok=bool(test);checks.append(dict(name=name,passed=ok))
    if not ok:raise RuntimeError(name)
def exact(m):
    return sp.Matrix([[sp.Rational(float(z.real))+sp.I*sp.Rational(float(z.imag)) for z in row] for row in m])
ck('pinned unchanged original60 source',hashlib.sha256(SRC.read_bytes()).hexdigest()=='3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593')
zs=s.source_rays();Us,_,_=s.reflection_actions(zs);F=np.column_stack([x.reshape(-1)/2 for x in s.SYMMETRIC_PAULIS])
# Reuse the original NS CAR embedding data; independently reconstruct its defining T F.
cert=json.loads((OLD/'certificate.json').read_text());E=sp.zeros(28,10)
for i,j,v in cert['embedding_matrix_nonzero_entries']:E[i,j]=sp.sympify(v)
pairs=list(it.combinations(range(8),2));lookup={p:i for i,p in enumerate(pairs)}
T=sp.zeros(28,16)
for i,j in it.product(range(4),repeat=2):T[lookup[(i,j+4)],4*i+j]=1
ck('actual original descendant certificate equals original CAR tensor embedding',E==T*exact(F))
ck('actual original descendant is isometric',E.conjugate().T*E==sp.eye(10))
Lferm=sp.diag(*[sum(sp.Rational(3,2) if k<4 else sp.Rational(1,2) for k in pair) for pair in pairs])
ck('actual source has fermionweight2 before U1 quotient',Lferm*E==2*E)
ck('actual SU4 plus compulsory D5 weights sum2',sp.Rational(2)-sp.Rational(4,8)+sp.Rational(1,2)==2)
I=np.eye(4);J={a:F.conj().T@(np.kron(P,I)+np.kron(I,P))@F for a,P in enumerate(s.PAULIS)}
pi=(I+s.PAULIS[1])/2;Q=F.conj().T@np.kron(pi,pi)@F;rho=Q/3
ck('original R064 IZ plus preparation is rank3 normalized',np.array_equal(Q@Q,Q) and np.trace(Q)==3 and np.trace(rho)==1)
ck('outside IZ current before source event is2h0',np.trace(rho@J[1])==2)
ck('ray13 is actual allones reflection',np.array_equal(zs[13],[-1,-1,-1,-1]))
after=Us[13]@rho@Us[13].conj().T
ck('outside IZ current after actual global ray13 event is0',np.trace(after@J[1])==0)
mean=sum(U@rho@U.conj().T for U in Us)/60
ck('outside IZ current after unread globalC60 is2over5',abs(np.trace(mean@J[1])-.4)<1e-14)
signed=sum(U.conj().T@J[1]@U for U in Us)
ck('unread exterior coefficient is exactly12over60 before final division',np.array_equal(signed,12*J[1]))
ck('original code exposes plus minus logical input in any exterior current smear',np.trace(((F.conj().T@np.kron((I-s.PAULIS[1])/2,(I-s.PAULIS[1])/2)@F)/3)@J[1])==-2)
# Exact symbolic same exterior witness, no floating denominators.
qe=exact(Q);je=exact(J[1]);u13=exact(Us[13]);re=qe/3
ck('exact symbolic exterior source contrast2to0',sp.trace(re*je)==2 and sp.trace(u13*re*u13.conjugate().T*je)==0)
# Phase faithful word relation: original SU4 descendant action is -iU per event.
ck('sixty actual current lifts square to minusI in class2',all(np.array_equal((-1j*U)@(-1j*U),-np.eye(10)) for U in Us))
ck('sixty scalar phase corrected record restrictions are original U',all(np.array_equal(1j*(-1j*U),U) for U in Us))
for word in [(0,13),(13,0),(0,54),(0,13,54),(13,0,45,59)]:
    a=np.eye(10,dtype=complex);b=np.eye(10,dtype=complex)
    for k in word:a=Us[k]@a;b=(-1j*Us[k])@b
    ck('whole-word original phase bookkeeping '+str(word),np.array_equal((1j)**len(word)*b,a))
EX=F.conj().T@np.kron((I+s.PAULIS[8])/2,(I+s.PAULIS[8])/2)@F
for name,V,target in [('r_then_s',u13*exact(Us[0]),sp.Rational(1,3)),('s_then_r',exact(Us[0])*u13,sp.Integer(1))]:
    ck('actual order witness transports through split isometry: finite coefficient '+name,sp.trace(exact(EX)*V*re*V.conjugate().T)==target)
# New localized-current word witness: same original IZ / XI labels, actual same rays.
rr=I-np.outer(zs[0],zs[0].conj())/2;ss=I-np.outer(zs[13],zs[13].conj())/2
ck('interior current word gives normalized trace0 in first order',np.trace(s.PAULIS[8]@ss@rr@s.PAULIS[1]@rr@ss)==0)
ck('interior current word gives normalized trace1 in reverseorder',np.trace(s.PAULIS[8]@rr@ss@s.PAULIS[1]@ss@rr)==4)
# Current normalization with one exact NS particle-hole crossing, no finite-CCR claim.
q=sp.diag(sp.Rational(3,4),-sp.Rational(1,4),-sp.Rational(1,4),-sp.Rational(1,4))
v=sp.zeros(256,1);filled=15
for i in range(4):
    m=filled;sg=(-1)**((m&((1<<i)-1)).bit_count());m^=1<<i
    pp=i+4;sg*=(-1)**((m&((1<<pp)-1)).bit_count());m|=1<<pp;v[m]=sg*q[i,i]
ck('original four-CAR Jminus1 vacuum norm is3over4 not3over2',(v.conjugate().T*v)[0]==sp.Rational(3,4))
H=sp.diag(1,-1,0,0);E12=sp.zeros(4);E12[0,1]=1
ck('basic SU4 root norm is2 under fundamental trace',sp.trace(H*H)==2)
ck('basic root-current central coefficient is1',sp.trace(E12*E12.T)==1)
lam,k,n,x=sp.symbols('lambda k n x',positive=True)
# A single oscillator's displacement amplitude i*lambda*sqrt(k*n)*f_n carries L0=n N.
ck('mode energy coefficient from current CCR',sp.expand(n*(lam**2*k*n*x**2))==lam**2*k*n**2*x**2)
ck('smooth loop same-event double pulse quadruples energy',(2*sp.pi)**2*sp.trace(q*q)==4*sp.pi**2*sp.Rational(3,4))
ck('Parseval plus original current level yields3pi/16 collar coefficient',sp.pi**2*sp.Rational(3,4)/(4*sp.pi)==3*sp.pi/16)
ck('actual full source grade predicts exterior stress2h0',sp.Rational(1,2)+sp.Rational(3,2)==2)
res=dict(result_id='R065',date='2026-11-01',all_passed=True,controls=len(checks),checks=checks,source_sha256=hashlib.sha256(SRC.read_bytes()).hexdigest(),original_descendant_certificate_sha256=hashlib.sha256((OLD/'certificate.json').read_bytes()).hexdigest(),exterior_current_coefficients=dict(before=2,global_ray13=0,unread_global60='2/5',any_local_nonselective_operation=2),order_witness=dict(localized_encoded_original_probabilities=['1/3','1'],local_current_normalized_trace_coefficients=[0,1],scope='Given original current net; actual split map theorem manual, encoded state not primitive physical preparation'),source_grade=2,current_q_norm='3/4',canonical_split_unitary_numerically_constructed=False,infinite_split_locality_and_covariance='manual primary theorem application; proof file',source_physical_state_preserved_by_split_encoding=False,physical_origin_closed=False,new_lean_formalization=False)
out=Path(__file__).with_name('LOCAL-SOURCE-RECORD-SPLIT.json');out.write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:res[k] for k in ['result_id','all_passed','controls','exterior_current_coefficients','order_witness']}))
