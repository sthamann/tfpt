# A second local source iteration with coherent low-mode feedback

2026-09-07. **NON-RH / conditional, unpromoted research.** A finite-time local
bound for the unchanged model, not a selected TFPT vacuum, physical prediction,
complete lattice trajectory, or closure of T1-T8. The result is a written
derivation with reproducible algebraic/numerical checks, not a proof-assistant
formalization or independent peer review.

## 1. Same parent, preparation and observable

Keep the Round30/33/37/38 unrotated U(1) parent

\[
H=H_0+V=\frac\kappa2\sum_\ell E_\ell^2+
d\Gamma\begin{pmatrix}A+\beta A^2&\eta A\\\eta A&M I\end{pmatrix},
\qquad A_{xy}=aU_{xy},
\]

with a=1/12, beta=1/4, eta=1/2, kappa=1/100, M=4, Vmag=0. These remain declared
model choices, NOT derived physical constants. H0 contains the electric energy
and the original low backtracks d_y=beta a^2 deg_G(y), plus M n_H,y. V contains
the direct and nonbacktracking two-step hopping terms, on the whole Fock space
and all integer electric fluxes. No species rotation or high-mode elimination
is performed.

The target is a bulk site x of the ordinary cubic lattice, with the radius-four
neighborhood unaffected by a physical boundary. Finite open ambient boxes can
grow without changing the bound. Their actual outer onsite degrees remain
unchanged. Near x, all relevant d_y=d=1/96. The 7-cubed graph used below only
enumerates the radius-three source expression, with its ORIGINAL ambient d
retained. It is not a dynamical spatial truncation or a replacement ambient
Hamiltonian. The estimate includes all subsequent propagation outside it.

Initial states have E_l=0 and exactly one low/high fermion per site, q_x=1.
Arbitrary finite local coherent, mixed or entangled species preparations are
allowed, with the bare-low filling elsewhere. This is not the dressed Haar
state of earlier work. The observable remains the physical even operator
n_H,x=c_H,x^*c_H,x. Charged odd annihilators below are intermediate algebraic
operators, not new physical initial vacua.

The argument uses elementary strong Duhamel identities. For the necessary
care with unbounded onsite generators and strong rather than norm integrals,
see [Nachtergaele and Sims](https://arxiv.org/html/1410.8174v1). This work does
not claim to invent a general local simulation method; related short-time
cluster methods are developed by [Wild and Alhambra](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.020340).
Our contribution here is the concrete second source, its model-specific
constants and its evaluated remainder, not a transfer of that paper's general
algorithm to this rotor model.

## 2. Exact source identity and a specified second approximation

Let tau_t and tau_t^0 be the H and H0 Heisenberg evolutions. With
B_xy=U_xy c_L,y and g=eta a,

\[
\tau_t(c_{H,x})=e^{-iMt}c_{H,x}
-ig\sum_{y\sim x}\int_0^t e^{-iM(t-s)}\tau_s(B_{xy})\,ds.                 \tag{1}
\]

Round38 replaced the inner source by tau_s^0(B). To iterate, use the exact
identity, including its sign and time ordering,

\[
\tau_s(B)-\tau_s^0(B)
=i\int_0^s \tau_{s-u}([V,\tau_u^0(B)])\,du.                             \tag{2}
\]

Write U_xy=U_l^sigma, sigma=+/-1, P_u=exp(i kappa u(sigma E_l+1/2)). Since
[V,U_l]=0 on the UNCUT U(1) space, split the commutator into

\[
\begin{split}
L_u&=e^{-idu}U_l^\sigma P_u[V,c_{L,y}],\\
R_u&=e^{-idu}U_l^\sigma[V,P_u]c_{L,y},\\
[V,\tau_u^0(B)]&=L_u+R_u.
\end{split}                                                            \tag{3}
\]

The nonlinear electric-force contribution R_u is generally NONZERO. Define

\[
Z_x(t)=e^{-iMt}c_{H,x}-ig\sum_{y\sim x}\int_0^t e^{-iM(t-s)}
\left\{\tau_s^0(B_{xy})+i\int_0^s\tau_{s-u}^0(L_u)\,du\right\}ds.        \tag{4}
\]

This retains the first low-row feedback with its exact free electric and
species phases. It is not the entire first Duhamel correction: R_u is omitted
WITH an explicit norm allowance. Likewise the subsequent interaction evolution
of L_u is replaced by free evolution WITH a remainder. No electric-force term
is silently declared zero, and no uncontrolled approximation is used in the
eventual probability interval.

## 3. A volume-uniform whole-Fock remainder

The inherited uncut link force and CAR row bounds are

\[
\|[V,E_l]\|\le b=53/288,\qquad
\|[V,c_{L,j}]\|\le C_L=\sqrt{107/2048},\quad
\|[V,c_{H,j}]\|\le C_H=\sqrt{1/96}.                                    \tag{5}
\]

The high row has six cross couplings. The low row has six direct low, six
cross-high, and thirty nonbacktracking two-step monomials. Its Euclidean CAR
norm includes constructive aggregation of the two paths to each diagonal
endpoint; this is the same exact row constant checked in Round38. There is no
particle-number factor. For the SUM OF ABSOLUTE COEFFICIENTS of this low row,

\[
W_L=6a+30\beta a^2=53/96,\quad W_H=6\eta a=1/4,\quad W=77/96.
\]

A term in [V,c_L,y] is -w_j U^{p_j}c_j. Its path has length one or two. Put
r_j=sigma e_l+p_j, keeping cancellations in the actual operator. Then

\[
L_u=-\sum_j w_j e^{-idu}U_l^\sigma P_u U^{p_j}c_j.
\]

Under further free time v, each term is a scalar phase times

\[
U^{r_j}\exp\{i\kappa(u\sigma e_l+v r_j)\cdot E\}\,c_j.                 \tag{6}
\]

All transporter multiplications commute with V. For any real vector theta,
the strong commutator integral and (5) imply

\[
\|[V,e^{i\theta\cdot E}]\|\le b\sum_l|\theta_l|.                       \tag{7}
\]

Apply the product rule to (6). For the annihilator part, bound each unitary
coefficient times [V,c_j] by C_L or C_H, then sum its absolute weight. **Do not
apply a commuting-coefficient CAR identity across distinct E-dependent
phases.** The triangle estimate is sufficient and legitimate. For the phase
part use (7). For u,v>=0 this yields

\[
\|[V,\tau_v^0(L_u)]\|
\le K_2+\kappa b(Wu+W_\ell v),\quad
K_2=W_L C_L+W_H C_H,                                                    \tag{8}
\]

where a simple conservative path-length bound is

\[
W_\ell=12a+90\beta a^2+12\eta a=53/32.                                 \tag{9}
\]

Here |r_j|_1<=1+|p_j|_1. Cancellations actually give weighted length 25/18
per complete cubic row, independently checked, but the certificate uses the
larger 53/32. This modest slack is declared rather than hidden.

Equation (7) also gives ||R_u||<=kappa b u. Subtract (4) from (1), use (2)-(3),
and expand ONLY the difference tau_{s-u}(L_u)-tau_{s-u}^0(L_u) once more by
Duhamel. Unitary conjugations outside the commutators do not enlarge the norm.
Thus each original source has residual at most

\[
\frac{K_2+\kappa b}{2}s^2
+\frac{\kappa b(W+W_\ell)}6s^3.                                       \tag{10}
\]

Integrating the high-source equation, for T=|t|<=1, z=6,

\[
\boxed{\ \|\tau_t(c_{H,x})-Z_x(t)\|\le
D_2(T)=zg\left\{\frac{K_2+\kappa b}{6}T^3
+\frac{\kappa b(W+W_\ell)}{24}T^4\right\}.\ }                          \tag{11}
\]

The same estimates with absolute times handle t<0. Every step can first be
made in a finite ambient volume with bounded V and unbounded self-adjoint H0;
the final expression never uses the extensive ||V||. It is uniform in volume,
electric flux and particle count. Compatible exhaustion limits inherit the
expectation interval wherever those dynamics are constructed. No relativistic
or continuum limit is asserted. Cubic subgraph trees with retained ambient d
also satisfy the conservative constants, with their actual source degree z.

At T=1, outward rational square roots give D2<0.006444946679180. Its parts are

| Contribution | Approximate amplitude bound |
|---|---:|
| Further matter iterations | 0.006321143269650 |
| Omitted electric-force commutator R | 0.000076678240741 |
| Propagation of E-dependent phases in L | 0.000047125168789 |

The old first-source bound was <0.02864843378435. This is a controlled
improvement, not the elimination of the remaining terms.

## 4. Evaluate Z without an environmental state vector

On E=0, (6) reduces to a computable scalar phase times U^{r_j}c_j. For each
original outer link and subsequent low-row path, the exact frequencies are

\[
\alpha_j=\kappa(\sigma p_{j,l}+1/2)-d,\qquad
\gamma_j=\kappa|r_j|_2^2/2-\epsilon_j,
\quad \epsilon_j=d\ (L),\ M\ (H).                                     \tag{12}
\]

The cross term sigma p_j,l and the net squared flux |r_j|_2^2 matter, especially
for backtracking paths. Merely assigning an energy cost to the uncontracted
path length would give the wrong phase. The coefficient of this second path
is -g w_j times

\[
J_j(t)=\int_{u,v\ge0,\ u+v\le t}
e^{-iM(t-u-v)}e^{i\alpha_j u+i\gamma_j v}\,du\,dv.                     \tag{13}
\]

For negative t use the oriented ordered integral from (4). The direct c_H
coefficient is e^-iMt; first-source coefficients are -ig times the analogous
single integral with frequencies (-M,kappa/2-d). The checker evaluates both
using exact rational complex polynomials and a real-phase Taylor remainder.

For m+1 frequencies lambda_0,...,lambda_m, integrate the total-degree-N Taylor
polynomial of the phase over the m-simplex. The result is

\[
\sum_{n=0}^N i^n h_n(\lambda_0,\ldots,\lambda_m)
\frac{t^{n+m}}{(n+m)!},
\]

where h_n is the complete homogeneous polynomial. Its absolute error is at most

\[
\frac{T^m}{m!}\frac{(T\max_j|\lambda_j|)^{N+1}}{(N+1)!}.               \tag{14}
\]

This follows by integrating the scalar real-phase unitary Taylor remainder;
no numerical quadrature or division by possibly coincident frequencies is
required. The mass phase is not replaced by the leading small-time term.

Combine equal (fermion mode, net link-flux) keys BEFORE squaring. For this bulk
source there are six first paths and 252 second paths, collected into 218
mode/flux coefficients: 187 low and 31 high. There are six distinct second-path
frequency pairs. This is a finite list representing Z, not a truncated list of
physical dynamical states. The uncomputed processes are controlled by (11).

## 5. Phase-sensitive response for an entire initial family

For each site j and net flux r, write the two coefficient components as f_L,jr,
f_H,jr. Distinct fluxes are orthogonal on E=0. Distinct hole sites are also
orthogonal for ANY initial density supported on exactly one fermion per site,
including entangled densities. At one hole site, low/high removal vectors need
not be orthogonal: their overlap is an onsite coherence. Therefore

\[
q_2(t)=\operatorname{Tr}(\rho Z^*Z)
=\sum_{j,r}\left\{(1-p_{H,j})|f_{L,jr}|^2+p_{H,j}|f_{H,jr}|^2
+2\operatorname{Re}(\overline{f_{L,jr}}f_{H,jr}\zeta_j)\right\},         \tag{15}
\]

where zeta_j=<c_L,j^* c_H,j>, |zeta_j|^2<=p_H,j(1-p_H,j). This is the exact
response of the approximating operator for every density in the stated family,
not just a list of sampled preparations. It need not be the exact response of
the interacting parent. In particular higher-order dynamics may depend on
intersite correlations that (15) does not resolve; the common remainder covers
that difference rather than declaring such correlations irrelevant.

The checker uses degree60 in (14), giving total amplitude error <1.415e-47 at
t=1 by summing absolute coefficient errors. Call that epsilon_num, and qhat
the rational norm computed with polynomial coefficients. Hilbert-Schmidt norm
triangle and reverse-triangle inequalities give the physical interval

\[
\boxed{\quad
\max(0,\sqrt{\widehat q}-D_2-\epsilon_{num})^2
\le\langle n_{H,x}(t)\rangle\le
\min(1,(\sqrt{\widehat q}+D_2+\epsilon_{num})^2).\quad}                  \tag{16}
\]

Square roots are outward-enclosed on the Round38 integer 10^-24 grid. No
approximate square root is treated as exact.

For the bare-low input this yields the evaluated full-bulk intervals:

| Model time | High occupation interval |
|---|---|
| 1/100 | [0.00000104151769, 0.00000104154382] |
| 1/10 | [0.00010268476697, 0.00010294444741] |
| 1/2 | [0.00178997477322, 0.00192839016833] |
| 1 | [0.00169010920758, 0.00291608976684] |

At t=1, qhat is approximately 0.00226156214951035, but the interval, NOT that
center, is the certified answer. Its width is approximately 4.34853 times
smaller than Round38's [0.00031949062781,0.00565070454854], for the SAME parent,
time, preparation and observable. It still falls far short of Round37's
unexecuted <1e-9 spatial-window accuracy plan; no like-for-like speedup over that
plan is claimed.

For root p_H=1/2 and zeta=+i/2 or -i/2 (all other sites bare), the two qhat
values are approximately 0.498688874805175 and 0.503616730991372. The full
intervals OVERLAP. Thus the new response retains phase information, but these
bounds do not certify an exact phase-dependent separation in the full bulk.
The independent edge benchmark below does resolve such a separation there.

## 6. Independent checks, costs and open obligations

The inherited edge and six-leaf star benchmarks evolve their ENTIRE physical
tree Gauss sector, dimensions 6 and 3432. Every flux allowed by tree Gauss is
included: E_leaf=N_leaf-1, not a chosen flux cutoff. They retain the original
ambient onsite d. A tree has no independent loop rotors and is not the full
cubic lattice. Their role is an independent check of the analytic bound and
phase conventions, not a replacement 3D simulation.

At t=1 the full star bare probability is [0.00219096851702,0.00219096851703];
the edge bare probability is [0.00036097226121,0.00036097226122]. Both are inside
their second-source bounds. The edge sorted-mode rays bare +/- i rootHigh have
full probabilities [0.50058909763542,0.50058909763543] and
[0.49977067776822,0.49977067776823], respectively. In sorted low-all/high-all
mode ordering, the onsite coherence of bare+i phase rootHigh is
i phase (-1)^(n-1)/(1+phase^2); this fermionic sign must not be omitted.

Checks also compare the WHOLE charged source vector
U_(N-1)^* c_H U_N psi against Z psi, using both complete uncentered tree
Hamiltonians and both certified polynomial tails. They separately verify the
zeroth, first and second time jets against full parent matrices; CAR
commutators on arbitrary large positive/negative flux; both electric
orientations; degree/geometry enlargement; actual entangled inputs; and
exact density positivity and phase conventions. Finite tests support the
derivation but are not mistaken for its all-volume norm proof.

An additional independent calculation takes all four E=0 physical input basis
columns of the edge at once. The Frobenius norm of the full charged evolution
minus Z, with both unitary polynomial remainders included, lies below D2 for
z=1. Since it dominates the induced norm, this checks the entire local edge
input family, including every coherent combination. It still is not a
finite-dimensional substitute for the bulk argument. There are 25 new tests
and 244 predecessor tests (Rounds30-38), all passing normally and under -OO.

The production bulk calculation constructs a fixed 7-cubed path enumeration,
not a 4^343 many-body matrix, and reduces to 218 Gaussian-rational coefficients.
At degree60 it uses one direct, one single-integral and six cached
double-integral frequency lists per time, plus rational coefficient collection,
onsite response sums and integer square roots. This has no ambient-volume
state-vector cost. The full-sector benchmark cost remains additional: the
star has 64,416 Hamiltonian entries and the inherited degree100 evolution
visits approximately 12.88 million real integer coefficients. These are
explicit workload descriptions, not measured asymptotic or wall-clock speedups.

The remaining error is dominated by further matter iterations, not electric
feedback. The next useful step is to retain another controlled source level
or resum the quadratic matter feedback while keeping a certified bound on
noncommuting electric phases. A common certified response for other physical
observables is still absent here. In particular this does NOT derive a chiral
mirror-free spectrum, select the state or parameters, construct a massless
spin-two sector, or prove a continuum limit. T1-T8 remain physically open.

Only the experiment catalog and research notes accompany these files. There
is no evidence-scorecard, verification-ledger, paper or website promotion.
