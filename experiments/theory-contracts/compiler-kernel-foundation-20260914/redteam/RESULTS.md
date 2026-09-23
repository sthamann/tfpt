# Minimal compiler trace kernel: what is fixed, and what is not

2026-09-14. Small exact redteam on M4(C), not an enlarged physical model.
No original source files were changed.

## 1. The trace kernel is unique under the stated assumptions

Assume a **complex-linear** normalized cyclic functional on the actual
complexified compiler algebra. The sixteen signed word matrices from
`compiler-clifford-bridge/checker.py:60-64`, `:107-120`, `:156-175` span M4(C)
and satisfy the source ordered-cocycle multiplication table exactly.

Cyclicity gives tau(Eij)=0 for i!=j by the commutator [Eii,Eij]=Eij, and
tau(Eii)=tau(Ejj) by [Eij,Eji]=Eii-Ejj. Normalization therefore forces

    tau(a)=Tr(a)/4,       G(a,b)=Tr(a†b)/4.

Positivity is then automatic and faithful. It is important that "positive
kernel" means positive semidefinite Gram matrices, not entrywise nonnegative
numbers: G(I,iI)=i and G(g,-g)=-1 for unitary compiler words. The exact signed
composition data are retained, unlike in a classical transition matrix.

The GNS Hilbert space is the sixteen-complex-dimensional operator space
M4(C), with cyclic process vector Omega=I. The sixteen source words form an
orthonormal basis. This is **not** a derivation of a new physical sixteen-state
system or a replacement for the four-dimensional spinor state space.

## 2. Order12 is not automatically an observable twelve-step clock

Let sigma³=I and c=i sigma. Left multiplication L_c has exact linear order12,
while Ad_c has order3. Starting from Omega=I, every left observable is static:

    <c^n,L_a c^n> = tau(c^-n a c^n)=tau(a).

Every right observable separately is static as well. Joint left-right access
can see nontrivial three-step process correlations, such as

    |<Omega,c^n>|² = |tau(c^n)|².

But even arbitrary observables on the full GNS state vector cannot see the
extra factor4 in this unreferenced orbit, because

    c^(n+3)=-i c^n,
    |c^(n+3)><c^(n+3)|=|c^n><c^n|.

Thus merely adding right observables does not make this orbit a twelve-state
clock. A coherent alternative between I and c^n could expose the complex
relative amplitude tau(c^n); its real and imaginary parts distinguish the
central phases. Such controlled process interference is an additional access
resource, not supplied by the existence of the Gram kernel.

The trace itself is invariant. Its faithful density matrix is I4/4, so the
finite modular operator rho tensor rho^-T is I16. The corresponding modular
dynamics is trivial. Selecting a nontracial boundary state would be new data,
not a consequence of normalized cyclicity.

## 3. Positive boundary gluing still does not choose a transfer rate

Let P be the GNS rank-one projector onto Omega and Q=I-P. The sixteen actual
source-word conjugations obey the exact twirl identity

    P = (1/16) sum_word Ad_word.

The family T_r=P+rQ, 0<=r<=1, therefore has all of the following properties:
Hilbert positivity and self-adjointness, normalized boundary T_r Omega=Omega,
complete positivity and trace preservation as an algebra map, covariance
under every unitary adjoint action, and the gluing law

    T_r T_s=T_(rs).

Its CPTP realization is r times the identity channel plus (1-r) times the
source-word twirl. On an orthonormal process basis e_j, the kernels
K_r(a,b)=<a,T_r b> obey

    sum_j K_r(a,e_j) K_s(e_j,b)=K_(rs)(a,b).

In continuous notation all rates gamma>=0 satisfy these requirements:

    T_gamma(t)=P+exp(-gamma t)Q.

The choice gamma=0 is static; different positive gamma values yield distinct
decay rates with the same normalized trace and boundary composition rule.
Neither positivity nor this semigroup/gluing law fixes gamma or its physical
units. The base kernel is K_1=G.

Important precision: all strictly positive common gamma values in this
one-rate family are related by a change of time unit. They do not by themselves
prove different dimensionless dynamics. The source-marked two-rate extension
in `TWO_RATE_ADDENDUM.md` below supplies a stronger, explicitly CPTP
nonuniqueness result when the symmetry retained is the marked qstar/S5 action
instead of the full unmarked Clifford group.

This counterfamily addresses the explicit positivity/normalization/covariance/
gluing requirements above. It does not assert that it satisfies every stronger
axiom someone might add. In particular, nontrivial r does not preserve matrix
multiplication as an algebra homomorphism. If instead one demands strictly
topological identity-cylinder gluing without length or transfer data, one gets
an identity cylinder, not a selected nontrivial physical time. A stronger
selection principle must state its extra requirement explicitly.

## 4. The two sigma realizations are source-consistent but must not be merged

The initial trace warning has a concrete source resolution, not a contradiction
between the original computations.

- `v689_gaussian_code_bridge.py:96`, `:189-190` defines the ambient permutation
  (4,5,0,1,2,3,6,7). The same PI_SIG occurs in
  `v774_arf_spinor_compiler.py:204` and `v783_two_qubit_clifford.py:273`.
- `v774_arf_spinor_compiler.py:490-516` transports this very lattice operation
  to the quotient family bits and checks it against sig_bits at lines432-434.
  It fixes three nonzero quotient labels.
- `v783_two_qubit_clifford.py:39-49` fixes the Gaussian complex-coordinate
  chart. Its sigma matrix sends (z0,z1,z2,z3) to (z2,z0,z1,z3), so Tr sigma=1.
- `v783_two_qubit_clifford.py:58-69`, `:1000-1016` associates each Gaussian
  class with a **Pauli context**, not a Pauli operator label.
  Lines928-935 explicitly describe point-line duality and the S6 outer twist.

The new source replay executes the original v774 lattice section and the
original v783 root/context construction. It rebuilds the actual15-class to
15-context dictionary, verifies its sigma equivariance for all240 roots, and
counts the fixed objects directly:

| Same original Gaussian sigma | Fixed nontrivial objects |
|---|---:|
| v774 quotient/class labels | 3 |
| v783 Pauli contexts | 3 |
| v783 Pauli operator labels | 0 |

The bridge subsequently builds the twisted word algebra from those quotient
labels and lifts their rotation by g1->g2->g3->g1, fixing g4. Its exact inner
implementer is

    sigma_B=-(I+g1g2+g2g3+g3g1)/2,
    sigma_B³=I,   Tr sigma_B=-2.

Consequently the original coordinate Ad_sigma has fixed-space dimension6,
while the bridge-word Ad_sigma_B has fixed-space dimension8. The invariant
|Tr sigma| distinguishes them as1 versus2. No unitary or antiunitary change of
basis, central phase, or sigma inversion removes that distinction. These are
different representations of the source action, related at the relevant
finite incidence/context level; they are not the same inner automorphism of
one identified C4 carrier.

The source already makes the needed distinction. This is therefore **not a
bug in v774 or v783**. It is a warning against an extra, unjustified
equivariant C4 identification. A class/context incidence connection is
consistent with the source evidence. No triality claim or new physical
interpretation is inferred. The full v783 group-Hom census is cited from the
source, not presented as rerun by this bounded check.

Both clock realizations satisfy the order12/order3 conclusion above. Their
GNS Omega-return sequence is respectively(1,1/16,1/16) or(1,1/4,1/4), repeated
four times. Any numerical return prediction must say which representation is
being used.

## Verification

`probe.py` supplies the exact signed-word, trace/GNS, clock and transfer-family
checks. `sigma_sources.py` independently replays the original source prefix
and lattice section and checks the class/context transport. `replay.py`
requires normal/-OO byte-identical outputs and rejects three mutations:
twelve-step observability without a reference, identification of the two
sigma realizations, and a uniquely selected gluing rate.

Source hashes and exact counts are in `verification.json`,
`sigma_verification.json` and `replay.json`. All artifacts are confined to this
new redteam directory; no original source or parent artifact was changed.
