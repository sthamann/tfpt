# Propagating the one-electric source with a fifth-order remainder

2026-09-07. **NON-RH / conditional, unpromoted theory experiment.** The
executed advance is the addition of both missing fourth-time-order source
contributions to the unchanged parent. This is not a complete gauge solver,
TFPT-selected vacuum, chiral mirror theorem or T1-T8 closure.

## 1. Same parent and an exact partition of the remaining branches

Keep the unrotated compact U(1) parent

\[
H=H_0+V=\frac\kappa2\sum_\ell E_\ell^2+
d\Gamma\begin{pmatrix}A+\beta A^2&\eta A\\\eta A&MI\end{pmatrix},
\qquad A_{xy}=aU_{xy},
\]

with a=1/12, eta=1/2, beta=1/4, kappa=1/100, M=4, Vmag=0. H0 retains the
original low backtracks d_y=beta a^2 deg_ambient(y), the high mass and the
full electric energy. In the cubic interior d=1/96. V contains direct and
nonbacktracking two-step hopping. Couplings and initial states remain
declared model assumptions, not selections derived from TFPT axioms.

The physical readout is n_H,x. Initial E=0 states have exactly one L/H
fermion per site, arbitrary coherent/mixed/entangled species preparations
on a finite patch, and bare-low filling elsewhere. Fixed Gauss background
q_y=1 is preserved. No dressed-state substitution, electric cutoff or
dynamical spatial window is introduced. The fourth matter source still
requires a normal radius-8 cubic neighborhood with original onsite terms;
all subsequent ambient propagation is bounded, not suppressed.

For a gauge coefficient F and a CAR word O, split the exact commutator as

\[
[V,FO]=F[V,O]+[V,F]O.                                      \tag{1}
\]

Call the first branch M (matter) and the second E (electric). These labels
describe terms in the same strong Duhamel identity, not different physical
Hamiltonians. The first branch from c_H,x is always M, with weight g=eta a.
Round41 retained P4 plus the ME source C1, with C1 freely propagated.

There are TWO fourth-time-order omissions: matter propagation of the
cubic ME word (MEM), and the next first-electric branch after two matter
steps (MME). Retain their free propagation explicitly:

\[
Z_{42}=P_4+C_{ME}+C_{MEM}+C_{MME}.                           \tag{2}
\]

The MEE branch is NOT retained. It has two electric phase differences and
is bounded separately beginning at time order five. Higher first-electric
branches and the remaining fifth matter branch also remain in the bound.
Thus (2) is not the full third-interaction Dyson expansion at finite time:
that expansion also contains MEE. It does recover all time coefficients
through order four on the finite-flux initial vectors.

Strong integral identities are used throughout, not norm differentiation
of unbounded rotor generators. In finite ambient volumes H0 is self-adjoint
and V bounded. The relevant framework is discussed by
[Nachtergaele and Sims](https://arxiv.org/html/1410.8174v1); the concrete
branch partition and numerical constants here are model-specific work.
The resulting estimates avoid the extensive norm of V and are uniform
in volume and initial flux. Compatible thermodynamic limits inherit the
expectation inequalities where that dynamics exists; no continuum-limit
construction is supplied by this calculation.

## 2. Phase accounting for both new branches

A phase history has cumulative fluxes r1,r2,r3 during free simplex times
s1,s2,s3; s0 is the free high-source time. Frequencies below multiply these
times in order. Write epsilon_L=d and epsilon_H=M. For a cubic word
O=c_a^dagger c_b c_y, define Delta(O)=epsilon_a-epsilon_b-epsilon_y.

### MEM: propagate the first cubic word

Start with the outer link r1=sigma e_ell. A force monomial with shift p2
produces r2=r1+p2 and O=c_a^dagger c_b c_y. Round41's frequencies are

\[
\alpha_0=\kappa/2-d,\quad \alpha_1=\alpha_0+\kappa r_1\cdot p_2,
\quad \gamma=\kappa|r_2|^2/2+\Delta(O).
\]

Expand [V,O] with the ordinary derivation product rule. The creator leg
uses the TRANSPOSED row, [V,c_a^dagger]=sum_j V_ja c_j^dagger; the two
annihilator legs use -sum_j V_bj c_j. Consequently the creator transport
has the opposite orientation to the stored row. After a leg shift p3,
let r3=r2+p3 and O' be its updated cubic word. The two frequency lists are

\[
f^{MEM}_0=(-M,\alpha_0+\kappa r_1\cdot p_3,
                 \gamma+\kappa r_2\cdot p_3,
                 \kappa|r_3|^2/2+\Delta(O')),\qquad
f^{MEM}_1=f^{MEM}_0+(0,\kappa r_1\cdot p_2,0,0).             \tag{3}
\]

Every later matter shift acts on ALL earlier electric phases. These dot
products cannot be replaced by separate single-link energies.

### MME: electric force after the second matter step

Let the second matter hop take y to j with shift p2, so r2=r1+p2 and the
source word is c_j. A subsequent force monomial w3 U^p3 c_a^dagger c_b
gives r3=r2+p3 and O'=c_a^dagger c_b c_j. Then

\[
f^{MME}_0=(-M,\kappa/2-d+\kappa r_1\cdot p_2,
                 \kappa|r_2|^2/2-\epsilon_j,
                 \kappa|r_3|^2/2+\Delta(O')),\qquad
f^{MME}_1=f^{MME}_0+(0,\kappa r_1\cdot p_3,
                         \kappa r_2\cdot p_3,0).           \tag{4}
\]

Force terms must meet the UNION of the two prefix supports, even if r2
partly or wholly cancels. Testing only final net flux would lose terms.
For nonzero initial flux E, add kappa r_j dot E to both lists at stage j.
The difference between lists is independent of E; no large flux is removed.

Let J3(f;t) be the oriented 3-simplex integral of exp(i sum f_j s_j).
For a MEM path, weight w is the product g w2 w3 with positive creator-leg
sign and negative annihilator-leg sign. For MME take w=-g w2 w3. Both
contributions are

\[
i w\,[J_3(f_0;t)-J_3(f_1;t)]\,U^{r_3}O'.                 \tag{5}
\]

The signs follow from i per Duhamel commutator and the negative first
annihilator row. All raw weights use denominator 576^3 and all frequencies
denominator 2400. Exactly 18792 MEM and 15912 MME paths are enumerated.
Their signed equal-frequency groups are collected without numerical pruning.
They produce 57150 nonzero groups, 139 scalar frequency kernels and 23010
nonzero cubic word/flux coefficients at t=1.

The degree-80 scalar evaluator uses the outward tail
T^3/6 times (T max|f|)^81/81!, T=|t|. The new numerical amplitude error at
t=1 is below 9.427e-51, separate from both the inherited numerical errors
and the physical omitted-source bound. Numerical operator error is applied
on the E0 initial subspace; it does not approximate exp(i theta E) in
operator norm by a polynomial on the entire unbounded electric spectrum.

## 3. An explicit same-parent fifth-order remainder

Use the pinned whole-Fock CAR bounds

\[
C_L=\sqrt{107/2048},\quad C_H=\sqrt{1/96},\quad b=53/288,
\quad \|[V,e^{i\theta\cdot E}]\|\le b|\theta|_1.
\]

For each new path let d_j=(f1_j-f0_j)/kappa for j=1,2,3 and ell_j=|r_j|_1.
Thus d=(r1 dot p2,0,0) for MEM, and d=(r1 dot p3,r2 dot p3,0) for MME.
The difference of scalar phases is bounded by kappa sum |d_j| s_j. The
E-gradient of the remaining coefficient is kappa sum s_j r_j. For the
updated cubic word, the product rule gives

\[
\|[V,c_a^\dagger c_b c_y]\|\le C_a+C_b+C_y.
\]

After one additional Duhamel integral, first moments on the four-simplex
are T^5/5!; diagonal second moments are 2T^6/6!, and mixed second moments
are T^6/6!. Exact sums over the RAW paths, including words that may vanish
on the special initial subspace, give

\[
\begin{aligned}
A&=\sum_p |w_p|\Big(\sum_j|d_j|\Big)(C_a+C_b+C_y)
   =\frac{12745}{13824}C_L+\frac{961}{3456}C_H,\\
B&=\sum_p |w_p|\left[
    \Big(\sum_j|d_j|\Big)\Big(\sum_j\ell_j\Big)
    +\sum_j|d_j|\ell_j\right]
   =\frac{393481}{165888}.
\end{aligned}                                                    \tag{6}
\]

These coefficients are computed from the original full cubic rows, not
fitted to the numerical residual. The six outer orientations give equal
one-sixth contributions. For a specified cubic-subgraph tree with z first
neighbors use z/6 of these conservative full-cubic constants. A partial
tree census cannot replace the full-cubic constants in the bound interface.

The new unexpanded propagation of MEM and MME is bounded by

\[
R_{new}(T)=\frac\kappa{5!}A T^5+\frac{\kappa^2b}{6!}B T^6.        \tag{7}
\]

The first omitted double-electric branch MEE retains Round41's phase bound

\[
R_{EE}(T)=zg\kappa^2b(2S_0+S_L)\frac{T^5}{120},
\qquad S_0=53/144,\quad S_L=37/48.                              \tag{8}
\]

Let M4 and E1,...,E4 denote the pinned Round40 matter and first-electric
budgets. The new total is

\[
\boxed{\|\tau_t(c_{H,x})-Z_{42}(t)\|
\le D_{42}=M_4+E_3+E_4+R_{EE}+R_{new}.}                         \tag{9}
\]

For z<6 scale (7) by z/6 as above. Equivalently, subtract BOTH the old
ME-to-MEM matter-propagation budget and E2 from D41, then add R_new. The
already retained ME source is not added twice, and MEE is not discarded.
Equation (9) is O(T^5). All remaining full evolutions preserve operator
norms, so no extensive V norm, particle-number bound or electric truncation
is needed. The executed bound domain is |t|<=1 and 1<=z<=6.

At T=1, z=6:

| Omitted part | Approximate amplitude bound |
|---|---:|
| Fifth matter branch M4 | 0.000132517773738 |
| Later first-electric branches E3+E4 | 0.000014249704720 |
| First double-electric branch | 0.000000057774924 |
| New cubic matter propagation | 0.000019926111608 |
| New cubic electric propagation | 0.000000060626107 |
| Total D42 | 0.000166811991097 |

This is about 23.5% below D41. The fifth matter branch now supplies about
79% of this bound at t=1; further electric-only work cannot eliminate it.
The positive omitted-double-electric upper bound is not a lower bound on
the actual error and not a theorem that these branches can never cancel.

## 4. Correlation order stays fixed within the one-electric sector

A bilinear CAR commutator is a derivation preserving the number of factors
in a word. All matter propagation before the first E keeps the word linear;
the first E multiplies it by one creator/annihilator pair; every subsequent
M preserves its cubic form. Hence ME, MEM, MME, and arbitrarily many further
matter branches with EXACTLY ONE E remain cubic. This is a structural
statement, not merely a finite enumeration observation.

On exactly-one-fermion/site INITIAL states, the two rightmost annihilators
kill a word when their sites coincide. Otherwise a cubic word either has
three nonzero charge sites (+1,-1,-1), or one hole plus a neutral spectator
site. Unlike the first ME word, the propagated creator may coincide with
EITHER annihilator site; both possibilities are included. Pairing equal
output charge patterns shows that linear-cubic cross terms require at most
two-site species densities, and cubic-cubic terms at most three-site species
densities. Flux equality can only remove contributions. Fock signs are
kept explicitly; no product-state or factorized density ansatz is introduced.
The executed word census gives 12774 distinct candidate words after the
initial-space zero rule, still with maxima two and three.

There is also a uniform absolute convergence bound for the mathematical
sector containing exactly one E and arbitrarily many M branches. Let
mu=77/96 be the maximum absolute one-mode row sum. A path with r>=1 matter
branches before E and k>=0 after E has raw source norm sum at most

\[
zg\kappa S_0\,r^2\mu^{r-1}(3\mu)^k
\frac{T^{r+k+2}}{(r+k+2)!}.                                  \tag{10}
\]

Before E the prefix length sum is at most r^2. Each cubic matter step has
absolute row sum at most 3mu. Summing by n=r+k bounds the coefficient by
n^3(3mu)^(n-1). The ratio of successive resulting majorants is
3mu T (n+1)^3/[n^3(n+3)], which tends to zero. Thus this one-E sector
converges in operator norm uniformly in volume for bounded T. The same
three-site density sufficiency extends to its norm limit, referring to the
collection of triples throughout its growing spatial support, not three
fixed lattice sites.

This all-order sector is NOT numerically evaluated here. The executed
one-E depth stops at three interactions. Its norm convergence does not
turn it into the full dynamics: two-E words can have five CAR factors,
and neither their full resummation nor an exact three-site closure is
proved. The common 4x4/8x8 patch matrices below are response compressions
with bare filling elsewhere, not replacement physical Hamiltonians.

## 5. Evaluated finite-time responses and exact cross-checks

For q=Tr(rho Zhat^dagger Zhat), add the numerical amplitude error to D42
and use the same outward square-root enclosure as Round41. This follows
from the source norm inequality; mixed states follow by purification.
No leading Taylor coefficient is substituted for the finite-time integral.

For the original bare input:

| Time | Conditional full-cubic n_H,x interval |
|---|---|
| 0.01 | [0.00000104152743, 0.00000104152744] |
| 0.1 | [0.00010278180863, 0.00010278187546] |
| 0.5 | [0.00184357232031, 0.00184446167169] |
| 1 | [0.00218195851226, 0.00221323792966] |

For the same neighboring-site Bell preparations (LL-iHH)/sqrt2 and
(LL+iHH)/sqrt2, both with I/2 single-site densities and initial E=0,
the t=0.1 full-parent intervals are respectively

\[
[0.50004282065582,0.50004282531676],\qquad
[0.50004281536577,0.50004282002672].
\]

Their exact rational separation lower bound is greater than 6.29e-10.
Round41's intervals at this time overlap. The new distinction includes
all omitted dynamics and is certified in the cubic bulk under the declared
assumptions, not merely on the small tree benchmarks. It remains a small
mathematical model witness, not an empirical prediction. At t=0.5 and t=1
the Bell intervals still overlap; separation there is not established.

The entire charged edge source matrix independently agrees with direct
full-Hamiltonian expansion through time power four on every E0 input
column. The added fourth coefficient is nonzero. This uses powers of
the full physical 6-state and charged 4-state Hamiltonians, not the branch
decomposition. Whole-family finite-time comparisons additionally use all
four E0 columns of the edge and all eight E0 columns of the three-site tree,
including both full propagator tails and a Frobenius bound on the induced
operator error. Complete 6-, 20- and 3432-state physical Gauss-sector
occupation evolutions independently lie in their respective local bounds.
These trees are benchmarks, not substitutions for the cubic dynamics.

## 6. Cost, evidence class and next obligations

The calculation retains all 140372 inherited linear mode/flux coefficients
and evaluates 34704 new raw paths. On the two-site patch at nonzero times
the combined cubic source has 1711/3025/1755/3013 nonzero output components
per input basis column. Sparse cubic output columns and the unchanged
linear Gram shortcut avoid materializing a full lattice Fock state.
This is real additional enumeration work; no polynomial-cost all-time
solver, overall speedup, proof-assistant certificate or peer review is claimed.

The next same-parent acceptance target is to reduce the now dominant fifth
matter remainder without silently discarding double-electric branches, and
to extend compatible physical observables of the common source functional.
The one-electric grading above gives a way to organize further calculations;
it does not derive a physical vacuum or the parent parameters.

T1-T8 remain open: unconditional structure/dimension selection, charged seam
dictionary, a single selected parent, chiral measure and uniform mirror gap,
continuum/Lorentz/confinement/scattering, internal coupling and flavor
selection, quantum universal spin two, and the unique physical initial
state/common all-readout functional are not supplied by this round.
Only local theory-contract files and experiment catalog/notes are changed.
There is no paper, website, verification ledger or empirical scorecard
promotion, and no commit or push in this research round.
