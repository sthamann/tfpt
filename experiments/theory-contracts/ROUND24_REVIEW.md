# Round24 source, analytic and regression review

2026-09-07. Single-agent review; no independent human or proof-assistant
certification is claimed. Universal statements rely on the displayed
arguments and hypotheses, not the finite symbolic test population alone.

## Finite-density normalization and domains

- The thirteen source pins retain the original E8 cocycle/hopping,
  scalar Ward normalization, full 35-pair parent and the Round22/23
  comparison definitions. Pins are checked before source execution.
- The uniform shift is the actual product of projective charge unitaries.
  Its hopping conjugation signs cancel across each edge, rather than
  being discarded. Total physical charge is Np. The scalar occupation M
  is also allowed proportional to N, unlike the previous few-quanta case.
- The neutral unperturbed gap is 2/N. The unique perturbed ground vector
  lives in the full charge carrier. The proof retains 48NJ and e(p), and
  derives the new eps=24N^2J endpoint instead of copying the root sector.
- lambda_N=N u is declared. Here u is not the gravity coupling g.
  Background resummation gives m_*^2=m^2+2u e(p) without an extra 1/N.
  This is an exact rewrite, not a fitted mass or a vacuum subtraction.
- The residual includes the signed linear charge term. The E8 quadratic
  inequality and the second-order mean-energy estimate control it.
  The exact fourth moment includes the hard Gaussian pair contraction;
  the physical hard-mode vacuum has not been omitted.
- The scalar number preparation is an eigenstate at mass m_*. Free
  spectators are left unrestricted. Duhamel is along this reference
  orbit; neither interacting evolution is compressed to the preparation.
  Polynomial moments and D-graph approximations give the required
  interacting operator domain at each fixed finite regulator.
- The clock comparison keeps a common strictly positive lower bound.
  Restricted resolvents, not a presumed globally bounded interaction,
  give the square-root estimate in the canonical initial-data chart.
  No equality of old source-dependent encodings is inferred.
- The family has finite densities but J<=O(N^-2). Vanishing eps suppresses
  charge fluctuations and leaves a Gaussian scalar with shifted mass.
  No general dense-state, fixed-J thermodynamic, scattering, unbounded
  stress-observable or full-gravity error bound is claimed.

## Original-model locality, determinants and time regulator

- Retained boundary faces disconnect the eliminated interiors. This is
  spatial cell elimination, not a Fourier projection or torus average.
  Retaining only coarse points would invalidate the cell argument.
- The scalar Dirichlet block keeps all six-neighbor diagonal contributions.
  Positivity and the uniform gap come from the box spectrum and the
  nonnegative potential for arbitrary integer charges, not a charge cutoff.
- The Schur kernel has bounded spatial support and positive Euclidean form.
  Its determinant depends on charges and must remain in their induced
  weight. An exact finite-dimensional determinant factorization and
  log-determinant response check provide separate normalization tests.
- The static expansion retains the induced kinetic matrix and the
  frequency-dependent remainder, including its subthreshold real-frequency
  denominator. A positive canonical two-derivative realization does not
  prove locality of its square roots or identity with the full kernel.
- A real neutral hop and its inverse supply the nonstatic regression.
  Its exact three-slice fast matrix has 24 coordinates, a nonzero
  cross-time inverse entry and a history-dependent determinant.
- For every history the finite-time Gaussian formula is exact. The
  spatial block factorization survives, but memory spans times. Original
  hopping phases and all charge magnitudes stay outside the integral.
  No positivity of the history measure, interchange of infinite sums
  with limits, or nonstatic frequency-diagonal approximation is used.
- Dense algebra cost is stated separately from the unsolved history sum.
  Full g!=0 gravity invalidates Gaussian scalar elimination.
- Primary-source background was checked in
  [Dusson-Sigal-Stamm](https://arxiv.org/abs/2105.02058).
  Their Schur/Feshbach discussion is context, not an imported solution
  of this lattice's interacting charge dynamics.

## Systematic debugging and adversarial regressions

The systematic-debugging workflow isolated a prose error: the derivative
of a determinant had been described as an inverse diagonal. For
B=[[3+v,-1],[-1,3]], det(B)'=3 but (B^-1)_00=3/(3v+8).
The correct identity is (log det B)'=(B^-1)_00. The proof text now states
LOG det and the additional delta factor when varying a physical potential.

The checker already used det'/det and needed no mathematical change.
The minimal exact diagnostic distinguished the false prose identity from
the correct implemented one; no failing checker run is invented.
The auxiliary test-driven-development skill referenced by the debugging
skill was unavailable, so diagnostics and isolated fixtures were
implemented directly.

Six semantic variants are rejected: dividing the background mass shift
by N, dropping the hard Gaussian pair contraction, erasing the neutral
mean-energy contribution, dropping the determinant, deleting boundary
diagonal terms, and replacing the induced kinetic matrix by identity.
All thirteen input pins are tested missing and changed against BOTH
consumers, plus the source fail-before-execution check.

There are 29 infrastructure/source/semantic fixtures per run, distinct
from the 33/21 exact groups, 13 pins per checker and 23 prerequisite runs.
The new checkers and fixtures pass normally and under optimized Python;
the optimized runs use /tmp. The runner forces prerequisite assertions on
and rejects exit-zero JSON FAIL. Manifest checking establishes current
source/inventory/record consistency, not cryptographic or theorem
certification. Saved aggregate output is complete, not truncated.

Only Round24 research artifacts and three navigation entries are added.
Old evidence is preserved and checked without regenerating it.
New manifest consistency, syntax, JSON, links and whitespace are checked
before handoff. Existing paper, ledger and v472 changes remain untouched.
No commit/push, paper/web release, T1-T8/TOE/RH or empirical promotion.
