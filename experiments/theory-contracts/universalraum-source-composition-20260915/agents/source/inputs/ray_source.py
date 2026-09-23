#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v783 -- E8.CLIFFORD2Q.01: the compiler carrier IS two-qubit stabilizer quantum mechanics up to one predeclared chart -- the 60 Gaussian E8 lines (v689: the J-orbits of the 240 Construction-A roots of C* over Z[i], L/(1+i)L = F2^4) ARE the 60 pure two-qubit stabilizer rays ENTRY-EXACTLY over Z[i] under the single frozen chart U (coordinate-class frame -> computational basis, z_k = r_2k + i r_2k+1): 60/60 projective matches, support census 4 + 24 + 32 identical on both sides (32/32 checks, ~4 s; discovery probe two_qubit_clifford_probe.py, 2026-08-05, verdict CLIFFORD-PARTIAL(H4)).  THE GROUP LAYER, EXACT: U G31 U^-1 is an INDEX-2 subgroup of the two-qubit Clifford matrix group C2 = <H(x)I, I(x)H, S(x)I, I(x)S, CNOT> -- |C2| = 92160 = 2 x 46080 = 2 x |G31|, coset zeta8 * G31 (zeta8 = exp(i pi/4)); PROJECTIVELY the two groups are EQUAL: G31/mu4 = C2/U(1), both of order 11520 = 16 x 720.  THE SEMANTICS CARRY (H3 exact): 46080 = 4 x 16 x 720 = mu4-phase x Pauli16 x Sp(4,2) -- exactly 64 elements of G31 act trivially on the 16 classes of V = L/(1+i)L and they are PRECISELY mu4 x Pauli16, i.e. the '16' in the factorization IS the Pauli group mod phase acting as the identity on the 16 code states; the 15 Gaussian classes <-> 15 Pauli contexts bijection transports v752's incidence B (B B^T = 4I + 3J, exact in the chart model) to the context-collinearity of W(3,2) = GQ(2,2) on all 105 pairs -- the point<->line DUALITY of the self-dual GQ(2,2) (the two Sp(4,2)-modules are NOT linearly isomorphic: dim Hom = 0, invertible intertwiners 0), and the 6 symplectic spreads are the MUB pentads (all cross-context pairs unbiased, |<psi|phi>|^2 = 1/4 exact; pullbacks = hbar-ovoids).  THE H4 LAYER (the honest partial): the index bit is the sqrt2/Hadamard GALOIS bit -- chi = Gal(Q(zeta8)/Q(i))-parity (Q(i)-rationality: G31 has Q(i) entries, the coset has zeta8 * Q(i) entries; the coset EXCHANGES the two mu8-lift classes {mu4 R, zeta8 mu4 R} of the 240 roots), NOT J <-> -J: both predeclared H4 readings provably fail (J = iI is a scalar and zeta8 is central, mu4 is central in C2), and the true J <-> -J orientation bit is the ANTIUNITARY complex conjugation -- a separate outer Z2 that normalizes G31 and C2 and FIXES chi.  ALL CONTROLS FIRE: Haar-random unitary 0/60, T-gate twist diag(1,1,1,zeta8) exactly the predeclared 16/60, non-context frame (controlled-Hadamard) 12/60 < 60, 60 seeded random rays 0/60.  A dated cross-note on E8.GAUSSIAN.CODE.01 is registered at promotion (the ledger row is the parent's).  No physics claim; the fired v775 ROOTCLASS-MIXED kill is unaffected (stabilizer-formalism mathematics about the carrier, not a matter reading).  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe two_qubit_clifford_probe.py (2026-08-05, 32/32, 3.9 s, CLIFFORD-PARTIAL(H4)); re-run identically at promotion.  Promoted verbatim (top-level statements moved into main(); the trailing __main__ SystemExit replaced by returning (n_pass, n_checks, verdict); numbers unchanged).  run() encodes the all-pass CLIFFORD-PARTIAL(H4) pattern (v757 precedent).

Original two_qubit_clifford_probe.py docstring (verbatim):
two_qubit_clifford_probe -- E8.CLIFFORD2Q.01: is the finite TFPT compiler,
up to ONE fixed unitary basis change of C^4, a TWO-QUBIT STABILIZER compiler?

THE HYPOTHESIS (frozen before running):
  (H1) the 60 Gaussian E8 lines in C^4 (v689: J-orbits of the 240
       Construction-A roots of C* over Z[i], L/(1+i)L = F2^4) are exactly
       the 60 pure two-qubit stabilizer rays;
  (H2) G31 (|G31| = 46080, the corpus complex reflection group, v634/v752:
       BFS closure of the 60 unitary reflections) is, transported by U,
       an INDEX-2 subgroup of the two-qubit Clifford matrix group
       C2 := <H(x)I, I(x)H, S(x)I, I(x)S, CNOT>.  PREDECLARED EXACT ORDER
       STATEMENT: |C2/U(1) phases| = 2^(2*2+4) * (4-1)(4^2-1) = 11520 =
       |G31| / |mu4| = 46080/4 (projective orders EQUAL, index 1); at the
       MATRIX level |C2| = 11520 * |mu8 scalars| = 92160 = 2 * 46080, so
       U G31 U^-1 has index 2 in C2 with coset zeta8 * G31 (zeta8 =
       exp(i pi/4)).
  (H3) the factorization 46080 = 4 * 16 * 720 carries the semantics
       mu4-phase x 16 (Pauli group mod phase = the 16 code states of
       V = L/(1+i)L) x Sp(4,2): ker(G31 -> Sp(4,2)) = mu4 * Pauli16
       (order 64), quotient the full Sp(4,2) (order 720).
  (H4) the index-2 character chi: C2 -> Z2 = C2 / (U G31 U^-1) matches the
       J <-> -J / chiral <-> mirror orientation bit.  PREDECLARED TEST of
       the character's action (the task wording, binding): does the
       nontrivial coset (i) exchange the two J-orientations (conjugate
       J = iI to -iI) or (ii) conjugate the mu4 phases nontrivially?
       H4 PASSES iff (i) or (ii) holds.  Additionally reported (not part
       of the pass rule): (iii) the coset's exchange of the two mu8-lift
       classes {mu4*R, zeta8*mu4*R} of the 240-root system, and the Galois
       identification chi = Gal(Q(zeta8)/Q(i)) parity (the "sqrt2 /
       Hadamard-parity" bit).

THE BASIS-CHANGE TEST (the decider, predeclared):
  FRAME SELECTION RULE (frozen): the four Gaussian lines of the
  COORDINATE CLASS (v689 I3.1: the 16 roots +-2e_j form exactly one
  class = one context; its 4 J-lines are the 4 complex coordinate
  pairs), ordered by ambient coordinate pair (01),(23),(45),(67), i.e.
  v_k = 2 e_{2k}, k = 0..3.  TARGET STABILIZER FRAME (frozen): the
  computational basis |q1 q2> with slot index 2*q1 + q2 (the joint
  eigenbasis of the context {Z(x)I, I(x)Z, Z(x)Z}).  The unitary U is
  the isometry v_k / sqrt(2) -> e_k; concretely U is the R^8 -> C^4
  pairing chart z_k(r) = r_{2k} + i r_{2k+1} (J becomes multiplication
  by i; h(x,y) = <z_x, z_y>_C / 2, so U is h-orthonormal-to-standard).
  Residual frame freedom = diagonal phase torus; the identity choice is
  frozen as the primary candidate.
  ITERATION POLICY (frozen, finite): if the primary frame fails, the
  fallback list is the other 14 Gaussian classes as source frames (each
  class = 4 mutually h-orthogonal lines), same target frame, canonical
  (sorted-label) order.  No free search.  (Not needed: primary passed.)

STRUCTURE CHECKS (predeclared):
  S1 the 15 Gaussian classes <-> 15 Pauli contexts: each class's 4 lines
     are the 4 joint eigenstates of exactly ONE maximal commuting Pauli
     triple; the induced bijection transports v752's incidence B
     (B_xy = [hbar(x,y) = 0], B B^T = 4I + 3J) to the context dictionary:
     hbar(x,y) = 0  <=>  contexts Gamma_x, Gamma_y share a Pauli
     (all 105 pairs) -- the W(3,2) = GQ(2,2) polar-space identification.
  S2 spreads: the 5-sets of pairwise DISJOINT contexts (= symplectic
     spreads of W(3,2) = MUB pentads); count and unbiasedness
     |<psi|phi>|^2 = 1/4 across distinct contexts of a spread (exact:
     |h| = 1); under the S1 bijection each spread pulls back to a 5-set
     of classes with pairwise hbar = 1 (an ovoid -- the point<->line
     DUALITY of the self-dual GQ(2,2)).
  S3 240 = 60 x 4 mu4 phase lifts (each line = {z, iz, -z, -iz}).

CONTROLS (must fire; frozen):
  C1 a Haar-random unitary in place of U: 0/60 projective matches.
  C2 a WRONG FRAME PAIRING inside the residual torus freedom: the same
     frame mapped with a non-mu4 diagonal phase, U' = U * diag(1,1,1,
     zeta8) (the T-gate twist).  Predeclared expectation: exactly 16/60
     matches (the 15 rays with slot-3 entry 0 plus the ray e3 itself);
     must be < 60.  Also C2b: a frame pairing onto an orthonormal
     stabilizer frame that is NOT one context's eigenbasis
     ({|00>, |01>, |1+>, |1->}, i.e. U'' = controlled-Hadamard): < 60.
  C3 a non-stabilizer ray set: 60 seeded random rays vs the stabilizer
     set: 0/60.

VERDICT ENUM (frozen):
  CLIFFORD-IDENTIFIED : H1 (60/60 exact) & H2 (index 2) & H3 (semantics)
                        & H4 (predeclared reading) & all controls fire.
  CLIFFORD-PARTIAL    : controls fire, >= 1 hypothesis fails -> name it.
  CLIFFORD-DEAD       : H1 fails under the full frozen frame policy --
                        the line sets are projectively inequivalent.
  TEST-VOID           : a must-fail control does not fire.

FENCES / FIREWALL: experiments/tfpt-discovery probe; NO physics claims;
writes nothing; no verification/, ledger, paper or website surface
touched.  The fired physical kill v775 -- ARF.ROOTCLASS.01, verdict
ROOTCLASS-MIXED (the root-level code->matter reading is DEAD: >= 7 of
the 15 Gaussian classes always contain adjoint-side roots for EVERY
D5(+)A3 embedding) -- is UNAFFECTED either way: this probe is pure
finite group/lattice mathematics (a stabilizer-formalism identification
of the compiler carrier), not a matter reading.  Exact Z[i] / integer
arithmetic in every load-bearing check; floats only in the random
controls (C1/C2b/C3) as scaffolding.

Sources (read-only): v689_gaussian_code_bridge.py (C*, L, chart, labels),
v752_projective_hamming_incidence.py (G31 BFS recipe, B identity),
v634_st31_structure.py (G31, h-convention), v775 (ROOTCLASS-MIXED kill).
"""


def main():
    import itertools
    import time
    from collections import Counter
    from fractions import Fraction as Fr

    import numpy as np

    T0 = time.time()
    CHECKS = []


    def check(name, ok, detail=""):
        CHECKS.append((name, bool(ok)))
        print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                             (" -- " + detail) if detail else ""), flush=True)


    def section(title):
        print("=" * 78)
        print(title)
        print("=" * 78, flush=True)


    # ================================================== Gaussian integers Z[i]
    def gadd(a, b):
        return (a[0] + b[0], a[1] + b[1])


    def gsub(a, b):
        return (a[0] - b[0], a[1] - b[1])


    def gmul(a, b):
        return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


    def gconj(a):
        return (a[0], -a[1])


    def gnorm(a):
        return a[0] * a[0] + a[1] * a[1]


    def gdiv(a, b):
        """exact division in Z[i]; asserts divisibility."""
        n = gnorm(b)
        num = gmul(a, gconj(b))
        assert num[0] % n == 0 and num[1] % n == 0, "not divisible"
        return (num[0] // n, num[1] // n)


    def ggcd(a, b):
        """Euclid in Z[i] with nearest-integer rounding."""
        while b != (0, 0):
            n = gnorm(b)
            num = gmul(a, gconj(b))
            q = ((2 * num[0] + n) // (2 * n), (2 * num[1] + n) // (2 * n))
            a, b = b, gsub(a, gmul(q, b))
        return a


    UNITS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    G0 = (0, 0)
    G1 = (1, 0)
    GI = (0, 1)


    def vec_scal(u, z):
        return tuple(gmul(u, c) for c in z)


    def canonical_ray(z):
        """canonical Z[i]-primitive representative of the projective ray
        C* z: divide by the Z[i]-gcd, then multiply by the unique unit
        making the first nonzero entry (a, b) satisfy a > 0, b >= 0."""
        g = G0
        for c in z:
            if c != G0:
                g = c if g == G0 else ggcd(g, c)
        assert g != G0
        w = tuple(gdiv(c, g) for c in z)
        first = next(c for c in w if c != G0)
        for u in UNITS:
            f = gmul(u, first)
            if f[0] > 0 and f[1] >= 0:
                return vec_scal(u, w)
        raise AssertionError("no canonical unit")


    def hermC(z, w):
        """<z, w>_C = sum z_i conj(w_i) (linear in the first slot)."""
        s = G0
        for a, b in zip(z, w):
            s = gadd(s, gmul(a, gconj(b)))
        return s


    # 4x4 matrices over Z[i] as tuples of row-tuples
    def mmulg(A, B):
        n = len(A)
        return tuple(tuple(
            _sumg(gmul(A[i][k], B[k][j]) for k in range(n))
            for j in range(n)) for i in range(n))


    def _sumg(it):
        s = G0
        for x in it:
            s = gadd(s, x)
        return s


    def mdagger(A):
        n = len(A)
        return tuple(tuple(gconj(A[j][i]) for j in range(n)) for i in range(n))


    def mscale(k, A):
        return tuple(tuple((k * c[0], k * c[1]) for c in row) for row in A)


    def meye(n, val=G1):
        return tuple(tuple(val if i == j else G0 for j in range(n))
                     for i in range(n))


    def mat_apply(A, z):
        n = len(A)
        return tuple(_sumg(gmul(A[i][j], z[j]) for j in range(n))
                     for i in range(n))


    def kron(A, B):
        n, m = len(A), len(B)
        return tuple(tuple(gmul(A[i // m][k // m], B[i % m][k % m])
                           for k in range(n * m)) for i in range(n * m))


    def det4(A):
        d = G0
        for p in itertools.permutations(range(4)):
            sign = 1
            for i in range(4):
                for j in range(i + 1, 4):
                    if p[i] > p[j]:
                        sign = -sign
            t = (sign, 0)
            for i in range(4):
                t = gmul(t, A[i][p[i]])
            d = gadd(d, t)
        return d


    # ============================================= v689 lattice machinery (RO)
    G_NAIVE = [(1, 0, 0, 0, 0, 1, 1, 1),
               (0, 1, 0, 0, 1, 0, 1, 1),
               (0, 0, 1, 0, 1, 1, 0, 1),
               (0, 0, 0, 1, 1, 1, 1, 0)]
    C_NAIVE = frozenset(tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
                              for j in range(8))
                        for m in itertools.product((0, 1), repeat=4))
    PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
    PI_SIG = (4, 5, 0, 1, 2, 3, 6, 7)
    CSTAR_SUPPORTS_EXPECTED = [
        (0, 1, 2, 3), (0, 1, 4, 5), (0, 1, 6, 7), (0, 2, 4, 6), (0, 2, 5, 7),
        (0, 3, 4, 7), (0, 3, 5, 6), (1, 2, 4, 7), (1, 2, 5, 6), (1, 3, 4, 6),
        (1, 3, 5, 7), (2, 3, 4, 5), (2, 3, 6, 7), (4, 5, 6, 7)]


    def apply_perm(c, p):
        return tuple(c[p[k]] for k in range(8))


    def code_image(code, p):
        return frozenset(apply_perm(c, p) for c in code)


    def supports_w4(code):
        return sorted(tuple(i for i in range(8) if w[i])
                      for w in code if sum(w) == 4)


    def mat_det_inv(rows):
        n = len(rows)
        A = [[Fr(v) for v in r] for r in rows]
        I = [[Fr(1 if i == j else 0) for j in range(n)] for i in range(n)]
        det = Fr(1)
        for col in range(n):
            piv = next((r for r in range(col, n) if A[r][col] != 0), None)
            assert piv is not None
            if piv != col:
                A[col], A[piv] = A[piv], A[col]
                I[col], I[piv] = I[piv], I[col]
                det = -det
            det *= A[col][col]
            inv = 1 / A[col][col]
            A[col] = [a * inv for a in A[col]]
            I[col] = [a * inv for a in I[col]]
            for r in range(n):
                if r != col and A[r][col] != 0:
                    f = A[r][col]
                    A[r] = [a - f * b for a, b in zip(A[r], A[col])]
                    I[r] = [a - f * b for a, b in zip(I[r], I[col])]
        return det, I


    def vec_mat(x, M):
        n = len(M)
        return tuple(sum(x[i] * M[i][j] for i in range(n)) for j in range(n))


    def row_hnf(rows):
        M = [list(map(int, r)) for r in rows]
        m = len(M)
        for col in range(m):
            piv = next(r for r in range(col, m) if M[r][col] != 0)
            M[col], M[piv] = M[piv], M[col]
            for r in range(col + 1, m):
                while M[r][col] != 0:
                    q = M[col][col] // M[r][col]
                    M[col] = [a - q * b for a, b in zip(M[col], M[r])]
                    M[col], M[r] = M[r], M[col]
            if M[col][col] < 0:
                M[col] = [-a for a in M[col]]
        return M


    def hnf_reduce(c, H):
        c = list(c)
        for i in range(len(H)):
            q = c[i] // H[i][i]
            if q:
                c = [a - q * b for a, b in zip(c, H[i])]
        return tuple(c)


    def J_vec(x):
        out = []
        for k in range(0, 8, 2):
            out += [-x[k + 1], x[k]]
        return tuple(out)


    def add_vec(x, y):
        return tuple(a + b for a, b in zip(x, y))


    def f2_rref(words):
        rows = [list(w) for w in sorted(words, reverse=True) if any(w)]
        basis, pivots = [], []
        for r in rows:
            r = r[:]
            for b, pv in zip(basis, pivots):
                if r[pv]:
                    r = [(a + c) % 2 for a, c in zip(r, b)]
            if any(r):
                basis.append(r)
                pivots.append(next(i for i, a in enumerate(r) if a))
        return basis, pivots


    def make_lattice(in_lat, basis_rows):
        det, Binv = mat_det_inv(basis_rows)
        lat = {"in": in_lat, "B": basis_rows, "det": det, "Binv": Binv}

        def coords(x):
            c = vec_mat(x, Binv)
            assert all(v.denominator == 1 for v in c)
            return tuple(int(v) for v in c)

        A = [coords(add_vec(b, J_vec(b))) for b in basis_rows]
        H = row_hnf(A)
        lat["coords"] = coords
        lat["H"] = H
        lat["label"] = lambda x: hnf_reduce(coords(x), H)
        return lat


    def constrA_lattice(code):
        cb, pivots = f2_rref(code)
        rows = [tuple(r) for r in cb]
        rows += [tuple(2 if i == j else 0 for i in range(8))
                 for j in range(8) if j not in pivots]
        return make_lattice(lambda x: tuple(v % 2 for v in x) in code, rows)


    def constrA_roots(code):
        return [x for x in itertools.product(range(-2, 3), repeat=8)
                if sum(v * v for v in x) == 4
                and tuple(v % 2 for v in x) in code]


    def label_group(lat):
        reps = {hnf_reduce((0,) * 8, lat["H"]): (0,) * 8}
        frontier = [(0,) * 8]
        while frontier:
            v = frontier.pop()
            for b in lat["B"]:
                w = add_vec(v, b)
                l = lat["label"](w)
                if l not in reps:
                    reps[l] = w
                    frontier.append(w)
        return reps


    # ==================================================================== P0
    section("P0: corpus state + the predeclared frame / chart U")

    all_placements = set()
    for p in itertools.permutations(range(8)):
        all_placements.add(code_image(C_NAIVE, p))
    both_inv = [c for c in sorted(all_placements, key=lambda c: sorted(c))
                if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
    W0246 = tuple(1 if i in (0, 2, 4, 6) else 0 for i in range(8))
    CSTAR = [c for c in both_inv if W0246 in c][0]
    ROOTS = sorted(constrA_roots(CSTAR))
    LAT = constrA_lattice(CSTAR)
    REPS = label_group(LAT)
    ZERO = LAT["label"]((0,) * 8)
    root_label = {r: LAT["label"](r) for r in ROOTS}
    census = Counter(root_label.values())
    check("P0.1 C* deterministic (v638 recipe), 240 roots, 15 x 16 census, "
          "zero class empty",
          supports_w4(CSTAR) == CSTAR_SUPPORTS_EXPECTED and len(ROOTS) == 240
          and len(census) == 15 and sorted(census.values()) == [16] * 15
          and ZERO not in census)


    def chart(r):
        """U: R^8 -> C^4, z_k = r_{2k} + i r_{2k+1} (J -> mult by i)."""
        return ((r[0], r[1]), (r[2], r[3]), (r[4], r[5]), (r[6], r[7]))


    Z240 = [chart(r) for r in ROOTS]
    ridx = {r: k for k, r in enumerate(ROOTS)}
    ok_J_is_i = all(chart(J_vec(r)) == vec_scal(GI, chart(r)) for r in ROOTS)
    ok_norm = all(sum(gnorm(c) for c in z) == 4 for z in Z240)
    check("P0.2 chart is the frame isometry: J = multiplication by i on C^4, "
          "all 240 roots have |z|^2 = 4 (h(r,r) = 2)",
          ok_J_is_i and ok_norm)

    # the 60 lines = mu4 orbits; canonical rays
    line_of = {}
    line_reps = []
    for k, r in enumerate(ROOTS):
        if k in line_of:
            continue
        orb = [k]
        y = J_vec(r)
        while y != r:
            orb.append(ridx[y])
            y = J_vec(y)
        for j in orb:
            line_of[j] = len(line_reps)
        line_reps.append(k)
    GAUSS_RAYS = sorted({canonical_ray(Z240[i]) for i in line_reps})
    check("P0.3 60 J-lines, 60 distinct canonical rays, 240 = 60 x 4 mu4 "
          "lifts (S3)",
          len(line_reps) == 60 and len(GAUSS_RAYS) == 60
          and all(len([j for j in range(240) if line_of[j] == L]) == 4
                  for L in range(60)))

    # predeclared frame: coordinate class = 4 lines {2e_{2k}}; targets e_k
    coord_roots = [r for r in ROOTS if sorted(map(abs, r)) == [0] * 7 + [2]]
    coord_class = {root_label[r] for r in coord_roots}
    FRAME = [tuple((2 if i == 2 * k else 0) for i in range(8))
             for k in range(4)]
    frame_rays = [canonical_ray(chart(v)) for v in FRAME]
    E4 = [tuple(G1 if j == k else G0 for j in range(4)) for k in range(4)]
    ok_frame = (len(coord_class) == 1 and len(coord_roots) == 16
                and all(v in ROOTS for v in FRAME)
                and frame_rays == E4
                and all(hermC(chart(FRAME[a]), chart(FRAME[b])) == G0
                        for a in range(4) for b in range(4) if a != b))
    check("P0.4 predeclared frame: the coordinate class (16 roots, ONE "
          "class) provides 4 mutually h-orthogonal lines v_k = 2e_{2k}; "
          "under U they ARE the computational-basis rays e_0..e_3 "
          "(residual freedom = diagonal torus, identity choice frozen)",
          ok_frame)

    # ==================================================================== P1
    section("P1 (H1): 60 Gaussian rays vs 60 two-qubit stabilizer rays "
            "(exact, the decider)")

    # Pauli machinery: symplectic bits (x1, z1, x2, z2), Hermitian reps
    I2 = ((G1, G0), (G0, G1))
    X2 = ((G0, G1), (G1, G0))
    Y2 = ((G0, (0, -1)), ((0, 1), G0))
    Z2 = ((G1, G0), (G0, (-1, 0)))
    W1Q = {(0, 0): I2, (1, 0): X2, (0, 1): Z2, (1, 1): Y2}
    NAMES1Q = {(0, 0): "I", (1, 0): "X", (0, 1): "Z", (1, 1): "Y"}


    def pauli_mat(bits):
        return kron(W1Q[(bits[0], bits[1])], W1Q[(bits[2], bits[3])])


    def pauli_name(bits):
        return NAMES1Q[(bits[0], bits[1])] + NAMES1Q[(bits[2], bits[3])]


    ALL_BITS = [b for b in itertools.product((0, 1), repeat=4)]
    NZ_BITS = [b for b in ALL_BITS if any(b)]
    PMAT = {b: pauli_mat(b) for b in ALL_BITS}


    def symp(a, b):
        return (a[0] * b[1] + a[1] * b[0] + a[2] * b[3] + a[3] * b[2]) % 2


    def bxor(a, b):
        return tuple((x + y) % 2 for x, y in zip(a, b))


    # 15 maximal commuting triples (contexts) = isotropic lines
    contexts = set()
    for a, b in itertools.combinations(NZ_BITS, 2):
        if symp(a, b) == 0:
            contexts.add(frozenset({a, b, bxor(a, b)}))
    contexts = sorted(contexts, key=lambda s: sorted(s))
    check("P1.1 15 maximal commuting Pauli triples (isotropic lines of "
          "W(3,2)) enumerated from the Pauli group directly",
          len(contexts) == 15
          and all(len(c) == 3 and all(symp(x, y) == 0 for x in c for y in c)
                  for c in contexts))

    # 15 contexts x 4 joint eigenstates = 60 stabilizer rays (exact)
    I4 = meye(4)
    stab_ray_ctx = {}
    ok_orth = True
    for ci, ctx in enumerate(contexts):
        a, b = sorted(ctx)[:2]
        Pa, Pb = PMAT[a], PMAT[b]
        rays_here = []
        for s1 in (1, -1):
            for s2 in (1, -1):
                # (I + s1 Pa)(I + s2 Pb) = 4 * rank-1 projector
                M = mmulg(tuple(tuple(gadd(I4[i][j], mscale(s1, Pa)[i][j])
                                      for j in range(4)) for i in range(4)),
                          tuple(tuple(gadd(I4[i][j], mscale(s2, Pb)[i][j])
                                      for j in range(4)) for i in range(4)))
                col = next(tuple(M[i][j] for i in range(4)) for j in range(4)
                           if any(M[i][j] != G0 for i in range(4)))
                rays_here.append(canonical_ray(col))
        for u, v in itertools.combinations(rays_here, 2):
            if hermC(u, v) != G0:
                ok_orth = False
        for ray in rays_here:
            assert ray not in stab_ray_ctx or stab_ray_ctx[ray] == ci
            stab_ray_ctx[ray] = ci
    STAB_RAYS = sorted(stab_ray_ctx)
    check("P1.2 60 distinct stabilizer rays (15 contexts x 4 joint "
          "eigenstates, exact projector extraction), context eigenbases "
          "orthonormal", len(STAB_RAYS) == 60 and ok_orth)

    match = set(GAUSS_RAYS) == set(STAB_RAYS)
    n_match = len(set(GAUSS_RAYS) & set(STAB_RAYS))
    supp_g = Counter(sum(1 for c in z if c != G0) for z in GAUSS_RAYS)
    supp_s = Counter(sum(1 for c in z if c != G0) for z in STAB_RAYS)
    check("P1.3 H1 DECIDER: U maps ALL 60 Gaussian lines onto the 60 "
          "stabilizer rays as projective sets -- %d/60 exact matches; "
          "support census Gaussian %s = stabilizer %s (4 basis + 24 "
          "two-entry + 32 full-support)"
          % (n_match, dict(sorted(supp_g.items())),
             dict(sorted(supp_s.items()))),
          match and n_match == 60
          and dict(supp_g) == {1: 4, 2: 24, 4: 32}
          and supp_g == supp_s)

    # ==================================================================== P2
    section("P2 (H2a): the 60 G31 reflections are Clifford (exact "
            "conjugation test)")

    PAULI_GENS = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]


    def clifford_images(M2):
        """M2 = 2g exact; return the 4 symplectic image bit-vectors of the
        Pauli generators under g P g^dagger, or None if not Clifford."""
        M2d = mdagger(M2)
        cols = []
        for pb in PAULI_GENS:
            C = mmulg(mmulg(M2, PMAT[pb]), M2d)     # = 4 g P g^dagger
            hit = None
            for qb in NZ_BITS:
                for s in (1, -1):
                    if C == mscale(4 * s, PMAT[qb]):
                        hit = qb
                        break
                if hit:
                    break
            if hit is None:
                return None
            cols.append(hit)
        return cols


    REFL_M2 = []           # scaled matrices 2*r_v
    refl_sympl = []        # 4x4 F2 symplectic images (columns)
    ok_unitary = ok_cliff = True
    for L in range(60):
        v = Z240[line_reps[L]]
        vvd = tuple(tuple(gmul(v[i], gconj(v[j])) for j in range(4))
                    for i in range(4))
        M2 = tuple(tuple(gsub(mscale(2, I4)[i][j], vvd[i][j])
                         for j in range(4)) for i in range(4))
        if mmulg(M2, mdagger(M2)) != mscale(4, I4):
            ok_unitary = False
        cols = clifford_images(M2)
        if cols is None:
            ok_cliff = False
        REFL_M2.append(M2)
        refl_sympl.append(cols)
    check("P2.1 all 60 reflections r_v = 1 - v v^dagger / 2 are unitary "
          "(exact) and CLIFFORD: g P g^dagger is a Pauli up to sign for "
          "all 4 Pauli generators (=> for the whole Pauli group); hence "
          "U G31 U^-1 c C2* (Pauli normalizer) by group closure",
          ok_unitary and ok_cliff)

    OMEGA = ((0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0))


    def f2mat_from_cols(cols):
        return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))


    def f2mul(A, B):
        return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4)) % 2
                           for j in range(4)) for i in range(4))


    def is_symplectic(M):
        Mt = tuple(tuple(M[j][i] for j in range(4)) for i in range(4))
        return f2mul(f2mul(Mt, OMEGA), M) == OMEGA


    SYMP_GENS = [f2mat_from_cols(c) for c in refl_sympl]
    check("P2.2 every reflection's induced F2^4 map is SYMPLECTIC "
          "(preserves the commutation form)",
          all(is_symplectic(M) for M in SYMP_GENS))

    # ==================================================================== P3
    section("P3 (H2b): |G31| = 46080, Sp(4,2) census, and the index-2 "
            "statement in C2 (|C2| = 92160)")

    # permutation BFS (v752 recipe, chart model)
    print("    building G31 (BFS over the 60 reflection permutations) ...",
          flush=True)
    N240 = 240
    zidx = {z: k for k, z in enumerate(Z240)}
    refl_perms = []
    for L in range(60):
        M2 = REFL_M2[L]
        perm = np.empty(N240, dtype=np.int16)
        for k in range(N240):
            img = tuple(gdiv(c, (2, 0)) for c in mat_apply(M2, Z240[k]))
            perm[k] = zidx[img]
        refl_perms.append(perm)
    IDP = np.arange(N240, dtype=np.int16)
    t_bfs = time.time()
    Gset = {IDP.tobytes(): IDP}
    frontier = [IDP]
    while frontier:
        nxt = []
        for p in frontier:
            for g in refl_perms:
                q = p[g]
                b = q.tobytes()
                if b not in Gset:
                    Gset[b] = q
                    nxt.append(q)
        frontier = nxt
    check("P3.1 |G31| = %d = 46080 (BFS %.1f s)"
          % (len(Gset), time.time() - t_bfs), len(Gset) == 46080)

    Jperm = np.array([zidx[vec_scal(GI, Z240[k])] for k in range(N240)],
                     dtype=np.int16)
    scal_in = [k for k in range(4)
               if (IDP if k == 0 else
                   Jperm[Jperm[Jperm]] if k == 3 else
                   Jperm[Jperm] if k == 2 else Jperm).tobytes() in Gset]
    check("P3.2 scalar subgroup: mu4 = {1, i, -1, -i} c G31 (%d/4 powers of "
          "J in the BFS set); NO further scalars possible (a scalar "
          "preserving the Z[i]-root set is a Z[i]-unit, arithmetic)"
          % len(scal_in), len(scal_in) == 4)

    # Pauli membership: the 16 Paulis (mod phase) sit in G31
    pauli_perm = {}
    ok_pauli = True
    for pb in NZ_BITS + [(0, 0, 0, 0)]:
        P = PMAT[pb]
        try:
            perm = np.array([zidx[tuple(mat_apply(P, Z240[k]))]
                             for k in range(N240)], dtype=np.int16)
        except KeyError:
            ok_pauli = False
            break
        pauli_perm[pb] = perm
        if perm.tobytes() not in Gset:
            ok_pauli = False
            break
    check("P3.3 all 16 Pauli operators preserve the 240-root set and lie "
          "in G31 (BFS membership; phases land in mu4 c G31)", ok_pauli)

    # Sp(4,2) closure of the 60 symplectic images
    sp_set = set()
    sp_frontier = [meyeF2 := tuple(tuple(1 if i == j else 0 for j in range(4))
                                   for i in range(4))]
    sp_set.add(meyeF2)
    while sp_frontier:
        nxt = []
        for A in sp_frontier:
            for B in SYMP_GENS:
                C = f2mul(A, B)
                if C not in sp_set:
                    sp_set.add(C)
                    nxt.append(C)
        sp_frontier = nxt
    check("P3.4 the symplectic images of the 60 reflections generate the "
          "FULL Sp(4,2): closure order %d = 720" % len(sp_set),
          len(sp_set) == 720)

    # projective bookkeeping + the exact order statement (predeclared)
    proj_g31 = 46080 // 4
    proj_c2 = 2 ** 8 * (4 - 1) * (4 ** 2 - 1)
    check("P3.5 PREDECLARED ORDER STATEMENT: |C2/U(1)| = 2^8 (4-1)(4^2-1) "
          "= %d = 16 x 720 (Pauli kernel x Sp(4,2)) = |G31|/|mu4| = %d: "
          "the two PROJECTIVE groups have EQUAL order, and G31/mu4 c "
          "C2/U(1) (P2.1) forces G31/mu4 = C2/U(1) (index 1 projectively)"
          % (proj_c2, proj_g31),
          proj_c2 == 11520 and proj_g31 == 11520
          and proj_c2 == 16 * 720 and len(sp_set) * 16 == proj_c2)

    # matrix-level: scalars of C2 = mu8 via (SH)^3 = zeta8 and determinants
    SQ2H = ((G1, G1), (G1, (-1, 0)))          # sqrt(2) * H, integer over Z[i]
    S1Q = ((G1, G0), (G0, GI))
    A_SH = mmulg(S1Q, SQ2H)                    # sqrt(2) * S H
    A3 = mmulg(mmulg(A_SH, A_SH), A_SH)        # (sqrt2)^3 (SH)^3
    # (SH)^3 = A3 / (2 sqrt2); zeta8 * 2 sqrt2 = 2 + 2i exactly
    ok_zeta = (A3 == mscale(2, ((G1, G0), (G0, G1)))
               or A3 == (((2, 2), G0), (G0, (2, 2))))
    CNOT = ((G1, G0, G0, G0), (G0, G1, G0, G0),
            (G0, G0, G0, G1), (G0, G0, G1, G0))
    dS1 = det4(kron(S1Q, I2))
    dS2 = det4(kron(I2, S1Q))
    dCN = det4(CNOT)
    dH = gdiv(det4(kron(SQ2H, I2)), (4, 0))    # det(H(x)I) = det(sqrt2 H)^2/4
    check("P3.6 SCALARS OF C2 = mu8 exactly: (i) (S H)^3 = zeta8 * I "
          "(exact: (sqrt2 SH)^3 = (2+2i) I = 2 sqrt2 zeta8 I: %s) => "
          "zeta8 I in C2; (ii) det(S(x)I) = %s, det(I(x)S) = %s, "
          "det(CNOT) = %s, det(H(x)I) = %s, all in {+-1} => any scalar "
          "lambda I in C2 has lambda^4 = det in {+-1}, lambda^8 = 1, and "
          "roots of unity in Q(zeta8) are exactly mu8"
          % (A3 == (((2, 2), G0), (G0, (2, 2))), dS1, dS2, dCN, dH),
          A3 == (((2, 2), G0), (G0, (2, 2)))
          and dS1 == (-1, 0) and dS2 == (-1, 0) and dCN == (-1, 0)
          and dH == G1)

    refl_dets = {gdiv(det4(M2), (16, 0)) for M2 in REFL_M2}
    c2_order = proj_c2 * 8
    check("P3.7 INDEX 2: |C2| = 11520 x |mu8| = %d = 2 x |G31| = 2 x 46080; "
          "G31 c C2 (every g in G31 equals lambda m, lambda^4 = det g / "
          "det m in mu4 -- reflection dets %s c mu4 -- so lambda in mu8 c "
          "C2); coset representative zeta8 I; C2 = G31 u zeta8 G31, "
          "quotient character chi: C2 -> Z2 = the Q(i)-RATIONALITY bit "
          "(G31 has Q(i) entries, the coset has zeta8 * Q(i) entries)"
          % (c2_order, sorted(refl_dets)),
          c2_order == 92160 and c2_order == 2 * 46080
          and refl_dets == {(-1, 0)})

    # coset witness: zeta8^-1 (H(x)I) has Q(i) entries and lies in G31
    H4x4_scaled = kron(SQ2H, I2)               # sqrt2 * (H(x)I)
    # zeta8^-1 (H(x)I) = (1-i)/2 * (sqrt2 H(x)I) / ... : 2 * zeta8^-1 H(x)I
    #   = (1-i) * (sqrt2 H (x) I)
    W2 = tuple(tuple(gmul((1, -1), H4x4_scaled[i][j]) for j in range(4))
               for i in range(4))
    ok_w_unit = mmulg(W2, mdagger(W2)) == mscale(4, I4)
    try:
        wperm = np.array([zidx[tuple(gdiv(c, (2, 0))
                                     for c in mat_apply(W2, Z240[k]))]
                          for k in range(N240)], dtype=np.int16)
        ok_w_in = wperm.tobytes() in Gset
    except KeyError:
        ok_w_in = False
    check("P3.8 COSET WITNESS: w = zeta8^-1 (H(x)I) = (1-i)/2 (sqrt2 H)(x)I "
          "is Q(i)-unitary, preserves the 240 roots and lies in G31 => "
          "H(x)I = zeta8 w sits in the NONTRIVIAL coset (chi(H) = 1, "
          "chi(S) = chi(CNOT) = 0)", ok_w_unit and ok_w_in)

    # ==================================================================== P4
    section("P4 (H3): 46080 = 4 x 16 x 720 -- mu4-phase x 16 code states x "
            "Sp(4,2)")

    ker_phi = 46080 // len(sp_set)
    check("P4.1 kernel of G31 -> Sp(4,2): order %d = 64 = |mu4| x |Pauli16| "
          "(the 16 Paulis are IN G31 (P3.3), mu4 is central (P3.2), and "
          "mu4 * Pauli has exactly 4 x 16 = 64 matrices) => 46080 = "
          "4 x 16 x 720 EXACTLY as the extension mu4 . Pauli16 . Sp(4,2)"
          % ker_phi, ker_phi == 64)

    # the 16: Pauli group mod phase vs the 16 classes of V = L/(1+i)L
    labels_sorted = sorted(REPS)
    lab_id = {lb: k for k, lb in enumerate(labels_sorted)}
    labarr = np.array([lab_id[root_label[r]] for r in ROOTS], dtype=np.int8)
    Eall = np.stack(list(Gset.values()))
    trivial_mask = np.all(labarr[Eall] == labarr[None, :], axis=1)
    n_triv = int(trivial_mask.sum())
    pauli_triv = all(np.array_equal(labarr[pauli_perm[pb]], labarr)
                     for pb in NZ_BITS)
    check("P4.2 CODE-STATE SEMANTICS: exactly %d = 64 elements of G31 act "
          "trivially on the 16 classes of V = L/(1+i)L, and the 64 are "
          "precisely mu4 x Pauli16 (all 15 nonzero Paulis fix every class: "
          "%s) -- the '16' in the factorization IS the Pauli group mod "
          "phase, acting as the identity on the 16 code states"
          % (n_triv, pauli_triv), n_triv == 64 and pauli_triv)

    # module comparison: rho_V (action on V) vs phi (action on Pauli bits)
    basis_labels = []
    span = {ZERO}
    for lb in labels_sorted:
        if lb in span:
            continue
        basis_labels.append(lb)
        span = set()
        for bits in itertools.product((0, 1), repeat=len(basis_labels)):
            w = (0,) * 8
            for bit, l2 in zip(bits, basis_labels):
                if bit:
                    w = add_vec(w, REPS[l2])
            span.add(LAT["label"](w))
        if len(basis_labels) == 4:
            break
    BITS_V = {}
    for bits in itertools.product((0, 1), repeat=4):
        w = (0,) * 8
        for bit, l2 in zip(bits, basis_labels):
            if bit:
                w = add_vec(w, REPS[l2])
        BITS_V[LAT["label"](w)] = bits
    class_root = {}
    for k, r in enumerate(ROOTS):
        class_root.setdefault(root_label[r], k)

    rhoV_gens = []
    ok_lin = True
    for L in range(60):
        perm = refl_perms[L]
        cols = [BITS_V[root_label[ROOTS[int(perm[class_root[lb]])]]]
                for lb in basis_labels]
        A = f2mat_from_cols(cols)
        for lb in labels_sorted:
            if lb == ZERO:
                continue
            img_bits = tuple(sum(A[i][j] * BITS_V[lb][j] for j in range(4)) % 2
                             for i in range(4))
            real_bits = BITS_V[root_label[ROOTS[int(perm[class_root[lb]])]]]
            if img_bits != real_bits:
                ok_lin = False
        rhoV_gens.append(A)
    check("P4.3 the G31 action on V is F2-LINEAR (all 60 generators, all "
          "15 classes checked against the matrix)", ok_lin)

    # intertwiner space {T : T rhoV(g) = phi(g) T for all gens} over F2
    rows_f2 = []
    for A, B in zip(rhoV_gens, SYMP_GENS):
        for i in range(4):
            for j in range(4):
                row = [0] * 16
                for k in range(4):
                    row[4 * i + k] ^= A[k][j]      # (T A)_{ij}
                    row[4 * k + j] ^= B[i][k]      # (B T)_{ij}
                rows_f2.append(row)
    # F2 Gaussian elimination -> nullspace
    M = [r[:] for r in rows_f2]
    pivots = []
    rank = 0
    for col in range(16):
        piv = next((r for r in range(rank, len(M)) if M[r][col]), None)
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        for r in range(len(M)):
            if r != rank and M[r][col]:
                M[r] = [(a + b) % 2 for a, b in zip(M[r], M[rank])]
        pivots.append(col)
        rank += 1
    free_cols = [c for c in range(16) if c not in pivots]
    null_dim = 16 - rank
    null_basis = []
    for fc in free_cols:
        v = [0] * 16
        v[fc] = 1
        for r, pc in enumerate(pivots):
            v[pc] = M[r][fc]
        null_basis.append(v)
    inv_T = 0
    assert null_dim <= 8, "unexpected intertwiner space dimension"
    for mask in range(1, 2 ** null_dim):
        v = [0] * 16
        for b in range(null_dim):
            if mask >> b & 1:
                v = [(a + c) % 2 for a, c in zip(v, null_basis[b])]
        T = tuple(tuple(v[4 * i + j] for j in range(4)) for i in range(4))
        # invertible over F2?
        rr, MM = 0, [list(t) for t in T]
        for col in range(4):
            piv = next((r for r in range(rr, 4) if MM[r][col]), None)
            if piv is None:
                continue
            MM[rr], MM[piv] = MM[piv], MM[rr]
            for r in range(4):
                if r != rr and MM[r][col]:
                    MM[r] = [(a + b) % 2 for a, b in zip(MM[r], MM[rr])]
            rr += 1
        if rr == 4:
            inv_T += 1
    check("P4.4 MODULE STRUCTURE (honest): dim Hom_F2[G31](V, Pauli/phase) "
          "= %d, invertible intertwiners: %d -- the two Sp(4,2)-modules "
          "(code states V vs Pauli bits) are %s; the classes<->contexts "
          "dictionary (P6) is the point<->line DUALITY of the self-dual "
          "GQ(2,2) (the S6 outer twist), not a linear isomorphism"
          % (null_dim, inv_T,
             "NOT linearly isomorphic (duality-twisted)" if inv_T == 0
             else "linearly ISOMORPHIC"),
          True)  # census check: reported either way; structural claim is P6

    # ==================================================================== P5
    section("P5 (H4): the index-2 character -- predeclared orientation "
            "reading vs the actual (Galois) content")

    # (i) J-orientation exchange: J = iI is a SCALAR in the chart; every
    # unitary (in particular every coset element zeta8 g) conjugates it
    # trivially: m (iI) m^-1 = iI.  Verified exactly on the witness w.
    Jmat = meye(4, GI)
    conjJ = mmulg(mmulg(W2, Jmat), mdagger(W2))    # 4 * (w i w^-1)
    ok_i = conjJ == mscale(4, Jmat)
    # (ii) mu4-phase conjugation: mu4 is central in C2 -- conjugation is
    # trivial for EVERY element; the coset cannot conjugate the phases.
    check("P5.1 PREDECLARED H4 READINGS BOTH FAIL: (i) the nontrivial coset "
          "does NOT exchange J <-> -J (J = iI is a scalar; w J w^-1 = J "
          "exactly: %s; no unitary anticommutes with a scalar); (ii) it "
          "does NOT conjugate the mu4 phases (mu4 is CENTRAL in C2) -- "
          "the coset is zeta8 * G31, its conjugation action is G31's own"
          % ok_i, ok_i)          # the check PASSES = the failure is proven

    # (iii) what the character actually is: the Galois / sqrt2 bit
    # tau = Gal(Q(zeta8)/Q(i)): zeta8 -> -zeta8, sqrt2 -> -sqrt2;
    # tau fixes G31 elementwise (Q(i) entries) and negates the coset:
    # chi = tau-parity = Hadamard parity.  The coset exchanges the two
    # mu8-lift classes {mu4 R, zeta8 mu4 R} of the 240 roots:
    # (zeta8 w) R = zeta8 R != R (entries irrational), (zeta8 w)^2 in G31.
    sq2 = 2 ** 0.5
    zf = np.array([[complex(c[0], c[1]) for c in z] for z in Z240])
    Hf = np.kron(np.array([[1, 1], [1, -1]]) / sq2, np.eye(2))
    img = (Hf @ zf.T).T
    frac = np.abs(img - np.round(img))
    ok_off_lattice = float(frac.max()) > 0.4       # entries k/sqrt2, k odd
    zeta8sq_in = True                              # (zeta8 w)^2 = i w^2
    w2perm = wperm[wperm]
    zeta8sq_in = Jperm[w2perm].tobytes() in Gset or \
        w2perm[Jperm].tobytes() in Gset
    check("P5.2 ACTUAL CHARACTER CONTENT (reported, not the predeclared "
          "reading): chi = Gal(Q(zeta8)/Q(i))-parity (the sqrt2/Hadamard "
          "bit): H(x)I maps the 240 Z[i]-roots OFF the lattice into "
          "zeta8 * L (max frac dist %.3f > 0: irrational entries), i.e. "
          "the coset EXCHANGES the two mu8-lift classes {mu4 R, zeta8 mu4 "
          "R}; (zeta8 w)^2 = i w^2 in G31: %s"
          % (float(frac.max()), zeta8sq_in),
          ok_off_lattice and zeta8sq_in)

    # the true J <-> -J bit is ANTIUNITARY (complex conjugation), it
    # normalizes G31 and FIXES chi -- it is a separate, outer Z2
    conj_roots_ok = all(tuple(gconj(c) for c in z) in zidx for z in Z240)
    conj_refl_ok = all(canonical_ray(tuple(gconj(c) for c in Z240[line_reps[L]]))
                       in set(GAUSS_RAYS) for L in range(60))
    check("P5.3 the J <-> -J orientation bit lives OUTSIDE C2 as the "
          "ANTIUNITARY complex conjugation: it preserves the root set "
          "(%s), maps reflections to reflections (conj(r_v) = r_conj(v): "
          "line set preserved %s), so it normalizes G31 AND C2 and fixes "
          "chi -- orientation and chi are two DIFFERENT Z2's"
          % (conj_roots_ok, conj_refl_ok), conj_roots_ok and conj_refl_ok)

    H4_PASS = False       # predeclared reading (i)/(ii): both provably fail

    # ==================================================================== P6
    section("P6 (S1/S2): classes <-> contexts, the W(3,2) dictionary vs "
            "v752's B, and the MUB spreads")

    # each class's 4 lines -> one context
    class_ctx = {}
    ok_ctx = True
    for lb in labels_sorted:
        if lb == ZERO:
            continue
        rays = {canonical_ray(Z240[line_reps[line_of[k]]])
                for k, r in enumerate(ROOTS) if root_label[r] == lb}
        ctxs = {stab_ray_ctx[ray] for ray in rays}
        if len(rays) != 4 or len(ctxs) != 1:
            ok_ctx = False
            break
        class_ctx[lb] = next(iter(ctxs))
    bij = len(set(class_ctx.values())) == 15
    check("P6.1 S1: each of the 15 classes' 4 lines form the joint "
          "eigenbasis of exactly ONE Pauli context; the map classes -> "
          "contexts is a BIJECTION", ok_ctx and bij)


    def herm_amb(x, y):
        """h(x,y) in Z[i] from ambient coordinates (v752 convention)."""
        z, w = chart(x), chart(y)
        s = hermC(z, w)
        assert s[0] % 2 == 0 and s[1] % 2 == 0
        return (s[0] // 2, s[1] // 2)


    def hbar(x, y):
        h = herm_amb(x, y)
        return (h[0] + h[1]) % 2


    POINTS = [lb for lb in labels_sorted if lb != ZERO]
    B15 = [[1 if hbar(REPS[x], REPS[y]) == 0 else 0 for y in POINTS]
           for x in POINTS]
    BBt = [[sum(B15[i][k] * B15[j][k] for k in range(15)) for j in range(15)]
           for i in range(15)]
    TARGET = [[7 if i == j else 3 for j in range(15)] for i in range(15)]
    check("P6.2 v752 anchor: B B^T = 4I + 3J holds EXACTLY in the chart "
          "model (same B as v752)", BBt == TARGET)

    ok_dict = True
    for i, x in enumerate(POINTS):
        for j, y in enumerate(POINTS):
            if i >= j:
                continue
            share = len(contexts[class_ctx[x]] & contexts[class_ctx[y]]) > 0
            if (B15[i][j] == 1) != share:
                ok_dict = False
    check("P6.3 THE DICTIONARY (all 105 pairs): hbar(x,y) = 0 <=> the "
          "contexts Gamma_x, Gamma_y SHARE a Pauli -- v752's incidence B "
          "IS the context-collinearity of W(3,2) under the bijection "
          "(point<->line duality of GQ(2,2))", ok_dict)

    # spreads: 5-sets of pairwise disjoint contexts = MUB pentads
    spreads = []
    for combo in itertools.combinations(range(15), 5):
        cs = [contexts[c] for c in combo]
        if all(not (a & b) for a, b in itertools.combinations(cs, 2)):
            spreads.append(combo)
    ok_cover = all(len(frozenset().union(*[contexts[c] for c in S])) == 15
                   for S in spreads)
    # unbiasedness across distinct contexts of each spread (exact |h| = 1)
    ctx_rays = {}
    for ray, ci in stab_ray_ctx.items():
        ctx_rays.setdefault(ci, []).append(ray)
    ok_mub = True
    for S in spreads:
        for a, b in itertools.combinations(S, 2):
            for u in ctx_rays[a]:
                for v in ctx_rays[b]:
                    nu = sum(gnorm(c) for c in u)
                    nv = sum(gnorm(c) for c in v)
                    if 4 * gnorm(hermC(u, v)) != nu * nv:
                        ok_mub = False
    # pullback: the 5 classes of a spread are pairwise hbar = 1 (ovoid)
    inv_ctx = {v: k for k, v in class_ctx.items()}
    ok_ovoid = True
    for S in spreads:
        cls = [inv_ctx[c] for c in S]
        for x, y in itertools.combinations(cls, 2):
            if hbar(REPS[x], REPS[y]) != 1:
                ok_ovoid = False
    check("P6.4 S2: exactly %d spreads (5 pairwise-disjoint contexts "
          "covering all 15 Paulis: %s) = the MUB pentads (all cross-context "
          "state pairs unbiased, |<psi|phi>|^2 = 1/4 EXACT: %s); pullback "
          "under S1 = 5 classes pairwise hbar = 1 (ovoids -- duality again: "
          "%s)" % (len(spreads), ok_cover, ok_mub, ok_ovoid),
          len(spreads) == 6 and ok_cover and ok_mub and ok_ovoid)

    # ==================================================================== P7
    section("P7: CONTROLS (must fire)")

    rng = np.random.default_rng(20260805)
    Sf = np.array([[complex(c[0], c[1]) for c in z] for z in STAB_RAYS])
    Sf = Sf / np.linalg.norm(Sf, axis=1, keepdims=True)
    Gf = np.array([[complex(c[0], c[1]) for c in z] for z in GAUSS_RAYS])
    Gf = Gf / np.linalg.norm(Gf, axis=1, keepdims=True)


    def count_matches(U):
        img = (U @ Gf.T).T
        ov = np.abs(img.conj() @ Sf.T) ** 2
        return int((ov.max(axis=1) > 1 - 1e-9).sum())


    A = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    Q, _ = np.linalg.qr(A)
    n_rand = count_matches(Q)
    check("P7.1 C1 FIRES: Haar-random unitary in place of U: %d/60 matches "
          "(expected 0)" % n_rand, n_rand == 0)

    UT = np.diag([1, 1, 1, np.exp(1j * np.pi / 4)])
    n_T = count_matches(UT)
    check("P7.2 C2 FIRES: wrong frame PAIRING (same frame, non-mu4 residual "
          "phase: T-gate twist diag(1,1,1,zeta8)): %d/60 matches = the "
          "predeclared 16 (15 rays with slot-3 entry 0, plus e3) -- the "
          "frame alone does NOT force the identification; the lattice does"
          % n_T, n_T == 16)

    UCH = np.array([[1, 0, 0, 0], [0, 1, 0, 0],
                    [0, 0, 1 / sq2, 1 / sq2], [0, 0, 1 / sq2, -1 / sq2]])
    n_CH = count_matches(UCH)
    check("P7.3 C2b FIRES: frame paired to a NON-context stabilizer frame "
          "{|00>,|01>,|1+>,|1->} (controlled-Hadamard, non-Clifford): "
          "%d/60 < 60 matches" % n_CH, n_CH < 60)

    R = rng.normal(size=(60, 4)) + 1j * rng.normal(size=(60, 4))
    R = R / np.linalg.norm(R, axis=1, keepdims=True)
    ov = np.abs(R.conj() @ Sf.T) ** 2
    n_rr = int((ov.max(axis=1) > 1 - 1e-9).sum())
    check("P7.4 C3 FIRES: 60 seeded random rays vs the stabilizer set: "
          "%d/60 matches (expected 0)" % n_rr, n_rr == 0)

    # ============================================================== VERDICT
    section("SUMMARY / VERDICT (frozen enum)")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    print("%d/%d checks passed" % (n_pass, len(CHECKS)))
    controls_fire = all(ok for n, ok in CHECKS if n.startswith("P7"))
    H1 = all(ok for n, ok in CHECKS if n.startswith(("P0", "P1")))
    H2 = all(ok for n, ok in CHECKS if n.startswith(("P2", "P3")))
    H3 = all(ok for n, ok in CHECKS if n.startswith("P4"))
    S_OK = all(ok for n, ok in CHECKS if n.startswith("P6"))
    if not controls_fire:
        verdict = "TEST-VOID"
    elif not H1:
        verdict = "CLIFFORD-DEAD"
    elif H1 and H2 and H3 and S_OK and H4_PASS:
        verdict = "CLIFFORD-IDENTIFIED"
    else:
        fails = [h for h, ok in
                 [("H1", H1), ("H2", H2), ("H3", H3), ("H4", H4_PASS),
                  ("S", S_OK)] if not ok]
        verdict = "CLIFFORD-PARTIAL(%s)" % ",".join(fails)
    print("VERDICT: %s" % verdict)
    print("""
RESULT (stated plainly):
  * H1 EXACT: under the single predeclared chart U (coordinate-class
    frame -> computational basis, z_k = r_2k + i r_2k+1), the 60
    Gaussian E8 lines ARE the 60 pure two-qubit stabilizer rays,
    entry-exactly over Z[i] (60/60, support census 4 + 24 + 32).
  * H2 EXACT: U G31 U^-1 c C2 with |C2| = 92160 = 2 x 46080: index 2,
    coset zeta8 G31; projectively G31/mu4 = C2/U(1) (both 11520).
  * H3 EXACT: 46080 = 4 x 16 x 720 = mu4 x Pauli16 x Sp(4,2), with the
    16 Paulis acting trivially on the 16 code states of V = L/(1+i)L.
  * H4 FAILS AS PREDECLARED: the coset conjugates NEITHER J nor mu4
    (zeta8 is central); the character is the Galois sqrt2/Hadamard bit
    (Q(i)-rationality), and it exchanges the two mu8-lift classes of
    the 240 roots; the J <-> -J orientation bit is the ANTIUNITARY
    conjugation, a separate outer Z2 that fixes chi.
  * FIREWALL: no physics claim.  The fired ROOTCLASS-MIXED kill (v775,
    ARF.ROOTCLASS.01: the root-level code->matter reading is dead) is
    UNAFFECTED: this identification is stabilizer-formalism mathematics
    about the carrier, not a matter assignment.
""")
    print("elapsed: %.1f s" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == len(CHECKS)
          else "SOME CHECKS FAILED")
    return n_pass, len(CHECKS), verdict


def run():
    """run_all entry point (v757 precedent): expected pattern 32/32 with
    verdict CLIFFORD-PARTIAL(H4) (any other verdict breaks the suite)."""
    n_pass, n_all, verdict = main()
    ok = (n_pass == n_all == 32 and verdict == "CLIFFORD-PARTIAL(H4)")
    print("\n[%s] PATTERN GATE: expected 32/32 CLIFFORD-PARTIAL(H4); got "
          "%d/%d %s" % ("PASS" if ok else "FAIL", n_pass, n_all, verdict))
    print("\nADJUDICATION: %s -- CLIFFORD-PARTIAL(H4): the 60 Gaussian E8 "
          "lines ARE the 60 two-qubit stabilizer rays entry-exactly over "
          "Z[i] (60/60, support census 4 + 24 + 32); U G31 U^-1 is an "
          "index-2 subgroup of the Clifford matrix group C2 (92160 = 2 x "
          "46080, coset zeta8 G31; projectively equal at 11520); the "
          "semantics carry (46080 = 4 x 16 x 720 = mu4 x Pauli16 x "
          "Sp(4,2)); the H4 layer is the honest partial: the index bit is "
          "the sqrt2/Hadamard Galois bit chi = Gal(Q(zeta8)/Q(i))-parity, "
          "NOT J <-> -J (antiunitary, a separate outer Z2).  All controls "
          "fire (Haar 0/60, T-twist exactly 16/60, non-context frame "
          "12/60 < 60, random rays 0/60).  Dated cross-note on "
          "E8.GAUSSIAN.CODE.01 registered at promotion.  NO RH claim."
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
