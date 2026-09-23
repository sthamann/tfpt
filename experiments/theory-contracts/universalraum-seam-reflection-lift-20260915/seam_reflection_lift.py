"""Does the raw TFPT seam supply the joint reflection on fermion sites and pair banks?

The v1.6.10 selection theorem is conditional: it assumes an explicit vertex/edge
reflection acting at once on the four fermion stations and on the pair banks, and
lists `raw-seam to vertex/edge action` as not derived.  This module derives that
action from the two pinned TFPT objects instead of positing it.

Part 1  RAW SEAM.  The mu4-marked antiperiodic seam ring of v480 (N=256, four
        mu4-symmetric intervals, clock rho with rho^4 = -1).  Which reflections of
        the ring preserve the marked region, what is their lift square, do they
        invert the clock, do they preserve the state, and how do they act on the
        four intervals (fermion stations) versus the four gaps (pair links)?

Part 2  NATIVE SOURCE.  The pinned native tensor W (60 x 2016, W W^T = 8 I) with
        its clock lift (G_F, G_B) of period six.  Does a reflection lift S_F exist
        with S_F^2 = I, S_F G_F S_F^-1 = G_F^-1 and W Lambda^2(S_F) = S_B W, i.e.
        does the same reflection carry pair transitions to pair transitions with
        the tensor W unchanged?

Part 3  SELECTION.  Feed the seam-derived station matrices into the v1.6.10
        argument: reflection covariance of the two-site source forces equal weight
        magnitudes, and excluding free fermion directions then leaves eta = -1.

Part 4  SCOPE.  What this does not close.

Exact throughout: integer / signed-permutation algebra and sympy for Part 3; the
ring covariance in Part 1 is numerical free-fermion data at machine precision.
"""
import json
import sys
from itertools import permutations
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.sparse import csr_matrix

REPO = Path(__file__).resolve().parents[3]
NATIVE_COMMON = REPO / 'universal_room/new-3/universalraum-v1.6.9/agents/source/inputs'
TENSOR_PATH = REPO / ('experiments/theory-contracts/universalraum-v16-integrated-20260915'
                      '/sources/native_tensor.npz')
CLOCK_PATH = REPO / 'experiments/theory-contracts/compiler-involution-types/checker.py'

# v480 seam-ring geometry, unchanged.
N_RING = 256
Q_RING = N_RING // 4
P0 = 8
ELL = 48
TOL = 1e-12

checks = []


def need(condition, name):
    if not bool(condition):
        raise RuntimeError('FAILED: ' + name)
    checks.append(name)


# ---------------------------------------------------------------- Part 1 -----

def _correlator(n):
    ks = 2 * np.pi * (np.arange(n) + 0.5) / n
    ks = np.where(ks > np.pi, ks - 2 * np.pi, ks)
    occ = ks[np.abs(ks) < np.pi / 2]

    def cf(d):
        d = np.asarray(d, dtype=float)
        return (np.exp(1j * occ[:, None] * d.ravel()[None, :]).sum(axis=0) / n).reshape(d.shape)
    return cf


def _intervals(n_ring=N_RING, p0=P0, ell=ELL, shift_first=0):
    quarter = n_ring // 4
    out = [list(range(p0 + j * quarter, p0 + j * quarter + ell)) for j in range(4)]
    if shift_first:
        out[0] = [s + shift_first for s in out[0]]
    return out


def _gaps(n_ring=N_RING, p0=P0, ell=ELL):
    """The four links of the station square: the complement arcs between intervals."""
    quarter = n_ring // 4
    return [[(p0 + j * quarter + ell + k) % n_ring for k in range(quarter - ell)]
            for j in range(4)]


def _ap_image(site, centre, n_ring=N_RING, antiperiodic=True):
    """Reflection s -> centre - s on the ring; the wrap count carries the sign."""
    t, sign = centre - site, 1
    while t < 0:
        t += n_ring
        if antiperiodic:
            sign = -sign
    while t >= n_ring:
        t -= n_ring
        if antiperiodic:
            sign = -sign
    return t, sign


def _block_action(blocks, centre, n_ring=N_RING, antiperiodic=True):
    """Permutation induced on a list of arcs, plus the wrap sign where it is constant.

    An arc that straddles the antiperiodic branch cut picks up both signs; that is a
    property of the cut, not of the reflection, so the sign is reported as None there.
    """
    where = {s: j for j, arc in enumerate(blocks) for s in arc}
    image, signs = [], []
    for arc in blocks:
        targets, arc_signs = set(), set()
        for s in arc:
            t, sg = _ap_image(s, centre, n_ring, antiperiodic)
            if t not in where:
                return None
            targets.add(where[t])
            arc_signs.add(sg)
        if len(targets) != 1:
            return None
        image.append(targets.pop())
        signs.append(arc_signs.pop() if len(arc_signs) == 1 else None)
    if sorted(image) != list(range(len(blocks))):
        return None
    return image, signs


def _vertex_edge_pattern(n_ring, p0, ell, antiperiodic=True, shift_first=0):
    """Centres whose reflection permutes the four stations, with their station/link action."""
    out = {}
    for centre in range(n_ring):
        st = _block_action(_intervals(n_ring, p0, ell, shift_first), centre, n_ring, antiperiodic)
        if st is None:
            continue
        lk = _block_action(_gaps(n_ring, p0, ell), centre, n_ring, antiperiodic)
        out[centre] = (st, lk)
    return out


# ell must stay strictly below the quarter so that the four links are non-empty arcs.
ROBUSTNESS_CASES = [(256, 8, 48), (256, 0, 40), (256, 13, 30), (128, 5, 24), (512, 17, 96)]


def _robustness():
    """The vertex/edge offset must not depend on the ring size or the mark placement."""
    report = {}
    for n_ring, p0, ell in ROBUSTNESS_CASES:
        tag = 'N=%d p0=%d ell=%d' % (n_ring, p0, ell)
        pattern = _vertex_edge_pattern(n_ring, p0, ell)
        need(len(pattern) == 4, 'exactly four station-preserving reflections for ' + tag)
        vertex = [c for c, (st, _) in pattern.items() if st[0] == [0, 3, 2, 1]]
        need(len(vertex) == 1, 'exactly one vertex reflection for ' + tag)
        (st, lk) = pattern[vertex[0]]
        need(st[1] == [1, -1, -1, -1],
             'station signs are the antiperiodic wrap signs (1,eta,eta,eta) for ' + tag)
        need(lk is not None and all(lk[0][j] != j for j in range(4)),
             'the same reflection acts on the links without a fixed link for ' + tag)
        report[tag] = {'centres': sorted(pattern), 'vertex_centre': vertex[0],
                       'station_image': st[0], 'station_signs': st[1], 'link_image': lk[0]}
    return report


def _boundary_control():
    """eta is the seam boundary condition, not a modelling choice; plus a negative control."""
    periodic = _vertex_edge_pattern(N_RING, P0, ELL, antiperiodic=False)
    need(len(periodic) == 4, 'the periodic ring has the same four station reflections')
    vertex = [c for c, (st, _) in periodic.items() if st[0] == [0, 3, 2, 1]]
    need(len(vertex) == 1, 'the periodic ring has one vertex reflection')
    need(periodic[vertex[0]][0][1] == [1, 1, 1, 1],
         'on the PERIODIC ring the same reflection carries signs (1,1,1,1), i.e. eta = +1 -- '
         'so eta in the selection matrix J is the seam boundary condition, not a choice; the '
         'TFPT seam is antiperiodic because RP-admissibility forbids the zero mode (v480)')

    displaced = _vertex_edge_pattern(N_RING, P0, ELL, shift_first=1)
    need(not displaced,
         'NEGATIVE CONTROL: displacing one interval by a single site destroys every station '
         'reflection -- the joint action belongs to the mu4-symmetric configuration')
    return {'periodic_station_signs': [1, 1, 1, 1],
            'antiperiodic_station_signs': [1, -1, -1, -1],
            'displaced_reflections': 0}


def raw_seam():
    cf = _correlator(N_RING)
    sites = np.concatenate([np.arange(P0 + j * Q_RING, P0 + j * Q_RING + ELL) for j in range(4)])
    index = {int(s): i for i, s in enumerate(sites)}
    n = len(sites)
    cov = cf(sites[None, :] - sites[:, None])

    clock = np.zeros((n, n))
    for i, s in enumerate(sites):
        t, sign = int(s) + Q_RING, 1.0
        if t >= N_RING:
            t, sign = t - N_RING, -1.0
        need(t in index, 'clock closes on the marked region')
        clock[index[t], i] = sign
    need(np.allclose(np.linalg.matrix_power(clock, 4), -np.eye(n), atol=1e-14),
         'raw seam clock is the negative lift rho^4 = -I')
    need(np.allclose(np.linalg.matrix_power(clock, 8), np.eye(n), atol=1e-14),
         'raw seam clock has order eight')
    clock_inv = np.linalg.matrix_power(clock, 7)

    found = {}
    for centre in range(N_RING):
        refl = np.zeros((n, n))
        ok = True
        for i, s in enumerate(sites):
            t, sign = _ap_image(int(s), centre)
            if t not in index:
                ok = False
                break
            refl[index[t], i] = sign
        if not ok:
            continue
        need(np.allclose(refl @ refl, np.eye(n), atol=1e-14),
             'seam reflection centre %d is a true involution S^2 = +I' % centre)
        need(np.allclose(refl @ clock @ refl.T, clock_inv, atol=1e-14),
             'seam reflection centre %d inverts the clock, S rho S^-1 = rho^-1' % centre)
        state = float(np.abs(refl @ cov @ refl.conj().T - cov).max())
        need(state < 1e-12,
             'seam reflection centre %d preserves the state, omega o sigma = omega' % centre)
        found[centre] = (refl, state)

    need(len(found) == 4, 'exactly four reflections preserve the mu4-marked region')
    centres = sorted(found)
    need(centres == [63, 127, 191, 255], 'the four reflection centres are the half-integer marks')

    # The reflections are the clock translates of one another: <rho, S> is dihedral of order 16.
    base = found[63][0]
    for k, centre in enumerate(centres):
        need(np.allclose(found[centre][0], np.linalg.matrix_power(clock, k) @ base, atol=1e-13),
             'reflection centre %d equals rho^%d S, so <rho,S> is D8 of order 16 (not dicyclic)'
             % (centre, k))

    stations, links = {}, {}
    for centre in centres:
        stations[centre] = _block_action(_intervals(), centre)
        links[centre] = _block_action(_gaps(), centre)
        need(stations[centre] is not None, 'reflection centre %d permutes the four stations' % centre)
        need(links[centre] is not None, 'reflection centre %d permutes the four pair links' % centre)

    vertex_image, vertex_signs = stations[63]
    link_image, link_signs = links[63]
    need(vertex_image == [0, 3, 2, 1],
         'the seam reflection sigma is a VERTEX reflection of the station square '
         '(fixes marks 1 and -1, swaps i and -i)')
    need(sum(1 for j in range(4) if link_image[j] == j) == 0 and link_image == [3, 2, 1, 0],
         'the SAME reflection acts on the pair links without a fixed link, i.e. as the '
         'half-step EDGE reflection -- the vertex/edge offset is geometry, not an extra premise')
    need(vertex_signs == [1, -1, -1, -1],
         'the station signs are the antiperiodic wrap signs (1, eta, eta, eta) with eta = -1')

    edge_image, _ = stations[127]
    need(edge_image == [1, 0, 3, 2],
         'the clock translate rho.sigma is the EDGE reflection of the station square')

    return {
        'robustness': _robustness(),
        'boundary_control': _boundary_control(),
        'clock_negative_lift': True,
        'reflection_centres': centres,
        'reflection_square': '+I',
        'clock_conjugation': 'S rho S^-1 = rho^-1',
        'state_residual_max': max(found[c][1] for c in centres),
        'group': 'dihedral of order 16 generated by rho (rho^4 = -I) and S (S^2 = +I)',
        'station_action_vertex': {'image': vertex_image, 'signs': vertex_signs},
        'link_action_edge': {'image': link_image, 'signs': link_signs},
        'station_action_of_rho_sigma': edge_image,
    }


# ---------------------------------------------------------------- Part 2 -----

def _slot_compose(a, b):
    return [a[b[i]] for i in range(5)]


def _slot_inverse(a):
    out = [0] * 5
    for i, v in enumerate(a):
        out[v] = i
    return out


def native_source():
    sys.path.insert(0, str(NATIVE_COMMON))
    import native_common as nc
    nc.TENSOR_PATH = TENSOR_PATH
    nc.CLOCK_PATH = CLOCK_PATH

    W = nc.load_tensor()
    Ws = csr_matrix(W)
    need(nc.casimir_identity(W), 'pinned tensor satisfies the Casimir identity')
    GF, GB, slot_clock, clock_sign = nc.clock_lift(W)
    need(np.array_equal(np.linalg.matrix_power(GF, 6), np.eye(64, dtype=np.int64)),
         'native clock lift has period six on the 64 fermion modes')
    GF_inv = np.linalg.matrix_power(GF, 5)
    GB_inv = np.linalg.matrix_power(GB, 5)

    even_index = {m: i for i, m in enumerate(nc.EV)}

    def lift(slot):
        """Exterior lift of a slot permutation to the even Spin(10) spinor, then to 64 modes."""
        block = np.zeros((16, 16), dtype=np.int64)
        for col, mask in enumerate(nc.EV):
            mapped = [slot[j] for j in range(5) if mask & (1 << j)]
            sign = (-1) ** sum(mapped[i] > mapped[j]
                               for i in range(len(mapped)) for j in range(i + 1, len(mapped)))
            block[even_index[sum(1 << j for j in mapped)], col] = sign
        return np.kron(block, np.eye(4, dtype=np.int64))

    slot_inv = _slot_inverse(slot_clock)
    candidates = [list(s) for s in permutations(range(5))
                  if _slot_compose(_slot_compose(list(s), slot_clock), _slot_inverse(list(s))) == slot_inv]
    need(len(candidates) == 6,
         'the slot clock (0 2 1)(3 4) admits exactly six inverting slot reflections')

    eye64 = np.eye(64, dtype=np.int64)
    eye60 = np.eye(60, dtype=np.int64)
    accepted = []
    for slot in candidates:
        SF = lift(slot)
        need(np.array_equal(SF @ SF.T, eye64), 'reflection lift %s is orthogonal' % slot)
        need(np.array_equal(SF @ SF, eye64),
             'reflection lift %s squares to +I on the fermion modes (Pin-plus type)' % slot)
        need(np.array_equal(SF @ GF @ SF.T, GF_inv),
             'reflection lift %s realises sigma.rho.sigma = rho^-1 on the fermion modes' % slot)
        pair = nc.exterior_square_group(SF)
        SB = (Ws @ pair @ Ws.T).toarray() / 8
        need(np.allclose(SB, np.rint(SB)),
             'induced boson map of %s is integral' % slot)
        SB = np.rint(SB).astype(np.int64)
        residual = Ws @ pair - csr_matrix(SB) @ Ws
        residual.eliminate_zeros()
        need(residual.nnz == 0,
             'W Lambda^2(S_F) = S_B W holds exactly for %s -- the same reflection carries pair '
             'transitions to pair transitions with W unchanged' % slot)
        need(np.array_equal(SB @ SB, eye60),
             'induced pair-bank reflection of %s squares to +I' % slot)
        need(np.array_equal(SB @ GB @ SB.T, GB_inv),
             'induced pair-bank reflection of %s inverts the boson clock' % slot)
        accepted.append(slot)

    need(accepted == candidates,
         'every clock-inverting slot reflection lifts jointly to fermion modes and pair banks')
    return {
        'slot_clock': slot_clock,
        'slot_clock_sign': clock_sign,
        'clock_period': 6,
        'joint_reflections': accepted,
        'fermion_square': '+I',
        'pair_bank_square': '+I',
        'covariance': 'W Lambda^2(S_F) = S_B W, exact, tensor unchanged',
    }


# ---------------------------------------------------------------- Part 3 -----

def selection(seam):
    """The v1.6.10 argument, now driven by the station/link matrices the seam produced."""
    a, b = sp.symbols('a b', real=True)
    out = {}
    for eta in (1, -1):
        R = sp.Matrix([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [eta, 0, 0, 0]])
        image, signs = seam['station_action_vertex']['image'], seam['station_action_vertex']['signs']
        J = sp.zeros(4, 4)
        for col, (row, sign) in enumerate(zip(image, signs)):
            J[row, col] = sign if eta == -1 else abs(sign)
        L = R * J
        U = a * sp.eye(4) + b * R

        need(J * J == sp.eye(4), 'station reflection is an involution, eta=%d' % eta)
        need(J * R * J == R.inv(), 'station reflection inverts the clock, eta=%d' % eta)
        need(L * L == sp.eye(4), 'link reflection is an involution, eta=%d' % eta)
        need(U * J == L * (b * sp.eye(4) + a * R),
             'the joint reflection exchanges on-site and neighbour weight, eta=%d' % eta)

        forced = []
        for row in range(4):
            v, w = (U * J)[row, :], (L * U)[row, :]
            diff = sp.simplify(v.T * v - w.T * w)
            need(diff.subs(b, a) == sp.zeros(4) and diff.subs(b, -a) == sp.zeros(4),
                 'equal weight magnitudes keep the pair reflection exact, eta=%d row %d' % (eta, row))
            for entry in diff:
                if entry != 0:
                    need(sp.cancel(entry / (a * a - b * b)) in (1, -1),
                         'the only obstruction is a^2 - b^2, eta=%d row %d' % (eta, row))
                    forced.append(row)
        need(forced, 'reflection covariance forces |a| = |b|, eta=%d' % eta)

        balanced = U.subs({a: sp.sqrt(2) / 2, b: sp.sqrt(2) / 2})
        out[str(eta)] = {'balanced_rank': balanced.rank(),
                         'free_fermion_directions': 4 - balanced.rank()}

    need(out['1']['free_fermion_directions'] == 1,
         'the untwisted balanced frame keeps one free fermion direction')
    need(out['-1']['free_fermion_directions'] == 0,
         'only the negative lift eta = -1 removes every free fermion direction')

    # The v1.6.10 counter-model is the untwisted asymmetric frame a = 3/5, b = 4/5.
    # It survives clock covariance and still has a unique weak-coupling ground state,
    # but the seam reflection measures exactly a^2 - b^2, which is nonzero there.
    obstruction = (sp.Rational(3, 5) ** 2 - sp.Rational(4, 5) ** 2)
    need(obstruction == sp.Rational(-7, 25) != 0,
         'the untwisted asymmetric counter-model a=3/5, b=4/5 fails seam reflection covariance '
         'by a^2 - b^2 = -7/25')
    out['counter_model_obstruction'] = str(obstruction)
    return out


# ---------------------------------------------------------------- driver -----

def run():
    seam = raw_seam()
    native = native_source()
    sel = selection(seam)
    return {
        'status': 'PASS',
        'exact_checks': len(checks),
        'raw_seam': seam,
        'native_source': native,
        'selection': sel,
        'derived': [
            'the raw mu4-marked antiperiodic seam ring carries exactly four region-preserving '
            'reflections; each squares to +I, inverts the negative-lift clock and preserves the state',
            'one and the same seam reflection acts as a VERTEX reflection on the four fermion '
            'stations and as the half-step EDGE reflection on the four pair links -- the offset '
            'the v1.6.10 theorem had to assume is forced by the geometry of the square',
            'the station signs (1, eta, eta, eta) are the antiperiodic wrap signs, so the seam '
            'supplies the reflection matrix J with eta = -1 already built in',
            'the pinned native tensor W admits six reflection lifts S_F with S_F^2 = I, '
            'S_F G_F S_F^-1 = G_F^-1 and W Lambda^2(S_F) = S_B W exactly; the native source is '
            'dihedral-covariant, not merely clock-covariant',
        ],
        'not_derived': [
            'one W pair bank per seam link is still a composition assumption',
            'the nearest-neighbour two-site source frame is still an ansatz',
            'the period-six internal clock is not identified with the period-four station clock',
            'physical g/Delta, 3+1D spacetime, chiral measure and dynamical spin 2 remain open',
        ],
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True, default=str))
