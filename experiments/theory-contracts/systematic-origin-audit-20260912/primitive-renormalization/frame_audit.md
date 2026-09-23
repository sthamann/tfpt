# Original-source audit: which isotropy is actually selected?

NON-RH, conditional finite model. This note does not select a physical energy,
derive a spacetime or promote T1–T8. All original files are read-only and pinned
in `frame_audit.py`; previous audit artifacts are unchanged.

## Answer

**Equal primitive weights are not forced by the reviewed marked source.** The
actual family cycle and anchor marking allow distinct positive weights J and K.
The original corpus also contains larger carrier automorphism groups; ignoring
those would be a misleading audit. The missing implication is that a particular
one of those groups must act as an **active symmetry of a physical dynamics**.
An algebra automorphism or passive change of chart does not assert that.

The distinction matters: optional isotropy of the four primitive axes selects
equal weights, whereas optional invariance under the larger original S5 acts on
**ten**, not four, primitive/bivector words. These are different assumptions and
give different spectra, despite selecting the same Bell line.

## Original evidence, not previous status summaries

| Source | Exact content and boundary |
| --- | --- |
| `verification/v752_projective_hamming_incidence.py:209,285` | `sig_vec` rotates three coordinate pairs and fixes the fourth. `family_anchor_basis` chooses a length-three orbit and an independent nonzero sigma-fixed anchor. Its `J_vec` is a complex structure, not the energy coefficient J below. |
| `verification/v774_arf_spinor_compiler.py:410` | Family/anchor Gram is the all-ones-off-diagonal matrix over F2. `sig_bits(v)=(v[2],v[0],v[1],v[3])`; `A_BIT=(0,0,0,1)`, `FSIG=(1,1,1,0)`. The frozen refinement additionally uses q(A)=1 and q(FSIG)=0. |
| `verification/v774_arf_spinor_compiler.py:786` | `s7_decomposition` proves Stab(q*) has order120, is S5, and has word orbits1+5+10. The parity lift identifies its ten-word orbit with q*=1. This is a larger algebraic symmetry, not a declared Hamiltonian selection. |
| `verification/v783_two_qubit_clifford.py:1` | Original carrier/stabilizer identification and the full projective two-qubit Clifford group are explicitly present. The source explicitly fences off a physics/matter interpretation. One must not replace this result with the false claim that only C3 exists. |
| `experiments/theory-contracts/compiler-clifford-bridge/checker.py:103,128,155` | Actual four skew-Hermitian generators, separate anchor a=g4 and family volume f=g1g2g3, and their signed family-cycle lift. Both Lorentz and Euclidean Clifford frames are constructed; physical signature is not selected. |
| `verification/v975_dimension_selector_4d.py:1` | Conditional dimensional selector has additional physical assumptions, including canonical gauge kinetic dimensional analysis. It explicitly does not derive those axioms from compiler primitives; it cannot supply the missing energy-isotropy implication. |

This is a targeted audit of these original definitions and certificates, not a
claim to have proved absence of a statement from every file in the repository.
None of the reviewed operational definitions supplies the missing implication.

## Precise conditional quadratic theorem

Let V=C4 with the actual source generators

    g1=i X⊗I, g2=i Z⊗I, g3=i Y⊗X, g4=i Y⊗Z.

On the additionally chosen physical dual pair V⊗bar(V), define

    ai=i gi,  Di=ai⊗I−I⊗ai^T,
    Qi=gi⊗bar(gi),  pi=(I−Qi)/2=Di²/4,
    H(C)=¼ Σij Cij DiDj,  C real symmetric.

C positive semidefinite is sufficient for H(C) positive semidefinite, by a
real factorization into sums of squares. This quadratic ansatz, the dual pair,
and dynamical covariance are **premises**, not source-derived physics.

The map from the ten entries of C to H(C) is injective, checked exactly using
all256 matrix entries. Conjugation by Qk sends Dk to itself and each other Di
to −Di. Thus Qk covariance for all four k kills every off-diagonal Cij. The
actual source lift

    w=(I+g1g2+g2g3+g3g1)/2

cycles the first three differences and fixes the fourth. Combined covariance
therefore gives **exactly**

    C=diag(J,J,J,K),
    H(J,K)=J(p1+p2+p3)+K p4.

For comparison, family covariance alone leaves four real parameters:

    C = [[J,b,b,c], [b,J,b,c], [b,b,J,c], [c,c,c,K]].

The exact constraint ranks are6 (family alone),6 (primitive record operations
alone),8 (both), on a10-dimensional injective quadratic ansatz. This theorem is
not a classification of arbitrary16×16 Hamiltonians or of all admissible
source actions.

The word Bell basis vec(Uv)/2 gives every mismatch syndrome once, hence the
spectrum of H(J,K) is aJ+bK for a=0,1,2,3 and b=0,1, with multiplicity C(3,a).
It follows that positivity is equivalent to J,K≥0, and the common-plus Bell
ground is unique exactly when J,K>0. The gap is min(J,K).

**Explicit underdetermination witness:** H(1,1) and H(1,2) have the same unique
Bell ground, the same gap1, and covariance under every actual primitive dual
record operation and w. Their spectra differ:

    H(1,1): 0^1,1^4,2^6,3^4,4^1
    H(1,2): 0^1,1^3,2^4,3^4,4^3,5^1.

They are not related merely by a common time/energy rescaling. Both are allowed
by the stated marked-covariance conditions; neither is asserted to be the
actual physical source dynamics.

## What added assumption would remove the ratio?

The abstract Spin-frame rotation r=(I+g3g4)/sqrt2 satisfies

    r g3 r†=g4,  r g4 r†=−g3,

and fixes g1,g2. Its dual action R=r⊗bar(r) swaps p3,p4. Consequently

    R H(J,K) R†−H(J,K)=(K−J)(p3−p4).

Additional covariance under this single rotation forces J=K; exact rank rises
from8 to9. No full continuous U4 symmetry is needed for that narrow result.
But r changes the actual anchor a=g4 to −g3, and is not a symmetry preserving
the marked family/anchor data. Adopting its invariance as physical is an extra
principle that deliberately forgets that marking. Equal Clifford lengths alone
do not implement the principle: both witness Hamiltonians use the same
normalized generators throughout.

## The stronger source S5 gives a different natural completion

The original parity lift makes q*(v)=wt(iota(v))/2 mod2. In the ordered four-word
chart, q*=1 comprises the four words of grade1 plus the six words of grade2.
Permuting all five parity-lift slots acts transitively on these ten words. In
particular it does not preserve the four primitive-word support. A single
primitive Bell word has energy3 under H(1,1), whereas a bivector Bell word has
energy2, so equal four-word weights still do **not** give this S5 invariance.

If one instead adds active S5 covariance and a uniform mismatch cost on that
entire source orbit, the resulting finite alternative is

    H10 = Σq*(v)=1 (I−Uv⊗bar(Uv))/2
        = H(1,1) + Σi<j (I−(gi gj)⊗bar(gi gj))/2.

In the complete word Bell basis its eigenvalue is the number of ten-orbit
words with nonzero original binary commutator pairing with the given word:

    0 on the identity line,
    4 on the five nonzero q*=0 words,
    6 on the ten q*=1 words.

Thus H10 has spectrum **0^1,4^5,6^10**, with the same unique Bell ground and a
different dynamical spectrum. Matrix evaluation and independent binary-pairing
enumeration agree on every one of the16 states. An initial draft expected the
two orbit energies in reverse; the exact matrix guard rejected that expectation,
and the separate commutator count identified the error before this note was
finalized. This is not evidence of a renormalization flow selecting H10.

There is also a particularly small exact relation, verified entrywise:

    H10=5 H4−H4²,  where H4=H(1,1).

Indeed Qi commute and Qi²=I, so expanding H4² reproduces all six pair products
QiQj=(gi gj)⊗bar(gi gj). Thus quadratic corrections in this primitive parent
already contain the ten-word completion algebraically. This observation alone
does not specify a correction coefficient, establish a flow to S5 invariance,
or identify a physical time-evolution law.

Full projective Clifford symmetry acts transitively on all15 nonidentity words.
Uniform completion to all15 gives

    H15=8(I−P_Bell),

again checked entrywise. Hence there are distinct conditional levels: marked
quadratic J,K; optional four-axis isotropic H4; optional ten-word S5 completion
H10; optional full-word flat H15. Source existence of the groups does not choose
which of these invariances governs the proposed interaction.

## Earliest missing axiom and next acceptance gate

The first missing axiom is a source operational statement specifying **which
record comparisons must cost the same physical amount, and which markings are
physical versus merely a choice of description**. One then still needs an
interaction/preparation law and a time scale. A passive change of coordinates,
a group-average prescription introduced here, or a shared ground-state line
cannot silently replace that statement.

A decisive next source test must supply an independently defined update/cost
rule and prove its covariance under the proposed extra transformations. It must
reject H(1,2) for a source reason if claiming four-axis equality, and explain why
the ten- or fifteen-word completion is or is not required. Without such a rule,
these exact alternatives demonstrate underdetermination, not a TOE solution.

Finally, representation roles remain distinct: on a physical doubled Hilbert
space the operators above are Hamiltonian/filter candidates, not automatic
trace-preserving cooling maps. On vec(End(V)), their negatives can represent
random-unitary Lindblad generators. Choosing one interpretation does not prove
the other.

## Reproduction

Run `frame_audit.py` with normal Python and with `python -OO`. The source pins,
exact covariance ranks, anisotropy control, complete spectra, S5 orbit, and
full-word completion are90 explicit checks; no `assert` guard is used.
