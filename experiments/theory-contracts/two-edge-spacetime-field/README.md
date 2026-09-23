# Two-edge half-transfer: a sharp spatial obstruction and a spacetime construction

2026-09-09. **NON-RH. Conditional construction on the two sourced limiting
CAR representations. No microscopic intersector-field limit, locality,
eight-channel selection, or T1–T8 closure is claimed.**

The new result is not a fitted exponent. The opposite edge creates a
specific ultraviolet obstruction: spatial momentum is a **difference** of
edge levels whereas energy is their **sum**. Keeping both edges gives a
finite spatially smeared vacuum vector, but not a finite-energy vector.
Spacetime smearing gives a nonzero operator on a dense finite-current core
with a densely defined adjoint partner. Its microscopic origin remains open.

## 1. Precisely which source space is used

Keep the source, embeddings, generator, reference-charge convention, and
two backgrounds in [source-half-sector-bridge](../source-half-sector-bridge/README.md).
Work in its **declared total-charge-zero direct sum**, not an extra bosonic
Hilbert factor. For background b=0,1 and integer relative edge charge q,

\[
 p_t=q+b/2=:p,\qquad p_b=-p,\qquad p\in\tfrac12\mathbb Z.
\]

On the top edge use `J_k^t=sum_j :c*_(j+k)c_j:` and on the bottom edge
`J_k^b=sum_j :c*_(j-k)c_j:`. Both satisfy

\[
 [J_k^e,J_l^e]=k\delta_{k,-l},\quad J_k^e|p\rangle=0\ (k>0),
 \quad a_k^e=J_k^e/\sqrt k,\quad
 L_e=\sum_{k>0}k(a_k^e)^*a_k^e.
\]

The CAR/partition proof in
[current-truncation-bridge, Section 2](../current-truncation-bridge/README.md)
extends to each integer-charge vacuum by shifting the filled Fermi label.
The central term and partition counts do not change. Thus the oscillator
coordinates describe the sourced limiting fermion space; they do not
postulate an additional independent oscillator system. Even current
bilinears of opposite edges commute. The finite checks here retain a
protected CAR window and do not assert a central commutator on the entire
finite-dimensional Fock space.

The source energy and spatial translation generator on this neutral sum are

\[
 H=L_t+L_b+h(p),\quad h(p)=p^2-p/2\ge0,
 \qquad K=L_b-L_t.
\]

Indeed the two zero-mode edge energies are equal when `p_b=-p_t`; they
cancel in K and add in H. Extend the previous carry map S to all current
descendants by intertwining their creation operators:

\[
 S|p;\nu_t,\nu_b\rangle=|p+1/2;\nu_t,\nu_b\rangle.
\]

The basis norms are unchanged, so S is a unitary on this direct sum.
It is not a cyclic two-state flip: S squared carries one integer unit
from bottom to top. It commutes with K and total charge, but
`[H,S]=Sp`. For the reference vacuum Omega at p=0,

\[
 H S\Omega=0,\qquad H S^*\Omega=\tfrac12 S^*\Omega.
\]

**Assumption boundary:** choosing this direct sum, the current prescription,
and an intertwiner with these phases is a limiting-model construction.
Neither the presence of both finite source backgrounds nor an isospectral
reflection selects a physical local operator connecting them. In particular
S is not identified with that reflection or a microscopic adiabatic pump.

## 2. A regulated operator with both adjoints and the source time evolution

Let real `0<=g_k<=1` obey `sum g_k^2/k<infinity` and approach 1 for each
fixed k along the regulator removal. This includes the previously used
Gaussian regulator and radial regulators. Put alpha=1/2 and

\[
 A_g(\theta)=\alpha\sum_{k>0}{g_k\over\sqrt k}
       \big(e^{-ik\theta}(a_k^t)^*-e^{ik\theta}(a_k^b)^*\big),
 \qquad
 V_g^+(0,\theta)=S e^{A_g(\theta)}e^{-A_g(\theta)^*}.
\]

The formula is first evaluated on finite-current vectors and has a bounded
extension: it is a Weyl unitary times

\[
 Z_g=\exp\left({1\over4}\sum_{k>0}g_k^2/k\right).
\]

The exponent is the sum of the two half-charge contributions, not the
single-edge factor `exp(sum g_k^2/k / 8)`. Define `V_g^-=(V_g^+)*` exactly.
Since S commutes with the oscillators, V minus has S star and the opposite
oscillator signs. Both transfer total charge zero and shift p by plus or
minus one half. Use the already sourced dynamics, without retuning it:

\[
 V_g^\pm(t,\theta)=e^{itH}V_g^\pm(0,\theta)e^{-itH}.
\]

Spatial covariance follows from K with the corresponding expression using
`e^(i theta K)`. The scalar Z diverges in the point-field limit; it is not
a uniform operator bound. No exchange law or locality is inferred.

## 3. Exact spatially smeared vacuum and its sharp energy threshold

For one edge the squared norm of coherent oscillator level n is

\[
 b_n={(a)_n\over n!},\qquad a=\alpha^2=1/4.
\]

This follows either from the occupation partitions or
`exp(a sum_(k>0) z^k/k)=(1-z)^(-a)`. The independent finite-CAR recurrence
used by the checker is `v_n=(alpha/n) sum_(k=1)^n g_k J_-k v_(n-k)`.
Its exact squared norms agree, including the opposite bottom sign and
nonzero integer relative source charges. At regulator g, the corresponding
coefficients lie between zero and b_n by the positive coefficient recurrence.

Write `fhat(k)=integral f(theta) exp(-ik theta) dtheta/(2 pi)`. Different
two-edge levels are orthogonal, so the forward spatially smeared vacuum has

\[
 \|V^+(f)\Omega\|^2
 =\sum_{n,m\ge0}b_nb_m|\widehat f(n-m)|^2
 =\sum_{k\in\mathbb Z}C_{|k|}|\widehat f(k)|^2,
\]

\[
 C_k=\sum_{n\ge0}b_nb_{n+k}
 ={\Gamma(1-2a)\over\Gamma(a)\Gamma(1-a)}
       {\Gamma(k+a)\over\Gamma(k+1-a)}.
\]

To obtain the last equality, factor out `(a)_k/k!` and apply Gauss summation
to `2F1(a,a+k;k+1;1)`, whose convergence condition is `1-2a>0`.
See [NIST DLMF 15.4.20](https://dlmf.nist.gov/15.4.E20).
In particular

\[
 C_0={\sqrt\pi\over\Gamma(3/4)^2},\qquad
 {C_{k+1}\over C_k}={k+1/4\over k+3/4}<1,
 \qquad \|V^+(f)\Omega\|^2\le C_0\|f\|_{L^2}^2.
\]

This is a bound on the **vacuum map**, not the full operator norm.
Individual occupation amplitudes converge and are dominated by the limiting
ones; the displayed summable norm therefore also proves the strong vacuum
limit for every L2 spatial f, for every allowed regulator sequence.

**Sharp domain theorem.** For nonzero smooth f and s>=0,

\[
 \boxed{V^+(f)\Omega\in D(H^s)\quad\Longleftrightarrow\quad s<1/4.}
\]

For necessity, choose a nonzero Fourier coefficient at k. Along the
orthogonal states `(n,n+|k|)`, energy is `2n+|k|`. By the gamma-quotient
asymptotic, `b_n~n^(-3/4)/Gamma(1/4)`, so the squared graph-norm summands
are a nonzero constant times `n^(2s-3/2)`. The series diverges for s>=1/4,
logarithmically at the endpoint. The asymptotic is
[NIST DLMF 5.11.12](https://dlmf.nist.gov/5.11.E12).

For sufficiency, `b_(n+k)<=b_n` and
`1+2n+k <= (1+2n)(1+k)` give an upper bound by the product

\[
 \left[\sum_{n\ge0}(1+2n)^{2s}b_n^2\right]
 \left[\sum_{k\in\mathbb Z}(1+|k|)^{2s}|\widehat f(k)|^2\right],
\]

finite when s<1/4. The adjoint vacuum has the same threshold; its energy
is shifted by 1/2. In particular neither spatially smeared nonzero vacuum
vector has finite expected energy (`D(H^(1/2))`). A spatially constant f
already exhibits the obstruction: all `n=m` have momentum zero but
arbitrarily large energy. Smoothing the difference n-m cannot suppress it.

## 4. Spacetime smearing controls the missing sum

For `F in C_c^infinity(R x S1)` (also Schwartz in time and smooth in space),
fix the transform convention

\[
 \widetilde F(\omega,k)=\int_{\mathbb R}dt\int_0^{2\pi}{d\theta\over2\pi}
             F(t,\theta)e^{it\omega}e^{ik\theta}.
\]

The exact forward vacuum identity is

\[
 \boxed{\|(1+H)^s V^+(F)\Omega\|^2
 =\sum_{n,m\ge0}b_nb_m(1+n+m)^{2s}
       |\widetilde F(n+m,m-n)|^2.}
\]

For the adjoint vacuum replace `n+m` by `n+m+1/2` in the energy weight
and the first transform argument. This asymmetry is fixed by the source
zero modes. At general charge vacuum p, the frequency is
`n+m+h(p +/- 1/2)-h(p)` and the output energy is
`n+m+h(p +/- 1/2)`; they need not be equal.

Repeated integration by parts in time gives
`|Ftilde(omega,k)| <= A_M(F)(1+|omega|)^(-M)`, uniformly in k, for every M.
The exact energy-shell convolution is

\[
 \sum_{n+m=\ell}b_nb_m={(1/2)_\ell\over\ell!}\le1.
\]

Consequently the norm above is bounded by
`A_M(F)^2 sum_l (1+l)^(2s-2M)`, finite, for example, when `M>s+1`.
The sharper convolution asymptotic gives `M>s+1/4`, but is not needed.
Coefficientwise convergence and the same majorant give strong convergence
in every `D(H^s)` graph norm as g is removed. The result is nonzero if,
for example, `Ftilde(0,0)` is nonzero for V plus. This is a positive
construction, not only a divergent-spatial-sum diagnosis.

## 5. Extension to a dense finite-current core and closability

Let D be the algebraic span of finitely many charge vacua and finite
oscillator creation monomials on each. It is dense in the declared source
direct sum. For a fixed monomial P of degree d, write its fixed-charge
input as `P(a*)|p>`. Normal ordering gives, at theta=0,

\[
 e^{A_g}e^{-A_g^*}P(a^*)\Omega
       =P(a^*-\overline\lambda_g)e^{A_g}\Omega,
\]

where `lambda_(t,k)=g_k/(2 sqrt k)` and
`lambda_(b,k)=-g_k/(2 sqrt k)`. Only the finitely many modes in P occur
in the polynomial shifts. Its coefficients are bounded uniformly in g.
On oscillator level l, a creation monomial of degree at most d has squared
norm bounded by a constant times `(1+l)^d`; its level shift is one of
finitely many fixed integers. The coherent-state squared level norms are
bounded by the preceding convolution, at most 1. Hence

\[
 \|\Pi_\ell V_g^\pm(0,0)P(a^*)|p\rangle\|^2
       \le C_P(1+\ell)^d
\]

with C_P independent of g. Here Pi_l selects output oscillator level l;
it includes all partitions and both edges. The estimate follows by the
finite triangle/Cauchy inequality over the shifted monomials, so destructive
or constructive interference is not ignored.

Split a general input in D into its finitely many joint H,K eigenvectors.
For each such input, every output matrix element of `V_g^pm(F)` is its
matrix element at `(0,0)` times
`Ftilde(Eout-Ein,Kout-Kin)`, by the two covariance identities. At large l,
`1+|Eout-Ein|` is comparable to `1+l` for this fixed input. Choosing M
larger than `s+(d+1)/2` therefore gives a summable graph-norm majorant.
The finitely many remaining levels have finite dimension. Coefficientwise
convergence on them proves a regulator-independent strong limit

\[
 V^\pm(F):D\longrightarrow\bigcap_{s\ge0}D(H^s).
\]

The constants and degree in this argument depend on the input monomial;
**this is not a uniform all-input energy bound.**

At every regulator, `(V_g^+(F))*=V_g^-(conjugate F)` because time evolution
is unitary and the zero-mode shift is reversed, including its changed
energy. Taking the strong limits on D yields the same sesquilinear identity
on D. Therefore `V^-(conjugate F)` on D is contained in the adjoint of
`V^+(F)` on D. Both adjoints are densely defined, and both constructed
operators are closable. This establishes individual smeared operators;
it does **not** establish an invariant common domain for their products,
boundedness, locality, or a field algebra of arbitrary words.

For context, [Constantinescu and Scharf, *Smeared and unsmeared chiral vertex
operators*](https://arxiv.org/html/hep-th/9712174) study smearing in chiral
representations. Their boundedness construction uses a specified Hilbert
space; it is not imported as a boundedness theorem for our full neutral
two-edge direct sum. The argument here is the explicit spectral/core
construction above.

## 6. Conditional eight-channel consequence: do not test only spatial smears

This is an implication **if** independent source pairs with these charges
are selected later, not evidence that eight such source pairs exist.
For d independent pairs at a common insertion, each edge has total weight
`beta=d/4` and level coefficient `b_n(beta)=(beta)_n/n!`. The same fixed
momentum argument now gives the spatial graph-norm threshold

\[
 s<1/2-\beta.
\]

Already at d=2 the spatial vacuum norm diverges logarithmically; for d>2
it also diverges. Specifically for d=8, beta=2 and `b_n=n+1`, so for the
constant spatial smear the exact cutoff norm is

\[
 \sum_{n=0}^N(n+1)^2={(N+1)(N+2)(2N+3)\over6}.
\]

Thus naively multiplying eight two-edge half-transfer factors cannot
produce an equal-time spatially smeared vacuum vector in this tensor
product representation. This does not rule out spacetime fields or a
different, independently derived channel construction. In fact

\[
 \sum_{n+m=\ell}(n+1)(m+1)=\binom{\ell+3}{3},
\]

so temporal Fourier decay of order `M>s+2` suffices for every vacuum
graph norm. Finite-current input again adds only a polynomial to the
bound in Section 5; smooth spacetime smearing still works. With the same
eight source generators the forward vacuum zero-mode energy is zero,
but the adjoint vacuum energy is 4, not zero. The checker verifies the
eightfold coefficient convolution, both polynomial identities, and this
zero-mode asymmetry. It does not supply an E8 cocycle or source selection.

## 7. What this resolves and the next acceptance test

- Resolved **within this candidate**: the exact spatial energy obstruction,
  a regulator-independent spacetime construction on D, the two charge
  directions with their actual energies, and a closability argument.
- Still open: a microscopic intersector operator with these limits;
  physical selection of the reference current and direct sum; a uniform
  energy bound/invariant field-word domain; locality and all-word
  convergence; the eight-channel/E8 source selection. No T1–T8 item closes.

The next source-side proof must provide a declared operator `B_N^pm` on
the **full** finite source Hilbert spaces, both adjoints, and its source
time evolution. For the existing embeddings `i_N` of each finite-current
input, the concrete target is

\[
 \|B_N^\pm(F)i_N\psi-i_N V^\pm(F)\psi\|\longrightarrow0
 \quad(\psi\in D),
\]

where on the right the embedding of an infinite-output vector must itself
be defined by energy truncation with a proved uniform tail estimate.
Equivalently one may compare all fixed output energy truncations and then
prove both tails uniformly small. **The latter tail step cannot be dropped.**
The source normal-ordering constant, phase, intersector action, and time
scale must be fixed before measuring convergence. Check at least both charge
vacua and a nonvacuum current descendant for each adjoint. A nonzero
`n=m` tower is a mandatory stress test: a momentum-only filter would falsely
pass a momentum cutoff while missing the energy obstruction proved here.

Defining `B_N` backwards by conjugating the desired limiting V through
the embeddings would be a realization of a target model, not a microscopic
derivation. Likewise, a neutral two-point determinant comparison alone
does not identify the intersector operator or its nonvacuum action.

## 8. Reproduction and evidence boundary

Run `checker.py --output validation.json`, then
`python -m unittest -v test_checker` and
`python -OO -m unittest -v test_checker` in this directory with the existing
TFPT discovery environment. The checker pins upstream source artifacts;
it leaves their code, records, finite-N integer-charge guards, and published
consolidation manifest unchanged.

Exact checks cover independent CAR and oscillator coefficients, both
source energy spectra, protected current commutators, noncyclic carry,
normal ordering and adjoints, and rational regulator coefficients.
Gaussian and partial-sum values are floating diagnostics. The infinite
limit and sharp threshold are analytic arguments above, not consequences
of passing a finite test suite. Independent mathematical review is pending.
