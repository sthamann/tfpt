# Native E8 root operator dictionary

Research contract `UR.COMPILER.NATIVE_ROOT_DICTIONARY.03`, 2026-09-18.

Verdict: **PARTIAL** toward the physical compiler/TOE. Exact scoped algebraic
results and a refuted source-action identification are separated in [PROOF.txt](PROOF.txt).
Verdict enum: PASS / PARTIAL / FAIL.

Run from any working directory, with Python 3, SymPy and NumPy:

```sh
python3 -B checker.py --out /tmp/tfpt-native-dictionary
python3 -B -OO checker.py --out /tmp/tfpt-native-dictionary-optimized
```

The checker pins the original repository sources, reads the prior integral
triality certificate, and runs four isolated exact comparisons: abstract
Spin(10) completion, decisive Weyl mismatch, native D8 root/CAR dictionary,
and cocycle-correct E8 clock lifts. Original source symbols are loaded through
AST extraction; no original verification module is edited.

The 5+3 coordinate marking and 3+2 hypercharge marking are explicit inputs.
The tested 48-weight readout is not invariant under the whole clock action.
This is neither a gauge no-go nor a derivation of physical clock evolution.
The native spinor module is not automatically a set of spacetime fermions.

Firewall: experiment-only internal structure audit; no empirical scorecard,
no load-bearing promotion, no physical state, spacetime or TOE closure.
See `source_pins.json`, `certificate.json`, `replay.json` and `contract_index.json`.
