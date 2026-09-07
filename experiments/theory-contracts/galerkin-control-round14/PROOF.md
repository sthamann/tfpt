# Finite-cutoff error control and what it can actually prove

Date: 2026-09-06. Non-RH Round14. This is an unconditional error theorem
for the unchanged Round13 minimal operator, plus an explicitly separate
solvable cubic MODEL showing why boundary selection matters. It does not
establish the interacting TFPT Galerkin limit.

## 1. The exact residual needs only three physical Hermite shells

Use the full unchanged expression of covariant-domain-round13, including
all auxiliary positions but not the still-unconstructed auxiliary-momentum
multipliers. In Fourier constraint coordinates write

    L = -i (bv).partial_r + h(c,y),
    h_N = Pi_N h Pi_N,  L_N = -i (bv).partial_r + h_N.                 (1)

Here Pi_N is the projection onto physical TT/matter Hermite degree at most
N, acting as the identity on constraint and auxiliary parameters. The
physical degree of the exact Weyl polynomial h is at most three. Scalar
parameter multiplication is included; the complement of Pi_N has h_N=0.
The unitary groups U_N(t) exist by Round13's finite-matrix characteristic
construction. Let D_0 consist of finite physical Hermite sums with smooth
compactly supported coefficients in all (c,y). This is dense in the full
kinematic Hilbert space, and is contained in the full Schwartz domain.
No deletion of a measure-zero constraint fiber is needed here.

For f in D_0 and N above its physical support, u_N(t)=U_N(t)f remains in
D_0 on every finite time interval: the parameter support follows the
complete affine flow, finite-matrix coefficients are smooth, and the
physical degree remains at most N. Its full differential residual is

    (L-L_N)u_N(t) = R_N u_N(t),
    R_N = (I-Pi_N) h Pi_N
        = (Pi_(N+3)-Pi_N) h (Pi_N-Pi_(N-3)).                          (2)

Set Pi_j=0 for j<0. Every coordinate or momentum changes Hermite degree
by one, so a word of length at most three cannot connect levels differing
by more than three. This proves (2) for the whole operator, not only a
chosen cubic monomial. The derivative in (1) commutes with Pi_N and adds
no discarded component. Equation (2) is the residual *outside* the
truncation, which is invisible to the projected finite evolution equation.

On a compact parameter set K, expand the Weyl polynomial in ordered
coordinate/momentum words w of length at most three, h=sum_w a_w(c,y) w.
Writing each Q or P as two ladder operators gives the explicit bound

    ||R_N v|| <= C_K (N+3)^(3/2) ||(Pi_N-Pi_(N-3))v||,
    C_K = sum_w 2^(length(w)/2) sup_K |a_w|,  v in ran Pi_N.          (3)

Each ladder step on levels through N+2 has norm at most sqrt(N+3).
The sum of the 2^length ladder words contributes 2^(length/2).
Lower degree words obey the same displayed overbound. The parameter
support swept out in a finite time interval is compact, so C_K is finite.
This bound depends on regulator, coupling, time interval and parameter
support; no volume- or continuum-uniform constant is claimed.

## 2. An a posteriori bound against every self-adjoint extension

Let H be ANY self-adjoint extension of L on this same Hilbert space.
Such extensions exist by Round12; no covariance or preferred extension
is assumed. Since u_N(t) lies in the common minimal test domain, its
H-action is the exact differential expression L u_N(t). Differentiating
e^(-i(t-s)H)u_N(s) and integrating gives, for t>=0,

    U_N(t)f - e^(-itH)f
       = i integral_0^t e^(-i(t-s)H) R_N U_N(s)f ds.                 (4)

All derivatives are legitimate in Hilbert norm: the integrand is smooth
with compact parameter support and finite Hermite degree. The same proof
works for negative t with reversed limits. Unitarity implies

    ||U_N(t)f-e^(-itH)f|| <= E_N(f,t),
    E_N(f,t) = integral_[0,t] ||R_N U_N(s)f|| |ds|.                  (5)

In particular, for any two self-adjoint extensions H_1,H_2,

    ||e^(-itH_1)f-e^(-itH_2)f|| <= 2 E_N(f,t).                     (6)

The bound is independent of their unspecified boundary domains. It is
a usable finite-cutoff error certificate once the residual norm integral
is itself rigorously bounded. A floating-point trajectory or one sampled
residual is NOT a certified value of the integral. No such all-parameter
numerical certificate for the complete interacting TFPT dynamics is
asserted in this round.

If E_N(f,t) tends to zero for every f in a dense D_0 and every finite
positive and negative t, all self-adjoint extensions have the same unitary
group. Therefore the minimal closure is essentially self-adjoint (ESA):
with equal deficiency indices, a nonzero deficiency space would permit
distinct von Neumann extension maps. Equivalently, this hypothesis proves
uniqueness of the extension, not merely existence of one covariant limit.
The same uniform convergence transports the exact covariance of U_N.

This is a significant scope limit of the proposed proof strategy. Mere
strong convergence of one Galerkin sequence to a chosen proper extension
does not imply residual convergence to zero: (5) is a sufficient estimate,
not a necessary characterization of all strongly convergent schemes.
No ESA or non-ESA result for the actual interacting operator is obtained.

## 3. Certified finite-order time control without an analytic-series claim

For f in the full Schwartz domain, polynomial differential operators map
Schwartz to itself. Thus f is in Dom H^k and H^k f=L^k f for every finite
k and every extension H. The spectral theorem's scalar integral remainder
gives

    ||e^(-itH)f - sum_(j=0)^(k-1) (-it)^j L^j f/j!||
       <= |t|^k ||L^k f||/k!.                                      (7)

In particular the difference between any two extensions is at most twice
the right side. Each finite-order quantity uses the unchanged minimal
polynomial only. This does not imply that its infimum over k is zero:
Schwartz vectors need not be analytic vectors for a cubic operator.
Agreement of every time derivative at zero therefore need not determine
the full evolution. The following exactly soluble example makes this
logical boundary explicit.

## 4. MODEL: a cubic with complete quantum extensions and boundary freedom

This section is NOT the actual TT/matter Hamiltonian. On L2(R_x) take

    B_min = ((1+x^2)p+p(1+x^2))/2
          = -i[(1+x^2)partial_x+x], p=-i partial_x,                  (8)

initially on Schwartz. It is a real classical cubic polynomial with
Hamilton equation dot x=1+x^2 and finite escape x(t)=tan(t+arctan x0).
Put y=arctan x, a=-pi/2, b=pi/2, ell=pi, and

    (Wf)(y)=sec(y) f(tan y).                                       (9)

Since dx=sec(y)^2 dy, W is unitary to L2((a,b)). Direct differentiation
gives W B_min W^-1=-i partial_y. W maps Schwartz functions to smooth
functions flat at both endpoints. Their closure in the derivative graph
norm is H^1_0((a,b)): inclusion follows from the zero traces; density
follows because C_c^infinity((a,b)) is in W Schwartz. The adjoint has
domain H^1((a,b)), and its two deficiency equations each have one
square-integrable exponential solution. All self-adjoint extensions are

    B_theta = W^-1 P_theta W,
    Dom P_theta = {v in H^1((a,b)): v(b)=e^(i theta)v(a)},
    theta in [0,2pi).                                              (10)

The boundary form -i[conj(u)v]_a^b proves symmetry and maximality of
this domain. The eigenvalues are (2pi n+theta)/ell, n in Z. These are
different extensions of the SAME full Schwartz expression.

Extend v quasiperiodically by v(y+ell)=e^(i theta)v(y). Then

    (e^(-itP_theta)v)(y)=v(y-t)                                    (11)

is the exact unitary group. Every compactly supported smooth packet
has identical finite derivatives at t=0 for all theta. Yet choose two
disjoint equal-norm smooth packets, one near b and one in the middle,
and a positive time at which only the first crosses b. For theta=0
and theta=pi the crossed part has opposite sign and the other part has
the same sign. The two evolved normalized superpositions are orthogonal.
Boundary freedom can thus change a relative phase, not only a physically
irrelevant global phase. There is no contradiction with (7): no shared
convergent Taylor expansion is guaranteed.

Adding an independent characteristic coordinate s gives

    K_theta = P_s tensor I + I tensor B_theta.                      (12)

This is self-adjoint by its joint spectral multiplier domain. It contains
the same full joint Schwartz differential expression for every theta.
For M_beta=e^(i beta s), M_beta^* K_theta M_beta=K_theta+beta with full
domain equality. More generally U(t)^* f(s) U(t)=f(s+t) for every bounded
Borel f. Its spectrum is R and purely absolutely continuous, as a direct
sum of translated free P_s spectra. The antiunitary

    Theta F(s,y)=conj(F(-s,-y))

preserves every theta boundary domain and commutes with K_theta.
Thus exact covariance, the necessary spectral condition, and this real
symmetry still do not select a unique boundary phase in this MODEL.
This is not an existence, nonuniqueness or deficiency computation for
the actual TFPT operator.

## 5. Verification, cost and remaining obligation

The companion checker independently reconstructs one actual L2 TT stress
from the repository Ward formulas and checks its full cubic Hermite
bandwidth and nonzero three-shell leakage. Ladder operations are applied
on the infinite basis with finite exact support, not by asserting CCR
for finite truncated matrices. It separately checks the cubic MODEL's
Jacobian, conjugation, boundary relation and relative-phase distinction.
General domain, Duhamel and spectral arguments are the proofs above.

An additional independent check uses a different, single-site scalar
displacement for the actual common-domain obstruction: phi_0 shifts by
R^2, pi_0 by R^3 and Q_0 by -2 C_0(t)R^2/g. Its actual TT source is 1/4.
The checked shifted two-TT-coordinate expression has degree at most five in
R; each remaining undisplaced TT vertex contributes degree at most four,
as proved in the companion common-domain contract. The
quadratic characteristic coefficient retains (3 sqrt(2)/128) R^6.
This verifies the cancellation with a second source profile; it does not
replace the Hilbert-space domain proof in the companion contract.

For d physical oscillator coordinates, rank Pi_N=binomial(N+d,d).
The external residual occupies levels N+1 through N+3. The exact
stencil is finite, but solving and certifying the growing matrix system
still has this combinatorial state count; no efficient large-volume
solver or asymptotic improvement is claimed.

Primary context: [Boussaid, Caponigro and Chambrion, weakly coupled
quantum systems](https://arxiv.org/abs/1109.1900) studies Galerkin error
control under additional hypotheses. Those hypotheses are not imported
for the actual cubic family here; (2)–(7) are derived directly.

The next actual task is to bound E_N or construct and select a variable
boundary-domain propagator by another valid method. Finite self-adjoint
matrices, small projected equation residuals, or agreement to all finite
perturbative orders do not settle that task. Auxiliary multipliers,
physical reduction, locality, the common TFPT parent and T1–T8 remain
separate open obligations.
