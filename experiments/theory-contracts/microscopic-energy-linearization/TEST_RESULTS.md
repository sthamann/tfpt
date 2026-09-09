# Verification record — 2026-09-08

Local HEAD b803b7e5. The root agent actually reran every suite below in this
round. Counts refer to distinct tests in the final suite, not repeated runs.

| Suite | Normal | Optimized (-OO) |
| --- | ---: | ---: |
| microscopic-energy-linearization | 10 pass | 10 pass |
| current-truncation-bridge | 13 pass | 13 pass |
| clock-neutral-access | 12 pass | 12 pass |
| history-reference-transport | 11 pass | 11 pass |
| polarization-history-bridge | 14 pass | 14 pass |
| clock-bilinear-response | 17 pass | 17 pass |
| Total | **77 pass** | **77 pass** |

This is 35 new tests plus 42 scoped predecessor regressions per mode, not a
full-repository test run. Each suite ran in a separate Python process to
avoid collisions between the local modules named checker. Final new energy
suite: 0.363 s normal, 0.354 s optimized; Clock-access: 36.637/35.884 s.

The two Clock suites emit a preexisting ResourceWarning from the unchanged
legacy seam_state_derivation_probe.py opening its own source without a
context manager. Tests pass; this warning was not suppressed or repaired by
changing the pinned source. The existing source adapter retains its declared
legacy handling, so optimized tests are not an OO-hardening of that source.

## Analytic review versus finite tests

The root agent read and checked the Current Galerkin proof: current/sea
conventions, exact compression, missing-energy cost, weighted coherent
tails and whole-word Duhamel. A separate agent independently reviewed all
five critical energy-linearization proof steps, found no mathematical error,
and reran the then-nine energy tests in both modes. Its requested explicit
self-adjointness/Schatten-domain qualifications were incorporated. The
additional exact per-leg phase identity received a tenth test, then the
root reran all ten in both modes. This is internal review, not external
peer review or a formal proof-assistant certificate.

The Clock branch uses exact original-Majorana algebra. Its local symbolic
coefficient-normalization correction and regression are documented in
../clock-neutral-access/TEST_RESULTS.md. No physical source, coupling or
Clock phase was altered to obtain a passing check.

`diagnostics.json` contains source-strip checks at N=8,32,128,512,2048.
For example, measured global energy defect at N2048 is about 0.000445488,
below the analytic cap 0.000445917. Same-polarization residuals remain below
6e-15. These are floating-point corroborations, not interval certificates.
The large prefactor in the history cap is explicitly retained; its finite
values do not establish a practical small-error threshold.

The mathematical asymptotic claims come from the written inequalities,
not from these test counts or finite convergence tables. The unresolved
source/current raw-operator match remains marked false in the diagnostics.

## Integration boundary

Only three new experiment directories and additive entries in the existing
experiments index/next ledger belong to this round. Other untracked work,
including the independent RH/inter-sheet research, was preserved. No source
pins, completion markers, paper, website, commit or remote were changed.
