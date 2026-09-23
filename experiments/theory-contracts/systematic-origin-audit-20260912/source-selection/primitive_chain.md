# Primitive synchronization is not the flattened Bell chain

12 September 2026. NON-RH source-generator comparison.
Reproduction: `primitive_chain.py`.

## Ergebnis in einfachen Worten

**Derselbe perfekte Paarzustand legt die gekoppelte Dynamik nicht fest.**
Zwei besonders einfache Strafterme unterscheiden sich:

- Die primitive Synchronisierung zählt, wie viele der vier Bedingungen
  verletzt sind: Energie 0,1,2,3 oder4.
- Der flache Bell-Term fragt nur, ob überhaupt eine Bedingung verletzt
  ist: Energie0 oder1.

Beide haben denselben eindeutigen Bell-Grundzustand auf einem Paar.
Auf einer Kette mit drei Faktoren haben sie aber verschiedene Spektren
und verschiedene Grundraum-Einbettungen. Der bisherige flache ternäre
Baustein Z ist unter der primitiven Dynamik nicht einmal invariant.

Ein neuer passender vierdimensionaler Grundraum wurde ausdrücklich
konstruiert. Seine Überlappung mit Z ist groß, aber nicht exakt eins.
Deshalb lassen sich die bisherigen exakten Bell-Ketten-/Rekonstruktions-
Resultate nicht allein aufgrund desselben Paargrundzustands übernehmen.

## 1. Source, construction and assumptions

Use the actual four 4x4 skew-Hermitian Clifford generators g_i from
`compiler-clifford-bridge/checker.py`, SHA-256
`bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d`.
All eight inherited source hashes are checked. No changes to the source,
existing flat-chain experiments, paper, website or ledger are made.

The two conditional pair Hamiltonians compared here are

    S_i=g_i tensor conjugate(g_i),
    H_sync=sum_(i=1)^4 (I-S_i)/2,
    H_flat=I-P_Bell.

The S_i are commuting Hermitian involutions. Their unique joint +1 vector
is Phi=(1/2)sum_a|a,a>, and

    P_Bell=product_i (I+S_i)/2.

The source fixes g_i; interpreting these combinations as physical energy,
choosing equal coefficients, adding independent conjugate tensor factors
and connecting them on a physical graph remain additional premises. Here
"primitive parent" means constructed from these primitive source matrices,
not independently established as the unique physical TFPT parent.

## 2. Same pair ground, different primitive violations

The primitive pair spectrum is exactly

| Energy | Multiplicity |
| --- | --- |
| 0 | 1 |
| 1 | 4 |
| 2 | 6 |
| 3 | 4 |
| 4 | 1 |

The flattened pair instead has spectrum0 (onefold),1 (15-fold).
Their joint diagonalization also proves the exact operator bounds

    H_flat <= H_sync <= 4 H_flat.

These inequalities add on any fixed common graph, but do not identify
ground eigenvectors or excitation spectra of overlapping sums. Both pair
operators are bounded finite-range interactions; failure to transfer
special flat-chain identities is not a failure of the general bounded-
interaction construction of finite or quasilocal dynamics.
If h_i=(I-S_i)/2, the flattening is

    H_flat=I-product_i(I-h_i).

This retains the common kernel but replaces the sum of violations by
their Boolean union. It is not a harmless global energy scale or offset.
Flattening also enlarges symmetry: H_flat commutes with every U tensor
bar(U), whereas H_sync does not. An explicit failed Lie commutator is
checked using the actual Hermitian source word i g1.

## 3. Exact three-site primitive-chain spectrum

On the conditional alternating triple define

    A_i=g_i tensor conjugate(g_i) tensor I,
    B_i=I tensor conjugate(g_i) tensor g_i,
    H=4I-(1/2)sum_i(A_i+B_i).

Within each edge the generators commute. Across edges, A_i commutes with
B_i and anticommutes with B_j for i!=j. These exact relations are all
verified directly from the original matrices.

There is a simple full unitary reduction, not a numerical diagonalization.
Let V psi=Phi_12 tensor psi_3. All A_i act as +1 on V. For each binary
four-word r, set v_i=r_i XOR parity(r), and define the four-column block

    U_r=(product_i B_i^v_i) V.

The sixteen blocks concatenate to a 64x64 unitary U. B_i flips the A_j
signs for every j except i. The binary flip matrix I+all-ones is its own
inverse in four dimensions, which is exactly the stated exponent rule.
In these coordinates the Hamiltonian is

    U* H U = [4I16-(1/2)T] tensor I4,
    T=sum_(i=1)^4 [Z_i + product_(j!=i) X_j],

where X_i,Z_i are Pauli operators on four syndrome qubits. The explicit
unitary and every primitive intertwining equation are tested.

The exact characteristic polynomial of T is

    x^6 (x^2-16)(x^2-24)(x^2-8)^3.

Thus the COMPLETE 64-dimensional spectrum of H is

| Energy | Multiplicity |
| --- | --- |
| 4-sqrt(6) | 4 |
| 2 | 4 |
| 4-sqrt(2) | 12 |
| 4 | 24 |
| 4+sqrt(2) | 12 |
| 6 | 4 |
| 4+sqrt(6) | 4 |

Its ground dimension is still four, but the ground energy is 4-sqrt(6)
and the gap is sqrt(6)-2. The flat chain's corresponding energies were
3/4,5/4,2 with multiplicities4,4,56. Equal ground dimension is not equality
of encoded states or dynamics.

## 4. The old flat Z is not invariant

Keep the previous exact flat-chain encoding

    Z=(V+W)/sqrt(5/2),
    W psi=psi_1 tensor Phi_23.

Direct calculation with the primitive-chain H gives

    Z* H Z=(8/5)I4,
    L=HZ-(8/5)Z,
    Z*L=0,
    L*L=(6/25)I4.

Every nonzero old logical input therefore leaves the old encoded range
under infinitesimal primitive evolution. There is no hidden old-Z
subcode on which this defect vanishes. The compressed scalar energy does
not supply invariant dynamics.

More precisely,

    [(H-4I)^2-6I]Z=0.

The old encoding occupies only the two extreme energies4+-sqrt(6), not
the intermediate bands. Its exact weight in the actual ground is

    r=1/2+sqrt(6)/5.

This is approximately0.989898, illustrating why close numerical overlap
would be insufficient to justify transferring exact old formulas.

## 5. An explicit replacement ground encoding

Project Z onto the lower of its two occupied energy bands:

    Y=[I+(4I-H)/sqrt(6)] Z/2,
    Z*Y=Y*Y=r I4,
    G=Y/sqrt(r).

Then

    G*G=I4,
    HG=(4-sqrt(6))G.

Since the independently established ground multiplicity is four, G spans
the complete primitive-chain ground. This gives a concrete replacement
isometry, rather than stopping at a failed transfer of Z.

For every actual source generator g_i and the actual family-cycle w,

    R(u)=u tensor conjugate(u) tensor u,
    [H,R(u)]=0,
    R(u)G=Gu.

These identities are explicitly checked. Full active U(4) equivariance
does NOT follow: the Lie action of i g1 fails both to commute with H and
to intertwine G with the original one-factor action. Thus an assumption
used to obtain the earlier full-U4 boundary depolarization law has changed.

The boundary channel is independently computed below. Repeated
composition, chain refinement and any common continuum still need their
own derivation from G and the primitive H. They are not established by
inheriting the flat Bell model's 9/25 compressed link, cloning
identification or other exact Temperley-Lieb-chain energy identities.
The Bell projectors themselves still satisfy their algebraic relations;
what changed is the Hamiltonian and its low-energy embedding.

## 6. Original compiler directions persist, but not isotropically

Let P_v be the Hermitian version of the original ordered word
g1^v1 g2^v2 g3^v3 g4^v4, and let its Clifford degree be |v|. The exact
boundary compression of G on BOTH outer factors is

    G*(P_v tensor I tensor I)G
     =G*(I tensor I tensor P_v)G = lambda_|v| P_v.

The independently evaluated complete sixteen-word map gives

| Original Clifford degree | Number of words | Boundary multiplier |
| --- | --- | --- |
| 0 | 1 | 1 |
| 1 | 4 | sqrt(6)/4 |
| 2 | 6 | 7/12 |
| 3 | 4 | sqrt(6)/4 |
| 4 | 1 | 1/2 |

Thus no original word direction is mixed into other directions. Finite
source covariance preserves their separate conjugation characters, but
does not impose a common attenuation. In particular the four original
generators have multiplier sqrt(6)/4, not the flat model's 3/5; the
bivector and pseudoscalar directions differ again. Linear extension
determines the whole boundary channel from these sixteen exact tests.

This is a constructive source-specific replacement of the old isotropic
boundary map within the stated finite model. The equality within each
degree uses the chosen equal weights of all four primitive conditions.
It does not prove that the original anchor condition and the three
family conditions must have equal physical coefficients.

The old boundary depolarization law and symmetric-cloning identification
therefore cannot simply be transferred. Nor is an analogous recursive
primitive-chain effective Hamiltonian claimed without a separate test.

This boundary map is not merely a finite positive-time step of the
primitive one-register noise semigroup either. Under vectorization the
primitive synchronization operator assigns decay energies 3 and 1 to
Clifford degrees 1 and 3, respectively: conjugation by g_i changes the
sign of a degree-k word k times for even k and 4-k times for odd k.
A step exp(-t H_sync) would therefore have multipliers exp(-3t) and
exp(-t). For any finite t>0 these cannot both equal sqrt(6)/4. At t=0
both would be 1, also incorrect. This excludes that specific semigroup
identification, not other channels, generators or dressed reductions.

## 7. Scope

This is an exact finite comparison of two explicitly defined parents
using the same original four matrices, not a proof that either parent is
the unique physical source. Finite primitive/family symmetry is retained;
full U(4) symmetry was deliberately not smuggled into the primitive model.
No numerical eigensolver or tolerance is required. All T1-T8 and the
physical register/graph/time selection remain open.

## 8. Executed verification

The checker passed 87 exact acceptance checks under normal Python and
Python -OO, with byte-identical JSON results. The source-selection file
diff whitespace check passed. The checks include the full 64-dimensional
unitary spectral reduction, the constructive ground isometry, all
sixteen boundary words on both ends, source covariance and explicit
full-U4 counterexamples. They are finite mathematical checks, not
additional physical-gate closures.
