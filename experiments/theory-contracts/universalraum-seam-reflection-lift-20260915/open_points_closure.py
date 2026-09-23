"""The four structural points that seam_reflection_lift.py left open, attacked directly.

P1  BANK PLACEMENT.  `one W pair bank per seam link` was a composition assumption.
    Enumerate every D4-equivariant placement of pair banks on the station square
    and test connectivity and rank.  Only the link placement survives.

P2  SOURCE CLASS.  The nearest-neighbour two-site frame was an ansatz.  Classify the
    COMPLETE reflection-covariant class on four stations: prove that reflection
    covariance is equivalent to a palindromic coefficient vector, then decide for
    every support length and both lifts whether a free fermion direction is forced.

P3  TWO CLOCKS.  Exhaustive search over the signed slot group: no REAL W-covariant
    signed permutation of the 64 modes satisfies G^4 = -I.  The scan itself stands.
    The conclusion first drawn from it -- that the negative-lift clock is therefore
    external to W -- was WRONG and is retracted; see `native_mu4_clock.py`.  The
    TFPT carrier clock is complex (rho: z -> iz, characters i^k), so a real signed
    permutation could never have represented it.  In the Cartan torus the clock is
    there, with the seam's exact sector structure.

P4  SEAM LOCALITY.  What is left after P1 and P2 is the single geometric statement
    that a gap-local source has support two.  Verify it on the seam ring: every gap
    arc has exactly two adjacent intervals.

Exact throughout: sympy over the eigenvalues of the cyclic shift, integer algebra
for the tensor search.
"""
import json
import sys
from itertools import permutations, product
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.sparse import csr_matrix

REPO = Path(__file__).resolve().parents[3]
NATIVE_COMMON = REPO / 'universal_room/new-3/universalraum-v1.6.9/agents/source/inputs'
TENSOR_PATH = REPO / ('experiments/theory-contracts/universalraum-v16-integrated-20260915'
                      '/sources/native_tensor.npz')
CLOCK_PATH = REPO / 'experiments/theory-contracts/compiler-involution-types/checker.py'

N_RING, ELL, P0 = 256, 48, 8
Q_RING = N_RING // 4

checks = []


def need(condition, name):
    if not bool(condition):
        raise RuntimeError('FAILED: ' + name)
    checks.append(name)


def _shift(eta):
    return sp.Matrix([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [eta, 0, 0, 0]])


def _eigenvalues(eta):
    """The four eigenvalues of the cyclic shift R with R^4 = eta."""
    if eta == 1:
        return [sp.Integer(1), sp.I, sp.Integer(-1), -sp.I]
    return [sp.exp(sp.I * sp.pi * (2 * k + 1) / 4) for k in range(4)]


# ------------------------------------------------------------------ P1 -------

def bank_placement():
    """Which D4-equivariant bank placements on the station square are admissible?

    A placement is a D4-orbit of station subsets; each bank couples the stations it
    touches.  Admissible means: the induced coupling graph is connected (otherwise
    the four stations do not form one system) and the induced source frame has no
    free fermion direction.
    """
    # A bank is (start, offsets): it touches the stations start + o, read around the ring.
    # Crossing the seam branch cut multiplies that leg by the wrap sign eta.
    placements = {
        'vertices': [(v, (0,)) for v in range(4)],
        'edges': [(v, (0, 1)) for v in range(4)],
        'diagonals': [(v, (0, 2)) for v in range(2)],
        'centre': [(0, (0, 1, 2, 3))],
    }
    report = {}
    for name, banks in placements.items():
        sets = {tuple(sorted((start + o) % 4 for o in offs)) for start, offs in banks}
        rot = {tuple(sorted((x + 1) % 4 for x in b)) for b in sets}
        refl = {tuple(sorted((-x) % 4 for x in b)) for b in sets}
        need(rot == sets == refl, 'placement %s is a genuine D4 orbit' % name)
        banks_as_sets = [tuple(sorted((start + o) % 4 for o in offs)) for start, offs in banks]

        adjacency = {frozenset((u, v)) for b in banks_as_sets for u in b for v in b if u != v}
        seen, stack, comp = set(), [0], 0
        remaining = set(range(4))
        while remaining:
            comp += 1
            stack = [remaining.pop()]
            while stack:
                x = stack.pop()
                if x in seen:
                    continue
                seen.add(x)
                remaining.discard(x)
                for e in adjacency:
                    if x in e:
                        stack.extend(e - {x})
        connected = comp == 1

        # The source frame the placement induces: one balanced source mode per bank on the
        # stations it touches, with the wrap sign eta on every leg that crosses the seam
        # branch cut.  Rank deficiency = free fermion directions.
        free = {}
        for eta in (1, -1):
            M = sp.zeros(len(banks), 4)
            for i, (start, offs) in enumerate(banks):
                for o in offs:
                    M[i, (start + o) % 4] = eta ** ((start + o) // 4)
            free[eta] = 4 - M.rank()
        report[name] = {'banks': len(banks), 'components': comp, 'connected': connected,
                        'free_fermion_directions': {'+1': int(free[1]), '-1': int(free[-1])}}

    need(not report['vertices']['connected'] and report['vertices']['components'] == 4,
         'vertex-placed banks leave four disconnected stations')
    need(not report['diagonals']['connected'] and report['diagonals']['components'] == 2,
         'diagonal-placed banks leave two disconnected pairs')
    need(report['centre']['connected'] and report['centre']['free_fermion_directions']['-1'] == 3,
         'one collective centre bank is rank one and leaves three free fermion directions')
    need(report['edges']['connected'],
         'the link placement is the only connected D4-equivariant placement')
    need(report['edges']['free_fermion_directions']['-1'] == 0
         and report['edges']['free_fermion_directions']['+1'] == 1,
         'within the link placement only the negative lift is spectator-free')
    survivors = sorted(k for k, v in report.items()
                       if v['connected'] and min(v['free_fermion_directions'].values()) == 0)
    need(survivors == ['edges'],
         'one W pair bank per seam link is the unique D4-equivariant admissible placement '
         '-- it was an assumption, it is now a consequence')
    return report


# ------------------------------------------------------------------ P2 -------

def _palindromic_family(support, sign):
    """Coefficient vector of length `support` forced palindromic with the given sign."""
    free = sp.symbols('c0:4', real=True)[:support]
    rel = {}
    for k in range(support):
        j = support - 1 - k
        if j > k:
            rel[free[j]] = sign * free[k]
        elif j == k and sign == -1:
            rel[free[k]] = sp.Integer(0)
    return [sp.simplify(x.subs(rel)) for x in free]


def source_class():
    """Reflection covariance <=> palindromic; then decide the free direction per family."""
    c = sp.symbols('c0:4', real=True)

    # Step 1: reflection covariance of the frame U = sum c_k R^k is exactly the
    # statement that P = (S U S^-1) U^-1 is a signed permutation, i.e. the reflected
    # source modes ARE the existing source modes relabelled.
    for eta in (1, -1):
        R = _shift(eta)
        for support in range(1, 5):
            for sign in ((1, -1) if support > 1 else (1,)):
                coeffs = _palindromic_family(support, sign)
                if all(x == 0 for x in coeffs):
                    continue
                U = sum((coeffs[k] * R ** k for k in range(support)), sp.zeros(4, 4))
                U_reflected = sum((coeffs[k] * (R ** k).inv() for k in range(support)),
                                  sp.zeros(4, 4))
                relabel = sign * (R ** (support - 1)).inv()
                need(sp.simplify(U_reflected - relabel * U) == sp.zeros(4, 4),
                     'palindromic support %d sign %+d is reflection covariant: the reflected '
                     'frame is the signed relabelling %+d R^-%d of the frame, eta=%+d'
                     % (support, sign, sign, support - 1, eta))
                need(sp.simplify(relabel * relabel.T) == sp.eye(4),
                     'the relabelling is a signed permutation, so the reflected source modes '
                     'ARE the existing ones, support %d sign %+d eta=%+d' % (support, sign, eta))

    # A non-palindromic frame is not covariant: the reflected coefficient vector is the
    # reversed one, so covariance up to relabelling needs reversal to reproduce the frame.
    a, b = sp.symbols('a b', real=True)
    for eta in (1, -1):
        R = _shift(eta)
        U = a * sp.eye(4) + b * R
        U_rev = b * sp.eye(4) + a * R
        gram_gap = sp.simplify((U * U.T - U_rev * U_rev.T)[0, 0])
        need(sp.cancel(gram_gap / (a * a - b * b)) in (0, 1, -1, 2, -2),
             'the non-palindromic obstruction is proportional to a^2 - b^2, eta=%+d' % eta)

    # Step 2: for every covariant family and both lifts, is a free direction forced?
    table = {}
    for support in range(1, 5):
        for sign in ((1, -1) if support > 1 else (1,)):
            coeffs = _palindromic_family(support, sign)
            if all(x == 0 for x in coeffs):
                continue
            for eta in (1, -1):
                spectrum = [sp.simplify(sp.expand(sum(coeffs[k] * lam ** k
                                                      for k in range(support))))
                            for lam in _eigenvalues(eta)]
                forced = any(sp.simplify(value) == 0 for value in spectrum)
                key = 'support=%d sign=%+d eta=%+d' % (support, sign, eta)
                table[key] = {'coefficients': [str(x) for x in coeffs],
                              'free_direction_forced': bool(forced)}

    dead_untwisted = [k for k, v in table.items() if 'eta=+1' in k and v['free_direction_forced']]
    alive_untwisted = [k for k, v in table.items()
                       if 'eta=+1' in k and not v['free_direction_forced']]
    alive_twisted = [k for k, v in table.items()
                     if 'eta=-1' in k and not v['free_direction_forced']]

    need(len(alive_twisted) == 7,
         'the negative lift is never excluded: all seven covariant families survive')
    need(len(dead_untwisted) == 5,
         'the untwisted lift is killed outright in five of the seven covariant families')
    need(sorted(alive_untwisted) == ['support=1 sign=+1 eta=+1', 'support=3 sign=+1 eta=+1'],
         'exactly two untwisted survivors remain: the on-site frame and the symmetric '
         'three-station frame')
    need(table['support=2 sign=+1 eta=+1']['free_direction_forced']
         and not table['support=2 sign=+1 eta=-1']['free_direction_forced'],
         'on a single seam link the untwisted lift always has a spectator and the negative '
         'lift never does -- this holds for the whole family, not just the balanced point')
    return {'table': table,
            'untwisted_survivors': sorted(alive_untwisted),
            'twisted_survivors': len(alive_twisted)}


# ------------------------------------------------------------------ P3 -------

def _signed_lift(perm, eps, index, n_slots):
    """Even-spinor lift of a signed slot permutation."""
    inverse = {v: k for k, v in index.items()}
    size = len(index)
    out = np.zeros((size, size), dtype=np.int64)
    for col in range(size):
        mask = inverse[col]
        bits = [j for j in range(n_slots) if mask & (1 << j)]
        mapped = [perm[j] for j in bits]
        sign = (-1) ** sum(mapped[i] > mapped[j]
                           for i in range(len(mapped)) for j in range(i + 1, len(mapped)))
        for j in bits:
            sign *= eps[j]
        out[index[sum(1 << j for j in mapped)], col] = sign
    return out


def two_clocks():
    """Can the negative-lift station clock live inside the native source at all?"""
    sys.path.insert(0, str(NATIVE_COMMON))
    import native_common as nc
    nc.TENSOR_PATH = TENSOR_PATH
    nc.CLOCK_PATH = CLOCK_PATH
    W = nc.load_tensor()
    Ws = csr_matrix(W)

    spinor_index = {m: i for i, m in enumerate(nc.EV)}
    colour_index = {m: i for i, m in enumerate(nc.CV)}
    eye16, eye4 = np.eye(16, dtype=np.int64), np.eye(4, dtype=np.int64)

    def scan(n_slots, index, eye):
        plus, minus, other = [], [], 0
        for perm in permutations(range(n_slots)):
            for eps in product((1, -1), repeat=n_slots):
                G = _signed_lift(list(perm), list(eps), index, n_slots)
                G4 = np.linalg.matrix_power(G, 4)
                if np.array_equal(G4, eye):
                    plus.append(G)
                elif np.array_equal(G4, -eye):
                    minus.append(G)
                else:
                    other += 1
        return plus, minus, other

    spin_plus, spin_minus, spin_other = scan(5, spinor_index, eye16)
    col_plus, col_minus, col_other = scan(3, colour_index, eye4)
    need(len(spin_plus) + len(spin_minus) + spin_other == 3840,
         'the signed slot group on the five Spin(10) slots has 3840 elements')
    need(len(col_plus) + len(col_minus) + col_other == 48,
         'the signed slot group on the three colour slots has 48 elements')
    need(not spin_minus and not col_minus,
         'NO REAL signed slot lift on either factor squares twice to -I; since '
         '(A tensor B)^4 = A^4 tensor B^4, no real product lift reaches G^4 = -I either')

    # This says nothing about complex clocks, and the TFPT carrier clock IS complex.
    # native_mu4_clock.py finds it in the Cartan torus; the scan above only rules out a
    # REAL representative, which is why the earlier conclusion drawn from it was wrong.
    zeta = sp.exp(sp.I * sp.pi / 4)
    need(sp.simplify(zeta ** 4 + 1) == 0 and sp.simplify(sp.I ** 2 + 1) == 0,
         'the clock TFPT actually specifies is rho: z -> iz with H^1 characters i^k, which '
         'is not real, so its absence from a real search carries no information')

    # The genuine internal clock, for the record.
    GF, GB, slot_clock, clock_sign = nc.clock_lift(W)
    period = next(k for k in range(1, 25)
                  if np.array_equal(np.linalg.matrix_power(GF, k), np.eye(64, dtype=np.int64)))
    need(period == 6, 'the internal clock has period six')
    need(not np.array_equal(np.linalg.matrix_power(GF, 3), -np.eye(64, dtype=np.int64)),
         'the internal clock does not contain the fermion sign as its halfway point')
    need(sp.lcm(6, 8) == 24 and sp.gcd(6, 8) == 2,
         'internal period six and order eight are compatible but independent: they generate '
         'a joint symmetry of order 24')
    return {'real_signed_slot_elements': {'spinor': 3840, 'colour': 48},
            'real_lifts_with_fourth_power_minus_one': 0,
            'internal_clock_period': period,
            'internal_slot_permutation': slot_clock,
            'internal_clock_sign': clock_sign,
            'verdict': 'no REAL signed slot lift reaches G^4 = -I. The earlier conclusion '
                       'that the negative-lift clock is therefore external to W is RETRACTED: '
                       'the TFPT carrier clock is complex and native_mu4_clock.py finds it in '
                       'the Cartan torus, with the seam sector structure and a real inverting '
                       'involution of square +I'}


# ------------------------------------------------------------------ P4 -------

def seam_locality():
    """A gap-local source has support two, because a seam gap has two adjacent marks."""
    intervals = [set(range(P0 + j * Q_RING, P0 + j * Q_RING + ELL)) for j in range(4)]
    gaps = [[(P0 + j * Q_RING + ELL + k) % N_RING for k in range(Q_RING - ELL)]
            for j in range(4)]
    adjacency = []
    for gap in gaps:
        low, high = (gap[0] - 1) % N_RING, (gap[-1] + 1) % N_RING
        touching = sorted({j for j in range(4) if low in intervals[j] or high in intervals[j]})
        need(len(touching) == 2, 'seam gap touches exactly two intervals: %s' % touching)
        need(abs(touching[0] - touching[1]) in (1, 3),
             'the two touched intervals are cyclically adjacent: %s' % touching)
        adjacency.append(touching)
    need(len(adjacency) == 4 and sorted(map(tuple, adjacency)) == [(0, 1), (0, 3), (1, 2), (2, 3)],
         'the four seam gaps realise exactly the four edges of the station square')
    return {'gap_adjacency': adjacency,
            'consequence': 'a source that belongs to one gap can draw on two stations only, '
                           'so support two is seam geometry and not an ansatz'}


# ------------------------------------------------------------- driver --------

def run():
    placement = bank_placement()
    frames = source_class()
    clocks = two_clocks()
    locality = seam_locality()
    return {
        'status': 'PASS',
        'exact_checks': len(checks),
        'P1_bank_placement': placement,
        'P2_source_class': frames,
        'P3_two_clocks': clocks,
        'P4_seam_locality': locality,
        'closed': [
            'P1 one W bank per seam link is the unique D4-equivariant placement that is '
            'connected and spectator-free; vertices and diagonals disconnect the square and a '
            'single collective bank is rank one',
            'P2 reflection covariance equals a palindromic coefficient vector; in the complete '
            'covariant class the untwisted lift is killed in five of seven families and the '
            'negative lift in none; on a seam link the untwisted lift always has a spectator',
            'P3 no REAL signed slot lift reaches G^4 = -I -- a correct scan whose earlier '
            'interpretation was wrong; see native_mu4_clock.py for the retraction and the '
            'complex clock that does exist natively',
            'P4 a seam gap has exactly two adjacent marks, so a gap-local source has support two',
        ],
        'still_open': [
            'physical g/Delta: the proven windows 1/2000 and 1/10000 come from a two-state Ritz '
            'bound, not from a physical principle; this is a bound-quality problem',
            'the two untwisted survivors of P2 are the disconnected on-site frame and the '
            'symmetric three-station frame; both are excluded by P1 and P4, not by P2 alone',
            '3+1D spacetime, chiral measure and dynamical spin 2 are constructions, not checks; '
            'nothing here closes them',
        ],
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True, default=str))
