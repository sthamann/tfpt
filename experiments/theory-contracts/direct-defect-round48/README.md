# Round48: direct full-H defect certificate for the pinned cubic column

2026-09-08. **NON-RH / conditional same-parent theory experiment.**
This round tightens the error certificate of Round47's ALREADY COMPUTED
bare-low E0 bulk column. It does not compute a new column or retain another
numerical matter layer. All original couplings and the physical model stay
unchanged. T1-T8 and the full electric solution remain open.

## Result and mechanism

The new certificate follows the actual finite source directly through its
defect against the full physical Hamiltonian. Norm-preserving full-H
propagation bounds every continuation after an omitted boundary event.
This avoids going through a different infinite-M intermediate target.
For each extended leaf p, the complete boundary is pE, pMM and pME; none
of these branches is discarded. Older first-electric and MEME/MMEE bounds
are retained separately.

A second rigorously scoped simplification removes only literal words that
are zero on the WHOLE Fock space. Words merely null on the chosen input
remain. Raw full-cubic counts and phase moments still reproduce the pinned
earlier records before this safe zero test is applied to the error census.

See [DIRECT_DEFECT.md](DIRECT_DEFECT.md) for the derivation and
[validation.json](validation.json) for exact raw/retained moments, direct
and control bounds, unchanged rational center, numerical error and outward
decimal interval. The experiment catalog records the numerical outcome.

The bulk numerical configuration/phase errors are reused without reduction.
Only the analytic defect certificate changes. The ideal global error stays
sixth order; the inherited configuration error can start at fourth order.
No new bulk Bell calculation or empirical prediction validation is claimed.

## Reproduce

From the repository root, using the shared environment:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/direct-defect-round48/checker.py --output experiments/theory-contracts/direct-defect-round48/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/direct-defect-round48 -p 'test_*.py'
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/direct-defect-round48 -p 'test_*.py'
```

The checker reruns the complete raw seed census and pins Round47, its source
files and transitive parents. Tests cover complete-Fock zero decisions,
safe versus unsafe pruning, exact branch coverage, species and current
moments against explicit additional hops, full edge readouts, all error
components, unchanged bulk center, guards and deterministic replay.
The underlying Round47 replay still requires its C++17 compiler and the
large physical-column calculation; it is not made free by this certificate.

Verdict: `DIRECT_FULL_H_DEFECT_CERTIFIES_PINNED_BULK_COLUMN_MORE_TIGHTLY`.

## Remaining work and experiment firewall

Next are the unchanged older first-electric/MEME/MMEE branches, sharper
retained-source control and additional bulk observables. No state/vacuum or
parameter selection, chiral continuum, or universal spin-two sector is proved.
Under the TFPT experiment rules this stays local conditional research:
no paper, website, verification, ledger or scorecard promotion, no commit
or push, and no empirical, proof-assistant or peer-review status change.
