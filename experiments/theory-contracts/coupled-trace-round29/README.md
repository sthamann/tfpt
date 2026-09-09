# Round29: genuine scalar-charge coupling through a positive trace

2026-09-07. **NON-RH; local, unpromoted research.**

The original finite-regulator E8 charge/scalar model now has four
quantitatively enclosed partition functions with **u>0**, retaining all
integer neutral charges, continuous scalar amplitudes, the original
signed hopping, and the contribution of every higher hopping order.
This extends Round28's u=0 reference by an analytic trace comparison;
it is not an exact decimal value or direct integration of all histories.

The big-picture result is complementary: Noether identities leave u
undetermined, and an exact internal geometric representation needs a
specific measure correction. Merely calling u a metric does not select it.
For this ansatz, Ricci flatness or constant scalar curvature would force
u=0; these conditions do not select a nonzero interaction.

## Results and declared physical inputs

All cases use L=T=3, N=27, beta=a=m=1, delta=1/3, g=0,
J=1/2592 and theta=1/2. Couplings are explicitly chosen, not derived from
TFPT. The full original charge Hilbert space is infinite despite the
finite spatial and temporal regulator.

| Spatial charge coupling nu | Scalar-charge coupling u | Relative-minimax estimate of Z | Guaranteed relative error |
|---|---|---|---|
| 0 | 1/65536 | 2.39228735635 x 10^212 | <0.86721% |
| 1/486 | 1/65536 | 1.38073568686 x 10^199 | <0.86722% |
| 0 | 1/4096 | 2.18379109772 x 10^212 | <9.50698% |
| 1/486 | 1/4096 | 1.26039970193 x 10^199 | <9.50699% |

The table abbreviates the estimates; the error certification applies to
the longer, outward-controlled values in [validation.json](validation.json).
The scalar covariance is exactly 167106/682465 for the same primitive
T3 transfer. The moment bound satisfies beta <W>_0 <= M <758. The
supporting-tangent estimate is

    exp(-u M) Z(0) <= Z(u) <= Z(0),
    W=sum_x e(n_x) phi_x^2 >=0.

Positivity is used for the operator trace, not for its signed word
expansion. The original negative four-hop loop remains. No field/charge
cutoff, conditional positivity assumption, or generic sign cure is used.

## Proof, geometric calculation, and reproduction

* [PROOF.md](PROOF.md): Schatten-interpolation trace lemma, unbounded
  interaction limit, charge-energy comparison, exact scalar covariance,
  complete partition enclosures, and proof boundary.
* [COMPILER.md](COMPILER.md): same-model Noether deformation test, exact
  warped-torus measure correction, why no constant curvature ordering
  removes it, and the conditional Einstein/Deser perspective.
* [checker.py](checker.py): rational enclosures and symbolic identities;
  re-executes pinned Round28 rather than trusting an isolated saved number.
* [test_checker.py](test_checker.py): 18 independent/adversarial test
  methods, including all nine source-pin mutants, all declared reference
  parameter guards, neutral-sector current controls, wrong operator-order
  rejection, and full saved-record replay.

From the repository root:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/coupled-trace-round29/checker.py
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/coupled-trace-round29 -p 'test_*.py' -v
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/coupled-trace-round29 -p 'test_*.py' -v
```

To regenerate the local record, add `--output
experiments/theory-contracts/coupled-trace-round29/validation.json` to the
checker invocation. The record hashes the proof, compiler calculation,
checker, tests and this README, as well as pinning its nine direct inputs.
The Round28 checker enforces its own prerequisite pins transitively.

Cost is a re-execution of Round28's 104 local signed-word representatives
and 1008 temporal allocations, four rational comparison intervals, and
small exact matrix/Noether calculations. It does not enumerate the charge
lattice. This workload is not an asymptotic efficiency proof; the bound
width grows with uM and the source reference still uses weak J. A positive
lower bound for general u does not give arbitrary relative accuracy.

## What is and is not resolved

Resolved here: for the declared four cases, the formerly absent u>0
partition enclosure; for the specific onsite geometric representation,
the exact measure-induced potential and the failure of a constant xi R
replacement. These are written analytic derivations with exact numerical
and symbolic controls, not independent proof-assistant certification.

Still open: a compiler rule selecting the couplings and common parent;
strong-coupling/arbitrary-accuracy and regulator-uniform evaluation;
physical 3+1D reconstruction, chiral matter and its measure, all physical
couplings, universal quantum gravity, and a derived initial state and
common real-time source functional. All physical T1-T8 requirements stay
open. No empirical score, ledger marker, paper or website is promoted.

The earlier Round28 files are preserved byte-for-byte. Round28 and Round29
remain local additions after the published Round27 release; this research
turn does not commit, push, or rebuild publication artifacts.
