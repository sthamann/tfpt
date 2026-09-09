# Verification record — 2026-09-08

Base checkout HEAD: `b803b7e5`. Existing dirty research was preserved.
No paper, website, verification-source, ledger or RH edit; no commit/push.

| Suite | Normal Python | Python -OO |
|---|---:|---:|
| half-twist-grade-carry | 23 passed, 1.151 s | 23 passed, 1.178 s |
| charged-cocycle-lift | 20 passed, 1.480 s | 20 passed, 1.480 s |
| compiler-clifford-bridge | 18 passed, 1.215 s | 18 passed, 1.204 s |
| Total | 61 passed | 61 passed |

The new suite includes:

- Seven direct source hashes and the previous certificate's transitive pins.
- Exact A3/D3 isometry, inverse source-lattice membership and 240-root census.
- 57,600 root-pair grade additions and unbounded-integer carry controls.
- Inherited cocycle square, fourfold charge carry and zero-mode energies.
- 48 actual QWZ source configurations with exact dyadic matrix comparisons.
- Independent exact small-matrix residual ranks and block norm identities.
- Exact polynomial edge recurrences and tail bounds at several widths.
- 36 floating full-source low-mode strip cross-checks (12 N/sector choices,
  three strip widths), independently of the symbolic proof.
- Separate finite-filled-vacuum diagnostics, reproduced to 1e-9; never
  promoted to a continuum theorem or many-body energy bound.
- Full exact JSON replay and explicit no-closure/no-clock-identification guards.

The first checker run failed at a structural SymPy equality: its off-diagonal
expression was unexpanded, while the comparison target was expanded. The
independent expanded residual was the zero matrix. Following
`systematic-debugging`, the single equality guard was corrected to compare
the exact expanded residual, and test 16 covers both the correct identity
and the wrong-sign control. No numerical tolerance or physical condition
was substituted for the failed guard. The skill's additionally referenced
`superpowers:test-driven-development` skill was unavailable; the local
reproduction and regression test were used directly.

Final artifact hashes:

```text
checker.py
1336ef54c776794f2a587fbd9c7250f069394ae9e509e2e32dc91a357fa8ab47
test_checker.py
49d86f653630bc589dc786e8a6a28e26f5c4d4a3af18dfa63d88b68bf9ed07c8
validation.json
68306ccccd20bba83faf37ce9e2705aa97952c11ca3756caf09258c887f8606d
vacuum_diagnostic.py
10bf40c9d6714ddd122dbee3cd9a5b655676e25158fb97862c28b66c5ef18ecc
vacuum_diagnostic.json
9079ea8d448976c5cef9bc1ad7bcd09abdb5dce618c4d5caa8507d400072c3d5
```

The test counts certify the stated implementations and scoped identities.
They do not certify a microscopic charged field, the many-body scaling limit,
3+1D reconstruction, chiral Standard Model matter, gravity, or full TOE.
