"""Exact, vectorised Krylov computation of the N=64 sector of the pinned native
Fock model, in the hole picture (H_hole). Produces rigorous variational (Ritz)
upper bounds on the ground energy, closure tests, observables, the one-particle
charged response and sector-selection bounds.

NON-RH research contract: no paper/ledger/website edits, no commits.
Read-only w.r.t. common.py and other folders.
"""
import json
import time
import os
from pathlib import Path
from hashlib import sha256
import numpy as np
import sympy as sp

from common import (
    load_tensor, channel_support, weights, one_body_generators,
    boson_generator, parity_below, FULL_MASK, N_MODES, N_BOSONS,
)

HERE = Path(__file__).resolve().parent

DELTA = 1
G_LIST = [sp.Rational(1, 20), sp.Rational(1, 40), sp.Rational(1, 100), sp.Rational(1, 400)]
G_NUM = [float(g) for g in G_LIST]

# ---- boson monomial code helpers ----------------------------------------
# sorted tuple (A1,A2,A3), A1<=A2<=A3, unused slots padded by 60.
# code = A1 + 60*A2 + 3600*A3
# size-3 range [0,215999]; size-2 [216000,219599]; size-1 [219600,219659]; size-0 = 219660
PAD = 60
CODE0 = PAD + 60 * PAD + 3600 * PAD  # 219660


def decode_code(code):
    """Return (A1,A2,A3) int arrays. Size-aware: empty slots are PAD=60.
    size-3 range [0,215999]; size-2 [216000,219599]; size-1 [219600,219659]; size-0 = 219660."""
    code = np.asarray(code, dtype=np.int64)
    A1 = np.full(code.shape, PAD, dtype=np.int64)
    A2 = np.full(code.shape, PAD, dtype=np.int64)
    A3 = np.full(code.shape, PAD, dtype=np.int64)
    s3 = code < 216000
    s2 = (code >= 216000) & (code < 219600)
    s1 = (code >= 219600) & (code < 219660)
    # size 3
    c3 = code[s3]
    A3[s3] = c3 // 3600
    r3 = c3 % 3600
    A2[s3] = r3 // 60
    A1[s3] = r3 % 60
    # size 2
    c2 = code[s2] - 216000
    A2[s2] = c2 // 60
    A1[s2] = c2 % 60
    # size 1
    c1 = code[s1] - 219600
    A1[s1] = c1
    return A1, A2, A3


def encode3(A1, A2, A3):
    return A1 + 60 * A2 + 3600 * A3


def insert_boson(code, A_new):
    """Insert channel A_new (int array) into each code's sorted multiset, re-encode."""
    A1, A2, A3 = decode_code(code)
    c1 = A_new <= A1
    c2 = (~c1) & (A_new <= A2)
    new1 = np.where(c1, A_new, A1)
    new2 = np.where(c1, A1, np.where(c2, A_new, A2))
    new3 = np.where(c1, A2, np.where(c2, A2, A_new))
    return encode3(new1, new2, new3)


def remove_boson(code, A_rem):
    """Remove one copy of channel A_rem; return (newcode, multiplicity m_A before removal)."""
    A1, A2, A3 = decode_code(code)
    m = ((A1 == A_rem).astype(np.int64) + (A2 == A_rem).astype(np.int64)
          + (A3 == A_rem).astype(np.int64))
    slots = np.stack([A1, A2, A3], axis=1)
    removed = np.zeros(code.shape, dtype=bool)
    out = np.full((code.shape[0], 2), PAD, dtype=np.int64)
    idx = np.zeros(code.shape, dtype=np.int64)
    for col in range(3):
        vals = slots[:, col]
        take = (~removed) & (vals == A_rem)
        removed = removed | take
        keep = ~take
        write = keep & (idx < 2)
        out[np.where(write)[0], idx[write]] = vals[write]
        idx = idx + keep.astype(np.int64)
    n1, n2 = out[:, 0], out[:, 1]
    lo = np.minimum(n1, n2)
    hi = np.maximum(n1, n2)
    return encode3(lo, hi, np.full(code.shape, PAD, dtype=np.int64)), m


def weight_factor(codes):
    """prod_A m_A! for the unnormalised monomial basis (codes are sorted A1<=A2<=A3)."""
    A1, A2, A3 = decode_code(codes)
    eq12 = (A1 == A2) & (A1 != PAD)
    eq23 = (A2 == A3) & (A2 != PAD)
    all3 = eq12 & eq23
    two = (eq12 | eq23) & ~all3
    return np.where(all3, 6, np.where(two, 2, 1)).astype(np.int64)


# ---- state: three parallel arrays ---------------------------------------
def make_state(masks, codes, amps):
    return (np.asarray(masks, dtype=np.uint64),
            np.asarray(codes, dtype=np.int64),
            np.asarray(amps, dtype=np.int64))


def merge(state):
    masks, codes, amps = state
    if masks.shape[0] == 0:
        return state
    order = np.lexsort((masks.view(np.int64), codes))
    sm = masks[order]; sc = codes[order]; sa = amps[order]
    changed = np.ones(masks.shape[0], dtype=bool)
    changed[1:] = (sc[1:] != sc[:-1]) | (sm[1:] != sm[:-1])
    starts = np.flatnonzero(changed)
    sums = np.add.reduceat(sa, starts)
    keep = sums != 0
    return (sm[starts][keep], sc[starts][keep], sums[keep])


def norm2(state):
    """<v|v> as an exact Python int (int64 arithmetic with an a-priori overflow guard)."""
    masks, codes, amps = state
    if masks.shape[0] == 0:
        return 0
    w = weight_factor(codes)
    amax = int(np.max(np.abs(amps)))
    # a-priori bound: every term <= amax^2 * 6, at most len(masks) terms
    need(amax * amax * 6 * masks.shape[0] < (1 << 62), 'norm2 int64 overflow guard')
    return int(np.sum(amps * amps * w, dtype=np.int64))


# ---- T† and T (vectorised) ----------------------------------------------
def apply_Tdag(state, support):
    """T† = sum_A b_A† Q_A† ; Q_A† = sum_{i<j} W h_i† h_j† (h_j† first then h_i†)."""
    masks, codes, amps = state
    out_m, out_c, out_a = [], [], []
    for A in range(N_BOSONS):
        for (i, j), wval in support[A]:
            bi = np.uint64(1) << np.uint64(i)
            bj = np.uint64(1) << np.uint64(j)
            keep = (masks & bi == 0) & (masks & bj == 0)
            if not np.any(keep):
                continue
            m = masks[keep]; c = codes[keep]; a = amps[keep]
            sj = parity_below(m, j)
            m1 = m | bj
            si = parity_below(m1, i)
            m2 = m1 | bi
            sign = sj * si
            na = a * np.int64(wval) * sign
            nc = insert_boson(c, np.full(c.shape, A, dtype=np.int64))
            out_m.append(m2); out_c.append(nc); out_a.append(na)
        if out_m:
            cm = np.concatenate(out_m); cc = np.concatenate(out_c); ca = np.concatenate(out_a)
            out_m, out_c, out_a = [], [], []
            merged = merge((cm, cc, ca))
            out_m.append(merged[0]); out_c.append(merged[1]); out_a.append(merged[2])
    if not out_m:
        return make_state([], [], [])
    return merge((np.concatenate(out_m), np.concatenate(out_c), np.concatenate(out_a)))


def apply_T(state, support):
    """T = sum_A Q_A b_A ; Q_A = sum_{i<j} W h_j h_i (h_i first then h_j)."""
    masks, codes, amps = state
    A1, A2, A3 = decode_code(codes)
    out_m, out_c, out_a = [], [], []
    slots = [A1, A2, A3]
    for slot in range(3):
        A_rem = slots[slot]
        # b_A acts once per DISTINCT channel with factor m_A: use first occurrences only
        first = A_rem != PAD
        if slot > 0:
            first &= slots[slot - 1] != A_rem
        if not np.any(first):
            continue
        idx = np.flatnonzero(first)
        chan_vals = np.unique(A_rem[idx])
        for A in chan_vals:
            sel = idx[A_rem[idx] == A]
            m = masks[sel]; c = codes[sel]; a = amps[sel]
            nc, mult = remove_boson(c, np.full(c.shape, A, dtype=np.int64))
            for (i, j), wval in support[int(A)]:
                bi = np.uint64(1) << np.uint64(i)
                bj = np.uint64(1) << np.uint64(j)
                keep = ((m & bi) != 0) & ((m & bj) != 0)
                if not np.any(keep):
                    continue
                mm = m[keep]; cc_ = nc[keep]; aa = a[keep] * mult[keep]
                si = parity_below(mm, i)
                m1 = mm ^ bi
                sj = parity_below(m1, j)
                m2 = m1 ^ bj
                na = aa * np.int64(wval) * (si * sj)
                out_m.append(m2); out_c.append(cc_); out_a.append(na)
    if not out_m:
        return make_state([], [], [])
    return merge((np.concatenate(out_m), np.concatenate(out_c), np.concatenate(out_a)))


# ---- inner product (merge-join on sorted (code,mask)) -------------------
KEY_DTYPE = np.dtype([('c', np.int64), ('m', np.uint64)])


def _keys(state):
    masks, codes, _ = state
    k = np.empty(masks.shape[0], dtype=KEY_DTYPE)
    k['c'] = codes
    k['m'] = masks
    return k


def inner(a, b):
    """<a|b> = sum over common (mask,code) of amp_a*amp_b*prod m_A! (real amplitudes).

    Both states are merged first (unique keys); the join uses one structured
    dtype so that sorting and equality use the same total order on (code, mask).
    """
    a = merge(a)
    b = merge(b)
    if a[0].shape[0] == 0 or b[0].shape[0] == 0:
        return 0
    common, ia, ib = np.intersect1d(_keys(a), _keys(b), assume_unique=True, return_indices=True)
    if common.size == 0:
        return 0
    wa = weight_factor(a[1][ia]).astype(object)
    return int(np.sum(a[2][ia].astype(object) * b[2][ib].astype(object) * wa))


GUARDS = []


def need(ok, name, kind='exact'):
    if not ok:
        raise RuntimeError(f'GUARD FAILED ({kind}): {name}')
    GUARDS.append((name, kind))


def hole_picture_guard(support, W):
    """For >=10 channels A, apply P_A to |F> in fermion mask picture and compare
    with -Q_A†|0_h> after complementing masks, including signs.

    Fermion picture: |F> = full mask (2^64-1), amp +1. P_A = sum W f_j f_i.
    f_i on mask m: sign = (-1)^{popcount(m & (2^i-1))}; new mask m ^ bit_i.
    Apply f_i first then f_j (P_A = sum W f_j f_i).
    Result state (fermion mask) should equal - (Q_A†|0_h>) with masks complemented.
    Q_A†|0_h>: hole vacuum mask 0; Q_A† = sum W h_i† h_j† (h_j† first then h_i†).
    """
    from common import ann as f_ann
    full = np.array([FULL_MASK], dtype=np.uint64)
    results = {}
    for A in range(min(10, N_BOSONS)):
        # fermion picture: P_A |F> = sum W f_j f_i |F>
        fm = []; fa = []
        for (i, j), wval in support[A]:
            bi = np.uint64(1) << np.uint64(i)
            bj = np.uint64(1) << np.uint64(j)
            m = full.copy()
            # f_i first
            r = f_ann(int(m[0]), i)
            if r is None:
                continue
            m1, si = r
            r = f_ann(m1, j)
            if r is None:
                continue
            m2, sj = r
            fm.append(np.uint64(m2)); fa.append(np.int64(wval) * si * sj)
        # hole picture: -Q_A† |0_h> ; Q_A† = sum W h_i† h_j† (h_j† first then h_i†)
        hm = []; ha = []
        hmask = np.array([0], dtype=np.uint64)
        for (i, j), wval in support[A]:
            bi = np.uint64(1) << np.uint64(i)
            bj = np.uint64(1) << np.uint64(j)
            m = hmask.copy()
            sj = parity_below(m, j)
            m1 = m | bj
            si = parity_below(m1, i)
            m2 = m1 | bi
            sign = sj * si
            hm.append(m2); ha.append(-np.int64(wval) * sign)
        # The particle-hole map is the unitary U with U f_i U^-1 = h_i^dagger and
        # U|F> = |0_h>. The hole occupation state |mu>_h = h_{i1}^+ ... h_{ik}^+ |0_h>
        # (i1<...<ik, CAR convention) equals f_{i1} ... f_{ik} |F> in the fermion
        # picture, which is s(mu) * |complement(mu)>_f with a sign s(mu) obtained by
        # applying f_{ik} first, ..., f_{i1} last to the filled mask. Hence the
        # fermion amplitude of |m>_f translates into hole amplitude amp * s(mu).
        def ph_sign(hole_mask):
            m = FULL_MASK
            sign = 1
            for i in sorted((k for k in range(N_MODES) if hole_mask & (1 << k)), reverse=True):
                m, s = f_ann(m, i)
                sign *= s
            return sign
        fm = np.array(fm, dtype=np.uint64).reshape(-1)
        fa = np.array(fa, dtype=np.int64).reshape(-1)
        hm = np.array(hm, dtype=np.uint64).reshape(-1)   # entries were length-1 arrays
        ha = np.array(ha, dtype=np.int64).reshape(-1)
        comp = np.uint64(FULL_MASK) ^ fm  # complement fermion masks -> hole masks
        signs = np.array([ph_sign(int(mu)) for mu in comp], dtype=np.int64)
        fa_h = fa * signs
        order_f = np.lexsort((comp.view(np.int64),))
        order_h = np.lexsort((hm.view(np.int64),))
        ok = np.array_equal(comp[order_f], hm[order_h]) and np.array_equal(fa_h[order_f], ha[order_h])
        need(ok, f'hole picture P_A|F> = -Q_A†|0_h> under the particle-hole unitary, channel {A}')
        # negative control: without the particle-hole sign the naive complement map fails
        naive = np.array_equal(fa[order_f], ha[order_h])
        results[A] = {'identity_holds': bool(ok), 'naive_complement_without_sign_holds': bool(naive)}
    need(not all(r['naive_complement_without_sign_holds'] for r in results.values()),
         'negative control: the naive complement map without s(mu) is not an identity')
    return results


def singlet_guard(v1, v2, support, W):
    """Lift one-body generators to hole picture and check they annihilate v1,v2.
    Hole action of generator X (64x64): -sum_ij (X^T)_ij h_i† h_j  (conjugate rep).
    Boson action: boson_generator(W, X) on the monomial basis.
    """
    spin, colour = one_body_generators()
    gens = []
    # Every gamma_j gamma_k generator is either purely real or purely imaginary;
    # the overall factor i is irrelevant for annihilation, so a real integer
    # matrix is used for each (guarded).
    for X in spin[:3] + colour[:3]:
        re_part, im_part = np.real(X), np.imag(X)
        need(not (np.any(re_part) and np.any(im_part)), 'generator is purely real or purely imaginary')
        Xr = re_part if np.any(re_part) else im_part
        need(np.array_equal(Xr, np.rint(Xr)), 'generator entries are integers')
        gens.append(Xr.astype(np.int64))
    results = {}
    for gi, X in enumerate(gens):
        for vn, v in [('v1', v1), ('v2', v2)]:
            res = apply_one_body_hole(v, X, support)  # fermion/hole part
            resb = apply_one_body_boson(v, X, W)      # boson part
            # total = hole_part + boson_part ; check annihilates
            tot = add_states(res, resb)
            ok = tot[0].shape[0] == 0
            need(ok, f'singlet gen {gi} annihilates {vn}')
            results[f'gen{gi}_{vn}'] = bool(ok)
    return results


def apply_one_body_hole(state, X, support):
    """Hole action: -sum_ij (X^T)_ij h_i† h_j. For each pair (i,j) with (X^T)_ij !=0,
    apply h_j (annihilate hole at j) then h_i† (create hole at i), factor -(X^T)_ij.
    """
    masks, codes, amps = state
    XT = X.T
    rows, cols = np.nonzero(XT)
    out_m, out_c, out_a = [], [], []
    for r in range(len(rows)):
        i = int(rows[r]); j = int(cols[r])
        val = XT[i, j]
        bi = np.uint64(1) << np.uint64(i)
        bj = np.uint64(1) << np.uint64(j)
        keep = (masks & bj) != 0
        if not np.any(keep):
            continue
        m = masks[keep]; c = codes[keep]; a = amps[keep]
        # h_j (annihilate hole at j): sign = parity_below(m, j); m1 = m ^ bj
        sj = parity_below(m, j)
        m1 = m ^ bj
        # h_i† (create hole at i): need bit i clear; sign = parity_below(m1, i); m2 = m1 | bi
        ok2 = (m1 & bi) == 0
        if not np.all(ok2):
            m = m[ok2]; m1 = m1[ok2]; sj = sj[ok2]; c = c[ok2]; a = a[ok2]
        si = parity_below(m1, i)
        m2 = m1 | bi
        sign = sj * si
        na = a * np.int64(val) * (-sign)
        out_m.append(m2); out_c.append(c); out_a.append(na)
    if not out_m:
        return make_state([], [], [])
    return merge((np.concatenate(out_m), np.concatenate(out_c), np.concatenate(out_a)))


def apply_one_body_boson(state, X, W):
    """Boson action: sum_{A'B'} (X_B)_{A'B'} b_A'† b_B on monomial basis."""
    # X is the real integer representative of a purely real/imaginary generator;
    # boson_generator is linear, so its induced matrix is real integer as well.
    XB = boson_generator(W, X.astype(complex))
    need(not np.any(np.imag(XB)) and np.array_equal(np.real(XB), np.rint(np.real(XB))),
         'induced boson generator is real integer for a real generator')
    XB = np.rint(np.real(XB)).astype(np.int64)
    masks, codes, amps = state
    out_m, out_c, out_a = [], [], []
    rows, cols = np.nonzero(XB)
    for r in range(len(rows)):
        Ap = int(rows[r]); B = int(cols[r])
        val = int(XB[Ap, B])
        # apply b_B then b_A'†
        nc, mult = remove_boson(codes, np.full(codes.shape, B, dtype=np.int64))
        keep = mult > 0
        if not np.any(keep):
            continue
        nc = nc[keep]; mult = mult[keep]; m = masks[keep]; a = amps[keep]
        nc2 = insert_boson(nc, np.full(nc.shape, Ap, dtype=np.int64))
        na = a * mult * np.int64(val)
        out_m.append(m); out_c.append(nc2); out_a.append(na)
    if not out_m:
        return make_state([], [], [])
    return merge((np.concatenate(out_m), np.concatenate(out_c), np.concatenate(out_a)))


def add_states(a, b):
    if a[0].shape[0] == 0:
        return b
    if b[0].shape[0] == 0:
        return a
    return merge((np.concatenate([a[0], b[0]]), np.concatenate([a[1], b[1]]),
                   np.concatenate([a[2], b[2]])))


def qqdag_v1_guard(v1, support):
    """<v1| sum_A Q_A Q_A† |v1> should equal 458*480."""
    # Q_A† v1_entry: v1 has 1 boson A0 and 2 holes. Q_A† creates 2 more holes (if room) + 0 bosons.
    # sum_A Q_A Q_A† |v1> : apply Q_A† to v1 (no boson change), then Q_A.
    # Easier: <v1| sum_A Q_A Q_A† |v1> = sum_A ||Q_A† v1||^2  (since Q_A† adds 2 holes, Q_A removes them)
    # Actually Q_A Q_A† is number-conserving on bosons (Q_A† no boson, Q_A no boson).
    # Compute state s = sum_A Q_A† v1 (2-boson? no: Q_A† only acts on holes, no boson).
    # v1 entries have 1 boson. Q_A† keeps boson, adds 2 holes -> 4 holes, 1 boson (N=64? 4 holes -> N_f=60, +2N_b=2 -> N=62). Wait N = N_f + 2N_b. Holes=4 -> N_f=60, N_b=1 -> N=62. So Q_A† v1 is in N=62 sector (not our N=64). That's fine for the norm.
    # <v1| sum_A Q_A Q_A† |v1> = sum_A ||Q_A† v1||^2 : one norm per channel, then summed
    # (NOT the norm of the summed state).
    masks, codes, amps = v1
    val = 0
    for A in range(N_BOSONS):
        out_m, out_c, out_a = [], [], []
        for (i, j), wval in support[A]:
            bi = np.uint64(1) << np.uint64(i)
            bj = np.uint64(1) << np.uint64(j)
            keep = (masks & bi == 0) & (masks & bj == 0)
            if not np.any(keep):
                continue
            m = masks[keep]; c = codes[keep]; a = amps[keep]
            sj = parity_below(m, j); m1 = m | bj
            si = parity_below(m1, i); m2 = m1 | bi
            na = a * np.int64(wval) * (sj * si)
            out_m.append(m2); out_c.append(c); out_a.append(na)
        if out_m:
            s = merge((np.concatenate(out_m), np.concatenate(out_c), np.concatenate(out_a)))
            val += norm2(s)
    need(val == 458 * 480, f'<v1|sum Q_A Q_A†|v1> = {val}, expected {458*480}', 'exact')
    return val


# ---- main computation ---------------------------------------------------
def main():
    t0 = time.time()
    W = load_tensor()
    support, lookup = channel_support(W)

    # ---- hole picture guard ----
    hpg = hole_picture_guard(support, W)

    # ---- Krylov chain v0..v3 ----
    v0 = make_state(np.array([0], dtype=np.uint64), np.array([CODE0], dtype=np.int64),
                    np.array([1], dtype=np.int64))
    chain_times = {}
    t = time.time()
    v1 = apply_Tdag(v0, support)
    chain_times['v1'] = time.time() - t
    n1 = v1[0].shape[0]
    nu1 = norm2(v1)
    need(n1 == 480, f'|v1| = {n1}, expected 480')
    need(nu1 == 480, f'nu1 = {nu1}, expected 480')

    t = time.time()
    v2 = apply_Tdag(v1, support)
    chain_times['v2'] = time.time() - t
    n2 = v2[0].shape[0]
    nu2 = norm2(v2)
    need(nu2 == 439680, f'nu2 = {nu2}, expected 439680')

    t = time.time()
    v3 = apply_Tdag(v2, support)
    chain_times['v3'] = time.time() - t
    n3 = v3[0].shape[0]
    nu3 = norm2(v3)

    # ---- singlet guards ----
    sg = singlet_guard(v1, v2, support, W)
    qq = qqdag_v1_guard(v1, support)

    # ---- closure tests ----
    closure = {}
    # (i) T v1 = 480 v0
    Tv1 = apply_T(v1, support)
    # compare with 480 v0
    ok = inner(Tv1, v0) == 480 and inner(Tv1, Tv1) == 480 * 480 and inner(Tv1, v0) * inner(Tv1, v0) == inner(Tv1, Tv1) * 1
    # simpler: T v1 = 480 v0 means Tv1 has single entry (0,CODE0,480)
    ok = (Tv1[0].shape[0] == 1 and int(Tv1[0][0]) == 0 and int(Tv1[1][0]) == CODE0
          and int(Tv1[2][0]) == 480)
    need(ok, 'closure (i) T v1 = 480 v0')
    closure['T_v1_eq_480_v0'] = bool(ok)

    # (ii) T v2 = c2 v1, c2 = nu2/nu1
    c2 = nu2 // nu1
    need(nu2 % nu1 == 0, 'nu2/nu1 integer')
    Tv2 = apply_T(v2, support)
    # T v2 should be c2 * v1
    ok = (Tv2[0].shape[0] == v1[0].shape[0]
          and np.array_equal(Tv2[0], v1[0]) and np.array_equal(Tv2[1], v1[1])
          and np.array_equal(Tv2[2], v1[2] * c2))
    need(ok, f'closure (ii) T v2 = {c2} v1')
    closure['T_v2_eq_c2_v1'] = bool(ok)
    closure['c2'] = int(c2)

    # (iii) u = T v3 ; <v2|u> = nu3 ; w2 = u - (<v2|u>/nu2) v2
    u = apply_T(v3, support)
    vu = inner(v2, u)
    need(vu == nu3, f'adjoint guard <v2|T v3> = {vu}, expected nu3 = {nu3}')
    closure['v2_u_inner'] = int(vu)
    closure['adjoint_guard_holds'] = bool(vu == nu3)
    u_norm2 = inner(u, u)
    # w2 = u - (vu/nu2) v2 ; vu == nu3 ; <w2|v2> = 0.
    # subtract_scaled returns q*w2 with integer amplitudes (alpha = p/q in lowest terms),
    # so the true norm is ||q w2||^2 / q^2 = ||u||^2 - nu3^2/nu2 (exact rational identity).
    alpha = sp.Rational(vu, nu2)
    w2 = subtract_scaled(u, v2, alpha)
    w2_scale = int(alpha.q)
    w2_scaled_norm2 = inner(w2, w2)
    w2_norm2 = sp.Rational(w2_scaled_norm2, w2_scale ** 2)
    need(w2_norm2 == sp.Rational(u_norm2) - sp.Rational(vu * vu, nu2),
         'exact ||w2||^2 = ||T v3||^2 - nu3^2/nu2 (Pythagoras on the v2 component)')
    closure['u_norm2'] = int(u_norm2)
    closure['w2_scale_q'] = w2_scale
    closure['w2_norm2_exact'] = str(w2_norm2)
    closure['w2_norm2_float'] = float(w2_norm2)
    closure['closure_defect'] = float(w2_norm2 / u_norm2) if u_norm2 else 0.0
    closure['w2_coupling2_over_nu3'] = float(w2_norm2 / nu3)
    closure['chain_closes_exactly_at_k2'] = bool(w2_norm2 == 0)
    # <w2|v2> guard
    wv2 = inner(w2, v2)
    need(wv2 == 0, f'<w2|v2> = {wv2}, expected 0')
    closure['w2_v2_orthogonal'] = bool(wv2 == 0)
    # <w2|H|v1> = g <w2|T† v1> = g <w2|v2> = 0 by the line above; <w2|H|v3> = g <w2|T v3> = g ||w2||^2
    need(sp.Rational(inner(w2, u), w2_scale) == w2_norm2,
         '<w2|T v3> = ||w2||^2 (w2 couples to v3 with matrix element g ||w2||^2)')

    # ---- Ritz / variational ----
    # Jacobi: diag n*Delta, off g*sqrt(nu_{n+1}/nu_n)
    norms = [1, nu1, nu2, nu3]
    # check norms_by_traces.json
    nbt_path = HERE / 'norms_by_traces.json'
    use_extended = False
    if nbt_path.exists():
        nbt = json.loads(nbt_path.read_text())
        nu_map = nbt.get('nu', {})
        for k in ['1', '2', '3']:
            if k in nu_map:
                need(int(nu_map[k]) == norms[int(k)], f'norms_by_traces nu[{k}] = {nu_map[k]} vs {norms[int(k)]}')
        # extend chain
        extra = sorted(int(k) for k in nu_map if int(k) > 3)
        for k in extra:
            norms.append(int(nu_map[str(k)]))
        use_extended = len(extra) > 0
    Kmax = len(norms) - 1  # max n index
    ritz = compute_ritz(norms, w2_norm2, use_extended)

    # ---- observables on Omega_K ----
    observables = compute_observables(norms, w2_norm2, ritz, v0, v1, v2, v3, w2, support, use_extended)

    # ---- charged response ----
    charged = compute_charged_response(norms, w2_norm2, ritz, v0, v1, v2, v3, w2, support, observables)

    # ---- sector selection bounds ----
    sector = compute_sector_bounds(ritz, norms, w2_norm2)

    wall = time.time() - t0
    result = {
        'status': 'PASS',
        'guards': {
            'hole_picture': hpg,
            'singlet': sg,
            'qqdag_v1': int(qq),
            'closure': closure,
        },
        'krylov': {
            'entry_counts': {'v0': 1, 'v1': int(n1), 'v2': int(n2), 'v3': int(n3)},
            'norms': {'nu0': 1, 'nu1': int(nu1), 'nu2': int(nu2), 'nu3': int(nu3)},
            'norms_by_traces_used': use_extended,
        },
        'ritz': ritz,
        'observables': observables,
        'charged_response': charged,
        'sector_bounds': sector,
        'common_sha256': sha256((HERE / 'common.py').read_bytes()).hexdigest(),
        'checker_sha256': sha256((HERE / 'native_ground_state.py').read_bytes()).hexdigest(),
    }
    result['guards_count'] = len(GUARDS)
    result['guards_exact'] = sum(1 for _, kind in GUARDS if kind == 'exact')
    result['guards_numerical'] = sum(1 for _, kind in GUARDS if kind != 'exact')
    out_path = HERE / 'native_ground_state.json'
    out_path.write_text(json.dumps(result, indent=1, sort_keys=True))
    print(json.dumps(result, indent=1, sort_keys=True))
    import sys
    print(json.dumps({'wall_time_s': float(wall), 'chain_times_s': {k: float(v) for k, v in chain_times.items()}}), file=sys.stderr)
    return result


def subtract_scaled(u, v, alpha):
    """Return u - alpha*v with alpha a rational p/q. amplitudes scaled to ints."""
    p, q = alpha.p, alpha.q
    # u amps * q - v amps * p, over common (mask,code)
    mu, cu, au = u
    mv, cv, av = v
    # combine
    all_m = np.concatenate([mu, mv])
    all_c = np.concatenate([cu, cv])
    all_a = np.concatenate([au * q, -(av * p)])
    return merge((all_m, all_c, all_a))


W2_INDEX = 3  # w2 is the component of T v3 orthogonal to v2; it couples to v3 only


def jacobi_matrix(norms, include_w2, w2n):
    """Exact sympy matrix of H (Delta=1, g factored out of off-diagonals) in the
    orthonormalised basis {v_0..v_K} (+ w2). Chain: diag n, off-diag sqrt(nu_{n+1}/nu_n).
    w2 (a two-boson state, energy 2) couples only to v_3 with g*sqrt(||w2||^2/nu_3):
    <w2|H|v_1> = g<w2|v_2> = 0 and <w2|H|v_n> = 0 for n != 3 by boson number.
    It is included only when K >= 3."""
    K = len(norms) - 1
    with_w2 = bool(include_w2) and w2n > 0 and K >= W2_INDEX
    n = K + 1 + (1 if with_w2 else 0)
    M = sp.zeros(n, n)
    for i in range(K + 1):
        M[i, i] = i  # n*Delta, Delta=1
    for i in range(K):
        r = sp.Rational(norms[i + 1], norms[i])
        M[i, i + 1] = sp.sqrt(r)
        M[i + 1, i] = M[i, i + 1]
    if with_w2:
        idx = K + 1
        M[idx, idx] = 2  # 2*Delta
        M[W2_INDEX, idx] = sp.sqrt(sp.Rational(w2n) / norms[W2_INDEX])
        M[idx, W2_INDEX] = M[W2_INDEX, idx]
    return M


def build_H(M, g):
    """H = Delta*diag(M) + g*offdiag(M), Delta=1."""
    n = M.shape[0]
    H = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            if i == j:
                H[i, j] = M[i, j]
            else:
                H[i, j] = g * M[i, j]
    return H


def lowest_eig(M, g):
    """Return (E0_exact_or_charpoly_str, E0_num, evec_num, E0_num_check).

    Closed-form radicals only for size <= 2 (the 2-level formula); for larger
    Ritz matrices the exact characteristic polynomial is recorded and the
    lowest root is computed numerically (labelled 'numerical' downstream).
    """
    H = build_H(M, g)
    Hn = np.array(H.evalf(), dtype=float)
    w_eig, V_eig = np.linalg.eigh(Hn)
    idx = int(np.argmin(w_eig))
    if H.shape[0] <= 2:
        spec = sorted((sp.nsimplify(ev) for ev in H.eigenvals()), key=lambda x: float(x))
        exact = str(spec[0])
        E0 = float(spec[0].evalf())
    else:
        z = sp.symbols('z')
        exact = 'charpoly: ' + str(sp.expand(H.charpoly(z).as_expr()))
        E0 = float(w_eig[idx])
    return exact, E0, V_eig[:, idx].copy(), float(w_eig[idx])


def compute_ritz(norms, w2n, use_extended):
    """Ritz table for K=1,2,3,(more) with/without w2 at each g."""
    Kmax = len(norms) - 1
    K_values = list(range(1, Kmax + 1))
    table = {}
    for include_w2 in [False, True]:
        label = 'with_w2' if include_w2 else 'no_w2'
        if include_w2 and w2n == 0:
            table[label] = {'skipped': True, 'reason': 'w2_norm2 is zero (chain closed)'}
            continue
        perK = {}
        for K in K_values:
            M = jacobi_matrix(norms[:K + 1], include_w2, w2n)   # w2 enters only for K >= 3
            per_g = {}
            for g in G_LIST:
                e_str, e_num, evec, e_chk = lowest_eig(M, g)
                per_g[str(g)] = {'E_exact': e_str, 'E_numerical': e_num, 'size': int(M.shape[0])}
            perK[str(K)] = per_g
        table[label] = {'per_K': perK}
    table['w2_norm2'] = str(w2n)
    table['Kmax'] = int(Kmax)
    return table


def compute_observables(norms, w2n, ritz, v0, v1, v2, v3, w2, support, use_extended):
    """For g=1/20, K=Kmax, with/without w2: <N_b>, overlap, entropy, perturbative ref."""
    Kmax = len(norms) - 1
    out = {}
    g = sp.Rational(1, 20)
    gn = float(g)
    for include_w2 in [False, True]:
        label = 'with_w2' if include_w2 else 'no_w2'
        if include_w2 and w2n == 0:
            out[label] = {'skipped': True}
            continue
        M = jacobi_matrix(norms, include_w2, w2n)
        include_w2 = M.shape[0] == Kmax + 2   # w2 actually present
        e_str, e_num, evec, e_chk = lowest_eig(M, g)
        E0 = e_num
        nb_vec = np.array([i for i in range(Kmax + 1)] + ([2] if include_w2 else []),
                          dtype=float)
        Nb = float(np.sum(evec**2 * nb_vec))
        overlap = float(evec[0]**2)
        p = {}
        for i in range(Kmax + 1):
            p[i] = p.get(i, 0.0) + float(evec[i]**2)
        if include_w2:
            p[2] = p.get(2, 0.0) + float(evec[-1]**2)
        p = {int(k): float(v) for k, v in sorted(p.items()) if v > 0}
        ent = 0.0
        for k, v in p.items():
            if v > 0:
                ent -= v * np.log2(v)
        # Hellmann-Feynman: dE/dDelta = <N_b>
        dD = 1e-6
        n = M.shape[0]
        Hp = np.zeros((n, n)); Hm = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if i == j:
                    Hp[i, j] = float(M[i, j]) * (1 + dD)
                    Hm[i, j] = float(M[i, j]) * (1 - dD)
                else:
                    Hp[i, j] = gn * float(M[i, j])
                    Hm[i, j] = gn * float(M[i, j])
        hf = (np.linalg.eigvalsh(Hp)[0] - np.linalg.eigvalsh(Hm)[0]) / (2 * dD)
        out[label] = {
            'E_numerical': E0,
            'Nb': Nb,
            'overlap_F2': overlap,
            'p_k': p,
            'entropy_bits': float(ent),
            'HF_dEdDelta': float(hf),
            'HF_Nb_match': bool(abs(hf - Nb) < 1e-3),
            'perturbative_ref': float(-480 * gn * gn),
        }
    return out


def merge_float(state):
    masks, codes, amps = state
    if masks.shape[0] == 0:
        return state
    order = np.lexsort((masks.view(np.int64), codes))
    sm = masks[order]; sc = codes[order]; sa = amps[order]
    changed = np.ones(masks.shape[0], dtype=bool)
    changed[1:] = (sc[1:] != sc[:-1]) | (sm[1:] != sm[:-1])
    starts = np.flatnonzero(changed)
    sums = np.add.reduceat(sa, starts)
    keep = np.abs(sums) > 1e-15
    return (sm[starts][keep], sc[starts][keep], sums[keep])


def state_norm2_float(state):
    masks, codes, amps = state
    w = weight_factor(codes).astype(float)
    return float(np.sum(amps * amps * w))


def build_omega_state(states, evec, norms):
    """Omega = sum_n (evec[n]/sqrt(nu_n)) v_n as a float-amplitude state."""
    parts = []
    for n, st in enumerate(states):
        c = float(evec[n]) / np.sqrt(float(norms[n]))
        masks, codes, amps = st
        parts.append((masks, codes, amps.astype(float) * c))
    all_m = np.concatenate([p[0] for p in parts])
    all_c = np.concatenate([p[1] for p in parts])
    all_a = np.concatenate([p[2] for p in parts])
    return merge_float((all_m, all_c, all_a))


def apply_holedag(state, r, support):
    """h_r† : create a hole at r (requires bit r clear)."""
    masks, codes, amps = state
    br = np.uint64(1) << np.uint64(r)
    keep = (masks & br) == 0
    if not np.any(keep):
        return merge_float((np.array([], dtype=np.uint64), np.array([], dtype=np.int64),
                            np.array([], dtype=float)))
    m = masks[keep]; c = codes[keep]; a = amps[keep]
    s = parity_below(m, r).astype(float)
    m2 = m | br
    return merge_float((m2, c, a * s))


def apply_hole(state, r, support):
    """h_r : annihilate a hole at r (requires bit r set)."""
    masks, codes, amps = state
    br = np.uint64(1) << np.uint64(r)
    keep = (masks & br) != 0
    if not np.any(keep):
        return merge_float((np.array([], dtype=np.uint64), np.array([], dtype=np.int64),
                            np.array([], dtype=float)))
    m = masks[keep]; c = codes[keep]; a = amps[keep]
    s = parity_below(m, r).astype(float)
    m2 = m ^ br
    return merge_float((m2, c, a * s))


def first_moment_float(psi, support, gn):
    """<psi|H_hole|psi> = Delta*<N_b> + 2g Re<T psi|psi>. Delta=1.
    T lowers boson number. <psi|T|psi> = <T† psi|psi>... use T psi directly.
    <psi|H|psi> = <psi|N_b|psi> + 2g * <T psi | psi>  (since H = N_b + g(T†+T),
    <psi|H|psi> = <N_b> + g(<T†psi|psi> + <psi|Tpsi|>) = <N_b> + 2g Re<psi|T|psi>
    = <N_b> + 2g Re<T psi|psi> (real). We compute <T psi|psi> via inner_float(T psi, psi)."""
    nb = state_norm2_float_nb(psi)
    Tpsi = apply_T_float(psi, support)
    tps = inner_float(Tpsi, psi)
    return nb + 2 * gn * tps


def state_norm2_float_nb(state):
    """<N_b> expectation = sum |amp|^2 * (N_b of entry) * prod m_A!."""
    masks, codes, amps = state
    A1, A2, A3 = decode_code(codes)
    nb = ((A1 != PAD).astype(float) + (A2 != PAD).astype(float) + (A3 != PAD).astype(float))
    w = weight_factor(codes).astype(float)
    return float(np.sum(amps * amps * nb * w))


def inner_float(a, b):
    """Float inner product with the same structured (code, mask) join as inner()."""
    a = merge_float(a)
    b = merge_float(b)
    if a[0].shape[0] == 0 or b[0].shape[0] == 0:
        return 0.0
    common, ia, ib = np.intersect1d(_keys(a), _keys(b), assume_unique=True, return_indices=True)
    if common.size == 0:
        return 0.0
    wa = weight_factor(a[1][ia]).astype(float)
    return float(np.sum(a[2][ia] * b[2][ib] * wa))


def apply_T_float(state, support):
    """T = sum_A Q_A b_A on float amplitudes (lowers boson number)."""
    masks, codes, amps = state
    A1, A2, A3 = decode_code(codes)
    out_m, out_c, out_a = [], [], []
    slots = [A1, A2, A3]
    for slot in range(3):
        A_rem = slots[slot]
        first = A_rem != PAD
        if slot > 0:
            first &= slots[slot - 1] != A_rem   # one action per distinct channel
        if not np.any(first):
            continue
        idx = np.flatnonzero(first)
        chan_vals = np.unique(A_rem[idx])
        for A in chan_vals:
            sel = idx[A_rem[idx] == A]
            m = masks[sel]; c = codes[sel]; a = amps[sel]
            nc, mult = remove_boson(c, np.full(c.shape, A, dtype=np.int64))
            for (i, j), wval in support[int(A)]:
                bi = np.uint64(1) << np.uint64(i)
                bj = np.uint64(1) << np.uint64(j)
                keep = ((m & bi) != 0) & ((m & bj) != 0)
                if not np.any(keep):
                    continue
                mm = m[keep]; cc_ = nc[keep]
                aa = a[keep] * mult[keep].astype(float)
                si = parity_below(mm, i).astype(float)
                m1 = mm ^ bi
                sj = parity_below(m1, j).astype(float)
                m2 = m1 ^ bj
                na = aa * float(wval) * (si * sj)
                out_m.append(m2); out_c.append(cc_); out_a.append(na)
    if not out_m:
        return merge_float((np.array([], dtype=np.uint64), np.array([], dtype=np.int64),
                            np.array([], dtype=float)))
    return merge_float((np.concatenate(out_m), np.concatenate(out_c), np.concatenate(out_a)))


def compute_charged_response(norms, w2n, ritz, v0, v1, v2, v3, w2, support, observables):
    """Charged response on the explicit Ritz state Omega (g=1/20) built from the stored
    vectors v_0..v_3 and w2 (the K=3 chain plus the k=2 correction). Higher chain
    members from the trace norms have no stored vectors and are not used here."""
    Kc = min(3, len(norms) - 1)
    g = sp.Rational(1, 20)
    gn = float(g)
    M = jacobi_matrix(norms[:Kc + 1], True, w2n)
    with_w2 = M.shape[0] == Kc + 2
    e_str, E0, evec, e_chk = lowest_eig(M, g)
    nb_vec = np.array(list(range(Kc + 1)) + ([2] if with_w2 else []), dtype=float)
    Nb = float(np.sum(evec**2 * nb_vec))
    states = [v0, v1, v2, v3][:Kc + 1]
    state_norms = list(norms[:Kc + 1])
    if with_w2:
        states = states + [w2]
        state_norms = state_norms + [float(state_norm2_float(w2))]  # stored w2 is q*w2: use its own norm
    Omega = build_omega_state(states, evec, state_norms)
    need(abs(state_norm2_float(Omega) - 1.0) < 1e-9, 'Ritz state is normalised', 'numerical')
    out = {'E_K': E0, 'Nb': Nb, 'basis': 'v0..v%d%s' % (Kc, ' + w2' if with_w2 else ''),
           'ritz_size': int(M.shape[0])}
    Z = {}
    for r in [0, 5, 63]:
        psi_rem = apply_holedag(Omega, r, support)
        psi_add = apply_hole(Omega, r, support)
        Zh = state_norm2_float(psi_rem)
        Zadd = state_norm2_float(psi_add)
        Z[r] = {'Z_h': Zh, 'Z_add': Zadd, 'sum': Zh + Zadd}
    for r in [0, 5, 63]:
        need(abs(Z[r]['Z_h'] + Z[r]['Z_add'] - 1.0) < 1e-6, f'Z_h+Z_add=1 for r={r}', 'numerical')
        need(abs(Z[r]['Z_h'] - (1 - Nb / 32)) < 1e-3, f'Z_h=1-Nb/32 for r={r}', 'numerical')
        need(abs(Z[r]['Z_add'] - Nb / 32) < 1e-3, f'Z_add=Nb/32 for r={r}', 'numerical')
    out['Z'] = Z
    eps = {}
    for r in [0, 5, 63]:
        psi_rem = apply_holedag(Omega, r, support)
        psi_add = apply_hole(Omega, r, support)
        Zh = state_norm2_float(psi_rem)
        Zadd = state_norm2_float(psi_add)
        if Zh > 1e-14:
            eps_h = first_moment_float(psi_rem, support, gn) / Zh - E0
        else:
            eps_h = None
        if Zadd > 1e-14:
            eps_add = first_moment_float(psi_add, support, gn) / Zadd - E0
        else:
            eps_add = None
        eps[r] = {'eps_h': float(eps_h) if eps_h is not None else None,
                   'eps_add': float(eps_add) if eps_add is not None else None}
    out['eps'] = eps
    out['Z_chi'] = float(23 * Nb / 480)
    out['N4_ref_Zh'] = float((1 + 5 / np.sqrt(29)) / 64)
    return out


def compute_sector_bounds(ritz, norms, w2n):
    """Sector selection bounds (Delta = 1).

    Lower bound for every state (Casimir identity sum_A P_A^dag P_A <= (15/2) N_f
    plus completing the square with a fraction theta of Delta N_b):
        H >= (1-theta) N_b - (15 g^2 / (2 theta)) N_f ,  theta in (0,1].
    In sector N: N_f = N - 2 N_b, 0 <= N_f <= 64. L(N; g) = max_theta min_{N_b} bound.
    Upper bound for N = 64: the Ritz energy E_K(g) of the Jacobi chain (no w2).
    """
    def E64(gn):
        # best available rigorous upper bound: full chain plus the w2 correction
        Mfull = jacobi_matrix(norms, True, w2n)
        Hn = np.array(Mfull.evalf(), dtype=float)
        Hn = np.diag(np.diag(Hn)) + gn * (Hn - np.diag(np.diag(Hn)))
        return float(np.linalg.eigvalsh(Hn)[0])

    THETA = np.concatenate([np.linspace(0.002, 1.0, 2000), [1.0]])

    def L_of_N(N, gn):
        # valid bound: max over theta of the min over admissible N_b (max-min, not min-max)
        nb_min = max(0, -((64 - N) // 2))  # ceil((N-64)/2)
        nb_max = N // 2
        Nb = np.arange(nb_min, nb_max + 1, dtype=float)
        Nf = N - 2 * Nb
        ok = (Nf >= 0) & (Nf <= 64)
        Nb, Nf = Nb[ok], Nf[ok]
        if Nb.size == 0:
            return np.inf
        bound = (1.0 - THETA)[:, None] * Nb[None, :] - (15.0 * gn * gn / (2.0 * THETA))[:, None] * Nf[None, :]
        return float(np.max(np.min(bound, axis=1)))

    def competitors(gn):
        # N != 64 up to N = 64 + 2*64 (beyond that every N_b >= 64 and the bound only grows)
        return {N: L_of_N(N, gn) for N in range(0, 64 + 2 * 64 + 1) if N != 64}

    def proven(gn):
        e = E64(gn)
        comp = competitors(gn)
        return all(e < L for L in comp.values()), e, comp

    sector = {}
    for g in G_LIST:
        gn = float(g)
        ok, e, comp = proven(gn)
        worst_N = min(comp, key=comp.get)
        sector[str(g)] = {
            'E_K_64': e,
            'N64_proven_global_ground': bool(ok),
            'tightest_competitor': {'N': int(worst_N), 'L': float(comp[worst_N])},
            'L_N62': float(comp[62]), 'L_N66': float(comp[66]), 'L_N0': float(comp[0]),
            'crude_N62_minus_465_g2': float(-465.0 * gn * gn),
        }
    # largest g/Delta (bisection to 1e-4) for which the proof holds
    lo, hi = 0.0, float(G_LIST[0])
    if proven(hi)[0]:
        g_star = hi
    else:
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if proven(mid)[0]:
                lo = mid
            else:
                hi = mid
            if hi - lo < 1e-5:
                break
        g_star = lo
    sector['g_star_proof_range'] = float(g_star)
    sector['g_star_note'] = ('largest g/Delta <= 1/20 for which E_K(64) < L(N) for all N != 64 '
                             'with the Casimir/theta lower bounds; the worker claim (1/20) is '
                             'reproduced only if this equals 0.05')
    e20 = E64(float(G_LIST[0]))
    sector['mu_star_at_1_20'] = float(-e20 / 64.0)
    sector['mu_Delta_over_50'] = 0.02
    return sector


if __name__ == '__main__':
    main()
