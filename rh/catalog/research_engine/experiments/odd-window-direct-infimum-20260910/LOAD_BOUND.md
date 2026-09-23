# A lower bound on the shell-attachment load and the fate of the constant gate

10 September 2026. Research documentation for the queue items
`odd_shell_whole_input_coupling` / `odd_form_complete` (NEXT.md items 1–2).
NO RH CLAIM. No promotion, no Lean adapter, no change to sealed sources.

## 1. Inherited structure (as quoted in the consolidated report, Q061 §3, §7 and Q063 §1)

Old odd window I = (-9/8, 9/8), big window J = (-6/5, 6/5), shell S = J \ I.
For f in Dom Q_I and v in Dom Q_S (zero extension):

    Q_J(f + v) = Q_I(f) + Q_S(v) + 2 Re <f, X v>,                          (1)

X the explicit bounded cross operator (Gamma kernel, old translations, poles).
Old whole-odd certificate with response representation W = Y - Z0,
P160 W = I, M > 0 (80x80), C_s = D + V >= c > 0 on the high space:

    Q_I(f) - mu0 ||f||^2 >= (1/8) [ u^* M u + <w, C_s w> ],                (2)
    f = W u + w,  u = P160-coordinates of f,  w = (1 - P160)(f - W u).

Attachment load and target (Q061 eq. 14, Q063 eq. 1):

    load(v) := 8 (B_low v)^* M^{-1} (B_low v) + 8 ||B_high v||^2_{C_s^{-1}},
    B_low = W^* X,  B_high = (1 - P160) X,  d_new(v) = Q_S(v) - mu0 ||v||^2,
    full comparison (14):  load(v) <= d_new(v);
    constant gate (7):     load(v) <= tau ||v||^2,  tau = 7/10 < c_S = 0.71162...

where c_S ||v||^2 <= Q_S(v) is the proven shell floor (Q061 eq. 13).

## 2. Lemma (load is bounded below by the cross term)

For every f in Dom Q_I with A(f) := Q_I(f) - mu0 ||f||^2 > 0 and every v in Dom Q_S,

    load(v) >= |<f, X v>|^2 / A(f).                                        (3)

Proof. With u, w as in (2): u^* B_low v = <W u, X v> and <w, B_high v> = <w, X v>,
so u^* B_low v + <w, B_high v> = <f, X v>. Cauchy–Schwarz for the positive
forms M and C_s gives 8 x^* M^{-1} x >= 8 |u^* x|^2 / (u^* M u) and
8 ||y||^2_{C_s^{-1}} >= 8 |<w, y>|^2 / <w, C_s w>. By |alpha|^2/a + |beta|^2/b
>= |alpha + beta|^2/(a + b) and (2), load(v) >= 8 |<f, X v>|^2 / (u^*Mu + <w,C_s w>)
>= |<f, X v>|^2 / A(f).  QED

## 3. Corollary (the load carries the whole shell share of any near-null big-window vector)

Let F in Dom Q_J, f = P_I F, v = P_S F (legal split by Q061 §2), and
eps(F) := Q_J(F) - mu0 ||F||^2. By (1), 2 <f, X v> = eps(F) - A(f) - d_new(v). Then (3) gives

    load(v) >= (A(f) + d_new(v) - eps(F))^2 / (4 A(f)) >= d_new(v) - eps(F),     (4)

the last step being (A - (d_new - eps))^2 >= 0. Consequently

    constant gate (7) with tau  ==>  Q_J(F) - mu0||F||^2 >= (c_S - tau) ||P_S F||^2   for all F.  (5)

With tau = 7/10 the right side is >= 0.0116 ||P_S F||^2. So the constant gate can only
pass if every odd big-window vector has energy at least 1.16 percent of its shell
mass. Conversely, a single odd F with

    Q_J(F) / ||P_S F||^2 < c_S - 7/10 = 0.01162...                              (6)

refutes the constant gate (and, since K_J + (8/d_J) R^*R >= K by Q063 eq. 6, every
correctly certified finite-plus-tail version (7) of it, at every J).

The full comparison (14) is untouched: (4) shows only load >= d_new - eps, and
(14) holds iff the big window is (mu0-shifted) positive on that direction; the
two statements are equivalent in this direction, as expected.

## 4. Why such F exist (Fourier concentration below the first zero)

Q_J(F) = sum_rho |Fhat(gamma_rho)|^2 by the explicit formula (verified in this
folder's probe to 1.7e-10 relative on a smooth odd test function, `result.json`
`explicit_formula_control`). The first zero is at gamma_1 = 14.1347. An odd
function supported in a window of length L can concentrate all but a fraction
~ 1 - lambda_1(c) of its Fourier mass below gamma_1, c = gamma_1 L/2 (prolate
spheroidal concentration; the odd leading term is ~ sqrt(pi) 2^5 c^{3/2} e^{-2c}).
For L = 9/4 and 12/5 this fraction is ~ 1e-11 to 1e-12, so

    m(L) := inf { Q_J(F)/||F||^2 : F odd, supp F in J }  <~  1e-11   (L >= 9/4),

decreasing like e^{-gamma_1 L}. This is what the direct eigenvalue computation in
`result.json` shows: lambda_min(L) is at the float64 noise floor (|lambda_min| < 4e-13)
already for N = 10 odd Legendre modes, for every L in {9/4, 12/5, 5/2, 3, 4}, with
the decomposition E ~ 6.4, a0-term ~ -5.4, primes ~ -1.06, poles ~ -5e-5 cancelling
to 13 digits. Unless these near-null vectors vanish on the shell to relative mass
< 1e-10, (6) holds. The numbers for the actual near-null eigenvectors are in
`result.json` under `shell_share` (see §5) once computed.

## 5. Numerical check of (6)  (probe.py --shell-share, result.json key `shell_share`)

L = 12/5, near-null eigenvectors F_k (||F_k|| = 1), N = 80 (all lambda_k > 0) and N = 160:

    N=80:  lambda_k in [4.0e-14, 6.6e-12],  r_k = ||P_S F_k||^2 in [1.6e-9, 5.4e-4],
           q_k = lambda_k / r_k <= 3.8e-5  (all seven k),   required for the gate: >= 0.01162.
           Q_S(v_k)/||v_k||^2 in [2.347, 2.582]  (floor c_S = 0.7116 holds, by a factor > 3),
           Q_I(f_k)/||f_k||^2 in [3.9e-9, 1.2e-3],
           load lower bound (3)/||v_k||^2 in [2.347, 2.582]   versus the gate value 0.7.
    N=160: lambda_k in [-3.2e-13, 5.9e-12] (noise floor), |q_k| <= 9.4e-4, same Q_S range,
           load lower bound in [2.347, 2.841].

Quadrature doubling (240 -> 480 nodes) changes Q_S by <= 3.5e-13 and Q_I by <= 1.1e-11.
For L = 9/4 the near-null vectors have shell ratios 1e-8 ... 1e-3 and boundary values
|F(L/2)| ~ 1e-7 ... 6e-5: they are concentrated away from the boundary but not
confined; their shell share is nonzero and (6) holds with margin >= 300.

Hence the constant gate tau = 7/10 is violated by every near-null direction, and by
a factor of at least 3.3 (load >= 2.35 ||v||^2 versus 0.7 ||v||^2), not marginally.
The independently evaluated shell diagonal confirms the Q061 floor; its actual
values (~2.5) sit far above the floor, which is exactly why the floor-based gate
loses the whole shell share of the near-null directions.

## 6. Consequences for the queue

- REFUTED_SCOPED: the simpler constant-floor gate `||K|| <= 7/10` (and any tau < c_S),
  including its finite-plus-tail form (7) at J = 320 or any J. Reason: the floor
  d_new >= c_S ||v||^2 discards exactly the shell share of the near-null directions,
  whose load equals their d_new up to the (~1e-13) window energy.
- NOT refuted: the full comparison (14); it is equivalent to mu0-shifted odd positivity
  of the L = 12/5 window on each direction and therefore exactly as hard as the
  original whole-window problem. The shell decomposition does not lower the required
  precision: any certificate of the 12/5 window must resolve a margin
  <~ m(12/5) ~ 1e-12 (and ~ e^{-gamma_1 L} for larger windows). Constant-floor
  reductions of any kind cannot do this; only exact/high-precision positivity of the
  Fourier-concentrated (prolate-type) directions can.
- Reformulated next test for a cofinal odd family: control, on the local side
  (Gamma + primes + poles), the finitely many prolate-type directions concentrated
  below gamma_1 with precision e^{-gamma_1 L}; their positivity is the local encoding
  of "no zero below the concentration frequency". A method that does not use the
  location of the first zero cannot produce a positive constant floor at any L > ~1.
