# The first nonlinear electric source and a correlation-sensitive response

2026-09-07. **NON-RH / conditional, unpromoted theory experiment.** This is a
same-parent local dynamics calculation, not a TFPT vacuum selection, chiral
construction or closure of T1-T8. The new finite-time result is a certified
distinction between two preparations with identical single-site reduced
densities. Its small magnitude and all assumptions are stated below.

## 1. Fixed problem and exact branch being added

Keep the unrotated compact U(1) parent of Rounds30/33/37-40:

\[
H=H_0+V=\frac\kappa2\sum_\ell E_\ell^2+
d\Gamma\begin{pmatrix}A+\beta A^2&\eta A\\\eta A&MI\end{pmatrix},
\qquad A_{xy}=aU_{xy}.
\]

The declared parameters remain a=1/12, eta=1/2, beta=1/4, kappa=1/100,
M=4, Vmag=0. H0 contains the electric energy, high onsite mass and the
ORIGINAL low backtracks d_y=beta a^2 deg_ambient(y). In the cubic interior
d=1/96. V contains direct and nonbacktracking two-step hopping. None of
these choices is derived from the TFPT axioms in this experiment.

The initial class has E=0 and exactly one L/H fermion per site, allowing
arbitrary coherent, entangled or mixed species preparations on a finite
patch and bare-low filling elsewhere. The fixed Gauss background is q_y=1.
The target is the physical occupation n_H,x. Charged annihilators are
intermediate source operators, not additional physical states. Work in
finite ambient volumes with the cubic source neighborhood in the interior;
the inherited fourth matter level needs a normal radius-8 neighborhood.
Propagation outside that neighborhood is bounded, not cut off. All rotor
fluxes and the full Fock space are retained in the operator estimates.

Write tau and tau0 for full and free Heisenberg evolution. Round40 constructed
P4 by four matter branches of

\[
[V,Fc_j]=F[V,c_j]+[V,F]c_j
\]

and kept EVERY electric branch in a separate remainder. The exact first
high-source identity, with g=eta a=1/24, is

\[
\tau_t(c_{H,x})=e^{-iMt}c_{H,x}
-ig\sum_{y\sim x}\int_0^t e^{-iM(t-s)}\tau_s(U_\ell^\sigma c_{L,y})\,ds.
\tag{1}
\]

For one outer link define

\[
P_u=\exp[i\kappa u(\sigma E_\ell+1/2)],\qquad
R_u=e^{-idu}U_\ell^\sigma[V,P_u]c_{L,y}.
\tag{2}
\]

The electric part in the next strong Duhamel integral has coefficient
(-ig)i=+g. Retain its FREE propagation explicitly:

\[
C_1(t)=g\sum_{y\sim x}\int_0^t ds\,e^{-iM(t-s)}
\int_0^s du\,\tau^0_{s-u}(R_u),\qquad Z(t)=P_4(t)+C_1(t).
\tag{3}
\]

The full-versus-free propagation of R_u is not omitted: it is bounded in
Section 3. Later first-electric branches are still retained in their old
remainder. Z is an approximating source, not a new physical Hamiltonian or
an exact closed low-energy theory.

The strong Duhamel framework with unbounded onsite generators is explained
by [Nachtergaele and Sims](https://arxiv.org/html/1410.8174v1). In each finite
volume H0 is self-adjoint and V bounded; the formulas are strong integrals.
Norm differentiability of unbounded electric transport is not assumed.
The estimates below use local force bounds, not the extensive norm of V.
Their explicit constants and evaluated response are this model-specific
calculation, not results quoted from that reference.

## 2. Exact phases and cubic fermion words

For an original parent monomial V_t=w_t U^p c_a^dagger c_b meeting the outer
link, the rotor shift relation gives

\[
[V_t,P_u]=w_tU^p(1-e^{i\kappa u\sigma p_\ell})P_u c_a^\dagger c_b.
\tag{4}
\]

This phase difference must not be set to zero or given the opposite sign.
Let r=sigma e_ell+p and O_t=c_a^dagger c_b c_L,y. On E=0 define

\[
\alpha_0=\kappa/2-d,\quad
\alpha_1=\kappa(1/2+\sigma p_\ell)-d,\quad
\gamma=\kappa|r|_2^2/2+\epsilon_a-\epsilon_b-d.
\tag{5}
\]

The corresponding term in (3) is exactly

\[
gw_t\{J(-M,\alpha_0,\gamma;t)-J(-M,\alpha_1,\gamma;t)\}U^rO_t,
\tag{6}
\]

where J is the symmetric two-simplex integral

\[
J(f_0,f_1,f_2;t)=\int_0^t ds\int_0^s du\,
e^{i[f_0(t-s)+f_1u+f_2(s-u)]}.
\]

For general initial flux E, add kappa sigma E_ell to both alpha values and
kappa r dot E to gamma. Equation (4), and the remainder proof, hold for all
integer fluxes; only the numerical preparation response uses E=0.

Every frequency is an integer over 2400: -M gives -9600, alpha0 gives -13,
alpha1 gives -13+24 sigma p_ell, and gamma gives
12 sum r_ell^2+epsilon_a*2400-epsilon_b*2400-25. Hopping weights are integers
over 576. All 156 paths (six outer links, 26 force monomials per link) are
included. Equal word/flux contributions are summed before forming norms.

The inherited degree-60 rational simplex evaluator has the outward error
T^2/2 times (T max|f|)^61/61!, T=|t|. Both integrals in (6) are bounded
separately, without assuming a cancellation of numerical errors. At t=1
the electric numerical amplitude error is below 9.639e-49. The inherited
matter numerical error is below 1.441e-47. Neither is the physical remainder.

## 3. Uniform remainder: replace the first electric budget

Use the inherited whole-Fock CAR row constants

\[
C_L=\sqrt{107/2048},\quad C_H=\sqrt{1/96},\quad b=53/288,
\qquad \|[V,e^{i\theta\cdot E}]\|\le b|\theta|_1.
\]

For each first source link, direct enumeration of the unchanged parent gives

\[
S_0=\sum_t|w_tp_\ell|=53/144,\qquad
S_L=\sum_t|w_tp_\ell|(1+|p|_1)=37/48.
\tag{7}
\]

The low-low force weight is 29/144 (direct 1/6 plus two-step 5/144), and
the cross-species force weight is 1/6. Thus the product-rule CAR bound for
the cubic word has coefficient

\[
S_C=\sum_t|w_tp_\ell|(C_a+C_b+C_L)
=\frac{15}{16}C_L+\frac16 C_H.
\tag{8}
\]

Indeed ||[V,c_a^dagger c_b c_y]|| <= C_a+C_b+C_L. This uses the exact
derivation product rule; it is not an invalid one-particle norm for a cubic
operator. Under additional free time v, the E-gradient is
kappa(u sigma e_ell+v r). The scalar phase difference in (4) has absolute
value at most kappa |u p_ell|. Since |r|_1 <= 1+|p|_1,

\[
\|[V,\tau_v^0(R_u)]\|
\le\kappa|u|\{S_C+\kappa b(S_0|u|+S_L|v|)\}.
\tag{9}
\]

The actual weighted sum of |r|_1 is 29/72, smaller than S_L; this round
keeps the stated conservative S_L bound. All factors preceding the words
are unitaries, and the full evolutions of unexpanded terms preserve norms.
Strong Duhamel gives

\[
\|\tau_v(R_u)-\tau_v^0(R_u)\|
\le\int_0^{|v|}\|[V,\tau_w^0(R_u)]\|\,dw.
\]

On the nested region 0<=u<=s<=T, 0<=v<=s-u, the integrals of u, u^2 and
uv are respectively T^4/24, T^5/60 and T^5/120. Therefore the new remainder
for z first neighbors is

\[
D_R(T)=zg\left[\frac{\kappa S_CT^4}{24}
+\frac{\kappa^2b(2S_0+S_L)T^5}{120}\right].
\tag{10}
\]

The old first-electric budget was E1=zg kappa b T^3/6. Equation (3) replaces
that branch, so it must be SUBTRACTED, not counted twice:

\[
\boxed{\|\tau_t(c_{H,x})-Z(t)\|
\le D_{41}(T)=D_4(T)-E_1(T)+D_R(T).}
\tag{11}
\]

D4 is the pinned Round40 bound including later electric branches and the
remaining fifth matter branch. This proves a volume-independent, whole-Fock,
all-flux inequality in every compatible finite ambient volume. A constructed
thermodynamic dynamics inherits its expectation bound; this is not a new
continuum-limit existence theorem. The executed domain is |t|<=1, z<=6.
The same conservative constants apply to the specified cubic-subgraph tree
benchmarks with the retained original bulk onsite terms.

At T=1, z=6:

| Quantity | Approximate value |
|---|---:|
| Old amplitude remainder D4 | 0.000270570887988 |
| Removed first electric budget E1 | 0.000076678240741 |
| Added cubic-word propagation remainder | 0.000024093595001 |
| Added electric-phase propagation remainder | 0.000000057774924 |
| Remaining pure matter remainder | 0.000132517773738 |
| Later first-electric branches | 0.000061374873509 |
| New amplitude remainder D41 | 0.000218044017173 |

This is a roughly 19.4% reduction, not complete electric resummation.
Importantly, D41=O(T^4), whereas the removed branch began at T^3.

## 4. Why at most three-site species densities suffice for this response

Project only the INITIAL states to exactly one fermion per site. Do not
project the dynamics to that space. A word c_a^dagger c_b c_y kills this
initial space when b and y have the same site, regardless of species.
The remaining words have a.site != b.site because V is offsite. There are
only two possible charge patterns:

1. If a.site=y.site, the result has one hole at b and a species operation
   on the spectator site y. Its support is at most two sites.
2. If a, b, y have three different sites, the charge pattern is +1 at a,
   -1 at b and -1 at y. Its support is exactly those three sites.

On the input space, an expectation of two source words can survive only
if their output charge patterns match at EVERY site. A linear annihilator
has a single hole, so P4^dagger C1 can only use case 1: at most two sites.
For C1^dagger C1, two case-2 words must share the same three charge sites;
two case-1 words share their hole and can have two different spectators:
again at most three sites. The two cases cannot pair. P4^dagger P4 needs
only one-site densities. Equal electric output flux is an additional
selection rule that can only remove terms.

After this per-site charge projection the surviving operators are even
at each site; any Fock ordering signs are fixed, not hidden state-dependent
strings through other species sites. Thus the expectation of Z^dagger Z
is determined by species reduced densities on at most THREE sites, also
for entangled or mixed initial states. No factorization is assumed. The
checker independently enumerates the charge patterns: 108 distinct candidate
words survive the initial-space zero rule, with maxima two and three.

This is a sufficiency ceiling for THIS APPROXIMATION and initial class.
It is not an exact all-time three-site closure, nor a proof that all
three-site terms survive after every further cancellation. Later electric
iterations can introduce additional correlations.

The executable response is a common Gram matrix

\[
Q_{ij}=\langle Z\psi_i,Z\psi_j\rangle
\]

for a specified patch of zero through three sites, dimension 1 through 8,
with bare filling elsewhere. Bit j selects high on patch[j], in interleaved
site L/H Fock order. These are exact rational matrices for the numerically
evaluated source polynomial, not independent state fits. Arbitrary rational
complex rays and positive trace-one density matrices use the SAME Q. The
4x4/8x8 matrices are not an 8-state replacement for the full bulk Hilbert
space or the general many-site initial class.

For q=Tr(rho Q), the physical interval is

\[
\max(0,\sqrt q-\delta)^2\le\langle n_{H,x}(t)\rangle
\le\min(1,(\sqrt q+\delta)^2),\qquad
\delta=D_{41}+\epsilon_{\rm numerical}.
\tag{12}
\]

For mixed states, apply the same operator bound to a purification. All
square roots and final decimals are rounded outward with rational bounds.

## 5. A restored third coefficient and a nonzero-time correlation witness

On the complete charged edge, the third source coefficient missing from
Round40 was, in basis (Lroot,E-1),(Lleaf,E0),(Hroot,E-1),(Hleaf,E0),

\[
(0,-i/172800,0,-i/345600)^T.
\]

C1 restores it exactly. A separate test expands the full 4x6 rectangular
Liouville operator space through two interactions, rather than the
linear/cubic splitting, and agrees for all four E0 input columns.

There is also a direct full-cubic consequence. Take neighboring sites x,y
and the two declared Bell preparations

\[
|\Psi_s\rangle=(|LL\rangle+i s|HH\rangle)/\sqrt2,\qquad s=\pm1,
\tag{13}
\]

with all other sites bare. Both sites have exactly rho=I/2, zero onsite
coherence, and identical flux data. Every matter-only response is the same
for the two states. Equation (6) begins with -i g kappa w sigma p_ell t^3/6.
In its cross term with c_H,x only zero total flux survives. The reversed
cross-species hopping on the x-y link contributes on the Bell span

\[
[t^3]Q=\frac{i\kappa g^2}{6}
(|LL\rangle\langle HH|-|HH\rangle\langle LL|).
\tag{14}
\]

The CAR sign follows from
c_H,x^dagger c_H,y^dagger c_L,x c_L,y |LL> = -|HH>.
Other zero-flux terms do not contribute an odd coefficient to these states.
The matter response has only even powers on their identical real diagonal
one-site densities. Since the full remainder (11) is O(t^4),

\[
\boxed{[t^3]\langle n_{H,x}(t)\rangle_{\Psi_s}=-s/345600.}
\tag{15}
\]

This is an exact derivative statement, not by itself a finite-time answer.
The explicit phase-integral calculation and (12) additionally give:

| Time | Psi_minus full-parent interval | Psi_plus full-parent interval |
|---|---|---|
| 1/100 | [0.50000043397108, 0.50000043397314] | [0.50000043396529, 0.50000043396736] |
| 1/50 | [0.50000173518060, 0.50000173521415] | [0.50000173513447, 0.50000173516802] |
| 1 | [0.50058462807682, 0.50120190030960] | [0.50058633394510, 0.50120360722931] |

The exact rational lower bounds on minus-phase minus plus-phase responses
are greater than 3.7e-12 at t=1/100 and 1.25e-11 at t=1/50. Both include
ALL omitted operator terms, not just rounding. These are conditional
full-bulk finite-time separations, not tree-only or truncated Taylor-jet
differences. The t=1 intervals OVERLAP; separation there is NOT established.
Short times were chosen to resolve an O(t^3) signal with an O(t^4) bound,
not by changing the Hamiltonian parameters or using experimental data.

Consequently no functional of only the complete collection of initial
single-site species densities and these initial flux data can reproduce
this exact readout for every allowed preparation. A correlation-aware
source response is necessary. This does not select either Bell preparation
as a physical vacuum, and the very small witness is not an empirical claim.

For continuity, the bare t=1 interval becomes
[0.00217694175355, 0.00221782566303], about 1.24 times narrower than Round40.
The previously certified single-site phase separation at t=1 survives.

## 6. Verification, cost and remaining obligations

The implementation reuses all 140372 matter mode/flux coefficients and adds
156 cubic word/flux coefficients. It does not enumerate the full lattice
Fock state. Linear Gram terms use exact one-site selection; sparse electric
outputs and inverse annihilator lookup supply the cross terms. The two-site
patch has 13/37/11/31 nonzero electric output components per basis input.
The large inherited source enumeration remains real offline work; no total
speedup or arbitrary-time polynomial-cost solver is claimed.

Independent checks include the full 24-component Liouville expansion,
full charged edge Heisenberg evolution on all four E0 columns (including
negative time and both propagator tails), direct Fock columns with the
different sorted-mode ordering, complete 6-state edge and 3432-state star
Gauss-sector occupation benchmarks, exact commutator signs, large uncut
fluxes, charge selection, Hermitian/positive density handling, common-matrix
restriction and spectator tests, parent mutation rejection and replay.
These are analytic derivations and executable regressions, not a proof
assistant certificate or independent peer review. Trees remain separate
benchmarks, not substitutions for the cubic lattice.

Relative to the T1-T8 obligations recorded in Round30, this develops a
conditional dynamics tool relevant to T3/T4 and exposes necessary initial
correlation data for T8. It closes none of those gates. Parent/parameter
selection, the microscopic seam dictionary, chiral measure and uniform
mirror decoupling, the 3+1D continuum and scattering, full flavor/coupling
selection, an emergent universal spin-two sector and a uniquely derived
physical state remain open.

The next concrete dynamics target is to propagate this cubic source through
an additional full interaction step and include the next first-electric
branch, preserving the same-parent norm proof and the increasing correlation
order. A further matter-only iteration cannot remove these missing branches.
All resulting response operators must eventually be made compatible with
the common physical source functional; this one observable is not that
complete construction. No verification ledger, paper, website or empirical
scorecard is promoted by this experiment.
