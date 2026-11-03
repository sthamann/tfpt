#!/usr/bin/env python3
"""Actual existing W tensor and exact finite-path 16th order evaluation.

Retains all other native modes. At the minimum sixteen pair-creation steps,
the specified initial boson population permits only channels0 and30. This
is coefficient extraction in the full H, not a new truncated Hamiltonian.
"""
from pathlib import Path
from hashlib import sha256
from math import factorial
from collections import Counter
import json
import runpy
import sympy as S

ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
OUT=Path(__file__).resolve().parent
SRC=ROOT/'experiments/theory-contracts/universalraum-keyD-native-instruments-20260915/native_source.py'
ns=runpy.run_path(str(SRC))
W,PAIRS,BETA=ns['W'],ns['PAIRS'],ns['BETA']
pair_action=ns['pair_action']
lookup={pair:j for j,pair in enumerate(PAIRS)}
def Q(A,i,j):
    return int(W[A,lookup[(i,j)]]) if i<j else (-int(W[A,lookup[(j,i)]]) if j<i else 0)
x,y=S.symbols('x y')
M=S.Matrix(16,16,lambda s,t:x*Q(0,4*s,4*t+1)+y*Q(30,4*s,4*t+1))
if M != x*S.Matrix(BETA[0])+y*S.Matrix(BETA[5]): raise RuntimeError('Original W/beta mismatch')
det=S.factor(M.det())
if det!=x**8*y**8: raise RuntimeError('Original minor determinant')
nnz=[(A,i,j,int(W[A,k])) for A in range(60) for k,(i,j) in enumerate(PAIRS) if W[A,k]]
if any(i%4==j%4 for A,i,j,w in nnz): raise RuntimeError('Same family pair present')

# Exact coefficient of H^16 on the specified normalized states. Track actual
# native interleaved64-mode bit ordering and integer boson b|n>=n|n-1>.
terms=[(A,pair,int(W[A,k])) for A in (0,30) for k,pair in enumerate(PAIRS) if W[A,k]]
state={(0,8,8):1}
layer_sizes=[]
for step in range(16):
    nxt={}
    for (mask,n0,n30),amp in state.items():
        for A,pair,w in terms:
            nb=n0 if A==0 else n30
            if not nb: continue
            hit=pair_action(mask,pair,dagger=True)
            if hit is None: continue
            key=(hit[0],n0-int(A==0),n30-int(A==30))
            nxt[key]=nxt.get(key,0)+amp*w*hit[1]*nb
    state={k:v for k,v in nxt.items() if v}
    layer_sizes.append(len(state))
target=sum((1<<(4*s))+(1<<(4*s+1)) for s in range(16))
integer_coefficient=state.get((target,0,0),0)
normalized=integer_coefficient//factorial(8)
if integer_coefficient != factorial(16)*factorial(8)**2:
    raise RuntimeError('Full native pair path sign/coefficient failed')

sources=[SRC,ROOT/'experiments/theory-contracts/source-native-retarded-selection-20260922/PROOF.md',
ROOT/'experiments/theory-contracts/source-static-register-20260920/SOURCE_INTERACTION_INVENTORY.txt']
result={'result_id':'R109','verdict':'declared_larger_native_source_executed_not_primitive_H_adm',
 'W_nonzero':len(nnz),'same_family_nonzero':0,
 'cross_edges_per_family':[sum((i%4==c)!=(j%4==c) for A,i,j,w in nnz) for c in range(4)],
 'endpoint_degrees':dict(Counter(sum(i==k or j==k for A,i,j,w in nnz) for k in range(64))),
 'selected_family':0,'rest_fermion_modes':48,'boson_modes':60,
 'boson_channels':[0,30],'beta_ranks':[S.Matrix(BETA[k]).rank() for k in (0,5)],
 'actual_W_minor_determinant':str(det),'native_path_layer_sizes':layer_sizes,
 'sixteenth_power_normalized_matrix_element_coefficient':normalized,
 'expected_16factorial_8factorial':factorial(16)*factorial(8),
 'coupling_monomial':'gbar^16', 'conserved_Q_initial':32,'conserved_Q_final':32,
 'H_F0_as_rest_operator':0,'Hn_F0_zero_orders':list(range(16)),
 'first_nonzero_open_Hpower':16,
 'dyson_leading_coefficient':'8!*gbar^16*((1-exp(-Delta*tau))/Delta)^16',
 'next_coupling_order':18,
 'scope':'Actual declared W-bank only. No scalar bath replacement, no spatial lattice/site source invented. First Dyson coefficient, not full propagator.',
 'primitive_H_adm_F0':None,'primitive_status':'not_computed',
 'source_hashes':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in sources}}
(OUT/'native-sixteen-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('actual_W_minor_determinant','native_path_layer_sizes','sixteenth_power_normalized_matrix_element_coefficient','expected_16factorial_8factorial','dyson_leading_coefficient','primitive_status')},indent=2))
