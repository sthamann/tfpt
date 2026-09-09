# Same-source vacuum dressing: Gaussian filter and background compensation

2026-09-08. **NON-RH. A constructive unscaled finite-Fock vacuum-energy
result and an asymptotic one-particle half-string limit. Not a completed
charged field, microscopic charge carry, local-net identification or TOE.**

## Result and scope

The previous half-twist experiment found an unwanted energy cost growing
with the length of a raw top-edge strip. Here the operator is corrected
using only the unchanged QWZ Hamiltonian and its actual change of boundary
condition. No extra matter sector or fitted physical coupling is added.

For an explicit sequence of corrected finite CAR unitaries, the excess
energy of the transformed filled vacuum over the **target-sector** ground
energy tends to zero in **unscaled lattice units**. This statement is
proved below for all sufficiently large N; the small-N computations are
separate diagnostics. The one-particle action tends strongly to the
desired top-edge half string and to the identity on the bottom edge.

The distinction between unscaled and physical energy is essential:
the conformal energy includes a factor N/(2*pi). The proof does **not**
bound that rescaled energy. At the tested sizes, the one-particle action
errors are also still large, around 0.7. Neither small vacuum energy nor
a limiting one-particle map is a completed microscopic charged field.

The approach is related to time-filtered local-operator constructions in
[Hastings–Wen, *Quasi-adiabatic Continuation of Quantum States*](https://arxiv.org/abs/cond-mat/0503554).
Their gapped-continuation theorem is not invoked for this gapless collar.
All finite-dimensional estimates needed here are derived directly.

## 1. Construction from the actual source

Use `v988`/`v1033`, mass M=1, open width Ny=8, circumference N and forward
seam factor `i^r`. Let H=H_r and H'=H_(r+2). In the numerical comparison,
r=1 and r+2=3 avoid ambiguous zero-mode occupation. A is the on-site
projection onto the top two rows of `0<=x<N/2`; the old string is
`D=exp(i*pi*A)=I-2A`.

Define a Gaussian average using this same H:

\[
\Phi_\delta(B)=\int_{\mathbb R}\frac{\delta}{\sqrt{2\pi}}
 e^{-\delta^2t^2/2}e^{itH}Be^{-itH}\,dt.
\]

In an H eigenbasis it is exactly

\[
(\Phi_\delta B)_{ij}=B_{ij}
 e^{-(E_i-E_j)^2/(2\delta^2)}.
\]

This is a unital completely positive average of unitary conjugations.
It preserves self-adjointness and operator bounds. It is not a projection
onto a hand-selected edge band. In particular,
`Phi(B)^2 <= Phi(B^2)` for self-adjoint B.

The first attempt `exp(i*Phi(pi*A))` removes the extensive source-vacuum
cost but leaves an O(1) target-boundary cost. To address the actual target
Hamiltonian, define the source-fixed gauge ramp

\[
G(x)=e^{-i\pi x/N},\quad R(x)=\pi x/N,\quad
B=\pi A+R,\quad
U_N=G\exp(i\Phi_{\delta_N}(B)),\quad \delta_N=4N^{-3/4}.
\]

Before filtering, `G exp(iB)=D` exactly. Also `||B||<=2*pi`.
The ramp does **not** remove the change of holonomy: it redistributes
the specified H-to-H' background difference across the horizontal bonds.
Let `K=G* H' G`, where star denotes adjoint. The sourced Fourier symbol
gives the exact bound

\[
\|K-H\|=2\sin(\pi/(2N))\le\epsilon_N:=\pi/N.
\]

The width, coefficient 4 and exponent 3/4 are auxiliary regulators, not
derived physical constants. The argument works with other fixed positive
coefficients and exponents between 1/2 and 1, with adjusted estimates.

## 2. Finite-angle energy-transfer estimate

It is insufficient to filter only the first pair-creation term: higher
powers in the exponential can connect additional energies. The following
bound treats the full unitary.

For any real a, the scalar identity

\[
e^{a\omega-\omega^2/(2\delta^2)}
=e^{a^2\delta^2/2}
 e^{-(\omega-a\delta^2)^2/(2\delta^2)}
\]

rewrites `exp(aH) Phi(B) exp(-aH)` as a Gaussian unitary average with
an additional phase of modulus one. Consequently

\[
\|e^{aH}\Phi_\delta(B)e^{-aH}\|
\le L e^{a^2\delta^2/2},\qquad L=\|B\|\le2\pi.
\]

Expanding the full exponential and taking a=1/delta yields

\[
\|P_{[\Delta,\infty)}e^{i\Phi_\delta(B)}P_{(-\infty,0]}\|
\le e^{-\Delta/\delta+L\sqrt e}.
\]

The opposite-sign estimate follows by replacing H with -H. For d=16N
one-particle states, the **total particle-plus-hole number** outside
`[-Delta,Delta]` in the transformed filled vacuum is therefore at most

\[
d\,e^{4\pi\sqrt e-2\Delta/\delta}
\le d\,e^{22-2\Delta/\delta}.
\]

This is a finite-Fock statement through its exact one-body covariance,
not just a low-momentum one-particle estimate. It needs no uniform full
spectral gap. Any zero-energy filling can be absorbed in the low window.

## 3. Source density-of-states bound and vanishing unscaled energy

The transverse operator at momentum zero consists of seven independent
dimers with eigenvalues +/-1 and two zero modes. Call it K0. The full
strip matrix is `H(p)=K0-sin(p) SX+(1-cos(p)) SZ`, with the Pauli matrices
acting on every row. The transverse part anticommutes with SX, so
`H(p)^2 >= sin(p)^2 I`. For cos(p)<=0, the reverse triangle inequality
for `K0+(1-cos(p))SZ` strengthens this to `H(p)^2>=I`.

Thus an eigenvalue of absolute value below `a<=1/4` requires
`|p|<=arcsin(a)<=2a` near zero. There the perturbation of K0 has norm
`2|sin(p/2)|<=2a`, so only the two edge eigenvalues can enter the window.
Counting the shifted momentum grid gives

\[
d_{\rm low}(a)\le2Na+2,\qquad \|H\|\le3.
\]

The norm bound follows from `||K0||=1` and the remaining symbol norm
at most 2. These are properties of the actual source, not of an assumed
continuum edge theory.

Set

\[
\Delta_N=\delta_N(2\log N+22).
\]

For all N>=16384, Delta_N<=1/4. This follows from `log 2<7/10` at the
initial value and monotonicity of `N^(-3/4)(2 log N+22)` thereafter.
The preceding high-energy estimate is then at most `16/N^3`. Writing
P for a filled ground-state projector of H and
`C=exp(i Phi(B)) P exp(-i Phi(B))`, we obtain

\[
\operatorname{Tr}(C-P)^2\le m_N:=2N\Delta_N+2+16/N^3,
\]
\[
E_H(C)-E_0(H)\le b_N:=2N\Delta_N^2+2\Delta_N+48/N^3
\longrightarrow0.
\]

The first bound counts particles plus holes. The second weights low
states by Delta_N and the remaining states by `||H||<=3`.
Its leading bound is O(N^-1/2 log²N); it is deliberately loose.

## 4. The target-sector vacuum is controlled too

Let Q be a ground-state projector of K=G*H'G. With `epsilon=||K-H||`,
each H eigenvector of energy at least a has negative-K projection norm
at most epsilon/a: apply `(K-E_i)Q` to that eigenvector. The analogous
bound holds below -a. Summing over the H eigenbasis gives

\[
\|P-Q\|_{\rm HS}^2\le d_{\rm low}(a)+d\epsilon^2/a^2.
\]

The variational principle, together with the reverse ground-state
comparison, implies

\[
0\le E_K(P)-E_0(K)
\le\operatorname{Tr}((K-H)(P-Q))
\le\epsilon\sqrt d\,\|P-Q\|_{\rm HS}.
\]

Choose a=N^-1/2. For N>=16 this yields the explicit ramp bound

\[
g_N=\frac\pi N\sqrt{16N}
 \sqrt{2\sqrt N+2+16\pi^2}\longrightarrow0.
\]

Finally, the cross term for the already filtered state is bounded by
`epsilon*sqrt(d*m_N)`. Hence the full, background-compensated unitary
satisfies

\[
\boxed{E_{H'}(U_N\Omega_H)-E_0(H')
\le b_N+g_N+\frac\pi N\sqrt{16N m_N}\longrightarrow0.}
\]

Here `U_N Omega_H` means the second-quantized unitary acting on the filled
vacuum. All estimates concern the original lattice-energy normalization.
Multiplying this bound by N does **not** give a bounded physical-energy
estimate. The general ramp bound, O(N^-1/4), is much weaker than the
small-N numerical behavior; no fit is substituted for this proof.

## 5. What happens to locality and to the desired edge action?

### A longitudinal locality bound for the filtered arc component

For a site-supported operator B_arc=pi*A and distance R from its support,
weighted finite-range propagation gives

\[
\|P_{\rm outside}e^{itH}P_{\rm arc}\|
\le e^{-R+v|t|},\qquad v=4(e-1).
\]

Indeed, conjugating H by `exp(distance-to-arc)` changes each of at most
four norm-one hopping blocks per row and column by at most e-1. The
block Schur bound is v. Duhamel's formula against the original unitary
evolution then gives the displayed estimate.

Split the Gaussian integral at `|t|=R/(2v)`. With P_R projecting onto
the enlarged support, the difference between the filtered arc unitary
and `exp(i P_R Phi(B_arc) P_R)` is at most

\[
2\pi\left(e^{-R/2}
+2e^{-\delta^2R^2/(8v^2)}\right).
\]

For `R=N^(3/4) log N`, this is superpolynomially small while `R/N->0`.
On the full finite Fock space the error is at most another factor d:
the k-particle exterior power has error at most k times the one-particle
error. Thus the filtered **arc component** has a genuine longitudinal
quasi-local estimate, not merely an observed matrix decay.

This does **not** prove microscopic one-edge locality of the full
compensated operator. The ramp is global, and R eventually exceeds the
fixed transverse width Ny=8. Cancellation of the ramp in the limit and
low-energy decoupling of the opposite edge must not be promoted to an
identification of the full local CAR/net algebras.

### The one-particle limit is retained, not erased by energy pinching

Use the previous source-derived normalized top/bottom quasimodes and
embed each fixed set of Fourier modes. Their energies are O(1/N), and
their residuals are O(N^-16). For any bounded on-site B or B², Duhamel
gives an error O(N^-16/delta_N) when their evolution is replaced by the
quasimode phases. The Gaussian factor between fixed modes tends to one,
because `N*delta_N=4N^(1/4)->infinity`. The remaining matrix elements
converge by the ordinary Riemann sums to the multiplication operators

\[
b(x)=\pi\chi_I(x)P_{\rm top}+\pi x I,\qquad b(x)^2.
\]

This initially proves weak convergence on a dense Fourier core. The
Gaussian Schwarz inequality `Phi(B)^2<=Phi(B²)` upgrades it to strong
convergence: expand the squared norm of `(Phi(B)-b)f`, use Schwarz for
the first term, and approximate bf by finite Fourier sums for the cross
term. Uniform boundedness controls the approximation and rules out loss
of norm into the bulk. The same argument applies on both edges.
Uniformly bounded functional calculus then gives strong convergence of
the exponentials. Multiplying by G cancels the ramp:

\[
U_N\ longrightarrow\ (I-2\chi_I)\text{ on the top edge},\qquad
U_N\ longrightarrow\ I\text{ on the bottom edge}.
\]

This is an asymptotic theorem, not a claim of small error at N<=64.
A filter shrinking faster than 1/N would instead erase the relevant
off-diagonal low-mode matrix elements; that negative control is tested.

## 6. Finite measurements and an unavoidable Fock-space boundary

One source copy, top width two, half-circle arc, sectors 1->3:

| N | Raw target excess | Simple filter | Filter plus background compensation | Compensated times N/(2*pi) |
|---:|---:|---:|---:|---:|
| 8 | 13.808556 | 9.328772 | 2.830012 | 3.603284 |
| 16 | 18.326264 | 9.402571 | 1.457631 | 3.711826 |
| 32 | 27.367091 | 9.384872 | 0.749898 | 3.819198 |
| 64 | 45.450089 | 9.352306 | 0.387313 | 3.945138 |

All entries are finite floating diagnostics. They confirm the removal of
the large raw cost, but do not establish a limit of rescaled energy.
At N=64, the full action error on three top modes is still 0.71245 and
on three bottom modes 0.71244. The asymptotic preservation proof does
not make these finite operators an already accurate field realization.

There is a sharper reason not to claim a unitary Fock limit. In source
and target top-edge Fourier frames, the sharp limit has multiplier
`W(x)=exp(i*pi*x) D_I(x)`. Direct integration gives

\[
|W_m|^2=\frac1{\pi^2(m-1/2)^2}.
\]

One occupied/unoccupied block therefore has squared Hilbert–Schmidt norm

\[
\frac1{\pi^2}\sum_{k\ge1}\frac{k}{(k+1/2)^2}=\infty,
\]

since each summand is at least `4/(9*k)` before the pi² denominator.
This is the actual half-shifted intersector calculation, not an inference
from small-N vacuum energies. Under the standard fermionic implementability
criterion, the sharp map has no ordinary unitary implementer between these
Fock polarizations; see
[Lill, *Implementing Bogoliubov Transformations Beyond the Shale–Stinespring Condition*](https://doi.org/10.1007/s10955-025-03415-y).
This rules out promoting the unrenormalized finite unitaries to the final
unitary field. It does **not** rule out the intended renormalized, smeared
charged operator-valued distribution.

There is also a concrete opposite-edge issue. The common source holonomy
changes the bottom spin structure as well. Although the bottom limit is
the identity in position space, its source-to-target Fourier-frame
multiplier is `exp(i*pi*x)`, whose squared Fourier coefficients are the
**same** `1/(pi²*(m-1/2)²)`. Its crossed covariance block therefore also
fails the Hilbert–Schmidt test. Bottom identity on one-particle wavefunctions
does not mean bottom-vacuum invariance across the two backgrounds. This
candidate has not isolated the requested single-edge charged extension.

## 7. Remaining acceptance gate

The next construction must determine the vacuum normalization and the
intersector determinant phase for this **same corrected sequence**, and
prove a nonzero smeared field and its adjoint on the common finite-energy
core. It must also recover the preceding full lattice charge carry and
cocycle, not merely nonperiodicity of `exp(i Phi(B))`. These finite CAR
unitaries preserve total microscopic fermion number; their nontrivial
fourth power is not by itself the required `U_s^4=U_4s` charge identity.

A concrete next diagnostic is the neutral pair `U_N(x)* U_N(y)`, with
star denoting adjoint: its common ramp cancels exactly. The Slater
determinant of its compression to the occupied source space supplies
the corresponding vacuum two-point function without adding a new model.
Testing whether its bottom/bulk factors separate with a controlled phase
would address normalization and the opposite-edge problem together.
That factorization and its charged, not merely neutral, lift are not
established here.

Longitudinal quasi-locality of the arc component and strong low-edge
convergence do not replace the full support-preserving one-edge algebra
identification. No 3+1D, chirality, gravity, coupling or T1–T8 claim is
closed by this experiment.

## Reproduction

```text
python3 experiments/theory-contracts/gaussian-vacuum-filter/checker.py
python3 experiments/theory-contracts/gaussian-vacuum-filter/checker.py --diagnostics
python3 experiments/theory-contracts/gaussian-vacuum-filter/test_checker.py
python3 -OO experiments/theory-contracts/gaussian-vacuum-filter/test_checker.py
```

The deterministic `validation.json` records exact identities, theorem
formulas, source hashes and explicit boundaries. The proofs are above,
not a consequence of passing assertions. `diagnostics.json` separately
records floating measurements and floating evaluations of loose analytic
majorants. The previous half-twist artifacts and all original sources
are unchanged. No paper/website/ledger promotion or commit/push is made.
