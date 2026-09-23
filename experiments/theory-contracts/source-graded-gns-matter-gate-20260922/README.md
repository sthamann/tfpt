# Graded GNS source: transfer selection and matter gate

Research ID `UR.SOURCE.GRADED_GNS_MATTER_GATE.01`, 2026-09-22, **PARTIAL**.

The two supplied continuations are checked at their first load-bearing identifications. The cubic solution is reproduced within its stated polynomial-minimality class. An unsplit parity lift of the existing six Kraus contributions instead yields the exact survival transfer `I-N/6` and Hamiltonian `-log(I-N/6)`. Both share all even responses. The latter is unique only under its separate explicit event-lift rule, not selected from P1/P2.

A same-space charged CAR completion follows from spectral raising/lowering. The subsequent direct Spin(10)-spinor-field identification is ruled out by the central action on the full M32 operator algebra. This is a scoped candidate exclusion, not a full TFPT obstruction.

Run:

```sh
python3 -B checker.py > results.json
python3 -OO -B checker.py > results_optimized.json
cmp results.json results_optimized.json
```

Dependencies: Python, NumPy, SymPy, mpmath. General arguments and original-source audit: `PROOF.md`. Input hashes: `source_pins.json`. Exact matrices versus numerical transcendental values are distinguished in the proof and results.

Firewall: experiments only; no empirical scorecard, no paper/ledger promotion, no physical T1-T8 closure. The original microstep, source parity-lift rule, native spinor sector and spacetime realization remain open.
