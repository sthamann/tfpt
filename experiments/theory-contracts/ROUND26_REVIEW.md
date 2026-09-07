# Round26 analytic and source review

2026-09-07. Single-agent derivation and review with separate exact checks.
No independent human or proof-assistant certification. General statements
depend on the displayed arguments, not a finite census of examples.

## Transfer, absolute convergence and normalization

- The transfer operator is explicitly symmetric and positive. Its scalar
  kinetic and charge hopping factors commute because they act on different
  tensor factors. Positive hopping gives a trace-class upper comparison;
  the scalar mass and coercive charge energy make its trace finite.
- This is the same declared finite Euclidean regulator used by the local
  Gaussian work, not an equality with the exact unsliced exp(-beta H).
  The fixed-volume neutral sector is explicit. A nonneutral sector needs
  its own lower reference; the present zero-charge bound is not reused there.
- The twelve input pins retain actual E8 phases, 48N directed channels,
  48NJ constant, Gram and scalar Ward normalization. The graph search was
  insufficient for the current local Round25 code; known sources were read
  directly. HEAD and the actual remote main were verified.
- The unsigned process is only an absolute majorant. Its row/column
  normalization uses the original exp(-beta kappa). Omitting the constant
  would destroy the cancellation in the absolute bound and change the model.
- Schatten Holder applies to the full coercive charge operator on the
  neutral infinite carrier and norm-one translations. The heat exponents
  sum to beta. Summing positive word bounds justifies Tonelli; the finite
  majorant then justifies the signed history interchange. No infinite
  volume or time-continuum interchange is asserted.
- The lower partition bound uses spectral Jensen for the actual zero
  diagonal of A_sign and Schatten compression monotonicity. It never
  treats the zero-charge configuration as an interacting eigenstate.
- The resulting cancellation factor is finite, positive and generally
  huge. No estimate of the actual average sign or efficient sign cure is
  claimed from this very conservative lower bound.

## Kernel and observable errors

- Schur minimization retains the entire temporal mass operator because
  it is block diagonal in the spatial retained/fast partition. Its inverse
  trace, not T copies of the worst inverse eigenvalue, controls the new
  logarithmic Gaussian error. The one-half determinant exponent and
  1/(1-eta) margin remain.
- The exact eliminated determinant stays in both Gaussian factors. The
  conditional ratio error is multiplied by the full cancellation budget
  before normalizing the signed sum. A positive truncated scalar kernel
  alone would not justify dropping that budget.
- The 2rho/(1-rho) observable estimate is only for bounded one-time
  charge observables. Its exact numerator is bounded by the positive
  original transfer trace. Arbitrary signed multi-time functions and
  scalar insertions do not automatically obey this estimate.
- The approximate sum is positive only when its certified relative error
  is below one. No positive transfer or reflection positivity is inferred
  for the memory-truncated history weights themselves.

## Finite tails and costs

- The charge event is a union over sampled time boundaries. Splitting
  half of one heat factor leaves beta-delta/2 for Holder and yields the
  explicit Gaussian coordinate tail with a_c=1/(62N). No intermediate
  word charge is discarded using that boundary-only estimate.
- Hop order is TOTAL order across slices, with multinomial/factorial
  allocation weights. The geometric tail condition P+2>theta is checked.
  The e^(-theta) tail factor cancels the lower-reference e^theta in the
  relative hop bound, not in unrelated error terms.
- The executable planner uses exact rational/integer bounds pi<4, e<3,
  e>2. K=4096,P=962 at the declared N=27,T=3,beta=1,J=1/10 passes its
  omission-error target. It uses FULL memory, so a_R=0; it is not evidence
  that a nontrivial memory cutoff survives the cancellation budget.
- No complete interacting partition has been computed. The candidate
  envelope is a deliberately naive upper count, not an optimality or
  necessary-cost lower bound. Exact Gaussian and transcendental evaluation
  would require additional precision accounting. The calculation does not
  establish an efficient all-J/large-volume solver or a physical prediction.

## Negative-loop audit

- The four steps use actual old monomial shifts, not a hand-assigned sign
  graph. The two overlapping channels have odd Gram pairing. Energies,
  neutrality, phase sequence, closure and a second starting profile are
  checked. The general profile independence follows from the original
  overlapping-hop identity, not those two examples alone.
- Each transition is a distinct actual hopping matrix element at L>=3.
  Diagonal phase factors telescope around the loop. The conclusion is
  limited to diagonal configuration-basis rephasing, not arbitrary bases.
- The scalar-integrated negative contribution retains the full N=27,T=4
  matrix and its positive mass margin, exp(-beta kappa), (delta J)^4 and
  exp(-7delta/N). It is a nonzero word contribution, not an invariant
  four-state model, the full partition or a claim about every resummed
  transfer-entry sign at every delta.
- Primary-source context was checked in
  [Hen](https://arxiv.org/abs/2012.02022). Non-stoquasticity and universal
  simulation impossibility are not identified. The E8 loop proof here
  does not import a broader no-go theorem from that work.

## Regression, preservation and claim boundaries

The ten isolated semantic variants cover doubled charge coercivity,
lost charge coordinates, the wrong heat split, missing factorial,
wrong tail ratio, a missing observable normalization term, a missing
temporal Green trace, erased loop signs, a dropped hopping constant and
a false assertion that the partition sum was executed. Each is rejected.
Every one of the twelve pinned files is also tested missing and changed
against both consumers under optimization, before source execution.

There are 33 fixture tests per run, distinct from the 22/14 exact groups,
twelve source pins per checker and 27 prerequisite runs. The aggregate
forces prerequisite assertions on and rejects exit-zero JSON FAIL. Saved
output and inventories are complete; manifest verification establishes
current record/hash consistency, not theorem certification or attestation.

Old Round10-25 evidence is checked without regeneration. New syntax,
JSON, links, whitespace and manifest consistency are verified before
handoff. Only Round26 artifacts and three navigation entries are added.
Concurrent paper, ledger and v472 edits remain untouched. No commit/push,
paper/web release or T1-T8/TOE/RH/empirical promotion.
