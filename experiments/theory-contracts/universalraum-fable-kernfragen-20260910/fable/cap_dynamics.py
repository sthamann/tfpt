"""Corrected dynamical extension of the Wilson cap and the state/time connection.

Exact (rational) computations on the uncut rotor/CAR parent restricted to small
graphs (one ring; two disjoint rings = two plaquettes), plus exact formulas.
Research documentation for UPDATE-1; no RH / factoring / TOE claim.

Sections
  A. general graph model (CAR + integer link fluxes, Gauss law), leak theorem
  B. iterative source dressing of the cap code: exact leak sequence
  C. two-plaquette cap: energy increase, variance, balancing commutator,
     electric breathing of the balancing observable, leak
  D. volume window of the perturbative dressing (exact 2x2 Rabi reduction)
  E. state selection on the loop clock M_4: uniqueness of the marked-invariant
     state; four thermal roads to the same state; theta-function deviation
"""
from __future__ import annotations

from fractions import Fraction as F
import json
import math
from pathlib import Path
import sys

import mpmath as mp

HERE = Path(__file__).resolve().parent
A_LL, B_LH, C_LL2, EPS_L, M_H, E_EL = F(1, 12), F(1, 24), F(1, 576), F(1, 96), F(4), F(1, 200)
KAPPA = 2 * E_EL  # H_E = (kappa/2) sum E^2
MAX_ORDER = 3  # exact rational dressing orders 0..2 (order 3 exceeds the time budget)


def require(ok, message):
    if not ok:
        raise ValueError(message)


class Graph:
    """Sites 0..n-1, oriented links (x,y); L mode x, H mode n+x."""

    def __init__(self, n_sites, links):
        self.n = n_sites
        self.links = list(links)
        self.out = {x: [] for x in range(n_sites)}
        self.inc = {x: [] for x in range(n_sites)}
        for k, (x, y) in enumerate(self.links):
            self.out[x].append(k)
            self.inc[y].append(k)
        self.neighbors = {x: [] for x in range(n_sites)}
        for k, (x, y) in enumerate(self.links):
            self.neighbors[x].append((y, k, +1))
            self.neighbors[y].append((x, k, -1))

    # -- fermions -----------------------------------------------------------
    @staticmethod
    def fermion(mask, i, create):
        occupied = (mask >> i) & 1
        if create == bool(occupied):
            return None, 0
        sign = -1 if bin(mask & ((1 << i) - 1)).count("1") % 2 else 1
        return mask ^ (1 << i), sign

    def hop(self, state, amp, x, y, k, orient, s_from, s_to):
        mask, E = state
        i, j = x + self.n * s_from, y + self.n * s_to
        m1, s1 = self.fermion(mask, i, False)
        if m1 is None:
            return None
        m2, s2 = self.fermion(m1, j, True)
        if m2 is None:
            return None
        E = list(E)
        E[k] += orient
        return (m2, tuple(E)), amp * s1 * s2

    def gauss_ok(self, state):
        mask, E = state
        for x in range(self.n):
            q = ((mask >> x) & 1) + ((mask >> (x + self.n)) & 1) - 1
            div = sum(E[k] for k in self.out[x]) - sum(E[k] for k in self.inc[x])
            if q + div != 0:
                return False
        return True

    def diagonal(self, state):
        mask, E = state
        nL = sum((mask >> x) & 1 for x in range(self.n))
        nH = sum((mask >> (x + self.n)) & 1 for x in range(self.n))
        return EPS_L * nL + M_H * nH + E_EL * sum(e * e for e in E)

    def apply_H(self, vec):
        out = {}
        for state, amp in vec.items():
            add(out, state, amp * self.diagonal(state))
            for x in range(self.n):
                for (y, k, o) in self.neighbors[x]:
                    for (sf, st, coef) in ((0, 0, A_LL), (0, 1, B_LH), (1, 0, B_LH)):
                        res = self.hop(state, amp * coef, x, y, k, o, sf, st)
                        if res:
                            add(out, *res)
                    # two-link LL term of l^* A_U^2 l: direct endpoint bilinear c^dagger_{L,z} c_{L,x}
                    # with BOTH link shifts, no fermionic factor at the intermediate site y
                    # (reviewer correction 10 Sep 2026); non-backtracking z != x.
                    for (z, k2, o2) in self.neighbors[y]:
                        if z == x:
                            continue
                        res = self.two_link_hop(state, amp * C_LL2, x, z, ((k, o), (k2, o2)))
                        if res:
                            add(out, *res)
        return out

    def two_link_hop(self, state, amp, x, z, shifts):
        mask, E = state
        m1, s1 = self.fermion(mask, x, False)
        if m1 is None:
            return None
        m2, s2 = self.fermion(m1, z, True)
        if m2 is None:
            return None
        E = list(E)
        for (k, o) in shifts:
            E[k] += o
        return (m2, tuple(E)), amp * s1 * s2


def add(vec, key, amp):
    if amp == 0:
        return
    vec[key] = vec.get(key, 0) + amp
    if vec[key] == 0:
        del vec[key]


def axpy(out, vec, factor):
    for k, a in vec.items():
        add(out, k, a * factor)


def inner(u, v):
    return sum(a * v[k] for k, a in u.items() if k in v)


def shift_loop(state, loop_links, amount):
    mask, E = state
    E = list(E)
    for k in loop_links:
        E[k] += amount
    return (mask, tuple(E))


def S_loop(state, loop_links, key_link, power=1):
    """S = W(I-P3)+W^{-3}P3 on the loop; negative powers via S^{-1} = S^3."""
    for _ in range(power % 4):
        shift = -3 if state[1][key_link] % 4 == 3 else 1
        state = shift_loop(state, loop_links, shift)
    return state


def leak_of_family(graph, vecs):
    """<d_a, H(I-P)H d_b> / (norms) for an orthogonal family; returns matrix and HJ."""
    HJ = [graph.apply_H(v) for v in vecs]
    n = len(vecs)
    norms2 = [inner(v, v) for v in vecs]
    JHJ = [[inner(vecs[a], HJ[b]) for b in range(n)] for a in range(n)]
    JH2J = [[inner(HJ[a], HJ[b]) for b in range(n)] for a in range(n)]
    leak = [[JH2J[a][b] - sum(JHJ[k][a] * JHJ[k][b] / norms2[k] for k in range(n)) for b in range(n)]
            for a in range(n)]
    return leak, HJ, JHJ, norms2


def gram_schmidt(vecs):
    """Exact unnormalized Gram-Schmidt (rational amplitudes)."""
    out = []
    for v in vecs:
        w = dict(v)
        for u in out:
            axpy(w, u, -inner(u, v) / inner(u, u))
        out.append(w)
    return out


def dress_once(graph, vecs, HJ, JHJ, norms2):
    """First-order dressing of each vector by the leaked components of H v (nonresonant)."""
    dressed = []
    for a, v in enumerate(vecs):
        Ea = JHJ[a][a] / norms2[a]
        w = dict(v)
        # component of H v orthogonal to the family
        res = dict(HJ[a])
        for k in range(len(vecs)):
            axpy(res, vecs[k], -inner(vecs[k], HJ[a]) / norms2[k])
        for h, amp in res.items():
            Eh = graph.diagonal(h)
            require(Eh != Ea, "nonresonant")
            add(w, h, -amp / (Eh - Ea))
        dressed.append(w)
    return dressed


# --------------------------------------------------------------------------
def section_ring():
    g = Graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    loop = [0, 1, 2, 3]
    omega0 = (0b1111, (0, 0, 0, 0))
    code = [{S_loop(omega0, loop, 0, a): F(1)} for a in range(4)]
    out = {"N_dir": 8}
    fam = code
    seq = []
    for order in range(MAX_ORDER):
        fam = gram_schmidt(fam)  # exact, unnormalized orthogonal family
        leak, HJ, JHJ, norms2 = leak_of_family(g, fam)
        diag = [leak[a][a] / norms2[a] for a in range(4)]
        offdiag = max((abs(float(leak[a][b])) / math.sqrt(float(norms2[a] * norms2[b]))
                       for a in range(4) for b in range(4) if a != b), default=0.0)
        require(all(leak[a][b] == leak[b][a] for a in range(4) for b in range(4)), "leak matrix symmetric")
        support = [len(v) for v in fam]
        sys.set_int_max_str_digits(0)
        exact = [str(d) for d in diag] if order <= 1 else None  # higher orders: rationals with >4300 digits
        seq.append({"order": order, "leak_diag_exact": exact,
                    "leak_diag_denominator_digits": [len(str(d.denominator)) for d in diag],
                    "leak_float": [float(d) for d in diag],
                    "max_offdiag_float": offdiag, "support_states": support})
        if order == 0:
            require(all(d == 8 * B_LH * B_LH for d in diag) and offdiag == 0, "bare leak 8 b^2, diagonal")
        fam = dress_once(g, fam, HJ, JHJ, norms2)
    ratios = [seq[k]["leak_float"][0] / seq[k + 1]["leak_float"][0] for k in range(len(seq) - 1)]
    out["iterative_dressing"] = seq
    out["reduction_factors"] = ratios
    out["recursion_definition"] = ("E_v := <v,Hv>/||v||^2 (Rayleigh value of the current vector) for vectors spread over "
                                   "several diagonal energies; the family is re-orthogonalized exactly before each step; "
                                   "marks are not carried along in this computation")
    # Duhamel contract needs the full residual operator norm, not one initial column:
    # ||R||^2 <= max_a sum_b |(R^*R)_ab| (normalized), reported per order from the full leak matrix.
    out["duhamel_bounds"] = duhamel_bounds(g, code)
    out["flux_window_caveat"] = flux_window_caveat()
    return out


def duhamel_bounds(g, code):
    fam = code
    rows = []
    for order in range(MAX_ORDER):
        fam = gram_schmidt(fam)
        leak, HJ, JHJ, norms2 = leak_of_family(g, fam)
        n = len(fam)
        normalized = [[float(leak[a][b]) / math.sqrt(float(norms2[a] * norms2[b])) for b in range(n)] for a in range(n)]
        row_sum_bound = max(sum(abs(normalized[a][b]) for b in range(n)) for a in range(n))
        rows.append({"order": order, "sqrt_max_row_sum_RR": math.sqrt(row_sum_bound),
                     "min_column_sqrt": math.sqrt(min(normalized[a][a] for a in range(n))),
                     "note": "uniform Duhamel coefficient ||R|| <= sqrt(max_a sum_b |(R^*R)_ab|); a single column value is not a trajectory bound"})
        fam = dress_once(g, fam, HJ, JHJ, norms2)
    # exact counterexample (REVIEW-FABLE-ZUSATZ sec. 1): H = tridiagonal(1) on C^3, V = (e1,e2), R v = 0 for v = e1
    # but R h v = e3 != 0, so the column bound 0 is false; the full ||R|| = 1 is the safe coefficient.
    H3 = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    h = [[0, 1], [1, 0]]
    R = [[0, 0], [0, 0], [0, 1]]  # HV - Vh in the e3 row
    Rv = [sum(R[i][j] * [1, 0][j] for j in range(2)) for i in range(3)]
    hv = [sum(h[i][j] * [1, 0][j] for j in range(2)) for i in range(2)]
    Rhv = [sum(R[i][j] * hv[j] for j in range(2)) for i in range(3)]
    require(Rv == [0, 0, 0] and Rhv == [0, 0, 1], "Duhamel column-bound counterexample reproduced")
    return {"per_order": rows, "counterexample_3x3": {"R v": Rv, "R h v": Rhv, "conclusion": "column bound 0 is false; ||R|| = 1"}}


def flux_window_caveat():
    """Hop detuning Delta(E) = M - eps_L + (2 sigma E + 1)/200 is not uniformly ~4 on the rotor."""
    def Delta(sE):
        return M_H - EPS_L + F(2 * sE + 1, 200)
    require(Delta(0) == F(9587, 2400), "Delta at zero flux")
    require(Delta(-399) == F(11, 2400) and abs(B_LH / Delta(-399)) == F(100, 11), "b/Delta = 100/11 at sigma E = -399")
    require(Delta(-400) < 0, "denominator changes sign at sigma E = -400")
    return {"Delta_zero_flux": str(Delta(0)), "Delta_at_sigmaE_-399": str(Delta(-399)), "b_over_Delta": str(abs(B_LH / Delta(-399))),
            "statement": "the dressing is controlled only on the tested flux window (|E| small); it is not uniform on the uncut rotor"}


def section_scope_theorem1():
    """Exact: for an all-low code that is NOT H_diag-invariant the leak exceeds b^2 N_dir.

    Gamma^*Gamma = b^2 N_dir I + J^* H_diag (I-JJ^*) H_diag J  (the two pieces live in orthogonal
    sectors: all-low flux states versus one-high states).  Witness: v = |flux 0> + |flux 1>
    (unnormalized), leak/||v||^2 = 8 b^2 + (E_1 - E_0)^2 / 4 with E_1 - E_0 = 4 e = 1/50.
    """
    g = Graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    loop = [0, 1, 2, 3]
    s0 = (0b1111, (0, 0, 0, 0))
    s1 = S_loop(s0, loop, 0, 1)
    v = {s0: F(1), s1: F(1)}
    leak, HJ, JHJ, norms2 = leak_of_family(g, [v])
    ratio = leak[0][0] / norms2[0]
    dE = g.diagonal(s1) - g.diagonal(s0)
    require(dE == 4 * E_EL, "flux-1 minus flux-0 electric energy is 4e")
    require(ratio == 8 * B_LH * B_LH + dE * dE / 4, "leak = b^2 N_dir + electric variance of the superposition")
    return {"superposition_leak": str(ratio), "b2_Ndir": str(8 * B_LH * B_LH), "extra_H_diag_term": str(dE * dE / 4),
            "statement": "equality Gamma*Gamma = b^2 N_dir I holds for H_diag-invariant codes (flux basis vectors); general all-low codes add the positive term J*H_diag(I-JJ*)H_diag J"}


def section_krylov_block():
    """Codex ERWEITERUNG on the ring: V1 = (J, eta), eta = Gamma/g; exact block, moments, H^4 defect.

    Compared with the source dressing (which changes the preparation) the Krylov block keeps the
    preparation and adds the leaked direction as a new isometric block.
    """
    g = Graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    loop = [0, 1, 2, 3]
    omega0 = (0b1111, (0, 0, 0, 0))
    J = [{S_loop(omega0, loop, 0, a): F(1)} for a in range(4)]
    HJ = [g.apply_H(v) for v in J]
    # Gamma J_a = (I - P_J) H J_a  (unnormalized eta; ||Gamma J_a||^2 = g^2 = 8 b^2)
    eta = []
    for a in range(4):
        w = dict(HJ[a])
        for k in range(4):
            axpy(w, J[k], -inner(J[k], HJ[a]))
        eta.append(w)
    g2 = [inner(e, e) for e in eta]
    require(all(x == 8 * B_LH * B_LH for x in g2), "||eta_a||^2 = g^2 = 8 b^2")
    require(all(inner(J[a], eta[b]) == 0 for a in range(4) for b in range(4)), "J^* eta = 0")
    require(all(inner(eta[a], eta[b]) == 0 for a in range(4) for b in range(4) if a != b), "eta blocks orthogonal")
    Heta = [g.apply_H(e) for e in eta]
    # coupling block: <J_a, H eta_b>/g = g delta_ab  (since <J_a,H eta_b> = <Gamma J_a, Gamma J_b>)
    coup = [[inner(J[a], Heta[b]) for b in range(4)] for a in range(4)]
    require(all(coup[a][b] == (8 * B_LH * B_LH if a == b else 0) for a in range(4) for b in range(4)), "coupling block g I (squared entries g^2)")
    h0 = [[inner(J[a], HJ[b]) for b in range(4)] for a in range(4)]
    h1 = [[inner(eta[a], Heta[b]) / (8 * B_LH * B_LH) for b in range(4)] for a in range(4)]
    require(all(h1[a][b] == h1[b][a] for a in range(4) for b in range(4)), "h1 symmetric (off-diagonal loop coupling allowed)")
    # residual of the new column and moment identities
    fam = J + eta
    leakm, HF, JHF, nf = leak_of_family(g, fam)
    RRm = [[leakm[4 + a][4 + b] / (8 * B_LH * B_LH) for b in range(4)] for a in range(4)]  # R^*R for normalized eta
    RR = [RRm[a][a] for a in range(4)]
    require(all(leakm[a][a] == 0 for a in range(4)), "J columns have no residual outside V1 (HJ in ran V1)")
    # moments: J^*H^k J vs (V1^*HV1)^k for k <= 3 exact, H^4 defect = g^2 R^*R
    def matmul(A, B):
        n = len(A)
        return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    gval2 = 8 * B_LH * B_LH
    # work with unnormalized eta but rescale: use normalized block entries via sqrt-free trick:
    # (V1^*HV1) in basis (J, eta/g): [[h0, gI],[gI, h1]]; its powers restricted to J-J block involve g^2 only.
    # Compute J^*H^k J exactly by repeated application.
    def power_moment(k):
        vecs = [dict(v) for v in J]
        for _ in range(k):
            vecs = [g.apply_H(v) for v in vecs]
        return [[inner(J[a], vecs[b]) for b in range(4)] for a in range(4)]
    def block_power_JJ(k):
        # 8x8 matrix in basis (J, eta_norm); entries with sqrt(g^2) appear only in odd positions; the
        # JJ block of powers is a polynomial in g^2.  Build with symbolic g via a 2-step trick:
        # represent numbers as pairs (p, q) meaning p + q*g with g^2 = gval2 (all rational).
        def mul(x, y):
            return (x[0] * y[0] + x[1] * y[1] * gval2, x[0] * y[1] + x[1] * y[0])
        def addp(x, y):
            return (x[0] + y[0], x[1] + y[1])
        M = [[(F(0), F(0)) for _ in range(8)] for _ in range(8)]
        for a in range(4):
            for b in range(4):
                M[a][b] = (h0[a][b], F(0))
                M[4 + a][4 + b] = (h1[a][b], F(0))
            M[a][4 + a] = (F(0), F(1))
            M[4 + a][a] = (F(0), F(1))
        P = [[((F(1), F(0)) if i == j else (F(0), F(0))) for j in range(8)] for i in range(8)]
        def sum_pairs(items):
            acc = (F(0), F(0))
            for it in items:
                acc = addp(acc, it)
            return acc
        for _ in range(k):
            P = [[sum_pairs([mul(P[i][l], M[l][j]) for l in range(8)]) for j in range(8)] for i in range(8)]
        return [[P[a][b] for b in range(4)] for a in range(4)]
    moments_ok = []
    for k in range(4):
        full = power_moment(k)
        red = block_power_JJ(k)
        ok = all(red[a][b][1] == 0 and red[a][b][0] == full[a][b] for a in range(4) for b in range(4))
        moments_ok.append(ok)
    require(all(moments_ok), "moments 0..3 reproduced exactly by the V1 block")
    full4 = power_moment(4)
    red4 = block_power_JJ(4)
    defect = [[full4[a][b] - red4[a][b][0] for b in range(4)] for a in range(4)]
    require(all(red4[a][b][1] == 0 for a in range(4) for b in range(4)), "H^4 block power rational")
    require(all(defect[a][b] == gval2 * RRm[a][b] for a in range(4) for b in range(4)),
            "H^4 defect = g^2 R^*R (full 4x4 matrix)")
    # onsite exchange channel Z0 ~ sum_x d_x^* l_x J and two-pair channel norm on the ring
    def onsite_exchange(vec):
        out = {}
        for st, amp in vec.items():
            for x in range(4):
                m1, s1 = Graph.fermion(st[0], x, False)
                if m1 is None:
                    continue
                m2, s2 = Graph.fermion(m1, 4 + x, True)
                if m2 is None:
                    continue
                add(out, (m2, st[1]), amp * s1 * s2)
        return out
    Z0 = [onsite_exchange(v) for v in J]   # norm^2 = N = 4
    require(all(inner(Z0[a], Z0[a]) == 4 for a in range(4)), "onsite channel norm N")
    z0_coupling = [inner(Z0[a], Heta[a]) for a in range(4)]   # unnormalized: <sum d*l J, H Gamma J>
    require(all(z == -2 * A_LL * B_LH * 4 for z in z0_coupling),
            "onsite-exchange coupling <sum d*l J, H Gamma J> = -deg * a * b * N with ring degree 2")
    return {"g2": str(gval2), "h0_diag": [str(h0[a][a]) for a in range(4)],
            "h1_matrix": [[str(h1[a][b]) for b in range(4)] for a in range(4)],
            "h1_minus_h0_diag": [str(h1[a][a] - h0[a][a]) for a in range(4)],
            "RR_matrix_normalized_eta": [[str(RRm[a][b]) for b in range(4)] for a in range(4)],
            "RR_diag_float": [float(r) for r in RR],
            "moments_0_to_3_exact": moments_ok, "H4_defect_diag": [str(defect[a][a]) for a in range(4)],
            "onsite_exchange_coupling_unnormalized": [str(z) for z in z0_coupling],
            "onsite_exchange_coupling_formula": "<sum_x d_x^* l_x J, H Gamma J> = -deg a b N; normalized by sqrt(N) g this is -deg a b sqrt(N)/g (torus deg 6: -6ab sqrt(N)/g = -1/sqrt(24), Codex ERWEITERUNG sec. 3; ring deg 2: -1/36 unnormalized)",
            "comparison": "Krylov block keeps the preparation (psi,0) and reproduces moments 0..3 exactly; the order-1 source dressing changes the preparation and reduces the leak of the prepared family to 3.32e-5; both are built from H alone"}


def section_two_plaquettes():
    # two disjoint rings: sites 0-3 (loop 1, links 0-3) and 4-7 (loop 2, links 4-7)
    links = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4)]
    g = Graph(8, links)
    l1, l2 = [0, 1, 2, 3], [4, 5, 6, 7]
    omega0 = (0b11111111, (0,) * 8)
    require(g.gauss_ok(omega0), "Omega0 Gauss")
    code = {}
    for a in range(4):
        for b in range(4):
            st = S_loop(S_loop(omega0, l1, 0, a), l2, 4, b)
            require(g.gauss_ok(st), "code Gauss")
            code[(a, b)] = st
    vecs = [{code[(a, b)]: F(1)} for a in range(4) for b in range(4)]
    leak, HJ, JHJ, norms2 = leak_of_family(g, vecs)
    n_dir = 16
    require(all(leak[i][j] == (n_dir * B_LH * B_LH if i == j else 0) for i in range(16) for j in range(16)),
            "16-dim cap code leak = N_dir b^2 I")
    # cap state Psi = (1/2) sum_a S1^a S2^{-a} Omega0
    cap = {}
    for a in range(4):
        st = S_loop(S_loop(omega0, l1, 0, a), l2, 4, -a)
        add(cap, st, F(1, 2))
    require(inner(cap, cap) == 1, "cap normalized")
    Hcap = g.apply_H(cap)
    E0 = g.diagonal(omega0)
    mean = inner(cap, Hcap)
    energies = [g.diagonal(st) - E0 for st in cap]
    var_el = sum(F(1, 4) * (e - (mean - E0)) ** 2 for e in energies)
    full_var = inner(Hcap, Hcap) - mean * mean
    require(mean - E0 == 14 * KAPPA, "cap energy increase 14 kappa")
    require(var_el == 68 * KAPPA * KAPPA, "electric variance 68 kappa^2")
    require(full_var == var_el + n_dir * B_LH * B_LH, "full variance = electric + leak")
    # balancing operator T_bal = S1 S2^{-1}; commutator norm on the all-low sector
    def T_bal(vec):
        out = {}
        for st, amp in vec.items():
            add(out, S_loop(S_loop(st, l1, 0, 1), l2, 4, -1), amp)
        return out
    require(inner(cap, T_bal(cap)) == 1, "cap is T_bal invariant")
    comm = dict(g.apply_H(T_bal(cap)))
    axpy(comm, T_bal(Hcap), F(-1))
    alllow = {k: v for k, v in comm.items() if k[0] == 0b11111111}
    require(inner(alllow, alllow) == 208 * KAPPA * KAPPA, "||P_AllLow [H,T_bal] Psi||^2 = 208 kappa^2")
    # electric breathing: <Psi(t), T_bal Psi(t)> under H_E alone = (1/4) sum_a e^{i(E_{a+1}-E_a)t}
    diffs = [energies[(a + 1) % 4] - energies[a] for a in range(4)]
    require(sorted(diffs) == sorted([20 * KAPPA, -4 * KAPPA, 4 * KAPPA, -20 * KAPPA]), "level differences")
    revival = 2 * math.pi / float(4 * KAPPA)
    return {"N_dir": n_dir, "leak_diag": str(n_dir * B_LH * B_LH),
            "cap_energy_increase": str(mean - E0), "electric_variance": str(var_el),
            "full_variance": str(full_var), "balancing_commutator_alllow": str(inner(alllow, alllow)),
            "cap_relative_energies": [str(e) for e in energies],
            "T_bal_expectation_under_H_E": "(1/2)[cos(20 kappa t) + cos(4 kappa t)] = (1/2)[cos(t/5)+cos(t/25)]",
            "electric_revival_time": revival,
            "log_time_comparison": "under alpha_t(S_m)=m^{it}S_m the cap and T_bal are stationary; under H_E they breathe with period 2 pi/(4 kappa)"}


def section_two_level_model():
    """ISOLATED 2x2 MODEL VALUES ONLY (not physical weights of the parent).

    The exact coupling block g I (g^2 = N_dir b^2) is a compression, not an invariant two-level
    space: ERWEITERUNG.md proves R_1 = (I - V_1V_1^*)H eta != 0 with R_1^*R_1 >= I/24 + G_2.  The
    numbers below are properties of the auxiliary matrix [[0, g],[g, Delta]] with the constant
    Delta = 9587/2400 and are reported only to separate two model quantities that must not be
    confused: the eigenvector high weight and the normalized first-order vector weight.
    """
    Delta = F(9587, 2400)  # M - eps_L + kappa/2
    d = float(Delta)
    rows = []
    for label, n_dir in (("ring", 8), ("two rings", 16), ("L=5 torus", 750)):
        g2 = float(n_dir * B_LH * B_LH)
        eig_weight = 0.5 * (1 - d / math.sqrt(d * d + 4 * g2))
        first_order_weight = g2 / (d * d + g2)
        rows.append({"graph": label, "g2": str(n_dir * B_LH * B_LH), "model_eigenvector_high_weight": eig_weight,
                     "model_first_order_vector_high_weight": first_order_weight})
    torus = rows[-1]
    require(abs(torus["model_eigenvector_high_weight"] - 0.065858) < 2e-6 and abs(torus["model_first_order_vector_high_weight"] - 0.075445) < 2e-6,
            "N=125 model values 6.5858 % and 7.5445 % (REVIEW-FABLE-ZUSATZ sec. 2)")
    return {"rows": rows,
            "status": "auxiliary two-level model; NOT a theorem about the parent (the first block is not invariant: R_1 != 0), no volume threshold or orthogonality catastrophe is asserted",
            "what_is_proved": "the exact first coupling of the global all-low preparation grows like sqrt(N_dir) b = sqrt(N/96) on the torus"}


def section_state_selection():
    """On M_4 = C*(Z,S): the unique Ad(S), Ad(Z)-invariant state is the trace; four roads to it."""
    import numpy as np
    w = np.exp(2j * np.pi / 4)
    Z = np.diag([w ** k for k in range(4)])
    S = np.roll(np.eye(4), 1, axis=0)
    require(np.allclose(Z @ S, w * S @ Z), "ZS = iSZ")
    # invariant states: rho with S rho S^* = rho and Z rho Z^* = rho -> rho = I/4
    basis = [np.outer(np.eye(4)[a], np.eye(4)[b]) for a in range(4) for b in range(4)]
    cons = []
    for X in (S, Z):
        cons.append(np.array([(X @ B @ X.conj().T - B).flatten() for B in basis]).T)
    Mc = np.vstack(cons)
    null = 16 - np.linalg.matrix_rank(Mc)
    require(null == 1, "unique invariant state (trace) on M_4")
    # cap restriction to loop 1 is the trace: <Psi, F_ab^{(1)} Psi> = delta_ab / 4  (exact, from section C fluxes)
    # thermal roads
    mp.mp.dps = 40
    kappa = mp.mpf(1) / 100
    def electric_weights(beta):
        Zs = mp.nsum(lambda n: mp.e ** (-beta * kappa / 2 * n * n), [-mp.inf, mp.inf])
        return [mp.nsum(lambda k, r=r: mp.e ** (-beta * kappa / 2 * (4 * k + r) ** 2), [-mp.inf, mp.inf]) / Zs for r in range(4)]
    roads = []
    for beta in (mp.mpf("0.1"), mp.mpf(1), mp.mpf(10), mp.mpf(100), mp.mpf(1000)):
        ws = electric_weights(beta)
        dev = max(abs(x - mp.mpf(1) / 4) for x in ws)
        bound = 2 * mp.nsum(lambda k: mp.e ** (-2 * mp.pi ** 2 * k * k / (beta * kappa * 16)), [1, mp.inf])
        roads.append({"beta_electric": str(beta), "weights_mod4": [mp.nstr(x, 10) for x in ws],
                      "max_deviation": mp.nstr(dev, 5), "poisson_bound": mp.nstr(bound, 5)})
        require(dev <= bound + mp.mpf(10) ** -30, "theta deviation within Poisson bound")
    return {"unique_marked_invariant_state": "normalized trace on M_4 (null space dimension 1; numpy rank of an exact integer system)",
            "restricted_coincidences_on_residue_algebra": [
                "cap restriction to one loop clock M_4 (exact from the flux pattern)",
                "critical ax+b state tau (KRITISCHER-GRENZZUSTAND: weak* limit of the zeta density operators on the affine C*-algebra) restricted to residues mod 4",
                "beta->1+ limit of the zeta-Gibbs residue laws (checks.json gibbs_residues; per fixed modulus only)",
                "beta->0 limit of the electric Gibbs residue laws exp(-beta kappa E^2/2)"],
            "not_identified": "the full pure two-loop cap is NOT identified with the full critical/Haar state (I_4/4 and |+><+| share the diagonal but differ on the shift); H_log acts trivially on the diagonal algebra, so KMS there selects no temperature",
            "electric_gibbs_roads": roads,
            "poisson_bound_formula": "|w_r - 1/4| <= 2 sum_{k>=1} exp(-2 pi^2 k^2 /(16 beta kappa)) = 2 exp(-pi^2/(8 beta kappa)) + ...",
            "not_a_ground_state": "beta -> infinity gives weights (1,0,0,0): the Frobenius weights are a prepared/hot feature, never the electric ground state",
            "finite_energy_box_alternative": box_approximation(),
            "local_gauss_preserving_covering": local_covering()}


def box_approximation():
    """KRITISCHER-GRENZZUSTAND sec. 5: sigma_K uniform on -K..K; residue error <= 1/(2K+1), energy kappa K(K+1)/6."""
    out = []
    for K in (3, 10, 50):
        span = 2 * K + 1
        worst = F(0)
        for n in (2, 3, 4, 5, 7):
            for r in range(n):
                hits = sum(1 for k in range(-K, K + 1) if k % n == r)
                worst = max(worst, abs(F(hits, span) - F(1, n)))
        require(worst <= F(1, span), "residue projection error <= 1/(2K+1)")
        energy = sum(F(k * k, 1) for k in range(-K, K + 1)) / span * KAPPA / 2
        require(energy == KAPPA * K * (K + 1) / 6, "electric energy kappa K(K+1)/6")
        out.append({"K": K, "worst_residue_error": str(worst), "bound": str(F(1, span)), "electric_energy_one_rotor": str(energy),
                    "electric_energy_neutral_plaquette": str(4 * energy)})
    return {"rows": out, "statement": "finite-energy, explicit-error approximation of the critical residue weights; prepared mixed state, not stationary, physical selection open"}


def local_covering():
    """S_m^(p)|E> = |E + (m-1) E_e p> on the ring flux space: injective, Gauss-preserving, S W = W^m S."""
    p = (1, 1, 1, 1)
    def S(m, E):
        return tuple(E[k] + (m - 1) * E[0] * p[k] for k in range(4))
    def W(E, power=1):
        return tuple(E[k] + power * p[k] for k in range(4))
    fluxes = [(e0, e1, e2, e3) for e0 in range(-3, 4) for e1 in range(-2, 3) for e2 in range(-2, 3) for e3 in range(-2, 3)]
    for m in (2, 3):
        images = [S(m, E) for E in fluxes]
        require(len(set(images)) == len(images), "S_m^(p) injective on the sampled flux box")
        require(all(img[0] % m == 0 for img in images), "image lies in E_e = 0 mod m")
        require(all(S(m, W(E)) == W(S(m, E), m) for E in fluxes), "S_m^(p) W = W^m S_m^(p)")
        # divergence on the ring: div_x = E_x - E_{x-1}; unchanged since p is divergence free
        require(all([img[k] - img[k - 1] for k in range(4)] == [E[k] - E[k - 1] for k in range(4)]
                    for E, img in zip(fluxes, images)), "Gauss divergence unchanged")
    return {"statement": "explicit bounded local isometry on the full flux space (membership in the large rotor algebra), Gauss-preserving for every matter configuration; not generated with controlled cost by H"}


def two_link_witness():
    g = Graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    start, target = (75, (0, 0, 0, 0)), (78, (1, 1, 0, 0))
    require(g.gauss_ok(start), "witness Gauss")
    out = g.apply_H({start: F(1)})
    require(out.get(target, 0) == F(-1, 576), "native two-link endpoint amplitude -1/576")
    return {"start": [75, [0, 0, 0, 0]], "target": [78, [1, 1, 0, 0]], "amplitude": str(out[target])}


def record():
    return {"status": "CAP_DYNAMICS_AND_STATE_CONNECTION",
            "claims_not_made": ["no RH", "no factoring speedup", "no TOE/T1-T8 closure",
                                "no derivation of the parent from P1/P2",
                                "one- and two-ring graphs do not establish a general TFPT dynamics", "no volume threshold, no all-order dressing statement, no minimality claim"],
            "evidence_classes": {
                "exact_fraction": ["two_link_witness", "scope_theorem1", "krylov_block", "ring.iterative_dressing", "ring.flux_window_caveat", "two_plaquettes (all rational entries)", "state_selection.finite_energy_box_alternative", "state_selection.local_gauss_preserving_covering", "ring.duhamel_bounds.counterexample_3x3"],
                "float_formula_model_values": ["two_level_model (auxiliary 2x2 only)", "two_plaquettes.electric_revival_time", "ring.duhamel_bounds (float sqrt of exact entries)"],
                "numpy_rank": ["state_selection.unique_marked_invariant_state"],
                "mpmath_numeric": ["state_selection.electric_gibbs_roads"]},
            "two_link_witness": two_link_witness(),
            "scope_theorem1": section_scope_theorem1(),
            "krylov_block": section_krylov_block(),
            "ring": section_ring(),
            "two_plaquettes": section_two_plaquettes(),
            "two_level_model": section_two_level_model(),
            "state_selection": section_state_selection()}


if __name__ == "__main__":
    out = record()
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "cap_dynamics.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
