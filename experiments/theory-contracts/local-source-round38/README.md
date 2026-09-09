# Round38: an actually evaluated local 3D readout without a giant window

**NON-RH, unpromoted conditional theory contract.** Verdict:
`EVALUATED_VOLUME_UNIFORM_LOCAL_HIGH_OCCUPATION_INTERVAL`.
This is one observable's certified interval, not a full 3D solver or T1-T8 closure.

## Result

For the unchanged unrotated U(1) cubic parent, the bare filled-low, zero-electric-
flux preparation has at unit model time

**0.00031949062781 <= local high occupation <= 0.00565070454854.**

The bound is independent of the surrounding lattice volume and includes every
electric flux and all high fermions. It is actually evaluated with scalar
rational arithmetic, without a spatial window, a flux cutoff or a full lattice
state vector. At t=1/100 the interval is
`[0.00000103570437, 0.00000104736828]`.

This does not deliver Round37's unexecuted high precision at lower cost: the
new unit-time interval is much wider. It gives a nontrivial finite-time local
answer where the previous direct-window computation was not performed.

## How it works

The high annihilation operator obeys an exact local source equation. Replacing
the transported low-mode sources by their free evolution retains the entire
mass and electric phases. A whole-Fock CAR row bound C^2=107/2048, together
with the electric force bound b=53/288, controls the entire omitted source
contribution. At t=1 the annihilator error is below 0.02864843378435.
Triangle inequalities turn that amplitude error into a probability interval.

The phase gap is exactly 9587/2400; the original onsite backtrack and the
electric half-step are both present. This is not the old t^2 derivative
reported as a finite-time answer. [LOCAL_SOURCE.md](LOCAL_SOURCE.md) gives the
complete argument, assumptions, exact arithmetic and boundaries.

Parameters remain a=1/12, beta=1/4, eta=1/2, kappa=1/100, M=4, Vmag=0. They and
the preparation are declared model choices, not selected TFPT constants or a
physical vacuum. The sharp cubic row bound assumes an ordinary bulk neighborhood;
small three/four-site wrapping aliases are excluded. The infinite-volume statement
is a fixed-lattice one, not a continuum or gravity result.

The same interval construction covers arbitrary coherent or mixed local
one-fermion-per-site preparations at initial E=0 using their local occupation
marginals. It does **not** declare different phases equivalent: only the
interval is shared, and full benchmark evolutions with opposite phases differ.
The dressed filled-Haar state is not silently substituted for this input class.

## Independent checks

The certificate checks all 42 relevant row monomials on actual 5x5x5 and 6x6x6
cubic tori. Tests also check 7x7x7. Independent full-parent rational evolutions
cover a six-state edge and a 3,432-state, seven-vertex star with six gauge links.
At t=1 the star gives `[0.00219096851702, 0.00219096851703]`, inside the local
bound. These are complete TREE Gauss sectors, not cubic lattices; the full-cubic
claim comes from the analytic source bound, not from transplanting the star.

Tests compare the entire charged source vector against the local approximation,
not only its probability, and check CAR norms, rotor phases, the physical gap,
coherent phases, polynomial remainders, Gauss, parent pins and deterministic replay.
The proof is written mathematics with exact arithmetic checks, not a formally
mechanized proof or empirical confirmation.

## Reproduce

The standalone readout requires only Python's standard library:

```bash
python3 experiments/theory-contracts/local-source-round38/checker.py --time 1
python3 experiments/theory-contracts/local-source-round38/checker.py --time 1/100
```

Rebuild provenance and complete-sector benchmarks; tests use the existing SymPy
environment:

```bash
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/local-source-round38/checker.py --output experiments/theory-contracts/local-source-round38/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/local-source-round38 -p test_checker.py
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/local-source-round38 -p test_checker.py
```

The scalar CLI uses fixed constants from the documented certificate. Parent
provenance is checked by the full rebuild, which pins Round37 transitively. An
arbitrarily edited script is not certified merely because the CLI produces output.

## Next boundary and firewall

A second source iteration should explicitly retain low-mode feedback and
electric phase corrections, narrow the unit-time interval and extend to the
other physical readouts. No complete four-source dynamics or common reduced
generator is supplied here. Finite-time production of bare high occupation is
not a no-go theorem for dressed spectral effective theories.

The experiment workflow keeps this result in research artifacts and catalog/
notes. No verification, paper, website, ledger, empirical scorecard or public
T1-T8 status is changed. Chirality, vacuum/parameter selection, continuum gravity
and the full TOE problem remain open.
