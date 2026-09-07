# Non-RH TOE research: Round11, exact combinations and their limits

Date: 2026-09-06. Current HEAD and actual remote main were checked again:
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`.
This round is locally integrated research, not a release, commit or push.
Existing Round9/10 work and concurrent paper/ledger/v472 edits are preserved.

## What is newly established

| Result | Precise solution | Boundary that remains |
| --- | --- | --- |
| [Joint clock and inversion](cy-joint-equivariance-round11/JOINT_EQUIVARIANCE.md) | Honest C4 x C2 action on the rank-four boundary bundle, exactly two lift choices with necessary eighth-root phases; explicit determinant and stabilizers. Joint parity sectors refine the old flat spectrum. | No ordinary coarse Kummer descent; no selected physical projection, chiral spectrum, mass or TFPT operator family. |
| [Mixed constraints](mixed-constraints-round11/README.md) | Finite canonical dressing and second-class elimination commute. Complete mixed classical stabilization, canonical physical brackets, source-independent measure and rigorous strongly commuting quantum cross-constraints. | The full extended first vertex includes lambda tau. Matching V1 is exact after elimination. Full unreduced interacting Hamiltonian domains and microscopic locality are not supplied. |
| [All auxiliary modes](homogeneous-completion-round11/AUXILIARY_ZERO_MODE.md) | Five explicit constant slacks and removal of three redundant auxiliary coordinates yield invertible K of size 28n+2, inertia (22n+2,6n), and complete removal of all introduced pairs. | Constant source energy remains zero. This is bookkeeping for the previous zero-mean model, not homogeneous gravity. |
| [Quantum clock norm](homogeneous-completion-round11/QUANTUM_CLOCK.md) | For the postulated C=A-P^2/12 and A>=epsilon>0, convergent group averaging gives weight 6/sqrt(12E), a positive physical Hilbert completion and unitary intrinsic-time evolution. | Energy reference, global constraint and time orientation remain assumptions; classical vacuum singularity is not removed. |
| Finite translation alternative | The actual positive Hamiltonian admits a nonzero reducing invariant subspace of the genuine finite lattice-translation group. Joint R x Gamma averaging with the clock is consistent on that space. | This changes the constraint prescription; it is not the old infinitesimal momentum or a local gravitational momentum constraint. |
| [Actual-source obstruction](reduced-locality-round11/PROOF.md) | Exact finite and all-size actual-stress results show non-finite-range dynamics on the given scalar local algebra and nonpreservation of the old total momentum by the chosen g^2 interaction. | Does not exclude another dressed observable algebra, a different parent, finite symmetry restriction, or a controlled causal continuum limit. |

## Two necessary corrections to a proposed full combination

The five constant auxiliary slacks are now completely stabilized, but absorb
constant source values with **zero** energy cost. Calling that a gravitational
receiver would remain false after the algebraic completion.

The old free-matter momentum is a sharper obstruction than a missing proof.
For the actual chosen interaction on a strict cubic 6^3 lattice,

    {J_z,R} = -568433/21952,

at the explicitly supplied rational configuration with all old J_i=0.
Thus {J_z,H_+}=g^2{J_z,R} is nonzero for g!=0. Genuine one-site discrete
translation invariance is independently checked and does not imply the
false infinitesimal conservation law. The finite symmetry restriction above
is a consistent alternative, not a rebranding of the failed J_i constraint.

For the same scalar observable algebra, a second exact cubic witness is

    partial_X partial_Y R = -1762469675117/170400029184000,
    distance(X,Y)=3.

The full retained TT and local matter terms cannot cancel this first-time-
order response. An all-size cubic proof has a canonically normalized pole
3/(4 ell_z), establishing the absence of a uniform finite interaction range.
The theorem names the algebra and allowed operations; it is not an inference
of acausality from an instantaneous gauge-fixed kernel alone.

## T1-T8 status after this round

No full T-gate is closed or promoted.

* T1 still needs selection of dimension, geometry, scale and markings.
* T2 has an explicit simultaneous boundary representation, but not its
  identification with the TFPT seam and common parent.
* T3/T7 gain a complete finite mixed-class construction and conditional clock
  norm. A derived local nonlinear gravitational system, its homogeneous
  constraints and full unreduced quantum domains remain open.
* T4 still requires the actual chiral operator, measure and interacting mirror
  decoupling argument. The boundary bundle here has no holomorphic zero modes.
* T5 needs a shared controlled continuum/Lorentz limit and physical local
  observable algebra; the present chosen regulator has the precise obstruction
  above on its original scalar net.
* T6 gains a two-symmetry spectral refinement, not three family masses or a
  normalized analytic determinant connection. The geometric and dynamical
  constructions are still not a single identified model.
* T8 has conditional Hilbert/state constructions, not microscopic initial-state
  selection and common SK readouts.

## Reproduction and independent review

Run `experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/run_round11.py`
from the repository root. It emits source/proof hashes, runtime, exit codes and
full transcripts. Each subprocess has a 180-second ceiling. Per-folder saved
`validation.json` records and `ROUND11_VALIDATION.json` retain the result;
`--check-manifests` verifies hash/inventory integrity only, not mathematical
truth or a fresh execution. No finite CCR truncations or floating tolerances
are used by the new checks.

Final combined run: all six new check programs and all five unchanged
prerequisite programs passed. New runs took approximately 28.9 seconds and
prerequisites 13.1 seconds on Python 3.14.3 / SymPy 1.14.0. Evidence counts are
kept distinct: six CY unittest cases, 16 auxiliary symbolic groups, 22 clock
symbolic groups, 53 mixed-system groups, the uncounted exact actual-source
assertions, and the separately itemized independent source/projector audit.
These are not added into a count of proved physical facts.

The main review read every proof and checker. Separate independent reviews
checked the quantum-clock domains/norm, the auxiliary constant block and the
finite-translation construction. The source audit independently compared the
stress with the prior Ward formulas (648 component comparisons), the old current
(three sums and 162 flow coefficients), and all 53 nonzero-mode kernels against
an independent weighted-nullspace TT projector. This added checker is included
in the combined runner and its full transcript is retained. The
mixed-system witness includes noncommuting sources and negative controls for
an undressed source, omitted multiplier term, wrong gauge section and incorrect
extended first vertex. Unchanged prerequisite checks are reported separately.

## Next decisive construction

Specify a common candidate parent's **physical local observable algebra and
permitted local preparations**, then map the bounded scalar operations into it
and recompute the full response. At the same time derive and preserve its
actual homogeneous momentum constraints. Another positive-energy rewrite or
finite group average alone cannot meet both obligations. The boundary bundle
must independently be identified with that same parent's operator family;
adding the two presently separate models does not solve the TOE conjunction.
