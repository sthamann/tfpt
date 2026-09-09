# Round40: controlled matter hierarchy and certified bulk phase sensitivity

2026-09-07. **NON-RH / unpromoted conditional research.** Same unrotated U(1)
parent, same declared parameters and E=0 one-fermion/site family. No TFPT
vacuum/parameter selection, empirical prediction or physical T1-T8 closure.

## Executed result

At model time t=1, for the unchanged bare-low input:

**0.00217210099436 <= <n_H,x(1)> <= 0.00222283452421.**

The interval is about **24.17 times narrower than Round39** and **105.08 times
narrower than Round38**, for the same parent, input, time and observable.
The fourth-order amplitude remainder is <0.000270570887988; all electric
branches and later matter branches remain bounded, not silently omitted.

There is also a new full-bulk phase distinction. Give the root p_H=1/2 and
onsite coherence zeta=<c_L^* c_H>=-i/2 or +i/2, keeping all other sites bare.
The inputs share all initial occupations and fluxes:

| Root coherence | Full-bulk high occupation at t=1 |
|---|---|
| -i/2 | [0.50317655238322, 0.50394456239144] |
| +i/2 | [0.49818165797508, 0.49894584802176] |

The intervals are disjoint: **the first exact model response exceeds the
second by more than0.00423**, under the derivation's stated assumptions.
This does not choose a physical state or provide every source response.

## What was actually computed

All matter paths through depth4: 1,6,252,9288,343440 paths at successive
levels, with no sampling or pruning. Exact collection gives229913
mode/flux/frequency groups,180 scalar kernels and140372 complex operator
coefficients. Genuine cubic plaquette paths are present. These are NOT a
finite physical state space replacing the surrounding lattice.

Free electric and mass phases are evaluated through rational simplex
polynomials, with total numerical amplitude error <1.441e-47. No electric
cutoff or dynamical spatial window is introduced. Later matter levels5-8 in
the validation record contain BOUNDS ONLY, not executed higher-order readouts.
Direct path enumeration beyond4 is intentionally not implemented here.

[MATTER_HIERARCHY.md](MATTER_HIERARCHY.md) contains the full derivation,
phase accounting, two-species bound recurrences, cost and proof boundaries.
[checker.py](checker.py) and [test_checker.py](test_checker.py) reproduce it;
[validation.json](validation.json) records exact rational results and source
hashes. The standard-library checker uses the inherited parent; tests also
use the existing environment's SymPy.

Validation: **24 new tests plus269 predecessor tests (Rounds30-39), all
passing both normally and with Python -OO**. This includes the whole charged
edge input family, exact third-time-jet witness, all collected Gauss
covariances, genuine cubic plaquettes and deterministic replay. These checks
support the written derivation; they are not proof-assistant formalization or
independent peer review.

From the repository root:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/matter-hierarchy-round40/checker.py --output experiments/theory-contracts/matter-hierarchy-round40/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/matter-hierarchy-round40 -p 'test_*.py'
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/matter-hierarchy-round40 -p 'test_*.py'
```

## Important limit of the result

The matter-only series converges at all orders, but at positive kappa it is
NOT exact unitary dynamics. Its electric upper-bound budget tends to about
0.00013839782796. That is a limit of this certificate, NOT a lower bound on
the actual error. An independent full-matrix third-time-jet witness confirms
that the discarded electric branch is genuinely nonzero; higher matter
orders cannot repair that missing coefficient by themselves.

The next task is therefore the explicit nonlinear electric branch, not merely
an ever-larger matter path list. The present round neither eliminates high
fermions nor derives chirality, the continuum limit, spin-two gravity, a
selected vacuum or all parameters. Tree benchmarks are independent checks,
not substitutes for the cubic proof. No empirical scorecard, verification,
paper, website, ledger, commit or push is part of this experiment-only round.
