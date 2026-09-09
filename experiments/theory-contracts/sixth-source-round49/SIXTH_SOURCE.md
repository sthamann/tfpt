# Completing the sixth-order ideal electric source

2026-09-08. **NON-RH / conditional, same-parent theory experiment.**
The new source includes MMMME, MEME and MMEE. Its entire E0 edge matrix
agrees with the independent full Hamiltonian through order six, and every
one of these three families is needed there. The ideal cubic error now
starts at order seven. This is not an all-time solution or a T1-T8 closure.

## 1. Physical parent, source and proof boundary

Keep H=H_E+dGamma(h), H_E=kappa sum E_l^2/2 and

\[
h=\begin{pmatrix}A+\beta A^2&\eta A\\\eta A&M\end{pmatrix},
\quad a=1/12,\;\eta=1/2,\;\beta=1/4,\;\kappa=1/100,\;M=4.
\]

Vmag=0 and the ambient cubic low onsite backtrack 1/96 are unchanged.
The executed bulk input is uniform bare-low E0 filling at t=1, and the
readout is n_H,0. These parameters and this preparation are assumptions,
not deductions or selections from the TFPT axioms.

Let Z48 denote the finite ideal source actually approximated in Round47
and directly certified in Round48. Define

\[
Z_{49}=Z_{48}+C_{MMMME}+C_{MEME}+C_{MMEE}.                    \tag{1}
\]

All previous sources, including MEMMM/MMEMM/MMMEM/MEEM, are retained.
The new one-E source has five interaction events and one phase difference;
the two-E sources have four events and two phase differences. Both begin
at time order six. The new literal arities remain three and five.

## 2. General first-electric and next-electric construction

After q initial matter events, store every original hop, cumulative
current r_j, intermediate mode i_j and signed hopping weight. The old
free frequencies, in the pinned units 1/2400, are

\[
f_0=-9600,\qquad
f_j=12(2r_j\cdot r_q-|r_j|^2)-\epsilon(i_j),\quad j=1..q,
\quad\epsilon(L)=25,\;\epsilon(H)=9600.                    \tag{2}
\]

For each original V monomial c_a^dagger U_p c_b with a nonzero dot product
against ANY prefix, the final word is c_a^dagger c_b c_iq and the final
frequency is 12|r_q+p|^2+Delta(word). The two earlier frequency lists differ
by (0,24 r_1 dot p,...,24 r_q dot p,0). Their signs are (+,-).
In the common -i^n convention, the stored weight is
(-1)^(q-1) times the product of all q+1 hopping weights. In particular,
q=4 has a NEGATIVE stored weight. Keeping that sign is essential.

For MEME/MMEE, start with the exact raw MEM/MME path and prepend the new
creator/annihilator pair. Append the new final frequency to each old list;
then duplicate these lists with the shifts 24 r_j dot p and opposite
branch signs. This gives (+,-,-,+). Append zero to the old difference
vector, and store the new prefix-dot vector with a final zero. All old
mass, electric and canceled-prefix information survives. The literal
pattern is (+,-,+,-,-); it is not replaced by normal ordering without
the associated cubic CAR contractions.

An exact incidence index accelerates the force search: every monomial
with a nonzero prefix dot product meets at least one link in that prefix
union. Gather all ORIGINAL monomials incident to those links, then compute
the full dots and retain precisely those with a nonzero result. This is
set-theoretically equal to the earlier complete neighborhood scan.
It is not a truncated spatial row or a substituted Hamiltonian. Tests
compare the two enumerators, including canceled final currents.

## 3. Independent full-H sixth-order check

On the original edge, the complete two-particle Gauss sector has dimension
six and the charged output sector dimension four. Using the original
Hamiltonian matrices H_N,H_Q and annihilator matrix c, the coefficient
after factoring i^p out of e^(iH_Q t)c e^(-iH_N t) is

\[
\sum_{j=0}^p\frac{(-1)^j H_Q^{p-j}cH_N^j}{(p-j)!j!}.       \tag{3}
\]

Independently, each n-event electric path contributes

\[
-\frac{w}{576^n p!}\sum_\nu\sigma_\nu
 h_{p-n}(f_{\nu,0}/2400,...,f_{\nu,n}/2400),                \tag{4}
\]

where h_m is the complete homogeneous polynomial and h_m=0 for m<0.
The linear resummed part uses its independent one-particle auxiliary
sectors, not the physical matrices in (3). The assembled matrices agree
exactly on all four E0 input columns for p=0,...,6. The old source fails
at p=6. Removing ANY of MMMME, MEME or MMEE gives a nonzero sixth-order
matrix discrepancy. The check covers all coherent or mixed combinations
of those four inputs, not only one expectation value.

This finite test is an independent falsification gate, not by itself a
proof for the cubic lattice. The volume-uniform defect argument below
supplies the order statement for the ideal cubic source.

## 4. Seventh-order direct defect, with every boundary retained

Use Round48's full physical Duhamel identity. Its outer propagator is
norm preserving, so a boundary source encloses all subsequent matter
AND electric events. Strong rather than norm differentiation is required
for the unbounded electric generator; see the general framework in
[Nachtergaele and Sims](https://arxiv.org/html/1410.8174v1).
The model-specific source construction and census are not claims from
that reference. All inherited dynamical/thermodynamic-limit assumptions
remain explicit conditions.

The new sources replace two disjoint old budgets: the first-E event after
four matter events, and the old further electric propagation of MEM/MME.
Each new leaf p has two uncomputed children, pM and pE. For the two families
let A_k be the complete raw absolute phase moment times the whole-Fock
CAR row constant summed over literal legs, and B_k the corresponding
phase-gradient moment. Only whole-operator zero seeds may be excluded,
using Round48's separately checked occupancy-consistency rule. Initial
state zero rules are NEVER used in these norms. Raw and safe-reduced
censuses and counts are both recorded.

Since n+k=6, the new boundary bounds are

\[
R_{kM}=\frac{\kappa^k A_k T^7}{7!},\qquad
R_{kE}=\frac{\kappa^{k+1}(53/288)B_k T^8}{8!}.              \tag{5}
\]

The complete new bound is

\[
D_{49}=D_{48}-R_{MMMME,old}-R_{MEME/MMEE,old}
                       +\sum_{k=1,2}(R_{kM}+R_{kE}).       \tag{6}
\]

The next boundary includes MMMMEM, MMMMEE, MEMEM, MEMEE, MMEEM and MMEEE.
In particular the THREE-electric branches MEMEE/MMEEE are bounded in (5),
not silently discarded because the new evaluated sources have at most
two E events. All earlier Round48 boundary terms remain. First-electric
events after five or more initial M events retain their infinite-tail
certificate. Every remaining ideal branch begins at least at T7.
For original cubic subgraphs use the inherited first-degree factor z/6,
without replacing global row constants by a smaller fitted finite census.

Thus D49=O(T7) under the stated assumptions. This does not assert that
the full all-electric hierarchy has been summed or that the unknown
remainder is actually as large as its upper bound.

## 5. Execute the new cubic column rather than moving an old interval

The native helper receives the ENTIRE raw new source stream and groups
only FINAL bare-low physical occupation flips, final current and sorted
scalar simplex frequencies. No further hopping is performed by this helper.
It uses exact checked integer sums, never floating phase estimates or
magnitude pruning. A bounded input protocol and explicit seed/group resource
guards fail closed. The recorded costs include raw seeds, active final
actions, groups before/after exact cancellation and generated binary sizes.

Python then evaluates the distinct scalar kernels with rational degree-80
arithmetic and its outward simplex tail. Each absolute grouped weight
contributes to that error. The error scope is the executed bare-low E0
column, not uniform approximation of all electric spectral values.
Temporary executables and binary streams are generated in task-specific
temporary directories and removed when those scopes exit or unwind.

The whole Round47 physical column is independently regenerated first and
must reproduce its pinned rational probability EXACTLY. The new sources
are then inserted into the same common physical output space. All six
cubic images use the inherited fermionic rotation cocycle and interfere
before squaring. The new rational center is actually calculated; it is
not the old center with D49 attached.

The final interval uses

\[
\epsilon=D_{49}+\epsilon_{config}+\epsilon_{old\ arithmetic}
                         +\epsilon_{new\ arithmetic},
\quad
[\max(0,\sqrt q-\epsilon)^2,\min(1,(\sqrt q+\epsilon)^2)].   \tag{7}
\]

Round44's configuration-exit error remains and can start at T4. Therefore
the new seventh-order IDEAL defect does not make the numerical projected
source sixth-order exact. This distinction is explicit in the record.

Complete edge finite-time readouts, including coherent Bell inputs, are
also compared with independent full physical evolution. They are not
a new cubic Bell calculation: only bare-low input is executed in the bulk.

## 6. Reproduction and open obligations

The deterministic record binds all five sources and the pinned Round48
and transitive parents. Tests cover independent source generators, each
sixth-order omission mutant, all prefix phases and creator signs, native
versus Python physical grouping, original force incidence, complete norm
censuses, boundary accounting, time orders, finite-time physical controls,
the regenerated old center, the new interval and full replay.

This is a higher-order controlled dynamical calculation for the fixed
conditional model, not parameter/preparation selection, a chiral continuum
or universal spin-two emergence. T1-T8 remain open. Subsequent first-E,
matter and repeated-electric branches still need work, as do additional
bulk observables and general initial-state columns. No empirical,
proof-assistant or peer-review status is promoted. Only local experiments
and catalog/continuation notes change; no paper, website, verification,
ledger, scorecard, commit or push is included.
