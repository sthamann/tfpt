# Actual characteristic Hamiltonians cannot share a fixed operator or form domain

Date: 2026-09-06. Round14, non-RH. This is a new obstruction for the unchanged
finite scalar/TT/auxiliary seed Hamiltonian, not a construction of its missing
strongly constraint-covariant evolution. Locally integrated research; no physical gate is promoted.

## 1. Precise result

Fix any real `g!=0`. Consider the actual `L=2`, spacing-one finite model with
scalar mass squared two, retaining **all** nonzero gravity modes and all eight
scalar variables. Choose the regular constraint characteristic described below,
with auxiliary positions fixed at zero. Let `h_t,min` be its original Weyl
differential expression on physical Schwartz space.

For any two distinct real characteristic times `s,t`, and **any** self-adjoint
extensions `A_s,A_t` of these two minimal operators, if such extensions are
chosen, one necessarily has

\[
 \operatorname{Dom}(A_s)\ne\operatorname{Dom}(A_t),\qquad
 \operatorname{Dom}|A_s|^{1/2}\ne\operatorname{Dom}|A_t|^{1/2}.
 \tag{1}
\]

The second assertion concerns the canonical absolute-value square-root
domains of possibly indefinite self-adjoint operators. It does not assume
semiboundedness or identify an indefinite expression with a Friedrichs form.
The obstruction persists on a nonempty open set of regular orbit labels for
times in a sufficiently small interval. Thus it is not only an exceptional
single-orbit issue which can be discarded in a direct integral.

The proof uses exact displaced Schwartz wave packets. The time-dependent
quadratic coefficient has norm/expectation of order `R^6`, whereas the entire
interacting Hamiltonian acts on those packets with norm at most order `R^5`.
This is stronger than failure of the earlier oscillator-number commutator
estimate: **no boundary choice can repair the required relative bound**, since
all extensions agree on these packets.

This excludes an unchanged common-operator-domain or common-absolute-form-domain
construction for the actual fibers. It does **not** exclude a moving-domain
propagator, a common dense test space, or a common Schwartz core if essential
self-adjointness happens to hold. It also does not prove failure of every Kato
method: a different invariant intermediate space or a controlled moving-domain
trivialization is a genuinely different hypothesis.

## 2. Actual orbit and the coefficient that must be controlled

Use the full normal form established in `covariant-domain-round13`:

\[
 H_{\rm sa}=-i(bv)\cdot\partial_r+h_g(r,v,z,y),
 \quad A=\begin{pmatrix}0&b\\0&0\end{pmatrix},
 \quad b=(D_1^-,D_2^-,D_3^-).
 \tag{2}
\]

The coordinate `t` below is the parameter along a regular `c=(r,v)`
characteristic, not the dressing parameter `g`. Choose the normalized real
mode `w(x)=(-1)^(x_1+x_2)/sqrt(8)`, with `ell=8`. In this one mode set
`v=(1/2,0,0)` and `r=t`, and put every other constraint label and all `y` to
zero. Its speed is one because the actual propagation row is `(2,2,0)`.
No physical TT or matter variable is removed.

The actual fiber is

\[
 h_t=h_0+gtB-t^2/32,
\]
\[
 h_0=H_{\rm TT}+H_m+g\sum_\alpha Q_\alpha T_\alpha(\phi)
             -gv^TB_vJ_v+\tfrac12v^TB_vv,
 \tag{3}
\]

where `J_v=-j` and

\[
 B_v=\frac1{32}\begin{pmatrix}5&-3&0\\-3&5&0\\0&0&8\end{pmatrix},
 \quad
 B=\frac{s_0^T\tau}{128}+\frac\rho{16},
 \quad s_0=(4,4,8,0,0,4\sqrt2)^T.
 \tag{4}
\]

All sources in (3)--(4) are the fixed actual Ward sources. In particular
`B` is a real homogeneous quadratic matter polynomial, and exactly

\[
 \partial_{\pi_i}\partial_{\pi_j}B
      =\frac3{16}w_i\delta_{ij},\qquad
 \partial_\pi^2 h_t=I+\frac{3gt}{16}\operatorname{diag}(w_i).
 \tag{5}
\]

The TT stresses `T_alpha` depend only on `phi`. The vector-current term is
bilinear `phi*pi`. Every other term in (3) is quadratic or scalar. Formula
(3) is the unreduced fiber before auxiliary elimination; there is no positive
`g^2 R` term in it. On other auxiliary fibers the prescribed `g lambda.tau`
term must be retained; setting `y=0` here specifies a particular orbit label,
not a change in the global operator. Section 6 gives the open-label version.

The actual normalized TT pair in this mode uses tensor polarizations

\[
 e_0=(1,1,-2,0,0,\sqrt2)^T/\sqrt8,\qquad
 e_1=(0,0,0,1,-1,0)^T/\sqrt2.
\]

For the actual scalar datum, in lexicographic site order,

\[
 \phi_* =(-2,1,3,-1,4,0,-4,2),\qquad
 (T_0(\phi_*),T_1(\phi_*))=(3/4,0).
 \tag{6}
\]

The checker reconstructs density, all three currents and all six stresses
from their lattice formulas. It does not replace these polynomials by an
invented cubic interaction. Other TT stresses can be nonzero at this datum;
they are retained, as addressed explicitly below.

## 3. Exact displaced-packet bounds

Fix `t` and `g!=0`. Pick a site `i` with sign `sigma=sign(w_i)` aligned
with `gt` (either sign is allowed when `t=0`). Then

\[
 C_i(t)=1+\frac{3gt}{16}w_i
       =1+\frac{3|gt|}{16\sqrt8}\ge1.
 \tag{7}
\]

For `R>=1`, choose phase-space displacement centers

\[
 \phi_R=R^2\phi_*,\qquad
 \pi_R=\frac3{2\sqrt2}R^3 e_i,
 \qquad
 Q_{0,R}=-\frac{3C_i(t)}{4g}R^2,
 \tag{8}
\]

with every other TT configuration center and all TT momentum centers zero.
Let `f` be any fixed normalized Schwartz function of **all** physical
variables and put `f_R=W(z_R)f`, using the unitary Weyl displacement.
Each `f_R` is still Schwartz and normalized. The exact identity

\[
 W(z_R)^*\operatorname{Op}_W(a)W(z_R)
       =\operatorname{Op}_W(a(z+z_R))
 \tag{9}
\]

holds on Schwartz space. It follows directly by conjugating coordinates and
momenta; no asymptotic pseudodifferential approximation is used. Primary
background for Weyl displacements and real quadratic quantization is
[Combescure--Robert, sections 2--4](https://arxiv.org/html/math-ph/0509027v1).

There are only two scalar contributions of order `R^6` in the displaced
Hamiltonian, and they cancel exactly:

\[
 \tfrac12 C_i(t)|\pi_R|^2
       =\frac{9C_i(t)}{16}R^6,
 \qquad
 gQ_{0,R}T_0(\phi_R)
       =-\frac{9C_i(t)}{16}R^6.
 \tag{10}
\]

No operator-valued `R^6` coefficient survives. Replacing any shifted
configuration factor in the cubic vertex by its unshifted operator lowers
the displacement degree by two. Replacing a shifted momentum factor lowers
it by three. The mixed current has maximum degree five; the remaining
configuration quadratics have maximum degree four. Therefore

\[
 W(z_R)^*h_{t,\min}W(z_R)=\sum_{j=0}^5R^jD_j(t,g)
 \quad\hbox{on Schwartz space},
\]
\[
 \|h_{t,\min}f_R\|\le C_{f,t,g}R^5.
 \tag{11}
\]

The `D_j` are finitely many fixed polynomial differential operators, so
their norms on this fixed `f` are finite. This is a bound on the **operator
norm applied to a vector**, not merely cancellation of an energy expectation.

The untouched TT modes do not alter it. Their centers `Q_beta,R` vanish,
so `Q_beta T_beta(phi+R^2 phi_*)` has displacement degree at most four.
Their other oscillator terms have degree zero. This proves the bound for
the full physical fiber, not only for a two-TT-coordinate truncation.

For `B` the leading term does not cancel:

\[
 W(z_R)^*\widehat B W(z_R)
       =\beta_i R^6 I+\sum_{j=0}^4R^jE_j,
\qquad
 \beta_i=\frac{27w_i}{256}
       =\sigma\frac{27\sqrt2}{1024}\ne0.
 \tag{12}
\]

Consequently, for some finite `R_0(f,t,g)` and all `R>=R_0`,

\[
 |\langle f_R,\widehat B f_R\rangle|
       \ge\frac{|\beta_i|}{2}R^6,
 \qquad \|\widehat Bf_R\|\ge\frac{|\beta_i|}{2}R^6.
 \tag{13}
\]

Every self-adjoint extension `A_t` containing the minimal Schwartz operator
has `A_t f_R=h_t,min f_R`. Hence the same bounds hold independently of its
boundary choice. In particular `B` has no finite `A_t`-relative operator
bound on Schwartz space, at any real `t` and nonzero `g` on this orbit.

## 4. No common self-adjoint operator domain

Suppose extensions `A_s,A_t` have the same domain `D`, with `s!=t`.
The graph norms of two closed operators with identical domain are equivalent:
the identity map from `D` with the `A_t` graph norm to `D` with the `A_s`
graph norm has closed graph, since both convergences imply the same Hilbert
limit. The closed graph theorem gives constants `a,b<infinity` such that

\[
 \|A_s f\|\le a\|A_t f\|+b\|f\|\qquad(f\in D).
 \tag{14}
\]

On Schwartz space their difference is prescribed exactly:

\[
 (A_s-A_t)f=g(s-t)\widehat Bf-(s^2-t^2)f/32.
 \tag{15}
\]

Combining (14)--(15) would make `B` relatively bounded by `A_t` on Schwartz
space, contradicting (11)--(13). This proves the first assertion of (1).

One may also formulate (15) on the whole common domain. The real quadratic
`B` is essentially self-adjoint on Schwartz. Testing the adjoint equation
against Schwartz functions shows that every vector in `D` belongs to
`Dom(B)` and that (15) holds there. But this extra observation is not needed
for the contradiction: equality on the original test domain already suffices.

## 5. No common absolute-value form domain either

Suppose instead that
`Q=Dom(|A_s|^(1/2))=Dom(|A_t|^(1/2))`. These are Hilbert spaces with norms

\[
 \|f\|_{Q_t}^2=\|f\|^2+\||A_t|^{1/2}f\|^2.
 \tag{16}
\]

The same closed-graph argument makes the two norms equivalent. The symmetric
spectral forms `a_t` satisfy

\[
 |a_t[f]|\le\||A_t|^{1/2}f\|^2,
 \qquad a_t[f]=\langle f,A_t f\rangle\quad(f\in\operatorname{Dom}A_t).
\]

Thus (15), evaluated on `f_R`, would imply for a finite constant `C`

\[
 |g(s-t)|\,|\langle f_R,Bf_R\rangle|
   \le C\left(1+\||A_t|^{1/2}f_R\|^2\right)
   \le C\left(1+\|A_t f_R\|\right).
 \tag{17}
\]

The last inequality is spectral Cauchy--Schwarz and `||f_R||=1`.
Equations (11) and (13) make the left side grow as `R^6` and the right
side at most as `R^5`, a contradiction. This proves the second assertion
of (1) without any positivity hypothesis for the fibers.

In particular a constant-form-domain theorem cannot be applied to this
family by merely declaring a common form domain. Its required domain equality
is false for every possible pair of extensions of the specified expressions.
For comparison, the hypotheses of the Simon/Kisynski approaches reviewed by
[Balmaseda--Lonigro--Perez-Pardo](https://arxiv.org/abs/2112.11063) include
semiboundedness and a constant form domain. Neither is inferred here, and
their existence theorems are not being invoked outside those hypotheses.

## 6. The obstruction is not supported only on a null orbit label

Fix `g!=0` and a bounded interval around `t=0`. Near the selected regular
orbit, use the smooth transversal where the selected scalar constraint
coordinate is zero. Orbit labels consist of the other scalar coordinates,
the vector constraints, and `y`. The selected velocity component remains
nonzero in a neighborhood, so these are genuine regular local orbit labels.

Write the general nearby family as
`h_t(eta)=h_0(eta)+gt B_d(eta)+a_1(eta)t+a_2(eta)t^2`, retaining every
original auxiliary source term. Its matter kinetic coefficient in the
selected site direction, `C_i(eta,0)`, is continuous and equals one at the
base label. The kinetic coefficient `b_i(eta)=partial_pi_i^2 B_d(eta)` is
also continuous and equals `3/(16 sqrt(8))` for the positive site there.
Choose an open label neighborhood satisfying

\[
 |C_i(\eta,0)-1|<1/4,\qquad
 |b_i(\eta)-b_i(\eta_*)|<|b_i(\eta_*)|/2.
 \tag{18}
\]

After shrinking the time interval so that
`|gt| sup_eta |b_i(eta)|<1/4`, one has `C_i(eta,t)>1/2` and
`b_i(eta)!=0` throughout. Use exactly (8), replacing `C_i(t)` by this
coefficient. The kinetic/cubic cancellation still holds. Other quadratic
kinetic terms have no order-six contribution because only one matter
momentum is displaced; mixed momentum terms contribute at most order three
after that displacement. Every other quadratic or cubic term obeys the
same degree count as before. The coefficient in (12) becomes
`beta_i(eta)=9 b_i(eta)/16`, which stays nonzero.

The proofs of sections 4--5 consequently apply to every orbit in this open
label set, for every pair of distinct times in that interval. Auxiliary
coordinates need not be exactly zero there. This is a positive-measure
obstruction in the regular direct-integral label space, not an inference
from a single measure-zero fiber to an almost-everywhere conclusion.

## 7. What this says about extension and propagator methods

The original task remains open: no actual all-time covariant self-adjoint
realization is constructed. Sections 3--6 rule out a substantial class of
proposed existence proofs, including a fixed-domain perturbative extension
family whose restriction is the unchanged `h_t`, and the analogous constant
absolute-form-domain construction. They do not establish nonexistence of
individual self-adjoint fiber extensions or of a sufficiently controlled
moving-domain propagator.

For clarity there is an elementary **different model** showing why that
distinction matters. On `L2(R)` put

\[
 U_t=e^{-itx^2/2},\quad B_0=p^2-x^2/2,\quad
 H_t=(p+tx)^2=U_t p^2 U_t^*,
\]
\[
 K(t,s)=U_t e^{-i(t-s)B_0}U_s^*.
 \tag{19}
\]

Every `H_t` is a self-adjoint square on `U_t Dom(p^2)`. The real quadratic
`B_0` has its self-adjoint metaplectic realization; the primary quadratic
result cited in section 3 suffices here. Differentiating (19) on Schwartz
space gives

\[
 i(\partial_tU_t)U_t^*=x^2/2,\qquad
 U_tB_0U_t^*+x^2/2=(p+tx)^2,
\]

so `K` is an explicit global unitary propagator with the exact composition
law and correct instantaneous Hamiltonian on a common Schwartz core.
This statement is about differentiating on that invariant core; it does not
assert that `K(t,s)` maps the entire instantaneous `Dom(H_s)` onto `Dom(H_t)`.
Nevertheless its operator domains, and its absolute form domains, are
different for distinct times. Indeed `f=(1+x^2)^(-1/2)` belongs to `H^2`,
whereas for any nonzero `delta` the first derivative of
`e^(-i delta x^2/2) f` has nonzero constant magnitude at infinity and the
second derivative grows linearly. These are not `L2`, so multiplication by
that phase does not preserve either `H^1` or `H^2`.

This is a counterexample to promoting the actual fixed-domain obstruction
into a universal moving-domain no-go. It is **not** a metaplectic solution
of the actual cubic model: the latter retains its noncommuting TT/matter
cubic interaction, absent from (19). Finding a comparable domain transport
for that unchanged interaction is still a substantive missing theorem.

No withdrawn Schlegelmilch--Schnaubelt existence assertion is used. No finite
matrix or exact displacement calculation is identified with the missing
infinite-dimensional propagator. A possible strong-resolvent limit of the
actual covariant approximants from Round13 remains another route, pursued
separately; this result neither proves nor disproves that limit.

## 8. Reproduction

Run `python3 common_domain_checker.py` with SymPy. The current result is
**27/27 exact checks, zero floating-point checks**. The checker verifies
the actual source datum and both signs of the full operator-valued Weyl
displacement expansion, including cancellation of every `R^6` Hamiltonian
coefficient and the nonzero `B` coefficient. It retains unshifted operator
variables: it does not merely compare classical central energies.

The other-mode degree estimate is proved generally in section 3 and
checked algebraically with an undisplaced TT spectator. Mutants removing
or reversing the actual cubic interaction fail the requisite degree
improvement. The separate quadratic model tests only the final scope
warning. The common-domain impossibility is the Hilbert-space proof in
sections 4--6, not a numerical extrapolation from these finite identities.
