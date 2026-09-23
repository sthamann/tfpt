# Common-engine threeway: exact statements and their boundaries

## A. Same-parent electric interaction on the physical square

Use the unmodified Round37 parameters
`a=1/12, eta=1/2, beta=1/4, kappa=1/100, M=4` and its actual ordered graph

```
0 ----> 2
|       |
v       v
1 ----> 3
```

The native edge order is `(0,2),(0,1),(1,3),(2,3)`. Each vertex has low
and high modes. All original hopping and two-step terms are retained;
onsite backtrack degree is six. Omitted exterior hopping is a declared
finite patch, not a controlled spatial approximation to the infinite bulk
for this four-site calculation. No magnetic plaquette potential is added.

Let `q_x=n_Lx+n_Hx-1`, and let B be the incidence matrix with +1 at the
source of an oriented edge. The physical constraint is `B E=-q`.
Summing it forces total occupation four. There are eight complex modes,
but neither their count nor their finite CAR algebra identifies them
with eight chiral continuum channels or the source Clock representation.

### A1. Exact integer parametrization and Hodge energy

Put `q3=-q0-q1-q2` and choose the integer coordinate `w=E3`. Every physical
integer flux, without a cutoff, is uniquely

```
E=(q2+w, -q0-q2-w, -q0-q1-q2-w, w),   w in Z.
```

The Laplacian `L=B B^T` has the exact pseudoinverse

```
Lplus = (1/16) [[ 5,-1,-1,-3],
               [-1, 5,-3,-1],
               [-1,-3, 5,-1],
               [-3,-1,-1, 5]].
```

For `z=(1,-1,-1,1)`, `B z=0`, `z.z=4`. Orthogonal projection gives

```
E = -B^T Lplus q + z lambda,
lambda = w + q0/2 + q1/4 + 3 q2/4,
H_E = (kappa/2) [q^T Lplus q + 4 lambda^2].
```

Indeed `B(-B^T Lplus q)=-q` on the neutral subspace, its inner product
with z vanishes, and the displayed flux parametrization has exactly the
stated projection onto z. Squaring proves the identity for all charges
and all integer w. The program additionally verifies 432 integer states
at flux cutoff three. This finite enumeration is corroboration of the
symbolic identity, not its extension argument.

**Important:** lambda is generally in a charge-dependent shifted lattice,
not an independent real coordinate. Dropping its charge dependence would
give the wrong electric energy. For `q=(1,-1,0,0), w=0`, the energy is
`kappa/2`, whereas the longitudinal-only expression is `3 kappa/8`.

### A2. A nonadditive energy and a same-hop witness

For `qA=(1,-1,0,0)`, `qB=(0,0,1,-1)` at fixed w=0,

```
H_E(qA+qB,0)-H_E(qA,0)-H_E(qB,0)+H_E(0,0) = kappa = 1/100.
```

These are allowed occupation charges. Thus the physical electric energy
has a genuine mixed charge contribution. It is not a quartic term
invented by squaring the old single-particle Majorana Hamiltonian.

A direct kinetic comparison keeps the native `U_01 c_L1^* c_L0` term.
Both source masks 45 and 101 allow it, with coefficient +1/12. The first
has q=0, E=0. The second has `q=qB`, `E=(1,-1,-1,0)`, with unchanged
occupations at sites 0 and 1. The hop shifts E1 by +1 and preserves all
Gauss constraints. Its diagonal energy change is respectively
`kappa/2` and `-kappa/2`. Original mass and onsite terms cancel in this
comparison because a low mode moves between equal-degree sites.
Consequently the disjoint spectator dipole changes the cost of the same
transport by `-kappa`, without changing its amplitude.

This is the standard electric mechanism instantiated on the actual
declared parent, not a newly discovered universal force law. In reduced
coordinates its charge kernel is spatially extended; the unreduced
Hamiltonian still consists of local terms. No instantaneous signalling
or continuum Coulomb phase is inferred.

### A3. Evolution and approximation boundaries

On a finite spatial graph the electric operator is diagonal and
self-adjoint on its natural square-summability domain; all matter and
unitary rotor hoppings are bounded. Bounded perturbation therefore gives
a self-adjoint total Hamiltonian. The invariant Gauss sector is retained.
Flux truncation gives `P_K H P_K`, not a cyclic rotor: moves leaving the
cutoff are omitted and never wrap to the other endpoint.

The calculation constructs every retained matrix entry from original
`apply_parent` calls, including its CAR signs. It evolves the full neutral
state using a matrix exponential. At K=10 there are 1,412 states. Dense
Hermitian diagonalization at K=2 supplies an algorithmically independent
numerical comparison. Both are floating-point calculations, not an
interval-arithmetic proof of every digit.

The inherited `flux_error(4,K,t)` bounds norm-one bounded readout error
between the finite-flux and uncut-flux evolution at this fixed spatial
patch and initially zero flux. Its argument depends on bounds for
flux-changing hoppings and commutation of the diagonal evolution with
the cutoff. Therefore the same estimate applies when only kappa or M
is varied here. It does not certify an infinite spatial-volume limit,
unbounded electric-energy readouts, or errors from rounding the numerical
matrix exponential. Conserved matrix energy is checked separately.

## B. Reverse charge construction and the operator entry point

Let `D8={d in Z^8: sum_i d_i even}`, `s=(1/2)^8`. The inherited source
target basis generates precisely `D8 union (D8+s)`. One direct proof is
inclusion of every basis vector in this union, together with determinant
one for the physical Gram matrix: D8 has covolume two and adjoining s
halves it. The same-covolume inclusion is equality. The root-shell
enumeration independently checks 112 vectors `+/-e_i +/-e_j` and 128
half-sign vectors with even minus parity against the existing source.

With a sector bit b, represent a charge as `d+b*s`. Then

```
(d,b) * (e,c) = (d+e+2bc*s, b xor c).
```

The carry identity follows from `b+c=(b xor c)+2bc`. Associativity follows
from integer charge addition; equivalently the bit carry satisfies its
2-cocycle identity. Twice a half transfer is the nonzero integer vector
2s. Replacing this rule with a cyclic flip loses physical charge.

In d co-propagating complex chiral channels with the common standard
quadratic normalization, the half-vector has weight `d/8`. Thus eight
complex (sixteen real) channels are minimal for integral weight in this
specified class. Integral weight alone is not the proof of full field
locality, nor does the dimension count select the microscopic channels.

The external construction is identified in README, with its prerequisites
and dimensional boundary. Our independently checked algebraic transfer
template is conditional: assume an automorphism sigma and unitary u with
`sigma^2=Ad(u)` and `sigma(u)=u`. In a suitable representation put

```
pi(a)=diag(a,sigma(a)),    S=[[0,1],[u,0]].
```

Direct multiplication proves `S pi(a)=pi(sigma(a)) S`, `S^2=pi(u)` and
unitarity. The supplied finite example checks all nine matrix units for
an inner sigma on M3(C). It is a consistency and wrong-flip control, not
a chiral conformal-net representation, locality theorem, or nontrivial QCA.

Source-generated smooth twists, both adjoints, a common energy domain,
interval locality, the parity extension and a suitable inverse algebra
are still needed before the continuum construction can be imported.
Boundary algebra equivalence does not fix a unique microscopic Hamiltonian.

## C. Robustness exposes a specific missing dynamical condition

For the declared positive diagonal zero-mode energy family

```
h_v(q) = (1/2) sum_i v_i q_i^2,
```

the D8 root energies are `(v_i+v_j)/2`. Equality for every pair implies
`v_j=v_k`: choose i different from j,k and subtract the two equations.
All velocities must therefore be equal. The half-root energy is then
the same. Seven independent equal-energy constraints leave one common
positive scale. Unequal v do not change the lattice, but split its
zero-mode energies. In the anisotropic case these numbers are not being
identified with conformal weights under a single common Virasoro generator.

Now retain the **actual** J and sigma maps from the pinned lattice source.
J rotates four coordinate pairs; sigma cycles the first three pairs and
fixes the last. Invariance of a diagonal metric forces

```
v0=v1=v2=v3=v4=v5=a,   v6=v7=b.
```

These are six independent constraints. The positive counterexample
`a=1, b=11/10` preserves both maps, the full charge lattice and its carry.
Its root energies are `1, 41/40, 21/20, 11/10`. Hence those source-target
symmetries alone do not impose the additional `a=b` condition. This is
an exact counterexample inside the declared diagonal family, not a
classification of all energies or a counterexample to all TFPT premises.

There is a precise connection to the half-twist task: its energy in this
family is `(3a+b)/4`, whereas an integer root within the first six
coordinates has energy a. Requiring these to be same-energy members of
one source-derived current multiplet would impose `(b-a)/4=0`. This one
conditional equality fixes the remaining ratio in this diagonal family.
Merely constructing an abstract charge shift does not prove the premise.

This pinpoints a useful next requirement: source dynamics must protect
or produce the relative-velocity equality, rather than silently assigning
it. Finite cutoff convergence and small coefficient sensitivity in the
rotor square do not establish that condition or RG universality.

## D. What would join these results

The plaquette supplies physical integer charges and interacting transport
in one declared model. The reverse construction specifies a compatible
E8 target charge extension. No state-, operator-, energy- and Clock-
preserving intertwiner between the two is constructed here. A compact
integer rotor also does not automatically provide the missing half-sector
field. All TOE gates remain open; this work provides a concrete interaction
test and sharper conditions for an attempted common-source construction.
