# Round17 internal review record

2026-09-06. Agent-assisted mathematical and source review of bounded NON-RH
research. This is not external peer review, a proof-assistant certificate,
empirical confirmation or a full physical gate promotion.

## Division of work

- The root authored the full constraint-parent construction and its checker.
  The clock/vertex reviewer independently read the complete proof, checked
  its analytic interfaces, read the checker and reran it normally and with
  -OO from outside the repository. Its 34 exact groups passed.
- The source-limit author developed the actual Gaussian commutator estimates,
  form-core and nonautonomous convergence proof, and the 45-group checker.
  The root and clock/vertex reviewer independently read the complete proof.
  Both also reviewed the checker; the reviewer reran it normally and with
  -OO outside the repository, with all 45 groups passing.
- The charge-parent author developed the full rotor representation, Gauss
  reduction, charge energy and cocycle, operator domains, bounded interactions
  and support obstruction. The root independently read the entire proof and
  checker. The author's normal and optimized runs passed all 45 NEW groups,
  with provenance controls and inherited prerequisites separately typed.

## Load-bearing points reviewed

1. The actual Gaussian embedding is retained, not replaced to make the
   source theorem tautological. Ordered Q_a Q_b residuals include the
   noncommuting and constant ordering terms. An identically zero source
   channel is explicitly retained rather than assumed quadratic and nonzero.
2. Compact cutoffs and mollification establish the needed common FORM core.
   Weak compactness uses local derivative control and compact exhaustion,
   not a nonexistent global bound on the quadratic displacement derivative.
   The time-dependent form equation has the controlled Hilbert-triple
   regularity needed for uniqueness and full-norm convergence.
3. Full constraint dynamics follows by characteristic propagation and
   dominated integration. The two limits remain sequential at fixed lattice;
   no uniform continuum estimate is claimed.
4. E_dyn and E_clock have different roles. The latter retunes the spectral
   clock momentum and exactly intertwines gauge constraints; it does not
   prove finite-parameter equality of physical square-root clock dynamics.
5. The native centered momentum fails at nonzero coupling. A displaced
   compact seed provides exact Gaussian equivariance without inventing
   commutation with the positive parent. The joint compact closure, source
   first vertex and full first-vertex limit are distinguished explicitly.
6. Locality of B is not locality of the full g^2 |c|^2 sum Q_a^2 completion.
   Positive base energy is not positivity of the complete constraint generator.
   Physical fast oscillators are not the optional old gauge auxiliaries.
7. Compact rotor Gauss averaging produces an actual nonzero Hilbert subspace.
   All Gram entries, the cocycle, unbounded charge register, fourth-power
   translation and finite-code multiplicity survive the exact isometry.
8. The energy identity holds on Gauss, not for arbitrary nonuniform flux.
   The physical gap one differs from the unconstrained gap 1/M. Local bounded
   terms cannot change physical charge; winding support and the 3D extra-cycle
   obstruction remain. An E8 metric does not turn U(1)^8 into nonabelian E8.
9. A main-checker failure was investigated using systematic-debugging before
   changing the fixture. The nonzero equivariance polynomial happened to
   vanish on the initial datum. The corrected datum gives -5/4; the original
   zero datum remains a regression. Neither source nor theorem was weakened.
   The source checker additionally rejects an actual Ward-source mutation.

## Evidence and preservation

The new checkers use explicit failure exceptions, not removable assertions.
Three integrated checker runs and six unchanged prerequisites are recorded
separately from twenty normal and twenty optimized runner fixtures.
Manifest validation checks current inventories, digests and successful
recorded runs; it cannot certify an analytic proof.

The independent runner audit found a transitive provenance omission: the
charged-lift checker also executes the Round15 eight-channel checker. That
script is now an explicit audited input, so later changes cannot evade the
saved-manifest check. Raw new/provenance/prerequisite counts stay separate.

The detailed full-parent review is in
[full-constraint-parent-round17/REVIEW.md](full-constraint-parent-round17/REVIEW.md).
Previous Round10--16 evidence and concurrent paper, ledger and v472 edits are
not rewritten. No commit, push, release, empirical score or T1--T8 status
promotion is part of this round.
