# E6 and seam D4 operator connection

Research contract, 2026-09-18. Verdict: **PARTIAL**, enum PASS / PARTIAL / FAIL.
Read [PROOF.txt](PROOF.txt) for the assumptions, exact statements and physical boundaries.

The checker derives the marked E6+A2 decomposition from the original E8 root bracket,
extends the original seam deck/inversion to E8, and verifies the determinant completion
`W = det(V)^* + V` and its three-family projector. The source family identification is explicit.

Run with Python 3, SymPy and NumPy from any directory:

```sh
python3 -B checker.py --out /tmp/tfpt-e6-seam
python3 -B -OO checker.py --out /tmp/tfpt-e6-seam-optimized
```

Firewall: experimental structural audit, no physical state, spacetime, gauge-field assignment
or TOE closure. No empirical scorecard or load-bearing promotion. Input sources are pinned
and reused via AST extraction. No original verification modules are modified.
