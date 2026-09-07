# Non-RH TOE research: Round12, physical observables and quantum domains

Date: 2026-09-06. HEAD and actual remote main were rechecked at
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`.
This is locally integrated, unpromoted research, not a release, commit or push.
Prior Round9–11 artifacts and concurrent paper/ledger/v472 edits are preserved.
No RH result or empirical confirmation is claimed.

## New results

| Contract | Established result | Precise remaining boundary |
| --- | --- | --- |
| [Relational observables](relational-observables-round12/README.md) | An explicit finite regular reference system makes the full original observable algebra available on the joint invariant physical space, with exact states, domains and dynamics. | It transports the original remote response as well. An additive finite reference Hamiltonian cannot cancel it for all states. This is not a no-go for dynamical local reference fields or a uniformly energy-restricted theory. |
| [Canonical tensor shear](canonical-shear-round12/PROOF.md) | The square-completing change of variables is a global canonical map and an exact unitary operator, including the full transformed kinetic term and bounded Weyl observables. | It is not a free theory. An isospectral free alternative changes the prescribed first-order vertex. Simultaneously transporting dynamics and observables preserves the original responses. |
| [Momentum deformation](momentum-deformation-round12/PROOF.md) | The first-order centered total momentum can be repaired. A nonzero second-order resonance, including both static and tensor-exchange terms, excludes every smooth strongly conserved deformation with that seed for all finite nonnegative masses and lattice sides divisible by six. | This is not a proof against every weak, constraint-proportional closure on a deformed constraint surface, another seed, singular coupling dependence, or a different microscopic Hamiltonian. |
| [Unreduced quantum domain](unreduced-domain-round12/README.md) | The actual seed Weyl operator admits a jointly measurable choice of self-adjoint extensions preserving time reversal, and its dressed operator is defined by unitary conjugation. The free limit is strong-resolvent continuous. | Essential self-adjointness, physical selection, the full total-Hamiltonian domain and strong propagation of the mixed constraints remain open. Every extension of the unchanged full expression is unbounded below. |

These are complete proofs of the named restricted statements, accompanied by
finite exact algebraic checks. The checks do not prove the infinite-dimensional
domain and smooth-function theorems by themselves.

## What the results resolve

### An invariant sector alone was not a local observable construction

Compression to a finite-translation invariant sector is not an algebra
homomorphism. A three-spin exact witness starts with two commuting observables
and obtains a nonzero commutator after compression. For the actual finite group,
the ideal regular reference provides the isometry

    V psi = |Gamma|^(-1/2) sum_a |a> tensor U_a psi.

Its image is the joint invariant space. Relational observables intertwine with
the original operators exactly, so the physical space is isomorphic to the
full original system, not merely its old invariant sector. The original scalar
net is now genuinely represented, but so is its nonlocal interaction response.
The required ideal reference has |Gamma| mutually orthogonal states.

For any additive finite reference Hamiltonian, the induced physical correction
is a bounded group-algebra operator B. Its nested commutator with two bounded
Weyl shifts has norm at most 4||B||. The actual quartic source response along
translated packets grows quadratically, with the previously verified nonzero
remote Hessian. Hence this finite correction cannot cancel the response for
all states. Each packet has finite energy, but those energies are not bounded
uniformly; no fixed-low-energy-only impossibility is claimed.

### Completing a potential square does not eliminate the interaction

The shift q=Q+gF(phi) necessarily shifts the scalar momenta as well. The
transformed Hamiltonian contains both order-g momentum coupling and an
order-g-squared kinetic square. The exact transformed Weyl operators include
a field-dependent tensor translation. Their dynamics is unitarily equivalent
to the original response. Removing those terms instead defines a different
model, already different at the first prescribed coupling vertex.

### A genuine second-order obstruction, not merely a failed ansatz

The momentum theorem retains the actual scalar source, TT projector, Fourier
normalization and real Nyquist oscillator. At side length six and m^2=4/7,
the resonant quartic coefficient is

    C_static = 7/36864,
    C_exchange = -77/1198080,
    C_total = 301/2396160.

Its forcing has nonzero average 301 sqrt(3)/599040 on a closed free orbit.
The derivative of any smooth single-valued correction has zero such average.
After eliminating the nonresonant cubic Hamiltonian, arbitrary freedom in
the first momentum correction cannot alter this second-order equation.

For all finite mu=m^2>=0 the same coefficient is

    C(mu,n) = 9(2mu+5) / [64n(4mu+7)sqrt((mu+2)(mu+4))] > 0.

A two-angle torus average proves the obstruction without a rational-frequency
or ergodicity assumption. On side lengths divisible by six only n=L^3 changes.
This closes the question of a smooth, strongly conserved deformation of the
specified seed through this order. It does not close the separate problem of
weak first-class closure, which must allow for the deformed constraint surface
and constraint-proportional terms.

### Existence is now separated from physical domain selection

The unreduced expression has a real symmetric polynomial differential core.
Time reversal pairs its deficiency spaces. Paired countable Gram–Schmidt and
Cayley transforms select extensions measurably in coupling and auxiliary
coordinates; their direct integral agrees with the full specified expression
on the joint Schwartz test domain. At zero coupling the operator has a unique
free closure, and the selected extensions approach it in strong resolvent
sense. Neither statement selects the interacting physical boundary condition.

The actual auxiliary Hessian also has a negative direction. Translated
normalized packets have energy -4t^2+O(t) for the checked nonzero mode.
Every extension agreeing with the expression shares these expectations.
Reduced positivity is compatible with this, but cannot be imported into the
unchanged unreduced model. The cubic interaction is also not relatively
bounded by the specified quadratic comparison operator, so the simplest
Kato–Rellich shortcut is unavailable.

The audit explicitly separates unitary quantum dressing from Weyl quantization
of the classically dressed symbol. Two independent contractions give a
second-order ordering difference -3/128 for one actual-source mode witness.
This is not the full all-mode constant, a vacuum-energy prediction, or an
empirical TFPT observable.

## T1–T8 after this round

No complete T-gate is closed or promoted.

- T1: dimension, scale, markings and microscopic geometry selection remain open.
- T2: the previous boundary representation still needs identification with the
  TFPT seam and the same dynamical parent; this round does not supply it.
- T3: finite domain existence is advanced, but the full local nonlinear parent,
  homogeneous constraint system and strongly preserved physical domain remain open.
- T4: the actual chiral operator, interacting mirror decoupling and fermion
  measure remain open; no such spectrum is obtained from the reference system.
- T5: the physical scalar net is explicitly reconstructed, not made local.
  A shared controlled continuum/Lorentz limit remains to be constructed.
- T6: no family masses or common normalized analytic determinant family are
  derived; the prior geometric and dynamical models remain distinct.
- T7: an unreduced self-adjoint extension exists, but strong mixed-constraint
  propagation and physical extension selection are not established. The
  strong momentum-deformation obstruction is not a blanket constraint no-go.
- T8: conditional states, relational readouts and unitary dynamics are precise;
  a microscopic initial-state selection and common physical SK construction
  remain open.

## Reproduction, independent checks and provenance

Run `experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/run_round12.py`
from the repository root. The bounded runner emits the five new checker runs
and six unchanged prerequisite runs separately, including full output, source
and proof hashes, runtime versions, base revision and exit codes. Saved records
are in `ROUND12_VALIDATION.json` and the four folders' `validation.json` files.
`--check-manifests` is a hash/inventory/record consistency check, not a test
rerun or mathematical certification.

The separate `test_round12_runner.py` uses temporary generated fixtures, not
real repository manifests. Its 20 infrastructure regressions cover empty and
duplicate input records, changed hashes, stale aggregate records, missing or
failed prerequisites, false successful statuses, malformed records and inherited
Python optimization settings. `ROUND12_RUNNER_VALIDATION.json` retains normal
and optimized-parent executions separately from the mathematical checks.
The runner forces assertions on in every mathematical child process. These
hardening changes followed reproduction with the systematic-debugging skill;
they do not change the mathematical conclusions.

The main review read all proofs and checker sources. Independent reviews
examined the finite reference construction and its norm bound, the canonical
shear, the all-mass momentum obstruction, and the measurable extension proof.
The separately implemented momentum checker imports the original Ward source,
reconstructs TT projectors from nullspaces, and recalculates contact and exchange
coefficients. The domain checker separately contracts the ordering correction
in two ways. No finite CCR truncations or floating tolerances are used by the
new checks. Algebraic assertion groups are not added into a count of physical
facts or full theorems.

## Next decisive work

1. Analyze weak closure of the actual deformed homogeneous constraints,
   including their common zero set, instead of identifying it with strong
   conserved-quantity deformation.
2. Construct a self-adjoint realization with domains compatible with the
   linear constraint transport and auxiliary stabilization, not just arbitrary
   measurable extension existence.
3. Supply a common microscopic parent with an explicitly derived physical
   local algebra. A new reference field or changed interaction must declare
   which vertices and observables it changes and meet the same tests.

The finite CY boundary data must still be identified with that same parent.
Combining separate successful partial models does not establish their common
physical realization or the TOE conjunction.
