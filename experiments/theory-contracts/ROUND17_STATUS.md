# NON-RH Round17: full source dynamics, joint clock embedding and local charge energy

2026-09-06. Local research integration on repository base
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`, also the actual remote main
verified at the start of this round. Earlier research and concurrent
paper/ledger/v472 edits are preserved. No commit, push, public release,
empirical scorecard change or full T1--T8 promotion in this round.

## The original Gaussian embedding now carries the full stabilized dynamics

The [full constraint-parent construction](full-constraint-parent-round17/PROOF.md)
and its [source-limit proof](adiabatic-source-round17/PROOF.md) extend the
Round15 local positive base through the ACTUAL scalar source operators Q_a.
For X equal to the subtracted local parent B_delta,eta, its effective A_delta,
or the limiting A_0, the declared closed form is

    h_X(c) = q_X + g sum_a c_a <Q_a> + g^2 |c|^2 sum_a ||Q_a psi||^2.

This is a new full completion built on the local base; it is not a claim
that the unmodified local base already contains these global terms.
Its common form domain, energy estimates along the constraint characteristics,
all-time unitary propagators and strong constraint covariance are controlled.

More strongly, the ORIGINAL physical Gaussian embedding J_delta,eta satisfies

    V_B,c(t) J - J V_A_delta,c(t) -> 0,

strongly, uniformly on compact time intervals, first eta->0 at fixed delta.
The subsequent delta->0 limit gives the full source-stabilized limiting model,
including its 4n+2 extra free modes. The statement is not just a compression
J* B J, a finite spectral calculation, or convergence after a freely chosen
new embedding. The corresponding full constraint-space unitary groups
converge by dominated integration over characteristics.

The load-bearing new estimates handle the actual ordered quadratic
operators and their fourth-order products: Q_a J-J Q_a is controlled by
eta^(1/4) and eta^(1/2), while Q_a Q_b J-J Q_a Q_b has terms through eta.
Gaussian derivatives, an explicit common FORM core, varying-space lower
bounds and weak-solution uniqueness yield full-norm convergence. No
essential self-adjointness of the fourth-order expression on an unproved
operator core is assumed. These are fixed-lattice, statewise limits with
compact-time uniformity, not uniform cutoff-independent error rates.

## One compatible clock, constraint group and positive physical norm

The existing characteristic gauge S_X represents the SAME full Hamiltonian,

    H_X = S_X (K_c + X) S_X*.

The dynamical embedding E_dyn=S_B J S_Y* is exactly isometric and
asymptotically dynamical. The source theorem also proves E_dyn-J->0 strongly.
The correct quadratic-clock spectral charts give another embedding,

    E_clock = W_B J W_Y*,      C_X = H_X - P_0^2/12.

E_clock exactly intertwines the clock/constraint group at finite parameters
on the declared proper negative-sheet tube. It retunes the clock momentum;
it must NOT be replaced by E_dyn tensor identity in the old clock coordinate.
The positive lower bound e_m>0 supplies a common admissible tube. Physical
square-root clock readouts and weighted clock-slice isometries are inherited
separately from Round16: their dynamics converges in the adiabatic limit,
not exactly at finite parameters.

There is also an explicit compatible homogeneous seed. With the triangular
displacement F_delta and the joint slow/fast compact rotation group, set

    R_B = F_delta (R_D tensor R_fast) F_delta*.

It preserves J exactly and intertwines the compact projectors and the
resulting positive joint physical norm. This is a declared displaced seed,
not the original native parent momentum at nonzero coupling; no commutation
with the positive parent B is invented. At zero coupling it recovers the
native free action. A source-level L=3 centered-flow defect is exactly -5/4,
demonstrating why the native interacting seed cannot simply be reused.
Joint compact closure is retained; no false factorization of its projector
or identification of physical fast modes with gauge auxiliaries is made.

The original constraint-source first vertex is retained at finite parameters.
The complete original TT-plus-constraint first dressed vertex is recovered
only after the specified sequential limits. The finite local-base first
vertex is different. The full parent costs 35n+4(n-1) canonical pairs before
clock and optional old gauge auxiliaries; the target physical space is
embedded as a subspace, not equated to the entire parent physical space.

## A separate local rotor parent exactly realizes the full charge energy

The [charge construction](local-charge-parent-round17/PROOF.md) replaces the
single global charge-energy register by M>=3 links of U(1)^8 rotors on a
cycle. Nearest-neighbor Gauss constraints force uniform integer electric
flux. The explicit unitary identification is

    |n> -> |n,...,n>,      H_E = sum_j E_j^T G E_j / (2M).

On the Gauss kernel this is exactly the whole previous charge Hamiltonian
n^T G n/2, including every Gram cross-term. Compact Haar averaging gives an
ordinary nonzero physical Hilbert space and positive norm. The Hamiltonian
is positive and self-adjoint on its explicit weighted sequence-space domain,
with compact resolvent. Its physical gap is one; the unconstrained gap is
1/M. Gauss is an imposed constraint, not an emergent enforcement gap.

The frozen cocycle and ALL charged shifts lift exactly as winding Wilson
operators times an explicit phase at a marked link. The spinor fourth
power remains a genuine nontrivial neutral translation. Finite-code
multiplicity and bounded gauge-invariant interactions have controlled
domains and all-time dynamics.

This resolves local ENERGY and local GAUSS terms for this declared ring.
It does not produce local charged fields: any bounded operator missing one
link has charge-diagonal compression to the physical space. Charge-changing
operators therefore require the whole cycle in this parent. On a periodic
3D lattice, Gauss leaves 8(2n+1) integer cycle coordinates, not the desired
eight; the L=3 incidence check gives 440. The construction is abelian U(1)^8
with the fixed E8 charge metric, NOT a nonabelian E8 gauge theory.

## What is still missing

The full constraint-square term g^2 |c|^2 sum Q_a^2 is spatially global even
though its positive base is local. The displaced momenta, subtraction,
clock sheet, stabilizer and ring normalization are declared choices, not
derived unique microscopic data. The two parents above are not yet ONE
shared local 3+1D model with the required interacting observables.

A full local microscopic parent, local charged scaling fields, selected
chiral matter and flavor, measure and regulator-independent relativistic
continuum limit remain open. Earlier T1--T8 obligations are conjunctive:
none is promoted to universal or empirical closure by these results.
There is no RH claim.

## Reproduction and review

Run `run_round17.py` with the repository research Python to rerun three
new checkers and six unchanged prerequisites. The three new checkers contain
34, 45 and 45 new exact check groups respectively; the rotor's two provenance
controls and nested predecessor group are reported separately, not counted
as new results. Finite exact checks support, but do not prove, the analytic
domain and limiting theorems.

The [internal review record](ROUND17_REVIEW.md) and
[detailed independent argument review](full-constraint-parent-round17/REVIEW.md)
describe the checks and limits. Twenty runner/provenance regression fixtures
are run both normally and with an optimized parent interpreter. The
[aggregate evidence](ROUND17_VALIDATION.json), per-folder validation records
and [runner evidence](ROUND17_RUNNER_VALIDATION.json) retain source digests.
`run_round17.py --check-manifests` verifies evidence completeness, successful
recorded executions and unchanged audited sources; it is not a proof checker
or signed attestation. Round10--16 evidence is preserved and checked separately.
