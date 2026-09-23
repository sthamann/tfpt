# Odd-window direct-infimum numerical probe

Definitions are from *Universalraum-TFPT consolidated report 2026-09-10,
Q061 section 1*. For real \(f\) supported in \(J=(-L/2,L/2)\), this probe uses
\(Q=E+a_0\|f\|^2-2\sum w_n C_f(\log n)+P\), with the stated real-space
triangle-plus-potential formula for \(E\), \(a_0=-5.372183419225665\),
\(w_n=\Lambda(n)/\sqrt n\), and \(P=-2(\int\sinh(x/2)f(x)\,dx)^2\) for odd \(f\).

## Explicit-formula control

For \(L=9/4\) and \(f(x)=x(1-(2x/L)^2)^3\):

- Local \(Q(f)\): `4.305443474798082e-06`.
- Spectral value (600 positive zeros, both signs, smooth tail): `4.305443474798564e-06`.
- Local minus spectral: `-4.819617469876969e-19` (relative `1.1194241657306768e-13`).
- Smooth-density tail estimate after \(\gamma_{600}=939.0243008992184\): `1.3170295154150753e-18`.
- Real-space \(E\): `0.2928095081618558`; Fourier-control \(E\): `0.29280950816187`;
  difference: `-1.4210854715202004e-14`.
- Local terms: \(a_0\|f\|^2=-0.3477697158499732\), prime `0.06573021474017932`,
  pole `-0.010765701608587136`.

## Ritz upper bounds: lambda_min

| L | N=10 | N=20 | N=40 | N=80 | N=160 | N=320 |
|---:|---:|---:|---:|---:|---:|---:|
| 2.25 | 4.355714e-13 | 1.916653e-13 | 1.642428e-13 | 1.574694e-13 | 1.569129e-13 | 1.584097e-13 |
| 2.4 | 2.715052e-13 | 1.799730e-13 | 1.552964e-13 | 1.476863e-13 | 1.486713e-13 | 1.476786e-13 |
| 2.5 | -2.020007e-13 | -2.790668e-13 | -3.271912e-13 | -3.519463e-13 | -3.532373e-13 | — |
| 3 | -2.026009e-13 | -2.974895e-13 | -3.797551e-13 | -4.720653e-13 | -5.115650e-13 | — |
| 4 | -2.438224e-13 | -3.266312e-13 | -4.243766e-13 | -5.818706e-13 | -1.083893e-12 | — |

All entries have three eigenvalues in `result.json`. Deviations from exact
monotonicity and the displayed signs occur at the float64 cancellation floor.

## Largest-N decomposition and quadrature check

At \(L=2.25,N=320\): \(E=4.449881468733146\), \(a_0=-5.3721834192256654\),
Arch including \(a_0=-0.9223019504925194\), Prime `1.2023782464631376`,
Pole `-0.28007629597046124`, sum `1.5740261327411444e-13`, and
\(|f(L/2)|/\|f\|=1.3571593604488896e-07\).

At \(L=2.4,N=320\): \(E=4.3765386942734015\), \(a_0=-5.372183419225665\),
Arch including \(a_0=-0.9956447249522631\), Prime `1.3665830182779708`,
Pole `-0.37093829332556255`, sum `1.4763479353626157e-13`, and
\(|f(L/2)|/\|f\|=7.076568508956882e-08\).

Doubling triangle orders 680→1360 in each direction, potential 680→1360, and
prime/pole 650→1300 changed \(\lambda_{\min}\) by `-9.895604524017174e-13`
at \(L=2.25\) and `-1.0238862280227452e-12` at \(L=2.4\). Thus no digits or
sign near zero are quadrature-stable in float64.

## Limits

These are upper bounds on the odd-window infimum; float64; no rigorous tail
control; no independent review; no RH claim; a positive lambda_min is not a
certificate and a small lambda_min is not a negative Weil vector.

## Shell share of the near-null vectors (L = 12/5)

Here \(r_k=\|P_SF_k\|^2\), \(q_k=\lambda_k/r_k\), and the final column is the
cross-term lower bound divided by \(\|P_SF_k\|^2\). Every listed \(q_k\) is below
`0.0116212142999173`.

| N | k | lambda_k | r_k | q_k | Q_S/||v||^2 | Q_I/||f||^2 | load_k/||v||^2 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 80 | 0 | 4.0353e-14 | 6.7920e-7 | 5.9413e-8 | 2.576812 | 1.7338e-6 | 2.576868 |
| 80 | 1 | 4.7736e-14 | 4.8693e-7 | 9.8036e-8 | 2.578575 | 1.2439e-6 | 2.578631 |
| 80 | 2 | 5.4431e-14 | 7.0072e-8 | 7.7679e-7 | 2.568105 | 1.7827e-7 | 2.568161 |
| 80 | 3 | 5.8971e-14 | 1.5675e-9 | 3.7622e-5 | 2.525067 | 3.9203e-9 | 2.525087 |
| 80 | 4 | 6.1185e-14 | 6.3118e-8 | 9.6937e-7 | 2.552687 | 1.5960e-7 | 2.552743 |
| 80 | 5 | 6.3357e-14 | 3.8597e-8 | 1.6415e-6 | 2.581564 | 9.8711e-8 | 2.581619 |
| 80 | 6 | 6.6343e-12 | 5.3733e-4 | 1.2347e-8 | 2.347303 | 1.2490e-3 | 2.347365 |
| 160 | 0 | -3.2336e-13 | 6.8843e-7 | -4.6970e-7 | 2.607210 | 1.7783e-6 | 2.607267 |
| 160 | 1 | -3.1783e-13 | 3.3961e-10 | -9.3587e-4 | 2.840309 | 9.5648e-10 | 2.841299 |
| 160 | 2 | -2.7795e-13 | 3.6537e-9 | -7.6074e-5 | 2.592111 | 9.3829e-9 | 2.592243 |
| 160 | 3 | -2.4076e-13 | 7.6367e-8 | -3.1526e-6 | 2.628326 | 1.9888e-7 | 2.628384 |
| 160 | 4 | -2.1008e-13 | 7.7106e-8 | -2.7246e-6 | 2.674212 | 2.0434e-7 | 2.674269 |
| 160 | 5 | -1.5460e-13 | 7.2207e-8 | -2.1411e-6 | 2.713580 | 1.9420e-7 | 2.713636 |
| 160 | 6 | 5.9365e-12 | 5.3970e-4 | 1.1000e-8 | 2.346844 | 1.2543e-3 | 2.346906 |

The independent restricted-form computation gives no shell-floor violation:
all \(Q_S(v_k)/\|v_k\|^2\) exceed \(c_S=0.71162121429991727\). Doubling the
Gauss--Legendre order from 240 to 480 changes \(Q_S(v_k)\) by at most
`3.42e-13` and \(Q_I(f_k)\) by at most `1.03e-11`; per-vector differences are
stored in `result.json`.

For \(L=9/4\), the corresponding \((r_k,|F_k(L/2)|)\) values are:

| N | k | r_k | abs boundary value |
|---:|---:|---:|---:|
| 80 | 0 | 1.1351e-7 | 7.0643e-8 |
| 80 | 1 | 2.0510e-8 | 2.5870e-8 |
| 80 | 2 | 2.5884e-7 | 1.1166e-7 |
| 80 | 3 | 1.9220e-7 | 1.0118e-7 |
| 80 | 4 | 4.4187e-6 | 4.6903e-7 |
| 80 | 5 | 1.0375e-3 | 5.9546e-5 |
| 160 | 0 | 5.0797e-7 | 1.5276e-7 |
| 160 | 1 | 1.3481e-7 | 7.5320e-8 |
| 160 | 2 | 1.4144e-6 | 2.4032e-7 |
| 160 | 3 | 1.8017e-6 | 2.6715e-7 |
| 160 | 4 | 1.1351e-6 | 2.0671e-7 |
| 160 | 5 | 1.0419e-3 | 5.5835e-5 |

The float64 noise floor (about `1e-12` in \(\lambda_k\)) means that \(q_k\)
is an upper bound only to that precision. Near-null eigenvectors are
numerically mixed within their approximately `1e-13` cluster, so individual
\(r_k\) values are basis- and rounding-dependent, but every member of the
cluster is a legitimate numerical witness.
