# Round42: propagated electric sources and a fifth-order error bound

2026-09-07. **NON-RH / unpromoted same-parent research.** This closes a
specific source-expansion omission, not T1-T8 or the full gauge dynamics.
Couplings, initial E=0, and exactly one fermion per site remain declared
assumptions, not TFPT-selected physical constants or a vacuum.

## What is now calculated

Both missing fourth-time-order contributions are explicit: matter
propagation of the first cubic electric word (MEM) and the next electric
force after two matter steps (MME). The first double-electric branch stays
in a separate nonzero bound. The same unrotated U(1) parent, all fluxes,
original onsite backtracks and source preparation are retained.

The source now agrees with the complete edge Hamiltonian through time
order FOUR on the whole E0 initial family. Its uniform omitted-source
bound begins at order FIVE. At t=1 it falls from approximately
0.000218044017 to **0.000166811991**, a further 23.5% reduction. For the
original bare input the full-cubic occupation interval becomes
**[0.00218195851226, 0.00221323792966]**.

A correlation witness is certified at a longer nonzero time. At t=0.1,
the neighboring-site states (LL-iHH)/sqrt2 and (LL+iHH)/sqrt2 have intervals:

| Preparation | Conditional full-parent occupation interval |
|---|---|
| Minus phase | [0.50004282065582, 0.50004282531676] |
| Plus phase | [0.50004281536577, 0.50004282002672] |

Their exact separation lower bound exceeds **6.29e-10**, including all
omitted dynamics. Round41's intervals overlap at this time. Both inputs
have identical I/2 single-site species densities and the same initial
fluxes; the difference requires correlation information. This is a small
conditional model result, not an empirical prediction. At t=0.5 and t=1,
the Bell intervals still overlap: separation there is not established.

## Structural simplification

Matter commutators preserve CAR word degree. Therefore any number of
matter steps around exactly one electric branch remains cubic, with a
proved sufficient correlation ceiling of three-site species densities
on the one-fermion/site initial class. A factorial majorant proves uniform
operator-norm convergence of that one-electric sector at bounded time.

Only its terms through three interactions are NUMERICALLY EVALUATED here.
The all-order sector is not the full dynamics; two electric branches can
generate five-factor words. Nor does the three-site ceiling mean only three
fixed sites matter, or that the full evolution has an exact three-site
closure. Common 4x4/8x8 matrices describe patch preparations with bare
filling elsewhere, including coherent and mixed inputs without state fits.

The derivation, complete phase formulas, bounds and scope are in
[ELECTRIC_PROPAGATION.md](ELECTRIC_PROPAGATION.md).

## Reproduce

Use the existing shared Python environment from the repository root:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/electric-propagation-round42/checker.py --output experiments/theory-contracts/electric-propagation-round42/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/electric-propagation-round42 -p 'test_*.py' -v
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/electric-propagation-round42 -p 'test_*.py' -v
```

The deterministic record pins Round41 and its transitive parents and hashes
this checker, tests and two documents. No observational dataset is used.
The 20 tests include full-parent source jets through order four, full charged
edge and three-site initial families, complete 6/20/3432-state Gauss-sector
benchmarks, force census, large-flux phase identities, Gauss covariance,
simplex moments, norm constants, finite-time Bell separation, the explicit
nonseparation boundary, mixed densities, common matrix restrictions,
time reversal, numerical tails, mutation guards and replay.

Verified on 2026-09-07: all **20 new tests plus 318 predecessor tests** from
Rounds30-41 pass in normal and optimized Python, **338 tests per mode**.
The predecessor sources and pinned records are unchanged.

All 18792 MEM plus 15912 MME raw paths are evaluated. Exact collection yields
57150 frequency/word/flux groups, 139 scalar kernels and 23010 nonzero new
cubic coefficients at t=1, beside the inherited 140372 linear coefficients.
The new numerical amplitude tail is below 9.427e-51 at t=1, separate from
the physical remainder. No full lattice Hilbert space is assembled; the
enumeration and large exact integers still cost real resources. There is
no total speedup, proof-assistant or peer-review claim.

## Boundary and next target

The fifth matter branch accounts for about 79% of the t=1 remainder and is
the next dominant target. It must be reduced while retaining explicit
control of double-electric branches and compatibility with further physical
readouts. None of this by itself selects a chiral 3+1D parent, physical
state, continuum theory, flavor parameters or universal spin-two sector.
All T1-T8 completeness gates remain open.

The TFPT experiment firewall keeps this as local theory-contract work and
experiment catalog/notes. No paper, website, verification ledger, empirical
scorecard, commit or push is changed by this round.
