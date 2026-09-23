# Geometric source charge, full-sea half shift and low-energy conservation

9 September 2026. NON-RH, source-specific mathematical research. This is a
written derivation with executable controls, not independent mathematical
review, a formal certificate, a half-transfer field or T1–T8 closure.

## 1. Observable and source; no second oscillator system

Keep the pinned QWZ cylinder `h_(N,r)=QWZ(N,8,1,r)` for r=1,3, its complete
negative spectral projector P_(N,r), and

```
s_N=N/(2 pi),
H_(N,r)=dGamma(s_N h_(N,r))-Tr(P_(N,r) s_N h_(N,r)).
```

The finite one-body space has dimension 16N and the actual sea has rank
8N. No occupied or massive mode is removed. Put T=I_x tensor T_cut, where
T_cut is the identity on both spin components of transverse rows y>=cut.
The main estimates use cut=4; every fixed cut in {1,...,7} has the same
limiting charge and half shift.

Use the already employed Gaussian width `delta_N=4 N^(-3/4)`, and define

```
A_(N,r)=delta_N/sqrt(2 pi) integral_R
          exp(-delta_N^2 t^2/2) exp(it h_(N,r)) T exp(-it h_(N,r)) dt.
```

This is an actual time average of a geometric density, not an assignment
of charge numbers to energy eigenvectors. Its energy-basis matrix entries
are `A_ab=T_ab exp[-(lambda_a-lambda_b)^2/(2 delta_N^2)]`.
It is a positive contraction and averaging I-T gives I-A. Define

```
Qtilde_(N,r)=dGamma(A_(N,r))-Tr(P_(N,r) T),
Ctop_(N,r)=dGamma(A_(N,r))-Tr(P_(N,1) T).
```

The first is normal ordered in its own sea; the second uses one common,
explicitly declared r=1 reference. Since P commutes with h, `Tr(PA)=Tr(PT)`
exactly. No fitted half constant is introduced.

An integrated charge has support along the whole circumference already
before time averaging. The averaged one-body operator is not strictly
supported in the original transverse region. No local half-field or
uniform full-Fock conservation follows from this construction.

## 2. A source-specific uniform bulk gap and marked edge branches

Let `p=2 pi(j-r/4)/N`, `rho=1-cos p`, and `s=sin p`. In the fixed eigenbasis
of the original SX, with all plus components followed by all minus ones,
the ACTUAL strip matrix is

```
h(p) = [[-s I, D], [D* , s I]],
D = rho I - shift_upper,                 dimension(D)=8.
```

This identity is checked against the original hopping matrices, including
their signs. Hence its eigenvalues are `+/-sqrt(s^2+d_i^2)`, where d_i are
the singular values of D. At rho=0 these are 0,1,...,1. For rho<=1 the
second and subsequent singular values are at least 1-rho. For rho>=1,
all singular values are at least rho-1. Since

```
sin(p)^2+(1-rho)^2=1,
```

there are at most two eigenvalues in (-1,1), at every momentum. All other
positive/negative pairs are separated by at least one if at least one
member is a bulk mode. This concerns the one-body spectrum; it is not an
assertion of a many-body gap in the circumference limit.

For `0<|p|<=1/4`, use the already sourced normalized quasimodes

```
q_top proportional to rho^(7-y) (1,1),
q_bottom proportional to rho^y (1,-1).
```

Their residuals at energies -s and s are at most rho^8. Indeed
`D* (rho^7,...,1)^T=(rho^8,0,...,0)^T`. Every eigenvalue other than the
corresponding marked edge eigenvalue is at distance at least 2|s| from
its quasimode energy: the opposite edge has that distance and the bulk
distance is at least `1-rho-|s|>=23/32>2|s|`.

Choose each exact edge eigenvector u with positive overlap with q.
Spectral projection of the residual gives

```
||u_edge-q_edge|| <= rho^8/|s|.                         (1)
```

Thus this small-momentum branch is selected by the original geometric
edge profile, not by freely naming eigenvectors. The exact vectors and
the previously used same-polarization vectors have vanishing difference;
the old filled-sea particle/hole embeddings are unchanged in the limit.

For cut=4, both geometric wrong-half quasimode probabilities equal
`rho^8/(1+rho^8)`. Consequently, with t_top=1 and t_bottom=0,

```
|<u,T u>-t_edge| <= (rho^4+rho^8/|s|)^2 =: epsilon_p^2.
```

The Gaussian average keeps eigenvector diagonal entries unchanged.
Positive contraction of A therefore implies

```
||(A-t_edge)u_edge|| <= epsilon_p.                     (2)
```

For each fixed Fourier label this is O(N^-8). For a different proper
transverse cut, use its exact geometric tail instead of rho^4. The worst
cut still gives O(N^-2), enough for the fixed-mode energy-graph statement.

The opposite-edge matrix element of T has an especially useful bound.
The two quasimodes have orthogonal SX spinors even after T, so their
cross element is zero. By (1),

```
|<u_top,T u_bottom>| <= 2 rho^8/|s| <= |p|^15/64,        (3)
```

using rho<=p^2/2 and |s|>=|p|/2. This bound holds for every proper cut.

## 3. The complete sea is controlled, including its energy

For any finite filled sea, the CAR identities give exactly

```
||Qtilde Omega||^2 = sum_(a positive,b negative) |A_ab|^2,
||H Qtilde Omega||^2
 = sum_(a positive,b negative) [s_N(lambda_a-lambda_b)]^2 |A_ab|^2.
```

These are sums over all 8N occupied and 8N unoccupied modes, not just an
edge compression. Translation invariance of T makes only equal momentum
blocks contribute. A separate four-mode full Fock calculation checks both
identities, including the adjoint/creation commutator.

On |p|<=1/4 the one potentially small-gap pair obeys (3). Its squared
filtered matrix element is at most `p^30 exp(-p^2/delta^2)/4096`.
For |p|>1/4, whenever a subgap pair exists, its gap is at least 1/4.
All other pairs have gap at least one. The strip norm is at most four,
so every one-body energy difference is at most eight.

The maximum of `x^(2m) exp(-x^2/delta^2)` is `(m/e)^m delta^(2m)`.
With harmless overcounting of the 64 pairs per block this proves

```
||Qtilde Omega||^2
 <= N (15/e)^15 delta^30/4096 + 65 N exp[-1/(16 delta^2)],           (4)

||H Qtilde Omega||^2
 <= N^3 (16/e)^16 delta^32/(1024 pi^2)
    + (1040 N^3/pi^2) exp[-1/(16 delta^2)].                       (5)
```

For (5), the low-p pair has gap at most 4|p| because its small singular
value is at most rho^8. Thus its rescaled gap squared is at most
`4 N^2 p^2/pi^2`. The remaining pairs use the uniform gap/norm bounds.

At the inherited delta_N, the polynomial parts of (4) and (5) are
respectively O(N^(-43/2)) and O(N^-21), and the other terms decay faster
than any inverse power. Both the vacuum fluctuation and its H graph norm
vanish. The displayed constants are intentionally loose; numerical tiny
variances below machine-resolution scales are not interval certificates.

The unfiltered density fails this test: the executed full-sea variance
grows approximately as 0.108087 N. Normal ordering alone subtracts its
mean, not its particle/hole fluctuations. Conversely, the filtered
one-body commutator norm on the whole source does NOT tend to zero in the
executed samples. The valid conservation statement is the low-energy
one below, not convergence in full-Fock operator norm.

## 4. Half a unit from the unrenormalized complete source sea

Put `f_cut(p)=Tr[T_cut 1_(h(p)<0)]`. There is only one zero crossing on
the momentum circle: det D=rho^8 implies h(p) is invertible unless p=0
modulo 2 pi. Away from it the negative projector is analytic.

At p=0 the two zero vectors are precisely the top and bottom row SX
spinors; every proper cut gives them weights 1 and 0. As p passes from
negative to positive, the occupied edge branch switches from bottom to
top. Therefore f_cut has a jump of exactly +1.

The jump is not a finite-p difference. The seven occupied massive modes
have a smooth, generally nonconstant contribution on both sides of zero.
This contribution must be retained when checking finite p.

For completeness the smoothness needed to sum the grid can be established
without assuming an infinite-volume Chern theorem. The smallest eigenvalue
of D*D is a simple isolated eigenvalue at rho=0 and is analytic in rho.
The corresponding left/right singular lines are analytic there. Their
signed coupling has a zero of order eight in rho, while sin p has a simple
zero. The edge 2-by-2 eigenprojection therefore continues analytically
across p=0 when labeled by its geometric edge, with off-diagonal mixing
of order p^15. For a cut adjacent to an edge, the wrong-region probability
is already O(p^4); interior cuts vanish to higher order. Hence subtracting
the unit step leaves at least two continuous derivatives. The massive
projector stays separated by a gap and is analytic near zero.

Define the periodic sawtooth, for -pi<p<pi, p!=0,

```
S(p)=sign(p)/2-p/(2 pi),
R_cut(p)=f_cut(p)-(8-cut)-S(p).
```

R_cut is periodic C2. Moreover the ACTUAL source has
`h(-p)=-C h(p) C`, `C=I_y tensor SX`, and [C,T_cut]=0. Thus
`f_cut(-p)=2(8-cut)-f_cut(p)` and R_cut is odd with zero mean.

For `a=r/4 in (0,1)` the shifted grid gives the exact identity

```
sum_(j=0,...,N-1) S(2 pi(j-a)/N) = a-1/2.                       (6)
```

For the smooth remainder, let
`B_cut=(1/(2 pi)) integral |R_cut''(p)| dp < infinity`.
Two integrations by parts bound its nonzero Fourier coefficients by
`B_cut/k^2`. Exact grid aliasing then gives

```
|sum_j R_cut(2 pi(j-a)/N)| <= pi^2 B_cut/(3N).
```

Consequently the original, UNNORMAL-ORDERED finite sea obeys

```
Tr(P_(N,r) T) = (8-cut)N + r/4-1/2 + O(N^-1),
Tr[(P_(N,3)-P_(N,1)) T] -> +1/2.                               (7)
```

The constant B_cut is finite by the written argument; it has not been
numerically interval-enclosed. The O(N^-1) claim is deliberately weaker
than some observed convergence rates. For I-T the difference is -1/2,
since each complete sea has exactly 8N particles.

This is independent of the former Abel/point-splitting prescription: it
uses finite full-source expectations and then N to infinity. It does not
contradict the zero obtained by coinciding the separately truncated
low-mode Abel covariances before their cutoff removal. Those are different
operations. In particular one cannot delete the massive covariance
contribution and still claim to have evaluated (7).

## 5. A limiting conserved charge with both adjoint Ward actions

Equations (4), (5), and (7) imply, for the actual r-sector vacuum,

```
Ctop_(N,r) Omega_(N,r) -> [(r-1)/4] Omega_(N,r)
```

in the compatible vacuum embeddings, including the H graph norm.
Thus the half value is not merely a noninteger expectation in a state
with persistent fluctuations: the variance vanishes too.

For a one-body eigenmode u the exact CAR identity is
`[dGamma(A),c*(u)]=c*(Au)`; the annihilation identity is its adjoint.
Use the original sea's particle/hole embeddings, with the asymptotically
equivalent exact geometric edge eigenvectors from Section 2. On a product
of k fixed creation/annihilation excitations, commuting Qtilde through the
product leaves at most k errors controlled by (2), plus its vacuum error.
The whole sea has already been included in (4); there is no extra 8N
factor in this finite-excitation estimate.

The energy graph estimate follows by also commuting H through that finite
product. Each input eigenmode has bounded rescaled energy. For a mode
error v, `||s_N h v||<= (2N/pi)||v||`; hence the cut=4 error is O(N^-7),
and even an outermost proper cut gives O(N^-1). The remaining vacuum term
is controlled by (5). The same estimate applied to
`[H,dGamma(A)]` gives a commutator tending to zero on each such fixed core.

Finite linear combinations therefore give strong, energy-graph convergence
on every fixed finite particle/hole core to

```
Ctop = q_top + b/2,
Cbottom = q_bottom - b/2,           b=(r-1)/2 in {0,1}.
```

The limiting charges commute with the sourced limiting dynamics and have
the correct +1/-1 action on top charged fields and their adjoints. At
every finite N the two common-reference regional operators sum EXACTLY to

```
Ctop_(N,r)+Cbottom_(N,r)=dGamma(I)-8N.
```

The limiting fractional regional offsets therefore do not change the
integer microscopic total charge. The regional Gaussian average is not
an exact integer-number projection at finite N; no impossible finite-N
half-step unitary for an integer total-charge spectrum is asserted.

## 6. What this closes, and what it does not

The earlier sector dictionary now has a geometric, full-sea source
observable with the right offsets, vanishing vacuum fluctuations, and
fixed-excitation energy/adjoint control. The construction does not require
an arbitrary nonlocal assignment of charge labels to eigenvectors.
It still uses a declared common r=1 reference, and does not prove that
TFPT uniquely chooses this measurement prescription.

The two background Hamiltonians are still distinct external source
backgrounds. Comparing their ground states is NOT executing adiabatic
flux insertion, selecting their direct sum physically, or producing an
operator V_N that changes r. Still missing is a source-derived intersector
field with a nonzero local smeared limit, energy control, both adjoints,
the correct half-charge Ward identity and integer carry on composition.
Nor are eight channels, Clock marking or the interacting rotor parent
identified by this calculation.

Fractional boundary response to background flux is not claimed as a new
general physical phenomenon. See the original
[Qi–Wu–Zhang model paper](https://arxiv.org/abs/cond-mat/0505308) and
[Yao–Fukusumi on background-field bosonization](https://arxiv.org/abs/1902.06584).
Their results are context, not substitutes for the source-specific
derivation above or for the missing TFPT field construction.
