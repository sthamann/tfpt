# Ordered Current-Weyl four-point limit on the full endpoint torus

2026-09-09. This contract proves the complete complex, normal-ordered
four-point kernel of the declared one-copy Current model, for all six
neutral sign words. The limit is in L1 of the **entire** four-endpoint
torus, including all collision neighborhoods. This is a direct Weyl/BCH
calculation and an integrability proof, not a Wick factorization inferred
from two-point data. It does not, by itself, prove microscopic QWZ
identification, charged fields, reflection positivity, E8, TOE or RH.

## 1. Frozen Current representation and conventions

The source chain is pinned in [checker.py](checker.py). It reuses
[neutral-current-limit](../neutral-current-limit/README.md),
[history-reference-transport](../history-reference-transport/README.md)
and [current-truncation-bridge](../current-truncation-bridge/README.md).
No older source is changed. Their historical open-status statements are
not silently updated by importing their fixed numerical implementations.

Work in the filled-positive-Fourier, charge-zero current vacuum:

\[
 [a_k,a_l^\dagger]=\delta_{kl},\quad a_k\Omega=0,\qquad
 J(f)=\sum_{k>0}\sqrt{k}(f_k a_k+\overline{f_k}a_k^\dagger).
\]

The CAR-to-current convention and its Galerkin identification are proved
in the preceding truncation contract. The standard representation is also
discussed in Alistair Savage's
[A geometric boson-fermion correspondence](https://arxiv.org/abs/math/0508438),
section 1. That reference is background for the representation, not a
source-specific four-point-limit theorem or a priority claim here.

For t>0, define

\[
 w_k=e^{-(2\pi k/t)^2},\quad H_t=\sum_{k\ge1}{w_k\over k},\quad
 S_t(d)=\sum_{k\ge1}{w_k\over k}e^{2\pi i k d},\quad Z_t=e^{H_t/8},
\]

and \(f_{t,a,k}=i e^{-2\pi i k a}\sqrt{w_k}/(2k)\).
Put \(W_t(a)=e^{iJ(f_{t,a})}\). Products below are written in actual
operator order, from left to right; the endpoints need not be spatially
sorted. The diagonal coefficient of f multiplies the normal-ordered
fermion charge, which is zero throughout this current representation.
At finite fermion cutoff it is removed instead by the exact phase
\(\exp[-i\sum_l\epsilon_l\operatorname{Tr}(P_{\rm cur}T_{a_l})]\).
This subtraction is per leg and does not require neutrality.

The signs are *formal endpoint charges*. The oscillator Weyl operators
do not themselves change the fermionic zero-mode charge. No physical
charge superselection or charged vertex operator is assumed here.

## 2. Exact ordered word, including the full BCH phase

For any fixed word of L signs \(\epsilon_l\in\{-1,+1\}\), set

\[
 C_{t,\epsilon}(a_1,\ldots,a_L)
 =\langle\Omega,\prod_{l=1}^L W_t(a_l)^{\epsilon_l}\Omega\rangle.
\]

Each factor is a Weyl displacement with square-summable amplitude

\[
 \alpha_{l,k}={\epsilon_l\sqrt{w_k}\over2\sqrt{k}}e^{2\pi i k a_l},
 \qquad D(\alpha)=e^{\alpha a^\dagger-\overline\alpha a}.
\]

The CCR give
\(D(\alpha)D(\beta)=
 e^{(\alpha\overline\beta-\overline\alpha\beta)/2}D(\alpha+\beta)\).
For finitely many modes, composition followed by
\(\langle D(\gamma)\rangle=e^{-\|\gamma\|^2/2}\) gives

\[
 \log C_{t,\epsilon}
 =-\frac12\sum_l\|\alpha_l\|^2
  -\sum_{i<j}\langle\alpha_i,\alpha_j\rangle
 =-{L H_t\over8}-{1\over4}\sum_{i<j}\epsilon_i\epsilon_j
                         S_t(a_j-a_i).\tag{1}
\]

All sums converge absolutely at fixed t, so the same identity follows
for the full current Weyl representation by the square-summable limit.
Here log C denotes the BCH exponent, continuously lifted by scaling all
generators from zero; it is not necessarily the principal logarithm for
an arbitrary long word.
In particular the exact normalizing factor is **one Z per endpoint**:

\[
 K_{t,\epsilon}:=Z_t^L C_{t,\epsilon}
 =\exp\!\left[-{1\over4}\sum_{i<j}\epsilon_i\epsilon_j
                                      S_t(a_j-a_i)\right].\tag{2}
\]

This identity does not need neutrality. Neutrality is needed for the
particular four-point integrability proof and for cancellation of a
common microscopic/reference spectator in the separate source comparison.

For \(\epsilon=(-,+,-,+)\), write \(S_{ij}=S_t(a_j-a_i)\). Then

\[
 K_{t,-+-+}
 =\exp[(S_{12}-S_{13}+S_{14}+S_{23}-S_{24}+S_{34})/4].\tag{3}
\]

The complex phase is \(-\tfrac14\sum_{i<j}\epsilon_i\epsilon_j
\operatorname{Im} S_{ij}\), with no fitted phase. Swapping adjacent
endpoint/sign pairs changes the word by
\(\exp[-\tfrac i2\epsilon_i\epsilon_{i+1}
\operatorname{Im}S_t(a_{i+1}-a_i)]\), in the original/swapped orientation.
Reversing the order **and** all signs gives the complex conjugate.
Replacing S by its real part, sorting endpoints, or using an unordered
product erases this information.

Although the currents J have Gaussian vacuum correlations, the W's are
exponentials, not linear Gaussian fields. Equation (3) is not the sum of
the two allowed neutral two-pair Wick contractions. The tests explicitly
reject both the naive bosonic sum and fermionic difference.

## 3. Continuum kernel and its branch

For d not zero modulo 1, monotone-coefficient Dirichlet summation gives

\[
 S_t(d)\longrightarrow S(d)=-\operatorname{Log}(1-e^{2\pi i d}).
\]

For example the tail after k=K is bounded uniformly in t by
\(1/[(K+1)|\sin\pi d|]\). First let t tend to infinity in a finite
prefix and then let K tend to infinity. This also proves convergence
uniformly away from d=0. The branch is the analytic boundary value from
the disk, equivalently, for 0<d<1,

\[
 \operatorname{Log}(1-e^{2\pi i d})
 =\log(2\sin\pi d)+i(\pi d-\pi/2).
\]

Therefore, for any of the six neutral sign patterns,

\[
 K_\epsilon(a_1,a_2,a_3,a_4)
 =\prod_{i<j}(1-e^{2\pi i(a_j-a_i)})^{\epsilon_i\epsilon_j/4},\tag{4}
\]

with that branch applied **separately to each ordered pair**. Collapsing
the product into a single principal power of a cross-ratio can change
its phase and is not the definition. Formula (4) is initially pointwise
only when all four endpoints are distinct modulo 1.

At finite t the kernel is smooth even at collisions. If adjacent inverse
operators cancel, the unnormalized word reduces exactly, but the four
normalization factors remain. For instance
\(K_{t,-+-+}(a,a,b,b)=K_{t,-+-+}(a,b,b,a)=Z_t^4\).
One must not replace these values by a two-point normalization. The
collision sets have zero four-dimensional measure; assigning any finite
value there to (4) defines the same L1 representative. No finite pointwise
limit on those sets is claimed.

## 4. Full T4 integrability, including simultaneous collisions

Let \(v(x)=-\log(2|\sin\pi x|)\), an L1 circle function bounded below
by \(-\log 2\). Its nonzero Fourier coefficients are
\(\widehat v(k)=1/(2|k|)\). The periodized Gaussian

\[
 G_t(x)={t\over2\sqrt\pi}\sum_{m\in\mathbb Z}
                  e^{-t^2(x+m)^2/4}
\]

is nonnegative, integrates to one, and has Fourier multiplier
\(e^{-(2\pi k/t)^2}\); the last identity follows by integrating the
ordinary Gaussian over the real line. Consequently

\[
 \operatorname{Re}S_t=G_t*v\ge-\log2.
\]

Set \(h=e^{v/4}=(2|\sin\pi x|)^{-1/4}\) and
\(h_t=e^{(G_t*v)/4}\). Jensen's inequality and positive convolution give

\[
 h_t\le G_t*h,\qquad
 \|h_t\|_q\le\|h\|_q\quad(1\le q<4).\tag{5}
\]

Both signs occur twice. The two same-sign factors in (2) together have
modulus at most \(2^{1/2}\). Label the minus endpoints x,z and the plus
endpoints y,w, irrespective of their positions in the ordered word.
The four opposite-sign factors give the bound

\[
 |K_{t,\epsilon}|\le\sqrt2\,
 h_t(y-x)h_t(y-z)h_t(w-x)h_t(w-z).\tag{6}
\]

For any fixed 1<p<2, integrate first in y and w. Each integral is bounded
by Cauchy-Schwarz, uniformly in x,z:

\[
 \int h_t(y-x)^p h_t(y-z)^pdy\le\int h_t(y)^{2p}dy.
\]

Thus the full four-dimensional bound is

\[
 \|K_{t,\epsilon}\|_p^p
 \le2^{p/2}\|h_t\|_{2p}^{4p}
 \le2^{p/2}\left[\int_0^1(2\sin\pi x)^{-p/2}dx\right]^2<\infty.\tag{7}
\]

The bound is uniform in t and in all six sign patterns. An explicit
constant follows from the elementary beta integral: for 0<r<1,

\[
 I(r)=\int_0^1(2\sin\pi x)^{-r}dx
 ={2^{-r}\Gamma((1-r)/2)\over\sqrt\pi\Gamma(1-r/2)},
 \qquad \|K_{t,\epsilon}\|_p\le\sqrt2\,I(p/2)^{2/p}.
\]

This argument integrates over the **whole** T4 and does not discard
pair, triple, disjoint-pair or complete coincidences. The restriction
p<2 is a convenient sufficient range of this estimate, not a claimed
sharp integrability threshold for (4).

Off the collision sets, (2) converges to (4). Equation (7) yields uniform
integrability on a space of finite measure, so Vitali's theorem proves

\[
 \boxed{\ K_{t,\epsilon}\longrightarrow K_\epsilon
       \text{ in }L^1(\mathbb T^4)\ }.\tag{8}
\]

In fact the same reasoning gives Lq convergence for every 1<=q<2 by
choosing p strictly between q and 2. This is a complex-kernel result:
phase and modulus converge together. For any bounded joint test function
Phi on T4, the smeared amplitudes converge, with error at most
\(\|\Phi\|_\infty\|K_{t,\epsilon}-K_\epsilon\|_1\).
No extra contact measure can hide in this one-copy L1 limit. Taking eight
independent copies is a different integrability/distribution problem;
raising this L1 theorem to the eighth power is not justified.

## 5. Correct Gram orientation and the precise positivity statement

Consider the actual current pair vectors
\(\Psi_t(a,b)=Z_t^2W_t(a)^\dagger W_t(b)\Omega\). Their Gram kernel is

\[
 \langle\Psi_t(a,b),\Psi_t(c,d)\rangle
 =K_{t,-+-+}(b,a,c,d),\tag{9}
\]

**not** \(K_{t,-+-+}(a,b,c,d)\). Therefore for every bounded F on T2,

\[
 \int\overline{F(a,b)}K_{t,-+-+}(b,a,c,d)F(c,d)\,da\,db\,dc\,dd\ge0.
\]

The finite-t integral is the squared norm of the Bochner integral of the
pair vectors. Equation (8), unchanged under endpoint permutation, passes
this positivity to the limiting smeared form. This does not assert a
finite pointwise Gram matrix of unsmeared limiting vectors: its diagonal
contains a collision and grows like Z_t^4.

More generally let \(Y_s(a,b)=W_t(a)^{s_1}W_t(b)^{s_2}\Omega\).
The overlap with \(Y_r(c,d)\) uses endpoint/sign word
\((b,a,c,d);(-s_2,-s_1,r_1,r_2)\). If
\(s_1+s_2=r_1+r_2\), this is one of the six neutral words. Consequently
any finite family of two-letter types with the same *formal* sign sum
has a positive limiting matrix of smeared forms, including mixed +-/-+
types. No physical superselection law is inferred from that grouping.

These statements establish the displayed four-point Gram forms. They
do not establish all-order positivity, operator domains, charged zero
modes, locality/exchange axioms, OS reflection positivity or a complete
field reconstruction.

## 6. Interfaces to finite Current and microscopic words

The earlier Galerkin theorem controls the **whole normal-ordered finite
Current determinant** for any fixed word of total variation L, not just
its generator tail. Its explicit unnormalized error is

\[
 2L C(t)\sqrt{1+L^2ct/4}\,
           e^{L^2c/4-(M+1)/t},
\]

with c and C(t) defined in the pinned truncation contract. Multiplication
by Z_t^L supplies the normalized error. This is distinct from compressing
an already exponentiated multiplier, which introduces a spurious extra
occupation edge. The tests here compare all six four-leg determinants
to (1), and independently implement their fixed-number CAR words.

Unitarity in the current representation gives
\( |K_{t,\epsilon}|\le Z_t^L\). Differentiating (2) gives, per endpoint,

\[
 |\partial_{a_l}\log K_{t,\epsilon}|
 \le{(L-1)\pi\over2}\sum_{k\ge1}w_k
 \le{(L-1)\sqrt\pi\over8}t.
\]

The second inequality follows from integrating the decreasing Gaussian.
For t>=1, H_t<=2+log t, so the derivative of K itself is
\(O_L(t^{1+L/8})\), uniformly including collisions. Replacing endpoints
by their circle-grid representatives at mesh 1/N costs
\(O_L(t^{1+L/8}/N)\). In the fixed source scaling t=4 N^(1/4),
the L=4 interpolation error is O(N^(-5/8)). Thus a separately proved
uniform grid comparison of the microscopic four-word to (2) suffices
to transfer (8). Such a microscopic comparison is not proved by this
contract or by its finite Current tests.

In the original source \(U_a=e^{-iR}e^{iF_a}\). The physical alternating
word \(U_a^\dagger U_b U_c^\dagger U_d\) reduces exactly to
\(e^{-iF_a}e^{iF_b}e^{-iF_c}e^{iF_d}\). General neutral signed F-words
are legitimate auxiliary observables, but must **not** be renamed
general signed U-words: outer ramps do not cancel in arbitrary order.
For physical pair states V(a,b)=U_a^dagger U_b, the same (b,a,c,d)
Gram orientation applies. Endpoint normal-order phases must continue
to come from the per-leg trace, not from separately fitted pair phases.

## 7. Reproducible checks and boundaries

The checker has explicit input guards, including in optimized Python.
It checks frozen hashes before importing inherited implementations.
The tests independently cover sequential coherent composition, a
truncated single oscillator, fixed-number CAR words, all six finite
determinants, the complex interchange phase, branch, exact cancellations,
the correct Gram orientation and its wrong-orientation control, Lp
constants, Gaussian lower bound, and analytic series tails.

The diagnostic integral uses a staggered midpoint grid after exact
translation reduction from T4 to T3. This is ordinary floating numerical
quadrature, not an interval certificate or the proof of (8). The analytic
argument in section 4 is what controls arbitrarily close collisions.

All **15 tests pass in ordinary and optimized Python**. For M=16,t=8,
the largest absolute complex finite-Current error among the six words is
2.20e-14. The sampled pair Gram matrix has Hermiticity residual 6.10e-16
and minimum eigenvalue 0.05963; the naive two-pair Wick sum differs by
0.79425 at the recorded endpoints. These are floating checks of the
proved identities, not additional asymptotic claims.

At t=8,16,32,64, the staggered 20^3-point diagnostic mean absolute errors
against (4) are 0.4788, 0.3285, 0.2045, 0.1120. This fixed grid eventually
under-resolves collision layers; it is not a convergence rate. For
comparison the rigorous uniform p=3/2 norm bound from (7), evaluated in
floating arithmetic, is 3.00936 (rounded up here).

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s experiments/theory-contracts/current-fourpoint-limit -p test_checker.py -v
    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 -OO -B -m unittest discover -s experiments/theory-contracts/current-fourpoint-limit -p test_checker.py -v
    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 -B experiments/theory-contracts/current-fourpoint-limit/checker.py

The final command prints the diagnostic JSON; the checked-in
[diagnostics.json](diagnostics.json) records that output. No dense QWZ
matrices, historical sources, registry entries, paper or website are
changed here. All-order/higher-copy distributions and charged-field
construction remain separate obligations.
