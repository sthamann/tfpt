# A sum in a formula need not require extra physical branches

2026-09-12. NON-RH finite quantum-dynamics clarification. No full theory claim.

## Correction to the proposed next priority

INDEX_VERSUS_QUANTUM_OPERATION.md correctly separates ring addition from
sequential multiplication and shows that A_n=I+n u becomes unitary after
normalization. But this particular normalized sum does NOT intrinsically
need a linear-combination-of-unitaries ancilla or a postselection protocol.
For u*=-u and u^2=-I,

    exp(theta u)=cos(theta)I+sin(theta)u,
    (I+n u)/sqrt(1+n^2)=exp(arctan(n) u), n real.

The first identity follows by grouping even and odd terms of the convergent
matrix exponential. The second follows from elementary trigonometry.
The Hermitian generator is H=i u, since exp(-i theta H)=exp(theta u).
Thus ONE available continuous generator would suffice. Availability of the
single discrete operation u does not by itself provide arbitrary times of
that flow: powers of u form only a four-element group. Nor does the integer
n choose the physical time without an external rule. This is standard
Pauli-rotation mathematics, not a new TFPT dynamics theorem.
Reference: https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.PauliEvolutionGate

The special collapse does not apply automatically to the older seven-word
filter T/7 in compiler-cone-object-audit/PROCESS_BOUNDARIES.md. That source
gives a conditional instrument, not the same unitary family W_n.

## Actual source: global phase versus observable relative motion

The inspected construction seam_state_derivation_probe.py:586-627 uses
J=I8 tensor [[0,1],[-1,0]], B=A_int and D=alpha J+g B. The exact source
audits clock-marking-audit/README.md and clock-bilinear-response/checker.py
establish [J,B]=0 and the CAR lift Hhat_J=Ntotal-4. Hence

    exp(s D)=exp(s alpha J) exp(s g B).

This is a coordinate flow identity, not a choice of physical time units.
On the eight complex one-body modes, the J factor is a common phase.
On number-neutral observables Q, [Ntotal,Q]=0, so the corresponding Fock
flow leaves Q unchanged. It cannot create their nonzero relative frequencies.

The known active corner has energies

    alpha-g, alpha+sqrt(3)g, alpha-sqrt(3)g.

Its relative frequencies depend on g, not alpha. In a two-mode restriction,
subtracting the mean gives a Pauli-type diagonal generator, so a rotation
is available algebraically there. However the corner identity is a projector,
not the full-space identity, and actual preparation/access are not supplied
by merely restricting the matrix. Existing source audits find the slow
number-neutral channels dark in the vacuum at alpha=1,g=1/8, and inaccessible
to the stated boundary-generated algebra.

These are separate statements: a global common phase is not measurable by
number-neutral observables; relative phase evolution exists in other modes;
the specified source preparation and access do not yet yield its response.
No impossibility for all preparations, all observables or enlarged models.

## Verification and revised next gate

The normalized-sum/rotation identity and unitarity were checked symbolically
for arbitrary real n. Actual source construction and existing exact audit
definitions were inspected, not rerun as a full source or Fock suite.

The next gate is a SOURCE-ALLOWED preparation and observable coupling for
the already present relative-motion sector. First establish whether these
exist before adding ancillas, new interactions, or a new Hamiltonian. The
state, preparation cost, charge/Clock action and observable response must
belong to that same source. No additional arithmetic claim is made here.
