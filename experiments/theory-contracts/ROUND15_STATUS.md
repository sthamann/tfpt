# Non-RH TOE research: Round15, stability selection, original vertex and local dynamics

2026-09-06. Local research integration on repository HEAD
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`; actual remote main was
reverified at the same revision. No commit, push or public release in this
round. Earlier proof/manifests and concurrent paper/ledger/v472 edits are
preserved. No full T1–T8 gate or empirical scorecard row is promoted.

## Outcome

Four bounded problems now have constructive answers: the sharp minimum
positive completion, a covariant quantum realization retaining the ORIGINAL
first interaction vertex, a local positive dynamical family with a proved
quantum TT limit, and an exact eight-channel realization of the frozen
charged lattice. They share explicit inputs where stated; they are not
silently identified as one microscopic TFPT Hamiltonian.

| Construction | Result | Exact remaining price |
| --- | --- | --- |
| [Minimal stability](minimal-stability-round15/PROOF.md) | The chosen R_min=T^T L^-1 T/2 is the unique pointwise least stabilizing homogeneous quartic correction. Quantum and classical necessity both hold at every fixed g!=0. | Fixed kinetic/free/first-vertex input, quartic correction class and least-correction principle are still selection assumptions. |
| [Original-vertex quantum completion](vertex-preserving-round15/PROOF.md) | A new second-constraint-ideal form yields all-time unitary evolution, strong constraint covariance and the same positive physical norm, without changing the first dressed vertex V1. | New g^2 source-operator squares and a specified form realization; not the unchanged all-order H_sr or automatically the Round14 joint clock model. |
| [Local dynamical parent family](local-parent-round15/PROOF.md) | A local positive 35-pair/site Hamiltonian has a controlled, norm-preserving quantum limit to the chosen TT/matter factor. | 28 extra oscillator pairs/site, singular sequential limits, explicit divergent energy subtraction and 4n+2 surviving free tensor modes. |
| [Eight-channel charged lattice](matter-geometry-round15/PROOF.md) | An exact A3-to-D3 isometry identifies the frozen charge with (1/2)^8; GSO, all four grades, cocycle and nonzero charged corners are explicit. | Abstract lattice/Fock identification, not QWZ spin-field scaling or 4D chirality. A separate finite transporter changes the seam/code prescription. |

## 1. The physical positive term is the sharp least stabilizer

Keep every existing kinetic and quadratic term and g Q.T(phi). In the
class g^2 C_4(phi) of real homogeneous quartic scalar corrections,

    H is classically lower bounded
      iff H is quantum lower bounded on compact smooth tests
      iff C_4(phi)>=R_min(phi)=T(phi)^T L^-1 T(phi)/2.

Completing the full TT square proves sufficiency. Necessity is a genuine
infinite-Hilbert-space variational statement: if C_4-R_min is negative at
u, packets with phi=t u and Q=-g t^2 L^-1 T(u) have negative order-t^4
energy; all Gaussian corrections are at most order t^2.

For the actual full 2^3 lattice, all fourteen TT oscillators retained,
the coefficient family C_4=kappa R_min has exact Gaussian expectation

    3g^2(kappa-1)t^4/256 +(4+43kappa g^2/576)t^2
                                +91/2+43kappa g^2/288.

Thus kappa<1 fails even quantum lower boundedness. All admissible quartics
are R_min plus a nonnegative quartic. Stability alone does not remove that
family; selecting the least member does. Positivity on the actual source
image also does not imply uniqueness of a source-matrix representation:
nine TT source polynomials vanish identically at L=2, although all fourteen
free oscillators remain. Fixed-coupling mass compensation, additive energy
shifts and higher-degree corrections are explicit counterexamples outside
the theorem's hypotheses.

## 2. The first coupling vertex no longer has to be sacrificed

Round14 solved a separated completion by removing the old first-order
constraint-ideal term. The new construction instead RETAINS it. Let
Q_a denote the actual Weyl-quadratic sources (Bcal,-B_v J_v), c=(r,v):

    H_vp = K_c+A_+(g)+g sum c_a Q_a
                              +g^2|c|^2 sum Q_a^2.

The added term is defined as a sum of positive operator-square forms,
not by silently dropping Weyl-ordering constants. It is second order
both in g and in the constraints. The free Hamiltonian, original first
dressed vertex V1 and reduced physical A_+ are unchanged.

For c!=0 the common closed form domain is
Dom(A_+^(1/2)) intersect all Dom(Q_a). Along every nonzero characteristic
c(t)=exp(t A_c)c0, its positive form norm obeys

    |partial_t(h_c(t)+1)| <= 5||A_c|| (h_c(t)+1).

This supplies an all-time common-form propagator and then a self-adjoint
full generator with strong spectral constraint covariance. The energy
bound remains uniform near c=0; a weak-equation argument proves strong
propagator convergence to exp(-it A_+) there. A specified Gaussian-regulated
constraint average consequently gives exactly <F(0),G(0)> and the same
physical evolution. Unregulated absolute Haar convergence on its entire
continuous test space is not asserted.

This is a form-selected self-adjoint realization, not a proof that all
extensions of every minimal expression coincide. Its added metric and
source squares are new off-shell input. The separated Round14 clock tube
cannot simply be reused for this different operator. The two constructions
are deliberately kept distinct until a joint identification is proved.

## 3. A genuinely local dynamical family reaches the positive TT model

The local parent uses one scalar, six unrestricted tensor coordinates
and 28 actual auxiliary oscillator coordinates per site. Its potential is
a sum of local positive squares, and all kinetic energies are positive.
It has complete classical flow and a unique self-adjoint quantum closure.

Exact fast-coordinate elimination gives the positive source kernel

    R_delta=[ell+delta+delta^-1 NN*+(delta+delta^-1 ell)^-1]^-1.

At fixed lattice it converges to P_TT ell_nonzero^-1, with the whole
homogeneous source correctly removed and an explicit O(delta) matrix bound.
The full TT quadratic/cubic/quartic square converges together; changing
only the quartic term would miss part of the result.

A displaced Gaussian isometry J_delta,eta has exactly the ordinary
positive slow norm. Its actual operator residual after the explicitly
specified fast zero-point subtraction obeys, on every compact smooth test,

    ||(H_delta,eta-E_fast)J psi-J A_delta psi||
                     <= C_delta,psi eta^(1/4)+D_delta,psi eta^(1/2).

A core/resolvent argument proves strong intertwining of the full unitary
groups, uniformly on compact time intervals. First eta tends to zero at
fixed delta; then delta tends to zero at fixed lattice. The result is
A_+ tensored with 4n+2 extra free tensor modes, not their gauge deletion.
Their independent energy matters for any clock construction.

Finite interaction range here is not relativistic microcausality. The
encoding is spatially nonlocal; the limiting scalar response remains the
one already proved nonlocal. Constants are not volume uniform, the bare
contact diverges, and no bounded-cost continuum parent has been obtained.

## 4. Frozen matter charge: an explicit eight-channel map

The exact map on the trace-zero A3 coordinates is

    B y=((y1+y2-y3-y4)/2,
         (y1-y2+y3-y4)/2,(y1-y2-y3+y4)/2).

It sends A3 onto D3 and omega_f onto (1/2,1/2,1/2), so the literal
D5+A3 lambda becomes (1/2)^8. The full extension is
D8 union (D8+s), with internal grade r=2 sum_(i<=5)x_i mod4.
Its four root counts are exactly [52,64,60,64]. GSO projectors, an
integral even unimodular basis, cocycle and charged shifts on one Hilbert
space are explicitly constructed.

The relative fermionic monodromy is (-1)^r, not i^r. A separate finite
QWZ candidate therefore uses a Z^2 seam, a new invariant code and an
endpoint Majorana pair. It has four nonzero projected charged corners.
Its defect is a coefficient on the WHOLE far transverse cut, plus the
local neighborhood of the pair, multiplied by the disorder string.
The new regression rejects the false single-transverse-bond replacement.
No width-uniform point locality follows.

The operator distinction remains decisive: lattice T_s^4=T_(4s)!=I,
while the finite register transporter has T^4=I. A scaling identification
must preserve the missing neutral charge data; matching grade counts does
not do that. Nothing here selects generations, neutrino masses, or a
four-dimensional anomaly-free chiral measure.

## Verification and remaining dependencies

Run from the repository root:

    experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/run_round15.py

Four new checkers record 49, 35, 50 and 29 exact groups respectively; the
last checker additionally records five floating source-matrix groups.
Six unchanged prerequisite runs are separate. Twenty infrastructure
fixtures are run under each of normal and optimized parent settings.
Commands, transcripts and artifact/source hashes are retained in
ROUND15_VALIDATION.json, per-folder validation.json files and
ROUND15_RUNNER_VALIDATION.json. The runner's --check-manifests checks
inventory/hash/record consistency, not proof correctness.

The independent internal proof reviews and the resulting source-locality
correction are recorded in [ROUND15_REVIEW.md](ROUND15_REVIEW.md).
These are agent-assisted reviews, not external peer review or proof-assistant
certification. Existing Round10--14 proof/manifests remain unchanged.

The remaining load-bearing task is ONE microscopic identification, not an
arithmetic sum of these constructions: select the stability/constraint
prescriptions, recover the intended local observable net and uniform
continuum behavior, identify the charged scaling fields and derive the
chiral/flavor/measure and clock-state data on that same parent. T1--T8 as
full physical contracts remain open. No paper/website/ledger promotion is
made by this local research round.
