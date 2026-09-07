# Round23 source, analytic and regression review

2026-09-07. Single-agent review; no independent human or proof-assistant
certification is claimed. General statements rely on displayed analytic
arguments, not on the finite list of exact check examples alone.

## Source and locality audit

- Eleven pinned inputs cover the full E8 charge net, actual scalar Ward
  operator, charge-band constants, full 35-pair parent and the exact
  Round22 averaging prescription. Imports occur after every pin is checked.
  The aggregate retains the older prerequisite chain as actual reruns.
- The local witnesses are bounded neutral spectral projectors, in the
  original local observable net and the zero-total-charge sector. They
  do not rely on charged observables that leave a fixed sector.
- The finite translation orbit is exact and invariant for translations
  and diagonal sources. It is NOT asserted invariant for hopping. No
  finite charge Hilbert space is substituted for the physical carrier.
- The signed logarithm coefficient is a geometric-sum identity. The
  Hamiltonian witness separately transforms the actual removed Fourier
  plane, includes both scalar/volume normalization factors and the proper
  double-commutator sign. Other parent terms cannot cancel it because of
  their charge support or their unchanged diagonal/continuous action.
- The chosen vectors lie in the polynomial/finite-charge core. The weak
  first derivative is justified on the Friedrichs operator's domain;
  no global boundedness of the unbounded commutator is assumed. The lower
  bound excludes the explicitly stated uniform exponential small-time
  estimate, not all notions of propagation or a continuum limit.
- General context was checked in primary sources:
  [Nachtergaele-Sims-Young](https://arxiv.org/abs/1810.02428) and
  [Wilming-Werner](https://arxiv.org/abs/2006.10062). The latter's k-body
  converse is not invoked outside its hypotheses for this global operator.

## Compression, dynamics and domains

- The soft compression uses the actual polynomial degree, zero-momentum
  hard contractions and the strict no-alias inequality. The charge
  character projection does not bound integer charge magnitudes. Its
  common-core closure is distinguished from unexamined maximal domains.
- The dynamical comparison is restricted to g=nu=0 and the exact isolated
  charge band with 48N^2 J<=1/32. Its domain control comes from D P_band
  and full oscillator ladder norms, with M+2 output retained. Duhamel is
  evaluated along the invariant FREE preparation orbit, not the interacting
  one. Both full interacting evolutions are retained.
- The all-time bound is uniform over that prepared few-quanta sector.
  It is not small uniformly in density, in times of order N, or at fixed
  nonvanishing J as N grows. An unbounded stress observable does not inherit
  a norm estimate merely because bounded observables do.
- A positive-gap resolvent integral extends the comparison to sqrt(12H)
  clock generators. Only the restricted preparation operator difference
  is bounded; the full interaction is not. The two clock dynamics are
  compared in a common canonical positive-frequency initial-data chart,
  not by claiming equality of old source-dependent wavefunction encodings.
- The hard-mode witness starts in the soft scalar/charge projection and
  exits it at positive J. The identical pair has the exact sqrt(2) Bose
  normalization; the charge form factor uses the full-carrier resolvent
  result, with the new L5 endpoint recomputed rather than copied from L3.
- Positivity of the leakage-coefficient difference follows from orthogonal
  total-K sectors. Only first strong time differentiability is needed;
  no Dom H^2, analytic coupling expansion or uniform little-o bound is claimed.

## Systematic debugging and regression

A domain review found an initially implicit unit-frequency reference
vacuum where the physical scalar vacuum was required. The systematic-
debugging workflow reproduced the mismatch: its reference occupation is
(Omega/omega+omega/Omega-2)/4, which is 1/8 at Omega=1, omega=2. The new
regression first FAILED. Choosing Omega=omega makes it zero, while an
exact cosine/sine calculation confirms that the translation generator
is independent of that common reference frequency.

The documentation now separates the all-species compression theorem from
the dynamical scalar/charge projection tensored with identity on other
free species. No unproved stationary auxiliary vacuum is assumed. The
checker passes after the change; an isolated mutation to the old unit
reference is rejected under optimized Python. The auxiliary test-driven-
development skill referenced by the debugging skill was unavailable; the
failing/passing regression was implemented directly in this repository.

Two new checkers (38/49 groups, 11 provenance inputs each), 21 prerequisite
runs and 28 infrastructure/source/semantic fixtures have distinct counts.
Five semantic mutants and all missing/changed source pins are exercised.
Checkers and fixtures are run normally and under optimization from /tmp.
Saved manifests contain full stdout and source inventories; verification
of their hashes is record consistency, not theorem certification.

Only Round23 research files and three navigation entries are added.
Earlier evidence is preserved, with old manifest checks rather than
regenerating it. New manifests, syntax, links and whitespace are checked
before handoff. Concurrent paper, ledger and v472 changes remain untouched.
No commit/push, paper/web release, T1-T8/TOE/RH or empirical promotion.
