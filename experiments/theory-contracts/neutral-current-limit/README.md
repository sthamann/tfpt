# Neutral current limit: an explicit endpoint normalization

2026-09-08. Research contract, not a promoted T1–T8, TOE or RH result.
The chiral-current statements below are proved in the declared comparison
model. Their identification with the unchanged microscopic QWZ determinants
is tested at finite sizes but is not proved in the scaling limit.

## 1. Source and the new comparison

We keep the source, occupation and Gaussian filter of
[neutral-pair-composition](../neutral-pair-composition/README.md) and
[gaussian-vacuum-filter](../gaussian-vacuum-filter/README.md).
In particular Ny=8, M=1, holonomy r=1, negative-energy occupation, and
delta_N=4 N^(-3/4) are unchanged. The full occupied compression is used,
including both edges and the bulk; it is not replaced by a small edge block.

For endpoint length a, put F_a=Phi_delta(pi A_a+R), R=pi x/N.
The one-particle operator is U_a=exp(-iR) exp(iF_a). Thus

\[
 W_{ab}=U_a^\dagger U_b=e^{-iF_a}e^{iF_b},\qquad
 C_{ab}=\det\nolimits_{\operatorname{ran}P}(P W_{ab}P).
\]

The outer ramp cancels exactly, but F_a and F_b do not commute. Remove the
endpoint-coboundary phase

\[
 \theta_{ab}=\operatorname{Tr}P(F_b-F_a)P,\qquad
 C^\circ_{ab}=e^{-i\theta_{ab}}C_{ab}.
\]

This is a diagonal rephasing of the full endpoint Gram matrix and preserves
its positivity. It is not an arbitrary phase fitted separately to each pair.

Use u=x/N and now let a,b be fractional endpoints, d=b-a in (0,1).
In the separate linear chiral model h=-p the nonzero Fourier coefficients of
f_a(u)=pi u+pi 1_[0,a](u) are

\[
 (f_a)_k={i\over2k}e^{-2\pi i k a}\quad(k\ne0).
\]

The ramp and interval therefore combine into translated copies of one
function. The Gaussian energy filter multiplies this coefficient by
exp[-(2 pi k/t)^2/2], with t=N delta. This observation fixes the comparator;
no exponent, phase coefficient or separation dependence is fitted.

## 2. Exact current-model calculation

For the filled-positive-Fourier vacuum appropriate to h=-p, normal-ordered
currents obey

\[
 \langle J(f)J(g)\rangle=\sum_{k>0}k f_k g_{-k}.
\]

The vacuum is Gaussian for the current Weyl algebra. Write
w_k(t)=exp[-(2 pi k/t)^2] and H_t=sum_(k>0) w_k/k.
The covariance and central commutator give

\[
\begin{split}
 \log C^{\rm cur}_t(d)
 &=-{1\over2}\sum_{k>0}{w_k\over k}\sin^2(\pi kd)
   +{i\over4}\sum_{k>0}{w_k\over k}\sin(2\pi kd)\\
 &=-{H_t\over4}+{1\over4}\sum_{k>0}{w_k\over k}e^{2\pi i kd}.
\end{split}
\]

For example [J(f_a),J(f_b)]=(i/2) sum w_k sin(2 pi kd)/k.
The BCH half-commutator has the positive sign in the formula above.
The tests also reconstruct it independently from the Fourier covariance.

The required normalization is consequently a factor per endpoint:

\[
 Z_t=e^{H_t/8},\qquad
 K_t(d)=Z_t^2 C^{\rm cur}_t(d)
 =\exp\left({1\over4}\sum_{k>0}{w_k\over k}e^{2\pi i kd}\right).
\]

For fixed d in (0,1), Dirichlet summation gives the exact limit

\[
 K_t(d)\longrightarrow(1-e^{2\pi i d})^{-1/4}
 =[2\sin(\pi d)]^{-1/4}e^{i(\pi/8-\pi d/4)}.
\]

The branch is fixed by analytic continuation from the unit disk. This is
the oscillator two-point factor associated with the conventional level-one
charge-1/2 vertex, with candidate weight h=1/8. This current calculation
does not construct its charged zero mode, a microscopic field operator,
or a conformal transformation law in TFPT.

## 3. Positivity and a smeared limit, including eight independent copies

For any beta>0 define

\[
 G_t(z)=\exp\left(\beta\sum_{k\ge1}{w_k(t)\over k}z^k\right)
       =\sum_{n\ge0}a_n(t)z^n.
\]

Differentiation gives a_0=1 and

\[
 n a_n(t)=\beta\sum_{k=1}^n w_k(t)a_{n-k}(t).
\]

Induction proves 0<=a_n(t)<=b_n=(beta)_n/n!, with a_n(t) increasing
to b_n as t increases. Since b_n has only polynomial growth, these are
positive-type circle kernels and converge as distributions to the analytic
boundary value of (1-z)^(-beta). This proves a smeared two-point limit,
not merely a pointwise formula away from coincidence.

Conventions matter: with fhat_n=integral f(x) exp(-2 pi i n x) dx, the
overlap orientation K(b-a) gives

\[
 \iint\overline{f(a)}K_t(b-a)f(b)\,da\,db
 =\sum_{n\ge0}a_n(t)|\widehat f_{-n}|^2.
\]

The opposite orientation K(a-b) uses fhat_n instead.

There is an additional L1 statement for 0<beta<1. Let
s=|sin(pi d)| and M=floor(1/s). The first M terms of sum w_k exp(2 pi i kd)/k
have absolute sum at most 1+log(1/s). Abel summation bounds the remaining
sum by 1/((M+1)s)<=1. Hence

\[
 |G_t(e^{2\pi i d})|\le e^{2\beta}|\sin(\pi d)|^{-\beta}.
\]

Dominated convergence proves L1 convergence for beta=1/4.
For eight *independent tensor copies*, the kernel is K_t^8 and beta=2.
Now b_n=n+1, so the limiting smeared quadratic form is finite, for example,
on H^(1/2) test functions. The boundary kernel is
(1-e^{2 pi i d-0})^(-2), the oscillator factor associated with candidate
chiral weight 1 under that same conventional vertex interpretation.
It must be treated as an analytic boundary distribution, including its
contact terms; the bare off-diagonal function is not integrable.

This proves positivity of a two-point form and hence a Hilbert space of
vacuum-created vectors. It does NOT by itself establish common field
domains, an adjoint-closed field algebra, higher-point positivity,
exchange/locality, E8 gluing/GSO projection or microscopic eight-channel
identification.

## 4. Unchanged-source tests and an additional holdout size

The N=8,16,32,64 determinants are reused only after checking their source
and data hashes. N=128 was evaluated after fixing the comparator.
The relative complex error below is |C_source^circ/C_current - 1|.
It compares with the finite-t **smoothed** current model.

| N | Separation d | Complex ratio error |
| ---: | ---: | ---: |
| 8 | 1/2 | 0.03286299 |
| 16 | 1/2 | 0.00924075 |
| 32 | 1/2 | 0.00309130 |
| 64 | 1/2 | 0.00106474 |
| 128, holdout | 1/2 | 0.00036650 |
| 128, holdout | 1/4 | 0.00030839 |

At N=128 the half-interval phase error is about -2.10e-11 radians;
the quarter-interval phase error is 2.38e-5 radians.
The discrepancy is approximately 0.03–0.04 percent relative to the
smoothed comparator. It is NOT a 0.04-percent continuum-limit error:
the absolute difference of the normalized microscopic value from the
final limiting kernel is still 0.01199 at d=1/2 and 0.03419 at d=1/4.

Additional N=64 regulator controls replace only the declared coefficient
in delta=c N^(-3/4); no comparator parameter is refitted:

| c | Error at d=1/4 | Error at d=1/2 |
| ---: | ---: | ---: |
| 2 | 0.00028539 | 0.00034494 |
| 6 | 0.00199748 | 0.00226306 |

These are floating-point diagnostics, not interval-certified determinant
error bounds or a uniform convergence theorem.

The comparator series itself has an analytic truncation bound. With
A=(2 pi/t)^2, after M terms,

\[
 \sum_{k>M}{e^{-Ak^2}\over k}
 \le {e^{-A(M+1)^2}\over(M+1)(1-e^{-A(2M+3)})}.
\]

The loss and phase tails are bounded respectively by one half and one
quarter of this bound. Floating-point roundoff is a separate issue.

## 5. Why an uncorrected edge/bulk split is not a proof

Let the occupied projection be P=P_e+P_r and write the occupied compression
as [[E,X],[Y,D]]. For invertible D,

\[
 \det(PWP)=\det D\det S,\qquad S=E-XD^{-1}Y.
\]

For L_r=P_r W^\dagger(1-P_r)W P_r, let r=||L_r||<1,
ell=Tr L_r. Then

\[
 \sigma_{\min}(D)=\sqrt{1-r},\quad
 \|XD^{-1}Y\|_1\le{\|X\|_2\|Y\|_2\over\sqrt{1-r}},\quad
 {\ell\over2}\le-\log|\det D|\le{\ell\over2(1-r)}.
\]

The norms on X,Y here are Hilbert–Schmidt norms. A relative determinant
comparison also needs invertibility of E: if B=E^(-1)XD^(-1)Y and
eta=||B||<1, then

\[
 \left|\log{\det S\over\det E}\right|
 \le{\|B\|_1\over1-\eta},\qquad
 |{\rm tail}_{>M}|\le{\|B\|_1\eta^M\over(M+1)(1-\eta)}.
\]

Here the logarithm is log det(I-B)=-sum_(k>=1) Tr(B^k)/k, with its
branch fixed by continuation from B=0 inside ||B||<1.

An absolute small Schur correction would not suffice when E is nearly
singular. Moreover 1-P_r includes the removed *occupied* edge subspace.
Leakage relative to P_r is therefore not all physical particle production.

Exact counterexample: rotate two occupied modes by the matrix
[[4/5,-3/5],[3/5,4/5]] and leave every unoccupied mode unchanged.
The full vacuum determinant is 1, yet D=E=4/5, XD^(-1)Y=-9/20,
and S=5/4. The rest and Schur factors compensate exactly.

The actual N=64 source at occupied-energy cutoff 0.25 gives
log|det D|=-0.38692057, log|det S|=+0.00812597 and total
-0.37879460. The Schur-correction trace norm is 0.7534, not a demonstrated
vanishing remainder. All nine recorded finite factorization checks agree
to ordinary floating precision. Dropping the compensating factor is unjustified.

There is also a conditional phase estimate. Follow the actual two-leg path
W_1(u)=exp(-iu F_a), W_2(u)=exp(-iF_a)exp(iu F_b), 0<=u<=1,
with W'=iWK and K=-F_a or F_b. If D(u) stays invertible throughout,
then after subtracting Tr P_r(F_b-F_a)P_r the continuous determinant phase
has absolute error at most

\[
 \Gamma_r=\sum_{\rm legs}\int_0^1
 {\|(1-P_r)KP_r\|_2\sqrt{\operatorname{Tr}L_r(u)}
  \over\sqrt{1-\|L_r(u)\|}}\,du.
\]

This follows from D'=i D K_rr+i(P_r W(1-P_r))K_qr and the logarithmic
derivative. Together with the endpoint modulus bound it yields
|exp(-i theta_r)det D-1|<=ell/[2(1-r)]+Gamma_r.
No source-uniform Gamma_r bound has been established here.

## 6. Next proof obligation

The first remaining edge is a uniform *complex* determinant comparison for
the same QWZ source as delta_N tends to zero and N delta_N tends to infinity.
It must retain the Schur compensation or bypass the artificial occupied
cut, control both phase and modulus, and provide near-diagonal bounds
strong enough for smeared limits. Pointwise finite-size agreement is not
enough, especially after taking eight copies.

Only after this should the charged zero-mode/cocycle/carry construction be
combined with the oscillator field on a common domain. The separate
[carrier-module audit](../carrier-module-conjugation/README.md) identifies
an additional preparation/holonomy issue at that interface.

For related primary-source methodology, see
[Ivanov and Levkivskyi, smoothing and bosonization of full counting statistics](https://arxiv.org/html/1507.07896).
That work motivates a comparison of smooth counting operators with current
models; it does not prove the source-specific QWZ limit claimed open here.
The coefficients and sign above were derived for this one-chiral-edge
convention rather than copied from a two-Fermi-point formula.

## Reproduction

    python3 experiments/theory-contracts/neutral-current-limit/checker.py --holdout --output experiments/theory-contracts/neutral-current-limit/diagnostics.json
    python3 -m unittest discover -s experiments/theory-contracts/neutral-current-limit -p test_checker.py
    python3 -OO -m unittest discover -s experiments/theory-contracts/neutral-current-limit -p test_checker.py

The first command evaluates dense microscopic matrices, including N=128.
The thirteen tests check exact finite algebra, independent covariance and
coefficient identities, tail controls, Schur counterexamples, source hashes,
and the explicit no-promotion boundary. See [test record](TEST_RESULTS.md).
