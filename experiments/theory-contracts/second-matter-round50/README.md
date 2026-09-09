# Round50: a second matter layer and exact source compilation

2026-09-08. **NON-RH / conditional same-parent theory experiment.**

Add MEMMMM, MMEMMM and MMMEMM to the unchanged Round49 source. The new
compiler groups paired frequency/current-prefix multisets and antisymmetric
annihilator legs before propagation. It also memoizes final actions while
retaining intermediate words that vanish only on the initial state.
Neither reduction changes the original Hamiltonian or raw error census.

The independently resummed edge source confirms this one-electric family
through order seven. Its new boundaries start at orders eight and nine;
the GLOBAL ideal remainder remains order seven because other families
remain unevaluated. At t=1 the prospective new ideal defect is
1.2356578297871707e-6, versus 2.9183911450664386e-6 in Round49.
It may enclose a new bulk value ONLY after the changed column is evaluated.

[SECOND_MATTER.md](SECOND_MATTER.md) gives the construction, proof,
independent checks and explicit resource/claim boundaries. The completed
[validation.json](validation.json), when present, records the actual new
bulk interval, exact reconstruction of the old column, arithmetic errors
and costs. The experiment catalog records the current execution status.

## Reproduction

From the repository root, using the shared Python environment and clang++
with C++17 support and GMP's C++ headers/libraries. Homebrew GMP prefixes
are detected on macOS; set `TFPT_GMP_PREFIX` for a nonstandard installation.
On other supported 64-bit Unix systems the compiler's system search path
is used when no prefix is found. No dependency is installed automatically.

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/second-matter-round50/checker.py --baseline-only --output experiments/theory-contracts/second-matter-round50/baseline-orbit-validation.json
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/second-matter-round50/checker.py --output experiments/theory-contracts/second-matter-round50/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/second-matter-round50 -p 'test_*.py'
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/second-matter-round50 -p 'test_*.py'
```

Two full representations produced no bulk result: separated-frequency
keys grew too quickly, and direct unprojected physical amplitudes reached
the 40-million-entry gate. They remain small-test references.

The new candidate accumulates the SAME rational amplitudes in bounded
blocks and then exactly folds them into signed proper-cubic orbit sums.
Its Gram divides each squared orbit sum by the physical orbit size;
fermionic stabilizer signs and all cross-family interference are retained.
This reduction requires a scalar full column and is not applicable to
arbitrary preparations. The complete Round49 baseline must be reproduced
before treating the representation as accepted. The baseline-only result
is explicitly not a new Round50 bulk interval.

The [baseline-only validation](baseline-orbit-validation.json) reproduces
Round49 exactly: 6882808 physical outputs represented by 286969 nonzero
orbit sums, with unchanged rational probability and numerical error.
The separate new bulk calculation must still produce `validation.json`.

The proof also includes a reusable finite repeated-electric moment
recurrence, checked against complete assignments for up to four electric
differences. This prepares the MEEE branch; it does not evaluate it.

Full replay is deliberately an expensive end-to-end check. Run large
replays sequentially unless the actual machine resource envelope supports
concurrency. Native streams and executables live in task-specific temporary
directories, cleaned on exit or unwind. Explicit resource gates fail closed.

Success verdict: `SECOND_MATTER_SUFFIX_EVALUATED_ON_FULL_CUBIC_BARE_COLUMN`.
No success may be inferred from the existence of this README or the bound.

## Remaining work and experiment firewall

The numerical configuration error remains separate and is not upgraded to
seventh order. No general coherent/mixed or Bell bulk readout is claimed.
All-order electric propagation, state/parameter selection, a chiral continuum
and universal spin-two emergence remain open. T1-T8 are not closed.

This is local conditional research under the TFPT experiment rules: no
paper, website, verification, ledger, scorecard, commit or push, and no
empirical, proof-assistant or peer-review promotion.
