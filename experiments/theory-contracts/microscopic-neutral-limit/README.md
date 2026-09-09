# Microscopic neutral two-point limit: low-energy control of full histories

2026-09-08, NON-RH. Written proof with independent internal mathematical review;
not an external peer review or proof-assistant certificate.
Scope: the original width-8, mass-1, sector-r=1 QWZ source, its negative
spectral occupation, Gaussian width delta=4N^(-3/4), and normal-ordered
neutral endpoint pairs. No charged field, eight-channel identification,
four-dimensional parent, T1–T8 or TOE completion is claimed.

## 1. Precisely which gap this closes

Keep the physical source and use the auxiliary objects from
`microscopic-energy-linearization`:

```
M=min(floor(N/8),floor(sqrt N)), t=N delta,
P=1_(H<0)=1_(Hsharp<0), Q=I-P,
J*J=I, PJ=J Pcur, R=I-JJ*,
Hsharp=J diag(-p_j)J*+RHR, p_j=(2pi j-pi/2)/N.
```

Endpoints a=L/N have integer 0<=L<N. Write B_a=ramp+pi Arc_a with Arc
on the top two rows, and Fsharp_a=Phi_(delta,Hsharp)(B_a). The half-cell
aligned current reference proved in `source-current-symbol-match` is

```
Tbar_a = D_N T_a D_N* - pi/(2N) I, D_N[j,j]=exp(i pi j/N),
Fref_a = J Tbar_a J* + R Phi_(delta,Hsharp)(ramp) R.
```

This is exactly Phi_Hsharp(Bref_a), where Bref_a has unsmoothed Tbar on J
and the compressed raw ramp on R. Both ||B_a||op and ||Bref_a||op are <=b=2pi;
their difference has norm <=Bdiff=4pi. The normal-ordered neutral reference
amplitude is unchanged by both the half-cell conjugation/scalar shift and
the common R term. Neither operation changes the source.

The separate J/J proof supplies the uniform bound

```
||J*Fsharp_a J - Tbar_a||op <= eJJ_N = O(N^-3/2).
```

We prove below the formerly missing complete-history estimate

\[
 \boxed{I_{\sharp,ref}=O(N^{-1}).}
\]

Together with the previous I_lin=O(N^-1/4), Aref=O(N^1/8), Z_t^2=O(N^1/16)
and the Current Galerkin estimate, this gives

\[
 \boxed{\sup_{a,b\in\{0,1/N,\ldots,(N-1)/N\}}
 |Z_t^2 C^\circ_N(a,b)-K_t(b-a)|=O(N^{-1/16})\to0.}
\]

Here C_N^circ is the full source determinant with its fixed endpoint
coboundary phase removed, not a small edge determinant or a fitted phase.
K_t is the previously fixed smoothed current kernel. Constants are very
coarse; the theorem does not claim small certified errors at modest N.

## 2. Exact low-energy inventory of the source remainder

Let Gamma=I_y tensor sigma_x. In its plus/minus spin basis the exact source
strip at momentum p is

\[
 H(p)=\begin{pmatrix}-\sin p\,I&A^*\\ A&\sin p\,I\end{pmatrix},
 \quad A=\rho I-S,\quad \rho=1-\cos p,
\]

where S is the eight-site unilateral shift. Its singular values are seven
ones and one zero at rho=0. Singular-value perturbation therefore puts the
seven larger singular values of A at least 1-rho=cos p whenever cos p>0.
The corresponding fourteen bulk eigenvalues of H have absolute value at
least cos p; every eigenvalue has absolute value at least |sin p|.

For principal |p| between pi/3 and 2pi/3, |sin p|>=sqrt(3)/2. For
|p|>=2pi/3, rho>=3/2 and the smallest singular value of A is >=rho-1>=1/2.
Thus any source eigenvalue of absolute value below 1/4 has |p|<pi/3.
The global absolute-energy lower bounds |sin p| and the outside-window
gap persist on each sign-preserving R compression. The bulk-only bound
cos p is not simply inherited after removing a tilted J; its corrected
compression bound is derived explicitly below.

Set

```
lambda = M/(8N), E_c=1_(|Hsharp|<=c), lambda<=1/64,
r = 8 lambda^2, s = 2 r^(15/2).
```

All modes in E_(2lambda) have |p|<=arcsin(2lambda)<=4lambda, except that
the explicit J modes obey the even stronger |p|<=2lambda. Hence rho<=r.
All these momenta belong to [-M,M]: a missing label has principal
|p|>2pi M/N, and, if |p|<pi/3, |sin p|>=2|p|/pi>4M/N>2lambda.

There is exactly one possible low source eigenvector of each sign at a
fixed such p. The normalized top/bottom quasimodes are

```
qtop(y) proportional rho^(7-y) chi_plus,
qbottom(y) proportional rho^y chi_minus,
|| (H+sin p)qtop ||=|| (H-sin p)qbottom || <=rho^8.
```

Their targeted-sign edge eigenvector is separated from all other
eigenvalues by at least |sin p| measured from the quasimode energy.
Indeed the opposite sign lies on the other side of zero, while the bulk
has cos p-|sin p|>0.9 in this small-p window. Consequently the normalized
edge eigenvectors differ, with phases aligned, from their quasimodes by
at most sqrt(2) rho^8/|sin p| <=2 rho^(15/2)<=s.
The same estimate applies to J versus qtop by its sign projection.
There is no p=0 in sector r=1.

The R compression removes the low top eigenvector, up to a quantitatively
negligible tilt. In detail, let vtop be the true top eigenvector. The bulk
part of J has norm <=rho^8/[sqrt(r0)(cos p-|sin p|)]<=2rho^8, where
r0=1-1/49152. Any unit x in its sign sector orthogonal to J therefore has
|<vtop,x>|<=2rho^8. Its sign-adjusted energy form is at least
cos p (1-4rho^16)>0.9. There is no residual low top mode in R.
The opposite sign is untouched by removing J and retains precisely the
true bottom eigenvector if its energy is within the chosen window.
For the displayed constants, r<=1/512 implies
cos p-|sin p|>=1-r-sqrt(2r)>=479/512 and sqrt(r0)>3/4.
If J=a vtop+w, the projection identity
||(I-JJ*)vtop||=||w|| gives the tilt bound without a hidden factor 1/|a|.

Therefore E_(2lambda) splits into selected J top modes and actual R bottom
modes, with no bulk or missing-window modes. The comparison isometries to
qtop and qbottom have operator errors <=s, not sqrt(number of modes) s:
different momenta remain orthogonal.

## 3. The low-energy source/operator match

Every actual raw B_a commutes with Gamma, so the ideal mixed top/bottom
matrix is **exactly zero**, at any two momenta. Replacing both ideal
isometries by the true ones costs at most 2b s in operator norm.
The bottom quasimode has top-two-row norm <=rho^6. Thus the low-bottom
part of the added arc has norm at most pi(r^6+s)^2.

Gaussian averaging is operator-norm contractive and commutes with the
spectral projections and the J/R splitting. Combining the separately
proved J/J part, the off-diagonal J/R part (its self-adjoint block matrix
has norm equal to the crossblock norm), and the R/R arc part gives

\[
 \|E_{2\lambda}(F^\sharp_a-F^{ref}_a)E_{2\lambda}\|_{op}
 \le e_N:=eJJ_N+2bs+\pi(r^6+s)^2=O(N^{-3/2}).
\]

This is only a low-energy estimate. To obtain the needed global comparison,
use Gaussian suppression rather than deleting the remaining blocks.
Put d=16N and g=exp(-lambda^2/(2delta^2)). An input in E_lambda and output
outside E_(2lambda) have energy difference at least lambda. Entrywise
filtering and ||B_a-Bref_a||HS<=Bdiff sqrt(d) give

\[
 \|(F^\sharp_a-F^{ref}_a)E_\lambda\|_{op}
 \le\epsilon_N:=e_N+Bdiff\sqrt d\,g.
\]

P/Q diagonal pinching is contractive, so the same bound holds for
(D_a-Dref_a)E_lambda, where D=PF P+QF Q. Also ||D-Dref||op<=Bdiff.

For C=QF P, opposite-sign energies have difference equal to the sum of
their absolute values. Splitting both sides at E_lambda therefore gives

\[
 \|C_a-Cref_a\|_{HS}
 \le c_N:=\sqrt d\,e_N+2Bdiff\sqrt d\,g.
\]

The two tail pieces are retained in this bound. A static-crossblock
estimate alone would still be insufficient; the next section controls
the diagonal frames that rotate it.

## 4. Energy tails of the complete reference frames

For any self-adjoint raw B of norm <=b and D=P Phi_Hsharp(B) P+Q Phi_Hsharp(B) Q,
energy-basis Gaussian multiplication gives, for v>=0,

\[
 \|e^{v|H^\sharp|}D e^{-v|H^\sharp|}\|_{op}
 \le b e^{v^2\delta^2/2}.
\]

Proof: separately on P and Q, |Hsharp| equals -Hsharp or Hsharp. Complete
the square in exp(+-v(E_i-E_j)-(E_i-E_j)^2/(2delta^2)). The shifted Gaussian
Schur multiplier is an average of unitary conjugations with a scalar
oscillatory weight, whose absolute integral is e^(v^2 delta^2/2).
The two sign blocks form a direct sum, so their maximum norm suffices.

Every forward or backward reference subword Uref of total raw variation
at most Lb therefore satisfies

```
||exp(v|Hsharp|) Uref exp(-v|Hsharp|)||op
 <=exp(Lb exp(v^2 delta^2/2)).
```

For a reference crossblock Cref and also its adjoint, completing the same
square with the opposite-sign energy gap gives

```
||exp(v|Hsharp|) Cref||HS <=b sqrt(d) exp(v^2 delta^2/2).
```

Choosing v=1/delta proves, uniformly for those subwords,

\[
 \|(1-E_\lambda)Uref\,Cref\|_{HS}
 \le b\sqrt d\,W e^{-\lambda/\delta},
 \quad W=\exp(Lb e^{1/2}+1/2).
\]

The same holds with Cref*. This estimate controls excursions during the
whole history; it does not assume a low-energy subspace is invariant.
The elementary finite-matrix proof is self-contained. General Gaussian
smearing methods are discussed in
[Bachmann et al., arXiv:2508.15913](https://arxiv.org/abs/2508.15913);
no spin-system theorem from that paper is assumed here.

## 5. Full right-evolving history comparison

For L unit legs, G'=iGD and Gref'=iGref Dref, Duhamel in the correct order is

```
G(s)-Gref(s) = i integral_0^s G(u)(D-Dref)(u) Uref(u,s) du,
Uref(u,s)=Gref(u)*Gref(s).
```

Use the E_lambda estimate before each insertion and the weighted tail
after it. Since ||Uref Cref||HS<=b sqrt(d), both Cref and Cref* give

```
||(G(s)-Gref(s)) Cref||HS
 <=s b sqrt(d) [epsilon_N+Bdiff W exp(-lambda/delta)].
```

The rotated cross difference is bounded by its direct difference plus
one frame difference on each side. Integration over 0<=s<=L yields

\[
 \boxed{I_{\sharp,ref}\le
 L c_N+L^2 b\sqrt d\,[\epsilon_N+Bdiff W e^{-\lambda/\delta}].}
\]

For L=2, b=2pi and M~sqrt N, lambda/delta=M/(8t)~N^(1/4)/32.
Every Gaussian/exponential tail beats any fixed power of N. Since
sqrt(d)e_N=O(N^-1), this proves I_sharp,ref=O(N^-1), with no deleted
diagonal blocks and no Fock operator-norm shortcut.

## 6. Combining the proved comparisons and smearing

For the full endpoint supremum the previous linearization estimate is used
with Btot<=4pi, not its narrower empty-to-arc constant 3pi.
The half-cell shift does not change the reference cross HS norm or its
common-rest heat-trace bound. Hence Aref=O(N^1/8) still holds. The triangle
inequality for histories and the pinned vacuum-history theorem give

```
Z_t² |C_source^circ-C_reference^circ|
 <= Z_t²(1+2sqrt(2) Aref)(I_lin+I_sharp,ref)
 = O(N^-1/16).
```

The separate whole-Current Galerkin error, after norming, is
O(N^(3/16)sqrt(log N) exp(-N^(1/4)/4)). Adding it proves Section 1.

There is also an actual smeared two-point limit, not just separated-point
values. Define the microscopic kernel piecewise constantly on endpoint
grid cells. The current kernel obeys

```
sup |K_t'| <= (pi/2) exp(H_t/4) sum_(k>=1) exp(-(2pi k/t)^2)
           = O(t^(5/4)).
```

Changing both endpoints to their grid representatives changes their
separation by at most 2/N, so the interpolation error is O(t^(5/4)/N)
=O(N^-11/16). The existing beta=1/4 current-model L1 theorem then implies
L1 convergence of the microscopic kernel on the endpoint square to

\[
 (1-e^{2\pi i(b-a)})^{-1/4},
\]

with the previously fixed analytic branch. Integrating against bounded
endpoint test functions is justified. Finite kernel positivity is retained
by endpoint rephasing, positive normalization and piecewise-constant
interpolation. This establishes a positive two-point form for the stated
neutral source construction, not a charged local field algebra.

## 7. Boundaries that remain open

No claim here establishes charged zero modes, a common adjoint-closed
field domain, higher-point products/exchange/locality, E8 gluing, a
microscopic eight-channel tensor factorization or a 3+1-dimensional theory.
In particular the single-kernel L1 bound cannot simply be raised to the
eighth power at coincident points to infer the weight-one distribution.
The original Hamiltonian and all physical choices are unchanged.
