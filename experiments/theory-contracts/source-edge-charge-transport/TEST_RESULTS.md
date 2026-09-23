# Verification record — 9 September 2026

Repo basis: `66b91e40e245569f06ab440ead80f446c9be0ee5`.

| Suite | Ordinary Python | Optimized Python (`-OO`) |
| --- | ---: | ---: |
| `source-edge-charge-transport/test_checker.py` | 18 passed | 18 passed |
| `source-half-sector-bridge/test_checker.py` | 16 passed | 16 passed |
| `microscopic-charged-car-limit/test_checker.py` | 19 passed | 19 passed |
| Total per mode | **53 passed** | **53 passed** |

These are 53 distinct tests executed twice, not a full-repository test
run or independent mathematical review. All calls used the existing
TFPT Python environment and `-B`; upstream evidence was not overwritten.

Both full local replays completed. `validation.json` and
`validation_optimized.json` are byte-identical. The three recorded local
code SHA-256 values match the current files after the final test edits.
The source pins and the upstream loader's transitive validation passed.

## Independent checks and negative controls

- The original 16N cylinder and the complete collection of 16-dimensional
  momentum blocks give the same filtered operator and complete-sea density.
- A separate 40-decimal mpmath symmetric eigensolver reconstructs the
  strip from the actual source hopping coefficients. At N=16 the sea
  difference is `0.499990152881393945724168401240721692516`.
  This is an independent numerical control, not interval arithmetic.
- Gaussian time averaging is checked independently by numerical quadrature.
- Explicit four-mode Fock matrices check the full-sea fluctuation identity,
  its energy-weighted version, and the creation/adjoint Ward identities.
- Symbolic calculations check the bidiagonal source decomposition,
  smallest-singular-value residual and gap identity. Exact fractions
  check the shifted sawtooth sum.
- Every proper transverse cut is tested without deleting bulk modes.
- The unfiltered density has a nonvanishing, increasing vacuum variance;
  mean subtraction alone therefore does not pass the charge limit.
- The full one-body commutator does not vanish in the samples. This guards
  against promoting fixed-excitation conservation to a full-Fock norm claim.
- Own-sector vacuum subtraction would give zero in both sectors; the
  recorded half shift instead uses the one declared common reference.
- No microscopic intersector field, eight-channel identification, local
  half-transfer, source-selected background dynamics or TOE closure is
  asserted in the saved record.

## Two initial test-assumption errors, resolved without changing the model

The initial 17-test version had two failures. Systematic cause analysis
found both in the proposed controls, not in the source dynamics:

1. `(N,r,j)=(16,3,1)` was incorrectly expected to violate the small-p
   guard. Its actual momentum is pi/32, inside the domain. The invalid
   test case now uses j=0, whose absolute momentum is 3pi/32>1/4.
2. A finite-p difference was compared too closely to the limiting jump.
   The source's smooth massive contribution is nonzero at finite p. The
   replacement checks the exact p=0 geometric zero modes and massive
   projector separately, then tests convergence of the finite-p values.

Neither correction changes a source parameter or relaxes the written
theorem. The supplementary test-first skill named by the debugging guide
was unavailable; the two existing failing cases were used directly as
reproductions. The final suite adds an independent-precision check and has
18 tests, all passing in both modes.

## Reproduction

From the repository root, for each of the three folders in the table:

```sh
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/source-edge-charge-transport -p test_checker.py -v
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/source-edge-charge-transport -p test_checker.py -v
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/source-edge-charge-transport/run.py --output /tmp/source-charge-replay.json
```

Analytic estimates and scope are in [PROOF.md](PROOF.md). The next field
acceptance test is specified, but not executed, in
[NEXT_FIELD_TEST.md](NEXT_FIELD_TEST.md).

Only this new research directory was added. No old source, paper, website,
global status marker or foreign change was edited. No commit or push.
