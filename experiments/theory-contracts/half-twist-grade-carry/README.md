# A sourced half twist with charge carry, and a one-edge low-mode bound

2026-09-08. **NON-RH. Exact target-lattice and microscopic one-particle
results; no complete charged-field construction, no T1–T8 closure.**

The useful advance is not another E8 root count. The existing order-four
glue vector can be expressed as the half twist of the existing eight
complex channels. Its order-four *charge grading* is compatible with an
order-two change of boundary condition, provided a genuine integer-charge
carry is retained. On the actual QWZ source, the half string works across
the full width. Restricting it to one edge produces bulk-interface terms,
but their action on explicit low-momentum edge quasimodes has an exact
vanishing bound. A separate filled-vacuum check shows why this is still
short of the required many-body field.

The abstract D8-plus-spinor route to E8, and the D5+A3 glue census, already
exist in `v469` and `v983`. They are **not new results of this experiment**.
The new work connects the particular sourced lambda, its charge carry,
the actual `v988`/`v1033` matrices, and the remaining microscopic obstruction.

## 1. The lambda target needs a half twist, not a common quarter twist

Use the actual `v983` coordinates

\[
\lambda=((1/2)^5;3/4,-1/4,-1/4,-1/4),\qquad L_0=D_5\oplus A_3.
\]

On the sum-zero hyperplane in the last four coordinates, set

\[
T=\tfrac12\begin{pmatrix}
1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1
\end{pmatrix}.
\]

Then `TT^t=I3`, `T^tT=I4-11^t/4`, and T maps the twelve A3 roots
bijectively to the twelve D3 roots. In particular,

\[
T(3/4,-1/4,-1/4,-1/4)^t=(1/2,1/2,1/2)^t,
\qquad \lambda\longmapsto s=(1/2)^8.
\]

Thus the target has eight, not nine, independent bosons; the original
four A3 coordinates obey one constraint. Its conformal weight is
`h=|s|²/2=1`. The old common quarter twist still has weight `1/4`.
It cannot be converted to weight one by a norm-preserving coordinate
change: **the operator ansatz must change from quarter to half twist**.

The standard lattice vertex construction has a group-algebra charge
factor, oscillator factors, and weight `|alpha|²/2`; see
[Dong–Nagatomo, sections 2.1–2.2](https://arxiv.org/html/math/9808088#S2.SS2).
That theorem describes the target VOA, not the finite QWZ realization.
The isometry above is an explicit coordinate convention. It does not
derive an intertwiner for the microscopic family action, Gaussian deck,
or time-like clock.

## 2. Four glue grades do not require four distinct boundary phases

In the eight-dimensional coordinates,

\[
L_0=D_5\oplus D_3\subset D_8\subset
L=D_8\cup(D_8+s),\qquad
D_n=\{a\in\mathbb Z^n:\textstyle\sum a_i\text{ even}\}.
\]

Define on **all charges**, not just roots,

\[
k(q)=2\sum_{i=1}^{5}q_i\pmod4,\qquad C|q\rangle=i^{k(q)}|q\rangle.
\]

The kernel is L0; `k(s)=1`. Hence `L/L0=Z4`, whereas `L/D8=Z2`.
Grades 0 and 2 have integer charges; grades 1 and 3 have half-integer
charges. Writing `q=n+b*s`, with `n in D8` and `b=0,1`, gives

\[
C|q\rangle=i^b(-1)^{\sum_{i=1}^{5}n_i}|q\rangle,
\qquad C^2|q\rangle=(-1)^b|q\rangle.
\]

Thus a two-sector NS/R description retains a four-grade spin lift.
For bare fermion charges the underlying rotation changes the sign of
the first five complex fermions, not all eight by a common factor i.
This internal C is **not identified** with the source holonomy register,
the Gaussian J, or the time-like deck merely because all can involve Z4.

The 128 half-integer norm-two charges have an even number of minus signs.
They split into 64+64 according to first-block parity. The complete
root census is `[52,64,60,64]`; adding the eight Cartan generators gives
`[60,64,60,64]`, totaling 248. The even-NS subalgebra alone gives D8;
the Ramond spinor extension is an additional algebraic step, not a
consequence of merely projecting onto even parity. The even-CAR sector
framework is described by
[Böckenhauer, *An Algebraic Formulation of Level One Wess–Zumino–Witten Models*](https://arxiv.org/abs/hep-th/9507047).

## 3. The missing carry is a real charge translation

Use the previous experiment's full zero-mode representation on `ell²(L)`
with its pinned integral-basis cocycle, not just a four-state register:

\[
U_\alpha|q\rangle=\varepsilon(\alpha,q)|q+\alpha\rangle.
\]

For the inherited convention,

\[
U_s^2=-U_{2s},\qquad U_s^4=U_{4s}\ne I,
\qquad CU_sC^{-1}=iU_s.
\]

The minus sign in the square is convention-dependent; the nonzero
integer-charge carry is not removed by scalar rephasing. If
`q=r+k*s`, `r in L0`, `0<=k<4`, the fourth step sends
`(r,3)` to `(r+4s,0)`. On the ray `0,s,2s,3s,4s`, zero-mode energies
are `0,1,4,9,16`. These are **not** the minimal weights of their four
cosets: neutral translations lower the representative energy.

A plain boundary flip `n+b*s -> n+(1-b)*s` changes the grade by +1
on its first leg and -1 on its return. The correct second leg must also
shift `n -> n+(1,...,1)`. Consequently squaring the old flux-register
shift and matter string supplies the boundary change but does not yet
supply the charged field. The full integer-charge energy identity is

\[
[H_0,U_s]=U_s(P_s+1).
\]

This is checked in the inherited lattice basis, including charges of
magnitude `10^12`. No finite cutoff or cyclic identification is used.
The zero-mode translations are not the full weight-one vertex field;
oscillator factors remain necessary for its locality and energy bounds.

## 4. The half string on the actual finite QWZ cylinder

Nothing is changed in `v988` or `v1033`. Their forward seam hopping is
`i^r TX`, with

\[
T_x=-i\sigma_x/2-\sigma_z/2,\qquad
T_y=\tfrac12\begin{pmatrix}-1&-1\\1&1\end{pmatrix}.
\]

Let D be -1 on the arc `0<=x<=a` and +1 elsewhere, initially on
**every** transverse row. This is exactly the square of the source's
quarter-phase string. For the sourced matrices,

\[
R=H_{r+2}D-DH_r
\]

has support only on the other arc endpoint, the bonds `a -> a+1`.
Per copy, it has exact norm 2 and rank `2 Ny`, independently of N.
It still acts on both edges of the cylinder.

Restrict D to the top w rows. The exact residual decomposes into:

1. the desired far-endpoint term on those w rows;
2. a vertical-interface term V at each of the `a+1` arc sites;
3. an uncancelled seam term S on the remaining `Ny-w` rows.

Each vertical bond has block `2 TY` and reverse block `-2 TY*`.
Thus `rank(V)=2(a+1)`, `||V||=2`, and `||V||HS²=8(a+1)`.
A purely scalar on-site phase cannot exactly avoid this term: away from
endpoints, `(d_below-d_above) TY=0` forces equality of the two phases
because TY is nonzero. Connected transverse hopping forces the full
width to twist. This is a restriction on this **specific ansatz**, not
a no-go theorem for dressed charged fields or their scaling limits.

All 48 combinations of three circumferences, four source sectors and
four widths are checked using actual source matrices. Entries are
dyadic complex numbers and compared exactly; ranks and operator norms
follow separately from exact symbolic rank-one hopping blocks.

## 5. Constructive escape: the unwanted defect vanishes on low edge modes

Exact finite-support locality was too strong a test for a scaling-limit
candidate. This can be shown constructively, without assuming an exact
finite-cylinder edge eigenvector.

For the source convention `exp(+ipx)`, use
`p=(2*pi*n-r*pi/2)/N`; the sign agrees with the actual forward seam.
Let `rho=1-cos(p)` and

\[
v_y(p)=\frac{\rho^{N_y-1-y}}{\sqrt{\sum_{j=0}^{N_y-1}\rho^{2j}}}
\frac{(1,1)^t}{\sqrt2}.
\]

The strip symbol is `h(p)=-sin(p) sigma_x+rho sigma_z` on each row,
with the exact TY transverse bonds. Direct polynomial multiplication
gives

\[
\|(h(p)+\sin p)v(p)\|
=\frac{\rho^{N_y}}{\sqrt{\sum_j\rho^{2j}}}\le\rho^{N_y}.
\]

The sole residual is at the opposite boundary. This is an explicit
**quasimode**, not an exact eigenvector at finite width.

The exact vertical defect on v is of order `rho^w`, not `rho^(w-1)`,
because

\[
T_y\chi_+=-\chi_-,\qquad T_y^\dagger\chi_+=0.
\]

For the isometric Fourier embedding Q of any set of these profiles
with `rho(p)<=rmax<1`, Fourier orthogonality and restriction to the arc
(a contraction) give

\[
\|VQ\|\le2r_{\max}^w,\qquad
\|SQ\|\le2r_{\max}^w,\qquad
\|(V+S)Q\|\le4r_{\max}^w.
\]

Here the seam bound uses its exact norm 2 and the normalized tail
estimate `||P_below-strip Q||<=rmax^w`. The latter follows from

\[
\rho^{2w}\sum_{j=0}^{N_y-1}\rho^{2j}
-\sum_{j=w}^{N_y-1}\rho^{2j}
=\sum_{j=N_y}^{N_y+w-1}\rho^{2j}\ge0.
\]

Similarly `||(D_strip-D_full)Q||<=2rmax^w`. On each fixed Fourier
core `|p|<=K/N`, use `1-cos(p)<=p²/2`. In the energy normalization
`N/(2*pi)`,

\[
\frac{N}{2\pi}\|(V+S)Q\|
\le\frac{2^{1-w}K^{2w}}{\pi}\,N^{1-2w}.
\]

**For w=2 this is O(N^-3).** At fixed `Ny=8`, the opposite-boundary
quasimode error after the same rescaling is O(N^-15).
These bounds are uniform in the arc length and extend to any fixed
finite one-particle Fourier core. The reverse-sector one-particle
calculation has the same bounds; it is not a many-body adjoint theorem.
The exact numeric caps use K=11, which includes `n=-1,0,1` in every
source sector, rather than a momentum window containing only a zero mode.

## 6. Why this still does not construct the charged field

Low one-particle momenta do not exhaust the filled Fermi sea. The raw
string can excite ultraviolet and massive occupied modes. A separate
finite-Fock diagnostic uses the nondegenerate ground state of sector
1 and measures its transformed energy relative to sector 3. For one
source copy and `Ny=8`, with an arc of length N/2:

| N | Top-two-row string: unscaled vacuum excess | Whole-width string |
|---:|---:|---:|
| 8 | 13.808556 | 9.287762 |
| 16 | 18.326264 | 9.284668 |
| 32 | 27.367091 | 9.283900 |

These are floating finite-size measurements, **not an asymptotic lower
bound or proof that a renormalized smeared field is impossible**. They
do prevent promoting the low-mode estimate to vacuum control. Even the
whole-width sharp string is not automatically a bounded-energy point
field after conformal rescaling. Smearing, vacuum normalization and
the oscillator tails must be controlled together.

The next concrete construction is a **bulk-corrected half string from
the same QWZ covariance**, with the sourced charge carry and cocycle.
A mere edge projection or separately appended charge register does not
meet that condition. Its acceptance test must include a nonzero smeared
field and its adjoint on the many-body finite-energy core, with uniform
energy bounds and a support-preserving local-algebra identification.

Only then can this seam result feed the common-parent 3+1D, chirality,
gauge, gravity and dynamics contracts. No T1–T8 status is changed here.

## Reproduction and provenance

Run from the repository root:

```text
python3 experiments/theory-contracts/half-twist-grade-carry/checker.py
python3 experiments/theory-contracts/half-twist-grade-carry/test_checker.py
python3 -OO experiments/theory-contracts/half-twist-grade-carry/test_checker.py
python3 experiments/theory-contracts/half-twist-grade-carry/vacuum_diagnostic.py
```

`validation.json` is the deterministic exact certificate, including the
checker hash and seven direct source pins; the preceding charged-cocycle
checker validates its own transitive sources. `vacuum_diagnostic.json`
is separately labeled floating evidence. Tests include wrong source,
wrong twist, wrong sign, no-carry and no-promotion controls, independent
exact small-matrix ranks, polynomial profiles at several widths, and
full-source low-mode checks. All guards survive Python optimization.
The first checker run exposed a structural-versus-algebraic symbolic
equality issue; an exact expanded-zero check and regression cover it.
`systematic-debugging` was used to isolate that implementation issue;
no tolerance or scientific hypothesis was weakened to pass the check.
