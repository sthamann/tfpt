# Measured validation: 2026-09-08

Environment: Python 3.14.3, SymPy 1.14.0, NumPy 2.4.2 on the local TFPT
checkout. This is an exact finite algebra/symbol experiment, not a physical
continuum simulation. Timings are observed wall/runner times, not benchmarks.

## New artifact and unchanged predecessor

| Execution | Result | Reported test time |
| --- | --- | --- |
| New bridge, normal Python | 18/18 passed | 1.222 s |
| New bridge, `-OO` | 18/18 passed | 1.486 s |
| Unchanged parent-selection audit, normal | 15/15 passed | 1.033 s |
| Unchanged parent-selection audit, `-OO` | 15/15 passed | 1.030 s |

The new full checker completed with exit zero in 0.941 s. Each mode's test
suite also regenerates the complete result in memory and compares it with
the recorded JSON, including the local checker/test/README hashes. All eight
frozen verification source hashes match. No assertion-removal bypass: the
new checker uses explicit exception guards rather than Python `assert`.

New mathematical coverage: 4,096 cocycle associativity cells, all 256 matrix
products, all 256 signed-sigma product cells, complementary Arf-zero/Arf-one
planes, four nontrivial sigma word phases, Clifford identities in complex
4x4 and independent real 16x16 representations, both metric signatures,
formal Dirac determinant and opposite Weyl blocks, preserved wall linear jet,
eight exact overlap corners, 27 rational non-corner checks, and the inherited
internal hypercharge census. Negative controls fire without editing originals.

Recorded validation SHA-256:

```
a40b338e99cb0bb0e09d63861621d6b228e4ad5afeed7ea0335352ad043d4e0c
```

## Existing foundational modules rerun read-only

These were executed in ordinary Python, up to three concurrently. Their
historical internal checks were **not** independently converted to `-OO`
proofs and are not included in the new suite's 18 tests.

| Existing module | Result | Elapsed | Preserved meaning |
| --- | --- | --- | --- |
| v774 Arf compiler | 46/46 plus pattern gate, exit 0 | 2.226 s | Exact finite compiler; matter interpretation fenced |
| v775 root-class purity | 18/18 plus pattern gate, exit 0 | 0.107 s | ROOTCLASS-MIXED: proposed pure matter dictionary still fails |
| v783 two-qubit Clifford | 32/32 plus pattern gate, exit 0 | 3.935 s | CLIFFORD-PARTIAL(H4), not physical spacetime |
| v975 dimension selector | 16/16, exit 0 | 0.307 s | Conditional dimension selector, not compiler-derived axioms |
| v1027 signed wall | 47/47, exit 0 | 0.366 s | Narrow DET-CAR/fixed-background result and existing vectorlike overlap |
| v14 carrier uniqueness | 8/8, exit 0 | 0.193 s | Conditional carrier rank and SM charge constraints |

No mathematical test failures occurred. These are reproducible computation
and explicit proofs in the notes, not independent peer review or a new
proof-assistant formalization. The broader scalar bulk remains unchanged.
No T1--T8, ledger, paper or website claim was promoted; no commit/push was run.
