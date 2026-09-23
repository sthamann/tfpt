"""Exact integer Krylov norms via Onishi/Wick trace networks."""
import sys, json, time, hashlib
from pathlib import Path
from itertools import permutations
from math import factorial
from fractions import Fraction

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import common as C

N_MODES = C.N_MODES
N_BOSONS = C.N_BOSONS


GUARDS = []


def need(ok, name):
    if not ok:
        raise RuntimeError('GUARD failed: ' + name)
    GUARDS.append(name)


MAX_N = 5  # fixed depth: output must be deterministic (normal vs -OO byte-identical)


def load_model():
    W = C.load_tensor()
    M = C.channel_matrices(W)
    M_arr = np.stack(M).astype(np.int64)
    for A in range(N_BOSONS):
        need(int(np.count_nonzero(M_arr[A])) == 16, 'M_A 16 nonzero A=%d' % A)
        need(np.array_equal(M_arr[A], -M_arr[A].T), 'M_A antisym A=%d' % A)
    trAB = np.einsum('aij,bji->ab', M_arr, M_arr)
    need(np.array_equal(trAB, -16 * np.eye(N_BOSONS, dtype=np.int64)), 'tr M_A M_B = -16 delta')
    sumM2 = np.einsum('aij,ajk->ik', M_arr, M_arr)
    need(np.array_equal(sumM2, -15 * np.eye(N_MODES, dtype=np.int64)), 'sum M_A^2 = -15 I')
    need(int(np.max(np.abs(M_arr))) < (1 << 40), 'entries fit int40')
    return M_arr, W


def cycle_types(n):
    results = []
    def rec(rem, maxp, parts):
        if rem == 0:
            ck = {}
            for p in parts:
                ck[p] = ck.get(p, 0) + 1
            results.append(dict(sorted(ck.items())))
            return
        for p in range(min(rem, maxp), 0, -1):
            rec(rem - p, p, parts + [p])
    rec(n, n, [])
    return results


def build_slots(cyc_type):
    cycles = []
    slot = 0
    for k in sorted(cyc_type.keys()):
        for _ in range(cyc_type[k]):
            # position j of a k-cycle carries its own z-slot and zbar-slot index
            pairs = [(slot + j, slot + j) for j in range(k)]
            slot += k
            cycles.append(pairs)
    return cycles, slot


_PHI_CACHE = {}
EXACT_FLOAT_BOUND = 2 ** 53


def phi_tensor(M_arr):
    """Phi[i,j,k,l] = sum_A (M_A)_{ij} (M_A)_{kl}: the 60-contraction done once (64^4).

    Every supported pair belongs to exactly one channel, so Phi has entries in {-1,0,1}
    (guarded). It is stored as float64 so that BLAS tensordot can be used; exactness
    is certified per contraction step by an a-priori integer magnitude bound < 2^53.
    """
    key = id(M_arr)
    if key not in _PHI_CACHE:
        phi = np.einsum('aij,akl->ijkl', M_arr, M_arr)
        need(int(np.max(np.abs(phi))) == 1, 'Phi entries are in {-1,0,1}')
        _PHI_CACHE[key] = phi.astype(np.float64)
    return _PHI_CACHE[key]


PRIMES = [8191, 8179, 8171, 8167, 8161]   # all < 2^13: p^2 * 64^4 < 2^50 keeps every step exact
_PHI_MOD = {}
STATS = {'fast': 0, 'crt': 0}


class BoundExceeded(Exception):
    pass


def _steps(subs, Phi):
    einstr = ','.join(subs) + '->'
    path, _ = np.einsum_path(einstr, *([Phi] * len(subs)), optimize='optimal')
    return path[1:]                                  # path[0] is the header


def _contract_steps(subs, tensors, steps, reduce=None, abs_tensors=None):
    """Pairwise contraction along a precomputed path.

    reduce=p       : every intermediate is reduced mod p (used by the CRT route).
    abs_tensors    : companion contraction of the absolute values along the same path;
                     since |sum a_k b_k| <= sum |a_k||b_k| entrywise and the companion is a
                     sum of non-negative exactly representable terms, max(companion) < 2^53
                     certifies that every product and partial sum of the signed contraction
                     was exactly representable in float64 (raises BoundExceeded otherwise).
    """
    operands = [(s, t, a) for s, t, a in zip(subs, tensors, abs_tensors or [None] * len(subs))]
    for step in steps:
        idx = sorted(step, reverse=True)
        picked = [operands.pop(i) for i in idx]
        in_subs = [p[0] for p in picked]
        remaining = set(''.join(o[0] for o in operands))
        all_in = ''.join(in_subs)
        keep = ''.join(sorted({c for c in all_in if c in remaining}))
        expr = ','.join(in_subs) + '->' + keep
        result = np.einsum(expr, *[p[1] for p in picked], optimize=len(picked) > 1)
        companion = None
        if reduce is not None:
            result = np.mod(result, reduce)
        elif abs_tensors is not None:
            companion = np.einsum(expr, *[p[2] for p in picked], optimize=len(picked) > 1)
            if float(np.max(companion)) >= EXACT_FLOAT_BOUND:
                raise BoundExceeded()
        operands.append((keep, result, companion))
    need(len(operands) == 1 and operands[0][0] == '', 'contraction closes to a scalar')
    return operands[0][1]


def contract_exact(subs, Phi, n_cycles):
    """Exact integer value of a trace network built from n copies of Phi.

    Fast path: float64 with the absolute-value companion certificate (see
    _contract_steps). Fallback: evaluation modulo five primes < 2^13 (every step exact
    in float64 because p^2 * 64^4 < 2^53) and CRT reconstruction; uniqueness follows
    from the a-priori bound |network| <= 60^n * 64^(#cycles) < prod(p)/2 (guarded).
    """
    steps = _steps(subs, Phi)
    n = len(subs)
    try:
        absPhi = _PHI_CACHE.setdefault(('abs', id(Phi)), np.abs(Phi))
        val = float(_contract_steps(subs, [Phi] * n, steps, abs_tensors=[absPhi] * n))
        need(val == np.rint(val), 'trace network value is an integer')
        STATS['fast'] += 1
        return int(val)
    except BoundExceeded:
        pass
    apriori = 60 ** n * 64 ** n_cycles
    modulus = 1
    for p in PRIMES:
        modulus *= p
    need(2 * apriori < modulus, 'CRT modulus exceeds twice the a-priori network bound')
    residues = []
    for p in PRIMES:
        if p not in _PHI_MOD:
            _PHI_MOD[p] = np.mod(Phi, p)
        r = float(_contract_steps(subs, [_PHI_MOD[p]] * n, steps, reduce=p))
        residues.append(int(r) % p)
    x, m = 0, 1                                      # CRT (Garner) into the symmetric range
    for p, r in zip(PRIMES, residues):
        t = ((r - x) * pow(m, -1, p)) % p
        x += m * t
        m *= p
    if x > m // 2:
        x -= m
    need(abs(x) <= apriori, 'CRT value respects the a-priori bound')
    STATS['crt'] += 1
    return x


_PHI_SPARSE = {}


def phi_sparse(M_arr):
    """Phi as an exact sparse dict {(i,j,k,l): +-1}. Every supported ordered pair (i,j)
    has exactly the 16 ordered pairs of its own channel as partners, so nnz = 60*16*16."""
    key = id(M_arr)
    if key not in _PHI_SPARSE:
        d = {}
        for A in range(M_arr.shape[0]):
            nz = list(zip(*np.nonzero(M_arr[A])))
            for (i, j) in nz:
                v1 = int(M_arr[A, i, j])
                for (k, l) in nz:
                    d[(int(i), int(j), int(k), int(l))] = v1 * int(M_arr[A, k, l])
        need(len(d) == 60 * 16 * 16, 'sparse Phi has 60*16*16 nonzeros')
        _PHI_SPARSE[key] = d
    return _PHI_SPARSE[key]


def _sparse_contract_pair(sa, ta, sb, tb):
    """Exact contraction of two sparse tensors over their shared index letters."""
    shared = [c for c in sa if c in sb]
    keep_a = [c for c in sa if c not in shared]
    keep_b = [c for c in sb if c not in shared]
    ia = [sa.index(c) for c in shared]
    ib = [sb.index(c) for c in shared]
    ka = [sa.index(c) for c in keep_a]
    kb = [sb.index(c) for c in keep_b]
    index_b = {}
    for key, val in tb.items():
        index_b.setdefault(tuple(key[t] for t in ib), []).append((tuple(key[t] for t in kb), val))
    out = {}
    for key, val in ta.items():
        hits = index_b.get(tuple(key[t] for t in ia))
        if not hits:
            continue
        rest_a = tuple(key[t] for t in ka)
        for rest_b, vb in hits:
            k = rest_a + rest_b
            out[k] = out.get(k, 0) + val * vb
    out = {k: v for k, v in out.items() if v}
    return ''.join(keep_a) + ''.join(keep_b), out


def _self_trace(sub, t):
    """Contract repeated letters inside one sparse tensor (e.g. 'abba')."""
    while len(set(sub)) < len(sub):
        c = next(ch for ch in sub if sub.count(ch) > 1)
        pos = [i for i, ch in enumerate(sub) if ch == c]
        keep = [i for i in range(len(sub)) if i not in pos]
        out = {}
        for key, val in t.items():
            if all(key[pos[0]] == key[q] for q in pos[1:]):
                k = tuple(key[i] for i in keep)
                out[k] = out.get(k, 0) + val
        sub = ''.join(sub[i] for i in keep)
        t = {k: v for k, v in out.items() if v}
    return sub, t


def contract_sparse(subs, phi):
    """Exact integer value of a network by greedy sparse contraction (Python ints)."""
    ops = [_self_trace(s, phi) for s in subs]
    while len(ops) > 1:
        best = None
        for a in range(len(ops)):
            for b in range(a + 1, len(ops)):
                shared = sum(1 for c in ops[a][0] if c in ops[b][0])
                score = (shared, -(len(ops[a][1]) * len(ops[b][1])))
                if best is None or score > best[0]:
                    best = (score, a, b)
        _, a, b = best
        sb, tb = ops.pop(b)
        sa, ta = ops.pop(a)
        ops.append(_self_trace(*_sparse_contract_pair(sa, ta, sb, tb)))
    sub, t = ops[0]
    need(sub == '', 'sparse contraction closes to a scalar')
    return int(t.get((), 0))


LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def network_subs(cycles, sigma):
    """Index strings of the n Phi tensors for one Wick/trace network.

    Ring positions: a k-cycle has 2k positions, alternating z-slot (a_slot) and
    zbar-slot (b_slot) matrices, tr(M_{A_1} M_{B_1} ... M_{A_k} M_{B_k}). Wick pairing
    identifies B_{sigma(s)} = A_s, so every 60-index appears exactly twice; each pair
    becomes one Phi tensor whose four legs are the (row, col) bonds of the two ring
    positions.
    """
    n = len(sigma)
    zpos, zbpos = {}, {}
    bond = 0
    for cyc in cycles:
        k = len(cyc)
        ring = 2 * k
        base = bond
        bond += ring
        for j in range(k):
            a_slot, b_slot = cyc[j]
            zpos[a_slot] = (base + 2 * j, base + 2 * j + 1)
            nxt = base + 2 * j + 2
            if nxt >= base + ring:
                nxt = base
            zbpos[b_slot] = (base + 2 * j + 1, nxt)
    subs = []
    for s in range(n):
        r1, c1 = zpos[s]
        r2, c2 = zbpos[sigma[s]]          # zbar-slot sigma(s) carries A_{inv[sigma(s)]} = A_s
        subs.append(LETTERS[r1] + LETTERS[c1] + LETTERS[r2] + LETTERS[c2])
    return subs


def trace_network(cycles, sigma, M_arr):
    subs = network_subs(cycles, sigma)
    return contract_sparse(subs, phi_sparse(M_arr))


_SLOT_SWAP = (2, 3, 0, 1)


def graph_canonical_key(subs):
    """Canonical form of the 4-leg multigraph under the sign-free symmetries of Phi:
    relabelling of the n Phi nodes and, per node, the slot swap (ij)<->(kl)
    (Phi_{ij,kl} = Phi_{kl,ij}). Bond letters are anonymous; only the pairing of
    (node, leg) endpoints matters."""
    n = len(subs)
    endpoints = {}
    for node, sub in enumerate(subs):
        for leg, letter in enumerate(sub):
            endpoints.setdefault(letter, []).append((node, leg))
    edges = [tuple(v) for v in endpoints.values()]
    need(all(len(e) == 2 for e in edges), 'every bond joins exactly two endpoints')
    best = None
    for perm in permutations(range(n)):
        for swap_bits in range(1 << n):
            relabelled = []
            for (n1, l1), (n2, l2) in edges:
                if (swap_bits >> n1) & 1:
                    l1 = _SLOT_SWAP[l1]
                if (swap_bits >> n2) & 1:
                    l2 = _SLOT_SWAP[l2]
                a, b = (perm[n1], l1), (perm[n2], l2)
                relabelled.append((a, b) if a <= b else (b, a))
            key = tuple(sorted(relabelled))
            if best is None or key < best:
                best = key
    return best


def canonical_key(cycles, sigma):
    return graph_canonical_key(network_subs(cycles, sigma))


def compute_nu(n, M_arr, use_cache=True):
    total = Fraction(0)
    n_networks = 0
    cache = {}
    for cyc_type in cycle_types(n):
        cycles, ns = build_slots(cyc_type)
        pref = Fraction(1)
        for k, ck in cyc_type.items():
            pref *= Fraction(-1, 2 * k) ** ck / factorial(ck)
        net_sum = 0
        for sigma in permutations(range(n)):
            key = canonical_key(cycles, sigma) if use_cache else None
            if use_cache and key in cache:
                net = cache[key]
            else:
                net = trace_network(cycles, sigma, M_arr)
                if use_cache:
                    cache[key] = net
            net_sum += net
            n_networks += 1
        total += pref * net_sum
    nu = total * factorial(n) ** 2
    if nu.denominator != 1:
        raise RuntimeError('trace-network norm is not an integer for n=%d' % n)
    return int(nu), n_networks, len(cache) if use_cache else n_networks


def brute_force_nu1(M_arr):
    s = sum(int(np.trace(M_arr[A] @ M_arr[A])) for A in range(N_BOSONS))
    return (-1) * s // 2


def brute_force_nu2(W):
    support, _ = C.channel_support(W)
    def four_hole_state(A, B):
        st = {}
        for p, wa in support[A]:
            for q, wb in support[B]:
                if set(p) & set(q):
                    continue
                key = tuple(sorted(set(p) | set(q)))
                st[key] = st.get(key, 0) + wa * wb
        return st
    S_sum = 0
    for A in range(N_BOSONS):
        for B in range(N_BOSONS):
            st = four_hole_state(A, B)
            S_sum += sum(v*v for v in st.values())
    return 2 * S_sum


def main():
    M_arr, W = load_model()
    results = {}
    # Brute force validation in the occupation basis
    bf1 = brute_force_nu1(M_arr)
    need(bf1 == 480, 'brute nu1 == 480 (got %d)' % bf1)
    bf2 = brute_force_nu2(W)
    need(bf2 == 439680, 'brute nu2 == 439680 (got %d)' % bf2)
    # Trace formula
    wall_times = {}
    n_networks = {}
    n_canonical = {}
    for n in range(1, MAX_N + 1):
        t0 = time.time()
        nu, nnets, ncan = compute_nu(n, M_arr)
        wall_times[str(n)] = time.time() - t0
        n_networks[str(n)] = nnets
        n_canonical[str(n)] = ncan
        results[str(n)] = str(nu)
        need(nu > 0, 'trace nu%d positive' % n)
        if n == 1:
            need(nu == 480, 'trace nu1 == 480 (got %d)' % nu)
            need(nu == bf1, 'trace nu1 == brute nu1')
        if n == 2:
            need(nu == 439680, 'trace nu2 == 439680 (got %d)' % nu)
            need(nu == bf2, 'trace nu2 == brute nu2')
    # Cross-check of the exact sparse route against the independent dense float64 route
    # (Phi tensor, optimal einsum path, absolute-value companion certificate, CRT fallback)
    # on every canonical network with n <= 4.
    Phi = phi_tensor(M_arr)
    phi_sp = phi_sparse(M_arr)
    checked = 0
    for n in range(1, 5):
        seen = set()
        for cyc_type in cycle_types(n):
            cycles, _ = build_slots(cyc_type)
            for sigma in permutations(range(n)):
                subs = network_subs(cycles, sigma)
                key = graph_canonical_key(subs)
                if key in seen:
                    continue
                seen.add(key)
                need(contract_sparse(subs, phi_sp) == contract_exact(subs, Phi, len(cycles)),
                     'sparse and dense-certified network values agree (n=%d)' % n)
                checked += 1
    path_stats = {'dense_cross_checked_networks': checked,
                  'dense_fast_path': STATS['fast'], 'dense_crt_path': STATS['crt']}
    # Jacobi ratios nu_{n+1}/nu_n as exact fractions
    jacobi = {}
    for n in range(1, MAX_N):
        frac = Fraction(int(results[str(n + 1)]), int(results[str(n)]))
        jacobi[str(n)] = {'num': int(frac.numerator), 'den': int(frac.denominator), 'float': float(frac)}
    common_sha = hashlib.sha256(Path(C.__file__).read_bytes()).hexdigest()
    checker_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out = {
        'status': 'PASS',
        'nu': results,
        'max_n': MAX_N,
        'guards': list(GUARDS),
        'guards_count': len(GUARDS),
        'checker_sha256': checker_sha,
        'common_sha256': common_sha,
        'n_networks': n_networks,
        'n_canonical': n_canonical,
        'evaluation_paths': path_stats,
        'network_evaluation': 'exact sparse dict contraction over Python integers (Phi has 15360 nonzeros); '
                              'networks canonicalised as 4-leg multigraphs under node relabelling and slot swap',
        'apriori_network_bound': '|network| <= 60^n * 64^(#cycles); CRT modulus prod(PRIMES) = %d' % (
            8191 * 8179 * 8171 * 8167 * 8161),
        'jacobi_ratios': jacobi,
        'method': 'Onishi determinant + bosonic coherent-state Gaussian integral + Wick pairing; '
                  'exact Fraction prefactors, int64 einsum trace networks',
    }
    with open(HERE / 'norms_by_traces.json', 'w') as f:
        json.dump(out, f, indent=1, sort_keys=True)
    print(json.dumps(out, indent=1, sort_keys=True))
    print(json.dumps({'wall_times_s': wall_times}), file=sys.stderr)


if __name__ == '__main__':
    main()
