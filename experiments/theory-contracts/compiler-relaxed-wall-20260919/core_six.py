"""Exact candidate native invariant six-bond block; stage-one symbolic audit."""
import itertools as it
import json
from pathlib import Path
import sympy as s
import numpy as np
from scipy.linalg import eigh

states=list(it.permutations(range(3))) # 0=L(outer Omega1),1=Phi2,2=R(outer Omega4)
n=len(states);index={p:i for i,p in enumerate(states)}
def swap(p,a,b):
    q=list(p);q[a],q[b]=q[b],q[a];return tuple(q)
def trans(a,b):
    M=s.zeros(n)
    for j,p in enumerate(states):M[index[swap(p,a,b)],j]=1
    return M
S01,S02,S12=trans(0,1),trans(0,2),trans(1,2)
I=s.eye(n)
K3=I/30+2*(S01+S02+S12)/15-(S01*S12+S12*S01)/15
parts=[s.zeros(n) for _ in range(4)]
for j,p in enumerate(states):
    posL=p.index(0);posP=p.index(1);posR=p.index(2)
    if posL!=0:
        parts[0][j,j]+=s.Rational(4,5)
        parts[0][index[swap(p,0,posL)],j]-=s.Rational(1,5)
    if posP in(0,1):parts[1][j,j]=s.Rational(1,2)
    else:parts[1][:,j]=(I-K3)[:,j]
    parts[2][:,j]=((4*I-S12)/5)[:,j]
    if posR!=2:
        parts[3][j,j]+=s.Rational(4,5)
        parts[3][index[swap(p,2,posR)],j]-=s.Rational(1,5)
H=sum(parts,s.zeros(n))
def cycles(p):
    seen=set();c=0
    for j in range(len(p)):
        if j in seen:continue
        c+=1;k=j
        while k not in seen:seen.add(k);k=p[k]
    return c
G=s.zeros(n)
for i,p in enumerate(states):
    for j,q in enumerate(states):
        rel=tuple(p.index(x) for x in q)
        G[i,j]=s.Rational(4)**(cycles(rel)-3)
if G*H!=H.T*G:raise RuntimeError('not Hermitian in packet Gram')
if any(G*h!=h.T*G for h in parts):raise RuntimeError('local mismatch')
x=s.symbols('x')
print('states',states)
print('H',H)
print('G',G)
print('charpoly',s.factor(H.charpoly(x).as_expr()))
print('eig',sorted([float(s.re(v)) for v in s.nroots(H.charpoly(x).as_expr())]))
print('G eig',G.eigenvals())
print('core expectation', (G*H)[0,0])
print('core variance', (G*H*H)[0,0]-(G*H)[0,0]**2)
result={'states':states,'H':str(H),'Gram':str(G),'charpoly':str(s.factor(H.charpoly(x).as_expr())),
        'eigenvalues_numeric':[float(s.re(v)) for v in s.nroots(H.charpoly(x).as_expr())]}
Q=s.zeros(6)
for j,p in enumerate(states):Q[index[tuple(2-v for v in p[::-1])],j]=1
if Q.T*G*Q!=G:raise RuntimeError('reflection Gram')
values,vectors=eigh(np.array(G*H,dtype=float),np.array(G,dtype=float))
v=vectors[:,0]
eta=float(v @ np.array(G*Q,dtype=float) @ v)
result.update({'reflection':str(Q),'ground_coefficients':v.tolist(),
               'relaxed_middle_hopping_over_mu':-eta/8,
               'relaxed_middle_overlap_eta':eta,
               'end_middle_energy_difference':float(s.Rational(1,2)+(8-s.sqrt(19))/5)-values[0]})
print('eta',eta,'hop/mu',-eta/8,'v',v)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
