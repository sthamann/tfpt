# Source audit: family symmetry is not yet physical time

Date: 2026-09-12. NON-RH. This is a bounded original-source audit, not a
complete search of every historical TFPT document. No status, paper, or website
promotion is authorized by this result.

## Outcome

The inspected source defines the family cycle as an algebraic automorphism.
It does not define it as the physical update of a state. The source also
contains a concrete interaction-matrix recipe, so saying "there is no
interaction in TFPT" would be wrong. What remains unselected is the physical
carrier identification, coupling, time scale, and update/composition rule.

An exact supplementary result closes a tempting shortcut: on the single
four-dimensional Clifford module, arbitrary compositions of the four source
generators and the family lift generate just 96 unitary matrices, or 48
operations modulo global phase. A **fixed word repeated as the update** has
physical channel period at most six. Thus adding these already available
operations to the isolated family three-cycle does not by itself produce a
new unbounded state-evolution mechanism on this site.

This does not forbid nonperiodic schedules, growing systems, interacting
tensor networks, continuum constructions, or extra continuous generators.
A nonperiodic schedule can have an infinite history even though the set of
possible cumulative single-site operations is finite. Neither such a schedule
nor intersite wiring follows from the finite closure calculation.

## Original-source chain

All paths below are relative to the repository; their exact hashes are
enforced by `checker.py`.

| Original location | What is actually present | Missing implication |
|---|---|---|
| `verification/v774_arf_spinor_compiler.py:432` | `sig_bits(v)=(v[2],v[0],v[1],v[3])`; the family bits cycle, anchor fixed. The module explicitly separates finite algebra from physical matter interpretation. | A coordinate automorphism is not yet a law saying states advance by that operation. |
| `experiments/theory-contracts/compiler-clifford-bridge/checker.py:103` | Explicit four skew-Hermitian Clifford generators; `algebra_certificate` at line 155 lifts sigma by permuting generators and proves algebra multiplication is preserved. | The lift represents the assigned symmetry; it does not assign an elapsed time or a source of physical updates. |
| `experiments/tfpt-discovery/seam_state_derivation_probe.py:601` | `put_ordered` **assigns** matrix entries. Lines 608–615 assemble a covariant antisymmetric interaction `A_int` by orbit representatives. | The order of array writes is not a sequence of physical pulses. |
| `experiments/tfpt-discovery/seam_state_derivation_probe.py:634` | `kms_A_gen(Am,u,t,beta)` uses `h=-(u*Adep_f+t*Am)` and a Fermi/Gibbs function of `beta*i*h`. | Here `t` is a coupling coordinate, **not elapsed time**. `u,t,beta` are inputs to a candidate state family. Identifying `exp(time*h)` as actual evolution would additionally require the physical dynamics and its units. |
| `verification/v252_full_finite_triple.py:102` | `full_D(Yu,Yd,Ye,Ynu,MR)` explicitly constructs a nontrivial finite Dirac matrix. Its tests use random Yukawas (209–210) and inserted mass values (315–316). | Existing finite spectral geometry is a legitimate conditional construction, not a derivation of those matrices from the family cycle. |
| `verification/v181_clock_is_conformal_symmetry.py:1` | An older mu4-clock argument explicitly leaves carrier-clock = seam-conformal-deck identification open. | The order-four deck action is not the order-three family action. Neither the shared word "clock" nor a finite group order identifies elapsed physical time. |

The seam source's introduction also explicitly asks whether its actual state
realizes the constructed candidate, and records that its prior normalization
gates failed to select the proposed point. That is corroborating source scope,
not a newly replayed numerical reflection-positivity experiment.

## Exact finite-gate theorem

Let `g_1,...,g_4` be the pinned 4-by-4 generator matrices, and

\[
w=\frac{I+g_1g_2+g_2g_3+g_3g_1}{2}.
\]

Then `w` is unitary, `w^3=-I`, and its adjoint action cycles the first
three generators and fixes the fourth. Let `U_v` denote their ordered words,
with `v` in `F_2^4`. The group is exactly

\[
G=\{\epsilon U_v w^k:\epsilon\in\{1,-1\},\ v\in\mathbb F_2^4,
\ k\in\{0,1,2\}\}.
\]

There are 96 distinct normal forms. The checker establishes:

1. Unitarity and closure under right multiplication by every original
   generator and `w`.
2. Independent reachability of every normal form from the identity.
3. Exactly 48 operations after quotienting by global scalar phases.
4. Exact orders of every element, not a numerical near-period census.

Matrix-order counts are `{1:1, 2:11, 3:8, 4:20, 6:40, 12:16}`.
Physical channel-order counts, counted over the 96 matrices, are
`{1:2, 2:30, 3:16, 6:48}`. The maxima twelve and six are attained.

No claim is made that a six-step system cannot be useful, or that this bounds
the physical complexity of TFPT as a whole. It precisely bounds this proposed
single-site fixed-word extension. Repetition of different, selected words
would need a schedule; the original `g_1` and `w` do not commute, so the
schedule cannot be discarded as an irrelevant convention.

The broader historical Clifford module `v783_two_qubit_clifford.py` was
inspected and pinned as context but not executed. Its advertised larger
finite Clifford group is **not** used as an independently verified result
here, nor does the 96-element theorem claim to enumerate all source operators.

## Earliest missing causal edge and acceptance gate

The first missing implication is

> **source automorphism / matrix wiring → actual state-update law on the same
> physically interpreted carrier.**

A completion should exhibit a source rule `U` or a source generator `H` and
derive, rather than assign after the fact:

- its action on the existing states and observable algebra;
- any carrier enlargement or intersite interaction;
- its composition/scheduling rule and physical clock calibration, or an
  explicit relational-clock construction with operational predictions;
- agreement with the reconstructed compiler operations and the actual seam
  source, preserving products and adjoints, not just dimensions or spectra.

The productive simple direction is therefore a **source-native composition
law between registers**, not another representation of the same isolated
finite cycle. It is a research direction, not an established existence result.
If a discrete rule suffices, a continuous interpolation need not be imposed;
but its empirical continuum behavior would still have to be derived and
compared rather than supplied through a chosen logarithm.

## Verification and ownership

`checker.py` passes 306 exact checks in normal and optimized (`-OO`) execution,
with matching reported results, and extracts only the reviewed
`generators` and `sig_bits` functions from pinned sources. It does not execute
the upstream suites, write source files, or repeat the reflection-positivity
scan. All guards are explicit exceptions and remain active under `python -OO`.
No T1–T8 problem is marked closed. Files in this new directory are the only
changes made by this worker.
