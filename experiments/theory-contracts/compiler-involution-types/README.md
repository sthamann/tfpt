# Two 16D carriers have inequivalent involution types

2026-09-08. Exact finite representation and rank theorem. No TOE/RH
promotion; not a no-go for larger or infinite microscopic embeddings.

## Outcome

The carrier-module conjugation K and a linear sign-reversing reflection of
the coupled Majorana compiler cannot be identified by an invertible map
between their entire sixteen-dimensional spaces. The invariant is simple:

| Object | Actual space | Involution eigenspace dimensions |
| --- | --- | --- |
| K, with any of the four inherited coherent cocycle phases | Irreducible sixteen-dimensional representation of the E8 charge-sign algebra M16(R) | 12+4, or 4+12 after changing overall sign |
| Any involution reversing an invertible Majorana source operator | Sixteen real Majorana mode coordinates, complexified for H=-iA | 8+8 |

The previous positive result remains intact: K preserves the marked
carrier module and changes U_s into U_delta U_s, with a genuine neutral
charge shift. The new result says that equal dimensions and similar
reflection language do not identify these two operator representations.

It also does **not** refute a Boundary-preserving reflection on the second
source. Whether that reflection preserves Boundary is immaterial to the
type obstruction. Work on such witnesses in other sessions is untouched.

## 1. The actual K implementer, not an arbitrary 16x16 involution

Inputs are pinned from [carrier-module-conjugation](../carrier-module-conjugation/README.md).
That source imports the full E8 charge-sign algebra W=L/2L, its normalized
cocycle, and its faithful irreducible real representation rho on sixteen
states. The 256 signed matrices span M16(R).

For a coherent phase p, the automorphism is

    alpha_K(rho(x)) = (-1)^p(x) rho(Kx).

The four allowed character corrections relative to the existing coherent
J and sigma lifts are 0,126,128,254. They are all checked, not selected by
the desired eigenvalue multiplicities. This is not a classification of
every conceivable microscopic phase convention or representation.

Construct the exact matrix

    U = (1/128) sum_x alpha_K(rho(x)) rho(x)^(-1).

The checker verifies directly U^T=U, U^2=I and all 256 identities
U rho(x) U=(-1)^p(x)rho(Kx). Thus the averaging formula is certified by
explicit products, rather than assumed to work as a general recipe.
For the inherited zero-character choice,

    U_K = [rho(0)+rho(1)+rho(102)-rho(103)]/2
        = diag(+,+,+,+,+,-,+,-,+,-,+,-,+,+,+,+).

The minus entries have zero-based indices 5,7,9,11. Therefore
Tr U_K=8 and rank((I+U_K)/2)=12, rank((I-U_K)/2)=4.
All four coherent choices have the same ranks. Multiplying an implementer
by -1 merely exchanges 12 and 4.

There is no overlooked different involutory implementer of the *same*
automorphism in this irreducible representation: the ratio of two
implementers commutes with every rho(x), hence is scalar. After imposing
the involution condition the scalar freedom is only an overall sign.

### Independent character check

On the 256-dimensional algebra, alpha_K is a signed permutation of the
rho(x) basis. Exactly 64 labels are fixed and the signed fixed-point sum
is 64 for each of the four coherent choices. Independently,

    Tr(Ad U_K) = Tr(U_K) Tr(U_K^-1) = (Tr U_K)^2 = 64.

Together with U_K^2=I this gives |Tr U_K|=8. The explicit matrix fixes
the displayed positive sign. Counting fixed labels without their signs
would not establish this invariant.

## 2. The other source and the balanced-involution lemma

The separate source is the unchanged construction prefix of
`experiments/tfpt-discovery/seam_state_derivation_probe.py`. The local
adapter follows the pinned `double-cover-rh-audit-2026-09-08/seam_source.py`
extraction boundary, before Aint_f. It compiles the unmodified source with
`optimize=0`, even when our test process uses `-OO`: the upstream module
hashes its own docstring during import, so an ordinary `-OO` import fails
before construction. This adapter retains the docstring and all upstream
guards; it does not modify the foreign source or disable a failed check.
The legacy source itself is not claimed to be `-OO`-hardened: only this
experiment's guards and verification logic are exercised under `-OO`.
Both full-source and extracted-prefix hashes are recorded. It supplies

    A0 = direct_sum_8 [[0,1],[-1,0]],   B=A_int,
    H(u,t) = -i(u A0+t B).

This is a one-particle Majorana-coordinate construction, not the sixteen
states of the irreducible E8 charge-sign representation above. The
source's five original exact prefix checks are retained in provenance.
A0^2=-I and det A0=1 are exact. The fixed coupled example A0+B/8 is
also verified invertible by an exact rational determinant.

**Lemma.** If T^2=I and an invertible D obeys TD=-DT, then D maps
ker(T-I) bijectively onto ker(T+I). Thus both eigenspaces have equal
dimension. On this entire 16D source, every such T has type 8+8.

This applies to an involution reversing the whole family, since it
must reverse A0, and also to any invertible fixed member separately.
The bare pair swap is an explicit 8+8 witness for A0 but fails to reverse
B; it is not promoted to a symmetry of the coupled family. The newer
Boundary-preserving witness need not be reconstructed for the lemma.

## 3. The exact mismatch and its sharper rank consequences

An invertible intertwiner cannot change eigenspace dimensions. Hence no
invertible whole-space 16D map can take any of the four specified K lifts
to an involution reversing the invertible source. This is stronger than
checking a particular coordinate identification or a Boundary projector.

Two related bounds make useful small kill tests:

1. If a 16D operator D is odd under a 12+4 involution, its matrix in an
   eigenbasis is [[0,A],[B,0]], with A of size 12x4 and B of size 4x12.
   Therefore rank D<=8 and nullity D>=8. A Hermitian example attains
   equality; the checker verifies it exactly. Retyping the invertible
   source as a K-odd Dirac operator cannot evade those eight zero modes.
2. Any linear intertwiner from type 12+4 to type 8+8 has rank at most
   min(12,8)+min(4,8)=12. The test constructs an exact sharp rank-12
   example; it is necessarily noninvertible.

These are algebraic rank statements, not a claim of eight physically
realized particles, chiral generations or massless bands in TFPT.

## 4. Scope and the useful next question

The result concerns the **whole two 16D spaces and the specific carried
linear actions**. It does not exclude a larger common parent, infinite
lattice-charge or field representation, nonreducing compression,
antiunitary map, Bogoliubov transformation, or a different supported
observable dictionary. Such alternatives must be constructed explicitly;
an arbitrary extra tensor factor is not a proved repair.

In particular, a symmetry of a many-body state, a particle-hole
transformation with a transpose, and a complex-linear one-particle
sign-reversing operator are different contracts. They cannot be matched
merely by calling all three K or a double-cover reflection. The genuine
microscopic problem remains the support-preserving charged-field map,
including oscillator factors, domains, adjoints and neutral carry.

The positive next step is to specify **which representation the physical
seam map actually lands in**, and whether it must intertwine conjugation,
particle-hole covariance, or spectral sign reversal. Run the multiplicity
and rank test before a costly search for its matrix entries. No inference
about the full RH trace or its global positivity follows from this finite
typing result. No T1-T8 gate closes.

## Reproduction

Subsequent positive cross-session result:
[primitive C6 clock information in existing Majorana bilinears](CLOCK_READOUT.md).
The source coordinate space has no grades 1 or 5; its exterior square has
four of each. This is an exact operator-algebra possibility, not a selected
physical preparation or a repair of the involution mismatch. Three further
tests per mode verify the census independently on all 120 exterior minors.

From the repository root:

    python3 -B experiments/theory-contracts/compiler-involution-types/checker.py
    python3 -B -m unittest discover -s experiments/theory-contracts/compiler-involution-types -p test_checker.py
    python3 -B -OO -m unittest discover -s experiments/theory-contracts/compiler-involution-types -p test_checker.py

The saved validation record records exact matrices/invariants and source
hashes. Tests include mutated-pin rejection, all four phases, explicit
matrix and signed-character checks, source invertibility, coordinate
change, both sharp rank witnesses, and inference-boundary guards.
Only this experiment directory is owned by this work; no foreign source,
index, paper, website, ledger, commit or push is changed here.
