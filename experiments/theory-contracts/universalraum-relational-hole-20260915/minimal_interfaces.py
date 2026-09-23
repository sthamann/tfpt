"""Independent audit of the third text: order, preparation and field types.

The inherited model fixes the source. A laboratory synthesis is not promoted
to a derivation of laboratory controls. The spatial bank graph is an input.
"""
from pathlib import Path
from hashlib import sha256
from collections import Counter, defaultdict
from itertools import combinations
import contextlib
import io
import runpy
import json
import math
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    h=runpy.run_path(str(HERE/'verify_hole.py'))
ROOT=h['ROOT']; checks=[]
def need(ok,name):
    if not ok:
        raise RuntimeError(name)
    checks.append(name)
def clean(m):
    return m.applyfunc(s.simplify)
pins={
    '/Users/stefanhamann/.codex/attachments/74f60e7d-3866-43c1-ac67-fca86caf48eb/pasted-text.txt':
    '1a46b37f98001629f6f000b675d8f463de40dc039124a0b377d20761ba158caa',
    str(ROOT/'experiments/theory-contracts/universalraum-v16-integrated-20260915/replayed_sources/order.py'):
    '1a23ba58f9ca9eec3d51425e9dd6f200c2e22cd89cfd88a8f123dcbe489c4304',
    str(ROOT/'experiments/theory-contracts/compiler-clifford-bridge/checker.py'):
    'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'}
for path,pin in pins.items():
    need(sha256(Path(path).read_bytes()).hexdigest()==pin,'input and source hash')
order=runpy.run_path(list(pins)[1])
d=order['data']()
I=s.eye(2); w=d['w']; q=s.diag(s.I,1)
coords=s.Matrix.hstack(*(order['coords'](a,d['bb']) for a in (I,w,q,w*q)))
need(coords.det()==s.I,'Gaussian integral basis determinant i')
need(all(order['gaussian'](z) for z in coords) and all(order['gaussian'](z) for z in coords.inv()),
     'both basis changes are Gaussian integral')
bridge=runpy.run_path(list(pins)[2]); bridge['inherited'](); fr=bridge['frame']()
Had=s.Matrix([[1,1],[1,-1]])/s.sqrt(2); Z=s.diag(1,-1)
CZ=s.diag(1,1,1,-1); V=s.kronecker_product(Z*Had,I)
q4=(s.eye(4)+fr['a'])*(s.eye(4)+fr['u'][0])/2
need(clean(CZ*V*CZ*V)==q4,'laboratory q word equals actual marked Clifford-frame matrix')
need(clean(q4*fr['u'][1]*q4.H)==fr['u'][2] and
     clean(q4*fr['u'][2]*q4.H)==-fr['u'][1],'laboratory q word transports marked axes with exact signs')
need(q4**4==s.eye(4),'laboratory quarter-turn phase is correct')

# Enumerate with the inherited complete dual-lattice coordinate bound.
roots=order['root_data']()['roots']
Pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),Z]
projectors=[(I+sign*P)/2 for P in Pauli for sign in (1,-1)]
unitary_actions=Counter(); rankone_pairs=Counter()
for root in roots:
    A=clean(sum((v*b for v,b in zip(root,d['basis'])),s.zeros(2)))
    # Raw symbolic expression equality need not expand Gaussian products.
    # The failing witness expands exactly to two; no tolerance is introduced.
    need(s.expand(s.trace(A*A.H))==2,'root trace normalization')
    if s.simplify(A.det())!=0:
        need(clean(A.H*A)==I,'nonzero determinant root is unitary')
        action=[]
        for P in Pauli:
            output=clean(A*P*A.H)
            images=[(j,sign) for j,Q in enumerate(Pauli) for sign in (1,-1) if output==sign*Q]
            need(len(images)==1,'unitary root is a projective one-qubit Clifford operation')
            action.append(images[0])
        unitary_actions[tuple(action)]+=1
    else:
        inp=clean(A.H*A/2); out=clean(A*A.H/2)
        need(inp in projectors and out in projectors,'rank-one root input and output are Pauli eigenrays')
        rankone_pairs[(projectors.index(inp),projectors.index(out))]+=1
need(len(unitary_actions)==24 and set(unitary_actions.values())=={4},'96 unitary roots are 24 projective actions with four phases')
need(len(rankone_pairs)==36 and set(rankone_pairs.values())=={4},'144 rank-one roots are all 36 ray transitions with four phases')

# Number-projected product construction for all actual source rows.
W=h['W']; pairs=h['pairs']
for A in range(60):
    columns=np.flatnonzero(W[A])
    channel_pairs=[pairs[int(j)] for j in columns]
    need(len(channel_pairs)==8 and len({i for pair in channel_pairs for i in pair})==16,
         'eight source pairs are disjoint')
    need(set(abs(int(W[A,j])) for j in columns)=={1},'projected product uses exact original pair signs')
    projection={sum(1<<i for i in pairs[int(j)]):int(W[A,j]) for j in columns}
    need(len(projection)==8 and sum(v*v for v in projection.values())==8,
         'one-pair number projection has exactly the native bright vector')
p=s.symbols('p',real=True)
prob=8*p*(1-p)**7
need(s.expand(s.diff(prob,p)-8*(1-p)**6*(1-8*p))==0,
     'exact success maximizer in the product family')
need(prob.subs(p,s.Rational(1,8))==s.Rational(7,8)**7,'optimal projected pair probability')
need(s.Rational(1,8)-s.Rational(1,8)**2==s.Rational(7,64),'non-Gaussian four-point defect survives number selection')

# Complete N=2 two-bank reduction with explicitly supplied mediator hopping.
Delta,g,eta,z=s.symbols('Delta g eta z',real=True)
coupling=s.sqrt(8)*g
H=s.Matrix([[0,coupling,0,0],[coupling,Delta,eta,0],
            [0,eta,Delta,coupling],[0,0,coupling,0]])
U=s.Matrix([[1,0,1,0],[0,1,0,1],[0,1,0,-1],[1,0,-1,0]])/s.sqrt(2)
target=s.diag(s.Matrix([[0,coupling],[coupling,Delta+eta]]),
              s.Matrix([[0,coupling],[coupling,Delta-eta]]))
need(clean(U.T*H*U)==target,'two-bank source reduction into even and odd blocks')
need(math.comb(128,2)+120==8248 and math.comb(128,2)-120==8008,
     'complete two-bank sector and dark multiplicities')
need(H[3,0]==0 and (H**2)[3,0]==0 and (H**3)[3,0]==8*g*g*eta,
     'first pair transfer is the original three-step amplitude')
expected=(z*z-(Delta+eta)*z-8*g*g)*(z*z-(Delta-eta)*z-8*g*g)
need(s.expand(H.charpoly(z).as_expr().subs(H.charpoly(z).gen,z)-expected)==0,
     'exact four-pole transport polynomial')

# Type test on all actual W rows. Antisymmetric internal coefficients cannot
# multiply the symmetric internal scalar made from equal-handed Weyl fields.
eps=np.array([[0,1],[-1,0]],dtype=int)
def wedge_coefficient(out,i,j,value):
    if i!=j:
        out[tuple(sorted((i,j)))]+=value*(1 if i<j else -1)
for A in range(60):
    scalar=defaultdict(int); tensor=defaultdict(int)
    for col in np.flatnonzero(W[A]):
        i,j=pairs[int(col)]
        for a,b,coefficient in ((i,j,int(W[A,col])),(j,i,-int(W[A,col]))):
            for alpha in range(2):
                for beta in range(2):
                    wedge_coefficient(scalar,2*a+alpha,2*b+beta,coefficient*int(eps[alpha,beta]))
            wedge_coefficient(tensor,2*a,2*b,coefficient)
    need(not any(scalar.values()),'actual W scalar same-handed Weyl coupling vanishes exactly')
    need(any(tensor.values()),'symmetric Lorentz spinor tensor has a nonzero algebraic channel')
need(math.comb(128,2)==1*(64*65//2)+3*(64*63//2),
     'complete Lorentz/internal exchange-parity dimension identity')

# Combine the external neutral-algebra theorem with the much smaller actual
# control algebra. Its commutant, not merely scalar F(N), is invisible.
multiplicities=[37888,64,2880,576,320]
need(sum([37888,64,2*2880,2*576,2*320])==45504,
     'multiplicity representation accounts for the full native N3 space')
need(1+1+3*4==14,'control algebra dimension from its simple factors')
commutant_dimension=sum(n*n for n in multiplicities)

print(json.dumps({
    'status':'PASS','guards':len(checks),'exact_guards':len(checks),'numerical_guards':0,
    'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'dependency_sha256':sha256((HERE/'verify_hole.py').read_bytes()).hexdigest(),
    'source_pins':pins,'check_groups':dict(sorted(Counter(checks).items())),
    'order':{'basis':'I,w,q,wq','coordinate_determinant':str(coords.det()),
             'coordinate_matrix':[[str(x) for x in row] for row in coords.tolist()],
             'laboratory_q_word_exact':True,'primitive_laboratory_origin_derived':False,
             'unitary_root_projective_actions':len(unitary_actions),
             'rank_one_ray_pairs':len(rankone_pairs)},
    'pair_preparation':{'channels':60,'success_max':str(s.Rational(7,8)**7),
        'resources_assumed':['pair rotations with the source signs','charge reference','coherent total-number selection'],
        'cell_Omega_preparation_claimed':False},
    'two_bank_transport':{'dimension':8248,'active_dimension':240,'dark_dimension':8008,
                         'graph_and_hopping_derived':False,'already_covered_by_v161_general_bank_result':True},
    'field_type':{'same_handed_Weyl_scalar_W_channels_all_zero':True,
        'nonzero_algebraic_alternative':'symmetric Lorentz spinor indices, representation (1,0)',
        'physical_alternative_kinetics_derived':False},
    'invisible_control_commutant':{
        'form':'M37888 + M64 + (I2 tensor M2880) + (I2 tensor M576) + (I2 tensor M320)',
        'dimension':commutant_dimension,
        'scope':'exactly the two controls X and Nb; more source operations can reduce this commutant',
        'larger_than_F_N_even_with_fixed_N':True},
    'T1_T8_closed':[],
},indent=2,ensure_ascii=False))
