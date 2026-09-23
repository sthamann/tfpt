"""Check the exact raw v331 point-form obstruction and cutoff resolvent.

No writes. Extract only the inspected dtn function from pinned source syntax.
Finite numerical source checks are separate from the analytic proof in COLLAR_LIMIT.md.
"""
import ast
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import numpy as np

checks = []


def require(name, ok):
    if not ok:
        raise RuntimeError(name)
    checks.append(name)


def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)), F(0))


def coeffs(n):
    h = harmonic(n)
    return {4*sign*k:F(1,2*k)/h for k in range(1,n+1) for sign in [-1,1]}


def q0(v):
    return sum((abs(k)*a*a for k,a in v.items()),F(0))


sequence = []
for n in [1,2,4,16,64,128]:
    v = coeffs(n)
    h = harmonic(n)
    mass = sum((a*a for a in v.values()), F(0))
    require(f'all_four_point_values_one_N{n}', sum(v.values()) == 1 and all(k%4==0 for k in v))
    require(f'principal_form_N{n}', q0(v) == 2/h)
    require(f'L2_formula_N{n}', mass == sum((F(1,k*k) for k in range(1,n+1)),F(0))/(2*h*h))
    sequence.append({'N':n,'L2_squared':float(mass),'principal_energy':float(q0(v)), 'point_penalty_eps_2_over_5':1.6})
for n,m in [(1,2),(2,16),(4,64),(64,128)]:
    vn,vm = coeffs(n),coeffs(m)
    diff = {k:vn.get(k,F(0))-vm.get(k,F(0)) for k in set(vn)|set(vm)}
    require(f'difference_point_penalty_zero_{n}_{m}', sum(diff.values()) == 0)
    require(f'difference_energy_formula_{n}_{m}', q0(diff) == 2/harmonic(n)-2/harmonic(m))

repo = Path(__file__).resolve().parents[3]
source = repo/'verification/v331_necessity_of_H.py'
raw = source.read_text()
tree = ast.parse(raw)
fun = [node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name=='dtn']
require('single_source_dtn_function',len(fun)==1)
scope={'np':np}
exec(compile(ast.Module(body=fun,type_ignores=[]),str(source),'exec'),scope)
angles=np.arange(4)*np.pi/2
eps=0.4
for M in [4,8,14]:
    lam,modes=scope['dtn'](angles,M=M,eps=eps)
    exact=np.diag(abs(modes)).astype(float)+eps*4*((modes[:,None]-modes[None,:])%4==0)
    require(f'actual_source_matrix_M{M}',np.max(abs(lam-exact))<1e-12)
    R=np.diag(1/(abs(modes)+1))
    V=np.exp(-1j*modes[:,None]*angles[None,:])
    G=V.conj().T@R@V
    formula=R-R@V@np.linalg.solve(np.eye(4)/eps+G,V.conj().T@R)
    direct=np.linalg.inv(lam+np.eye(len(modes)))
    require(f'woodbury_actual_source_M{M}',np.max(abs(formula-direct))<1e-12)

diagnostics=[]
for M in [16,64,256,1024,4096]:
    modes=np.arange(-M,M+1)
    # Residue diagonalization avoids a (2M+1)-square matrix.
    g=np.array([4*np.sum(1/(abs(modes[modes%4==r])+1)) for r in range(4)])
    b=np.array([4*np.sum(1/(abs(modes[modes%4==r])+1)**2) for r in range(4)])
    diff_norm=float(np.max(b/(1/eps+g)))
    N=(M-3)//4
    lower=float(harmonic(N+1)-1)
    require(f'Gram_lower_bound_M{M}',float(min(g))>=lower)
    require(f'resolvent_bound_M{M}',diff_norm<=12/(1/eps+lower))
    diagnostics.append({'cutoff':M,'resolvent_difference_norm_numeric':diff_norm,'gram_min_numeric':float(min(g))})

# Working alternative: smoothing preserves square covariance, not uniqueness.
for r in [F(1,3),F(1,2)]:
    modes=range(-2,3)
    B=np.array([[float(F(abs(k),1) if k==l else 0)+float(F(2,5)*4*r**abs(k-l))*(int((k-l)%4==0)) for l in modes] for k in modes])
    rho=np.diag([1j**k for k in modes])
    require(f'smoothed_clock_covariance_{r}',np.max(abs(rho@B-B@rho))<1e-12)
    expected=[float(F(8,5)),float(F(13,5)),float(F(13,5)),float(F(18,5)-F(8,5)*r**4),float(F(18,5)+F(8,5)*r**4)]
    require(f'smoothed_spectrum_{r}',np.max(abs(np.linalg.eigvalsh(B)-sorted(expected)))<1e-12)

print(json.dumps({'status':'RAW_POINT_FORM_NONCLOSABLE_POSITIVE_CUTOFF_LIMIT_FREE',
 'source_sha256':hashlib.sha256(raw.encode()).hexdigest(),
 'checks_passed':len(checks),'checks':checks,'sequence':sequence,
 'numeric_resolvent_diagnostics':diagnostics,
 'general_proof':'COLLAR_LIMIT.md',
 'source_unchanged':True,'continuum_interacting_TFPT_derived':False,
 'all_TFPT_collar_models_excluded':False},sort_keys=True,indent=2))
