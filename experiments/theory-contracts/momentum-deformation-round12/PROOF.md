# Actual positive reduced Hamiltonian: resonant obstruction to momentum deformation

2026-09-06. Independent Round12 analysis, integrated as an unpromoted research contract.

## Precise result

On the actual 6x6x6 periodic model, the standard total **centered-difference**
free momentum can be corrected at order g, but cannot be deformed to a
time-independent conserved quantity through order g squared by arbitrary
globally smooth corrections `J1,J2`. The obstruction already occurs at
`m^2=4/7` on an explicitly periodic free orbit. It includes the actual
quartic completion **and** all relevant virtual TT-exchange channels.
It is not the weaker statement that the old momentum fails to commute
with R, and is not a finite-polynomial-ansatz search failure.

The same coefficient calculation and an independent two-phase torus average
extend the obstruction to every finite `m^2>=0`, and to cubic side lengths
divisible by six. The explicit periodic witness is sufficient independently
of this extension. The conclusion fixes the zeroth-order generator stated
below. Different generators, exact finite translation symmetry, conserved
crystal momentum modulo a reciprocal lattice vector, different Hamiltonians,
or nonsmooth/singular-in-g constructions are not excluded.

## 1. All conventions and the actual Hamiltonian

Lattice spacing and hbar are one. Let n=L^3, initially L=6. Momentum labels
are integer triples modulo L; the physical angle is 2pi times label/L.
Use the unitary cell-label Fourier transform

\[
\widehat\phi_k=n^{-1/2}\sum_x e^{-ik\cdot x}\phi_x,
\qquad\widehat\pi_k=n^{-1/2}\sum_x e^{-ik\cdot x}\pi_x.
\]

Real fields obey `phi_hat_-k=conj(phi_hat_k)` and likewise for pi;
`{phi_hat_k,pi_hat_l}=delta_(k+l,0)`. Define

\[
\omega_k=\sqrt{m^2+\ell(k)},\qquad
\ell(k)=\sum_i(2-2\cos k_i),
\]
\[
a_k=\frac{\sqrt{\omega_k}\widehat\phi_k
               +i\widehat\pi_k/\sqrt{\omega_k}}{\sqrt2},
\quad \{a_k,\overline a_l\}=-i\delta_{kl},
\]
\[
\widehat\phi_k=\frac{a_k+\overline a_{-k}}{\sqrt{2\omega_k}},
\qquad
\widehat\pi_k=-i\sqrt{\frac{\omega_k}{2}}
                      (a_k-\overline a_{-k}).
\tag{1}
\]

Importantly, `a_-k` is **not** constrained to equal `conj(a_k)`. These are
independent travelling-wave oscillator amplitudes; equation (1) enforces
reality of phi and pi. The massless uniform scalar is treated separately
as its free canonical pair; it is absent from every stress vertex used
here because those vertices depend only on differences.

In the actual positive reduced model,

\[
H(g)=H_0+gH_1+g^2R,
\quad H_1=\langle q_{TT},\sigma(\phi)\rangle,
\quad R=\tfrac12\langle\sigma,P_{TT}\ell^{-1}\sigma\rangle,
\quad (P_{TT}\ell^{-1})(0)=0,
\tag{2}
\]

where H0 is the free scalar Hamiltonian plus all nonzero TT oscillators,
with gravity frequency `r_q=sqrt(ell(q))`. Sigma is exactly the gradient
part of [R8.1/R8.2](../free-scalar-3d/README.md):

\[
\sigma_{ii}=\tfrac12G_i(x)G_i(x-e_i)
-\tfrac14\sum_{j\ne i}[G_j(x)^2+G_j(x-e_j)^2],
\]
\[
\sigma_{ij}=\tfrac14[G_i(x)+G_i(x+e_j)]
                         [G_j(x)+G_j(x+e_i)].
\tag{3}
\]

The common diagonal pi-squared and mass terms are killed by TT projection.
The tensor inner product uses the orthonormal component convention
`(11,22,33,sqrt(2)23,sqrt(2)13,sqrt(2)12)`, with the inherited staggered
offdiagonal placements. Neither H1 nor R is changed in this audit.

### The zeroth-order total momentum is fixed, including gravity

For `D_i^c=(S_i-S_i^-1)/2`, let

\[
J_{0,i}=-\sum_x\pi_x(D_i^c\phi)_x
        -\sum_{x,A}p_A(x)(D_i^cq_A)(x),
\tag{4}
\]

where q,p are the original zero-mean TT tensors and A is the orthonormal
tensor index. D_i^c commutes with the TT projector and preserves the TT
subspace, so the second term is well-defined with the reduced symplectic
structure. It generates the same centered shift on q and p as the first
term does on phi and pi. In compatible travelling-wave coordinates,

\[
J_{0,i}=\sum_k\sin k_i\,|a_k|^2
       +\sum_{q,s}\sin q_i\,|b_{q,s}|^2.
\tag{5}
\]

Here s runs over the two TT polarizations. At self-conjugate Nyquist
momentum `(pi,0,0)`, the centered x derivative and its momentum weight
are zero. Its real TT oscillator is counted once, not as independent q
and -q copies. Equation (4) commutes with H0 exactly.

## 2. First order: a real mismatch, but no cubic resonance obstruction

The equation for `J(g)=J0+gJ1+g^2J2` begins

\[
\{J_1,H_0\}=-\{J_0,H_1\}.
\tag{6}
\]

Actual vertices conserve lattice wave vector only modulo reciprocal
vectors. Centered derivative weights sin(k) are not additive. Thus the
order-g mismatch must not be presumed zero even after adding the normal
TT momentum.

Nevertheless every nonzero actual cubic vertex is nonresonant for H0 at
each fixed finite volume. To see this, put `d(k)=(exp(ik_i)-1)_i`. Then

\[
d(k+l)=d(k)+\operatorname{diag}(e^{ik})d(l).
\]

For k,l both nonzero modulo the lattice periods, the Euclidean triangle
inequality is strict. Equality would require the two nonzero complex
vectors on the right to be positively real collinear. Every common
nonzero component would then require `k_i+l_i=0 mod 2pi`, but at that
component the two terms sum to zero, contradicting positive collinearity.
Disjoint nonempty supports also prevent collinearity. Therefore

\[
\omega_0(k+l)<\omega_0(k)+\omega_0(l).
\tag{7}
\]

The same fact excludes difference-frequency resonances by relabeling the
three momenta. For m>0, use the strictly noncollinear decomposition
`(m,d(k+l))=(m,d(k))+(0,diag(exp(ik))d(l))` for emission/absorption;
pair creation is excluded by the preceding triangle bound and the larger
massive scalar energies. The only massless equality cases involve a zero
scalar momentum; equation (3) makes their vertices zero. Homogeneous TT
oscillators are excluded already in (2).

Thus all cubic monomials actually present can be removed by a real cubic
canonical generator S1, at every fixed finite volume. No uniform bound
on its small denominators as the volume or cutoff changes is claimed.
An explicit particular correction is `J1=-{J0,S1}` with the convention in
the next section; the checker verifies (6) directly for the active channel.
This proves existence of an order-g correction, not failure at first order.

## 3. Fixing normal-form signs and the order-g squared obligation

Use the pullback convention

\[
H'=H+g\{H,S_1\}+\tfrac12g^2\{\{H,S_1\},S_1\}+O(g^3),
\qquad \{H_0,S_1\}=-H_1.
\]

Then

\[
H'=H_0+g^2H_2'+O(g^3),\qquad H_2'=R+\tfrac12\{H_1,S_1\}.
\tag{8}
\]

For a real TT oscillator Q,P of frequency r and a scalar quadratic
monomial T_Omega with `{H0,T_Omega}=i Omega T_Omega`, its contribution is

\[
S_1=-\frac{P+i\Omega Q}{r^2-\Omega^2}T_\Omega.
\tag{9}
\]

Equation (9) is checked by a direct Poisson bracket, not a sign convention
inferred from static elimination. Restricting the quartic expression (8)
to the invariant **free** slice with every TT Q=P=0, its gravity bracket
gives the scalar virtual-exchange term

\[
H_2'|_{Q=P=0}
=R-\tfrac12\sum_{q,s,\Omega,\Omega'}
 \frac{T_{q,s,\Omega}T_{-q,s,\Omega'}}{r_q^2-\Omega'^2}.
\tag{10}
\]

Reality-compatible normalization is implicit in the q,s sum; the explicit
self-conjugate channel below uses one real oscillator and has no duplicate
mode factors. Scalar Poisson brackets in `{H1,S1}` contain at least two TT
coordinates/momenta and vanish on this free slice. For resonant scalar
pairs Omega'=-Omega, the static counterterm and exchange combine to

\[
\frac1{r^2}-\frac1{r^2-\Omega^2}.
\tag{11}
\]

In particular Omega=0 cancels. Testing only `{J0,R}` would miss this.

If smooth J1,J2 existed, transform J by the same canonical pullback:
`J'=J0+gF1+g^2F2+O(g^3)`. Its conservation requires

\[
\{F_1,H_0\}=0,\qquad
\{F_2,H_0\}=-\{J_0,H_2'\}.
\tag{12}
\]

An arbitrary H0-invariant freedom F1 has disappeared from the second
equation because the transformed Hamiltonian has no order-g term. Thus
the obstruction below applies to **every** possible smooth J1, not just
the particular cubic solution. The pullback need only exist near the
compact orbit used below, where the cubic vector field has a local flow.
A complete global flow of S1 is not assumed.

## 4. The actual Umklapp quartet and all its exchange partitions

On L=6 use labels

\[
k=(1,1,0),\quad l=(2,5,0),\quad -k=(5,5,0),\quad-l=(4,1,0),
\quad q=k+l=(3,0,0).
\tag{13}
\]

The physical angles of l may equivalently be `(2pi/3,-pi/3,0)`.
Here ell(k)=2, ell(l)=4, ell(q)=4. Since `2(k+l)=0 mod 6`, the monomial

\[
M=a_k a_l\overline a_{-k}\overline a_{-l}
\tag{14}
\]

conserves lattice wave vector but changes the centered x momentum:
`{J0,x,M}=i gamma M`, with `gamma=2sqrt(3)`.

For scalar plane waves `u exp(ikx)+v exp(ilx)`, direct use of (3) and the
staggered projector gives the coefficient of uv in the TT-projected stress:

\[
P_{TT}(q)\sigma_{uv}=(0,3/4,-3/4,0,0,0),
\quad e_+=(0,1,-1,0,0,0)/\sqrt2,
\quad e_+\cdot\sigma_{uv}=\frac3{2\sqrt2}.
\tag{15}
\]

No yz cross polarization is excited. As a simple check of (15),
`sigma_22-sigma_33` has anisotropic part one quarter the square of the
centered y field difference. Its uv coefficient is
`-2 sin(k_y) sin(l_y)=3/2`.

Equation (15) uses unnormalized plane waves. With the unitary Fourier
transform and oscillator convention (1), the coefficient of each relevant
quadratic scalar oscillator monomial in T_q,+ is

\[
b=\frac{3/(2\sqrt2)}{2\sqrt{n\omega_k\omega_l}},
\qquad b^2=\frac9{32n\omega_k\omega_l}.
\tag{16}
\]

Write a=a_k, bvar=a_l, c=a_-k, d=a_-l (b in (16) remains the coefficient).
The part of this one **real**, Nyquist TT source using these four modes is

\[
T=b[(a+\overline c)(bvar+\overline d)
          +(c+\overline a)(d+\overline {bvar})].
\tag{17}
\]

The H1 coefficient of `Q a bvar` is b. Its order-g centered momentum
mismatch is `i sqrt(3) b Q a bvar`, nonzero: the TT Nyquist momentum weight
is zero, while sin(k_x)+sin(l_x)=sqrt(3). This explicitly checks the first
vertex mismatch requested in the audit.

For M, the three partitions of its four external scalar factors are:

| Pairing | Intermediate momentum | Source frequency |
| --- | --- | --- |
| `(a,bvar)` with `(conj(c),conj(d))` | q=(3,0,0), self-conjugate | plus/minus (omega_k+omega_l) |
| `(a,conj(d))` with `(bvar,conj(c))` | the same q | plus/minus (omega_k-omega_l) |
| `(a,conj(c))` with `(bvar,conj(d))` | 2k and 2l=-2k | zero |

The third partition has zero actual TT vertices: a source formed by two
equal scalar momenta is TT-annihilated at twice that momentum. The checker
verifies this with the full staggered projectors at 2k and 2l. Independently,
even if a zero-frequency vertex were retained it would cancel in (11).
No partition involves excluded homogeneous TT momentum. These are all
three partitions; no omitted s/t/u channel can change the coefficient.

The complete coefficient of M in (8) is consequently

\[
C=b^2\left[\frac2{r^2}
-\frac1{r^2-(\omega_k+\omega_l)^2}
-\frac1{r^2-(\omega_k-\omega_l)^2}\right],\qquad r^2=4.
\tag{18}
\]

Both exchange denominators, their signs, the positive R contribution,
the volume factor, and the two source orderings have now been included.

## 5. Explicit periodic-orbit obstruction at m squared = 4/7

Put `nu=sqrt(2/7)`, so omega_k=3nu and omega_l=4nu. Then

\[
(\omega_k+\omega_l)^2=14,\quad
(\omega_k-\omega_l)^2=2/7,\quad b^2=7/18432,
\]
\[
\frac24-\frac1{4-14}-\frac1{4-2/7}=\frac{43}{130},
\qquad C=\frac{301}{2396160}>0.
\tag{19}
\]

Set initial travelling amplitudes `a=bvar=c=1`, `d=i`, with their genuine
complex conjugates, all other scalar modes zero, and every TT Q=P=0.
This is a real scalar phase-space point by (1), with J0,x=0. Its H0 orbit
is periodic with period `2pi/nu`; M is the constant -i on that orbit.

The calculation does not silently assume that M is the only resonant
term. The checker enumerates **all** degree-four monomials in these eight
amplitude/conjugate variables. Imposing zero free frequency, zero lattice
wave vector, and nonzero centered x charge leaves precisely M and its
complex conjugate. Terms with TT variables vanish along the chosen orbit.
Unoccupied scalar variables vanish; scalar contractions of intermediate
unoccupied modes in (8) still leave TT factors and hence vanish. Every
other surviving scalar monomial either averages to zero or commutes with
J0. Therefore the full averaged forcing is exactly

\[
\frac1T\int_0^T\{J_{0,x},H_2'\}(\Phi_{H_0}^t z_*)\,dt
=i\gamma C(M-\overline M)
=4\sqrt3 C
=\frac{301\sqrt3}{599040}\ne0.
\tag{20}
\]

For any single-valued smooth F2 defined near this periodic orbit,
the integral of `{F2,H0}` over one period is zero. Equation (20) contradicts
(12). Thus no smooth time-independent J1,J2 can satisfy the deformation
equations through second order. Scaling all four initial amplitudes by
epsilon scales (20) by epsilon to the fourth power and makes the orbit
arbitrarily small. The obstruction therefore also rules out a smooth
deformation defined on a full neighborhood of the free origin, not merely
globally on all phase space.

## 6. Controlled extension to all finite masses and larger allowed cubes

For mu=m^2>=0, the same exact expression simplifies to

\[
\frac12-\frac1{4-(\sqrt{\mu+2}+\sqrt{\mu+4})^2}
-\frac1{4-(\sqrt{\mu+2}-\sqrt{\mu+4})^2}
=\frac{2\mu+5}{2(4\mu+7)}>0,
\]
\[
C(\mu,n)=
\frac{9(2\mu+5)}{64n(4\mu+7)\sqrt{(\mu+2)(\mu+4)}}>0.
\tag{21}
\]

Use the full two-phase torus
`a=c=exp(-i theta1)`, `bvar=exp(-i theta2)`,
`d=i exp(-i theta2)`, with genuine conjugates and all remaining modes zero.
It is invariant under H0. For any smooth single-valued F2 on this torus,

\[
\{F_2,H_0\}=\omega_k\partial_{\theta_1}F_2
                +\omega_l\partial_{\theta_2}F_2,
\qquad
\int_{\mathbb T^2}\{F_2,H_0\}\,d\theta_1d\theta_2=0.
\tag{22}
\]

This identity holds even when the frequency ratio is rational; no dense-
orbit or ergodicity hypothesis is needed. Torus averaging retains precisely
monomials balanced separately in the two frequency species. The checker
enumerates all degree-four monomials satisfying these two balances and
lattice wave-vector conservation: those with nonzero centered x charge
are exactly M and its conjugate. Hence the torus mean of the right side
of (12) has magnitude `4sqrt(3) C(mu,n)>0`, contradicting (22).

As an extra control, the executable also lists the only possible positive
unbalanced two-frequency ratios for degree-four monomials: 1/3,1,3. None
lies in the actual interval `(1,sqrt(2)]`. This is not needed for (22),
but confirms that the one-orbit and two-phase selections agree here.
At m=0 the uniform scalar is fixed with uniform momentum zero on this
torus, and S1 is independent of that free pair, so the argument is
unchanged. No infinite-volume limit is involved.

For L divisible by six, choose the same physical angles as (13). All
frequencies, actual vertices, resonance classifications and charge changes
are unchanged; only n=L^3 replaces 216 in (16),(21). C remains nonzero.
Thus no side length divisible by six, at any finite mass squared >=0,
admits the claimed deformation of the specified centered total momentum.

## 7. What changes can evade the theorem, and what they actually change

- The exact finite lattice translation group still commutes with H(g).
  Averaging its genuine pullbacks, restricting to an invariant sector,
  or labelling quantum states by crystal momentum modulo reciprocal
  vectors is allowed. None is the smooth deformation of (4) proved
  impossible here. A quantum logarithm of a finite translation operator
  also does not automatically have (4) as a smooth classical limit.
- Merely replacing sin(k) by a spectral derivative weight does not turn
  aliased pointwise products into a derivation. Reciprocal-vector/Umklapp
  sums survive; the real self-conjugate Nyquist sector needs an explicit
  convention as well. No alternative spectral generator is assumed to be
  the old J0, and no universal no-go for all alternative seeds is claimed.
- Dealiasing, restricting triads to no-wrap wave-vector sums, or changing
  the field product removes actual vertices. In particular the retained
  q=(pi,0,0), k+l=q vertex (15), or its reciprocal-lattice partner needed
  by reality, cannot simply be erased while claiming the same H1.
- Averaging H1 under the continuous centered flow generated by (4) projects
  onto additive sin-weight zero. The actual `Q a_k a_l` monomial has weight
  sqrt(3), so this procedure removes it already at order g. It is a new
  Hamiltonian, not a nonlinear repair of the same conserved momentum.
- Altering R to cancel the frequency-dependent resonant coefficient in
  (18), adding propagating fields, or replacing the physical local algebra
  requires a new construction. The existing positive static completion
  cancels zero-frequency exchange, not this nonzero-frequency resonance.

No conclusion about a fully diffeomorphism-invariant gravitational momentum
constraint, all possible microscopic parents, nonperturbative integrability,
or quantum domains follows. In particular the theorem is about a conserved
quantity with prescribed zeroth-order limit, not the absence of every
conserved function (H itself is conserved).

More specifically, conservation here is strong: the Poisson bracket vanishes
as a function, through the stated perturbative order. The proof does not
automatically exclude a merely weak or constraint-proportional identity
`{J_i(g),H(g)}=M_i^j(g) J_j(g)` on a deformed constraint surface. That problem
has additional coefficient and surface terms and requires a separate proof.
No homogeneous gravitational constraint no-go is inferred by conflating it
with the strong conserved-quantity deformation treated here.

## 8. Verification and primary-source context

The companion `momentum_deformation_check.py` is exact, standalone and
imports no repository code. It derives the local actual vertex, checks
staggered TT projection and equal-momentum channels, fixes Fourier and
oscillator factors, directly checks `{H0,S1}=-H1`, computes the quartic
Poisson bracket and its coefficient, enumerates all charged resonances,
and takes the exact constant Laurent coefficient on the periodic orbit.
The general-mass factor is checked symbolically. No numerical tolerance,
truncated CCR representation or finite-ansatz exhaustion is involved.

The use of resonant monomials and cubic elimination is standard normal-
form machinery; the needed finite-dimensional identities and the orbit
obstruction are proved explicitly above. For primary context, see
[Bambusi and Grebert, Birkhoff normal form for PDEs with tame modulus](https://web.ma.utexas.edu/mp_arc-bin/mpa?yn=04-332).
Discrete Umklapp resonances and removal of nonresonant three-wave terms
also occur in [Onorato, Vozella, Proment and Lvov's FPU study](https://arxiv.org/abs/1402.1603).
Those are different Hamiltonians; none of their thermalization, normal-
form convergence or long-time conclusions is imported into this model.

The narrowly supported result is a new order-g-squared obstruction for
the actual chosen H(g) and explicitly fixed total centered momentum. It
does not close T8 or a complete TOE claim.
