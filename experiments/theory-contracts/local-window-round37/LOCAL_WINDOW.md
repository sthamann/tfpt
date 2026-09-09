# A spatial window and a full-rotor error budget for the cubic parent

2026-09-07. **NON-RH / unpromoted conditional research theorem.**
This supplies an explicit spatial approximation bound missing from Round33,
and a sharper electric cutoff bound for a different, explicitly flux-supported
preparation class. It does not report an executed large 3D evolution, an
efficient algorithm, a low-energy spectral reduction, or any closed T1-T8 gate.

## 1. Same Hamiltonian; genuinely local preparations

Use the unrotated signed-wall parent from Round30/33 on a finite simple cubic
box or torus (periodic sides at least three), with two fermion modes per vertex
and one unbounded U(1) rotor per oriented nearest-neighbor link:

\[
H=\frac{\kappa}{2}\sum_\ell E_\ell^2+
d\Gamma\begin{pmatrix}A+\beta A^2&\eta A\\\eta A&M I\end{pmatrix},
\qquad A_{yx}=aU_{xy},\quad A_{xy}=aU_{xy}^*.
\tag{1}
\]

Keep a=1/12, beta=1/4, eta=1/2, kappa=1/100, M=4, Vmag=0. These are declared
model choices, not constants or a vacuum selected by TFPT's compiler. All high
fermion modes and all electric fluxes are initially retained in the parent.

The background charge is q_x=1. The bare reference has one low fermion per
vertex and E_l=0 on every link. On a fixed finite patch S replace the occupied
low mode by an arbitrary density on the local one-fermion low/high species
space, leaving the rest of this reference unchanged. Both species have the
same gauge charge. Arbitrary complex superpositions and entangled mixtures
on S therefore stay in the same physical Gauss sector. No global cycle-flux
superposition is required. For four patch sites the input density is 16x16;
it is not four independent classical choices. The initial energy is at most
N/96+M|S| on an N-site degree-six lattice. This is a bounded local excitation
of a specified reference, not the complete low-energy spectral subspace.

This family has exactly E_l=0 initially. It is NOT Round31's dressed filled-Haar
family, whose electric wavefunction has a tail. The new factorial flux bound
below must not be applied to that dressed family without a separate initial-tail
and preparation-error budget. Round33's moment-based result remains valid there.

The spatial part of the theorem is state-independent for bounded even local
observables. The electric and finite-data parts are uniform over this specified
flux-zero family. Choose S and the observable support inside a fixed central
2x2x1 box. The four source types remain meaningful in 3D: high occupation,
an electric-zero projector, onsite species coherence, and the real elementary
square Wilson loop. All are gauge invariant, even and norm at most one.
The square loop replaces the earlier three-site cycle's triangle; it is not
claimed to have the same finite-time numerical answer.

## 2. Exact local interaction bookkeeping and the boundary term

Assign each positively oriented link rotor to its source vertex's cell. A cell
contains its two fermion modes and up to three such rotors. Work in the graded
local fermion algebra: even operators on disjoint supports commute. No nonlocal
Jordan-Wigner string is interpreted as a physical interaction.

Expand A^2 in (1) before either spatial or electric truncation. Backtracking
paths give the onsite term beta a^2 deg_G(x) n_low,x. The remaining terms are:

* One Hermitian direct-link group per edge, with support at its two endpoints
  and norm at most a(1+2 eta)=1/6.
* One Hermitian low-low hopping per unoriented nonbacktracking length-two path,
  with support in its three vertices and norm at most beta a^2=1/576.

The norm statements are on the entire Fock space. For distinct fermion modes
c_i^*c_j plus its adjoint has spectrum in {-1,0,1}; a commuting unitary rotor
transporter does not change this bound. The three direct species hoppings are
bounded by their norm sum. Each path changes a given link flux by at most one.

At a degree-six vertex there are six direct edges, 30 length-two paths where
it is an endpoint and 15 where it is the middle. Thus, writing w_Z for the
individual group norm upper bounds (distinct paths need not have distinct
vertex supports),

\[
j:=\sup_x\sum_{Z\ni x}w_Z
\leq6\frac16+45\frac1{576}=\frac{69}{64}.
\tag{2}
\]

Each support has at most three cells and graph diameter at most two. Every
link belongs to one direct group and at most ten nonbacktracking path groups:

\[
b:=\sup_\ell\sum_{Z\text{ changes }E_\ell}w_Z
\leq\frac16+\frac{10}{576}=\frac{53}{288}.
\tag{3}
\]

Equation (3) agrees numerically with Round33's force bound, but it is established
here as a bound on the flux-changing part itself. A commutator bound alone would
not justify that replacement for arbitrary Hamiltonians.

For a spatial window W, retain the ORIGINAL onsite terms at its vertices and
all path groups wholly supported in W. Delete crossing path groups. In a
regular cubic bulk the onsite low term is always n_low/96, including the window
boundary. Rebuilding A_W+beta A_W^2 instead gives degree_W(x) n_low/576 and
loses the correction

\[
\frac{6-\deg_W(x)}{576}\,n_{low,x}.
\tag{4}
\]

More generally use the actual ambient degree, not six at a physical open edge.
On a one-vertex window the omitted term is n_low/96. It is NOT a harmless scalar
on the allowed low/high preparation family: it changes their relative phase.
Each retained or removed original path is separately gauge invariant. Spatial
selection and the electric projection preserve the full Gauss constraints.
One does not impose new zero boundary-charge sectors on an arbitrary reduced
state. For the declared product-flux preparation, dangling rotors that occur in
no retained interaction stay in E=0 and can be integrated out exactly. Only
internal links need finite rotor state variables in the cost count below.

## 3. Spatial norm estimate without an electric cutoff

The unbounded onsite part is a sum of commuting cell Hamiltonians. Pass to its
interaction picture: each bounded interaction retains its support and norm.
Strongly continuous, bounded interaction-picture generators suffice for the
Duhamel integrals; no norm differentiability of arbitrary rotor observables
under E^2 is assumed. The standard support-commutator recursion can be justified
this way; see [Nachtergaele and Sims, Section 3](https://arxiv.org/html/1410.8174v1#S3).
For the even fermionic interactions the same recursion uses disjoint-support
commutation. The principle of replacing distant dynamics by a neighborhood is
also established in [Barthel and Kliesch](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.108.230504).
The constants, path counts, physical preparation and cutoff composition here
are specific to (1), not new general Lieb-Robinson theory.

Let O have even support X, ||O||<=1, and let W contain the distance-R neighborhood
of X. Compare the full evolution to one with all crossing groups deleted, but
the same onsite terms. A Duhamel integral of commutators with each crossing
group, followed by the support recursion, gives a sum of chains
Z_1,...,Z_n with

\[
Z_1\cap X\ne\varnothing,\quad Z_{i+1}\cap Z_i\ne\varnothing,
\quad Z_n\text{ crossing }W.
\]

Each such chain contributes at most (2T)^n/n! times the product of its n norm
bounds. The first group costs at most |X|j, and each subsequent group at most
3j. A chain reaching outside W must satisfy 2n>R, since each group diameter is
at most two. This yields the explicit uniform bound, T=|t|,

\[
\|\tau_t^G(O)-\tau_t^W(O)\|
\leq\epsilon_{space}(R,T,X)
:=\min\left\{2,\frac{|X|}{3}
 \sum_{n\geq\lfloor R/2\rfloor+1}\frac{(6jT)^n}{n!}\right\}.
\tag{5}
\]

For clarity about factors: the commutator contributes an initial factor two;
each of its n-1 recursive steps another two. The final time integration changes
T^(n-1)/(n-1)! to T^n/n!, giving 2^n, not an extra 2^(n+1). In the n=1 case,
the bound reduces to 2T times the sum of crossing group norms meeting X.
All chain sums are finite-volume sums before taking the uniform upper bound;
positive majorants justify interchanging the sums and integrals.

An axis-aligned bounding box of X, expanded by R in every coordinate, contains
the required graph neighborhood. The window must embed in the ambient lattice
with the declared local coefficients; a wrapped small torus is not substituted
for it. For fixed X,T, (5) tends to zero as R grows. It also makes finite-volume
local evolutions a norm-Cauchy family along compatible cubic exhaustions.
This is a fixed-lattice spatial limit, not a continuum limit, a vacuum
construction or Lorentz invariance. Time continuity on all bounded rotor
operators is not asserted in the operator norm topology.

## 4. A factorial single-link tail independent of every other link

Fix a link ell in the uncut finite window. Split

\[
H_W=H_{pres,\ell}+V_\ell,\qquad
[H_{pres,\ell},E_\ell]=0,\quad\|V_\ell\|\leq b.
\tag{6}
\]

H_pres contains all onsite terms and every group not changing E_ell. It is
self-adjoint as the unbounded diagonal electric operator plus a bounded
finite-volume perturbation. It can include the FULL dynamics on every other
rotor and fermion: its unitary norm is one, regardless of its extensive energy.
Conjugation by that dynamics preserves the property that V_ell changes E_ell
by at most one. Consequently n Dyson factors cannot move an initial
|E_ell|<=K0 vector to |E_ell|>K unless n>=K-K0+1. With

\[
F_m(x):=\sum_{n\geq m}\frac{x^n}{n!},
\]

one obtains the subspace operator bound

\[
\|1_{|E_\ell|>K}e^{-itH_W}1_{|E_\ell|\leq K0}\|
\leq F_{K-K0+1}(bT).
\tag{7}
\]

There is no total-volume interaction norm in (7). This estimate is stronger
than a second-moment Markov estimate only because it assumes exact initial
flux support. It is uniform over arbitrary complex inputs in that support.

## 5. Full finite-window electric compression

Project all r internal window rotors onto |E_l|<=K, with P the joint projection,
Q=1-P and K>=K0. The spectral projections commute, so (7) gives

\[
\|Q e^{-itH_W}P_{initial}\|\leq\sqrt r F_m(bT),
\qquad m=K-K0+1.
\tag{8}
\]

Use H_WK=P H_W P on ran P, compressing the complete expanded Hamiltonian, and
start with the same initial state. There is no initial normalization correction
because P P_initial=P_initial. Only groups changing selected rotor fluxes can
appear in P H_W Q, so ||P H_W Q||<=rb. Projected Duhamel and (8) yield

\[
\begin{split}
\|e^{-itH_W}P_{initial}-e^{-itH_{WK}}P_{initial}\|
&\leq\sqrt r\left[F_m(bT)+rb\int_0^T F_m(bs)ds\right]\\
&=\sqrt r\left[F_m(bT)+r F_{m+1}(bT)\right]=:d_{flux}.
\end{split}
\tag{9}
\]

Both exact evolutions are isometric on the input subspace. Hence any bounded
norm-one observable, compressed as P O P with any free boundary E=0 factors
integrated out, has error

\[
\epsilon_{flux}\leq\min\{2,2d_{flux}\}.
\tag{10}
\]

The vector statements imply all coherent-input bounds, and purification or
convexity supplies arbitrary density matrices. No number of input states
enters (8)-(10). In the recorded case K0=0 and K=12, m=13. Dropping the extra
r F_(m+1) term would discard the projected return-path error.

All tails are enclosed rationally. If x<m+1, use

\[
F_m(x)\leq\frac{x^m}{m!}\frac1{1-x/(m+1)}.
\tag{11}
\]

Otherwise sum finitely up to at least ceil(2x), then apply the same geometric
tail. The checker rounds sqrt(r) upward to an integer. No numerical comparison
of two cutoffs is used as a bound for omitted infinite fluxes.

## 6. Finite computability and explicit, prohibitive costs

For a source box 2x2x1 expanded by R, the finite window has dimensions
(2+2R,2+2R,1+2R). Write N for its vertex count and r for its internal edge count.
A simple unreduced finite Hilbert space has dimension

\[
D_{WK}=4^N(2K+1)^r.
\tag{12}
\]

Gauss and total-charge restrictions reduce this representation, but no cost
reduction for those restrictions or minimal dimension is claimed here. All
high fermions remain. The finite matrix coefficients are rational with the
declared parameters. A conservative whole-Hamiltonian norm bound is

\[
B_{WK}=\frac\kappa2 rK^2+MN+6\beta a^2N
                  +a(1+2\eta)r+15\beta a^2N.
\tag{13}
\]

To specify finite numerical error rather than assume an exact black-box
matrix exponential, divide time into q=max(1,ceil(2 B_WK T)) steps. A degree-p
Taylor polynomial on each step has unitary remainder tau<=2^(-(p+1)). Its
product is not exactly unitary. With mu=q tau<1,

\[
\|U_{WK}(t)-P_p(-itH_{WK}/q)^q\|
\leq(1+\tau)^q-1\leq\frac\mu{1-\mu}=d_{num}.
\tag{14}
\]

This gives epsilon_num=d_num(2+d_num), without renormalizing away an error.
Choose p so mu<=tolerance/8 for tolerance<=1. All arithmetic can be rational
for a supplied rational initial density. Unknown irrational input-data
approximations need an additional preparation error; none is silently assumed.
This is a finite construction and a cost plan, **not an executed solver run**.

At R=64, K=12, T=1, |X|<=4, the checker obtains:

| Quantity | Value or outward bound |
|---|---|
| Window dimensions | 130 x 130 x 129 |
| Vertices N | 2,180,100 |
| Internal rotors r | 6,489,860 |
| Spatial source error | <1.083873e-10 |
| Electric source error | <1.962411e-11 |
| Planned numerical source error | <1.262378e-11 |
| Combined error | <1.406352e-10 |
| Unreduced finite dimension | 4^2180100 times 25^6489860 |
| Base-two dimension bounds | 30,319,640 <= log2(D_WK) <= 36,809,500 |
| Planned exact-polynomial steps | 29,108,451 |
| Polynomial degree per step | 61 |

In particular the combined error is below 1e-9 and is independent of the
ambient lattice volume. The dimension is nevertheless enormous. Even the
unreduced number of amplitudes, not merely their bit precision, is prohibitive.
This is neither a practical runtime claim nor evidence that a full 3D readout
was calculated. The result removes an absent spatial/flux error estimate,
not the computational or spectral problem itself.

## 7. What was actually evaluated and independently checked

The checker enumerates the real cubic graph, oriented link monomials, path
supports and Gauss transitions on open 2x2x2 and 3x3x3 boxes and periodic 3x3x3
and 4x4x4 lattices. The tests include a 5x5x5 periodic incidence check. Their
full-Fock interaction counts agree with (2)-(3). An independent symbolic
Laurent-matrix expansion checks (1), including all backtracks, on the cube.

The uncut sparse H action is also evaluated on the bare reference and an
onsite-flipped reference. In the degree-six bulk the EXACT initial t^2
coefficients are

\[
\begin{array}{c|c}
\text{local observable}&\text{coefficient of }t^2\\\hline
n_{high,x}&1/96\\
1-1_{E_\ell=0}&1/288\\
c_{high,x}^*c_{low,x}+c_{low,x}^*c_{high,x}&1/48
\end{array}
\tag{15}
\]

The initial values of these three observables are zero, and their linear
coefficients vanish. Equation (15) gives derivatives, not finite-time
predictions: no bound on neglected higher coefficients is inferred. An
independent complete second jet on the eight-vertex cube checks the adjoint
shortcut used for the coherence coefficient. All generated states obey Gauss.

Additional checks exercise coherent preparation sectors, support-chain order,
factorial tails, the flux-support margin, boundary correction, a deliberately
too-late spatial/flux tail, nonunitary Taylor product errors, resource counts,
parent-hash rejection, deterministic artifact replay and the budget CLI.
These exact checks support the written analytic argument; they do not amount
to a formal proof assistant derivation, independent peer review or empirical
verification of TFPT.

## 8. Remaining bridge

Compared with Round36 this is a genuinely spatial, ambient-volume-uniform
error result for local preparations. It does NOT transplant the 60-state cycle
generator onto the cubic lattice. A useful next target is a directly evaluated
local-source/connected-cluster or tensor reduction with this same parent,
preparation, source corrections and explicit space/flux/numerical remainders.
Sharper path geometry may shrink the window; it is not by itself a guarantee
against exponential state cost. Genuine spectral mirror elimination, chirality,
parameter and vacuum selection, the continuum limit and spin-two gravity remain
separate open obligations. No T1-T8, TOE, RH, paper, website, ledger or empirical
scorecard status is promoted by this experiment.
