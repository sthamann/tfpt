# Round25 analytic, source and adversarial review

2026-09-07. Single-agent derivation and review, with separately implemented
dense algebra checks. No independent human or proof-assistant certification.
The finite exact tests are not substituted for the displayed general proofs.

## Source and scope audit

- Graph discovery found no indexed Round24 symbols; known source files
  were read directly. HEAD and actual remote main were reverified.
- Ten pinned inputs retain the original E8 cocycle and scalar/parent
  normalization, the Round24 local cells and density theorem. Hashes are
  checked before imported input code executes. The older prerequisite
  chain remains an actual rerun, distinct from manifest consistency.
- Both new contracts act on the ORIGINAL g=0 Gaussian scalar sector.
  All integer charge magnitudes and hopping phases stay in place.
  No torus-average model or continuous momentum repair is imported.
- Arbitrary finite histories, not a charge-register cutoff, are covered
  by the analytic lower-gap argument. The finite examples include a
  noncommuting actual eight-site cell and a very large scalar potential
  jump; these examples do not exhaust the claim's quantifiers.

## Memory proof audit

- The Neumann series is controlled in a block-row norm by
  2/(2+delta^2 b)<1. Each ordered product is bounded before summation,
  giving a scalar cycle Green function without commuting B_j matrices.
  Only a LOWER energy bound enters. An upper charge/condition-number
  bound, and hence a small-hopping condition, is not smuggled in.
- The Green function contains both periodic images and the factor
  1/(1-q^T). Tail counting uses cyclic distance and two directions.
  The T>=3 convention avoids doubled-edge ambiguities for a two-slice cycle.
- The scalar inverse is masked symmetrically, but its positivity is not
  presumed. The retained Schur kernel is positive only through the stated
  mass-gap margin. Both delta coupling factors and a volume-free global
  norm of C are retained; cell count does not multiply the operator bound.
- Finite memory applies to the quadratic scalar kernel, NOT the entire
  charge-dependent weight. The exact determinant is kept. Action errors
  carry the retained field norm, and log-partition errors carry the full
  number of retained space-time coordinates. No intensive/global relative
  error confusion or automatic reflection positivity is introduced.
- The determinant's mixed derivative is -delta^2 G_ik G_ki. Its integrated
  finite-update bound requires a positive-gap interpolation rectangle and
  retains update magnitudes. The charge action and log Gaussian weight
  have opposite signs and one-half factors. This is not a global
  determinant-tail or signed-history-sum estimate.
- The physical-time limit concerns the explicit finite-regulator bound,
  not an exchanged path-integral limit. Euclidean decay is not interpreted
  as real-time damping or a unitary reconstruction theorem.
- Primary-source context was checked in
  [Molinari](https://arxiv.org/abs/1210.8001), on block matrices and inverse
  decay. The new uniform lower-gap walk estimate is derived directly;
  no theorem requiring a bounded condition number is applied to unbounded
  physical charges.

## Solver and cost audit

- The open-chain matrix keeps the endpoint diagonal and positive gap.
  LDL pivots and forward/back substitution preserve matrix order.
- The rank-2d periodic correction is indispensable. Its small matrix need
  not be symmetric, so the solve order is tested on noncommuting blocks.
  Its positive determinant ratio follows from the two positive full
  matrices, not from unexamined small-matrix eigenvalues.
- The physical signed update is produced by the old E8 hop, with an
  explicitly retained neutral compensator. Energy decreases are not
  replaced by absolute values; determinant ratios invert on a reverse hop.
- A complete 81-coordinate scalar action is reduced with the actual
  retained-to-fast coupling. The fast Euler equation and induced action
  agree exactly. Other oscillator species are untouched factors; this is
  not promoted to a solution of the full interacting state.
- O(T d^3) counts arithmetic operations for a given history and cell.
  Storage and additional-source costs are separate. Growing rational bit
  lengths, floating-point certification, all-inverse output, history sum
  and sign cancellations are not hidden in that count.

## Systematic debugging and regression evidence

The systematic-debugging workflow found a double-counted factor two in
the draft physical-time limit. The already two-sided tail has prefactor
delta^2/[sinh(alpha)(1-q)], whose exact limit is 1/b, not 2/b. A minimal
symbolic test against the draft value FAILED, then passed with 1/b.
The corrected coefficient is in the proof and a dedicated mutant test
rejects the old factor. This was a normalization correction, not a change
of model or an empirical fit.

The first solver checker also exposed an immutable dense-reference copy
when applying a signed charge update. A minimal reproduction confirmed
that SymPy's Kronecker result and its copy remained immutable. Making an
explicit mutable Matrix copy fixed that test-harness operation; no solver
identity was changed. The signed update then passed the dense comparison.
The auxiliary test-driven-development skill referenced by the debugging
skill was unavailable; minimal failing/passing tests were implemented here.

Ten isolated semantic variants cover missing periodic images, a halved
two-sided tail, a missing delta factor, noncyclic masking, a dropped
periodic determinant, incorrect solve order, clipped signed updates,
wrong pivot time normalization, the double-counted continuum prefactor,
and erased determinant memory. All ten pins are also tested missing and
changed against BOTH consumers under optimization, plus a source
fail-before-execution test. There are 33 fixtures per complete run.

The two exact checker counts (39/25), ten provenance pins per checker,
25 prerequisite runs and 33 infrastructure/source/semantic fixtures are
distinct evidence types. New normal and optimized runs are checked
separately. The aggregate forces prerequisite assertions on and rejects
exit-zero JSON FAIL. Full stdout and inventories are saved without
truncation; manifest checking is record consistency, not attestation.

Old Round10-24 manifests are checked without regeneration. New hashes,
syntax, JSON, local links and whitespace are verified before handoff.
Only Round25 research artifacts and three navigation entries are added;
concurrent paper, ledger and v472 changes remain untouched.
No commit/push, paper/web release or T1-T8/TOE/RH/empirical promotion.
