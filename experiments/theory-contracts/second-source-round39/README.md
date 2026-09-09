# Round39: evaluated second local source and phase-sensitive response

2026-09-07. **NON-RH / unpromoted conditional research.** The unchanged U(1)
parent gets a tighter full-bulk interval for one local physical observable.
This is not an empirical TFPT prediction, selected vacuum or T1-T8 solution.

## Result

For the same bare-low, E=0 input and model time t=1 as Round38,

**0.00169010920758 <= <n_H,x(1)> <= 0.00291608976684.**

The interval is approximately **4.35 times narrower** than Round38's. It
comes from the first explicit low-row feedback with exact free electric and
mass phases, plus a whole-Fock, volume-uniform amplitude remainder
**D2(1)<0.006444946679180**. No electric or dynamical spatial cutoff is used.

The nonlinear electric-force commutator is not silently discarded: it has
its own positive error contribution. The remaining error is mostly from
further matter iterations. The response now retains actual onsite complex
coherences for arbitrary one-fermion/site initial densities, including
entangled states. Distinct approximate phase responses still have overlapping
bulk error intervals; exact bulk phase separation has NOT been certified.

| Model time | Full-bulk high occupation |
|---|---|
| 1/100 | [0.00000104151769, 0.00000104154382] |
| 1/10 | [0.00010268476697, 0.00010294444741] |
| 1/2 | [0.00178997477322, 0.00192839016833] |
| 1 | [0.00169010920758, 0.00291608976684] |

## Derivation and execution

[SECOND_SOURCE.md](SECOND_SOURCE.md) specifies the full strong Duhamel
derivation, three separate remainder terms, electric phases, initial family,
onsite density response and costs. [checker.py](checker.py) evaluates exact
rational complex simplex polynomials with an explicit real-phase Taylor
remainder; [validation.json](validation.json) records the deterministic result
and source hashes. [test_checker.py](test_checker.py) supplies independent
full-parent matrix jets, charged-vector, CAR, phase, complete-sector, density,
geometry, numerical-remainder and provenance checks.

Validation: **25 new tests plus 244 predecessor tests (Rounds30-38), each
passing normally and with Python -OO**. The entire four-dimensional E=0
one-fermion/site edge input family additionally passes an induced-operator
error check via the independently calculated Frobenius bound, not only a
list of separate probability comparisons.

From the repository root:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/second-source-round39/checker.py --output experiments/theory-contracts/second-source-round39/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/second-source-round39 -p 'test_*.py'
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/second-source-round39 -p 'test_*.py'
```

The checker itself uses the standard library. Tests additionally use the
existing environment's SymPy. Parent provenance is pinned to Round38 and its
transitive parent chain. Both fermion species and all electric fluxes remain.

The bulk expression has 6 first and 252 second paths, collected into 218
mode/flux coefficients, not an ambient many-body vector. The fixed 7-cubed
graph enumerates only these exact radius-three paths; its ambient onsite
backtracks are retained. An 8-cubed enumeration gives the identical result.
The bound, not a dynamical window cutoff, accounts for everything beyond them.

## Independent checks and boundary

The inherited complete edge and star Gauss sectors, dimensions6 and3432,
give independent full answers inside their corresponding bounds. The full
charged vector U_(N-1)^* c_H U_N psi is checked, not only its norm square. The
edge resolves distinct exact responses for opposite coherent phases; the
second source reproduces their ordering. These trees are NOT a full cubic
lattice and have no independent loop rotors.

Parameters a=1/12, eta=1/2, beta=1/4, kappa=1/100, M=4, Vmag=0 and the bare
preparation remain declared choices. Time is in model units. This is not a
dressed low-energy sector, mirror-elimination theorem, universal reduced
Hamiltonian, selected flavor/vacuum, continuum limit or spin-two construction.
There is still only one physical local readout here, not a common multi-source
3D solver. Neither finite tests nor the narrower interval close T1-T8.

General Duhamel/local-dynamics methods are established; primary background
sources are linked in the derivation. The written bound is not formally
proof-assistant checked or independently peer reviewed. No scorecard, paper,
website, ledger, commit or push is part of this experiment-only round.
