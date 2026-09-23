# An existing edge suffices conditionally; source selectability remains open

12 September 2026. Exact finite-source result, not a physical closure.

## The source actually contains these terms

`seam_state_derivation_probe.py:586-627` constructs B=A_int by writing
individual channel blocks and transporting them around Clock orbits. It
deploys their covariant aggregate, not separately available instruments.
The fifteen antisymmetric matrices E_ab obtained by retaining each existing
off-diagonal channel block obey sum E_ab=B exactly. No new block values or
new interaction type are introduced in this decomposition.

Every E_ab commutes with J, so its quadratic CAR lift preserves total
particle number. In particular none of these terms excites the empty vacuum
on its own. Compiler construction steps do not prove physical sequential
operations; retaining their labels in code does not prove a physical record.

## Exhaustive conditional edge-access census

Start with the six real boundary coordinate vectors. Compute the smallest
linear subspace closed under both D=J+B/8 and one separately available E_ab.
This finite algebraic closure stabilizes in dimension at most sixteen.

| Additional separately available edge | Number of such edges | Real accessible dimension |
| --- | ---: | ---: |
| Boundary 0 to triple 1,2,3 | 3 | 14 |
| Boundary 0 to pair 4,5 | 2 | 12 |
| Within triple 1,2,3 | 3 | 14 |
| Triple 1,2,3 to pair 4,5 | 6 | 16 |
| Within pair 4,5 | 1 | 10 |

Thus any one of the SIX pre-existing triple-to-pair edges would suffice for
full linear access, IF separately operable alongside the original dynamics.
This is not a proof of arbitrary many-body controllability or source-native
measurement. Every Clock-averaged edge preserves the old P/Q split and
cannot improve boundary access, even if such averaged edges are separately
available. The original aggregate has accessible rank ten.

## Stronger analytic result for a modified, fixed Hamiltonian

Separately from the switched-generator census, consider

    B(x)=B+x E_14,  D(x)=J+B(x)/8,  x real.

This CHANGES the source's equal edge weighting; x is not derived. It does
not require switching between two generators once the modified model is
stipulated. In the eight-complex-mode convention define

    h(x)=I+[B(x)[even,odd]+i B(x)[even,even]]/8.

For the eight-column matrix with columns

    e5,e6,e7,h(x)e5,h(x)^2 e5,...,h(x)^5 e5

(zero-based complex indices), exact symbolic calculation gives

    det = -i x^3 p(x)/2^41,
    p(x)=x^4+7x^3+(24+4i)x^2+(32+26i)x+24+36i.

The imaginary part of p is 4x^2+26x+36=2(2x+9)(x+2).
It vanishes at -9/2 and -2; the real part has no common root with it,
as checked by the exact polynomial gcd. Hence p has no real zero.
For EVERY real x != 0 the complex boundary cyclic space has dimension
eight, equivalently sixteen real Majorana directions. The coefficient
convention uses the conjugate/transposed one-body matrix, which has the
same cyclic rank for these real seeds.

The rank-ten obstruction is therefore not stable under this particular
edge-resolving perturbation. However the determinant vanishes cubically
as x tends to zero: exact nonzero rank is NOT uniform measurement
sensitivity, bounded observation time or numerical robustness. No such
operational bound is proved here. Nor is a nonzero x selected by TFPT.

## What this does and does not settle

This improves the constructive target from an arbitrary additional carrier
operator to one of six terms already present in the candidate Hamiltonian.
It does not derive a control handle, a reference, an occupied preparation,
spacetime, or a T1-T8 solution. A permanently selected edge also breaks the
original C6 invariance; a relational implementation would have to derive a
transforming reference and joint coupling instead of quietly imposing it.

The immediate source question is whether the primitive channel grammar
provides an independently operable edge or physical edge record. The reviewed
construction and v898 candidate contract provide an aggregate matrix/state,
not such an instrument. Source generation, operator decomposition and
physical selectability must remain distinct.

## Verification and provenance

`source_edge_access.py`: 44 exact checks in normal and -OO modes, including
the original source hash, reconstruction, all fifteen edges, negative
averaging controls and the symbolic all-real-parameter determinant proof.
Uses the existing reconstruction adapter; the upstream permutation search
is not rerun. This is an algebraic proof/check, not an experimental run.

A first Hermiticity check compared symbolic expression trees and rejected
algebraically identical entries. Systematic debugging reproduced this with
i(-x-1)/8 versus -i(x+1)/8. The corrected test expands the exact polynomial
difference; a deliberately non-Hermitian matrix is explicitly rejected.
No floating tolerance, weakened claim or source change was used.

No source, paper, public status or ledger promotion. No commit or push.
