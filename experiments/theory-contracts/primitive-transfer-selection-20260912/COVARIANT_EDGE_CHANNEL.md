# Covariant edge operations can transmit a signal without a recorded orientation

2026-09-12. Exact conditional finite-model result, not source-derived dynamics.

## Distinction from the preceding result

The original source deploys the covariant Hamiltonian sum. The preceding
edge audit correctly excludes transfer for individually Clock-averaged edge
Hamiltonians. This does NOT exclude an average of the CHANNELS obtained by
applying individual edges. These are different operations:

    exp(-i theta average(K_k))
    versus Phi(rho)=average(exp(-i theta K_k) rho exp(+i theta K_k)).

The latter is generally not a unitary evolution of the system alone. Convex
mixtures of unitary channels are completely positive and trace preserving;
see [IBM's channel representations](https://quantum.cloud.ibm.com/learning/en/courses/general-formulation-of-quantum-information/quantum-channels/representations-of-channels).
Their use here is standard mathematics, not a new quantum principle.

## Construction using the existing edge orbit

Use the pinned original B,J,O,P reconstruction, on eight complex modes.
Let E_14 be the existing real antisymmetric block linking channels 1 and 4,
and K=E_14[even,odd]+i E_14[even,even] its Hermitian one-body lift.
It obeys K^3=K. Define

    U(theta)=I+(cos(theta)-1)K^2-i sin(theta)K,
    U_k=O^k U O^(-k), k=0,...,5,
    Phi_theta(rho)=(1/6) sum_k U_k rho U_k*.

Each U_k is unitary; Kraus operators U_k/sqrt(6) satisfy completeness.
The six edges form the existing triple-to-pair orbit. Phi is Clock-covariant:
Phi(O rho O*)=O Phi(rho) O*. No value of k must be retained for the signal
below. This differs from the earlier signed POVM example, whose coarse
graining erased its particular witness information.

The averaged generator Kbar commutes with O and P Kbar Q=0, Q=I-P.
Nonetheless the channel Phi transfers population between P and Q.

## Two exact transfer witnesses

For the invariant occupied mode p=(1,1,1,0,0,0,0,0)/sqrt(3), put rho=p p*.
The hidden population after the channel is, with c=cos(theta),

    tr(Q Phi(rho)) = (c^2-8c+7)/18.

For an initially hidden one-particle mixed state rho_H=Q/3,

    tr(P Phi(rho_H)) = (35-34c-c^2)/108.

At theta=pi/2 these are 7/18 and 35/108 respectively. Inputs and outputs
are Clock-invariant density matrices. Invariance of a density matrix does
not mean its support lies exclusively in the trivial Clock representation.
In particular this calculation must NOT be promoted to a Gauss-law
physical-state construction if a stronger gauge restriction is imposed.

## A signal at the literal original boundary

The initial hidden one-particle state and the Fock vacuum have exactly the
same accessible marginal: the accessible vacuum. They differ in global
particle number, not in a coherence between parity sectors. Both are valid
parity-invariant density operators in the declared unconstrained CAR model;
neither occupied preparation is claimed to arise from TFPT.

The edge pulse touches only carrier modes. Let rho'=Phi_(pi/2)(Q/3),
and let R_B project onto original complex boundary modes 5,6,7. Then
R_B rho'=0. Evolve afterward with the UNCHANGED source one-body Hamiltonian
h=I+(B[even,odd]+i B[even,even])/8. The boundary particle probability is

    tr(R_B exp(-i h tau) rho' exp(+i h tau))
       = tau^2/24 + O(tau^3).

The coefficient is checked exactly as tr(R_B h rho' h)=1/24; the zeroth
and first orders vanish because R_B rho'=rho' R_B=0. Analytic finite
matrix evolution and a positive coefficient give a nonzero response for
sufficiently small nonzero tau. This is more than a cyclic-rank statement.
It is not a uniform experimental precision/time guarantee.

Without the additional channel, the hidden state stays boundary-dark under
the original h at all times. The vacuum stays vacuum both with and without
the channel: the second-quantized edge unitaries conserve particle number.
Thus the stipulated protocol distinguishes hidden occupation from vacuum
at the actual boundary without recording which edge was selected.

## Physical boundary and next acceptance test

This does not provide a self-generated reference from the closed quadratic
source. It shows that a persistent oriented reference is not necessary for
this particular population-transfer signal IF stochastic edge operations
are available. A system-only channel can exchange Clock representation
content with its implementation environment while respecting covariance.
That is weaker than conservation of every system Clock sector.

The reviewed source contains the edge matrices and their covariant sum,
but does not derive their stochastic application, pulse angle, environment,
or occupied preparation. The new map is an explicitly additional dynamical
law, not a reinterpretation of the same original Hamiltonian.

The useful next source test is therefore whether the primitive compiler
describes independently realized events (with a derived reduced channel),
or only terms in a coherently summed Hamiltonian. Source labels and loops
alone do not decide this. A successful derivation must reproduce an
actual map and a nonzero boundary response, not merely the same symmetry.

## Verification

`covariant_edge_channel.py` passes 20 exact checks in normal and -OO modes:
source pin/split, Hermitian edge, polynomial unitary identity, Kraus
completeness, covariance, zero-transfer averaged-generator control, exact
population formulas and the original-boundary leading coefficient.
Symbolic identities reduce modulo sin(theta)^2+cos(theta)^2-1; no floating
tolerances. This is the exact one-particle sector with the analytic
number-preserving Fock lift, not a new 256-dimensional matrix execution.
No original-source change, T1-T8 closure, paper promotion, commit or push.
