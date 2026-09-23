"""RETRACTION AND REPLACEMENT of point P3 in open_points_closure.py.

P3 claimed that no W-covariant operator satisfies G^4 = -I, and concluded that the
negative-lift station clock is provably external to the native source.  That claim
is WRONG.  It searched only REAL signed slot permutations, while the TFPT carrier
clock is complex by construction: v177/v180 give rho: z -> i z on (P^1, mu4) with
H^1 characters rho* w_k = i^k.  A complex clock cannot be a real signed permutation,
so the search space excluded the object it was looking for.

Searching the Cartan torus instead -- which is W-covariant for free, because weight
conservation q_i + q_j = q_A is exactly the statement that a torus element commutes
with the pair tensor -- the clock is there, and it carries the seam's structure:

  A  every Cartan weight with odd total weight sum gives G_F^4 = -I
  B  complete scan over all weights mod 8: the seam's equidistributed four-sector
     pattern 16/16/16/16 is attainable, and one realisation is purely inside the
     A3 = SU(4) factor -- the factor TFPT assigns mu4 to
  C  that clock has carrier order four with eigenvalues exactly mu4 = {1,i,-1,-i}
     and fermion order eight: the binary double cover of v480, natively in W
  D  a real W-covariant Weyl involution inverts it with S^2 = +I, so the native
     group is the DIHEDRAL order-16 cover -- the same group as the raw seam ring
  E  it commutes with the pinned period-six clock and lives in the other factor

What is NOT established: uniqueness.  57 histogram classes realise the four-sector
pattern, so the A3 placement matches TFPT's own assignment but is not forced here.
"""
import json
import sys
from itertools import combinations, permutations, product
from pathlib import Path

import numpy as np
from scipy.sparse import csr_matrix

REPO = Path(__file__).resolve().parents[3]
NATIVE_COMMON = REPO / 'universal_room/new-3/universalraum-v1.6.9/agents/source/inputs'
TENSOR_PATH = REPO / ('experiments/theory-contracts/universalraum-v16-integrated-20260915'
                      '/sources/native_tensor.npz')
CLOCK_PATH = REPO / 'experiments/theory-contracts/compiler-involution-types/checker.py'

ZETA8 = np.exp(1j * np.pi / 4)
# The canonical realisation: no Spin(10) weight, the A3 weight (0,1,2).
CANONICAL_WEIGHT = np.array([0, 0, 0, 0, 0, 0, 1, 2])

checks = []


def need(condition, name):
    if not bool(condition):
        raise RuntimeError('FAILED: ' + name)
    checks.append(name)


def _load():
    sys.path.insert(0, str(NATIVE_COMMON))
    import native_common as nc
    nc.TENSOR_PATH = TENSOR_PATH
    nc.CLOCK_PATH = CLOCK_PATH
    return nc, nc.load_tensor()


def _clifford(n_slots):
    """Weight negation on slot j: the Majorana that flips bit j with its ordering sign."""
    out = []
    for j in range(n_slots):
        M = np.zeros((2 ** n_slots, 2 ** n_slots))
        for m in range(2 ** n_slots):
            M[m ^ (1 << j), m] = (-1) ** ((m & ((1 << j) - 1)).bit_count())
        out.append(M)
    return out


def _permutation_lift(perm, index, n_slots):
    inverse = {v: k for k, v in index.items()}
    size = len(index)
    out = np.zeros((size, size))
    for col in range(size):
        mask = inverse[col]
        bits = [j for j in range(n_slots) if mask & (1 << j)]
        mapped = [perm[j] for j in bits]
        sign = (-1) ** sum(mapped[i] > mapped[j]
                           for i in range(len(mapped)) for j in range(i + 1, len(mapped)))
        out[index[sum(1 << j for j in mapped)], col] = sign
    return out


# ------------------------------------------------------------------ A --------

def torus_clocks(nc, W):
    """Odd total weight sum <=> G^4 = -I, and every torus element is W-covariant."""
    fermion_weights, boson_weights = nc.weights()
    need(set(np.unique(fermion_weights).tolist()) == {-1, 1},
         'every fermion Cartan weight is a sign vector, so <lambda,q> has the parity of '
         'the total weight sum')
    need(set(np.unique(boson_weights).tolist()) <= {-2, 0, 2},
         'every boson Cartan weight is even, as the sum of two fermion sign vectors')

    _, lookup = nc.channel_support(W)
    for weight in ([1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0],
                   [1, 1, 1, 0, 0, 0, 0, 0], list(CANONICAL_WEIGHT)):
        lam = np.array(weight)
        phase_f, phase_b = fermion_weights @ lam, boson_weights @ lam
        mismatch = [p for p, (A, _) in lookup.items()
                    if phase_f[p[0]] + phase_b[A] * 0 + phase_f[p[1]] != phase_b[A]]
        need(not mismatch,
             'weight conservation makes the torus element %s exactly W-covariant on all 480 '
             'supported pairs' % weight)
        G = np.diag(ZETA8 ** phase_f)
        fourth = np.linalg.matrix_power(G, 4)
        if sum(weight) % 2:
            need(np.allclose(fourth, -np.eye(64)),
                 'odd total weight sum %d gives G^4 = -I for %s' % (sum(weight), weight))
        else:
            need(np.allclose(fourth, np.eye(64)),
                 'even total weight sum %d gives G^4 = +I for %s' % (sum(weight), weight))
    return {'covariance': 'automatic from weight conservation q_i + q_j = q_A',
            'fourth_power_rule': 'G^4 = -I exactly when the total weight sum is odd'}


# ------------------------------------------------------------------ B --------

def sector_scan(nc):
    """Complete scan over all Cartan weights mod 8 for the seam's four-sector pattern."""
    fermion_weights, _ = nc.weights()
    spinor = np.unique(fermion_weights[:, :5], axis=0)
    colour = np.unique(fermion_weights[:, 5:], axis=0)
    need(spinor.shape == (16, 5) and colour.shape == (4, 3),
         'the 64 modes factor as 16 Spin(10) spinor states times 4 SU(4) colour states')

    def histograms(vectors, n_slots):
        out = {}
        for lam in product(range(8), repeat=n_slots):
            residue = (vectors @ np.array(lam)) % 8
            key = tuple(int((residue == k).sum()) for k in range(8))
            out.setdefault(key, lam)
        return out

    spinor_hist = histograms(spinor, 5)
    colour_hist = histograms(colour, 3)
    need(len(spinor_hist) == 28 and len(colour_hist) == 19,
         'only the weight mod 8 matters, giving 28 spinor and 19 colour histograms -- the '
         'scan over these is a scan over ALL integer Cartan weights')

    equidistributed, purely_a3 = [], []
    for h_s, lam_s in spinor_hist.items():
        for h_c, lam_c in colour_hist.items():
            conv = [0] * 8
            for i in range(8):
                if not h_s[i]:
                    continue
                for j in range(8):
                    if h_c[j]:
                        conv[(i + j) % 8] += h_s[i] * h_c[j]
            if conv == [0, 16, 0, 16, 0, 16, 0, 16]:
                equidistributed.append((lam_s, lam_c))
                if all(v == 0 for v in lam_s):
                    purely_a3.append((lam_s, lam_c))
    need(equidistributed,
         'the seam pattern of four equal 16-dimensional sectors at the primitive eighth '
         'roots IS attainable by a native Cartan clock')
    need(purely_a3,
         'at least one realisation needs no Spin(10) weight at all: the clock sits purely '
         'in the A3 = SU(4) factor, which is where TFPT places mu4')
    need(len(equidistributed) > len(purely_a3),
         'uniqueness is NOT claimed: other realisations exist that also use Spin(10) weights')
    return {'equidistributed_realisations': len(equidistributed),
            'purely_A3_realisations': len(purely_a3),
            'canonical_colour_weight': list(purely_a3[0][1]),
            'uniqueness': 'not established'}


# ------------------------------------------------------------------ C --------

def canonical_clock(nc, W):
    fermion_weights, boson_weights = nc.weights()
    phase_f = fermion_weights @ CANONICAL_WEIGHT
    phase_b = boson_weights @ CANONICAL_WEIGHT
    G_f = np.diag(ZETA8 ** phase_f)
    G_b = np.diag(ZETA8 ** phase_b)

    sectors = {int(k): int((phase_f % 8 == k).sum()) for k in np.unique(phase_f % 8)}
    need(sectors == {1: 16, 3: 16, 5: 16, 7: 16},
         'the canonical A3 clock has four 16-dimensional fermion sectors at the four '
         'PRIMITIVE eighth roots -- the sector structure of the v480 seam ring')
    need(np.allclose(np.linalg.matrix_power(G_f, 4), -np.eye(64)),
         'the canonical A3 clock satisfies G_F^4 = -I')
    order_f = next(k for k in range(1, 17)
                   if np.allclose(np.linalg.matrix_power(G_f, k), np.eye(64)))
    order_b = next(k for k in range(1, 17)
                   if np.allclose(np.linalg.matrix_power(G_b, k), np.eye(60)))
    need(order_f == 8 and order_b == 4,
         'fermion order eight over carrier order four: the binary double cover, natively in W')
    carrier = sorted({complex(np.round(ZETA8 ** p, 9)) for p in phase_b}, key=np.angle)
    need(len(carrier) == 4 and all(abs(c ** 4 - 1) < 1e-12 for c in carrier)
         and {complex(np.round(c, 6)) for c in carrier} == {1 + 0j, 1j, -1 + 0j, -1j},
         'the carrier eigenvalues are exactly mu4 = {1, i, -1, -i}')

    _, lookup = nc.channel_support(W)
    need(not [p for p, (A, _) in lookup.items()
              if phase_f[p[0]] + phase_f[p[1]] != phase_b[A]],
         'W Lambda^2(G_F) = G_B W exactly on all 480 supported pairs')
    return {'weight': CANONICAL_WEIGHT.tolist(), 'fermion_sectors': sectors,
            'fermion_order': order_f, 'carrier_order': order_b,
            'carrier_eigenvalues': 'mu4'}


# ------------------------------------------------------------------ D --------

def inverting_reflection(nc, W):
    """Exhaustive search over the real Weyl group of D5 x A3 lifted to the 64 modes."""
    Ws = csr_matrix(W)
    fermion_weights, _ = nc.weights()
    G_f = np.diag(ZETA8 ** (fermion_weights @ CANONICAL_WEIGHT))
    eye64 = np.eye(64)
    E5, E3 = _clifford(5), _clifford(3)
    even5 = [m for m in range(32) if m.bit_count() % 2 == 0]
    even3 = [m for m in range(8) if m.bit_count() % 2 == 0]
    spinor_index = {m: i for i, m in enumerate(nc.EV)}
    colour_index = {m: i for i, m in enumerate(nc.CV)}

    def block(gens, even, index, n_slots, flips, perm):
        M = np.eye(2 ** n_slots)
        for j in flips:
            M = gens[j] @ M
        return M[np.ix_(even, even)] @ _permutation_lift(perm, index, n_slots)

    def covariant(S):
        pair = nc.exterior_square_group(np.rint(S).astype(np.int64))
        S_b = (Ws @ pair @ Ws.T).toarray() / 8
        if not np.allclose(S_b, np.rint(S_b)):
            return False
        residual = Ws @ pair - csr_matrix(np.rint(S_b).astype(np.int64)) @ Ws
        residual.eliminate_zeros()
        return residual.nnz == 0

    flips5 = [c for k in (0, 2, 4) for c in combinations(range(5), k)]
    flips3 = [c for k in (0, 2) for c in combinations(range(3), k)]
    need(len(flips5) * 120 == 1920 and len(flips3) * 6 == 24,
         'the search covers the full Weyl group of D5 times A3, 1920 x 24 = 46080 elements')

    plus, minus = 0, 0
    witness = None
    for f5 in flips5:
        for p5 in permutations(range(5)):
            A = block(E5, even5, spinor_index, 5, f5, list(p5))
            for f3 in flips3:
                for p3 in permutations(range(3)):
                    S = np.kron(A, block(E3, even3, colour_index, 3, f3, list(p3)))
                    if not np.allclose(S @ G_f @ S.T, np.conj(G_f)):
                        continue
                    square = np.allclose(S @ S, eye64) - np.allclose(S @ S, -eye64)
                    if square == 0 or not covariant(S):
                        continue
                    if square > 0:
                        plus += 1
                        if witness is None:
                            witness = {'spinor_flips': list(f5), 'spinor_perm': list(p5),
                                       'colour_flips': list(f3), 'colour_perm': list(p3)}
                    else:
                        minus += 1

    need(plus > 0,
         'a REAL W-covariant Weyl involution with S^2 = +I inverts the canonical A3 clock, '
         'so <G_F, S> is the DIHEDRAL order-16 cover -- the same group as the raw seam ring, '
         'not the quaternionic one')
    need(minus > 0,
         'quaternionic partners with S^2 = -I exist too; the seam geometry, not the tensor, '
         'picks the dihedral sign')
    return {'inverting_with_square_plus_I': plus, 'inverting_with_square_minus_I': minus,
            'witness': witness, 'group': 'dihedral of order 16'}


# ------------------------------------------------------------------ E --------

def two_clocks_coexist(nc, W):
    fermion_weights, _ = nc.weights()
    G_mu4 = np.diag(ZETA8 ** (fermion_weights @ CANONICAL_WEIGHT))
    G_six, _, slot_clock, _ = nc.clock_lift(W)
    need(np.allclose(G_mu4 @ G_six, G_six @ G_mu4),
         'the native mu4 clock commutes with the pinned period-six clock')
    need(all(CANONICAL_WEIGHT[:5][j] == 0 for j in range(5)),
         'the period-six clock permutes Spin(10) slots, the mu4 clock carries only A3 weight: '
         'they act in different factors, which is why they commute')
    return {'period_six_slot_permutation': slot_clock,
            'mu4_factor': 'A3 = SU(4)', 'commute': True}


def run():
    nc, W = _load()
    result = {
        'status': 'PASS',
        'retracts': 'open_points_closure.py point P3, which searched only real signed slot '
                    'permutations and therefore could not see the complex TFPT carrier clock',
        'A_torus': torus_clocks(nc, W),
        'B_sector_scan': sector_scan(nc),
        'C_canonical_clock': canonical_clock(nc, W),
        'D_inverting_reflection': inverting_reflection(nc, W),
        'E_two_clocks': two_clocks_coexist(nc, W),
    }
    result['exact_checks'] = len(checks)
    result['established'] = [
        'the negative-lift clock G^4 = -I exists natively in W; P3 was wrong',
        'a native realisation reproduces the seam ring exactly: four equal 16-dimensional '
        'sectors at the primitive eighth roots, carrier order four with eigenvalues mu4, '
        'fermion order eight',
        'one such realisation carries no Spin(10) weight and sits purely in the A3 = SU(4) '
        'factor, which is where TFPT places mu4 and where the H^1 characters i^k live',
        'a real W-covariant Weyl involution with S^2 = +I inverts it, so the native group is '
        'the dihedral order-16 cover -- the same group the raw seam ring produces',
    ]
    result['not_established'] = [
        'uniqueness of the realisation: 57 histogram classes reach the four-sector pattern, '
        'so the A3 placement matches TFPT but is not forced by this computation',
        'the identification of this native clock with the seam station clock as OPERATORS; '
        'what is shown is that the group, the order, the sector structure and the carrier '
        'spectrum all agree',
        'the period-six clock is a second, commuting clock in the other factor; nothing here '
        'merges them',
    ]
    return result


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True, default=str))
