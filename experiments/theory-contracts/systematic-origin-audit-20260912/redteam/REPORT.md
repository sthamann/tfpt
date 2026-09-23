# Independent red-team: coherent compiler record and dynamics selection

12 September 2026. NON-RH. No physical gate or publication status changed.

## Outcome

The audited finite claims are correct in the explicitly chosen complex
four-dimensional irreducible representation. An independent reconstruction
found no sign or tensor-order defect in the encoding, constraint projector,
record-only recovery, adjoint right-action, all-logical-H freedom, assigned
family-cycle implementation or positive-logarithm counterexample.

Two extra scope restrictions are established here:

1. Invariance under the family cycle alone leaves an eight-real-dimensional
   Hermitian commutant, hence seven Hamiltonian parameters after scalar energy
   shifts. This is distinct from invariance under all four logical generators,
   which leaves only scalars.
2. Uniqueness of the unitary implementing the assigned generator action is an
   irreducible-representation statement. It does not extend to an enlarged
   physical parent: `w tensor I2` and `w tensor Z` implement the same action on
   every `gi tensor I2` but are not related by a scalar phase.

Neither restriction refutes a correctly scoped statement in the audited notes.
They prevent plausible but invalid next inferences.

## Independence and reproducibility

`independent_check.py` imports no audited implementation or helper.
It transcribes the four source matrices, reconstructs left and right
multiplication using Hilbert-Schmidt projection, constructs the decoder
entrywise, and uses the standard two-qubit Hermitian basis for commutant ranks.
Real and imaginary equations are split explicitly for real parameter counts.
The output records SHA256 hashes of the four directly inspected source files.

Two deliberately defective alternatives are rejected: omission of decoder
complex conjugation, and omission of the adjoint in right-action reconstruction.
The successful checker is a finite certificate, not a physical simulation.

Run from repository root:

```sh
/opt/homebrew/bin/python3 -B experiments/theory-contracts/systematic-origin-audit-20260912/redteam/independent_check.py
/opt/homebrew/bin/python3 -B -OO experiments/theory-contracts/systematic-origin-audit-20260912/redteam/independent_check.py
```

## Why recovery is generic, not yet a universal physical object

For any orthogonal unitary matrix basis of `Md(C)`,

    W psi = (1/d) sum_v |v> tensor Uv psi,
    F[(a,b),v] = conjugate(Uv[a,b])/sqrt(d),

operator-basis completeness gives

    (F tensor I) W psi
      = (1/sqrt(d)) sum_a |a> tensor |psi> tensor |a>.

Thus the recovered logical state is already a tensor factor after a register
basis change, while the other two factors form a fixed Bell pair. There is no
spatial locality, area law or physical access map in this identity. Dimension
16 is conditionally minimal for a pure encoding of a four-dimensional input
whose erased four-dimensional marginal is completely depolarizing: that
marginal and an external reference form a rank-16 state requiring a purifier
of dimension at least 16. Dropping the full-rank erased marginal drops this
lower bound; a fixed pure erased factor needs only a dimension-four register.

## Why the source constraints do not select a Hamiltonian

After the explicit register transform, the four signed constraints act on the
first register factor and the erased system, but not the logical factor.
For every Hermitian `h` the lift

    hR = F* (I4 tensor h) F

preserves all four constraints and implements `h` on the code. Consequently
all 16 real Hermitian directions, or 15 modulo scalars, survive. The explicit
positive isospectral pair in the audited work really produces return
probabilities 1 and 0 for the same input and same readout at the same assigned
time. Spectral agreement cannot replace a marked dynamical intertwiner.

If the ordered automorphism `g1->g2->g3->g1, g4->g4` is assigned, its
irreducible implementer `w=(I+g1g2+g2g3+g3g1)/2` is fixed up to phase:
two implementations differ by an operator commuting with all of `M4(C)`.
But its two eigenspaces each have dimension two. A Hermitian matrix commuting
with `w` therefore consists of arbitrary Hermitian 2x2 blocks, dimension
`4+4=8`. Fixed symmetry, assigned update, and selected autonomous generator
are three different requirements. Two positive logarithms already exhibit
different half-step predictions for identical integer steps.

## Source and physical acceptance audit

Inspected originals:

- `verification/v774_arf_spinor_compiler.py`: finite F2 quotient and selected
  quadratic refinement; its own semantic fence rejects automatic code-to-matter
  interpretation and distinguishes the family-bit and carrier-slot registers.
- `experiments/theory-contracts/compiler-clifford-bridge/checker.py`: explicitly
  constructs both Lorentz and equally equivariant Euclidean Clifford frames.
  Its momentum arguments are formal inputs; it does not derive spacetime
  derivatives or physical signature.
- `tfpt_research_contracts.tex`, named `TFPT.TOE.COMPLETE.01` section: physical
  completeness is the AND of T1–T8; validation additionally requires independent
  holdouts. Subcontract harnesses reusing labels T1/T2 must not be confused with
  these top-level gates.
- `experiments/theory-contracts/RESEARCH_2026-09-09.md`, acceptance map and
  half-charge source obligation; `docs/OPEN_PROBLEMS.md`, September 12 update.

| Gate | What the coherent-code result does not supply |
| --- | --- |
| T1 | Source selection of P1/P2, physical register or dimension/signature. |
| T2 | Actual renormalized half-charge inter-sector fields, common energy domain, both adjoints, marked E8 seam scaling limit. |
| T3 | Selected local/quasi-local 3+1D parent, spatial interactions, actual time update. |
| T4 | Chiral SM measure, anomaly/index realization, uniform mirror decoupling. |
| T5 | Interacting continuum, Lorentz behavior, confinement/clustering/scattering. |
| T6 | Source-derived couplings and complete neutrino texture/scale. |
| T7 | Collective quantum massless spin two and universal coupling from that parent. |
| T8 | Unique physical preparation and one source functional for all readouts. |

No physical acceptance gate closes. This is not a general impossibility theorem
for TFPT; it identifies exactly what this finite construction establishes.

## Strongest next shared-parent acceptance condition

Require a **single marked source realization**, not another unmarked matrix:

    (source states, source algebra, update, state, access, refinement maps).

The same realization must carry the signed compiler action and any proposed
charged operators. Its maps to logical and seam sectors must preserve products,
adjoints, the chosen state, actual evolution and specified accessible readouts.
For a continuum claim these requirements need one compatible refinement family,
not separately successful parents for each sector. Gauge/basis transformations
must carry preparations and observables too; otherwise they change predictions.

First finite acceptance: derive the physical register and constraint coupling
from an existing source, then demonstrate one source-prepared state and one
source-accessible joint observable whose dynamics agree across the proposed
intertwiners. Parameter freedom must be resolved by source premises or admitted
as genuine freedom. Do not optimize an invented Hamiltonian and call that origin.

A particularly sharp compatibility check follows if the same finite cycle is
claimed to carry persistent half-charge: on a common invariant domain,
`[Q,w]=w/2` implies `[Q,w^3]=3w^3/2`, incompatible with `w^3=-I`.
An infinite charge-shift factor can avoid that finite-order obstruction, but
adjoining it is a new realization obligation, not a consequence of code recovery.

## Verification receipt

Normal and `-OO` runs both pass and were compared byte-for-byte with identical
output. Both sign/conjugation mutation controls reject the defective variants.
No foreign files are edited. No paper, ledger, website, commit,
push or cloud export is included in this isolated review.
