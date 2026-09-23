"""KeyC tasks 1+4: level-2 localization profile and condensate criterion.

Theory contract, experiments only. No paper/ledger/website edits, no commits.
Self-contained (copied W construction + hole-picture Krylov code, no imports
from source folders). Deterministic JSON to stdout (no timestamps).

Task 1 (exakt underlying, numerisch Ritz combination):
- v2 (108240 entries) via exact double-vertex enumeration (hole masks).
- Irrep R-projections (54,1),(1,20'),(54,20'),(45,15) via spin/color traces
  (verify_two_boson method): exact integer norms 17280,7680,241920,172800.
- Full numpy chain v0..v3 + w2 (15.25M entries streamed, merged per channel):
  exact guards (Tv1=480v0, Tv2=916v1, <v2|u>=nu3, Pythagoras, w2 norm).
- w2 R-profile: exact cross/norm traces on the scaled integer vector (q=229).
- K=3 Ritz evec at g/Delta=1/20 (numerisch float64 eig) => |<s_R|Omega>|^2.

Task 4 (condensate): muN splitting 0 (exakt); G-invariant diagonal shifts keep
all R weights >0 (couplings all nonzero, numerisch scan); verdict: localization
requires breaking G.
"""
import json
from collections import defaultdict
from itertools import combinations, permutations
from fractions import Fraction
from pathlib import Path
import numpy as np

checks = []
def need(ok, name):
    if not ok:
        raise RuntimeError(name)
    checks.append(name)

N_MODES = 64
N_BOSONS = 60
PAD = 60
CODE0 = PAD + 60*PAD + 3600*PAD

# ---------- W reconstruction (copied, no external file) ----------
def build_W():
    def _jw(n):
        out = []
        for j in range(n):
            a = np.zeros((2**n, 2**n), dtype=np.int64)
            for m in range(2**n):
                if (m >> j) & 1:
                    a[m ^ (1 << j), m] = (-1)**((m & ((1 << j)-1)).bit_count())
            out.append(a)
        return out
    ANN5 = _jw(5)
    EVEN16 = [m for m in range(32) if m.bit_count() % 2 == 0]
    CONJ = np.eye(32, dtype=np.int64)
    for _a in ANN5:
        CONJ = CONJ @ (_a + _a.T)
    BETA = [(CONJ @ _a)[np.ix_(EVEN16, EVEN16)] for _a in ANN5 + [_a.T for _a in ANN5]]
    PAIRS = list(combinations(range(64), 2))
    COLORS = list(combinations(range(4), 2))
    W = np.zeros((60, 2016), dtype=np.int64)
    for k, beta in enumerate(BETA):
        for c, (l, r) in enumerate(COLORS):
            for j, (v, w) in enumerate(PAIRS):
                vs, vc = divmod(v, 4)
                ws, wc = divmod(w, 4)
                W[6*k + c, j] = beta[vs, ws] * (int(vc == l and wc == r) - int(vc == r and wc == l))
    need(np.array_equal(W @ W.T, 8*np.eye(60, dtype=int)), 'W WT = 8I')
    need(int(np.count_nonzero(W)) == 480, '480 vertices')
    return W, PAIRS, COLORS

# ---------- numpy hole-chain helpers (copied from native_ground_state) ----------
def decode_code(code):
    code = np.asarray(code, dtype=np.int64)
    A1 = np.full(code.shape, PAD, dtype=np.int64)
    A2 = np.full(code.shape, PAD, dtype=np.int64)
    A3 = np.full(code.shape, PAD, dtype=np.int64)
    s3 = code < 216000
    s2 = (code >= 216000) & (code < 219600)
    s1 = (code >= 219600) & (code < 219660)
    c3 = code[s3]
    A3[s3] = c3 // 3600
    r3 = c3 % 3600
    A2[s3] = r3 // 60
    A1[s3] = r3 % 60
    c2 = code[s2] - 216000
    A2[s2] = c2 // 60
    A1[s2] = c2 % 60
    c1 = code[s1] - 219600
    A1[s1] = c1
    return A1, A2, A3

def encode3(A1, A2, A3):
    return A1 + 60*A2 + 3600*A3

def insert_boson(code, A_new):
    A1, A2, A3 = decode_code(code)
    c1 = A_new <= A1
    c2 = (~c1) & (A_new <= A2)
    new1 = np.where(c1, A_new, A1)
    new2 = np.where(c1, A1, np.where(c2, A_new, A2))
    new3 = np.where(c1, A2, np.where(c2, A2, A_new))
    return encode3(new1, new2, new3)

def remove_boson(code, A_rem):
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
    A1, A2, A3 = decode_code(codes)
    eq12 = (A1 == A2) & (A1 != PAD)
    eq23 = (A2 == A3) & (A2 != PAD)
    all3 = eq12 & eq23
    two = (eq12 | eq23) & ~all3
    return np.where(all3, 6, np.where(two, 2, 1)).astype(np.int64)

def parity_below(masks, j):
    masks = np.asarray(masks, dtype=np.uint64)
    low = masks & np.uint64((1 << j) - 1)
    return 1 - 2*(np.bitwise_count(low).astype(np.int64) & 1)

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
    masks, codes, amps = state
    if masks.shape[0] == 0:
        return 0
    w = weight_factor(codes)
    amax = int(np.max(np.abs(amps)))
    need(amax*amax*6*masks.shape[0] < (1 << 62), 'norm2 int64 guard')
    return int(np.sum(amps*amps*w, dtype=np.int64))

KEY_DTYPE = np.dtype([('c', np.int64), ('m', np.uint64)])
def _keys(state):
    masks, codes, _ = state
    k = np.empty(masks.shape[0], dtype=KEY_DTYPE)
    k['c'] = codes
    k['m'] = masks
    return k

def inner(a, b):
    a = merge(a); b = merge(b)
    if a[0].shape[0] == 0 or b[0].shape[0] == 0:
        return 0
    common, ia, ib = np.intersect1d(_keys(a), _keys(b), assume_unique=True, return_indices=True)
    if common.size == 0:
        return 0
    wa = weight_factor(a[1][ia]).astype(object)
    return int(np.sum(a[2][ia].astype(object)*b[2][ib].astype(object)*wa))

def apply_Tdag(state, support):
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
            na = a*np.int64(wval)*sj*si
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
    masks, codes, amps = state
    A1, A2, A3 = decode_code(codes)
    out_m, out_c, out_a = [], [], []
    slots = [A1, A2, A3]
    for slot in range(3):
        A_rem = slots[slot]
        first = A_rem != PAD
        if slot > 0:
            first &= slots[slot-1] != A_rem
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
                mm = m[keep]; cc_ = nc[keep]; aa = a[keep]*mult[keep]
                si = parity_below(mm, i)
                m1 = mm ^ bi
                sj = parity_below(m1, j)
                m2 = m1 ^ bj
                na = aa*np.int64(wval)*(si*sj)
                out_m.append(m2); out_c.append(cc_); out_a.append(na)
    if not out_m:
        return make_state([], [], [])
    return merge((np.concatenate(out_m), np.concatenate(out_c), np.concatenate(out_a)))

def subtract_scaled(u, v, alpha):
    p, q = alpha.numerator, alpha.denominator
    mu, cu, au = u
    mv, cv, av = v
    all_m = np.concatenate([mu, mv])
    all_c = np.concatenate([cu, cv])
    all_a = np.concatenate([au*q, -(av*p)])
    return merge((all_m, all_c, all_a))

# ---------- R-projection helpers (ordered tensor + traces) ----------
def ordered_R(vdict):
    R = {}
    for (mask, A, B), c in vdict.items():
        if A == B:
            R[(mask, A, B)] = 2*c
        else:
            R[(mask, A, B)] = R.get((mask, A, B), 0) + c
            R[(mask, B, A)] = R.get((mask, B, A), 0) + c
    return {k: v for k, v in R.items() if v}

def traces_of(R, cb, ce):
    spin_trace = defaultdict(int)
    color_trace = defaultdict(int)
    both_trace = defaultdict(int)
    rf = 0
    for (mask, A, B), amp in R.items():
        k, c = divmod(A, 6); l, d = divmod(B, 6)
        rf += amp*R.get((mask, 6*l+c, 6*k+d), 0)
        if l == (k+5) % 10:
            spin_trace[(mask, c, d)] += amp
        if d == cb[c]:
            color_trace[(mask, k, l)] += ce[c]*amp
        if l == (k+5) % 10 and d == cb[c]:
            both_trace[mask] += ce[c]*amp
    return spin_trace, color_trace, both_trace, rf

def main():
    W, PAIRS, COLORS = build_W()
    PAIR_INDEX = {p: j for j, p in enumerate(PAIRS)}
    support = []
    for A in range(60):
        cols = np.flatnonzero(W[A])
        support.append([(tuple(PAIRS[c]), int(W[A, c])) for c in cols])
    need(sum(len(s) for s in support) == 480, 'support 480')
    # ---- v2 dict (hole masks, sorted boson pairs) ----
    def sign(mask, i):
        return (-1)**((mask & ((1 << i)-1)).bit_count())
    verts = [(int(A), p[0], p[1], int(W[A, PAIR_INDEX[p]]))
             for A in range(60) for p, _ in support[A]]
    # rebuild verts with values
    verts = []
    for A in range(60):
        for (i, j), wv in support[A]:
            verts.append((A, i, j, wv))
    need(len(verts) == 480, '480 verts')
    v2 = defaultdict(int)
    for A, i, j, w in verts:
        mask = (1 << i) | (1 << j)
        for B, k, l, z in verts:
            if mask & ((1 << k) | (1 << l)):
                continue
            s = sign(mask, l)*sign(mask | (1 << l), k)
            key = (mask | (1 << k) | (1 << l), min(A, B), max(A, B))
            v2[key] += w*z*s
    v2 = {k: v for k, v in v2.items() if v}
    nu2 = sum(c*c*(2 if A == B else 1) for (mask, A, B), c in v2.items())
    need(len(v2) == 108240 and nu2 == 439680, 'v2 108240 entries norm 439680')
    # ---- R projections of v2 ----
    eps = {p: (-1)**sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4))
           for p in permutations(range(4))}
    cb = []; ce = []
    for c, (a, b) in enumerate(COLORS):
        other = tuple(v for v in range(4) if v not in (a, b))
        cb.append(COLORS.index(other)); ce.append(eps[(a, b, *other)])
    R = ordered_R(v2)
    nr = sum(c*c for c in R.values())
    need(nr == 2*nu2, 'ordered norm 2*nu2')
    st, ct, bt, rf = traces_of(R, cb, ce)
    ps = Fraction(sum(a*a for a in st.values()), 10)
    pc = Fraction(sum(a*a for a in ct.values()), 6)
    p00 = Fraction(sum(a*a for a in bt.values()), 60)
    pplus = Fraction(nr + rf, 2); pminus = Fraction(nr - rf, 2)
    norms = {'(1,1)': p00/2, '(54,1)': (pc-p00)/2, '(1,20p)': (ps-p00)/2,
             '(54,20p)': (pplus-pc-ps+p00)/2, '(45,15)': pminus/2}
    need(p00 == 0, 'scalar-scalar vanishes')
    need(sum(norms.values()) == nu2, 'projections exhaust v2')
    need(all(v > 0 for k, v in norms.items() if k != '(1,1)'), 'all four populated')
    need(all(v.denominator == 1 for v in norms.values()), 'R norms integral')
    nR = {k: int(v) for k, v in norms.items()}
    need(nR == {'(1,1)': 0, '(54,1)': 17280, '(1,20p)': 7680, '(54,20p)': 241920, '(45,15)': 172800},
         'R norms 17280/7680/241920/172800')
    couplings = {k: Fraction(v, 480) for k, v in nR.items() if v}
    need(sum(couplings.values()) == 916, 'couplings sum 916')
    need(set(couplings.values()) == {36, 16, 504, 360}, 'couplings 36/16/504/360')
    # ---- numpy chain v0..v3, w2 (heavy, streamed) ----
    v0 = make_state(np.array([0], dtype=np.uint64), np.array([CODE0], dtype=np.int64),
                    np.array([1], dtype=np.int64))
    v1 = apply_Tdag(v0, support)
    need(v1[0].shape[0] == 480 and norm2(v1) == 480, 'v1 480 norm 480')
    v2n = apply_Tdag(v1, support)
    need(norm2(v2n) == 439680, 'numpy v2 norm 439680')
    # cross-check numpy v2 vs dict v2 (keys + amps, boson factor aware)
    # decode numpy v2 to dict
    A1, A2, A3 = decode_code(v2n[1])
    need(bool(np.all(A3 == PAD)), 'numpy v2 all level-2 (third slot empty)')
    conv = {}
    for mm, a, b, amp in zip(v2n[0].tolist(), A1.tolist(), A2.tolist(), v2n[2].tolist()):
        key = (int(mm), min(int(a), int(b)), max(int(a), int(b)))
        conv[key] = conv.get(key, 0) + int(amp)
    conv = {k: v for k, v in conv.items() if v}
    need(len(conv) == len(v2), 'numpy v2 support matches dict v2')
    # compare up to global sign? both use same hole convention => exact equality
    diff = sum(1 for k in v2 if conv.get(k, 0) != v2[k])
    need(diff == 0, 'numpy v2 equals dict v2 entrywise')
    v3 = apply_Tdag(v2n, support)
    nu3 = norm2(v3)
    need(nu3 == 575078400, 'nu3 575078400')
    need(v3[0].shape[0] == 15252960, 'v3 15252960 entries')
    # closure
    Tv1 = apply_T(v1, support)
    need(Tv1[0].shape[0] == 1 and int(Tv1[0][0]) == 0 and int(Tv1[1][0]) == CODE0
         and int(Tv1[2][0]) == 480, 'T v1 = 480 v0')
    Tv2 = apply_T(v2n, support)
    need(Tv2[0].shape[0] == v1[0].shape[0] and np.array_equal(Tv2[0], v1[0])
         and np.array_equal(Tv2[1], v1[1]) and np.array_equal(Tv2[2], v1[2]*916),
         'T v2 = 916 v1')
    u = apply_T(v3, support)
    vu = inner(v2n, u)
    need(vu == nu3, 'adjoint <v2|u> = nu3')
    u_norm2 = inner(u, u)
    alpha = Fraction(vu, nu2)
    need(alpha == Fraction(299520, 229), 'alpha 299520/229')
    w2 = subtract_scaled(u, v2n, alpha)
    q = int(alpha.denominator)
    need(q == 229, 'w2 scale 229')
    w2s_norm2 = inner(w2, w2)
    w2n_exact = Fraction(w2s_norm2, q*q)
    need(w2n_exact == Fraction(5001523200, 229), 'w2 norm 5001523200/229')
    need(Fraction(u_norm2) - Fraction(vu*vu, nu2) == w2n_exact, 'Pythagoras')
    need(inner(w2, v2n) == 0, 'w2 perp v2')
    need(Fraction(inner(w2, u), q) == w2n_exact, '<w2|u> check')
    # ---- w2 R-profile (scaled integer vector) ----
    wA1, wA2, wA3 = decode_code(w2[1])
    # all w2 entries must be level-2 (2 bosons): A3 == PAD
    need(bool(np.all(wA3 == PAD)), 'w2 all level-2')
    need(bool(np.all(wA1 != PAD)) and bool(np.all(wA2 != PAD)), 'w2 two bosons present')
    wdict = {}
    for mm, a, b, amp in zip(w2[0].tolist(), wA1.tolist(), wA2.tolist(), w2[2].tolist()):
        key = (int(mm), min(int(a), int(b)), max(int(a), int(b)))
        wdict[key] = wdict.get(key, 0) + int(amp)
    wdict = {k: v for k, v in wdict.items() if v}
    # norm check with boson factorials: ||w_scaled||^2 = w2s_norm2
    wcheck = sum(c*c*(2 if A == B else 1) for (mask, A, B), c in wdict.items())
    need(wcheck == w2s_norm2, 'wdict norm matches scaled norm')
    Rw = ordered_R(wdict)
    nrw = sum(c*c for c in Rw.values())
    need(nrw == 2*w2s_norm2, 'ordered w norm')
    # cross <R_v|R_w> must vanish (orthogonality)
    # iterate over smaller dict
    if len(R) <= len(Rw):
        nrcross = sum(amp*Rw.get(k, 0) for k, amp in R.items())
    else:
        nrcross = sum(amp*R.get(k, 0) for k, amp in Rw.items())
    need(nrcross == 0, 'ordered cross vanishes (v2 perp w2)')
    stw, ctw, btw, rfw = traces_of(Rw, cb, ce)
    # self traces for w (Fractions)
    psw = Fraction(sum(a*a for a in stw.values()), 10)
    pcw = Fraction(sum(a*a for a in ctw.values()), 6)
    p00w = Fraction(sum(a*a for a in btw.values()), 60)
    pplusw = Fraction(nrw + rfw, 2); pminusw = Fraction(nrw - rfw, 2)
    normsw = {'(1,1)': p00w/2, '(54,1)': (pcw-p00w)/2, '(1,20p)': (psw-p00w)/2,
              '(54,20p)': (pplusw-pcw-psw+p00w)/2, '(45,15)': pminusw/2}
    need(sum(normsw.values()) == w2s_norm2, 'w projections exhaust scaled norm')
    need(all(v >= 0 for v in normsw.values()), 'w projections nonnegative')
    # cross traces
    def cross_sum(dv, dw):
        if len(dv) <= len(dw):
            return sum(a*dw.get(k, 0) for k, a in dv.items())
        return sum(a*dv.get(k, 0) for k, a in dw.items())
    psx = Fraction(cross_sum(st, stw), 10)
    pcx = Fraction(cross_sum(ct, ctw), 6)
    p00x = Fraction(cross_sum(bt, btw), 60)
    # rf cross: sum over ordered R_v entries of R_v * R_w(swapped)
    rfx = 0
    for (mask, A, B), amp in R.items():
        k, c = divmod(A, 6); l, d = divmod(B, 6)
        rfx += amp*Rw.get((mask, 6*l+c, 6*k+d), 0)
    pplusx = Fraction(nrcross + rfx, 2); pminusx = Fraction(nrcross - rfx, 2)
    crossR = {'(1,1)': p00x/2, '(54,1)': (pcx-p00x)/2, '(1,20p)': (psx-p00x)/2,
              '(54,20p)': (pplusx-pcx-psx+p00x)/2, '(45,15)': pminusx/2}
    need(sum(crossR.values()) == 0, 'cross R sum vanishes')
    # lambda_R = C_R/(q * norms_R) for the four populated copies
    lam = {}
    for k in ('(54,1)', '(1,20p)', '(54,20p)', '(45,15)'):
        lam[k] = crossR[k]/(q*nR[k])
    # w2 own profile q_R = normsw_R / w2s_norm2 (exact, sums to 1)
    qR = {k: (normsw[k]/w2s_norm2 if w2s_norm2 else Fraction(0)) for k in normsw}
    need(sum(qR.values()) == 1, 'w profile sums to 1')
    # ---- K=3 Ritz evec at g=1/20 (numerisch) ----
    NU = [1, 480, 439680, 575078400]
    gnum = 1.0/20.0
    # 5x5: v0..v3 + w2 (energy 2 at index 4, coupling to v3)
    H = np.zeros((5, 5))
    for i in range(4):
        H[i, i] = float(i)
    H[4, 4] = 2.0
    for i in range(3):
        H[i, i+1] = H[i+1, i] = gnum*np.sqrt(NU[i+1]/NU[i])
    H[3, 4] = H[4, 3] = gnum*np.sqrt(float(w2n_exact)/NU[3])
    evals, evecs = np.linalg.eigh(H)
    gi = int(np.argmin(evals))
    E3 = float(evals[gi]); ev = evecs[:, gi].copy()
    need(abs(E3 - (-1.0942318710142456)) < 2e-9, 'K=3 Ritz energy')
    need(abs(float(ev @ ev) - 1.0) < 1e-12, 'evec normalized')
    c0, c1, c2, c3, cw = (float(x) for x in ev)
    # overlaps |<s_R|Omega>|^2 with s_R = P_R v2/||P_R v2||
    import math
    wtrue = math.sqrt(float(w2n_exact))
    sqnu2 = math.sqrt(float(nu2))
    overlaps = {}
    for k in ('(54,1)', '(1,20p)', '(54,20p)', '(45,15)'):
        s = math.sqrt(float(nR[k]))
        amp = s*(c2/sqnu2 + cw*float(lam[k])/wtrue)
        overlaps[k] = amp*amp
    p2tot = float(c2*c2 + cw*cw)
    need(abs(sum(overlaps.values()) - p2tot) < 1e-9, 'overlaps sum to level-2 weight')
    # exact v2 profile p_R and participation ratios
    pR = {k: Fraction(nR[k], nu2) for k in nR if nR[k]}
    need(sum(pR.values()) == 1, 'v2 profile sums to 1')
    ipr_v2 = sum(v*v for v in pR.values())
    PR_v2 = float(1/ipr_v2)
    max_v2 = max(float(v) for v in pR.values())
    ipr_w = sum(v*v for v in qR.values())
    PR_w = float(1/ipr_w) if ipr_w else 0.0
    max_w = max(float(v) for v in qR.values())
    # Omega level-2 conditional distribution (numerisch): overlaps / p2tot
    cond = {k: (overlaps[k]/p2tot if p2tot else 0.0) for k in overlaps}
    PR_o = float(1/sum(v*v for v in cond.values())) if p2tot else 0.0
    max_o = max(cond.values()) if cond else 0.0
    need(max_v2 < 0.6 and PR_v2 > 2.0, 'v2 delocalized over copies')
    # ---- Task 4: condensate criterion ----
    # muN splitting within N=64 level-2: Nf=60,Nb=2 for all => 0 (exakt)
    # G-invariant diagonal scan: 6-dim model (v0,v1,4R), eps in {-1,0,1}
    coup = [36.0, 16.0, 504.0, 360.0]
    keys4 = ['(54,1)', '(1,20p)', '(54,20p)', '(45,15)']
    def ground_max(eps):
        M = np.zeros((6, 6))
        M[0, 0] = 0.0; M[1, 1] = 1.0
        for t in range(4):
            M[2+t, 2+t] = 2.0 + eps[t]
        M[0, 1] = M[1, 0] = gnum*math.sqrt(480.0)
        for t in range(4):
            M[1, 2+t] = M[2+t, 1] = gnum*math.sqrt(coup[t])
        w, V = np.linalg.eigh(M)
        g0 = V[:, int(np.argmin(w))]
        lv = np.array([g0[2+t]**2 for t in range(4)])
        s = lv.sum()
        dist = lv/s if s > 0 else lv
        return float(dist.max()), float(1/np.sum(dist**2)) if s > 0 else 0.0
    worst_max = 0.0
    worst_PR = 10.0
    for e0 in (-1.0, 0.0, 1.0):
        for e1 in (-1.0, 0.0, 1.0):
            for e2 in (-1.0, 0.0, 1.0):
                for e3 in (-1.0, 0.0, 1.0):
                    mx, pr = ground_max([e0, e1, e2, e3])
                    worst_max = max(worst_max, mx)
                    worst_PR = min(worst_PR, pr)
    need(worst_max < 0.9, 'no symmetric O(Delta) shift localizes (max<0.9)')
    need(min(coup) > 0, 'all bright couplings nonzero')
    def fr(x):
        return '%d/%d' % (x.numerator, x.denominator) if isinstance(x, Fraction) else str(x)
    out = {
        'status': 'PASS',
        'guards_count': len(checks),
        'guards': checks,
        'v2': {'entries': len(v2), 'norm2_exact': nu2,
               'R_norms_exact': {k: nR[k] for k in keys4},
               'couplings_exact': {k: int(couplings[k]) for k in keys4},
               'profile_pR_exact': {k: fr(pR[k]) for k in keys4},
               'profile_pR_float': {k: float(pR[k]) for k in keys4},
               'participation_ratio': PR_v2, 'max_weight': max_v2, 'kind': 'exakt'},
        'w2': {'scale_q_exact': q, 'norm2_exact': fr(w2n_exact),
               'scaled_entries': len(wdict), 'scaled_norm2_exact': w2s_norm2,
               'R_norms_scaled_exact': {k: fr(normsw[k]) for k in keys4},
               'profile_qR_exact': {k: fr(qR[k]) for k in keys4},
               'profile_qR_float': {k: float(qR[k]) for k in keys4},
               'lambda_exact': {k: fr(lam[k]) for k in keys4},
               'participation_ratio': PR_w, 'max_weight': max_w, 'kind': 'exakt'},
        'ritz_K3_g_1_20': {'kind': 'numerisch (float64 eig, variational upper bound)',
                           'E': E3, 'evec': [c0, c1, c2, c3, cw],
                           'p_level2_total': p2tot},
        'omega_overlaps': {'kind': 'numerisch (exakt R-norms x numerisch Ritz coeffs)',
                           'values': overlaps, 'conditional_level2': cond,
                           'participation_ratio_level2': PR_o, 'max_weight_level2': max_o},
        'localization_verdict': {
            'kind': 'exakt/numerisch',
            'statement': ('Delocalized: normalized v2 spreads (max 504/916=0.550, PR=2.18) over all four '
                          'copies (exakt); w2 profile exact above; K=3 Ritz level-2 conditional max %.4f, '
                          'PR %.3f (numerisch) — concentrated single-copy weight never reached.' % (max_o, PR_o)),
            'localized': False,
        },
        'condensate': {
            'muN_splitting_kind': 'exakt',
            'muN_splitting_within_level2': 0,
            'muN_reason': 'N=64 level-2 has Nf=60,Nb=2 for all states; muN is a c-number, no splitting.',
            'G_invariant_scan_kind': 'numerisch (81 corners, 6-dim exact-diagonalization scan)',
            'couplings_all_nonzero': [36, 16, 504, 360],
            'worst_max_weight_O Delta': worst_max,
            'worst_PR_O Delta': worst_PR,
            'verdict_kind': 'exakt/numerisch',
            'verdict': ('No symmetry-allowed level-diagonal perturbation with |eps|<=Delta localizes '
                        '(max<0.9, all couplings>0 so all R weights stay >0 for finite shifts); '
                        'localization onto one copy requires zeroing 3 of 4 bright couplings or '
                        'R-mixing, i.e. breaking internal G.'),
        },
        'labels': {'v2_R': 'exakt', 'w2_R': 'exakt', 'ritz': 'numerisch',
                   'omega_overlaps': 'numerisch', 'verdict': 'exakt/numerisch'},
    }
    print(json.dumps(out, indent=1, sort_keys=True))

if __name__ == '__main__':
    main()
