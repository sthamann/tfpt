# A second matter layer and an exact source compiler quotient

2026-09-08. NON-RH / conditional same-parent experiment. This is not a
complete seventh-order Hamiltonian source or a closure of T1-T8.

## 1. Precisely the next disjoint source family

Keep Round49's original cubic U(1) Hamiltonian, couplings, ambient onsite
terms, Vmag=0 and uniform bare-low E0 preparation. At t=1 the observable
is n_H,0. Neither the model parameters nor this preparation are derived
or selected from the TFPT axioms by this experiment.

For each Round45 one-electric leaf p in {MEMM, MMEM, MMME}, Round49
already contains p and pM. Add exactly pMM, giving

Z50 = Z49 + C_MEMMMM + C_MMEMMM + C_MMMEMM.

Do not replace the other Round49 families. In particular the two-electric
leaf MEE is not given its second M suffix here. Each new source has six
interaction events and one electric phase difference, hence starts at t7.
The complete ideal remainder stays O(t7), because other seventh-order
branches remain. Only the boundary of this new family moves to t8/t9.

## 2. Two exact compiler reductions before further propagation

An original cubic seed stores its literal word (+,-,-), final current r,
integer weight w and two signed frequency branches. Append the empty
prefix r0=0 to the four existing spectral prefixes. A branch can be
represented by

  (literal word, final current, multiset of pairs {(f_j,r_j)}_{j=0..4}).

The scalar simplex integral is symmetric in its frequency arguments.
After any later M transport with cumulative shift s, its five early
frequencies are f_j+24 r_j dot s, in the pinned units 1/2400.
Consequently permutations of WHOLE frequency/prefix pairs remain equal
for every s, and also for arbitrary initial electric spectral values.
The final current is retained separately; it is not inferred from the
last element of the sorted multiset. Sorting frequencies alone before
propagation would be invalid.

The two annihilator legs can additionally be put into canonical order,
with their CAR sign. Equal annihilator modes give the zero operator on
the entire Fock space. The full M derivation commutes with interchange
of these two identical annihilator tensor factors, so it descends to
this antisymmetric quotient. These identities hold before projection
onto any initial state. No tensor-to-Fock norm isometry is assumed.

Group and cancel the resulting signed integer seed classes exactly.
No electric phase is approximated, no small coefficient is discarded,
and no initially vanishing but nonzero operator is removed here.
The raw norm census is still computed BEFORE all these reductions.

## 3. Final-action memoization is not intermediate-state pruning

For a fixed intermediate literal word I, construct the full list of
second-M hops whose FINAL word acts nontrivially on bare-low filling.
This list depends only on I, not on the earlier phases or currents.
It can therefore be cached and reused. A zero action of I itself does
NOT suppress this list: a later hop may reactivate the contribution.

The cache has a fixed size and may be cleared. Cache-off, small-cache
and cached computations must give exactly identical final integer groups.
Only the final-action optimization is preparation-specific; the error
norms and the first two seed reductions are not.

For successive signed current shifts u,v, the old five frequencies become

  f_j + 24 r_j dot (u+v).

The two newly appended frequencies are

  12|r+u|^2 + Delta(I_after_first_M) + 24(r+u) dot v,
  12|r+u+v|^2 + Delta(I_after_second_M).

Creator hops reverse the original gauge transport and have the positive
commutator sign; annihilator hops have the negative sign. The middle
frequency is retained even when the final current cancels.

## 4. Full-H remainder and exact positive moment transport

Use the inherited strong full-H Duhamel defect identity: the outer
propagator is norm preserving and already includes ALL later M/E events.
The distinction between strong and norm differentiation for unbounded
generators matters; the general framework is discussed by
[Nachtergaele and Sims](https://arxiv.org/html/1410.8174v1).
The source identities and constants below are model-specific derivations,
not results asserted by that reference. Inherited infinite-volume and
dynamical assumptions remain conditions of the experiment.

Let a,b,f be the eight-component species tensors of the original raw
one-E leaves: phase moment, phase-gradient moment, and phase moment times
final-current length. The whole-operator zero rule of Round48 may be
used; no initial-space zero rule may be used in these tensors.

Let S_W act as W on each of the three literal legs and sum, with

  W = [[53/96, 1/4], [1/4, 0]].

For current-length weighted original hoppings, use instead

  J = [[29/48, 1/4], [1/4, 0]].

The first low-low entry is (6*48 + 30*2)/576. Thus it includes all
original direct and two-step monomials. One complete M extension obeys

  a' = S_W a,
  f' <= S_W f + S_J a,
  b' <= S_W(b+f) + S_J a.

The inequalities follow from |r+u| <= |r|+|u|; the a identity is exact.
Apply this recurrence twice. With C_L=sqrt(107/2048), C_H=sqrt(1/96),
use outward rational upper bounds for the square roots and define

  A2 = sum_sigma a2_sigma sum_leg C_(sigma_leg), B2 = sum_sigma b2_sigma.

The new direct boundary is

  R_pMMM = kappa A2 T8/8!,
  R_pMME = kappa^2 (53/288) B2 T9/9!.

Hence

  D50 = D49 - R_old_pMM + R_pMMM + R_pMME.

At T=1, the removed bound is 2.230026483626852e-6, the new bounds are
5.437969126778481e-7 and 3.496255669735822e-9, and
D50 = 1.2356578297871707e-6. All other old boundaries, including old
pE/pME and the two-electric, higher-first-E and repeated-E branches,
remain unchanged. Use the inherited z/6 first-degree factor on original
cubic subgraphs, without replacing the global W,J,C by fitted rows.

## 5. Independent dynamical controls and actual bulk evaluation

The complete one-electric fixed-word auxiliary generator of Round46
independently resums every later M event on the original edge. Compare
its exact integer source recurrence with p+pM+pMM on all selected E0
literal coefficients. The new source agrees through order seven and
fails at eight; p+pM already fails at seven. This verifies precisely
the added family, not the entire physical Hamiltonian at order seven.
Separate finite-time bare and two coherent Bell controls use the whole
original physical edge Hamiltonian and the new complete error bound.

The native compiler is also checked against explicit Python enumeration
of two consecutive full original commutators, including nonzero outputs,
creator signs and every intermediate phase. Depth zero and one must
reproduce the old native implementation exactly.

### Direct rational amplitude accumulation

An instrumented complete-stream attempt with separated physical-output/
frequency groups was stopped before completion: at 60000 of 1311090 seed
classes it already held 30969471 groups. No new bulk result came from that
attempt. Its generated temporary stream was removed by normal cleanup.
The initial 1000-seed timing was not representative of this memory growth.

The second representation evaluates each distinct scalar kernel once and accumulates its
EXACT rational polynomial directly by physical output. For n events,
degree N and integer frequencies f_j in units 1/2400, use the common
denominator

  D = (n+N)! 2400^N 576^n.

The integer complex numerator is

  -sum_(m=0..N) i^(n+m) h_m(f) ((n+N)!/(n+m)!) 2400^(N-m).

This is exactly the earlier rational simplex polynomial, not floating
point accumulation or a new approximation scheme. GMP performs arbitrary
precision integer arithmetic. Signed 64-bit path weights have explicit
checked conversion to GMP's signed-long interface on supported 64-bit
Unix platforms. The binary protocol transports signed big-endian integer
magnitudes with bounded lengths; physical keys are emitted in sorted order.

The numerical tail is summed BEFORE cancellation of phase branches at
their final physical outputs. For absolute branch weight w and integer
frequency radius R it is

  |w|/(576^n n!) (R/2400)^(N+1)/(N+1)!.

Thus it can exceed the old grouped arithmetic bound, but remains a safe
enclosure. There is no transfer of the initial-action optimization into
the ideal operator norm bound. Direct and grouped rational amplitudes
are independently required to agree exactly in regression tests.

This direct, unprojected representation also reached its fail-closed
40-million physical-output gate, after the last recorded progress of
851000/1311090 classes. It produced no new probability or interval. Two
replay attempts using the same representation were stopped as well and
are not counted as passing tests.

### Exact proper-cubic orbit sums

The third representation retains the same exact scalar kernels and
absolute tails, but folds completed physical amplitudes in bounded blocks
under the 24 proper signed coordinate permutations G. This step is AFTER
both M derivations and the final bare action, not an intermediate-state
quotient. It does not alter the full-operator remainder census.

The original hopping rows are G-covariant. Rotations preserve species,
the onsite energies, oriented-current dot products and the rooted Round44
configuration ball. The bare-low E0 preparation and root readout are
scalar under this action. For globally sorted flip modes F, rotation gives

  U_g |F,r> = sigma(g,F) |sort(gF),gr>,

where sigma is the parity of the permutation sorting gF. The background
phase sum_x (x1+x2+x3) is unchanged modulo two by signed permutations.
Independent complete CAR action checks verify this cocycle, including
negative phases; it must not be replaced by a bosonic permutation.

Choose a canonical representative of each physical orbit O. If a
stabilizer fixes the representative with sign -1, every G-invariant
column has zero coefficient there. Otherwise define the signed orbit sum

  B_O = sum_(y in O) sigma(y -> rep(O)) a_y.

For a G-invariant complete column, a_y is recovered as its signed
B_O/|O|, so the exact Gram is

  q = sum_O |B_O|^2/|O|.

Interference between ALL old and new families is retained inside the
common B_O before squaring. The physical nonzero-output count is the
sum of |O| over nonzero complete orbit sums, not the number of stored keys.
For a non-invariant column this formula computes only the invariant
projection's norm and is not a valid substitute for its full norm. A
non-invariant singleton regression explicitly detects this failure.

The complete first-+x seed family is invariant under its four-element
stabilizer H. All subsequent original M hops and E phases commute with
H. The six old rotations are representatives for G/H, and the full
six-image source is (1/4) sum_G U_g v. Its orbit sum is therefore exactly
6 B_O(v). This is a linear signed sum, NOT multiplication of a partial
source norm by six. A generic orbit of size 24 with nonzero three-flip
amplitudes independently checks this coset identity.

The native compiler flushes up to one million unprojected physical
amplitudes into exact orbit sums and then clears only that completed
buffer. Opposite-stabilizer contributions vanish by the scalar symmetry
identity; no small coefficients or future-reactivatable words are dropped.
The final rational coefficients are unchanged by block size in explicit
direct-vector comparisons using blocks of 1, 101 and 100000 entries.

Before accepting this representation, regenerate ALL old sources and
require the entire Round49 probability, numerical error and physical
output count to match the pinned column exactly. The baseline-only entry
point performs this check without claiming a new result. The complete
new run repeats it and then adds the new orbit sums at a common integer
denominator. Never attach D50 to the old q49 without evaluating this
changed common column. Passing small orbit controls alone is insufficient.

The baseline-only run has passed: the pinned rational probability, full
numerical error and all 6882808 physical outputs were reproduced exactly
from 286969 nonzero orbit sums (286973 peak), using 1804403 input
contributions. A further nonzero control constructs an H-invariant
original one-E seed, applies both full M commutators, and compares the
orbit result with all six explicitly expanded physical images. Both the
exact probability and nonzero physical-output count agree. These checks
validate the representation, not the still-separate new bulk evaluation.

The final amplitude budget is D50 plus the complete old configuration
and arithmetic errors plus the new scalar-simplex arithmetic tail. The
Round44 configuration error remains and can start at t4. The ideal
time-order statement is not a new order claim for that numerical error.

Integer arithmetic is overflow-checked. Native input and cache sizes,
four million seed classes, 180 million legacy phase groups, 40 million
direct physical outputs, 20 million orbit sums and 200000 exact phase
kernels have explicit fail-closed resource gates. The proposed large
path is the BLOCKWISE ORBIT vector; neither failed representation is a
completed evaluation. Costs report original seeds, canonical
classes, canonical extension slots, nonzero actions, cache activity,
peak orbit keys, buffer entries, orbit flushes and binary sizes.
Canonical slots are NOT raw path counts. Execution outcomes are recorded
separately in the catalog and generated validation, never inferred here.
No end-to-end speedup follows from a small-prefix timing test. Repeated
full runs must stay within the observed machine memory envelope.

## 6. A finite repeated-electric moment lemma (not a new bulk source)

There are nine further weighted-grade-seven words beyond the three added
here: MEEE, MEEMM, MEMEM, MEMME, MMEEM, MMEME, MMMEE, MMMMEM and MMMMME.
The first involves three electric differences. The following helper
extends the old one-/two-difference moment algebra, without asserting
that these sources have been enumerated or evaluated.

For k labelled phase-difference vectors d_ai on n explicit simplex
intervals u_i, and nonnegative current lengths L_i, define

  A_k = sum_assignment product_a |d_a,j_a| product_i m_i!,
  B_k = sum_assignment product_a |d_a,j_a| product_i m_i!
                        times sum_i (m_i+1)L_i,

where m_i counts labels assigned to interval i. The unlisted interval
u0=T-sum_i u_i carries no differences and has exponent zero. Integrating
product_a sum_i |d_ai|u_i gives A_k T^(n+k)/(n+k)!. Multiplication by
sum_i L_i u_i gives B_k T^(n+k+1)/(n+k+1)!. This follows directly from
the [Dirichlet simplex integral, DLMF 5.14.2](https://dlmf.nist.gov/5.14.E2).
It bounds the corresponding finite phase differences after expressing
each as an integral of its derivative; it is not an all-order convergence
theorem for the full Hamiltonian.

An exact subset recurrence processes one interval at a time. Assign a
disjoint subset S of unassigned labels to interval i with weight
w=|S|! product_(a in S)|d_ai|. Update the two accumulated moments by

  A'[used union S] += w A[used],
  B'[used union S] += w (B[used]+A[used](|S|+1)L_i).

The finite implementation supports at most eight differences and sixteen
intervals with explicit guards. Fifteen independent complete assignment
checks cover k=0..4 and n=3,4,5; k=1,2 reproduce the pinned old formulas.
This is a reusable exact algebraic subproblem, not an MEEE bulk readout
and not part of the new pMM numerical column or its claimed error budget.

## 7. Claim boundary

This is conditional local theory research, not a derivation of a chiral
continuum, universal spin two, parameters or preparation. Full electric
dynamics and T1-T8 remain open. There is no new bulk Bell calculation,
proof-assistant certification or empirical validation. Only experiments
and catalog/continuation notes change; no paper, website, verification,
ledger, scorecard, commit or push is included.
