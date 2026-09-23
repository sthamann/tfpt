# One mixed field seed removes the finite linear-access gap, conditionally

2026-09-12. NON-RH. No Hamiltonian change, no physical access postulate promoted.

## Exact question and result

Keep the pinned sixteen-real-Majorana source at D=J+B/8. Its boundary-generated
coefficient subspace is im P of dimension ten, P=(1/6)sum O^j.
For an explicitly ADDED field seed v, define

    R(v)=im P + span_R{v,Dv,...,D^15 v}.

Cayley-Hamilton makes this the entire D-invariant linear span, not a
finite-time approximation. Analyticity of exp(sD) implies that it also equals
the span of all evolved seed coefficient vectors together with im P.
The sign convention for forward versus backward field evolution does not
change this span. This is linear field observability/algebraic generation,
not automatic quantum-state controllability or a implemented measurement.

The source coordinates 0..5 belong to the three-pair carrier block,
6..9 to the two-pair block, and 10..15 to the original boundary.
The exhaustive finite classification is:

| Additional seed(s) | Dimension including original boundary span |
| --- | --- |
| none / any further boundary coordinate | 10 |
| one coordinate from 0..5 | 14 |
| one coordinate from 6..9 | 12 |
| two coordinates both in 0..5 | 14 |
| two coordinates both in 6..9 | 12 |
| one coordinate from each carrier block | 16 |
| one mixed vector e_0+e_6 | 16 |
| clock-averaged vector P(e_0+e_6) | 10 |

All ten single-coordinate cases and all 45 coordinate pairs are checked with
exact rational matrices. Among coordinate-axis access additions, two are
necessary and sufficient; among unrestricted vector seeds, one suffices.
There are 24 successful coordinate pairs. The mixed seed has no new dynamical
parameter. Its normalization by sqrt(2) would not change its span.

## Why this differs from a boundary-only protocol

The new vector is not in the original boundary algebra; it has components in
the previously hidden sectors. BOUNDARY_PROTOCOL_LIMIT.md is unchanged.
No inference that a boundary instrument can generate this new vector is made.
Conversely the result shows that a new Hamiltonian term is not mathematically
necessary to remove this LINEAR access gap, if the larger field readout is
independently justified. The measured frequencies remain those of the old D.

The gamma(v) field is fermion-parity odd. Its existence in the full CAR
algebra does not make it an allowed standalone physical observable. A
parity-respecting apparatus/reference, an even observable realization, or a
source theorem allowing this access is still needed. Products of the generated
linear fields span the full CAR algebra mathematically, but this is not proof
of a source-native preparation/control/tomography protocol.
In particular the old vacuum-null slow neutral response is not repaired merely
by proving that the corresponding operators belong to a generated algebra.

## Symmetry distinction

P v is the arithmetic average of the FIELD COEFFICIENT over the clock orbit.
It is invariant and loses the nontrivial-grade components that open access.
This does not prove that every symmetric physical experiment is blind.
A covariant multiplet with retained outcomes, a relational reference, or a
randomized instrument is not the same thing as replacing a field by its
average. The source must decide whether the clock is a physical symmetry or
a redundancy requiring invariant observables, and which reference is allowed.

## Provenance and reproduction

minimal_carrier_access.py uses the reviewed source_matrices() helper extracted
from our boundary_access.py. That helper checks the original source hash and
rebuilds the documented deployed permutation's blocks with the original pure
orbit helpers. The upstream permutation derivation is not rerun.
The boundary helper's refactoring preserves its existing nine-check output.

58 exact checks pass normally and under -OO. These include a check-count
guard; they are not 58 independent theorems. There is no float rank threshold,
modified physical source, paper/ledger promotion, T1--T8 closure or RH claim.

Classical linear observability background:
https://ee263.stanford.edu/lectures/observ.pdf . The explicit matrix ranks
above concern this source and are independently calculated here.

Next gate: inspect the original carrier observable/constraint and reference
contract for an allowed cross-block readout. Do not add it just because it
passes the algebraic test; equally, do not assume all physical readouts must
be individually clock-invariant without a source justification.
