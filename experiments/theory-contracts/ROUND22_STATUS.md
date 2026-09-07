# NON-RH Round22: positive hopping and a constructive momentum alternative

2026-09-07. Local research on HEAD and actual remote main
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`, both verified this round.
No commit/push, paper/web release, ledger or empirical promotion. Earlier
local rounds and concurrent paper/ledger/v472 edits are preserved.

## Constructed: an interacting positive parent with conserved global momentum

The [translation completion](translation-completion-round22/PROOF.md)
constructs a continuous translation symmetry of a deliberately CHANGED
common scalar/gravity/auxiliary/E8-charge Hamiltonian. All 35 continuous
canonical pairs per site and all integer charge configurations remain.
There is no appended independent toy model or finite charge truncation.

The construction extends the original discrete translations to a torus
action U with a signed Fourier generator on continuous fields and the
joint crystal-translation logarithm on charges. It averages the WHOLE
original positive quadratic form over that action, including each complete
auxiliary square. Positivity and the original source-independent subtraction
are retained. Finite Fourier factors define a closable sum of squares;
its chosen Friedrichs realization is self-adjoint and positive, with
all-time dynamics, exact total charge and continuous GLOBAL momentum
conservation. The positive square-root clock shares that symmetry.

This is an explicit finite prescription at fixed odd L, not an unevaluated
formal integral: on L=3, the average is exactly 343 positive conjugates
with weights 1/343. That number follows from the actual square-factor
frequency bound. Sampling only the 27 spatial lattice translations would
fail, because it retains the unwanted reciprocal-lattice aliases.

The changed model still interacts. One actual nonzero charge/scalar
exchange survives; a second, incompatible exchange is removed. Among
19,683 lowest-band, scalar-number-preserving candidate channels at L=3,
6,859 unwrapped channels remain and 12,824 wrapped channels are removed.
These are a bounded selection-rule inventory, not all physical vertices
or a claim that every listed channel has a nonzero amplitude.

The price is explicit: spatial NONLOCALITY and changed FIRST interaction
vertices. A conserved global momentum is not a local relativistic stress
tensor. Neither microscopic TFPT selection, local gravity constraints,
causal/Lorentz dynamics nor the old source/Gaussian/observable-net limits
has been established for this alternative. It is not installed as the
repository's default physical model.

## Established for the unchanged model: genuinely positive-J charge motion

The [charge-band proof](positive-hopping-band-round22/PROOF.md) treats
the original full hopping operator on the infinite E8 charge space, with
nu=0 and total root charge p=e2. At zero hopping its lowest eigenspace is
isolated by Delta=1/N. The FULL hopping operator leaks out of that space;
this leakage is retained, not discarded in a projected surrogate.

An explicit resolvent argument constructs one exact lowest-band state per
translation character for 48N^2 J<=1/32. At L=3 this gives

    0<J<=1/1119744,
    |<chi_l|F_(l-k)|chi_k>|>=29/40.

The source F is unbounded. Its graph bound is included in the estimate,
so closeness of bounded projections alone is not mistaken for control of
an unbounded matrix element. Exact proper-cubic energy equalities survive.
The dispersion also has an explicit second-order error bound; a smaller
positive interval J<=1/181398528 certifies a nonflat bandwidth >=8J.
These intervals are conservative dimensionless sufficient bounds, not
fitted or empirically selected parameters; they are not uniform in volume.

## Excluded: the tested regular repair, now at strictly positive hopping

The [positive-J momentum test](positive-hopping-momentum-round22/PROOF.md)
uses two genuine equal-energy charge/scalar processes on the SAME charge
transition, at any fixed J in the interval above. Their nonzero matrix
elements require the same additive charge-momentum difference to be both
sqrt(3)/2 and -sqrt(3). No such difference exists.

Thus an arbitrary regular first mixed correction in lambda cannot repair
the original centered scalar seed plus a charge-only generator strongly
commuting with the charge Hamiltonian and its translations. No smoothness
as J goes to zero is assumed. A separate cubic-covariance argument also
excludes every nonzero scalar number-preserving quadratic vector seed in
the tested class, including signed spectral weights. This is more than
the zero-hopping resonance or a finite polynomial ansatz failure.

The hypotheses remain essential: fixed nu=0, root sector, L=3, a small
positive-J interval, the additive translation-covariant free seed and a
regular lambda expansion. Arbitrary mixed zeroth-order seeds, nonregular
branches, other parameters/sectors, full dynamical gravity and a controlled
continuum remain separate problems. The witness modes are regulator-scale;
this does not rule out emergent low-energy Lorentz symmetry. Exact original
discrete crystal momentum is never claimed to fail.

## Evidence and reproducibility

| New contract | Exact check groups | Pinned source inputs |
| --- | ---: | ---: |
| Full-carrier positive-hopping band | 25 | 16 |
| Strictly positive-J momentum obstruction | 27 | 16 |
| Positive continuous-translation completion | 24 | 16 |

The three checkers pass normally and under optimized Python from a foreign
working directory. The aggregate separately runs 18 predecessor checkers.
There are 27 infrastructure/source/semantic mutation fixtures, passing in
both normal and optimized runs. Each of 16 frozen sources is tested missing
and changed against ALL THREE new consumers; four semantic mutants guard
quadrature aliasing, the unbounded-source cost, hidden charge truncation
and the resonance sign. Counts are not combined into a proof total.

See [review](ROUND22_REVIEW.md),
[runner evidence](ROUND22_RUNNER_VALIDATION.json) and
[aggregate evidence](ROUND22_VALIDATION.json). With the research
Python/SymPy environment, from the repository root:

    python -B experiments/theory-contracts/test_round22_runner.py
    python -B experiments/theory-contracts/run_round22.py
    python -B experiments/theory-contracts/run_round22.py --check-manifests

The runner prints JSON without rewriting evidence. Hash/inventory checks
verify recorded consistency, not mathematical correctness or attestation.
This round has a single-agent analytic/source review and exact regression
checks, not new independent human or proof-assistant certification.

## Remaining solution target

There is now a concrete positive, interacting global-symmetry alternative,
and a positive-hopping obstruction identifying which original vertices
conflict with the tested continuous additive momentum. The next essential
question is whether a physically selected interaction can recover local
relativistic stress and controlled long-distance dynamics, rather than
merely a globally conserved label. The alternative's old source and
observable limits also need their own derivation before use.

Still absent: microscopic selection of one shared parent, full gravitational
stress/constraint closure, chiral statistics and observed particles/flavor,
native-net identification, spectator interpretation, a controlled relativistic
continuum and parameter-fixed external predictions. No T1-T8/TOE/RH or
empirical contract is promoted.
