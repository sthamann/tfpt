# Source-polarized reference transport and inert neutral spectators

2026-09-08. **NON-RH. Exact finite reference construction, a sufficient
history-rate target, and small unchanged-source measurements. Not a uniform
microscopic determinant limit, charged field, or TOE closure.**

## Result

The missing common polarization in `polarization-history-bridge` can be
constructed explicitly from the actual QWZ top quasimodes. A reference
completion that retains the original empty-arc generator on its complement
has exactly the same neutral reference determinant as zero padding, while
its full rotated-history distance is substantially smaller in the first
source tests. This distinction is mathematical, not an amplitude fit.

An exact two-mode counterexample shows why a small, or even zero, neutral
determinant error cannot select an adequate reference history. A separate
source heat-trace estimate bounds the completed reference history by
`A0=O(N^(1/8))`. Consequently `I_N=o(N^(-3/16))` is an explicit sufficient
source-to-reference requirement after the existing endpoint normalization;
it needs no unproved `A0=O(sqrt(log N))` assumption. The rate itself remains
unproved.

Only this directory is new. All upstream source files are read without
modification, and their existing hash chain is checked.

## 1. Fixed source and declared choices

Use the original cylinder with circumference N, width 8, mass 1 and sector
r=1. Write `P=1_(H<0)`, `Q=I-P`, `delta=4N^(-3/4)` and `t=N delta`.
There is no zero-mode occupation choice in this sector. Let `F_a` be the
existing Gaussian-filtered top-two-row arc plus the fixed ramp; `F_0` is
the source empty-arc generator, not the zero matrix. In this document `a`
is a fractional endpoint, so `a=1/4` means a lattice arc of length N/4.
The diagnostic requires N divisible by four, rather than silently rounding
that endpoint.

The auxiliary reference window is `j=-M,...,M`, `M=floor(N/8)`. This is an
explicit non-fitted cutoff choice, not a new derived physical constant.
The reference is the finite Fourier truncation of the previously fixed
current comparator. It is **not** assumed equal to the microscopic source.

## 2. Exact source-polarized isometry

For each selected label define

\[
 p_j={2\pi j-\pi/2\over N},\qquad \rho_j=1-\cos p_j,
\]
\[
 q_j(x,y)={e^{ip_jx}\over\sqrt N}
 {\rho_j^{7-y}\over\sqrt{\sum_{s=0}^7\rho_j^{2s}}}\chi_+,
 \qquad \chi_+=(1,1)/\sqrt2.
\]

These are the unchanged source top quasimodes from
`half-twist-grade-carry`. Their directly verified strip identity is

\[
 \|(H+\sin p_j)q_j\|
 ={\rho_j^8\over\sqrt{\sum_{s=0}^7\rho_j^{2s}}}\le\rho_j^8.
\]

Set `Pcur_j=1` for j>=1 and zero for j<=0, following the source dispersion
`E_top=-sin p_j`, not an arbitrary occupied-eigenvector ordering. Define

\[
 Je_j=\begin{cases}
 Pq_j/\|Pq_j\|,&j\ge1,\\
 Qq_j/\|Qq_j\|,&j\le0.
 \end{cases}
\]

**Lemma.** For every N>=8 with the declared window, J is well-defined and

\[
 J^*J=I,\qquad PJ=JP_{\rm cur},\qquad
 \|P_{\text{selected sign}}q_j\|^2\ge1-1/49152.
\]

**Proof.** The wrong-sign spectral part has distance at least `|sin p_j|`
from the quasimode energy, so its norm is at most `rho_j^8/|sin p_j|`.
Here `0<|p_j|<=pi/4+pi/(2N)<=5pi/16<pi/3`. The function
`(1-cos p)^8/sin p` is increasing on `(0,pi/3]`: its logarithmic derivative
is `8 cot(p/2)-cot p>0`. Its value at pi/3 is `1/(128 sqrt3)`.
Squaring proves the retention bound. Twisted translation commutes with
the actual H and hence P,Q. The selected momentum characters are distinct,
so their projected columns remain mutually orthogonal. Normalization then
proves both identities. This gives an exact identification, not merely
equal dimensions.

The numerical implementation makes this projection in the actual energy
basis and checks isometry and polarization. The analytic estimate concerns
the default window; a manually overridden cutoff does not inherit that
estimate without checking its domain.

## 3. The finite current reference and a neutral spectator lemma

Let `k=j-l`. The reference matrices are

\[
 (T_a)_{jl}=\begin{cases}
 {i e^{-2\pi i k a}\over2k}
 e^{-\frac12(2\pi k/t)^2},&k\ne0,\\
 \pi/2+\pi a,&k=0.
 \end{cases}
\]

They are Hermitian and retain the current Fourier sign and the original
normal-ordering convention. Put `R_J=I-JJ*`, which commutes with P. For
any one Hermitian operator S supported on `R_J`, define

\[
 F^{\rm ref}_a=JT_aJ^*+S.
\]

**Neutral spectator lemma.** If `sum_l epsilon_l=0`, then

\[
 \prod_l e^{i\epsilon_lF^{\rm ref}_{a_l}}
 =J\left(\prod_l e^{i\epsilon_lT_{a_l}}\right)J^*+R_J.
\]

The filled-P determinant and its phase-removed counterpart therefore equal
their finite-current versions on `Pcur`, for every such fixed neutral word.

**Proof.** On `ran J` each factor is the finite-current factor. On `ran R_J`
all factors are exponentials of the same S, hence their product is the
identity when the sum of coefficients is zero. Since J intertwines P and
Pcur, the occupied determinant splits into the current determinant and an
identity determinant. The normal-ordering phase is

\[
 \theta_{\rm ref}=\sum_l\epsilon_l\operatorname{Tr}(P_{\rm cur}T_{a_l})
 +\Big(\sum_l\epsilon_l\Big)\operatorname{Tr}(PS),
\]

so the spectator contribution also cancels. Non-neutral words do not have
this conclusion. No diagonal phase is discarded in the source comparison.

The checker compares two declared choices:

1. **Zero completion:** S=0.
2. **Source-empty completion:** `S=R_J F_0 R_J`, using the same original
   empty-arc generator at every endpoint.

The second is not a claimed microscopic decoupling theorem: source couplings
between J and its complement, as well as endpoint-dependent source changes
inside the complement, still enter the measured full history error.

## 4. Why neutral amplitudes alone cannot choose the history

Take `P=diag(1,0)`, `K=c sigma_x` with real c>0, source legs `(-K,K)`, and
reference legs `(0,0)`. Both normal-ordered neutral determinants are exactly
one. Both diagonal blocks of K vanish. Nevertheless the two source history
legs have crossblock norms c, so

\[
 I=\int_0^2\|Q(B-B_0)P\|_{\rm HS}\,ds=2c.
\]

For c=.4 the checker obtains I=.8 exactly to floating precision. This
counterexample persists for every N if inert modes are added. It does not
prove that the actual zero-completed QWZ reference fails asymptotically;
it proves that equal amplitudes cannot rule out this failure.

The source-empty completion is motivated by this specific mechanism: the
empty ramp acts also on the opposite edge and other modes during both
source legs. Shared excursions can cancel at the endpoint while remaining
visible to an inverse-free history comparison.

## 5. An explicit sufficient target without an assumed logarithmic bound

For any endpoint, orthogonal support of J and R_J gives exactly

\[
 \|QF^{\rm ref}_aP\|_{\rm HS}^2
 =d_N+r_N,\quad
 d_N=\|Q_{\rm cur}T_aP_{\rm cur}\|_{\rm HS}^2\le H_t/4,
 \quad r_N=\|QSP\|_{\rm HS}^2.
\]

The current inequality follows because at Fourier difference k there are
at most k occupied-to-unoccupied pairs, each of squared magnitude
`exp(-(2pi k/t)^2)/(4k^2)`. Its norm is endpoint-independent. For two unit
legs the reference quantity in the history theorem is therefore
`A0(2)=2 sqrt(d_N+r_N)` exactly.

For the source-empty completion, `r_N<=||QF_0P||HS^2`. Write `R(x)=pi x/N`
for the source ramp, so `F_0=Phi_delta(R)` and `||R||<=pi`. In the H energy
basis, opposite signs give `(E_i-E_j)^2>=E_i^2+E_j^2`. Hence

\[
 \|QF_0P\|_{\rm HS}^2
 =\sum_{E_i\ge0,E_j<0}|R_{ij}|^2e^{-(E_i-E_j)^2/\delta^2}
 \le\pi^2\operatorname{Tr}e^{-H^2/\delta^2}.
\]

The already source-proved counting bound
`n_low(a)<=2Na+2` for `a<=1/4`, and the full dimension 16N, imply

\[
 \operatorname{Tr}e^{-H^2/\delta^2}
 =\int_0^\infty {2a\over\delta^2}e^{-a^2/\delta^2}n_{\rm low}(a)\,da
 \le \sqrt\pi N\delta+2+16N e^{-1/(16\delta^2)}=:L_N.
\]

Extend the low-count integrals to infinity and integrate the remaining
16N tail from 1/4 to prove the last inequality. Also `H_t<=2+log t` for
t>=1, by splitting its Gaussian sum at t. Thus an explicit envelope is

\[
 A_0(2)\le2\sqrt{(2+\log t)/4+\pi^2 L_N}
 =O(\sqrt t)=O(N^{1/8}).
\]

The finite history theorem supplies

\[
 |C_N^\circ-C_{{\rm ref},N}^\circ|
 \le I_N(1+2\sqrt2 A_0(2)).
\]

Since `Z_t^2=O(t^(1/4))=O(N^(1/16))`, the **proved-reference-envelope**
sufficient target is

\[
 \boxed{I_N=o(N^{-3/16}).}
\]

This is stronger than the earlier conditional target
`o(N^(-1/16)/sqrt(log N))`, but does not assume a logarithmic spectator
estimate. If `r_N=O(log t)` can later be proved, the weaker target becomes
available again. Neither history rate is asserted by the measurements.
The independent normalized finite-reference-to-infinite-current error must
still vanish; the history theorem does not supply that limit.

## 6. First unchanged-source discriminator

All runs use the same reference and regulator choices, no parameter fit.
The half-circle results below use the full rotated P/Q histories, including
the diagonal rotations on both legs:

| N | I, zero rest | I, source-empty rest | Conditional-rate indicator, source-empty | Source-to-finite-current relative error |
| --- | ---: | ---: | ---: | ---: |
| 8 | 0.877232 | 0.475138 | 0.780254 | 0.035839 |
| 16 | 0.832105 | 0.276596 | 0.547705 | 0.008877 |
| 24, unchanged intermediate holdout | 0.854565 | 0.194088 | 0.422030 | 0.004864 |
| 32 | 0.880224 | 0.150146 | 0.347122 | 0.003069 |

Here the displayed conditional-rate indicator is
`I_N N^(1/16) sqrt(log N)`, not a proof of its limit. The record also saves
`I_N N^(3/16)` for the proved-envelope target. Quarter-circle histories
show the same finite trend. At N=8,16,32 the current/spectator squared
crossblock norms are respectively `(0.10640,0.13669)`,
`(0.14573,0.15327)`, `(0.18517,0.18780)`. Their apparent near equality is
observational, not an identity or logarithmic estimate.

The two completions' reference amplitudes agree with their identical
finite-current determinant within 7e-14. Gauss-Legendre orders five and
seven differ by less than 5e-9 in these history integrals. **This is not an
interval enclosure or rigorous quadrature error bound.** Small-N trends
do not establish asymptotic powers, endpoint-uniformity, or near-diagonal
control. The heat-trace envelope is rigorous but intentionally loose at
these small sizes.

## 7. Reproduction and remaining gate

Run from the repository root with a single BLAS thread, for example:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B experiments/theory-contracts/history-reference-transport/checker.py --sizes 8 16 32 --output experiments/theory-contracts/history-reference-transport/diagnostics.json
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B experiments/theory-contracts/history-reference-transport/checker.py --sizes 24 --output experiments/theory-contracts/history-reference-transport/holdout_N24.json
python3 -B -m unittest discover -s experiments/theory-contracts/history-reference-transport -p test_checker.py
python3 -OO -B -m unittest discover -s experiments/theory-contracts/history-reference-transport -p test_checker.py
```

Eleven tests cover the actual source quasimode residual and polarization,
current Fourier bound, neutral-word completion, its non-neutral boundary,
HS orthogonality, exact excursion counterexample, correct right-path order,
the source heat-trace envelope, and input rejection without Python asserts.

The immediate mathematical gate is now specific: bound the full rotated
source-to-completed-reference histories by `I_N=o(N^(-3/16))`, uniformly on
the endpoint domain needed for smearing, and separately control the
normalized finite-current truncation. The construction removes the missing
polarization identification and an avoidable spectator mismatch. It does
not identify microscopic charged fields, settle zero modes, establish all
word domains/locality, or close T1-T8.
