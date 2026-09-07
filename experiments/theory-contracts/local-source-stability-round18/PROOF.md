# Round18: a cellwise source stabilizer with complete covariant dynamics

2026-09-06. NON-RH, unpromoted finite-lattice research. This constructs a NEW
higher-order completion that preserves the specified first vertex and physical
zero-constraint dynamics. It is not equal to the old global stabilizer and does
not make nonlocal Darboux sources local. That distinction is quantified below.

## 1. Exact finite-dimensional constraint setup and result

There are N cells, scalar coordinates r_i and m-component vectors v_i (m=3
in the lattice application). The allowed constraint coordinate space C is
either the full real space or a fixed linear subspace invariant under

    r'(t)=b v(t),       v'(t)=0,
    c(t)=Phi_t c=(r+t b v,v).                                    (1)

For the original mean-free gravitational chart, C has dimension 4(N-1).
Cell coordinates then have linear dependencies, but their Euclidean norm is
the norm induced from the full cell space. The shear restricted to C has
determinant one. All canonical source and constraint inner products are
reconstructed in this same fixed real cell chart; no independent homogeneous
canonical mode is added by using redundant cell labels.

Let X>=0 be one of the chosen scalar/TT Hamiltonians A_+, A_delta, A_0 or the
zero-point-subtracted local parent B_delta,eta. In each case X has a positive
constant kinetic matrix and a smooth polynomial multiplication potential
bounded below. Source operators Q_i=(Q_ri,Q_vi1,...,Q_vim) are the closures
of the literal real Weyl quadratics, acting on the scalar coordinates. They
may be noncommuting and may have identically zero members. Write

    d_i=(b v)_i,
    rho_i(c)=r_i^2+|v_i|^2+d_i^2,
    S_i[u]=||Q_ri u||^2+sum_j ||Q_vij u||^2.                    (2)

Define the new form

    h_c[u]=q_X[u]+g sum_i <u,(r_i Q_ri+v_i.Q_vi)u>
                          +g^2 sum_i rho_i(c) S_i[u].         (3)

The previous term g^2|c|^2 sum_i S_i is **replaced**, not algebraically
rewritten. The result is an all-time unitary characteristic propagator, strong
continuity across all active/inactive cell strata, a shear-covariant full
self-adjoint generator, and exactly the original positive physical norm and
X dynamics at c=0. No extra canonical pairs are required by (3).

If b has finite range and Q_i has uniformly bounded spatial support near i,
the NEW stabilizer has finite range. The actual Darboux Q_ri=Bcal_i fails the
second hypothesis: its kinetic coefficient is an inverse spatial Laplacian.
Thus (3) removes a separate all-to-all constraint/source multiplier, but it
is not a native-local TFPT Hamiltonian. A different local chart/source bridge
must establish its own first-vertex identification before using that label.

## 2. Why the transport contribution in rho is necessary

Along (1), d_i and v_i are constant, hence

    rho_i(t)=(r_i+t d_i)^2+|v_i|^2+d_i^2,
    |rho_i'(t)|=|2(r_i+t d_i)d_i|<=rho_i(t).                    (4)

In particular rho_i(t)=0 at one finite time if and only if
r_i=v_i=d_i=0, in which case it is identically zero. The active set

    I(c)={i:rho_i(c)>0}                                       (5)

is invariant along the entire characteristic. Moreover
exp(-|t-s|)rho_i(s)<=rho_i(t)<=exp(|t-s|)rho_i(s).
On a compact time interval each active rho_i has a positive minimum.

Using only r_i^2+|v_i|^2 would not have this property. A neighboring v can
give d_i!=0 while r_i=v_i=0, so a cell would acquire a new source-graph domain
immediately after t=0. For v_i=0,d_i=1,r_i=epsilon, the uncorrected relative
derivative is 2/epsilon. Including d_i^2 is a new positive local-in-b choice
that prevents this singular activation. No uniqueness/minimality of that
choice is claimed; units and the cell metric are fixed input.

## 3. Closed forms, finite-volume lower bound and energy control

For g!=0 define precisely

    D_I=Dom(X^(1/2)) intersection
                           (intersection_(i in I, alpha) Dom Q_i,alpha).

Inactive sources impose NO graph condition: their coefficients and first
linear couplings vanish. D_I is complete in its sum of closed graph/form
norms and contains C_c^infinity. Set W_c[u]=g^2 sum_i rho_i S_i[u]. Then

    |g sum_i <u,c_i.Q_i u>|
       <=sum_(i in I) |g|sqrt(rho_i) sqrt(S_i[u]) ||u||
       <=sqrt(N) sqrt(W_c[u]) ||u||
       <=W_c[u]/2+N||u||^2/2.                               (6)

Consequently e_c[u]=h_c[u]+N||u||^2 obeys

    q_X+W_c/2+(N/2)||u||^2 <= e_c
       <=q_X+3W_c/2+(3N/2)||u||^2.                          (7)

These are equivalent complete positive form norms at each fixed c. The
linear term has relative form bound at most 1/2, so h_c is closed with a
specified self-adjoint form representative. The sharper completed-square
bound, with c_i=(r_i,v_i), is

    h_c[u]=q_X[u]+sum_(i in I,alpha)
        ||g sqrt(rho_i) Q_i,alpha u+c_i,alpha u/(2sqrt(rho_i))||^2
                   -sum_(i in I) |c_i|^2/(4rho_i)||u||^2
             >=q_X[u]-N||u||^2/4.                           (8)

The sign of g is retained inside the square. No source commutation or
self-adjointness of a bare noncommuting sum of squares is assumed. At c=0
or g=0 the form reduces to q_X on its original domain.

Differentiate at fixed u along a characteristic. The derivative of the linear
term is controlled by sum_i |g||d_i|sqrt(S_i)||u||, and |d_i|<=sqrt(rho_i).
The derivative of W is controlled by W through (4). Equations (6),(7) give

    |partial_t e_c(t)[u]|<=3W_c(t)[u]/2+N||u||^2/2
                                      <=3e_c(t)[u].          (9)

The number 3 refers to the displayed fixed time/coordinate units; the cost
of b enters rho itself. The shift and finite-volume lower bound grow with N.
No uniform thermodynamic/continuum stability theorem follows from (7)--(9).

## 4. All-time characteristic propagators on every activity stratum

The active set is fixed on a characteristic, so D_I is one common dense
complete form space there. Equations (4),(7) give equivalent positive norms
on each compact time interval, and all coefficients in (3) are smooth in t.
Thus Assumption 3.8 and Theorem 3.10 of
[Balmaseda, Lonigro and Perez-Pardo](https://arxiv.org/html/2112.11063v2)
apply. Removing the constant N phase gives the unique unitary propagator
V_c(t,s), preserving D_I. Patching compact intervals gives every real time.

Its energy obeys

    e_c(t)[V_c(t,s)u]<=exp(3|t-s|) e_c(s)[u].                  (10)

For inactive I the propagator is exp(-i(t-s)X). For an active I it is the
form-selected realization, not a claim that every fourth-order minimal
expression has the same extension. Compact smooth physical tests belong to
the representing operator domain and its action there is the displayed
polynomial expression X+g sum c_i.Q_i+g^2 sum rho_i sum Q_i,alpha^2.

## 5. Strong continuity across changes of active cells, including c=0

This is required; assigning independent values on zero-measure strata would
not justify the zero-fiber physical reduction. Let c_k->c_* in C and start
with a compact smooth physical psi. Initial energies e_ck[psi] are uniformly
bounded, hence so are the evolved energies (10) on compact time intervals.
The norm and q_X bounds are uniform. For every i active at c_*, rho_i(c_k(t))
has a positive lower bound for large k on that time interval. Thus all target-
active source graph norms are uniformly bounded, and weak limits belong to
D_I(c*) by closedness of the individual source/form operators.

For newly inactive cells the weighted norm bound still gives the explicit
weak suppression

    |g c_ki.<Q_i z,u_k>|<=C_z |c_ki|,
    |g^2 rho_i(c_k) sum_alpha <Q_i,alpha z,Q_i,alpha u_k>|
                                     <=C_z sqrt(rho_i(c_k)),  (11)

uniformly in time. At an exactly inactive approximant both terms are defined
as zero without imposing Q_i u_k membership. For compact smooth tests there
is an even direct coefficient statement: h_ck(t)z->h_c*(t)z in H uniformly
on compact time sets, because every Q_i,alpha^2 z and Xz is in H.
The corresponding scalar weak-solution amplitudes are uniformly equicontinuous.

The common form-core argument of
[Round17, Section 4](../adiabatic-source-round17/PROOF.md) holds for ANY subset
of these Weyl quadratics: first use compact radial cutoffs, whose commutators
need only H1 derivatives, then mollify on a compact support. For a base with
potential bounded below, add its finite constant before this argument.
Thus C_c^infinity is a form core in every D_I, including all the domains
appearing at a boundary between activity strata.

Weak subsequential limits therefore solve the target equation first on
compact smooth tests and then, by the form core and uniform target D_I bound,
in L2_t D_I intersect H1_t D_I*. The Hermitian form energy identity gives
uniqueness and preservation of Hilbert norm in this class. Consequently the
only weak limit is V_c*(t,0)psi, with the same norm as every approximant.
Weak convergence plus equal norms gives strong convergence. A finite net
along the continuous limiting orbit makes it uniform on compact time sets.
Density and unitarity extend this to every Hilbert vector. In particular,

    sup_(|t|<=T)||V_c(t,0)psi-exp(-itX)psi|| ->0 as c->0.      (12)

No global invariance of Schwartz vectors, common operator domain, or uniform
source graph bound for a vanishing coefficient has been assumed.

## 6. A full covariant generator and the unchanged positive reduction

Let k(c) be the same real scalar free constraint potential and use Lebesgue
measure on the independent orthonormal coordinates of C. Define on L2(C;H)

    (U(t)F)(c)=exp(-i integral_0^t k(Phi_-s c) ds)
                         V_(Phi_-t c)(t,0) F(Phi_-t c).       (13)

The characteristic propagator cocycle gives the group property, the shear
has determinant one, and Section 5 supplies strong continuity. Stone's
theorem gives a self-adjoint generator whose action on smooth compact
constraint sections with compact smooth physical factors is

    H_cell=-i(bv).partial_r+k(c)+X+g sum_i c_i.Q_i
                              +g^2 sum_i rho_i sum_alpha Q_i,alpha^2. (14)

To justify differentiation on these tests, for a fixed compact smooth z use
V_c(t,0)z-z=-i integral_0^t V_c(t,s)h_c(s)z ds. The norm of h_c(s)z is
bounded on compact c/time sets. The active set is fixed along each integral,
so the common-form propagator theorem legitimizes this identity even for
labels on a stratum boundary. Dominated convergence then gives the full
L2 difference quotient. There is no asserted core uniqueness of the full
minimal expression.

For every bounded Borel F on C the exact strong covariance is

    U(t)^* F(c) U(t)=F(Phi_t c).                              (15)

For k(0)=0, normalized Gaussian-regulated constraint averaging on continuous
compact sections gives

    q_phys(F,G)=<F(0),G(0)>,
    [U(t)F](0)=exp(-itX)F(0).                               (16)

The quotient completion is exactly H with its original positive norm. It is
not an ordinary kinematic L2 zero kernel. The added cell stabilizer has degree
two in c and starts at g^2, so it and its first constraint derivative vanish
at c=0. It does not change the entire original first dressed interaction
vertex of the model whose base X is being held fixed, provided the unchanged
linear term is expressed in the same chart. In particular X=A_+ gives the
original target TFPT vertex identity from Round15. With finite X=B_delta,eta,
this preserves that declared local parent's first jet, NOT an equality of
its enlarged finite-parameter interaction with the old scalar/TT vertex.
The target scalar/TT plus constraint vertex is reached only through the
stated eta and delta limits; the base-family choice and its extra fields
cannot be ignored when comparing first jets.
Weyl operator-square ordering constants remain multiplied by rho_i and also
vanish to second constraint order; they may not be dropped off the surface.

## 7. The existing adiabatic source bridge survives this replacement

Take X=B_delta,eta and the same Gaussian J_delta,eta as in Round15/17.
On a fixed characteristic the active set is fixed. The exact Round17 residuals
for every Q and every Q^2 imply on compact smooth slow tests

    ||(h_B,cell(t)J-J h_delta,cell(t))psi||
                    <=sum_(k=1)^4 C_k eta^(k/4),             (17)

uniformly on compact time intervals. The constants use only finitely many
cell coefficients and the existing K_delta/f_delta derivative bounds.
Equation (10) bounds the base B form and the ACTIVE source graphs uniformly.
The varying-space weak-limit proof of Round17 applies to that subset: local
derivatives of J^* are controlled on compact slow sets, potentials commute
with J^*, and source graphs are identified distributionally. Its subset form
core gives the unique limiting weak evolution. The equality-of-norm argument
therefore proves full uncompressed direct-J intertwining for (3) as eta->0.

The subsequent delta->0 limit follows from the same compact-local positive-
potential convergence, with no equality of global potential form domains
asserted across delta. All 4n+2 physical spectator modes remain. This is a
statewise sequential finite-regulator result, not an arbitrary joint parameter
limit or a state/volume-uniform error bound. Clock constructions must retain
the same explicit energy subtraction and spectator treatment.

## 8. Finite-range conditional theorem and the actual Darboux obstruction

If (a) b has range R_b in the chosen cell chart, and (b) each Q_i,alpha is
supported within a fixed neighborhood of i of radius R_Q, then each term of
the new stabilizer depends only on the union of those neighborhoods and the
constraint cell. Its range is bounded independently of N. Operator squaring
does not enlarge support beyond the variables on which Q_i already acts.
This removes the old coupling between every constraint cell and every source
cell. It says nothing about the range of the remaining base X or k(c).

For the original staggered chart the free transport really is local:

    (bv)(x)=sum_j [v_j(x)-v_j(x-e_j)].                        (18)

But source locality does not follow. On a nonzero Fourier mode of the actual
scalar constraint vector S(k),

    |S|^2=2ell^2,       S^T trace=2ell,       B_H=-1/(2ell),
    Bcal=(S^T tau)/(2ell^2)+rho/(2ell).                       (19)

The literal Ward kinetic terms are tau_ii=pi^2/2+configuration terms and
rho=pi^2/2+configuration terms. Hence, after reconstruction into the mean-free
cell source,

    (Bcal_i)_kinetic=(3/4) sum_j G_ij pi_j^2,
    G=ell_nonzero^(-1),       ell G=I-P_mean.                 (20)

These are genuine coefficients of the original source; no other term can
cancel them because the other displayed terms contain only configurations.
On the original L=3 periodic graph,

    G_(000,111)=-11/486,
    coefficient_(pi_111^2) Bcal_000=-11/648,
    partial_(pi_111)^2 Bcal_000=-11/324.                     (21)

The separation has graph distance three, exceeding the nearest-neighbor
transport stencil. More generally G cannot have any volume-independent finite
range R: then ell G would have range R+1, whereas I-P_mean has nonzero entry
-1/N at every distinct pair, including arbitrarily distant ones on growing
periodic lattices. This argument does not rely on fitting numerical tails.

Thus replacing the global source multiplier is a real independent improvement,
but the current Darboux-source application remains nonlocal. The theorem gives
a usable finite-range stabilizer for a genuinely local source chart IF that
chart independently realizes the required linear vertex and constraint algebra.
It neither proves such a chart impossible nor silently supplies one.

## 9. Verification and explicit remaining costs

The companion checker imports the original Ward energy, stress and currents;
verifies the actual shear matrices on L=2,3, the source inverse-kernel kinetic
coefficient, first-vertex/second-ideal preservation, exact ordering terms,
activity invariance, domain-change failure control, coercivity and derivative
constants, and the original L3 nonlocal source witness. Finite algebra checks
support the analytic domain and propagator proof, not a finite CCR truncation.

The completion changes higher off-shell orders; fixes a cell metric and time
normalization; retains fourth-order source differential operators, extensive
lower-bound/shift costs and the original local-parent singular limits; and
does not remove source/TT nonlocality, select chiral matter, derive the trace
clock or establish the full microscopic/continuum TFPT contracts. No RH claim.
