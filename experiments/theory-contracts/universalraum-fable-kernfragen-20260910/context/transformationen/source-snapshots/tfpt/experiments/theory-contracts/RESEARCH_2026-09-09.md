# Research consolidation — 9 September 2026

This is the publication map for the post-Round27 archive, including Rounds
28–50 and the subsequent named branches. Written arguments and executable
controls have distinct roles: passing a test is not independent mathematical
review, a proof-assistant certificate or physical TOE closure. **All T1–T8
and `TFPT.TOE.COMPLETE.01` remain open.** No empirical or RH claim is promoted.

Historical `ROUND_STATUS`, validation transcripts and source-pinned files are
preserved byte-for-byte. Their original “local”, “uncommitted” and publication
labels describe their creation time, not the publication state after this
integration. This file supersedes them only as an archive/publication index.

## The new results, and exactly which source they concern

| Source | Result now available | Remaining bridge |
|---|---|---|
| Original complex QWZ strip, width 8, mass 1, sector r=1, actual filled sea | Local smooth charged CAR fields and both adjoints converge, with integer charge and finite-energy generator control. Top-edge sector minimum is q²/2−q/4. | Half-charge inter-sector field; eight selected channels, cocycle and family/Clock marking; not the compiler's 16 real Majoranas. |
| Same strip and filled sea | Alternating neutral four-point functions converge including collisions in L¹; auxiliary-window grid estimate O(N^−3/4 log³N), interpolation O(N^−5/8). | Pair-Gram positivity is not OS positivity; no automatic all-word collision theorem. |
| Declared compact-U(1) rotor/CAR parent, a=1/12, η=1/2, β=1/4, κ=1/100, M=4 | Full all-time quasi-local dynamics; periodic neutral ground-state cluster representations with nonnegative physical generator; quantitative nonzero Wilson-loop excitation weight. | Dynamics is not point-norm continuous on the full bounded algebra. State uniqueness, charged-sector positive energy, compiler selection and continuum remain open. |
| Actual compiler/Clock matrices and actual rotor hoppings, compared without identifying them | Site-fixed rotor-independent internal Clock identification is excluded; compiler scalar quadratic dynamics alone supplies no connected quartic interaction. | A source-derived spatial/flux-dressed or other allowed correspondence, not an invented internal symmetry. |
| Actual E8 lattice and marked finite modules | Minimal eight-bit charge-sign refinement, charge-carry cocycle, half-charge target s=(1/2)^8 of weight 1. | This target representation is not yet the microscopic seam field. |

### Source-field advance

The new [charged CAR proof](microscopic-charged-car-limit/README.md) uses
`H_N = dΓ(N h_N/(2π)) − Tr(P_N N h_N/(2π))`, which is nonnegative on the
whole finite source Fock space. Top-row fields are genuinely local sampled
operators. Momentum-polarized comparison maps intertwine the actual occupied
projector exactly; their second quantizations include particles **and holes**.
The filled sea does not introduce a spurious factor 8N in the excitation
generator error. Smooth Fourier alias tails are controlled in ℓ¹.

The current dependency runner has 131 tests in each of ordinary and optimized
Python across 11 isolated suites. Its saved `verification.json` is the original
timestamped record; publication reruns use separate output files. N=32–256
samples check the predicted errors but are not proofs of the infinite limit.

### Dynamics and physical-state advance

The [all-electric majorant](all-electric-majorant/README.md) sums arbitrary
electric insertions with `ρ(T)=77T/96+53T²/14400`, `ρ(1)<1`.
The separate [all-observable argument](observable-dynamics/README.md) includes
every hopping footprint and establishes composition at arbitrary real times.
The proper maximal point-norm-continuous subalgebra must not be replaced by
the full bounded algebra; a neutral Wilson loop itself detects the difference.

[Neutral ground states](neutral-ground-state/README.md) and
[loop-response bounds](ground-state-loop-response/README.md) use the original
uncut electric spectrum. The improved outgoing-electric moment bound is
`C*=1706590130/3033378777 ≈ 0.562604`. A Wilson loop has first spectral moment
1/50 and positive-energy weight at least 0.571383. The positive spectral
infimum is **at most** 0.035003 in the declared model's units, not bounded
away from zero. Neither this number nor M=4 is a measured particle mass.
The old all-low/zero-flux preparation is not a ground state.

## Complete branch map

Paths below are relative to this directory; each branch retains its proof,
checker, tests and available original validation records.

| Development | Archived branches |
|---|---|
| Finite charge and common-parent routing | `poisson-charge-round28`, `coupled-trace-round29`, `toe-bridge-round30` |
| Locality, virtual response and memory | `projector-locality-round31`, `virtual-readout-round32`, `local-flux-dynamics-round33`, `memory-closure-round34`, `auxiliary-dynamics-round35`, `coherent-family-round36`, `local-window-round37` |
| Source and matter hierarchy | `local-source-round38`, `second-source-round39`, `matter-hierarchy-round40`, `electric-source-round41`, `electric-propagation-round42` |
| Higher-order resummation and direct defect | `matter-resummation-round43`, `cubic-resummation-round44`, `higher-electric-round45`, `word-resummation-round46`, `bulk-word-round47`, `direct-defect-round48`, `sixth-source-round49`, `second-matter-round50` |
| Completion of the lattice control chain | `third-electric-cubic`, `seventh-frontier-edge`, `seventh-frontier-bound`, `all-electric-majorant`, `observable-dynamics`, `neutral-ground-state`, `ground-state-loop-response`, `parent-selection-audit`, `plaquette-gap-certificate` |
| Compiler, marking and origin | `compiler-clifford-bridge`, `compiler-involution-types`, `carrier-module-conjugation`, `clock-marking-audit`, `clock-bilinear-response`, `clock-neutral-access`, `clock-interaction-provenance`, `clock-rotor-joint-charge`, `origin-composition-audit` |
| Charge and inter-sector target | `charged-cocycle-lift`, `half-twist-grade-carry`, `gaussian-vacuum-filter` |
| Neutral-to-charged microscopic chain | `neutral-pair-composition`, `neutral-current-limit`, `microscopic-neutral-limit`, `source-current-symbol-match`, `microscopic-energy-linearization`, `current-truncation-bridge`, `history-reference-transport`, `polarization-history-bridge`, `current-fourpoint-limit`, `microscopic-fourpoint-limit`, `microscopic-charged-car-limit` |

Adjacent investigations are also included, without conflating their scope:

- [Double-cover/Clock audit](../double-cover-rh-audit-2026-09-08/): exact
  involution, readout and finite algebra checks. A sheet involution does not
  imply arithmetic positivity. The original source interpretation is still
  a candidate; finite-temperature readout does not automatically survive a
  zero-temperature plateau.
- [Inter-sheet dynamics audit](../inter-sheet-dynamics-audit-2026-09-08/):
  its derivations and source records remain a separate research branch.
- [Prime-event investigation](../pi-prime-event-log-2026-09-08/README.md):
  tested digit rules show no robust extra prime signal. Overlap explains an
  apparent correlation. The recorded spectral factoring comparison does
  not establish a speed advantage. Timing and large-data results are archived
  measurements, not claimed to have been rerun in the publication pass.

## Current T1–T8 acceptance map

| Gate | Concrete remaining obligation |
|---|---|
| T1 | Derive P1/P2, dimensional and compiler choices; distinguish elegance from selection. |
| T2 | Construct the actual half-charged, marked E8 seam algebra and its scaling limit, including energy, both adjoints and charge/cocycle transport. |
| T3 | Derive **one** TFPT-selected local/quasi-local unitary 3+1D parent shared by all sectors. |
| T4 | Construct its chiral SM gauge/Weyl measure, anomalies/index and uniform mirror decoupling. |
| T5 | Prove the interacting physical continuum, Lorentz behavior, confinement/clustering and scattering where required. |
| T6 | Derive all three gauge couplings and complete neutrino texture/scale internally. |
| T7 | Obtain massless quantum spin two with two helicities and universal coupling from that same parent. |
| T8 | Select the physical initial state and derive one source functional for all readouts. |

The frozen scalar-symbol prototype depends on only `x(k)=Σcos(k_i)/6` and
has Pauli-Jacobian rank at most one; scalar retuning cannot create a Weyl
node. This is a useful restriction on that prototype, not a no-go theorem
for all interacting or matrix-valued parents. The older E8 logarithmic
cascade telescopes and retains a separate scale input; it does not by itself
derive a prime-spectrum dynamics.

## Next experiment after publication

Use the newly constructed charged source Fock space to test a **renormalized
half-charge inter-sector field**. A sharp unrenormalized twist fails the
Hilbert–Schmidt implementability sum, so repeating finite sharp-string
numerics is not the missing proof. The acceptance test is a common
inter-sector energy domain, both adjoints, source-derived normalization,
nonzero smeared limits and the correct charge/cocycle carry. Eight independent
copies or a formal charge register are targets, not evidence of their
microscopic identification. See the contracts paper's 9 September section.

## Reproduction

From the repository root, after installing `requirements.txt`:

```sh
python -B experiments/theory-contracts/microscopic-charged-car-limit/run_verification.py --output /tmp/tfpt-charged-rerun.json
python -B experiments/theory-contracts/run_consolidation_20260909.py --output /tmp/tfpt-consolidation-rerun.json
python -B verification/test_make_manifest.py
python -B verification/audit_sync.py
python -B verification/make_manifest.py --check
```

The consolidation runner freezes 61 newly shipped test modules and runs their
bounded tests in separate processes in both modes. Three explicitly listed
full production replays (Rounds 47, 49 and 50) are not part of that tier;
their original tests and records remain intact. Round47 alone re-enumerates
95,599,440 native extensions, and a five-minute publication run timed out
inside that calculation, not on an asserted identity. To request those
large replays too, add `--include-large-replays --timeout 7200 --workers 1`.
The runner reports exclusions explicitly and does not overwrite old records.
It is not the full 1028-module core suite, a new large digit-data measurement,
independent review or a proof that T1–T8 are solved.
