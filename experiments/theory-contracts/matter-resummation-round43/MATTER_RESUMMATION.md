# Exact matter-row resummation, a closed-loop computation, and its CAR boundary

2026-09-07. **NON-RH / conditional, unpromoted theory experiment.**
The all-order matter sector is represented exactly and evaluated with
certified errors on two trees and a four-site cycle. The full cubic-lattice
resummed readout is NOT evaluated here. Electric branches remain in the
approximation and in a separate nonzero bound. No T1-T8 gate is closed.

## 1. Fixed parent and meaning of the matter sector

Retain the original unrotated compact U(1) parent of Rounds37-42,

\[
H=H_E+d\Gamma(h),\qquad H_E=\frac\kappa2\sum_\ell E_\ell^2,
\qquad h=\begin{pmatrix}A+\beta A^2&\eta A\\\eta A&MI\end{pmatrix}.
\tag{1}
\]

The unchanged declared inputs are a=1/12, eta=1/2, beta=1/4, kappa=1/100,
M=4 and Vmag=0. Original ambient-cubic low onsite backtracks d=1/96 are
retained in the finite comparison graphs. Restrict only the offdiagonal
direct and nonbacktracking two-step hopping to the specified graph. This
is the same convention as the previous tree benchmarks, not a replacement
of the physical cubic lattice by a cycle or a new choice of onsite terms.

Initial E=0 states have exactly one L/H fermion per site, with arbitrary
species coherence, mixture or entanglement on a finite patch and bare-low
filling elsewhere. These remain assumed preparations, not selected vacua.
The physical readout is n_H,0 under H, not an auxiliary particle count.

Round40 defines M and E by the exact commutator partition

\[
[V,Fc_j]=F[V,c_j]+[V,F]c_j. \tag{2}
\]

The matter-only series keeps the first term at every branching and the
full free electric and onsite evolution between branches. It is NOT the
Hamiltonian obtained by setting kappa to zero. The omitted second term
is generally nonlinear in fermions and does not vanish at positive kappa.

## 2. Exact rotor/one-particle representation

Let F be a row of operators on the rotor Hilbert space, initially
F(0)=e_H,0^T. Its matter-only equation is

\[
\dot F=iH_E F-iF(H_E I+h).
\]

Consequently, with K=H_E I+h on rotor times one-particle space,

\[
\boxed{F(t)=e^{iH_Et}e_{H,0}^{T}e^{-iKt},\qquad
P_\infty(t)=\sum_j F_j(t)c_j.} \tag{3}
\]

In finite ambient volume h is bounded and self-adjoint, so K is
self-adjoint on D(H_E I). Equation (3) means the corresponding strong
integral equation; no norm derivative of the unbounded electric generator
is assumed. The absolute matter-path majorant proved in Round40 converges
in operator norm uniformly in volume at bounded time. Its Dyson expansion
therefore identifies (3) with that same series, rather than introducing a
different approximation by numerical resemblance. Compatible limiting
dynamics inherit the bounds where constructed; no continuum or full
infinite-volume gauge-dynamics construction is supplied here. For strong
evolution with unbounded onsite terms, see the framework of
[Nachtergaele and Sims](https://arxiv.org/html/1410.8174v1).

In particular, for the source-row path j0=(0,H),...,jn, shifts p1,...,pn,
prefix r_k=sum_{a<=k} p_a and simplex times s0,...,sn, the left electric
factor in (3) gives on E0 the same frequencies as Round40:

\[
\lambda_k=\frac\kappa2\bigl(|r_n|^2-|r_n-r_k|^2\bigr)
-\epsilon_{j_k}
=\kappa(r_k\cdot r_n-|r_k|^2/2)-\epsilon_{j_k}. \tag{4}
\]

This retains the action of every later shift on every earlier phase.
Dropping e^(+i H_E t) is incorrect: already the low-leaf to high-root
edge coefficient changes at order t^2 by exactly 1/4800. Independent
matrix-power and path-simplex calculations agree for ALL source columns
through order four on both the edge and the cycle. Those finite jets
check the derivation; they are not used in place of the finite-time
error-controlled evaluation of (3).

## 3. Translation reduces the row to two evolved columns

On a homogeneous translation-covariant lattice or periodic graph define

\[
\psi_s(k,\rho;t)=\langle k,H,\rho|e^{-iKt}|0,s,E0\rangle,
\qquad s=L,H.
\]

Translation invariance of K and E0 implies

\[
F_{(j,s),r}(t)=e^{iH_E(r)t}\psi_s(-j,T_{-j}r;t). \tag{5}
\]

Thus just TWO evolved auxiliary columns, one initially L and one initially
H at the origin, determine all coefficients of the single source row.
No sum over many-body configurations appears in this identity. In the
executed oriented four-cycle, T is cyclic relabeling of vertices and edges;
on the homogeneous cubic lattice it is the ordinary spatial translation.
The identity is not asserted for inhomogeneous open boxes or trees.

There is also no hidden volume factor in the reconstruction error on the
declared input class. Suppose column s has l2 error delta_s. The map from
(k,rho) to (j,r) in (5) preserves the sum of squared coefficient errors.
After an annihilator acts on an exactly-one-fermion/site state, distinct
hole sites give orthogonal matter subspaces. For each hole site j, the
local two-column map is bounded by its Frobenius norm, also when the site
is entangled with the rest. Summing these orthogonal output sectors gives

\[
\|(\widetilde P_\infty-P_\infty)\Psi\|
\le\sqrt{\delta_L^2+\delta_H^2}\,\|\Psi\|. \tag{6}
\]

This is an E0, exactly-one-per-site bound, NOT a whole-Fock numerical
operator-error bound. On a tree, where translation is unavailable, the
implementation instead evolves both species columns for each source-site
point-charge background. Equation (6) uses the sum over all 2n column
errors in that case. On a homogeneous graph the bare-state matter-only
readout is exactly the total auxiliary high-species probability for the
column initially L. Electric corrections must still be added to recover
the physical readout within its separate bound.

## 4. Complete Gauss sectors and all winding tails

For a graph with n vertices, let b_i be the fixed reference occupation:
b_i=1 in the physical n-fermion sector; b_i=delta_i,source for an auxiliary
one-particle column. If N_i is the occupation of a Fock mask, Gauss requires

\[
N_i+\operatorname{div}_i E=b_i. \tag{7}
\]

On the rooted star with edges 0 -> j, the unique solution is
E_(0->j)=N_j-b_j. Enumerating every mask with sum N=sum b is therefore
the complete finite Gauss sector, not a selected flux ansatz.

On the oriented cycle 0->1->2->3->0, all solutions are parameterized by
one arbitrary integer winding m=E_3:

\[
E_i=m+\sum_{j=0}^{i}(b_j-N_j)\ (i=0,1,2),\qquad E_3=m. \tag{8}
\]

The physical sector is countably infinite. Only its evaluation is
compressed to |m|<=K; individual edge fluxes are NOT all cut at K. The
other edges have the occupation offsets shown in (8).

Each original offdiagonal V monomial changes m by at most one. Free
electric and onsite propagation preserve m. The sum of absolute hopping
weights in a one-particle row on this cycle is bounded by nu=73/288;
on the p-particle sector ||V||<=p nu by lifting each one-particle term and
the triangle inequality. The bound is independent of m.

Let U_K be the compressed propagator, embedded in the full Gauss space,
with initial winding zero. In its interaction expansion, at least K
hopping events are required to reach the boundary |m|=K before V can
leave it. The Duhamel boundary-source integral is bounded by integrating
p nu times the tail starting at K events. This yields

\[
\|(U(t)-U_K(t))\Psi\|\le B_{p,K}(T):=
\sum_{a=K+1}^{\infty}\frac{(p\nu T)^a}{a!}
\le\frac{(p\nu T)^{K+1}}{(K+1)!}
\frac1{1-p\nu T/(K+2)},\quad T=|t|. \tag{9}
\]

The denominator must be positive. There is no assumed cancellation or
omitted factor of volume in (9). This derivation uses the full unitary
propagator on the left of the residual source, not a finite-section
eigenvalue claim. The numerical interface restricts |t|<=1.

The auxiliary calculation uses K=12 (dimension 200), and the independent
physical four-fermion calculation uses K=16 (dimension 2310). The latter's
all-winding vector tail at t=1 is below 3.767e-15. Finite matrices and the
left scalar electric phases are evaluated by exact rational Taylor
polynomials of degree 140 with explicit outward remainders. If tau is
the finite-matrix propagator error and eta the largest left-phase error,
each auxiliary column has total error

\[
\delta_s\le B_{1,K}+\tau+(1+\tau)\eta. \tag{10}
\]

Equation (6) gives a cycle source numerical error below 4.124e-18. The
translation of a compressed reference column need not respect a cutoff
on the same closing edge in the translated background. This does not
invalidate (5)-(10): they compare embedded vectors in the UNCUT space.
An independent computation of all eight site/species columns agrees
within the two errors. Cutoffs K=8 and K=12 are checked separately as well.

## 5. Retain the electric terms; take the hierarchy limit honestly

Keep the three already evaluated cubic terms of Round42 and replace only
its finite matter row:

\[
Z_{43}=P_\infty+C_{ME}+C_{MEM}+C_{MME}. \tag{11}
\]

For every matter depth m>=4 the same exact Duhamel branch partition gives
M_m plus the first-electric budgets from level three through m, together
with the two unchanged propagated-electric remainders. Let m tend to
infinity. M_m vanishes, but later first-electric branches remain:

\[
\boxed{D_{43}=D_{42}-M_4+
\left(E_\infty-E_4^{\mathrm{total}}\right).} \tag{12}
\]

Use Round40's rational UPPER enclosure of E_infinity, summing through
level 12 with an explicit geometric tail. Removing M4 without adding
the last parenthesis would give an unjustified bound. At T=1 for a cubic
source with six neighbors:

| Contribution | Approximate amplitude bound |
|---|---:|
| Old D42 | 0.000166811991097188 |
| Removed finite matter remainder M4 | 0.000132517773737996 |
| Added later first-electric budgets | 0.000000344713716153 |
| New D43 | 0.000034638931075344 |
| Numerical enclosure tail for E_infinity | 4.476e-15 (upper bound) |

The new bound is about 79.23% smaller; it is a bound on the exact hybrid
source (11), uniform in volume and flux under the predecessor assumptions.
It is NOT a newly evaluated full-cubic probability interval. This round
computes (11) only on the named finite graphs. For those cubic subgraphs,
the inherited conservative constants apply with the actual source degree
z, including the cycle: every row and force path is a subset of the
original bounded-degree cubic census, with the original onsite d kept.

The common patch-response matrices use the same coherent CAR words and
flux matching as Round41. Include (6), the electric numerical tails and
D43 before squaring the amplitude enclosure. Independently evolving the
complete tree sectors or the cycle with (9) encloses the physical readout
inside every reported hybrid interval. The four-site cycle bare-state
hybrid interval at t=1 is [0.00072348740629, 0.00072473021731]; the
independent full-parent interval is
[0.00072410866669, 0.00072410866672]. These are MODEL results for the
finite cycle, not experimental predictions or the full 3D lattice.

## 6. An exact obstruction to declaring the auxiliary row the full theory

Equation (3) implies FF^dagger=I. It does NOT imply that P_infinity is a
canonical full-Fock annihilator. Gauge coefficients commute with fermions
but not necessarily with each other. Direct CAR algebra gives

\[
\{P_\infty,P_\infty^\dagger\}
=I+\sum_{i,j}c_j^\dagger[F_j^\dagger,F_i]c_i. \tag{13}
\]

There is an exact witness even on the declared bare input of the edge,
with one low fermion at each site and E=0:

\[
\boxed{\langle\{P_\infty(t),P_\infty^\dagger(t)\}\rangle_{LL,E0}
=1-\frac{383}{33177600}t^4+O(t^5).} \tag{14}
\]

The checker computes (14) from exact powers of complete four-state
auxiliary matrices, not from subtracting floating-point near-ones.
With modes ordered (L0,L1,H0,H1), only the occupied L1 term contributes
to the fourth-order correction. The companion row-unitarity norm jet
is exactly (1,0,0,0,0).

An independent symbolic calculation also explains the coefficient. Put
g=eta*a and leave a,g,d,M,kappa symbolic. The two point-background matrices
in that same mode ordering are

\[
K_0=\begin{pmatrix}
d&a&0&g\\a&d+\kappa/2&g&0\\0&g&M&0\\g&0&0&M+\kappa/2
\end{pmatrix},\qquad
K_1=\begin{pmatrix}
d+\kappa/2&a&0&g\\a&d&g&0\\0&g&M+\kappa/2&0\\g&0&0&M
\end{pmatrix}.
\]

For a real symmetric K and i!=j, the fourth coefficient of
|exp(-iKt)_ij|^2 is (K^2)_ij^2/4-K_ij(K^3)_ij/3. Subtracting the
K0 adjoint transition L1<-H0 from the K1 direct transition H0<-L1 gives

\[
[t^4]\langle\{P_\infty,P_\infty^\dagger\}\rangle_{LL,E0}
=-\frac{\kappa g^2(M-d)}6. \tag{15}
\]

Thus the defect is tied to electric coupling, interspecies hopping and
the onsite mass difference, not just an unexplained numerical accident
of the pinned constants. For nonzero kappa*g*(M-d) it is already an
obstruction at fourth order. Vanishing of this one coefficient alone is
not an all-orders converse. No parameters are changed in the executed
physical benchmarks to remove it.

Row unitarity alone therefore cannot supply a physical full-Fock unitary
reduction. This is a counterexample to that proposed
identification, not a no-go theorem for TFPT or all possible reductions.
The inherited electric terms recover the previously checked full source
jet through order four; exact all-time CAR preservation of Z43 is NOT
claimed.

## 7. Cost, executed scope, and next proof obligation

The two-column cycle computation uses a 200-state auxiliary matrix;
the independent physical check uses 2310 states and a different cutoff.
These solve DIFFERENT intermediate problems, so their dimensions are
not a demonstrated speedup for exact many-body evolution. Trees use
four columns of dimension four, or fourteen columns of dimension fourteen;
their complete physical comparison sectors have 6 and 3432 states.
Rational denominators and Taylor arithmetic still carry real cost.

The structural advance is the exact all-order matter-row representation
and its actual error-controlled evaluation on a graph with a closed loop.
The next computational obligation is to evaluate the two auxiliary
columns on the full cubic geometry, including independent plaquette
fluxes and a proved spatial/flux tail, then form the SAME hybrid readout.
No such bulk evaluation is hidden in the analytic bound (12). Further
electric propagation, multiple electric branches, compatible additional
observables, and the physical state/parameter/continuum/chiral/gravity
obligations all remain. T1-T8 remain open. No proof-assistant, peer-review,
empirical or complete-TOE claim is made.
