# Actual free-scalar reduced completion: operator domain and ground state

Date: 2026-09-06. Independent bounded mathematical review. This note treats
the actual Round-8 free-scalar TT stresses in the chosen Round-9 positive
*reduced* completion. It does not change repository claims, define the full
unreduced quantum model, select the completion from TFPT, or close T8.

## 1. Hypotheses checked against the actual source

Fix a finite connected periodic cubic lattice of n sites, spacing a>0.
Keep all n real scalar coordinates phi, including the uniform coordinate.
Delete homogeneous gravity as in the original reduction. There are
M=2(n-1) real TT oscillator coordinates Q_alpha with r_alpha>0; a real
orthonormal basis can be chosen after imposing Fourier reality. Use the
canonical cell normalization and hbar=1. The Hilbert space is
`L2(R^(M+n),dQ dphi)`. The coupling g is any fixed real number and m>=0.
No limit in n,a,g or m is taken here.

The actual source is
[free-scalar-3d/README.md, R8.1 and R8.2](../free-scalar-3d/README.md):

\[
\tau_{ii}(x)=\tfrac12\pi_x^2-\tfrac12m^2\phi_x^2+\sigma_{ii}(D\phi),
\qquad\tau_{ij}(x)=\sigma_{ij}(D\phi)\quad(i\ne j),
\]

where the sigma expressions are the displayed real quadratic products of
finite differences/averages of phi. The diagonal components share the
same site placement. The kinetic and mass pieces therefore have the exact
tensor form `t h_x`, `t=(1,1,1,0,0,0)`,
`h_x=(pi_x^2-m^2 phi_x^2)/2`.

For each real TT test tensor w_alpha, its trace vanishes at every site:
`sum_i (w_alpha)_ii(x)=0`. This follows equivalently from the zero Fourier
trace at every momentum. Consequently

\[
\tau_\alpha=\langle w_\alpha,\tau\rangle
=\langle w_\alpha,\sigma(D\phi)\rangle=:T_\alpha(\phi).
\]

This cancellation is an exact operator identity on Schwartz space as well
as a classical polynomial identity. Each T_alpha is a real homogeneous
quadratic polynomial in phi, depends only on its lattice differences,
and is independent of pi and m. Its quantum realization is a multiplication
operator. These actual reduced stresses mutually strongly commute; the
general noncommuting quadratic examples used for broader checks in the
earlier contract are not required for this particular model.

The reduced positive completion in
[constraint-dressing/README.md, section 10](../constraint-dressing/README.md)
therefore has the concrete differential expression

\[
H_{g,m}=-\tfrac12\Delta_{Q,\phi}+V_{g,m}(Q,\phi),
\]
\[
V_{g,m}=\tfrac12m^2\|\phi\|^2+\tfrac12\|D\phi\|^2
+\tfrac12\sum_{\alpha=1}^M r_\alpha^2
\left(Q_\alpha+\frac{gT_\alpha(\phi)}{r_\alpha^2}\right)^2.
\tag{1}
\]

Summing the two adjacent half-gradient contributions in rho gives exactly
the `||D phi||^2/2` term under periodic boundary conditions. Here D is the
scalar forward-gradient operator, not a new quantum momentum operator.
The potential is real, smooth, polynomial of degree at most four, and
nonnegative. The differential order of H is **two**. Since the T_alpha
contain only mutually commuting field coordinates, operator squaring and
Weyl quantization of T_alpha squared coincide here; no scalar ordering
correction of a mixed field/momentum quadratic is present.

## 2. Essential self-adjointness for every fixed g and m>=0

**Theorem 1.** The symmetric operator
`H_min=(-Delta/2+V)|Cc_infinity(R^(M+n))` is nonnegative and essentially
self-adjoint. Its closure equals the self-adjoint operator defined by the
previous positive quadratic form. Schwartz space is an invariant test
domain for the polynomial differential expression and an operator core
for its closure.

**Proof.** Write d=M+n. Nonnegativity follows by integration by parts.
Let u belong to `ker(H_min^*+1)`. In distributions,
`-Delta u/2+(V+1)u=0`. Since V is bounded on compact sets and u is locally
square integrable, interior elliptic regularity gives `u in H2_loc`.
Choose real cutoff functions chi_R supported in the radius-2R ball, equal
to one in the radius-R ball, with `0<=chi_R<=1` and
`|gradient chi_R|<=C/R`. Testing the weak equation against chi_R squared
times u and taking the real part yields the exact localization identity

\[
\frac12\int|\nabla(\chi_Ru)|^2
+\int(V+1)\chi_R^2|u|^2
=\frac12\int|\nabla\chi_R|^2|u|^2
\le\frac{C^2}{2R^2}\|u\|^2.
\tag{2}
\]

All integrations initially take place on compact sets; H2_loc justifies
the integration by parts by approximation. Dropping the nonnegative
gradient and V terms gives `integral_(|x|<=R)|u|^2 <= C^2||u||^2/(2R^2)`.
Letting R increase proves u=0.

For completeness, the semibounded operator criterion here requires no
choice of deficiency signs. Let A be the closure of H_min. Because A>=0,
`||(A+1)v||>=||v||`, so its range is closed. The vanishing kernel of
`H_min^*+1=A^*+1` makes this range dense, hence it is all of L2. Given
`v in Dom A^*`, choose `w in Dom A` with
`(A+1)w=(A^*+1)v`. Then v-w is in the same zero kernel, so v=w.
Thus `Dom A^*=Dom A` and A is self-adjoint.

The quadratic form is

\[
q[\psi]=\tfrac12\|\nabla\psi\|^2+\|\sqrt V\psi\|^2,
\quad Dom(q)=H^1(\mathbb R^d)\cap L^2(V\,dx).
\]

It is closed and dense. Its representing operator extends H_min, so the
essential self-adjointness just proved identifies it uniquely with A.
This is the same form as the earlier sum of the matter form, P_alpha
norms and the shifted-Q multiplication norms.

Finally polynomial multiplication and differentiation preserve Schwartz
space. Every Schwartz function is in the maximal adjoint domain, hence
in Dom A by essential self-adjointness. Since `Cc_infinity subset Schwartz
subset Dom A` and Cc_infinity is already an operator core, Schwartz is
also an operator core. This establishes algebraic test-domain invariance
under H, **not** invariance of Schwartz space under exp(-itH). No common
full operator domain for varying g is asserted. QED.

## 3. Positive mass: compact resolvent and a unique ground state

**Theorem 2.** For m>0, V_(g,m) tends to infinity as |(Q,phi)| tends to
infinity. H_(g,m) has compact resolvent. Its bottom eigenvalue is simple,
and a normalized ground-state vector can be chosen smooth and strictly
positive. It is unique up to a constant phase.

**Proof of confinement.** On a potential sublevel `V<=R`, equation (1)
implies `||phi||<=sqrt(2R)/m`. Every T_alpha is continuous, so it is bounded
on this compact phi-ball; call its bound C_alpha(R). Each positive square
also implies

\[
|Q_\alpha|\le\frac{\sqrt{2R}}{r_\alpha}
+\frac{|g|C_\alpha(R)}{r_\alpha^2}.
\]

All variables are bounded. The sublevel is closed, hence compact.
Continuity makes this equivalent to the claimed escape-to-infinity
property. The argument uses finitely many strictly positive r_alpha;
its constants are not volume-uniform.

**Proof of compact resolvent.** A sequence bounded in the form norm is
bounded in H1 on every ball. Rellich compactness supplies local L2
subsequences. Outside a large ball, put
`v_R=inf_(|x|>=R)V(x) -> infinity`; the squared L2 tails are bounded by
`q[psi]/v_R`. A diagonal subsequence and this uniform tail estimate give
global L2 compactness. The form-domain embedding into L2 is therefore
compact, so `(H+1)^(-1/2)` and hence the resolvent are compact.

**Proof of simplicity/positivity.** The Feynman--Kac heat kernel is the
positive free Gaussian kernel multiplied by the Brownian-bridge
expectation of `exp(-integral_0^t V(B_s) ds)`. For continuous finite V>=0,
every continuous bridge path has compact image, so this exponential is
strictly positive and at most one. Hence the heat kernel is strictly
positive for every t>0 and the semigroup is positivity improving.
The compact resolvent supplies an eigenvalue at the spectral bottom.
The positivity-improving Perron--Frobenius theorem then makes this
eigenvalue simple with a positive eigenfunction. Interior elliptic
regularity makes the eigenfunction smooth; the positive-kernel relation
gives positivity at every point. QED.

Consequently there is a positive spectral gap above the ground state for
each one of these fixed finite models. No lower bound uniform in volume,
cutoff, coupling, or vanishing mass is supplied. Nor is a closed formula
for the interacting ground state supplied. The existence of this state
for an explicitly chosen completion is not TFPT's required unique
microscopic state-selection mechanism.

## 4. Zero mass with the uniform scalar retained: no L2 ground state

**Theorem 3.** Suppose m=0 and the scalar coordinate space is still all
of R^n. Let

\[
x_0=n^{-1/2}\sum_x\phi_x,\qquad
\phi=x_0e_0+\xi,\quad e_0=n^{-1/2}(1,\ldots,1),\quad \xi\perp e_0.
\]

The exact self-adjoint operator splits as

\[
H_{g,0}=\left(-\tfrac12\partial_{x_0}^2\right)\otimes I
+I\otimes H_\perp,
\tag{3}
\]

on `L2(R_(x0)) tensor L2(R^(M+n-1)_(Q,xi))`. It has no square-integrable
ground-state eigenvector.

**Proof.** All scalar finite differences annihilate e0. Both the gradient
potential and every T_alpha depend only on xi. Orthogonal change of the
scalar coordinates splits the flat Laplacian without cross terms. The
closed forms split, proving (3) for the unique self-adjoint closures, not
only formally on polynomials.

For a connected finite lattice with n>1 the graph Poincare inequality is
`||D xi||^2>=lambda_1||xi||^2`, lambda_1>0, on mean-zero xi. The confinement
argument of Theorem 2 applies to H_perp with this bound replacing the
mass term. Thus H_perp has discrete spectrum and a simple ground state
at E_perp. In the trivial n=1,M=0 case the remaining Hilbert space is C
and H_perp=0, giving the same conclusion below.

Fourier transform in x0 and expansion in an eigenbasis of H_perp make
H_(g,0) multiplication by `p0^2/2+E_j` in each channel. The bottom is
E_perp. A bottom eigenvector would need Fourier support only at p0=0,
a set of Lebesgue measure zero, so it must vanish in L2. In fact the same
argument excludes every eigenvalue, since for each countable channel
`p0^2/2=E-E_j` permits at most two points. The spectrum is
`[E_perp,infinity)`; the required assertion is the absence of an L2 ground
state. QED.

A formal constant wavefunction in x0 or delta(p0) is not normalizable.
Removing/fixing the uniform scalar, compactifying its value, imposing
different boundary conditions, or adding a mass/potential changes the
model. The already deleted homogeneous *gravity* sector does not remove
this distinct uniform *scalar* coordinate.

## 5. Verification and claim boundary

The companion `quantum_domain_check.py` checks the actual local stress
polynomials on a 3x3x3 periodic lattice: exact trace cancellation,
two **nonzero**, real normalized transverse-traceless stress smearings,
gradient-only dependence, uniform-shift invariance, degree exactly two,
their exact vanishing Poisson bracket,
the periodic matter energy identity, the scalar Laplacian's one-dimensional
kernel, square-expansion coefficients, and the localization identity's
product-rule coefficient. The all-finite-volume operator theorems are
carried by the proofs above, not by a finite matrix approximation of CCR
or a numerical eigenvalue cutoff. No quantum-Hamiltonian spectral
computation is used; the finite scalar graph Laplacian is checked with
an explicit exact invertible product eigenbasis.

The original 2x2x2 axis-Nyquist witness gave two identically zero stress
polynomials, so its initially passing cancellation checks were vacuous as
interaction witnesses. Adding the requirement `T!=0` reproduced a failing
test before the fix. The reason is explicit: at side length two,
`G_i(x-e_i)=-G_i(x)` makes the diagonal gradient stresses isotropic, while
the selected off-diagonal smearing cancels on the transverse two-site
torus. This original witness is retained as an expected-degeneracy control.
The replacement uses `k=(0,0,2*pi/3)` and the real cosine profile with xx-yy
and xy+yx polarizations. Their supported components have no staggered phase
because kx=ky=0; trace, transversality, normalization and nonzero degree-two
output are each checked exactly. This is a witness correction, not a change
to any of the all-volume proofs.

This result strengthens the reduced domain subclaim for the **actual free
scalar**: essential self-adjointness on Cc_infinity, a Schwartz operator
core, and the stated conditional ground-state conclusions now have proofs.
It does not extend these proofs to arbitrary momentum-dependent stress
operators, the off-constraint/unreduced dressed operator, a physical inner
product derived from TFPT, relativistic locality, continuum or infinite-volume
limits, homogeneous gravity reception, or the microscopic uniqueness of
the completion. It does not close T8 or any complete TOE claim.

## Analytic primary sources checked

- Barry Simon, [Schrodinger semigroups, Bull. AMS 7 (1982), 447--526](https://doi.org/10.1090/S0273-0979-1982-15041-8),
  with the [author-uploaded article text](https://www.researchgate.net/publication/243072615_Schrodinger_semigroups):
  Feynman--Kac formula (A26), positivity and ground-state discussion in
  section A1. The nonnegative smooth polynomial here satisfies the local
  regularity/nonnegative-potential assumptions; the bridge weight is
  directly finite and positive as explained above.
- Gerald Teschl, [Mathematical Methods in Quantum Mechanics, 2nd edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf),
  Theorem 10.12, printed pp. 272--273: a bounded real self-adjoint
  positivity-improving operator has a simple positive eigenvector at an
  eigenvalue equal to its norm. We apply this to exp(-tH), after proving
  positivity improvement and ground-state existence for our potential;
  no relative-boundedness assumption from the later Coulomb examples is
  imported. The essential-self-adjointness and compactness arguments are
  explicitly proved in this note.
