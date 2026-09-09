# Validation record — 2026-09-08

Only this experiment directory was written. Source adapter and original
Majorana source remain byte-identical to their pinned versions.

## Final checks

| Invocation | Result |
| --- | --- |
| `python3 -B -m unittest discover -s experiments/theory-contracts/clock-neutral-access -p test_checker.py` | 12 tests passed; 35.878 s |
| Same invocation with `-OO` after `-B` | 12 tests passed; 35.850 s |
| `python3 -B experiments/theory-contracts/clock-neutral-access/checker.py` | Completed successfully; output stored in `validation.json` |

The tests validate all 256 original Majorana CAR anticommutators, original
source-number and mode-occupation commutators, the pure quartic grade and
boundary support, full Clock versus family-only symmetry, all four exact
conditional-frequency projectors, the complete degree census, thermal noise
versus response, explicit prepared response, the original vacuum bound,
unresolved equal-coupling lines, source-pin failure and no-overclaim flags.

No floating-point diagonalization is used for the operator identities.
Thermal weights are floating-point evaluations of the explicitly derived
finite formulas; the unit-test reference for the recovered weight is the
already independently replayed original value 0.2269715953.

## Debugging provenance

The first run stopped at `primitive stays charged`, before running any tests.
Systematic debugging reproduced literal dictionary inequality while the exact
coefficient difference was zero. A representative pair was

    sqrt(2)*(-sqrt(3)-3i)/48
    sqrt(6)*(-1-sqrt(3)i)/48.

The root cause was factored versus expanded representations of equal
radicals, not a wrong Clock action. `clean` now expands the simplified
coefficients and a focused regression test preserves this case. The phase,
source vectors, symmetry and model have not been changed to bypass the check.
The full systematic-debugging skill was read and applied before the fix.

Both final test modes display the same inherited non-failing ResourceWarning
from `seam_state_derivation_probe.py:366`, whose original `open(...).read()`
does not close its file explicitly. No upstream code was edited or warning
silenced. The pinned adapter compiles its legacy source with optimize=0;
this is not a claim that the legacy source itself is OO-hardened.

## SHA-256

    checker.py
    6f60772c639e9eb19745e363010e8ed0e39ed9cb51b38ca7997f7baecdd48f50

    test_checker.py
    f573e440e84a391c3a7d60a24c4c6a4b843578ec5849b77c59a758b88eb4c4dc

    ../compiler-involution-types/checker.py
    9bf99de79f224ffcd060359eb146510b6e49973170f9953a0aec26760bd2c1a1

    ../../tfpt-discovery/seam_state_derivation_probe.py
    5e54c416be72a125a8ce6e235b4300f9f9c2344b3ada796d2dc4c7e2ea01482b

The newly introduced quartic interaction, rational witness couplings and
probe preparation are not TFPT-derived. No T1–T8, continuum, TOE or RH
completion is claimed. No index, paper, website, commit or push was changed.
