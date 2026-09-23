# Source-generator synchronization: Bell selection without full active U(4)

12 September 2026. NON-RH. Companion checker: `synchronization.py`.
This tests the actual four source generators and all eight inherited source
hashes. No original source, paper, ledger, graph, or TOE status is changed.

## Ergebnis in einfachen Worten

**Eine bisher zusätzliche Voraussetzung lässt sich für die Auswahl des
Bell-Zustands ersetzen:** Wir müssen nicht alle möglichen unitären
Transformationen als aktive Symmetrie fordern. Es genügt, die vier echten
Compiler-Operationen auf einem angenommenen System und seinem konjugierten
Partner als exakt übereinstimmende Vergleiche zu behandeln.

Vier positive Vergleichsfehler wählen dann genau einen gemeinsamen
Nullzustand: den Bell-Zustand. Die ursprünglichen Vorzeichen des Compilers
werden dabei benutzt, nicht geglättet.

Aber: **„exakte Übereinstimmung“ ist selbst eine zusätzliche physische
Forderung.** Die bloße Unverändertheit eines Zustands unter den Operationen
reicht nicht. Vier alternative Vergleichsvorzeichen bleiben sogar mit dem
Familienzyklus verträglich. Auch die Kopplungsgewichte, der physische
Partner und das tatsächliche Erreichen des Grundzustands sind nicht aus
der Algebra allein abgeleitet.

## 1. Actual source, dual pair, and observable mismatch

The source is
`experiments/theory-contracts/compiler-clifford-bridge/checker.py`,
SHA256 `bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d`.
Only its reviewed `generators()` definition is extracted. Its eight
inherited source pins are checked without executing their full suites.

The four actual matrices satisfy

    g_i*=-g_i, g_i^2=-I, g_i g_j=-g_j g_i for i!=j.

Their sixteen ordered words U_v span M4(C). Introduce the **conditional**
physical pair V tensor conjugate(V), V=C4, and set

    Q_i=g_i tensor conjugate(g_i),
    a_i=i g_i,
    D_i=a_i tensor I-I tensor a_i^T.

The a_i are Hermitian involutions. Exact multiplication gives

    Q_i*=Q_i, Q_i^2=I, [Q_i,Q_j]=0,
    D_i*=D_i, D_i^2/4=(I-Q_i)/2.

Thus a primitive positive mismatch parent is

    H_sync=sum_i (I-Q_i)/2=(1/4)sum_i D_i^2.

The first and second comparisons are transposed partners, not four
simultaneously readable classical variables. The local a_i do not commute;
their paired correlation operators Q_i do. This distinction prevents
interpreting the Bell condition as classical duplication of an arbitrary
quantum state.

## 2. Exact uniqueness of the common +1 line

Let Phi=vec(I)/2. Row-major vectorization obeys

    (g tensor conjugate(g)) vec(X)=vec(g X g*).

Consequently Q_i Phi=Phi. Conversely, if all Q_i vec(X)=vec(X), then X
commutes with all g_i, hence with their entire word span M4(C). Its
commutant is scalar, so X=cI. This proves

    intersection_i ker(I-Q_i)=span{Phi}.

No full active U(4) covariance premise is needed for this conditional
kernel theorem. It follows from the irreducibility of the actual source
generators. The Bell projector is

    P_Phi=product_i (I+Q_i)/2.

This is not a claim that physical dual pairing or the common +1 condition
already follows from the compiler. It shows exactly what those conditions
would select.

## 3. Complete source-word spectrum and remaining weights

The sixteen states Phi_v=vec(U_v)/2 are orthonormal and form a complete
basis of the16-dimensional pair. On Phi_v,

    Q_i Phi_v=(-1)^(sum_(j!=i) v_j) Phi_v.

The binary syndrome map is the off-diagonal-ones4x4 matrix over F2. Its
square is I, so every four-sign pattern occurs exactly once. This gives
the **complete** primitive spectrum

| H_sync energy | multiplicity |
|---|---|
| 0 | 1 |
| 1 | 4 |
| 2 | 6 |
| 3 | 4 |
| 4 | 1 |

The actual family lift cycles Q1,Q2,Q3 and fixes Q4. Within positive
linear sums of these independent primitive penalties, family covariance
therefore gives

    H_(J,K)=J sum_(i=1)^3 (I-Q_i)/2 + K(I-Q_4)/2,   J,K>0.

It does not force J=K. The energies are aJ+bK, with a=0,1,2,3,
b=0,1 and multiplicities binomial(3,a); accidental coincidences combine
these multiplicities. The Bell ground remains unique and the gap is
min(J,K). Setting a coefficient group to zero removes conditions and
increases the ground space; it is not another derivation of the same
fully synchronized pair.

The flat Bell parent I-P_Phi has spectrum0 once and1 fifteen times.
It selects the same ground vector but is **not** H_sync. Source primitive
synchronization thus determines a state condition more readily than a
unique energy hierarchy, overall time scale, or physical evolution rule.

## 4. Why symmetry alone still leaves alternative states

Vector synchronization Q_i psi=+psi is strictly stronger than physical
ray or density invariance

    Q_i rho Q_i*=rho.

Every Phi_v ray satisfies the latter: its sign character cancels in the
density operator. For any target signs tau_i, the positive parent

    H_tau=sum_i (I-tau_i Q_i)/2

has a unique minimum at the corresponding Phi_v. These states are all
maximally entangled, but their paired correlations have different signs.
They are physically distinguishable states, not different global phases
of the same Bell vector.

Four choices also retain the source family cycle, namely tau=(s,s,s,t):

| target signs | source word giving its state |
|---|---|
| (+,+,+,+) | I |
| (-,-,-,+) | g4 |
| (+,+,+,-) | g1 g2 g3 |
| (-,-,-,-) | g1 g2 g3 g4 |

The checker verifies exact vector invariance under the family lift for
these four states, in addition to covariance of their signed parents.
Hence source symmetry plus a unique ground state still does not select
the common +1 target. Choosing equal, rather than signed or relabeled,
correlations is the added synchronization criterion.

### Relation to the older same-copy four-ground result

For this actual finite compiler, C=g1 g2 is unitary and satisfies

    C g_i C*=conjugate(g_i), C w C*=conjugate(w).

Therefore I tensor C carries the earlier simultaneous same-copy
operators g_i tensor g_i into Q_i. The two finite symmetry classifications
are unitarily equivalent. There is no contradiction with the previous
four admissible family-fixed unique grounds: synchronization narrows the
criterion to a chosen trivial vector character.

This finite intertwiner does not extend to every U in U(4), since a
nonreal central scalar U=e^(i theta)I cannot be conjugated to its complex
conjugate by C. The earlier distinction between full U tensor U and
U tensor conjugate(U) remains intact.

## 5. Exact averages, carefully separated by representation role

Expanding the product of commuting plus-projectors gives

    P_Phi=(1/16)sum_v U_v tensor conjugate(U_v).

The same operator results by uniformly averaging the actual96-element
group generated by the original g_i and family w. Word phases cancel in
the dual representation; the family fixes Phi. The checker verifies the
actual96 distinct source matrices and their full operator average.

Three interpretations must be kept separate:

**A. Single-register operator space (Liouville representation).** If the
16-component vector means vec(X), not a two-party physical state, then

    P_Phi vec(X)=vec(Tr(X)I/4).

The same matrix represents the single-register completely depolarizing
CPTP channel. Furthermore

    -H_sync vec(X)
      =vec((1/2)sum_i [g_i X g_i*-X]).

Here -H_sync is the matrix of a random-unitary Lindblad generator;
exp(-t H_sync) has a dissipative-channel interpretation for t>=0. It is
not a Hamiltonian commutator merely because H_sync is Hermitian on this
operator-space inner product.

**B. Actual physical doubled Hilbert space.** If V tensor conjugate(V)
is instead declared to describe two physical factors, then Phi is an
entangled state and P_Phi an orthogonal projector. Acting on a physical
density matrix as rho -> P_Phi rho P_Phi is generally trace-decreasing
filtering, not an unconditional preparation channel. A Hermitian H_sync
may be assigned as a physical parent, but unitary motion under it does
not cool an arbitrary excited state into its unique ground state.

**C. Random source operations on that physical doubled state.** The channel

    rho -> (1/16)sum_v Q_v rho Q_v*,
    Q_v=U_v tensor conjugate(U_v),

preserves all16 syndrome populations. For example it fixes any nontrivial
Phi_v Phi_v* orthogonal to Phi. Therefore this physical random-operation
channel does not prepare Bell either. It is not the same mathematical
object as the operator average in the displayed projector identity.

All single-register Liouville equalities are checked on all16 matrix
units. The physical doubled-channel counterexample is checked exactly.
Preparing Bell would require an additional state-preparation mechanism,
such as measurements with conditional correction or an appropriate bath;
no such physical mechanism is derived in this audit.

## 6. What was removed and what is still added

Removed from the **conditional state-selection proof**: the requirement
that the physical Hamiltonian have full active U(4) symmetry. Actual
source generators suffice to force the common +1 vector line.

Still added or unresolved:

- realization of a second physical conjugate factor, rather than only a
  mathematical vectorization of operators;
- physical identification of the compared markings and their transpose;
- selection of the trivial comparison character, rather than another
  physically invariant ray or signed correlation target;
- adoption of positive mismatch energy and choice of J/K, scale, schedule
  and actual state preparation;
- network geometry, compatibility of overlapping comparisons, and the
  missing relation to the actual TFPT charged/rotor source and continuum.

The result genuinely reduces one earlier sufficient hypothesis for a
specified Bell state. It does not silently derive all the other premises
or justify replacing the earlier Bell-chain dynamics by a new spectrum.

## Verification

Normal and `-OO` execution each pass242 exact guards; a subprocess comparison
confirms byte-identical JSON. The checker verifies all eight
inherited source hashes, the complete16-state syndrome basis, all four
family-fixed alternatives, the actual group average and the typed channel
identities. Explicit exceptions preserve every guard under optimization.

Systematic debugging isolated one implementation error: a symbolic energy
coefficient was multiplied by a Python Boolean. Casting the declared
indicator to integer0/1 fixed its type without changing a mathematical
formula or acceptance condition. Only synchronization.py and this note
were created; no T1-T8 problem is marked closed.
