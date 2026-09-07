# Round17: a constraint-compatible dynamical parent family and its actual-source limit

2026-09-06. NON-RH, unpromoted research. This connects the specified Round15
local positive dynamical family to the full source-stabilized constraint
construction, including the quadratic clock and a compatible homogeneous
relational prescription. The positive base Hamiltonian is local. The FULL
constraint completion below is not asserted spatially local: its existing
source-square prescription is global. No microscopic TFPT selection or
complete T1--T8/TOE conclusion is made.

## 1. The three physical Hamiltonians and the sources that are retained

Fix a connected periodic cubic lattice, n>1, spacing fixed, m>=0 and g in R.
Keep all scalar coordinates, six tensor coordinates per site and every fast
oscillator of [the local parent](../local-parent-round15/PROOF.md). Write

    B=B_delta,eta=H_delta,eta-E_fast(delta,eta) on H_B,
    A_delta=-Delta_x/2+V_m+<ell q+g sigma,R_delta(ell q+g sigma)>/2,
    A_0=A_+ tensor I+I tensor S_extra on H_D,
    S_extra=-Delta_extra/2,        d_extra=4n+2.

Here x=(phi,q), H_D=L2(R^(7n)), H_B=L2(R^(35n)), and delta,eta>0.
The normalized displaced Gaussian J=J_delta,eta:H_D->H_B obeys J*J=I.
The original local-parent proof gives uncompressed strong unitary convergence
B J ~ J A_delta as eta->0, then A_delta->A_0 as delta->0.
The [clock/spectator proof](../spectator-clock-round16/PROOF.md) strengthens
the common lower bound to B,A_delta,A_0>=gamma=e_m>0 at this fixed lattice.
The explicit divergent fast-energy subtraction is not optional in this claim.

On each space use the SAME scalar real Weyl-quadratic sources

    Q=(Bcal,-B_v J_v),

of [the original-vertex construction](../vertex-preserving-round15/PROOF.md),
tensored with identities on the other coordinates. The sources are not
replaced by their compressed matrix elements, classical squares or commuting
surrogates. All their operator-square ordering constants are retained.

For X=B,A_delta,A_0 define the closed form, at g!=0,c!=0,

    h_X(c)[psi]=q_X[psi]+g sum_a c_a <psi,Q_a psi>
                          +g^2 |c|^2 sum_a ||Q_a psi||^2,
    D_X=Dom(X^(1/2)) intersection all Dom(Q_a).               (1)

At c=0 or g=0 use X on its original domain. Equation (1) is a declared
higher-order constraint completion, not a claim that the bare local parent
already possesses these gauge constraints.

## 2. Complete full generators at every finite parameter

Put c=(r,v), A_c=[[0,b],[0,0]], K_c=-i(bv).partial_r+k(c), with the actual
nonzero-mode divergence b. For w=|g||c| the same Cauchy estimate gives

    q_X+(w^2/2)sum||Q_a psi||^2+||psi||^2/2
      <= h_X(c)[psi]+||psi||^2
      <= q_X+(3w^2/2)sum||Q_a psi||^2+3||psi||^2/2.           (2)

The sum graph/form space is complete and dense. It contains compact smooth
tests. Thus (1) defines a specified self-adjoint representing operator even
though the Q_a do not commute. Along c(t)=exp(t A_c)c0!=0 the domain is
constant and the coefficients are smooth. The common-form evolution theorem
used in Round15 applies to h_X+1, with all hypotheses given by (2), and

    e_t[V_X,c0(t,s)psi] <= exp(5||A_c|| |t-s|) e_s[psi].     (3)

At each fixed parameter, the zero-fiber continuity argument also applies:
V_X,c(t,0)->exp(-itX) strongly as c->0, uniformly on compact time sets.
The shifted nonnegative polynomial Schroedinger operator X has the needed
compact smooth operator core. No global Schwartz invariance is assumed.

The characteristic group

    [U_X(t)F](c)=exp(-i I_t(c))
          V_X,exp(-t A_c)c(t,0) F(exp(-t A_c)c)

therefore defines a self-adjoint H_X on L2(dc;H_Xphysical), with local
expression K_c+X+g c.Q+g^2|c|^2 sum Q_a^2 on the specified expression tests.
The spectral covariance U_X(t)* a(c) U_X(t)=a(exp(t A_c)c) is exact for
every bounded Borel a. H_X is not a positive Hamiltonian; positivity belongs
to the reduced base X. This is the same distinction as in Round15.

The common-form input is
[Balmaseda--Lonigro--Perez-Pardo, Assumption 3.8 and Theorem 3.10](https://arxiv.org/html/2112.11063v2).
No interacting fourth-order operator-core theorem is substituted for the
closed-form definition in (1).

## 3. Actual-source dynamics, not only static elimination

The companion [adiabatic-source theorem](../adiabatic-source-round17/PROOF.md)
controls the derivatives of the SAME Gaussian J through order four and
proves on every compact smooth slow test z

    ||(Q_a J-JQ_a)z||=O_(delta,z)(eta^(1/4)),
    ||(Q_a^2 J-JQ_a^2)z||=O_(delta,z)(eta^(1/4)).            (4)

Together with the local-parent B residual this controls the full h(c)
expression. A residual on tests alone is not asserted to prove propagation.
The companion proof supplies the additional form-core density and weak-energy
uniqueness argument: h_B+1 bounds B and every source graph norm; weak limits
of J*V_B J lie in the target common form domain and obey its variational
Schroedinger equation. Norm conservation then proves full, uncompressed
propagator convergence. It also treats the subsequent delta limit, without
assuming global form domains stay identical across that limit.

Consequently, for every fixed characteristic c0 and finite T,

    sup_(|t|<=T) ||V_B,c0(t,0)J z-J V_A_delta,c0(t,0)z|| ->0,
    sup_(|t|<=T) ||V_A_delta,c0(t,0)z-V_A0,c0(t,0)z|| ->0.   (5)

The first limit is eta->0 at fixed delta; the second is delta->0 at fixed
lattice. Both extend to every physical Hilbert vector by density and
unitarity. At c0=0 they are the earlier positive-base limits. No uniform
estimate over c0, volume, all states or an arbitrary joint parameter path
is inferred.

Let J_c=I_c tensor J. Integration over c and the determinant-one shear
then upgrade (5) to the full original characteristic groups:

    sup_(|t|<=T) ||U_B(t)J_c F-J_c U_A_delta(t)F|| ->0,       (6)

and similarly for delta. Pointwise characteristic convergence and the
bound 2||F(c)|| give domination after the common change of variables along
the shear; finite tensor approximations provide uniformity in t. Thus this
limit uses the actual Gaussian encoding, not an unknown effective operator.
For A_0 the source acts only on scalar coordinates, so exactly

    H_A0=H_vp tensor I+I tensor S_extra.                    (7)

The extra free modes have not been erased or called gauge.

## 4. Two different useful encodings must not be confused

The [Round16 measurable section](../clock-vertex-round16/PROOF.md) applies
separately to each X:

    tau(c)=r.bv/|bv|^2, c_perp=(r-tau bv,v),
    S_X(c)=V_X,c_perp(tau(c),0) exp(+i tau(c)X),
    H_X=S_X(K_c+X)S_X* .                                  (8)

These are equalities of full groups and domains. The exceptional bv=0
subspace is null. Fixed-shape radial averaging gives S_X(delta_c c)->I
strongly for almost every direction as delta_c->0. This regulator scale
delta_c is distinct from the parent stiffness delta.

For X=B and Y=A_delta define

    E_dyn=S_B (I_c tensor J) S_Y*.                         (9)

It is an exact isometry and exactly intertwines all bounded c functions.
Its H-group error reduces identically to the known base B/J/Y error by
unitary cancellation; it is generally NOT an exact dynamical intertwiner
at finite eta. Independently, (5) and the base group convergence imply
S_B J-J S_Y->0 strongly for almost every c, because tau(c) is fixed and
finite on each regular orbit. Dominated convergence extends this to L2(dc).
The adjoint-direction identity follows from unitarity. Thus E_dyn-J_c->0
strongly, consistent with (6). There is no uniform orbit-time bound near
the exceptional set.

Now add the unchanged quadratic clock C_X=H_X-P_0^2/12. Its full self-adjoint
domain is the joint spectral multiplier domain, not an assumed domain
intersection. Take the common interval I=(-gamma/2,gamma/2), negative P_0,
and the PROPER transported tube with S_X X S_X*-P_0^2/12 in I.
Let Z_X be the exact spectral coordinate change

    lambda=E-p^2/12, p_-=-sqrt(12(E-lambda)),
    (Z_X f)(lambda,E)=sqrt(6/sqrt(12(E-lambda))) f(E,p_-),
    W_X=S_X Z_X*,       W_X* C_X W_X=K_c+lambda.            (10)

The clock-compatible embedding is instead

    E_clock=W_B (I_(c,lambda) tensor J) W_Y*.              (11)

This is an exact isometry BETWEEN THE CLOCK TUBES and intertwines the
full c/time constraint group EXACTLY at every finite parameter. This follows
because J acts only on physical initial-data labels and both reference
generators are K_c+lambda. Equation (9) tensored with the old clock identity
need not even map these two tubes into each other: BJ!=JY in general.
Equation (11) adjusts clock momentum through the respective spectral charts.

Exact C-gauge intertwining is not exact physical clock-time dynamics. The
slice readout is D_X exp(-iq sqrt(12X)), D_X=3^(1/4)X^(-1/4). The
clock-slice isometry D_B J D_Y^(-1) preserves its weighted norm exactly;
its actual q-dependent dynamics converge only in the limits proved in
Round16. All half-density weights and that distinction are retained.

## 5. A compatible homogeneous constraint prescription with a true free limit

The bare centered spatial flow on all coordinates does NOT generally
intertwine J at nonzero g: f_delta(x) is quadratic, while the centered
difference is not a derivation on products. For the actual unit-spacing
L=3 massless Ward source, phi_(0,0,0)=phi_(1,0,0)=1 and all other scalar
coordinates zero give

    [d sigma_11(phi)[D_1^c phi]-D_1^c sigma_11(phi)]_(0,0,0)=-5/4.

The finite-delta h displacement is an invertible constant-coefficient map
of sigma, so this defect cannot be removed by its screened linear map.
Define the global triangular displacement unitary instead,

    [F_delta Psi](x,a)=Psi(x,a-f_delta(x)),
    J z=F_delta(z tensor chi_eta).

The Jacobian is one, so F_delta is unitary on the full L2 space. Let G be
the compact closure of the JOINT centered orthogonal flows on slow and
fast coordinates. Denote its representations R_D(alpha),R_fast(alpha).
All constant-coefficient spatial operators D,N,ell commute with those
centered translations; hence K_delta and its square root commute with
R_fast. The Gaussian chi_eta is exactly invariant. Therefore

    R_B(alpha)=F_delta[R_D(alpha) tensor R_fast(alpha)]F_delta*,
    R_B(alpha)J=J R_D(alpha),       Pi_B J=J Pi_D.            (12)

The last identity follows by normalized Haar integration over this common
compact closure. Independent closure factors are not presumed to form a
product. Their generators are simultaneously self-adjoint transported
orthogonal-flow generators, with transported domains.

At g=0, f_delta is linear in q and equivariant under the native centered
flow. Then F_delta commutes with that joint flow and R_B is exactly the
native free parent representation. At nonzero g, (12) is a new DISPLACED
seed choice. It is neither derived from TFPT nor identified with the
original local momentum currents. It need not commute with B. Its spectral
relational version W_B R_B W_B* DOES commute with C_B and c on the tube,
just as W_Y R_D W_Y* does on the target tube.

With these choices (11) also exactly intertwines all homogeneous relational
constraints, their compact projectors and the positive joint rigging norm.
In reference coordinates the latter is

    <F(0,0),Pi_D G(0,0)> -> <JF(0,0),Pi_B JG(0,0)>,

and these are equal by (12). This embeds the target physical Hilbert space
isometrically, but does not assert it is the whole parent physical space.
The parent has additional physical states.

If the old auxiliary gauge-unfixing is also retained, append its separate
primary coordinate xi and use W_X=U_g,X V_aux,X S_X Z_X* on each side of
(11). Tensor J with the xi identity before transport. The same exact group
and norm argument applies on the common reference list c,xi,lambda,G.
These old gauge auxiliaries are DISTINCT from the 28n physical fast
oscillators. No discarded second-class partner is imposed as an annihilator.

The delta limit uses the same R_D throughout. For the extra modes of A_0,
an isotropic Gaussian in momentum is invariant under their centered
orthogonal flow. Thus I_sigma R_+=R_D I_sigma and Pi_D I_sigma=I_sigma Pi_+
hold without asserting Pi_D=Pi_+ tensor Pi_extra. The normalized spectator
approximation and its energy/delocalization costs from Round16 consequently
remain compatible with the homogeneous projection too.

## 6. First vertex, locality and the exact remaining price

The term g c.Q is exactly the actual original constraint-source first vertex
at every parameter. The positive base parent, however, has finite-parameter
first vertex -g<DE-Nu-h,sigma>/delta, not the old TT vertex. After its fast
limit the linear term is g<ell q,R_delta sigma>; only after delta->0 is it
g<q_TT,sigma>. Together with g c.Q and the same gravity dressing this
recovers the original full first vertex at the target. It would be false
to claim that the enlarged finite parent has that full vertex before its
reduction. Higher-order terms remain the declared completion, not a
uniquely selected all-order TFPT interaction.

The base B has the finite spatial range and 35n pairs of Round15. Adding
the nonzero gravitational c pairs gives 35n+4(n-1) canonical pairs, before
the clock and any separately retained gauge auxiliaries. But
g^2|c|^2 sum Q_a^2 couples global constraint/source indices, and the original
Q_a themselves contain the inverse spatial coefficient matrices of the
Darboux chart. Neither this full term nor the S_X, F_delta or clock charts
have a demonstrated fixed spatial range. In particular even if Q_a were
local, the product (sum c_a^2)(sum Q_b^2) includes arbitrarily distant
cross terms. A local positive BASE plus this completion is not thereby
a local full constrained parent.

The result is a genuine dynamic and joint-constraint connection with exact
norms, actual sources, free-seed recovery and sequential convergence. It
does not solve a spatially local version of the full constraint-square
interaction, microscopic selection of the displaced momenta/clock/energy
reference, or derivation of the charged sector from this same Hamiltonian.
No relativistic microcausality, continuum limit, bounded-cost many-body
algorithm, four-dimensional chirality/flavor/measure or full TOE follows.

## Reproduction

The companion checker separates actual-source/finite-lattice controls from
explicit finite spectral models of the encoding distinctions. Its negative
controls include non-equivariant bare centered source transport, incorrect
clock-momentum retention, changing a conditional projector and falsely
assigning locality to the global stabilizer. The all-Hilbert-space results
rest on this proof and the separately reviewed source-evolution theorem,
not finite canonical-commutator matrices or a numerical fit.
