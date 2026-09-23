# Compiler restart: boundary sufficiency versus genuine quantum encoding

2026-09-12. NON-RH; documentation and a bounded exact checker. No physical
code, source measure, continuum, or T1–T8 completion is claimed.

## Provenance

`holographic_basics.py` calls the existing `boundary_access.source_matrices()`.
It checks the original source hash
`5e54c416be72a125a8ce6e235b4300f9f9c2344b3ada796d2dc4c7e2ea01482b`
and reconstructs the finite matrices using the already deployed permutation.
This does not rederive that permutation or the complete upstream compiler.
The reconstructed accessible/hidden Fock dimensions are 32 and 8. The
all-protocol argument is in [BOUNDARY_PROTOCOL_LIMIT.md](BOUNDARY_PROTOCOL_LIMIT.md).

## Exact recovery contract

For an isometry V:L→A⊗B, define N(ρ)=Tr_B(VρV†). Full quantum recovery
means a CPTP map R with R∘N=id on every logical density matrix, hence also
on matrix units and entangled extensions. In finite dimensions, erasure of B
is exactly correctable iff

    V†(I_A ⊗ |i><j|_B)V = c_ij I_L   for every i,j.

This is the standard Knill–Laflamme erasure criterion, not a new theorem:
[Knill–Laflamme](https://arxiv.org/abs/quant-ph/9604034).
Boundary reconstruction as quantum error correction is motivated by
[Almheiri–Dong–Harlow](https://arxiv.org/abs/1411.7041).
Neither external paper identifies TFPT's physical code or selects a state.

## A conditional simplification: full access forces a product code

Assume a nonzero finite-dimensional code subspace C⊂A⊗B is invariant under
every U_A⊗I_B, U_A unitary, and its ENTIRE state can be recovered from A.
Invariance under U and U† implies [P_C,U⊗I]=0. The commutant of the full
matrix algebra on A is I_A⊗End(B), so P_C=I_A⊗p for a projector p on B.
Thus C=A⊗K where K=im p.

If dim K≥2, take two orthogonal unit vectors b_0,b_1 in K and any a in A.
The orthogonal states |a,b_0> and |a,b_1> have the same A marginal.
Recovery of both by one channel is impossible. Hence dim K=1. Conversely,
when K=span b, appending the fixed state |b><b| is a recovery channel.

This proves: under this unrestricted-access, invariant-subspace contract,
all correctable nonzero codes have form A⊗span b. This is a standard
commutant argument specialized to the present research question, not a
new general QEC result or a statement against holography.

For the source split, retaining this generous M32 access leaves a chosen
hidden vector, not arbitrary hidden information. To keep this product
subspace invariant under H_A⊗I+I⊗H_B, b must also be an eigenvector of H_B.
This follows by projecting H(a⊗b) onto A⊗b-perp. It neither selects that
eigenvector uniquely nor derives a ground-state postulate. Clock and other
primitive operations require their own invariance checks.

Full access in the earlier no-signalling proof was an upper bound: failure
even with that access implies failure for smaller access. It was NOT a
derivation that TFPT physically implements all those operations. The code
classification here therefore cannot be imposed as an unconditional TFPT
restriction. If the allowed operations are smaller, or only a logical
subalgebra must be reconstructed, a nonproduct code is not excluded.

## Exact positive and negative controls

On two qubits with the second erased:

- Product code V|0>=|00>, V|1>=|10> satisfies every erasure matrix-unit
  condition; partial trace restores every logical matrix unit.
- Repetition code V|0>=|00>, V|1>=|11> preserves the two classical labels
  but fails full quantum recovery. Encoded |+> and |-> are orthogonal Bell
  states with identical first-qubit marginal I/2. The code also fails
  invariance under X⊗I.
- The full first-qubit algebra has a four-dimensional commutant on the
  two-qubit space, checked by exact linear equations.

These are standard toy controls, not embeddings derived from the compiler.
The general source limitation is established by the block split and the
written argument, not by pretending that a two-qubit example is TFPT.

## Reproduction

From this directory, run `/opt/homebrew/bin/python3 holographic_basics.py`
and `/opt/homebrew/bin/python3 -OO holographic_basics.py`. The checker uses
explicit exceptions rather than Python assertions. No original source is
changed and no new event process or gauge restriction is installed.

Executed on 2026-09-12: 22 exact checks passed in each mode, with byte-identical
JSON outputs. This includes the source-pin/split checks and the explicitly
separate toy controls. The general code classification is the written
finite-dimensional argument above; the count is not a proof of a physical code.

## Next acceptance gate

Find a source-derived nontrivial physical state space together with its
allowed operations. Test erasure recovery, adjoints/Clock and preservation
under these operations and the same source dynamics. Do not manufacture a
code just because it passes recovery; do not interpret a one-state code as
recovering independent physical degrees of freedom. Only then investigate
compatible reconstructions on multiple boundary regions or a refinement limit.
