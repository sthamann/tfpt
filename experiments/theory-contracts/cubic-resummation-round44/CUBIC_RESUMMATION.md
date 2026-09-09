# Full-cubic matter-row evaluation with a certified configuration-exit source

2026-09-07. **NON-RH / conditional, unpromoted theory experiment.**
Round43's unevaluated full-cubic hybrid readout is now evaluated with a
separate, explicit configuration-projection error. This does not solve
the full electric dynamics, select physical parameters or close T1-T8.

## 1. Exactly the same parent and initial class

Keep the unrotated U(1) parent H=H_E+dGamma(h), with

\[
H_E=\frac\kappa2\sum_\ell E_\ell^2,\qquad
h=\begin{pmatrix}A+\beta A^2&\eta A\\\eta A&MI\end{pmatrix},
\quad A_{xy}=aU_{xy}.
\tag{1}
\]

The pinned constants remain a=1/12, eta=1/2, beta=1/4, kappa=1/100,
M=4, Vmag=0. Every cubic low onsite backtrack is d=1/96. No field
rotation, parameter fit, replacement vacuum or tree substitution is made.
Initial E=0 states have exactly one L/H fermion per site, with a finite
coherent/mixed/entangled species patch and bare-low filling elsewhere.
The physical readout is n_H,0. These are declared model assumptions.

Use the exact matter-only row of Round43,

\[
F(t)=e^{iH_Et}e_{H,0}^T e^{-iKt},\qquad K=H_E I+h,
\qquad P_\infty=\sum_jF_jc_j. \tag{2}
\]

The nonlinear electric ME, MEM and MME terms remain separate. The matter
row is not a canonical full-Fock transformation; Round43's explicit CAR
counterexample remains valid. No assertion that (2) is the full H evolution
is introduced by evaluating it more accurately.

## 2. A configuration ball, not a physical spatial box

An auxiliary basis state is (x,s,r): particle position x in Z^3, species
s=L,H, and a finitely supported integer link current r. Its fixed
point-background Gauss constraint is

\[
\delta_{y,x}+\operatorname{div}_y r=\delta_{y,0}. \tag{3}
\]

Define B_L as all DISTINCT (x,r) produced by elementary nearest-neighbor
walks of length at most L, starting at 0 with r=0. Each step adds its
oriented unit link current; inverse traversals cancel exactly. Include
both species for each configuration. Breadth-first enumeration is a
finite way to construct precisely this set, with no magnitude pruning.

Different walks with identical final current and endpoint are identified;
different currents at the same endpoint are NOT identified. For example,
B_4 contains 24 distinct nonzero plaquette currents with x=0. The layer
counts through L=6 are

\[
1,\ 6,\ 30,\ 150,\ 750,\ 3750,\ 18750,
\]

giving 23437 endpoint/current configurations and 46874 species states.
This is not the dimension of the physical many-body Hilbert space. Nor
is L a cutoff on individual E_l or simply a radius of a spatial box:
configurations with link current magnitude two already occur inside.

Let Pi_L project onto this finite auxiliary set. Build

\[
K_L=\Pi_L K\Pi_L,\qquad B=Q_L V\Pi_L,\quad Q_L=I-\Pi_L. \tag{4}
\]

Here V is precisely the original direct and nonbacktracking two-step
hopping, with monomial weights 48/576, 24/576 and 1/576. A two-step
monomial is applied as an original parent monomial, not assembled by
squaring an already compressed nearest-neighbor operator. Onsite d and
the complete diagonal electric energy kappa sum r_l^2/2 remain intact.

Every inside transition AND every exit is enumerated from the original
cubic rows. Hermiticity is checked exactly. All nonzero outside rows of
B are finite in number (652522 for L=6), because an original V monomial
adds at most two elementary steps. The subsequent outside dynamics is
NOT compressed to those rows: it is the full propagator in the error
identity below. Thus distant propagation and arbitrarily many further
winding events are covered by the bound, not set to zero.

In particular, two edge-disjoint plaquette currents based at the root,
and a twice-wound plaquette, require length eight in the explicit tests.
They are outside B_6 but present in the calculated exit matrix B. Still
higher loop configurations are covered by its full propagated source.
This is not a calculation in a single fixed plaquette-flux sector.

## 3. An all-exit error certificate independent of the electric-energy norm

For initial column e_s=|0,s,E0>, embed exp(-iK_Lt)e_s in the full auxiliary
space. Strong Duhamel integration gives

\[
\|(e^{-iKt}-e^{-iK_Lt})e_s\|
\le\int_0^T\|B e^{-iK_Lu}e_s\|\,du,
\qquad T=|t|. \tag{5}
\]

K is a real diagonal self-adjoint electric/onsite operator plus bounded
hopping. Its bounded perturbation defines the auxiliary unitary group;
there is no norm differentiation of the unbounded electric generator.
The strong-dynamics distinction is discussed by
[Nachtergaele and Sims](https://arxiv.org/html/1410.8174v1).

Write A_+=Pi_L V Pi_L as a matrix in the current basis. For this particular
unrotated one-particle parent all entries of A_+ and B are nonnegative.
Diagonal electric/onsite interaction-picture factors have modulus one.
Termwise absolute values in its convergent Dyson expansion therefore give
the COMPONENTWISE comparison

\[
|e^{-iK_Lu}e_s|\le e^{uA_+}e_s.
\]

Using positivity of B and then the triangle inequality in (5) yields

\[
\delta_{s,L}(T)\le
\sum_{n=0}^N\frac{T^{n+1}}{(n+1)!}\|BA_+^n e_s\|
+\sum_{m=N+2}^{\infty}\frac{(\mu T)^m}{m!},
\qquad \mu=77/96. \tag{6}
\]

The row and column sums of the full symmetric hopping matrix are bounded
by mu, so ||V||, ||A_+|| and ||B|| are at most mu. This bounds the omitted
series in (6), uniformly in volume and electric flux. For x=mu T, its
rational upper enclosure is

\[
\sum_{m=q}^{\infty}\frac{x^m}{m!}
\le\frac{x^q}{q!}\frac1{1-x/(q+1)},\quad q=N+2. \tag{7}
\]

The denominator must be positive. No diagonal-energy norm occurs in
(6)-(7), so large electric fields outside Pi_L are not an uncontrolled
assumption. With integer hopping matrices A_int=576 A_+ and B_int=576 B,
the n-th norm in (6) is computed as

\[
\|BA_+^n e_s\|=
\frac{\sqrt{\sum_q((B_{int}A_{int}^n e_s)_q)^2}}{576^{n+1}}. \tag{8}
\]

The square is an exact integer; its square root has an outward rational
enclosure. Equal exit configurations are collected before taking norms.
This is an evaluated boundary-source certificate, not just a worst-case
count of all paths. The implementation evaluates through N=14.

At T=1, L=6:

| Auxiliary column | All-exit vector error, approximately |
|---|---:|
| Initially L | 1.269433839742e-7 |
| Initially H | 3.393891237658e-8 |
| Two-column reconstruction | 1.314019501687e-7 |

The L=4 and L=5 reconstruction bounds are approximately 2.89449134e-5
and 2.04998284e-6. They are valid coarser calculations of the same target,
not different physical parents.

## 4. Actual finite-time evolution, phases, and translation

The compressed Hermitian matrix is centered by c=(M+d)/2=385/192 to
reduce polynomial norms. This is only a scalar shift. Its effect is
restored together with the mandatory left electric phase:

\[
F_{(j,s),r}(t)=e^{i(H_E(r)-c)t}
\langle -j,H,T_{-j}r|e^{-i(K_L-c)t}|0,s,E0\rangle
\quad\text{up to the certified projection error}. \tag{9}
\]

The exact translation identity is for the full K. Translating an embedded
compressed column need not produce the same cutoff set based at j. This
is harmless: (5) compares it to the full column before translation, and
translation is an isometry. No boundary-invariance approximation is used.

Exact integer matrix powers evaluate the degree-60 Taylor polynomials at
t=1/10,1/5,1/2,1. The same power sequence is reused at these rational
times with exact common denominators. Its result is independently checked
against Round38's Horner evaluator, including negative time and t=0.
For radius R bounding ||K_L-c||, the self-adjoint propagator Taylor tail
is (RT)^61/61!. Scalar real phases have the analogous modulus-one
derivative bound. No floating-point eigenvalue or rounded norm is used.

If tau_s is the finite-matrix error and eta the largest left-phase error,
the column's full evaluation error is

\[
\epsilon_s=\delta_{s,L}+\tau_s+(1+\tau_s)\eta. \tag{10}
\]

On E0, exactly-one-fermion/site inputs, distinct annihilated sites leave
orthogonal hole sectors. Round43's two-column isometry therefore gives

\[
\| (\widetilde P_\infty-P_\infty)\Psi\|
\le\epsilon_{aux}\|\Psi\|,
\qquad \epsilon_{aux}=\sqrt{\epsilon_L^2+\epsilon_H^2}. \tag{11}
\]

This is a source error on the specified initial class, not a global
whole-Fock operator-norm bound for the numerical projection. It includes
both configuration truncation and arithmetic, despite the inherited
response interface's field name `numerical_amplitude_error`.

The projected source matches the exact cubic matter jets through time
order THREE, independently checked for every coefficient. No exact
fourth-order matching is claimed for this finite configuration ball:
four hopping events can already leave B_6. Its additional source error
bound can begin at order t^4. Round43's exact TARGET hybrid retains its
fifth-order electric remainder; the numerical configuration error is
additional and is always included, also at short times.

## 5. Physical full-cubic readouts with both errors included

The exact target approximation and executed version are

\[
Z=P_\infty+C_{ME}+C_{MEM}+C_{MME},\qquad
\widetilde Z=\widetilde P_\infty+
\widetilde C_{ME}+\widetilde C_{MEM}+\widetilde C_{MME}.
\]

Retain Round43's same-parent full-source bound
D43=D42-M4+(E_infinity-E_total4); it is below 0.000034638931076 at t=1.
Add epsilon_aux from (11) and the electric arithmetic errors. For
q=||Z_tilde Psi||^2, the complete physical occupation enclosure is

\[
\left[\max(0,\sqrt q-\varepsilon)^2,
\min(1,(\sqrt q+\varepsilon)^2)\right],
\quad\varepsilon=D43+\epsilon_{aux}+\epsilon_{electric,num}. \tag{12}
\]

The square root and displayed endpoints are rounded outward. The inherited
common 4x4/8x8 patch-response construction retains coherent fermionic
signs, exact flux matching and mixtures; it does not assume factorized
species densities. The initial finite patch is not the support of the
subsequent dynamics.

For the original bare-low input, the newly EXECUTED cubic intervals are:

| Time | Full-parent high-root occupation interval |
|---|---|
| 0.1 | [0.00010278183764, 0.00010278185085] |
| 0.2 | [0.00039486780602, 0.00039486863739] |
| 0.5 | [0.00184395123401, 0.00184413038992] |
| 1 | [0.00219466789203, 0.00220118831043] |

The t=1 interval is about 4.8 times narrower than Round42's executed
full-cubic interval and lies strictly inside it. The L=5 and L=6 source
vectors are compared independently within both all-exit certificates.
This is not an independent exact solution of the infinite physical
many-body Hamiltonian; the physical guarantee still uses the explicitly
derived electric remainder and the unchanged parent assumptions.

The neighboring Bell inputs (LL-iHH)/sqrt2 and (LL+iHH)/sqrt2 have
identical one-site species densities I/2 and the same initial E0. At t=0.2:

| Preparation | Full-parent occupation interval |
|---|---|
| Minus phase | [0.50016444486793, 0.50016447445617] |
| Plus phase | [0.50016441356383, 0.50016444315207] |

Their certified separation exceeds 1.715e-9 INCLUDING electric,
configuration and arithmetic errors. At t=0.1 the separation exceeds
4.369e-9. At t=0.5 and t=1 the Bell intervals STILL OVERLAP. Therefore
this work extends the conditional finite-time correlation witness, but
does not claim all-time separation or an experimentally observed signal.

## 6. Scope, verification, resource accounting, next obligation

All transitions in (4) are checked against the original parent Hamiltonian
on a sufficiently large cubic subgraph for every column of a smaller
configuration ball, including all exits. Additional checks cover arbitrary
currents generated inside/outside the ball, reflection symmetry, independent
matter jets, a diagonally stiff finite control, direct versus scaled
positive series, both polynomial evaluation orders, configurations with
independent loops, smaller/larger source agreement, correlation and mixture
responses, mutation guards and full deterministic replay.

This evaluates two columns on 46874 states, but also enumerates 652522
outside rows for the all-exit certificate. Those rows, their nonzero
transitions, the matrix powers and large exact integers are real costs;
quoting only the evolved matrix dimension would omit substantial work.
No total speedup, asymptotic complexity breakthrough, proof-assistant
verification, peer review or empirical prediction is claimed.

The bounds are uniform for finite ambient cubic parents with the target
and generated configurations interior, retaining actual boundary terms
outside. Compatible thermodynamic limits inherit them where the full
dynamics is constructed. The result is a cubic-lattice statement under
these assumptions, not a continuum/chiral/gravity reconstruction theorem.

The now dominant computational target is further ELECTRIC propagation:
at t=1 its bound exceeds the evaluated auxiliary error by over a factor
of 200. Enlarging the configuration ball alone no longer removes the
leading uncertainty. The next mechanism to evaluate is the previously
proved convergent one-electric sector with further matter propagation,
while keeping multiple-electric branches and compatible additional
physical observables explicit. State/parameter selection, chiral 3+1D
continuum dynamics, spin-two universality and the other T1-T8 obligations
remain open. No claims are promoted beyond this research contract.
