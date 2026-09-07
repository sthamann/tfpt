# Unreduced finite quantum Hamiltonian: measurable extension existence

Date: 2026-09-06. Bounded independent analysis of the **actual** scalar/stress
seed Hamiltonian in `mixed-constraints-round11`, not a new positive lift.
Locally integrated research; no RH work, microscopic selection or TOE closure.

## 1. The precise partial result

For the fixed finite model, choose Weyl ordering of the already specified
seed expression

\[
 H_{\rm sa}(g)=H_f+gW+\tfrac12 y^TKy+g\lambda^T\tau,
 \qquad W=V_1-\{H_f,S\},\quad S=-X^aJ_a.
 \tag{1}
\]

The auxiliary momenta do not occur in (1). For every real `g` there exists
a self-adjoint operator on the full kinematic Hilbert space that is
decomposable over `y` and agrees **exactly** with the Weyl-ordered
expression (1) on its Schwartz test domain. One can choose its fiber
resolvents measurably jointly in `(g,y)`. The selection can preserve the
actual time-reversal conjugation. This is an existence result without
changing the seed off-shell expression or importing reduced positivity.

What this proves and what it does not are importantly different:

- Existence of a self-adjoint extension and unitary evolution for that
  selected extension is proved.
- Essential self-adjointness of (1), uniqueness of the extension, a
  physically selected boundary condition, and strong constraint propagation
  are **not** proved. Nor is nonuniqueness for the actual operator proved:
  its deficiency indices have not been computed.
- The given expression on Schwartz space is preserved, but Schwartz is
  not asserted to be an operator core of a possibly proper extension.
- No extension of the unchanged full expression can be bounded below.
  This obstruction is proved directly using its actual auxiliary Hessian.
- Simultaneous quantum dressing is allowed, but must use its declared
  unitary ordering. It is not silently identified with Weyl quantization
  of every term of the classically dressed symbol.

The construction treats either the retained nonzero-mode auxiliary `K` or
the subsequently enlarged, invertible global auxiliary `K`. The gravity
coordinate space itself still excludes homogeneous gravity. Neither this
analysis nor the global auxiliary bookkeeping restores that receiver.

## 2. The actual antiunitary symmetry, including its Darboux sign

Use real original nonzero-mode gravity configuration coordinates `q` and
matter coordinates `phi`. These give a Schrödinger space
`H_seed=L2(R^(6(n-1)+n))`. Ordinary complex conjugation `Theta` fixes
`q,phi`, reverses `p,pi`, and obeys `Theta^2=I`.

The actual data have the following time-reversal parities:

\[
 H_0,H_m,V_1,\rho,\tau:\ +1,\qquad j_i:\ -1.
 \tag{2}
\]

Here `H_0` contains only real `qq` and `pp` quadratic terms, not `qp`
terms. The scalar density contains `pi^2`, `phi^2` and gradient squares.
The link current is `-(pi_x+pi_(x+e_i))D_i phi/2`. Every stress component
in the actual R8.1–R8.3 formulas is even in the matter momenta. Finally
`V_1=q:tau`. All assertions survive real smearing and deletion of gravity
means.

The real chart has `c_H` linear in `q`, `c_i` linear in `p`, and

\[
 X_H\text{ linear in }p,\qquad X_i\text{ linear in }q.
\]

Thus `X_H` is odd and `X_i` even; `J_H=rho` is even and `J_i=-j_i` odd.
The generator `S=-X_H J_H-X_iJ_i` is therefore odd. Time reversal is
antisymplectic, so for classical symbols

\[
 \mathcal T\{f,h\}=-\{\mathcal Tf,\mathcal Th\}.
\]

It follows that `D H_f={H_f,S}` is even, hence so is `W=V_1-DH_f`.
Take every auxiliary position `y=(E,u,lambda)` even. Both remaining
terms in (1) are then even as well. Weyl ordering transports this symbol
identity to the exact antiunitary identity

\[
 \Theta\widehat H_{{\rm sa},\min}(g;y)\Theta
       =\widehat H_{{\rm sa},\min}(g;y)
 \tag{3}
\]

on a `Theta`-invariant Schwartz domain, for every fixed real `(g,y)`.
The full seed expression has total polynomial degree at most three and
total momentum degree at most two. In original `q,phi` coordinates it
is a real, formally symmetric polynomial differential operator of order
at most two. No ellipticity, semiboundedness or completeness of its
classical Hamiltonian flow is being assumed.

**Do not use plain complex conjugation in every Darboux representation.**
When all `X` are represented as configuration variables, the transported
antiunitary is complex conjugation **combined with reflection of every
`X_H` coordinate**. It sends `(X_H,c_H)` to `(-X_H,c_H)` and `(X_i,c_i)`
to `(X_i,-c_i)`. The original-coordinate conjugation, or its exact
metaplectic transport, supplies the fixed antiunitary required below.

## 3. A fixed countable minimal domain

Let `e_1,e_2,...` be the usual real tensor Hermite basis of `H_seed`, in
any fixed enumeration, and let `D_fin` be its finite complex linear span.
For `t=(g,y)` write `L_t` for (1) acting on `D_fin` and `T_t=closure(L_t)`.
Real Weyl ordering makes `L_t` symmetric, hence closable. Every `L_t e_j`
is a finite Hermite sum with coefficients polynomial in `t`. Thus these
vectors are strongly measurable, indeed continuous, in `t`.

The closures obtained from `D_fin`, from full Schwartz space, or from
`C_c^infinity(R^(6(n-1)+n))` coincide. To see this, Hermite expansions of
a Schwartz function converge in every Schwartz seminorm, and polynomial
differential operators are continuous for those seminorms. Conversely,
smooth spatial cutoffs approximate each Hermite function, and more
generally each Schwartz function, in the operator graph norm because
all cutoff commutator terms have polynomial coefficients and decay
rapidly. This comparison is for each fixed parameter; no uniform graph
domain in `g,y` is asserted.

The standard real-symmetric extension criterion says that (3) pairs the
deficiency spaces

\[
 N_+(t)=\ker(T_t^*-i),\qquad
 N_-(t)=\ker(T_t^*+i),\qquad \Theta N_+(t)=N_-(t).
 \tag{4}
\]

This follows directly by applying the antiunitary to the adjoint equation;
`Theta T_t^* = T_t^* Theta` and `Theta i=-i Theta`. The two dimensions
are equal, possibly zero or infinite, so every individual fiber admits
self-adjoint extensions. The standard extension criterion is stated in
[Teschl, *Mathematical Methods in Quantum Mechanics*, Theorems 2.27 and
2.29, printed pp. 92–93](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
Fiberwise existence alone is not yet sufficient to form a direct integral;
the next section supplies the missing measurability explicitly.

## 4. Constructive measurable selection by Cayley transforms

This section gives a countable construction, not an unspecified choice of
one extension independently at every point. It uses ordinary Hilbert-space
limits, not a finite CCR approximation or a numerically computed
deficiency cutoff.

For each `t` define the paired vectors

\[
 b_j(t)=(L_t+i)e_j,\qquad a_j(t)=(L_t-i)e_j.
 \tag{5}
\]

Symmetry gives identical Gram matrices for these two sequences:
`<(T+i)f,(T+i)h>=<(T-i)f,(T-i)h>` on `D_fin`. Apply Gram–Schmidt to the
`b_j`, and apply the same finite subtraction/normalization coefficients
to the paired `a_j`. This gives measurable orthonormal sequences
`b'_j,a'_j`. No `b_j` step is zero: a finite combination with coefficient
one on `e_j` has norm at least one after applying `T_t+i`, since

\[
 \|(T_t+i)f\|^2=\|T_tf\|^2+\|f\|^2.
\]

Their closed spans are `Ran(T_t+i)` and `Ran(T_t-i)`. These ranges are
closed by the same norm identity, and `D_fin` is graph-dense by definition.
The strong limits

\[
 V_0(t)=\sum_j |a'_j(t)\rangle\langle b'_j(t)|,
 \qquad
 P_+(t)=I-\sum_j|b'_j(t)\rangle\langle b'_j(t)|
 \tag{6}
\]

are therefore measurable. `V_0` is the partial Cayley isometry from
`Ran(T+i)` to `Ran(T-i)`, extended by zero on `N_+`; `P_+` projects onto
`N_+`.

Apply Gram–Schmidt to `P_+(t)e_1,P_+(t)e_2,...`, setting a normalized vector
to zero whenever its residual norm is zero. Every operation is Borel
measurable: the positive-norm set is measurable, and division only occurs
there. The resulting sequence `h_j(t)`, including possible zero entries,
has its nonzero entries an orthonormal basis of `N_+(t)`. Define the
**linear**, rather than anti-linear, partial isometry

\[
 U(t)=\sum_j |\Theta h_j(t)\rangle\langle h_j(t)|.
 \tag{7}
\]

It sends `N_+` unitarily onto `N_-` and vanishes on its orthogonal
complement. Its matrix entries and its strong action on every fixed
vector are measurable by the convergent series. Both (6) and (7) have
operator norm at most one. The full operator

\[
 V(t)=V_0(t)-U(t)
 \tag{8}
\]

is unitary: the two initial spaces are orthogonal complements, as are
the two final spaces. It has no eigenvector at one. Indeed

\[
 (I-V(t))(T_t+i)e_j=2i e_j,
 \tag{9}
\]

so `Ran(I-V(t))` is dense; for a unitary this excludes the eigenvalue one.
The inverse Cayley transform therefore gives a self-adjoint extension

\[
 A_t=i(I+V(t))(I-V(t))^{-1},\qquad
 \operatorname{Dom}(A_t)=\operatorname{Ran}(I-V(t)),
\]
\[
 (A_t+i)^{-1}=\frac{I-V(t)}{2i},\qquad
 \|(A_t+i)^{-1}\|\le1.
 \tag{10}
\]

This resolvent is strongly measurable jointly in `(g,y)`. Equation (9)
also directly verifies `A_t e_j=L_t e_j`. The minus sign in (8) is
consistent with the usual plus-sign von Neumann domain

\[
 \operatorname{Dom}(A_t)=\operatorname{Dom}(T_t)
 \dotplus\{h+U(t)h:h\in N_+(t)\},
\]
\[
 A_t(f+h+Uh)=T_tf+ih-iUh.
 \tag{11}
\]

For the particular basis construction (7), `Theta U Theta=U^*` on the
deficiency spaces, so (11) is `Theta`-invariant and `A_t Theta=Theta A_t`
on its full domain. The only external extension input in this construction
is the Cayley/von Neumann correspondence; see
[Teschl, Theorem 2.26 and Lemma 2.28](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
Measurability was proved above, rather than inferred from existence of
the individual extensions.

This construction supplies a selection relative to a fixed basis and its
enumeration. It is not a physically canonical prescription. If a fiber
is essentially self-adjoint, `P_+=0` there and no extension freedom remains.
If its indices are nonzero, other deficiency isometries may select other
extensions. Which case actually occurs for interacting fibers remains open.

## 5. The direct-integral operator and its exact test-domain action

For a fixed real `g`, take the direct integral of the measurable unitaries
`V(g,y)` on `L2(R^d_y;H_seed)`. It is unitary and has no eigenvector at
one, by the fiberwise result and Fubini. Its inverse Cayley transform is
therefore self-adjoint. Equivalently it is

\[
 A_g=\int_{\mathbb R^d}^{\oplus} A_{g,y}\,dy,
\]
\[
 \operatorname{Dom}(A_g)=\left\{\psi:
 \psi(y)\in\operatorname{Dom}(A_{g,y})\ \text{a.e.},\quad
 \int\|A_{g,y}\psi(y)\|^2dy<\infty\right\}.
 \tag{12}
\]

Its resolvent is the direct integral of the uniformly bounded resolvents
in (10). This proves the self-adjointness of (12), rather than assuming
that arbitrary independently selected fiber domains form an operator.

Every jointly Schwartz function belongs to (12), and (12) acts there as
the original expression (1). Pointwise this follows because each fiber
extension contains the minimal Schwartz-domain operator. Integrated graph
norms are finite because coefficients in (1) grow only polynomially in
the auxiliary parameters. In particular no cubic interaction, auxiliary
source term, or higher prescribed **seed** term has been discarded.
Schwartz is an invariant test domain for the differential expression;
it is not asserted to be a core for a selected proper extension.

As a decomposable operator, `A_g` strongly commutes with bounded functions
of the auxiliary positions `y`. This is consistent with the absence of
`p_y` in (1), but it is not the full constrained physical-time evolution.
Classical auxiliary preservation uses the total Hamiltonian with the
additional fixed-multiplier terms `mu^T p_y`; the strong quantum domain
of such a total Hamiltonian is not constructed here.

At `g=0` the full expression is a real quadratic Hamiltonian plus the
quadratic auxiliary multiplication function. It is essentially
self-adjoint on Schwartz space, so (12) agrees with its unique free
closure. Moreover `A_g` tends to `A_0` in the strong resolvent sense as
`g -> 0`, irrespective of any interacting extension freedom. For a
Schwartz `f`, `(A_g-A_0)f=g(W+lambda^T tau)f -> 0`. On the dense set
`(A_0+i)Schwartz` the resolvent difference is bounded by that norm, using
`||(A_g+i)^(-1)||<=1`; density extends convergence to the full Hilbert
space. This is a continuity statement at the known free operator only.
It proves neither an analytic family of closed operators nor a common
graph domain or differentiability at arbitrary interacting coupling.

## 6. No semibounded extension of the unchanged full operator

This obstruction uses the actual local tensor Hessian, not a generic
counterexample substituted for the model. For a retained real nonzero
mode, choose a normalized TT tensor `w`, and use the auxiliary vector

\[
 v=(D^Tw,0,w),\qquad DD^T=\ell I,\qquad N^Tw=0.
\]

For the actual `K` of (1),

\[
 v^TKv=\|D^Tw\|^2-2w^TDD^Tw=-\ell<0.
 \tag{13}
\]

Fix normalized smooth compactly supported seed and auxiliary wave packets
`f,chi`, and translate the latter by `tv`. Every
`psi_t(y,z)=chi(y-tv)f(z)` belongs to the common minimal test domain.
Because the auxiliary source is linear in `y`, direct expansion gives

\[
 \langle\psi_t,A_g\psi_t\rangle
 =-\frac\ell2 t^2+O(t)+O(1)\longrightarrow-\infty.
 \tag{14}
\]

All extensions agreeing with (1) on the test domain have these same
expectations. Consequently **none** can be bounded below. The checked
actual `(pi,pi,0)` mode has `ell=8` and coefficient `-4t^2`.
Reduced positivity after eliminating second-class variables does not
contradict this unreduced statement. Unboundedness below does not forbid
self-adjointness or real-time unitary evolution; it forbids promoting the
chosen full operator to a positive Hamiltonian without changing its
off-shell specification or reducing its phase space.

There is also a concrete obstruction to the simplest perturbative domain
argument. Whenever an actual TT stress is nonzero, choose a scalar center
`phi_0` and a TT gravity center `q_0` with
`q_0:tau(phi_0)=gamma!=0`. Set all mean momenta and gauge coordinates to
zero. Translating a fixed normalized Schwartz packet to configuration
center `(t q_0,t phi_0)` gives

\[
 \langle f_t,\widehat W f_t\rangle=\gamma t^3+O(t),\qquad
 \|B_y f_t\|=O(t^2),
 \tag{14a}
\]

for any fixed quadratic free/frozen-source comparison operator
`B_y=H_f+g lambda^T tau+y^TKy/2`. The first identity follows from the
nonzero homogeneous cubic symbol and a centered packet; the second from
the degree-two translated polynomial differential expression. Hence
`||W f_t||>=|<f_t,W f_t>|` excludes any relative bound
`||Wf||<=a||B_y f||+b||f||`, even with arbitrarily large finite `a,b`.
The straightforward Kato–Rellich argument around this quadratic fiber is
therefore unavailable at nonzero coupling. This is not a proof of failure
of essential self-adjointness; other comparison operators or domain
arguments might still succeed. The checker supplies a nonzero actual
TT packet with `gamma=9/16` and the exact cubic/quadratic degree comparison.

## 7. What unitary dressing preserves, and the ordering distinction

Let `U_g=exp(-ig X^a J_a)` be the rigorously defined finite-quadratic
dressing unitary. It acts trivially on `y`. Then

\[
 \mathcal A_g=U_g A_g U_g^*,\qquad
 \operatorname{Dom}(\mathcal A_g)=U_g\operatorname{Dom}(A_g)
 \tag{15}
\]

is self-adjoint. On the compact-`X`, Schwartz-valued invariant test domain
from the mixed-constraint theorem, it agrees with conjugation of the
specified seed Weyl operator. Its first-order expression is exactly
`V_1+lambda^T tau`: the commutator with the quadratic `H_f` equals the
classical first Poisson derivative, with no first-order Moyal correction.
These are test-domain expression identities, not an analytic family or
an operator-norm perturbation statement. No positive new lift is used.

There is a separate issue if “preserve every off-shell vertex” is intended
to mean Weyl-quantize every coefficient of the *classical* dressed symbol.
That prescription need not coincide with (15). Put `hbar=1` and let
`P^3` be the third contraction with the full canonical Poisson tensor.
For cubic seed symbols,

\[
 i[\widehat S,\operatorname{Op}_W(B)]
 =\operatorname{Op}_W\!\left(\{B,S\}
                              +\tfrac1{24}P^3(S,B)\right).
\]

Thus the difference at order `g^2` between unitary conjugation of the
seed-Weyl operator and Weyl quantization of the classical dressed seed
is the scalar

\[
 \delta_2=\frac1{48}P^3(S,DH_f)+\frac1{24}P^3(S,W).
 \tag{16}
\]

The auxiliary source has no `c` dependence, so it supplies no such
contraction at this order. In the **actual-source single retained-mode
witness**, with the normalized real `(pi,pi,0)` mode on `L=2`, `a=1`
and `m^2=2`, two independent exact contractions give

\[
 P^3(S,DH_f)=3/8,\qquad P^3(S,W)=-3/4,
 \qquad\delta_2=-3/128.
 \tag{17}
\]

This is not advertised as the scalar for the full all-mode Hamiltonian.
It is a non-vacuous witness built from the actual stress, chart and free
gravity mode, showing why the two quantization prescriptions cannot simply
be equated in general. An independent arbitrary-function test fixes the
sign: for `J=(u^2+p^2)/2`, `Jhat^2=Op_W(J^2)-I/4`; conjugating `c^2/2`
therefore differs from `Op_W((c+gJ)^2/2)` by `-g^2 I/8`.

The existence result for (1) preserves the declared seed Weyl expression
exactly. Equation (15) preserves it by its declared unitary quantum
ordering. If a different all-orders ordering has been prescribed, that
different formal expression needs its own symmetry/domain audit; this
note does not rename an ordering correction as an unchanged coefficient.

## 8. Why strong gravitational stabilization still remains open

The classical and common-test-domain identities
`{c,H_sa}=Ac` and `[c,Hhat_sa]=i A c` do not imply the corresponding
identity on the domains of the selected self-adjoint extensions. They
do not show that Hamiltonian evolution preserves those domains or
transports the joint spectral measure of `c` by the expected linear flow.
The same warning applies to `p_y`, whose action differentiates the
parameter in the fiber selection; mere measurability is not enough to
control that derivative.

The exact Darboux structure identifies a possible next problem. The
strong classical identity forces

\[
 H_{\rm sa}=-X^aA_a{}^b c_b+h(c,z,y).
 \tag{18}
\]

Weyl ordering and Fourier transformation in `X` turn the first term into
the complete linear transport generator

\[
 -i\left[(A c)\cdot\partial_c+\tfrac12\operatorname{tr}A\right].
 \tag{19}
\]

The remaining operator is an unbounded matter/TT Hamiltonian depending
on `c,y`. A self-adjoint realization with the desired full constraint
covariance would require compatible domains and propagation along these
linear `c`-characteristics. The arbitrary measurable selection constructed
over `y` does not prove that compatibility.

Even for a truly commuting symmetry group, extension invariance requires
the deficiency isometry to intertwine the group representations; it is
not automatic from formal symmetry. This precise extra condition is
[Ibort–Lledó–Pérez-Pardo, *On self-adjoint extensions and quantum symmetries*,
Theorem 3.6](https://arxiv.org/html/1402.5537v2). Here the nonzero propagation
matrix makes the required covariance more general than plain commutation.
No assertion of complete quantum constraint dynamics follows from the
extension existence theorem.

### A precise sufficient condition for a future covariant extension

The missing dynamical hypothesis can be formulated independently of the
arbitrary Cayley selection. Let `c_0` denote an initial constraint momentum.
Suppose the formal operator family `h(e^(At)c_0,z,y)` admits unitary
propagators `K_y(t,c_0)` that are strongly measurable in their parameters,
strongly continuous in `t`, and satisfy

\[
 K_y(0,c_0)=I,\qquad
 K_y(t+s,c_0)=K_y(t,e^{As}c_0)K_y(s,c_0).
 \tag{20}
\]

Require also their correct test-domain differentiation: on the actual Schwartz matter/TT test space, `(K_y(t,e^(-At)c)-I)/t` tends to `-i h(c,z,y)`, with
locally uniform bounds in `c,y` sufficient to integrate compactly
supported test fields. Require these tensor-product test fields to be graph-dense
in the actual minimal polynomial differential operator (cutoffs and Schwartz
approximation give the relevant core comparison). Mere Hilbert-space density
of an unrelated test space would not suffice. This is the nonautonomous quantum well-posedness
condition for the Hamiltonians along the complete linear characteristics;
it is not implied by selecting an arbitrary self-adjoint fiber at each
point.

Then the explicit operators

\[
 (G_t\psi)(c,y)=e^{-t\operatorname{tr}A/2}
 K_y(t,e^{-At}c)\psi(e^{-At}c,y)
 \tag{21}
\]

form a strongly continuous unitary group. Norm preservation follows from
the Jacobian of `c=e^(At)c_0`; the group law follows from (20); strong
continuity follows by writing `G_t=T_t M_{K_y(t,c)}`, with `T_t` the
half-density pullback. The norm difference is bounded by
`||(K_y(t,c)-I)psi||+||T_t psi-psi||`, which tends to zero by dominated
convergence and strong continuity of `T_t`. No continuity in `c` is silently
assumed. Differentiating on
the stated test fields gives exactly (18)–(19), so Stone's generator is
a self-adjoint extension of the prescribed Fourier-transformed seed
operator. In addition, for every bounded Borel function `f`,

\[
 G_t^* M_{f(c)}G_t=M_{f(e^{At}c)}.
 \tag{22}
\]

Thus this **additional propagator hypothesis** would supply strong
gravitational constraint covariance, with no change to the formal seed
vertices. Existence of this compatible family for the actual `h` is not
proved here. Nor would (22) alone give the additional `p_y`-multiplier
domain theorem for the full second-class total Hamiltonian. Equations
(20)–(22) isolate a sufficient next condition instead of mistaking
measurable extension existence for that condition.

## 9. Reproduction and evidence typing

Run `python3 unreduced_domain_checker.py` with SymPy. The final run passes
**40/40 exact checks**, with no floating-point checks. The checker contains
no repository imports. It independently builds the actual anchored-real
`L=2`, `(pi,pi,0)` scalar/vector chart and free gravity block, the fixed
R8 density, link current and stress, and the corresponding `S,W`.
It tests the exact Ward identities before using the parity conclusion.
The TT stress and the second-order differential terms in `W` are both
required to be nonzero, so zero interaction is not accepted as a witness.

The negative auxiliary packet coefficient and the cubic ordering scalar
are exact. The latter is evaluated independently both by monomial
contraction and by matter Hessian contraction with the gravitational
Poisson tensor. Cayley signs are separately checked; a nonconstant scalar
fiber phase checks the conditional characteristic formula's cocycle,
half-density and generator. These are finite
algebraic controls; the measurable Hilbert-space extension result rests
on the proof in sections 3–5, not on finite-dimensional matrices.

The outcome is a genuine but limited domain advance: existence of a
measurably selectable unreduced self-adjoint extension of the specified
seed operator, plus a proof that its full spectrum cannot be bounded
below. Essential self-adjointness, physical extension selection, strong
mixed-constraint dynamics, a TFPT physical inner product, locality and
continuum limits remain separate obligations.
