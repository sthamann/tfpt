# Complete hidden-sector Clock classification, including higher-degree operators

2026-09-12. NON-RH. This is a finite source theorem, not a physical observable
selection or source-native measurement protocol.

The source's active three one-body modes have energies
(alpha-g, alpha+sqrt(3)g, alpha-sqrt(3)g) and Clock eigenvalues
(-1,eta,eta_bar), eta=exp(-2pi i/3). The checker reconstructs the pinned
source matrices and verifies these actual eigenvectors before using them.
Use their number-conserving second-quantized Clock with vacuum eigenvalue 1;
an overall Clock phase does not affect the conjugation-invariant algebra.

## Exhaustive eight-state result

Occupation bits (n0,n+,n-) have Clock grade

    q=3 n0+4 n++2 n- mod 6.

In binary enumeration n0+2n++4n-, grades are (0,3,4,1,2,5,0,3).
The complete invariant algebra consists of matrix units |r><c| with equal
grades. Its complex dimension is 12 and its structure is

    M2(C) direct_sum M2(C) direct_sum C^4.

This enumerates ALL operators of the hidden eight-state factor, not merely
quadratics. Every one is parity even and preserves n0. Indeed the cube of
the Clock is (-1)^n0; for a single binary mode its parity determines n0.
The two doublets are |000>,|011> and |100>,|111> (occupation-tuple notation).
Only creation/annihilation of the +,- pair can give nonzero off-diagonal
matrix entries. Their energy difference is

    (alpha+sqrt(3)g)+(alpha-sqrt(3)g)=2alpha.

Consequently the full invariant hidden algebra has only adjoint frequencies
0,+2alpha,-2alpha. None carries the slow g-dependent differences. At the
previous source point alpha=1,g=1/8 the nonzero magnitude is 2.
This is NOT a statement about every invariant observable involving boundary
modes or an external reference, nor about the dependence of chosen Gibbs
weights on g. It concerns autonomous hidden-operator frequencies.

## A positive invariant pair channel

T=c_+* c_-* satisfies [H,T]=2alpha T, is Clock invariant and parity even,
and T|vac> has norm one. X=T+T* is a Hermitian invariant observable with
nonzero vacuum two-point function <vac|X(s)X(0)|vac>=exp(-2i alpha s).
Thus Clock invariance does not imply absence of all hidden vacuum dynamics.
But this is a pair-frequency channel, not the earlier slow transfer, and
it changes total particle number by two. Its measurement/access and charge
or energy exchange are not derived from the boundary-only contract.

If one ALSO requires number conservation within this hidden factor, the
invariant algebra reduces to the diagonal C^8. All its operators commute
with H. In particular no higher-degree hidden neutral invariant operator
can rescue the slow dynamics: the entire eight-state algebra was classified.

## Interpretation and next gate

The minimal question is now the status of the Clock: physical symmetry with
covariant observable multiplets, or a redundancy demanding invariant
observables. If the latter is established, slow charged operators need a
source-derived compensating reference/sector. A clock-fixed boundary factor
alone cannot cancel their nontrivial grade. Invariant pair dynamics is a
separate valid possibility, not permission to rename its frequency.

Standard finite CAR/Gaussian background: Surace--Tagliacozzo,
https://arxiv.org/abs/2111.08343 . The concrete centralizer enumeration and
source eigenvector comparisons are exact calculations here, not claims
inferred from the external reference.

## Verification

clock_invariant_hidden.py passes 19 exact checks in normal and -OO modes
with identical output. The eight-state hidden Fock factor is complete;
this is not a new full 256-state computation. No free Hamiltonian or
original source was modified, and no physical access was assumed derived.

A local checker error was diagnosed with systematic-debugging: SymPy matrix
callbacks supply SymPy Integer indices, whose Zero object lacks Python's
bit_count method. A minimal reproduction confirmed the type boundary;
converting the index to int before the bit count repaired the checker.
No mathematical requirement was weakened. The error occurred after the
source eigenvector and complete grade/frequency checks had already passed.

No T1--T8/TOE/RH closure, native pair preparation or arbitrary control claim.
