# Actual cubic interaction: full-system classical escape and quantum limits

2026-09-06. Round14 locally integrated research, NON-RH. No physical gate is promoted.

## 1. Result and exact boundary

There is a rigorous finite-time classical escape theorem for the **full
finite TT plus scalar system** on the actual stationary off-shell fiber
`r=v=y=0`, at nonzero coupling. An exact `2^3`, `m^2=2`, `g=1` initial datum
has energy `-16384` and escapes in forward time no later than `t=1`.
The fourteen nonhomogeneous TT modes and all eight scalar modes remain in
the system. A second, initially unoccupied TT mode is immediately forced;
an invariant one-mode truncation is neither asserted nor needed.

This is a stationary `bv=0` fiber, **not** a regular constraint characteristic.
The fiber has measure zero in the kinematic constraint-label space. Its
classical blow-up does not establish a quantum deficiency index, boundary
nonuniqueness, failure of a covariant extension, or nonconvergence of the
Hermite approximants on the original Hilbert space.

Two additional conclusions are rigorous:

* Regular characteristic trajectories arbitrarily close to this fiber
  reach every prescribed finite radius before time one, with the label
  allowed to depend on that radius. This is not a proof that any one fixed
  regular characteristic has finite-time escape.
* Actual coherent-state expectations are unbounded above and below, already
  on the stationary physical fiber. The same cubic leading term proves
  this for every frozen regular fiber and the full minimal operator.
  Thus a semibounded/Friedrichs-extension argument is unavailable. This
  is much weaker than proving that more than one self-adjoint extension exists.

## 2. The unchanged Hamiltonian on the stationary fiber

Use the full actual off-shell expression in
[Round13, equations (6)--(8)](../covariant-domain-round13/README.md).
With `r=v=y=0`, the label flow is stationary and the physical Hamiltonian is

\[
 h=T+V_2+V_3,
 \quad T=\frac12(|P|^2+|\pi|^2),
 \quad V_2=\frac12\sum_\alpha\ell_\alpha Q_\alpha^2+V_m(\phi),
 \quad V_3=g\sum_\alpha Q_\alpha\tau_\alpha(\phi).
 \tag{1}
\]

Every nonhomogeneous TT mode is included. `V_2>=0`; the actual projected
Ward stresses `tau_alpha` are configuration-only homogeneous quadratics.
Hence `V_3` is a homogeneous cubic in the combined configuration
`x=(phi,Q)`. The kinetic energy is the ordinary positive Euclidean one
in these canonical physical coordinates. Let `p=(pi,P)`.

There is **no** counterterm

\[
 g^2R=\frac{g^2}{2}\sum_\alpha\tau_\alpha(\phi)^2/\ell_\alpha
 \tag{2}
\]

in this off-shell Hamiltonian. Adding (2) would produce the different
positive completion

\[
 h+g^2R=T+V_m+\frac12\sum_\alpha\ell_\alpha
       (Q_\alpha+g\tau_\alpha/\ell_\alpha)^2\ge0.
 \tag{3}
\]

The theorem below concerns (1), not (3). It does not transplant a runaway
into the positive reduced Hamiltonian by dropping its existing counterterm.

The conjugate gauge coordinates can evolve, but the physical expression
is independent of them. The label and auxiliary-coordinate choice is
invariant: `dot c=A c=0`, and the actual Hamiltonian has no auxiliary
momenta. It therefore specifies an actual classical subsystem of the
unchanged unreduced expression. It is not an assertion that this is an
ordinary nonzero kinematic `L2` sector.

## 3. Full-system concavity theorem with a quantitative bound

Consider any finite-dimensional smooth Hamiltonian of the form (1), with
`V_2` nonnegative homogeneous quadratic and `V_3` homogeneous cubic.
Let the initial conserved energy satisfy `E<0`, and define

\[
 F=|x|^2,\qquad F(0)>0,\qquad F'(0)=2x(0)\cdot p(0)>0.
 \tag{4}
\]

The maximal forward solution exists on `[0,T_max)`. Polynomial ODE local
existence is enough; completeness is not presumed. Euler homogeneity gives

\[
 F'=2x\cdot p,\qquad
 F''=4T-4V_2-6V_3=10T+2V_2-6E.
 \tag{5}
\]

In particular `F''>0`, so `F'>0` and `F` stays positive. Independently,
`x=0` would imply `E=T>=0`, which is impossible. The exact Cauchy remainder is

\[
 8FT-(F')^2
   =4\sum_{i<j}(x_i p_j-x_j p_i)^2\ge0.
 \tag{6}
\]

Consequently,

\[
 FF''-\frac54(F')^2
 =\frac54[8FT-(F')^2]+F(2V_2-6E)>0.
 \tag{7}
\]

For `Y=F^(-1/4)`, differentiating twice yields

\[
 Y''=-\frac14F^{-9/4}
            \left[FF''-\frac54(F')^2\right]<0,
 \quad Y'(0)=-\frac14F(0)^{-5/4}F'(0)<0.
 \tag{8}
\]

The positive function `Y` lies below its initial tangent line. It cannot
exist positively beyond that line's zero, giving

\[
 T_{\max}\le -Y(0)/Y'(0)=\frac{4F(0)}{F'(0)}<\infty.
 \tag{9}
\]

At a finite maximal time, `|x|` must diverge: if `x` were bounded, the
polynomial force `-grad(V_2+V_3)` would be bounded, so `p` would be bounded
and the ODE could be continued. Since `F` is increasing, its limit exists
and is therefore `+infinity`. This proves actual configuration-space
escape, rather than merely an unbounded momentum or a formal failure of
an estimate. Conditions `E<0` and `F'(0)>0` also define an open set of
escaping physical initial data on the fixed stationary fiber.

If `F'(0)=0`, (5) makes it positive at any sufficiently small positive
time; the same argument then starts there. The explicit bound (9) is
only used with a strictly positive initial derivative.

This is the elementary finite-dimensional concavity argument associated
with Levine's negative-energy method. Primary context is
[H. A. Levine, SIAM J. Math. Anal. 5 (1974), 138--146](https://epubs.siam.org/doi/10.1137/0505015).
No inaccessible theorem proof or stronger infinite-dimensional hypothesis
is imported: equations (5)--(9) provide the entire argument needed here.

## 4. Exact actual-source witness, including an excited omitted mode

Use the cubic `2^3` lattice at spacing one and scalar `m^2=2`. Order sites
lexicographically. The scalar initial profile is a multiple of a site delta:

\[
 \phi=\lambda\delta_{(0,0,0)},\qquad \lambda>0.
\]

For `q=(pi,pi,0)` the actual orthonormal-component TT polarization is

\[
 e_+=(1,1,-2,0,0,\sqrt2)^T/\sqrt8,
 \quad w_q(x)=(-1)^{x_1+x_2}/\sqrt8,
 \quad \ell(q)=8.
 \tag{10}
\]

The off-diagonal slots are `(yz,xz,xy)` and already carry the required
orthonormal `sqrt(2)` weight. The companion checks the actual staggered
divergence matrix annihilates (10), the trace is zero, and the real spatial
mode is normalized. On this lattice each nonzero wave vector is its own
negative: there is one real coordinate per polarization, not two copies.

Reconstructing the original Ward formulas gives exactly

\[
 \tau_+(\phi)=\frac14\bigl[
 (\phi_{000}-\phi_{110})^2+(\phi_{001}-\phi_{111})^2
 -(\phi_{010}-\phi_{100})^2-(\phi_{011}-\phi_{101})^2\bigr],
\]
\[
 \tau_+(\delta_{000})=\frac14,\qquad V_m(\delta_{000})=4.
 \tag{11}
\]

Set only this TT coordinate initially to
`Q_+=-sign(g) lambda`; all other TT coordinates initially vanish.
The combined initial configuration then satisfies

\[
 |x_0|^2=2\lambda^2,\quad
 V_2(x_0)=8\lambda^2,\quad
 V_3(x_0)=-|g|\lambda^3/4.
\]

Choose the **full** initial momentum parallel to this configuration:

\[
 p_0=a x_0,\qquad a=\sqrt{|g|\lambda}/4.
 \tag{12}
\]

Then

\[
 T_0=|g|\lambda^3/16,\quad
 E=8\lambda^2-3|g|\lambda^3/16<0
       \quad\text{if}\quad\lambda>128/(3|g|),
\]
\[
 F'_0=\sqrt{|g|}\lambda^{5/2}>0,\qquad
 T_{\max}\le8/\sqrt{|g|\lambda}.
 \tag{13}
\]

Thus for each fixed nonzero `g`, the upper bound can be made arbitrarily
small by increasing the actual initial amplitude. For `g=1,lambda=64`,

\[
 E=-16384,\quad F_0=8192,\quad F'_0=32768,
 \quad F''_0=327680,\quad T_{\max}\le1.
 \tag{14}
\]

This is not a purported one-mode exact solution. For example the different
TT mode `q'=(pi,0,pi)` with polarization
`(1,-2,1,0,sqrt(2),0)/sqrt(8)` is initially zero but has

\[
 \tau'_{+}(\phi)=\lambda^2/4,\qquad
 \dot P'_{+}(0)=-g\lambda^2/4\ne0.
 \tag{15}
\]

It is immediately excited. The checker constructs all seven nonzero
momentum sectors and both polarizations in each, and verifies (5)--(7)
symbolically on the resulting full 22-coordinate, 44-dimensional phase
space. No assumption about the subsequent Fourier support is used.

## 5. What survives on nearby regular characteristics

There is a concrete continuous family approaching this stationary fiber.
Use the one constraint momentum sector `q=(pi,pi,0)` from Round13, with
propagation row `b=(2,2,0)`. Choose

\[
 v_\varepsilon=(\varepsilon/2,0,0),\qquad
 r_\varepsilon(t)=\varepsilon t,
 \quad y=0,
\]

and set every other constraint label to zero. For every `epsilon!=0`,
`bv=epsilon!=0`, so this is a regular actual characteristic. Its full
physical time-dependent Hamiltonian equals (1) plus

\[
 g\varepsilon t\,\mathcal B
 -g\varepsilon v_*^TB_vJ_v
 +\frac12\varepsilon^2t^2 B_H
 +\frac12\varepsilon^2v_*^TB_vv_*.
 \tag{16}
\]

Here `v_*=(1/2,0,0)` and all source operators are exactly Round13's actual
quadratic polynomials, acting on the full matter system. No other TT mode
is removed. The last two terms do not affect the physical classical flow.
The physical vector fields converge smoothly to the stationary one on
every compact phase-space/time set as `epsilon->0`.

Fix the datum (14). Given any finite target radius `R`, its stationary
escaping trajectory has a time `t_R<T_max<=1` at which `|x(t_R)|>2R`.
Its segment up to `t_R` is compact. ODE continuous dependence therefore
gives `delta_R>0` such that every sufficiently small nonzero `epsilon`
has a solution through `t_R` with `|x_epsilon(t_R)|>R`.

In particular there is no uniform classical amplitude bound on `[0,1]`
over all sufficiently nearby regular labels and this fixed initial datum.
But `epsilon` is permitted to shrink with `R`. Exchanging the quantifiers
to obtain a single regular label escaping to infinity would be invalid.
No statement about the existence or nonexistence of each individual
regular-fiber quantum propagator follows from this continuity argument.

## 6. A separate rigorous quantum conclusion, not a deficiency argument

For the stationary physical differential expression, take normalized
unit-width product Gaussians on all 22 coordinates,

\[
 \psi_\lambda(x)=\pi^{-22/4}
      \exp(-|x-x_\lambda|^2/2),
\]

with `x_lambda` as in (11)--(13) but zero mean momentum. Every such vector
is Schwartz. Its position and momentum covariances are `I/2`. The full
free quadratic matrix has trace `160`: scalar trace `64` plus TT trace
`96`. Hence its Gaussian expectation is the center's free potential plus

\[
 (22+160)/4=91/2.
\]

Every nonzero-momentum TT source has zero scalar Hessian trace, checked
for all fourteen modes. Its isotropic Gaussian contraction vanishes.
Independence of the scalar and TT Gaussian coordinates therefore gives,
at `g=1`, the **exact** expectation

\[
 \langle\psi_\lambda,h\psi_\lambda\rangle
       =8\lambda^2-\lambda^3/4+91/2\longrightarrow-\infty.
 \tag{17}
\]

Reversing the TT displacement changes the cubic sign and gives `+infinity`.
Every self-adjoint extension containing this minimal Schwartz operator,
if chosen, has these same expectations and is unbounded in both directions.
In particular there is no semibounded Friedrichs extension of this actual
stationary physical minimal operator.

For any fixed finite regular label/time and auxiliary parameter, the
remaining actual terms in (7) of Round13 are at most quadratic in the
physical phase coordinates. Their expectations on the same translated
Gaussians grow at most as `O(lambda^2)`. They cannot cancel the nonzero
`lambda^3` coefficient. The same statement holds for the full minimal
operator after tensoring with one normalized smooth compactly supported
function of the constraint and auxiliary coordinates: label transport is
independent of the physical displacement, and all parameter coefficients
are bounded on that support. Thus two-sided lack of semiboundedness is
not confined to a measure-zero quantum sector.

Neither (17) nor classical incompleteness computes deficiency indices.
An actual proof of extra boundary data would need to analyze the adjoint
domain, construct deficiency vectors, or prove a relevant limit-circle
criterion for the full coupled differential expression. No such step is
claimed here. In particular a potential's cubic descent cannot simply be
treated as an independently quantized one-dimensional channel: the
transverse degrees of freedom and their boundary coupling remain present.

## 7. Relation to the Hermite leakage criterion

A finite Hermite matrix has a global finite-dimensional unitary propagator.
This fact is compatible with every result above. The limit is the issue.
Classical amplitude growth does not itself give quantum mass loss, a lower
bound on the Hermite-tail norm, or failure of a Duhamel error certificate.

There is an important quantifier check for such a certificate. Suppose
the same Galerkin sequence `U_N` satisfies, for **every** self-adjoint
extension `H` of the fixed minimal operator and every vector in one dense
test class, a common bound

\[
 \|U_H(t)f-U_N(t)f\|\le\mathcal E_N(t,f),\qquad
 \mathcal E_N(t,f)\longrightarrow0.
 \tag{18}
\]

If (18) holds for both signs of time, any two such unitary groups coincide
on that dense class by the triangle inequality, then on the full Hilbert
space by boundedness. Stone uniqueness makes the self-adjoint extensions
identical. Given existence of at least one extension, this proves essential
self-adjointness of the minimal symmetric operator, not merely existence
of one covariant extension. Boundary-sensitive convergence to a particular
extension could be a weaker result. Nothing in this escape certificate
decides which situation the actual minimal operator has.

## 8. Reproduction and provenance

Run `python3 escape_check.py` with SymPy. The checker is portable and has
no repository imports. It reconstructs the exact source formulas from
`free-scalar-3d/free_scalar_ward.py` and the staggered TT divergence symbol
used in Round13. Its tests stay active under Python optimization.

It verifies all fourteen TT modes, the complete source's homogeneity and
Gaussian contractions, the full 44-dimensional radial identities, the
negative-energy family, immediate excitation of another TT mode, the
positive-completion negative control, and the full Gaussian constant.
The finite-time theorem is the analytical proof in Section 3, not an ODE
simulation. No deficiency, regulator limit, physical gravitational
completion, or RH result is obtained from the finite certificates.
