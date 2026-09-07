# NON-RH Round26: summed-history error control, with the real signs retained

2026-09-07. Local research on HEAD and actual origin/main
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`, verified this round.
No commit/push, paper/web release, ledger or empirical promotion.
Prior local evidence and concurrent paper/ledger/v472 changes remain.

## New bridge: the estimates now reach a summed partition and observables

The [summation contract](history-sum-control-round26/PROOF.md) defines the
positive symmetric transfer operator of the ORIGINAL g=0 scalar/charge
model at finite spatial volume and a finite Euclidean time regulator.
It works in the neutral total-charge sector, with all integer charges,
any J>=0 and positive scalar mass. No small-hopping window is used.

Its full signed history expansion is absolutely convergent. With the
original hopping constant kappa=48NJ retained, the bounds are

    Z_abs <= Z_phi,0 Theta(beta),
    Z >= exp(-beta kappa) Z_phi,0 > 0.

The exact E8 Gram matrix gives D(n)>=||n||^2/(62N) and an explicit finite
integer-Gaussian bound for Theta. The unsigned shifts are used only as
an absolute comparison; the physical phases are not deleted. The lower
bound comes from a positive-operator compression, not a claim that the
zero-charge state is invariant under interacting evolution.

Consequently, errors in conditional Gaussian factors can be propagated
to the SUMMED partition and bounded one-time charge observables. The
proof keeps the possibly enormous cancellation factor
exp(beta kappa)Theta(beta). It is not an efficient or volume-uniform cure
of the sign problem.

The conditional determinant estimate is also sharpened: the full temporal
mass operator bounds the retained inverse trace. This avoids counting
every temporal mode with the worst zero-frequency bound and removes that
spurious linear-in-T factor under time refinement. The result remains
extensive in spatial volume and is not a continuum construction.

## Constructive finite tails, with an executable conservative planner

Explicit bounds now control both histories leaving a sampled charge box
and words exceeding a TOTAL hop order. The latter is a factorial/Poisson
tail, valid at arbitrary fixed J when the order is sufficiently large.
The charge bound retains the half-time-slice split and its cost under
time refinement. Intermediate charges inside one exponential word are
not clipped by an unproved boundary-only estimate.

The [exact rational planner](round26_algebra.py) has been run for
N=27,T=3,beta=1,J=1/10. Keeping full scalar memory, its conservative choices

    charge-coordinate box K=4096,
    total hop order P=962

certify a combined omission error below 1/100 of the exact partition.
This is a certified TRUNCATION PLAN, not a computed one-percent partition
value or a parameter-fixed physical prediction. The complete sum was
not evaluated; Gaussian/transcendental evaluation would need an additional
numerical precision budget. The naive candidate-count envelope has a
decimal-digit upper bound of 3846. That is a combinatorial cost warning,
not a measured runtime, necessary lower bound or efficient algorithm.

For the memory approximation, a separate error term enters the same
summed bound. Nonzero memory removal may be useless under the large
cancellation budget; the planner does not silently omit that term.

## Negative result: the cocycle signs cannot simply be rephased away

The [sign contract](cocycle-sign-obstruction-round26/PROOF.md) exhibits
an actual closed four-hop word on three adjacent sites of the L3 torus.
Two different E8 channels with odd Gram pairing give total phase -1.
All intermediate charges are neutral and unwrapped. The product of the
four Hamiltonian matrix elements is -J^4 for J>0.

Any diagonal rephasing of the full charge-configuration basis telescopes
around the loop and leaves that sign unchanged. It therefore cannot make
all off-diagonal hopping entries nonpositive. Positive scalar integration
does not erase this word: the checker retains all 108 scalar space-time
coordinates of its T=4,N=27 history.

This rules out only that basis-rephasing cure. It is NOT an intrinsic
sign-problem theorem for every representation, regrouping, auxiliary
construction or QMC algorithm, and one word is not the full partition.

## Evidence and remaining obligations

Two checkers have 22 and 14 exact groups, with twelve source pins each.
The aggregate reruns 27 prerequisite checkers. There are 33 separate
infrastructure/source/semantic fixtures, including ten wrong variants.
New checkers and fixtures pass normally and under optimized Python;
the optimized runs use /tmp. Analytic proofs and finite checks are
distinct; no independent-human or proof-assistant certification is claimed.

See [review](ROUND26_REVIEW.md), [fixture evidence](ROUND26_RUNNER_VALIDATION.json)
and [aggregate evidence](ROUND26_VALIDATION.json). In the research environment:

    python -B experiments/theory-contracts/test_round26_runner.py
    python -B experiments/theory-contracts/run_round26.py
    python -B experiments/theory-contracts/run_round26.py --check-manifests

Absolute convergence and certified finite summation errors are established
for this neutral finite regulator, but practical cancellation control and
an executed complete interacting calculation remain open. So do uniform
volume/continuum limits, real-time reconstruction, full g!=0 gravity,
microscopic parent/parameter selection, observed chiral matter/flavor,
local relativistic stress, native observables, spectators and external
predictions. No T1-T8/TOE/RH or empirical promotion.
