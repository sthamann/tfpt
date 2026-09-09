# Same-polarization energy linearization: an analytic sub-bridge

2026-09-08, NON-RH. This proves a contribution to the microscopic-to-current
comparison, not that whole comparison, a charged field, or a TOE. The physical
source, its Gaussian width, vacuum and raw observables remain unchanged.

## 1. A mesoscopic reference choice

Use the pinned r=1, mass=1, width-8 QWZ cylinder H on 16N modes and its actual
negative-energy projector P. Set

```
delta = 4 N^(-3/4), t = N delta,
M = min(floor(N/8), floor(sqrt(N))), N >= 8,
p_j = (2 pi j - pi/2)/N, -M <= j <= M.
```

This changes only the auxiliary current window. It does not retroactively
change the older fixed-window diagnostics in `history-reference-transport`.
The latter construction applies to every such smaller window. Its polarized
top-edge isometry J obeys J*J=I and PJ=J Pcur, Pcur=1_(j>=1).
Let R=I-JJ*. Momentum orthogonality is exact in the actual twisted cylinder.

The raw top profile q_j has transverse components proportional to
rho_j^(7-y)(1,1), rho_j=1-cos(p_j). Its exact residual is

```
||(H+sin(p_j))q_j|| = rho_j^8 / sqrt(sum_(s=0)^7 rho_j^(2s)).
```

J_j is the normalized P q_j for j>=1 and normalized (I-P)q_j otherwise.
Since |p_j| <= p_*=(2pi M+pi/2)/N <= 5pi/16 < pi/3, the earlier spectral
projection estimate gives retained norm squared at least
r0=1-1/49152. Indeed rho<=1/2 and
rho^8/|sin p|=rho^(15/2)/sqrt(2-rho)<=1/(128 sqrt(3)).
The residual columns have different momenta, so

\[
 \|HJ-J\Lambda_{\sin}\|_{op}\le
 \varepsilon_N={(1-\cos p_*)^8\over\sqrt{r_0}},
 \qquad \Lambda_{\sin}=\operatorname{diag}(-\sin p_j).
\]

There is no extra square root of the number of columns here.

## 2. An auxiliary Hamiltonian with the same vacuum

Define, for comparison only,

\[
 H^\sharp=J\operatorname{diag}(-p_j)J^*+RHR.
\]

It is Hermitian and has exactly the same negative spectral projector P.
On J the prescribed eigenvalue -p_j has the selected sign. On R, compression
of the strictly negative/positive source forms retains that sign. Also
[R,P]=0, so the two signs do not mix. No zero is introduced at r=1.

If E=HJ-J Lambda_sin, then J*E is Hermitian and exactly

```
H - (J Lambda_sin J* + RHR) = E J* + J E* - J(J*E)J*.
```

Using |p-sin p|<=|p|^3/6 proves the global operator bound

\[
 \boxed{\|H-H^\sharp\|_{op}\le\eta_N
       =3\varepsilon_N+p_*^3/6=O(N^{-3/2}).}
\]

For N>=64, M=floor(sqrt N) and p_* <= (33pi/16)N^(-1/2).
Thus epsilon_N=O(N^-8), while the cubic dispersion error is O(N^-3/2).
The rate follows from these inequalities, not a fit to finite spectra.

## 3. Gaussian-filter stability, including full histories

For any matrix B write

\[
 \Phi_{\delta,H}(B)=\int_{\mathbb R}
 {\delta e^{-\delta^2s^2/2}\over\sqrt{2\pi}}
 e^{isH}B e^{-isH}\,ds.
\]

Unitary Duhamel and the first absolute Gaussian moment give, for every
Schatten norm with 1<=p<=infinity, including the operator norm,

\[
 \boxed{\|\Phi_{\delta,H}(B)-\Phi_{\delta,H^\sharp}(B)\|_p
 \le\kappa_N\|B\|_p,\qquad
 \kappa_N=2\sqrt{2/\pi}\,\eta_N/\delta.}
\]

Specifically the integrand difference is at most
2|s| ||H-Hsharp||op ||B||p, and the first moment is sqrt(2/pi)/delta.
This finite-matrix lemma needs no gap or external locality theorem.
Gaussian smearing is also studied more broadly in
[Bachmann, Du, Fraas and Wessel, arXiv:2508.15913](https://arxiv.org/abs/2508.15913);
no result about their spin systems is being substituted for this proof.

For piecewise constant self-adjoint signed raw generators B_l, each leg of duration 1,
put b_l=||B_l||op and Btot=sum b_l. Compare the two filtered histories
K_l=Phi_H(B_l) and Ksharp_l=Phi_Hsharp(B_l), with the same P on both sides.
For the exact right-evolving diagonal frames from
`polarization-history-bridge`,

```
D_l = P K_l P + Q K_l Q,  G' = i G D,
rotated_cross = Q G (P K Q + Q K P) G* P.
```

Pinching is operator-norm contractive. At time s within leg l,
Bcum(s)=sum_(i<l)b_i+s b_l, and unitary Duhamel gives
||G-Gsharp||op <= kappa_N Bcum(s).
The direct cross difference is at most kappa_N b_l sqrt(16N) in HS norm.
The target cross norm is at most b_l sqrt(16N), since Gaussian averaging
is operator-norm contractive. Inserting the two frame differences yields

\[
 d_{lin}(s)\le\kappa_N\sqrt{16N}\,b_l(1+2B_{cum}(s)),
\]
\[
 \boxed{I_{lin}=\int d_{lin}(s)ds
 \le\kappa_N\sqrt{16N}(B_{tot}+B_{tot}^2)=O(N^{-1/4}).}
\]

This controls full rotated histories, including their diagonal-block
transport. It is not an estimate of static QKP alone. For the original
empty-to-arc pair, Btot<=pi+2pi=3pi, uniformly over endpoints. For a fixed
general word, its fixed total raw norm replaces 3pi. The prefactor is large;
the bound need not be numerically sharp at accessible N.
For two arbitrary nonempty endpoints, Btot<=4pi gives the same rate.
Moreover the normal-ordering phases agree exactly on each leg:
Tr(P Phi_H(B_l))=Tr(P B_l)=Tr(P Phi_Hsharp(B_l)), since P commutes with
both Hamiltonians. No phase comparison is being inferred from a modulus.

## 4. How this contributes to the normalized comparison

Use the common-rest reference

```
Fref_a = J T_a J* + Ssharp,
Ssharp = R Phi_(delta,Hsharp)(ramp) R.
```

Every neutral word cancels Ssharp exactly, including normal-ordering phase,
as in the previous reference construction. Its finite determinant is still
the same current determinant. Changing this common rest does not alter that
neutral reference amplitude.

The reference cross variation Aref remains O(N^(1/8)). To check that the
new rest preserves the old estimate rather than assuming it: by eigenvalue
perturbation and x^2 >= y^2/2-(x-y)^2,

```
Tr exp(-(Hsharp)^2/delta^2)
 <= exp(eta_N^2/delta^2) Tr exp(-H^2/(2delta^2))
 <= exp(eta_N^2/delta^2) [sqrt(2pi) N delta + 2
                              +16N exp(-1/(32delta^2))].
```

The last line is the pinned source heat-trace bound at width sqrt(2)delta.
For opposite signs, (E_q-E_p)^2>=E_q^2+E_p^2, so the filtered ramp cross
HS norm squared is bounded by pi^2 times this trace. Restricting to R
cannot increase it. The current part is bounded by H_t/4. Consequently the
reference-history bound with Z_t^2=exp(H_t/4)=O(N^(1/16)) gives for the
linearization contribution alone

\[
 Z_t^2(1+2\sqrt2 A_{ref}) I_{lin}=O(N^{-1/16})\longrightarrow0.
\]

Use the triangle inequality for histories to split I_source,ref into
I_lin + I_sharp,ref, and then the same final reference weight for both.
This is **not** a proof that I_sharp,ref vanishes.

## 5. The remaining exact target

Hsharp is block diagonal on J plus R and has exactly linear energy on J.
If Traw_a denotes the finite unsmoothed current matrix, then exactly

```
Fref_a = Phi_(delta,Hsharp)(J Traw_a J* + R ramp R).
```

Thus the outstanding source/current obligation is a comparison of the
actual raw ramp plus top-two-row arc with that raw reference, through the
same filter and complete P/Q histories. J-to-R leakage, transverse edge
profiles, the sampled longitudinal symbol and diagonal transport all remain
part of that obligation. A small dispersion defect alone cannot settle it.

The separate `current-truncation-bridge` estimate applies to this mesoscopic
M as well: its normalized error is
O(N^(3/16) sqrt(log N) exp(-N^(1/4)/4)). This closes another reference-only
step, not the remaining microscopic operator match.

The most concrete next gate is an endpoint-uniform bound
I_sharp,ref=o(N^(-3/16)), or a sharper direct vacuum estimate proving the
same normalized limit. After that, charged fields, products, domains and
the common four-dimensional parent remain separate obligations.

## 6. Verification and scope

`checker.py` pins the previous source and constructs only exact source
momentum strips, not guessed dispersion data. Tests independently compare
them with the full source cylinder and with its full energy-basis embedding.
Other tests cover Gaussian op/HS stability, complete rotating histories,
same spectral polarization and exact current smoothing under linear energy.
Finite diagnostics check implementation; Sections 1–4 supply the rate proof.

Run from this directory with `python3 -m unittest -v`, and repeat with
`python3 -OO -m unittest -v`. `python3 checker.py` prints finite diagnostics.
No original Hamiltonian, source pin, paper, website, or T1–T8 status is changed.
