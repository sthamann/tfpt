# NON-RH Round21: complete hopping dressing and exact momentum repair tests

2026-09-07. Local research on HEAD and actual remote main
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`, both verified this round.
No commit/push, paper/web release, ledger or empirical promotion. Previous
local rounds and concurrent paper/ledger/v472 edits are preserved.

## Constructed: the missing dressing term at every finite coupling

[The dressing proof](dressed-hopping-round21/PROOF.md) gives the complete
operator for the additional gravity/charge-hopping term left at first
order in Round20. For a hop n->n+s with its ORIGINAL cocycle c_e(n),

    W_n=exp(-i kappa S_n),
    (W U_e W*) |n,psi> = c_e(n)|n+s,W_(n+s)W_n* psi>.

The two scalar evolutions are computable through finite 2N-dimensional
canonical matrices and their continuous metaplectic lifts. The sign of
that lift and the lattice cocycle are BOTH retained. This is a definition
at all real kappa, not a formal infinite series or a finite charge cutoff.
The completed hopping remains positive and bounded by 96JN, with its
48JN constant retained. Conjugating the entire parent transports its
self-adjoint domain, positive spectrum, clock and exact charge balances.
Changing only its hopping term would instead define a different model.

The first derivative is exactly Round20's -i[S,L_J]. From second order
on, an exponential of the endpoint energy difference alone is wrong:
the continuous scalar quadratics do not commute. The original edge
support also fails at third order. On the actual 3x3x3 cubic scalar
lattice an explicit beyond-edge canonical coefficient is 2/15.

Source audit matters here: the ORIGINAL gravity chart has zero-mean
coordinate fields. An initial exploratory uniform source profile was
discarded. The frozen witness has xi_r=1 except -26 at (2,2,2), xi_v=0;
it has zero mean and gives the same nonzero coefficient. This is guarded
by an optimization-safe check and an isolated negative-control mutation.
No new homogeneous native gravity mode was smuggled into the construction.

## Established: two distinct obstructions to repairing the momentum

[The momentum proof](charge-momentum-round21/PROOF.md) derives the actual
global scalar force, then goes beyond merely observing a failed bracket.

1. For L>=3, lambda>0 and ANY finite hopping strength J, no momentum
   P_m+P_charge can be conserved if the correction acts only on charges
   and satisfies the stated common-core conditions. A diagonal charge
   block contains a nonconstant scalar quadratic that a charge-only
   commutator cannot cancel. Neither nonlocal charge operators nor a
   fixed total-charge sector, including the neutral sector, evade it.
   Stress-only changes keeping P_m fail the same integrated-force test.
2. At J=0 on L=3, a stronger quantum resonance excludes ANY regular
   first-order mixed correction to the specified free seed as lambda
   turns on. Two genuine equal-energy scalar one-quantum states give

       <C|i[V_1,P_0]|S> = sqrt(3)/(729 sqrt(m^2+3)) != 0.

   Every commutator [H_0,P_1] has zero matrix element between those states,
   whatever the allowed mixed P_1 is. Exact untruncated oscillator actions
   and the independent Ward-force polynomial give the same coefficient.
   This is not a finite-ansatz search failure. It is distinct from
   Round12's classical scalar–TT resonance at order g^2.

The second result is NOT an all-J mixed-momentum no-go. It concerns the
specified seed and regularity at zero hopping/coupling; a fixed nonzero-J
construction, a different free seed, a singular branch, changed matter
algebra/interaction or full dynamical gravity needs its own analysis.
Discrete simultaneous lattice translations survive exactly and give a
bounded crystal-momentum logarithm, but not a local relativistic stress.
Literal infinitesimal translations of the diagonal integer occupations
also fail a separate pure-point matrix-element test; actual charge flow
is off-diagonal and is not in conflict with that result.

## Evidence and reproducibility

| New contract | Exact check groups | Pinned source inputs |
| --- | ---: | ---: |
| Complete dressed hopping | 32 | 8 |
| Charge momentum and regular mixed correction | 63 | 8 |

Both checkers pass normally and under optimized Python from a foreign
working directory. These counts are distinct from the 16 predecessor
checker runs in the aggregate and from 25 infrastructure/mutation tests.
Both normal and optimized infrastructure runs pass. Eight frozen source
inputs are each tested missing and changed against both new consumers;
additional mutants test the gravity zero mode and matrix multiplication
order. See [review](ROUND21_REVIEW.md),
[runner evidence](ROUND21_RUNNER_VALIDATION.json) and
[aggregate evidence](ROUND21_VALIDATION.json).

From the repository root with the research Python/SymPy environment:

    python -B experiments/theory-contracts/test_round21_runner.py
    python -B experiments/theory-contracts/run_round21.py
    python -B experiments/theory-contracts/run_round21.py --check-manifests

The runner prints JSON without overwriting saved evidence. Hash and
inventory agreement is not theorem certification. This round had a
single-agent source/analytic review, not a new independent human or
proof-assistant certification. The two different resonance calculations
cross-check the coefficient, not all universal domain hypotheses.

## What the next solution must actually address

The specified missing dressing operator is constructed. The full momentum/
stress problem is NOT closed: two seemingly natural repairs are excluded
under their precise hypotheses. A next useful target is a mixed generator
at strictly positive hopping or a different infinitesimal symmetry/carrier,
tested first by its equal-energy commutator blocks and by its action on
local observables. Merely extending the same regular zero-hopping expansion
or renaming the energy current cannot pass these tests.

Still not supplied: TFPT selection of the charge/frame/hopping laws,
full gravitational stress, chiral statistics and observed particle content,
native-net identification, spectator interpretation, controlled relativistic
continuum and parameter-fixed external predictions. No T1–T8/TOE/RH or
experimental contract is promoted by the new mathematical work.
