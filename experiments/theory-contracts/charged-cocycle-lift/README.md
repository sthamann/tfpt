# Charged cocycle lift: the missing dual bits and deck-paired Clifford factors

2026-09-08. **NON-RH. An exact finite charge-sign reconstruction plus the full
lattice zero-mode representation. Not a microscopic seam identification, a
3+1D fermion construction, a chiral Standard Model or full TOE.**

## Result

The preceding compiler-to-Clifford construction is mathematically valid, but
its four-bit Gaussian quotient is not a quotient of the charged lattice sign
algebra. This note locates that failure using actual E8 roots, repairs the
finite charge-sign loss with the minimal additive refinement, and classifies
all compatible Clifford lifts rather than choosing one by hand.

The refinement is `L/2L`, with eight binary coordinates. Its irreducible sign
representation is sixteen-dimensional. The old compiler is its sixteen-point
configuration quotient, not its complete charge phase space. Exactly **64**
linear sections preserve the old compiler quadratic form; exactly **four**
also respect the actual family cycle. The deck exchanges each such section
with its charged orthogonal complement. Thus there are **two unordered
deck-paired splittings**, not a unique physical spin factor.

Each factor is the previous quaternionic Clifford algebra. Together they give

\[
M_2(\mathbb H)\otimes_{\mathbb R}M_2(\mathbb H)
\cong M_{16}(\mathbb R).
\]

Both factors are generated inside the E8 charge-sign algebra: the second
factor is not an arbitrary spectator tensor inserted into the model. Their
joint commutant in this finite representation is scalar. This finite result
does **not** prove prime completion of the microscopic local field net.

## 1. The charged commutator does not descend to the Gaussian quotient

Let L be the even unimodular E8 lattice in the exact standard doubled basis
read from `v774`. Actual vectors are the displayed integer vectors divided
by two, so their physical scalar product is integer dot product divided by
four. Let J rotate each coordinate pair by `(-x2,x1)` and let sigma cycle
the first three pairs. These are the actual source isometries, not new ones.

For the usual lattice central-extension factors, use

\[
e_\alpha e_\beta=\epsilon(\alpha,\beta)e_{\alpha+\beta},
\qquad
\frac{\epsilon(\alpha,\beta)}{\epsilon(\beta,\alpha)}
=(-1)^{\langle\alpha,\beta\rangle}.
\]

This is the standard even-lattice VOA construction, stated explicitly in
[Dong and Nagatomo, section 2.1](https://arxiv.org/html/math/9808088#S2.SS1).
The TFPT charged-field manuscript uses a normalized lattice cocycle and a
normal-ordered exponential. Its microscopic realization is still an open
identification, so the theorem here concerns that **target charge algebra**.
The commutator sign of its cocycle factors is not, by itself, the exchange
statistics of the complete vertex field: oscillator and coordinate factors
also enter locality. In particular, the sourced lambda still has weight one.

Take physical roots

\[
y=(1,0,1,0,0,0,0,0),\quad
y'=-Jy=(0,-1,0,-1,0,0,0,0),\quad
z=(1,0,0,0,1,0,0,0).
\]

All have norm squared two. Since `y-y'=(1+J)y`, y and y' have the same
nonzero label in `V=L/(1+J)L`; in the source family/anchor coordinates it
is `(0,1,1,0)`. But `y.z=1` whereas `y'.z=0`. Their cocycle factors
therefore have opposite commutator signs against z. A representation
depending only on that compiler label cannot reproduce both.

No scalar rephasing repairs this: multiplying epsilon by a coboundary
`f(alpha) f(beta)/f(alpha+beta)` leaves its commutator unchanged. This is
not a phase-convention mismatch, and it does not contradict `v774` or the
previous finite Clifford proof: they use a different bilinear form.

## 2. The minimal sign-preserving refinement is already in the lattice

Put

\[
W=L/2L,\quad \beta(x,y)=\langle x,y\rangle\pmod2,\quad
Q(x)=\langle x,x\rangle/2\pmod2,
\]
\[
K=(1+J)L/2L,\qquad N=1+J:W\longrightarrow W.
\]

Unimodularity makes beta nondegenerate on W. If an additive quotient
`L/R` retains every commutator, then `<R,L>` is even, hence `R subset 2L`.
Thus `L/2L` is the smallest such additive quotient; this is not a claim
that a finite quotient retains all integer charges or complete fields.

On W, `N^2=0`, and `im N=ker N=K` has dimension four. Also
`<(1+J)a,(1+J)b>=2<a,b>` and `Q((1+J)a)=<a,a>=0 mod 2`.
Consequently K is a maximal totally singular subspace. The exact sequence is

\[
0\longrightarrow K\longrightarrow W\overset{\pi}{\longrightarrow}V
\longrightarrow0.
\]

The existing compiler pairing is recovered by

\[
\bar h(\pi x,\pi y)=\beta(x,Ny)
=\langle x,y\rangle+\langle x,Jy\rangle\pmod2.
\]

All 65,536 pairs are checked against the source's actual bit labels.
The missing variables are the four dual coordinates paired with the
configuration quotient V. The full Q has 136 zeros and Arf zero; the old
selected compiler form q has six zeros and Arf one. They are not the same
quadratic form on differently named coordinates.

## 3. Complete lift classification and the deck/complement identity

Seek linear sections `s:V -> W` satisfying

\[
\pi s=1,\qquad Q(sv)=q(v).
\]

Polarization then gives `beta(sv,sw)=hbar(v,w)`. Starting with any section,
a variation is a map `V -> K`, with sixteen binary coefficients. The four
basis-square equations and six cross-pairing equations are affine linear.
Exact elimination gives rank ten, hence **64** sections. Requiring
`s sigma = sigma s` leaves exactly **four**. The count is complete for
this declared class of linear sections, not for arbitrary physical models.

For every such section, not merely the sigma-compatible four,

\[
\beta(sv,Jsw)=\beta(sv,sw)+\beta(sv,Nsw)
=\bar h(v,w)+\bar h(v,w)=0.
\]

Therefore, with `S=s(V)`,

\[
JS=S^\perp,\qquad W=S\perp JS.
\]

J preserves Q, so both four-dimensional factors have Arf one. They carry
the old real algebra `M2(H)` and are exact mutual commutants. The whole
algebra is `M16(R)`. On the four sigma-compatible sections the deck
permutation is `(0 3)(1 2)` in the recorded order.

There is **no J-equivariant section** if the quotient's trivial J action
is used: `Js(v)=s(v)` would imply `s(v) in ker(1+J)=K`, contradicting
`pi s(v)=v` for nonzero v. Thus interpreting the actual deck as a central
scalar on one isolated Clifford factor is incompatible with this lift.
This compares two different representations; it does not refute the
central scalar deck in the older Gaussian complex-coordinate representation.

## 4. Actual matrices and coherent symmetry phases

Choose a hyperbolic basis `(k_i,d_i)` with k in K, both halves Q-zero and
`beta(k_i,d_j)=delta_ij`. This is a computational basis convention, not a
physical selector. For `w=sum u_i d_i+v_i k_i`, act on sixteen states t by

\[
\rho(w)|t\rangle=(-1)^{\phi(w)+v\cdot t}|t+u\rangle.
\]

The explicit phase phi converts the canonical X/Z cocycle into the
ordered lattice cocycle

\[
c(x,y)=\sum_i(G_{ii}/2)x_i y_i+\sum_{i>j}G_{ij}x_i y_j\pmod2
\]

in the inherited integral E8 basis. Hence
`rho(x) rho(y)=(-1)^c(x,y) rho(x+y)`. All **65,536 products, every one
of their sixteen columns**, are verified using signed permutations. The
256 matrices are trace orthogonal, span `M16(R)`, and have scalar joint
commutant. A nonzero complex representation of `M16(C)` has dimension
at least sixteen, proving minimality in the declared sign-algebra class.

The section generators `rho(s(e_i))` square to minus one and anticommute,
so they reproduce the previous Clifford frame without postulating new
generators. This is checked for all four sigma-compatible sections. The
embedded Weyl projectors have ranks eight and eight: opposite sectors
remain, with multiplicity. These are not sixteen established physical
matter states and no SM gauge-commuting spatial spin is established.

The isometry lifts also need phases. Independently chosen J and sigma
lifts initially disagree on 128 basis words when composed in opposite
orders. An explicit character correction makes them commute while
preserving the chosen J square. There are four corrections in this gauge;
the smallest bitmask is a deterministic recording convention only.
The corrected J has order four on the sign algebra, although J on W has
order two. Sigma has order three. Generator rephasings implement the
family cycle exactly at operator level. These phases are not claimed to
be the normalized microscopic seam implementers.

## 5. Restoring full charges without appending a spectator

The sign representation cannot replace the integer charge Hilbert space.
Use the source lattice itself and its finite-support core in `ell^2(L)`:

\[
U_\alpha|\mu\rangle=\epsilon(\alpha,\mu)|\mu+\alpha\rangle,
\quad P_h|\mu\rangle=\langle h,\mu\rangle|\mu\rangle,
\quad H_0|\mu\rangle=\tfrac12|\mu|^2|\mu\rangle.
\]

Here epsilon is the displayed bilinear sign convention lifted to all
integer basis coordinates. U is unitary; its adjoint is
`U_alpha^*=(-1)^Q(alpha) U_-alpha`, not always bare `U_-alpha`.
On the common finite-support core,

\[
[P_h,U_\alpha]=\langle h,\alpha\rangle U_\alpha,
\qquad
[H_0,U_\alpha]=U_\alpha(\langle\alpha,P\rangle+|\alpha|^2/2).
\]

These follow for arbitrary integer charges, with no cutoff. The checker
tests actual root shifts at zero, nonzero, negative and million-scale
charges; the tests additionally use both signs of trillion-scale charges.
The vacuum basis vector is cyclic under all lattice shifts. A bounded
operator commuting with the spectral projections of all P_h is diagonal
in the joint charge basis, and commuting also with all U_alpha makes
that diagonal constant. Thus their joint commutant is scalar on this
**zero-mode target representation**, not an asserted microscopic bulk.

No finite unitary replacement can preserve a nonzero charge Ward identity:
`U* P U-P=<h,alpha>I` has trace zero on the left but nonzero trace on the
right. Even the refined sign quotient aliases charges zero and `2 alpha`
for a root alpha, although their H0 energies are zero and four.

The full vertex field additionally contains oscillator exponentials and
the coordinate/charge factor; see [Dong and Nagatomo, section
2.2](https://arxiv.org/html/math/9808088#S2.SS2). Reconstructing these
standard zero modes is not a proof that the finite TFPT collar produces
them, that its charged fields converge with their adjoints, or that a
3+1D local fermion emerges. The lambda identified in `v983` still has
conformal weight one and is not turned into a spacetime fermion by a
Klein-factor anticommutator.

## Consequence for the solution programme

The preceding question, "can the compiler Clifford matrices be used as
the whole charged operator?", now has a precise negative answer and a
constructive replacement. Preserve the full lattice charge shifts and
their dual phase data; regard the Clifford algebra as a represented
factor, not as a quotient that erases the conjugate charges. Treat the
deck-paired factors together before attempting a physical spin assignment.

The next physical acceptance test is an actual support-preserving map
from the same microscopic collar observables to these charge/phase/field
operators, including the source's normalized lambda, its adjoint and
energy bounds. Test that map against the root-pair sign witness and the
charge Ward identity before extracting a kinetic symbol. Any proposed
spatial spin factor must then meet the previously established gauge
commutation test; its actual two-point pole and mirror sector must be
computed in the same selected parent. This does not select the state,
couplings, flavor mechanism or universal gravitational response.

No T1--T8 closure is claimed. No original source, ledger, paper or website
is modified. Existing scalar and compiler experiments remain intact.

## Reproduction

```sh
python3 checker.py --output validation.json
python3 -m unittest discover -s . -p test_checker.py -v
python3 -OO -m unittest discover -s . -p test_checker.py -v
```

Six source pins include the actual lattice source, charged target and
unchanged prior Clifford artifact. The JSON also pins this checker,
README and twenty-test suite. See `TEST_RESULTS.md` for measured runs.
Finite enumeration supports the explicit proofs above; it is not an
independent peer review or a proof-assistant formalization.
