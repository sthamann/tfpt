# Clock and electric rotor: complete local phase-lift classification

2026-09-09. NON-RH. Exact result for a declared lift class on the unchanged
two-species compact-U(1) parent in `local-window-round37`. This is not a
no-go against every Clock/rotor embedding, a new interaction, or TOE closure.

## 1. Which proposed bridge is being tested

The previous `clock-interaction-provenance` contract found a genuine quartic
component in the electric double commutator of the existing rotor parent.
That parent and the original sixteen-Majorana Clock are still different
physical constructions. Can their actions be identified merely by giving
the actual matter and rotor operators consistent C6 grades?

Use omega=exp(2pi i/6), with the proposed automorphism

```
alpha(c_Lx)=omega^l_x c_Lx,
alpha(c_Hx)=omega^h_x c_Hx,
alpha(U_uv)=omega^k_uv U_uv,
alpha(E_uv)=E_uv.
```

The vertices are fixed, charges are integers modulo six, and [E,U]=U.
There are no extra U^3 factors, new hoppings, new local hybridization or
additional matter species. Both actual species and all original links
and two-step paths must be retained. Isolated vertices are discussed below.

## 2. Exact classification forced by the original hopping list

For each oriented edge u->v the actual source includes all three nonzero terms

```
a U_uv c_Lv^dagger c_Lu,
eta a U_uv c_Hv^dagger c_Lu,
eta a U_uv c_Lv^dagger c_Hu,
```

and their adjoints, where a=1/12 and eta=1/2. The distinct matter monomials
are linearly independent, so invariance requires exactly

```
k_uv+l_u-l_v=0,
k_uv+l_u-h_v=0,
k_uv+h_u-l_v=0                  (mod 6).
```

Subtracting the first equation from the second and third gives

```
h_u=l_u, h_v=l_v, k_uv=l_v-l_u.
```

Thus on every nonisolated vertex l_x=h_x=:q_x, and on every edge
k_uv=q_v-q_u. Conversely every assignment of site grades q_x gives a
solution. This proves completeness on an arbitrary graph, not just a
small example. The one-edge checker independently enumerates all 6^5
assignments and finds exactly the expected 6^2=36 solutions.

The original two-step low-low terms have coefficient beta a^2, beta=1/4.
For a path u->m->v their oriented link grades sum to
(q_m-q_u)+(q_v-q_m)=q_v-q_u, so these terms and their adjoints are also
invariant. Backtracks are already included in the original onsite degree.
The electric E^2 term and onsite number terms are invariant automatically.
The full square and a three-dimensional periodic torus are tested with
their actual two-step term lists; these lists are not replaced by only
the low-low nearest-neighbor terms.

All closed paths have zero total grade by telescoping, including the
noncontractible cycles of a periodic lattice. These are exact gradients;
there is no hidden discrete Wilson-loop holonomy in this lift class.

## 3. The common symmetry is only gauge on the physical space

The source convention is

```
G_x=N_Lx+N_Hx-1+div E_x,
div E_x=sum_outgoing E - sum_incoming E.
```

Set N_x=N_Lx+N_Hx and theta=2pi/6. The automorphism above is implemented by

```
W=exp[i theta (sum_(u->v)(q_v-q_u) E_uv - sum_x q_x N_x)]
 = exp[-i theta sum_x q_x] exp[-i theta sum_x q_x G_x].
```

The equality is an exact linear polynomial identity in the occupations
and every integer electric flux. The implementation signs follow from
[N,c]=-c and [E,U]=U. The first factor is the fixed background-charge phase.
On G_x=0 the entire action is scalar, and after removing that phase it is
the identity. It therefore provides no additional physical Clock action.
It is not enough to show that a joint transformation commutes with H:
one must also check its action after the Gauss constraint.

The proof is valid for unbounded integer flux; no finite cyclic rotor or
flux cutoff is used. The checker verifies the polynomial identity with
symbolic site charges and fluxes, and separately checks full H matrix
elements at E=0,+/-1,+/-10^9. Physical states reached by repeated exact
full H action have the same scalar phase, whereas kinematic states outside
the physical sector need not. These examples corroborate the identity;
they are not what extends it to all fluxes.

## 4. Why the phase class also covers local internal U(2) mixing

For any retained ambient degree 0<=d_x<=6 the actual onsite one-body block is

```
h_x=diag(beta a^2 d_x, M),
beta a^2 d_x<=1/96 < M=4.
```

Its eigenvalues are distinct. A site-fixed, particle-number-preserving,
rotor-independent U(2) action that preserves this onsite block must
therefore be diagonal in the existing L/H basis. For a C6 action its two
phases are sixth roots of unity. Section 2 then forces the same phase
on both species. A local U(2) basis mixing cannot evade the classification.

This uses the original diagonal onsite term, not an invented off-diagonal
L/H hybridization. The source has local L/H coherence observables and
preparation freedom, but no extra onsite hybridization term is inserted
as a Hamiltonian hypothesis.

## 5. Independent spectral obstruction to the full eight-mode Clock map

The pinned source reconstruction returns the actual sixteen-Majorana
Clock permutation. It preserves complex Majorana pairs; its action on
the eight annihilation modes has cycle lengths (1,1,1,2,3), hence

```
chi_Clock(x)=(x-1)^5 (x+1)(x^2+x+1),
C6 grades=(0,0,0,0,0,2,3,4).
```

Any representation made from four nonisolated L/H cells in the class above
has each character repeated twice. Its characteristic polynomial is a square,
and every character multiplicity is even. The original Clock multiplicities
are instead 5,1,1,1. Therefore no unitary eight-mode intertwiner exists
between the full Clock representation and these four scalar local cells.
This spectral argument is basis-independent: merely changing the eight-mode
basis does not repair it.

The grade list is reconstructed from the original permutation, not assumed
from a target register. The source's current algebra and the separate rotor
Hilbert space are not identified by having the same number of fermion modes.

## 6. Scope, internal review and the next useful test

The three-link proof, Gauss identity, original Clock grades and onsite-U(2)
argument were derived and checked independently in the parallel research
branch, then independently checked against the original source here.
The root implemented the reproducible artifacts and full-term exact tests.
This is internal review, not external peer review or a formal certificate.

Excluded is the declared site-fixed, number-preserving, rotor-independent
internal lift with constant link phases and the full unchanged hopping list.
For an isolated vertex the link proof does not force equal L/H charges;
such a vertex supplies no transport, and adding isolated spectators is not
the four-connected-cell identification tested here. Spatial permutations,
nonlocal transformations, Bogoliubov actions, flux-dependent dressings, more
matter species, or a differently selected parent are not classified.

The result does not remove the previous physical electric interaction.
It says that assigning those local Clock grades is not its missing physical
dictionary. A next candidate must first give an operator that acts nontrivially
on the Gauss-physical algebra, intertwines the complete original Clock action,
and preserves the actual parent Hamiltonian and locality requirements.
An arbitrary newly chosen coupling would be another parent, not this proof.

## 7. Reproduction

`python3 checker.py --output diagnostics.json` records the source pins, exact
Clock polynomial, 36 complete single-edge solutions, all 1296 site-grade
assignments on the square, symbolic all-flux identity and full-H controls.
`python3 -m unittest -v test_checker` and the same command with `-OO` run the
ten separate tests. The combined round transcript is linked from
`../microscopic-fourpoint-limit/TEST_RESULTS.md`.

The frozen upstream source emits a ResourceWarning for its existing unclosed
read handle when Python warnings are enabled. That historical source is not
modified here; the warning is retained in test transcripts, not suppressed
or represented as a new failing mathematics check.
