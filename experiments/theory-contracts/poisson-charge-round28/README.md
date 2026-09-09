# Round28: an evaluated partition, in a declared subcase

Research only, NON-RH; no T1-T8 or physical TOE status moves. This directory
was developed **after** the Round27 paper/website publication at commit
461603b2. It is a new local research artifact, not part of that release.

Target: the original neutral, infinite-integer-charge primitive transfer
at L=T=3, a=m=beta=1, g=u=0, J=1/2592, for both nu=0 and nu=1/486.
The second case retains a genuine spatial charge-gradient interaction.
Scalar decoupling is an explicit
restriction. The original signed charge hopping remains present.

The [proof](PROOF.md) sums the complete initial charge lattice by Poisson
summation, enumerates closed words through order three, and bounds all
omitted dual modes and signed words. The checker produces an actual
partition interval with directed rational arithmetic, not a finite charge
box or floating-point convergence claim. Standard Poisson/E8-theta tools
are credited in the proof. All source inputs come from this repository;
there are no observational data or empirical scorecard entries.

From the repository root, with its existing dependencies installed:

```sh
python -B experiments/theory-contracts/poisson-charge-round28/checker.py
python -B experiments/theory-contracts/poisson-charge-round28/test_checker.py
python -B -OO experiments/theory-contracts/poisson-charge-round28/test_checker.py
```

Use `--output PATH` to save a deterministic JSON result with source hashes;
`--input-root PATH` supports isolated provenance-failure tests.
The verdict is `CERTIFIED_PARTITION_IN_DECLARED_SUBCASE`, never a claim of
arbitrary-coupling, continuum, efficient generic sign-problem or TOE closure.
Read `validation.json` for the generated numerical interval and exact
coefficient histograms. The independent regression suite also checks the
Gaussian determinant normalization, inverse neutral metric, original
non-root channel, factorial weights, and failure on corrupted source pins.

## Executed result

The complete partition is enclosed as follows (endpoints rounded outwards):

| Spatial charge coupling | Lower Z | Upper Z | Guaranteed midpoint relative error |
|---|---:|---:|---:|
| nu=0 | 2.399291166243939603314353e212 | 2.413214914832390577569586e212 | <0.291% |
| nu=1/486 | 1.384777868678860823538154e199 | 1.392814413577446187647600e199 | <0.291% |

The exact 14-test suite passes normally and with `-OO`. A deterministic
checker replay is byte-identical; one local replay of both examples took
about 1.2 seconds. This measured cost is for these two weak-hop subcases,
not an asymptotic runtime bound. A total of 104 original local words and
1008 slice allocations are evaluated; spatial symmetry supplies the
1296 and 2592 closed full-lattice word multiplicities at orders two/three.
Higher orders, including the actual negative four-hop loop, are included
in an analytic remainder bound, not enumerated or made positive.
