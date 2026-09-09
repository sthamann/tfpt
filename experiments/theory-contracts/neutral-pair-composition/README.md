# Neutral composition on the actual Gaussian-dressed source

2026-09-08. Finite Slater identities and diagnostics; no completed charged
scaling field, physical four-dimensional reconstruction or RH claim.

## Construction and exact cancellation

Use the unchanged pinned [Gaussian source](../gaussian-vacuum-filter/README.md),
sector r=1, Ny=8, mass 1, top strip width 2, delta=4 N^(-3/4).
For arc length a let A_a select 0<=x<a in that strip and put

    F_a = Phi_delta(pi A_a + R), R=pi x/N,
    U_a = G exp(i F_a), G=exp(-i R).

All these maps have the same destination sector. The neutral pair is

    W_ab = U_a* U_b = exp(-i F_a) exp(i F_b).

Thus the external ramp G cancels **on the complete finite one-particle
space**, not just after edge projection. The ramp R inside F_a does not
cancel by subtraction: filtering destroys commutativity of the original
diagonal generators. In particular W_ab is not exp(i(F_b-F_a)). The
actual N=64 half-arc Frobenius difference is 1.22049.

Composition and reversal are exact: W_ab W_bc=W_ac and W_ba=W_ab*.
This is a groupoid composition identity of unitaries, not a new physical
equation of motion. Importantly, vacuum expectations do not inherit its
multiplicativity.

## Full finite vacuum expectation, including its phase

Let V_- be occupied orthonormal columns for the unchanged H_r, and let
Omega be their exterior product. Finite exterior algebra gives

    C_ab = <Omega, Gamma(W_ab) Omega>
         = det(V_-* W_ab V_-).

In the H_r eigenbasis this is the occupied block of exp(-iF_a)exp(iF_b).
It uses **all occupied bulk and edge states**, not a hand-selected edge
determinant. The matrix (C_ab) is a positive Gram matrix because it is
the overlap matrix of Gamma(U_a)Omega. Its diagonal is 1. Positivity
alone does not provide a nontrivial scaling limit or a local field net.

The determinant follows directly by multilinearity of exterior products.
Tests independently sum their minors in small systems. The general
Fock-trace connection is classical: [Klich (2002)](https://arxiv.org/abs/cond-mat/0209642).
The stored phase is the phase of this specified finite second quantization;
it is not already the normalized microscopic lattice-vertex cocycle.

## A controlled connected-log expansion

Write P for the occupied projection and A=P W_ab P restricted to ran(P).
Unitarity implies the exact identity

    A* A = I-L, L=P W_ab* (I-P) W_ab P >= 0.

For r=||L||<1,

    log |C_ab| = (1/2) Tr log(I-L)
               = -(1/2) sum_(k>=1) Tr(L^k)/k.

This is an ordinary convergent spectral expansion, not a fitted
asymptotic series. After M terms its positive loss remainder is bounded by

    0 <= -log|C_ab| - (1/2) sum_(k=1..M) Tr(L^k)/k
       <= Tr(L) r^M / (2(M+1)(1-r)).

Proof: diagonalize the positive finite L. Bound each higher trace by
Tr(L) r^(k-1), then use 1/k <= 1/(M+1) and sum the geometric tail.
If r=1 the determinant vanishes and this finite-log formulation must be
replaced; the checker rejects that case. Numerical radii and tails in
diagnostics.json are floating evaluations, not interval certificates.

## What the new computation establishes

Half-arc pair a=0,b=N/2, one complex-fermion copy:

| N | abs(C_ab) | -log abs(C_ab) | Bottom three-mode error, Frobenius norm | Top three-mode error, Frobenius norm |
| --- | ---: | ---: | ---: | ---: |
| 8 | 0.784695 | 0.242460 | 0.0115068 | 1.18947 |
| 16 | 0.755972 | 0.279751 | 0.00195083 | 1.17858 |
| 32 | 0.719185 | 0.329637 | 0.000541530 | 1.11515 |
| 64 | 0.684686 | 0.378795 | 0.0000101122 | 1.03600 |

The bottom error is measured against identity and the top error against
the raw interval string, on the three explicitly sourced quasimodes.
These are not full bottom-subspace operator norms or determinant
factorization errors. At N=64 the eight-term log expansion has remainder
0.000357704, within its floating cap 0.000395978.

The useful result is that the full finite neutral expectation can now be
computed with phase and controlled connected-log truncation. The opposite
edge's tested low modes improve substantially. The top error remains
order one; there is **no** measured or proved charged-field limit here.

## Connection to the broader composition question

The 1/k in the connected determinant log also appears when repeated
primitive arithmetic contributions are separated from composites. It is
not by itself arithmetic information. If one hypothesizes positive
linear prime channels L=x A_p+y A_q, then

    [xy](-log|C|) = (1/2) Tr(A_p A_q).

For positive A_p,A_q this vanishes precisely when their supports are
orthogonal: Tr(A_p A_q)=||A_q^(1/2) A_p^(1/2)||_HS^2. A multivariable
Euler-factorized target has no mixed connected prime coefficients. Thus
nonorthogonal positive linear channels cannot realize that specific
factorization by cancellation. This does not exclude nonlinear channels,
complex phases, relative determinants, or interacting observables that
are not supposed to equal an Euler product. Tests include the exact
nonorthogonal value 1/64 and an orthogonal zero control.

The complex determinant contains information absent from L: a block
diagonal phase rotation has L=0 but a nontrivial vacuum phase. Keep that
information when testing a microscopic cocycle or a signed trace identity.

## Next acceptance gates

1. Bound the full bottom/bulk contribution to the **complex determinant**,
   uniformly enough for field renormalization, not just three low modes.
2. Derive endpoint normalization and smeared neutral kernels from this
   same source; test nontrivial regulator-independent limits. Smooth full
   counting statistics provides related methods, not an automatically
   applicable theorem: [Ivanov--Levkivskyi (2015)](https://arxiv.org/abs/1507.07896).
3. Only then match adjoints, exchange phases and unbounded charge carry
   to the previously constructed target lattice algebra.

Run `python3 checker.py --output diagnostics.json` in this folder and
`python3 -m unittest discover -s . -p test_checker.py -v`.
The same 13 tests pass under python3 -OO. No paper/site/ledger promotion.
