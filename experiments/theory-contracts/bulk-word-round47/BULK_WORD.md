# A controlled cubic evaluation of the resummed-word target

2026-09-07. **NON-RH / conditional, unpromoted theory experiment.**
This round evaluates the bare-low E0 column of Round46's cubic target
with one explicit additional matter layer and an independently bounded
tail for EVERY later matter layer. It does not exactly evaluate the
infinite suffix, supply a new bulk Bell witness, or solve full electric
dynamics or T1-T8. Numerical values and exact error components are in
the deterministic `validation.json`, notably `readout.decimal_interval`.

## 1. Unchanged physical problem and explicit numerical approximation

Keep the compact U(1) parent H=H_E+dGamma(h),

\[
H_E=\frac\kappa2\sum_\ell E_\ell^2,\qquad
h=\begin{pmatrix}A+\beta A^2&\eta A\\\eta A&MI\end{pmatrix},
\quad A_{xy}=aU_{xy},                                      \tag{1}
\]

with a=1/12, eta=1/2, beta=1/4, kappa=1/100, M=4, Vmag=0 and
the original cubic low onsite backtracks d=1/96. No coupling is fitted.
The executed input is uniform bare-low filling, one fermion/site, E0;
the readout is n_H,0 at model time t=1. The calculation is on the full
cubic parent under the inherited dynamical assumptions, not an edge
or a spatial-tree substitute.

Round46's target replaces the final free propagation of the leaves
MEMM, MMEM, MMME and MEE by all subsequent M events. Here the evaluated
source is the Round45 numerical source PLUS exactly one further M
event on each of these four leaves. Call it Z_tilde47. The difference
from the ideal all-M-suffix target Z46 is bounded separately below.
The extra retained terms are MEMMM, MMEMM, MMMEM and MEEM.

This is a finite numerical representation of the resummed target,
not a claim that only one more M event exists. It uses a path-depth
cutoff with an all-later-layer tail, not a hard spatial or electric
cutoff. Every original cubic hop in that retained layer is enumerated.
Round44's independent configuration-exit error for P_infinity is
also retained; the two approximation errors are not conflated.

## 2. Integer grouping before expensive scalar phase evaluation

All 4993824 cubic one-E leaf paths and 6936 two-E leaf paths enter
the seed census. One representative first direction is enumerated,
with multiplicity six for the norm census. In particular, there is
NO initial-space zero-word pruning before the new M event.

For each leg, apply the original V row with a positive, transposed
creator transport or a negative annihilator transport. For new hop
p, every earlier prefix frequency shifts by kappa r_j dot p, and the
new last frequency is kappa |r_final|^2/2+Delta(updated literal word).
All branch signs and both phase differences of the two-E leaf survive.
The five-factor pattern remains creator/annihilator/creator/annihilator/
annihilator. Onsite mass and backtrack phases are not dropped.

The native helper contains ONLY integer geometry, CAR action and
signed grouping. It applies the FINAL updated word to bare filling,
then collects the key

\[
(\text{physical occupation flips},\;\text{final current},\;
  \text{sorted simplex frequencies}).                       \tag{2}
\]

Paths ending in the same physical state and frequency kernel can
cancel exactly. This is not magnitude pruning. The final-output zero
rule is safe because there is no subsequent retained operator action
on that projected output; all omitted action is covered by the
independent raw-census tail. Applying the rule to the SEED word instead
would be incorrect, as Round46's mutant already demonstrated.

The native original hopping rows are independently compared against
Python enumeration. Raw extension counts, active final CAR actions,
groups before/after cancellation and generated data sizes are recorded.
Signed weights use checked 64-bit multiplication/addition, not silent
integer wraparound. A 12-million-group resource guard fails the run
rather than silently dropping terms. Sorted binary output makes the
grouping deterministic. The executable is built from the pinned source
in a task-specific temporary directory; it and intermediate data are
removed when that computation's temporary-directory scope ends.

No floating-point phase evaluation occurs in the native helper.
Python evaluates each distinct n-simplex kernel with exact rational
arithmetic at degree 80 and its outward tail

\[
\frac{T^n}{n!}\frac{(T\max|f|)^{81}}{81!}.                  \tag{3}
\]

Every absolute grouped weight and all restored directions count toward
the error. The prefactor is -i^n times the stored signed weight: -i
for the new n=5 cubic source and -1 for the n=4 five-factor source.
The arithmetic certificate here is for the bare physical column,
not a uniform polynomial approximation on the unbounded E spectrum.

## 3. Relative occupation states and the fermionic rotation sign

Store only finitely many occupation flips from uniform low filling.
A mode is ordered lexicographically by site and then species. In a
sufficiently large odd-side cube with even half-width, the parity of
the number of initially occupied modes preceding (x,y,z,s) is

\[
x+y+z+s\pmod2.                                             \tag{4}
\]

Add the number of earlier occupation flips to obtain the current CAR
parity. Applying a whole literal word produces a finite sorted flip
set and a sign. This is a compressed description of a physical Fock
column. No finite spatial box is used to evolve the dynamics. An
independent complete filled-cube embedding checks (4), including
negative coordinates, creator order and repeated modes.

Restoring six cubic directions requires a FERMIONIC sign, not just
rotating coordinates. Given output flips D, choose a canonical word
with its high-mode creators followed by its low-mode annihilators.
If it acts on bare filling with sign s_D, and its literal rotation
acts with sign s_RD, the physical output rotation factor is
s_RD/s_D. This factor depends only on the output and the rotation,
not the original path. Independent tests compare it with directly
rotating the original three-/five-factor words.

All six images are added to the SAME physical output vectors before
squaring. The inherited linear and free electric terms are evaluated
in this same relative-state convention. Its reconstruction of the
old bare column must agree EXACTLY with the pinned Round45 probability;
this is a regression gate, not a rounded-number comparison.

The current native projection is specialized to bare-low input. It
does not certify new coherent/mixed/entangled BULK readouts. The old
general-patch results remain unchanged, but are not claimed as a
newly executed feature of this projected compiler.

## 4. Bound all remaining matter layers without a false isometry

Use the pinned positive single-leg species matrix

\[
W=\begin{pmatrix}53/96&1/4\\1/4&0\end{pmatrix},\qquad
\mu=77/96,\quad
C_L=\sqrt{107/2048},\quad C_H=\sqrt{1/96}.                   \tag{5}
\]

For literal word degree d=3 or 5, let W_d be the Kronecker sum of W
over its d legs. Creator reversal does not change these absolute cubic
row weights. Let c_sigma be the sum of C_species over the word's legs.
Let a_sigma be the RAW seed weight sum |w| times its scalar electric
phase-difference moment, sorted by the full species pattern sigma.
The native input producer accumulates a before any final-output pruning.
It is a vector of dimension 8 or 32, not a spatial-state truncation.

For the contribution with m>=1 further M events, first enumerate the
previous m-1 events in absolute weight with W_d. Group the LAST event
as the full CAR commutator [V,O]. Its norm is at most c_sigma. Final
free evolution is an automorphism and preserves that norm. Hence

\[
\|C_{leaf,M^m}(t)\|
\le \kappa^k\,a W_d^{m-1}c\,
        \frac{T^{5+m}}{(5+m)!},\qquad k=1\text{ or }2.       \tag{6}
\]

The seed has n+k=5. Its last phase-difference entries are zero; an M
step shifts both old frequency lists equally. The same first/second
simplex moment defining a therefore survives all later matter shifts.
The factorial in (6) includes those seed moments and every extra
time integral. Unbounded free electric phases retain modulus one.

No l2 isometry of the physical CAR reconstruction is used. Such an
isometry is false, as shown in Round46. Instead (6) uses a whole-Fock
CAR commutator at the last step and a positive coefficient census for
all earlier steps. These bounds are uniform in ambient volume and
initial flux. The strong-Duhamel framework is discussed by
[Nachtergaele and Sims](https://arxiv.org/html/1410.8174v1);
the species tensor moment and concrete computation are model-specific.

Since this numerical source retains m=0 and m=1, its suffix error is

\[
\Delta_M(T)\le\sum_{k=1,2}\kappa^k
 \sum_{m=2}^{\infty}a_k W_{d_k}^{m-1}c_k
                         \frac{T^{5+m}}{(5+m)!}.             \tag{7}
\]

The implementation evaluates through m=18. With v=a W_d^18, the
first omitted numerator is bounded by ||v||_1 d C_L. Subsequent
terms have ratio at most d mu T/25, below one for |t|<=1. A rational
geometric tail encloses the rest. Equation (7) begins at time order
seven. As an independent control, it contains the discrepancy between
the one-M approximation and Round46's complete lifted edge resummation
on every E0 edge basis vector, with both numerical errors added.

The m=1 CAR moment a c is also checked against Round45's exact full
cubic A1/A2 constants. This guards species order, the six-direction
factor and any accidental initial-state pruning of the norm census.

## 5. Every error enters the physical bulk interval

Let D46 be the pinned ideal electric bound from Round46. It is still
sixth order because older first-E and MEME/MMEE branches remain
unevaluated. For the executed common bare column,

\[
\|\tau_t(c_{H,0})\Psi-\widetilde Z_{47}(t)\Psi\|
\le D_{46}+\Delta_M+\epsilon_{aux}+\epsilon_{phase},          \tag{8}
\]

where epsilon_aux includes Round44's full configuration-exit source
and its arithmetic error. It can begin at fourth order and is NOT
hidden inside the new seventh-order suffix tail. For q equal to the
exact rational norm square of the computed column, the physical
occupation interval is

\[
\left[\max(0,\sqrt q-\epsilon)^2,
       \min(1,(\sqrt q+\epsilon)^2)\right],                  \tag{9}
\]

with epsilon the entire right side of (8). The record includes each
component, outward decimal endpoints, exact q, the old-column control,
and native/arithmetic resource counts. The regression gate requires
the interval to be narrower than the previous evaluated cubic bare
interval; it does not infer a new interval from a smaller ideal bound
around the OLD numerical center.

This supplies an actually computed, controlled bare-column approximation
to the previously unevaluated cubic target. It is not exact evaluation
of infinitely many M events, full electric evolution, a new bulk Bell
calculation or a state/parameter-selection theorem.

## 6. Reproduction and remaining acceptance gates

The checker pins Round46 and all transitive parents. The deterministic
record hashes this proof, README, checker, tests and native source.
Tests independently cover native zero/one-M grouping, original cubic
rows and prefix phases, complete filled-cube CAR action, rotation
signs, species tensor counts, all-M tail convergence, the complete
edge lift, scalar phase evaluation, negative/zero times, polynomial
degrees, protocol and pin guards, deterministic binary grouping,
full raw seed counts, exact old bulk reconstruction, the complete
new error budget and end-to-end replay.

The native enumeration, generated binary groups, scalar kernels,
exact integer arithmetic, restored physical outputs and the inherited
auxiliary configuration graph are all real costs. They are reported
in `validation.json`; no end-to-end speedup claim is made. The temporary
native files are generated computation artifacts, not new physical
assumptions or external observational data.

Next gates are stronger all-later-M error control or additional retained
layers, a common coherent/mixed bulk column family with the same signed
rotation accounting, and evaluation of the older first-E and MEME/MMEE
branches. Parameter/preparation selection, chiral continuum dynamics,
universal spin-two dynamics and the remaining T1-T8 obligations stay
open. Only local experiments and catalog/continuation notes change;
no public paper, website, verification, ledger, scorecard, proof-assistant
or peer-review status is promoted, and no commit or push is included.
