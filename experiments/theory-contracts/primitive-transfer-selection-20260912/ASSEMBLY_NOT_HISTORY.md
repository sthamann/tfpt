# The compiler's matrix-enumeration loop is not a physical event history

2026-09-12. NON-RH; source reading and exact finite controls. No change to
the original source, its physical status, or the T1–T8 ledger.

## 1. What the inspected implementation actually specifies

Pinned source: `experiments/tfpt-discovery/seam_state_derivation_probe.py`, SHA
`5e54c416be72a125a8ce6e235b4300f9f9c2344b3ada796d2dc4c7e2ea01482b`.
At lines 448–469, `edge_orbits` enumerates unordered channel edges under a
permutation. At lines 599–615, `put_ordered` ASSIGNS signed matrix entries;
the outer loop enumerates symmetry orbits and the inner loop writes six
images. At lines 633–642, the resulting matrix is combined into one candidate
generator and a Fermi occupation function is evaluated spectrally.

This is an assembly of a static candidate, not a specified temporal sequence
of pulses. Its parameter t is a mixing coefficient in that construction,
not an elapsed physical time. Random pairings elsewhere in that program
are explicitly negative controls on reflection choices, not an event sampler.
Targeted corroborating readings: `seam_mixing_normalization_probe.py`,
lines 564–580 and 712, and `kms_schur_mixing_probe.py`, lines 610–628.
These readings do not certify that no other file in the entire TFPT project
could contain an event law. Nor is this a full rerun of the upstream compiler
census selecting the deployed permutation.

## 2. Why reading program iteration as physical time fails here

The five orbit lengths are 3,2,3,6,1. The source performs six writes for each
orbit: 30 block-write records for 15 distinct channel edges. Multiplicities:

| Writes per distinct edge | Number of edges |
| --- | ---: |
| 1 | 6 |
| 2 | 6 |
| 3 | 2 |
| 6 | 1 |

Every overlapping assignment has the same value. Therefore the order of all
writes is immaterial, not only in the sampled cases. The checker verifies
this coordinate agreement, all 120 permutations of the five orbit groups,
and reversal of the whole record list. Every assembly reproduces the pinned B.

If assignment is reinterpreted as adding one event contribution on each visit,
the resulting entries instead acquire ratios 1,2,3,6 relative to B. No common
normalization removes these relative differences. The repeated visits are a
feature of the enumeration procedure, not source-derived event frequencies.
For actual finite pulses, ordering introduces a further noncommutativity.

## 3. Same spectrum, maximally different marked answers

As an explicitly ADDITIONAL model, take the Hermitian E14 generator K used
in previous reports and L=O^2 K O^(-2). Both satisfy K^3=K and L^3=L. Define

    U=exp(-i pi K/2)=I-K^2-iK,
    V=exp(-i pi L/2)=I-L^2-iL.

The two histories are A=VU (U first) and B=UV (V first). They differ, but

    B=U A U†.

They therefore have exactly the same spectrum and characteristic polynomial.
Both identities are checked. With the SAME input complex coordinate ket |1>
and output projector |0><0| (zero-based indexing in the eight-mode source),

    |<0| A |1>|^2 = 0,
    |<0| B |1>|^2 = 1.

This is a carrier-coordinate witness, NOT a literal original-boundary
measurement. Its preparation, pulse implementation, finite angle and measurement
access have not been derived from TFPT. The witness was found by an exhaustive
scan of coordinate pairs during this audit; it is not a blind prediction.

There is no contradiction with unitary equivalence: transforming both the
state and observable together with the operator preserves all predictions.
Here those physical markings are held FIXED. A spectral shadow forgets their
relative placement. This distinction is exactly what a source-preserving
bridge must retain; counting spectra cannot replace it.

## 4. Consequence for the simplicity search

The source currently supplies a composed candidate matrix and symmetries.
It does not supply a physical pulse law via the order of its assignment loop.
The earlier ensemble model remains an additional hypothesis; no hidden
stochastic dynamics has been recovered merely by reading that loop as time.

A sharper elementary test for a proposed universal object is now available:
it must retain the joint relation between operation, preparation, readout and
composition. If it maps both A and B to their common spectrum and cannot
retain their fixed markings, it cannot predict the two probabilities above.
That rejects the proposed DESCRIPTION as insufficient under this access
contract, not the physical existence of either process.

The next source question is not "which event order looks best?" but whether
the original compiler provides a physical order and clock, or only an
equivalence class of algebraic constructions. If it provides only the latter,
study what can be derived from that actual contract; do not assign physical
significance to incidental implementation order.

## Verification

`assembly_not_history.py`: 371 exact checks in normal and -OO modes;
byte-identical JSON outputs. Many are small repeated-write consistency
checks; this count is not 371 independent physical findings. The source pin,
matrix reconstruction, multiplicities, permutation controls and same-spectrum
probability witness are checked. No paper, website, iCloud export, commit or
push was performed for this audit.
