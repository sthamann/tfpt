# Exact sampled source-to-current symbol match on J

2026-09-08. **NON-RH. This proves the original-source J/J operator block
comparison after same-P energy linearization. J/R, R/R and complete rotated
histories are not proved in this contract. No charged-field or TOE claim.**

## 1. Scope and statement

Keep the actual r=1, mass-1, width-8 QWZ source and its same-P projected top
isometry J from `microscopic-energy-linearization`. Use

```
M=min(floor(N/8),floor(sqrt(N))), -M<=j<=M,
p_j=(2pi j-pi/2)/N, delta=4 N^(-3/4), t=N delta,
B_a(x,y)=pi x/N + pi 1_(0<=x<aN) 1_(top two rows),
a=L/N, L=0,...,N-1.
```

Write `Phi_lin` for the Gaussian filter on J with exact energies -p_j.
The ordinary finite-current matrix is T_a. Define one common halfcell change

\[
 D_N=\operatorname{diag}(e^{i\pi j/N}),\qquad
 \overline T_a=D_NT_aD_N^*-{\pi\over2N}I.
\]

This is a declared common reference coordinate change, not a fitted pair
phase. It is exactly inert for whole normal-ordered current words (§3).

Put

\[
 p_*={2\pi M+\pi/2\over N},\quad \rho_*=1-\cos p_*,\quad
 \gamma_*={\rho_*^{15/2}\over\sqrt{2-\rho_*}},\quad d_*=1-\pi^2/96.
\]

**Theorem.** Uniformly on all original lattice endpoints,

\[
 \|\Phi_{\rm lin}(J^*B_aJ)-\overline T_a\|_{op}
 \le E_N:=6\pi\rho_*^2+4\pi\sqrt2\,\gamma_*
 +{\pi^2\over6d_*N^2}
   \left({t^2\over4\pi^2}+{t\over2\sqrt{2\pi}}\right).
\]

The first two terms bound the transverse raw profiles and their actual
spectral polarization; the last bounds the filtered discrete sampling.
Because `rho_*=O(N^-1)`,

\[
 E_N=O(N^{-3/2}),\qquad
 \|\Phi_{\rm lin}(J^*B_aJ)-\overline T_a\|_{HS}
 \le\sqrt{2M+1}\,E_N=O(N^{-5/4}).
\]

These estimates concern this block, not its replacement inside an otherwise
uncontrolled full microscopic history. All constants and source choices are
independent of a. No numerical fit is used.

## 2. Exact discrete Fourier coefficients, including the diagonal

The twist cancels between bra and ket, so the longitudinal mode difference
is `k=j-l`. For k!=0 and z=exp(-2pi i k/N), the normalized sums are exactly

\[
 R_k={\pi\over N^2}\sum_{x=0}^{N-1}xz^x
     =-{\pi\over N(1-z)},\qquad
 (A_a)_k={1\over N}\sum_{x=0}^{L-1}z^x
         ={1-z^L\over N(1-z)}.
\]

Consequently the ideal scalar top symbol is

\[
 (R+\pi A_a)_k=-{\pi e^{-2\pi ika}\over N(1-e^{-2\pi ik/N})}
 ={i e^{-2\pi ika}\over2k}\,
   e^{i\pi k/N}{\pi k/N\over\sin(\pi k/N)}.
\]

At k=0 the exact coefficient is

\[
 (R+\pi A_a)_0={\pi(N-1)\over2N}+\pi a
 ={\pi\over2}+\pi a-{\pi\over2N}.
\]

Thus the halfcell phase has positive sign and the diagonal correction has
negative sign. Omitting either is not the exact source symbol. The finite
window has `|k|<=2M<=N/4`, so no nonzero alias denominator vanishes.

## 3. The halfcell change is amplitude-inert and has raw norm at most 2pi

On matrix Fourier coefficients, `Tbar_a=T_(a-1/(2N))`, with the latter
understood through its explicit Fourier formula also at negative a.
Equivalently it is precisely `D_N T_a D_N^* - pi/(2N) I`.
Since D_N commutes with Pcur, a word with real coefficients epsilon_l gains
only the scalar `exp(-i pi sum epsilon_l/(2N))` on one-particle space.
Its occupied determinant gains that scalar to power M. The simultaneous
normal-ordering phase changes by exactly the opposite factor. Hence

\[
 e^{-i\sum_l\epsilon_l\operatorname{Tr}P_{cur}\overline T_{a_l}}
 \det_{P_{cur}}\!\left(P_{cur}\prod_l e^{i\epsilon_l\overline T_{a_l}}P_{cur}\right)
 =e^{-i\sum_l\epsilon_l\operatorname{Tr}P_{cur}T_{a_l}}
 \det_{P_{cur}}\!\left(P_{cur}\prod_l e^{i\epsilon_lT_{a_l}}P_{cur}\right).
\]

This holds even when the word is not neutral. In a neutral word the scalar
factor itself also cancels. No individual overlap is rephased by a fit.

The unsmoothed T_a is the finite Fourier compression of the real function
`f_a(u)=pi u+pi 1_[0,a)(u)`, bounded between zero and 2pi. Therefore

\[
 -{\pi\over2N}I\le\overline T^{raw}_a
 \le\left(2\pi-{\pi\over2N}\right)I,
 \qquad \|\overline T^{raw}_a\|_{op}\le2\pi.
\]

Positivity of Tbar itself is not assumed: the translated symbol minus the
constant can be slightly negative. Gaussian averaging is unital and positive,
so the same operator-norm bound holds after smoothing. This supplies the
uniform raw reference norm without an additional N-dependent constant.

## 4. Transverse profiles: an operator estimate without sqrt(M)

First use the normalized unprojected source quasimodes q_j. With r=0 the
top row, their transverse amplitudes are

\[
 a_r(j)={\rho_j^r\over\sqrt{\sum_{s=0}^7\rho_j^{2s}}},
 \quad r=0,...,7,\quad \chi_+=(1,1)/\sqrt2.
\]

Let A_r be the diagonal matrix of a_r(j), and let V be their full twisted
Fourier isometry. Write R_N,A_N for the finite longitudinal ramp and arc
compressions; `0<=R_N<=pi I`, `0<=A_N<=I`. The source compression is exactly

\[
 V^*B_aV=A_0(R_N+\pi A_N)A_0
       +\sum_{r=1}^7 A_rR_NA_r+\pi A_1A_NA_1.
\]

The last term is present because the actual arc occupies the top **two**
rows. Since the normalized geometric profile obeys

\[
 \sum_r A_r^2=I,\quad
 \|I-A_0\|\le\|I-A_0^2\|\le\rho_*^2,\quad
 \|A_1\|^2\le\rho_*^2,
\]

the first term differs from `R_N+pi A_N` by at most `4pi rho_*^2`.
Positivity bounds the remaining ramp sum by `pi(I-A_0^2)` and the second-row
arc term by `pi A_1^2`. Altogether

\[
 \boxed{\|V^*B_aV-(R_N+\pi A_N)\|_{op}\le6\pi\rho_*^2.}
\]

For the geometric-profile inequality, the tail fraction satisfies
`1-a_0(j)^2=(rho_j^2-rho_j^16)/(1-rho_j^16)<=rho_j^2`.
There is no column-count loss because these are diagonal weights and
positive operator sums, rather than entrywise error accumulation.

Now replace V by the actual source isometry J. The wrong-sign part of q_j
is bounded by `rho_j^8/|sin p_j|<=gamma_*`, as proved in the pinned
same-P construction. Normalizing its selected spectral projection gives
`||J_j-q_j||<=sqrt2 gamma_*`. Different momentum columns remain orthogonal,
including their differences, hence `||J-V||op<=sqrt2 gamma_*`. Since
`||B_a||op<=2pi`,

\[
 \boxed{\|J^*B_aJ-V^*B_aV\|_{op}\le4\pi\sqrt2\,\gamma_*.}
\]

These two raw estimates survive Phi_lin because the Gaussian average is
operator-norm contractive.

## 5. Filtered sampling estimate

After the exact halfcell and diagonal changes, only
`x/sin x-1`, `x=pi k/N`, remains in the scalar Fourier comparison.
For `|x|<=pi/4`, Taylor's elementary lower bound on sin gives

\[
 0\le{x\over\sin x}-1
 \le{x^2\over6(1-x^2/6)}\le{x^2\over6d_*}.
\]

Gaussian smoothing at energies -p_j multiplies the k-th coefficient by
`exp(-2pi^2 k^2/t^2)`. Each error entry is bounded by

\[
 {\pi^2|k|\over12d_*N^2}e^{-2\pi^2k^2/t^2}.
\]

The maximum row and column sums, hence the operator norm, are at most
`pi^2/(6d_*N^2) sum_(k>=1) k exp(-2pi^2 k^2/t^2)`. For c>0,

\[
 \sum_{k\ge1}ke^{-ck^2}
 \le\int_0^\infty(x+1)e^{-cx^2}\,dx
 ={1\over2c}+{\sqrt\pi\over2\sqrt c}.
\]

On each interval [k-1,k], both `(x+1)>=k` and `exp(-cx^2)>=exp(-ck^2)`
prove the inequality. Substituting `c=2pi^2/t^2` supplies the last term in
E_N. Combining the three independent errors proves the theorem.

## 6. A separate exact diagonal check

The diagonal of the true projected block is

\[
 (J^*B_aJ)_{jj}={\pi(N-1)\over2N}
                +\pi a\|P_{top2}J_j\|^2.
\]

Therefore its difference from the translated current diagonal is exactly

\[
 -\pi a\|(I-P_{top2})J_j\|^2,
 \quad |\text{difference}|
 \le\pi(\rho_*^2+\sqrt2\gamma_*)^2=O(N^{-4}).
\]

The raw quasimode norm below the first two rows is at most rho_j^2;
combine this with the projected-vector bound and square. Filtering does
not change diagonal entries. The occupied trace of this defect is at most
M times the displayed bound, O(N^(-7/2)). Thus the scalar `-pi/(2N)` has
not silently been left as an error or folded into the transverse estimate.

## 7. Reproduction and the boundary of this result

The checker constructs source strip matrices through the unchanged pinned
implementation. Its exact overlap formula is independently compared with
the full original N=8 cylinder and on-site observable, not only another
version of the same closed-form Fourier sum. All grid endpoints are checked
for the small discrete Fourier identities; larger diagnostics use five
declared endpoints including the empty arc and L=N-1.

Representative half-circle filtered J/J operator errors are:

| N | M | Measured operator error |
| ---: | ---: | ---: |
| 64 | 8 | 1.7595e-2 |
| 128 | 11 | 1.0588e-3 |
| 256 | 16 | 1.0003e-4 |
| 512 | 22 | 3.8498e-5 |
| 2048 | 45 | 5.2225e-6 |

These are ordinary floating diagnostics, not interval enclosures or fitted
rates. At large N the tiny polarization correction is below the floating
precision floor; its rate is established by the analytic bound, not those
rounded values. The explicit bounds are intentionally conservative.

Nine tests cover exact Fourier/diagonal/sinc identities, full-source J/J
compression and polarization, actual diagonal losses, the three error
components, whole normal-current-word invariance, raw norm, exact linear
Gaussian filtering and input rejection under both normal and -OO Python.

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B experiments/theory-contracts/source-current-symbol-match/checker.py --output experiments/theory-contracts/source-current-symbol-match/diagnostics.json
python3 -B -m unittest discover -s experiments/theory-contracts/source-current-symbol-match -p test_checker.py
python3 -OO -B -m unittest discover -s experiments/theory-contracts/source-current-symbol-match -p test_checker.py
```

The codegraph was checked first and contained no TFPT index; the permitted
direct source fallback was used. No older source, index, paper or website
was changed. This contract supplies only the J/J part of a larger proof:
it does not assert J/R or R/R decoupling, control complete diagonal-frame
excursions, or infer a charged field from a small inner-block error.
