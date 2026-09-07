# Round19: orientation selection and a fully framed single-copy charge parent

2026-09-07. NON-RH. Finite periodic cubic lattice, side L>=2, N=L^3.
This constructs one full E8-metric charge copy with a positive physical norm
and local selection penalties, at an explicit price: additional complete
finite frames, finite gauge links and a new gauge-covariant site-field net.
It first separates the native three-branch construction from that new model.
Neither is a derivation of microscopic TFPT matter, chirality or a continuum.

## 1. Frozen charge data and what must actually be selected

Keep the full basis B and Gram matrix G=B^T B from
[Round18](../charge-hodge-round18/PROOF.md), not merely its spinor direction.
In integer coordinates, e(n)=n^T G n/2 is a nonnegative integer, positive
for n!=0; the source spinor is n_s=e8 and e(n_s)=1. The frozen cocycle is

    beta(n,m)=sum_a n_a m_a G_aa/2+sum_(a>b)n_a m_b G_ab mod 2,
    epsilon(n,m)=(-1)^beta(n,m),
    T_n|m>=epsilon(n,m)|m+n>.                          (1)

Round18's electric Gauss and curl kernel is exactly three constant oriented
fluxes (n1,n2,n3), each in Z^8. Its exact physical Hilbert space is l2(Z^24),
and its normalized electric energy is sum_i e(ni). Cubic rotations act by
signed permutations on these three directions and trivially internally.
An invariant additive rank-eight sublattice is impossible for that action,
but this does not exclude extra nonlinear orientation/frame fields.

## 2. A native local selector gives three honest copies, not one

Add a three-state UNORIENTED axis variable a_x in {1,2,3} at every vertex
of the original edge-rotor lattice. Let P_H be the Round18 divergence/curl
penalty at scale Delta. With lambda,mu,kappa>0 use

    P_F=lambda sum_(positive edges xy)(1-delta_(a_x,a_y)),
    P_A=mu sum_(edge x->x+ei)
                    [2-delta_(a_x,i)-delta_(a_(x+ei),i)] e(E_i(x)),
    u_i(x)=e(E_i(x))+e(E_i(x-ei)),
    P_Q=kappa sum_x sum_(i<j) u_i(x)u_j(x).            (2)

These are local, positive, mutually commuting multiplication operators.
Using both endpoints in P_A and both incoming/outgoing energies in P_Q is
important: the unsymmetrized outgoing-site quartic is cubic invariant only
on harmonic configurations, not generally on native link fields. Equations
(2) are invariant on the FULL native lattice under proper cubic rotations.
The orientation field transforms as an unoriented axis and link reversal
changes E's sign and endpoint as usual. Energy e is even. Round18's Hodge
penalty is also cubic invariant as the cochain Laplacian norm.

The zero set of P_H+P_F+P_A+P_Q is exactly

    a_x=a for all x,
    E_i(x)=delta_(i,a) n,   n in Z^8.                 (3)

Proof: P_H forces constant integer n_i; connected ferromagnetic constraints
force a constant a; P_A kills both inactive n_i. Conversely (3) annihilates
every term, including P_Q. Thus P_Q is a compatible nonlinear selector,
but becomes redundant after the more informative axis alignment constraints.
Without a_x and P_A, the quartic alone gives three charge branches sharing
one zero-flux state; with a_x there are THREE distinct zero-flux states.

The physical basis is |a,n>, so the kernel is C^3 tensor l2(E8), not l2(E8).
Its inherited norm is sum_(a,n)|psi(a,n)|^2 and its energy is exactly e(n)
per branch. The local penalty has a nonzero lower gap at least
min(2Delta,lambda,mu,kappa), since a violated term has integer value at least
one, and the Hodge bound is 2Delta. No sharp gap is claimed. The full
finite-volume Hamiltonian has three zero-energy vacua; no automatic branch
selection or spontaneous symmetry-breaking theorem is inferred.

Each branch has the complete (1), by the Round18 all-parallel-link Wilson
operator. A change of n requires every link of its active orientation. An
operator between distinct uniform orientation branches must in addition
touch every orientation variable. The exact code therefore does not acquire
local charged fields or a local branch-changing observable.

## 3. Why merely quotienting the three axes is not sufficient

Let G_c be the 24 proper signed permutation matrices in three dimensions.
Writing R e_a=sigma_R(a)e_(pi_R(a)), its native harmonic action is

    U_R|a,n>=|pi_R(a),sigma_R(a)n>.                    (4)

The spinor and its negative are distinct charge states. On each branch,
T_n becomes T_(sigma n) under a sign reversal; beta(-n,-m)=beta(n,m), so
there is no missing cocycle correction that would remove this change.

An unsigned axis identification would encode |n> as
3^(-1/2)sum_a|a,n>. The proper pi rotation diag(1,-1,-1) takes it out of
that subspace for n!=0. Hence that simple three-axis quotient does not even
retain the original cubic action. If instead all proper cubic rotations
are gauged on (4), then n and -n lie on the same orbit. In the trivial
connection sector its basis is one vacuum and one state per nonzero pair
{n,-n}, not the faithful regular E8 charge representation. A bare T_n does
not descend; invariant combinations such as T_n+T_-n are not unitary charge
translations and do not supply the frozen fourth-power/winding law.

### What ordinary flat finite-gauge connections add

There is a precise local gauge-bundle version of this failed shortcut.
At sites take three-component integer vectors F_x and unoriented axes a_x;
introduce G_c-valued oriented links U_xy, U_yx=U_xy^-1. Impose alignment,
covariant constancy (a_x,F_x)=U_xy(a_y,F_y), and identity plaquette holonomy.
Gauge transformations act on sites by g_x and on links by
U_xy -> g_x U_xy g_y^-1. These are local constraints, but they replace the
native electric cochain constraints; F is now an internal site-vector field.

On the periodic cube, flat connections modulo based gauge are commuting
triples (h1,h2,h3). To see completeness, transport along lattice paths:
plaquette flatness makes contractible path changes immaterial; winding
paths give the three commuting holonomies. Conversely put any commuting
triple on the three closing cuts, identity elsewhere. Residual gauge is
simultaneous conjugation. Covariant site data require each h_i to fix the
chosen datum. This classifies states by gauge orbits, not just Lie ranks.

Choose reference axis 1. For n!=0, its signed stabilizer is C4 (rotations
about the positively oriented reference axis), so there are 4^3=64
holonomy sectors for each charge PAIR {n,-n}. Choosing one representative
of that pair leaves the C4 stabilizer, whose conjugation is trivial. For
n=0 but the retained unoriented axis, the stabilizer is the order-eight
dihedral group D4. Commuting triples in D4 have 92 conjugacy orbits:

    |Hom(Z^3,D4)|=2*40+6*16=176,
    number of orbits=(2*176+6*64)/8=92.                (5)

Here D4 has two central elements and six noncentral elements with abelian
centralizer of order four. Burnside's lemma then gives the second formula.
Thus local plaquette flatness by itself neither removes global sectors nor
restores a faithful signed charge lattice. These counts concern this exact
flat-connection model; no claim about all finite-gauge models is made.

## 4. Constructive repair: a complete local frame, not just an axis

There is a local way to remove both defects, if additional fields and a
different observable net are accepted. Retain at each site a full vector

    F_x=(F_x,1,F_x,2,F_x,3) in (Z^8)^3,

but now add a FULL proper-cubic frame f_x in G_c and independent finite
links U_xy in G_c on every positive spatial edge. The kinematic Hilbert
space is the ordinary tensor product of l2(Z^24) and C[G_c] per site and
C[G_c] per link. It has 24N unbounded integer coordinates and 4N finite
24-state registers. Its site-vector spatial action is declared below; it
is not the old off-shell native oriented-edge transformation law.

The local finite gauge group G_c^N acts by

    f_x -> g_x f_x,   F_x -> g_x F_x,
    U_xy -> g_x U_xy g_y^-1.                           (6)

These are unitary permutations of the full orthonormal basis. Adjacent
vertex actions commute (left and right multiplication commute). Their
averages A_x=24^-1 sum_g V_x(g) are commuting orthogonal projectors.

Define the gauge-invariant BODY coordinates and the dressed connection

    q_x=f_x^-1 F_x in (Z^8)^3,
    Uhat_xy=f_x f_y^-1.                               (7)

Every coordinate remains integral because all f_x are signed permutations.
For mu,nu,lambda,zeta>0 define the local selection Hamiltonian

    P_align=mu sum_x [e(q_x,2)+e(q_x,3)],
    P_grad=nu sum_(positive edges xy) sum_a e(q_x,a-q_y,a),
    P_lock=lambda sum_(positive edges xy)(1-delta_(U_xy,Uhat_xy)),
    P_G=zeta sum_x (I-A_x),
    P_sel=P_align+P_grad+P_lock+P_G.                   (8)

The gradient is an exact Higgs-dressed covariant derivative:
sum_a e(q_x,a-q_y,a)=sum_a e((F_x-Uhat_xy F_y)_a).
On the lock constraint, Uhat is the actual independent link U. This
choice of the OFF-CONSTRAINT derivative is declared: replacing Uhat by U
there would define a different off-shell Hamiltonian.

There is a useful exact chart on the ENTIRE kinematic orthonormal basis:
(f,F,U) <-> (f,q,h), where h_xy=f_x^-1 U_xy f_y. Its inverse is
F_x=f_x q_x and U_xy=f_x h_xy f_y^-1. This is a bijection, hence a unitary
with no measure Jacobian. The gauge group acts only by left translation
of f, leaving q and h fixed. In this chart P_lock penalizes h_xy!=I,
P_align and P_grad act only on q, and P_G averages the independent finite
frame coordinates. No residual quotient or hidden orbit weight is omitted.

All terms in (8) strongly commute. The first three are diagonal; they are
gauge invariant, so commute with every A_x. Their diagonal eigenvalues are
nonnegative integer multiples of their displayed scales. Consequently

    spec(P_sel) subset {0} union [c,infinity),
    c=min(mu,nu,lambda,zeta)>0,                       (9)

uniformly in lattice size with fixed unscaled coefficients. This is a
penalty gap, not a thermodynamic phase diagram or sharp-gap assertion.

The diagonal zero conditions force

    q_x=(n,0,0) independently of x,
    F_x=f_x e1 n,
    U_xy=f_x f_y^-1.                                 (10)

All closed-loop holonomies are identity by telescopic cancellation of the
LOCK on each edge, including noncontractible loops. No chosen spanning
tree, hidden winding constraint or deletion of twisted sectors is used.
The extra full-frame locking field is exactly what forbids those sectors.

For each n there are precisely 24^N configurations (10), one for each
choice of f_x. The gauge group acts freely and transitively on them: the
unique transformation from f to f' is g_x=f'_x f_x^-1. Thus the only
gauge-invariant vector in that orbit is its normalized sum

    J|n>=24^(-N/2) sum_(f in G_c^N)
                    |f, F_x=f_x e1 n, U_xy=f_x f_y^-1>.          (11)

Different n have disjoint orthonormal orbit supports, including n and -n.
Equation (11) is unitary from l2(E8) onto ker P_sel. There is ONE vacuum,
no residual orientation multiplicity and no residual finite holonomy label.
The norm is exactly sum_n|psi(n)|^2. Projecting one basis representative
gives 24^(-N/2)J|n>, not the normalized orbit vector itself; this volume
normalization must not be omitted.

This is the familiar finite-gauge/Higgs setting in a specifically solvable
constraint model. Primary context: [Kitaev's finite-group lattice
construction](https://arxiv.org/abs/quant-ph/9707021) and
[Fradkin--Shenker's gauge--Higgs models](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.19.3682).
No phase-continuity or topological-order theorem from those papers is used;
(6)--(11) are proved directly here on the finite three-dimensional graph.

## 5. Exact energy, dynamics, cubic symmetry and the full charge algebra

Use the inherited charge normalization

    H_E=(1/N)sum_x sum_a e(F_x,a)=(1/N)sum_x sum_a e(q_x,a),
    H_charge=H_E+P_sel.                               (12)

H_E is invariant under the gauge group, hence strongly commutes with every
selection term. The diagonal part is coercive in all 24N electric integer
coordinates at fixed L. Adding the bounded self-adjoint P_G gives a positive
self-adjoint operator with the same operator domain, finite electric-support
core and compact resolvent. Its unitary group exists for every real time;
all selection projections reduce it. On the actual physical Hilbert space,

    J* H_charge J=e(n),  exp(-itH_charge)J=J exp(-it e(n)).        (13)

The complete Hamiltonian has a unique ground state J|0> and gap at least
min(1,c): nonphysical states pay (9), physical nonzero n cost at least one.
This is an exact finite-volume model result, uniform under the stated fixed
selection scales. The electric coefficient 1/N is still a declared global
charge normalization; no Maxwell or TFPT coupling law has been derived.

A spatial proper cubic rotation R acts by site/edge permutation and

    F'_x=R F_(R^-1 x),  f'_x=R f_(R^-1 x),
    U'_xy=R U_(R^-1 x,R^-1 y) R^-1.                   (14)

Reversed edges use U_yx=U_xy^-1. Then q'_x=q_(R^-1 x), so every term in
(8),(12) is invariant and J|n> is fixed. Cubic symmetry is retained without
choosing a physical orientation branch. Crucially this now makes n an
INTERNAL scalar charge under spatial cubic rotations; the frame remembers
the sign that the bare axis quotient lost. It does not turn n into a spinor
of spatial rotations or identify this gauge symmetry with spacetime gravity.

For every p in Z^8 define on the FULL kinematic basis the unitary

    Tcal_p |f,F,U> = epsilon(p,q_0,1)
                     |f, F_x+f_x e1 p for ALL x, U>.            (15)

The anchor q_0,1 is gauge invariant. Body coordinates q_x,1 increase by p
at every site; all other body coordinates and finite fields are unchanged.
Thus (15) commutes with every selection term and every gauge projector.
Its exact product, adjoint, and physical identification are

    Tcal_p Tcal_r=epsilon(p,r) Tcal_(p+r),
    Tcal_p*=epsilon(p,-p) Tcal_(-p),
    Tcal_p J=J T_p.                                   (16)

No charge direction or cocycle term was discarded. In particular
Tcal_(n_s)^4=Tcal_(4n_s)!=I. The whole Round16 grade-plus-integer-carry
unitary now applies ONCE, not three times, with all seven neutral transverse
coordinates and the unbounded winding retained. Tcal_p preserves the
energy domain by the usual positive-square translation bound; its physical
energy difference is n^T G p+e(p), unbounded in n for p!=0.

There is still a strict support cost. The gauge-invariant body charge q_x,1
is a local site observable with sharp eigenvalue n on J|n>. An operator
omitting one site's frame AND electric variables commutes with that site's
spectral projections, so has zero matrix elements between J|n> and J|m>
when n!=m. Every charge-changing operator must touch every site's charged
factor. Equation (15) saturates that site support bound; it is not a local
matter creation operator.

## 6. Interface to a common scalar--charge parent, and explicit costs

The local positive density

    Ecal_x=sum_a e(F_x,a)=sum_a e(q_x,a)               (17)

commutes with all selection constraints and reduces to e(n). Thus a local
scalar interaction built from Ecal_x and commuting scalar-site operators
ports to this single-copy model without reintroducing branch multiplicity.
For example a nonnegative coefficient times phi_x^2 Ecal_x is gauge and
selection preserving and reduces to e(n)phi_x^2. Its unbounded operator
realization and the coupled Ward/constraint source equations must be proved
for the proposed common parent; (17) is an algebraic interface, not that
missing coupled-source theorem. No charge transitions are generated by
interactions diagonal in Ecal_x alone.

More generally, a scalar source Q(Ecal) whose electric dependence is only
through these invariant densities is fiberwise in q and acts trivially on
f,h in the complete chart. Its self-adjoint fiber closures and spectral
groups therefore commute with all frame-selection projectors, including
the finite gauge averages. This statement uses the actual diagonal source
dependence; an operator shifting q would require a new check. At fixed N,
P_lock and P_G together are bounded by 3N lambda+N zeta. P_align and P_grad
are UNBOUNDED and belong to the electric diagonal fiber energy, not to that
bounded finite-register perturbation estimate. This distinguishes the
source-domain interface from an unjustified global boundedness claim.

What has been solved is the declared finite single-copy selection problem
with faithful charge translations, norm, energy and local constraints. Its
price is substantial and explicit:

- three-axis selection on the original native rotor net still has three
  physical branches;
- the successful one-copy parent adds full 24-state frames and finite links,
  replaces native edge fields by gauge-covariant site vectors, and chooses
  local Higgs locking rather than deriving it from TFPT;
- bare F and axis orientation are gauge variant; only dressed/internal
  observables and invariant densities survive the specified quotient;
- the regulator-normalized global charge energy and volume-wide charged
  operators remain, with no local charged scaling field, 3D chirality,
  flavor, Lorentz/continuum limit or microscopic uniqueness theorem.

The checker retains and reruns the frozen complete Round18 charge chain,
then tests literal integer/source data, native rotation covariance,
selection/cocycle signs, finite-group holonomy counts and free orbit
normalization. Finite exact checks support the above all-size proofs; they
are not a proof-assistant certificate, empirical validation or TOE closure.
