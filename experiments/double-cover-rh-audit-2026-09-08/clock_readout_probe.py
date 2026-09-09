#!/usr/bin/env python3
"""Canonical normalized six-channel readout of the existing finite source.

Distinguishes the existing duad/Pfaffian extractor from a CAR covariance map.
No Hamiltonian changes, no prime/zero input, no global or physical promotion.
"""
import ast
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as s

from seam_source import construct

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CHECKS = []
DATA = {}


def check(name, ok):
    CHECKS.append({'name':name,'passed':bool(ok)})
    print(('PASS ' if ok else 'FAIL ')+name, flush=True)


def serial(M):
    return [[str(v) for v in row] for row in M.tolist()]


def err(M):
    return float(np.max(np.abs(M)))


def thermal(H, beta):
    e, V = np.linalg.eigh(H)
    return (V*(1/(1+np.exp(beta*e))))@V.conj().T


def modular(C):
    e, V = np.linalg.eigh(C)
    if not (e.min()>0 and e.max()<1):
        raise ValueError('Nonfaithful covariance; no clipping')
    return (V*np.log((1-e)/e))@V.conj().T


src = construct()
A, B = s.Matrix(src['A16_dep']), s.Matrix(src['A_int'])
O = s.zeros(16)
for i,j in enumerate(src['img']):
    O[j,i] = 1
old = json.loads((HERE/'seam_geometry_results.json').read_text())
check('same_source_as_saved_reflection', old['provenance']['source_sha256']==src['provenance']['source_sha256'])
U = s.Matrix([[s.Rational(v) for v in row] for row in old['data']['reflection']['U']])
I16, I12 = s.eye(16), s.eye(12)
J = s.Matrix([[0,1],[-1,0]])
IO = s.Matrix(src['IOTA6'])

# Readout column order: averaged boundary pair first, then five carrier pairs,
# exactly matching the channel labels of the source's compress12 extractor.
L = s.zeros(16,12)
L[:10,2:] = s.eye(10)
L[10:,:2] = IO/3
G = L.T*L
W = L*s.diag(s.sqrt(3),s.sqrt(3),*([1]*10))
P = W*W.T
check('raw_mean_Gram_not_identity', G == s.diag(s.Rational(1,3),s.Rational(1,3),*([1]*10)))
check('normalized_readout_isometry_exact', W.T*W == I12 and P*P == P and P.rank()==12)
check('source_defined_range_carrier_plus_bright_boundary', P[:10,:10] == s.eye(10)
      and P[10:,10:] == IO*IO.T/3 and P[:10,10:]==s.zeros(10,6))
check('discarded_boundary_modes_decouple_exact', (I16-P).rank()==4 and B*(I16-P)==s.zeros(16))
check('readout_range_reduces_source_clock_and_reflection', all(P*M==M*P for M in (A,B,O,U)))
Ar, Br, Or, Ur = [(W.T*M*W).applyfunc(s.simplify) for M in (A,B,O,U)]
check('exact_source_intertwiners', all((M*W-W*Mr).applyfunc(s.simplify)==s.zeros(16,12)
      for M,Mr in ((A,Ar),(B,Br),(O,Or),(U,Ur))))
check('reduced_reflection_and_clock_exact', Ur*Ur==I12 and Or**6==I12
      and (Ur*Ar*Ur+Ar).applyfunc(s.simplify)==s.zeros(12)
      and (Ur*Br*Ur+Br).applyfunc(s.simplify)==s.zeros(12)
      and (Ur*Or*Ur-Or.T).applyfunc(s.simplify)==s.zeros(12))

z = s.symbols('z')
clock_poly = s.factor(Or.charpoly(z).as_expr())
check('all_source_clock_characters_retained', clock_poly==(z-1)**6*(z+1)**2*(z*z+z+1)**2)
Pi0 = sum((Or**k for k in range(6)),s.zeros(12))/6
Pim = sum(((-1)**k*Or**k for k in range(6)),s.zeros(12))/6
Pitri = I12-Pi0-Pim
check('clock_sector_ranks_6_2_4', [Q.rank() for Q in (Pi0,Pim,Pitri)]==[6,2,4])
check('nontrivial_clock_restriction_exact', (Br*Pim+Ar*Pim).applyfunc(s.simplify)==s.zeros(12)
      and (Br*Pitri-(Or-Or.T)*Pitri).applyfunc(s.simplify)==s.zeros(12))
moments = [s.simplify(s.trace(Or**k*(-s.I*Br))) for k in range(6)]
check('nonconstant_clock_twisted_energy_moments', moments==[0,6*s.I,-6*s.I,0,6*s.I,-6*s.I])

# The earlier marked-space obstruction survives this exact reducing readout.
PB = s.diag(1,1,*([0]*10))
P3 = s.diag(*([0]*2+[1]*6+[0]*4))
P2 = I12-PB-P3
triangle = s.simplify(s.trace(P3*Br*P2*Br*PB*Br))
check('marked_triangle_obstruction_survives', triangle==-36)

# Load the exact source function, rather than replace its intended graph map
# by our isometry. It explicitly suppresses all channel-diagonal blocks.
source_path = Path(src['provenance']['source'])
tree = ast.parse(source_path.read_text())
main = next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main')
f = next(n for n in main.body if isinstance(n,ast.FunctionDef) and n.name=='compress12')
env = {'np':np,'IOTA6':src['IOTA6'],'CH':src['CH'],
       'CH2':{i:[2*i,2*i+1] for i in range(6)},
       'DUADS_CH':list(itertools.combinations(range(6),2))}
exec(compile(ast.fix_missing_locations(ast.Module(body=[f],type_ignores=[])),str(source_path),'exec'),env)
graph_map = env['compress12']
Ag = graph_map(np.array(A,float))
Bg = graph_map(np.array(B,float))
check('graph_map_discards_bare_onsite', np.array_equal(Ag,np.zeros((12,12))) and Ar!=s.zeros(12))
check('graph_and_covariance_boundary_scalings_differ', err(Bg[:2,2:]-np.tile(np.eye(2),(1,5)))<1e-14
      and Br[:2,2:4]==s.sqrt(3)*s.eye(2))
check('raw_mean_not_unital', L.T*(I16/2)*L != I12/2 and W.T*(I16/2)*W==I12/2)

# Faithful, C6-invariant Gaussian covariance counterexample to using the
# graph extractor as a physical covariance map. This does not invalidate
# the source's intended duad/Pfaffian use.
R = s.eye(3)-2*s.ones(3)/3
Actrl = s.Rational(9,10)*s.diag(s.kronecker_product(R,J),s.kronecker_product(s.eye(5),J))
check('graph_control_is_faithful_CAR_and_C6', Actrl.T==-Actrl and Actrl**2==-s.Rational(81,100)*I16 and Actrl*O==O*Actrl)
Cctrl = np.array((I16+s.I*Actrl)/2,complex)
Agraph = graph_map(np.array(Actrl,float))
Cgraph = (np.eye(12)+1j*Agraph)/2
Wn = np.array(W,float)
Cphysical = Wn.T@Cctrl@Wn
eg, ep = np.linalg.eigvalsh(Cgraph), np.linalg.eigvalsh(Cphysical)
check('graph_covariance_counterexample_outside_0_1', abs(eg.min()+.1)<1e-12 and abs(eg.max()-1.1)<1e-12)
check('normalized_covariance_control_stays_physical', ep.min()>.049 and ep.max()<.951)

# At a reducing subspace, unlike an arbitrary compression, functional calculus
# commutes with the readout. No numerical eigenvalue clipping is used.
An, Bn, On, Un = [np.array(M,complex) for M in (A,B,O,U)]
Arn, Brn, Orn, Urn = [np.array(M,complex) for M in (Ar,Br,Or,Ur)]
rows=[]
for u,t in ((1,0),(1,.125),(.5,.2),(1,.4)):
    H=-1j*(u*An+t*Bn)
    Hr=-1j*(u*Arn+t*Brn)
    for beta in (.5,1,2):
        C=thermal(H,beta)
        Cr=Wn.T@C@Wn
        rows.append({'u':u,'t':t,'beta':beta,
            'covariance_reduction':err(Cr-thermal(Hr,beta)),
            'modular_reduction':err(modular(Cr)-beta*Hr),
            'reflected_covariance':err(Urn@Cr@Urn+Cr-np.eye(12)),
            'clock_covariance':err(Orn@Cr-Cr@Orn)})
check('reducing_readout_functional_calculus_12_samples', max(max(r[k] for k in
      ('covariance_reduction','modular_reduction','reflected_covariance','clock_covariance')) for r in rows)<1e-10)

# Full spectrum formula: active cubic plus the two nontrivial clock sectors.
roots=np.sort(np.roots([1,-1,-21,9]).real)
spectra=[]
for u,t in ((1,.125),(.5,.2),(1,.4)):
    expected=np.sort(np.array([sgn*(u+t*x) for x in roots for sgn in (-1,1)]
       +[u+s3*np.sqrt(3)*t for s3 in (-1,1)]
       +[-u+s3*np.sqrt(3)*t for s3 in (-1,1)]+[u-t,-u+t]))
    actual=np.linalg.eigvalsh(-1j*(u*Arn+t*Brn))
    spectra.append(err(actual-expected))
check('full_twelve_dimensional_spectrum_reproduced', max(spectra)<1e-11)

# Port minimality under the explicitly fixed demand: retain every carrier
# direction, and close under B. B immediately adds exactly the bright boundary.
Carrier=s.eye(16)[:,:10]
K=s.Matrix.hstack(Carrier,B*Carrier)
check('minimal_reducing_extension_of_full_carrier_rank_12', K.rank()==12 and P*K==K)

DATA = {'W':serial(W),'P':serial(P),'A12':serial(Ar),'B12':serial(Br),'O12':serial(Or),'U12':serial(Ur),
    'clock_character_multiplicities_r0_to_r5':[6,0,2,2,2,0],
    'clock_polynomial':str(clock_poly),'twisted_B_energy_moments':list(map(str,moments)),
    'graph_covariance_counterexample':{'input_eigenvalues':[.05,.95],
        'output_min':float(eg.min()),'output_max':float(eg.max()),
        'physical_readout_min':float(ep.min()),'physical_readout_max':float(ep.max()),
        'scope':'graph extractor is not a covariance channel; its intended Pfaffian/duad use remains untouched'},
    'thermal_grid':rows,'spectrum_residuals':spectra,
    'minimality_scope':'smallest B-invariant subspace retaining all ten carrier components; not minimum among arbitrary measurements',
    'selection_rule_scope':'a linear equivariant amplitude map from a trivial-clock port has fixed-space image; no claim excluding arbitrary global invariant measurements',
    'status':'canonical normalization of existing source channel stack; common physical TFPT/QWZ representation and arithmetic identification remain open'}
result={'passed':sum(c['passed'] for c in CHECKS),'total':len(CHECKS),'checks':CHECKS,'data':DATA,
    'provenance':src['provenance'],
    'source_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in (Path(__file__),HERE/'seam_source.py',HERE/'seam_geometry_results.json')},
    'versions':{'numpy':np.__version__,'sympy':s.__version__}}
(HERE/'clock_readout_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(f"{result['passed']}/{result['total']} passed. FINITE READOUT ONLY.")
raise SystemExit(0 if result['passed']==result['total'] else 1)
