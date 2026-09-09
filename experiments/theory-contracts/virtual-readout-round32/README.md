# Round32: virtual readouts and the missing local-energy premise

2026-09-07. **NON-RH / unpromoted theory experiment.**
Verdict: `CONDITIONAL_DRESSED_READOUT_AND_LOCAL_ENERGY_OBSTRUCTION`.
No empirical prediction, physical T1-T8 gate closure, or RH claim.

## Constructive result in the existing physical Gauss cell

[VIRTUAL_READOUT.md](VIRTUAL_READOUT.md) derives an explicit rational
second-order Hamiltonian retaining virtual high transitions, its local
site-occupation readout, and the required isometric initial-state encoding.
The input is the pinned Round30 four-dimensional one-fermion Gauss sector
with kappa=1/100; neither its parameters nor its Hamiltonian are replaced.

- Hamiltonian remainder norm <=243/42133000000 (<5.768e-9).
- Both low energies have this certified absolute error. Independent Sturm
  intervals sharpen the two actual errors to <=1.39e-13 and <=2.138e-12.
- For every norm-one observable and consistently encoded initial low
  state, the expectation error is <=2 epsilon_H |t|+epsilon_O,
  where epsilon_O=243/68466125000; at |t|=1 this is <1.509e-8.
- Independent exact rational real-time evaluation of the local Ny
  readout gives <=1.445188e-9 at t=1, uniformly over all encoded low
  initial vectors. The Taylor-tail contribution is below 1e-18.

These are upper enclosures in model units, not experimental errors. Using
the old bare initial state or dropping the transformed readout does not
inherit the small low-only bound. For unchanged arbitrary initial data,
the accurate dressed representation retains both dynamical blocks.

## New obstruction to extending a density estimate to every local readout

[LOCAL_ENERGY.md](LOCAL_ENERGY.md) constructs an exact physical U(1)
cycle-flux sector of the inherited signed-wall family. Concentrated
electric energy resonates with the high matter cost. At fixed t=4pi,
an initially exactly low physical state has a dressed local high readout
above 0.9413 for the declared M=204817/1600 example, even though its mean
energy is below 0.010000783 per site and its high-number density is at most
1/163840000. Analytically, the local lower bound tends to one while the
mean energy tends to 1/100 and the high density tends to zero.

The padding gauge graph is connected, but matter hopping on the spectator
links is zero. This is NOT a homogeneous interacting cubic lattice or
Round31's filled-Haar initial state. It refutes a general inference from
global energy density and a growing fiber gap alone, not those special
states or the existing averaged-density theorem. All integer fluxes are
physical; no cutoff or substitution of the old one-link sector is used.

## Positive symmetry step on the homogeneous connected lattice

There is a constructive way to add the missing premise for **population**:
on homogeneous periodic three-dimensional lattices with the Round31
filled-low Haar preparation, Hamiltonian and density matrix are translation
invariant. Thus <dGamma(Q Pi_x Q)>=<N_high>/N for every site and time.
The previously averaged bounds become uniform local dressed-population
bounds. At kappa=1/100 and M=400 this gives
min(0.00128,0.00017 abs(t)) at every site, for every torus size with sides
>=3. This uses the actual connected hopping family, not spectator padding.

The new ingredient is the exact symmetry argument, not another density
formula. It does not extend to arbitrary inhomogeneous states or the
boundaries of open boxes. Nor is small population already a comparison
of every observable: virtual terms and relative phases remain relevant.
The next target is the consistent dressed effective-dynamics comparison
on this same family, including local energy/flux-tail control as needed.

## T1-T8 boundary and provenance

This advances one finite-sector part of T4, respecting the inherited
Gauss constraints relevant to T3. T4's uniform interacting mirror gap and
T3's physical chiral measure remain open. No compiler-unique bulk (T1/T2),
continuum (T5), physical flavor selection (T6), graviton (T7), or selected
state (T8) is derived. These are not eight independent models being added
up and called a TOE.

Three Round31 artifacts are pinned, followed by Round31's Round30 pins and
their transitive provenance. Five new sources are SHA-256 recorded in
validation.json. The standard unitary reduction idea is contextualized by
[Bravyi, DiVincenzo and Loss (2011)](https://arxiv.org/abs/1105.0675);
the model-specific estimates are derived explicitly here, without importing
their bounded-spin assumptions into an unbounded-rotor theorem.

## Reproduce

From repository root, using the existing SymPy environment:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/virtual-readout-round32/checker.py
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/virtual-readout-round32 -p 'test_*.py' -v
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/virtual-readout-round32 -p 'test_*.py' -v
```

Add `--output experiments/theory-contracts/virtual-readout-round32/validation.json`
to regenerate the deterministic record. Thirty tests check independent
Sylvester vectorization, commutator coefficients, sign and source-omission
mutants, exact time/energy enclosures, Gauss constraints, resonance tuning,
strict-low preparation, asymptotic density/local-readout separation,
periodic vertex/link translation covariance, inherited local constants,
source pin rejection and byte-identical replay. Enforcement uses explicit exceptions
and remains active in optimized Python.

The dynamical computations use matrices of dimension at most four, and
translation witnesses reach 36 sites and 108 oriented links. The general
flux, padding and periodic-volume statements follow from the written
invariant-sector, symmetry and analytic arguments, not from simulation of
millions of sites. There is no
efficient generic many-body or arbitrary-volume solver here. The arguments
are not proof-assistant or independently peer-review certified.

Experiment firewall: no verification, ledger, scorecard, paper, website or
generated public status is changed. No promotion, commit or push is part
of this local research round.
