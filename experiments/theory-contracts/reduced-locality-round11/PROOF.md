# Actual reduced scalar locality and homogeneous-momentum audit

2026-09-06. Independent Round11 audit, integrated as an unpromoted research contract.

## Outcome and exact scope

For any fixed nonzero coupling g, the selected positive reduced Hamiltonian
has a genuinely non-finite-range
generator on the **given canonical scalar observable algebra**. This is
proved with the actual Round-8 stress, not arbitrary independent sources.
The existing TT oscillators do not cancel the exhibited first-time-order
scalar response. A local nondynamical constrained representation of the
energy is therefore not, by itself, a causal local dynamics theorem for
this observable algebra.

There is a second concrete issue: the old free-scalar homogeneous momentum
`J_i=-pi^T D_i^c phi` is not conserved by this selected interaction. One
cannot impose the old `J_i=0` conditions and silently assume preservation.

These statements do **not** rule out a different dressed/relational local
observable net, a dynamical gauge completion with different observables,
or a controlled causal continuum limit. They do not claim that every
instantaneous gauge-fixed term is acausal. No T-gate or TOE is closed.

## 1. Model, stress, and exact kernel

Use spacing and hbar equal to one. The physical reduced phase space is the
canonical scalar pairs `(phi_x,pi_x)` and the already retained nonzero TT
oscillator pairs `(Q_alpha,P_alpha)`. At fixed finite volume,

\[
H_+=\frac12\|\pi\|^2+\frac12m^2\|\phi\|^2
+\frac12\|D\phi\|^2+\frac12\sum_\alpha(P_\alpha^2+r_\alpha^2Q_\alpha^2)
+g\langle q_{TT},\sigma(\phi)\rangle+g^2R(\phi),
\qquad R=\frac12\langle\sigma,K\sigma\rangle,
\quad K=P_{TT}\ell^{-1},\quad K(0)=0.
\tag{1}
\]

Here sigma is the gradient part of the actual stress in
[R8.1/R8.2](../free-scalar-3d/README.md):

\[
\sigma_{ii}(x)=\frac12G_i(x)G_i(x-e_i)
-\frac14\sum_{j\ne i}(G_j(x)^2+G_j(x-e_j)^2),
\]
\[
\sigma_{ij}(x)=\frac14(G_i(x)+G_i(x+e_j))
                              (G_j(x)+G_j(x+e_i)),\quad i\ne j.
\tag{2}
\]

The omitted pi-squared and mass terms are common diagonal trace and are
annihilated by K and by TT smearing. Sigma is a real quadratic configuration
polynomial. Every one of its monomials contains scalar sites at graph
distance at most two. In particular, at distance greater than two,
`sigma_xy:=partial_(phi_x) partial_(phi_y) sigma=0` identically.

For reproducibility, the checker implements the complete staggered kernel,
including its phases; it does not replace the projector by a continuum
formula at unshifted tensor placements. In label-coordinate Fourier space,
write `z_i=exp(ik_i)`, `d_i=z_i-1`, `r2=sum_i(2-z_i-z_i^-1)`. In orthonormal
tensor coordinates `(11,22,33,sqrt(2)23,sqrt(2)13,sqrt(2)12)`, V has diagonal
blocks d_i and offdiagonal blocks `(1-z_j^-1)/sqrt(2)`. Set t=(1,1,1,0,0,0).
Then

\[
VV^\dagger=\tfrac12(r^2I+dd^\dagger),\qquad Vt=d,
\quad S=V^\dagger d-r^2t,
\]
\[
P=I-V^\dagger\left(\frac{2I}{r^2}-\frac{dd^\dagger}{r^4}\right)V
-\frac{SS^\dagger}{2r^4}.
\tag{3}
\]

For raw symmetric tensor Fourier vectors a,b, the raw inner product has
weights `(1,1,1,2,2,2)`. Put v_a=V a_orth, u_a=d^dagger v_a, and
s_a=u_a-r2 trace(a), and likewise for b. The exact bilinear kernel is

\[
\widehat a^\dagger K\widehat b
=\frac{\langle a,b\rangle_{raw}}{r^2}
-\frac{2v_a^\dagger v_b}{r^4}
+\frac{\overline{u_a}u_b}{r^6}
-\frac{\overline{s_a}s_b}{2r^6}.
\tag{4}
\]

Unnormalized Fourier sums use Parseval factor 1/number-of-sites. Momentum
zero is omitted in full. The checker evaluates (4) in an exact algebraic
number field and obtains rational final values. Independent real-space
controls verify annihilation of `V^dagger v` and trace sources, and the
known value for an actual real TT plane wave. This checks the placement
phases and offdiagonal weights, not merely nonzero output from one formula.

## 2. Actual separated-site witness

On the 3x3x6 periodic lattice, let

\[
\phi_{(x_1,x_2,x_3)}=f(x_1),\quad f=(1,-1,0),\quad
X=(0,0,0),\quad Y=(0,0,3).
\tag{5}
\]

The two sites have graph distance three. For `J_X=partial_X sigma`,

\[
\partial_X\partial_Y R
=\langle J_X,KJ_Y\rangle+\langle\sigma,K\sigma_{XY}\rangle
=\langle J_X,KJ_Y\rangle
=-\frac{12000311}{381024000}\ne0.
\tag{6}
\]

The checker verifies sigma_XY=0, and independently obtains the same answer
from the four exact energies at `phi +/- e_X +/- e_Y`. Their alternating
sum divided by four equals (6): with sigma_XY=0, quadratic sigma permits
no other odd-odd term in this finite difference. Thus this is a witness
using actual scalar configurations, not unconstrained stress data.

For the plane directions `delta phi=f(x_1) delta_(x_3,0)` and
`delta phi=f(x_1) delta_(x_3,3)`, it also gives
`partial_(a_0) partial_(a_3) R=-104093/87808`.

Both the local matter potential and `g<q_TT,sigma>` have zero mixed scalar
derivative at this separation for **every** q_TT. All pure TT terms have
zero scalar derivative. Hence `partial_X partial_Y V=g^2 partial_X
partial_Y R` exactly; it cannot be canceled by the already present TT
oscillators at this derivative order.

The companion additionally checks a strictly cubic 6x6x6 lattice, with
the same profile repeated with period three in x_1 and the same sites X,Y.
The answer is `-1762469675117/170400029184000`, again nonzero. The all-size cubic
argument below is independent of the rectangular finite witness.

## 3. Observable response, with bounded operators and domain control

Classically, since dot(pi_X)=-partial_X V,

\[
\{\dot\pi_X,\pi_Y\}=-\partial_X\partial_Y V.
\tag{7}
\]

With `[phi_x,pi_y]=i delta_xy`, the corresponding equal-time algebraic
identity on Schwartz space is

\[
[\dot\pi_X,\pi_Y]=-i\partial_X\partial_Y V.
\tag{8}
\]

No formal infinite operator Taylor series is needed. Use the bounded
onsite translation unitaries `A=T_X(a)=exp(i a pi_X)` and
`B=T_Y(b)=exp(i b pi_Y)`. They preserve Schwartz space. Define
`Delta_X^a V(phi)=V(phi+a e_X)-V(phi)`. Since all kinetic terms commute
with these translations and A,B commute with one another,

\[
\left.\frac d{dt}[e^{itH_+}Ae^{-itH_+},B]\right|_{t=0}
=i[[H_+,A],B]
=i(\Delta_Y^b\Delta_X^a V)AB.
\tag{9}
\]

Equation (9) holds weakly between Schwartz vectors. To justify it,
differentiate each unitary group in the matrix element using the two
vectors in Dom(H_+); A,B and their products preserve Schwartz, and the
Round-10 theorem puts Schwartz in Dom(H_+). No claim that the full time
evolution preserves Schwartz, and no unbounded operator-norm derivative,
is required. The nonzero mixed derivative in (6) makes the multiplier in
(9) nonzero for sufficiently small suitable nonzero a,b. Nonzero weak
derivative means a nonzero matrix element for all sufficiently small
nonzero times of one sign. Real or imaginary parts give bounded Hermitian
local observables if desired.

Operationally within the **specified reduced tensor-product scalar net**,
take two classical initial data differing only by `epsilon e_Y` in phi,
with identical pi,Q,P. The initial remote acceleration difference is
`-epsilon g^2 partial_X partial_Y R+O(epsilon^2)`. Quantum mechanically,
rho and B rho B^dagger have identical initial expectations for observables
outside Y. Equation (9), with a suitable smooth finite-energy state and
the real or imaginary part of A, makes a remote later expectation differ
at first order in time. Existence of a detecting state follows from the
nonzero quadratic form, using polarization on the dense Schwartz domain.
More concretely, choose small a,b and a nonnegative smooth compactly
supported scalar wavefunction in a neighborhood where the finite-difference
multiplier has fixed nonzero sign, with overlap with its a-translate.
Tensor it with a smooth finite-energy TT wavefunction. The resulting
integral of that multiplier times the two overlapping wavefunctions is
nonzero, so the imaginary part of A detects the first-order response.

This conclusion is conditional on these onsite operations being physical
and local. They are the canonical scalar operations in this reduced model.
Under a nonlocal canonical dressing or embedding in another gauge theory,
their representatives may no longer be local operations there.

## 4. All-size finite-range obstruction from the actual stress vertex

The finite witness alone excludes only interaction ranges shorter than its
separation. The following proves that no one fixed finite range works for
the same dynamics on the same scalar algebra across growing cubic volumes.

Take a cubic LxLxL torus with L divisible by three, background
`phi=f(x_1 mod 3)`, and plane perturbations
`delta phi=f(x_1 mod 3) delta a_(x_3)`. At background a=1, the three
diagonal stress Jacobian profiles in one transverse period are

\[
J_{11}=(-2,-2,1),\qquad
J_{22}=J_{33}=(-5/2,-5/2,-1).
\tag{10}
\]

Their transverse means are (-1,-2,-2). The only possible offdiagonal
Jacobian is

\[
J_{13}(x_1,x_3)=\tfrac12(f(x_1+1)^2-f(x_1)^2)
                   (\delta a_{x_3+1}-\delta a_{x_3}),
\tag{11}
\]

whose transverse mean is zero. Consequently at momentum `(0,0,k)`,
k nonzero, the mean TT Jacobian is `(1/2,-1/2,0)` in diagonal components.
Its squared norm is 1/2. The zero-transverse contribution to the a-Hessian
of R is therefore exactly

\[
\frac{L^2}{2\ell_z(k)},\qquad \ell_z(k)=2-2\cos k.
\tag{12}
\]

Normalize the plane direction to scalar norm one:
`delta phi=f(x_1) delta c_(x_3)/(sqrt(2/3)L)`. Its Hessian symbol, for
nonzero longitudinal k, has the form

\[
S_R(k)=\frac{3}{4\ell_z(k)}+B(k),
\tag{13}
\]

where B is independent of L and continuous, bounded near k=0. For H_+ this
is multiplied by g squared and has the local matter Hessian added; the
pole remains for g nonzero. Here is why
no hidden cancellation is in B:

- All other transverse Jacobian momenta are `(plus/minus 2pi/3,0)`.
  They have transverse Laplacian eigenvalue three. Formula (4) has only
  denominators `(3+ell_z)^j`, with j at most three, and Laurent-polynomial
  vertices from (10)-(11). These channels are regular at k=0.
- In fact the remaining Hessian term `<sigma,K sigma''>` is zero at this
  background. Its nonzero Fourier momenta are along x_1, its offdiagonals
  vanish and sigma_22=sigma_33. The transverse-traceless projection is
  therefore zero; the fully homogeneous part is removed by K(0)=0.
  Hence K sigma=0 (also checked from the exact zero base energy). More
  generally, without this simplification the stress second derivative
  would still have scalar separation at most two.
- The local matter and fixed-q source Hessians are finite range. Set q=0
  for the obstruction. They cannot remove the pole in (13).

In particular the nonzero pole is an **actual scalar vertex residue**.
At the zero scalar background every stress Jacobian vanishes, so an audit
around that special background would miss this mechanism.

Suppose a Hamiltonian on this same local algebra had an exact interaction
diameter bounded by rho for every L and agreed with H_+'s dynamics. Its
double commutator with separated onsite translations would vanish beyond
rho at first time order. Summing such derivatives over two planes gives
a Hessian convolution of range at most rho in x_3. At this translation-
invariant background its symbol is a Laurent polynomial of degree rho.

One need not assume volume-independent interaction coefficients. Choose
2rho+1 fixed distinct nonzero rational multiples of 2pi belonging to a sufficiently
large common momentum grid, and take L along its multiples (also divisible
by three). The full H_+ Hessian values at those angles determine all Laurent coefficients
by an invertible Vandermonde system, so the hypothetical polynomial is the
same along this subsequence. It is bounded at k=0. But on additional grid
points k=2pi/L, equation (13) diverges as L squared. Contradiction.

Thus the generator has no uniform finite interaction range on the same
physical algebra. This does not exclude a constrained local parent whose
reduced observable embedding or Dirac brackets are spatially nonlocal.
It also does not establish or refute any particular generalized long-range
Lieb--Robinson bound.

## 5. Why TT mediators and Coulomb gauge do not erase this calculation

The current TT modes are retained in (1); they have not been integrated out
to manufacture the result. For the specified scalar observables all their
contributions to the first derivative (9) are already included. The pure
TT terms commute with A and B, and the actual q-sigma coupling has scalar
range two. Their subsequent response cannot cancel a nonzero first
derivative at zero time.

The Round-10 local auxiliary construction has elliptic-in-space,
nondynamical equations. Its minimizing auxiliaries depend on a global
inverse Laplacian. The paired scalar configurations above therefore induce
different auxiliary configurations far away. They are locally different
states in the **reduced scalar net**, but generally not states differing
only locally if these auxiliary values are counted as independent local
measurable data. Locality of the static constraint equations does not
resolve that distinction.

In electromagnetism, a superficially instantaneous Coulomb-gauge term is
not by itself a causality violation: gauge-invariant electric fields have
additional transverse-potential contributions that cancel the instantaneous
part. This is demonstrated directly by Wundt and Jentschura,
[Sources, potentials and fields in Lorenz and Coulomb gauge (2012)](https://arxiv.org/abs/1110.6210).
Our calculation therefore does not infer a no-go merely from K being
nonlocal. It computes the complete first derivative for explicitly named
observables, and limits the obstruction to preserving their local meaning.
Whether another gauge-invariant relational net provides the required
cancellation is a different, presently unspecified construction.

Likewise, nonzero commutators at arbitrarily short time occur even in many
ordinary finite-range lattice models at sufficiently high time order.
The discriminating result here is the **first-order** remote derivative
at unbounded distances, not a naive strict lattice light-cone test.
Bounds for unbounded oscillators require their own hypotheses and suitable
observables; one cannot import a bounded-spin theorem wholesale. Compare
[Nachtergaele, Raz, Schlein and Sims (2009)](https://arxiv.org/abs/0712.3820)
and [Raz and Sims (2009)](https://arxiv.org/abs/0902.0025), which treat
specific harmonic/anharmonic oscillator classes and Weyl observables.
No relativistic continuum or infinite-volume limit has been proved here.

## 6. The old homogeneous scalar momentum is not conserved

Let `D_i^c=(S_i-S_i^-1)/2`, a real antisymmetric matrix, and

\[
J_i=-\pi^T D_i^c\phi.
\tag{14}
\]

It commutes with the free matter Hamiltonian: D_i^c is antisymmetric and
commutes with the periodic Laplacian and mass matrix. But discrete
translation invariance of an interaction does not imply invariance under
the continuous canonical flow generated by (14); a central difference
does not satisfy the Leibniz rule.

For R depending only on phi,

\[
\{J_i,R\}=dR(\phi)[D_i^c\phi]
=\langle\sigma(\phi),K\,d\sigma(\phi)[D_i^c\phi]\rangle.
\tag{15}
\]

Take the 3x3x6 rational configuration

\[
\phi=f(x_1)a_{x_3},\qquad f=(1,-1,0),\quad
a=(1,2,-1,0,1,0),\qquad \pi=Q=P=0.
\tag{16}
\]

The exact checker finds

\[
R=\frac{115645}{24696},\qquad
\{J_1,R\}=\{J_2,R\}=0,\qquad
\{J_3,R\}=-\frac{568433}{87808}\ne0.
\tag{17}
\]

Indices here are physical 1,2,3; the executable prints them as 0,1,2.
It separately verifies invariance of R under an actual one-site discrete
translation and exact zero free-matter directional derivative. Thus (17)
is not a Fourier-phase artifact or broken periodic translation symmetry.

At (16), the source coupling is zero and its bracket with J_i is zero
because Q=0. Any ordinary tensor translation momentum bilinear in Q,P
has vanishing first derivatives at Q=P=0, so cannot cancel (17). Therefore

\[
\{J_3,H_+\}=-g^2\frac{568433}{87808}\ne0\quad(g\ne0)
\tag{18}
\]

at a point where all the old J_i vanish. The old zero-momentum constraint
surface is not invariant under this chosen reduced Hamiltonian. Extending
the same field with transverse period three to 6x6x6 multiplies (17)-(18)
by four, because only the repeated source's existing transverse Fourier
channels occur and the Parseval transverse area is quadrupled. This gives
the strictly cubic value `-568433/21952`, also checked directly with all
6x6x6 Fourier modes in the companion.

A corrected generator, a new constraint completion, or a different
Hamiltonian could change the conclusion, but is additional work. A clock
constraint using A=H_+ may be valid by itself while its proposed combination
with these old J_i constraints fails closure. At the quantum polynomial
level J_i is quadratic, so its Weyl/Moyal bracket with R has no higher odd
Moyal corrections; this obstruction is not removed by an ordering choice.

There is no obstruction here to restricting to the invariant subspace of
the **finite discrete translation group** by averaging its genuine unitary
pullbacks, provided that group commutes with the chosen Hamiltonian. That
is a different symmetry restriction from the old continuous `J_i=0`
constraints. The local scalar translations used in section 3 need not
preserve such a globally invariant subspace; locality on its physical
observable algebra must consequently be posed anew. Neither the momentum
counterexample nor the same-algebra locality theorem prohibits this finite
symmetry restriction or an otherwise valid clock construction on it.

## 7. Verification record and next discriminating test

`locality_check.py` is standalone, uses exact SymPy algebraic-number-field
arithmetic and rational actual stresses, imports no repository code, and
prints its results. It checks both finite tensor geometries, phase-sensitive
kernel controls, an independent four-energy Hessian identity, the actual
infrared vertex residue, the momentum counterexample, and the translation
and free-energy controls. It uses no floating-point tolerances, finite CCR
matrices, approximate quantum time evolution, or spectral cutoff.

The separate `redteam_source_projector.py` cross-checks the original repository
Ward formulas (648 component values), three current sums and 162 flow
coefficients, and all 53 nonzero-mode kernels against a weighted-nullspace
construction. Its finite data do not replace the all-size proof, but detect
source transcription, sign and projector-phase errors independently.

The most useful next test is not another positivity check: specify the
candidate parent's **physical local observable net and allowed local
preparations**, map these bounded scalar translations into it, and compute
the corresponding complete double commutator. Independently, demand
preservation/closure of every proposed homogeneous momentum constraint
under the exact selected Hamiltonian. A nonlocal dressing can evade the
same-algebra locality obstruction only by explicitly changing what counts
as a local observable or operation; it cannot silently establish both
identifications at once.
