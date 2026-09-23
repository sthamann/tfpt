# A lattice index is not automatically a quantum information increment

2026-09-12. Source-provenance supplement to PRIME_INFORMATION_REVIEW.md.
No new RH mechanism or proof promotion. The shared research index still
reports a missing registered source and paper/source review drift.

## Existing results recovered, not newly discovered

origin-composition-audit/README.md already constructs the conditional index
clock on submodules and proves that direct identification with quadratic
charge energy fails. compiler-cone-object-audit/ORDER_PROOF.md supplies the
actual algebra B=M2(Q(i)), its orders, and u1=diag(i,-i), u1*= -u1.
Its trace lattice norm is explicitly different from |det A|^2.
PROCESS_BOUNDARIES.md already distinguishes coherent sums, quantum
normalization, ancillary control and physical source access.

## A minimal exact discriminator using those actual generators

For integer n>=0 set A_n=I+n u1, an element already in the original order.
Here n u1 uses additive ring closure, not n sequential executions of u1.

    det_2 A_n=1+n^2,
    A_n* A_n=(1+n^2)I.

For any of the full rank-eight orders M under discussion, left
multiplication maps M injectively into itself. On M2(C), its complex
determinant is (det_2 A_n)^2 (one copy for each column). Its real determinant,
and hence ordinary integral index, is

    [M:A_n M]=|det_2 A_n|^4=(1+n^2)^4.

Thus n=6 yields determinant 37 and index 37^4=1874161. The determinant,
its Gaussian norm 37^2, and the rank-eight lattice index 37^4 are three
different numbers; do not interchange their logarithms.

But the normalized two-level operator

    W_n=A_n/sqrt(1+n^2)

is exactly unitary. It preserves all density-matrix eigenvalues and von
Neumann entropy. For a valid single Kraus branch K=A_n/c with
|c|^2>=1+n^2, its success probability is (1+n^2)/|c|^2 independent of
the input normalized state, and its conditional state is W_n rho W_n*.
An apparatus could record branch outcomes, but their probability and reset
cost depend on its specified implementation, not on the integer index alone.
This is a concrete counterexample to interpreting every log lattice index
as a state entropy increment. It does not say all arithmetic information is
erased: the phase angle atan(n) remains in W_n, and more general coherent
sums need not be proportional to unitaries.

## Why products alone and additive closure have different power

The actual quaternion units and family unit have determinant of modulus
one. Sequential products retain that modulus. More generally the root
determinants listed in ORDER_PROOF.md are 0 or Gaussian units: products of
those roots cannot produce a nonunit nonzero determinant such as 37.
Ring addition can, as A_6 demonstrates. Existence in the ring is therefore
not evidence of implementability by the closed sequential unitary source.

In fact the family 1+n^2 has unbounded prime support: if its prime divisors
were a finite set S, choose n=product_(p in S)p. Then 1+n^2>1 has no prime
divisor in S, a contradiction. This elementary argument is not a prime
generation algorithm with a complexity guarantee, nor does it realize all
prime types. An odd divisor p of n^2+1 must satisfy p=1 mod 4 (Fermat's
theorem excludes p=3 mod 4). Unbounded prime support is weaker than the
required all-prime arithmetic and trace weights.

## Verification and next boundary

The determinant, adjoint product and complex left-action determinant were
checked symbolically for arbitrary real n, with the n=6 index computed
exactly. The lattice-index and unbounded-support statements have the
explicit general proofs above; no full source suite or Lean rebuild ran.

Next inspect the source-derived operation that could retain both coherent
branch amplitudes and the integral correspondence. It must specify its
state, normalization, accessible record and clock, rather than declaring
log(index) to be physical time. Existing norm-37 coherent protocols in
PROCESS_BOUNDARIES.md are comparators with extra apparatus assumptions,
not a missing source derivation already discharged.
