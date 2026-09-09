# Round34: closed memory evolution and unchanged physical readouts

**NON-RH. Unpromoted theory contract.** Verdict:
`CLOSED_MEMORY_EVOLUTION_WITH_SOURCE_RECONSTRUCTION`.
No physical T1-T8 gate is closed and no empirical scorecard row is created.

## Result

The retained-amplitude memory equation is now **actually evaluated** for the
unchanged Round33 three-site U(1) cycle. All four matter/gauge readouts reproduce
the frozen full-dynamics certificate, with identical rational interval endpoints
and a full-rotor absolute error at t=1 of at most 9.3081e-14 at cutoff K12.
The comparison includes every excluded integer electric flux through the
inherited analytic bound, not through an assumption that two cutoffs suffice.

| Full physical observable | Certified t=1 interval, K12 |
|---|---|
| High-mode occupation at site 0 | [0.00071934464413, 0.00071934464432] |
| Probability E0=0 | [0.99928328547964, 0.99928328547983] |
| Onsite low/high coherence | [-0.00404633584758, -0.00404633584738] |
| Real cycle Wilson loop | [0.00000021720204, 0.00000021720223] |

The initial state remains the bare-filled, zero-flux state with three fermions
and background charge one per site. The parameters remain a=1/12, beta=1/4,
eta=1/2, kappa=1/100, M=4 and Vmag=0. This is **not** the earlier dressed Haar
state, a selected vacuum, or a three-dimensional lattice calculation. The
retained bare-occupation subspace is not a low-energy spectral band.

## What was solved and what was not

The equation for p=P psi is

\[
\dot p(t)=-iLp(t)-\int_0^t C^\dagger e^{-iD(t-s)}C p(s)\,ds.
\]

Its parent-derived memory moments evolve only the retained components. Source
maps reconstruct the eliminated components at the final readout; keeping those
source terms is essential for all four observables. Neither the full-state
propagator nor the frozen answer enters this recurrence. An independent test
compares **every component** of its polynomial with the full-state Horner
calculation, not only the four reported numbers.

The source correction is physically significant within the model: simply
using the unnormalized P-only Wilson readout gives a strictly negative value
near -8.55845e-5, whereas the full value is positive near 2.17202e-7. A small
discarded probability is therefore not enough to justify dropping these sources.

The projection method itself is established, not a new TFPT discovery; see
[Chruscinski and Kossakowski](https://arxiv.org/html/1302.6218v3).
The new work here is its certified evaluation on the inherited Gauss-constrained
parent and the explicit source, preparation, and cost accounting. The analytic
derivation, assumptions and remaining bridge are in
[MEMORY_CLOSURE.md](MEMORY_CLOSURE.md).

Three useful restrictions are made explicit:

- A time-independent Hamiltonian on this **same bare retained subspace**, with
  unchanged preparation, cannot reproduce its exact projected propagator:
  its second derivative misses C^dagger C. The actual all-bare-low survival at
  t=1 is [0.99784311496210, 0.99784311496230], not one. This does not rule out
  dressed or controlled approximate effective descriptions.
- The first memory moment contains the exact signed nearest-flux coefficient
  -1/2304. Its leading large-mass interpretation gives the same induced triangle
  Wilson term as Round33, without inserting a new magnetic coupling. This is
  not a bound on the error of a memoryless approximation.
- The closed finite cycle does not supply an automatically decaying memory
  kernel. At K12 one kernel entry has long-time mean square at least 1/4267008;
  the uncut fixed cycle also has pure-point spectral recurrence. A short history
  window needs a separate oscillatory or low-energy error argument.

## Reproduction and checks

From the repository root:

```bash
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/memory-closure-round34/checker.py --output experiments/theory-contracts/memory-closure-round34/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/memory-closure-round34 -p test_checker.py
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/memory-closure-round34 -p test_checker.py
```

The deterministic validation records both cutoffs, interval comparisons,
source-omission diagnostics, exact kernel/source hashes and four artifact
hashes. Three direct Round33 pins and transitive source checks guard provenance.
The benchmark is compared only after solving; a changed benchmark causes an
error, not a refit. Cached certification still rechecks provenance.

Tests cover independent non-diagonal block powers; entire physical state-vector
equality; source and memory omission mutants; the unchanged initial state;
normalization and nonunitary projection; the elementary Wilson sign; both flux
cutoffs; minimum polynomial degree; source pin and benchmark mutants; exact
replay and normal/optimized execution. The mean-square memory bound is checked
from the actual source norm and independent spectral-weight examples.

## Explicit costs and firewall

At K12, the recurrence has 25 retained components per jet, but compilation uses
the full 463-dimensional eliminated sector. It stores **49,375 memory integers
and 926,000 source integers**, of growing bit length, plus parent matrices and
other arrays. The final readout reconstructs all high components. At K8 the
corresponding counts are 17 retained, 311 eliminated, 22,831 memory integers
and 422,960 source integers. Both cutoffs may be cached simultaneously.
**No speedup or smaller total memory footprint is claimed.**

Degree 80 is a certified Taylor order; it is not a finite history duration.
The result is an exact-memory reformulation with a controlled numerical
evaluation, not a memoryless effective Hamiltonian or uniform local 3D EFT.
All physical T1-T8 requirements, including physical parameter/state selection,
chiral/continuum identification and full gravity, remain unpromoted. Papers,
website, ledger, verification suite and empirical scorecard are unchanged.

The next acceptance test is a genuinely simpler, controlled low-energy/local
description that reproduces these same observables with its preparation and
source corrections, followed by a volume-uniform local-readout comparison on
the actual three-dimensional dynamical lattice. The present exact-memory
benchmark is a reference for that test, not a substitute for it.
