# Round49: sixth-order ideal source and a new cubic bare readout

2026-09-08. **NON-RH / conditional same-parent theory experiment.**
This round adds the actually evaluated sources MMMME, MEME and MMEE.
The complete ideal source agrees with the independent full edge Hamiltonian
through time order six on its entire E0 initial family. Each of the three
additions is necessary for that check. The direct ideal remainder now begins
at seventh order, with every later boundary branch explicitly bounded.

## What changes

The original cubic Hamiltonian, its couplings, onsite backtracks and the
bare-low E0 bulk input at t=1 remain unchanged. No parameter is selected or
fitted. Both creator transport and literal five-factor CAR contractions
remain in the new sources. The new electric search uses an exact incidence
index of the original hopping monomials; it does not replace the model.

The full old cubic source is regenerated as an exact rational control. The
new sources are then added into the common physical output vectors, with
all six directions and their fermionic rotation signs restored BEFORE
squaring. This calculates a new center, unlike Round48's recertification.
The result, outward interval, complete error components and resource counts
are in [validation.json](validation.json); the catalog states the numbers.

See [SIXTH_SOURCE.md](SIXTH_SOURCE.md) for the source construction, exact
sixth-order test, seventh-order direct defect and numerical proof boundary.

**The numerical configuration error remains separate and can start at
fourth order.** The ideal seventh-order defect is not a claim of the same
order for the fully numerical approximation. No new bulk Bell or general
coherent/mixed bulk readout is claimed. Independent complete edge controls
are not substituted for a cubic calculation.

## Reproduce

From the repository root, with the shared Python environment and `clang++`
supporting C++17:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/sixth-source-round49/checker.py --output experiments/theory-contracts/sixth-source-round49/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/sixth-source-round49 -p 'test_*.py'
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/sixth-source-round49 -p 'test_*.py'
```

The native helper and binary streams live in task-specific temporary
directories, cleaned when the scopes exit or unwind. Exact sums, bounded
protocols and resource guards prevent silent pruning or integer overflow.
The substantial original Round47 calculation is a real dependency cost;
no end-to-end speedup claim is made.

Verdict: `SIXTH_IDEAL_SOURCE_COMPLETED_AND_CUBIC_BARE_READOUT_EXECUTED`.

## Remaining work and experiment firewall

The source hierarchy is not completely solved. Higher first-electric,
matter and repeated-electric terms remain explicitly bounded, not evaluated
to all orders. Parameter/preparation selection, a chiral continuum and
universal spin-two emergence remain open; T1-T8 are not closed.
Under the TFPT experiment rules this stays local conditional research:
no paper, website, verification, ledger, scorecard, commit or push, and
no empirical, proof-assistant or peer-review promotion.
