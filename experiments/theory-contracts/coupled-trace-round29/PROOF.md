# A positive-trace comparison for the actual scalar-charge interaction

2026-09-07. NON-RH, unpromoted research. This extends the evaluated
[Round28](../poisson-charge-round28/PROOF.md) regulator to **u>0** without
a scalar-amplitude cutoff, a charge box, or removal of any signed hopping.
It is not an arbitrary-precision solver at arbitrary coupling, a continuum
theorem, or physical T1-T8 closure. The change of viewpoint is to control
the whole positive trace, not the Poisson remainder separately at each
unbounded scalar trajectory.

## 1. The SAME transfer, with an actual interaction

On the original neutral charge space and continuous scalar space put

    W = sum_x e(n_x) phi_x^2 >= 0,
    V_u = D_nu(n) + (1/2) phi^t(-Delta_a+m^2)phi + u W,
    Q_u = exp(-delta V_u/2)
          exp[-delta(K_phi+H_hop)] exp(-delta V_u/2),
    Z(u) = Tr Q_u^T, beta=T delta.

Here H_hop=48NJ I-J A_sign has the original E8 cocycle. Because V_0 and W
are multiplication operators, for E_u=exp(-delta u W/2) we have the exact
identity Q_u=E_u Q_0 E_u. No reordering through kinetic or hopping terms
is used. In particular this is not exp[-beta(H_0+uW)] substituted for
the primitive transfer, and W is not a frozen scalar mass profile.

## 2. General lemma: a logarithmically convex trace sandwich

Let Q_0>=0 be compact with 0<Tr Q_0^T<infinity, integer T>=1, and W>=0.
Initially assume W bounded. Define

    F(u)=Tr(E_u Q_0 E_u)^T
        = ||E_u Q_0^(1/2)||_(2T)^(2T).

The second equality uses the identical nonzero spectra of B B* and B* B.
For 0<=a<b and z in the strip 0<=Re z<=1 use

    B(z)=exp[-delta(a+(b-a)z)W/2] Q_0^(1/2).

Along either boundary, imaginary exponentials are left unitary factors,
so the Schatten 2T norms are independent of Im z. Complex interpolation
with the SAME Schatten exponent at both boundaries gives

    log F((1-t)a+tb) <= (1-t)log F(a)+t log F(b).

This is the ordinary log-convexity of F, not operator convexity of exp.
The standard interpolation theorem is stated for separable Hilbert spaces
in [Sutter, Berta and Tomamichel, Theorem 3.1](https://arxiv.org/html/1604.03023v3#S3.SS1).
Here its specialization needs only the constant boundary norms; no new
general interpolation theorem is claimed.

Differentiate at zero using cyclicity of the trace:

    F'(0)=-delta T Tr(W Q_0^T),
    (log F)'(0)=-beta <W>_0,
    <W>_0 = Tr(W Q_0^T)/Tr Q_0^T.

The supporting tangent to this convex function therefore gives

    F(u) >= F(0) exp[-beta u <W>_0].                    (1)

For the upper bound note that Q_0^(1/2) E_u^2 Q_0^(1/2) decreases in
positive-operator order as u increases. Its compact eigenvalues decrease,
and summing their Tth powers gives F(u)<=F(0). We do NOT claim that
E_u Q_0 E_u <= Q_0: this generally fails, as the exact 2x2 counterexample
in the checker verifies.

For unbounded W take W_M=min(W,M). The preceding argument applies to
each bounded W_M. Its exponential converges strongly to E_u and is a
contraction. Multiplication of this strongly convergent bounded family
by Q_0^(1/2) converges in Schatten 2T (first approximate the latter by
finite-rank operators). Hence F_M(u)->F(u). Monotone convergence gives
<W_M>_0-><W>_0 when this moment is finite. Passing to the limit in (1)
proves the infinite-carrier lemma

    exp[-beta u <W>_0] Z(0) <= Z(u) <= Z(0), u>=0.      (2)

Positivity is used at operator/trace level. The signed word expansion
is not a classical probability measure; applying a classical Gibbs
inequality to its signed weights would not prove (2).

## 3. A finite, explicit interacting reference moment

At u=0 the reference density factorizes into scalar and charge factors,
although its charge factor is NOT a product over sites. Scalar translation
invariance gives the same v_phi=<phi_x^2>_0 at every site, so

    <W>_0 = v_phi <E_charge>_0,
    E_charge=sum_x e(n_x) <= N D_nu(n), nu>=0.           (3)

To bound D_nu, vary its coefficient only: let Z_ch(s) be the primitive
charge partition with D_nu replaced by s D_nu, keeping J, beta and the
additive hopping constant fixed. The same interpolation argument makes
f(s)=log Z_ch(s) convex for s>0. Coercive Gaussian charge damping makes
it differentiable there, including the D_nu insertion: D_nu^k exp(-cD_nu)
is bounded for c>0. For 0<r<1, the supporting slope implies

    beta <D_nu>_0 = -f'(1) <= [f(r)-f(1)]/(1-r).        (4)

Round27's complete-reference comparison, applied at each s, gives

    Z_ch(r) <= Z_D,ch(r),
    Z_ch(1) >= exp(-theta) Z_D,ch(1), theta=48 beta N J.

The neutral Gaussian has dimension d=8(N-1). Poisson summation from
Round28 gives Z_D,ch(s)=C0 s^(-d/2)(1+R_s), where 0<=R_s<=eta for
0<s<=1: all zero-shift dual terms are positive and the dual decay only
gets stronger when s decreases. This statement includes the evaluated
nu=1/486 quadratic form, not only nu=0. Thus

    beta <D_nu>_0
      <= [theta + (d/2)log(1/r) + log(1+eta)]/(1-r).

Combining with (3) and log(1+eta)<=eta supplies a computable M:

    beta <W>_0 <= M
       := N v_phi [theta + 4(N-1)log(1/r) + eta]/(1-r).
    exp(-u M) Z(0) <= Z(u) <= Z(0).                    (5)

This also establishes the finite moment needed by the unbounded-W limit
in Section 2. The charge differentiability used in (4) can alternatively
be proved by the trace-norm analytic family exp(-s delta D_nu/2) on
Re s>0, without ever differentiating unbounded W.

No coupling is selected by this estimate. The comparison parameter r is
an error-bound choice, not a physical parameter. It can be optimized
without changing the model. We use the exact rational r=9/10 throughout.

## 4. Same-regulator scalar covariance, not a continuum substitution

At L=T=3, beta=a=m=1 and delta=1/3, the spatial squared frequencies are
lambda=1,4,7,10 with multiplicities 1,6,12,8. For one scalar mode the
temporal precision matrix is

    M_lambda=delta^-1 L_C3 + delta lambda I.

Its diagonal inverse is

    (M_lambda^-1)_jj = 1/lambda + 2/(lambda+27).

Therefore

    v_phi = (1/27) sum_lambda mult(lambda)
                         [1/lambda+2/(lambda+27)]
          = 167106/682465.

The tests invert each actual 3x3 matrix independently. Replacing this
quantity by 1/(2omega), by the zero-temperature variance, or by an
unsliced thermal covariance would change the operator under study.
For both Round28 reference cases theta=1/2, and the rational upper
estimate in (5) yields M<758.

## 5. Four complete, interacting partition enclosures

Use the two actual Round28 intervals [L0,U0], for nu=0 and nu=1/486,
and re-execute their pinned checker. For each of those two choices,
evaluate u=1/65536 and u=1/4096. All other regulator values remain those
of Section 4 and J=1/2592. The new interval is

    L=L0 * lower_exp(-u M), U=U0.                       (6)

The logarithm log(10/9)=2 atanh(1/19) is enclosed by its positive rational
series and a geometric tail. The exponential uses adjacent alternating
Taylor sums; all displayed examples have u M<1. Every acceptance test,
operation and outward decimal rounding uses exact integer fractions.
The analytic inequality (5) has no u M<=1 restriction; that restriction
belongs only to this simple numerical exponential routine.

For a positive interval [L,U], the harmonic estimate

    zhat=2 L U/(L+U), rho=(U-L)/(U+L)

minimizes max_(z in [L,U]) |zhat-z|/z: its two endpoint errors are equal.
The checker also includes rounding of the displayed estimate. Both
u=1/65536 examples have relative error below 1 percent, and both
u=1/4096 examples have relative error below 10 percent. These are
quantitative enclosures of the full coupled traces, not numerical
quadrature of every scalar trajectory or explicit enumeration of all
words. No scalar determinant is discarded: (2) bounds its net effect
inside the original operator trace.

All integer charge profiles, all scalar amplitudes and all signed hop
orders remain in the target quantity. Negative original four-hop loops
still exist at u>0; changing their positive scalar weights does not
change their phase. There is no claimed generic sign-problem cure.

## 6. Why this helps, and where it stops

The previous demand for a tiny Poisson remainder uniformly at each
unbounded scalar trajectory was unnecessarily strong for this particular
finite-regulator goal. A single positive trace and one controlled moment
suffice for a nonzero-u enclosure. This removes that obstruction in the
declared small-coupling cases; it does not solve arbitrary-accuracy
evaluation at fixed strong u or J, or prove a uniform large-volume bound.

The remaining structural question is separate: which u,nu,J,m,a, state
and parent are actually derived from the compiler? [COMPILER.md](COMPILER.md)
gives exact Noether and geometric tests, including the measure correction
needed for a warped internal-torus interpretation. Merely naming the
coupling a metric does not select it. No physical T1-T8, chirality,
massless interacting spin-2, continuum, real-time reconstruction or
empirical status is promoted. This is a written analytic proof with
exact regressions, not independent proof-assistant certification.
