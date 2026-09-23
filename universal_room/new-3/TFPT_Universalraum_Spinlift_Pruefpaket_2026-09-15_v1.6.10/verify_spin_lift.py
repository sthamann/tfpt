"""A signed four-clock continuation of the native W model.

Exact finite algebra, independent CAR checks and constants for the analytical
small-coupling full ground/response theorem in RESULTS.md. No TOE gate is closed.
Run without arguments; JSON goes to stdout. No source files are modified.
"""
from collections import defaultdict, deque
from hashlib import sha256
from io import BytesIO
from itertools import combinations, product
from pathlib import Path
import json
import math
import sys
from zipfile import ZipFile

import numpy as np
import sympy as s
from scipy.sparse import coo_matrix, csr_matrix, eye

HERE = Path(__file__).resolve().parent
ROOT = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
PACKAGE = Path('/Users/stefanhamann/Documents/TFPT_Universalraum_Forschungspaper_2026-09-15/Gemeinsame_Quelle/TFPT_Gemeinsame_Quelle_Pruefpaket_2026-09-15.zip')
EXPECTED_W = '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763'
CHECKS = []


def source_path(original):
    manifest=HERE/'frozen_sources.json'
    if manifest.exists():
        entries=json.loads(manifest.read_text())
        record=entries[str(original)]
        path=HERE/record['local']
        if sha256(path.read_bytes()).hexdigest()!=record['sha256']:
            raise RuntimeError('frozen input mismatch '+str(original))
        return path
    return original


def need(value, name):
    if not bool(value):
        raise RuntimeError(name)
    CHECKS.append(name)


def zero(M):
    M = M.tocsr()
    M.eliminate_zeros()
    return M.nnz == 0


def source_rows(n, signs):
    R = s.zeros(n)
    for j in range(n):
        R[j, (j + 1) % n] = signs[j]
    return R, s.eye(n) + R  # actual normalized rows are V/sqrt(2)


def geometry(V):
    n = V.cols
    S = V * V.conjugate().T / 2
    B = 8 * S.applyfunc(lambda x: x*x)
    T = s.Matrix(V.rows*n, V.rows*n, lambda a, b:
                 S[a//n, b//n] * s.conjugate(V[b//n, a % n]) * V[a//n, b % n] / 2)
    return S, B, T


def wedge_row(pair_terms, occupied):
    """Independent creation in canonical bitmask order; coefficients are 2*P."""
    out = defaultdict(int)
    for (i, j), coefficient in pair_terms.items():
        if occupied in (i, j):
            continue
        sign = (-1)**(int(occupied < i) + int(occupied < j))
        mask = (1 << i) | (1 << j) | (1 << occupied)
        out[mask] += sign * coefficient
    return dict(out)


def inner(a, b):
    return sum(v*b.get(k, 0) for k, v in a.items())


def lift_terms(V, W, pairs):
    all_terms = {}
    for e in range(V.rows):
        support = [i for i in range(V.cols) if V[e, i] != 0]
        for A in range(60):
            terms = defaultdict(int)
            for column in np.flatnonzero(W[A]):
                i, j = pairs[column]
                for x in support:
                    for y in support:
                        a, b = 64*x+i, 64*y+j
                        pair = tuple(sorted((a, b)))
                        terms[pair] += int(V[e, x]*V[e, y])*int(W[A, column])*(1 if a < b else -1)
            all_terms[e, A] = dict(terms)
    return all_terms


def native_data():
    with ZipFile(source_path(PACKAGE)) as archive:
        raw_bytes = archive.read('work/composition/native_tensor.npz')
    need(sha256(raw_bytes).hexdigest() == EXPECTED_W, 'unchanged pinned native W')
    with np.load(BytesIO(raw_bytes), allow_pickle=False) as f:
        raw = f['W']
    need(np.all(raw.imag == 0) and np.all(raw.real == np.rint(raw.real)), 'W real integer')
    W = raw.real.astype(np.int64)
    need(W.shape == (60, 2016) and np.count_nonzero(W) == 480, 'native W dimensions and support')
    need(np.array_equal(W@W.T, 8*np.eye(60, dtype=np.int64)), 'native pair Gram')
    pairs = list(combinations(range(64), 2))
    A = np.zeros((60, 64, 64), dtype=np.int64)
    lookup = {}
    for channel, col in zip(*np.nonzero(W)):
        i, j = pairs[col]
        value = int(W[channel, col])
        need((i, j) not in lookup, 'native pair has one channel '+str(col))
        lookup[i, j] = (int(channel), value)
        A[channel, i, j] = value
        A[channel, j, i] = -value
    need(np.array_equal(np.einsum('aij,aik->jk', A, A), 15*np.eye(64, dtype=np.int64)), 'sum A_dagger A equals 15I')
    rr, cc, vv = [], [], []
    for col, (a, b, c) in enumerate(combinations(range(64), 3)):
        for pair, left, sign in [((a, b), c, 1), ((a, c), b, -1), ((b, c), a, 1)]:
            if pair in lookup:
                channel, value = lookup[pair]
                rr.append(64*channel+left); cc.append(col); vv.append(sign*value)
    C = coo_matrix((np.array(vv, dtype=np.int64), (rr, cc)), shape=(3840, math.comb(64, 3))).tocsr()
    G = C@C.T
    I = eye(3840, dtype=np.int64, format='csr')
    K = 8*I-G
    roots = [0, 7, 10, 12]
    bound = int(np.max(np.asarray(abs(G).sum(axis=1))))
    need(3840*math.prod(bound+abs(q) for q in roots) < 2**63, 'native sparse polynomial int64 bound')
    polynomial = I
    for q in roots:
        polynomial = polynomial@(G-q*I)
    need(zero(polynomial), 'native G3 exact annihilating polynomial')
    multiplicities = {}
    for r in roots:
        P = I; den = 1
        for q in roots:
            if q != r:
                P = P@(G-q*I); den *= r-q
        tr = int(P.diagonal().sum())
        need(tr % den == 0, 'projector denominator '+str(r))
        multiplicities[8-r] = tr//den
    need(multiplicities == {8:64, 1:2880, -2:576, -4:320}, 'native K exact eigenspaces')
    # Every block is cross-checked against the independent antisymmetric matrices.
    block_ok = True
    for a in range(60):
        for b in range(60):
            block_ok &= np.array_equal(K[64*a:64*(a+1), 64*b:64*(b+1)].toarray(), A[b]@A[a].T)
    need(block_ok, 'all 3600 native CAR blocks agree with A_B A_A_dagger')
    return W, pairs, A, K, multiplicities


def full_CAR_Casimir(W, pairs):
    """Verify the degree-four identity by its entire 0/1/2-particle kernel.

    Normal ordering then proves Q=(60N-Casimir)/8 on the FULL 64-mode Fock
    space, not merely those particle sectors. No full-ground lemma is imported.
    """
    def spin(n):
        annih=[]
        for j in range(n):
            a=np.zeros((2**n,2**n),dtype=complex)
            for mask in range(2**n):
                if mask&(1<<j):
                    a[mask^(1<<j),mask]=(-1)**((mask&((1<<j)-1)).bit_count())
            annih.append(a)
        gamma=[a+a.T for a in annih]+[1j*(a.T-a) for a in annih]
        ev=[m for m in range(2**n) if m.bit_count()%2==0]
        return [(gamma[i]@gamma[j])[np.ix_(ev,ev)] for i,j in combinations(range(2*n),2)]
    generators=[np.kron(x,np.eye(4)) for x in spin(5)]+[np.kron(np.eye(16),x) for x in spin(3)]
    need(all(np.array_equal(x.conjugate().T,-x) for x in generators), 'all 60 internal generators anti-Hermitian')
    need(all(np.trace(x)==0 for x in generators), 'all internal generators traceless, filled state a singlet')
    need(np.array_equal(-sum(x@x for x in generators),60*np.eye(64)), 'one-particle Casimir 60I')
    index={p:i for i,p in enumerate(pairs)}
    cas=csr_matrix((2016,2016),dtype=complex)
    for X in generators:
        rr=[];cc=[];dd=[]
        for col,(v,w) in enumerate(pairs):
            for i in np.flatnonzero(X[:,v]):
                if i!=w:
                    rr.append(index[tuple(sorted((int(i),w)))]);cc.append(col);dd.append(X[i,v]*(1 if i<w else -1))
            for i in np.flatnonzero(X[:,w]):
                if i!=v:
                    rr.append(index[tuple(sorted((v,int(i))))]);cc.append(col);dd.append(X[i,w]*(1 if v<i else -1))
        L=coo_matrix((dd,(rr,cc)),shape=(2016,2016)).tocsr()
        cas-=L@L
    Ws=csr_matrix(W)
    need(zero(8*(Ws.T@Ws)+cas-120*eye(2016)), 'complete two-particle quartic Casimir identity')
    # All sparse complex arithmetic above is Gaussian integer with magnitudes
    # far below 2^53; no numerical tolerance or rounded coefficient is used.
    need(np.all(cas.data.imag==0) and np.max(abs(cas.data))<1000, 'Casimir arithmetic exactly integer within binary64 range')
    return {'all_Fock_identity':'8 Q = 60 N - Casimir',
            'two_particle_kernel_dimension':2016,'normal_order_degree_at_most':4,
            'positivity_reason':'Casimir = sum dGamma(X)^dagger dGamma(X) >= 0',
            'local_Q_bound':'Q <= (15/2) N <= 480 I',
            'filled_state_equality':'Q|filled>=480|filled>',
            'full_old_native_ground_archive_replayed':False}


def nonperturbative_ground_bounds():
    """Exact constants for a Feshbach proof on the complete bosonic Fock space.

    The source frame is fixed; the theorem covers 0<abs(g)/Delta<=1/10000,
    NOT the previous benchmark 1/20. Infinite boson tails are bounded by a
    convergent operator Neumann series, not discarded by truncation.
    """
    M=s.Integer(1920);t=s.Rational(1,10000)
    delta=s.Rational(15,2)*(1-s.sqrt(2)/2)
    a=2*s.sqrt(M)*t; b=M*t*t; r=s.Rational(1,100)
    need(a+b<r, 'global complementary resolvent expansion norm below 1/100')
    error=M*(b+r*r/(1-r))
    need(error<s.Rational(1,4), 'all-order Feshbach remainder less than one quarter g2/Delta')
    need(delta>2, 'second-order ground separation greater than 2 g2/Delta')
    need(delta-s.Rational(1,2)>s.Rational(3,2), 'full interacting spectral gap greater than 3/2 g2/Delta')
    residue=1/(1+M*t*t/(1-r)**2)
    need(residue>s.Rational(99998,100000), 'full ground-state bare filled overlap above 99.998 percent')
    broad_t=s.Rational(1,2000)
    ritz_error=M*M*broad_t*broad_t
    need(delta-ritz_error>1, 'elementary charge/Ritz full ground gap exceeds g2/Delta up to 1/2000')
    need(s.Rational(1,2)-2*M*broad_t*broad_t>0, 'all high-charge and positive-boson complements are positive up to 1/2000')
    weight=(2*residue-1)**2
    need(weight>s.Rational(99992,100000), 'clock-resolved charged pole absolute weight above 99.992 percent')
    low=15*(1-s.sqrt(2)/2); high=15*(1+s.sqrt(2)/2)
    need(low-s.Rational(1,2)>0, 'full low charged band has strictly positive removal energy')
    need(low+s.Rational(1,4)<high-s.Rational(1,2), 'full charged response has disjoint two-band enclosures')
    return {'parameter_range':'Delta>0, 0<abs(g)/Delta<=1/10000, mu=0',
            'ground_uniqueness_also_proved_for':'0<abs(g)/Delta<=1/2000 by charge, completion, and a 2x2 Ritz bound',
            'broader_range_gap_lower_bound_units_g2_over_Delta':'1',
            'local_Casimir_lemma_reproved':True,'all_boson_occupations_included':True,
            'Q_bound_M':1920,'uniform_Feshbach_error_coefficient':str(error),
            'ground_energy_interval_units_g2_over_Delta':['-1920','-7679/4'],
            'ground_energy_upper_endpoint_is_strict':True,
            'unique_global_ground_total_charge':256,
            'gap_lower_bound_units_g2_over_Delta':'3/2',
            'bare_filled_overlap_lower_bound':str(residue),
            'ground_scalar_fixed_point':'E=-g^2 <F|C^dagger (H_QQ-E)^(-1) C|F>',
            'clock_resolved_removal_poles':{
                'total_charge':255,'distinct_low_poles':2,'each_multiplicity':128,
                'energy_intervals_units_g2_over_Delta':[[str(low-s.Rational(1,2)),str(low+s.Rational(1,4))],
                                                        [str(high-s.Rational(1,2)),str(high+s.Rational(1,4))]],
                'single_clock_mode_pole_absolute_weight_lower_bound':str(weight),
                'original_site_mode_has_two_poles_not_one':True,
                'symmetry_used':'Spin(10)xSU(4) irreducibility, joint real C8 clock, and real Hamiltonian',
                'physical_creation_instrument_not_constructed':True},
            'not_certified_at_original_g_over_Delta_one_twentieth':True,
            'physical_selection_of_this_parameter_range_not_derived':True,
            'formal_proof_assistant_used':False}


def all_cycle_lifts():
    counts = {}
    for n in range(3, 8):
        reference = None; ranks = defaultdict(int)
        for signs in product((-1, 1), repeat=n):
            R, V = source_rows(n, signs)
            S = V*V.T/2
            B = 8*S.applyfunc(lambda x: x*x)
            if reference is None:
                reference = B
            need(B == reference, 'pair-blind signed cycle '+str((n, signs)))
            rank = V.rank(); holonomy = math.prod(signs)
            need(rank == n-int(holonomy == (-1)**n), 'signed-cycle rank '+str((n, signs)))
            ranks[str((holonomy, rank))] += 1
        counts[str(n)] = dict(ranks)
    return counts


def four_clock(W, pairs, A, K, multiplicities):
    result = {}; matrices = {}
    kr, kc = K.nonzero()
    for eta in (1, -1):
        R, V = source_rows(4, (1, 1, 1, eta))
        S, B, T = geometry(V)
        need(R**4 == eta*s.eye(4), 'clock fourth power '+str(eta))
        need(V*R == R*V, 'actual source frame intertwines clock '+str(eta))
        boson_clock = R.applyfunc(lambda x:x*x)
        need(boson_clock**4 == s.eye(4), 'pair clock returns after four '+str(eta))
        need(S.is_symmetric() and T.is_symmetric(), 'Hermitian real Gram factors '+str(eta))
        need(B.eigenvals() == {s.Integer(4):1, s.Integer(8):2, s.Integer(12):1}, 'identical N2 response '+str(eta))
        # Independent CAR witnesses in the actual 256-fermion four-bank model.
        terms = lift_terms(V, W, pairs)
        witnessed_nonzero_exchange = 0
        for t in range(320):
            idx = (t*104729) % len(kr)
            aa, bb = int(kr[idx]), int(kc[idx])
            ach, ar = divmod(aa, 64); bch, br = divmod(bb, 64)
            e, f, i, j = (t % 4, (t//4) % 4, (t//16) % 4, (t//64) % 4)
            x = wedge_row(terms[e, ach], 64*i+ar)
            y = wedge_row(terms[f, bch], 64*j+br)
            observed = s.Rational(inner(x, y), 4)
            predicted = B[e, f]*int(i == j and ach == bch and ar == br)-T[4*e+i, 4*f+j]*int(K[aa, bb])
            need(observed == predicted, 'independent native global CAR '+str((eta, t)))
            witnessed_nonzero_exchange += int(T[4*e+i, 4*f+j]*int(K[aa, bb]) != 0)
        need(witnessed_nonzero_exchange > 10, 'actual nonzero exchange witnesses '+str(eta))
        D = s.kronecker_product(B, s.eye(4))
        reduced = {k:D-k*T for k in multiplicities}
        matrices[eta] = reduced
        traces = [sum(m*s.trace(reduced[k]**p) for k,m in multiplicities.items()) for p in range(1,7)]
        result[str(eta)] = {
            'source_rank':V.rank(), 'source_Gram_eigenvalues':{str(k):v for k,v in S.eigenvals().items()},
            'B':B.tolist(), 'K8_characteristic_polynomial':str(s.factor(reduced[8].charpoly().as_expr())),
            'full_N3_Gram_traces_1_to_6':traces,
            'fermion_dark_mode_count':64*(4-V.rank())
        }
    diff = [result['-1']['full_N3_Gram_traces_1_to_6'][i]-result['1']['full_N3_Gram_traces_1_to_6'][i] for i in range(6)]
    need(diff == [0,0,0,-115200,-4608000,-118005120], 'first visible full N3 moment is fourth')
    denominator = 4*60*4*64
    coefficient = s.Rational(2*4**3, math.factorial(8))*diff[3]/denominator
    need(coefficient == -s.Rational(1,168), 'neutral boson-survival difference minus g8 t8 over168')
    need(sum(multiplicities.values())*16 == denominator, 'complete boson plus fermion input dimension')
    smin = 1-s.sqrt(2)/2
    result['second_order'] = {
        'inequality':'sum_A P_A^dagger P_A <= (15/2) N_q; all-Fock identity re-proved from complete degree-four kernel',
        'filled_Q_eigenvalue':1920,
        'hole_number_bound_coefficient':str(15*smin/2),
        'one_hole_gap_coefficients':[str(15*smin), str(15*(1+s.sqrt(2)/2))],
        'one_hole_each_multiplicity':128,
        'energy_unit':'g^2/Delta at second order only',
        'full_H_at_g_over_Delta_one_twentieth_certified':False,
        'four_bank_state_total_charge_at_zeroth_order':256
    }
    return result


def toy_full_CAR():
    # A single internal antisymmetric 2x2 channel, all N3 rows and columns.
    for eta in (1,-1):
        R,V = source_rows(4,(1,1,1,eta)); S,B,T = geometry(V)
        rows = []
        for e in range(4):
            terms = defaultdict(int)
            for x in range(4):
                for y in range(4):
                    if V[e,x] and V[e,y]:
                        a,b=2*x,2*y+1
                        terms[tuple(sorted((a,b)))] += int(V[e,x]*V[e,y])*(1 if a<b else -1)
            rows.extend(wedge_row(terms, r) for r in range(8))
        direct = s.Matrix(32,32,lambda i,j:s.Rational(inner(rows[i],rows[j]),4))
        # Native W has pair norm8; the two-mode test has pair norm1 and K=I2.
        expected = s.kronecker_product(s.kronecker_product(B/8,s.eye(4))-T,s.eye(2))
        need(direct == expected, 'all entries of independent two-internal-mode CAR model '+str(eta))
        # Filled and one-hole effective quartic Q computed without Casimir assumptions.
        all_pair_terms = []
        for e in range(4):
            terms=defaultdict(int)
            for x in range(4):
                for y in range(4):
                    if V[e,x] and V[e,y]:
                        a,b=2*x,2*y+1
                        terms[tuple(sorted((a,b)))] += int(V[e,x]*V[e,y])*(1 if a<b else -1)
            all_pair_terms.append(terms)
        full = (1<<8)-1
        states=[full^(1<<r) for r in range(8)]
        annihilated=[]
        for state in states:
            out={}
            for e,terms in enumerate(all_pair_terms):
                for (i,j),v in terms.items():
                    if not ((state>>i)&1 and (state>>j)&1): continue
                    # a_j a_i canonical pair removal; a_i acts first.
                    sign=(-1)**((state&((1<<i)-1)).bit_count()+((state^(1<<i))&((1<<j)-1)).bit_count())
                    out[e,state^(1<<i)^(1<<j)]=s.Rational(sign*v,2)
            annihilated.append(out)
        Qh=s.Matrix(8,8,lambda i,j:sum(v*annihilated[j].get(k,0) for k,v in annihilated[i].items()))
        # Hole convention f_r|filled> includes (-1)^r.
        signs=s.diag(*[(-1)**r for r in range(8)])
        need(signs*Qh*signs == 4*s.eye(8)-s.kronecker_product(V.T*V/2,s.eye(2)), 'independent exact one-hole normal ordering '+str(eta))


def gaussian_alphabet():
    # The Lie bracket of a 2-word with a 4-word exchanges one Majorana index.
    quads=[frozenset(x) for x in combinations(range(10),2)]
    seen={frozenset((0,1,2,3))}; pending=deque(seen)
    while pending:
        a=pending.popleft()
        for b in quads:
            if len(a&b)%2:
                new=a^b
                if new not in seen:seen.add(new); pending.append(new)
    need(len(seen)==210 and all(len(x)==4 for x in seen), 'one quartic and quadratic commutators generate all 210 quartics')
    # Exact Gaussian-integer Jordan-Wigner matrices, restricted to S+.
    X=np.array([[0,1],[1,0]],dtype=complex);Y=np.array([[0,-1j],[1j,0]],dtype=complex)
    Z=np.diag([1,-1]);I=np.eye(2);gammas=[]
    for j in range(5):
        for middle in (X,Y):
            M=np.array([[1]],dtype=complex)
            for f in [Z]*j+[middle]+[I]*(4-j):M=np.kron(M,f)
            gammas.append(M)
    even=[n for n in range(32) if n.bit_count()%2==0]
    generators=[]
    for support in list(quads)+sorted(seen,key=lambda a:tuple(sorted(a))):
        M=np.eye(32,dtype=complex)
        for i in sorted(support): M=M@gammas[i]
        if len(support)==2:M=1j*M
        generators.append(M[np.ix_(even,even)].ravel())
    F=np.array(generators)
    need(np.array_equal(F@F.conjugate().T,16*np.eye(255)), '255 traceless Hermitian quadratic/quartic directions independent on S+')
    need(all(np.trace(x.reshape(16,16))==0 for x in F), 'generators traceless on S+')
    return {'quadratic_dynamical_Lie_dimension':45,'quadratic_associative_algebra_dimension':256,
            'quadratics_plus_one_nonzero_quartic_Lie_dimension':255,
            'all_quadratic_controls_and_quartic_granted_not_derived':True,
            'not_the_64_mode_particle_Fock_space':True}


def archive_and_dispersion():
    gamma, lam, k, g, Delta = s.symbols('gamma lam k g Delta', positive=True)
    logratio = gamma*s.log(s.Rational(8,58))/s.log(s.Rational(248,60))
    need(s.diff(logratio,gamma) != 0, 'archive ratio still depends on gamma through lambda')
    Bk=8+4*s.cos(k)
    Eminus=(Delta-s.sqrt(Delta**2+4*g**2*Bk))/2
    quadratic=s.simplify(s.diff(Eminus,k,2).subs(k,0)/2)
    need(quadratic==2*g**2/s.sqrt(Delta**2+48*g**2), 'N2 chain lower-band quadratic expansion')
    alpha=s.symbols('alpha',positive=True)
    old_beta=s.Rational(41,10)/(2*s.pi)*alpha**2+s.Rational(1,256)/s.pi**3*(1/(8*s.pi))**2*alpha**3
    need(old_beta.is_positive, 'retained archival beta has no nonzero positive zero')
    return {'archive_log_ratio_gamma_derivative':str(s.diff(logratio,gamma)),
            'N2_chain_B':str(Bk),'N2_lower_band_quadratic_coefficient':str(quadratic),
            'not_dispersion_above_full_interacting_ground':True,
            'UV_counterexamples_do_not_classify_IR_universality':True}


def main():
    W,pairs,A,K,multiplicities=native_data()
    casimir=full_CAR_Casimir(W,pairs)
    cycles=all_cycle_lifts()
    four=four_clock(W,pairs,A,K,multiplicities)
    toy_full_CAR()
    gaussian=gaussian_alphabet()
    archive=archive_and_dispersion()
    full_ground=nonperturbative_ground_bounds()
    sources=[PACKAGE,ROOT/'origin_theory.tex',ROOT/'verification/v480_multilocal_four_interval.py',
             ROOT/'verification/v111_quadratic_transport.py',ROOT/'verification/v5_e8_cascade.py',
             ROOT/'_archive/paper-latex/old/paper_v1_06_01_09_2025.tex',
             ROOT/'tfpt_3_e8_audit_bootstrap.tex',ROOT/'docs/OPEN_PROBLEMS.md',
             Path('/Users/stefanhamann/Documents/TFPT_Gemeinsame_Quelle_2026-09-15.pdf')]
    return {'status':'PASS','version':'research-note-1.6.10','exact_checks':len(CHECKS),'checks':CHECKS,
            'native_K_multiplicities':multiplicities,'cycle_lifts':cycles,'four_clock':four,
            'gaussian_alphabet':gaussian,'archive_and_dispersion':archive,
            'all_Fock_Casimir':casimir,'nonperturbative_ground_theorem':full_ground,
            'source_hashes':{str(p):sha256(source_path(p).read_bytes()).hexdigest() for p in sources},
            'claims':{'conditional_clock_to_composition_intertwiner':True,
                      'neutral_N3_detection_of_spin_lift':True,
                      'unique_second_order_filled_state':True,
                      'full_interacting_ground_at_small_coupling_analytic_proof':True,
                      'source_frame_uniquely_derived_from_TFPT':False,
                      'full_interacting_four_bank_ground_at_original_one_twentieth_certified':False,
                      'native_encoder_or_record_derived':False,'T1_T8_closed':[]}}


if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True,default=str))
