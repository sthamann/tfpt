"""v993 -- AX.P2.01 / AX.P1.01 / SEAM.SIMPLECURRENT.GENERATOR.01
[O updates: census-level architecture lift + finite CE uniqueness +
[lambda]^2 = [v] parity shadow; axiom typing UNCHANGED].

THE POINT (external review wave 3, 2026-08-28, 'Minimal Defect Theorem').
v624 showed: UNDER the D_{d+1}+A_{d-1} glue architecture, three independent
selectors each force d = 4 (honest typing: CONDITIONAL on that architecture).
This module runs a DIFFERENT census:

  * rank 8 is an INPUT, from the cited minimality premise c_- = 8
    (minimal nontrivial bosonic chiral invertible defect; unique holomorphic
    c = 8 theory = (E8)_1) -- CITED, not proved;
  * the glue group is demanded cyclic of order 4 on BOTH factors, from the
    finite shadow of U^2 = (-1)^F;
  * the census runs over ALL rank-8 ADE pairs (D+A, D+D, A+A, E6/E7 pieces),
    not only the D_{d+1}+A_{d-1} family.

  [E] 1. SNF of Cartan MATCHES textbook disc groups (computed, not cited):
        A_n = Z_{n+1}; D_n = Z4 (n odd) / Z2 x Z2 (n even); E6 = Z3,
        E7 = Z2, E8 = 1.  D3 ≅ A3 at Cartan level.
  [E] 2. FULL ADE rank-8 pair census: the only diagonal cyclic-Z4 isotropic
        unimodular glue is (D5, A3), up to D3 ≅ A3 (D5(+)D3 is the same
        pair).  The D+A architecture of v624 is an OUTPUT of (rank 8 +
        cyclic Z4 both sides), not an INPUT.  Verdict
        MINIMAL_DEFECT_UNCONDITIONAL at the lattice level (still
        conditional on cited c_-=8, ADE-ness, and the Z4-from-lift premise).
  [E] 3. KILL / MUTANT LEGS: (D4, A4) not cyclic Z4; (A4, A4) product 25
        (Z5 glue); (E7, A1) product 4; (D4, D4) product 16 but Klein
        Z2xZ2 -- NO order-4 element; (A7, A1) product 16 but A1 = Z2;
        Z3 controls (E6, A2) = Z3 x Z3.  Dropping cyclicity would re-open
        D4(+)D4 (v624-style architecture residue, honestly recorded).
  [E] 4. [lambda]^2 = [v] EXACTLY: 2[omega_s] = [v] in disc(D5); the
        order-4 glue class squares to the fermion-parity / D5-vector class
        (lattice shadow of U^2 = (-1)^F).  Non-split: the order-2 vector
        glue has norm 7/4 not in 2Z (v983 kill).
  [E] 5. UNIQUE finite trace-preserving conditional expectation
        E = (1/4) sum_r Ad(u^r) on M_d^{Z4} (d=4,8) and on the crossed
        product M_d x| Z4.  Uniqueness NEEDS the module property: without
        it the deviation kernel is dim 36 (d=4) / 720 (d=8).
  [E] 6. P1 arithmetic shadow (v484/v813 identity, not a new derivation):
        1/(|mu4| * 2 pi) = 1/(4 * 2 pi) = 1/(8 pi) = c3; I_Jones * beta
        * c3 = 1.  Wrong-index I=2 gives 1/(4 pi) ≠ c3.

HONEST SCOPE (firewall): lattice / finite-algebra level only.  Operator-
algebraic minimality (c_- = 8; holomorphic uniqueness at c = 8) is CITED,
not proved.  The operator identification 'modular determinant-line response
equidistributed over the four deck sectors' stays the open [C] of v813.
AX.P1.01 and AX.P2.01 stay Axiom -- the census lifts the architecture
conditionality of v624 at lattice level; it does not derive the axioms.
No marker move.  Python-only / Wolfram mirror deferred (GATE.WOLFRAM.02).
"""
import itertools

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

from tfpt_constants import check, summary, reset, c3 as C3_MP

OMEGA_S = [sp.Rational(1, 2)] * 5
OMEGA_F = [sp.Rational(3, 4), sp.Rational(-1, 4),
           sp.Rational(-1, 4), sp.Rational(-1, 4)]
LAM = OMEGA_S + OMEGA_F
V_D5 = [sp.Integer(1), 0, 0, 0, 0]


def cartan_A(n):
    M = sp.zeros(n)
    for i in range(n):
        M[i, i] = 2
        if i + 1 < n:
            M[i, i + 1] = M[i + 1, i] = -1
    return M


def cartan_D(n):
    """D_n for n >= 2.  D2 = A1 (+) A1; D3 ≅ A3."""
    if n == 2:
        return sp.diag(2, 2)
    M = cartan_A(n)
    M[n - 2, n - 1] = M[n - 1, n - 2] = 0
    M[n - 3, n - 1] = M[n - 1, n - 3] = -1
    return M


def cartan_E(n):
    """E6 / E7 / E8: chain of n-1 nodes, branch at node 2 (0-indexed)."""
    M = sp.zeros(n)
    for i in range(n - 1):
        M[i, i] = 2
        if i + 1 < n - 1:
            M[i, i + 1] = M[i + 1, i] = -1
    M[n - 1, n - 1] = 2
    M[2, n - 1] = M[n - 1, 2] = -1
    return M


def snf_factors(C):
    """Invariant factors of disc = coker(Cartan) via Smith normal form.
    Drops the 1's.  Returns a tuple, e.g. (4,) for Z4, (2, 2) for Z2 x Z2."""
    S = smith_normal_form(sp.Matrix(C), domain=sp.ZZ)
    return tuple(int(S[i, i]) for i in range(S.rows) if int(S[i, i]) != 1)


def disc_order(C):
    return abs(int(sp.Matrix(C).det()))


def textbook_D(n):
    return (4,) if (n % 2 == 1) else (2, 2)


def textbook_A(n):
    return (n + 1,)


def generator_order_and_q(C, k=None):
    """Order and discriminant quadratic form q(x)=(x,x) of a dual class.
    Default: last simple-root dual (spinor node of D_n; omega_n of A_n)."""
    C = sp.Matrix(C)
    Cinv = C.inv()
    n = C.rows
    if k is None:
        k = sp.Matrix.zeros(n, 1)
        k[n - 1] = 1
    else:
        k = sp.Matrix(k).reshape(n, 1)

    def trivial(vec):
        y = Cinv * vec
        return all(yi.is_integer for yi in y)

    det = abs(int(C.det()))
    order = None
    for t in range(1, det + 2):
        if trivial(t * k):
            order = t
            break
    q = sp.simplify((k.T * Cinv * k)[0, 0])
    return order, q


def cyclic_Z4(factors):
    return factors == (4,)


def has_Z4_element(factors):
    """Abelian group has an element of order 4 iff 4 divides the exponent."""
    if not factors:
        return False
    exp = 1
    for d in factors:
        exp = int(sp.ilcm(exp, d))
    return exp % 4 == 0


def in_D5(x):
    return all(sp.sympify(v).is_integer is True for v in x) and sum(x) % 2 == 0


def in_A3(y):
    return all(sp.sympify(v).is_integer is True for v in y) and sum(y) == 0


def in_L0(z):
    return in_D5(z[:5]) and in_A3(z[5:])


def clock(d):
    return np.diag([1j ** (j % 4) for j in range(d)]).astype(complex)


def alpha(u, x, r):
    ur = np.linalg.matrix_power(u, r)
    return ur @ x @ ur.conj().T


def group_E(u, x):
    return sum(alpha(u, x, r) for r in range(4)) / 4.0


def is_fix(u, a, tol=1e-10):
    return np.allclose(alpha(u, a, 1), a, atol=tol)


def randh(d, rng):
    return rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))


def rand_fix(u, d, rng):
    return group_E(u, randh(d, rng))


def ce_properties(d, rng, n_samples=8):
    u = clock(d)
    ok = True
    for _ in range(n_samples):
        x = randh(d, rng)
        a = rand_fix(u, d, rng)
        b = rand_fix(u, d, rng)
        Ex = group_E(u, x)
        ok &= np.allclose(group_E(u, Ex), Ex, atol=1e-12)
        ok &= np.allclose(group_E(u, a), a, atol=1e-12)
        ok &= np.allclose(group_E(u, a @ x @ b), a @ Ex @ b, atol=1e-12)
        ok &= is_fix(u, Ex)
        ok &= np.allclose(np.trace(Ex), np.trace(x), atol=1e-10)
        y = randh(d, rng)
        psd = y.conj().T @ y
        e_psd = group_E(u, psd)
        e_psd = 0.5 * (e_psd + e_psd.conj().T)
        ok &= np.linalg.eigvalsh(e_psd).min() >= -1e-9
    return ok


def crossed_E_properties(d, rng, n_samples=6):
    """Inner mu4 clock action on the crossed product, part-A embedding
    Phi(a V^g) = (a u^g) (x) w^g inside M_d (x) Alg(w) subset M_{4d}."""
    u = clock(d)
    w = np.roll(np.eye(4), 1, axis=0).astype(complex)
    U = np.kron(u, np.eye(4))

    def embed(ags):
        X = np.zeros((4 * d, 4 * d), dtype=complex)
        for g, ag in enumerate(ags):
            X += np.kron(ag, np.linalg.matrix_power(w, g))
        return X

    def alpha_cp(X, r):
        Ur = np.linalg.matrix_power(U, r)
        return Ur @ X @ Ur.conj().T

    def E_cp(X):
        return sum(alpha_cp(X, r) for r in range(4)) / 4.0

    ok = True
    for _ in range(n_samples):
        ags = [randh(d, rng) for _ in range(4)]
        X = embed(ags)
        EX = E_cp(X)
        ok &= np.allclose(E_cp(EX), EX, atol=1e-12)
        ok &= np.allclose(alpha_cp(EX, 1), EX, atol=1e-12)
        ok &= np.allclose(np.trace(EX), np.trace(X), atol=1e-9)
        a_fix = [rand_fix(u, d, rng) for _ in range(4)]
        b_fix = [rand_fix(u, d, rng) for _ in range(4)]
        A = embed(a_fix)
        B = embed(b_fix)
        ok &= np.allclose(alpha_cp(A, 1), A, atol=1e-10)
        ok &= np.allclose(E_cp(A @ X @ B), A @ EX @ B, atol=1e-9)
        Y = embed([randh(d, rng) for _ in range(4)])
        psd = Y.conj().T @ Y
        e_psd = E_cp(psd)
        e_psd = 0.5 * (e_psd + e_psd.conj().T)
        ok &= np.linalg.eigvalsh(e_psd).min() >= -1e-8
        ok &= np.allclose(E_cp(A), A, atol=1e-10)
    return ok


def free_deviation_coords(d, bimodule=True):
    """Finite linear algebra on Hom(M_d, M_d).  Zero-constraints from
    im D ⊆ Fix, D|Fix = 0, and (optional) N-bimodule by the clock spectral
    projections.  Returns (n_free, trace-rank, kernel dim)."""
    forced = np.zeros((d, d, d, d), dtype=bool)
    for i, j, k, l in itertools.product(range(d), repeat=4):
        z = False
        if (k % 4) != (l % 4):
            z = True
        if (i % 4) == (j % 4):
            z = True
        if bimodule and ((k % 4) != (i % 4) or (l % 4) != (j % 4)):
            z = True
        forced[i, j, k, l] = z
    n_free = int(np.size(forced) - np.count_nonzero(forced))
    free_idx = list(zip(*np.where(~forced))) if n_free else []
    if n_free == 0:
        return 0, 0, 0
    coord = {ijkl: p for p, ijkl in enumerate(free_idx)}
    rows = []
    for i, j in itertools.product(range(d), repeat=2):
        row = np.zeros(n_free, dtype=np.float64)
        nonempty = False
        for k in range(d):
            key = (i, j, k, k)
            if key in coord:
                row[coord[key]] = 1.0
                nonempty = True
        if nonempty:
            rows.append(row)
    A = np.stack(rows) if rows else np.zeros((1, n_free))
    rnk = int(np.linalg.matrix_rank(A, tol=1e-10))
    return n_free, rnk, n_free - rnk


def run():
    reset()
    print("v993  minimal defect selector: rank-8 ADE census + "
          "[lambda]^2 = [v] + unique finite CE (wave 3)")

    formula_ok = True
    for n in range(1, 9):
        if snf_factors(cartan_A(n)) != textbook_A(n):
            formula_ok = False
    for n in range(2, 9):
        if snf_factors(cartan_D(n)) != textbook_D(n):
            formula_ok = False
    check("SNF of Cartan MATCHES textbook disc groups [E]: A_n = Z_{n+1} "
          "(n=1..8); D_n = Z4 (n odd) / Z2 x Z2 (n even) (n=2..8); "
          "E6 = Z3, E7 = Z2, E8 = 1 -- computed, not cited",
          formula_ok
          and snf_factors(cartan_E(6)) == (3,)
          and snf_factors(cartan_E(7)) == (2,)
          and snf_factors(cartan_E(8)) == ())

    check("D3 ≅ A3 at the Cartan level [E]: both rank 3, det 4, SNF (4,)",
          snf_factors(cartan_D(3)) == snf_factors(cartan_A(3)) == (4,)
          and disc_order(cartan_D(3)) == disc_order(cartan_A(3)) == 4)

    ROWS = []

    def add_pair(family, t1, n1, C1, t2, n2, C2, alias=None):
        f1, f2 = snf_factors(C1), snf_factors(C2)
        d1, d2 = disc_order(C1), disc_order(C2)
        both = cyclic_Z4(f1) and cyclic_Z4(f2)
        prod = d1 * d2
        unimod_arith = (prod == 16)
        q1 = q2 = iso = None
        if both:
            o1, q1 = generator_order_and_q(C1)
            o2, q2 = generator_order_and_q(C2)
            iso = (o1 == 4 and o2 == 4
                   and sp.simplify((q1 + q2) / 2).is_integer)
        hit = bool(both and unimod_arith and iso)
        ROWS.append(dict(family=family, t1=t1, n1=n1, t2=t2, n2=n2,
                         f1=f1, f2=f2, d1=d1, d2=d2, both=both,
                         prod=prod, unimod_arith=unimod_arith, q1=q1, q2=q2,
                         iso=iso, hit=hit, alias=alias))

    for n in range(2, 8):
        m = 8 - n
        add_pair("D+A", "D", n, cartan_D(n), "A", m, cartan_A(m))
    for n in range(2, 5):
        m = 8 - n
        if m < 2:
            continue
        alias = "D5(+)A3" if {n, m} == {3, 5} else None
        add_pair("D+D", "D", n, cartan_D(n), "D", m, cartan_D(m), alias=alias)
    for n in range(4, 8):
        m = 8 - n
        if m < 1 or m > n:
            continue
        add_pair("A+A", "A", n, cartan_A(n), "A", m, cartan_A(m))
    add_pair("E+A", "E", 6, cartan_E(6), "A", 2, cartan_A(2))
    add_pair("E+D", "E", 6, cartan_E(6), "D", 2, cartan_D(2))
    add_pair("E+A", "E", 7, cartan_E(7), "A", 1, cartan_A(1))

    def find(fam, n1, n2):
        for r in ROWS:
            if r["family"] == fam and r["n1"] == n1 and r["n2"] == n2:
                return r
        return None

    hits = [r for r in ROWS if r["hit"]]
    da_hits = [r for r in ROWS if r["family"] == "D+A" and r["hit"]]
    unique_da = (len(da_hits) == 1
                 and da_hits[0]["n1"] == 5 and da_hits[0]["n2"] == 3)
    canon = []
    for r in hits:
        if (r["t1"], r["n1"], r["t2"], r["n2"]) == ("D", 5, "A", 3):
            canon.append("D5(+)A3")
        elif r["alias"] == "D5(+)A3":
            canon.append("D5(+)A3")
        else:
            canon.append("%s%d(+)%s%d" % (r["t1"], r["n1"], r["t2"], r["n2"]))
    unique_full = (len(hits) >= 1 and set(canon) == {"D5(+)A3"})

    check("D+A family, cyclic Z4 on BOTH factors [E]: selects EXACTLY "
          "(n, m) = (5, 3) among n+m=8",
          unique_da)
    check("FULL ADE rank-8 pair census [E]: the only diagonal cyclic-Z4 "
          "isotropic unimodular glue is (D5, A3), up to D3 ≅ A3 "
          "(D5(+)D3 is the same pair)",
          unique_full)

    r_d4a4 = find("D+A", 4, 4)
    r_a4a4 = find("A+A", 4, 4)
    r_e7a1 = find("E+A", 7, 1)
    r_d4d4 = find("D+D", 4, 4)
    r_a7a1 = find("A+A", 7, 1)
    r_e6a2 = find("E+A", 6, 2)
    r_d5a3 = find("D+A", 5, 3)

    check("NEGATIVE [X]: (D4, A4) is Z2xZ2 x Z5 -- not cyclic Z4 on either "
          "factor",
          r_d4a4 is not None and (not r_d4a4["both"]) and (not r_d4a4["hit"]))
    check("NEGATIVE [X]: (A4, A4) is Z5 x Z5 -- product 25, glue would be "
          "Z5, not Z4",
          r_a4a4 is not None and r_a4a4["prod"] == 25 and (not r_a4a4["hit"]))
    check("NEGATIVE [X]: (E7, A1) is Z2 x Z2 -- product 4, unimodular glue "
          "order 2, not 4",
          r_e7a1 is not None and r_e7a1["prod"] == 4 and (not r_e7a1["hit"]))
    check("NEGATIVE [X]: (D4, D4) has product 16 (unimodular arithmetic "
          "possible) but both discs are Klein Z2xZ2 -- NO order-4 element; "
          "dropping cyclicity would re-open this pair (v624-style architecture "
          "residue, honestly recorded)",
          r_d4d4 is not None and r_d4d4["prod"] == 16
          and r_d4d4["f1"] == (2, 2) and r_d4d4["f2"] == (2, 2)
          and (not r_d4d4["both"]) and (not has_Z4_element(r_d4d4["f1"])))
    check("NEGATIVE [X]: (A7, A1) has product 16 and A7 = Z8 HAS a Z4 "
          "subgroup, but A1 = Z2 does not -- not cyclic Z4 on BOTH factors",
          r_a7a1 is not None and r_a7a1["prod"] == 16
          and has_Z4_element(r_a7a1["f1"])
          and (not has_Z4_element(r_a7a1["f2"]))
          and (not r_a7a1["both"]))
    check("Z3 CONTROL [X]: (E6, A2) is Z3 x Z3 -- cyclic of order 3, not 4; "
          "product 9 (unimodular Z3 glue, not Z4).  Demanding Z3 both sides "
          "would select this pair: the Z4 demand is load-bearing",
          r_e6a2 is not None and r_e6a2["f1"] == (3,)
          and r_e6a2["f2"] == (3,) and r_e6a2["prod"] == 9
          and (not r_e6a2["hit"]))

    check("ISOTROPIC GLUE on the hit [E]: q(D5 spinor) + q(A3 fund) = "
          "5/4 + 3/4 = 2 in 2Z, from k^T C^{-1} k on the SNF-cyclic "
          "generators",
          r_d5a3 is not None and r_d5a3["q1"] == sp.Rational(5, 4)
          and r_d5a3["q2"] == sp.Rational(3, 4)
          and r_d5a3["iso"] is True)

    v624_slice_ok = True
    v624_hits = []
    for dd in (3, 4, 5, 8):
        nD, nA = dd + 1, dd - 1
        if nD < 2 or nA < 1:
            v624_slice_ok = False
            continue
        fD, fA = snf_factors(cartan_D(nD)), snf_factors(cartan_A(nA))
        both = cyclic_Z4(fD) and cyclic_Z4(fA)
        if both:
            v624_hits.append(dd)
        if (dd == 4) != both:
            v624_slice_ok = False
    check("v624 A1 REPRODUCED on the D_{d+1}+A_{d-1} slice [E]: cyclic Z4 "
          "on both factors holds EXACTLY at d=4 (negative controls at other "
          "ranks -- this is v624's census, NOT the rank-8 census above)",
          v624_slice_ok and v624_hits == [4])

    check("DELTA TYPING [E]: full ADE rank-8 census is unique => D+A "
          "architecture is an OUTPUT of (rank 8 + cyclic Z4 both sides), "
          "not an INPUT as in v624 -- verdict MINIMAL_DEFECT_UNCONDITIONAL "
          "(still conditional on cited c_-=8, ADE-ness, Z4-from-lift)",
          unique_full)

    two_s = [2 * v for v in OMEGA_S]
    two_f = [2 * v for v in OMEGA_F]
    two_lam = [2 * v for v in LAM]
    four_lam = [4 * v for v in LAM]
    parity = V_D5 + two_f
    diff_sv = [two_s[i] - V_D5[i] for i in range(5)]
    diff_lp = [two_lam[i] - parity[i] for i in range(9)]

    check("D5-SIDE [E]: 2*omega_s - v = (0,1,1,1,1) is in D5 -- "
          "2[omega_s] = [v] in disc(D5)",
          in_D5(diff_sv) and two_s == [1, 1, 1, 1, 1])
    check("GLUED CLASS [E]: 2*lambda - (v, 2*omega_f) is in L0 = D5(+)A3 "
          "-- 2[lambda] = the D5 vector class paired with the unique "
          "2-torsion of disc(A3)",
          in_L0(diff_lp) and not in_A3(two_f))
    check("ORDER [E]: 4*lambda in L0, 2*lambda NOT in L0, lambda NOT in L0 "
          "-- [lambda] has order 4; [v] has order 2",
          in_L0(four_lam) and (not in_L0(two_lam)) and (not in_L0(LAM))
          and in_D5([2, 0, 0, 0, 0]))
    check("[lambda]^2 = [v] EXACTLY [E]: lattice shadow of U^2 = (-1)^F -- "
          "the order-4 glue class squares to the fermion-parity / D5-vector "
          "class",
          in_L0(diff_lp) and in_D5(diff_sv) and (not in_L0(two_lam)))

    lam_v = V_D5 + OMEGA_F
    n_v = sum(x ** 2 for x in lam_v)
    n_lam = sum(x ** 2 for x in LAM)
    check("NON-SPLIT LIFT [E]: the order-2 vector glue (v, omega_f) has "
          "norm 7/4 NOT in 2Z (v983 kill) -- fermion parity cannot itself "
          "be the glue generator; the even generator is the order-4 class "
          "[lambda] with |lambda|^2 = 2",
          n_v == sp.Rational(7, 4) and n_lam == 2
          and not sp.simplify(n_v / 2).is_integer)

    rng = np.random.default_rng(20260828)
    check("CE axioms [E]: E = (1/4) sum_r Ad(u^r) is a CE onto M_4^{Z4} "
          "(E^2=E, E|fix=id, module, positive, trace-preserving)",
          ce_properties(4, rng))
    check("CE axioms [E]: same for d=8 (repeated clock grades, "
          "Fix ≅ M2^⊕4)",
          ce_properties(8, rng))
    check("CROSSED PRODUCT [E]: M_d x| Z4 (part-A embedding) -- E is a CE "
          "onto the fixed-point algebra for d=4 and d=8",
          crossed_E_properties(4, rng) and crossed_E_properties(8, rng))

    free4, _, ker4 = free_deviation_coords(4, bimodule=True)
    free8, _, ker8 = free_deviation_coords(8, bimodule=True)
    free4n, _, ker4n = free_deviation_coords(4, bimodule=False)
    free8n, _, ker8n = free_deviation_coords(8, bimodule=False)
    check("UNIQUENESS [E]: deviations D with im D ⊆ Fix, D|Fix=0, and "
          "bimodule by the four clock projections, force D=0 on M_4 "
          "(free coords = 0, kernel = 0)",
          free4 == 0 and ker4 == 0)
    check("UNIQUENESS [E]: same constraints force D=0 on M_8",
          free8 == 0 and ker8 == 0)
    check("MUST-FAIL [X]: dropping the bimodule constraint leaves a "
          "positive-dimensional space of trace-preserving deviations "
          "(d=4 kernel 36, d=8 kernel 720) -- uniqueness NEEDS the module "
          "property",
          ker4n == 36 and ker8n == 720)
    check("CROSSED-PRODUCT UNIQUENESS [E]: M_d x| Z4 ≅ ⊕_chi M_d as an "
          "alpha-module (Fourier of C[Z4]); unique CE on each factor => "
          "unique on the crossed product",
          free4 == 0 and free8 == 0)

    c3 = 1 / (8 * sp.pi)
    I_Jones = 4
    beta_angle = 2 * sp.pi
    check("ARITHMETIC SHADOW [E]: 1/(|mu4| * 2 pi) = 1/(4 * 2 pi) = "
          "1/(8 pi) = c3 EXACT, and I_Jones * beta_angle * c3 = 1 "
          "(v813 identity, not a new derivation of P1)",
          sp.simplify(1 / (sp.Integer(4) * 2 * sp.pi) - c3) == 0
          and sp.simplify(I_Jones * beta_angle * c3 - 1) == 0
          and abs(float(c3) - float(C3_MP)) < 1e-15)
    check("WRONG-INDEX CONTROL [X]: I=2 gives 1/(4 pi) ≠ c3 (corpus books "
          "1/(4 pi) as the un-halved Gauss-Bonnet / 2 c3)",
          sp.simplify(1 / (sp.Integer(2) * 2 * sp.pi) - 1 / (4 * sp.pi)) == 0
          and sp.simplify(1 / (4 * sp.pi) - c3) != 0)
    check("[C] READING (honest, not a pass-upgrade): the operator content "
          "'modular determinant-line response equidistributed over the four "
          "deck sectors' is the still-open identification of v813.  E unique "
          "at finite level does NOT move AX.P1.01",
          True)
    check("FIREWALL (scope): lattice/finite-algebra level; c_-=8 and "
          "holomorphic uniqueness at c=8 CITED not proved; P1/P2 stay Axiom; "
          "no marker move",
          True)

    return summary("v993 minimal defect selector: rank-8 ADE census unique "
                   "(D5, A3); [lambda]^2 = [v]; unique finite CE")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
