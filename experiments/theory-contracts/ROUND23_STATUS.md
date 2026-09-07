# NON-RH Round23: locality decided, restricted dynamics controlled

2026-09-07. Local research on HEAD and actual remote main
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`, verified this round.
No commit/push, paper/web release, ledger or empirical promotion.
Previous local evidence and concurrent paper/ledger/v472 changes remain.

## Positive result: an explicit full-dynamics comparison

The [soft-sector contract](soft-sector-round23/PROOF.md) now supplies an
all-time operator-norm error bound between the ORIGINAL dynamics and the
changed continuous-translation completion. On the actual g=nu=0 slice,
prepare a state in the exact lowest charge band with at most M free scalar
quanta. Neither interacting Hamiltonian is projected or truncated. Then

    ||(U_lambda(t)-U_av,lambda(t)) P_(band,M)||
       <=min(2, 4 lambda |t| sqrt((M+1)(M+2))
                            (1+2eps)/(m N)),
    eps=48N^2 J<=1/32, m>0, lambda>=0, J>0.

All integer charge states and all other continuous species remain. The
bound uses Duhamel comparison along the free orbit, not an assumption
that interactions preserve the preparation subspace. For scalar-vacuum
preparations the sharper coefficient is sqrt(3) lambda |t|(1+2eps)/(mN).
Bounded-observable expectation differences inherit a corresponding bound.

The same comparison is proved for the positive-frequency clock generated
by sqrt(12H), with an extra factor sqrt(3/gamma) from the retained common
positive lower bound gamma. Its square-root resolvent integral is norm
convergent on the preparation space, without assuming the full interaction
bounded. This uses the common canonical initial-data chart, not an
unproved identification of the old source/Gaussian maps.

This is a controlled DILUTE comparison. It becomes small at fixed M,
lambda,m,t as N grows, with J forced to scale at most as N^(-2). At finite
density M proportional to N it need not vanish. Both interactions are
weak on these preparations; this is not a nontrivial relativistic continuum
construction, arbitrary-J result or bound on unbounded stress observables.

## Exact soft compression is useful, but not an effective evolution

For Fourier cutoff kappa with 4 kappa<L, the original and averaged common
parent have identical forms on the specified compressed core: discrete
momentum conservation cannot hide a nonzero multiple of L within that
frequency range. This applies to the full degree-four positive parent,
including its 35 continuous species. Integer charge magnitudes are not cut.

However, starting with the physical scalar vacuum and a zero-character
charge-band state, the original interaction can create two equal hard
scalar quanta and shift charge momentum by one. Their total signed
momentum is L, not zero. Averaging removes that transition. Its amplitude
is bounded away from zero at any fixed positive J in the certified window.

The difference in hard-mode escape probabilities is therefore
lambda^2 t^2 D_leak+o(t^2), with explicit positive lower and upper bounds.
This is actual short-time dynamics requiring only an operator domain,
not a presumed convergent perturbation expansion. It is consistent with
the all-time upper bound above. Identical compressed forms alone would
have missed it.

The scalar reference vacuum is explicitly matched to its physical free
frequency. The dynamical projection leaves the other free species alone;
it does not assume that an arbitrary auxiliary reference vacuum is
stationary. This distinction was added after a failing/passing domain
consistency regression, without changing the Round22 symmetry generator.

## Negative result: this completion is not a local stress solution

The [locality contract](translation-locality-round23/PROOF.md) now gives
an EXACT witness rather than only describing the construction as nonlocal.
Two bounded, neutral, on-site charge projectors are separated by (L-1)/2.
Their double commutator with the conserved momentum has a matrix element
of magnitude pi/[La sin(pi/L)]>=1/a. The conserved generator cannot be
the sum of uniformly local stress densities on the original observable net.

More importantly, the averaged HAMILTONIAN itself has a nonzero double
commutator between those supports, whereas the original one has zero.
Its magnitude is 2 lambda/[L N^2 sqrt(m omega_e1)]. This produces a real
first-time-derivative effect at arbitrary separation, with an inverse-
seventh-power lower bound at fixed lattice spacing and parameters.
It excludes the stated volume-uniform exponential small-time locality
estimate. Positivity and exact global momentum conservation remain valid.

Neither a different observable net, power-law/state-dependent estimates
nor a carefully scaled continuum is ruled out by this finite-regulator
test. But this exact global momentum cannot simply be renamed a local
relativistic stress solution.

## Reproducibility and next obligation

Two new exact checkers have 38 and 49 groups, with 11 pinned sources each.
The aggregate separately runs 21 predecessor checkers. There are 28
infrastructure/source/semantic fixtures, including five isolated mutants:
wrapped selection, an unsafe cutoff, Bose normalization, the missing second
Duhamel term and the wrong reference vacuum. Each pinned source is tested
both missing and changed against both consumers. Normal and optimized
checks are separate from source-hash consistency and analytic proof review.

See [review](ROUND23_REVIEW.md), [fixture evidence](ROUND23_RUNNER_VALIDATION.json)
and [aggregate evidence](ROUND23_VALIDATION.json). In the research environment:

    python -B experiments/theory-contracts/test_round23_runner.py
    python -B experiments/theory-contracts/run_round23.py
    python -B experiments/theory-contracts/run_round23.py --check-manifests

The next substantive problem is a nontrivial, physically selected scaling
and local effective dynamics at finite density, with hard-mode effects and
full gravity controlled. The dilute comparison does not solve that problem.
Microscopic selection, chiral observed matter/flavor, native observable-net
identification, full gravitational constraints, spectators and external
parameter-fixed predictions remain open. No T1-T8/TOE/RH promotion.
