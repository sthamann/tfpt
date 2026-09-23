# The finite boundary limitation survives adaptive protocols

2026-09-12. NON-RH. Source-scoped operational consequence, not an all-TFPT no-go.

## Exact source split

boundary_access.py reconstructs the original B and J blocks from the pinned
source's reviewed orbit helpers and the already documented deployed channel
permutation (0,3,1,2,5,4). It does not rerun the upstream derivation of that
permutation. The full source SHA is checked before extraction; no original
module is imported or mutated.

For P=(1/6)sum_(j=0..5)O^j, Q=I-P, exact checks give

    rank P=10, rank Q=6,
    span{B^k b: b in boundary, 0<=k<=4}=im P,
    PBQ=PJQ=0, [J,B]=0.

Thus D=alpha J+g B preserves both subspaces for all alpha,g. For nonzero g
the existing full boundary CAR access generates ten real Majorana modes.
With these modes ordered first, the finite Fock Hilbert space is
C^32 tensor C^8 and its accessible full field algebra is M32(C) tensor I8.
The quadratic even Hamiltonian splits as

    H=H_access tensor I + I tensor H_hidden

up to a scalar. Fermionic odd hidden fields involve a parity convention;
their even Hamiltonian and the hidden primitive bilinears act in the second
factor. Restricted physical even-only access is no stronger than this full
field access. Coordinate dimensions 10+6 are not Fock dimensions 32+8.

## All finite boundary-only protocols

Fix any initial joint state rho, including an entangled state. Allow arbitrary
instruments in the accessible factor, local ancillas, feedback based on earlier
accessible outcomes, and free evolution between steps. For each resolved branch
r its total Kraus operator factors

    L_r tensor V_r,

where V_r is a unitary hidden evolution. Summing unresolved Kraus labels gives
the same conclusion for general instruments. The outcome probability is

    p(r)=Tr[(L_r* L_r tensor I)rho]
        =Tr[L_r* L_r rho_access].

It is independent of H_hidden at fixed accessible dynamics and initial
accessible marginal. The proof applies to arbitrary finite branch depth;
adaptive choices only change the branch labels and L_r. Postselection on
accessible outcomes does not evade it: all conditional probabilities are
ratios of the same accessible probabilities where denominators are nonzero.
Any well-defined limit of these protocol distributions inherits the equality.

This is stronger than a zero linear-response computation. It is a standard
partial-trace/no-signalling consequence applied to the verified source split,
not a new general quantum-information theorem. Background:
https://quantum.cloud.ibm.com/learning/en/courses/general-formulation-of-quantum-information/density-matrices/multiple-systems

## What correlations do and do not change

Entangled initial states need not have zero connected cross-correlations.
Conditioning on an accessible measurement can steer the hidden conditional
state. But observing those cross-correlations needs hidden or joint access;
they are not extra boundary-only outcomes.

The independent Bell-state control in the checker verifies this distinction:
a hidden Z rotation leaves rho_access=I/2 unchanged while switching the joint
X tensor X expectation from +1 to -1. This is a two-qubit illustrative control,
not a replacement for the source-specific split or the all-protocol proof.

If a chosen preparation law ties rho_access to hidden parameters, those
parameters may be inferred from preparation-dependent boundary statistics.
That is different from reading hidden autonomous evolution with a fixed
initial marginal. No initial statistical independence is assumed above.

## Simplicity and the next source question

Under precisely this boundary-only contract, all states with equal accessible
partial trace give identical future boundary experiment statistics. The 32D
accessible factor is an exact sufficient description for those experiments.
It is not a declaration that the hidden modes are physically nonexistent or
irrelevant once a larger observable contract is supplied.

Therefore another boundary-only protocol, longer waiting, or an accessible
ancilla cannot close this particular access gap. The next task must inspect
whether TFPT independently supplies a non-boundary observable or a coupling
mixing the two factors. Do not insert such a coupling merely to get a signal.
Conversely, if boundary-only access is fundamental, reconsider assigning the
hidden primitive sector an observable role in this finite model.

Nine exact checks passed in normal and -OO modes with identical JSON output.
No full upstream source derivation, existing 256D Fock suite, physical
preparation, continuum construction or T1--T8 closure is claimed.
