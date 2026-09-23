# Source selection: matching, energy, and physical interpretation

12 September 2026. NON-RH. This extends the preceding conditional Bell-chain
work by returning to the actual four compiler generators. It does not modify
the original source, paper, website, or T1–T8 status.

## 1. The precise selection gain

Let the actual irreducible four-generator representation act on V=C4, and let
Q_i=g_i tensor conjugate(g_i). These are commuting Hermitian involutions.
Their common +1 space is exactly the line Phi=vec(I4)/2. Indeed,

    Q_i vec(X)=vec(g_i X g_i*),

so simultaneous fixed vectors are precisely the commutant of the source
generators. Their sixteen words span M4(C), whose commutant is scalar.
Consequently

    P_Phi=product_i (I+Q_i)/2,
    H_sync=sum_i (I-Q_i)/2,
    ker(H_sync)=span(Phi).

This removes full active U(4) from the **conditional state-identification
lemma**. It does not derive a second physical system or the zero-mismatch
condition. Ordinary symmetry invariance of a density matrix is weaker:
all sixteen joint-character pure states are invariant under conjugation by
the Q_i, and four of them also respect the source family operation.

The source family cycles the first three comparisons and fixes the fourth.
Positive penalties therefore still permit two independent weights J,K:

    H_(J,K)=J sum_(i=1)^3 (I-Q_i)/2 + K(I-Q_4)/2.

Every J,K>0 has the same Bell ground, but its excited energies are aJ+bK.
Neither the ratio J/K nor an absolute physical time scale is selected here.
The displayed H_sync sets J=K=1 as an explicit diagnostic convention.

See [synchronization.md](synchronization.md) for the exact spectrum,
alternative target signs, and equivalence of same-copy and dual
representations for this particular finite source group.

## 2. A state does not determine its parent Hamiltonian

The earlier flat parent is H_flat=I-P_Phi. It assigns one common cost to every
failed comparison pattern; H_sync counts the number of failed primitive
comparisons. Their spectra are respectively

    H_flat: 0 (once), 1 (fifteen times),
    H_sync: 0,1,2,3,4 with multiplicities 1,4,6,4,1.

They have the same kernel, not the same dynamics. On a three-site alternating
V,conjugate(V),V chain, the primitive Hamiltonian has complete exact spectrum

| energy | multiplicity |
|---|---:|
| 4-sqrt(6) | 4 |
| 2 | 4 |
| 4-sqrt(2) | 12 |
| 4 | 24 |
| 4+sqrt(2) | 12 |
| 6 | 4 |
| 4+sqrt(6) | 4 |

The earlier flat-ground encoding Z is not an invariant subspace of this
Hamiltonian H. Its mean and orthogonal leakage are exactly

    Z* H Z=(8/5)I4,
    (HZ-(8/5)Z)*(HZ-(8/5)Z)=(6/25)I4.

This is not just a numerical warning: a replacement primitive ground
encoding has been constructed explicitly. Set r=1/2+sqrt(6)/5 and

    G=[I+(4I-H)/sqrt(6)]Z/(2sqrt(r)).

Then G*G=I4 and HG=(4-sqrt(6))G. It intertwines the actual compiler and
family operations. Its squared overlap with Z is r, about 98.99 percent,
yet the old exact full-U(4) encoding law fails. High overlap cannot transfer
an exact theorem between different parents. The complete spectrum is
certified using an explicit 64-dimensional unitary reduction to a
16-dimensional syndrome operator tensor I4, not floating-point diagonalization.

The new encoding also gives a simple exact transport law on both end sites.
For an ordered compiler word U of Clifford degree k, its end compression
G*(U tensor I tensor I)G, or G*(I tensor I tensor U)G, is lambda_k U:

| word degree k | lambda_k |
|---|---|
| 0 | 1 |
| 1 and 3 | sqrt(6)/4 |
| 2 | 7/12 |
| 4 | 1/2 |

All sixteen word directions are retained without mixing, but attenuated
unequally. This is more structured than arbitrary loss, yet it is not the
old depolarizing attenuation 3/5. The equal primitive weights remain a premise.
Nor is this compression simply a time step of L_sync below: its decay
energies on degrees 1 and 3 are respectively 3 and 1, so equal nontrivial
attenuations on those degrees cannot equal exp(-3t) and exp(-t) at any t>0.
Spatial compression and noisy time evolution must also be distinguished.

See [primitive_chain.md](primitive_chain.md). The prior flat-chain
Temperley–Lieb and special compression results remain true for their stated
model; no transfer of those identities to this primitive chain is asserted.

## 3. The same matrix can mean different physical operations

This is an essential representation check, not a proposed new duality.

| role of the 16 components | meaning of P_Phi | meaning of H_sync |
|---|---|---|
| Physical pair V tensor conjugate(V) | entangled-state projector | possible coherent pair Hamiltonian |
| Vectorized single-register operator X | map X -> Tr(X)I4/4 | negative matrix of a noise generator |
| Normalized Choi representation of a process | identity channel's Choi state | not automatically the same superoperator |

For the single-register reading, define

    L_sync(X)=(1/2)sum_i (g_i X g_i* - X).

Its Liouville matrix is -H_sync. Each commuting constituent has the exact
finite-time channel

    exp[t(Ad_g-I)/2] = ((1+exp(-t))/2) Id
                       + ((1-exp(-t))/2) Ad_g.

For t>=0 this is a convex mixture of unitary channels. Their product proves
complete positivity and trace preservation directly for every t. Its unique
stationary density is I4/4, not a physical two-party pure vacuum. This is
a finite-dimensional Lindblad semigroup with jump operators g_i/sqrt(2).
The standard framework is due to
[Lindblad (1976)](https://doi.org/10.1007/BF01608499); the displayed
random-unitary decomposition proves the claims needed here directly.

The full word average instead gives the completely depolarizing channel E,
whose Liouville matrix is P_Phi. The flat generator E-Id produces

    exp[t(E-Id)]=exp(-t)Id+(1-exp(-t))E.

Both channels have the same stationary density and different relaxation
spectra. At t=log(2), starting from diag(1,0,0,0), the exact outputs are

    primitive: diag(15,3,9,5)/32, purity 85/256,
    flat:      diag(5,1,1,1)/8,   purity 7/16.

The primitive channel's inverse at t=-log(2) maps that input to
diag(15,3,-9,-5)/4, which is not positive. Thus this dissipative semigroup
is not a reversible physical time group on all single-register states.
By contrast exp(-it H_sync) on an assumed physical pair is unitary and
preserves purity. These are different assignments of states and operations.

The checker also performs the Choi realignment explicitly:

    normalized Choi(Id)=P_Phi,
    normalized Choi(superoperator with Liouville matrix P_Phi)=I16/16.

Calling both matrices a Bell object without tracking this realignment would
confuse perfect information preservation with complete information loss.
Random conjugations on the physical pair are a third process: they preserve
all sixteen syndrome populations and do not prepare a selected Bell state.

## 4. What survives at infinite length

The special flat-chain invariant sectors do not transfer automatically.
However, the earlier **general locality existence argument does transfer**.
For the explicitly chosen alternating half-line, a primitive edge is a
bounded positive interaction with norm 4, or norm 3J+K for fixed positive
J,K. It is nearest-neighbor, uniformly bounded, and time-independent.

Using the same F(r)=(1+r)^(-2) and F_mu(r)=exp(-mu r)F(r) on the half-line,

    ||Phi||_(F_mu) <= 4 exp(mu) (3J+K),

which is 16 exp(mu) at J=K=1. The summability and convolution estimates
from [the earlier proof](../chain-extension/README.md) are unchanged.
The standard thermodynamic-limit theorem therefore gives norm convergence
of finite-volume evolutions on every local observable, uniformly on
compact time intervals, and a strongly continuous quasi-local automorphism
group. See [Nachtergaele and Sims, Theorem 3.1](https://arxiv.org/pdf/1004.2086).

Likewise, finite-volume ground states have weak-star accumulation states.
For each fixed local A, the local commutator stabilizes once the boundary
is outside its interaction neighborhood; the nonnegative ground-state
form passes to the limit. At least one infinite-volume ground state and
its positive-energy GNS dynamics follow by the same argument. This does
not claim uniqueness, a uniform spectral gap, an explicit ground state,
or a physical 3+1D continuum limit. It is an analytic application of a
standard theorem, not a theorem proved by the finite checker.

Thus the source-nearer primitive candidate is not blocked on existence of
infinite dynamics. Its missing steps are source selection of physical
composition, couplings, state, and operational interpretation.

## 5. A smaller conditional selection principle

A concrete simplification is available for the next source audit. It is a
conditional lemma, not a newly derived physical premise. Equip
W=span_R{a_i=i g_i} with its actual trace metric
Tr(a_i a_j)/4=delta_ij. For D_i=a_i tensor I-I tensor a_i^T, restrict the
energy to a positive quadratic mismatch form

    H_C=sum_ij C_ij D_i D_j,   C=C* >=0.

If the form is actively isotropic under all orthogonal Clifford-frame
rotations, R^T C R=C for every R in O(4), then C=cI, c>=0. Sign flips
kill all off-diagonal entries and coordinate permutations equate the
diagonal entries. Consequently

    H_C=c sum_i D_i^2=4c H_sync.

For c>0 this fixes J=K and the primitive spectral shape, leaving the overall
scale. This requires less active symmetry than full U(4), and selects
the primitive, rather than the flat, parent **because of the quadratic
ansatz**. Isotropy alone would also allow the flat parent.

This is not passive coordinate covariance: transforming both coordinates
and C permits arbitrary anisotropy. It is an added statement that the
physical quadratic form has no preferred Clifford direction. The source's
marked fourth generator/anchor makes this an actual issue to justify.
For general Hermitian C, its imaginary antisymmetric part contributes
commutator terms since the D_i do not commute; full O(4) isotropy eliminates
that part too. Positivity of C is an assumption, not inferred from mere
positivity of the represented H_C.

Thus a precise next question is whether the source requires **positive
quadratic comparison plus Clifford-frame isotropy**, while permitting the
anchor to remain distinguished elsewhere. If yes, the two-weight freedom
closes for this interaction term. If not, the freedom must remain visible.
The lemma is an elementary analytic proof independently reviewed here,
not part of the finite checker count.

## 6. Decisive follow-ups, without silently adding the answer

1. **Define what a compiler state represents.** Give the actual operational
   map from source objects to physical states and accessible operations.
   Distinguish a physical conjugate factor from operator vectorization.
   Acceptance: matching observables and compositions, not equal dimensions.
2. **Derive which failures cost energy.** Primitive mismatch counting and
   a flat failed/passed test are explicit competing candidates. Give a
   source axiom that chooses a rule and J/K, or retain the family as
   underdetermined. Reproducing the same Bell ground does not pass this gate.
3. **Continue with the selected primitive encoding, conditionally.** The
   exact G now permits real tests of source-operation transport. Derive
   repeated-block effective operators and keep any generated interactions;
   do not impose the old flat closure. Separate effective information loss
   from coherent full-system dynamics.

No T1–T8 gate, physical clock, RH, factoring, P versus NP, or Hylæan
capability is closed here. The gain is a weaker state-identification premise,
an exact source-nearer three-site solution, and an explicit obstruction to
confusing representation with dynamics.

## 7. Reproduction

Run `python3 -B run_checks.py` in this directory. Each checker is replayed
normally and with `-OO`; explicit exception guards remain active. The
receipt records checker hashes and exact outputs. Upstream generator and
eight inherited source hashes are verified by each checker. Finite exact
checks and separately stated all-length analytic arguments are not merged
into a single machine-proof claim.

Current replay: 467 explicit guards per pass across three new checkers;
normal and optimized outputs agree in all six executions. The previous
three chain-extension checkers also passed in six executions, recorded in
`previous_chain_verification.json`. This is twelve checker executions,
not twelve independent proofs or physical acceptance tests.
