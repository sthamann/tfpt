# Joint source response and native operator bridge

**UR.SOURCE.JOINT_RESPONSE.01 — PARTIAL — 21 September 2026.**

Read ERGEBNIS.md for the result, PROOF.md for the conditional joint state/time theorem, NATIVE_PAULI_RAW_AFFINE.md for the exact native/affine sign audit, and INDEPENDENT_REVIEW.md for the mathematical review and normalization boundary. SOURCE_AUDIT.md locates the first remaining source-selection premise.

Reproduce with Python, NumPy and SymPy:

```sh
python3 -B joint_response_check.py --out joint_response_certificate.json
python3 -B -OO joint_response_check.py --out joint_response_certificate_optimized.json
python3 -B check_native_pauli.py --output native_pauli_audit.json
python3 -B -OO check_native_pauli.py --output native_pauli_audit_optimized.json
```

Compare normal and optimized result files byte for byte. The native checker preserves six original pinned source-prefix guards via optimize=0. Infinite-dimensional assertions are proved analytically, not inferred from finite tests.

The source Gram is full rank 2076 for nonzero separation and has a controlled 3/4/5-energy collision limit. Perfect polar-label exchange depends on the normalization protocol and is not an elementary physical interaction claim.

Experiments firewall: no paper, verification, ledger or empirical scorecard promotion; no physical T1–T8 closure.
