# Round27 — full-reference error control and nonzero summed memory cutoff

2026-09-07. NON-RH research, local and unpromoted. Repository HEAD and
actual remote main checked at a21616c41bc9503f5a21ee79c42c4224f6a3d0b0.
No commit/push, public paper or website release in this round. Earlier
round artifacts and unrelated concurrent tracked edits are preserved.

## What changed mathematically

[The full-reference argument](full-reference-control-round27/PROOF.md)
keeps all constant charge profiles and their scalar determinants in one
positive reference Z_D. All-block pinching and full scalar/charge Schatten
Holder give, for the original signed finite-regulator model,

    exp(-48 beta N J) Z_D <= Z <= Z_abs <= Z_D.

Thus the previous artificial charge factor Theta(beta) is removed from
the sign budget and from the relative memory/hop errors. No original
E8 phase, hopping constant, charge state or scalar determinant is removed
to obtain this result. The sign/reference bound works in any fixed total
charge sector. The explicit coordinate-tail envelope still uses neutrality.

This is not a sign cure: exp(48 beta N J) remains extensive and can be
enormous. The actual negative closed loop of Round26 remains negative.

## Concrete certified consequences

[The exact rational planner](reference-tail-planner-round27/PROOF.md)
provides two reproducible bound calculations, not evaluated partitions.

| Case | Certified result | Remaining limitation |
| --- | --- | --- |
| Same N=27,T=3,beta=1,J=0.1 as Round26 | K=2670,P=354 for <1% omission error, versus published K=4096,P=962 | Full memory; naive enumeration still has a 1912-digit count upper bound |
| L=9,N=729,T=33,beta=99/4,J=1/866052,m^2=1,a=1,u,nu>=0 | R=12 retains 25 of 33 quadratic time offsets; memory error <=0.2045%; K=12235,P=5 give combined error <1% | Declared weak-total-hopping example; full determinant and enormous charge enumeration remain |

For a fair algorithm-independent comparison, applying the new integer
search to the OLD inequalities gives K=4035,P=956. The improvement is
therefore not explained by smaller search steps.

The second example is a genuine nonzero memory cutoff whose bound survives
the full signed history sum. It is not merely a conditional Gaussian test.
The complete eliminated determinant remains a full-history function;
this does not make the entire statistical weight finite-memory/Markovian.
The 1% budgets do not include numerical evaluation error of a future sum.

## Reproducibility and evidence types

- Two new checkers: 23 and 25 exact check groups, 18 source pins each.
- 108 finite noncommuting word tuples test the general lemmas; these
  matrices are NOT replacements for the original TFPT carrier.
- 37 isolated runner/adversarial fixtures pass normally and under -OO,
  including 14 typed formula/claim mutations and all source-pin mutations.
- Both new checkers also pass under -OO from an unrelated working directory.
- The aggregate runner reruns 29 prerequisites; its authoritative results
  and content hashes are in [ROUND27_VALIDATION.json](ROUND27_VALIDATION.json).
- [ROUND27_RUNNER_VALIDATION.json](ROUND27_RUNNER_VALIDATION.json) records
  the fixture/optimization runs. Manifest checking validates saved-run
  consistency and hashes; it is not an independent proof certificate.
- [Analytic review](ROUND27_REVIEW.md) records inequality directions,
  source typing, normalization, scope and deliberately rejected shortcuts.

Reproduce from the repository root:

    experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/run_round27.py
    experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/test_round27_runner.py
    experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/run_round27.py --check-manifests

## What is still genuinely open

The complete interacting partition has NOT been numerically evaluated.
Practical charge summation and cancellation control, arbitrary-coupling
efficient sampling, determinant locality, uniform time/volume limits and
real-time reconstruction are not solved by these inequalities. Neither
are the shared microscopic parent, full chiral sector, gravity and the
remaining T1-T8 obligations. No empirical or TOE-completion status is
promoted. The immediate computational bottleneck is now the remaining
high-dimensional charge sum and full-history determinant, not the removed
artificial reference factor.
