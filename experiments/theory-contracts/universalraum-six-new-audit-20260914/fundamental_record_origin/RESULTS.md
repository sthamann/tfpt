# Fundamental record origin: a real simplification, with a narrower remaining gap

Date: 2026-09-14. Scope: original finite compiler, the added wedge carrier,
occupation records and measurement. No original source was edited; no paper,
ledger, native-physics or T1–T8 completion claim is made.

## Result

The external coherent occupation-copy gate **Q is unnecessary for the actual
bare-input preparation/echo/end experiment**. Given the already specified
addressable wedge Hamiltonian and fixed-Delta on/off control, its physical
22-dimensional carrier itself supplies the required coherent parity record.
The phase-correct transfer is the canonical wedge involution

    D = H - Delta N = g [[0,W†],[W,0]],
    A = P_kernel(D) + D/g = [[P_sym,W†],[W,0]].

Here WW†=I6 and W†W=P_antisym. Consequently A²=I22 exactly, and on a bare
matter input

    A N1 A = P_antisym,      A N0 A = P_sym.

The equations denote the restrictions of the complete Kraus operators to
bare matter. On all 22 dimensions the latter operator is
diag(P_sym,I6), not diag(P_sym,0); completeness was checked exactly.

This is a positive conditional mechanism, not a proof that foundational P1/P2
select the physical Hamiltonian, its controller or its readout. It removes a
genuine added coherent-control assumption. It does **not** remove the need for
a nondestructive, coherence-preserving occupation instrument.

## Provenance: where each resource first enters

All paths below are repository-relative. Hashes of the inspected source files
are saved in `origin_verification.json`.

| Source and lines | What is actually supplied |
|---|---|
| `tfpt_1_architecture_e8.tex:163-176` | Foundational P1: oriented seam, primitive reflection-positive kernel, unit winding and c3 normalization; not an executable controlled-gate list. |
| `tfpt_1_architecture_e8.tex:177-188` | Foundational P2: the g_car=5 interface, split into three color and two weak slots; distinction between interface input and algebraic consequences. |
| `verification/v783_two_qubit_clifford.py:8-27`, `:92-105` | Frozen mathematical finite-compiler hypothesis and explicit boundary against deriving physical realization. |
| `verification/v783_two_qubit_clifford.py:417-451`, `:493-535`, `:581-629` | Actual Construction-A roots, C4 chart, Pauli contexts and all sixty source root reflections normalizing the two-qubit Pauli group. |
| `experiments/theory-contracts/compiler-origin-audit-20260913/context_instrument.py:109-110`, `:144-166`, `:192-205` | Born/repeatability and the controlled-reflection isometry are premises; the physical coherent controller and record measurement basis are explicitly not derived. |
| `experiments/theory-contracts/compiler-single-execution-20260914/README.md:23-39`, `:43-65` | Four carriers, wedge dynamics, address/order, occupation copy and pointer initialization/readout are added resources. Q is explicitly specified as a block operator. |
| `experiments/theory-contracts/compiler-single-execution-20260914/check.py:88-119` | W and its transfer are constructed, covariance is checked, then Q is separately constructed at line108 and conjugated into R. |
| `experiments/theory-contracts/compiler-single-execution-20260914/check.py:129-145` | Central charge grading is not occupation phase; native/non-Clifford/resource boundary is explicit. |
| `experiments/theory-contracts/universalraum-native-closure-20260914/controls/verify_controls.py:104-118`, `:159-176` | Wedge/off drift, Z_occ and Q are separate definitions. The proposed finite Q Hamiltonian is pi/(2tau)(I-Q), hence it inserts a Q-equivalent conditional generator rather than deriving Q from wedge dynamics. |

The labels P0/P1/P2 inside `v783` are checker-section names, **not** the
foundational P1/P2 axioms. The independent probe executes the original source
prefix through its reflection/Clifford section, not merely the shorter prefix
that counts the sixty rays. It preserves all assertions as always-on checks.
It establishes the actual sixty reflections as Clifford; it does not infer a
physical controller from abstract group membership or a control Lie algebra.

## Physical synthesis and spectator boundary

At t/Delta=1/20, g/Delta=sqrt(2)/20, the independent probe reconstructs the
forward transfer schedule with twelve on pulses and eleven pi-duration
occupation parking intervals. Two additional unconditional parking intervals
correct the transfer phases: pre=3.3432741628219316 and
post=1.3342074236147385 in hbar/Delta units. The total A time is 25pi hbar/Delta.
The full physical 22D propagator differs numerically from the exact algebraic A
by about 4.4e-15 in operator norm. This residual is a numerical cross-check;
the involution and its Kraus identities are exact symbolic identities, not
norm theorems inferred from small residuals.

Six A calls implement the full nonaborted preparation/echo/end protocol, for
150pi hbar/Delta total controlled-Hamiltonian exposure, with no Q, helper bit
or separately addressable coherent pointer. This replaces four earlier
70pi R macros. The matter channel and classical flags match the previous
protocol; the construction does not supply its full arbitrary-pointer unitary
on 32 dimensions or all subsequent coherent accesses to two external fresh
pointers.

The correct edge record space is

    Sym²(C4) tensor |0>  direct-sum  Lambda²(C4) tensor C2_occupation,

of dimension 10+6*2=22. Ten symmetric/pointer-one states of a full 32D tensor
product are absent. Every preparation/readout pair returns the supported state
to bare matter before a different edge or arbitrary matter operation is used.

There is a compulsory spectator phase. Each physical bright two-level
generator has trace Delta, both on and off. Therefore

    det U_bright = exp(-i Delta T/hbar).

Since det X=-1, an exactly phase-correct A necessarily has odd-pi total drift
time. Every uncoupled, same-Delta mediator acquires -1, **not identity**. The
root's 544D three-edge star model explicitly includes -I192 on unaddressed
mediators. Its declared bare-input, return-to-bare use is consistent. This is
not an automatic invariant-space proof under arbitrary leakage, simultaneous
disjoint mediator occupation or noise across a larger matching space.

## Readout is now the decisive physical premise

An occupied result must preserve coherence between the six wedge colors.
Resolving mediator flavor and then forgetting that record has exactly the same
preparation herald probability 3/8 but only **1/6 conditional target fidelity**.
The reason is that occupied Omega is maximally entangled across the six
mediator/spectator wedge-color channels. Flavor dephasing destroys their
off-diagonal terms.

Color symmetry alone does not select a Lüders instrument. A completely
depolarizing map on the occupied six-dimensional sector is SU(4)-covariant,
preserves the occupied flag and yields only **1/36 conditional fidelity**.
These are exact finite-dimensional counterexamples, not merely insufficient
upper bounds. Symmetry and the correct outcome probabilities do not prevent
unseen environment leakage.

A useful sufficient contract can nevertheless be stated sharply. Assume:

1. The POVM effects are exactly N0 and N1.
2. Each outcome has exactly one Kraus operator (an efficient instrument).
3. The measurement is repeatable/nondestructive with respect to occupation.
4. The instrument is covariant under the full SU(4) color action.
5. In the four-site implementation it acts on the addressed 22D edge carrier
   and as the identity on the two spectator carriers.

On the irreducible occupied Lambda²(C4) sector, these assumptions force
K1=e^(i phi)N1. Indeed repeatability confines the isometry to that sector;
single-Kraus covariance implies covariance up to a one-dimensional character;
SU(4) has no nontrivial continuous characters; Schur's lemma makes the
isometry scalar. This is a conditional mathematical implication, not a source
derivation of these four assumptions.

They do not force a globally Lüders K0: its matter space is the inequivalent
Sym10 plus Anti6 representation, so K0 can have two different scalar phases.
The exact counterexample K0=diag(I10,-I6,0), K1=N1 has the right POVM,
repeatability and covariance but is not global Lüders measurement. For the
actual bare-input A protocol, however, the unoccupied state at readout lies
only in Sym10 and the occupied state lies only in Med6. The otherwise free
phases are global within each branch and disappear from the matter instrument.
Thus these stronger assumptions suffice operationally here. The Schur argument
is edge-local: the occupied sector with spectators has dimension96, not an
irreducible6. Global SU(4) covariance on that larger space alone does not imply
the fifth, locality assumption.

Full SU(4) covariance in this sufficient contract must not be silently replaced
by the original finite compiler group: its irreducibility and possible
one-dimensional twist intertwiners would require their own check. Efficiency
also forbids hidden which-color records; it is substantive additional physics,
not a consequence of observing one macroscopic outcome bit.

## What remains true about an external coherent Q

If one insists on a separate pointer and its complete coherent output, wedge
and occupation drift acting on the system alone cannot implement Q. Even
granting arbitrary system-only and pointer-only controls, product initial
resources and classical feedback leave the system/pointer output separable.
Q maps a system superposition of one symmetric bare state and one occupied
mediator, tensored with pointer zero, to a maximally entangled two-term state.
Its Bell projector has expectation one, while every separable state has
expectation at most one half. Hence the half-diamond distance of coherent Q
from this disconnected/LOCC resource class is at least **1/2**.

This obstruction is scoped: it forbids generating an external coherent Q from
disconnected controls, not recording parity in the system's own occupation.
Ordinary occupation readout supplies a classical flag, not freely accessible
coherent Q merely because a Stinespring dilation mathematically exists.

A concrete nonselection family is

    H_kappa = H_wedge tensor I + I tensor H_pointer
              + kappa N_occ tensor (I-X)/2.

Every kappa has the same color covariance and central charge grading. The
central iI4 acts as -I on both the two-matter and wedge sectors, so it is not
Z_occ and cannot select the conditional pointer coupling. kappa=0 gives the
factorization countermodel; a nonzero kappa, isolated during a parked pulse,
implements Q at duration pi hbar/kappa. Adding that term therefore supplies
exactly the functional missing control. It is not selected by the inspected
finite source identities.

The earlier 15/64 lower bound against stabilizer instruments remains correct
for the complete bare-input single-record preparation instrument. It is not a
P1/P2-wide impossibility theorem. In the new implementation the nonstabilizer
resource is carried by the wedge/occupation instrument bundle; no separate Q
needs to be charged to its operational resource list.

## Verification and independent root review

`replay_origin.py` runs this source-pinned probe in normal and optimized Python,
requires byte-identical outputs, and rejects two mutants: deriving Q from
disconnected controls and treating odd-pi spectator drift as identity.
`origin_verification.json` contains exact algebra separately from numerical
schedule checks.

The same runner independently replays
`../fundamental_record_execution/mediator_record.py` twice and checks its source
hash did not change. The full 22D/352D physical transfer, 544D spectator phase,
all 256 bare-basis end amplitudes and flavor-resolution counterexample were
also read directly. Its exact end effect is (3/8)P_Omega for arbitrary bare
input. The unconditioned retained/fresh successes remain 9/64 and 153/2048,
ratio 17/32 and difference 135/2048. No separately renormalized branch was used
to reconstruct these raw probabilities.

The result is therefore a material conditional simplification: the native
origin question has moved from an external coherent controlled occupation-copy
gate to the physical wedge/on-off realization and a sharply specified,
color-coherence-preserving occupation instrument. Those remaining premises
must be derived or measured before claiming foundational closure.
