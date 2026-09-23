# Round37: explicit local 3D window and rotor error bounds

**NON-RH, unpromoted conditional theory contract.** Verdict:
`EXPLICIT_VOLUME_UNIFORM_LOCAL_WINDOW_AND_FLUX_BOUND`.
No T1-T8 gate is closed. The large-window evolution has **not** been executed.

## New result

The unchanged unrotated U(1) signed-wall parent now has an explicit spatial
window error bound, independent of the surrounding lattice volume, together
with a factorial electric-tail estimate for initially flux-supported states.
This extends the research beyond a finite cycle and a global flux family.

The stated preparation is one bare-low fermion per site and E=0 on every link,
with an arbitrary coherent or mixed low/high species state on a fixed local
patch. All these inputs have the same one-fermion-per-site Gauss charge. For
four patch sites this is a whole 16-dimensional input subspace, not a set of
sampled basis states. It is not a selected vacuum or a full low-energy spectral
space. In particular it is NOT the dressed filled-Haar preparation; that state's
initial flux tail would require an additional error estimate.

The model parameters remain a=1/12, beta=1/4, eta=1/2, kappa=1/100, M=4, Vmag=0.
The spatial theorem controls all bounded even local sources. High occupation,
electric-zero probability, species coherence and a real square Wilson loop
are concrete norm-one gauge-invariant examples. All high fermion modes remain.

## Concrete bound, with its full cost

For sources on at most four cells in a 2x2x1 box, time |t|<=1 and an enclosing
window expanded by 64 lattice steps, electric cutoff K=12 gives:

- Spatial source error <1.083873e-10.
- Full-rotor source error <1.962411e-11 for the specified initial support.
- A specified, unexecuted rational integration plan adds <1.262378e-11.
- Combined conditional source error <1.406352e-10, hence below 1e-9.

The bound holds uniformly over the entire preparation family and over compatible
ambient volumes. But its conservative window contains **2,180,100 vertices and
6,489,860 dynamic rotors**. A direct finite representation has dimension
`4^2180100 * 25^6489860`. The recorded integration plan would take 29,108,451
degree-61 exact Taylor steps on that immense space. No practical solver,
large-volume readout, speedup or minimum resource requirement is claimed.

The reduction must retain the original onsite backtracks of A^2. Rebuilding
the polynomial from the induced window adjacency omits boundary terms and
changes even the relative phase of a local low/high superposition. This is
guarded by an explicit physical counterexample.

## Actual calculations and proof

The executable checks real open 2x2x2 and 3x3x3 cubes and periodic 3x3x3 and
4x4x4 lattices, exact interaction/path incidence, Gauss-preserving transitions,
and local initial derivatives. In the degree-six bulk the coefficients of t^2
are 1/96 for high occupation, 1/288 for nonzero link-flux probability and 1/48
for onsite species coherence. These derivatives are **not** finite-time
predictions. Tests compare against an independent Laurent-matrix expansion
and an independent full second jet on the eight-site cube.

[LOCAL_WINDOW.md](LOCAL_WINDOW.md) gives the support-chain proof, the
unbounded-onsite domain justification, the per-link Dyson argument, source and
preparation accounting, numerical-error construction and remaining limitations.
The general locality method is established; see
[Nachtergaele and Sims](https://arxiv.org/html/1410.8174v1) and
[Barthel and Kliesch](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.108.230504).
The experiment supplies the explicit inherited-parent constants and composition,
not a new fundamental law or the invention of Lieb-Robinson bounds.

## Reproduce

The checker itself uses only the standard library. Tests additionally use the
repository's existing SymPy environment.

```bash
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/local-window-round37/checker.py --output experiments/theory-contracts/local-window-round37/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/local-window-round37 -p test_checker.py
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/local-window-round37 -p test_checker.py
```

Inspect another window's bound and resource plan, without running its evolution:

```bash
python3 experiments/theory-contracts/local-window-round37/checker.py --radius 64 --cutoff 12
```

The validation records exact fractions, geometry and initial-derivative results,
the 40/48/56/64 spatial-margin scan, and source hashes. Parent checks pin Round33
and verify its transitive provenance. No empirical data or old finite-cycle
answers are used to fit this bound. A passing suite validates the implemented
algebra and budgets; the written analytic proof is not formally mechanized.

## Next acceptance test and firewall

The next task is an actually evaluated, manageable local-source or connected
cluster calculation with controlled residuals for the same 3D parent. A smaller
spatial window alone may still have prohibitive state cost. Spectral elimination,
chirality, a physical vacuum, continuum gravity and the complete T1-T8 conjunction
remain open. The Round36 60-state generator has not been certified on this lattice.

Following the experiment workflow, only research artifacts and the experiment
catalog/notes are updated. No verification, paper, website, ledger, empirical
scorecard or public TOE status changes are made.
