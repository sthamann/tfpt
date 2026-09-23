# One object, different actions: charge carry cannot be a finite clock reset

12 September 2026. NON-RH. This bridges two investigated fronts without
identifying their physical carriers. It supplements, not replaces, the older
half-twist-grade-carry and source-half-sector-bridge results.

## 1. Retain the actual charged-sector dictionary

The [source-half-sector calculation](../source-half-sector-bridge/README.md)
uses the actual two QWZ backgrounds and a declared common-reference limiting
direct sum. On its neutral charge-vacuum basis write

    n = 2 q_top + b,  b=0,1,  q_bottom=-q_top,
    p_top = n/2 =: Q,  p_bottom=-Q,
    H |n> = n(n-1)/4 |n>,  S |n> = |n+1>.

This is a limiting-sector construction. The microscopic intersector field,
physical direct-sum selection and marked source identification remain open.
The formula does not claim the finite-QWZ total charge is half-integral;
the two edge shifts compensate, and their sum is zero.

On finite-support sequences (a common invariant dense domain),

    [Q,S] = S/2,       [H,S] = S Q.

The second identity follows from h(n+1)-h(n)=n/2 for all integers n.
H is nonnegative, with ground charges n=0 and n=1. The inverse shift is
the adjoint, not a wrap-around at a finite charge cutoff.

## 2. A precise joint obstruction

The compiler family lift w obeys w^3=-I. Any hypothetical identification
of the SAME invertible operator U with this central finite-order action
and with persistent half-charge carry would require

    U^3 = phase * I,       [Q,U] = U/2.

Leibniz on a common invariant domain gives [Q,U^3]=(3/2)U^3, while the
first equation gives zero. They are incompatible. More generally an
invertible finite-order operator cannot shift a nonzero additive charge
on every application. This excludes that identification, not a common
larger algebra containing distinct clock, charge and time operations.

There is also no finite-dimensional unitary representation of
U* Q U=Q+I/2: taking the trace yields 0=dim/2. A finite cutoff may still
approximate charge fields on protected windows, but must record a boundary
defect rather than assert the exact global relation. Noninvertible charged
operators and nonperiodic infinite representations are outside this no-go.

The checker includes intentional cyclic replacements of dimensions 4,6,16.
For Q_j=j/2 and C|j>=|j+1 mod m>, the charge Ward defect is exactly

    [Q,C] - C/2 = -(m/2)|0><m-1|.

These replacements fail even though every non-wrapping transition looks right.

## 3. The simplest consistent extension, and what it does not achieve

Conditionally adjoin the compiler spinor to the limiting charge sequence:

    K = ell^2(Z) tensor C^4,
    U(|n> tensor psi) = |n+1> tensor w psi.

Then U is unitary, [Q,U]=U/2, and U^3=-S^3 tensor I, not a scalar reset.
It consistently retains the charge carry and a finite family tag. This is
an explicitly ADDED tensor-product representation, not a source-derived
physical joint space, E8 field or 3+1D parent.

Moreover [H,U]=UQ for the sourced charge energy H. Therefore U is not
exp(-itH) for any fixed t on the whole space: autonomous evolution generated
by H must commute with H. A charge-changing field, a symmetry and a time
propagator are different operations even when they live in one algebra.
Externally driven, relational or larger-system energy-conserving processes
are not excluded by this observation, but have not been supplied here.

The product does not create an interaction. Define the block-diagonal
unitary D on K by D_n=w^(-n). Then

    D U D* = S tensor I,       D Q D*=Q,       D H D*=H.

This is an exact simplification of this product dressing. It is NOT license
to discard the compiler marking: a marked generator I tensor g_i transforms
to the charge-dependent block w^(-n) g_i w^n. Physical equivalence requires
transporting preparation, accessible operations and measurements too.

For general unitary link factors V_n on an open integer chain, choose
D_(n+1)=D_n V_n*. The same blockwise calculation removes the link factors
from a decorated shift. Loops, additional Hamiltonians and fixed operational
markings can carry further data; none is fixed by writing down the decorated
shift itself. This is a representation identity, not a universal gauge
triviality claim about field theories.

## 4. How this changes the joint research question

Seeking one common algebra is consistent. Seeking one finite operation
that simultaneously IS a clock cycle, additive charge field and autonomous
time propagation is inconsistent with these sourced relations.

The joint acceptance test must instead exhibit the maps between distinct
operations on the SAME selected parent: the charged intersector field,
the internal family automorphism, the Hamiltonian and the physical state.
Their Ward identities and adjoints must agree under those maps. A tensor
product of individually successful models does not establish this.

Written domain and all-integer arguments above provide the general scope;
the checker pins both original sources, verifies extracted source carry
branches and symbolic energies, and catches finite cyclic mutants. It does
not rerun the microscopic QWZ continuum estimates. No T1-T8 marker changes.
