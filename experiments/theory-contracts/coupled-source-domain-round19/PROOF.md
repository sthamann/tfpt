# Round19: coupled electric-sector source domains, Ward force and clock norm

2026-09-07. NON-RH finite-lattice construction. This treats the declared
positive electric/scalar interaction as NEW physical input. It supplies the
source and operator-domain bridge for the coupled parent, not a microscopic
derivation of its coupling, chiral matter or a continuum limit.

## 1. One countable electric-sector model and its exact mass profile

Fix the periodic cubic lattice of N=L^3 sites, L>=2. Each of its 3N links
carries the eight commuting integer electric coordinates of
[the Round18 Hodge parent](../charge-hodge-round18/PROOF.md). Write

    e(n)=n^T G n/2 >=0,
    H_E(E)=(1/N)sum_(x,i)e(E_i(x)),
    epsilon_E=H_E(E)+P_Delta(E) >=0.                          (1)

The full electric configuration set Z^(24N) is countable. Without magnetic
or hopping terms, every configuration is conserved; angles are not silently
replaced by commuting electric coordinates in an interaction that changes E.

At lambda>=0 add the endpoint-symmetric local interaction

    V_lambda(E,phi)=lambda/(2N) sum_(x,i)e(E_i(x))
                                        [phi_x^2+phi_(x+e_i)^2]
                   =(1/2)sum_x u_E(x) phi_x^2,
    u_E(x)=lambda/N sum_i[e(E_i(x))+e(E_i(x-e_i))] >=0.         (2)

Each u_E is a static real field in one sector. The relevant scalar mass
profile is m^2+u_E(x), not a spatially uniform mass on an arbitrary sector.
The coupling is finite range, but its normalization 1/N is a declared global
charge convention, not a derived Maxwell/TFPT continuum scaling.

Let B_delta,eta=H_delta,eta-E_fast be the positive local scalar/tensor/fast
base of Round15. The sector Hamiltonian and its slow limit are

    X_delta,eta,E=B_delta,eta+epsilon_E+V_lambda(E,phi),
    A_delta,E=A_delta+epsilon_E+V_lambda(E,phi),
    A_0,E=A_0+epsilon_E+V_lambda(E,phi).                     (3)

They have positive constant kinetic matrices and smooth polynomial potentials
bounded below. Their unique self-adjoint realizations use the established
compact smooth Schrodinger cores. In particular

    X_delta,eta,E >= H_m+epsilon_E >= e_m+epsilon_E,
    A_delta,E >=e_m+epsilon_E,
    e_m=(1/2)sum_k sqrt(m^2+ell(k))>0,                       (4)

uniformly in E, delta and eta at this fixed nontrivial lattice. The fast
zero-point subtraction is the SAME source-independent constant as before.
It remains an explicit prescription, not a harmless change once the
quadratic trace clock's energy origin is fixed.

## 2. Exact static-profile Ward identities: a force term must be retained

Use precisely the original Ward functions rho_m,j_i,tau_m,ij from
`free-scalar-3d/free_scalar_ward.py`, with spacing a. The scalar force is

    phi_dot(x)=pi_x,
    pi_dot(x)=Delta phi_x-[m^2+u_E(x)]phi_x.                  (5)

Define the updated scalar source list

    rho_E(x)=rho_m(x)+u_E(x)phi_x^2/2,
    j_E,i(x)=j_m,i(x),
    tau_E,ii(x)=tau_m,ii(x)-u_E(x)phi_x^2/2,
    tau_E,ij(x)=tau_m,ij(x),                 i!=j.           (6)

The exact **energy** Ward identity still holds:

    partial_t rho_E + sum_i D_i^- j_E,i=0.                  (7)

Its added density derivative u_E phi pi cancels the added force term in
the kinetic energy derivative. The electric profile is static; adding a
term which changes E would require its additional evolution contributions.

For y=x+e_i the change in the time derivative of the original link current
is (u_E(x)phi_x+u_E(y)phi_y)(phi_y-phi_x)/(2a). The changed diagonal stress
divergence is -(u_E(y)phi_y^2-u_E(x)phi_x^2)/(2a). Their sum is

    partial_t j_E,i(x)+Div_i tau_E(x)
       =-[u_E(x+e_i)-u_E(x)] phi_x phi_(x+e_i)/(2a).          (8)

Thus a generic nonharmonic electric configuration produces an exact local
body-force residual. A force-free momentum Ward identity with (6) would be
false. Keeping the OLD stress is worse: it fails even for a nonzero uniform
mass shift. Since the scalar sector Hamiltonian and sources here are quadratic,
the corresponding Heisenberg/Weyl identities have exactly the same polynomial
residual; no higher Moyal term rescues an omitted force.

Equations (7),(8) concern the free scalar INPUT at fixed electric profile,
not an assertion of the same free identity after nonlinear gravitational
backreaction has been switched on. Exact discrete simultaneous translations
of the full electric/scalar model should not be confused with a force-free
continuous scalar momentum current inside a fixed inhomogeneous sector.

## 3. Harmonic sectors have an exact, but charge-dependent, uniform mass

The Hodge constraints select E_i(x)=n_i independently of x. Consequently

    E_charge=sum_i e(n_i),       P_Delta=0,
    u_E(x)=2lambda E_charge/N,
    mu_n^2=m^2+2lambda E_charge/N.                          (9)

Every original constant-mass Ward identity is now recovered by the exact
substitution m^2->mu_n^2, including the original repaired stress and currents.
The corresponding source decomposition and first dressed vertex therefore
hold in each harmonic sector **with that substituted mass**. They do not
claim the original lambda=0 mass or empirical predictions remain unchanged.
This identifies the limiting TT/matter target vertex. A finite delta,eta
auxiliary parent has its own base-dependent first jet; identification with
that target still requires the sequential local-parent limits, as in Round18.

The additive E_charge commutes strongly with the scalar/gravitational source
operators and their dressing: all are electric-sector diagonal and contain no
angle shift. It adds physical energy to the quadratic clock, but no omitted
commutator to the same-sector vertex identity. The corrected physical target
contains A_+(g;mu_n^2)+E_charge and the retained free tensor spectators.

When lambda>0 this is genuinely not a fixed scalar Hamiltonian plus a scalar
charge-energy offset. For a zero-flux sector and one unit source-spinor flux,
the zero-constraint Hamiltonian difference is

    X_(unit)-X_(zero)=1+(lambda/N)sum_x phi_x^2,              (10)

not a scalar multiple of identity. Electric labels still do not change:
the model gives charge-dependent scalar dynamics, not local charged creation
or a magnetic/hopping sector. Coherent electric-sector superpositions may
become correlated with the scalar state despite this exact conservation.

## 4. The actual local preconditioned sources and the unchanged Gaussian

Use the fixed finite stencils A,ell,F_v from
[Round18's preconditioned chart](../preconditioned-local-parent-round18/PROOF.md).
For each electric sector define

    Q_tilde,H(E)=[A tau_E+ell rho_E]/2,
    Q_tilde,v(E)=F_v j_E,
    F_v=2ell I_3-(3/2)d d*.                                (11)

They are real Weyl quadratics in scalar variables with finite spatial support,
though their coefficients grow without bound over the electric sectors.
They retain their self-adjoint metaplectic closures sectorwise. With A t=2ell,
the mass-profile correction is especially simple:

    Q_tilde,H(E)-Q_tilde,H(m)=-(1/4)ell[u_E phi^2],
    Q_tilde,v(E)=Q_tilde,v(m).                              (12)

The scalar source correction is a multiplication polynomial; its spatial
Laplacian acts on the coefficient field u_E phi^2, not only on phi. Omitting
derivatives/differences of u_E here would change the source. The sum of each
preconditioned source over sites still vanishes, as the stencils kill means.

In nonharmonic sectors (11) is a DECLARED source list for the new full
constraint completion. Its analytic covariance below does not require (8)
to vanish. No original force-free Ward, complete native diffeomorphism or
old first dressed-vertex identity is asserted on those sectors. On harmonic
sectors it is exactly the mass-substituted original list, so the corresponding
vertex conclusion of Section 3 is available.

The local parent's gradient stress representative is unchanged even for a
nonconstant profile. Pointwise in all six tensor components,

    sigma_E=tau_E-t[pi^2-(m^2+u_E)phi^2]/2
           =tau_m-t[pi^2-m^2 phi^2]/2=sigma_m.              (13)

All trace shifts cancel. Therefore the complete fast Hessian K_delta,
quadratic displacement f_delta, fast energy E_fast and Gaussian isometry
J_delta,eta are independent of E. The positive coupling in (2) is added only
to the slow multiplication potential; it is not inserted again into the
fast source or zero-point subtraction.

Exactly, with J=I_electric tensor J_delta,eta,

    (X_delta,eta,E J-J A_delta,E)psi
           =(B_delta,eta J-J A_delta)psi.                  (14)

The extra potential and epsilon_E commute with J. The Round17 residuals for
every ordered source square also apply to (11), since at each fixed E it
is a real quadratic with fixed coefficients. Their constants may depend on
E; no sector-uniform source bound follows from the unmodified Gaussian.

## 5. Countable direct sums specify the domains, not a formal infinite sum

Let H_b be the original finite-dimensional-coordinate base Hilbert space.
The coupled Hilbert space is

    H_coupled=direct_sum_(E in Z^(24N)) H_b.

The exact self-adjoint base is the direct sum of (3), with domain

    Dom X={Psi: Psi_E in Dom X_E for every E,
                      sum_E ||X_E Psi_E||^2<infinity}.       (15)

Finite electric support with compact smooth base factors is an operator
core: first truncate the square-summable graph norm, then use each sector's
Schrodinger core. Positivity and (4) hold on the entire direct sum. A real
source Q_i,alpha is likewise the self-adjoint direct sum of its sector
closures, with sum_E ||Q_i,alpha(E)Psi_E||^2 finite. Neither one common
unweighted source domain nor boundedness in E is assumed.

On the independent gravitational site chart set

    rho_i(c)=r_i^2+|v_i|^2+|(bv)_i|^2,
    h_E(c)=X_E+g sum_i c_i.Q_i(E)
                         +g^2 sum_i rho_i sum_alpha Q_i,alpha(E)^2, (16)

always as the closed form of
[the cellwise theorem](../local-source-stability-round18/PROOF.md). The active
set I(c) is independent of E and invariant along the shear. At fixed c the
global form domain is the square-summable direct sum of the sector form
domains, with the positive norm h_E+N||.||^2. Equivalently, it is the base
form domain intersected with the active direct-sum source graph domains when
g is nonzero; at g=0 it is simply the base form domain.
The uniform inequalities

    h_E>=X_E-N/4,
    q_XE+(g^2/2)sum_i rho_i S_i,E+(N/2)||.||^2
                                 <=h_E+N||.||^2,
    |partial_t(h_E+N||.||^2)|<=3(h_E+N||.||^2)               (17)

give closedness and one all-time common-form propagator, or equivalently
the direct sum of the sector propagators. Their proofs use only the finite
source count, positivity and quadratic source structure, not an electric-
independent coefficient bound. Strong parameter continuity across inactive
strata follows sectorwise and then by uniformly small Hilbert tails.
The nonautonomous form theorem is the same one used in Round17/18; its
common-domain hypotheses and regularity are reviewed by
[Balmaseda, Lonigro and Perez-Pardo](https://arxiv.org/html/2112.11063v2).

The determinant-one gravitational shear therefore gives the full covariant
self-adjoint generator on L2(C;H_coupled). Its maximal domain is the strong
difference-quotient domain of that group; it is not defined by guessing an
infinite sum of formal differential expressions. The added gravitational
mean gauge pairs are exactly the declared Round18 choice, not homogeneous
physical gravity or a place to discard the coupled electric energy.

## 6. Direct-J limits on the whole coupled Hilbert space

For every fixed electric sector and characteristic, (14), the source-square
residuals and the Round17 subset form-core argument prove the full direct-J
propagator limit. The added V_lambda is nonnegative, so the varying-space
lower-bound/compactness proof still controls the complete slow kinetic and
positive coupled potential. Next delta->0 follows by compact-local positive-
potential convergence. Global potential form domains need not coincide.

To pass to arbitrary electric superpositions, take a finite set F of sectors.
For any initial Psi in the coupled Hilbert space, the error outside F is at
most 2||Psi_(F complement)||, uniformly in time and both auxiliary parameters:
all propagators are unitary, preserve E, and J is an isometry diagonal in E.
Inside F the maximum of finitely many sector errors tends to zero uniformly
on each compact time interval. Send eta->0 at fixed delta, then delta->0,
then exhaust F. This proves strong compact-time uncompressed convergence for
every Psi, without interchanging an unbounded source sum with a limit.

The same argument applies after the bounded harmonic projector P_H, to the
full gravitational covariant group, and to finite products of uniformly bounded
observables with the relevant intertwining property. The exact identity
J=I_electric tensor J_old means bounded charge-only operators commute with J.
That does not make harmonic charge shifts spatially local or preserve their
energy-dependent clock slice weight without the appropriate normalization.

There is no operator-norm rate uniform in E, volume, c or all states, no
arbitrary simultaneous eta=delta choice, and no newly proved electric-label
mixing interaction. The statewise finite-tail argument is the precise extension.

## 7. Hodge projection, full-clock tube and correct positive physical norm

All divergence/curl generators, their compact averaging projector P_H and
electric-sector projections commute strongly with X, (11), every (16) and
the full gravitational propagator: each acts diagonally in the same electric
configuration labels. Thus exact Hodge reduction keeps the harmonic sectors
and their ordinary positive sum norm without a leakage approximation.
The finite penalty does not replace exact Hodge projection at all energies.

After gravitational constraint reduction the positive base is X. For its
quadratic clock C_X=X-P_q^2/12 on the negative P_q sheet, define

    omega_X=sqrt(12X),       D_X=3^(1/4)X^(-1/4),
    Psi_v(q)=D_X exp(-iq omega_X)v.                         (18)

The common bound e_m in (4) permits the SAME spectral interval
I=(-e_m/2,e_m/2) for every electric sector. For a spectral value z of X_E,

    lambda=z-p_q^2/12,
    p_-=-sqrt(12(z-lambda)),
    dp_-/d lambda=6/sqrt(12(z-lambda)).                      (19)

The exact half-density chart and constraint average therefore give

    ||v||_phys^2=sum_E ||v_E||^2,
    ||Psi||_(K_X)^2=(1/6)||omega_X^(1/2)Psi||^2,
    D_X:H_coupled -> K_X=Dom(X^(1/4)) is unitary.             (20)

After P_H the sum runs over the three harmonic integer fluxes only. Both
the charge energy and its induced scalar mass remain inside X_E in (18),(19).
A charged shift generally changes both, so a unitary on normalized initial
data is represented on slice amplitudes by D_X T D_X^(-1), not an unweighted
shift that silently leaves the old clock norm fixed.

For the unreduced gravitational full generator H_full, do NOT take its
positive square root: it is not semibounded. Apply the Round16/18 characteristic
trivialization sectorwise and take its countable direct sum S. The positive
observable is X_cov=S X S*, and the negative-sheet tube is defined by
X_cov-P_q^2/12 in I. The full constraint H_full-P_q^2/12 then transports to
the separated shear generator plus the same lambda multiplier. This gives
the declared full joint clock construction; it does not assume the raw base
band is invariant under H_full.

Finally D_XB J D_XA^(-1) is an exact isometry of weighted clock slice spaces
at each auxiliary parameter. Their compact-time dynamical limits follow from
the base direct-J limit, the common e_m bound, functional calculus with energy
cutoffs and the finite electric-tail argument, exactly as in Round16. No
divergent charge-dependent normalization is dropped from the measure.

## 8. Scope and reproduction

The checker imports the literal Ward source, verifies the endpoint-derived
mass profile, exact energy Ward identity, precise inhomogeneous momentum force,
uniform harmonic mass substitution, unchanged TT representative and fast
encoding input, local preconditioned source correction, source-sensitive
negative controls and the clock half density. Finite algebra supports these
analytic domain/direct-sum statements; it does not certify an interacting
continuum theory or replace the infinite-dimensional Hilbert spaces by matrices.

The new lambda coupling, electric-curl constraint, source completion and clock
energy origin remain choices. The harmonic-sector vertex is the mass-substituted
one; arbitrary off-Hodge sectors have declared sources with an explicit force
residual, not an old force-free gravity Ward derivation. No nonabelian/chiral
matter, local charge-changing fields, microscopic uniqueness, complete TOE or RH
claim is made.
