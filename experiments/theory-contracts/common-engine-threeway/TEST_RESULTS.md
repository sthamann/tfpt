# Executed checks — 9 September 2026

Runtime: Python 3.14.3, NumPy 2.4.6, SciPy 1.17.1, SymPy 1.14.0.
Parent source: commit `66b91e40e245569f06ab440ead80f446c9be0ee5`, with
explicit file digests and the parent's unchanged transitive pin checks.

| Suite | Normal | `-OO` |
| --- | ---: | ---: |
| `common-engine-threeway/test_engine.py` | 25 passed | 25 passed |
| `local-window-round37/test_checker.py` | 29 passed | 29 passed |
| `clock-rotor-joint-charge/test_checker.py` | 10 passed | 10 passed |
| `half-twist-grade-carry/test_checker.py` | 23 passed | 23 passed |
| Total distinct test cases per mode | 87 passed | 87 passed |

The new suite includes independent brute-force Gauss enumeration, exact
matrix Hermiticity, sequential creation/annihilation sign checks,
time reversal, energy/number/norm conservation, the original small-time
jet, wrong-source pins, incorrect winding elimination, wrong spinor
parity, missing integer carry, plain-flip covariance failure, and an
energy-anisotropy counterexample preserving the actual J/sigma maps.

The normal and optimized full experiment runners were also executed to
produce `validation.json` and `validation_optimized.json`. The records
include fingerprints of the exact tested local code. The runner does not
modify any original source, historical validation record or global status.

## Numerical comparisons

- Physical plaquette at flux cutoff 10: 1,412 states, all 32 original
  matter hopping/path terms, initial neutral product state with high modes
  at sites 1,2 and low modes at 0,3, all initial flux zero.
- Cutoffs 2,3,4,6,8,10 compared at model times 1,2,4.
- At time 4, source low occupation at site 1: approximately
  `0.1985320775390017`.
- Switching off only electric energy changes the low readout by up to
  `6.742653e-6`. The inherited norm-one-readout flux-truncation budget
  for each cutoff-10 computation at time 4 is `4.567143e-9`.
- Independent dense diagonalization versus sparse exponential action at
  cutoff 2 and time 2: vector difference approximately `2.151779e-14`.

The last digits of floating-point diagnostics may vary with numerical
library or hardware. The tests use tolerances, not exact decimal matching.
Analytic flux-truncation control is separate from numerical solver checks;
there is no interval enclosure of all floating-point errors.

The pre-existing Clock suite emits a `ResourceWarning` for an unclosed
read handle in the pinned historical source. It passes in both modes;
that historical source was not changed in this investigation.

## Reproduction

From the repository root, run the three commands in README. For each
upstream suite replace the `unittest discover -s` directory with its
directory from the table, use `-p test_checker.py`, and repeat with `-OO`.

These are scoped regression results, not independent peer review, a
proof-assistant certificate, a full-repository test run, universality,
or T1–T8 closure. The common plaquette-to-E8 intertwiner is still
`NOT_CONSTRUCTED`.
