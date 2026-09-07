# Round27 source and analytic review

2026-09-07. Single-agent derivation and review with separate exact
regressions. No independent human, second-agent or proof-assistant
certification is claimed. General statements rest on the displayed
arguments and hypotheses, not finite test coverage alone.

## Reference and positivity

- The same signed g=0 Hamiltonian and symmetric primitive Euclidean
  regulator are retained. The scalar kinetic/hopping factors commute
  with each other, not with the charge-dependent potential.
- Q=S* exp(-delta H_hop) S and Q_D=S* S use the SAME S. Cyclicity moves
  the words into C=S S*, preserving scalar noncommutativity and all
  charge-dependent Gaussian weights. Replacing C by scalar eigenvalues
  or dropping the charge-dependent determinant would not be this proof.
- The eighteen pins include the original E8 source, normalization, Ward
  input and Round25/26 derivations. Code-graph search returned no Round26
  nodes, so the known local source paths were read directly.
- Scalar spectral Jensen applies because every original hop changes the
  full profile. It is not an assertion that exp is operator convex.
- Pinching covers every charge block and retains the whole scalar space.
  The infinite countable partition follows by finite pinching with one
  complement block, then a monotone sum of nonnegative contributions.
- Trace-power comparisons use Schatten contraction or eigenvalue ordering.
  The stronger lower bound is not promoted to a false Loewner order.
  An exact negative quadratic-form witness guards that distinction.
- Any nonempty fixed total-charge sector admits Z_D>0. Only the explicit
  charge concentration envelope reuses the neutral zero-profile lower
  bound; the universal sign/reference inequality does not need neutrality.

## Absolute words, tails and errors

- C has nonnegative scalar integral kernels, and bare translations are
  sector-preserving unitaries. The unsigned trace equals the sum of
  moduli BEFORE cancellation of the original profile/word phases.
  It is not the modulus of a resummed signed trace.
- Holder controls the complete joint scalar/charge trace of each word
  tuple. Positive coefficients sum with the correct total-order
  multinomial weights. The exp(-theta) hopping constant is retained.
  A separate positive-operator unsigned comparison checks the upper bound.
- Finite Z_D establishes Tonelli/Fubini at fixed regulator only. No
  infinite-volume or time-refinement interchange is smuggled in.
- Hop tails lose the Poisson exp(-theta) upon division by the lower
  reference. Charge and memory errors still pay exp(theta). Removing
  those factors merely because the new Theta penalty disappears is wrong.
- R_K commutes with C but not with hopping. Holder gives p_D^(1/T),
  not p_D; the checker supplies a counterexample to the latter shortcut.
  Reference heat splitting uses beta/2 before taking the T-th root,
  which restores delta in the decay exponent afterward.
- Charge cutoffs concern sampled boundaries only. Intermediate charge
  states inside retained words, including those outside the box, remain
  in the computation with their actual phases.
- The error decomposition restricts histories first, approximates the
  retained scalar weights second, and sums the three budgets. The
  normalized 2rho/(1-rho) conclusion remains limited to bounded one-time
  charge observables with an exact positive transfer as their reference.

## Nonzero memory example and fair cost claims

- L9/ell3 gives the actual 27 interiors of 8 sites, 513 retained sites,
  and cell gap 4 for a=m=1. The chosen q_b=1/4 is exactly compatible
  with delta=3/4 and that gap.
- q_0=1/2 corresponds to mass squared 8/9, BELOW the physical value 1.
  It provides a rigorous upper inverse-trace comparison. Using an upper
  mass here would point the error bound in the wrong direction.
- R12 truncates eight cyclic time offsets. Its error bound is nonzero
  and remains below 1/300 after the sign budget at theta=1. Full R16
  returns exactly zero approximation error. The fast determinant is
  never truncated or replaced by a local normalization.
- The coupling J=1/866052 is specified, not inferred from TFPT or data.
  This witness has weak total hopping; it is not evidence of an efficient
  all-J approximation. u and nu may nevertheless be any nonnegative
  values within the same g=0 model.
- Exact ceil roots, upward exponent bounds, factorials and the positive
  logarithm margin are guarded by typed mutations that remain active
  under -OO. All original source pins are checked before loading sources.
- The old inequalities were also optimized over the cutoff integers.
  Their refined K4035/P956 remain worse than K2670/P354, so changing
  the search grid alone cannot explain the gain.
- Candidate digit counts are conservative upper counts for naive
  enumeration, not executed runtime or a lower complexity barrier. No
  complete partition value, data fit or external prediction is produced.

## Literature and project boundaries

Primary-source context was checked in
[Perez-Garcia et al., Contractivity of positive and trace preserving maps](https://arxiv.org/abs/math-ph/0601063)
and [Hansen-Pedersen, Jensen's Operator Inequality](https://arxiv.org/abs/math/0204049).
Those are context for the norm/Jensen tools, not prior TFPT-specific
completion claims. The proof gives its own explicit pinching argument.

No prior round artifact is rewritten, no unrelated work is absorbed,
and no T1-T8, empirical, RH or TOE status is promoted. Paper/website and
remote publication are unchanged in this round.
