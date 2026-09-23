"""Exact local-charge architecture and native dimer/monomer transport audit.

Independent finite algebra. No inherited checker imports and no native origin
of the postulated TFPT wedge vertex is inferred. Assertions are not used.
"""
from pathlib import Path
from itertools import combinations, product
import argparse
import hashlib
import json
import numpy as np
import sympy as s
from scipy.linalg import expm

HERE = Path(__file__).resolve().parent
CHECKS = []


def need(value, label):
    if not bool(value):
        raise RuntimeError(label)
    CHECKS.append(label)


def exact_non_diagonal():
    # e=01, f=12. All matrices rational; no floating point spectral premise.
    weights = s.Matrix([[1, 0], [1, 1], [0, 1]])
    U = s.Matrix([[s.Rational(3, 5), s.Rational(4, 5)],
                  [-s.Rational(4, 5), s.Rational(3, 5)]])
    need(U.T*U == s.eye(2), 'rational non-diagonal mode rotation unitary')
    V = s.zeros(4)
    V[2:4, 0:2] = U
    V[0:2, 2:4] = U.T
    charges = []
    for v in range(3):
        matter = s.diag(*list(weights.row(v)))
        med = U*matter*U.T
        Q = s.diag(matter, med)
        charges.append(Q)
        need(Q*V == V*Q, 'full coupling preserves rotated charge '+str(v))
        for e in range(2):
            need(med*U[:, e] == weights[v, e]*U[:, e],
                 'coupling vector is charge eigenvector '+str((v, e)))
    need(charges[0][2, 3] != 0, 'charge genuinely non-diagonal in chosen mediator basis')
    need((U[:, 0].T*U[:, 1])[0] == 0, 'distinct endpoint weights force orthogonal active modes')
    # A single mediator with e's charge cannot couple to f as well.
    badV = s.Matrix([[0, 0, 1], [0, 0, 1], [1, 1, 0]])
    badQ = s.diag(1, 0, 1)
    badcomm = badQ*badV-badV*badQ
    need(badcomm != s.zeros(3), 'negative: one common charged mode violates Q0')
    # Different edge annihilators have different matrix units/holes, so their
    # coefficients cannot cancel. This models the relevant independent inputs.
    x, y = s.symbols('x y')
    K0, K1 = s.Matrix([[1, 0]]), s.Matrix([[0, 1]])
    need(s.linsolve(list(x*K0+y*K1), (x, y)) == s.FiniteSet((0, 0)),
         'distinct edge inputs give independent cancellation equations')
    # Same conserved charge values on a compressed sector do not determine a
    # microscopic tensor factorization, or even the separate charge operators.
    flatQ = s.eye(3)
    need(flatQ*badV == badV*flatQ,
         'counterexample: Q=1 compressed-sector data alone allows shared mediator')
    return {'rotation': [[str(x) for x in U.row(i)] for i in range(2)],
            'charged_one_particle_space_min_per_independent_wedge_color': 2,
            'general_min_dimension': 'sum over edges rank(C_e); 6|E| if every SU(4) wedge channel has rank six',
            'primitive_tensor_bank_count_derived': False,
            'assumptions': ['self-adjoint additive charge Q_v=n_f(v)+b†q_v b',
                            'linear mediator creation vertex',
                            'nonzero independent matter edge operators',
                            'full operator commutators, not just Q_v=1 after projection']}


def ann(bits, mode):
    if not (bits >> mode)&1:
        return None
    sign = -1 if (bits & ((1 << mode)-1)).bit_count()%2 else 1
    return bits ^ (1 << mode), sign


def wedge_blocks():
    colors = range(4)
    pairs = list(combinations(colors, 2))
    edges = [(0, 1), (1, 2)]
    matter = list(product(colors, repeat=3))
    mi = {x:i for i,x in enumerate(matter)}
    rows = [(edge, pair, c) for edge in range(2) for pair in pairs for c in colors]
    ri = {x:i for i,x in enumerate(rows)}
    B = np.zeros((48, 64), dtype=np.int64)
    for word, col in mi.items():
        bits = sum(1 << (4*v+word[v]) for v in range(3))
        for ei, (i,j) in enumerate(edges):
            spectator = ({0,1,2}-{i,j}).pop()
            for a,b in pairs:
                for ci,cj,sign in [(a,b,1),(b,a,-1)]:
                    left = ann(bits, 4*i+ci)
                    if left is None:
                        continue
                    right = ann(left[0], 4*j+cj)
                    if right is None:
                        continue
                    need(right[0] == 1 << (4*spectator+word[spectator]),
                         'CAR wedge leaves only spectator '+str((word,ei,a,b,ci)))
                    B[ri[(ei,(a,b),word[spectator])], col] += sign*left[1]*right[1]
    need(np.array_equal(B[:24]@B[:24].T,2*np.eye(24,dtype=int)), 'each left edge wedge has norm squared two')
    need(np.array_equal(B[24:]@B[24:].T,2*np.eye(24,dtype=int)), 'each right edge wedge has norm squared two')
    C = B[24:]@B[:24].T
    gram = s.Matrix(C.T@C)
    spectrum = gram.eigenvals()
    need(spectrum == {s.Integer(1):20,s.Integer(4):4}, 'exact recoupling singular squares 1 twentyfold and 4 fourfold')
    need(s.Matrix(C).rank() == 24, 'all 24 dimer-color/monomer channels admit nonzero source recoupling')
    swaps = []
    for i,j in edges:
        swap = np.zeros((64,64),dtype=int)
        for word,col in mi.items():
            target = list(word)
            target[i],target[j] = target[j],target[i]
            swap[mi[tuple(target)],col] = 1
        swaps.append(swap)
    need(np.array_equal(B.T@B,2*np.eye(64,dtype=int)-swaps[0]-swaps[1]),
         'zero-mediator source reduction is the same SU4 exchange sum')
    one_color_in, one_color_out = mi[(1,0,0)], mi[(0,1,0)]
    need((-B.T@B)[one_color_out,one_color_in] == 1,
         'leading low-energy source exchange moves color without any extra charge carrier')
    H2 = np.zeros((112,112),dtype=int)
    H2[:64,64:] = B.T
    H2[64:,:64] = B
    # Full source configurations, not just an abstract effective hopping.
    nf = np.zeros((3,112),dtype=int)
    nf[:,:64] = 1
    nb = np.zeros((2,112),dtype=int)
    for row,(ei,pair,c) in enumerate(rows):
        nb[ei,64+row] = 1
        spec = ({0,1,2}-set(edges[ei])).pop()
        nf[spec,64+row] = 1
    incidence = np.array([[1,0],[1,1],[0,1]])
    q = nf+incidence@nb
    for v in range(3):
        need(np.all(q[v] == 1),'all full matching configurations carry local Q=1 '+str(v))
        need(np.all((q[v][:,None]-q[v][None,:])*H2 == 0), 'each native matrix element conserves local Q '+str(v))
    need(np.any((nf[0][:,None]-nf[0][None,:])*H2 != 0), 'local matter occupation itself is not conserved')
    # One concrete full-color transition: left dimer(01), spectator color 2.
    col = ri[(0,(0,1),2)]
    nonzero = [(rows[24+r],int(C[r,col])) for r in range(24) if C[r,col]]
    need(len(nonzero) == 2,'concrete three-distinct-color input has two coherent recoupling outputs')
    t = .05
    H = t*H2.astype(float)
    H[64:,64:] += np.eye(48)
    U = expm(-1j*H)
    p = float(np.sum(abs(U[88:,64+col])**2))
    need(p > 1e-7, 'same time-independent wedge Hamiltonian moves dimer to adjacent edge')
    neg = H.copy()
    neg[:64,88:] = 0
    neg[88:,:64] = 0
    pne = float(np.sum(abs(expm(-1j*neg)[88:,64+col])**2))
    need(pne == 0, 'negative: deleting receiving source edge kills transport')
    # H^2 off-diagonal coefficient is exact, not a fitted effective parameter.
    need(np.array_equal((H2@H2)[88:,64:88],C), 'full source H^2 equals two-vertex recoupling coefficient')
    return {'dimension':112,'matter_dimension':64,'mediator_dimension':48,
            'recoupling_rank':24,'recoupling_singular_squared_multiplicities':{'1':20,'4':4},
            'example_in':'b_01^[0,1] plus f_2^2',
            'example_out':[[[e,list(ab),color],coeff] for ((e,ab,color),coeff) in nonzero],
            'at_t_over_Delta':t,'at_time_hbar_over_Delta':1,
            'probability_on_edge_12':p,'negative_without_edge_12_probability':pne,
            'small_time_amplitude':'-(tau^2*t^2/(2*hbar^2))*B_12 B_01† + O(tau^3)',
            'energy_resolved_effective_offdiag':'(t^2/E)*B_12 B_01† near the one-mediator band E~Delta',
            'low_energy_leading_operator':'-(t^2/Delta) B†B = (t^2/Delta)(S_01+S_12-2I)',
            'low_energy_color_hop_coefficient':'t^2/Delta = J/2',
            'new_transport_generator_required':False,
            'caveat':'Needs both source edges, a dimer and a monomer. This finite high-energy channel is not the low-energy critical many-cell chain.'}


def carrier_and_ring():
    # Minimal nontrivial balance carrier for e=01 -> f=12.
    qe = np.array([1,1,0],dtype=int)
    qf = np.array([0,1,1],dtype=int)
    delta = qf-qe
    hop = np.array([[0,0],[1,0]],dtype=int)
    lower = np.array([[0,1],[0,0]],dtype=int)
    A = np.kron(hop,lower)
    H = A+A.T
    for v in range(3):
        qm = np.diag([qe[v],qf[v]])
        qr = np.diag([0,delta[v]])
        Q = np.kron(qm,np.eye(2,dtype=int))+np.kron(np.eye(2,dtype=int),qr)
        need(np.array_equal(Q@H,H@Q),'two-state reference balances endpoint '+str(v))
    got = expm(-1j*np.pi/2*H)[:,1]
    target = np.zeros(4,dtype=complex);target[2]=-1j
    need(np.linalg.norm(got-target)<1e-14,'minimal two-state charged reference gives deterministic balanced transfer')
    bare = hop+hop.T
    need(not np.array_equal(np.diag(qe[[0,2]])@bare,bare@np.diag(qe[[0,2]])), 'negative: bare mediator hop changes a local charge')
    # Two dimers on the opposite sides of a four-cycle conserve every Q_v.
    vertices = list(range(16))
    generators = [1,2,4,8,15]
    clebsch = {tuple(sorted((x,x^g))) for x in vertices for g in generators}
    cycle = [0,1,3,2]
    need(all(tuple(sorted((cycle[i],cycle[(i+1)%4]))) in clebsch for i in range(4)),
         'explicit Clebsch four-cycle 0,1,3,2 exists')
    edges = [(0,1),(1,3),(2,3),(0,2)]
    incidence = np.array([[int(v in e) for e in edges] for v in [0,1,3,2]])
    shift = np.array([1,-1,1,-1])
    need(np.array_equal(incidence@shift,np.zeros(4,dtype=int)), 'quartic ring preserves all endpoint charges')
    for a,b in combinations(range(4),2):
        need(not np.array_equal(incidence[:,a],incidence[:,b]), 'no nontrivial quadratic bare ring hop '+str((a,b)))
    ring = np.array([[0,1],[1,0]],dtype=int)
    need(np.linalg.norm(expm(-1j*np.pi/2*ring)@np.array([1,0])-np.array([0,-1j]))<1e-14,
         'balanced two-dimer resonance gives exact movable plaquette')
    return {'single_transfer_min_reference_charge_sectors':2,
            'reference_charge_difference':delta.tolist(),
            'exact_repeat_K_same_direction_min_sectors':'K+1 for a nonzero fixed charge shift',
            'reference_returned_unchanged_in_single_transfer':False,
            'exact_catalytic_return_with_nonzero_system_charge_transfer_possible':False,
            'no_extra_field_option':'existing monomer carries opposite shift via two native wedge vertices',
            'pure_mediator_option':'b_01† b_23† b_13 b_02 + adjoint on the displayed Clebsch cycle',
            'pure_mediator_min_degree_for_number_preserving_motion_between_distinct_edges_on_simple_graph':4,
            'ring_coefficient_derived_from_TFPT':False}


def main():
    out = {'architecture':exact_non_diagonal(),'native_transport':wedge_blocks(),
           'minimal_balance':carrier_and_ring(),
           'status':'CONDITIONAL_ARCHITECTURE_AND_NATIVE_VERTEX_TRANSPORT',
           'T1_T8_closed':[], 'native_wedge_origin_from_P1_P2_proved':False,
           'count':len(CHECKS),'checks':CHECKS,
           'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    srcs = [Path('/Users/stefanhamann/Documents')/name for name in
            ['antwort_spark.md','antwort_grok_1.md','BEWEISE.md','neu_1.md']]
    out['input_sha256'] = {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in srcs}
    ap = argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=HERE/'verification.json')
    a = ap.parse_args()
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:out[k] for k in ['status','count','native_transport','minimal_balance']},indent=2))


if __name__ == '__main__':
    main()
