# One complete finite conditional constraint model, including auxiliaries and clock

Date: 2026-09-06. NON-RH Round14. This constructs a joint classical/quantum
constrained model for the chosen finite scalar/TT sector. It uses an explicit
first-class constraint-ideal completion, auxiliary gauge-unfixing, and the
postulated negative-sheet trace clock with relational homogeneous momenta.
It is not a proof of the unchanged old off-shell Hamiltonian, a microscopic
choice of these prescriptions, or complete T1–T8/TOE closure.

## 1. Inputs and the precise physical equivalence being claimed

Fix a finite connected periodic lattice with n>1 and scalar mass m>=0.
Let A_+ be the unique positive TT/matter Hamiltonian of the actual chosen
completion, including every scalar coordinate. Round13 proves A_+>=e_*>0
uniformly in g at fixed regulator, with the unsubtracted energy convention.
Let H_z be its Hilbert space. For the nonzero gravitational constraints
c=(r,v), define the original free gauge quadratic

    K_c=-i(bv).partial_r+q(c),
    q(c)=r.B_H.r/2+v.B_v.v/2,
    A_c=[[0,b],[0,0]], Tr A_c=0, A_c^2=0.                            (1)

The companion first-class-completion theorem proves self-adjointness,
an exact Schwartz core, and the unitary action

    U_c(t)f(c)=exp(-i I_t(c))f(exp(-t A_c)c),
    I_t(c)=integral_0^t q(exp(-u A_c)c)du.                           (2)

In particular U_c(t)f(0)=f(0), and U_c(t)^*a(c)U_c(t)=a(exp(t A_c)c)
for every bounded Borel a. Set H_first=A_++K_c on its joint spectral domain.

Relative to the actual eliminated seed, the change is precisely

    Delta H=-g r.B+g v.B_v.J_v,                                    (3)

with the actual quadratic matter sources. It lies in the first-class
constraint ideal and vanishes on c=0. Its Hamiltonian vector field there
is a gauge-direction combination; every gauge-invariant physical observable
has the same restricted evolution. The free H_f is unchanged. Off c=0 the
first vertex is changed, so this is not silently called the old H_sr.
At the quantum level equivalence to A_+ is proved by the explicit reduction
below; it is not inferred from an unspecified extension of the old operator.

Introduce auxiliary momenta eta and the metaplectic direct-integral unitary
V(eta)=exp(-i eta.f), f=-K_aux^-1 s, from auxiliary-domain-round14. After
the declared gauge-unfixing, keep eta=0 and use V H_first V*. The secondary
quadratic has been removed in the joint spectral-calculus sense; the
second-class total Hamiltonian before that removal does not preserve eta.
Simultaneous gravity dressing U_g gives W_0=U_g V. All these choices and
their off-surface changes are part of the constructed model.

## 2. Add the unchanged quadratic clock on the correct transported tube

Add the already-postulated trace pair (q_0,p_0), P_0=-i partial_(q_0),
with negative P_0 sheet. Use the Round13 interval I=(-e_*/2,e_*/2) and its
unitary clock transformation Z, acting only on H_z and this clock:

    lambda=E-p_0^2/12,
    p_-(E,lambda)=-sqrt(12(E-lambda)),
    (Zf)(lambda,E)=sqrt(6/sqrt(12(E-lambda))) f(E,p_-).                (4)

This is valid for any spectral type of A_+. It uses no positivity of the
full unbounded H_first. The reference Hilbert space is

    H_ref=L2(R_c^d) tensor L2(R_eta^a)
          tensor L2(I_lambda) tensor H_z.                           (5)

Define the single unitary identification from (5) to a subspace of the
original variables by W=W_0 Z*. Its range is the TRANSPORTED tube W_0 K_I,
not in general the old raw A_+-clock tube. More explicitly put

    B_g=W_0 A_+ W_0*,   K'_c=W_0 K_c W_0*=U_g K_c U_g*.

These are strongly commuting self-adjoint operators and B_g>=e_*.
The chosen subspace is P_0<0 and B_g-P_0^2/12 in I. Both W_0 factors
commute with P_0, but need not commute with A_+.

On this specified subspace the completed full clock constraint is

    C=W C_ref W*,    C_ref=K_c+M_lambda,
    C=K'_c+B_g-P_0^2/12.                                          (6)

The full C can have unbounded positive and negative spectrum because of
K'_c. The tube is NOT a bounded interval of this total constraint spectrum.
Since lambda is bounded on I, Dom C_ref is the tensor extension of
Dom K_c. Equivalently its domain is the exact joint multiplier condition
for (kappa+lambda)^2. Equation (6) proves self-adjointness with that
transported domain, rather than a formal addition on an unspecified core.

## 3. The full constraint algebra is represented by an actual unitary group

Let J0_i be the simultaneous self-adjoint centered homogeneous momentum
generators on H_z, and G their compact orthogonal-flow closure. These are
the prescribed free seed generators, not conserved currents of A_+.
In reference variables define

    c_a=M_(c_a),  eta_j=M_(eta_j),  J_i=I tensor J0_i.                (7)

Their domains are the appropriate multiplication or L2 graph domains.
They strongly commute with one another. J_i and eta_j strongly commute
with C_ref. The c_a have the exact strong covariance

    exp(it C_ref) a(c) exp(-it C_ref)=a(exp(t A_c)c).                 (8)

Thus C_ref and c are a semidirect constraint group, not a falsely asserted
set of strongly commuting operators. One concrete representation is

    R(t,u,zeta,a)=exp(i u.c) exp(i zeta.eta)
                   exp(-it C_ref) U0(a),   a in G.                 (9)

The action on the dual u variable has determinant exp(-t Tr A_c)=1.
Hence the semidirect group is unimodular; product Lebesgue measure in
(t,u,zeta), together with normalized Haar measure on G, is valid on both
sides. Conjugating the entire representation by the same W gives the
joint gravitational, auxiliary and clock-relative constraints in the
original transported space. No individual unbounded commutator alone is
used to claim this group-level closure.

## 4. Simultaneous averaging, a positive norm, and the complete physical space

Take reference tests which are finite sums of

    F(c,eta,lambda)=a(c)b(eta)u(lambda)v,
    a,b smooth compactly supported, u in C_c^infinity(I), v in H_z.  (10)

They are dense and stable under (9) up to finite sums of the same type.
Their images under W define the averaging tests; no preservation of the
original full joint Schwartz space by W is assumed.

Matrix-element averaging of (9), with measure

    dt du dzeta/(2pi)^(1+d+a) times normalized Haar on G,

is absolutely convergent on pairs of tests (10). Here is the required
joint, not merely iterated, convergence argument. Fourier integration by
parts in c and eta bounds the matrix element by an integrable power of
(u,zeta), times a polynomial in t. The only t-dependent coefficient is
the quadratic phase I_t(c), of degree at most three in t, and the affine
shear exp(-t A_c). Compact support of the bra coefficient bounds all
spatial integrals; derivatives of the ket coefficient grow at most
polynomially in t. Independent integration by parts in lambda produces
arbitrarily rapid inverse powers of t, dominating that polynomial.
The compact G matrix elements are bounded by ||v||||w||. Choosing the
spatial derivative order above d+a and then a sufficiently large lambda
order proves absolute integrability of the full product-group integral.

Fourier evaluation in u and zeta sets c=eta=0. At c=0, both the phase
and shear in (2) disappear. Time averaging sets lambda=0, and compact G
averaging supplies Pi_0, the orthogonal projection onto ker J0. Therefore

    eta_phys(WF,WG)=<F(0,0,0), Pi_0 G(0,0,0)>_(H_z),
    H_phys=ran Pi_0=intersection_i ker J0_i.                         (11)

This form is positive. Its null quotient has exactly the indicated
completion: choose the three scalar factors to have value one at zero
to reach any vector of ran Pi_0. An isotropic normalized Gaussian is
invariant under G, so this space is nonzero. The simultaneous ordinary
kinematic L2 zero kernel is zero because c=eta=lambda=0 has measure zero;
it is not substituted for (11).

If homogeneous relational momenta are not imposed, omit G and Pi_0;
then the same construction yields all of H_z. This is an explicitly
different retained constraint list, not a second answer for the same list.

## 5. Readouts, dynamics and what has not been selected

The clock factor of a normalized solution readout is precisely the
Round13 expression

    Psi_v(q_0)=sqrt(6) omega^(-1/2) exp(-i omega q_0)v,
    omega=sqrt(12A_+),  v in ran Pi_0.                              (12)

It carries the same declared global Fourier readout normalization as that
proof. The full distributional solution is obtained from (11) and the
unitary transport W; it is not a kinematic L2 vector on the zero shell.
All half-density weights in (4) are retained on their respective sides
of the physical projection, which need not commute with A_+.

There is no assertion that exp(-i omega q_0) preserves the fixed subspace
ran Pi_0. These are clock-dependent solution readouts for the declared
relational constraints, not an autonomous restriction of the old rest
Hamiltonian to that subspace. Every bounded operator on H_phys does have
a bounded Dirac representative: extend it as Pi_0 O Pi_0 on H_z, tensor
with identities in (5), and transport by W. This supplies the abstract
physical operator algebra, not the original local scalar field algebra
or a spacetime locality theorem.

Classically the same choices also give a complete flow at finite regulator:
the positive physical Hamiltonian has complete flow, K_c is a complete
quadratic flow, and the trace momentum is constant. Both the auxiliary
and gravity dressing canonical maps are global at finite parameters.
For p_0<0, T=-6q_0/p_0 and the old J0 evaluated at backward physical time
-T give globally defined relational classical constraint functions, with
the same semidirect c covariance. Completeness here is a theorem for the
completed Hamiltonian/clock-constraint flow, not for every relational
momentum gauge flow throughout the entire off-shell negative sheet.
The zero-energy classical p_0=0 vacuum remains
outside that clock chart; it is not regularized by the quantum bound.

The constructive quantum-sector task is thus solved for THIS declared
finite completion: one Hilbert space, self-adjoint constraint generator,
exact group closure, positive joint physical norm and Dirac observables.
No interacting Galerkin limit or unproved unchanged-fiber propagator is
assumed anywhere in the construction.

The price is not hidden: the first-class ideal term (3), the auxiliary
primary-dependent completion and gauge-unfixing, the trace clock and
negative sheet, energy zero and homogeneous relational prescription are
inputs. No equality to the old Hamiltonian away from its constraints,
unique microscopic TFPT selection, chirality/flavor/measure, continuum
locality, or full T1–T8 solution follows. A microscopic derivation must
still decide whether this physically equivalent reduced completion is
the intended TFPT realization.

## 6. Dependencies and reproducible checks

The analytic inputs are the [first-class completion](../firstclass-completion-round14/PROOF.md),
the [combined auxiliary reduction](../auxiliary-domain-round14/COMBINED.md),
and the [clock spectral construction](../clock-shell-round13/README.md).
The arguments above supply the common transported tube, semidirect group,
joint absolutely convergent average, and physical operator representation.

Run `joint_constraint_check.py` with the repository's SymPy environment.
Its 20 exact checks cover the phase/group identities and zero-fiber
evaluation, the noncommuting-versus-covariant constraint distinction,
and explicit negative controls for the raw-versus-transported clock tube
and projection/half-density ordering. These finite symbolic checks support
the displayed identities; they do not replace the Hilbert-space proofs.
The Round14 runner also revalidates the actual-source dependencies.
