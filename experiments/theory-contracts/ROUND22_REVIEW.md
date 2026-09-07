# Round22 source, mathematical and implementation review

2026-09-07. Single-agent source/analytic review and exact/adversarial checks.
No independent human reviewer or proof-assistant certification is claimed.

## Source and model identity

- Sixteen frozen inputs cover the actual Ward operator, full E8 hopping,
  original coupled energy/source domains, the 35-pair positive parent and
  Round21's momentum/dressing conventions. New consumers verify every pin
  before importing the old code. No cocycle sign, charge channel or physical
  energy constant is silently removed.
- The first two contracts use the unchanged Round20 gravity-decoupled
  scalar/charge model with nu=0, total charge e2 and small positive hopping.
  The third explicitly changes the WHOLE common positive parent, including
  its gravity/auxiliary interactions. It is a research alternative, not a
  claim that the original Hamiltonian has acquired a new symmetry.
- All integer charges remain in the Hilbert space. The isolated lowest
  eigenspace is used for a resolvent argument and exact matrix elements,
  not as an invariant replacement: its full hopping image contains 1,296
  nonzero configurations, 1,290 outside the one-charge space.

## Analytic checks and boundaries

- All-charge band isolation follows from positivity and integrality of
  the actual E8 energy, not a finite box search. Bounded hopping gives a
  contour resolvent, exact rank-one character projections and an explicit
  reduced-gap Schur bound. Proper rotations imply exact degeneracies.
  The separate smaller nonflat-band window is not confused with the
  larger window proving isolation and a nonzero form factor.
- F_h is UNBOUNDED. The eigenvector equation supplies its D-graph bound;
  norm continuity of projections alone would be insufficient. The exact
  error 11/40 and lower bound 29/40 include that graph cost.
- A test initially compared factored and expanded rational expressions
  using structural equality and failed. The systematic-debugging workflow
  reproduced the failure and showed their exact difference was zero.
  Comparing the cancelled difference and checking the derivative numerator's
  positivity resolves that verification bug; no physical bound was changed.
  The auxiliary test-driven-development skill mentioned by that workflow
  was unavailable; the failing/passing regression was implemented directly.
- The positive-J obstruction uses exact charge eigenstates and genuine
  untruncated scalar oscillator matrix elements. Charge translation
  covariance, an additive zeroth-order seed and regularity in lambda are
  explicit assumptions. Arbitrary first mixed corrections are allowed.
  The two processes have the same charge transition and different scalar
  shells; their energy equalities do not require equality between those
  two shells. No continuity in J at zero is assumed.
- The broader vector-weight argument concerns number-preserving quadratic
  scalar seeds on L=3, with proper-cubic covariance. It does not classify
  every nonlinear conserved operator or rule out a low-energy continuum.
- The torus extension uses all 35 continuous species and the joint charge
  translation projectors on the FULL carrier. Odd L prevents an assumed
  real Nyquist interpolation. Continuous quadratic terms, D, L_J and
  source-independent constants remain unchanged; nonlinear interactions
  generally change already at first coupling order.
- Positivity is proved by averaging COMPLETE squares. Fourier square
  factors have coordinatewise frequencies at most 3h, so M=6h+1 exactly
  integrates their squared norms. M=3 at L=3 is a real aliasing error.
  The finite Fourier sum is constructive but spatially global and can be
  expensive; it is not an efficient infinite-state dynamics solver.
- Closability follows from the common invariant finite-charge/Schwartz
  adjoint domain. The new operator is the chosen Friedrichs realization;
  its form core is specified. Equality of old and new operator domains,
  or essential self-adjointness on the old core, is NOT asserted. Haar
  invariance extends to the closed form, giving strong commutation and
  a compatible positive square-root clock.
- The averaging preserves a demonstrably nonzero exchange and deletes
  the incompatible one. The 6,859/12,824 channel counts classify a bounded
  number-preserving selection rule, not all vertices or their amplitudes.
  Conservation of global momentum does not establish locality, causal
  propagation, Lorentz symmetry or native local observable-net limits.

General isolated-eigenvalue perturbation background was checked against
[Wahl](https://arxiv.org/abs/1910.08460) and
[Kloeckner](https://www.theta.ro/jot/archive/2019-081-001/2019-081-001-008.html).
The explicit model-specific constants and infinite-charge hypotheses are
derived here; no result for a different operator class is imported.

## Regression and integration audit

Three new exact checkers (25/27/24 groups, 16 provenance checks each),
18 prerequisite runs, and 27 runner/source/semantic fixtures are distinct.
Normal and optimized runs exercise the checkers and fixtures; optimized
checks use /tmp to reject reliance on the repository working directory.
Every pinned input is tested both missing and changed against each new
consumer. Four isolated semantic mutants corrupt the quadrature grid,
unbounded form-factor estimate, full charge output and momentum sign;
each is rejected under optimized Python.

The frozen aggregate stores original child stdout, runtime, source hashes
and complete inventories. Its subprocesses force assertions on even when
the parent is optimized. A zero exit with JSON status FAIL is not success.
Manifest checks are hash/record consistency, not reruns or attestations.

Only Round22 artifacts and three navigation entries are added. Previous
rounds' saved evidence is not regenerated. Old manifest checks, new normal
and optimized manifests, syntax, local links and whitespace are checked
before handoff. Concurrent paper, ledger and v472 changes are preserved.
No commit/push, paper/web release, empirical or T1-T8/TOE/RH promotion.
