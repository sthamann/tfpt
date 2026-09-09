# Whole finite-current determinant: a uniform Galerkin bridge

2026-09-08. **NON-RH. The finite-current-reference-to-current two-point
obligation is proved below, including phase and endpoint uniformity. The
microscopic QWZ-to-reference history estimate remains open. No charged-field,
local-net, eight-channel source identification or TOE claim is made.**

## 1. Result for the frozen reference

Keep exactly the matrices from `history-reference-transport`: labels
`j=-M,...,M`, occupied labels `j>=1`, and

\[
 (T_a)_{jl}=\begin{cases}
 {i e^{-2\pi i(j-l)a}\over2(j-l)}
 e^{-\frac12(2\pi(j-l)/t)^2},&j\ne l,\\
 \pi/2+\pi a,&j=l.
 \end{cases}
\]

Write

\[
 C^\circ_{M,t}(a,b)=e^{-i\operatorname{Tr}P_M(T_b-T_a)}
 \det\nolimits_{\operatorname{ran}P_M}
       (P_M e^{-iT_a}e^{iT_b}P_M).
\]

The separate current-model value from `neutral-current-limit` is

\[
 C_t^{\rm cur}(a,b)=
 \exp\left[-{H_t\over4}+{1\over4}
 \sum_{k\ge1}{w_k\over k}e^{2\pi ik(b-a)}\right],\quad
 w_k=e^{-(2\pi k/t)^2},\quad H_t=\sum_{k\ge1}w_k/k.
\]

**Theorem.** Define, for t>=1,

\[
 c={e^{1/(2\pi^2)}\over2\sqrt{2\pi}},\qquad
 C(t)=e^{1/(4\pi^2)}
 \left({\pi\over\sqrt6}+{\sqrt{2+\log t}\over2}\right).
\]

Then, uniformly in all real endpoints a,b,

\[
 \boxed{|C^\circ_{M,t}(a,b)-C_t^{\rm cur}(a,b)|
 \le4C(t)\sqrt{1+ct}\exp\left(c-{M+1\over t}\right).}
\]

This is a bound on the whole complex determinant, not on its generator or
only its modulus. The right side can exceed the trivial bound at small M;
it is an asymptotic estimate, not a tight small-matrix enclosure.

For the frozen choice `M=floor(N/8)`, `t=4N^(1/4)`, and the fixed endpoint
normalization `Z_t=exp(H_t/8)`, it follows that

\[
 \boxed{\sup_{a,b} Z_t^2
 |C^\circ_{M,t}(a,b)-C_t^{\rm cur}(a,b)|
 =O\left(N^{3/16}\sqrt{\log N}\,e^{-N^{3/4}/32}\right).}
\]

The estimate includes coincident and approaching endpoints; it does not
claim uniform convergence of the singular *final* continuum kernel itself.
The proof below supplies all cutoff estimates; it invokes no uniform
Szego or Fisher-Hartwig theorem.

**Mesoscopic-window corollary.** If a subsequent source comparison declares
the different reference choice `M=min(floor(N/8),floor(sqrt N))`, the same
general-M theorem applies without changing its constants. For N>=64,
`M=floor(sqrt N)` and `(M+1)/t>=N^(1/4)/4`. Thus

\[
 \sup_{a,b} Z_t^2|C^\circ_{M,t}-C_t^{\rm cur}|
 =O\left(N^{3/16}\sqrt{\log N}\,e^{-N^{1/4}/4}\right).
\]

This is a separate declared reference-window corollary, not a relabeling
of the frozen linear-window measurements in Section 8. Neither reference
window changes the microscopic source.

## 2. The common infinite reference space and its energy

Use the charge-zero polarized fermion Fock space with vacuum occupation
`n_j^0=1_(j>=1)`. Its finite-excitation basis has energy

\[
 L=\sum_{j\in\mathbb Z}(j-1/2)(n_j^0-n_j)\ge0.
\]

Introduce currents

\[
 J_k=\sum_j:c^*_{j+k}c_j:,
 \quad [J_k,J_l]=k\delta_{k,-l}I,
 \quad J_k\Omega=0\ (k>0),
 \quad a_k=J_k/\sqrt k\ (k>0).
\]

Here normal ordering subtracts `n_j^0` on diagonal bilinears. In charge zero,
`J_0=0`. The usual boson-fermion identification gives
`L=sum_(k>0) k a_k^*a_k`. These conventions are the reflection of the
filled-negative convention reviewed in
[Savage, *A geometric boson-fermion correspondence*, Section 1, pp. 4–6](https://arxiv.org/pdf/math/0508438).
That source supplies the standard Fock/Heisenberg identification, not the
finite-cutoff estimate proved here.

For completeness, the algebraic justification needs only CAR and energy
counting. The normal-ordered bilinear commutator telescopes to the displayed
central term on finite-energy vectors. Products of `J_-k` on the vacuum
are orthogonal with the oscillator norms and energy `sum k n_k`. The
charge-zero fermion basis is indexed by partitions with that same energy.
The partition counts match in every finite-energy eigenspace, so the
oscillator basis spans it. Completion yields the energy identity used
below; an unproved microscopic bosonization assumption is not being made.

For the smoothed function f_a with Fourier coefficients `(T_a)_(j,l)`,
the charge-zero current is

\[
 J(f_a)=\sum_{k>0}\sqrt k\left((f_a)_k a_k+
                  (f_a)_{-k}a_k^*\right).
\]

Its Weyl unitaries exist since `sum k |(f_a)_k|^2=H_t/4<infinity`.
Their vacuum word is the stated current comparator, with the positive
central/BCH phase fixed in `neutral-current-limit`.

## 3. What the finite operation actually compresses

Let Pi_M be the Fock projection that freezes every occupation outside
`[-M,M]` at its original vacuum value. Inside that window it permits all
states with exactly M particles. This is a finite-dimensional space;
it is **not** a new vacuum with every mode above M empty.

**Exact compression identity:**

\[
 \Pi_MJ(f_a)\Pi_M\big|_{\operatorname{ran}\Pi_M}
 =d\Gamma(T_a)-\operatorname{Tr}(P_MT_a)I=:K_{M,a}.
\]

To prove this, examine the normal-ordered bilinears. Terms connecting the
window to its complement change an outside occupation and vanish after
compression. Off-diagonal terms wholly outside also vanish, or leave
outside excitations removed by Pi_M. Normal-ordered outside diagonal terms
vanish because those occupations are frozen. The surviving inside terms
are exactly the right side. In particular the scalar Fourier coefficient
`f_0=pi/2+pi a` multiplies `number_inside-M=0`. Thus diagonal phase removal
is exact for each leg, not merely when endpoint signs add to zero.

Consequently

\[
 \langle\Omega,e^{-iK_{M,a}}e^{iK_{M,b}}\Omega\rangle
 =C^\circ_{M,t}(a,b).
\]

Extend `K_(M,a)=Pi_M J(f_a) Pi_M` by zero on the complement. Comparing its
unitaries with the true current unitaries is a Fock Galerkin problem.
No equality `exp(i Pi J Pi)=Pi exp(iJ) Pi` is asserted.

## 4. The exact energy cost of reaching an outer cutoff

Pi_M commutes with L and

\[
 I-\Pi_M\le1_{[M+1,\infty)}(L).
\]

Indeed the first missing positive label is j=M+1. A hole there costs
M+1/2, and charge zero requires a compensating particle costing at least
1/2. Equality M+1 is attained with the particle at j=0. A particle at the
first missing negative label j=-M-1 instead costs M+3/2, plus at least
1/2 for its compensating hole: total M+2. Extra excitations only increase
these costs. This tracks the asymmetric boundary labels explicitly.

## 5. Weighted current norms and coherent-state energy tails

Put `h_k=(f_a)_k`, so `|h_k|^2=w_k/(4k^2)`, independent of a. For s>=0
define

\[
 S_0(s)=\sum_{k>0}|h_k|^2e^{2sk},\quad
 S_1(s)=\sum_{k>0}k|h_k|^2e^{2sk},\quad
 C_s=2\sqrt{S_0(s)}+\sqrt{S_1(s)}.
\]

Bosonic Cauchy-Schwarz and CCR give

\[
 \left\|e^{sL}J(f_a)e^{-sL}\xi\right\|
 \le C_s\|(L+1)^{1/2}\xi\|.
\]

Explicitly, for an annihilator `A=sum g_k a_k`,
`||A xi||<=sqrt(sum |g_k|^2/k) ||L^(1/2)xi||`; its adjoint has the extra
bound `sqrt(sum |g_k|^2)||xi||`. Under energy conjugation the creation
coefficients gain `e^(sk)` and annihilation coefficients gain `e^(-sk)`.
Bounding both by the positive weight proves the displayed inequality.

Consider any partial current word with total absolute leg length at most
ell. Its state psi is coherent up to a phase, with oscillator displacements

\[
 |\alpha_k|^2\le {\ell^2w_k\over4k}.
\]

The exact coherent-state energy generating function therefore gives

\[
 \|(L+1)^{1/2}e^{sL}\psi\|
 \le \exp\left({\ell^2D_s\over8}\right)
       \sqrt{1+{\ell^2E_s\over4}},
\]
\[
 D_s=\sum_{k>0}{w_k\over k}(e^{2sk}-1),\qquad
 E_s=\sum_{k>0}w_ke^{2sk}.
\]

This follows either from independent oscillator occupation distributions,
or by differentiating
`||e^(sL)psi||^2=exp(sum |alpha_k|^2 (e^(2sk)-1))`.
The Gaussian coefficients make every sum finite for every fixed s.

Choose s=1/t. For x>=0,
`-4pi^2 x^2+2x <= -2pi^2 x^2+1/(2pi^2)`. Integration of the decreasing
Gaussian sum gives

\[
 E_{1/t}\le ct,\quad D_{1/t}\le(2/t)E_{1/t}\le2c,
 \quad S_0(1/t)\le e^{1/(2\pi^2)}\pi^2/24,
\]
\[
 S_1(1/t)\le {e^{1/(2\pi^2)}\over4}(2+\log t),
 \qquad C_{1/t}\le C(t).
\]

For the harmonic Gaussian sum, split at `floor t`: the first part is at
most `1+log t`; its decreasing integral tail starts no lower than t/2
and is less than one. Also `e^x-1<=xe^x` proves the bound on D.

## 6. Duhamel for the whole word, with the phase retained

Write Pi=Pi_M and `Qcut=I-Pi` in this section only. For an ideal coherent
history state psi,

\[
 (J-\Pi J\Pi)\psi=Q_{\rm cut}J\psi+\Pi JQ_{\rm cut}\psi.
\]

Use the energy-cost inequality on the first term after J, and on the
second term before J. Since Pi commutes with L, the preceding norm bounds
give

\[
 \|(J-\Pi J\Pi)\psi\|
 \le (C_s+C_0)e^{-s(M+1)}
             \|(L+1)^{1/2}e^{sL}\psi\|.
\]

For example, the first norm is at most
`e^(-s(M+1)) ||e^(sL) J psi||`; the second is bounded by
`C_0 ||(L+1)^(1/2)Qcut psi||`. Both have exactly the displayed majorant.
The coherent states lie in all the required weighted domains. One may
first truncate the oscillator sums and then use these convergent bounds
to justify the identity and Duhamel integral on their natural closures.

Both current and Galerkin propagators are unitary. Duhamel applied to the
ideal history, with total variation ell, consequently proves

\[
 \left|\langle\Omega,\prod_r e^{i\epsilon_rK_{M,a_r}}\Omega\rangle
       -\langle\Omega,\prod_r e^{i\epsilon_rJ(f_{a_r})}\Omega\rangle\right|
 \le2\ell C(t)\sqrt{1+\ell^2ct/4}
       e^{\ell^2c/4-(M+1)/t},\quad \ell=\sum_r|\epsilon_r|.
\]

The pair theorem is ell=2. Normal-ordering constants are part of each
generator before Duhamel; the central phase is therefore preserved, not
estimated from a determinant modulus afterwards.

For the frozen scaling, `(M+1)/t>=N^(3/4)/32` and
`Z_t^2<=exp(1/2)t^(1/4)`. The pair bound thus has polynomial prefactor
`O(t^(3/4)sqrt(log t))`, proving Section 1. Every fixed unit-coefficient
word likewise survives its finite power of Z_t because the exponential
cutoff decay dominates every power. This is a reference-word statement,
not construction of charged field domains in the microscopic model.

## 7. The finite trace anomaly and the wrong two-edge operation

The proof does not pretend that the finite current commutator is central.
For the truncated one-particle shift S_k, k<=M,

\[
 [d\Gamma(S_k),d\Gamma(S_k^*)]
 =d\Gamma(1_{\rm upper\ k}-1_{\rm lower\ k}).
\]

Its full finite-Fock trace is zero, while its vacuum expectation is k:
the upper k labels are filled and lower k labels empty. It is not kI.
The cutoff terms matter on sufficiently excited states; Sections 4–6
control precisely those states rather than discarding the anomaly.

A different operation, compressing the *completed* infinite one-particle
multiplier to occupied labels 1,...,M, introduces a second empty exterior
above M. Already at quadratic order, for a real Fourier symbol g,

\[
 \operatorname{Tr}(P_{[1,M]}g(1-P_{[1,M]})gP_{[1,M]})
 =2\sum_{k>0}\min(k,M)|g_k|^2.
\]

There are two boundary crossings instead of the half-line's
`sum k|g_k|^2`. This exact counting identity diagnoses the extra edge; it
is not a substitute for a determinant theorem. The checker independently
evaluates this **different** completed-multiplier operation by Fourier
quadrature. At t=8,d=1/4 it approaches the real value `exp(-2 loss)` and
stays about 0.163244 from the correct complex current value. No general
Szego limit is invoked from that numerical control.

## 8. Finite checks and remaining microscopic boundary

The frozen-current half-circle errors for the whole complex determinant are:

| N | M | Absolute finite-current error |
| ---: | ---: | ---: |
| 8 | 1 | 2.5042e-3 |
| 16 | 2 | 2.7984e-4 |
| 24 | 3 | 1.9560e-5 |
| 32 | 4 | 1.6213e-5 |
| 64 | 8 | 2.9964e-8 |
| 128 | 16 | 3.4128e-13 |
| 256 | 32 | floating roundoff, approximately 8.1e-15 |

The diagnostic also checks quarter/eighth separations, d=1/N approaching
coincidence, and translated endpoints. The estimates above are proofs;
these floating-point values are ordinary corroboration, not certificates
below the roundoff floor. Large N=1024,4096,16384 entries evaluate only
the explicit analytic envelope, not large determinants or QWZ matrices.

Thirteen tests independently cover fixed-number CAR versus the whole determinant,
normal-ordered Fock compression, the noncentral finite commutator, exact
outside-window energy cost and low-energy partition counts, phase removal,
translation/cancellation, determinant convergence, the wrong compression
control and exact two-edge counting, non-neutral normal ordering, both window
scalings, the explicit envelope, and input guards in normal and -OO modes.

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B experiments/theory-contracts/current-truncation-bridge/checker.py --output experiments/theory-contracts/current-truncation-bridge/diagnostics.json
python3 -B -m unittest discover -s experiments/theory-contracts/current-truncation-bridge -p test_checker.py
python3 -OO -B -m unittest discover -s experiments/theory-contracts/current-truncation-bridge -p test_checker.py
```

This closes the previously separate finite-reference-to-smoothed-current
obligation for the declared reference and scaling. Its normalized two-point
kernel inherits the already proved current-model L1 limit; eight independent
reference copies inherit the current distributional limit, since their
finite normalization powers also lose to the exponential cutoff bound.

The actual QWZ-to-reference rotated-history rate remains a distinct open
problem. This theorem neither changes the original QWZ source nor proves
microscopic bosonization, charged zero modes, E8 gluing, local field domains,
or any T1–T8/TOE completion.
