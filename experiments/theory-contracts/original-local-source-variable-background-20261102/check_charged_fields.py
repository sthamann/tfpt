#!/usr/bin/env python3
"""Exact evaluation of GIVEN charged lattice fields, not a new physical model.

No writes to original sources. V0 and Vc remain distinct. Canonical mirror
embedding and primitive H_adm coefficient are explicitly NOT manufactured.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from hashlib import sha256
import json
import sympy as S

ROOT = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
OUT = Path(__file__).resolve().parent
K = S.diag(*([1]*9+[-1]))
n = S.Matrix([1,1,1,-1,-1,-1,-1,-1,-1,3])
z = S.Matrix([0]*8+[1,-1])
a = n[:8,0]
u,v = (n+z)/2,(n-z)/2
Vc = K+2*K*v*v.T*K
Y = S.Matrix([-S.Rational(1,3)]*3+[S.Rational(1,2)]*2+[0]*3+[1,1])
def T(p):
    k=(a.T*p)[0]/2
    return S.Matrix(list(p)+[-k,k])
def B(x,y): return (x.T*K*y)[0]
def cocycle(x,y):
    return S.Integer(-1)**int(sum(x[i]*y[j] for i in range(10) for j in range(i)))
def weights(x,V):
    dim=(x.T*V*x)[0]/2
    spin=B(x,x)/2
    return [(dim+spin)/2,(dim-spin)/2]
def serial(x):
    if isinstance(x,S.MatrixBase): return [serial(t) for t in x]
    if isinstance(x,S.Basic): return int(x) if x.is_Integer else str(x)
    if isinstance(x,dict): return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [serial(v) for v in x]
    return x

# ONE already named bar4 family weight (+++). This is an algebraic component,
# not a selected physical family state. All sixteen D5 weights are retained.
ps=[S.Matrix([S.Rational(j,2) for j in signs+(1,1,1)])
    for signs in product((-1,1),repeat=5) if signs.count(-1)%2==1]
xs=[T(p)+u for p in ps]
ys=[T(p)+v for p in ps]
if len(xs)!=16 or not all(t.is_Integer for x in xs+ys for t in x):
    raise RuntimeError('Original integral sixteen-component branch failed')
if not all(B(x,x)==3 for x in xs): raise RuntimeError('Spinor-u norm')
if not all(weights(x,Vc)==[S.Rational(3,2),0] for x in xs):
    raise RuntimeError('Original Vc weights')
if not all(weights(x,Vc)==[1,S.Rational(1,2)] for x in ys):
    raise RuntimeError('Original Vc v-dressed weights')

# Two literal original vertices, already chiral at the unmodified V0.
p=S.Matrix([1,-1,1,1,1,1,1,1])/2
q=S.Matrix([-1,1,1,1,1,1,1,1])/2
literal_x,literal_xp=T(p)+u,T(q)+u
x,xp=literal_x,literal_xp
if list(x)!=[1,0,1,0,0,0,0,0,1,0]: raise RuntimeError('Literal x')
if list(xp)!=[0,1,1,0,0,0,0,0,1,0]: raise RuntimeError('Literal xprime')
if B(x,xp)!=2 or x[-1]!=0 or xp[-1]!=0: raise RuntimeError('Original OPE test')

# Exact original lattice-vertex mode witness, with Y(e_x,z)=sum A_m z^-m-1.
# x^2=3, B(x,xp)=2, r=xp-x. On |r>, A_1 vanishes because B=-1
# has no z^-2 coefficient. B_0|r>=eps(-xp,r)|-x>, and A_1|-x>
# reads the z^1 coefficient above its z^-3 leading term, namely x(-1)|0>.
# Thus {A_1,B_0}|r> !=0 for distinct components, without choosing Vc.
r=xp-x
if B(x,r)!=-1 or B(-xp,r)!=-1 or B(-xp,xp)!=-3:
    raise RuntimeError('Exact lattice mode exponents')
osc=cocycle(-xp,r)*cocycle(x,-x)*x
if osc==S.zeros(10,1): raise RuntimeError('Mode witness vanished')

rows=[]
for p,x,y in zip(ps,xs,ys):
    rows.append({'p':p,'x_u':x,'x_v':y,'V0_u':weights(x,S.eye(10)),
                 'V0_v':weights(y,S.eye(10)), 'Vc_u':weights(x,Vc),
                 'q':sum(x),'Y':Y.dot(x)})
srcs=[
 'experiments/theory-contracts/source-critical-local-fields-20260920/local_modules/PROOF.md',
 'experiments/theory-contracts/source-critical-local-fields-20260920/local_modules/check_local_modules.py',
 'experiments/theory-contracts/source-critical-local-fields-20260920/energy_bridge/PROOF.md',
 'experiments/theory-contracts/source-sector-reconstruction-20260920/PROOF.txt',
 'experiments/theory-contracts/source-dynamics-selection-20260920/PROOF.txt']
result={
 'result_id':'R109', 'verdict':'given_charged_fields_evaluated_not_primitive_mirror_embedding',
 'family_weight':[1,1,1], 'given_lattice':'Z^(9,1)', 'fields':rows,
 'V0_u_weights':dict(Counter(tuple(map(str,weights(x,S.eye(10)))) for x in xs)),
 'V0_v_weights':dict(Counter(tuple(map(str,weights(y,S.eye(10)))) for y in ys)),
 'u_branch_total_lattice_charge':sum(xs,S.zeros(10,1)),
 'u_branch_total_original_number':sum(sum(x) for x in xs),
 'u_branch_total_hypercharge':sum(Y.dot(x) for x in xs),
 'literal_vertex_pair':{'x':literal_x,'xp':literal_xp,'Bself':B(literal_x,literal_x),'Bcross':B(literal_x,literal_xp),
   'same_component_OPE_pole':3,'different_component_OPE_pole':2,
   'nonzero_root':literal_x-literal_xp,'mode_input_charge':r,
   'anticommutator_A1_B0_output_oscillator':osc,
   'scope':'Exact UV lattice vertex modes. They are not canonical independent CAR generators. Other smearings, dressed/IR maps not excluded.'},
 'primitive_H_adm_F0':None, 'primitive_H_adm_status':'not_computed',
 'source_hashes':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in srcs}}
result=serial(result)
(OUT/'charged-field-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('V0_u_weights','V0_v_weights','u_branch_total_lattice_charge','u_branch_total_original_number','u_branch_total_hypercharge','literal_vertex_pair','primitive_H_adm_status')},ensure_ascii=False,indent=2))
