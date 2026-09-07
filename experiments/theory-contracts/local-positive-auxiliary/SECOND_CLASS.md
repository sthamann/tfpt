# Finite second-class auxiliary embedding of the positive reduced completion

## The finite classical result

The local static auxiliary construction in `README.md` admits a complete
finite-dimensional **second-class** Hamiltonian realization on every
retained nonzero lattice mode. Its auxiliary constraints are regular and
preserved, all auxiliary multipliers are determined, no additional
physical canonical pairs remain, and the induced Poisson bracket and
Hamiltonian on the seed variables are exactly the original canonical
bracket and the chosen positive reduced Hamiltonian.

This result classifies the new auxiliary variables only. The seed is the
already reduced TT-plus-matter system. It neither replaces nor proves the
original gravitational first-class constraints, restores homogeneous
gravity, nor supplies a first-class local gauge parent. Quantization below
means quantization after this exact reduction; it does not mean imposing
noncommuting second-class operators on a common physical kernel.

## 1. Local auxiliary Hessian and its inverse

Use `D,N=[V^dagger,t],ell,P` from the local auxiliary proof. On the
nonzero-mode space,

\[
DD^\dagger=\ell I_6,\qquad
\operatorname{rank}N=4,\qquad P=I-N(N^\dagger N)^{-1}N^\dagger.
\]

Introduce auxiliary canonical pairs `(y,p_y)`, where
`y=(E,u,lambda)` has `18+4+6=28` real coordinates per real nonzero Fourier
component. Retain any canonical seed variables `z` and put

\[
H_b(z)=H_{\rm seed}(z)+g\langle q,\tau(z)\rangle,
\]
\[
H_{\rm ext}=H_b+\tfrac12 E^TE
-\lambda^T(DE-Nu-g\tau)
=H_b+\tfrac12 y^TKy+y^Ts(z),
\tag{1}
\]
\[
K=\begin{pmatrix}
I_{18}&0&-D^T\\
0&0&N^T\\
-D&N&0
\end{pmatrix},\qquad
s(z)=\begin{pmatrix}0_{18}\\0_4\\g\tau(z)\end{pmatrix}.
\tag{2}
\]

Here all fields are expressed in real canonical coordinates. The
dagger notation for lattice adjoints becomes transpose in (2). Complex
Fourier phases are either retained consistently or converted to real
paired/self-conjugate coordinates; no `i Bp` is silently declared a real
fibre. The checker uses the actual real anchored `(pi,pi,0)` boundary
symbols on the `L=2` periodic lattice.

The fixed real symmetric `K` is invertible at every retained momentum.
Indeed its stationary homogeneous equations force `lambda` to be TT and
`ell lambda=Nu`; projection gives `lambda=0`, then `E=0,u=0`. Its inertia
is `(22,6,0)`, as proved in the static analysis. Those negative directions
are multiplier/slack directions of the extended auxiliary functional,
not surviving physical ghost oscillators.

The unique stationary auxiliary value is

\[
y_*(z)=-K^{-1}s(z),\qquad
E_*=gD^T\ell^{-1}P\tau,
\quad\lambda_*=g\ell^{-1}P\tau,
\quad u_*=-g(N^TN)^{-1}N^T\tau.
\tag{3}
\]

In particular `(K^{-1})_(lambda,lambda)=-ell^{-1}P` and

\[
H_{\rm red}=H_{\rm ext}(z,y_*)
=H_b-\tfrac12s^TK^{-1}s
=H_{\rm seed}+g\langle q,\tau\rangle+
\tfrac{g^2}{2}\langle\tau,P\ell^{-1}\tau\rangle.
\tag{4}
\]

This is the chosen positive reduced completion. It is not the result of
minimizing a positive unconstrained `K`; the Hessian in (2) is a saddle.

## 2. Dirac–Bergmann algorithm and exact brackets

The first-order action has no auxiliary velocities apart from the
introduced canonical term, and enforces the primary constraints

\[
p_y=0,
\qquad H_T=H_{\rm ext}+\mu^Tp_y.
\]

Their preservation gives the secondary constraints

\[
\dot p_y=-\Phi\approx0,
\qquad \Phi=\partial_yH_{\rm ext}=Ky+s(z).
\tag{5}
\]

Let `F_ij(z)={s_i,s_j}_seed`; it is not assumed zero. Ordering the full
constraint vector as `chi=(p_y,Phi)` gives

\[
\mathcal C=\{\chi,\chi\}=
\begin{pmatrix}0&-K\\K&F\end{pmatrix},\qquad
\mathcal C^{-1}=
\begin{pmatrix}K^{-1}FK^{-1}&K^{-1}\\-K^{-1}&0\end{pmatrix}.
\tag{6}
\]

Both matrix products are the identity for *arbitrary* `F`, because `K` is
invertible. Thus the entire set is second class everywhere on the seed
phase space. No source-dependent rank test, small-coupling assumption, or
extra condition on matter states is needed.

For seed observables `f(z),h(z)`, their brackets with all `p_y` vanish.
The bottom-right zero block in (6) therefore gives the strong identity

\[
\{f,h\}_D=\{f,h\}_{\rm seed}.
\tag{7}
\]

This is also clear from the canonical one-form: on the embedded constraint
surface `(z,y_*(z),p_y=0)`,

\[
\iota^*(\theta_{\rm seed}+p_y^Tdy)=\theta_{\rm seed}.
\tag{8}
\]

It remains true when `y_*` depends on seed momenta. Each nonzero real
component adds 28 canonical pairs and 56 independent second-class
constraints, removing exactly those 28 pairs. No auxiliary canonical pair
survives reduction. This count concerns the present auxiliaries, not the
original gravity gauge/constraint pairs which have already been reduced.

## 3. All preservation multipliers are fixed

Write

\[
a_i(z)=\{s_i,H_b\}_{\rm seed},\qquad
h(z,y)=\{\Phi,H_{\rm ext}\}=a(z)+F(z)y.
\]

Secondary preservation under `H_T`, modulo the primary constraints, is

\[
\dot\Phi\approx a+Fy+K\mu=0.
\]

It determines every multiplier uniquely:

\[
\mu_*=-K^{-1}(a+Fy_*).
\tag{9}
\]

There are no tertiary constraints. An off-surface choice
`mu(z,y)=-K^{-1}(a+Fy)` gives preservation modulo `p_y`; derivatives of
this multiplier in Poisson brackets only multiply the primary constraints.
The assertion is Dirac preservation, not a claim that those terms vanish
identically off the constraint surface.

Differentiating (4) gives
`{s,H_red}=a+Fy_*`. Consequently

\[
\{y_*,H_{\rm red}\}_{\rm seed}
=-K^{-1}(a+Fy_*)=\mu_*.
\tag{10}
\]

Thus auxiliary motion follows the moving stationary graph exactly. The
seed equations also coincide with the Hamilton equations of (4): the
chain-rule correction from differentiating `y_*` multiplies
`partial_y H_ext=0`. Together (5), (9), and (10) close the full finite
auxiliary classical stabilization, with the physical phase space and
energy unchanged from the chosen reduced completion.

For the actual free scalar the reduced TT stresses depend on configuration
only, so `H_red=||p_seed||^2/2+V_g`, where `V_g>=0` is smooth polynomial.
Every finite-energy solution has bounded momenta, hence bounded position
growth on each finite time interval. Standard smooth-ODE continuation
therefore gives all-real-time classical evolution for this fixed finite
model, even if `V_g` is not proper. The polynomial graph (3) and (9) lift
that evolution globally. This additional completeness statement uses the
actual configuration-only scalar stress, not arbitrary quadratic currents
with momentum-dependent reduced interactions.

## 4. Actual source brackets are not silently set to zero

The full unprojected scalar stress is
`tau=t A(phi,pi)+sigma(phi)`, with
`A=pi^2/2-m^2 phi^2/2` pointwise. Its TT projection loses `A`, so the
projected stress components commute. Its unprojected smeared components
need not commute, and are exactly the components entering `s` in (2).

The checker constructs the fixed stress formulas R8.1–R8.3 on an actual
periodic `L=2` scalar lattice, normalizes the real `(pi,pi,0)` Fourier
smearing by `1/sqrt(8)`, and computes all fifteen independent brackets of
the six orthonormal stress components. It verifies a nonzero full source
bracket and `P F_tau P=0` for the TT projection. The nonzero source bracket
is carried in (6); it does not change the seed Dirac bracket.

It also checks that the `F y_*` term in (9) is nonzero for this actual source:
omitting it fails secondary preservation. This is distinct from the
generic noncommuting two-current witness used elsewhere.

## 5. Finite constrained Liouville measure

The same block structure shows that no source-dependent auxiliary
Jacobian survives the classical reduction. In fact

\[
\mathcal C=
\begin{pmatrix}I&0\\-FK^{-1}&I\end{pmatrix}
\begin{pmatrix}0&-K\\K&0\end{pmatrix},
\qquad \det\mathcal C=(\det K)^2.
\tag{11}
\]

The first factor has determinant one, independent of `F`. At fixed seed
point, `delta(Ky+s)=delta(y-y_*)/|det K|`. Therefore, for any integrable
seed test density, integrating the auxiliary factor gives

\[
\int dy\,dp_y\;
\delta(p_y)\delta(Ky+s(z))\sqrt{\det\mathcal C}=1.
\tag{12}
\]

The reduced measure is exactly the canonical seed Liouville measure,
with no hidden stress-dependent determinant. Equation (12) is a
finite-dimensional classical constrained-measure identity. It is not a
time-sliced, operator-ordered or continuum path-integral quantization
theorem.

## 6. Homogeneous and quantum boundaries

At zero momentum `K` is singular. Equations (3), (6), and (9) here apply
only to retained nonzero modes. The separate five constant traceless
bookkeeping slacks described in `README.md` are not silently included in
this invertible-Hessian theorem. They require their own treatment if one
wishes to extend the auxiliary Dirac analysis to the homogeneous block.
No homogeneous gravity pair has been restored.

The classical second-class reduction identifies the reduced phase space
canonically. One may therefore define the quantum version of this chosen
embedding by quantizing its reduced Hamiltonian with the already stated
positive operator/form prescription. This is reduction followed by
quantization. It is not a theorem that an independently quantized extended
Hamiltonian and operator constraints have the same physical Hilbert space.
In particular, the nonzero commutators corresponding to `{p_y,Phi}=-K`
preclude treating all second-class conditions as mutually compatible
annihilation constraints on a naive common kernel.

The original canonical dressing of gravity constraints and the present
second-class auxiliary construction are separate operations. No assertion
about their full unreduced quantum combination, a first-class gauge parent,
TFPT physical inner product, relativistic causality, continuum limit,
empirical prediction, TOE completion, or RH follows from this result.

The Dirac-bracket convention in (6)–(7) agrees with the standard formula in
[UF constrained-Hamiltonian lecture notes, section 3](https://www.phys.ufl.edu/courses/phz6607/fall20/Notes/constraints.pdf).
All block inversion, source, and stabilization identities needed here are
derived above and checked independently below.

## Reproduction

Run `python3 second_class_checker.py` in this directory. It uses exact
SymPy arithmetic, has no repository imports, tests the actual boundary
symbols and actual finite scalar stress, and supplies must-fail mutants
for dropping the source-bracket correction. The all-volume result rests on
the block proof for invertible `K`, not on the single-volume regression.

