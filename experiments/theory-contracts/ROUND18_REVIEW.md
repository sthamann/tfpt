# Round18 internal mathematical and implementation review

2026-09-06. NON-RH bounded research. This is internal agent-assisted review,
not external peer review, a proof-assistant certificate, empirical validation
or universal physical gate closure.

## Division of work and argument checks

- The cellwise author proved the active-domain stabilization, cross-stratum
  continuity, full covariant propagation and direct Gaussian limit. The root
  independently read the complete proof and checker. The proof explicitly
  distinguishes the finite-parent first jet from the old target first jet.
- The preconditioning author derived the native stencil identities, canonical
  source change, Haar normalization, mean gauge extension and full local
  parent. Both root and cellwise author independently read and checked the
  complete analytic construction and its interfaces.
- The root constructed the coherent-state readout dilation, exact noise
  formula and actual-source lower-bound witness. The cellwise and charge
  authors independently read the full proof and checker and reran it. Both
  reviews found the leakage, heat-transform and Weyl-ordering factors correct.
- The charge author proved the all-volume integral electric Hodge kernel,
  local penalty bound, cocycle/support and bounded cubic selection obstruction.
  The root independently read the complete proof and checker.

## Critical distinctions explicitly checked

1. The old inverse Laplacian is an actual source coefficient, not a numerical
   artifact. The exact preconditioning cancels it in the LINEAR source and
   free potential. It does not cancel the old global source-square completion.
2. The new cellwise stabilizer retains noncommuting source operators and
   their ordering corrections. The transport square in its weight prevents
   active graph domains from appearing or disappearing along a characteristic.
   Parameter continuity across different characteristics is proved separately.
3. The full Hamiltonian is local in its DECLARED independent site fields.
   The map back to native gravity is nonlocal and regulator-conditioned.
   Neither local observable-net equivalence nor a relativistic propagation
   bound follows from finite stencil support.
4. Restoring independent site coordinates adds four mean gauge pairs. The
   nonlinear completion can depend on their constraint coordinates, so they
   do not decouple off shell. Their constraints are first class and their
   specified reduction adds no physical Hilbert factor.
5. The chart's kinematic determinant and constant gauge-Haar normalization
   are included. No state-dependent measure is introduced to force a match.
6. Positive base B and positive reduced norm are not positivity of full H.
   The proper clock tube uses the transported base; the physical square-root
   clock limit remains distinct from exact constraint-group intertwining.
7. The unchanged linear source and second-ideal correction preserve the
   relevant first jet. Finite B has its own auxiliary first vertex; the old
   complete TT vertex appears only after eta then delta limits and dressing.
   The dressing need not preserve the new local field net.
8. Commuting auxiliary readouts can have exact first moments on a target
   whose sources do not commute, because the encoded range is not invariant.
   Their squared-energy defect is positive leakage. The actual normalized
   state family gives an unbounded lower bound; a constant subtraction fails.
   This is not an impossibility theorem for noncommuting local-source parents.
9. The 3D charge kernel is established integrally by vanishing differences,
   not inferred from real rank alone. Its 24 coordinates are not eight.
   The integer penalty gap, full Gram energy and all cocycles are retained.
10. Electric curl is an extra restriction which removes local transverse
    dynamics, not magnetic flatness or a photon/chiral-matter construction.
    The single-copy obstruction assumes a linear invariant sector and trivial
    internal cubic action; explicit nonlinear orientational branches fence
    any unjustified universal no-go.

## Verification practice and preservation

New checkers use explicit failure exceptions and distinguish new exact
groups from provenance and nested prerequisites. Optimized and foreign-cwd
executions check that verification does not rely on removable assertions or
an accidental launch directory. Actual-source mutations are rejected rather
than accepted as new data.

Systematic debugging isolated two implementation issues without changing
the mathematics: a dynamically loaded dataclass module needed registration
before execution, and generic symbolic rank elimination suffered integer
coefficient blowup. The first was reproduced by a two-case loader control;
the latter was replaced by exact polynomial-domain rank elimination, not a
floating tolerance or a smaller matrix. The charge predecessor count mapping
also retains its actual structured field name instead of silently dropping
inherited results.

A preconditioning fixture initially tested the scalar coordinate energy
against the momentum DeWitt matrix. The exact mismatch identified that
wrong reference sector. The fixture now uses the original coordinate
matrix K_q and separately checks the actual scalar transport row; the
analytic source and preconditioning formulas were not changed.

The aggregate runner executes four new scripts and five unchanged
prerequisites. Twenty isolated infrastructure fixtures are run normally and
with an optimized parent interpreter. Saved records retain inventories and
source hashes; manifest checks are consistency checks, not proof validation
or cryptographic attestations. Indirect charged-lift/eight-channel source
dependencies are explicitly audited.

Round10--17 artifacts are not rewritten. Concurrent paper, status-ledger
and v472 edits are preserved; only this round's research and index additions
are in scope. No commit, push, release or T1--T8/RH/empirical promotion.
