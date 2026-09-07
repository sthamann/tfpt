# CY seam continuation — Round 10

**Unpromoted mathematical research, 2026-09-06. No T1–T8 gate is closed.**
This follows the proposed rational elliptic/relative Calabi–Yau route rather
than adding an arbitrary compactification. It supplies a concrete local
boundary operator and determines several exact limits of the identification.
It is not an empirical test or a microscopic 3+1D Hamiltonian.

## Results and dependency map

| Piece | Established in this round | Boundary of the result |
| --- | --- | --- |
| [Equivariant bundle](EQUIVARIANT_BOUNDARY.md) | Minimal rank-four pullback-orbit bundle with coherent order-four clock; explicit twisted canonical orientation. | The original single torsion line does not admit the clock. Its cyclic tensor subgroup must enlarge to all sixteen E[4] classes. |
| [Local boundary operator](FLAT_OPERATOR.md) | Positive self-adjoint flat connection Laplacian, explicit domain and complete spectrum; all four character restrictions unitarily equivalent. | The operator and area are chosen. It supplies no chirality, character mass splitting, or actual TFPT operator identification. |
| [Relative determinant](RELATIVE_DETERMINANT.md) | Acyclic boundary gives a quasi-isomorphism and an algebraically trivial relative determinant; explicit surface cohomology theorem. | Absolute bulk determinants need not trivialize; Quillen connection/holonomy do not follow from acyclicity. |
| Orientation and descent | Rank-four determinant has unavoidable character -1; stack bundle exists. | Coarse quotient descent fails at fixed points. Constant character twists cannot fix the rank-one class obstruction or rank-four determinant sign. |

### The retained geometric seed

For `y²+xy+ty=x³+tx²`, the invariants are
`Delta=t⁴(1−16t)`, `c4=16t²−16t+1`, and
`c6=−(8t−1)(8t²+16t−1)`. Minimal fibres are I4, I1, I1*;
the rational elliptic frame is E8(-1), the fibre-root lattice is
D5(-1)+A3(-1), and the Mordell–Weil group is Z4. The section P=(0,0)
has 2P=(-t,0). With D_P=P−O−F, restriction gives

    E8(-1)/(D5(-1)+A3(-1)) ≅ <O_F(P−O)> ≅ Z4.

Roots restrict trivially because their vertical curves are disjoint from a
smooth fibre; D_P lies in the frame and restricts to the exact-order-four
line. An explicit torsion certificate is
`div(x²−y)=div(y²/(x+t))=4P−4O`. The frame quotient of order four is
not the full root discriminant group, which is (Z4)². The fibre/MW
classification agrees with [Kimura, Table 8](https://arxiv.org/html/1710.04984).

The successful affine clocks occur on the j=1728 fibres
`t=−1±3sqrt(2)/4`; `t=1/8` fails the four-branch-point cycle.
The point-marked choices remain distinct. This geometric realization does
not derive a unique geometry or metric from the TFPT axioms. The original
CM clock still has no compatible global lift on this surface.

### What changed since the preceding audit

Previously the equivariant orientation and extra determinant factor were
only identified as obligations. Here the rank-four boundary repair and a
twisted orientation are explicitly constructed. The resulting simplest
local operator has exactly equal spectra in all four clock characters.
Moreover the relative determinant factor can be handled algebraically in
the acyclic case, but it cannot be omitted from an absolute identification.

A sharp bulk-information counterexample uses D_P and 5D_P: their boundary
lines agree, but their surface H1 dimensions are zero and 24. In a family
over P1, the latter produces bulk determinant O(-24), while the boundary
determinant is O. Even algebraic triviality of a determinant line does not
force a flat connection: the Poincare-family counterexample in the proof
has a nonzero Quillen curvature away from its zero-mode locus.

The compact Borcea–Voisin candidate from the original proposal is not used
as an assumed three-family solution. Its separately audited Hodge data
(61,1), Euler number 120 and standard-embedding index magnitude 60 remain
the boundary of that other route, not an input to these constructions.

## Reproduce

Requires Python and SymPy (validated versions are in `validation.json`).
From this directory:

```bash
python check_elliptic.py
python test_equivariant_boundary.py
python check_relative_determinant.py
python flat_orbit_operator.py
```

`check_elliptic.py` repeats the prior audit's exact geometric algebra;
the other files exercise the new consequences. Tests of intersection
arithmetic and finite group matrices do not replace the general geometric
proofs, which invoke the stated Riemann–Roch/duality hypotheses. The
all-frequency isospectral theorem and the operator-domain proof are given
explicitly, not inferred from a finite spectral sample.

Validation retained a point-versus-holonomy convention correction: the
initial phase used the divisor point coordinates as flat holonomies. An
added regression failed on (1,0); the explicit principal polarization
P=(b,-a)/4 now determines T=2P and all affine phases. This changes the
phase implementation, not the proven spectra or character equivalence.
The root derivation and a separate internal mathematical review agree;
this is not external peer review or a formal proof-assistant certificate.

## Next discriminating work

1. Identify the actual TFPT seam algebra/operator with one of these bundle
   constructions, retaining stabilizer representations and the distinction
   between the original cyclic subgroup and its enlarged tensor closure.
2. If a splitting mechanism is proposed, specify additional local
   coefficient fields; block-preserving equivariant operators cannot do it.
3. Specify a common bulk/boundary operator family, including framing and
   analytic metrics, before comparing determinant connections and holonomy.

The separate [local positive auxiliary construction](../local-positive-auxiliary/README.md)
addresses the previous matter/gravity energy completion. No identity between
that dynamical construction and this CY boundary geometry has been proved.
They must not be added together and reported as a shared physical parent.

No ledger, empirical scorecard, main verification registry, paper or website
status is promoted by this research folder.
