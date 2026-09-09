# Verification — 2026-09-08

Local research on HEAD b803b7e5, preserving all pre-existing changes.
No commit/push, paper/site changes or completion-marker promotion.

| Contract | Normal | Python -OO |
| --- | ---: | ---: |
| polarization-history-bridge | 14 pass | 14 pass |
| compiler-involution-types, including new clock census | 12 pass | 12 pass |
| neutral-current-limit | 13 pass | 13 pass |
| carrier-module-conjugation | 9 pass | 9 pass |
| origin-composition-audit | 10 pass | 10 pass |
| neutral-pair-composition | 13 pass | 13 pass |
| compiler-clifford-bridge | 18 pass | 18 pass |
| charged-cocycle-lift | 20 pass | 20 pass |
| half-twist-grade-carry | 23 pass | 23 pass |
| gaussian-vacuum-filter | 21 pass | 21 pass |
| Total per mode | **153 pass** | **153 pass** |

All ten suites were rerun this round, using python3 [-OO] -m unittest
discover -s experiments/theory-contracts/<contract> -p test_checker.py.
The three additional clock tests and all nine involution tests were then
run together using -p 'test_*.py', independently in both modes. The clock
census checks the full 120x120 exterior-square matrix, not only a count.
The six complete QWZ history-reduction cases at N=8,16,32 were regenerated.
The previous N=128 current-comparison diagnostics were hash-checked, not
rerun as a new holdout in this round.

The new history proof and its conditional rate received an independent
read-only mathematical review. The involution proof was independently
developed, read in full by the root agent and its tests replayed there.
The final clock/Clifford census and boundary selection rule also received
an independent read-only mathematical review with no substantive correction.
Finite checks are not a proof of the remaining source-to-current limit.

The systematic-debugging workflow localized the optimized-import failure
to the pinned legacy source hashing its docstring. The new involution
adapter compiles that unchanged legacy source with optimize=0, preserving
its checks. The legacy module itself is not claimed to be -OO hardened.
An existing ResourceWarning at source line 366 (unclosed source-file handle
used by its hash routine) remains visible; both modes complete successfully.
No foreign-file fix or warning suppression was made.

Exact source and result hashes:

- History checker: 6f56240dbc892581986fc0ee631b15390838cfa708dcbaf926155541c06e247b
- History validation: 5cdb8408063062901787f1d2df222daa5d5b5bfac965f56c3cd5a6daa7ad712d
- Involution checker: 9bf99de79f224ffcd060359eb146510b6e49973170f9953a0aec26760bd2c1a1
- Involution validation: 220ad33a08b3568434c25babd02c6f083493870a38407b6094cccf1c0c586377

The numerical thermal helper can saturate by float64 underflow/roundoff.
This is tested and is not evidence that exact finite-beta covariances lose
faithfulness; no modular logarithm is computed from a saturated array.
