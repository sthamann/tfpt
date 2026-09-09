# Round41: nonlinear electric source and a certified correlation witness

2026-09-07. **NON-RH / unpromoted same-parent research.** No T1-T8 gate,
chiral sector, physical vacuum or parameter selection is declared solved.
This adds an explicitly calculated electric branch to Round40's matter
hierarchy, instead of treating the entire electric response as an error.

## Result

The unchanged U(1) parent produces a cubic fermion source
c_a^dagger c_b c_L,y with two distinct electric phases. All 156 force paths
are evaluated. A new uniform remainder controls its omitted propagation;
the old first-electric budget is replaced, not counted twice. At t=1 the
amplitude bound falls from approximately 0.000270570888 to 0.000218044017.
For the original bare-low E0 input, the full-parent occupation interval is
**[0.00217694175355, 0.00221782566303]**, about 1.24 times narrower.

The new source restores the previously missing exact third time coefficient.
It also sees correlations that the matter-only response cannot see. Two
neighboring-site Bell preparations (LL-iHH)/sqrt2 and (LL+iHH)/sqrt2 have
identical I/2 single-site species densities, zero onsite coherence and E=0.
Nevertheless their conditional full-cubic responses are provably different:

| Time | Minus phase | Plus phase |
|---|---|---|
| 0.01 | [0.50000043397108, 0.50000043397314] | [0.50000043396529, 0.50000043396736] |
| 0.02 | [0.50000173518060, 0.50000173521415] | [0.50000173513447, 0.50000173516802] |

The rational certified gaps exceed **3.7e-12** and **1.25e-11**, including
the full same-parent remainder. This rules out an exact response based
only on all initial one-site densities for the stated preparation class.
It is a small mathematical model witness, not an observable-world prediction.
At t=1 the two Bell intervals still overlap: separation there is NOT proven.
Round40's separate single-site phase separation at t=1 remains certified.

For this approximating response on exactly-one-fermion/site initial states,
the necessary correlations have a proved ceiling of three-site species
reduced densities, without a factorization assumption. Common exact rational
4x4 and 8x8 response matrices handle arbitrary coherent or mixed states on
the corresponding declared patch, bare elsewhere. This is not an exact
all-time three-site closure or an eight-state physical bulk model.

See [ELECTRIC_SOURCE.md](ELECTRIC_SOURCE.md) for the branch identity, phase
derivation, operator bound, correlation selection proof, exact third
coefficient, finite-time intervals and limitations.

## Reproduction and evidence

From the repository root, using the existing shared Python environment:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/electric-source-round41/checker.py --output experiments/theory-contracts/electric-source-round41/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/electric-source-round41 -p 'test_*.py' -v
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/electric-source-round41 -p 'test_*.py' -v
```

The checker pins Round40 and its transitive parents; the deterministic
record hashes the new checker, tests, derivation and README. Inputs are
those local parent artifacts, not external observational data. Rational
complex arithmetic and outward analytic tails control numerical error.

The 25 regression tests cover full rectangular Liouville expansion through
two interactions, whole charged edge-family evolution with both propagator
tails, independent complete 6/3432-state tree sectors, CAR/Fock ordering,
large fluxes, Gauss covariance, the restored coefficient, identical Bell
marginals and nonzero-time separation, mixed-state positivity, common
two-/three-site matrices, spectator independence, source pins and replay.
Run both normal and optimized Python; essential guards use explicit checks,
not removable assertions. These are not proof-assistant or peer-review
certificates. The complete trees are independent benchmarks, not full 3D.

Verified on 2026-09-07: all 25 new tests plus all 293 predecessor tests from
Rounds30-40 pass in both modes, **318 tests per mode**, including deterministic
replay. The predecessor sources and their pinned validation records are
unchanged.

The source uses the inherited 140372 linear mode/flux coefficients plus 156
cubic coefficients; only the small cubic output columns are materialized.
No full lattice Fock state, rotor cutoff or dynamical spatial window is
introduced. The inherited enumeration cost remains; no total speedup or
arbitrary-time solver is asserted.

## Scope and next acceptance gate

Declared couplings, the E0 preparation class and exactly one fermion per
site are assumptions, not results of TFPT state selection. The bound is
volume-independent at fixed spacing; no continuum, Lorentz, confinement,
mirror-elimination or spin-two result follows. T1-T8 remain open under the
requirements recorded in Round30. This specifically advances the conditional
T3/T4 dynamics machinery and the correlation requirements of T8.

Next: propagate the nonlinear electric source further and include the next
first-electric branch, with an explicit same-parent bound and correlation
accounting. Then extend compatible physical readouts of the common source
functional. Merely increasing matter depth leaves electric branches missing.

The TFPT experiment firewall keeps this work local to theory contracts and
the experiment catalog/notes. No empirical scorecard, verification ledger,
paper, website, commit or push is changed by this round.
