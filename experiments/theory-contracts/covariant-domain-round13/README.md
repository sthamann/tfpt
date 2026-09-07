# Actual constraint-characteristic dynamics: normal form and domain barriers

Date: 2026-09-06. Independent Round13 analysis of the unchanged finite
`mixed-constraints-round11` seed Weyl Hamiltonian. No RH work,
positive replacement lift, homogeneous gravity restoration, or TOE claim.

## 1. Outcome

**A strongly constraint-covariant self-adjoint realization at nonzero coupling
is not constructed here.** The result is a sharper actual normal form, a
constructive sequence of symmetry-preserving finite-rank approximants, and
several exact obstructions to proposed shortcuts. None is a no-go against
every possible covariant extension of the actual operator.

The new facts are:

- The actual propagation matrix is nilpotent of order two and rank `n-1`.
  Its regular characteristics are affine lines with a global orbit coordinate.
- The remaining physical Hamiltonian is affine in that coordinate, modulo
  an explicitly removable scalar quadratic term. Its coefficient is an
  actual nonzero quadratic matter operator, not a scalar.
- An actual-source single-mode characteristic passes through a degenerate
  matter kinetic matrix and then an indefinite one. Uniform positive
  ellipticity on the entire characteristic is false.
- Neither a scalar phase nor just the available quadratic metaplectic flow
  solves the interacting characteristic equation: the requisite operators
  do not commute. A usual global oscillator-moment Gronwall estimate also
  fails for every fixed positive integral power of the oscillator number.
- If a full covariant self-adjoint extension exists, it must have purely
  absolutely continuous spectrum equal to the whole real line on the
  regular kinematic sector (which has full Lebesgue measure).
- Self-adjointness, time reversal, measurable fibers, and the exact formal
  commutator do not imply strong covariance. An explicit Robin-boundary
  model demonstrates the missing domain condition without claiming to be
  a counterexample to existence for the actual model.

## 2. The actual all-volume propagation matrix and regular orbit chart

Let `m=n-1`, with gravity means already deleted. Write the independent
constraints as `c=(r,v)`, where `r=c_H in R^m` and `v=(c_1,c_2,c_3) in R^(3m)`.
The sign is fixed by the actual scalar continuity identity
`{rho,H_m}=-sum D_i^- j_i` and `J_i=-j_i`. Thus, in real zero-mean coordinates,

\[
 A=\begin{pmatrix}0&b\\0&0\end{pmatrix},\qquad
 b=(D_1^-,D_2^-,D_3^-),\qquad
 A^2=0,\quad \operatorname{tr}A=0.
 \tag{1}
\]

The positive operator `bb^T=-Delta` is invertible on scalar zero-mean
fields. Hence `rank b=rank A=m`. This uses the staggered difference, not
the centered difference with additional corner zeros. The checker confirms
the real-space identities and rank for `L=2,3`; the symbol argument proves
them for every finite periodic `L>=2`.

The flow is `v(t)=v`, `r(t)=r+t d`, where `d=bv`. For `d!=0` define

\[
 s(c)=\frac{d\cdot r}{|d|^2},\qquad r_\perp=r-sd.
 \tag{2}
\]

Then `s(c(t))=s(c)+t` and `r_perp,v` are conserved. The set `bv=0` has
codimension `m` and Lebesgue measure zero. It cannot be silently promoted
to a nonzero kinematic `L2` sector representing the physical constraint
surface. For fixed `v`, `dr=|d| ds dr_perp`; the Jacobian is independent of
`s` and can be absorbed into a unitary half-density. No time-dependent
half-density remains because `tr A=0`.

There is no loss of the common minimal domain from working away from
`bv=0`: cutoffs in `bv` commute with the formal operator, which has no
`v` derivatives. Removing a shrinking neighborhood converges in its
Schwartz test-function graph norm by dominated convergence. Orbit-coordinate
singularities at the excluded null set therefore do not themselves solve
or obstruct the interacting domain problem.

## 3. Exact physical fiber expression, before any auxiliary elimination

To avoid a notation collision, denote the scalar constraint matrix by `S_0`
and the vector matrix by `V`. Let `T` be a real orthonormal TT frame and
put `G_H=S_0 S_0^T`, `G_v=VV^T`. The actual linear Darboux inverse is

\[
 q=TQ+S_0^TG_H^{-1}r+V^TX_v,\qquad
 p=TP-S_0^TX_H+V^TG_v^{-1}v.
 \tag{3}
\]

The verified actual free matrices give

\[
 H_f=H_{\rm TT}+H_m-X_H^Tbv
       +\tfrac12r^TB_Hr+\tfrac12v^TB_vv,
 \tag{4}
\]

where `B_H` has mode symbol `-1/(2 ell)`,
`B_v=G_v^-1 V K_p V^T G_v^-1`, and
`H_TT=sum(P_alpha^2+ell_alpha Q_alpha^2)/2`. In particular there are no
TT/constraint cross terms. The `X_v` quadratic block and `X_H^2` term vanish.

Use `J=(rho,J_v)`, `J_v=-j`, the generator `S=-X^aJ_a`, and the exact
actual first Ward identity. Since `W=V_1-{H_f,S}` is independent of all
`X`, evaluating it at `X=0` is an identity for all `X`, not a reduction:

\[
 W=Q^T\tau_{\rm TT}+r^T\mathcal B-v^TB_vJ_v,\qquad
 \mathcal B=G_H^{-1}S_0\tau-B_H\rho.
 \tag{5}
\]

Here every component of `mathcal B,J_v,tau` is the actual homogeneous
quadratic matter polynomial. Only `tau_TT` is configuration-only.
After Fourier transformation in `X`, the unchanged minimal Weyl operator is

\[
 L_g=-i(bv)\cdot\partial_r+\operatorname{Op}_W h_g(r,v,z,y),
 \tag{6}
\]
\[
 h_g=H_{\rm TT}+H_m+gQ^T\tau_{\rm TT}
       +g r^T\mathcal B-gv^TB_vJ_v+g\lambda^T\tau
       +\tfrac12r^TB_Hr+\tfrac12v^TB_vv+\tfrac12y^TKy.
 \tag{7}
\]

This includes the off-shell `g lambda^T tau` vertex; auxiliary momenta
and their preservation-multiplier terms are still absent, as in Round12.
Linear symplectic changes and Fourier transformation preserve Schwartz
space and Weyl ordering exactly. Thus (6) has precisely the original
minimal operator on full joint Schwartz space, not only on a reduced slice.

On a regular orbit `r=r_perp+s d`, (7) has the form

\[
 h_g(s)=h_*+gs\,d^T\mathcal B+a_0+a_1s+a_2s^2,
 \tag{8}
\]

with `h_*` containing the cubic TT interaction and the frozen quadratic
matter sources. A scalar phase removes the last three scalar terms.
The remaining operator is a genuine nonautonomous cubic Hamiltonian.

## 4. Actual-source nonzero controls and rejected shortcuts

The checker independently reconstructs the R8 scalar density, link current
and stress on `L=2`, spacing one, `m_scalar^2=2`, with the normalized real
mode `(-1)^(x+y)/sqrt(8)`. It verifies the Ward identity before using (5).
This is an **actual-source one-retained-mode witness**. It is not a claim
about the value of a coefficient after summing every mode.

For this mode, `ell=8` and

\[
 b=(2,2,0),\qquad B_H=-1/16,\qquad
 B_v=\frac1{32}\begin{pmatrix}5&-3&0\\-3&5&0\\0&0&8\end{pmatrix},
\]
\[
 \mathcal B=\frac{s_0^T\tau}{128}+\frac\rho{16},\qquad
 s_0=(4,4,8,0,0,4\sqrt2)^T.
 \tag{9}
\]

Take `v=(1/2,0,0)`, `r=s`, and `y=0`; this is a regular characteristic
of speed one. Let `w_x=(-1)^(x+y)/sqrt(8)`. Its matter kinetic Hessian is

\[
 \partial_\pi^2 h_g(s)=I_8+\frac{3gs}{16}\operatorname{diag}(w_x).
 \tag{10}
\]

At `g=1`, `s=32 sqrt(2)/3`, this has four zero and four positive eigenvalues.
At twice that time it has four eigenvalues `-1` and four eigenvalues `3`.
The fixed `v.J_v` term is mixed `phi*pi` and contributes no `pi*pi` term.
The scalar part `-s^2/32` is removed by phase integral `-s^3/96`, but that
does not change (10). Hence a global uniformly positive elliptic kinetic
argument along all characteristics is unavailable. This change of signature
does **not** by itself forbid unitary evolution: even indefinite quadratic
Hamiltonians have well-defined metaplectic evolution.

The checker also verifies
`{mathcal B,Q.tau_TT}!=0` and `{h_*,mathcal B}!=0`. Thus exponentiating the
integral of (8) without time ordering fails. The available unitary
`exp(-ig s^2 mathcal B/2)` merely transfers the time dependence into a
metaplectically conjugated cubic interaction. It does not remove that
interaction. A useful degree control is the exact identity

\[
 \{Q^T\tau_{\rm TT},\{Q^T\tau_{\rm TT},P^TP/2\}\}
       =\tau_{\rm TT}^T\tau_{\rm TT}\ne0.
 \tag{11}
\]

The quadratic-metaplectic theorem does not cover this quartic Lie bracket.
None of these tests proves that every more elaborate gauge construction fails.

There is another actual obstruction to a standard approximation proof.
Let `N` be the physical TT/matter oscillator number plus a positive constant.
For each fixed integer `k>=1`, a bound

\[
 |\langle f,i[\widehat h_g(s),N^k]f\rangle|
       \le C\langle f,N^kf\rangle
 \tag{12}
\]

cannot hold on all Schwartz vectors at nonzero coupling, even at one fixed
`s,v,y`. Indeed the leading symbol is
`g k n^(k-1){Q.tau_TT,n}`, where `n=(|Q|^2+|P|^2+|phi|^2+|pi|^2)/2`.
It has degree `2k+1`, versus degree `2k` on the right (with an overall
minus sign for the displayed `i[H,N^k]` convention). Choose coherent
packet centers on the actual ray
`Q=0`, `P=(1,0)`, `pi=0`, `phi=(-2,1,3,-1,4,0,-4,2)`, then scale every
center by `R`. The checked cubic Poisson coefficient is `3/4`, so the
leading left expectation is nonzero. Quadratic fiber terms and Weyl/Moyal
lower-degree corrections cannot cancel it. Taking `R -> infinity` proves
the failure of (12) for every `k`. Tests for `k=1,2,3` check the general
degree argument. This excludes this particular global Gronwall estimate,
not every possible compactness or boundary estimate.

## 5. A necessary strong spectral consequence for the actual full model

Suppose a self-adjoint extension `H` of (6), on the original kinematic
Hilbert space, has the requested covariance for every bounded Borel `f`:

\[
 U_t^*M_{f(c)}U_t=M_{f(e^{At}c)},\qquad U_t=e^{-itH}.
 \tag{13}
\]

On the full-measure regular set define `M_beta=exp(i beta s(c))` using (2).
It is a bounded unitary, even though `s(c)` is singular near `bv=0`.
Equation (13) yields the exact Weyl relation

\[
 U_t^*M_\beta U_t=e^{i\beta t}M_\beta,
 \qquad M_\beta^*HM_\beta=H+\beta I.
 \tag{14}
\]

The second identity includes `M_beta Dom(H)=Dom(H)`, by uniqueness of
Stone generators. It is an actual necessary **domain** condition; a formal
commutator on Schwartz space does not establish it. In particular the
singular multiplier need not preserve the original Schwartz test domain.

The spectrum must therefore be all of `R`. It is also purely absolutely
continuous. To prove the latter without assuming multiplicity theory,
let `E_H` be its spectral measure and let `B` be a Lebesgue-null Borel set.
For any `psi`, integrate the nonnegative, continuous function
`beta -> <M_beta psi,E_H(B)M_beta psi>`. Spectral translation (14) and
Tonelli give its integral as `|B| ||psi||^2=0`. Continuity forces its value
at zero to vanish. Thus `E_H(B)=0`. A point eigenvalue, singular-continuous
spectral component, or semibounded spectral realization on the regular
kinematic sector would falsify (13).

This is a useful selection obstruction, not a construction. It is entirely
consistent with a positive **reduced** Hamiltonian: the reduced/distributional
constraint surface is not the regular kinematic sector used here.

## 6. Why real symmetry and averaging do not complete the argument

The actual time-reversal conjugation maps `r -> r`, `v -> -v`, and reverses
the physical momenta. It therefore sends `d -> -d` and `s -> -s`, but
also changes the orbit label `v`. The Round12 deficiency pairing is not
automatically a boundary condition local in the conserved `v` labels,
let alone a solution of (14) along every orbit. This observation does not
compute the actual fiber deficiency indices or prove they are unequal.

Here is a fully explicit **model negative control**, not a replacement
for the actual interaction. On `L2(R_s x R_+)` take the minimal expression
`K=-i partial_s-partial_x^2`, with smooth compactly supported interior tests.
Fourier transform in `s`, and at each real `k` choose the self-adjoint
half-line operator `k-partial_x^2` with Robin condition

\[
 \partial_x\widehat f(k,0)=k^2\widehat f(k,0).
 \tag{15}
\]

The Robin resolvents are continuous in `k` (the elementary half-line
Green function has a continuous Robin reflection coefficient at nonreal
spectral parameter), so their direct integral is self-adjoint. It agrees
with the given interior minimal expression. The antiunitary
`Theta f(s,x)=overline(f(-s,x))` fixes its full operator and domain; in
Fourier variables this is ordinary conjugation. Thus self-adjointness,
measurable fibers, real symmetry, and the correct formal Weyl commutator
all hold.

Nevertheless `M_beta f=e^(i beta s)f` shifts the fiber label to `k-beta`.
Its boundary derivative becomes `(k-beta)^2` times the boundary value,
not `k^2` times it. A compactly `k`-supported nonzero packet with profile
`[1+(k^2+1)x]e^(-x)` is an explicit vector in the original domain for
which modulation leaves that domain. The exact defect is
`beta^2-2k beta`. Thus (14) fails. A constant Robin parameter would give
a covariant extension of this model, emphasizing that this is an
obstruction to an **automatic selection argument**, not to all extensions.

Amenability supplies no missing unitary boundary map by simply averaging
one. The average of two unitary maps can be a strict contraction, even
zero: `(I+(-I))/2=0`. Averaging Cayley maps therefore need not preserve a
self-adjoint extension, and averaging resolvents need not preserve the
resolvent identity. An invariant positive functional or a dilation on a
larger Hilbert space would be a different result from (13) on the specified
space. No impossibility of every amenable-extension method is claimed.

The extension-intertwiner issue is a genuine operator-domain condition;
compare [Ibort, Lledo and Perez-Pardo, Theorem 3.6](https://arxiv.org/html/1402.5537v2).
The actual covariance here is semidirect rather than ordinary commutation,
and the explicit model above establishes the relevant negative control.

## 7. Constructive actual approximants, and the precise unproved limit

There is an unconditional symmetry-preserving approximation scheme for
the unchanged expression, not an assumed interacting propagator.
Let `Pi_N` project the physical TT/matter Hilbert space onto total Hermite
degree at most `N`, and set

\[
 h_N(c,y)=\Pi_N\operatorname{Op}_W h_g(c,y)\Pi_N,
 \qquad L_N=-i(bv)\cdot\partial_r+h_N(c,y).
 \tag{16}
\]

On the orthogonal complement, `h_N=0`. For each orbit and fixed `y`, this
is a finite Hermitian matrix with polynomial time coefficients. Its matrix
ODE has a unique global unitary propagator on every finite time interval;
on the complement it is the identity. Coefficients depend continuously on
the parameters, so these propagators are measurable. Combining them with
the exact characteristic pullback defines a strongly continuous unitary
group `U_N(t)` and a self-adjoint `L_N`, with exact covariance (13).
Strong continuity follows from pointwise finite-dimensional continuity,
the unitarity bound, and dominated convergence, not from a uniform bound
over all unbounded parameters.

Every joint Schwartz function lies in `Dom(L_N)`, and `L_N` acts there as
(16). First differentiate compact parameter-supported Hermite-valued tests;
then use Schwartz approximation and parameter cutoffs in the differential
graph norm. Polynomial coefficients control every discarded tail. The
same Hermite argument gives, for each joint Schwartz `f`,

\[
 L_N f\longrightarrow L_g f\quad\hbox{in }L^2.
 \tag{17}
\]

On a fixed finite Hermite vector the physical polynomial, of degree at
most three, has finite Hermite output; its matrix entries eventually agree
exactly with the unchanged operator. General Schwartz convergence follows
from convergence in all Schwartz seminorms. Parameter polynomial weights
are included in the joint seminorms. The prescribed vertices have therefore
not been erased from the limiting minimal expression.

If a subsequence of `L_N` converges in **strong resolvent sense to a
self-adjoint operator on this same Hilbert space**, then that operator
does solve the requested problem. To verify the claim, let `R_N=(L_N+i)^-1`
and `R=(H+i)^-1`. Equation (17), `||R_N||<=1`, and strong convergence imply
`R(L_g+i)f=f` on Schwartz, so `H` contains the full specified minimal
operator. Strong resolvent convergence also gives strong convergence of
the unitary groups on compact time intervals. Passing bounded `M_f`
through those limits preserves (13).

**The actual strong-resolvent subsequence has not been proved to exist.**
Weak compactness is insufficient: weak limits of unitaries can lose norm
and need not obey the composition law. For example bilateral shifts on
`ell2(Z)` converge weakly to zero as the shift tends to infinity. The
uniform oscillator-moment argument that might supply compactness is
specifically unavailable by (12). Other boundary/compactness estimates
remain possible and are the concrete next analytical obligation.

At `g=0` there is no gap: the full real quadratic minimal operator is
essentially self-adjoint on Schwartz; (17) implies convergence to that
unique free closure. Equivalently, its orbit propagator is the free
TT/matter unitary multiplied by the integral of the scalar quadratic
in (7). This free result is not extended to nonzero `g` by assumption.

## 8. Source audit and scope

An apparently attractive general existence shortcut was investigated and
not used. The arXiv primary record for Schlegelmilch--Schnaubelt,
[*Wellposedness of hyperbolic evolution equations in Banach spaces*](https://arxiv.org/abs/math-ph/0507013),
explicitly records withdrawal because of a crucial gap in the main proof.
The related older thesis's broad approximative-evolution assertions are
therefore not imported as an unconditional propagator theorem here. This
does not purport to invalidate unrelated evolution-semigroup results;
such results have additional hypotheses to verify in this model.

The appropriate mathematical boundary remains: the actual unchanged
unreduced operator has a measurably selectable self-adjoint extension by
Round12, but neither that selection nor the actual Galerkin sequence here
has yet supplied the strong constraint-covariant extension at nonzero
coupling. Simultaneous unitary dressing would transport a proved relation
(13), but cannot manufacture it. The auxiliary `p_y` multiplier domain,
equivalence with reduced quantization, microscopic locality, and continuum
limits remain additional questions even if (13) is eventually obtained.

Run `python3 covariant_domain_checker.py` with SymPy. The exact algebra
controls actual normal-form signs, the real nonzero stress, kinetic
crossings and commutators; the Robin/averaging examples are explicitly
labelled MODEL. None of these finite tests substitutes for a proof of an
infinite-dimensional propagator or its strong-resolvent limit.
