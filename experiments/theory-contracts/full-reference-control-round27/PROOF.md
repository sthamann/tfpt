# Full charge-diagonal reference, without a charge-entropy sign penalty

2026-09-07. NON-RH, unpromoted analytic result for the SAME finite-regulator
g=0 scalar/charge model as Round26. This is not a new microscopic TFPT
parent, an efficient sign cure, or closure of T1-T8.

## 1. Scope and the reference that must not be compressed away

Fix a spatial torus L>=3, N=L^3, a,m>0, u,nu>=0, J>=0, delta>0,
integer T>=3 and beta=T delta. Keep every charge in Z^8 at every site.
Work on any fixed total-charge sector for Sections 1-4. The explicit
Gaussian charge-tail envelope in Section 5 is restricted to the neutral
sector. Other independent free species cancel in the ratios.

Use exactly the potential V, scalar kinetic K_phi and signed hopping of
[Round26](../history-sum-control-round26/PROOF.md):

    r=48N, kappa=rJ, theta=beta kappa,
    H_hop=kappa I-J A_sign,  0<=H_hop<=2 kappa I,
    Q=exp(-delta V/2) exp[-delta(K_phi+H_hop)] exp(-delta V/2).

Scalar kinetic and hopping commute, not generally either one with V.
Define

    S=exp(-delta K_phi/2) exp(-delta V/2),
    Q_D=S* S, C=S S*, Z_D=Tr Q_D^T=Tr C^T,
    Q=S* exp(-delta H_hop) S, Z=Tr Q^T.

Q_D is the complete charge-diagonal transfer on the same Hilbert space.
In particular Z_D sums ALL constant charge profiles in the chosen sector,
including their charge-dependent scalar determinants. It is not the
zero-charge scalar partition and is not obtained by setting u to zero.
The coercivity and mass argument in Round26 gives 0<Z_D<infinity and
trace class Q_D,C,Q. Each nonempty total-charge sector has a positive
constant-profile contribution, even if its zero profile is unavailable.

## 2. Pinching supplies the missing denominator

For each complete charge profile n, let P_n be its projection, leaving
the scalar space intact. Every elementary actual hop changes n, so
<n|A_sign|n>=0. Scalar Jensen on its spectral probability measure gives

    p_n=<n|exp(-delta H_hop)|n> >= exp(-delta kappa).
    P_n Q P_n=p_n Q_D(n).

This is scalar spectral Jensen, not operator convexity of the exponential.
Pinching into all charge blocks contracts every Schatten T norm:

    Tr Q^T >= sum_n Tr(P_n Q P_n)^T
             >= exp(-theta) sum_n Tr Q_D(n)^T
             = exp(-theta) Z_D.                              (1)

For completeness, finite-block pinching is the average of conjugations
by the diagonal root-of-unity unitary; triangle inequality and unitary
invariance prove contractivity. For any finite set of profiles, include
its complement as one additional block, discard the complement's
nonnegative trace contribution, and then increase the finite set.
Monotone convergence of these nonnegative numbers proves (1) for the
countably infinite charge carrier. No finite charge truncation is silently
substituted for the Hilbert space.

The upper bound Q<=Q_D gives Z<=Z_D by ordered compact eigenvalues.
Neither this nor (1) uses operator monotonicity of X -> X^T, which would
be false. In particular exp(-delta kappa) Q_D<=Q is NOT asserted: a
matrix can have adequate diagonal blocks while still failing that order.

## 3. Absolute words and the common-reference Holder bound

Expand each hopping exponential into its ordered elementary words,
retaining exp(-theta). Replace signs by bare charge translations only
in an absolute majorant. A bare word U_j is unitary, preserves the total
charge sector, and acts trivially on the scalar coordinates. The charge
diagonal C has nonnegative scalar integral kernels. Cyclic trace and
the expansion Q_word=S* U_j S therefore give, for any tuple of words,

    0 <= Tr(U_1 C ... U_T C)
      <= product_j ||U_j C||_T = Tr C^T = Z_D.                (2)

The left side sums the positive scalar weights over every initial
profile for the given tuple. It equals the sum of moduli of the signed
profile-resolved weights: each original monomial contributes a unit
phase, and the scalar kernel is nonnegative. It is not the modulus of
an already cancelled trace. Nonclosed tuples contribute zero.

For total elementary order k, there are r^k word choices and the slice
allocation weights sum to T^k/k!. Thus (2) bounds the whole absolute
order-k contribution by exp(-theta) theta^k Z_D/k!. Tonelli applies to
the nonnegative expansion; its summed finite majorant then justifies
the signed rearrangement. Consequently

    exp(-theta) Z_D <= Z <= Z_abs <= Z_D,
    1 <= Z_abs/Z <= exp(theta).                              (3)

Alternatively, the unsigned hopping transfer has 0<=exp(-delta H_+)<=I,
so its trace partition Z_abs is bounded above by Z_D. This independent
positive-operator comparison agrees with (2). Absolute here is always
word/profile resolved; an entry-resummed absolute sum can only be smaller.

The artificial factor Theta(beta) of Round26 has disappeared from the
sign bound, without changing the original signs or discarding any charge.
At J=0 the bound is exactly 1. At J>0 it still grows as exp(48 beta N J).
The negative original loop of Round26 survives unchanged. Equation (3)
is an upper bound on cancellation, not a measured average sign and not
a proof of polynomial simulation cost.

## 4. Summed memory and hopping errors

Retain the exact eliminated determinant from Round25. Its uniform
historywise scalar ratio bound in Round26 is |Z_phi,R/Z_phi-1|<=a_R,
where a_R=exp(B_R)-1 and

    B_R=epsilon_R |S_ret| T g_m(0)/[2(1-eta_R)],
    eta_R=epsilon_R/(delta m^2)<1.

The symbol S_ret denotes retained spatial sites, not the operator S.
Equation (3) now gives the summed relative memory error

    rho_memory <= exp(theta) [exp(B_R)-1].                   (4)

For TOTAL hop order P, P+2>theta, (2) and (1) give

    rho_hops <= sum_(k>P) theta^k/k!
              <= theta^(P+1)/(P+1)! /[1-theta/(P+2)].        (5)

The Poisson exp(-theta) factor cancels the denominator's exp(theta)
in (5). There is no Theta(beta), but neither is it valid to retain an
additional exp(-theta) suppression in this relative bound.

## 5. A charge-tail bound from the same reference

Let R_K be the charge projection onto max_(x,a)|n_(x,a)|>K and define

    p_D(K)=Tr(R_K C^T)/Z_D.

This is a positive reference probability, not an assumed sampling oracle.
R_K commutes with C. For an insertion at one of the sampled boundaries,
Schatten Holder applied to (R_K C) and T-1 copies of C gives an absolute
word trace at most Z_D p_D(K)^(1/T). Sum the positive word coefficients
and use a union bound over the T sampled boundaries:

    rho_charge <= T exp(theta) p_D(K)^(1/T).                 (6)

Inside a slice word the intermediate charges are NOT cut off by (6).
Their phases and translations remain exact. Only sampled profiles are
restricted when using this omission bound.

In the neutral sector the zero profile gives Z_D>=Z_phi,0. Also, for a
constant profile, Z_phi[n]<=Z_phi,0 and D(n)>=a_c||n||^2, a_c=1/(62N).
Splitting HALF THE TOTAL beta in the reference trace, not a time slice,
therefore gives

    p_D(K) <= min(1, exp[-beta a_c(K+1)^2/2] Theta(beta/2)),
    Theta(s)=Tr_neutral exp(-sD)
             <= [1+sqrt(pi/(s a_c))]^(8N).

Taking the T-th root yields the explicit version

    rho_charge <= T exp(theta) exp[-delta a_c(K+1)^2/2]
                  Theta(beta/2)^(1/T).                      (7)

Both the reduced entropy exponent 1/T and the resulting delta, rather
than beta, in the decay are essential. Equation (7) is still conservative
and is not a dimension-independent charge concentration theorem. For a
nonneutral sector retain (6) and supply its own certified p_D; do not
reuse the neutral zero-profile denominator.

Apply the charge/word restriction first and the memory approximation
on the retained paths second. Its error is bounded by a_R times the
absolute retained sum, itself at most Z_abs. Thus their sum, not a
product that double-counts omitted paths, bounds the total:

    rho <= rho_charge + rho_hops + rho_memory.

If rho<1, the approximate partition remains positive. For a selfadjoint
one-time charge observable of norm<=1, positivity of the EXACT Q^T
gives the normalized error <=2rho/(1-rho). This does not cover arbitrary
multi-time signed functionals, scalar insertions, or establish reflection
positivity of the memory-truncated weights.

## 6. Verification and boundaries

The accompanying checker uses exact noncommuting block-matrix witnesses,
the actual pinned E8 negative loop, and adversarially wrong inequality
directions. These are regressions of the formulas, not a finite proof of
the general infinite-carrier statement. The argument above supplies that
statement; it has not been independently certified by a proof assistant.

Primary-source context: positive unital trace-preserving maps and Schatten
contractivity are treated by [Perez-Garcia, Wolf, Petz and Ruskai](https://arxiv.org/abs/math-ph/0601063).
The distinction between scalar, trace and operator Jensen is discussed by
[Hansen and Pedersen](https://arxiv.org/abs/math/0204049).
Our pinching proof is the explicit unitary-average argument above; the
TFPT-specific full-reference application is derived here, not attributed
to those papers.

This remains a finite spatial and Euclidean-time regulator. No equality
with the unsliced heat kernel, uniform infinite-volume limit, real-time
reconstruction, chiral matter completion, gravity or empirical prediction
is proved. No RH claim.
