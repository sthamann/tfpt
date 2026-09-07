# NON-RH Round25: moving-history memory and an exact determinant solver

2026-09-07. Local research on HEAD and actual origin/main
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`, verified this round.
No commit/push, paper/web release, ledger or empirical promotion.
Prior local evidence and concurrent paper/ledger/v472 edits are preserved.

## New result: moving charges have a controlled scalar memory kernel

The [memory contract](moving-history-memory-round25/PROOF.md) no longer
requires static or slowly moving charge profiles. At the specified finite
Euclidean time regulator of the ORIGINAL local g=0 parent, it covers every
finite integer charge history, arbitrary charge jumps and density. There
is no small-J or J=O(N^-2) assumption in this CONDITIONAL result.

The positive Dirichlet energy bound b of the eliminated cell gives an
exponential bound on every time block of its inverse. The proof uses
ordered temporal walks, so it neither commutes different time-dependent
spatial matrices nor assumes an upper bound on the charge potential.
Periodic time images and both time directions are included exactly.

Keeping a cyclic temporal window of radius R gives

    ||K_R-K|| <= delta^2 c^2 tau_R,
    tau_R=delta q^(R+1)/[sinh(alpha)(1-q)(1-q^T)],
    cosh(alpha)=1+delta^2 b/2, q=exp(-alpha), c=6/a^2.

These are volume-uniform kernel constants, not multiplied by cell count.
If delta c^2 tau_R<m^2, the truncated scalar kernel stays positive.
At b=4,delta=3/4,T=9,R=3,c=6,m=1, the normalized error bound is
8192/145635, less than 0.057 and safely below the retained mass gap 1.
This is a kernel bound, NOT a 5.7-percent accuracy claim for all observables.

The bound has a finite physical memory scale under time refinement:
at beta=T delta and h=R delta fixed, it approaches

    (c^2/b) exp(-sqrt(b)h)/(1-exp(-sqrt(b)beta)).

This is the limit of a bound, not a construction of the continuum theory.
Conditional scalar action, Gaussian normalization and covariance errors
are stated separately; total field norms and partition bounds are extensive.

## The determinant is retained, not declared memory-free

The scalar kernel can be temporally truncated with the above error while
the charge-dependent determinant stays exact. The latter still depends
on the full history. Its mixed response now has an additional bound:

    d_i d_k log det M = -delta^2 (M^-1)_ik (M^-1)_ki.

It decays with the square of the temporal Green bound. Integrating this
identity controls the nonadditive effect of two finite potential changes,
including signed changes when the interpolating potentials retain the gap.
Update magnitudes remain in the bound. This is not a uniform determinant
truncation theorem for arbitrarily many unbounded charge changes.

## Exact history computation without a cubic-in-time dense solve

The [solver contract](history-determinant-solver-round25/PROOF.md) and
[implementation](round25_algebra.py) compute a given history's full scalar
determinant and induced action with exact block elimination. A rank-2d
correction restores periodic time, where d=(ell-1)^3 is the fast cell size.
The original projective hopping phases remain separate and unchanged.

Cost is O(T d^3) arithmetic operations per cell, O(T d^2) storage, and
O(T d^2) for each new single right-hand side after factorization. This
improves the generic dense O(T^3 d^3) arithmetic count of Round24. It does
not bound exact-rational bit growth or floating-point stability, compute
the whole inverse in linear output size, or solve the charge-history sum.

The physical regression includes a neutral actual E8 hop with signed
scalar stiffness changes (-6,+2), its inverse, the periodic determinant,
and a reduction of the full 81-coordinate original scalar action with
the retained neutral compensator. Separately assembled dense determinants
and solves agree exactly with the recursive calculation.

## What remains open

This closes two conditional finite-regulator obligations: a controlled
moving-history scalar memory kernel and an exact, lower-cost per-history
Gaussian computation. It does NOT prove a time-local real-time Hamiltonian,
reflection positivity of the truncated kernel, a controlled signed sum over
all charge histories, or a nontrivial continuum theory at fixed transport.
The Round24 REAL-TIME preparation theorem still has its small-J condition.

The next bridge is from these conditional bounds to the actual summed
charge dynamics: control energy-weighted history tails and cancellations,
then the real-time/continuum reconstruction. Full g!=0 gravity is
non-Gaussian and outside both contracts. Microscopic parent/parameter
selection, local relativistic stress, observed chiral matter/flavor,
native observables, spectators and external predictions remain open.
No T1-T8/TOE/RH or empirical promotion.

## Reproducibility

Two checkers contain 39 and 25 exact groups, with ten source pins each.
The aggregate reruns 25 prerequisite checkers. There are 33 separate
infrastructure/source/semantic fixtures, including ten deliberately wrong
variants. Checkers and fixtures run normally and with optimized Python;
the optimized runs use /tmp. Finite tests supplement the analytic
arguments; no proof-assistant or independent-human certification is claimed.

See [review](ROUND25_REVIEW.md), [fixture evidence](ROUND25_RUNNER_VALIDATION.json)
and [full aggregate evidence](ROUND25_VALIDATION.json). In the research environment:

    python -B experiments/theory-contracts/test_round25_runner.py
    python -B experiments/theory-contracts/run_round25.py
    python -B experiments/theory-contracts/run_round25.py --check-manifests
