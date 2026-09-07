# One joint clock model for the actual Round15 vertex-preserving generator

2026-09-06. NON-RH Round16. This combines the already constructed Round15
vertex-preserving quantum generator, the declared auxiliary gauge-unfixing,
and the unchanged quadratic trace clock into one self-adjoint constrained
model. Its homogeneous momenta are declared spectral relational constraints.
It does not derive the clock, those momentum constraints, or a microscopic
TFPT parent. It is not full T1--T8/TOE closure.

## 1. The operator being retained, not replaced

Fix the finite connected periodic lattice of side L>=2, spacing a>0, scalar
mass m>=0 and coupling g in R. Write N=n-1, c=(r,v) in R^(4N), and H_p for
the actual scalar/TT Hilbert space, including the scalar mean. The input
[Round15 theorem](../vertex-preserving-round15/PROOF.md) gives one specified
self-adjoint generator H_vp on H_c tensor H_p, with H_c=L2(R^(4N),dc),

    H_vp = K_c + A_+ + g c.Q + g^2 |c|^2 sum_a Q_a^2,          (1)
    K_c = -i(bv).partial_r + k(c),
    A_c = [[0,b],[0,0]],  c(t)=exp(t A_c)c,
    k(c)=r.B_H.r/2+v.B_v.v/2.

Equation (1) denotes exactly the closed-form and characteristic-propagator
realization in that proof, not a new extension of a formal differential
expression. The original first dressed vertex is retained there. The Q_a
are the actual noncommuting matter quadratics; none are replaced here.

The retained positive physical generator A_+ has the fixed-regulator bound
A_+>=e_*>0 with the unsubtracted energy convention of
[Round13](../clock-shell-round13/README.md). The actual b is the discrete
divergence (D_1^-,D_2^-,D_3^-) on mean-zero modes and has rank N>0.
Indeed, at a nonzero periodic Fourier mode at least one symbol
1-exp(-ik_i a) is nonzero; the divergence is onto that scalar mode.
The real form has the same rank. This is an all-volume symbol argument,
not an inference from a finite rank test.

Let V_c(t,s) denote the input propagator along the characteristic starting
at c. In particular V_c(t,0) propagates from c to exp(t A_c)c. It obeys

    V_c(t+s,0)=V_exp(s A_c)c(t,0) V_c(s,0),                 (2)
    V_c(t,0) -> exp(-it A_+) strongly as c->0,              (3)

where convergence in (3) is uniform on compact time intervals. The input
full group, with I_t(c)=integral_0^t k(exp(-u A_c)c)du, is

    [U_vp(t)F](c)=exp(-i I_t(c))
                    V_exp(-t A_c)c(t,0) F(exp(-t A_c)c).   (4)

We use these already established properties. We do not assume preservation
of a full Schwartz space or evaluate an interacting spectral transform.

## 2. A measurable characteristic gauge straightens this same generator

Set Omega={c: bv!=0}. Its complement is a linear subspace of codimension
rank b=N>0 and therefore has Lebesgue measure zero. For c in Omega put

    a(c)=bv,
    tau(c)=r.a(c)/|a(c)|^2,
    c_perp=(r-tau(c)a(c),v),
    S(c)=V_c_perp(tau(c),0) exp(+i tau(c) A_+).             (5)

The subscript c_perp in (5) is the initial characteristic label, not a
projection of physical modes. Every scalar and TT mode is still present.
Direct calculation gives

    c=exp(tau(c) A_c)c_perp,
    tau(exp(t A_c)c)=tau(c)+t,
    (exp(t A_c)c)_perp=c_perp.                             (6)

Define S arbitrarily, for example as the identity, on the null complement.
The input strong continuity of V makes S strongly measurable on Omega.
Every S(c) is unitary, so multiplication by S(c) defines a unitary S on
H_c tensor H_p. Its inverse is multiplication by S(c)*. It commutes with
every bounded Borel function of c. No Jacobian arises: S changes only the
physical fiber and does not change the variable c or its measure.

Using the propagator composition law along the same characteristic,

    V_c(t,0) S(c) = S(exp(t A_c)c) exp(-it A_+)              (7)

holds on Omega, hence as the needed almost-everywhere identity. Substituting
(7) into (4) proves equality of strongly continuous unitary groups:

    U_vp(t) S = S [exp(-it K_c) tensor exp(-it A_+)].        (8)

Consequently Stone generators and their complete domains satisfy

    H_vp = S (K_c+A_+) S*,
    Dom H_vp = S Dom(K_c+A_+).                            (9)

The sum in (9) is the exact joint spectral sum. Its domain is square
integrability of |kappa+E|^2 in the joint K_c,A_+ spectral measure; it
need not be the intersection of their individual domains. Equation (9)
does NOT replace H_vp with the Round14 Hamiltonian. It explicitly proves
a unitary representation of the already specified Round15 generator.
In particular the order-g vertex in its original expression is unchanged.

Define the two transported self-adjoint operators

    B = S A_+ S*,               K_tilde = S K_c S*.        (10)

Their spectral measures strongly commute, B>=e_*, and H_vp=K_tilde+B
on the transported joint domain. B is decomposable over c and commutes
strongly with c. It is not the instantaneous form operator h(c) from
Round15, and K_tilde is not the old bare K_c. These distinctions are
necessary: it would be false to claim that bare A_+ strongly commutes
with H_vp merely because the latter reduces to A_+ at c=0.

At g=0, h(c)=A_+(0) for every c, and (5) gives S(c)=I almost everywhere.
At nonzero g, (5) requires the full characteristic dynamics. It is not
a local formula, a cheap numerical algorithm, or an operator-norm
analytic family in g. A different characteristic section can change the
transported off-shell B and relational observables; no preferred section
is derived from TFPT here.

## 3. Why this gauge does not arbitrarily change the zero-fiber reduction

The function tau(c) is singular as bv approaches zero. In particular no
ordinary continuous extension of S to every point of that set, or a
uniform time estimate there, is claimed. Setting S(0)=I alone would not
justify a physical zero-fiber norm. The following limit does.

For every fixed c in Omega and every positive delta,

    tau(delta c)=tau(c),     (delta c)_perp=delta c_perp.

Therefore (3), applied at the fixed finite time tau(c), gives

    S(delta c) psi -> psi,  S(delta c)* psi -> psi
    for every psi in H_p, as delta->0.                    (11)

This is strong convergence for almost every fixed direction, not uniform
convergence over directions. The adjoint statement follows from unitarity.
It also holds after tensoring with the independent clock and auxiliaries.

Here is a direct trace test. Let rho>=0 be any integrable fixed-shape
probability density on R^(4N), and let f(c) be bounded and continuous at
zero with values in the physical Hilbert space (possibly tensor the
independent clock space). Then

    integral dc delta^(-4N) rho(c/delta)
        ||S(c)f(c)-f(0)||^2 -> 0.                         (12)

After c=delta x, the integrand tends to zero for almost every x by (11)
and continuity of f. It is bounded by an integrable constant times rho(x),
since S is unitary and f is bounded. Dominated convergence proves (12).
The same assertion holds with S*. The standard Gaussian rigging regulator
of Round15 is the special case delta=sqrt(epsilon).

Thus transported tests S f have the same Gaussian mean-square trace f(0).
For two such tests, their same-c scalar inner product even equals that
of the untransported tests exactly, because S(c)*S(c)=I. Mixed pairings
with ordinary continuous tests converge to the same trace by (12) and
Cauchy--Schwarz. This identifies the reduction with the previous physical
Hilbert space without promoting an arbitrary value on a null fiber.
No regulator concentrated on the exceptional subspace and no arbitrary
anisotropic limiting family is included in this statement.

The loss of ordinary continuity is a real possibility under these hypotheses,
not merely a missing estimate. In the labelled one-channel commuting model
with velocity a and h(r,a)=E+gqr+g^2q^2(r^2+a^2), the gauge is exp(-i theta),

    theta=gq r^2/(2a)+g^2q^2[r^3/(3a)+ar].

It tends to zero under common radial scaling. However at g=q=1 and
r=delta,a=delta^2 its phase tends to 1/2, while the phase diverges for
r=delta,a=delta^3. This controls an invalid continuity claim; it is not
a replacement for the actual noncommuting TFPT propagator.

## 4. The unchanged full quadratic clock has an exact self-adjoint domain

Add the postulated trace pair with P_0=-i partial_(q_0) on L2(R_q0).
The two operators H_vp tensor I and I tensor P_0 strongly commute by
their separate tensor factors. Hence the full clock constraint is

    C_vp = H_vp - P_0^2/12,                               (13)
    Dom C_vp = {Psi: integral |E-p^2/12|^2
                  d<Psi,(E_Hvp tensor E_P0)Psi> < infinity}.

This is a self-adjoint joint spectral multiplier on the full enlarged
space. The domain is not guessed from the separate-domain intersection.
Its unitary group is U_vp(t) tensor exp(+it P_0^2/12). The sign in the
second factor is essential. It has the same exact gravitational covariance

    exp(it C_vp) F(c) exp(-it C_vp)=F(exp(t A_c)c)            (14)

for all bounded Borel F. No square root of the non-semibounded H_vp is
taken. Tensoring S with the clock identity and using (9) gives

    C_vp = S [K_c+A_+-P_0^2/12] S*.                      (15)

Set I=(-e_*/2,e_*/2). The correct reducing clock tube for (13) is

    K_I^vp = {P_0<0, B-P_0^2/12 in I},                   (16)

interpreted as the range of these commuting spectral projections. It is
the S-image of the old A_+-clock tube, not in general that raw old tube.
It reduces C_vp and the c spectral constraints, since B commutes strongly
with K_tilde,c,P_0. It is not an interval of the TOTAL C_vp spectrum.

In any spectral representation of A_+, with spectral variable E and its
possibly continuous or singular spectral measure, use exactly the Round13
negative-sheet clock coordinate change

    lambda=E-p^2/12,
    p_-(E,lambda)=-sqrt(12(E-lambda)),
    w(E,lambda)=dp_-/dlambda=6/sqrt(12(E-lambda)),
    (Z f)(lambda,E)=sqrt(w(E,lambda)) f(E,p_-).             (17)

Because E-lambda>=e_*/2, every system energy is available for every
lambda in I. The norm identity dp=w dlambda proves that Z is a unitary
from the reference A_+-clock tube to L2(I_lambda) tensor H_p. This does
not assume a discrete interacting spectrum or replace the clock constraint
by P_0+sqrt(12A_+).

With T=S Z* (and identity on c in Z),

    T: L2(R_c^(4N)) tensor L2(I_lambda) tensor H_p -> K_I^vp,
    T* C_vp T = K_c+M_lambda.                             (18)

Since lambda is bounded, the domain on the right is the tensor extension
of Dom K_c. Equivalently it is the multiplier domain for |kappa+lambda|^2.
Equations (13) and (18) give both the full domain and its reducing-tube
restriction. The positivity required for the clock chart belongs to B,
not to the full H_vp or C_vp, whose spectra remain unbounded below.

## 5. Auxiliary gauge-unfixing and all homogeneous relational momenta

The same construction can include exactly the already declared auxiliary
choice, without silently restoring its discarded secondary constraints.
Add eta in R^a, a=28N, and use the existing quadratic-source unitary

    V_aux(eta)=exp(-i eta.fhat),     f=-K_aux^(-1)s,
    W_0=U_g V_aux,                 W=W_0 S Z*.             (19)

These are the actual metaplectic auxiliary translation and gravity
dressing in [the auxiliary construction](../auxiliary-domain-round14/COMBINED.md).
V_aux acts on the physical factor and commutes with bare c, X and eta;
S need not commute with V_aux. Their order in (19) is part of the definition.
Both commute with P_0. The full, gauge-unfixed Hamiltonian before adding
the clock is W_0 H_vp W_0*, tensor the auxiliary identity before transport.
The primary auxiliary list is eta=0. The secondary coordinate constraints
remain gauge-fixing partners, not simultaneous annihilation conditions.

The full dressed clock constraint is W_0 C_vp W_0*. The chosen reducing
tube is W_0 K_I^vp, characterized by P_0<0 and

    W_0 B W_0* - P_0^2/12 in I.                           (20)

All its domains are transported by the same W. On the reference space

    H_ref=H_c tensor L2(R_eta^a) tensor L2(I_lambda) tensor H_p

the complete retained list is

    C_ref=K_c+M_lambda,   c_a=M_c_a,   eta_j=M_eta_j,
    J_i=I tensor J0_i.                                    (21)

Here J0_i are the actual centered homogeneous free momentum generators
on H_p. As established in Round13, the commuting antisymmetric centered
difference matrices act by commuting orthogonal configuration pullbacks
on scalar and TT coordinates. The generators are simultaneously
self-adjoint; finite isotropic Hermite levels supply their operator cores.
Their compact orthogonal-flow closure G has normalized Haar projector

    Pi_0=integral_G U0(alpha) d alpha,
    ran Pi_0=intersection_i ker J0_i != {0}.               (22)

An isotropic normalized Gaussian proves nonzero range. This projector is
not the projector of the genuine finite lattice-translation group.

Transport each spectral measure in (21) by W. The resulting homogeneous
J_i^vp=W J_i W* are self-adjoint on the transported L2 graph domains and
strongly commute with one another, the dressed c, eta, and the clock
constraint. This is an actual JOINT representation on the same clock tube,
not the assertion of a formal commutator on some unspecified test domain.
The c constraints are covariant under C_ref as in (14); they do not
strongly commute with C_ref. At g=0, S=I, the auxiliary/gravity dressings
are the identity, and Z intertwines the old J0_i because J0_i strongly
commutes with A_+(0). Thus the free seed is recovered on its clock tube.

At nonzero g these are spectral relational momenta. They are not the old
time-independent local spatial momentum currents, and no claim that they
are a naive quantization of the full classical clock-flow formula is made.

## 6. One absolutely convergent joint average and a positive physical norm

In reference coordinates define the group representation

    R(t,u,zeta,alpha)=exp(i u.c) exp(i zeta.eta)
                       exp(-it C_ref) U0(alpha),          (23)

where alpha belongs to G. The c/time part is semidirect. Its action on the
dual u variable has determinant exp(-t Tr A_c)=1, so the group is
unimodular. Product Lebesgue measure and normalized Haar measure on G are
both left and right invariant. Its transported representation is W R W*.

Take the dense reference space of finite sums of

    F(c,eta,lambda)=a(c)b(eta)u(lambda)v,
    a,b smooth compactly supported, u in C_c^infinity(I), v in H_p.
                                                               (24)

This space is invariant under (23). In particular its physical factor is
the whole Hilbert space; no interacting Schwartz-invariance assumption is
needed. Let E=W E_ref. These tests need not lie in every generator domain;
the averaging space and the already specified operator domains are distinct.

For two tests the full matrix-element integral

    integral dt du dzeta/(2pi)^(1+4N+a) integral_G d alpha
                   <W F, W R(t,u,zeta,alpha) G>            (25)

is absolutely convergent, not merely a chosen iterated integral. Unitarity
of W cancels it exactly inside each matrix element. In reference variables,
integration by parts in c and eta gives arbitrarily high inverse powers
of (u,zeta), with at most polynomial growth in t: the constraint flow is
linear in t and the phase I_t(c) is polynomial of degree at most three in t.
Compact support of the bra bounds the spatial integrations. Independently,
integration by parts in lambda gives arbitrarily rapid inverse powers of t.
Choose spatial derivative orders above their dimensions and then choose a
lambda order that dominates the resulting polynomial growth. Compact-group
matrix elements are bounded by the product of Hilbert norms. This supplies
an integrable bound on the full product group. No derivatives of S(c) are
taken in this argument.

Fourier integration sets c=eta=0. There the reference shear and phase are
trivial. Time integration sets lambda=0; compact averaging gives Pi_0.
Hence the exact answer is

    eta_phys(W F,W G)=<F(0,0,0),Pi_0 G(0,0,0)>_H_p,
    H_phys=ran Pi_0.                                      (26)

It is positive and invariant under the full group. Every vector in ran
Pi_0 is attained with scalar factors equal to one at zero, so its null
quotient completes to exactly H_phys. The simultaneous ordinary kinematic
L2 kernel is zero because c=eta=lambda=0 is a null set; it is not used as
the physical space. If the homogeneous relational constraints are omitted,
omit G and Pi_0: this different retained list yields all of H_p.

The S part of this transported averaging agrees with the previous physical
zero-fiber trace by (11)--(12). The auxiliary and gravity factors retain
their previously declared transported reductions; no continuous pointwise
evaluation of their full original-variable wavefunctions is assumed.

## 7. Shell readouts, exact first vertex, and the remaining price

The physical shell still has omega=sqrt(12A_+) and the same declared
quadratic-clock normalization. Before the full unitary transports its
system readout is

    Psi_v(q_0)=sqrt(6) omega^(-1/2) exp(-i omega q_0)v,
    v in ran Pi_0.                                        (27)

Equation (27) keeps the half-density from (17). With the unitary q/p
Fourier convention it is sqrt(2pi) times the literal inverse transform of
Z* delta(lambda)v, as explicitly fixed in Round13. It is not a kinematic
L2 mass-shell vector. The full solution is the distributional functional
on E obtained by (26) and W, rather than multiplication of arbitrary
distributions by the merely measurable S. This avoids an unjustified
product of a discontinuous coefficient and delta(c).

Pi_0 need not commute with A_+ or omega. Thus (27) need not stay within a
fixed ran Pi_0 as q_0 varies; it is a clock-dependent solution readout,
not an autonomous restriction of omega to that fixed subspace. The shell
half-density cannot be moved through Pi_0 without proof. Bounded physical
operators do have Dirac representatives: extend O on ran Pi_0 to Pi_0 O Pi_0
on H_p, tensor reference identities, and transport by W. This constructs
the abstract physical observable algebra, not the original local field
algebra or a locality theorem.

Nothing in (5)--(27) alters H_vp. In particular the gravity-dressed
expression retains the exact Round15 first jet

    [g] U_g H_vp U_g* = D H_f + Q_TT.T + c.Q = V1.         (28)

The added -P_0^2/12 is g-independent and commutes with U_g. Equation (28)
is the first Weyl-expression jet on the previously specified local tests,
not an operator-norm Taylor series. The auxiliary extension in (19) is
still a declared primary-dependent completion and gauge-unfixing; it does
not prove equality with the original full second-class operator away from
its reduction. On the auxiliary primary reduction V_aux(0)=I, so that
extension does not reintroduce Round14's eliminated-gravity first-vertex
change. Before auxiliaries, (13) is the unchanged full Round15 clock sum.

The constructive compatibility gap is closed for this declared finite
quantum model: one specified self-adjoint C_vp, the auxiliary primary list,
the nonzero gravitational constraint group, the relational homogeneous
momenta, and a positive joint physical norm coexist, while (28) is retained.
The measurable gauge is an exact construction using the already controlled
propagators, not a finite numerical proxy.

Still required for a microscopic TFPT/TOE conclusion are selection of the
Round15 higher-order square prescription, the trace clock and its negative
sheet, the unsubtracted energy reference, the relational momentum choice,
the auxiliary gauge-unfixing, and compatibility with a common microscopic
matter/geometry model. No original homogeneous local current, classical
zero-energy p_0=0 clock chart, chiral/flavor sector, Lorentz/continuum limit,
or volume-uniform complexity bound is obtained. No full classical
counterpart of the measurable gauge or every relational gauge flow is
asserted. Evaluating S can require evolution for arbitrarily large |tau|
near the exceptional subspace, so the proof does not supply an efficient
numerical clock or momentum algorithm.

## 8. Verification boundaries and primary context

The companion exact checker is a regression and falsification aid for
the section, cocycle, domain-independent group identities, clock weights,
and claim boundaries. Its finite channels are not finite CCR matrices and
do not replace the all-Hilbert-space proof above.

The only nonautonomous existence theorem used is the input Round15
common-form construction, with its hypotheses explicitly checked there;
its primary mathematical context is
[Balmaseda--Lonigro--Perez-Pardo, Assumption 3.8 and Theorem 3.10](https://arxiv.org/html/2112.11063v2).
The new straightening identities are proved directly in (5)--(9), and
the norm and clock arguments directly in (11)--(27). The framework is
consistent with [Marolf's refined algebraic quantization](https://arxiv.org/abs/gr-qc/9508015)
and [Hoehn--Smith--Lock's relativistic relational construction](https://arxiv.org/abs/2007.00580),
but no general theorem from those works is substituted for the exact
convergence, normalization or TFPT-specific input checks given here.
