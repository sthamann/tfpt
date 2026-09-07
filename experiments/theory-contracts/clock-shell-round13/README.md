# Exact clock-assisted constraints for the chosen finite positive model

Date: 2026-09-06. Non-RH, unpromoted research. The Hamiltonian is the actual
chosen reduced scalar/TT completion. The quadratic trace-clock constraint is
still postulated, not derived from TFPT. This construction changes the momentum
constraints into clock-dependent relational quantities; it does not repair the
old time-independent spatial momentum on the original phase space.

## 1. A uniform-in-coupling lower bound for the actual operator

Use the unique positive self-adjoint operator A_g from
[the actual reduced domain proof](../local-positive-auxiliary/QUANTUM_DOMAIN.md):

    A_g = H_m + 1/2 sum_alpha [P_alpha^2
                    + r_alpha^2 (Q_alpha+g T_alpha(phi)/r_alpha^2)^2].       (1)

Here r_alpha>0, T_alpha is the actual real gradient-only TT stress, and
H_m is the finite free scalar Hamiltonian including its uniform mode. Write

    e_m = 1/2 sum_k sqrt(m^2+ell(k)),
    e_TT = 1/2 sum_alpha r_alpha,
    e_* = e_m+e_TT.                                                        (2)

In the massless case the zero-frequency scalar contributes zero and remains a
free coordinate. The standard oscillator factorization gives H_m>=e_m. For
each fixed phi, the second term of (1) is a translated tensor oscillator,
unitarily equivalent to its unshifted version and bounded below by e_TT.
Integrating this fiber inequality over phi and adding the matter form yields

    A_g >= e_* I, for every real g.                                        (3)

This does not conjugate the full matter kinetic energy or omit the shear's
kinetic correction. It is an inequality between quadratic forms of the two
actual summands. It extends from the common test domain by form closure.
For connected n>1 lattices, e_*>0 even at m=0. The n=1,m=0 free exception
has e_*=0 and is excluded from the quantum spectral-tube construction below.

This is a lower bound on the **unsubtracted energy**, uniform in coupling at
fixed regulator. It is not a uniform excitation gap above the interacting
ground state, a continuum bound, or a TFPT prescription for the energy zero.
Subtracting a vacuum constant changes the hypothesis used below.

## 2. Classical construction with the unchanged quadratic clock

The actual classical H_g is complete at every finite regulator. For m>0 its
energy sublevels are compact: the matter potential bounds phi, the kinetic
energy bounds all momenta, and the shifted tensor squares then bound Q. For
m=0 the nonconstant scalar is bounded by the finite Poincare inequality; its
constant coordinate is decoupled and moves linearly. The remaining variables
stay in a compact energy sublevel. The smooth polynomial vector field therefore
has no finite-time escape. Denote its global canonical flow by Phi_g^t.

Add the already-postulated canonical trace pair (q,p), with p<0, and keep

    C_g = H_g(z)-p^2/12,             T(q,p)=-6q/p.                          (4)

Then {T,C_g}=1. For the original mutually commuting centered total momenta
J0_i(z), including TT momentum, define

    K_i(g;q,p,z) = J0_i(Phi_g^(-T(q,p)) z).                                (5)

This is a smooth global function for finite (q,z) and p<0 at each finite g.
Along the C_g flow, T increases at unit rate while z evolves by Phi_g^t;
the two changes cancel. Hence, strongly and exactly,

    {K_i,C_g}=0,                       {K_i,K_j}=0.                        (6)

For the second equality, the system part is a common canonical pullback of
{J0_i,J0_j}=0. The clock contribution vanishes because both functions depend
on (q,p) only through the same scalar T: it is proportional to {T,T}=0.
At g=0, {J0_i,H_0}=0 implies K_i=J0_i. At q=0 this also holds for every g.
Rank of the three spatial constraints at fixed clock values is preserved by
the canonical flow. The clock constraint is independent at regular points:
in reference coordinates it has nonzero p derivative -p/6 on p<0.

Equations (4)–(6) do not change H_g or any of its prescribed vertices. They
change the spatial constraints. The K_i are initial-data charges referred to
the chosen clock origin, generally nonlocal functions of the full dynamics.
They are not asserted to be local spatial translation/diffeomorphism currents.
Clock-coordinate translations alone generally do not preserve them:

    {p,K_i}=(6/p) partial_T[J0_i(Phi_g^(-T)z)],                            (7)

which is nonzero when the old J0_i is not conserved. There is no claim of a
uniform limit as p approaches zero, an origin-independent choice, or efficient
evaluation of the full nonlinear flow.
The classical zero-energy vacuum has p=0 on the clock shell and remains outside
this construction; its earlier clock singularity is not regularized.

## 3. Exact quantum spectral coordinates, without replacing C_g

Set omega_g=sqrt(12A_g). On L2(R_q) tensor H keep the actual self-adjoint
joint multiplier C_g=A_g-P^2/12, with P=-i partial_q. Choose the negative
P sheet and a fixed interval I=(-e_*/2,e_*/2). The two spectral restrictions
commute and define a reducing kinematic subspace K_I of the original C_g.
This is an open spectral neighborhood of its physical zero shell, not all
off-shell states or the discarded positive-frequency sheet.

In a spectral representation H=integral H_E dmu(E) of A_g, introduce

    lambda = E-p^2/12,
    p_-(E,lambda)=-sqrt(12(E-lambda)),
    w(E,lambda)=dp_-/dlambda=6/sqrt(12(E-lambda)).                         (8)

For every lambda in I, E-lambda>=e_*/2>0. Thus all E in the spectrum are
available in every lambda fiber. The exact change of variables

    (Z_g f)(lambda,E)=sqrt(w(E,lambda)) f(E,p_-(E,lambda))                 (9)

is unitary from K_I to L2(I,dlambda) tensor H. Its inverse evaluates at
lambda=E-p^2/12 and multiplies by w^(-1/2). The norm identity follows from
dp=w dlambda; no Lebesgue density or discreteness of the E spectrum is needed.
In particular the construction covers the massless continuous uniform mode.

The original constraint, including its operator domain, becomes

    Z_g C_g Z_g^* = M_lambda tensor I.                                  (10)

On this bounded interval it is bounded. On a general allowed interval its
domain would be the exact multiplier domain. No square-root constraint has
been substituted for C_g, and its group-averaging Jacobian has not been lost.

## 4. Strongly commuting self-adjoint relational momenta

The original J0_i have simultaneous self-adjoint realizations on H. To see
this directly, centered differences are commuting real antisymmetric matrices
on scalar configuration space and on the translation-invariant TT space.
Their commuting orthogonal pullbacks define a strongly continuous R^3 unitary
representation. Its generators are the symmetric expressions
-pi.D_i^c phi-P_TT.D_i^c Q_TT. Finite Hermite spans for the isotropic reference
oscillator decompose into invariant finite-dimensional levels, providing cores
for the generators. Thus no finite CCR approximation is involved.

Define, on the restricted original kinematic space,

    Jcal_i(g)=Z_g^*(I tensor J0_i)Z_g,
    Dom Jcal_i = Z_g^* L2(I;Dom J0_i).                                  (11)

The domain notation includes integrability of ||J0_i v(lambda)||^2.
These operators are self-adjoint and strongly commute with each other and
with the unchanged C_g. These are transported joint spectral measures, not
formal commutators on an unspecified common domain. At g=0, J0_i commutes
strongly with A_0, so (9) intertwines the old I tensor J0_i exactly; the free
seed is recovered on the spectral tube. At g!=0, mixing system energies
requires a compensating clock-momentum change which keeps lambda fixed.

This supplies an exact quantum relational counterpart of the classical
construction. It is a declared spectral prescription, not a claim that the
naive Weyl quantization of every coefficient in (5) equals (11). No smooth
operator-norm perturbation family or evaluated interacting spectral transform
is asserted. Functional calculus gives existence and domains, not an efficient
local formula for these operators.

## 5. Joint averaging and the physical inner product

Let G be the compact closure of the three commuting orthogonal configuration
flows. Its unitary pullback representation has normalized Haar projector

    Pi_0 = integral_G U0(a) da,
    H_phys = ran Pi_0 = intersection_i ker J0_i.                         (12)

The equality holds even when the R^3 image is dense rather than closed: strong
continuity identifies its fixed vectors with those of its compact closure.
The physical space is nonzero; an isotropic normalized Gaussian is invariant.
This is not the previous genuine finite lattice-translation projector, nor
an assertion that the interacting A_g preserves H_phys as a fixed subspace.

In Z_g coordinates take the dense space of finite sums u(lambda)v, with
u smooth compactly supported inside I and v in H. Time averaging with ds/(2pi)
and normalized G averaging give the positive form

    eta(f,h)=< (Z_g f)(0), Pi_0 (Z_g h)(0) >_H.                         (13)

Integration by parts twice in lambda makes the time matrix element decay as
O(|s|^(-2)); the compact group causes no convergence difficulty. Fourier
evaluation gives (13). Its null quotient completes to H_phys, since arbitrary
v in ran Pi_0 is reached with u(0)=1. The kinematical L2 zero kernel remains
zero, as lambda=0 has measure zero.

At the shell (9) gives exactly the previous quadratic-clock factor:

    (Z_g f)(0,E)=sqrt(6/omega_g(E)) f(E,-omega_g(E)).                     (14)

Thus the old quadratic group-averaging normalization is retained, not replaced
by the unit-weight normalization of P+omega_g. The normalized solution readout
for suitable spectral-domain vectors is

    Psi_v(q)=sqrt(6) omega_g^(-1/2) exp(-i omega_g q) v,
    v in H_phys.                                                       (15)

The distributional extension and positive norm use (13), not a false L2
mass-shell kernel. Formula (15) is not an assertion that every physical vector
lies in all differentiation domains. With the unitary q/p Fourier convention,
(15) is sqrt(2pi) times the literal inverse Fourier transform of the rigging
distribution Z_g^* delta(lambda) v. This is an explicitly chosen normalization
of the solution readout, consistent with the previous Klein–Gordon norm; it
does not alter the Haar normalization in (13). The label q in (15) is not
claimed to be a self-adjoint clock-position operator on the spectrally
restricted space, which need not be preserved by the original q operator.

## 6. The price of this construction

The actual A_g need not commute with J0_i. Accordingly exp(-i omega_g q)
need not preserve the fixed subspace H_phys. One must not call its restriction
an autonomous Hamiltonian on that fixed space. The maps (15) instead describe
clock-dependent solution readouts; the complete solutions satisfy the newly
defined joint constraints. Raw bounded observables must also be made compatible
with those constraints before being interpreted as physical local readouts.

Every bounded operator on H_phys can be extended as Pi_0 O Pi_0 on H and then
transported by Z_g as a bounded Dirac observable on the spectral tube. This
does not faithfully embed the original full local scalar algebra: compression
is not multiplicative. No locality or continuum obstruction is removed.

The construction settles existence of a joint constrained model **after** this
explicit relational choice. It does not derive the trace clock, homogeneous
gravity, a microscopic state or a preferred time origin. Nor does it solve the
unreduced auxiliary Hamiltonian's domain problem. The negative spectral sheet,
energy reference and replacement momentum prescription remain inputs.

## 7. Verification and context

`clock_shell_checker.py` checks the actual periodic matter quadratic form,
its mode frequencies and free zero-point bound, exact half-density/Jacobian
and shell identities, genuine energy-channel transformations on arbitrary
continuous-clock test functions, and failure controls for the wrong Jacobian,
uncompensated clock momentum and naive clock-origin translation. Its finite
energy channels are algebraic witnesses for (8)–(11), not truncated CCR or an
approximation to the interacting TFPT spectrum. The infinite-dimensional
unitarity and domain results rest on the proof above.

Primary methodological context: [Marolf, refined algebraic quantization with
a single constraint](https://arxiv.org/abs/gr-qc/9508015) and
[Hoehn, Smith and Lock, relational quantum dynamics in relativistic settings](https://arxiv.org/abs/2007.00580).
The special spectral tube and chosen momentum prescription above are derived
explicitly here; no TFPT or microscopic completion is imported from those works.
