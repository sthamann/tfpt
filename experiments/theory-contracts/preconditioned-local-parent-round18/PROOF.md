# Round18: finite-range full completion in an explicitly preconditioned gauge chart

2026-09-06. NON-RH finite-lattice construction. This supplies a local SOURCE
chart for the companion cellwise stabilizer and the existing positive local
base. The resulting full Hamiltonian expression has bounded spatial range
in its DECLARED independent fields, a specified self-adjoint realization,
strong constraint covariance and positive physical reduction. Its relation
to the original native gravitational observable net is nonlocal. It changes
higher-order completion data and is not a microscopic TFPT/TOE derivation.

## 1. Exact native operators and the source that must be localized

Fix a periodic cubic lattice of n=L^3 sites, L>=2 and spacing a>0. Let
T_i be periodic shifts and set

    D_i^+=(T_i-I)/a,  D_i^-=(I-T_i*)/a,
    ell=-sum_i D_i^-D_i^+,
    d=(D_1^+,D_2^+,D_3^+)^T,  b=(D_1^-,D_2^-,D_3^-),
    d*=-b,                d*d=ell.                         (1)

The star is the actual real-lattice adjoint. In orthonormal tensor order
(11,22,33,23,13,12), the original scalar constraint row A and vector row V
are the finite stencils in
[the actual chart](../constraint-dressing/README.md), Section 8:

    A_ii=D_i^-D_i^+ + ell,
    A_ij=sqrt(2) D_i^-D_j^- for i<j,
    V_(i,ii)=D_i^+,
    V_(i,ij)=D_j^-/sqrt(2),  V_(j,ij)=D_i^-/sqrt(2).         (2)

Let t=(1,1,1,0,0,0)^T tensor I_n and K_p=I-t t*/2. Commuting periodic
shifts and the adjoints in (1) give the exact all-site identities

    A A*=2ell^2,       A t=2ell,       A V*=0,
    G_v=V V*=(ell I_3+d d*)/2,
    V t=d,            V K_p V*=ell I_3/2.                  (3)

All occurrences of ell in vector/tensor formulas act componentwise. On
mean-zero modes ell is positive and invertible; d d* squares to ell d d*.
Hence

    G_v^(-1)=2ell^(-1)I_3-ell^(-2)d d*,
    B_H=-1/(2ell),
    B_v=G_v^(-1)V K_p V*G_v^(-1)
       =2ell^(-1)I_3-(3/2)ell^(-2)d d*.                    (4)

These are real-space formulas, including staggered phases and boundary modes.
For the normalized (pi,pi,0) real block they reproduce b=(2,2,0), B_H=-1/16
and B_v=[[5,-3,0],[-3,5,0],[0,0,8]]/32.

The literal scalar Ward sources are rho, the three link currents j and the
orthonormal stress vector tau=(tau_11,tau_22,tau_33,sqrt(2)tau_23,
sqrt(2)tau_13,sqrt(2)tau_12). Set J_v=-j. The actual invariant first vertex
from [the original source decomposition](../covariant-domain-round13/README.md)
contains

    c.Q=r.Bcal-v.B_v J_v,
    Bcal=(2ell^2)^(-1) A tau+(2ell)^(-1)rho.                (5)

Every inverse and source projection in (4)--(5) is on the original mean-zero
constraint labels. The scalar matter itself retains its homogeneous mode.

## 2. A native-locality obstruction and a constructive preconditioning

The actual kinetic pieces are tau_ii=pi_x^2/2 plus configuration terms,
rho=pi_x^2/2 plus configuration terms, and j has one pi and one scalar
difference. Therefore

    (Bcal)_kinetic=(3/4)ell^(-1)pi^2.                       (6)

This is not a local source in the old c chart. Replacing r by its native
value A q does not generally remove the inverse. In the coefficient of
q_11 pi^2, at phi=0 and native gravitational p=0, the multiplier is

    (3/4)(1-|d_1(k)|^2/ell(k)).                            (7)

It approaches zero along the first momentum axis and 3/4 along the second.
A uniformly finite-range translation-invariant stencil has a continuous
Laurent-polynomial symbol and cannot equal (7) on every punctured
neighborhood of zero. This excludes a finite-range REWRITING of the old
undressed source term, not every other completion. The complete first
gravity-dressed vertex can still be local because its separate dressing
commutator cancels that inverse contribution.

There is, however, a useful invertible change on mean-zero constraint labels.
Use P=ell^2 componentwise and define

    c=P c_tilde,              X_tilde=P X.                 (8)

The original canonical bracket {X,c}=I gives {X_tilde,c_tilde}=I. The
physical variables and their norm are unchanged. Since P commutes with b,
the exact free constraint flow remains

    r_tilde'=b v_tilde,        v_tilde'=0.                 (9)

The LINEAR source becomes finite range:

    c.Q=c_tilde.Q_tilde,
    Q_tilde,H=(A tau+ell rho)/2,
    F_v=2ell I_3-(3/2)d d*,
    Q_tilde,v=-F_v J_v=F_v j.                             (10)

These are polynomial spatial stencils acting on the original Ward sources,
not adjustable new matter densities. Their sums over sites vanish identically.
The ordinary scalar products in (10) use the same real lattice measure.

The free scalar constraint potential also becomes a polynomial stencil:

    k_tilde(c_tilde)
      =-(1/4)<r_tilde,ell^3 r_tilde>
        +(1/2)<v_tilde,ell^2 F_v v_tilde>.                (11)

Indeed P B_H P=-ell^3/2 and P B_v P=ell^2 F_v. The transport term is still
-i(b v_tilde).partial_(r_tilde). No inverse spatial operator remains in
(9)--(11). The negative scalar term is retained; the full constraint-sector
generator is not being called a positive physical Hamiltonian.

The price is precise. Although X_tilde is a finite derivative of original
native gravity, c_tilde=ell^(-2)c is not. The map (8) is nonlocal relative
to that original observable net and becomes ill-conditioned in long
wavelength/continuum limits. It is not a local canonical identification
between the two native field theories.

Precisely, ||P^(-1)||=ell_min^(-2) and
cond(P)=(ell_max/ell_min)^2. At fixed spacing and growing periodic side L,
this condition number grows as order L^4. Preconditioning is therefore not
a uniformly bounded equivalence of continuum or growing-box observable
norms. The support radii below refer only to the newly declared fields.

## 3. Canonical and physical normalization of the change of chart

On the mean-zero space of dimension 4(n-1), P is a fixed positive matrix.
The exact kinematic unitary for (8) is

    (T f)(c_tilde)=(det P)^(1/2) f(P c_tilde).             (12)

It transports all operator domains and preserves the canonical Weyl
representation. The determinant is that of P on all four mean-zero
constraint fields, not a determinant on the scalar mean or physical matter.

There is a finite normalization factor in the gauge average. If old and
new constraint-parameter Haar measures are both independently chosen as
du/(2pi)^d, then evaluation at zero gives

    q_new(Tf,Tg)=det P q_old(f,g).                         (13)

Transporting the OLD Haar measure through u_tilde=P u instead inserts
(det P)^(-1) and preserves q_old exactly. Equivalently one can normalize
the resulting physical vectors by this positive constant. It is independent
of states and fields but depends on the fixed regulator. No determinant
is hidden or claimed to be a microscopic measure prescription.

The OLD global stabilizer does not become local under (8). Its transformed
expression still contains both P and P^(-1):

    g^2|P c_tilde|^2 sum_a ||(P^(-1)Q_tilde)_a psi||^2.    (14)

The next section replaces (14) by a different higher-order term. This
replacement, rather than an algebraic cancellation of (14), is essential.

## 4. Independent site fields and the optional mean-gauge extension

Keeping mean-zero c_tilde is sufficient for the exact chart identification,
but those constrained coordinates have equal-time bracket I-P_mean, not
independent canonical variables at every site. For an ordinary site tensor
product we instead DECLARE independent pairs (X_tilde,c_tilde) at all n sites,
four pairs per site, with the standard canonical bracket delta_xy.

Equations (9)--(11) are now their local Hamiltonian data. This adds four
mean pairs relative to the old chart. Their c_tilde means are additional
first-class constraints, imposed together with all nonzero c_tilde modes.
They are not the deleted homogeneous gravitational tensor modes, the trace
clock, or a receiver for total matter energy.

The linear sources in (10) have zero means, and k_tilde and b kill constants.
The nonlinear stabilizer below can nevertheless depend on the c_tilde means.
The added pairs are therefore NOT said to decouple dynamically off shell.
What is exact is that the Hamiltonian is independent of X_tilde means:
their coefficients are the mean of b v_tilde, which vanishes. Their
c_tilde means are conserved and generate translations of X_tilde means.
They are legitimate additional pure-gauge pairs in this declared model.

On the physical surface c_tilde=0 every added term below vanishes and the
same positive base and physical Hilbert space remain. The full normalized
gauge average simply adds four evaluation factors; it introduces no extra
physical mean Hilbert space. On the old mean-zero sector the chart comparison
uses the normalization in (13). The independent-site extension is an
additional model choice, not an invertible map on the original phase space.

## 5. The finite-range full source-stabilized parent

Use the actual Round15 base

    B_delta,eta=H_delta,eta-E_fast(delta,eta) >= e_m >0,

on its 35n physical canonical pairs: one scalar, six tensor and 28 fast
oscillator pairs per site. Every retained mode is present. Its nonnegative
form, unique self-adjoint domain and explicit divergent energy subtraction
are those of [the local parent](../local-parent-round15/PROOF.md) and
[its clock bound](../spectator-clock-round16/PROOF.md). Write B for brevity.

For each site i define, with d_i=(b v_tilde)_i,

    rho_i(c_tilde)=r_tilde,i^2+|v_tilde,i|^2+d_i^2,
    S_i[psi]=sum_(alpha=H,v1,v2,v3)||Q_tilde,i,alpha psi||^2.

Declare the fiber form

    h_loc(c_tilde)[psi]=q_B[psi]
      +g sum_i <psi,(r_tilde,i Q_tilde,i,H
                              +v_tilde,i.Q_tilde,i,v)psi>
      +g^2 sum_i rho_i(c_tilde) S_i[psi].                 (15)

The full generator has the specified expression

    H_loc=-i(b v_tilde).partial_(r_tilde)+k_tilde+B
             +g sum_i c_tilde,i.Q_tilde,i
             +g^2 sum_i rho_i sum_alpha Q_tilde,i,alpha^2. (16)

Each Q_tilde is a real Weyl quadratic in scalar fields. Its operator square
retains ordering terms and need not commute with the other sources. The
closure of (16) is defined by the following forms and group, not by an
unsupported claim that its fourth-order minimal expression has a unique
extension.

All spatial couplings in (16) have uniformly bounded range in the declared
independent fields. The Ward density, current and stress have finite support;
A,ell,F_v are finite stencils; b uses neighboring vector fields. A conservative
bound for each Q_tilde support is graph radius four lattice steps from its
site center (not its support diameter), and for k_tilde's bilinear kernel is
four steps. Squaring a source
does not introduce new field sites. A summand in (15) is supported inside
the union of its fixed matter neighborhood and the nearest-neighbor
constraint neighborhood. The range bounds do not grow with n.

The energy subtraction is a scalar identity and does not affect this support
statement. The kinetic and potential matrices may have arbitrarily large
coefficients as delta,eta or spacing vary; bounded range is not a uniform
Lieb--Robinson estimate, relativistic microcausality or finite numerical cost.

## 6. Domains, complete dynamics and positive reduction

The companion [cellwise theorem](../local-source-stability-round18/PROOF.md)
applies to (15) with N=n and the ACTUAL finite stencils (9)--(10).
Its hypotheses were checked explicitly above: positive base with constant
kinetic matrix, Weyl-quadratic sources, invariant complete affine shear,
and the chosen fixed cell metric. Let I(c_tilde)={i:rho_i>0}. Since

    r_tilde,i(t)=r_tilde,i+t d_i,
    |rho_i'(t)|<=rho_i(t),

the active set is invariant. The domain is precisely Dom(B^(1/2)) intersect
the Q_tilde graph domains at ACTIVE sites only. Inactive sources impose no
graph condition. The closed form and its representing self-adjoint operator
satisfy

    h_loc >= B-n/4,
    e=h_loc+n||psi||^2,
    q_B+(g^2/2)sum_i rho_i S_i+(n/2)||psi||^2 <= e,
    |partial_t e|<=3e.                                   (17)

Thus every characteristic has an all-time unitary form propagator with
e_t<=exp(3|t-s|)e_s. The subset form-core and weak-uniqueness proof in the
companion theorem also gives strong parameter continuity across inactive
strata, in particular V_c(t,0)->exp(-itB) as c->0 uniformly on compact time
intervals. No false uniform graph norm at a vanishing coefficient is used.

The determinant-one characteristic shear and the real phase from k_tilde
then define the full strongly continuous unitary group. Its Stone generator
is the specified self-adjoint H_loc in (16). Its complete operator domain
is the strong difference-quotient domain of that group. For every bounded
Borel F of all 4n independent constraints,

    U_loc(t)* F(c_tilde) U_loc(t)=F(exp(t A_c)c_tilde).      (18)

This is stronger than a formal commutator. In particular all added mean
constraint spectral measures are conserved.

Normalized Gaussian-regulated averaging of all c_tilde constraints on
continuous compact sections gives

    q_phys(F,G)=<F(0),G(0)>_(H_B),
    H_phys=H_B,       [U_loc(t)F](0)=exp(-itB)F(0).        (19)

This is positive, nonzero and onto the original base Hilbert space. It is
not an ordinary kinematic L2 zero kernel. It proves that adding the four
declared mean gauge pairs has not added physical states after the stated
reduction. Full H_loc is not semibounded; positivity belongs to B and the
physical norm, not the unreduced constraint generator.

## 7. Clock, adiabatic limit and exact first-vertex scope

The complete clock construction also survives. The actual b has rank n-1>0,
so bv!=0 is a full-measure regular set even with the four added mean pairs.
The Round16 measurable characteristic section gives

    H_loc=S_loc(K_tilde+B)S_loc*,
    C_loc=H_loc-P_0^2/12                                  (20)

with the full joint spectral domain. The proper negative-sheet tube uses
S_loc B S_loc*-P_0^2/12 in (-e_m/2,e_m/2), not the raw B-clock band or a
positive square root of H_loc. The exact spectral half-density chart turns
C_loc into K_tilde+lambda. All the positive joint averaging and physical
clock-norm statements therefore follow by the same unitary transport as in
[the vertex/clock proof](../clock-vertex-round16/PROOF.md). If homogeneous
relational constraints or the old auxiliary gauge-unfixing are retained,
use the same ordered common transports and displaced seed prescription as
[Round17](../full-constraint-parent-round17/PROOF.md). These additional
choices do not turn the mean gauge pairs into homogeneous gravity.

The local-source theorem and Round17 Gaussian derivative bounds apply to
every Q_tilde and its ordered square, because (10) is a fixed finite real
linear combination of the same quadratic scalar data. Hence the ORIGINAL
Gaussian embedding has full uncompressed characteristic and full-group
convergence as eta->0 at fixed delta, then delta->0 at fixed lattice.
The target still contains the positive scalar/TT base plus 4n+2 real free
tensor spectators. Their clock energy is handled by the existing normalized
spectator approximation; it is not silently erased.

The source term c_tilde.Q_tilde equals the original c.Q exactly on the
mean-zero chart. The new stabilizer starts at g^2 and is second order in
all c_tilde. Thus, after the sequential base limit and the SAME original
nonlocal gravity dressing, the complete original first dressed vertex is
retained. At finite parameters the local base has its different auxiliary
first vertex, exactly as in Round17. Equation (20) and the norm construction
are all-order statements for the NEW completion, not for the old global
stabilizer or original native microscopic Hamiltonian.

## 8. What locality has and has not been obtained

This is a finite-range full Hamiltonian expression with a controlled quantum
realization in its declared site-factorized variables, using 39n canonical
pairs before the trace clock and any separate old gauge auxiliaries. Four
of these pairs are the new mean gauge extension; reducing all 4n constraints
returns the 35n-pair positive base. The source metric/preconditioning and
cell stabilizer are declared choices. No added physical spatial derivatives
are hidden in an inverse in (16); the inverses instead reside in its map
back to the original native gravitational field net.

Pulling (16), its local observables or its clock charts back through that map
does not preserve bounded spatial support. Therefore this result does NOT
establish a local realization of the original native observable algebra,
a preferred metric/dimension, the full nonlinear diffeomorphism algebra,
chiral/flavor/measure data, or a regulator-independent relativistic limit.
It is separate from the U(1)^8 rotor charge parent. Their direct juxtaposition
is not one interacting 3+1D TOE.

## Reproduction

The companion checker reconstructs the native all-site matrices and imports
the literal Ward sources. It tests (3)--(11), actual local source supports,
the uncancelled native kinetic projector, canonical/Haar factors, the mean
constraint distinction and a nonzero difference from the old stabilizer.
Finite checks support the displayed all-volume stencil algebra; the domain,
continuity and dynamics claims use the companion analytic theorem, not a
finite canonical-commutator approximation or numerical time evolution.
