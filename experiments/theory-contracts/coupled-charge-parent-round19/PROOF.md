# Round19: one positive local scalar–charge parent with reciprocal response

Date: 2026-09-07. NON-RH. This is a declared finite-lattice construction,
not a derivation of the microscopic TFPT dynamics or a completed TOE.
The interaction, its scale, and the electric selection law are additional
inputs. Unlike a tensor sum of independent sectors, the resulting dynamics
changes scalar motion when charge changes and changes charge-transition
energies when the scalar state changes. It generates entanglement.

## 1. Fixed inputs and exact definition

Fix a periodic cubic lattice of side L >= 2, N=L^3 sites, spacing a>0,
scalar mass m>0, and the Round15 parameters delta, eta>0 and real g.
Let B=B_delta,eta(g,m) be the [positive local Round15 base](../local-parent-round15/PROOF.md),
after subtracting its fast oscillator ground energy. Its Hilbert space has
35N noncompact canonical pairs and B >= e_m>0. The omitted tensor channels
are not discarded. Distinguish the rotor electric labels below from the
Round15 continuous auxiliary electric field.

Use the complete integral basis of the [Round18 charge parent](../charge-hodge-round18/PROOF.md):

    G = B_E8^T B_E8,  e(n)=n^T G n/2,  n in Z^8.

This is the full even unimodular positive E8 Gram form, including cross
terms and the spinor coset; it is not an eight-coordinate diagonal surrogate.
Put eight rotors on each oriented edge, electric label F_i(x) in Z^8.
The Hilbert space is l2(Z^(24N)), without an electric cutoff. Let D and C
be the integer backward divergence and forward curl of Round18. Define

    H_F = (1/N) sum_(x,i) e(F_i(x))
          + Delta sum_x [e(D(x)) + sum_(i<j) e(C_ij(x))],  Delta>0,
    V_lambda = lambda/(2N) sum_(x,i) e(F_i(x))
                             [phi_x^2 + phi_(x+ei)^2],  lambda>=0,
    X_lambda = B + H_F + V_lambda.                            (1)

Tensor identities are understood. Every interaction summand is positive,
supported on one edge and its endpoints. The endpoint average is invariant
under edge reversal and cubic rotations because e(-n)=e(n). The explicit
1/N normalization is declared, not a locality-independent continuum scaling
result. The new coupling lambda is not the clock spectral coordinate.

## 2. Infinite electric space, domains, and positivity

All electric operators in (1) are commuting multiplication operators. In
the electric sector F,

    X_F = B + h_F + (1/2) sum_x u_F(x) phi_x^2,
    u_F(x) = (lambda/N) sum_i [e(F_i(x))+e(F_i(x-ei))] >= 0.   (2)

Each fiber is a finite-dimensional elliptic Schrodinger operator with a
smooth polynomial potential bounded below after the same constant fast
subtraction. Its C_c^infinity core defines the unique self-adjoint operator;
equivalently use the closed positive form. Addition of the nonnegative
potential leaves the lower bound X_F >= e_m+h_F intact. This does not assert
that an arbitrary unbounded perturbation preserves an operator domain.
The exact joint operator is the self-adjoint direct sum with domain

    Dom X_lambda = {Psi : Psi_F in Dom X_F,
                          sum_F ||X_F Psi_F||^2 < infinity}. (3)

The finite-electric-support C_c^infinity subspace is an operator core:
first truncate the countable direct sum in its graph norm, then approximate
in each of its finitely many fiber graph norms. It follows that
exp(-it X_lambda) exists for every real t, with no charge truncation and no
unproved uniform-in-F operator bound. Also X_lambda >= e_m+H_F.

The compact Hodge constraint projector P_H is the diagonal projection onto
D=C=0. It strongly commutes with (1). Round18's all-volume integer Hodge
theorem gives F_i(x)=n_i, so its physical space and Hamiltonian are

    H_H = direct sum_(n in (Z^8)^3) H_B,
    C(n)=sum_i e(n_i),    R=(1/N) sum_x phi_x^2,
    X_H(n)=B+C(n)+lambda C(n)R
          = B_delta,eta(g,mu_n)+C(n),
    mu_n^2=m^2+2lambda C(n)/N.                              (4)

Only the scalar mass changes: the auxiliary Gaussian center f_delta, the
fast Hessian, and the TT gradient source sigma are mass-independent. There
are three copies of E8 at this stage, not one. Non-Hodge sectors still have
the absolute lower bound e_m+2Delta; this is not a spectral gap separating
all high-energy Hodge states from all non-Hodge states.

## 3. The full source lift and its actual conservation boundary

Apply [Round18's local gauge lift](../preconditioned-local-parent-round18/PROOF.md)
to each X_F, with the mass profile (2). The full field count in this edge
model is 35N noncompact base pairs, 24N compact rotor pairs, and 4N new
noncompact gauge pairs before the clock. Its locality is in the new gauge
variables; it does not restore the native nonlocal inverse chart.

The [coupled source-domain proof](../coupled-source-domain-round19/PROOF.md)
defines the real quadratic sources Q_F on each electric fiber, proves the
active-source form domains, and constructs the covariant all-time group.
The gauge-source stabilizers are positive local squared-source terms.
Their full off-shell Hamiltonian need not be bounded below; X_lambda is
the positive physical c=0 generator. One must not take the square root of
that full indefinite Hamiltonian.

The scalar energy Ward identity holds with rho=rho_m+u_F phi^2/2, unchanged
j, and tau_ii=tau_m,ii-u_F phi^2/2. The scalar momentum Ward equation has
the force residual

    -(u_F(x+ei)-u_F(x)) phi_x phi_(x+ei)/(2a).              (5)

It vanishes on every Hodge sector, where u_F=2lambda C(n)/N is constant.
Thus the old force-free source identity survives there with the new mass
mu_n, not with the original m. These are the quadratic scalar input Ward
identities, not identities for free currents after gravitational backreaction.
Away from the Hodge sector the residual is
retained; a full conserved scalar-plus-dynamical-electric stress tensor is
not proved. The electric Hamiltonian commutes with the scalar/gravity
dressing because both are diagonal in F. Its energy is an additional
constant in a fixed sector, not a hidden scalar momentum term.

Compact Hodge averaging and c=0 rigging commute: on finite-electric-support
continuous gauge test vectors the positive form is exactly

    sum_(F: D=C=0) <Psi_F(0), Phi_F(0)>_B.                 (6)

Completion yields (4). The covariant group has the same evaluation action
on each fiber. For the clock, use the proper spectral tube and the negative
P0 branch of the source-domain proof with common gap e_m; the resulting
physical generator is the prescribed function of X_H. No assertion of
positivity of the full gauge generator enters this construction.

## 4. A one-copy variant without branch averaging by fiat

The [full-frame finite-gauge construction](../cubic-charge-selection-round19/PROOF.md)
provides a second, explicitly different charge carrier. It has site flux
F_x in (Z^8)^3, full proper-cubic frames f_x in G24 and finite-group links.
Local lock constraints U_xy=f_x f_y^-1 and local frame-dressed flux
selection/synchronization, followed by local finite-gauge averaging, leave
exactly l2(E8), not three orientation branches or unremoved holonomy sectors.
This is added field content and a changed observable net, not a theorem
identifying the original native edge theory with this model.

Let H_frame be its positive local charge Hamiltonian and

    E_x = sum_a e(F_x,a),
    X_frame,lambda = B + H_frame + (lambda/N) sum_x E_x phi_x^2. (7)

E_x is gauge-invariant, commutes with every selection constraint and equals
e(n) on the exact physical kernel. Gauge-transform to body-frame flux
coordinates. The continuous Schrodinger part is a direct sum in the
countable body flux; the finite gauge-projector terms are bounded at fixed
N and commute with the added potential. This supplies a self-adjoint
positive operator by the same fiber/core construction, not a formal
unbounded-tensor-product assertion. Equation (7) reduces exactly to

    X_one(n) = B + e(n)(1+lambda R),  n in Z^8.             (8)

Finite gauge averaging, scalar coupling, and the c-source reduction thus
share one parent. The source lift works orbitwise since E_x is invariant;
on its selected kernel the mass profile is constant. The frame variables
have a finite local state space, not additional noncompact canonical pairs.
The single E8 module and its old cocycle are realized, but no microscopic
principle selecting this added frame/lock construction is supplied.

## 5. Reciprocal response and an exact entanglement witness

Write C(n)=sum_i e(n_i) for (4), or C(n)=e(n) for (8). On the finite-charge
Schwartz core, let T_r be the physical unitary charge shift with the inherited
cocycle. Its phase cancels in conjugation. Directly from (4)/(8),

    T_r^* X T_r - X = [C(n+r)-C(n)](1+lambda R),
    d pi_x/dt |_interaction = -2lambda C(n) phi_x/N.       (9)

The first equation makes charge-transition energy depend on the scalar
state; the second makes scalar acceleration depend on charge. If lambda>0
these operators cannot be a sum of an independent scalar Hamiltonian and
an independent charge Hamiltonian. All electric charges are nevertheless
conserved by X. Charged shifts are observables/interventions, not dynamically
generated pair production, and remain extended over the finite volume.

For a quantitative witness choose charge states 0 and n_s with C(n_s)=1
(the complete spinor vector). Prepare their equal superposition and any
normalized Schwartz base vector psi. Put H0=B and H1=B+1+lambda R. The two
conditional vectors are exp(-itH0)psi and exp(-itH1)psi. The exact reduced
charge purity is

    P_charge(t) = [1+|<exp(-itH0)psi,exp(-itH1)psi>|^2]/2
                = 1-(lambda^2/2) Var_psi(R)t^2+o(t^2).   (10)

Proof: multiply the second-order strong Taylor expansions on their common
Schwartz core. The real part of <H0 H1> equals that of <H1 H0>; hence the
modulus square loses Var(H1-H0)t^2. The identity contribution in H1-H0
drops out of the variance. No commutativity between B and R is assumed.
For independent scalar Gaussians |psi|^2 proportional to exp(-sum phi_x^2),
Var(R)=1/(2N), so P_charge(t)=1-lambda^2 t^2/(4N)+o(t^2).
For every finite N and lambda>0 this is below one for sufficiently small
nonzero time: the interaction genuinely creates entanglement. The result
is not a claimed long-time entanglement rate or a thermodynamic bound.
Here t is the time generated by X. The nonlinear square-root clock has a
different conditional generator; (10) is not its purity coefficient.

## 6. Reduction limits, physical readouts, and explicit costs

On every physical charge sector the Round15 direct Gaussian embedding J
and the iterated eta->0 then delta->0 dynamics theorem apply with mass mu_n.
J is independent of n. Finite charge support plus norm-two domination of
unitaries extends the convergence to every vector in the full countable
charge space, uniformly on compact time intervals. Uniform-in-charge graph
estimates are not needed and are not claimed. The spectator operator of
Round16 remains in the target; no unwanted tensor channels are deleted.

The [physical observable bridge](../physical-observable-bridge-round19/PROOF.md)
gives fixed finite bounded scalar-Weyl and derivative-TT readout protocols.
Charge shifts intertwine with J exactly because J is charge-independent.
Combining the sectorwise unitary limit, this exact intertwining, the scalar
Gaussian-overlap estimate, and a telescoping finite product proves the same
limit for mixed charge/readout protocols. These are unprojected physical
base observables. Optional homogeneous projectors require their commutant
or corner algebra; general site Weyls cannot be silently projected as a
representation of the original local algebra. Matter observables in the
native gravitational chart may still require nonlocal dressing.
For clock-slice amplitudes, sector-changing readouts carry the exact
D_X O D_X^(-1) half-density weights of the source-domain proof. Base-time
Heisenberg correlations of scalar/TT readouts cancel an independent
spectator factor, whereas raw transition words of nonzero net duration
retain its amplitude. Square-root clock evolution does not factor over
spectators; their separate Round16 approximation is still needed there.

For states of finite expected physical energy E, charge truncation used
only for numerical approximation has an honest tail bound

    ||1_(C>M) Psi||^2 <= E/M,  M>0,

since X>=C. If gamma_G is the least eigenvalue of G, the number of retained
integer labels is at most (2 floor(sqrt(2M/gamma_G))+1)^d, with d=24 for
the Hodge carrier and d=8 for the frame carrier. This is a crude cost bound,
not an efficient solver or a uniform continuum resource estimate.

## 7. What is and is not closed

Closed inside the stated finite-lattice model: a positive self-adjoint
local scalar–charge interaction; exact joint charge/gauge reduction; a
one-E8 full-frame variant; reciprocal response and actual entanglement;
and mixed bounded-readout convergence on the stated observable algebra.

Still open for a full TFPT TOE: microscopic selection of these added fields
and couplings, native-net equivalence, a dynamical conserved electric stress
sector off the selected kernel, propagating charged matter and chirality,
removal or physical explanation of spectator modes, continuum/Lorentz
control, complete nonlinear constraints and empirically fixed parameters.
No T1–T8 gate is promoted. No RH, experimental, Standard Model, or universal
quantum-gravity conclusion follows from the algebraic checker below.

## Validation

[checker.py](checker.py) pins predecessor sources, reruns their charge
checker, and independently tests the Gram form, positive coupling and
mass shift on explicit periodic cells, cubic edge reversal, scalar force,
charge-shift differences, and the noncommuting purity coefficient. These
are exact regression groups, not numerical evidence for operator domains.
The all-volume/domain/readout statements above require their proofs and
the linked independent contracts; finite matrices are not CCR truncations.
