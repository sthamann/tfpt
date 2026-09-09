# Verification record — 2026-09-08

Local HEAD b803b7e5, existing work preserved. All suites below were actually
rerun by the root agent in this round, not copied from the previous total.

| Suite | Normal | Optimized (-OO) |
| --- | ---: | ---: |
| clock-bilinear-response | 17 pass | 17 pass |
| history-reference-transport | 11 pass | 11 pass |
| compiler-involution-types, including clock census | 12 pass | 12 pass |
| polarization-history-bridge | 14 pass | 14 pass |
| Total | **54 pass** | **54 pass** |

The 17 Clock tests last ran in 5.449 s / 5.482 s. The unchanged 26 predecessor
tests are scoped regressions, not a full repository test run. The eleven reference
tests include an actual N8 source construction and the final added heat-trace
test, rerun after it was added. Source comparisons at N8/16/32
and the separate N24 diagnostic were produced by the parallel reference worker.

Full-Fock verification independently assembles 16 Majorana operators on
256 states and diagonalizes the resulting quadratic Hamiltonian. It checks
thermal traces at (u,t)=(1,1/8) and (3/16,1/8) against analytic formulas.
Maximum absolute weight error <=5.2e-15; commutator-expectation error <=5.4e-15.
All original source pins remain enforced. A mathematical review independently
confirmed marker, family, frequency and zero-temperature-window statements.

## Reproduced and fixed comparator error

Root cause: conflation of the coefficient matrix acting on gamma(v) with
the transposed one-particle matrix in c^* h c. With the declared Jordan-Wigner
convention, the latter is h=uI+t(S+iR), not uI+t(S-iR).

Before correction, an explicit eight-state one-particle block extracted from
the full Fock Hamiltonian differed from the old expression by max-entry 0.25.
The plus-iR expression had residual exactly zero. This was reproduced before
editing, following the systematic-debugging skill. A dedicated regression
now checks both the correct identity and the wrong-transpose negative control.
The transpose-invariant leading minors, eigenfrequencies and thermal values
did not change. Saved results were regenerated after the correction.

The skill's separately named test-driven-development companion was not
available; a minimal failing read-only reproduction and explicit unittest
regression supplied that step. No foreign source was modified.

The known ResourceWarning at frozen source line 366 remains visible. The
inherited adapter retains legacy docstrings and guards with optimize=0;
this is not a claim that the legacy source is itself -OO hardened.

Final Clock artifact SHA256:

    checker.py     d3098de774f923c15d1d7adf2951cbfc530f6c77a3252610e657b2448a2e8191
    validation.json c48c85e1609db878701a189ea9ad4cb356aab70be9e6b687e441f2a7a6ffc3a1

Final reference artifacts, hashes verified again by the root after freeze:

    checker.py       17a8a1a3f438a42a4c884e0b93225c8773637a7a2ed8e2e18ddbffb53768d918
    diagnostics.json 9aacd23d174a28a6a6e17d673940096cbcf5aacfe94a5d651dc6dd2c637fc972
    holdout_N24.json be049d51bdf54047b65a1a50148bd94fbe98a5d2974b6ff8bfb65587afda1caf

The complete final reference proof was read by the root, including the
uniform quasimode retention bound, neutral spectator identity and the
heat-trace estimate. Both datasets identify the final checker hash.

Quadrature comparisons are not certified error intervals. Tests verify
finite formulas and boundaries, not the microscopic scaling limit or TOE.
No paper, site, completion marker, commit or push change.
