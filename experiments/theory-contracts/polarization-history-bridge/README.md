# Polarization-history bridge: exact reduction without an artificial edge cut

2026-09-08. New application and directly proved finite stability lemma.
No claim of mathematical priority, microscopic scaling-limit completion,
TFPT-selected preparation, TOE completion or RH.

Subsequent construction: [source-polarized finite current reference with an
amplitude-inert, source-empty spectator completion](../history-reference-transport/README.md).
This supplies a concrete reference and a conservative reference-size bound;
the required microscopic history-decay rate remains open.

## Outcome

The full occupied/unoccupied polarization is enough. All rotations *within*
the occupied and unoccupied spaces can be removed exactly as a moving
reference frame. The remaining time-dependent crossblock determines the
entire normal-ordered complex vacuum amplitude.

This removes the artificial occupied edge/rest cut used in the previous
[Schur analysis](../neutral-current-limit/README.md). No inverse occupied
compression, nonvanishing determinant hypothesis or separate bulk determinant
is needed. A dimension-free stability estimate reduces the next proof to
comparison of two crossblock histories. The actual source-to-current history
comparison is still open.

## 1. Exact identity on the full polarization

Let P be the full occupied projection, Q=I-P, and Omega_P its Slater vector.
For a piecewise Hermitian one-particle generator K(s), use the right-evolution
convention W'=iWK, W(0)=I. Define

\[
 D=PKP+QKQ,\quad O=K-D,\quad G'=iGD,\quad G(0)=I,\quad V=WG^\dagger.
\]

G is block diagonal. Direct differentiation gives

\[
 V'=iVB,\qquad B=GOG^\dagger,\qquad PBP=QBQ=0.
\]

Since det(PGP)=exp(i integral Tr(PK) ds), at the final time T

\[
 \boxed{e^{-i\theta}\det(PWP)
       =\langle\Omega_P,\Gamma(V)\Omega_P\rangle,\qquad
       \theta=\int_0^T\operatorname{Tr}(PK(s))\,ds.}
\]

For the actual source W=exp(-iF_a)exp(iF_b), choose K=-F_a and K=F_b on
two unit-length legs. Then G=exp(-iD_a)exp(iD_b) and
theta=Tr P(F_b-F_a), exactly the previous endpoint-coboundary phase.
No source, occupation or Gaussian filter has been changed.

The diagonal blocks are not deleted: their physical effect remains in the
rotated history B(s). In particular, the central-extension phase is retained.

## 2. Dimension-free comparison theorem

Let B,B_0 be piecewise continuous Hermitian histories, both purely off
diagonal for the **same P on the same finite space**. Let

\[
 X'=-iBX,\quad X_0'=-iB_0X_0,\quad X(0)=X_0(0)=I,
\]
\[
 d(s)=\|Q(B-B_0)P\|_{\rm HS},\qquad
 n_0(s)=\|QX_0(s)P\|_{\rm HS}^2 .
\]

The normal amplitudes are conjugates of the vacuum amplitudes of Gamma(X).
They obey

\[
 \boxed{|C^\circ-C_0^\circ|
 \le\varepsilon
 :=\int_0^T d(s)\sqrt{1+4\sqrt{n_0(s)}+8n_0(s)}\,ds.}
\]

A generator-only upper bound is

\[
 \varepsilon\le\int_0^T d(s)[1+2\sqrt2 A_0(s)]\,ds,\qquad
 A_0(s)=\int_0^s\|QB_0(u)P\|_{\rm HS}\,du.
\]

All constants are independent of the one-particle dimension and the number
of occupied modes. This is an amplitude estimate including phase, not merely
a modulus or a covariance estimate. Zero amplitudes are allowed.

### Proof

Put R=X_0PX_0^\dagger and Delta=B-B_0. The exact Slater-state variance
identity is

\[
 \|d\Gamma(\Delta)\Gamma(X_0)\Omega_P\|^2
 =\operatorname{Tr}(R\Delta(1-R)\Delta)
  +[\operatorname{Tr}(R\Delta)]^2.
\]

Off diagonality implies Tr(P Delta)=0, ||Delta||<=d,
||R-P||_HS^2=2n_0 and ||QRP||_HS^2<=n_0. Therefore

\[
 |\operatorname{Tr}(R\Delta)|\le2d\sqrt{n_0},
\]
\[
 \sqrt{\operatorname{Var}_R d\Gamma(\Delta)}
 ={1\over\sqrt2}\|[\Delta,R]\|_{\rm HS}
 \le d+2d\sqrt{n_0}.
\]

Adding the squared mean and variance proves the first integrand. Duhamel's
identity on the finite Fock space then bounds the difference of evolved
vacuum vectors by its integral; taking a vacuum matrix element gives the
stated complex-amplitude estimate. Since QB_0Q=0,
||(QX_0P)'||_HS<=||QB_0P||_HS, so sqrt(n_0)<=A_0.
Finally sqrt(1+4A_0+8A_0^2)<=1+2 sqrt(2) A_0.

The proof does not assume the Fock Hamiltonian has a dimension-independent
operator norm. It bounds its action on the actual comparison Slater vector.

## 3. What must now be shown for the microscopic limit

First construct a source-grounded finite current reference and identify its
polarization with the source polarization by an explicit isometric embedding
and any justified inert padding. Equal matrix dimensions alone are not an
identification. Then estimate the two **rotated histories**, not just their
unrotated endpoint crossblocks.

For the previously derived endpoint normalization Z_t=exp(H_t/8),
t=N delta_N, a sufficient amplitude requirement is

\[
 Z_{t_N}^{\,2}\varepsilon_N\longrightarrow0,
\]

in addition to a separately proved reference-to-current error. Uniform
endpoints and near-diagonal bounds are required for smeared convergence.
This theorem supplies a sufficient criterion, not proof that the actual
QWZ histories satisfy it.

One useful quantitative target follows conditionally. Elementary splitting
of the Gaussian sum gives H_t=log t+O(1), hence Z_t^2=O(t^(1/4)).
For delta_N=4N^(-3/4), this is O(N^(1/16)).
If the finite reference retains the current bound A_0(T)=O(sqrt(log t)),
then it suffices to prove

\[
 \int_0^T\|Q(B_N-B_{0,N})P\|_{\rm HS}\,ds
 =o\!\left({N^{-1/16}\over\sqrt{\log N}}\right).
\]

The reference bound and microscopic history estimate must both be verified;
they are not extracted from the earlier small relative determinant errors.
In the ideal current model, ||QF_aP||_HS^2=H_t/4 directly from its Fourier
coefficients; transporting that bound to a finite embedded reference is
part of the task.

For every fixed word W=product_j exp(i epsilon_j F_(a_j)), the exact identity
and stability proof work segment by segment, with
theta=sum_j epsilon_j Tr(PF_(a_j)). After field normalization the bound is
(product_j Z_j) epsilon_word. This offers a route beyond two-point functions
but requires a separate bound for each word's history. It does not infer
all higher correlations or common field domains from the two-point result.

## 4. Unchanged-source checks and the rejected simplification

All six exact-reduction checks, at N=8,16,32 and separations 1/4 and 1/2,
agree with the original full complex determinant to about 1.1e-13 or better.
These floating residuals verify the implementation of an algebraic identity;
they are not a convergence rate.

Deleting D_a,D_b and simply using exp(-iO_a)exp(iO_b) fails:

| N | Relative error, quarter interval | Relative error, half interval |
| ---: | ---: | ---: |
| 8 | 0.0117175 | 0.0187196 |
| 16 | 0.0171508 | 0.0275731 |
| 32 | 0.0261463 | 0.0394457 |

At the half-interval second-leg midpoint, the crossblock change caused by
the moving frame is 0.28517, 0.30848, 0.35640 respectively. These observations
reject the particular shortcut, not the existence of a better reference.

An exact two-mode example explains why the shortcut cannot be an identity:
P=diag(1,0), F_0=(pi/4)sigma_x and
F_1=F_0+(sqrt(3)pi/4)sigma_z have identical static crossblocks, but

\[
 C_0^\circ={\sqrt2\over2},\qquad
 C_1^\circ={i\sqrt3\over2}e^{-i\sqrt3\pi/4}.
\]

They differ even in modulus. Endpoint crossblocks alone lose real information.

## 5. Exact thermal/mixed-state adapter, without eigenvalue clipping

The other Seam session uses faithful thermal covariances, while the neutral
field calculation uses a pure occupied projection. There is an exact finite
mathematical adapter between the two calculation methods.

For any covariance 0<=C<=I define

\[
 J_C=\begin{pmatrix}\sqrt C\\\sqrt{I-C}\end{pmatrix},
 \quad\widetilde P=J_CJ_C^\dagger,\quad
 \widetilde W=W\oplus I .
\]

J_C is an isometry and Ptilde an orthogonal projection. Sylvester's identity
and the gauge-invariant quasifree trace formula give

\[
 \boxed{\det(J_C^\dagger\widetilde WJ_C)
       =\det(I-C+CW)=\omega_C(\Gamma(W)).}
\]

For completeness, in an eigenbasis of C the quasifree density matrix is
a product of Bernoulli occupations. Summing the occupied principal minors
of W with these weights expands precisely det(I-C+CW).
For a general C, unitary covariance reduces to that basis. The purification
compression is I-C+sqrt(C) W sqrt(C), whose determinant equals the same
expression by det(I+AB)=det(I+BA).
Also Tr(Ptilde (K direct_sum 0))=Tr(CK), so the correct normal phase is
integral Tr(CK(s)) ds. The history theorem now applies with Ptilde.

The full endpoint Gram matrix with W=U_a^\dagger U_b is positive. An exact
noncommuting two-mode control, C=diag(1/3,2/3) and
W=[[3/5,-4/5],[4/5,3/5]], gives 7/9 by both the purified determinant and
the independent full-Fock mixture.

No eigenvalues are clipped, and C may have eigenvalues 0 or 1. At fixed
finite source, the grandcanonical thermal limit is C_infinity=P_-+P_0/2.
The floating Fermi-function helper can still saturate to 0 or 1 by
underflow/roundoff at large finite beta; such arrays must not be used as
exactly faithful finite-temperature data for a modular logarithm. This
does not affect the exact purification identity or the zero-mode value 1/2.
Thus exact zero modes have occupation 1/2 without selecting an arbitrary
pure edge mixture. But this is the grandcanonical thermal prescription,
not a proof that TFPT chooses it or that it equals a fixed-charge state.
For C=diag(1,1/2), W=diag(1,-1), the amplitude is exactly zero, illustrating
why the inverse-free history formulation matters.

The additional copy is only a purification space, not a proposed physical
bulk or new matter sector. Changing from a pure sea to a thermal/zero-mode
mixture changes the preparation: the old current kernel must not simply
be reused without comparing those states and their polarizations.
No global finite modular logarithm is asserted for a projection.

The underlying finite Fock/determinant trace identity is classical:
[Klich, Full Counting Statistics](https://arxiv.org/abs/cond-mat/0209642).
The contribution here is its explicit use to connect the current TFPT
calculation interfaces and the directly proved history-error criterion.

## Verification

    python3 experiments/theory-contracts/polarization-history-bridge/checker.py --source --output experiments/theory-contracts/polarization-history-bridge/validation.json
    python3 -m unittest discover -s experiments/theory-contracts/polarization-history-bridge -p test_checker.py
    python3 -OO -m unittest discover -s experiments/theory-contracts/polarization-history-bridge -p test_checker.py

Fourteen tests per mode passed, including an independently assembled
many-body variance calculation, an exact rational purification example,
zero-amplitude and invalid-covariance controls, and unchanged-source replay.
All saved outputs explicitly retain the open microscopic-limit boundary.
