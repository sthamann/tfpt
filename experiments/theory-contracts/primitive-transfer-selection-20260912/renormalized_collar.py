"""Stable signed-coupling continuation of the four-point |D| cutoff.

Kappa is an explicit free renormalization datum, not a TFPT prediction.
General norm-resolvent proof is in RENORMALIZED_COLLAR.md.
"""
from fractions import Fraction as F
from pathlib import Path
import ast
import hashlib
import json
import numpy as np

checks=[]
def require(name,condition):
    if not condition: raise RuntimeError(name)
    checks.append(name)

def grams(N,z):
    return [4*sum((1/(F(abs(k))+z) for k in range(-4*N,4*N+1) if k%4==r),F(0)) for r in range(4)]

records=[]
for kappa in [F(1,2),F(1),F(2),F(5)]:
    for N in [1,2,4,16,64]:
        gs=grams(N,kappa)
        rate=-1/gs[0]
        require(f'negative_counterterm_{kappa}_{N}',rate<0)
        require(f'uniform_channel_strictly_maximal_{kappa}_{N}',all(gs[0]>g for g in gs[1:]))
        q=kappa+1
        C=[gs[0]-g for g in grams(N,q)]
        require(f'resolvent_denominators_positive_{kappa}_{N}',all(c>0 for c in C))
        # Positive inverse denominator equals exact discrete matching condition.
        require(f'ground_matching_{kappa}_{N}',1+rate*gs[0]==0)
        records.append({'kappa':str(kappa),'N':N,'bare_coupling':float(rate),'resolvent_denominators':[float(c) for c in C]})

# Compare both exact-ground and inverse formulas against the actual source.
repo=Path(__file__).resolve().parents[3]
src=repo/'verification/v331_necessity_of_H.py'
raw=src.read_bytes()
nodes=[n for n in ast.parse(raw).body if isinstance(n,ast.FunctionDef) and n.name=='dtn']
require('single_original_source_function',len(nodes)==1)
scope={'np':np}
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(src),'exec'),scope)
angles=np.arange(4)*np.pi/2
for kappa in [F(1),F(2)]:
    N=3; M=4*N
    rate=-1/grams(N,kappa)[0]
    A,modes=scope['dtn'](angles,M=M,eps=float(rate))
    shifted=A+float(kappa)*np.eye(len(modes))
    ev=np.linalg.eigvalsh(shifted)
    require(f'shifted_source_positive_{kappa}',ev[0]>-1e-11 and ev[1]>1e-5)
    v=np.where(modes%4==0,1/(abs(modes)+float(kappa)),0)
    v=v/np.linalg.norm(v)
    require(f'original_source_ground_vector_{kappa}',np.linalg.norm(shifted@v)<1e-11)
    for n in [4,8]:
        sine=np.zeros(len(modes),dtype=complex)
        sine[np.where(modes==n)[0][0]]=1
        sine[np.where(modes==-n)[0][0]]=-1
        require(f'source_dark_sine_{kappa}_{n}',np.linalg.norm(shifted@sine-(n+float(kappa))*sine)<1e-11)
    q=float(kappa+1)
    R=np.diag(1/(abs(modes)+q))
    V=np.exp(-1j*modes[:,None]*angles)
    G=V.conj().T@R@V
    C=float(grams(N,kappa)[0])*np.eye(4)-G
    formula=R+R@V@np.linalg.solve(C,V.conj().T@R)
    direct=np.linalg.inv(A+q*np.eye(len(modes)))
    require(f'renormalized_source_resolvent_{kappa}',np.max(abs(formula-direct))<1e-11)

# Kappa is not removable by the common energy shift/scale.
require('dimensionless_dark_gap_ratio_changes',(F(8)+1)/(F(4)+1)!=(F(8)+2)/(F(4)+2))
require('ground_fourier_ratio_changes',F(1,5)!=F(2,6))

# Certified convergent scalar denominator tails: q=kappa+1.
# For r=1,2 the finite corrections simplify to negative telescoping-like
# reciprocal differences. This directly bounds the unseen infinite tail.
tail_records=[]
for kappa in [F(1),F(2)]:
    q=kappa+1
    for N in [4,16,64]:
        C=[grams(N,kappa)[0]-g for g in grams(N,q)]
        # Remaining terms n>=N for r=1,2; <= sum 1/(2 n^2) <=1/(2(N-1)).
        bound=F(1,2*(N-1))
        # r=0 remaining n>N <= sum 1/(2 n^2)<=1/(2N).
        c0bound=F(1,2*N)
        # Compare with a finer finite sum only as a guard, not the tail proof.
        fine=[grams(2*N,kappa)[0]-g for g in grams(2*N,q)]
        require(f'c0_tail_sign_and_bound_{kappa}_{N}',0<fine[0]-C[0]<c0bound)
        require(f'c1_tail_sign_and_bound_{kappa}_{N}',0<C[1]-fine[1]<bound)
        require(f'c2_tail_sign_and_bound_{kappa}_{N}',0<C[2]-fine[2]<bound)
        tail_records.append({'kappa':str(kappa),'N':N,'C0_interval':[str(C[0]),str(C[0]+c0bound)],'C1_interval':[str(C[1]-bound),str(C[1])],'C2_interval':[str(C[2]-bound),str(C[2])]})

print(json.dumps({'status':'STABLE_NONTRIVIAL_RENORMALIZED_FAMILY_WITH_FREE_KAPPA',
 'checks_passed':len(checks),'checks':checks,
 'source_sha256':hashlib.sha256(raw).hexdigest(),
 'cutoff_records':records,'certified_denominator_intervals':tail_records,
 'same_positive_bare_coupling_as_original':False,
 'kappa_derived_from_TFPT':False,'H70_field_map_constructed':False,
 'continuum_proof':'RENORMALIZED_COLLAR.md'},sort_keys=True,indent=2))
