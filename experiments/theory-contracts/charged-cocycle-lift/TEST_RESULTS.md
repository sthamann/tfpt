# Measured validation: 2026-09-08

The new charge-sign reconstruction, its symmetry lifts and the full lattice
zero-mode formulas pass their stated checks. **This is not a full TOE result.**

## Reproduction results

| Suite | Normal Python | Python `-OO` |
| --- | --- | --- |
| New charged-cocycle lift | 20/20, 1.487 s | 20/20, 1.479 s |
| Unchanged compiler-Clifford bridge | 18/18, 1.233 s | 18/18, 1.249 s |
| Unchanged parent-selection audit | 15/15, 1.043 s | 15/15, 1.004 s |

Total: **53 tests in each mode**, all runners exit zero. The new checker
and all new assertions about the mathematical result use explicit guards
that are not removed by optimization. Every new test run includes complete
in-memory replay of the validation record and its local source hashes.
The independent exhaustive section search agrees with affine elimination.
No unexpected mathematical or software test failure occurred.

Final validation SHA-256:

```
170bc4f5a63727c8d26265bf87ba5c36a737b8d55de810a7a2ba214dbe2b4ef9
```

## Verified content

- Actual three-root non-descent witness; same compiler label `(0,1,1,0)`,
  opposite cocycle commutator signs. Rephasing cannot remove it.
- The actual unimodular Gram form and the Gaussian kernel give the exact
  eight-bit/four-bit sequence. All 65,536 pairings reproduce the inherited
  compiler form through `beta(x,(1+J)y)`.
- Exactly 64 quadratic-form-preserving linear sections and four sigma
  sections. An independent search covers every four-column candidate after
  its square constraints: `8^4=4096` possibilities.
- For all 64 sections, the deck image is the exact orthogonal complement.
  The four sigma sections give two unordered paired splittings; no section
  respects the quotient's trivial deck action as an isolated factor.
- Every one of 65,536 sign-algebra matrix products, all sixteen columns:
  1,048,576 exact column identities. The cocycle coboundary is also checked
  on all 65,536 pairs, with no floating-point tolerance.
- Explicit coherent deck/family cocycle lifts; their orders are four and
  three and they commute after the recorded character correction. The
  initial 128-word mismatch is an intentional phase-coherence diagnostic,
  not hidden by relabeling or by dropping phases.
- All four operator-level Clifford embeddings and their commuting deck
  partners, using the unchanged earlier frame routine; both Weyl sectors
  remain, each rank eight in the minimal charge-sign representation.
- Exact integer-charge translations and charge/energy Ward identities,
  including both signs of charges of size `10^12`; no charge cutoff. The
  finite sign alias does not preserve the energy or nonzero charge Ward
  identity, as explicitly tested.
- The actual sourced lambda remains weight one with order-four glue.

Six pinned source files are unchanged. The old validation hashes remain
`a40b338e99cb0bb0e09d63861621d6b228e4ad5afeed7ea0335352ad043d4e0c`
and `5825b4581b97d36d6d33bdd51f910264f32e197a5b9b50c2ce407b0c9af3db56`.
The broad verification suite was not rerun this turn; the two directly
relevant predecessor suites were. Proofs are given in README alongside
the computation, not independently peer-reviewed or Lean-formalized.

No microscopic support-preserving field map, adjoint/scaling-limit theorem,
gauge-commuting physical spin, selected 3+1D parent, net-chiral matter,
coupling/state/flavor selection, or nonlinear gravitational completion is
claimed. No T1--T8 marker, original parent, paper, website or ledger changed.
No commit or push was performed.
