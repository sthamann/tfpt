# Source symmetries select a hybrid candidate, not a full holographic code

2026-09-12. NON-RH. Exact finite calculation plus conditional algebraic proof.
No new fundamental axiom, physical Gauss law, or T1–T8 completion is claimed.

## Question and premise boundary

Can already present symmetries remove the inaccessible degrees of freedom,
instead of adding a new coupling? We test a SPECIFIED restriction of the
existing finite candidate: Clock-fixed vectors and one anchor character.
The existence of these symmetries does not imply that physical states must
satisfy those restrictions. See [CLOCK_TYPING_AUDIT.md](CLOCK_TYPING_AUDIT.md).

The reconstruction uses the same original source SHA
`5e54c416be72a125a8ce6e235b4300f9f9c2344b3ada796d2dc4c7e2ea01482b`,
reviewed orbit helpers and previously deployed permutation. It does not
rederive the permutation, all compiler representations, or a physical vacuum.
The 256-dimensional Fock space is the finite candidate's standard lift, not
a declared microscopic TOE state space.

## 1. Clock alone leaves a hidden qubit

The accessible one-particle subspace has dimension five and O acts as I there.
The three hidden modes have Clock grades (3,4,2) modulo six and energies

    alpha-g, alpha+sqrt(3)g, alpha-sqrt(3)g.

Use standard number-conserving second quantization with vacuum phase one.
The hidden Clock-fixed occupation states are exactly |000> and |011> in
the mode order (0,+,-). In bitmask notation they are 0 and 6. Their energies
are 0 and 2 alpha. Consequently the Clock-fixed space is

    C^32_accessible tensor span{|vac>,|pair>}  (dimension 64).

Clock invariance alone neither removes the hidden qubit nor uniquely chooses
its state. A ground-state rule and a sign assumption on alpha would be extra
conditions. Invariant density matrices are a different, larger set than
vectors fixed with eigenvalue one; we do not conflate these meanings.

## 2. Add one anchor character as a conditional state restriction

Take the standard Fock phase Gamma(iI)=i^(N_A+N_B). The original real J may
represent its inverse under the complex-coordinate convention; this relabels
the characters and leaves the fixed sector unchanged. Choosing the vacuum
phase-one lift is explicit, not a derived physical implementation or gauge law.

For the fixed character, N_A+N_B=0 modulo four. Inside the Clock-fixed space,
this leaves

    C = (A_0 tensor |vac>) direct_sum (A_2 tensor |pair>),
    A_0 = accessible occupations N_A=0 or 4, dim A_0=1+5=6,
    A_2 = accessible occupations N_A=2, dim A_2=10.

Thus dim C=16. The other three anchor characters also give dimension 16,
with block sizes (6,10), (10,6), (10,6). This dimension is NOT an identification
with another 16-dimensional compiler representation; such an identification
would need its own state/operation-preserving map.

The free number-conserving source Hamiltonian preserves C: it preserves
accessible number, and the two hidden vectors are eigenvectors. This follows
for the whole alpha,g family from the exact one-particle split. It is only
a preservation statement for this Hamiltonian, Clock and anchor; no proof
that all original compiler operations preserve C is supplied.

## 3. Exact boundary channel and the recoverable algebra

In C=A_0 direct_sum A_2, the partial trace has the form

    N([[rho_00,rho_02],[rho_20,rho_22]]) = rho_00 direct_sum rho_22

on the orthogonal accessible number subspaces. It preserves both blocks and
their weights, but erases their off-diagonal coherences. Its image dimension
is 6^2+10^2=136; its kernel dimension is 2*6*10=120 over C.

Compression of the generous accessible algebra End(A) tensor I to C yields
EXACTLY End(A_0) direct_sum End(A_2), not End(C). Hence the boundary-readable
logical algebra in this contract is M6(C) direct_sum M10(C).

For the block-diagonal state family a CPTP reconstruction exists: measure the
orthogonal accessible number block, then append |vac> or |pair> accordingly.
Extend it arbitrarily by a fixed prepared state on the unused accessible
subspace to obtain a trace-preserving channel on all inputs. On general code
states this reconstructs only the dephased state, not the missing coherence.
Physical preparation of that appended state and arbitrary block operations
are NOT source-derived. This is algebraic reconstructability under an upper
bound on access, not a new available apparatus.

Recovering an observable algebra rather than every density-matrix entry is
the standard operator-algebra error-correction distinction:
[Beny–Kempf–Kribs](https://arxiv.org/abs/quant-ph/0608071).
Its application here supplies no gravitational area law or continuum.

## 4. A symmetry-respecting negative control

Let a_4 be the accessible occupation bitmask 15 (four particles), and a_2
the bitmask 3 (two particles). Set

    |L> = |a_4> tensor |vac>,
    |R> = |a_2> tensor |pair>,
    |psi_+> = (|L>+|R>)/sqrt(2),
    |psi_-> = (|L>-|R>)/sqrt(2).

Both states have exact total number FOUR, Clock character one and anchor
character one. They are orthogonal and have identical accessible marginal
1/2(|a_4><a_4|+|a_2><a_2|).

The joint observable F=|L><R|+|R><L| has expectations +1 and -1 respectively.
It commutes with total particle number (thus with parity and the anchor)
and with Clock. It nevertheless requires joint accessible/hidden access.
It is not claimed to be local, elementary, energy conserving or available.

Therefore even imposing exact total-number symmetry does NOT by itself make
this lost relative phase gauge. The full symmetry-compatible joint algebra
contains an observable that detects it. To disregard it physically requires
a further observable restriction derived from the source, not a renaming of
invisibility as gauge. Mere existence of F likewise does not provide access.

## 5. Information-theoretic simplification and its limit

Writing a block-diagonal code state as p rho_0 direct_sum (1-p)rho_2 gives

    S(rho_access) = H_2(p) + p S(rho_0) + (1-p) S(rho_2).

Logs can consistently be natural or base two. The hidden marginal is diag(p,1-p).
For a pure state in C, the accessible/hidden entanglement is H_2(p), at most
one bit. This follows by the two orthogonal Schmidt branches, not by a fit.
The sector probability p is not selected by these symmetries. This finite
entropy split is not an area term: no geometric area or refinement scaling
has been derived. It illustrates a quantum state within each block plus a
classical sector flag, rather than a unique four-qubit quantum code.

## Verification and next gate

`symmetry_code_access.py`: 37 exact checks in normal and -OO execution;
byte-identical JSON. It verifies pinned source modes, all four character
sectors, the partial-trace matrix-unit ranks and the explicit equal-charge
phase witness. The entropy identity and general compression/reconstruction
arguments above are analytic, not separately evaluated numerical experiments.

The remaining fork is concrete:

1. If the original operations only expose the block algebra, derive that
   restriction and use the smaller operational state description. Do not
   claim recovery of missing coherences.
2. If the original source supplies joint phase-reading operations, construct
   them and their preparation/energy/readout contract; arbitrary symmetry-
   compatible matrices are not enough.
3. If a different source-derived code is proposed, test it against all original
   operations. An arbitrary choice of a hidden vector is not unique selection.

Neither branch is decided by this audit. Paper, website, external exports and
T1–T8 status are unchanged.
