# Round17: a local rotor parent for the full E8 charge lift

2026-09-06. NON-RH. The added charge representation and its energy now have
an explicit finite-graph parent with local rotor energies and local Gauss
constraints. The charged operators are dressed winding Wilson operators,
not local matter fields. The gauge group constructed is U(1)^8, not a
derived nonabelian E8 gauge theory or a chiral 3+1D TFPT parent.

## 1. The exact target and what becomes local

Retain the entire ordered E8 lattice basis B, Gram matrix G=B^T B, spinor
s=b8, and cocycle of [Round16](../charged-lift-round16/PROOF.md):

    L=B Z^8, b1=2e1, bi=e1+ei (2<=i<=7), b8=(1/2)^8,
    G integral positive definite with even diagonal,
    epsilon(n,m)=(-1)^beta(n,m),
    beta(n,m)=sum_a n_a m_a G_aa/2
                     +sum_(a>b) n_a m_b G_ab mod2.      (1)

The target charge Hilbert space is l2(Z^8), with energy e(n)=n^T G n/2
and unitary T_n|m>=epsilon(n,m)|m+n>. It includes the full neutral
lattice, not just the four simple-current grades. Round16 supplied its
explicit integer carry coordinates and its finite-code multiplicity.

Here the same Hilbert space is the ordinary nonzero Gauss kernel of an
M-link cycle of compact rotors. Its norm is the inherited Hilbert norm;
no distributional zero-fiber evaluation is required. Every energy term is
on one link and every Gauss generator on two adjacent links. A full-cycle
Wilson operator with one local electric-parity factor realizes every T_n,
including its cocycle and its fourth-power winding relation.

The primary lattice-gauge context is the canonical rotor construction in
[Kogut--Susskind, Hamiltonian formulation of Wilson's lattice gauge
theories](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.395).
The special U(1)^8 model, Gram metric, exact norm, cocycle and locality
boundaries used here are derived below, rather than imported as an E8 claim.

## 2. Compact links with unbounded electric flux

Fix an oriented cycle with M>=3 vertices and M links, indexed modulo M.
On each link take L2(T^8,dtheta/(2pi)^8), with Fourier basis |q_j>,
q_j in Z^8. The total kinematic Hilbert space is equivalently

    H_kin = tensor_(j=0)^(M-1) l2(Z^8).

The eight electric operators E_j^a multiply q_j^a in this basis. Their
domains are the corresponding weighted square-summability domains; they
are self-adjoint and strongly commute. The bounded link shift is

    U_j(n)|q_0,...,q_j,...> = |q_0,...,q_j+n,...>.

It is unitary for every integer vector n. On the finite-Fourier core,
[E_j^a,U_k(n)]=delta_jk n_a U_k(n); equivalently the exponentiated relation
holds everywhere. Compactness of the angle torus does not make electric
flux finite. Replacing this rotor by a finite clock changes these relations.

The local Gauss operators and compact gauge representation are

    D_j=E_j-E_(j-1),
    R(theta)=exp(i sum_j theta_j.D_j).                   (2)

All D_j^a strongly commute. The common diagonal subgroup of gauge angles
acts trivially because sum_j D_j=0; the effective group has dimension
8(M-1). Keeping the redundant compact factor in normalized Haar averaging
only multiplies the answer by one, not by an infinite gauge volume.

Normalized compact Haar averaging is the bounded orthogonal projection

    P_G=integral_(T^(8M)) R(theta) dtheta,
    P_G|q_0,...,q_(M-1)>=indicator[q_0=...=q_(M-1)]|q_0,...>.
                                                               (3)

The Fourier integrals are exact Kronecker deltas. In particular

    iota|n>=|n,n,...,n>,
    iota:l2(Z^8) -> H_phys=ran P_G                         (4)

is unitary onto the physical space. For arbitrary physical coefficients
the norm is sum_n |psi_n|^2. The vacuum |0,...,0> and every uniform-flux
vector are normalizable. This is not the null-set kernel problem of the
earlier noncompact c constraints. In angle variables the same map sends
f(theta) to f(sum_j theta_j), with normalized Haar measure and no extra
factor of M.

## 3. Strictly local electric energy, with its normalization exposed

Define the nonnegative one-link energies and their sum

    h_j=E_j^T G E_j/(2M),  H_E=sum_j h_j.                (5)

The total is a diagonal self-adjoint multiplication operator on

    Dom H_E={psi: sum_q [sum_j q_j^T G q_j/(2M)]^2
                                     |psi_q|^2<infinity}.

Finite Fourier support is an operator core. Positive definiteness of G
implies finitely many configurations below every finite energy, so H_E
has compact resolvent at fixed M. Its exact group is multiplication by
exp[-it sum_j q_j^T G q_j/(2M)]. The Gauss projection strongly commutes
with H_E, and its restriction satisfies

    iota* H_E iota = E_L,   E_L|n>=n^T G n |n>/2.       (6)

Thus the full off-diagonal Gram terms and the whole source charge energy
are retained. For example e(b2+b3)=3, whereas deleting the off-diagonal
Gram entry would give 2. The spinor direction still has e(s)=1.

The even positive Gram lattice has e(n) an integer at least one for every
nonzero n, with equality attained by s. Thus the pure physical charge
Hamiltonian has gap one, whereas the unconstrained M-link electric
Hamiltonian has gap 1/M, attained by exciting only one link. Gauss is an
explicit constraint, not a claim that every low-energy unconstrained
state is already physical or that an M-independent enforcement gap follows.

Equation (6) is an on-Gauss identity, not an equality for arbitrary
nonuniform electric fields. For qbar=M^(-1)sum_j q_j the exact defect is

    H_E(q)-qbar^T G qbar/2
      =sum_j (q_j-qbar)^T G(q_j-qbar)/(2M)>=0.           (7)

One link carrying s and every other link carrying zero has total energy
1/M; the energy of its average flux is 1/M^2. The difference is positive.

The coefficient 1/M is part of the declared parent. It can be read as
spacing a=1/M at fixed circumference one. More generally local weights
alpha_j>0 with sum_j alpha_j=1 reproduce (6) exactly. With a fixed
coefficient kappa/2 per link and increasing circumference instead, the
physical energy is M kappa e(n), not e(n). This construction does not claim
a fixed-spacing thermodynamic normalization theorem or select a physical
length/coupling from TFPT. The local energies are unbounded operators;
bounded-spin Lieb--Robinson estimates are not automatically applicable.

## 4. Every charged and neutral shift, with the full cocycle

Choose one marked link, called 0, only to write the cocycle. Define

    W(n)=product_j U_j(n),
    D(n)=(-1)^beta(n,E_0),
    Tcal(n)=W(n) D(n).                                 (8)

D(n) is a bounded one-link electric-parity operator. W(n) shifts every
link by the same vector and therefore commutes with all Gauss constraints.
D(n) also commutes with them. Thus Tcal(n) is a gauge-invariant unitary
on the whole kinematic Hilbert space and preserves H_phys.

Direct calculation, including the shifted argument in D(n)W(m), gives

    Tcal(n) Tcal(m)=epsilon(n,m) Tcal(n+m),
    Tcal(n)*=epsilon(n,-n) Tcal(-n),
    Tcal(n) Tcal(m)=(-1)^(n^T G m) Tcal(m) Tcal(n).       (9)

These identities hold on the whole kinematic space, not just after
Gauss projection. On its physical basis,

    iota* Tcal(n) iota = T_n.                           (10)

Changing the marked link changes the off-constraint representative but
not (10), because every E_j equals E_0 on H_phys. The phase in (8) is the
prescribed E8 lattice cocycle; it is not derived from a dynamical anomaly
and does not turn the abelian gauge group into a nonabelian E8 group.
Bare Wilson cycles W(n) commute. They cannot replace (8): for n=e2 and
m=e3 the original Gram pairing is odd and (9) requires anticommutation.

For the source spinor direction n_s=e8,

    Tcal(n_s)^4=Tcal(4n_s)=W(4n_s)!=I.                  (11)

The cocycle at 4n_s is trivial. Composing iota with the explicit Round16
unitary Phi gives exactly its integer carry C, and (11) is its neutral
winding increment. Composing iota tensor I with Round16's Omega likewise
realizes the finite-code lifted representation with exactly the same code
multiplicity. No grade-only identification or finite-cycle truncation is
used.

Translation preserves Dom H_E, since H_E(q+n)<=2H_E(q)+n^T G n. On the
finite-Fourier core its full kinematic energy commutator is

    [H_E,Tcal(n)] = Tcal(n) [n^T G qbar+n^T G n/2].      (12)

The corresponding bounded exponentiated evolution identity holds on the
whole Hilbert space. On Gauss states qbar is exactly the uniform charge.
The charged energy increment is unbounded; localizing the Hamiltonian has
not turned the charge shift into a uniformly bounded-energy operation.

## 5. Exact spatial support boundary

Let O be any bounded operator supported on a proper subset A of the links,
acting as the identity on at least one omitted link. For distinct uniform
fluxes n and m, that omitted link alone gives

    <m,...,m|O|n,...,n>=0.                              (13)

By linearity and density, P_G O P_G is diagonal in the uniform-flux basis.
No assumption of gauge invariance is needed for this compressed statement.
If O is gauge invariant, it preserves H_phys and its physical restriction
is therefore diagonal. It cannot produce any nonzero charged corner.

This is an exact support theorem: in this pure-gauge cycle, a nontrivial
physical flux-changing operator must involve the entire cycle. The W(n)
part of (8) has precisely that winding support. A one-link shift violates
Gauss at its two endpoints; an open product has the corresponding endpoint
charges. They are not physical closed-cycle charge operators. Adding
charged matter and changing Gauss's law is a different parent, not implicit
in the present proof.

The local energy can be measured on one link after imposing Gauss, but
the operator that changes its uniform flux remains nonlocal around the
cycle. Consequently this is a localization of energy and constraints,
not a local realization of the E8 vertex field or of chiral matter.

## 6. Finite bounded perturbations and the code multiplicity

Let B_fin be any bounded self-adjoint operator commuting with the gauge
representation; a finite sum of bounded local gauge-invariant terms is
an example. Then H_E+B_fin is self-adjoint on Dom H_E and is bounded
below by -||B_fin||. Its resolvent is compact: for imaginary z of modulus
larger than ||B_fin||, the Neumann factorization against the compact
(H_E-z)^(-1) proves this directly. Gauge invariance makes H_phys reducing,
so its inherited physical norm and the restricted self-adjoint domain are
unchanged. A shift by ||B_fin|| makes the Hamiltonian nonnegative.

Existence of its all-time unitary group is not left to finite matrices.
In the interaction picture the iterated strong integrals of the bounded
B_fin(t) have norms bounded by (|t| ||B_fin||)^k/k!, giving a uniformly
norm-convergent Dyson series on compact time intervals. If every term is
supported on a proper link subset, (13) makes its physical restriction
diagonal; such a perturbation changes charge energies but cannot change
the uniform electric flux. A winding perturbation can mix flux, but is
not a bounded-range term uniformly as M grows.

An additional finite Hilbert space H_0 can be tensored in exactly as in
Round16. A bounded self-adjoint family B_r on H_0 may be controlled by
the old grade r(E_0)=2 sum_(i<=5)(B E_0)_i mod4 at the marked link:

    B_code=sum_(r=0)^3 indicator[r(E_0)=r] tensor B_r.    (14)

It is bounded and gauge invariant, and strongly commutes with H_E.
Choosing B_r=V_r* H_r^code V_r reproduces the Round16 finite-code energy
under the displayed unitary. This is local with respect to the new rotor
cycle plus one finite ancillary cell. It does not prove locality inside
the original QWZ cylinder: H_0 is the previously selected global code
fiber, and the V_r include its disorder string. No global QWZ constraint
or hidden cylinder support is relabelled as an elementary local site.

## 7. What extends to a three-dimensional graph

On any finite connected oriented graph with v vertices and e links the
same eight-component rotors, local incidence Gauss laws, local Gram energy
and bounded gauge-invariant perturbations are well-defined with the same
self-adjointness argument. The physical integer fluxes are

    ker(incidence:Z^e->Z^v) tensor Z^8
                        ~= Z^[8(e-v+1)].               (15)

A spanning tree supplies an integral fundamental-cycle basis: every
non-tree edge sets one free flux and tree-edge Gauss equations determine
the rest with integer coefficients. This proves (15), not merely its
real dimension. The single cycle worked because e-v+1=1.

On a periodic three-dimensional cubic graph with n vertices, e=3n and
the cycle rank is 2n+1, so Gauss alone leaves 8(2n+1) integer coordinates,
not eight. In particular an elementary plaquette supports a nonzero
divergence-free electric circulation that is not a uniform global flux.
Local bounded plaquette Wilson terms give legitimate additional dynamics,
but preserve the Gauss law and do not delete these physical degrees of
freedom. Selecting just one winding sector, freezing other links, or adding
additional flatness constraints changes the model and requires its own
selection proof. Embedding the one-dimensional ring in space also does
not create three-dimensional propagation or a chiral spectrum.

## 8. Negative controls and the remaining claim boundary

The checker rejects dropping the off-diagonal Gram terms, applying the
physical energy identity off Gauss, forgetting the circumference
normalization, omitting the cocycle, replacing the full winding by one
link, or counting a three-dimensional Gauss kernel as one global flux.
It also distinguishes a compact rotor from a finite clock. With flux
truncated to -N,...,N, the hard-cutoff shift is not unitary; cyclic wrapping
instead changes [E,U]=U at the boundary by -(2N+1)|-N><N| and makes a
nonzero winding translation periodic. Neither is the exact full charge lift.

The constructive result is a spatially local energy and Gauss parent for
the entire specified lattice charge representation, together with its
exact physical norm, cocycle, carry and controlled finite-size quantum
dynamics. The parent, its normalization, compact gauge group and code
embedding are declared choices, not derived TFPT microscopic data. It
does not supply local charged fields, nonabelian gauge dynamics, the
oscillator/vertex scaling theorem, 4D chirality, flavor, a common matter-
gravity parent, or a continuum/thermodynamic limit. No TOE or RH promotion.

## Reproduction

Run `checker.py` from any directory with the project Python environment.
It verifies frozen source hashes, the unchanged complete Round16 checker
separately, and new exact graph/Gauss/cocycle/energy/support identities.
Tests use integer electric configurations and exact phases, not finite
CCR surrogates. The all-M and all-Hilbert-space claims rest on the proof
above; finite graph fixtures and negative controls are independent checks.
