# Round45: next electric sources with controlled fifth-order matching

2026-09-07. **NON-RH / conditional same-parent research.**
Three further one-electric terms and the first two-electric term are
now evaluated for the unchanged compact U(1) parent. The ideal source
matches through time order five and has a sixth-order omitted-electric
bound. This is not a complete solution of the gauge dynamics or T1-T8.

## Executed result

For bare-low, E0 input in the full cubic parent, the physical high
occupation at the origin at t=1 lies in

**[0.00219685812592, 0.00219899873816]**.

This is more than **three times narrower** than Round44's evaluated
interval. The electric source bound decreases from about 3.464e-5 to
1.129e-5. The separate auxiliary configuration error (below 1.315e-7
at t=1) and all arithmetic errors are still included. No parameter,
onsite term, initial preparation or physical parent was changed.

The neighboring-site states (LL-iHH)/sqrt2 and (LL+iHH)/sqrt2 now have
certifiably distinct readouts at **t=0.3**:

| Preparation | Certified occupation interval |
|---|---|
| Minus phase | [0.50034548173813, 0.50034550547455] |
| Plus phase | [0.50034542873258, 0.50034545246899] |

Their separation exceeds **2.926e-8**, including every error budget.
The inputs have the same one-site density matrices I/2 and the same
initial E0. This extends the previous t=0.2 correlation witness; it is
a conditional model result, not empirical validation. At t=1 these
Bell intervals still overlap.

## What was added and independently checked

The exact split [V,FO]=F[V,O]+[V,F]O labels matter and electric events
M and E. The new sources are MEMM, MMEM, MMME and MEE. All their mass
and electric phases are evaluated at finite time, rather than replacing
them by leading time coefficients. MEE contains a literal five-factor
fermion word with an essential cubic contraction.

An independent full-Hamiltonian calculation on the complete E0 edge
initial family matches the ideal source through fifth order. Removing
MEE fails specifically at fifth order. Six independent finite-time
full-parent checks (edge and cycle, bare and two Bell inputs) enclose
the full dynamics within the new hybrid bounds.

The raw cubic census contains **5000760 paths**. One representative
first direction is used to compute the coefficients; its six proper
rotations are restored into the same physical output vectors BEFORE
squaring. This keeps interference and does not assume a rotationally
symmetric initial state. Norm constants count the full raw paths before
any zero rules special to the one-fermion/site initial class.

The two-electric sector raises the sufficient reduced-density ceiling
from three to five sites. A nonzero quintic source and compatible
five-site support pairs are verified, but irreducible five-site
dependence of the final observable is **not proved**. The implemented
common response covers up to three prepared sites with bare filling
elsewhere; later electric events may raise the hierarchy further.

The sixth-order remainder describes the IDEAL source with its exact
matter row. Round44's reused finite-configuration calculation has its
own additional all-exit error, which may start at fourth order. The
numerically projected bulk source is not claimed to match every
fifth-order coefficient exactly.

See [HIGHER_ELECTRIC.md](HIGHER_ELECTRIC.md) for the phase derivation,
simplex-moment norm constants, exact partition of retained/omitted
branches, correlation bound, resource accounting and proof boundaries.

## Reproduce

From the repository root with the shared environment:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/higher-electric-round45/checker.py --output experiments/theory-contracts/higher-electric-round45/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/higher-electric-round45 -p 'test_*.py' -v
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/higher-electric-round45 -p 'test_*.py' -v
```

Twenty regression tests include independent physical source jets,
contractions, phases, simplex moments, the full cubic census, six-way
restoration, common mixed-state/Fock responses, retained remainder
branches, actual bulk and finite-parent readouts, guards and replay.
The deterministic record pins Round44 and all transitive parents and
hashes the checker, tests and both documents. Its verdict is
`EVALUATED_NEXT_ONE_E_AND_FIRST_TWO_E_WITH_SIXTH_ORDER_IDEAL_REMAINDER`.
It explicitly sets `bulk_readout_executed=true`,
`full_electric_dynamics_solved=false` and
`finite_configuration_error_included_separately=true`.

## Remaining work and firewall

The next target is controlled further propagation/resummation of the
cubic and five-factor sources, keeping the still omitted MEME/MMEE and
later first-electric branches explicit. R1M remains a major error
budget; a larger auxiliary configuration set alone cannot remove it.
An additional physical observable would provide another independent
acceptance gate. A positive upper error bound is not an impossibility
result or a lower bound on the true error.

State/parameter selection, a chiral continuum, universal spin-two
dynamics and the remaining T1-T8 obligations are still open. Only local
theory-experiment files and catalog/continuation notes are changed.
No paper, website, verification, ledger, scorecard, commit or push is
part of this round; no proof-assistant or peer-review promotion and no
observational evidence is claimed.
