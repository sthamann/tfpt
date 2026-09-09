# Round47: controlled cubic bare-column evaluation of the word target

2026-09-07. **NON-RH / conditional same-parent research.**
This round executes the bare-low E0 column of Round46's cubic resummed
target using one explicit additional matter layer and a separate
certificate for every later matter layer. It is not exact evaluation
of the infinite suffix or a complete solution of electric dynamics.

## What is actually calculated

All original cubic hops in the new layer are included. The three
cubic leaves and the literal five-factor leaf retain their complete
electric/mass phases, creator transport reversals and CAR contractions.
No seed is dropped merely because it vanishes on the initial state.

An integer-only helper groups equal FINAL physical occupation/current
states and scalar frequency kernels. The six cubic images are restored
with their fermionic rotation signs and added before squaring. The old
linear and electric sources use the same physical-state convention;
the old bare probability is reproduced exactly as a control.

The new physical interval includes all four contributions:

- Round46's ideal electric remainder;
- the newly derived tail of every omitted matter layer;
- Round44's inherited configuration-exit error;
- all scalar/matrix arithmetic errors.

The exact rational result, outward readable decimal endpoints and
individual error values are in [validation.json](validation.json),
under `readout`; the experiment catalog records the numerical outcome.
This is a NEW evaluated source, not the old numerical center with a
smaller theoretical error attached to it.

The executed input is uniform bare-low filling at model time t=1.
**No new coherent/mixed bulk or Bell readout is claimed.** The entire
electric dynamics and T1-T8 remain open. The same couplings, onsite
backtracks and physical readout n_H,0 are retained.

## Why the extra tail is controlled

The remaining matter layers are bounded with an 8- or 32-component
positive species tensor matrix and a full-Fock CAR commutator at the
last step. The bound is independent of ambient volume and initial
flux. It does not use the false coefficient-l2/CAR isometry identified
in Round46. It is independently checked against that round's complete
edge resummation on all E0 edge inputs.

See [BULK_WORD.md](BULK_WORD.md) for the derivation, physical-column
compression, fermionic rotation sign, all-later-layer tail, scope of
the numerical error and remaining proof obligations.

## Reproduce

Use the shared Python environment and a C++17 compiler (`clang++`) from
the repository root. The checker builds its integer helper and temporary
group data in a task-specific temporary directory and removes those
generated artifacts when the computation exits normally or unwinds.

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/bulk-word-round47/checker.py --output experiments/theory-contracts/bulk-word-round47/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/bulk-word-round47 -p 'test_*.py'
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/bulk-word-round47 -p 'test_*.py'
```

Twenty tests cover independent grouping, complete-cube CAR embedding,
rotation signs, raw species census, the infinite M tail and complete
edge control, phase arithmetic, guards, old/new cubic results and
deterministic replay. Native path/group counts and binary data sizes
are recorded as real costs, with checked integer arithmetic and a
fail-closed resource limit. No speedup or empirical claim is made.

The verdict is
`EVALUATED_CUBIC_BARE_RESUMMED_TARGET_WITH_EXPLICIT_ALL_LATER_M_TAIL`.
The record explicitly states one retained suffix M step, all later
layers bounded, new bulk Bell readout not executed, and full electric
dynamics not solved.

## Remaining work and firewall

Next are a tighter suffix tail or further retained layers, coherent
bulk column families, and the older first-electric/MEME/MMEE branches.
No parameter/vacuum selection, chiral continuum or universal spin-two
sector is proved. In accordance with the experiment firewall, only
local experiment files and catalog/continuation notes are changed:
no paper, website, verification, ledger, scorecard, commit or push,
and no empirical, proof-assistant or peer-review promotion.
