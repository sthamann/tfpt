# Round21 source, mathematical and implementation review

2026-09-07. Single-agent review; no independent reviewer is claimed.
The author checked the source definitions, derived the proofs and ran
the exact and adversarial tests. This is not formal proof certification.

## Source and sign audit

- The original actual Ward module, E8 transport proof/checker, Round20
  domain and energy definitions, original constraint-chart note and
  Round20 runner are eight hash-pinned inputs. They are imported only
  after the input firewall verifies all pins.
- The sign convention is W=exp(-i kappa sum xi.J). The old note named
  minus xi.J as S; Round20 used plus xi.J. Round21 follows Round20 and
  explicitly reconciles that notation before deriving the new term.
- The source is the old scalar rho_n,-j, not the full D+V+L energy density.
  The complete E8 Gram and cocycle are kept. Two endpoint signs cancel
  on inverse hops, while the odd-Gram sign survives overlapping hops.
- No native zero mode was added. Systematic debugging found that the
  initial uniform xi_r=1 illustrative fiber violated the old chart's
  P0 xi=0 condition. A newly added guard FAILED on that initial profile.
  The source alone was changed to the explicit zero-mean profile; the
  actual weighted Ward Hessian and kinetic weights were propagated.
  The guard, all canonical-matrix tests and the beyond-edge witness then
  passed. An isolated mutation back to a uniform profile fails under -OO.
  The referenced auxiliary test-driven-development skill was unavailable;
  the failing/passing regression was implemented directly in this repo.

## Mathematical boundaries checked

- The all-charge direct integral uses quadratic self-adjoint closures
  and a continuous metaplectic path; the final symplectic matrix does
  not determine its sign. Bounded L^W needs no convergent operator-norm
  Taylor series. Whole-parent conjugation and a changed-hop-only model
  are explicitly distinguished. Domain and clock assertions use the former.
- Nonlocality evidence is an exact actual-cubic third-order coefficient
  outside the original edge; it is not an all-distance propagation theorem.
  An independent coefficient ODE rejects reversed matrix multiplication.
- The all-J additive momentum proof is an infinite-carrier diagonal-
  block argument, not a finite matrix exhaustion. A scalar multiplication
  quadratic cannot cancel a scalar-independent charge commutator.
  L=2, uniform profiles and arbitrary fixed total-charge sectors are
  explicitly tested with their correct different conclusions.
- The stronger mixed-correction result is restricted to J=0 and a
  differentiable lambda expansion with the stated free seed. Actual
  degenerate cubic modes and untruncated oscillator actions give its
  nonzero coefficient. The independent force-polynomial calculation agrees.
  Equal-energy matrix elements of [H0,P1] vanish for ANY admitted P1;
  this excludes more than a polynomial ansatz without claiming all-J closure.
- Pure-point diagonal charge translation, actual off-diagonal charge
  current and the finite crystal-momentum logarithm are different objects.
  None is promoted to a complete relativistic stress tensor.
- The background primary sources are
  [Combescure–Robert](https://arxiv.org/html/math-ph/0509027v1) for quadratic
  evolution and [Kato–Sakamoto–So](https://arxiv.org/abs/0803.3121v3) for
  separate lattice-derivation context. The model-specific identities and
  obstructions are derived here, not quoted as consequences of those papers.

## Test and integration audit

Two new exact checkers (32 and 63 groups, each with eight provenance checks),
16 prerequisite runs, and 25 runner/source/order mutation fixtures are
recorded separately. The test runner and both checkers are also exercised
under optimized Python from /tmp. Previous rounds and their evidence are
not rewritten. New normal/optimized manifests, local links, syntax and
whitespace are checked before handoff; see the saved JSON evidence.

The integration adds only Round21 research artifacts and navigation entries.
The pre-existing paper, status ledger and v472 modifications are unrelated
and preserved. No commit, push, paper/web release, T1–T8 or empirical change
is part of this round. A fully derived microscopic TOE remains unproved.
