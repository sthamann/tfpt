"""Exact origin test, without modifying the TFPT source or Atlas.

Question: do a free seam deck, the RR 3+2 charge decomposition and the actual
finite native W tensor select the square four-mark configuration?

The analytic argument covers the entire family D_t={1,-1,t,-t}, |t|=1,
t != +/-1.  The code checks the identities and one exact nonsquare witness.
It does not construct or compare completed primitive P1 sources.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
from pathlib import Path
import sys
import numpy as np
import sympy as s

ROOT = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
ORIGINAL = ROOT / 'experiments/theory-contracts/rr-continuous-clock-20260921'
spec = importlib.util.spec_from_file_location('rr_original', ORIGINAL / 'checker.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def need(v, text):
    if not v:
        raise RuntimeError(text)

z, t = s.symbols('z t', nonzero=True)
P = s.expand((z*z-1)*(z*z-t*t))
need(s.expand(P.subs(z,-z)-P)==0, 'deck preserves every divisor in the family')
quarter_defect=s.expand(P.subs(z,s.I*z)-P)
need(s.factor(quarter_defect)==2*z*z*(t*t+1), 'whole family quarter obstruction')
cr=s.cancel(4*t/(1+t)**2)
j=s.factor(256*(cr*cr-cr+1)**3/(cr*cr*(1-cr)**2))
tw=(1+s.I*s.sqrt(3))/2
jw=s.simplify(s.expand_complex(j.subs(t,tw)))
need(jw==s.Rational(35152,9), 'nonsquare witness j')
need(s.simplify(j.subs(t,s.I))==1728, 'original square j')
need(s.simplify(tw*s.conjugate(tw))==1, 'witness marks lie on original seam circle')

# The adapted RR carrier basis puts all three even modes first.
g=np.diag([1,1,1,-1,-1]).astype(np.int64)
y6=np.array([-2,-2,-2,3,3],dtype=np.int64)
with np.load(ORIGINAL/'native_tensor.npz',allow_pickle=False) as src:
    W=np.rint(src['W'].real).astype(np.int64)
    masks=src['even_masks']
need(W.shape==(60,2016) and np.count_nonzero(W)==480,'original native W')
Gs=m.exterior_even_finite(g,masks)
# Actual half-turn on the four marked points in their cyclic order.
F=np.zeros((4,4),dtype=np.int64)
for a in range(4): F[(a+2)%4,a]=1
U=np.kron(Gs,F)
UF=np.zeros((6,6),dtype=np.int64)
for col,(a,b) in enumerate(m.FAMILY_PAIRS):
    aa,bb=(a+2)%4,(b+2)%4
    UF[m.FAMILY_PAIR_INDEX[tuple(sorted((aa,bb)))],col]=1 if aa<bb else -1
B=np.kron(np.block([[g,np.zeros_like(g)],[np.zeros_like(g),g]]),UF)
target=np.empty_like(W)
for col,(a,b) in enumerate(m.FERMION_PAIRS):
    aa=int(np.flatnonzero(U[:,a])[0]); bb=int(np.flatnonzero(U[:,b])[0])
    coeff=int(U[aa,a]*U[bb,b])*(1 if aa<bb else -1)
    target[:,col]=coeff*W[:,m.FERMION_PAIR_INDEX[tuple(sorted((aa,bb)))]]
mismatch=int(np.count_nonzero(target-B@W))
need(mismatch==0,'actual finite native W deck intertwining')

spin_y6=[sum(y6[k] for k in range(5) if (int(mask)>>k)&1) for mask in masks]
need(sorted(spin_y6)==[-4]*3+[-3]*2+[0]+[1]*6+[2]*3+[6], 'whole spinor charges')
result={
    'status':'PASS_SCOPED',
    'family':'D_t={1,-1,t,-t}; |t|=1; t!=+/-1',
    'quarter_polynomial_defect':str(quarter_defect),
    'cross_ratio':str(cr),
    'j_invariant':str(j),
    'witness_t':str(tw),
    'witness_j':str(jw),
    'square_j':1728,
    'carrier_parity_dimensions':[3,2],
    'W_nonzero_coefficients':int(np.count_nonzero(W)),
    'W_entries_compared':int(W.size),
    'W_deck_intertwining_mismatches':mismatch,
    'outcome':'free deck plus RR parity/charges and finite W covariance do not select square modulus',
    'not_claimed':['full P1 countermodel','primitive RP source equivalence','same physical state/time','native quartic-event P2 identification','new discovery of square rigidity or original RR bridge'],
}

# Natural puncture root/weight sequence. All four meridians have the SAME
# discriminant charge; a cyclic permutation does not translate glue sectors.
ones=s.ones(4,1)
N=s.eye(4)-ones*ones.T/4
roots=s.Matrix([[1,0,0],[-1,1,0],[0,-1,1],[0,0,-1]])
C=roots.T*roots
Gw=(N[:,:3].T*N[:,:3])
need(C.det()==4 and Gw.det()==s.Rational(1,4),'root and weight determinants')
need((N[:,0].T*N[:,0])[0]==s.Rational(3,4),'fundamental meridian norm')
for k in range(4):
    coords=C.inv()*roots.T*(N[:,k]-N[:,0])
    need(all(q.q==1 for q in coords),'all mark weights same discriminant coset')
index_matrix=N[:,:3].gauss_jordan_solve(roots)[0]
need(abs(index_matrix.det())==4,'A3 root index in puncture weight lattice')
result['puncture_root_weight_connection']={
    'H1':'Z4 / Z(1,1,1,1) = A3* with mark counting metric',
    'H_cohomology_1':'ker(sum:Z4->Z) = A3 with mark counting metric',
    'root_determinant':str(C.det()),
    'weight_determinant':str(Gw.det()),
    'index_root_in_weight':str(abs(index_matrix.det())),
    'meridian_norm_squared':'3/4',
    'mark_meridian_discriminant_classes':'all four equal generator [omega1]',
    'cyclic_mark_action_on_discriminant':'identity, not a four-sector translation',
    'D5_spinor_plus_A3_meridian_norm_squared':'5/4 + 3/4 = 2',
}

# Compare with the ACTUAL original simple-current vector, not an invented E8
# embedding. Original v983 already proves the complete four-coset census.
sys.path.insert(0,str(ROOT/'verification'))
gspec=importlib.util.spec_from_file_location('original_v983',ROOT/'verification/v983_simple_current_generator.py')
gm=importlib.util.module_from_spec(gspec)
gspec.loader.exec_module(gm)
need(s.Matrix(gm.OMEGA_F)==N[:,0], 'actual original v983 family weight is meridian m0')
mixed=[]
for signs in itertools.product((-1,1),repeat=5):
    if sum(a==-1 for a in signs)%2: continue
    spin=[s.Rational(a,2) for a in signs]
    for k in range(4):
        root=spin+list(N[:,k])
        need(sum(v*v for v in root)==2,'mixed original root norm')
        need(gm.in_L0([root[a]-gm.LAM[a] for a in range(9)]), 'mixed root in actual original first glue coset')
        mixed.append(tuple(root))
need(len(set(mixed))==64,'16 actual spinor weights times4 actual meridians')
need(gm.in_L0([4*v for v in gm.LAM]),'original glue order divides4')
need(all(not gm.in_L0([k*v for v in gm.LAM]) for k in (1,2,3)),'original glue exact order4')
result['actual_original_glue_identification']={
    'source':'verification/v983_simple_current_generator.py',
    'meridian_m0_equals_original_OMEGA_F':True,
    'first_coset_mixed_roots_checked':len(mixed),
    'lambda_norm_squared':str(sum(v*v for v in gm.LAM)),
    'lambda_discriminant_order':4,
    'uniform_meridian_map':'gamma_i -> [m_i]=1 mod4; sum of four images is0',
    'root_census_reused_not_rerun':[52,64,60,64],
}
print(json.dumps(result,indent=2,sort_keys=True))
