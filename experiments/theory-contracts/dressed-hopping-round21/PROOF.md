# Round21: the complete charge-changing gravity-dressing operator

2026-09-07. NON-RH. This completes the term left at first order in
[Round20](../hopping-source-domain-round20/PROOF.md), for its declared finite
model. It does not derive a new microscopic interaction or a stress tensor.

## 1. One fixed convention and a genuine all-charge unitary

Keep X=X_d+L_J, the complete E8 Gram form and projective hops U_e from
[local transport](../local-charge-transport-round20/PROOF.md). Write kappa
for the dressing parameter, separately from parameters inside X. In the old
commuting gravity-coordinate chart xi=(xi_r,xi_v), put

    S_n(xi)=sum_x [xi_r(x) rho_n(x)-sum_i xi_v,i(x) j_m,i(x)],
    rho_n=rho_m+(lambda/N)e(n_x)phi_x^2,
    W_n(kappa,xi)=exp(-i kappa S_n(xi)),
    W=direct-integral_xi direct-sum_n W_n.

Each component of xi is MEAN ZERO, as in sections 8–9 of the original
[constraint chart](../constraint-dressing/README.md): there are 4(N-1)
independent coordinates, not 4N unrestricted native ones. The spectator
mean pairs added in Round18 are not used to enlarge this old dressing.
Matter and the independent site charges do retain their uniform modes.

This is the sign of U_g in Round20; the S called negative X.J in the old
constraint-dressing note is its negative. No sign convention is changed.
At fixed finite xi,n, S_n is a real Weyl quadratic in N scalar canonical
pairs. Its self-adjoint metaplectic closure exists even when its quadratic
form is indefinite; see [Combescure–Robert, sections 4–5](https://arxiv.org/html/math-ph/0509027v1).
The coefficients depend measurably on xi; finite
dimensional quadratic evolution gives a measurable unitary field. Thus W
is a unitary on the full direct-integral space and is strongly continuous
in kappa by dominated convergence. Its generator has the direct-integral
graph-summable domain. No uniform bound on n, xi or S_n is assumed.

Unbounded polynomial identities below first mean the finite-charge,
compact-xi, scalar-Schwartz core. Fixed-fiber metaplectic maps preserve
Schwartz space; on compact xi and finite n their seminorms are controlled.
For other conjugated operators we use their transported domains, rather
than assuming a fixed expression core is invariant under every evolution.
The old gravity chart is not asserted to be the native local spatial net.

## 2. Explicit sector-resolved transfer, including the cocycle

Let s_e move p from x to y and write its exact old phase as c_e(n), so
U_e|n>=c_e(n)|n+s_e>. Then

    V_e=W U_e W*,
    V_e(|n> tensor psi)
       =c_e(n)|n+s_e> tensor R_e(n) psi,
    R_e(n)=W_(n+s_e) W_n*.                              (1)

Equation (1), not an exponential of a scalar energy difference, is the
full answer at every real kappa. Both factors act on the same scalar
Hilbert space. The continuous dressing can mix scalar positions and
momenta. The countably many charge sectors have NOT been cut off.

For a sequence of hops, intermediate W factors cancel exactly. The whole
continuous factor is W_final W_initial*, while the phase is the product
of the ORIGINAL cocycle phases along the path. In particular the odd-Gram
sign between overlapping hops is retained, inverse hops cancel, and total
integer charge is still conserved. Removing cocycle phases is not allowed.

Every V_e is unitary. Hence

    L_J^W=J sum_e(2-V_e-V_e*)
         =J sum_e(I-V_e)*(I-V_e)=W L_J W*,
    0<=L_J^W<=96JN I.                                   (2)

The constant 48JN is retained. These are operator inequalities on the
whole space. In particular there is no need to sum a generally unbounded
Taylor series to define this bounded operator. Because W commutes with
every n_x, the old bounded charge currents and continuity identities
transport exactly: I_e^W=W I_e W*. Their N-independent individual norm
bound 2J is unchanged. Local support in the OLD observable net is not.

To represent the SAME theory, conjugate the complete parent and its
observables: X^W=W X W*, Dom X^W=W Dom X. This is self-adjoint and has the
same positive lower bound. Replacing only L_J by L_J^W while leaving X_d
fixed defines a DIFFERENT, although still positive self-adjoint bounded-
perturbation model. We do not silently use that alternative. Clock square
roots and exact charge balances follow by functional calculus/conjugation
of the whole model. The gravity-coordinate extension is part of the old
dressing chart, not extra physical modes introduced in this round.

## 3. The additional vertex and all its higher orders

Put Delta_e S(n)=S_(n+s_e)-S_n. The charge-independent j and rho_m cancel:

    Delta_e S=(lambda/N)[
       xi_r(x)(-n_x^T Gp+e(p))phi_x^2
      +xi_r(y)( n_y^T Gp+e(p))phi_y^2].                  (3)

There is no gradient-energy term from D in (3): S was defined with the
scalar source density, not the entire physical energy density. Confusing
these two sources would change the dressing prescription.

On the specified core,

    R_e=I-i kappa Delta_e S
       +kappa^2/2[-(Delta_e S)^2+[Delta_e S,S_n]]+O(kappa^3),
    d L_J^W/d kappa at 0=-i[S,L_J]
       =iJ sum_e [U_e Delta_e S+U_e* Delta_-e S].         (4)

Coefficients in the last expression are to the RIGHT of the shifts.
This agrees with Round20's exact scalar/charge energy-transfer source.
The double commutator form of the second derivative is -[S,[S,L_J]].
The often tempting substitute exp(-i kappa Delta_e S) misses the second
term in (4). Already [phi_x^2,pi_x^2] is nonzero. Higher terms therefore
cannot be obtained by attaching only a charge-dependent scalar phase.
Taylor remainders here are fixed-core strong asymptotics at finite order,
not an operator-norm analytic expansion or a uniform-charge estimate.

## 4. A finite canonical-matrix recipe, with its metaplectic phase retained

Write z=(phi,pi), Omega=[[0,I],[-I,0]] and
S_n=Op_W(z^T K_n z/2), K_n real symmetric. The Hessian of the ACTUAL Ward
polynomial gives K_n directly, including its pi^2 and edge-gradient terms.
For A_n=Omega K_n, equation (1) acts on linear canonical observables as

    R_e* z R_e = M_e z,
    M_e=exp(kappa A_(n+s_e)) exp(-kappa A_n).            (5)

Both are 2N by 2N matrices, not finite Hilbert-space approximations to
canonical commutators. They provide a constructive finite matrix evolution
for each specified n,xi,e. The metaplectic lift is the CONTINUOUS path of
the two factors starting at identity. A final symplectic matrix alone
does not determine the sign of its metaplectic operator; dropping that
sign could change interference between different charge configurations.
The lattice cocycle c_e(n) is an additional independent factor.

Dense storage costs O(N^2) and ordinary fixed-precision dense matrix
operations scale cubically per requested configuration. This is not a
uniform-in-charge error bound or an efficient simulation of a superposition
over infinitely many configurations. No numerical matrix exponential is
used in the exact regression: its first three coefficients are rational
matrices reconstructed from the actual L=3 cubic Ward density.

## 5. What locality and momentum do NOT follow

Delta_e S has endpoint support in this chart, but its conjugates by S_n
need not. The actual cubic K_n has gradient couplings. In (5), a canonical
matrix entry joining a site outside the edge to an endpoint becomes
nonzero at third order for a single charge transfer on the full 3x3x3
scalar lattice. The admissible test profile has xi_r=1 except xi_r=-26
at (2,2,2), and xi_v=0, so every required mean is zero. For lambda/N=2/5
the pi_(0,0,1) row / phi_(0,0,0) column has coefficient 2/15 at kappa^3.
The earlier exploratory uniform profile was inadmissible in the old
chart and is not used as evidence. The checker explicitly guards this.
Thus even edge support, let alone a uniform propagation cone, must not be
inferred for the all-order dressed term. The transported observable net
does keep its original algebraic locality; identifying it with the native
net remains a separate obligation. This finite witness alone is not an
all-distances spreading theorem.

All known energy identities may be conjugated on transported domains.
An absent momentum identity cannot be created by conjugation: a nonzero
commutator becomes W[H,P]W*, still nonzero. In particular this completion
does not evade the companion [additive momentum obstruction](../charge-momentum-round21/PROOF.md).
Nor is S a derivation of a new nonlinear, conserved total stress tensor.
The analytic source lift of Round20 remains a declared construction; no
new native first-vertex matching or unbounded-current Gaussian limit is
claimed here. T1–T8, microscopic selection, chirality and continuum remain
open. NO RH CLAIM.
