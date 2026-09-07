# Internal independent review: full-constraint dynamical parent connection

2026-09-06. NON-RH. This is an internal agent-assisted mathematical review,
not external peer review, a formal proof-assistant certificate or TOE validation.
The reviewer independently investigated the characteristic embeddings and
then read both the root-authored PROOF.md and the separately authored
[source-evolution proof](../adiabatic-source-round17/PROOF.md) completely.
The reviewer did not author either of those two proofs.

## 1. Disposition and what was actually established

Analytic PASS within the stated finite-regulator assumptions. The positive
local base B_delta,eta can be equipped with the same actual Weyl-quadratic
constraint sources as the Round15 vertex-preserving model. Its closed-form
full generator, actual Gaussian dynamical limit, correct quadratic-clock
tube, displaced homogeneous relational momenta and positive physical norm
coexist in one specified construction.

This result is narrower than a spatially local full microscopic parent:
the base is local, while the added global constraint-square term is not
proved local. The complete original first vertex is recovered at the
target limit, not literally at every finite parent parameter.

## 2. Independent encoding calculation and its exact scope

For each positive base X the Round16 characteristic gauge gives equality
of complete unitary groups and transported Stone domains,

    H_X=S_X(K_c+X)S_X*.

For the normalized Gaussian isometry J:H_Y->H_B, the independently derived
encoding

    E_dyn=S_B(I_c tensor J)S_Y*

is an exact isometry and exactly intertwines every bounded c multiplier.
Its error is identically

    U_B(t)E_dyn-E_dyn U_Y(t)
      =S_B [exp(-it K_c) tensor
                   (exp(-it B)J-J exp(-it Y))] S_Y*.

Thus the positive-base dynamical limit alone already proves its strong,
compact-time intertwining. No nonautonomous convergence is hidden in this
weaker statement. It is not exact dynamics at finite eta.

The stronger proof now supplies actual-source nonautonomous convergence.
At each fixed regular c, the characteristic time tau(c) is fixed and finite.
The two physical group limits therefore imply

    S_B(c)J-J S_Y(c) -> 0

strongly. Its norm is bounded by two. Dominated convergence on the direct
integral extends this to L2(dc), and E_dyn-I_c tensor J tends strongly to
zero. The proof does not assert a uniform orbit-time bound near bv=0.

More directly, the full group formula can be reparametrized by the initial
characteristic label c. The common phase cancels and the shear has Jacobian
one, so the difference with the actual encoding is bounded by the integral
of the individual characteristic differences. Their compact-time suprema
tend to zero and are dominated by 2||F(c)||. This verifies the full-group
claim using the original Gaussian embedding, not merely a new abstract
embedding constructed to simplify the dynamics.

## 3. Review of the direct-source/nonautonomous proof

The exact directional Gaussian derivative bound and its singleton/pair
partition chain rule retain every derivative through order four. Hence
they control each actual Q_a and every ordered product Q_a Q_b, including
operator-square ordering constants. They do not replace noncommuting
sources by commuting scalar coefficients.

The following additional analytic steps are essential and are present:

- A real homogeneous Weyl quadratic has constant second-derivative,
  linear first-derivative and quadratic multiplication coefficients.
  Radial cutoffs therefore converge in all Q_a graph norms using the
  positive-base slow kinetic bound. Compact convolution then converges
  simultaneously in those graph norms and the base form norm. This proves
  a common FORM core; no fourth-order operator-core theorem is assumed.
- The exact frozen fast oscillator inequality leaves the full slow kinetic
  and effective potential, so q_B controls the vector-valued A_delta form.
- The derivative of J*Psi has an additional term involving partial f.
  That coefficient is unbounded globally, and the proof correctly estimates
  it only on compact slow regions before exhaustion. It does not silently
  assume a global small-gradient estimate for every projected approximant.
- Compact-test source residuals identify the weak limiting Q_a distributions.
  The individually self-adjoint Q_a and their compact smooth cores turn the
  maximal L2 distributional condition into membership in their actual domains.
- The weak limit lies in the complete common form domain. The common form
  core extends its equation from compact tests to that domain. Hilbert-triple
  uniqueness identifies the limit with the intended nonautonomous propagator.
- Equality of the two full-state norms and the limiting cross amplitude
  proves uncompressed strong convergence. It is not merely convergence
  after projecting with J* or agreement of compressed expectations.
- The delta limit uses local uniform convergence of nonnegative potentials
  and compact exhaustion. It does not assume the global form domains remain
  identical across the degenerate limit.

The source proof consequently justifies the stronger direct-J theorem.
It does not turn a bounded core residual into a uniform state-independent
many-body propagation rate. The stipulated limit order remains necessary.

## 4. Clock embedding: exact gauge representation versus limiting readouts

The exact clock-tube encoding is different from E_dyn. With

    W_X=S_X Z_X*,     W_X* C_X W_X=K_c+M_lambda,
    E_clock=W_B(I_(c,lambda) tensor J)W_Y*,

the reference constraint is independent of the physical energy label.
Thus E_clock exactly intertwines the whole c/time constraint group and
preserves its positive norm at every parameter. It compensates changes
in physical energy by changes in clock momentum through the spectral
charts. E_dyn tensored with the identity on the old clock need not even
map one chosen clock tube into the other, since BJ differs from JY.

This exact constraint-group fact does not assert exact physical clock-time
dynamics. The latter are the energy-dependent square-root readouts. Their
weighted isometry D_B J D_Y^(-1) and asymptotic dynamics use the independent
Round16 spectral/clock convergence result. This separation prevents an
abstract clock relabelling from being promoted to a dynamical solution.

The correct positive operator defining each tube is S_X X S_X*, not the
instantaneous source form h_X(c), the bare X in the original variables, or
the full non-semibounded H_X. All half-density factors remain on their
correct sides of noncommuting projections.

## 5. Homogeneous generators and the compact-group issue

The reviewer independently checked the new seed prescription. The triangular
translation F_delta is unitary with Jacobian one, and J=F_delta(· tensor chi).
The fast quadratic matrix commutes with the native centered orthogonal
representation because its constituent spatial operators have the same
translation-invariant Fourier multipliers. Therefore its normalized Gaussian
is exactly invariant and

    R_B=F_delta(R_D tensor R_fast)F_delta*,
    R_B J=J R_D,      Pi_B J=J Pi_D

hold without approximation. The common compact closure of the JOINT native
representation supplies the Haar projector. The proof does not replace that
closure by a product of independently closed groups.

At g=0, f_delta is a linear equivariant map, so F_delta commutes with the
native joint flow and the displaced seed recovers the original free parent
generators. At nonzero g, the source is quadratic and centered differences
are not a product derivation. Hence this is an explicitly new displaced
seed, not a proof that J intertwines the unchanged interacting local currents.
No commutation of that seed with B is assumed; its clock-relational version
commutes with the full clock constraint after the common spectral transport.

On the target scalar/TT-plus-spectator space the centered group acts on
both factors with common parameters. Its invariant subspace can include
correlated opposite charges. Consequently Pi_D is not assumed equal to
Pi_+ tensor Pi_extra. A normalized isotropic spectator Gaussian is invariant,
which is enough to give Pi_D I_sigma=I_sigma Pi_+ and preserve the target
physical norm without that false factorization.

## 6. First-vertex and locality limits retained by the proof

The actual gravitational source term g c.Q is retained at every parameter.
The finite local base, however, has the first vertex
-g<DE-Nu-h,sigma>/delta. Its effective first vertex is
g<ell q,R_delta sigma>, and only its subsequent delta limit is the original
TT vertex. The proof correctly distinguishes these three statements.

The global product (sum c_a^2)(sum Q_b^2) permits cross terms at arbitrarily
distant sites even for hypothetically local Q_b. Actual Darboux-coordinate
source coefficients already introduce further spatial inverses. Thus the
finite range of the positive base cannot be assigned to the full constraint
completion. No encoded observable locality or relativistic causal bound is
inferred from the isometries or the existence of the full group.

The added physical fast oscillators and the separately retained gauge-unfixed
auxiliaries are kept distinct. The latter still represent a declared change
of the original second-class prescription, not simultaneous annihilation
of both partners. The real target spectators retain their energy and are
handled by the already quantified normalized approximation, not a fictional
normalizable zero-energy state.

## 7. Independent executions and a corrected witness

The reviewer read both checker implementations in full and executed each
from a foreign working directory in ordinary and optimized Python modes:

- full-constraint-parent-round17/checker.py: 34 exact groups PASS in both;
- adiabatic-source-round17/checker.py: 45 exact groups PASS in both.

Both use explicit raised exceptions, so optimization does not remove their
checks. Both resolve and import the actual Ward source independently of
the process working directory. The common source SHA-256 in these runs was
6a07fde8b3c5336abac603e1979326784d9a2c451e5a5c68b4f03f9c7aed4d81.
These are separate internal executions, not external review or an actual
interacting many-body simulation.

An initial main-checker run failed at its proposed finite equivariance
witness. The nonzero exact defect polynomial had already passed, but the
chosen datum phi(0,0,0)=1, phi(1,0,0)=2 and all other fields zero was a
node of that polynomial. The systematic-debugging workflow was applied
before accepting a replacement: the failure was reproduced in normal and
optimized modes and traced to that datum, not to the analytic statement.
The author changed the second field to one and retained both outcomes as
regressions. The corrected datum gives exactly -5/4, while the old one is
still checked to give zero. The two complete independent reruns then passed.
No physical source, proof hypothesis or equivariance statement was weakened.

Source-mutation controls and complete integrated provenance belong to the
accompanying runner/validation records. The analytic assessment above is
based on the complete proofs and independent argument checks. Passing
finite algebraic controls is not a replacement for those arguments and
does not certify a continuum, microscopic selection, or full TOE.
