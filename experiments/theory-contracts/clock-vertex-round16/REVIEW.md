# Internal constructive review: vertex-preserving clock compatibility

2026-09-06. NON-RH. This is an internal agent-assisted review record, not
external peer review, a formal proof-assistant certificate, or TOE validation.
The research subagent authored PROOF.md after deriving the characteristic
gauge independently of the root's constructive check. The root separately
read the complete proof and checked the group, domains, radial trace and
averaging arguments. The subagent then independently reviewed and reran the
root-authored checker. Prior-round files were not changed by this subtask.

## Constructive result and review disposition

PASS within the explicit finite-regulator assumptions. The actual Round15
H_vp is unitarily equivalent to K_c+A_+ by a measurable physical-fiber
unitary S, with equality of the complete groups and transported Stone
domains. Thus adding the unchanged quadratic clock, the existing auxiliary
primary prescription and declared relational homogeneous momenta gives one
joint constrained quantum model without changing H_vp's original first
interaction vertex.

The result is not a proof that the old microscopic model selected H_vp,
the characteristic section, the clock or the relational momentum list.

## Specific failure modes checked

- The actual divergence has positive rank N=n-1 on every retained lattice.
  Its zero-velocity set is a proper null subspace, not just c=0. The
  construction would not apply by this argument to an identically zero b.
- For vector r, the correct section is r-(r.bv)bv/|bv|^2, not r=0.
- Propagator composition gives U_vp=S U_separated S* for the full group,
  not merely a guessed differential commutator. It retains the given
  Round15 self-adjoint realization and its operator domain.
- The sign in S=V(tau)exp(+i tau A_+) and the opposite sign of the clock
  group factor exp(+it P_0^2/12) are necessary.
- S is not claimed continuous near the zero-velocity set. Common radial
  scaling fixes tau, which permits the actual strong zero-fiber input and
  dominated convergence. A scalar model explicitly refutes replacing this
  radial statement with ordinary unrestricted continuity.
- B=S A_+ S* is not h(c), and K_tilde=S K_c S* is not bare K_c. The
  reducing tube uses B-P_0^2/12 and subsequently its W_0-transport; the
  raw A_+-clock tube and a total-C spectral interval are not substituted.
- Full joint multiplier domains permit spectral cancellation. They are
  not replaced by intersections of the summands' separate domains.
- All auxiliary, gravitational and relational momentum spectral measures
  are transported by the same ordered unitary W=W_0 S Z*. The S and
  auxiliary factors need not commute.
- The time/c group is semidirect, not abelian. Its Haar measure is
  unimodular because the actual shear has trace zero.
- Absolute joint averaging follows from exact cancellation of W inside
  matrix elements, polynomial reference phase bounds and independent
  rapid clock-Fourier decay. It needs no derivatives of measurable S.
- The physical shell is defined as a functional on transported tests.
  The proof does not multiply an arbitrary delta(c) distribution by S.
- The half-density cannot pass through the homogeneous physical projector
  without commutation. Fixed-subspace autonomous dynamics is not claimed.
- The auxiliary addition retains its declared gauge-unfixing and is not
  promoted to equality with the original off-shell second-class operator.

## Reproduction performed during review

The root's checker.py was read in full and executed from a foreign working
directory with the repository's SymPy environment in both ordinary and
optimized Python modes. Both independent executions exited successfully
and reported 38 exact check groups PASS. The checker uses explicit raised
exceptions rather than removable assert statements. It performs no output
file writes, and no current-directory import dependency was observed.

The checks distinguish actual L2/L3 divergence matrices and the normalized
(pi,pi,0) block from explicitly labelled scalar and two-channel spectral
models. The scalar phase controls include non-radial discontinuity and
unbounded orbit-time negative controls. Finite spectral models check
noncommuting order and normalization only; no interacting spectral or
canonical-commutator truncation is called a proof.

The analytic claims depend on the full proof and its already established
Round15 propagator input. The 38 exact groups are regression controls;
they do not establish the measurable-unitary or all-Hilbert-space claims.

## Remaining boundaries

No full TOE, local homogeneous current, preferred microscopic selection,
clock treatment of the classical p_0=0 vacuum, continuum/Lorentz limit,
or efficient implementation is obtained. Near the null exceptional set,
the characteristic gauge can require arbitrarily long evolution. The
construction is a genuine existence/domain/positive-norm result for the
declared finite quantum model and is presented only at that scope.
