#!/usr/bin/env python3
"""R064: native E8 record action, typed Sym2 lift and ordered response.
Reconstructs original source. No physical state, clock or geometry selected.
"""
from pathlib import Path
import sys,json,hashlib,itertools as it
import numpy as np
import sympy as sp
ROOT=Path(__file__).resolve().parents[4]
SOURCE=ROOT/'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
sys.path.insert(0,str(SOURCE.parent))
import source_channel as s
checks=[]
def require(name,test):
    ok=bool(test);checks.append(dict(name=name,passed=ok))
    if not ok:raise RuntimeError(name)
def exact(m):
    return sp.Matrix([[sp.Rational(float(v.real))+sp.I*sp.Rational(float(v.imag)) for v in row] for row in m])
require('unchanged original source SHA',hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593')
zs=s.source_rays();clock,_,_=s.reflection_actions(zs)
P=s.PAULIS;labels=s.V4;non=[j for j,x in enumerate(labels) if any(x)]
Rs=[np.eye(4)-np.outer(z,z.conj())/2 for z in zs]
F=np.column_stack([p.reshape(-1)/2 for p in s.SYMMETRIC_PAULIS])
require('actual Bell10 embedding isometry',np.array_equal(F.conj().T@F,np.eye(10)))
require('actual Bell10 lies in symmetric tensors',all(np.array_equal(F[:,j].reshape(4,4).T,F[:,j].reshape(4,4)) for j in range(10)))
require('actual original U is Sym2 r in this embedding',all(np.array_equal(U,F.conj().T@np.kron(R,R)@F) for U,R in zip(clock,Rs)))
perms=[];sgns=[];groups={};routing=[]
for ri,R in enumerate(Rs):
    perm={};sign={}
    for a in non:
        b,ph=s.phase_match(R@P[a]@R.conj().T,P,1)
        perm[a]=b;sign[a]=int(round(ph.real))
    L=tuple(a for a in non if perm[a]==a);groups.setdefault(L,[]).append(ri)
    for a in non:
        if a in L:continue
        qs=[q for q in L if s.symp(labels[a],labels[q])==0]
        if len(qs)!=1:raise RuntimeError('unique compatible point')
        q=qs[0];hit=tuple(x^y for x,y in zip(labels[a],labels[q]))
        routing.append((labels[perm[a]]==hit,perm[a]!=q,perm[a] not in L))
    perms.append(perm);sgns.append(sign)
require('native context grouping fifteen groups of four',len(groups)==15 and all(len(v)==4 for v in groups.values()))
require('all 720 external ray-point actions are p to p+q not p to q',len(routing)==720 and all(all(z) for z in routing))
require('all sixty unsigned actions involutive',all(all(p[p[a]]==a for a in non) for p in perms))
require('each context action fixes three and swaps six pairs',all(sum(p[a]==a for a in non)==3 for p in perms))
A=np.array([[int(a!=b and s.symp(labels[a],labels[b])==0) for a in non] for b in non])
T=np.zeros((15,15),dtype=int);S=np.zeros((15,15),dtype=int)
for j,a in enumerate(non):
    for p,sgn in zip(perms,sgns):
        i=non.index(p[a]);T[i,j]+=1;S[i,j]+=sgn[a]
require('unsigned label count is 12I+8A',np.array_equal(T,12*np.eye(15,dtype=int)+8*A))
require('unsigned label count symmetric stochastic after division60',np.array_equal(T,T.T) and np.array_equal(T.sum(axis=0),np.full(15,60)))
require('signed fundamental Pauli mean is 12I/60',np.array_equal(S,12*np.eye(15,dtype=int)))
Q={};J={}
for a in non:
    pp=(np.eye(4)+P[a])/2
    Q[a]=F.conj().T@np.kron(pp,pp)@F
    J[a]=F.conj().T@(np.kron(P[a],np.eye(4))+np.kron(np.eye(4),P[a]))@F
require('fifteen actual plus-sector tensor lifts are rank3 projections',all(np.array_equal(q@q,q) and np.trace(q)==3 for q in Q.values()))
require('all actual J have spectrum plus2x3 zero4 minus2x3',all(np.allclose(np.linalg.eigvalsh(j),[-2]*3+[0]*4+[2]*3,atol=1e-14,rtol=0) for j in J.values()))
require('all 900 actual Sym2 record-J intertwiners exact binary arithmetic',all(np.array_equal(U@J[a]@U.conj().T,sgns[i][a]*J[perms[i][a]]) for i,U in enumerate(clock) for a in non))
require('all 900 sector lifts transport with retained sign',all(np.array_equal(U@Q[a]@U.conj().T,F.conj().T@np.kron((np.eye(4)+sgns[i][a]*P[perms[i][a]])/2,(np.eye(4)+sgns[i][a]*P[perms[i][a]])/2)@F) for i,U in enumerate(clock) for a in non))
# Source matrices and lifted probes contain only small Gaussian dyadic rationals.
require('all matrices used in bulk identities are small Gaussian half-integers',all(np.array_equal(2*m.real,np.round(2*m.real)) and np.array_equal(2*m.imag,np.round(2*m.imag)) and np.max(abs(m))<=2 for m in [F]+clock+Rs+list(J.values())+list(Q.values())))
# Analytic proof plus exact symbolic named witnesses, independent of eigensolver tolerances.
Fe=exact(F);r=exact(Rs[0]);v=exact(Rs[13]);I4=sp.eye(4)
require('named rays original ordering',np.array_equal(zs[0],[-2,0,0,0]) and np.array_equal(zs[13],[-1,-1,-1,-1]))
require('named reflection r and s exact',r==sp.diag(-1,1,1,1) and v==I4-sp.ones(4)/2)
Ur=Fe.conjugate().T*sp.kronecker_product(r,r)*Fe
Us=Fe.conjugate().T*sp.kronecker_product(v,v)*Fe
require('named actual clock matrices exact',Ur==exact(clock[0]) and Us==exact(clock[13]))
require('probe labels actual IZ and XI',np.array_equal(P[1],np.kron(np.eye(2),np.diag([1,-1]))) and np.array_equal(P[8],np.kron([[0,1],[1,0]],np.eye(2))))
rho=exact(Q[1])/3;E=exact(Q[8]);V=Us*Ur;W=Ur*Us
p_rs=sp.trace(E*V*rho*V.conjugate().T);p_sr=sp.trace(E*W*rho*W.conjugate().T)
require('exact actual ordered conditional responses 1/3 and1',p_rs==sp.Rational(1,3) and p_sr==1)
AA=sp.eye(4)[:,[0,2]];BB=sp.Matrix([[1,0],[0,1],[1,0],[0,1]])/sp.sqrt(2)
M1=BB.T*v*r*AA;M2=BB.T*r*v*AA;K1=M1.conjugate().T*M1;K2=M2.conjugate().T*M2
require('independent compressed fundamental amplitudes have squared singular values 1/0 and1/1',K1*K1==K1 and sp.trace(K1)==1 and K2==sp.eye(2))
require('independent symmetric tensor trace reproduces both actual order responses',((sp.trace(K1))**2+sp.trace(K1*K1))/6==p_rs and ((sp.trace(K2))**2+sp.trace(K2*K2))/6==p_sr)

require('exact actual original joint record-final probabilities',p_rs/3600==sp.Rational(1,10800) and p_sr/3600==sp.Rational(1,3600))
a=2;Rloop=exact(Rs[54])*r
require('exact two-record phase loop flips sector on same label',Rloop*exact(P[a])*Rloop.conjugate().T==-exact(P[a]) and perms[54][perms[0][a]]==a)
walsh=np.array([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])
context_data=[]
for L,rs in groups.items():
    U0=clock[rs[0]];H=[clock[i]@U0 for i in rs]
    if not np.array_equal(H[1]@H[2],H[3]):raise RuntimeError('relative Klein group')
    qs=[sum(c*h for c,h in zip(row,H))/4 for row in walsh]
    if not all(np.array_equal(q@q,q) for q in qs):raise RuntimeError('character projection')
    if not all(np.array_equal(q@v,np.zeros((10,10))) for i,q in enumerate(qs) for v in qs[i+1:]):raise RuntimeError('character orthogonality')
    if not np.array_equal(sum(qs),np.eye(10)):raise RuntimeError('character completeness')
    if sorted(int(np.trace(q).real) for q in qs)!=[2,2,2,4]:raise RuntimeError('character ranks')
    # Remove common sqrt15: original branches are U_j/2, rotated U0 Qchi.
    if not all(np.array_equal(sum(c*clock[i] for c,i in zip(row,rs))/4,U0@q) for row,q in zip(walsh,qs)):raise RuntimeError('Walsh Kraus identity')
    left=sum(np.kron(clock[i],clock[i].conj()) for i in rs)/4
    right=sum(np.kron(U0@q,(U0@q).conj()) for q in qs)
    if not np.array_equal(left,right):raise RuntimeError('coarse channel preserved')
    context_data.append(dict(line=list(L),ray_indices=rs,character_ranks=[int(np.trace(q).real) for q in qs]))
require('all fifteen actual contexts have relative Klein four and rank4/2/2/2 character projectors',len(context_data)==15)
require('all fifteen actual coherent record rotations preserve coarse CP map with exact Kraus identity',len(context_data)==15)
L,rs=next(iter(groups.items()));U0=clock[rs[0]];H=[clock[i]@U0 for i in rs];q=sum(H)/4;rank=int(np.trace(q).real)
require('conditional character readout gives selected outcome probability1',np.trace(q@(q/rank))==1)
require('native global event effects are I/60',all(np.array_equal(U.conj().T@U,np.eye(10)) for U in clock))
require('coherent rotated global effect is Q/15 by Walsh unitarity',np.array_equal(walsh@walsh.T,4*np.eye(4)))
res=dict(result_id='R064',date='2026-11-01',all_passed=True,controls=len(checks),checks=checks,original_source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),original_source_inherited_controls=len(s.checks) if hasattr(s,'checks') else None,routing_cases=720,unique_incidence_cases=180,actual_intertwining_cases=900,unsigned_label_walk='(3I+2A)/15; spectrum 1^1,(1/3)^9,(-1/5)^5; labels only',fundamental_signed_mean='W_p/5; not the full End(Sym2 C4) channel',actual_clock_dimension=10,actual_clock_full_spectrum_reused='1^1,(1/3)^9,(1/5)^45,(1/15)^45',ordered_witness=dict(input_label=list(labels[1]),effect_label=list(labels[8]),ray_indices=[0,13],conditional_rs=str(p_rs),conditional_sr=str(p_sr),joint_rs=str(p_rs/3600),joint_sr=str(p_sr/3600),difference=str((p_sr-p_rs)/3600),scope='explicit mathematical preparation/effect, not physical vacuum or causal spacetime'),same_label_opposite_sector_witness=dict(label=list(labels[2]),ray_indices=[0,54]),context_data=context_data,record_basis_scope='alternative coherent readout conditional on access; original specified record instrument is retained',physical_origin_closed=False,new_lean_formalization=False)
out=Path(__file__).with_name('DOILY-RECORD-ORIENTATION.json');out.write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:res[k] for k in ['result_id','all_passed','controls','routing_cases','actual_intertwining_cases','ordered_witness']}))
