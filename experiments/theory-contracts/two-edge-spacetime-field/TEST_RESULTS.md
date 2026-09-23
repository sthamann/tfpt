# Two-edge spacetime field: local validation, 2026-09-09

Status: **PASS for the bounded checks listed below.** The analytic claims
are the conditional arguments in README; independent mathematical review
and the microscopic intersector-field identification remain open.

Runtime: Python 3.14.3, numpy 2.4.6, sympy 1.14.0, mpmath 1.3.0, from
`/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/tfpt-discovery/.venv/bin/python`.

| Module | Ordinary | `-OO` |
|---|---:|---:|
| `two-edge-spacetime-field` | 26 passed | 26 passed |
| `source-half-sector-bridge` unchanged upstream regression | 16 passed | 16 passed |
| `half-charge-energy-bridge` unchanged upstream regression | 12 passed | 12 passed |
| Total for these three modules | 54 passed | 54 passed |

All six test processes exited 0. These are not a rerun of the complete
published consolidation suite. No proof guard relies on Python assertions
that disappear under optimization.

## Exact checks

- CAR coherent levels 0 through 6, both edge orientations, relative integer
  charges -2 through 2, independently agree with the rational coefficients
  `(1/4)_n/n!`; both source backgrounds retain the correct level energies.
- Independent oscillator partitions, positive-current vacuum annihilation,
  and protected central terms agree. A finite-cutoff empty-state control
  explicitly rejects a globally central finite-matrix commutator.
- Rational radial and non-monotone mode regulators agree with the pinned
  kernel recurrence; the current amplitude uses g, the norm recurrence g squared.
- Half-charge carry is invertible and not a cyclic two-state flip.
  Forward/adjoint source-vacuum output energies are 0 and 1/2.
- Normal-ordering coefficient is 1/4 for two edges. Exact nilpotent
  oscillator matrices independently verify the finite matrix elements;
  their adjoints and reversed source energy differences agree.
- Energy shell convolution is `(1/2)_ell/ell!`. For the **conditional**
  eight-pair product it is `binomial(ell+3,3)`; the spatial cutoff norm is
  exactly `(N+1)(N+2)(2N+3)/6`. This does not select eight microscopic pairs.

## Floating diagnostics, not infinite-limit proofs

For the constant spatial smear and the forward vacuum:

| Oscillator diagonal cutoff N | Squared norm | Squared `(1+H)^(1/4)` norm | Squared `(1+H)^(1/2)` norm |
|---|---:|---:|---:|
| 100 | 1.165173123 | 1.561555712 | 3.926351397 |
| 1,000 | 1.175530742 | 1.808856508 | 10.507374703 |
| 10,000 | 1.178819161 | 2.056538406 | 31.314777235 |

The first column tends to `sqrt(pi)/Gamma(3/4)^2 = 1.180340599...`.
The next two diverge, by the analytic series criterion, not by extrapolating
this table. Finite partial sums also satisfy the separate Gauss-sum tail
enclosure used in the tests.

With normalized Gaussian time smearing of width 0.3, the forward squared
graph norms at powers 0, 1/2, 1, 2 are approximately
1.049956362, 1.163767151, 1.565819835, 9.638165264.
Both adjoint directions were checked up to power 4; cutoffs 40 and 120
agree at the stated test precision. Their finiteness for every power is
established by the explicit time-decay majorant in README, not those samples.

## Provenance and remaining boundary

`validation.json` was freshly generated and reproduced in both modes.
Only named floating diagnostic fields admit 1e-11 absolute last-bit
variation in the saved-record test. All pins, rational values, labels,
and scope flags must agree exactly; NaN and infinity are rejected.

SHA-256 of the checked artifacts:

| Artifact | SHA-256 |
|---|---|
| README.md | `7f1821d04b50ddac0917dfa9381aa85f425caa593354a16a6ecd7be4513109c2` |
| checker.py | `d9ea6aa7f1ab15a962585c6f8611e0aec84f341eb744f88952f08408de4020c5` |
| test_checker.py | `05e586689d8083894f70a34c244520898361fc8c47e7ae30daa552febc7f4993` |
| validation.json | `2e74ff752a5374e10aeb0d8d62c74700cb9f07c3f00e0ec290eaad20c316cc6e` |

The new directory is local research work, not a published paper/website
update. Upstream pinned files and the published consolidation manifest
were not changed by this step. The existing unrelated local CI/research
changes were preserved. No T1–T8 item was marked closed.

Next acceptance criterion: identify a full-source intersector operator and
its adjoint with the same normalization, phase, time evolution, and charge
carry, then prove finite-output-energy convergence **and** uniform energy
tails on vacuum and nonvacuum current inputs. The zero-momentum/high-energy
pair tower must be included. A target-defined pullback through the embeddings
would not count as a microscopic derivation.
