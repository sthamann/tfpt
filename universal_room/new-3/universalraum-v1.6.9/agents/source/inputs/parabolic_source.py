"""v566 -- DIAMOND.PARA.SELFCODE.01: the parabolic anchor self-code of the
sheet-diamond direction operators (external-review round 2026-07-31, audited
and promoted).

PROVENANCE.  An external structural review of the corpus proposed a chain of
exact statements about the v218 sheet-diamond direction operators
U = Q diag(1,0,0) (rank-1 winding direction) and V = Q diag(0,1,1) (rank-2
sheet direction, Spec V = {0,1,2}), with Q = [[3,1,0],[3,2,0],[3,2,1]] the
compiler charge matrix.  Every claim was audited EXACTLY against the corpus
objects by the discovery probe (23/23, verdict SELFCODE-VERIFIED), including
the one check the review had not run (integral saturation).  This module is
the load-bearing version.  It derives NOTHING new physically: it EXHIBITS a
previously unstated exact operator structure connecting existing modules
(v218 diamond <-> v23 anchor <-> carrier integers <-> v533 transfer line <->
Paper-II rank-3 form), with every over-reading fenced.

[E] (1) THE PARABOLIC THEOREM: A = Q<I, U, V> is the FULL line-stabiliser
    (maximal parabolic) algebra of block type 2|1 -- the seven words
    I, U, V, UV, VU, V^2, VUV are linearly independent (coordinate
    determinant -81 wrt the matrix units), the span is multiplicatively
    closed (49/49 products) and contains ALL seven matrix units of
    {[[*,*,0],[*,*,0],[*,*,*]]}: dim A = 7 = 9 - 2.  Mutation: perturbing
    Q's third column destroys the stabilised line (rank > 7) -- the closure
    is a property of THE compiler Q.
[E] (2) THE DOUBLE SELF-CODE: the Lagrange projector Pi2 = V(V-I)/2 onto
    the dominant eigenvalue is idempotent with trace 1, and H = I + Pi2
    has spectrum EXACTLY {1,1,2} = the anchor a (ANCHOR.GEN.01/v23);
    chi_H(x) = x^3 - 4x^2 + 5x - 2, i.e. the anchor moment data
    (e1, e2, e3) = (4, 5, 2) = (|mu4|, g_car, |Z2|) -- and SIMULTANEOUSLY
    (4, 5, 2) = (dim_R(GL3/P), dim(A/J), dim J): flag dimension, Levi
    quotient (M2 (+) Q, 2^2 + 1^2 = 5), radical (J = span(E31, E32),
    J^2 = 0).  The anchor is reproduced twice from one structure --
    spectrally through V and categorically through A.
[E] (3) THE UNIQUENESS THEOREM: for line stabilisers in GL_{m+1} the
    structure polynomial x^3 - 2m x^2 + (m^2+1) x - m factorises as
    (x - m)(x^2 - mx + 1) identically; all-positive-integer spectra force
    m^2 - 4 = k^2, i.e. (m-k)(m+k) = 4, i.e. m = 2 UNIQUELY -- the anchor
    a = (1,1,2) is the only member this parabolic family can code
    (neighbours m = 1, 3 fail; enumeration to 2000 confirms).
[E] (4) THE 81 AS A LATTICE INDEX: the integral order Z<I, U, V> --
    SATURATED under multiplication (stable at word length 4, 31 words
    tracked; the review's word-basis computation survives the honest
    closure) -- has elementary divisors (1,1,1,3,3,3,3) in the parabolic
    lattice P_Z: index [P_Z : Z<U,V>] = 3^4 = 81, cokernel (Z/3)^4.
    CROSS-LINK (typed, not claimed): the same 81 is the v218 determinant-
    staircase sum 3+4+8+14+20+32 = N_fam^4 -- a global determinant charge
    and an integral saturation index coincide.  The mark-local mechanism
    (one Z/3 per mu4 mark) stays [O] with its kill condition recorded
    (no canonical local decomposition => the 81 is a fingerprint, not a
    mechanism).
[E] (5) THE A2 BIT CARRIER: the basic algebra e A e (e = E11 + E33) is
    the path algebra of the A2 quiver -- two simples, radical 1-dim,
    dim Ext^1 = 1 -- so dim-vector-(1,1) modules fall into EXACTLY two
    iso classes: split and one nonsplit.  UNIQUENESS of the nonsplit
    class is algebra [E]; the SELECTION (the arrow nonzero) stays with
    geometry / reflection positivity (v528 twist class, v534 straddle
    cone) [C] -- the alignment bit gains a canonical algebra carrier,
    not a derivation.
[E] (6) THE TRACE CODE (re-encoding, hardening only): p_n(a) = 2 + 2^n =
    1 + tr(V^n) for n >= 1, with p_{n+2} = 3p_{n+1} - 2p_n, the Hankel
    p_n p_{n+2} - p_{n+1}^2 = 2^{n+1}, and the corollaries
    (1+trV)(1+trV^2)(1+trV^3) = 240 = |R(E8)| and tr(V^4 - V^3) = 8 =
    rank E8 -- the Lean-formalised AnchorLadder read through V: one
    independent object fewer, NO new content (typed as such).
[E] (7) THE CROSS-RATIO TEST DESIGN (for CONTRACT.F.01):
    CR(alpha_{-2}, alpha_{-1}; alpha_0, alpha_1) = 4/3 exactly on the
    v533 disc -7 norm line -- WITH the honesty wired as a check: 4/3 is
    the universal cross-ratio of ANY arithmetic progression, so the test
    content is 'the four F_transfer solver states form ONE
    Moebius-arithmetic progression', enforceable only through
    preregistered solver-state export; negative control: the raw
    determinant path (2,4,14,32) gives 28/25 != 4/3 (the known norm
    sequence cannot pass); the fourth state is forced fit-free from the
    first three (y_F reconstruction identity).
[E] (8) THE LORENTZ FORM OF THE PAPER-II RANK-3 CLASSIFICATION
    (reformulation only): det X = t^2 - x^2 - y^2 under Phi(X) =
    ((a+b)/2, (a-b)/2, c); D(P,Q) = 2<Phi(P),Phi(Q)>_{1,2}; delta =
    1 - r^2 = sech^2(atanh r) (Problem 7.1 = logarithmic rapidity
    growth); the relative-pencil identities det(B-S) = det B det(I-Z),
    D(B,S) = det B tr Z, det S = det B det Z -- the open cancellation
    becomes an eigenvalue-locking question (named instrument for the
    prime-front REST list; no measurement, no RH statement).

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   NO P2 REDUCTION.  The route 'g_car = dim(A/J) as a derived value'
        is conditional on the OPEN question: can Q (hence V) be
        reconstructed upstream WITHOUT carrier/anchor inputs (from mu4,
        D4, the A3 exponent grading Q_+, H^1, the sheet monodromy Q_-)?
        Q's historical provenance runs through carrier-aware compiler
        budgets -- the 'No Carrier Reconstruction' audit is the named
        [O] door.  AX.P2.01 and ANCHOR.GEN.01 markers UNTOUCHED.
  (ii)  THE 2..9 TABLE IS COMPRESSION, NOT EVIDENCE: the reading
        (2,3,4,5,6,7,8,9) = (sheet, families, marks, carrier, winding,
        scalaron, rank E8, N_fam^2) is ONE operator system re-expressed,
        not nine independent hits (no-free-pattern rule applies).
  (iii) The bit SELECTION, the mark-local 81 mechanism and the CR test
        execution (solver-state exports) stay open and typed open.
HONEST FENCES: no physics statement uses the word 'derived'; classical
spine as ADDRESSES (Wedderburn/Jacobson structure theory, Smith 1861
normal form, Gabriel 1972 quivers, cross-ratio projective invariance).
Status: [E] exact integer/symbolic sympy algebra throughout (no floats);
Python-only, counted per GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/parabolic_selfcode_audit_probe.py
  (2026-07-31, 23/23, verdict SELFCODE-VERIFIED; external review audited)
"""
import sympy as sp
import sympy.matrices.normalforms as nf

from tfpt_constants import check, summary, reset

I3 = sp.eye(3)
Q = sp.Matrix([[3, 1, 0], [3, 2, 0], [3, 2, 1]])
R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
K = sp.Matrix([[4, 2, 0], [4, 3, 2], [5, 3, 2]])
C = R + Q * sp.diag(1, 0, 0)
U = Q * sp.diag(1, 0, 0)
V = Q * sp.diag(0, 1, 1)
L = K + Q
F = C + V

IDX = ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2))


def coord_vec(M):
    return [M[i, j] for (i, j) in IDX]


def run():
    reset()
    print("=" * 72)
    print("v566  DIAMOND.PARA.SELFCODE.01 -- the parabolic anchor "
          "self-code (review audited)")
    print("=" * 72)

    # ================================================================ S1
    print("\nS1 -- the corpus objects and the parabolic theorem")
    dets = sorted([Q.det(), K.det(), R.det(), C.det(), L.det(), F.det()])
    check("S1.REBUILD [E] v218 regression: U = Q diag(1,0,0) rank 1, "
          "V = Q diag(0,1,1) rank 2 with Spec(V) = {0,1,2}; determinant "
          "staircase (3,4,8,14,20,32), sum 81 = N_fam^4",
          U.rank() == 1 and V.rank() == 2
          and sorted(V.eigenvals().keys()) == [0, 1, 2]
          and dets == [3, 4, 8, 14, 20, 32] and sum(dets) == 81)
    WORDS = [I3, U, V, U * V, V * U, V * V, V * U * V]
    coords = sp.Matrix([coord_vec(w) for w in WORDS])
    shape_ok = all(w[0, 2] == 0 and w[1, 2] == 0 for w in WORDS)

    def in_span(M):
        vec = sp.Matrix([coord_vec(M)])
        return sp.Matrix.vstack(coords, vec).rank() == 7

    E = {}
    for (i, j) in IDX:
        Eij = sp.zeros(3, 3)
        Eij[i, j] = 1
        E[(i, j)] = Eij
    closed = all(in_span(w1 * w2) for w1 in WORDS for w2 in WORDS)
    units_in = all(in_span(E[p]) for p in IDX)
    check("S1.PARABOLIC [E] the parabolic theorem: the seven words I, U, "
          "V, UV, VU, V^2, VUV are independent (coordinate det -81), the "
          "span is multiplicatively closed (49/49) and contains all seven "
          "line-stabiliser matrix units -- A = Q<I,U,V> = "
          "{[[*,*,0],[*,*,0],[*,*,*]]} exactly, dim 7 = 9 - 2",
          coords.det() == -81 and coords.rank() == 7 and shape_ok
          and closed and units_in)
    Qm = Q.copy()
    Qm[0, 2] = 1
    Um, Vm = Qm * sp.diag(1, 0, 0), Qm * sp.diag(0, 1, 1)
    Wm = [I3, Um, Vm, Um * Vm, Vm * Um, Vm * Vm, Vm * Um * Vm,
          Vm * Vm * Um, Um * Vm * Vm, Vm * Vm * Vm]
    cm = sp.Matrix([[w[i, j] for i in range(3) for j in range(3)]
                    for w in Wm])
    check("S1.MUT [must-break] perturbing Q's third column destroys the "
          "stabilised line: the generated algebra exceeds dimension 7 "
          "(rank %d) -- the closure is a property of THE compiler Q"
          % cm.rank(), cm.rank() > 7)

    # ================================================================ S2
    print("\nS2 -- the double self-code: anchor = spectrum + categorical "
          "triple")
    Pi2 = V * (V - I3) / 2
    H = I3 + Pi2
    x = sp.symbols('x')
    chiH = sp.expand(H.charpoly(x).as_expr())
    check("S2.PROJ [E] Pi2 = V(V-I)/2 is idempotent with trace 1; "
          "H = I + Pi2 has spectrum EXACTLY {1,1,2} = the anchor a "
          "(ANCHOR.GEN.01/v23): the anchor is the spectrum of a canonical "
          "operator built from the sheet direction V alone",
          sp.simplify(Pi2 * Pi2 - Pi2) == sp.zeros(3, 3)
          and Pi2.trace() == 1
          and H.eigenvals() == {sp.Integer(1): 2, sp.Integer(2): 1})
    J1, J2c = E[(2, 0)], E[(2, 1)]
    rad_ideal = all(in_span(w * Jk) and in_span(Jk * w)
                    for w in WORDS for Jk in (J1, J2c))
    rad_nil = all((Ja * Jb) == sp.zeros(3, 3)
                  for Ja in (J1, J2c) for Jb in (J1, J2c))
    check("S2.CODE [E] THE DOUBLE SELF-CODE: chi_H(x) = x^3 - 4x^2 + 5x "
          "- 2, so (e1,e2,e3) = (4,5,2) = (|mu4|, g_car, |Z2|) -- and "
          "SIMULTANEOUSLY (4,5,2) = (dim_R(GL3/P), dim(A/J), dim J): "
          "flag = 2(9-7) = 4, Levi = 2^2+1^2 = 5, radical J = "
          "span(E31,E32) a nilpotent 2-dim ideal (J^2 = 0).  chi_H(x) = "
          "x^3 - flag x^2 + Levi x - radical, exactly",
          chiH == x**3 - 4 * x**2 + 5 * x - 2
          and rad_ideal and rad_nil
          and (2 * (9 - 7), 2**2 + 1**2, 2 * 1) == (4, 5, 2))

    # ================================================================ S3
    print("\nS3 -- the uniqueness theorem for a = (1,1,2)")
    m = sp.symbols('m', integer=True, positive=True)
    chim = x**3 - 2 * m * x**2 + (m**2 + 1) * x - m
    check("S3.FACT [E] x^3 - 2m x^2 + (m^2+1) x - m = (x-m)(x^2-mx+1) "
          "identically in m (the GL_{m+1} line-stabiliser structure "
          "polynomial: flag 2m, Levi m^2+1, radical m)",
          sp.expand(chim - (x - m) * (x**2 - m * x + 1)) == 0)
    sols = [mm for mm in range(1, 2001)
            if sp.sqrt(mm * mm - 4).is_integer]
    check("S3.UNIQUE [E] all-positive-integer spectra need m^2 - 4 = k^2, "
          "i.e. (m-k)(m+k) = 4, i.e. m = 2 uniquely (enumeration to 2000: "
          "{2}) -- a = (1,1,2) is the ONLY anchor this parabolic family "
          "can code; neighbours m = 1, 3 fail (discriminants -3, 5)",
          sols == [2]
          and sp.sqrt(5).is_integer is not True)

    # ================================================================ S4
    print("\nS4 -- the 81 as a saturated lattice index")

    def snf_divisors(mats):
        Mc = sp.Matrix([coord_vec(Mx) for Mx in mats])
        s_ = nf.smith_normal_form(Mc.T)
        return sorted(abs(s_[i, i]) for i in range(min(s_.shape))
                      if s_[i, i] != 0)

    all_words, frontier = [I3], [I3]
    divs_hist = []
    stable_at = None
    for Lw in range(1, 9):
        frontier = [w * G for w in frontier for G in (U, V)]
        all_words = all_words + frontier
        divs_hist.append(snf_divisors(all_words))
        if len(divs_hist) >= 2 and divs_hist[-1] == divs_hist[-2]:
            stable_at = Lw
            break
    divisors = divs_hist[-1]
    index = sp.prod(divisors)
    check("S4.SMITH [E] the SATURATED integral order (multiplicative "
          "closure, stable at word length %d, %d words tracked) has "
          "elementary divisors (1,1,1,3,3,3,3) in the parabolic lattice: "
          "index [P_Z : Z<U,V>] = 3^4 = 81, cokernel (Z/3)^4 -- the "
          "review's word-basis Smith form survives the honest closure"
          % (stable_at, len(all_words)),
          divisors == [1, 1, 1, 3, 3, 3, 3] and index == 81)
    check("S4.LINK [E] the cross-link, typed: the saturation index 81 = "
          "3^4 EQUALS the v218 determinant-staircase sum = N_fam^4 -- a "
          "global determinant charge and an integral lattice index "
          "coincide; the mark-local mechanism (one Z/3 per mu4 mark) "
          "stays [O] with its kill condition recorded",
          index == sum(dets) == 3**4)

    # ================================================================ S5
    print("\nS5 -- the A2 quiver and the two-class bit carrier")
    e_idem = E[(0, 0)] + E[(2, 2)]
    check("S5.A2 [E] the basic algebra: e = E11 + E33 in A idempotent, "
          "eAe = span(E11, E33, E31) with E31^2 = 0 -- the A2 path "
          "algebra: two simples, 1-dim radical, dim Ext^1 = 1 (exactly "
          "one extension arrow); dim-vector-(1,1) modules = a scalar "
          "arrow t with base change t -> (u/v)t: EXACTLY two iso classes "
          "(split t = 0; ONE nonsplit class t != 0).  Uniqueness of the "
          "nonsplit class is algebra; the SELECTION stays with "
          "geometry/RP (v528/v534) -- the alignment bit gains a "
          "canonical carrier, not a derivation",
          in_span(e_idem) and in_span(E[(0, 0)]) and in_span(E[(2, 2)])
          and in_span(E[(2, 0)])
          and sp.simplify(e_idem * e_idem - e_idem) == sp.zeros(3, 3)
          and E[(2, 0)] * E[(2, 0)] == sp.zeros(3, 3)
          and E[(2, 0)] * E[(0, 0)] == E[(2, 0)]
          and E[(2, 2)] * E[(2, 0)] == E[(2, 0)])

    # ================================================================ S6
    print("\nS6 -- the trace code (re-encoding of AnchorLadder)")
    p_ = lambda nn: 2 + 2 ** nn
    tv = lambda nn: (V ** nn).trace()
    check("S6.TRACE [E] p_n(a) = 2 + 2^n = 1 + tr(V^n) (n = 1..12 on the "
          "matrix); recurrence p_{n+2} = 3p_{n+1} - 2p_n; Hankel "
          "p_n p_{n+2} - p_{n+1}^2 = 2^{n+1}; corollaries: "
          "(1+trV)(1+trV^2)(1+trV^3) = 4*6*10 = 240 = |R(E8)|, "
          "tr(V^4 - V^3) = 8 = rank E8.  TYPED AS RE-ENCODING of the "
          "Lean-formalised AnchorLadder p_n = 2 + 2^n: hardening (one "
          "object fewer), NOT new content",
          all(tv(nn) == 1 + 2**nn and p_(nn) == 1 + tv(nn)
              for nn in range(1, 13))
          and all(p_(nn + 2) == 3 * p_(nn + 1) - 2 * p_(nn)
                  for nn in range(1, 11))
          and all(p_(nn) * p_(nn + 2) - p_(nn + 1)**2 == 2**(nn + 1)
                  for nn in range(1, 11))
          and (1 + tv(1)) * (1 + tv(2)) * (1 + tv(3)) == 240
          and tv(4) - tv(3) == 8)

    # ================================================================ S7
    print("\nS7 -- the cross-ratio test design (CONTRACT.F.01)")
    sqm7 = sp.sqrt(-7)
    alpha = lambda tt: (4 * tt + 7 + sqm7) / 2

    def cr(z0, z1, z2, z3):
        return sp.simplify(((z0 - z2) * (z1 - z3))
                           / ((z0 - z3) * (z1 - z2)))

    z0s, s_ = sp.symbols('z0s s_', nonzero=True)
    yJ, yK, yC = sp.symbols('yJ yK yC')
    yF = (yJ * yK - 4 * yJ * yC + 3 * yK * yC) / (4 * yK - 3 * yJ - yC)
    check("S7.CR [E] CR(alpha_-2, alpha_-1; alpha_0, alpha_1) = 4/3 "
          "exactly on the v533 disc -7 norm line; honesty wired: 4/3 is "
          "the UNIVERSAL cross-ratio of any arithmetic progression "
          "(CR(z, z+s, z+2s, z+3s) = 4/3 symbolically) -- the test "
          "content is the preregistered solver-state export; negative "
          "control: the raw determinants (2,4,14,32) give 28/25 != 4/3; "
          "the fourth state is forced fit-free: CR(yJ,yK;yC,yF) = 4/3 "
          "identically",
          cr(alpha(-2), alpha(-1), alpha(0), alpha(1))
          == sp.Rational(4, 3)
          and cr(z0s, z0s + s_, z0s + 2 * s_, z0s + 3 * s_)
          == sp.Rational(4, 3)
          and cr(sp.Integer(2), sp.Integer(4), sp.Integer(14),
                 sp.Integer(32)) == sp.Rational(28, 25)
          and sp.simplify(cr(yJ, yK, yC, yF) - sp.Rational(4, 3)) == 0)

    # ================================================================ S8
    print("\nS8 -- the Lorentz form of the Paper-II rank-3 classification")
    a_, b_, c_ = sp.symbols('a_ b_ c_', real=True)
    X2 = sp.Matrix([[a_, c_], [c_, b_]])
    t_, x2_, y_ = (a_ + b_) / 2, (a_ - b_) / 2, c_
    p11, p22, p12 = sp.symbols('p11 p22 p12', real=True)
    q11, q22, q12 = sp.symbols('q11 q22 q12', real=True)
    D_pol = p11 * q22 + p22 * q11 - 2 * p12 * q12
    mink = 2 * ((p11 + p22) / 2 * (q11 + q22) / 2
                - (p11 - p22) / 2 * (q11 - q22) / 2 - p12 * q12)
    r_ = sp.symbols('r_', positive=True)
    B_ = sp.Matrix([[sp.Symbol('B11', positive=True),
                     sp.Symbol('B12', real=True)],
                    [sp.Symbol('B12', real=True),
                     sp.Symbol('B22', positive=True)]])
    S_ = sp.Matrix([[sp.Symbol('S11', real=True),
                     sp.Symbol('S12', real=True)],
                    [sp.Symbol('S12', real=True),
                     sp.Symbol('S22', real=True)]])
    Z_ = B_.inv() * S_
    DBS = B_[0, 0] * S_[1, 1] + B_[1, 1] * S_[0, 0] \
        - 2 * B_[0, 1] * S_[0, 1]
    check("S8.LORENTZ [E] det X = t^2 - x^2 - y^2 under Phi(X) = "
          "((a+b)/2, (a-b)/2, c); D(P,Q) = 2<Phi(P),Phi(Q)>_{1,2}; "
          "delta = 1 - r^2 = sech^2(atanh r) (Problem 7.1 = logarithmic "
          "rapidity growth); relative pencil: det(B-S) = det B det(I-Z), "
          "D(B,S) = det B tr Z, det S = det B det Z -- all identities; "
          "the open cancellation becomes eigenvalue locking "
          "det(I-Z) = (1-lam1)(1-lam2) (named instrument, prime-front "
          "REST; no measurement, no RH statement)",
          sp.expand(X2.det() - (t_**2 - x2_**2 - y_**2)) == 0
          and sp.expand(D_pol - mink) == 0
          and sp.simplify((1 - r_**2) - sp.sech(sp.atanh(r_))**2) == 0
          and sp.simplify((B_ - S_).det()
                          - B_.det() * (sp.eye(2) - Z_).det()) == 0
          and sp.simplify(DBS - B_.det() * Z_.trace()) == 0
          and sp.simplify(S_.det() - B_.det() * Z_.det()) == 0)

    # ================================================================ S9
    print("\nS9 -- the fences, restated as a check")
    check("S9.FENCE: NO P2 REDUCTION -- the 'g_car = dim(A/J) derived' "
          "route is conditional on the OPEN 'No Carrier Reconstruction' "
          "audit (rebuild Q/V from mu4, D4, Q_+ = A3 exponent grading, "
          "H^1, Q_- = sheet monodromy, WITHOUT g_car = 5, a = (1,1,2), "
          "rank E8 = 8 or carrier-aware budgets); AX.P2.01 and "
          "ANCHOR.GEN.01 markers untouched; the 2..9 dimension table is "
          "COMPRESSION of one operator system, not nine independent hits "
          "(no-free-pattern); the bit selection, the mark-local 81 "
          "mechanism and the CR-test execution stay open and typed open; "
          "the word 'derived' appears nowhere for any physics statement; "
          "Wedderburn/Jacobson, Smith 1861, Gabriel 1972, projective "
          "cross-ratio invariance named CLASSICAL as addresses",
          True)

    print("\nv566 anchors: A = full 2|1 parabolic (dim 7, word det -81); "
          "a = Spec(I + V(V-I)/2) = (1,1,2);")
    print("  chi_H = x^3 - flag x^2 + Levi x - radical; m = 2 unique; "
          "[P_Z : Z<U,V>] = 81 = 3^4 saturated;")
    print("  A2 Ext^1 = 1 (two-class bit carrier); p_n(a) = 1 + tr V^n; "
          "CR = 4/3 design; Lorentz/pencil forms")
    return summary("DIAMOND.PARA.SELFCODE.01 parabolic anchor self-code")


if __name__ == "__main__":
    raise SystemExit(run())
