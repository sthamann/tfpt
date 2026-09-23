"""Exact bounded audit: overlap resources, CAR, and a native-W four-state path.

The shared-boson star is NOT a native W row. The native-W witness adds a
boson-only mixer and uses an explicitly prepared N=9 Pauli-blocked state;
it is neither the N=64 ground state nor transfer between independent banks.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import argparse
import contextlib
import io
import json
import runpy
import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
CONTRACT = HERE.parents[1]
TENSOR = CONTRACT / 'sources/repo/experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz'
checks = []

def need(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    checks.append(label)

def annihilator(mode, number=3):
    out = s.zeros(1 << number)
    for mask in range(1 << number):
        if mask & (1 << mode):
            out[mask ^ (1 << mode), mask] = (-1) ** ((mask & ((1 << mode)-1)).bit_count())
    return out

fx, fs, fy = [annihilator(i) for i in range(3)]
eye = s.eye(8)
ns = fs.T * fs
nx, ny = fx.T * fx, fy.T * fy
for K in (1, 2, 3):
    # Exact invariant K=N_b+n_s sector, not a cutoff of the CCR algebra.
    nb = K * eye - ns
    q = s.sqrt(K) * fs  # b^dagger s, represented in fixed K.
    c_dag = q / s.sqrt(K)
    c = c_dag.T
    modes = (fx, c, fy)
    for i, a in enumerate(modes):
        for j, b in enumerate(modes):
            need(a*b+b*a == s.zeros(8), f'K={K} CAR annihilator {i},{j}')
            need(a*b.T+b.T*a == (eye if i == j else s.zeros(8)), f'K={K} CAR mixed {i},{j}')
    nc = c_dag*c
    need(nb == (K-1)*eye+nc, f'K={K} exact boson number dictionary')
    native_charge = nx+ny+ns+2*nb
    need(native_charge == (2*K-1)*eye+nx+ny+nc, f'K={K} exact native charge offset')
    Qx, Qy = q*fx, q*fy
    need(Qy.T*Qx-Qx*Qy.T == K*fy.T*fx, f'K={K} overlap commutator is hopping')
    need(native_charge*(Qx+Qx.T) == (Qx+Qx.T)*native_charge, f'K={K} joint charge conservation')
    endpoint_parity = eye-2*nx
    need(endpoint_parity*Qx != Qx*endpoint_parity, f'K={K} endpoint parity already broken by overlap')

Pi_x,Pi_s,Pi_y = eye-2*nx,eye-2*ns,eye-2*ny
Pi_A,Pi_B = Pi_x*Pi_s,Pi_s*Pi_y
Pi_global = Pi_x*Pi_s*Pi_y
need(Pi_A*Pi_B == Pi_x*Pi_y, 'overlapping chart parity product cancels shared mode')
need(Pi_A*Pi_B != Pi_global, 'overlapping chart parity product is not global parity')
overlap_pair = fs*fx
need(Pi_global*overlap_pair == overlap_pair*Pi_global, 'shared pair conversion is genuinely globally even')
need((Pi_A*Pi_B)*overlap_pair != overlap_pair*(Pi_A*Pi_B), 'globally even overlap operation need not commute with chart parity product')

# At g/Delta=1/20 in the hypothetical common-boson star, m=101 bright
# revivals give a fully controlled near-perfect transfer. No floats used.
# alpha=101(1-sqrt(50/51)); prove 199/200 < alpha < 1 by squaring.
need((F(100,101))**2 < F(50,51), 'alpha less than one')
need(F(50,51) < (1-F(199,200*101))**2, 'alpha greater than 199/200')
star_probability_lower = 1 - (F(355,113) / 400)**2
need(star_probability_lower > F(9999,10000), 'hypothetical exact star transfer exceeds 99.99 percent')

need(sha256(TENSOR.read_bytes()).hexdigest() == '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763', 'native tensor pin')
raw = np.load(TENSOR)['W']
need(not np.any(raw.imag), 'native tensor imaginary part zero')
W = raw.real.astype(np.int64)
need(np.array_equal(W, raw.real), 'native tensor integral')
pairs = list(combinations(range(64),2))
rows = []
for A, row in enumerate(W):
    terms = [(pairs[j][0], pairs[j][1], int(row[j])) for j in np.flatnonzero(row)]
    rows.append(terms)
    need(len(terms) == 8, f'native channel {A} has eight terms')
    flattened = [u for i,j,w in terms for u in (i,j)]
    need(len(set(flattened)) == 16, f'native channel {A} is a matching, not a star')

blockers = {8,16,28,32,44,52,56}
block_mask = sum(1 << i for i in blockers)
vacb = (0,)*60
def single_boson(A):
    v = [0]*60
    v[A] = 1
    return tuple(v)

basis = [(block_mask|(1<<4)|(1<<57),vacb),
         (block_mask,single_boson(0)),
         (block_mask,single_boson(1)),
         (block_mask|(1<<4)|(1<<58),vacb)]
index = {v:i for i,v in enumerate(basis)}
Delta,g,J = s.symbols('Delta g J', real=True)

def fstep(mask, mode, create):
    occupied = bool(mask & (1<<mode))
    if occupied == create:
        return None
    sign = (-1)**((mask & ((1<<mode)-1)).bit_count())
    return mask ^ (1<<mode), sign

def pair_step(mask,i,j,create):
    first,second = (j,i) if create else (i,j)
    a = fstep(mask,first,create)
    if a is None:
        return None
    b = fstep(a[0],second,create)
    return None if b is None else (b[0],a[1]*b[1])

def action(state,mixer):
    mask,bosons = state
    out = {}
    def add(target, coefficient):
        out[target] = out.get(target,0)+coefficient
    add(state,Delta*sum(bosons))
    for A,terms in enumerate(rows):
        for i,j,w in terms:
            down = pair_step(mask,i,j,False)
            if down is not None:
                counts = list(bosons); counts[A]+=1
                add((down[0],tuple(counts)),g*w*down[1]*s.sqrt(counts[A]))
            if bosons[A]:
                up = pair_step(mask,i,j,True)
                if up is not None:
                    counts = list(bosons); counts[A]-=1
                    add((up[0],tuple(counts)),g*w*up[1]*s.sqrt(bosons[A]))
    mixer_pairs = ((0,1),) if mixer is True else (mixer or ())
    for left,right in mixer_pairs:
        for src,dst in ((left,right),(right,left)):
            if bosons[src]:
                counts = list(bosons); counts[src]-=1; counts[dst]+=1
                add((mask,tuple(counts)),J*s.sqrt(bosons[src]*counts[dst]))
    return {state:s.expand(value) for state,value in out.items() if value != 0}

H,Hnat = s.zeros(4),s.zeros(4)
for column,state in enumerate(basis):
    need(state[0].bit_count()+2*sum(state[1]) == 9, f'native invariant basis {column} has N=9')
    for mixer, matrix in ((False,Hnat),(True,H)):
        out = action(state,mixer)
        need(set(out) <= set(index), f'full sixty-channel action is invariant, column={column}, mixer={mixer}')
        for target,value in out.items():
            matrix[index[target],column] = value
need(H == H.T, 'native restricted matrix Hermitian with full CAR signs')
need(H[0,1]**2 == g**2 and H[2,3]**2 == g**2, 'both native terminal pair couplings have magnitude g')
need(H[1,2] == J and H[2,1] == J, 'only additional control is boson-only mixer')
need(H[0,2] == H[0,3] == H[1,3] == 0, 'no direct fermion-hop added')
need(Hnat[0,2] == Hnat[1,2] == Hnat[0,3] == Hnat[1,3] == 0, 'unmixed native Hamiltonian has disconnected endpoint blocks')
need((H**3)[3,0]**2 == g**4*J**2, 'first transfer amplitude at third order has squared coefficient g^4 J^2')
need((H**2)[3,0] == H[3,0] == 0, 'no transfer amplitude at orders one or two')
need((Hnat**3)[3,0] == 0, 'native third-order transfer absent without added mixer')

# Full finite-time transfer with a stable (J<Delta) boson mixer. Reflection
# reduces the exact invariant matrix to two two-level blocks.
R = s.Matrix([[1,0,1,0],[0,1,0,1],[0,1,0,-1],[1,0,-1,0]])/s.sqrt(2)
need(R.T*R == s.eye(4), 'reflection basis orthonormal')
need(s.simplify(R.T*H*R) == s.diag(s.Matrix([[0,g],[g,Delta+J]]),s.Matrix([[0,g],[g,Delta-J]])), 'exact reflection reduction')
need((s.Matrix([[0,g],[g,2*Delta]])-Delta*s.eye(2))**2 == (Delta**2+g**2)*s.eye(2), 'two-level exponential identity')
# Choose J=Delta-2g/sqrt(3), g=Delta/20 and t=pi sqrt(3)/g.
# The minus block returns its endpoint with phase -1. The plus block has
# a=Delta-g/sqrt(3), omega=sqrt(a^2+g^2); use omega-a<=g^2/(2a),
# (1-a/omega)/2<=g^2/(4a^2), and |A_plus|^2>=1-g^2/a^2.
need(F(17,10)**2 < 3, 'sqrt three exceeds 17/10')
a_lower = F(33,34)
need(1-F(1,20)/F(17,10) == a_lower, 'rigorous positive a/Delta lower bound')
native_probability_lower = 1-(3*F(355,113)**2+8)/(6400*a_lower**2)
need(native_probability_lower > F(993,1000), 'actual W full transfer exceeds 99.3 percent')
need(0 < 1-F(1,10)/F(17,10) < 1, 'chosen mixer is strictly below Delta; no zero boson frequency')

# The actual pinned source Clock, not an assumed full continuous symmetry.
COMMON = CONTRACT/'sources/repo/experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/common.py'
common_sha = '2cc97522457ecc7e6774d96a25b2581b5d67cd051ae35e28a26f0e98e2adb994'
need(sha256(COMMON.read_bytes()).hexdigest() == common_sha, 'pinned actual Clock common constructor')
with contextlib.redirect_stdout(io.StringIO()):
    common = runpy.run_path(str(COMMON))
    native_W = common['load_tensor']()
    GF, GB, p, sign = common['clock_lift'](native_W)
need(np.array_equal(W,native_W), 'native W equals tensor used by actual Clock constructor')
need(p == [2,0,1,4,3] and sign == -1, 'actual source Clock permutation and boson sign')
need(np.array_equal(GB.T@GB,np.eye(60,dtype=np.int64)), 'actual boson Clock exactly orthogonal')
need(np.array_equal(np.linalg.matrix_power(GB,6),np.eye(60,dtype=np.int64)), 'actual boson Clock sixth power identity')

def mixer_matrix(i,j):
    matrix = np.zeros((60,60),dtype=np.int64)
    matrix[i,j] = matrix[j,i] = 1
    return matrix

M01,M1213,M67 = [mixer_matrix(i,j) for i,j in ((0,1),(12,13),(6,7))]
need(np.array_equal(GB@M01@GB.T,M1213), 'actual Clock sends M01 exactly to M12,13')
need(np.array_equal(GB@M1213@GB.T,M67), 'actual Clock sends M12,13 exactly to M6,7')
need(np.array_equal(GB@M67@GB.T,M01), 'actual Clock closes three-element mixer orbit')
commutator = GB@M01-M01@GB
need(int(np.sum(commutator*commutator)) == 4, 'actual Clock-M01 commutator Frobenius norm squared equals four')
M_orbit = M01+M1213+M67
need(np.array_equal(GB@M_orbit,M_orbit@GB), 'orbit-sum mixer passes exact Clock commutation test')
orbit_support = np.diag([int(k in (0,1,6,7,12,13)) for k in range(60)])
need(np.array_equal(M_orbit@M_orbit,orbit_support), 'orbit channels square to the six-mode support projector')
for i,state in enumerate(basis):
    need(action(state,((0,1),(12,13),(6,7))) == action(state,True),
         f'Clock-invariant global orbit mixer has same exact native four-state action {i}')

# A common SU(4) Cartan is conserved by H,Nb,actual Clock and separate
# Casimirs. It excludes BOTH the selective and the Clock-averaged mixer.
fermion_weights,boson_weights = common['weights']()
qf,qb = fermion_weights[:,6],boson_weights[:,6]
QF,QB = np.diag(qf),np.diag(qb)
need(np.array_equal(QF@GF,GF@QF), 'actual fermion Clock commutes with selected colour Cartan')
need(np.array_equal(QB@GB,GB@QB), 'actual boson Clock commutes with selected colour Cartan')
for A,terms in enumerate(rows):
    need(all(qf[i]+qf[j] == qb[A] for i,j,w in terms),
         f'native H exactly conserves selected colour Cartan, channel {A}')
need((int(qb[0]),int(qb[1])) == (0,2), 'mixer channels have different colour Cartan charges zero and two')
need(int(np.sum((QB@M01-M01@QB)**2)) == 8, 'single mixer colour Cartan commutator Frobenius squared eight')
need(int(np.sum((QB@M_orbit-M_orbit@QB)**2)) == 24, 'Clock-orbit mixer colour Cartan commutator Frobenius squared twenty-four')
state_charges = [int(sum(qf[j] for j in range(64) if mask & (1<<j))+sum(qb[A]*b for A,b in enumerate(bosons)))
                 for mask,bosons in basis]
need(state_charges == [7,7,9,9], 'actual four-state endpoint charges are seven and nine, not the same internal label')

result = {
    'status':'PASS', 'checks':len(checks), 'check_labels':checks,
    'overlapping_chart_parity':{
        'chart_sets':'A={x,s}, B={s,y}',
        'chart_parity_product':'(-1)^(n_x+n_y), shared s cancels',
        'actual_global_parity':'(-1)^(n_x+n_s+n_y)',
        'proposed_product_criterion_valid_for_overlap_without_extra_hypotheses':False},
    'common_boson_star': {
        'status':'conditional non-native comparison model',
        'exact_fixed_K_dictionary':'c^dagger=b^dagger s/sqrt(K), K=N_b+n_s>=1',
        'commutator':'[Q_y^dagger,Q_x]=K f_y^dagger f_x',
        'native_charge':'N=2K-1+n_x+n_y+n_c',
        'K1_g_over_Delta':'1/20',
        'revival_time':'202 pi/(Delta sqrt(51/50))',
        'probability_lower_rational':str(star_probability_lower),
        'probability_lower_decimal':float(star_probability_lower),
        'native_W_obstruction':'Each W row has eight disjoint pairs, so it contains no common-s two-edge star.'},
    'native_W_closed_four_state_witness': {
        'status':'exact full-H invariant subspace AFTER explicit boson-mixer addition',
        'channels':[0,1], 'shared_fermion':4, 'endpoints':[57,58],
        'prepared_blockers':sorted(blockers), 'total_native_charge':9,
        'basis':['blockers+{4,57}; no bosons','blockers; one b0','blockers; one b1','blockers+{4,58}; no bosons'],
        'H_matrix':[[str(H[i,j]) for j in range(4)] for i in range(4)],
        'transfer_probability_leading_term':'g^4 J^2 t^6/36',
        'controlled_full_transfer':{
            'g_over_Delta':'1/20',
            'J_over_Delta':'1-1/(10 sqrt(3))',
            'time':'20 pi sqrt(3)/Delta',
            'probability_lower_rational':str(native_probability_lower),
            'probability_lower_decimal':float(native_probability_lower),
            'positive_boson_frequency':'Delta-J=Delta/(10 sqrt(3))>0',
            'status':'analytic all-state bound using the exactly invariant native-W four-state subspace'},
        'without_mixer':'two disconnected 2x2 blocks: endpoint transfer identically zero',
        'not_claimed':['native derivation of boson-only mixer','preparation from N64 ground','external two-bank transfer','relativistic field dictionary','TOE closure']},
    'actual_clock_source_gate': {
        'clock_p':p, 'boson_sign':sign,
        'common_sha256':common_sha,
        'single_mixer_orbit':[[0,1],[12,13],[6,7]],
        'single_mixer_commutator_frobenius_squared':4,
        'single_mixer_derivable_from_clock_commuting_alphabet':False,
        'no_go_scope':'Alg(H,Nb,G,C) when each granted separate Casimir C commutes with this actual G; not a claim Clock equals full continuous group',
        'invariant_orbit_sum':'M01+M12,13+M6,7',
        'orbit_sum_same_four_state_transfer_proved':True,
        'orbit_sum_derived_from_original_controls':False,
        'colour_Cartan_boson_charges_0_1':[0,2],
        'colour_Cartan_single_mixer_commutator_frobenius_squared':8,
        'colour_Cartan_orbit_mixer_commutator_frobenius_squared':24,
        'four_state_colour_Cartan_charges':state_charges,
        'orbit_sum_excluded_from_H_Nb_Clock_separate_Casimirs':True,
        'minimal_resource_alternatives':['additional colour-Cartan-changing operation, selective or Clock-invariant','new global source dynamics with an explicitly derived charge-balancing resource'],
        'continuous_SU4_controls':'not assumed available; a granted active simultaneous operation is not the same as the boson-only mixer'},
    'tensor_sha256':sha256(TENSOR.read_bytes()).hexdigest(),
    'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path)
args = parser.parse_args()
rendered = json.dumps(result,indent=2)+'\n'
if args.output:
    args.output.write_text(rendered)
    print(json.dumps({'status':result['status'],'checks':result['checks'],'output':str(args.output)}))
else:
    print(rendered,end='')
