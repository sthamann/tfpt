# The missing HH rule is the onsite DET-wall premise: exact statements

10 September 2026. NON-RH. Conditional on the v1027 signed DET wall
(ledger `CHIRAL4D.MIRROR.SIGNED.CAR.01`, status `[C]`, pinned by SHA-256 in
`checker.py`). Nothing below derives that premise from P1/P2, selects a
vacuum or a continuum, or closes T1–T8.

## 0. Inputs

Native square (Universalraum consolidated report 2026-09-10, Q047 §1;
identical to `ground-state-loop-response/README.md`): two species L,H per
site, U(1) rotors on links, couplings

    a = 1/12 (LL nn), b = 1/24 (LH nn), c = 1/576 (LL two-link),
    epsilon_L = 1/96 (LL onsite backtrack, ambient degree 6), M = 4 (H onsite),
    delta = M - epsilon_L = 383/96, no HH nearest-neighbour term.

v1027 signed wall (`signed_block`), fixed c-number background A:

    h(A) = [[A + lam g^2 A^2, lam g A], [lam g A, (Delta + lam) I]]
         = (A (+) Delta I) + lam W^* W,        W = (g A, I).          (0.1)

The second form is the structural reading: free part = mobile low kernel A
plus onsite DET parent Delta (v1027: "the additive parent is Delta*N_a",
N_a onsite because the DET rotation is an onsite even unitary); interaction
= lam times the square of the matched current g A psi_L + psi_H, in which the
high species enters as the unit reference.

## 1. The native couplings are the wall coefficients (exact)

Put A = a Adj with Adj the gauge-covariant adjacency and (lam, g, Delta) =
(1, 1/2, 3). Expanding (0.1) in powers of Adj:

    LL: a Adj + lam g^2 a^2 Adj^2      -> nn = a, two-link = lam g^2 a^2 = c,
                                          backtrack onsite = deg * lam g^2 a^2 = 6c = epsilon_L
    LH: lam g a Adj                    -> b = lam g a
    HH: (Delta + lam) I                -> M = Delta + lam, no Adj power.

Hence the five relations

    b = lam g a,  c = lam g^2 a^2,  epsilon_L = 6c,  M = Delta + lam,  delta = M - epsilon_L,

and the parameter-free consequences b^2 = lam c and b/a = lam g. With the
pinned numbers: b^2 = 1/576 = c, b/a = 1/2, 6c = 1/96, M = 4, delta = 383/96.
`checker.py` verifies this symbolically and on the actual `signed_block` of
the 4-cycle adjacency (block error 0; the induced square has backtrack 2c,
the ambient parent 6c — the native square keeps the ambient value, as
Q050 §1 records).

Consequence for the "half ratio": b/a = 1/2 is the wall coupling lam g. It is
not a variational output; the minimax theorems of Q046/Q047 characterize the
same number under a different, explicitly declared objective.

## 2. HH transport vanishes iff the high species is onsite in D_0 and R

General wall class: free part A (+) D_0(A), current W = (g A, R(A)), with
D_0, R polynomials in A (any finite range). Then

    h_HH = D_0(A) + lam R(A)^2.                                          (2.1)

Proposition. h_HH is A-independent iff D_0 + lam R^2 is a constant. In
particular D_0 = Delta (onsite DET parent) and R = 1 (unit reference) give
h_HH = Delta + lam = M and no HH hopping of any range. Conversely, a
dispersive current R = r0 + r1 A alone produces the HH nearest-neighbour term
2 lam r0 r1 A; a dispersive free part D_0 alone produces it directly.

Proof: expand (2.1); the coefficients of A^k, k >= 1, are listed in
`validation.json` (`hh_structure`). Setting all nonconstant coefficients of
D_0 and R to zero annihilates them; keeping r1 leaves 2 lam r0 r1.

So the missing rule is exactly: *the high species has no spatial transport
in either the free DET parent or the wall current.* This is the declared
DET-CAR premise, now isolated as the single source-side hypothesis behind
h = 0. It also fixes the microscopic range class asked for in Q050 §7:
LL range <= 2 links (A + lam g^2 A^2), LH range 1 (lam g A), HH range 0.

## 3. The signed-determinant degree does not supply the rule (negative control)

For the general class of §2,

    det h = A [ D_0 + lam R^2 + lam g^2 A D_0 ]                          (3.1)

exactly (the lam^2 g^2 A^2 R^2 terms cancel). The v1027 property "det h =
M A (1 + c A), quadratic in A" therefore only constrains the bracket to be
linear in A. The family

    D_0 = M0 - (r1^2/g^2) A,   R = r0 + r1 A

keeps det h quadratic in A with the factor A (`checker.py`:
`det_degree = 2`, linear coefficient M0 + lam r0^2) while

    h_HH = M0 + lam r0^2 + r1 (2 g^2 lam r0 - r1)/g^2 * A + lam r1^2 A^2

is dispersive. Hence any attempt to derive h = 0 from the signed-determinant
degree alone fails; the onsite premise of §2 is genuinely additional.

## 4. Cubic coefficient and the Q050 identification

For a scalar spectral value x the low branch of (0.1) is

    f(x) = x + [lam g^2 - (lam g)^2/M] x^2 - [(lam g)^2/M^2] x^3 + O(x^4).

With (lam, g, M) = (1, 1/2, 4): f = x + (3/16) x^2 - (1/64) x^3 + O(x^4),
matching Q050 eq. (2) at xi = 0. In Q050's nearest-neighbour family the
cubic coefficient selects xi = 1 + 64 c3; the wall value c3 = -1/64 gives
xi = 0. Read correctly: this is *not* an independent derivation of xi = 0
(the wall already has a scalar high block); it shows that the DET-wall
premise and the low-energy identification are consistent and that a
compiler derivation of c3 = -(lam g)^2/M^2 would be equivalent to a
derivation of the onsite premise.

## 5. The identifying link-quadrature slope

On span{u, v = T u} with T the oriented HH transport and Y = i(T - T^*),
the only matrix element connecting u and v is the labelled HH coefficient
<v, K_xi u> = xi a (Q050 §5). Exactly,

    d/dt <U(t)u, Y U(t)u>|_{t=0} = i <u, [K_xi, Y] u> = -2 xi a = -xi/6.

Under the wall premise xi = 0, so the initial slope is predicted to vanish
before any Hamiltonian value is inserted; the finite-time original response
(-1.44e-7 at t = 0.1 in Q049) remains an indirect two-step effect and is not
contradicted.

## 6. Minimax versus wall (they are different principles)

Q048 gives ||R_x P||^2 = 2(a-h)^2 + 8[b-(a+h)/2]^2 + 4c^2. Restricting to
the wall family (h = 0, b = g a, c = g^2 a^2) yields

    J(g) = a^2 [ 2 + 8 (g - 1/2)^2 + 4 g^4 a^2 ],   J'(1/2) = 2 a^4 = 1/10368 != 0.

The minimax point is g* = 1/2 - g*^3 a^2 + O(a^4) = 0.4991364... , not 1/2.
So the worst-order-defect principle does not reproduce the wall coupling
exactly once c is tied to g; the two principles agree only at O(a^2). The
wall gives exactly 1/2.

## 7. What remains fundamental

The single remaining obligation for the HH rule is the onsite character of
the DET species (free parent Delta N_a and unit-reference current). It is
declared, hash-pinned and `[C]` in the verification suite; it is not derived
here from c3 = 1/(8 pi) or g_car = 5. A derivation of that premise would at
once fix b/a, c = b^2, epsilon_L = 6c, the range class, c3 and the zero
slope. No physical drive, apparatus or state selection is supplied.
