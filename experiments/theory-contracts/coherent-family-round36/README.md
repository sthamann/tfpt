# Round36: one reduced dynamics for a coherent preparation family

**NON-RH, unpromoted conditional theory contract.** Verdict:
`COMMON_HERMITIAN_DYNAMICS_WITH_UNIFORM_COHERENT_FAMILY_CERTIFICATE`.
No physical T1-T8 gate is closed.

## Result

One common **60-state Hermitian generator** now treats every normalized
superposition and every mixed state on the three-dimensional input space
spanned by the bare-filled physical cycle states k=-1,0,+1. It retains their
real and imaginary interference terms, not only three separate populations.

The certified input-operator error is <1.051e-18 for 0<=t<=1. At t=1 the
uniform observable error, including all excluded electric fluxes, is
<9.309e-14. The old k=0 result is included with unchanged interval endpoints.
The cutoff is now K13/528 physical components, preserving the previous
distance-to-boundary after allowing initial |k|=1.

All states use the same U(1) Gauss/background-charge sector, three fermions
and inherited parameters a=1/12, beta=1/4, eta=1/2, kappa=1/100, M=4, Vmag=0.
Every input has initial energy <=61/2400. This is a declared bounded-energy
preparation family, not the complete low-energy spectral subspace or a selected
physical vacuum. The geometry remains the three-site cycle, not a 3D lattice.

## A concrete interference check

The same compiled model gives these real Wilson intervals at t=1:

| Initial preparation | Certified interval |
|---|---|
| k=0 | [0.00000021720204, 0.00000021720223] |
| Equal superposition of k=0,1; relative phase 0 | [0.49994394265919, 0.49994394265938] |
| Equal superposition of k=0,1; relative phase pi | [-0.49994350829306, -0.49994350829286] |
| Equal superposition of k=0,1; relative phase +pi/2 | [0.00749991996345, 0.00749991996365] |
| Equal incoherent mixture of k=0 and k=1 | [0.00000021718307, 0.00000021718326] |

The large coherent-plus value is **not** a newly generated vacuum signal:
that preparation already has Wilson expectation 1/2 initially. The check
demonstrates that the reduced description preserves the distinction between
coherence and classical mixing. Dropping off-diagonal response entries would
destroy it.

## How the family guarantee works

A shared block Krylov space is proposed from the three inputs and their
successive images under the original Hamiltonian. It is not a direct sum of
three separately fitted one-state models. An exact rational Gram check and
an exact residual check validate the proposed basis and common generator.
The basis proposal uses 80-digit Decimal arithmetic; that numerical precision
is **not** treated as a certificate by itself.

The residual's integrated response is bounded for each input column, and a
Cauchy-Schwarz bound controls their combined operator on all complex inputs.
This establishes uniformity analytically, rather than testing finitely many
states and assuming the rest. The four physical sources are compressed with
the same embedding. At any time the calculation returns four complex Hermitian
3x3 response matrices M_O(t); any density gives Tr(rho M_O(t)). Additional
densities then require only these small traces, without rebuilding or evolving
the model again.

Block Krylov methods and residual certification are established methods;
see [Frommer, Lund and Szyld](https://epubs.siam.org/doi/10.1137/19M1255847).
The parent-specific proof, full-rotor support margin, roundoff accounting and
limitations are in [COHERENT_FAMILY.md](COHERENT_FAMILY.md).

## Run and independently verify

Standalone execution needs only the standard library and the compiled model:

```bash
python3 experiments/theory-contracts/coherent-family-round36/checker.py --model experiments/theory-contracts/coherent-family-round36/compiled_model.json --state coherent_plus
python3 experiments/theory-contracts/coherent-family-round36/checker.py --model experiments/theory-contracts/coherent-family-round36/compiled_model.json --state phase_plus --time 1/2
```

`--density path.json` accepts a general rational density matrix as an object
with `real` and `imag` 3x3 matrices. Entries may be rational strings, for example
`"1/2"`. Hermiticity, trace one and all principal minors are checked exactly.
The order is k=-1,0,+1. The certified time domain is [0,1].

Rebuild against the pinned parent and run the regression suites:

```bash
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/coherent-family-round36/checker.py --output experiments/theory-contracts/coherent-family-round36/validation.json --write-model experiments/theory-contracts/coherent-family-round36/compiled_model.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/coherent-family-round36 -p test_checker.py
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/coherent-family-round36 -p test_checker.py
```

Validation includes the 36/48/60-state scan, the four full complex response
matrices as certified intervals, and nine example densities. The examples
illustrate the operator theorem; they are not its proof. Tests check the entire
528x3 evolution matrix against the independent full solver, complex phase
superpositions, mixtures, source responses, support margins, Gram/density/pin
mutants, replay and standalone execution without a parent-repository path.

The standalone calculator uses certified budgets from the artifact. An
arbitrarily edited artifact is not certified merely because it can be parsed;
the pinned-parent build and SHA256 replay verify its provenance and budgets.

## Cost and remaining boundary

The compiled model is 949,010 bytes and contains 478 Hamiltonian integers,
14,400 source integers, denominators and the family/error contract. It contains
no 528-state basis, full states, parent matrix, benchmark responses or memory
history. Offline compilation still uses 31,680 basis integers and the full
parent, products and orthogonalization. Online, three input columns are evolved
through the common 60-state generator to obtain all response matrices. Large
integer arithmetic and source contractions remain explicit costs; no overall
runtime speedup or minimal dimension is claimed.

The new result is **uniform over this whole input subspace**, not uniform over
volume or all low-energy states. Global cycle-flux preparations are not spatially
local preparations; adjacency of block layers is not physical locality. High
states remain in the auxiliary description. A local 3D family with uniform
errors/costs, or a genuine dressed low-energy spectral reduction, is still the
next theoretical bridge. Parameter/vacuum selection, chirality, continuum
gravity and the full T1-T8 conjunction remain open.

Following the experiment workflow, this work does not alter papers, website,
verification, ledger or empirical scorecard and makes no TOE or RH claim.
