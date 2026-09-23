from common import ROOT,D,OUT
import json,itertools
from pathlib import Path
import sympy as s
A=[s.Matrix(a) for a in D['bilinear_maps']];R=s.Matrix(D['integral_triality']['vector_basis'])
G=[]
for a in A:
 m=s.zeros(16);m[:8,8:]=a.T;m[8:,:8]=a;G.append(m)
r=s.Matrix([1,-1,0,0,0,0,0,0]);t=s.Matrix([0,1,-1,0,0,0,0,0])
def cl(v):return sum((v[i]*G[i] for i in range(8)),s.zeros(16))
U=cl(r)*cl(t)/2
sub=[tuple(c) for k in [0,2,4] for c in itertools.combinations(range(5),k)];ix={x:i for i,x in enumerate(sub)}
perm=[1,2,0,3,4];W=s.zeros(16)
for j,c in enumerate(sub):
 d=[perm[k] for k in c];sign=(-1)**sum(d[a]>d[b] for a in range(len(d)) for b in range(a+1,len(d)))
 W[ix[tuple(sorted(d))],j]=sign
x=s.Symbol('x')
out={'geometric_spin_lift_trace':str(s.trace(U)),'native_D5_carrier_weyl_trace':str(s.trace(W)), 'geometric_polynomial':str(s.factor(U.charpoly(x).as_expr())),'native_polynomial':str(s.factor(W.charpoly(x).as_expr())),'geometric_order_three':U**3==s.eye(16),'native_order_three':W**3==s.eye(16),'source_root_coordinates':[[str(z) for z in R.inv()*v] for v in [r,t]],'decision':'NO_INTERTWINER_FOR_THIS_ORIGINAL_D5_WEYL_ACTION: neither lift sign has native trace','scope':'Refutes identification of root-space Spin8 lift with native carrier action for the same A2/D5 Weyl element; not abstract Spin10 representation equivalence.'}
if s.trace(U)!=-8 or s.trace(W)!=4 or U**3!=s.eye(16) or W**3!=s.eye(16):raise RuntimeError('Weyl witness failed')
if s.trace(U)==s.trace(W) or -s.trace(U)==s.trace(W):raise RuntimeError('lift sign removes mismatch')
(OUT/'weyl.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
