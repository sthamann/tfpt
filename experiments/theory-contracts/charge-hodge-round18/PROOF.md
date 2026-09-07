# Round18: three-dimensional electric Hodge parent and cubic selection boundary

2026-09-06. NON-RH. This is one explicit extension of the frozen rotor charge
parent to the whole periodic three-dimensional cubic lattice. Local electric
divergence and curl constraints select exactly three copies of the original
E8 charge lattice, with an explicit volume-independent penalty bound. No
single-copy, chiral, magnetic or full-TOE identification is inferred.

## 1. Retained data and precise operators

Keep the full integer-coordinate E8 basis B, even positive Gram matrix
G=B^T B, source spinor s=B e8, and cocycle epsilon(n,m)=(-1)^beta(n,m)
of [the frozen local rotor parent](../local-charge-parent-round17/PROOF.md).
Write e(n)=n^T G n/2. For every nonzero integer n, e(n) is an integer at
least one, and e(e8)=1. No internal charge coordinate or Gram cross term
is dropped.

Let the spatial lattice be (Z/LZ)^3, L>=2, with N=L^3 sites and all 3N
positively oriented links retained. Each link (x,i), i=1,2,3, carries
L2(T^8)~=l2(Z^8), with commuting integer electric coordinates E_i(x).
Use the matched forward and backward differences

    d_i^+ f(x)=f(x+e_i)-f(x),
    d_i^- f(x)=f(x)-f(x-e_i),
    D(x)=sum_i d_i^- E_i(x),
    C_ij(x)=d_i^+ E_j(x)-d_j^+ E_i(x), i<j.             (1)

D is the ordinary incidence Gauss divergence. C is an additional electric
curl, a four-edge local operator on an oriented plaquette. Every component
of D and C is an integer diagonal self-adjoint operator, and their spectral
measures strongly commute. The backward/forward choices in (1) matter.

The context is discrete Hodge theory; see the primary article
[Dodziuk, Finite-difference approach to the Hodge theory of harmonic
forms](https://academicworks.cuny.edu/gc_pubs/180/). The specific periodic
identity and the integer-kernel result needed here are proved directly next;
no continuum approximation theorem is imported from that article.

## 2. Exact discrete Hodge identity and the full integral kernel

For every real or complex electric configuration, with the G inner product
on internal coordinates, periodic summation gives

    sum_x [D(x)^* G D(x)+sum_(i<j) C_ij(x)^* G C_ij(x)]
      =sum_(x,i,j) (d_i^+ E_j(x))^* G(d_i^+ E_j(x)).    (2)

For clarity, at Fourier momentum k put z_i=exp(ik_i)-1. The divergence
symbol is -sum_i conjugate(z_i) E_i, and the curl symbols are
z_i E_j-z_j E_i. After applying G^(1/2) internally, (2) is precisely

    |sum_i conjugate(z_i) v_i|^2
       +sum_(i<j)|z_i v_j-z_j v_i|^2
      =sum_i |z_i|^2 sum_j |v_j|^2.

At every nonzero periodic momentum at least one z_i is nonzero. Equivalently,
positivity of G in (2) forces every forward difference of every E_j to
vanish whenever D=C=0. Connectivity then gives

    D=C=0  iff  E_i(x)=n_i independently of x,
    n_i in Z^8 for integer electric configurations.     (3)

There is no fractional harmonic-flux assumption: taking the value at any
one site recovers each n_i as an actual integer vector. Thus the integral
kernel is exactly Z^24, or L_E8 direct_sum L_E8 direct_sum L_E8 in physical
charge coordinates. Conversely every such constant triple satisfies (1).
This proves both directions and excludes extra integral torsion sectors.

Normalized compact averaging of exp[i theta.D+i eta.C] is the orthogonal
projector P_H onto this ordinary kernel. Redundant compact generators only
give normalized Haar factors of one. The displayed basis map

    iota_3|n_1,n_2,n_3>=tensor_(x,i)|n_i>               (4)

is unitary from l2((Z^8)^3) onto ran P_H. Its norm is the ordinary sum of
squared coefficients and it has a nonzero normalized vacuum. No evaluation
on a measure-zero noncompact constraint surface is being used.

For comparison, at L=3 Gauss alone leaves 8(2N+1)=440 integer cycle
coordinates, as in Round17. Joint electric divergence and curl leave 24.
Their real rank is 8[3N-3]; (3), not this rank count alone, proves the
integral statement.

## 3. Local positive penalty and exact charge energy

At a declared scale Delta>0 define

    P_Delta=Delta sum_x [e(D(x))+sum_(i<j)e(C_ij(x))],
    H_E=(1/N)sum_(x,i)e(E_i(x)),
    H_parent=H_E+P_Delta.                               (5)

These are local nonnegative diagonal Hamiltonians. The penalty kernel is
exactly (3). Each nonzero e(D) or e(C) is at least one. Moreover sum_x D=0
and sum_x C_ij=0 separately, so a nonzero value in any one of these fields
requires at least one other nonzero value in that same field. Therefore

    spec(P_Delta) subset {0} union [2 Delta,infinity).  (6)

This lower bound is uniform in L; no sharp-gap claim is made. One source
spinor flux on a single oriented link has penalty 6 Delta, so the nonzero
penalty spectrum is nonempty and its lowest value is at most 6 Delta.
The argument uses integer electric flux and an unscaled Delta in (5).
For real continuously variable electric fields, or a penalty coefficient
scaled to zero with N, that uniform conclusion would not follow.

On the exact harmonic kernel,

    iota_3* H_parent iota_3=sum_(i=1)^3 e(n_i).          (7)

The three-copy Gram energy, including every internal cross term, is
retained. The coefficient 1/N is a declared normalization of these global
charges; a fixed per-link coefficient instead multiplies (7) by N. It is
not claimed to be the standard Maxwell continuum scaling or a TFPT-derived
coupling. Equation (7) is not a claim that only eight charges survive.

On the full finite lattice H_parent is a positive self-adjoint diagonal
operator, with weighted square-summability domain and finite Fourier
support as an operator core. H_E is coercive in all 24N integer coordinates,
so H_parent has compact resolvent. Its exact group is the diagonal phase
exp(-itH_parent). The harmonic projection strongly commutes with it. Because
H_E>=0, any energy below 2 Delta lies in the harmonic sector; high-energy
harmonic fluxes are still physical even above that threshold. A finite
penalty does not replace the exact constraint prescription at all energies.

Bounded self-adjoint perturbations preserving all D,C constraints retain
the domain and the ordinary physical norm, by the same bounded-perturbation
argument as Round17. Merely preserving Gauss is insufficient here.

## 4. Full cocycle, carries and the support of a harmonic charge shift

Let U_(x,i)(n) shift the integer electric vector on that one link. For
each direction choose a marked link at x=0 and define

    W_i(n)=product_x U_(x,i)(n),
    Tcal_i(n)=W_i(n)(-1)^beta(n,E_i(0)).                 (8)

W_i changes every electric vector in direction i by the same n and leaves
the other directions unchanged. It preserves D and C on the whole
kinematic space. The one-link cocycle parity commutes with all of them.
Within each direction the frozen product and adjoint laws hold exactly;
different directions commute. Thus the full representation is

    Tcal(n_1,n_2,n_3)=product_i Tcal_i(n_i),
    epsilon_3(n,m)=product_i epsilon(n_i,m_i),
    iota_3* Tcal(n) iota_3=T_(n1) tensor T_(n2) tensor T_(n3).
                                                               (9)

For each source-spinor direction Tcal_i(e8)^4=W_i(4e8)!=I. Applying the
three copies of the exact Round16 carry map gives three order-four grades,
three integer carries, and all twenty-one transverse neutral coordinates.
It does not collapse these to one selected grade or one E8 copy.

A single winding loop at fixed transverse position preserves Gauss, but
does not preserve electric curl: its electric profile is not constant in
the two transverse directions. The operator W_i in (8) is the product of
all L^2 parallel winding loops, containing N links of direction i.

There is an exact support requirement. Between harmonic states with
n_i!=m_i, every one of the N direction-i link labels differs. An operator
omitting even one of those links has a zero matrix element between those
states by spectator orthogonality. Changing flux in a set I of directions
therefore requires all N|I| corresponding links. This is a finite-graph
support theorem, not a local chiral-field construction. The local energy
and constraints do not make their charged harmonic operators local.

## 5. Electric curl is an added physical restriction, not magnetic flatness

The conventional magnetic plaquette Wilson operator shifts electric flux
around the oriented boundary of one plaquette. This profile has zero
divergence, but nonzero electric curl. Consequently it preserves Gauss
and fails to preserve the additional C=0 list. It is a valid bounded
operator on the full rotor space, not an allowed exact-constraint
interaction for (3). Adding it to a finite-penalty Hamiltonian is a new
dynamics with mixing out of the harmonic subspace.

The magnetic plaquette itself is a product of compact angle variables.
Its cube-boundary/Bianchi identity follows from cancellation of link angles.
It is not the electric equation dE=0 in (1). Although d(dE)=0 is also an
algebraic cochain identity, that identity does not force dE=0. Thus the
new constraint deliberately removes ordinary transverse electric degrees
of freedom. It supplies neither the usual Maxwell photon sector nor a
3+1D matter or fermion spectrum.

## 6. Can cubic-symmetric local synchronization select one E8 copy?

Here spatial rotations act on the three oriented flux directions and act
trivially on the eight internal lattice coordinates. This assumption is
part of the present rotor model; no compensating internal rotation is
invented. On harmonic flux triples the proper cubic group is the group of
24 signed permutation matrices R with det R=1.

An explicit local synchronization term is

    P_sync=kappa sum_x sum_(i<j)e(E_i(x)-E_j(x)).        (10)

Together with (3) it selects n1=n2=n3=u, a rank-eight diagonal lattice.
But it is not invariant under proper cubic rotations. The pi rotation
R=diag(1,-1,-1) sends (u,u,u) to (u,-u,-u), outside that diagonal unless
u=0. For the source spinor u=e8, the harmonic synchronization energy per
site divided by kappa changes from 0 to 8. Equal treatment of the names
x,y,z is not the same as invariance under signed physical rotations.
Even on its selected diagonal, the retained energy (7) is 3e(u), not e(u);
recovering one-copy energy requires another declared rescaling.

Symmetrizing (10) does not solve the selection. Its direction matrix is
M=3I-11^T. On harmonic fields,

    (1/24)sum_R R^T M R=2I,
    average_R sum_(i<j)e((R n)_i-(R n)_j)=2 sum_i e(n_i).
                                                               (11)

The cubically averaged local positive term therefore annihilates only
the zero harmonic triple, not one nontrivial E8 copy. The full-space
average remains local; orientation-dependent edge-base shifts under
rotations do not affect this exact harmonic-sector calculation.

A more general bounded theorem avoids overinterpreting this one example.
If a real linear subspace S of R^3 tensor R^8 is invariant under all proper
cubic rotations with this internal action, then

    S=R^3 tensor W for some W subset R^8,
    dim S=3 dim W.                                     (12)

Indeed the pi rotations R_i fixing axis i give the coordinate projectors
P_i=(I+R_i)/2. Invariance implies P_i S subset S, so S is the direct sum
of its three axis parts. Rotations permuting the axes force their internal
subspaces to be equal, including the harmless signs. This proves (12).
The real span of an invariant additive rank-eight charge sublattice would
violate (12). Equivalently any invariant positive quadratic penalty has
direction form I_3 tensor A and a kernel whose dimension is divisible by
three. Thus local linear constraints or positive quadratic penalties,
restricted to these harmonic variables and this rotation action, cannot
select exactly one rank-eight lattice without an additional choice.

This is not a universal no-go. For example the local nonnegative quartic
term sum_(x,i<j) e(E_i(x))e(E_j(x)) has, on harmonic fields, the cubically
invariant zero set in which at most one n_i is nonzero. It keeps three
orientational branches, not a single additive E8 lattice; the sum of states'
flux labels from two different nonzero branches leaves that zero set. New
orientational matter, a selected symmetry-breaking branch, a nontrivial
internal rotation action or other nonlinear constraints are different
possibilities, not excluded by (12) and not derived here.

## 7. Constructive result and remaining scope

The whole periodic 3D lattice now has a local positive rotor Hamiltonian,
local commuting Gauss and electric-curl constraints, a rigorously identified
integral harmonic kernel, a volume-independent penalty lower bound, exact
physical norm, and the full three-copy E8 charge energy/cocycle/carry.
The original 440-dimensional integer Gauss cycle lattice at L=3 is reduced
to exactly 24 harmonic integer coordinates without deleting edges.

What remains is selection of one physical charge sector or a different
matter mechanism, not another missing matrix rank. The extra electric-curl
constraint is postulated; it removes local transverse dynamics rather than
proving 3D chiral matter. The normalization, penalty scale, source metric,
compact abelian gauge group and their relation to the TFPT microscopic
parent remain declared inputs. No oscillator/vertex scaling, nonabelian
gauge dynamics, flavor, continuum limit, complete TOE or RH claim follows.

## Reproduction

Run `checker.py` in the project Python environment, from any directory.
It retains frozen predecessor hashes and runs that predecessor separately.
New exact checks include the real full 3D incidence matrices, the matched
Hodge identity and kernel, integer penalty witnesses, source Gram energy,
Wilson support and cocycle, proper cubic averaging and negative controls.
They do not use finite-clock CCR substitutes or promote finite samples to
the all-volume statements proved above.
