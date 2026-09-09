# Verification record — 2026-09-08

Base HEAD: `b803b7e5`. Previous research and source files are unchanged.
No paper, website, verification-source, ledger, RH, commit or push change.

| Suite | Normal Python | Python -OO |
|---|---:|---:|
| gaussian-vacuum-filter | 21 passed, 3.351 s | 21 passed, 3.446 s |
| half-twist-grade-carry | 23 passed, 1.196 s | 23 passed, 1.188 s |
| charged-cocycle-lift | 20 passed, 1.497 s | 20 passed, 1.453 s |
| compiler-clifford-bridge | 18 passed, 1.212 s | 18 passed, 1.185 s |
| Total | 82 passed | 82 passed |

New checks cover source hashes, the Gaussian time-integral identity by
independent quadrature, positivity/unitality, Schwarz inequality, tilted
generator and finite-angle energy-transfer bounds, actual background-ramp
bonds, all-four-sector low-state counts, source covariance identities,
ground-projector comparison, finite target-vacuum improvement, weighted
spatial propagation, too-narrow filter rejection, all-N majorant domain,
half-shifted Fourier coefficients on **both** edges, exact certificate
replay and separately toleranced floating diagnostics.

No scientific assertion or test failed in the executed new suites. Three
documentation patch-context attempts were rejected due to misspelled or
unnecessary context lines; the rejected edits did not apply. The correct
context was read back before the final successful additions and reruns.

The first 21-test run passed before the additional opposite-edge audit;
the final two runs above include that audit. All explicit no-promotion
guards survive optimization. The analytic proof is in README, not implied
by the counts or by the recorded formula strings.

Final SHA-256:

```text
checker.py
4a319e059d25be9f0aace0fbc994c0a1201ac8846a6910962c9379d48248e9fa
test_checker.py
2ae80f5711b464e4585f67457f9cbb93b6f85067336ed84ca3e85bdb25937b24
validation.json
e43ed0349721e0b9a6a43d43efabc59fb9e260951ec0d2020e18b1873aad18d4
diagnostics.json
9df8a934620c189c6db0a2d3deddc3c52b2d8c660ce99e14cca6d92e284c6d1a
```

The analytic result is vanishing **unscaled** target-vacuum excess, not
bounded conformal energy. The finite action errors remain around 0.7.
Global-background opposite-edge polarization, field normalization, phase,
integer-charge carry, smeared field/adjoint and microscopic net locality
remain open. No T1–T8 closure is certified.
