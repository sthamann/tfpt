# Symmetric source product audit — 2026-09-21

Research ID: `UR.SOURCE.SYMMETRIC_PRODUCT_AUDIT.01`.

**Verdict: PARTIAL.** The attached exact symmetric E8 current-product spectrum and full marked weight characters are independently confirmed. The physical primitive-source selection, local charged-field map and common physical time remain open.

The new calculation reconstructs every symmetric pair from the archived native FW root directions and the explicitly stated grade-two lattice-vertex formula. It uses exact rational charge blocks. Kokzyklus column phases are removed by a diagonal unitary change for spectral and weight-character checks only. This is not a replay of the historical signed tensor map.

Read `ERGEBNIS.md` for proof scope and relevance; `SOURCE_AUDIT.md` records the bounded independent provenance review. The submitted text is preserved with its unresolved citation markers. No missing citation marker is treated as evidence.

Replay with Python 3, NumPy, SciPy and SymPy; the pinned source repository must be present at its recorded location:

```sh
python3 -B independent_gram_check.py --out independent_certificate.json
python3 -B -OO independent_gram_check.py --out independent_certificate_optimized.json
```

`source_manifest.json` records the original text, native source and result hashes. The checker explicitly guards the native source SHA256 before execution. The normal and optimized certificates are byte-identical.

Firewall: theory experiment, no empirical scorecard row, no paper or verification-ledger promotion, no T1-T8 closure. The 8 and 4 Gram eigenvalues do not constitute physical masses or measured coupling strengths. The pure grade-time response is scalar after Gram normalization.
