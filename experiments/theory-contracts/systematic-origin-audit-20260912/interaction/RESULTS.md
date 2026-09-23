# Interaction from compiler operations: a complete finite selection audit

12 September 2026. NON-RH. No TOE status promotion.

## Ergebnis in einfachen Worten

**Die lokale Compiler-Regel allein kann keine Wechselwirkung erzeugen.**
Wenn sie auf beiden Teilen eines zusammengesetzten Systems unverändert
gelten soll, bewegen sich diese Teile unabhängig. Lockert man die Forderung
zu gemeinsamer Symmetrie, werden Wechselwirkungen möglich, aber die
ursprüngliche Symmetrie lässt sieben nichttriviale Energieparameter offen.

Es gibt auch ein positives, besonders einfaches Ergebnis: **Wenn ein System
mit seinem komplex-konjugierten Gegenstück gepaart wird und die gemeinsame
Symmetrie auf alle unitären Basiswechsel erweitert wird, bestimmen diese
Symmetrie und ein eindeutiger Grundzustand den Bell-Kopplungstyp bis auf
Energieskala und Energie-Nullpunkt.** Das ist eine wirkliche bedingte Auswahl,
keine bloße Ähnlichkeit von Zahlen. Die Paarung und die stärkere Symmetrie
sind aber zusätzliche Voraussetzungen; ihre physikalische Auswahl ist
in den geprüften Compiler-Quellen nicht nachgewiesen.

Das vorhandene Rotor-Modell besitzt bereits eine andere, ausdrücklich
dynamische Rückwirkung. Dieses Ergebnis ersetzt es nicht und erklärt
auch nicht dessen Zuordnung zum Compiler.

## 1. Scope and frozen source

The checker reads only the original four-generator function in
`experiments/theory-contracts/compiler-clifford-bridge/checker.py`:
SHA-256 `bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d`.
All eight inherited source hashes are verified. No upstream research suite
is executed or silently represented as replayed. Prior selection audit:
`primitive-transfer-selection-20260912/COHERENT_RECORD_SELECTION.md`.

The actual source gives four skew-Hermitian 4x4 Clifford generators g_i,
their sixteen words spanning M4(C), and

    w = (I + g1 g2 + g2 g3 + g3 g1)/2,
    w g1 w* = g2, w g2 w* = g3, w g3 w* = g1, w g4 w* = g4.

We explicitly ADD two tensor copies C4 tensor C4. Their labels are not
derived spatial points, opposite holographic boundaries, chronological
steps, or the existing rotor matter modes. Hilbert tensor-product locality
does not establish spacetime locality. An algebra automorphism is not
automatically a physical update.

## 2. Exact local-operation preservation excludes a two-copy interaction

Suppose a unitary V is required to realize the above family action on BOTH
full local generator algebras:

    V (g_i tensor I) V* = sigma(g_i) tensor I,
    V (I tensor g_i) V* = I tensor sigma(g_i).

W0=w tensor w realizes these equations. Thus W0* V commutes with all local
generators on both sides. Their words span M4 tensor M4 = M16, whose
commutant is scalar. Therefore

    V = exp(i theta) (w tensor w).

This maps every product state to a product state and cannot couple the
two factors. The statement is complete under its hypotheses, rather than
a failed search over some Hamiltonians. An interaction requires an enlarged
operation-level update: some local operator must acquire support on both
factors. It cannot retain exactly the two displayed local rules.

## 3. Full classification under weaker simultaneous source symmetry

Now ask instead for a Hermitian H satisfying

    [H, g_i tensor g_i] = 0 for i=1,...,4,
    [H, w tensor w] = 0.

Let P_a be the sixteen Hermitian source words. Conjugation by g_i assigns
sixteen distinct four-sign characters to these words. In the full basis
P_a tensor P_b, simultaneous symmetry forces a=b. Family conjugation is a
signed permutation of P_a; its signs cancel in P_a tensor P_a. Its orbits
have lengths 1,1,1,1,3,3,3,3. Consequently

    H = sum_O c_O sum_(a in O) P_a tensor P_a,

with eight independent real coefficients, or SEVEN modulo scalar energy.
No one-factor nonconstant terms survive these conditions: each nonidentity
equal-label pair is a genuine two-factor operator. An allowed interaction
space is not a selected physical interaction.

### Positive cone and unique-ground counterexample, completely classified

The four commuting Hermitian involutions K_i=g_i tensor g_i yield sixteen
orthogonal rank-one projectors

    Pi_s = product_i (I+s_i K_i)/2,       s_i in {+1,-1}.

Family conjugation rotates the first three signs and fixes the fourth.
The invariant positive cone consists exactly of nonnegative sums of the
eight orbit-sum projectors. Its extreme-ray ranks are

    1,1,1,1,3,3,3,3.

In particular there are four family-fixed rank-one Pi_s. Any H_s=I-Pi_s
is positive, has exactly one ground state, gap one, and the same complete
spectrum 0 (multiplicity 1), 1 (multiplicity 15). These four choices obey
the same symmetries but have orthogonal ground states. Thus positivity,
a unique ground state, equal nonzero energies and a normalized gap do not
select a source-symmetric parent in this class.

## 4. Even full simultaneous U(4) symmetry does not force an interaction

Let F be factor swap, F(|a> tensor |b>)=|b> tensor |a>. It is expressible
in the actual source basis:

    F = (1/4) sum_a P_a tensor P_a.

F commutes with U tensor U for EVERY U in U(4), so also with all the source
symmetries. The partial-swap family

    V_theta = cos(theta) I - i sin(theta) F

is unitary and commutes with w tensor w. At theta=0 it does not interact;
at theta=pi/4 it maps |0,1> to (|0,1>-i|1,0>)/sqrt(2), whose one-factor
purity is 1/2. Positive Hamiltonians are available using (I-F)/2 or (I+F)/2,
with their coefficient free. Neither energy positivity nor stronger
simultaneous unitary symmetry chooses the coefficient or its nonzero value.

This gives an explicit required operation-level change. For A=g tensor I,
B=I tensor g, c=cos(theta), s=sin(theta),

    V_theta A V_theta* = c^2 A+s^2 B+i c s (A F-F A).

The last term is jointly supported. The checker verifies the identity at
theta=pi/4 using the source g1. Declaring this enlarged generator action
would specify an interaction, but it supplies new theta-dependent data.
No such rule is derived from the original family automorphism here.

Even asking for channel period three does not repair selection:
theta=pi/3 gives V_theta^3=-I, while theta=0 is also periodic. Since it
commutes with w tensor w, composing the two retains the channel period.
Periodicity is not sufficient to distinguish interacting and independent
updates, and is not a derived physical time scale.

## 5. A genuinely simple positive result: conjugate gluing

Change the hypotheses openly: choose the dual pairing U tensor conjugate(U),
and require covariance for EVERY U in U(4), not just the source's finite
generator symmetries. Then

    |Phi> = (1/2) sum_(a=0)^3 |a,a>,
    P_Phi = |Phi><Phi| = (1/16) sum_a P_a tensor conjugate(P_a)

is invariant. The complete invariant Hermitian space is exactly
span{I,P_Phi}. The checker establishes completeness by first using the
source Pauli conjugations to reduce to sixteen equal-label dual pairs,
then imposing all fifteen infinitesimal Hermitian generator conditions

    [H, P_a tensor I - I tensor conjugate(P_a)] = 0.

This exact linear system has rank fourteen on those sixteen coefficients.
Hence H=alpha I+beta P_Phi. A UNIQUE ground state forces beta<0; after
subtracting the ground energy, this is precisely

    H_glue = J (I-P_Phi),        J>0.

Thus the coupling TYPE is selected under these stronger assumptions,
with one undetermined positive energy scale. It is not merely scalar
motion: at model time pi/J it sends product |0,0> to a maximally entangled
state with reduced state I4/4. The checker verifies this exactly.

### Why this still does not select TFPT's physical motor

1. A conjugate Hilbert space is mathematically canonical, but adjoining it
   as an independent physical factor is not forced by that fact.
2. Full U(4) is stronger than the actual source generator/family symmetry.
   It treats the additional source markings as irrelevant to this term.
   That physical assumption must be derived, not hidden as a basis convention.
3. Covariance under a passive change of coordinates does NOT mean that an
   active Hamiltonian commutes with all those transformations. The selection
   proof uses the stronger active statement explicitly.
4. J, the update duration, the realization of the tensor pairing, a network
   of pairings and its propagation/continuum are still absent.
5. This rank-one gluing is compatible with the Bell-syndrome form exposed
   by the previous record decoder. It fixes the syndrome, NOT the four-
   dimensional logical Hamiltonian that commutes with those constraints.

This result identifies exact additional assumptions that yield simplicity,
not evidence that the assumptions already follow from the compiler.

## 6. Relation to the actual existing rotor source

This audit also read the source, rather than replacing it by the toy pair:
`local-window-round37/checker.py`, `parent_terms` and `apply_parent`, plus
`clock-interaction-provenance/README.md` and `common-engine-threeway/PROOF.md`.
The actual hopping list includes rotor shifts U_e accompanying fermion
transport; the actual diagonal generator includes (kappa/2) sum E_e^2.
Their noncommutativity [E,U]=U supplies a real operation-level interaction
input in that already DECLARED parent. Existing exact work proves the
nonzero mixed charge term in its double commutator and charge-dependent
transport energy. Those older numerical/analytic suites were not rerun here.

The compiler's scalar quadratic 16-Majorana model and this compact-rotor
parent are not the same representation. The existing provenance audit
already distinguishes them; the missing marking-, charge-, operation- and
energy-preserving identification is not furnished by a factor swap or by
Bell gluing. The present finite no-interaction result does NOT say the
rotor parent has no interactions.

## 7. Decisive next acceptance condition, not another free candidate

A claimed simple completion must exhibit ONE source-defined mixed update
on the actual observable algebra, prove preservation of products, adjoints,
constraints and source markings, and show where its interaction coefficient
and state come from. Its action on at least one local generator must differ
from the independent family permutation. Possible witness: a nonzero
joint-support term like section 4, or the actual rotor's flux-dressed
transport, accompanied by the missing identification.

Merely adding a tensor factor, choosing theta/J, replacing finite symmetry
by all U(4), or labeling a representation index as space fails this gate.
All T1-T8 remain open. No claim about RH, complexity or factorization is made.

## Reproduction

Run `checker.py` with SymPy, normally and under Python `-OO`. All checks use
explicit exceptions. The exact outputs are required to agree; no random
sampling, floating tolerance or optimized-away assertions are used.

Executed in this research round: normal and `-OO` each pass **135 exact
checks**; a subprocess comparison confirms byte-identical JSON output.
`git diff --check` passes for this directory. No source, shared paper,
website, exported file, status ledger or other worker file was edited.
