"""Seam-reflection operator contract — does the original marked TFPT seam
deliver exactly the common pair of reflection actions (vertex on fermion
sites, shifted edge on pair banks) including state compatibility?

Five exact parts, all finite and machine-checked:

  S1  Seam skeleton: the D4 of (P^1, mu4) from the v177/v180 normal form,
      its unique vertex-reflection class, the induced edge action, and the
      (unsigned) H^1 action w1<->w3, w2 fixed.
  S2  Exhaustive enumeration of the real two-neighbour 4-cycle frame class:
      every signed clock (16), every signed square reflection (4 permutation
      types x 16 sign patterns), filtered by involution, signed dihedral
      relation, pair covariance at balance, and absence of dark modes.
  S3  Native operator assignment: the explicit reflection Sigma on the
      256-fermion four-bank model with the pinned in-repo native W tensor,
      checked term by term (CAR signs included), plus Gram-level state
      compatibility (B, T, and every reduced operator D - kT).
  S4  Toy full-Fock state compatibility: 8-mode model, exact 256-dim Fock
      matrices, [U_Sigma, Q] = 0, filled-state eigenvalue, one-hole sector.
  S5  Growing-size probe: exact dark-mode rank rule for n = 3..16, and the
      N2-chain charged band versus a relativistic dispersion through O(k^6).

Honest residuals (recorded, not fabricated): the raw-seam production of the
marked boundary and kernel (QGEO.MARKS.01 / QGEO.KERNEL.01) stays open; the
spinorial sign is selected by the no-dark-mode condition, not derived from
raw seam geometry; the physical coupling, the 3+1D origin, the chiral
measure and the spin-2 sector are untouched. Firewall: theory contract —
no claims in verification/, status_ledger.csv, papers or website.

Run without arguments; JSON goes to stdout. No source files are modified.
"""
from collections import defaultdict
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import runpy
import time

import numpy as np
import sympy as s
from scipy.sparse import coo_matrix, csr_matrix, eye as speye

HERE = Path(__file__).resolve().parent
NATIVE_SOURCE = (HERE.parent / 'universalraum-singlet-observable-20260915'
                 / 'sources' / 'native_source.py')
EXPECTED_W_TOBYTES = '7a4a0b1c4401a20a84aee47b75f9b9d8882299bdff938ba11fd5b2bfe5656112'
CHECKS = []
T0 = time.time()


def need(value, name):
    if not bool(value):
        raise RuntimeError(name)
    CHECKS.append(name)


def signed_shift(signs):
    n = len(signs)
    return s.Matrix(n, n, lambda j, k: signs[j] if k == (j + 1) % n else 0)


def reflection_matrix(pi, sigmas):
    return s.Matrix(4, 4, lambda j, k: sigmas[k] if j == pi[k] else 0)


# ---------------------------------------------------------------- S1 -------
def seam_skeleton():
    """The geometric normal form of the marked seam and its reflection."""
    z = s.symbols('z')
    I = s.I
    mu4 = [s.Integer(1), I, s.Integer(-1), -I]
    rho = lambda w: I * w
    sig = lambda w: 1 / w
    need(s.simplify(sig(rho(sig(z))) - (-I * z)) == 0,
         'S1 seam dihedral sigma.rho.sigma = rho^-1')
    chain = [mu4[0]]
    for _ in range(3):
        chain.append(s.simplify(rho(chain[-1])))
    need(set(chain) == set(mu4) and s.simplify(rho(chain[-1])) == mu4[0],
         'S1 the four marks are one clock orbit')
    # Vertex permutation induced by sigma on the mark indices 0..3.
    image = [s.simplify(sig(m)) for m in mu4]
    pi_seam = tuple(mu4.index(v) for v in image)
    need(pi_seam == (0, 3, 2, 1),
         'S1 seam reflection fixes marks 1,-1 and swaps i,-i')
    # Induced action on the four edges of the mark square (edge e = (e, e+1)).
    edges = [(e, (e + 1) % 4) for e in range(4)]

    def edge_image(pi):
        out = []
        for a, b in edges:
            mapped = tuple(sorted((pi[a], pi[b])))
            out.append(next(k for k, e in enumerate(edges)
                            if tuple(sorted(e)) == mapped))
        return tuple(out)

    edge_perm = edge_image(pi_seam)
    need(edge_perm == (3, 2, 1, 0),
         'S1 induced edge permutation is (0 3)(1 2)')
    # The two vertex reflections of the square are clock-conjugate.
    rho_perm = (1, 2, 3, 0)  # mark index map of z -> i z
    inv = [rho_perm.index(i) for i in range(4)]
    conj_perm = tuple(rho_perm[pi_seam[inv[i]]] for i in range(4))
    need(conj_perm == (2, 1, 0, 3),
         'S1 the two vertex reflections are clock-conjugate')
    # H^1 action: sigma* w_k = + w_{4-k} (all signs positive).
    refl = {}
    for kk in (1, 2, 3):
        f = z**(kk - 1) / (z**4 - 1)
        sig_f = s.simplify(f.subs(z, 1 / z) * (-1 / z**2))
        target = z**((4 - kk) - 1) / (z**4 - 1)
        refl[kk] = 4 - kk if s.simplify(sig_f - target) == 0 else None
    need(refl == {1: 3, 2: 2, 3: 1},
         'S1 seam reflection on H^1: w1<->w3, w2 fixed, all signs +1')
    # The documented original inner clock (duad construction) has order 6.
    p = (2, 0, 1, 4, 3)
    cur, order = list(range(5)), 0
    while order < 12:
        cur = [p[cur[i]] for i in range(5)]
        order += 1
        if cur == list(range(5)):
            break
    need(order == 6 and order != 4,
         'S1 original inner clock has order 6, not the order-4 seam clock')
    return {'mark_reflection_perm': pi_seam, 'induced_edge_perm': edge_perm,
            'h1_reflection': refl, 'h1_signs': 'all +1 (classical geometry unsigned)',
            'original_inner_clock_order': order,
            'original_inner_clock_is_not_seam_clock': True}


# ---------------------------------------------------------------- S2 -------
def enumeration():
    """Exhaustive filter of the real two-neighbour 4-cycle frame class."""
    a, b = s.symbols('a b', real=True)
    vertex_types = {'(1 3)': (0, 3, 2, 1), '(0 2)': (2, 1, 0, 3)}
    edge_types = {'(0 1)(2 3)': (1, 0, 3, 2), '(1 2)(3 0)': (3, 2, 1, 0)}
    all_types = dict(vertex_types)
    all_types.update(edge_types)
    survivors, per_type = [], {}
    tested = 0
    for type_name, pi in all_types.items():
        for clock_signs in product((1, -1), repeat=4):
            R = signed_shift(clock_signs)
            h = 1
            for v in clock_signs:
                h *= v
            Rinv = R.inv()
            for refl_signs in product((1, -1), repeat=4):
                tested += 1
                J = reflection_matrix(pi, refl_signs)
                if J * J != s.eye(4):
                    continue
                if J * R * J != Rinv:
                    continue
                L = R * J
                U = a * s.eye(4) + b * R
                cov_ok = True
                for row in range(4):
                    v = (U * J)[row, :]
                    w = (L * U)[row, :]
                    diff = s.simplify(v.T * v - w.T * w)
                    if not (diff.subs(b, a) == s.zeros(4)
                            and diff.subs(b, -a) == s.zeros(4)):
                        cov_ok = False
                        break
                if not cov_ok:
                    continue
                if (s.eye(4) + R).rank() != 4:
                    continue
                survivors.append({'type': type_name, 'clock': clock_signs,
                                  'refl_signs': refl_signs, 'holonomy': h})
                per_type.setdefault(type_name, []).append((clock_signs, refl_signs))
    need(tested == 4 * 16 * 16, 'S2 exhaustive candidate count 1024')
    need(len(survivors) > 0, 'S2 survivors exist')
    need(all(r['holonomy'] == -1 for r in survivors),
         'S2 every surviving configuration has antiperiodic holonomy')
    # Gauge orbits under diagonal station-sign conjugation R -> D R D,
    # J -> D J D. First confirm the action stays inside the survivor set.
    survivor_keys = {(r['type'], r['clock'], r['refl_signs']) for r in survivors}
    for r in survivors:
        pi = all_types[r['type']]
        for ds in product((1, -1), repeat=4):
            D = s.diag(*ds)
            R2 = D * signed_shift(r['clock']) * D
            J2 = D * reflection_matrix(pi, r['refl_signs']) * D
            c2 = tuple(int(R2[j, (j + 1) % 4]) for j in range(4))
            r2 = tuple(int(J2[pi[j], j]) for j in range(4))
            need((r['type'], c2, r2) in survivor_keys,
                 'S2 diagonal sign conjugation preserves the survivor set')
    seen, orbits = set(), 0
    for r in survivors:
        k0 = (r['type'], r['clock'], r['refl_signs'])
        if k0 in seen:
            continue
        orbits += 1
        pi = all_types[r['type']]
        for ds in product((1, -1), repeat=4):
            D = s.diag(*ds)
            R2 = D * signed_shift(r['clock']) * D
            J2 = D * reflection_matrix(pi, r['refl_signs']) * D
            c2 = tuple(int(R2[j, (j + 1) % 4]) for j in range(4))
            r2 = tuple(int(J2[pi[j], j]) for j in range(4))
            seen.add((r['type'], c2, r2))
    # Negative control: same vertex permutation on the pair banks forces b = 0.
    eta = -1
    R = signed_shift((1, 1, 1, eta))
    J = reflection_matrix((0, 3, 2, 1), (1, eta, eta, eta))
    U = a * s.eye(4) + b * R
    v = (U * J)[0, :]
    w = (J * U)[0, :]
    same_vertex = s.simplify(v.T * v - w.T * w)
    need(same_vertex[3, 3] == b * b,
         'S2 negative control: vertex-on-banks mismatch is b^2, not a^2-b^2')
    need(same_vertex.subs(b, 0) == s.zeros(4),
         'S2 negative control: vertex-on-banks permits only the onsite source')
    # The documented model configuration is among the survivors.
    need(((1, 1, 1, -1), (1, -1, -1, -1)) in per_type.get('(1 3)', []),
         'S2 documented spin-lift configuration is a survivor')
    return {'candidates_tested': tested, 'survivor_count': len(survivors),
            'survivor_holonomies': sorted({r['holonomy'] for r in survivors}),
            'survivors_by_type': {k: len(v) for k, v in per_type.items()},
            'gauge_orbits_under_station_sign': orbits,
            'survivors': [{'type': r['type'], 'clock': r['clock'],
                           'refl_signs': r['refl_signs']} for r in survivors],
            'selection_rule': 'common reflection + pair covariance + no dark mode '
                              '=> antiperiodic holonomy and |a| = |b|'}


# ---------------------------------------------------------------- S3 -------
def native_assignment(survivors):
    """The explicit reflection operator on the native four-bank model."""
    ns = runpy.run_path(str(NATIVE_SOURCE))
    W = ns['W']
    need(sha256(W.tobytes()).hexdigest() == EXPECTED_W_TOBYTES,
         'S3 pinned in-repo native W reproduced')
    pairs = list(combinations(range(64), 2))
    FW = ns['FW']
    # No internal charge-conjugation signed permutation exists on the 64 modes.
    fw_set = {tuple(int(x) for x in row) for row in FW}
    missing = sum(1 for row in fw_set if tuple(-x for x in row) not in fw_set)
    need(missing == 64,
         'S3 internal charge conjugation absent on the native fermion bank')

    def bank_terms(V):
        terms = {}
        for e in range(4):
            support = [x for x in range(4) if V[e, x] != 0]
            for A in range(60):
                d = defaultdict(int)
                for col in np.flatnonzero(W[A]):
                    i, j = pairs[col]
                    wv = int(W[A, col])
                    for x in support:
                        for y in support:
                            aa, bb = 64 * x + i, 64 * y + j
                            key = (aa, bb) if aa < bb else (bb, aa)
                            d[key] += (int(V[e, x]) * int(V[e, y]) * wv
                                       * (1 if aa < bb else -1))
                terms[e, A] = {k: v for k, v in d.items() if v}
        return terms

    def reflect(terms_eA, pi, sigmas):
        out = defaultdict(int)
        for (aa, bb), c in terms_eA.items():
            x, i = divmod(aa, 64)
            y, j = divmod(bb, 64)
            a2, b2 = 64 * pi[x] + i, 64 * pi[y] + j
            c2 = c * sigmas[x] * sigmas[y]
            if a2 > b2:
                a2, b2 = b2, a2
                c2 = -c2
            out[(a2, b2)] += c2
        return {k: v for k, v in out.items() if v}

    # The operator assignment must work for every S2 survivor of the seam's
    # own reflection type (1 3).
    results = []
    tested_pairs = 0
    for r in survivors:
        if r['type'] != '(1 3)':
            continue
        clock, refl = r['clock'], r['refl_signs']
        R = signed_shift(clock)
        J = reflection_matrix((0, 3, 2, 1), refl)
        L = R * J
        V = s.eye(4) + R
        need(V * J == L * V, 'S3 balanced frame covariance V J = L V')
        pi = (0, 3, 2, 1)
        sigmas = [int(J[pi[j], j]) for j in range(4)]
        L_perm = tuple(next(row for row in range(4) if L[row, col] != 0)
                       for col in range(4))
        need(L_perm == (3, 2, 1, 0),
             'S3 bank action is the induced edge permutation (0 3)(1 2)')
        terms = bank_terms(V)
        for e in range(4):
            for A in range(60):
                mapped = reflect(terms[e, A], pi, sigmas)
                need(mapped == terms[L_perm[e], A],
                     'S3 term-level CAR covariance bank %d channel %d' % (e, A))
                tested_pairs += 1
        # Gram-level state compatibility. The physical bank-side operator is
        # the UNSIGNED bank permutation: the pair operators map exactly
        # (P_e -> P_{L(e)}, coefficient +1, checked above), so the bosons are
        # permuted without signs. The frame signs ell_e cancel through
        # V J = L V (ell_e^2 = 1 per bank).
        L_u = s.Matrix(4, 4, lambda u, v: 1 if v < 4 and L_perm[v] == u else 0)
        Sg = V * V.T / 2
        B = 8 * Sg.applyfunc(lambda x: x * x)
        T = s.Matrix(16, 16, lambda u, v:
                     Sg[u // 4, v // 4] * s.conjugate(V[v // 4, u % 4])
                     * V[u // 4, v % 4] / 2)
        need(L_u * B == B * L_u,
             'S3 pair response B invariant under the unsigned bank permutation')
        ST = s.kronecker_product(L_u, J)
        need(ST * T == T * ST,
             'S3 transfer matrix T commutes with the reflection')
        D = s.kronecker_product(B, s.eye(4))
        need(all(ST * (D - k * T) == (D - k * T) * ST
                 for k in (8, 1, -2, -4)),
             'S3 every reduced operator D - kT commutes with the reflection: '
             'all eigenspaces, including the ground eigenspace, are invariant')
        # Stricter optional subclass: the SIGNED L = R J commutes with B only
        # for uniform bank signs (boson-gauge-free configurations).
        signed_B = (L * B == B * L)
        results.append({'clock': clock, 'refl_signs': refl,
                        'signed_bank_operator_commutes_with_B': signed_B})
    need(len(results) > 0, 'S3 at least one native operator assignment')
    strict = sum(1 for r in results if r['signed_bank_operator_commutes_with_B'])
    return {'operator': 'Sigma = signed vertex reflection J on fermion stations '
                        '(x identity on the 64 internal modes) + UNSIGNED bank '
                        'permutation (0 3)(1 2) on the bosonic pair banks',
            'configurations_checked': results,
            'term_level_covariance_pairs': tested_pairs,
            'signed_bank_subclass_count': strict,
            'signed_bank_note': 'signed L commutes with B only for uniform '
                                'bank signs; the physical bosonic reflection '
                                'is unsigned (pair operators map with +1)',
            'internal_part': 'identity on the 64 modes (sufficient, exact)',
            'internal_charge_conjugation_exists': False,
            'ground_eigenspace_invariance_level':
                'exact Gram/reduced-operator commutation'}


# ---------------------------------------------------------------- S4 -------
def toy_state_compatibility():
    """Full-Fock exact check on the 8-mode toy (4 stations x 2 internal)."""
    eta = -1
    R = signed_shift((1, 1, 1, eta))
    J = reflection_matrix((0, 3, 2, 1), (1, eta, eta, eta))
    V = s.eye(4) + R
    pi = (0, 3, 2, 1)
    sigmas = [int(J[pi[j], j]) for j in range(4)]
    # Toy pair terms: one internal antisymmetric channel, modes 2x and 2y+1.
    bank_terms = []
    for e in range(4):
        support = [x for x in range(4) if V[e, x] != 0]
        terms = defaultdict(int)
        for x in support:
            for y in support:
                aa, bb = 2 * x, 2 * y + 1
                key = (aa, bb) if aa < bb else (bb, aa)
                terms[key] += int(V[e, x]) * int(V[e, y]) * (1 if aa < bb else -1)
        bank_terms.append({k: v for k, v in terms.items() if v})

    def annihilate(mask, j):
        if not (mask >> j) & 1:
            return None
        return (mask ^ (1 << j),
                (-1) ** ((mask & ((1 << j) - 1)).bit_count()))

    def pair_remove(mask, pair):
        i, j = pair
        one = annihilate(mask, i)
        if one is None:
            return None
        two = annihilate(one[0], j)
        if two is None:
            return None
        return two[0], one[1] * two[1]

    dim = 1 << 8
    Q = csr_matrix((dim, dim), dtype=np.int64)
    for terms in bank_terms:
        rr, cc, vv = [], [], []
        for mask in range(dim):
            for pair, c in terms.items():
                out = pair_remove(mask, pair)
                if out is not None:
                    rr.append(out[0])
                    cc.append(mask)
                    vv.append(out[1] * c)
        Pe = coo_matrix((np.array(vv, dtype=np.int64), (rr, cc)),
                        shape=(dim, dim)).tocsr()
        Q = Q + Pe.T @ Pe
    Q = Q.tocsr()

    # Fock lift of the signed station permutation (internal modes untouched).
    def fock_reflection():
        rr, cc, vv = [], [], []
        for mask in range(dim):
            image, sign, bits = 0, 1, []
            for j in range(8):
                if (mask >> j) & 1:
                    x, r = divmod(j, 2)
                    j2 = 2 * pi[x] + r
                    image |= 1 << j2
                    sign *= sigmas[x]
                    bits.append(j2)
            inv = sum(1 for u in range(len(bits))
                      for v in range(u + 1, len(bits)) if bits[u] > bits[v])
            rr.append(image)
            cc.append(mask)
            vv.append(sign * ((-1) ** inv))
        return coo_matrix((np.array(vv, dtype=np.int64), (rr, cc)),
                          shape=(dim, dim)).tocsr()

    US = fock_reflection()
    diff = (US @ US.T - speye(dim, dtype=np.int64, format='csr')).tocsr()
    diff.eliminate_zeros()
    need(diff.nnz == 0, 'S4 Fock reflection is orthogonal')
    comm = (US @ Q - Q @ US).tocsr()
    comm.eliminate_zeros()
    need(comm.nnz == 0, 'S4 [U_Sigma, Q] = 0 on the full 256-dim toy Fock space')
    sq = (US @ US - speye(dim, dtype=np.int64, format='csr')).tocsr()
    sq.eliminate_zeros()
    need(sq.nnz == 0, 'S4 U_Sigma^2 = I on the full toy Fock space')
    filled = dim - 1
    col = US[:, filled].toarray().ravel()
    need(all(int(col[m]) == 0 for m in range(dim) if m != filled),
         'S4 filled state is a reflection eigenstate')
    filled_eigenvalue = int(col[filled])
    need(filled_eigenvalue in (1, -1), 'S4 filled-state eigenvalue is +/-1')
    # One-hole sector commutation (8 x 8 exact).
    holes = [filled ^ (1 << r) for r in range(8)]
    Qh = Q[np.ix_(holes, holes)].toarray()
    USh = US[np.ix_(holes, holes)].toarray()
    need(np.array_equal(USh @ Qh, Qh @ USh),
         'S4 one-hole sector commutes with the reflection')
    return {'fock_dimension': dim, 'filled_state_eigenvalue': filled_eigenvalue,
            'commutator_exact_zero': True,
            'uniqueness_source': 'analytic small-coupling theorem of the '
                                 'spin-lift package (cited, not reproved here); '
                                 'a unique ground of a symmetric H is invariant'}


# ---------------------------------------------------------------- S5 -------
def scaling_probe():
    """Dark-mode rank rule for growing cycles and the charged-band shape."""
    # Exact determinant identity det(I + R) = 1 - (-1)^n * holonomy.
    for n in range(3, 9):
        syms = s.symbols('s0:%d' % n)
        Rn = s.Matrix(n, n, lambda j, k: syms[j] if k == (j + 1) % n else 0)
        h = 1
        for v in syms:
            h *= v
        need(s.simplify((s.eye(n) + Rn).det() - (1 - (-1)**n * h)) == 0,
             'S5 symbolic determinant identity n=%d' % n)
    rng = np.random.default_rng(20260915)
    for n in (10, 12, 16):
        for _ in range(40):
            signs = [int(v) for v in rng.choice((-1, 1), size=n)]
            Rn = s.Matrix(n, n, lambda j, k: signs[j] if k == (j + 1) % n else 0)
            h = 1
            for v in signs:
                h *= v
            need(int((s.eye(n) + Rn).det()) == 1 - (-1)**n * h,
                 'S5 sampled exact determinant identity n=%d' % n)
    # Nullity exactly one in the deficient case, exhaustive for n <= 8.
    for n in range(3, 9):
        for signs in product((1, -1), repeat=n):
            h = 1
            for v in signs:
                h *= v
            if h != (-1)**n:
                continue
            Rn = signed_shift(signs)
            need((s.eye(n) + Rn).rank() == n - 1,
                 'S5 deficient cycle has exactly one dark mode n=%d' % n)
    # Charged N2-chain band versus relativistic dispersion through O(k^6).
    k, g, D = s.symbols('k g Delta', positive=True)
    Bk = 8 + 4 * s.cos(k)
    Eminus = (D - s.sqrt(D**2 + 4 * g**2 * Bk)) / 2
    eps = Eminus - Eminus.subs(k, 0)
    ser = s.series(eps, k, 0, 7).removeO().expand()
    e2 = s.simplify(ser.coeff(k, 2))
    e4 = s.simplify(ser.coeff(k, 4))
    e6 = s.simplify(ser.coeff(k, 6))
    need(e2 == 2 * g**2 / s.sqrt(D**2 + 48 * g**2),
         'S5 quadratic coefficient matches the documented N2-chain value')
    # Relativistic form sqrt(m^2 + c^2 k^2) - m predicts e6* = 2 e4^2 / e2.
    e6_star = s.simplify(2 * e4**2 / e2)
    R6 = s.simplify(e6 - e6_star)
    need(e2 != 0 and e4 != 0, 'S5 band coefficients nonzero')
    need(R6 != 0, 'S5 the band is not exactly relativistic: O(k^6) residual')
    R6_lead = s.simplify(s.series(R6, g, 0, 8).removeO())
    return {'dark_mode_rule': 'no dark mode <=> holonomy = -(-1)^n '
                              '(antiperiodic exactly for even cycles)',
            'deficient_nullity': 'exactly 1 (exhaustive n <= 8)',
            'band_proxy': 'N2-chain band B(k) = 8 + 4 cos k; labelled proxy, '
                          'not the certified dispersion above the full ground',
            'band_e2': str(e2), 'band_e4': str(e4), 'band_e6': str(e6),
            'relativistic_prediction_e6': str(e6_star),
            'relativistic_residual_R6': str(R6),
            'R6_leading_in_g': str(R6_lead),
            'antiperiodic_momentum_grid': 'k_m = 2 pi (m + 1/2) / n at every size',
            'relativistic_at_growing_size': 'open; exact O(k^6) deviation recorded'}


def main():
    s1 = seam_skeleton()
    s2 = enumeration()
    s3 = native_assignment(s2['survivors'])
    s4 = toy_state_compatibility()
    s5 = scaling_probe()
    return {'status': 'PASS', 'contract': 'seam-reflection-operator-20260915',
            'exact_checks': len(CHECKS), 'checks': CHECKS,
            'S1_seam_skeleton': s1, 'S2_enumeration': s2,
            'S3_native_operator_assignment': s3,
            'S4_toy_state_compatibility': s4, 'S5_scaling_probe': s5,
            'verdict': 'conditional_structural_match: the marked seam carries '
                       'exactly the vertex/edge reflection pair the model '
                       'selects; the spinorial sign is fixed by the '
                       'no-dark-mode condition; raw-seam operator production '
                       '(QGEO.MARKS.01 / QGEO.KERNEL.01) remains open',
            'not_derived': ['raw seam -> marked boundary (QGEO.MARKS.01)',
                            'raw seam kernel operator identity (QGEO.KERNEL.01)',
                            'spinorial sign from raw seam geometry',
                            'physical coupling g/Delta',
                            '3+1D common origin, chiral measure, spin-2 sector'],
            'T1_T8_closed': [],
            'runtime_seconds': round(time.time() - T0, 3)}


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, sort_keys=True, default=str))
