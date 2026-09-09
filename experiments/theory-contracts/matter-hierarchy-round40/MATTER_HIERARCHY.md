# A convergent matter-source hierarchy and its separate electric remainder

2026-09-07. **NON-RH / conditional, unpromoted research.** The executed result
is fourth order in matter-source branching, with the mass and free electric
phases retained and all omitted terms bounded. An all-order matter series is
defined and shown to converge, but is NOT numerically evaluated to infinite
order and is NOT the full positive-kappa dynamics. No T1-T8 gate is closed.

## 1. Unchanged physical problem and the intended improvement

Keep the unrotated U(1) parent and preparation from Rounds30/33/37-39:

\[
H=H_0+V=\frac\kappa2\sum_l E_l^2+
d\Gamma\begin{pmatrix}A+\beta A^2&\eta A\\\eta A&M I\end{pmatrix},
\quad A_{xy}=aU_{xy},
\]

with a=1/12, eta=1/2, beta=1/4, kappa=1/100, M=4, Vmag=0. H0 contains the
original low backtracks d_y=beta a^2 deg_G(y) and high onsite mass, as well as
all electric energy. V contains direct and nonbacktracking two-step hopping.
No new parameter choice, field rotation, mirror elimination or dressed-state
substitution is made. These parameters and the preparation remain declared
model inputs, not TFPT-selected physical constants or a selected vacuum.

The target is n_H,x at an ordinary cubic bulk site. Initial states have E=0
and exactly one low/high fermion per site, with arbitrary coherent, mixed or
entangled preparations on a finite patch and bare-low filling elsewhere. The
Gauss sector remains q_y=1. All bulk d_y=1/96. For a finite ambient box, keep
its actual physical boundary onsite terms; choose the target sufficiently
interior that the source paths and onsite coefficients used below are the
cubic ones. At order m their maximum path radius is 2m-1; a normal radius-2m
neighborhood suffices. Subsequent propagation outside this neighborhood is
bounded, not removed by a dynamical window cutoff.

Round39's amplitude remainder at t=1 was approximately 0.00644495, of which
0.00632114 came from further matter iterations. This round computes two more
complete levels and exposes what remains after arbitrarily many matter levels.

Strong Duhamel integration with unbounded onsite generators follows the
careful framework explained by [Nachtergaele and Sims](https://arxiv.org/html/1410.8174v1).
General short-time cluster methods are established, for example in
[Wild and Alhambra](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.020340).
This concrete hierarchy, phase accounting and evaluated error budget are a
model-specific calculation, not a claim to have invented local simulation or
implemented the latter paper's general algorithm.

## 2. Exact branching identity

Let tau and tau0 denote full and H0 evolution. For a bounded source O,

\[
\tau_t(O)=\tau_t^0(O)+i\int_0^t\tau_{t-u}([V,\tau_u^0(O)])\,du.       \tag{1}
\]

For each monomial reached from c_H,x, write its coefficient as F(E,U) times
an annihilator c_j. The commutator splits EXACTLY into

\[
[V,Fc_j]=F[V,c_j]+[V,F]c_j.                                           \tag{2}
\]

Call the first term a matter branch and the second an electric branch.
This naming does not make the second term vanish. It is generally nonlinear
in fermion operators, and cannot be reclassified as another one-particle row.
The coefficient F is a scalar phase times U^r exp(i theta dot E).
[V,U^r]=0 before rotor compression, whereas

\[
\|[V,e^{i\theta\cdot E}]\|\le b|\theta|_1,\qquad b=53/288.            \tag{3}
\]

Use (1)-(2) recursively. Retain all matter branches through m steps. At each
level leave every electric branch in an exact full-evolution remainder.
After level m leave the next matter branch in an exact full-evolution
remainder as well. Let P_m(t) be the retained operator, including free c_H,x.
No electric branch is included in P_m by renaming it; its norm cost is below.

For fixed finite volume, V is bounded, H0 self-adjoint, and these are strong
integral identities. Norm differentiability of the unbounded electric
transport is not assumed. All estimates below avoid the extensive norm ||V||.

## 3. Correct phases at every matter depth

A matter path has modes j_0=(x,H), j_1,...,j_n and link shifts p_1,...,p_n.
Write r_k=p_1+...+p_k, r_0=0. Each matter commutator supplies -w_k, with positive
original hopping weight w_k. During free time s_k after the k-th branch, the
coefficient has E-gradient kappa s_k r_k. Later shifts act on this earlier
phase. They must not be ignored or replaced by independent link energies.

On the E=0 input subspace the resulting scalar frequency is

\[
\lambda_k=\kappa\left(r_k\cdot r_n-\frac{|r_k|_2^2}{2}\right)
-\epsilon_{j_k},\quad k=0,...,n,                                     \tag{4}
\]

where epsilon_L=1/96, epsilon_H=4, so lambda_0=-M. This follows directly from
the free energy change on flux r_n-r_k:

\[
\frac\kappa2\bigl(|r_n|^2-|r_n-r_k|^2\bigr)-\epsilon_{j_k}.
\]

For a nonzero initial E, add kappa r_k dot E. Thus this derivation does not
replace E^2 by a bounded operator. For n=2, (4) exactly reproduces Round39's
alpha=kappa(sigma p_l+1/2)-d and gamma=kappa|r_2|^2/2-epsilon_j.

The n-step coefficient of U^{r_n}c_jn in P_m is

\[
(-i)^n\prod_{k=1}^n w_k
\int_{s_k\ge0,\ \sum_{k=0}^n s_k=t}
\exp\left(i\sum_{k=0}^n\lambda_k s_k\right)\,d^n s.                  \tag{5}
\]

For t<0 use the oriented simplex. The integral is symmetric in its frequencies,
so sorting and grouping equal frequency lists is exact, not a time-ordering
approximation. Equal final mode/flux contributions are added BEFORE squaring.

The inherited rational simplex evaluator integrates the degree-N real-phase
Taylor polynomial, with error at most

\[
\frac{T^n}{n!}\frac{(T\max_k|\lambda_k|)^{N+1}}{(N+1)!},\quad T=|t|.  \tag{6}
\]

All masses and free electric phases are thereby evaluated with a certified
numerical remainder, not replaced by a leading small-time coefficient.

## 4. Two small matrices control the uncomputed hierarchy

The whole-Fock row norms inherited from Round38 are

\[
C_L=\sqrt{107/2048},\qquad C_H=\sqrt{1/96}.                             \tag{7}
\]

For species ordering (L,H), the sums of absolute monomial weights and those
weights multiplied by hop-path length are

\[
W=\begin{pmatrix}53/96&1/4\\1/4&0\end{pmatrix},\qquad
J=\begin{pmatrix}29/48&1/4\\1/4&0\end{pmatrix}.                       \tag{8}
\]

In the low-low entry, the 6 direct paths give 6a and the 30 nonbacktracking
two-step paths give 30 beta a^2; the latter contribute twice to J. The actual
original-parent rows, including all orientations, are independently matched
to the coordinate stencil in the checker. There is no change in Hamiltonian.

For z actual high-source neighbors, start at level one with the row vectors

\[
p_1=q_1=h_1=(z\eta a,0).
\]

Here p_k sums path weights by final species, q_k sums the weights times total
uncancelled hop length, and h_k sums the weights times the sum of all prefix
lengths. For k>=1 propagate

\[
q_{k+1}=q_k W+p_k J,\qquad p_{k+1}=p_k W,\qquad
h_{k+1}=h_k W+q_{k+1}.                                               \tag{9}
\]

These are nonnegative coefficient sums, NOT an effective two-state physical
Hamiltonian. Cancellations of flux paths can reduce actual |r_k|_1; using
uncancelled lengths gives conservative upper bounds without assuming away
any constructive interference.

After a prefix of k matter steps, an electric branch has
theta=kappa sum_{j=1}^k s_j r_j. Equation (3) bounds its norm by
kappa b sum_j s_j |r_j|_1 times the prefix weight. Integrating s_j over the
(k+1)-event simplex gives T^(k+2)/(k+2)!. The sum of these bounds is

\[
E_m(T)=\kappa b\sum_{k=1}^m
(h_k\mathbf1)\frac{T^{k+2}}{(k+2)!}.                                \tag{10}
\]

The remaining matter branch uses (7) on its last annihilator row. Each
preceding coefficient is unitary, so a triangle bound yields

\[
M_m(T)=(p_m\cdot(C_L,C_H))\frac{T^{m+1}}{(m+1)!}.                    \tag{11}
\]

No CAR norm identity is applied across different noncommuting E phases.
Only the last row uses the whole-Fock CAR norm, with its unitary prefix
factored outside. Full evolutions on the unexpanded branches preserve norms.
Consequently, uniformly in ambient volume, particle number and electric flux,

\[
\boxed{\quad\|\tau_t(c_{H,x})-P_m(t)\|\le D_m(T):=M_m(T)+E_m(T).\quad} \tag{12}
\]

These statements first hold in finite ambient volumes. Compatible thermodynamic
limits inherit the expectation bound where the dynamics are constructed. No
continuum, Lorentz, chiral or spectral-decoupling conclusion follows. The same
conservative row bounds apply to cubic subgraph trees with retained onsite d,
using their actual z for the first row. Those are the independent benchmarks.

Equations (9)-(12) recover Round38 EXACTLY for m=1 and Round39 EXACTLY for m=2,
including both of its electric remainder contributions. They are not newly
chosen error constants fitted to the fourth-order numerical result.

At T=1, z=6:

| Matter depth | Matter remainder, approximately | Electric budget, approximately | Total, approximately |
|---|---:|---:|---:|
| 1 | 0.02857175554 | 0.00007667824 | 0.02864843378 |
| 2 | 0.00632114327 | 0.00012380341 | 0.00644494668 |
| 3 | 0.00102126069 | 0.00013585802 | 0.00115711871 |
| 4 | 0.00013251777 | 0.00013805311 | 0.00027057089 |
| 5 | 0.00001432110 | 0.00013835931 | 0.00015268041 |
| 8 | 0.00000000775 | 0.00013839781 | 0.00013840555 |

Only paths through depth FOUR are executed in this round. The later rows are
evaluated bound recurrences, NOT evaluated physical readouts at those orders.

## 5. What can and cannot be resummed to all orders

Let mu=max_i sum_j W_ij=77/96. The n-step matter contribution has operator norm
at most z eta a mu^(n-1) T^n/n!. Hence the series of matter contributions
converges absolutely in operator norm, uniformly in ambient volume for fixed
T, to an operator P_infinity(t). Equation (11) tends to zero.

However, (10) tends to a positive upper-bound BUDGET, not zero. A computable
tail follows from h_k 1 <= z eta a mu^(k-1) k^2: the first path has length one,
subsequent paths at most two, so the sum of prefix lengths is at most k^2.
For the first omitted k=K+1, the ratios of successive majorant terms are

\[
\mu T\frac{(k+1)^2}{k^2(k+3)},
\]

and decrease because both (1+1/k)^2 and 1/(k+3) decrease. A geometric tail
therefore gives an outward rational enclosure. Summing through K=12 gives

\[
0.00013839782796 < E_\infty(1) < 0.00013839782797,
\]

with remainder upper bound <4.476e-15. Thus
||tau_t(c_H,x)-P_infinity(t)|| <= E_infinity(T), but no exact positive-kappa
equality is claimed. **The positive limit is a limit of this certificate's
upper bounds, NOT a lower bound on the true error or an impossibility theorem
for more accurate methods.** Including electric branches can improve it.

Nor does convergence make P_infinity a unitary effective theory or a map
preserving the full CAR algebra. Only at zero electric coupling would the
discarded electric branches vanish and this become the exact static-gauge
quadratic evolution. That limiting observation does not change our kappa=1/100
parent or turn a parameter-zero control into its solution.

There is also an exact small-model witness against silently equating the
matter-only series with full dynamics: on the complete edge Gauss sector,
the third time coefficient of tau_t(c_H,root) applied to the bare state differs
from P_infinity already through the omitted electric branch. Higher matter
orders cannot change a third time coefficient. The independent full-matrix
jet test verifies that this difference is NONZERO, while orders zero, one
and two agree. In the charged basis (L_root,E=-1), (L_leaf,E=0),
(H_root,E=-1), (H_leaf,E=0), the exact third-order difference is

\[
[t^3](\tau_t(c_{H,root})-P_\infty(t))\,\psi_{bare}
=\begin{pmatrix}0\\-i/172800\\0\\-i/345600\end{pmatrix}.               \tag{13a}
\]

It also follows directly from the first omitted term
i eta a kappa sigma U[V,E]c_L/6, with sigma=-1 for the edge source. This
is a concrete limitation of the approximation, not a
physical mirror/TOE no-go theorem.

## 6. Actually evaluated full-bulk readouts and a phase-separation bound

The original coordinate stencil enumerates all prefixes through depth four:

| Depth | Raw paths |
|---|---:|
| 0 | 1 |
| 1 | 6 |
| 2 | 252 |
| 3 | 9,288 |
| 4 | 343,440 |

Combining equal final mode, flux and frequency list gives 229,913 groups.
Exactly 180 scalar frequency kernels suffice at a fixed time. Coherent
collection gives 140,372 complex mode/flux coefficients: 116,935 low and
23,437 high, supported on 575 possible hole sites. This is an operator source
list, NOT a 575-state or 140,372-dimensional physical lattice solver.
No path is sampled or pruned. Genuine cubic plaquette fluxes occur and are
tested; this is not a tree embedding with loops omitted.

The simplex coefficients use degree60. Their exact rational denominators are
combined into one 1007-bit denominator at t=1, then accumulated with Gaussian
integers, not floating-point rounding. Summed numerical amplitude error is
<1.441e-47. A modest list of scalar kernels does not remove the cost of path
enumeration or storing the collected operator coefficients.

For E=0 with one fermion per site, distinct fluxes and distinct hole sites
are orthogonal. At a shared site/flux the low/high components retain their
onsite coherence zeta_j=<c_L,j^* c_H,j>. Thus the Round39 response formula
continues to apply to P4, for every initial density in the stated family:

\[
q_4=\sum_{j,r}\left((1-p_{H,j})|f_{L,jr}|^2+p_{H,j}|f_{H,jr}|^2
+2\operatorname{Re}(\overline f_{L,jr}f_{H,jr}\zeta_j)\right).          \tag{13}
\]

Entanglement between sites is allowed. Dependence only on onsite densities
here is a property of the approximating source norm, not a claim that the
full interacting response never sees intersite correlations. Equation (12)
covers the difference. Combining it with the numerical error epsilon and
outward square roots gives the physical interval

\[
[\max(0,\sqrt{\widehat q_4}-D_4-\epsilon)^2,
\ \min(1,(\sqrt{\widehat q_4}+D_4+\epsilon)^2)].                       \tag{14}
\]

For the bare-low initial state, the actually computed intervals are

| Model time | Full-bulk high occupation |
|---|---|
| 1/10 | [0.00010278013213, 0.00010278349146] |
| 1/2 | [0.00184253098273, 0.00184546515927] |
| 1 | [0.00217210099436, 0.00222283452421] |

At t=1, qhat is approximately 0.002197394550680. The INTERVAL, not that center,
is the controlled answer. Its width improves on Round39 by approximately
24.1651 and on Round38 by approximately 105.083, for the SAME observable,
parent, time and preparation. These are accuracy ratios, not speedup claims.

More importantly, take two inputs with p_H,root=1/2, all other sites bare,
and opposite actual onsite coherences. They share all species occupations
and initial electric fluxes, differing only in the root's relative phase:

| Root coherence | Full-bulk high occupation at t=1 |
|---|---|
| -i/2 | [0.50317655238322, 0.50394456239144] |
| +i/2 | [0.49818165797508, 0.49894584802176] |

These intervals are now disjoint. In exact rational arithmetic their ordering
implies

\[
\langle n_{H,x}(1)\rangle_{\zeta=-i/2}
-\langle n_{H,x}(1)\rangle_{\zeta=+i/2}>0.00423.                       \tag{15}
\]

This is a finite-time, volume-uniform PHASE-SENSITIVITY result for the declared
full cubic parent, conditional on the derivation and preparation assumptions.
It is not inferred by identifying the cubic lattice with the tree benchmark.
It does not select either input as the physical state, reconstruct an entire
source functional, or establish T8. It does rule out treating these two
phase-distinct inputs as the same exact response for this observable.

## 7. Independent checks, costs, and next obligation

The complete edge (6 physical states) and six-leaf star (3432 states) retain
all fluxes fixed by tree Gauss and the original ambient onsite backtracks.
They are not a full cubic lattice and have no independent loop rotors.
Their full uncut probabilities lie inside their corresponding fourth-order
bounds. The full star bare answer remains [0.00219096851702,0.00219096851703].

The entire four-dimensional E=0 physical edge input family is checked via the
Frobenius norm of the full charged-source evolution minus P4, which dominates
its induced operator norm. Both independently computed full-sector unitary
Taylor remainders are included. All coherent superpositions in that family
are covered by this small-model check, not just a few probability samples.
Separate tests check entangled inputs, sorted-Fock signs, source phases on
arbitrarily large positive/negative initial flux, old-round recovery, original
row incidence, all collected path Gauss covariances, cubic loops, direct
high-dimensional simplex integration, exact coefficient collection, tails,
time reversal, invalid domains and pinned source provenance.

All24 new tests and269 predecessor tests from Rounds30-39 pass both normally
and with Python -OO (293 tests per mode). The deterministic record is rebuilt
from the final source hashes; preceding research artifacts are unchanged.

The large source enumeration and storage are real costs. The raw counts grow
rapidly: the fifth level alone would have 12,698,208 paths under direct
enumeration, and is NOT run here. The checker rejects requested path depths
above four; later bound-only rows do not masquerade as executed higher-order
readouts. The independent full-star benchmark additionally performs the
inherited degree100 evolution on its 64,416 Hamiltonian entries. No complete
3D trajectory, thermodynamic state-vector evolution, asymptotic polynomial
algorithm or wall-clock speedup is claimed.

The new fourth-order error is roughly equally split between matter and
electric branches. Pushing only matter depth further has diminishing returns
within this certificate. The next constructive task is to retain the first
nonlinear electric branch explicitly, with its additional fermion correlations
and charged-sector/source bookkeeping, while maintaining a uniform remainder.
It must not be replaced by another chosen effective Hamiltonian or by ignoring
the nonzero commutator.

The full T1-T8 conjunction remains open: axiomatic and seam identification,
unique physical parent/state/parameters, chiral SM and mirror control,
continuum dynamics and spin-two emergence are not delivered here. The written
derivation and finite tests are not proof-assistant formalization or peer
review. This experiment is not empirical evidence and is not promoted to
verification, paper, website or ledger status.
