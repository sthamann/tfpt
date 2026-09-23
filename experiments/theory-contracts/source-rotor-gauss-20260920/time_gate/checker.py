#!/usr/bin/env python3
"""Exact charged-time consequence of the compatible gauge charge.

The conditional quarter-holonomy target and original clock matrices are
inherited. No additional Hamiltonian or native source is constructed.
"""
import argparse
from collections import Counter
from itertools import combinations, product
import hashlib
import json
from pathlib import Path
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'experiments/theory-contracts').is_dir())
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,default=HERE/'certificate.json')
args=parser.parse_args()
FILES=[
 'experiments/theory-contracts/source-rotor-gauss-20260920/PROOF.txt',
 'experiments/theory-contracts/source-dynamics-selection-20260920/controls.json',
 'experiments/theory-contracts/charged-source-time-audit-20260920/PROOF.txt',
 'experiments/theory-contracts/charged-source-time-audit-20260920/checker.py',
 'experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json',
 'experiments/theory-contracts/source-critical-local-fields-20260920/ERGEBNIS.md',
]
manifest=json.loads((HERE/'source_manifest.json').read_text())
for entry in manifest['files']:
    actual=hashlib.sha256((ROOT/entry['path']).read_bytes()).hexdigest()
    if actual != entry['sha256']:
        raise RuntimeError('Source drift: '+entry['path'])
if not set(FILES).issubset({entry['path'] for entry in manifest['files']}):
    raise RuntimeError('Missing source pin')
checks={}
def check(name, condition):
    checks[name]=bool(condition)
    if not checks[name]: raise RuntimeError(name)

data=json.loads((ROOT/FILES[1]).read_text())['basis']
n=S.Matrix(data['n']); z=S.Matrix(data['z'])
K=S.diag(*([1]*9+[-1])); g=K*n; a=n[:8,0]
q=S.ones(10,1); lam=S.symbols('lambda',real=True)
def F(r):
    t=a.dot(r)/2
    return S.Matrix(list(r)+[-t,t])-t*n
roots=[]
for i,j in combinations(range(8),2):
    for s,t in product((-1,1),repeat=2):
        r=S.zeros(8,1);r[i]=s;r[j]=t;roots.append(r)
for signs in product((-1,1),repeat=8):
    if signs.count(-1)%2==0: roots.append(S.Matrix(signs)/2)
clocks=json.loads((ROOT/FILES[4]).read_text())['clock_matrices']
C=S.Matrix(clocks['C']['vector']); J=S.Matrix(clocks['J']['vector'])
check('root_count',len(roots)==240 and len(set(map(tuple,roots)))==240)
check('actual_C_J_orthogonal',C.T*C==J.T*J==S.eye(8))
check('actual_C_has_no_fixed_vector',(S.eye(8)-C).det()==1)
check('actual_C_J_preserve_same_root_set',all({tuple(h*r) for r in roots}==set(map(tuple,roots)) for h in (C,J)))
check('source_number_not_candidate_gauge',q!=g and q!=-g)
check('candidate_gauge_leaves_all_E8_currents_neutral',all(g.dot(F(r))==0 for r in roots))
energies=[S.Rational(1)-q.dot(F(r))/4 for r in roots]
check('inherited_root_energy_histogram',Counter(energies)=={S.Integer(0):1,S.Rational(1,2):56,S.Integer(1):126,S.Rational(3,2):56,S.Integer(2):1})
check('all_real_gauge_generator_shifts_leave_root_energies_unchanged',all(S.expand(lam*g.dot(F(r)))==0 for r in roots))
s=S.ones(8,1)/2
check('selected_spinor_has_charge_four',q.dot(F(s))==4)
check('clock_images_have_charge_zero',q.dot(F(C*s))==q.dot(F(J*s))==0)
check('clock_energy_difference_remains_one_for_all_lambda',all(S.expand((1-q.dot(F(h*s))/4+lam*g.dot(F(h*s)))-(1-q.dot(F(s))/4+lam*g.dot(F(s)))-1)==0 for h in (C,J)))
check('global_source_charge_is_not_trivial_on_retained_roots',set(q.dot(F(r)) for r in roots)=={-4,-2,0,2,4})
u=(n+z)/2; v=(n-z)/2
ps=S.Matrix(S.symbols('p0:8',real=True))
def T(p):
    t=a.dot(p)/2
    return S.Matrix(list(p)+[-t,t])
check('candidate_gauge_neutrality_of_T_for_all_real_p',S.expand(g.dot(T(ps)))==0)
spinors=[S.Matrix(signs)/2 for signs in product((-1,1),repeat=8) if signs.count(-1)%2==1]
fields=[T(p)+w for p in spinors for w in (u,v)]
check('all_256_c_spinor_representatives_integral_and_odd',len(spinors)==128 and len(fields)==256 and all(all(x.is_integer is True for x in f) and int((f.T*K*f)[0])%2==1 for f in fields))
check('all_c_spinor_families_have_gauge_charges_plus_minus_one',all(g.dot(T(p)+u)==1 and g.dot(T(p)+v)==-1 for p in spinors))
selected=S.Matrix([-1]+[1]*7)/2
check('actual_explicit_critical_fields_reproduced',T(selected)+u==S.Matrix([0,1,1,0,0,0,0,0,1,0]) and T(selected)+v==S.Matrix([0,1,1,0,0,0,0,0,0,1]))
check('bare_critical_n_z_pair_not_jointly_candidate_gauge_neutral',g.dot(n)==0 and g.dot(z)==2)
out={
 'verdict':'PASS_EXACT_CONDITIONAL_TIME_GATE',
 'research_verdict':'PARTIAL','checks':checks,'count':len(checks),
 'c_spinor_field_charges':{'x_R':1,'x_L':-1,'representatives':256},
 'root_energy_histogram':{str(k):v for k,v in sorted(Counter(energies).items())},
 'scope':{
  'inherited_time':'conditional eight-channel E8 H=L0-Q/4; not a newly derived source',
  'statement':'Adding any real multiple of the compatible gauge generator cannot repair the original C/J charged-time mismatch. The specified local odd c fields have charges +1/-1, while the bare critical z vertex has charge 2.',
  'not_claimed':['No general impossibility of a time-dependent clock lift','No microscopic gauging, phase selection, fermion origin, or TOE closure'],
  'review':'parent derivation and exact replay; not a new independent review of the full charged-time source'
 },
 'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in FILES},
 'manifest_verified':True,
 'manifest_sha256':hashlib.sha256((HERE/'source_manifest.json').read_bytes()).hexdigest(),
}
args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'count':len(checks),'all_passed':all(checks.values())}))
