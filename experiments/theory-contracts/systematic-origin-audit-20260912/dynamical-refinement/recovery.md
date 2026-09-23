# Deterministic logical recovery is possible, but it is not ground filtering

12 September 2026. NON-RH. Exact finite subsystem construction.
Companion: `recovery.py`. Original branch overlaps: `../refinement/ternary.md`.

## Outcome

The three different bare trees can preserve exactly the same unknown logical
quantum state under a deterministic channel. The channel must retain the
tree information in an environment; it does not identify all three physical
states by one closed-system unitary, and it is not the literal ground-projector
filter. At d=4 an environment of dimension three is sufficient and minimal
for the specified pure-target recovery of all three branches.

The environment flags are NONORTHOGONAL, with overlap 17/20. They are not
three perfectly distinguishable classical branch labels.

## 1. General ground projection: exact success conditions

Let A be an isometry from the logical space into a physical space and P0
an orthogonal ground projector of a fixed physical Hamiltonian H. Define

    K_A=P0 A,          S_A=K_A* K_A=A* P0 A,          0 <= S_A <= I.

For logical density matrix rho the success probability of actually measuring
the ground projection is tr(rho S_A). If S_A=p_A I with 0<p_A<=1, the
normalized map B_A=P0 A/sqrt(p_A) is an isometry and preserves the unknown
logical state CONDITIONAL ON SUCCESS, whose probability is p_A.
Calling B_A an isometry does not change p_A to one.

If S_A is non-scalar, normalized projection generally filters different
logical directions differently. If S_A is positive definite one can define
the polar isometry P0 A S_A^(-1/2), but that correction is an additional
operator, not the action of P0 or an automatic deterministic realization.

If P0 contains one copy of the same irreducible fundamental representation
and A intertwines that representation, Schur's lemma supplies S_A=p_A I.
The nonzero normalized projected branch encodings then agree up to phase.
The single-copy and full-ground assumptions must actually be proved; the
lowest state in a restricted diagram span is not automatically the full
1024-dimensional ground state.

The separate `filter.py` gives FLOATING-POINT whole-H5 diagnostics: ground
energy approximately 1.574609470321, multiplicity four, and success
probabilities approximately 0.887717840848 for L/R and 0.603631068546 for M.
These are reported diagnostic values, not certified spectral inequalities;
`recovery.py` neither uses them nor reruns that diagonalization.

## 2. Why a deterministic channel is nevertheless possible

The exact original relation is A_alpha* A_beta=C_alpha,beta I4, where
alpha,beta run over L,M,R and

    C=(1-q)I3+q 11^T,             q=17/20.

C has eigenvalues 27/10,3/20,3/20 and rank three. Choose unit environment
vectors phi_alpha whose Gram is C. The checker constructs them by exact
Cholesky factorization C=L L*, with phi_alpha the columns of L*.

Let J=[L M R] denote the joined PHYSICAL branch map (here L is a branch,
not the Cholesky factor). Since J*J=C tensor I4, its range is isometrically
equivalent to C3_tree tensor C4_logical. More explicitly, writing T for the
invertible matrix whose columns are the flags, J*J=T* T tensor I4, and

    F=J (T^(-1) tensor I4),        F*F=I12,
    A_alpha psi=F(phi_alpha tensor psi).

Thus for ANY selected target isometry B there is an isometry on this source
span satisfying

    V A_alpha psi = B psi tensor phi_alpha.

It preserves all cross-branch inner products, not just separate branch norms.
Tracing the environment yields a deterministic completely positive
trace-preserving logical recovery on that span:

    R(A_alpha rho A_alpha*) = B rho B*.

External-reference entanglement is preserved. For coherent tree superpositions
with a common logical input the tree amplitude moves into the environment.
This does not identify arbitrary differently correlated logical/tree inputs
with a pure logical state; the general operation is partial trace of the
multiplicity factor, followed by B.

For fixed pure logical psi, any isometric dilation producing the same pure
target B psi on all branches must reproduce C as its environment Gram.
Therefore dim(environment)>=rank(C)=3. This is a lower bound for the stated
pure-target dilation, not a universal lower bound for every mixed-apparatus
protocol or restricted set of input states.

## 3. Why this is not a closed-system Hamiltonian-preserving refinement

A single physical unitary cannot send both L and M to the same B, even up
to phases: it would change L*M=qI into a unitary scalar of modulus one.
The environment in section2 is exactly where those distinguishable physical
degrees of freedom remain.

For ONE specified branch, an abstract unitary extending A->B exists because
both are isometries of the same logical dimension. It is not generally an
H-preserving unitary. If [U,H]=0 then U commutes with P0 and preserves each
input's ground weight. Hence it cannot map a branch with p_A<1 entirely into
P0. A driven control, energy-exchanging apparatus or dissipative operation
is needed; its preparation, work, noise and reset are additional resources.

The deterministic decoder constructed here is an existence theorem on a
known finite span, not a native local control construction, an efficient
circuit bound or a physical source selection of B.

## 4. The invariant five-diagram hull: preserve logical state, reset multiplicity

The separate hull audit identifies a 20-dimensional invariant space with
metric G tensor I4 and Hamiltonian h tensor I4 in five diagram coordinates.
After an orthonormal change using G, this is C5_multiplicity tensor C4_logical,
with physical Hamiltonian K tensor I4 and K Hermitian. This identification
and H5 action are prerequisites supplied by that other audit, not re-proved
by the recovery checker.

On such a space there is a simple deterministic channel

    rho -> |v0><v0| tensor Tr_multiplicity(rho),

where v0 is any selected normalized multiplicity state. Its Kraus operators
are (|v0><j|) tensor I4 for j=1,...,5. It preserves the logical density matrix
and all its external-reference correlations. A pure-environment dilation
needs dimension at least five to reset arbitrary pure multiplicity inputs
to one pure v0: orthogonal input states must leave orthogonal records in
the environment. Dimension five suffices. The checker verifies the generic
swap/partial-trace dilation, without duplicating the source hull calculation.

Choosing v0 as the true multiplicity ground state would prepare a ground
encoding deterministically via this channel, but not via isolated evolution
under K tensor I4. The reset exports multiplicity information and generally
energy. An apparatus implementing and later resetting those records remains
an additional physical obligation.

## 5. Scalar ground dynamics is not autonomous logical interaction

For any ground encoding B into P0,

    H B=E0 B,              B* exp(-itH) B=exp(-itE0) I4.

The encoded logical state has no nontrivial autonomous evolution under this
same ground Hamiltonian. More generally K tensor I4 evolves multiplicity
but preserves the entire logical reduced state even for correlated inputs.
Keeping the full invariant hull is an exact conditional many-state dynamics,
not a derivation of nontrivial logical physics. An additional logical action
must be identified, including its symmetry and source assumptions.

## Acceptance boundary

Established: exact branch-flag Gram, a deterministic logical decoder, and
conditional minimal pure-environment dimensions three and five.
Not established: a native physical measurement/controller, accessible reset,
energy budget, source-selected target encoding, common all-level refinement,
3+1D dynamics or any T1-T8 closure. Literal P0 postselection and deterministic
environment-assisted recovery remain separate constructions.

## Verification

The pinned-source Gram reconstruction, exact Cholesky flags, isometric
dilation and Kraus normalization pass in normal and `-OO` runs. Subprocess
comparison confirms byte-identical JSON output. This is a finite exact
decoder certificate, not an executed apparatus or full-H5 spectral proof.
