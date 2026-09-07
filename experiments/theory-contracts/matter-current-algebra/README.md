# Round 9 — exact scalar source algebra and the onsite-potential classification

**Unpromoted theory contract.** Internal exact algebra, not empirical evidence,
a registered verification module, or a nonlinear-gravity/T1–T8 closure.
The checker imports the existing [full-3D scalar source](../free-scalar-3d/README.md)
for its independent finite-volume regression. No RH claim or external data.

## Fixed data

Use the canonical bracket `{F,G}=sum(F_phi G_pi-F_pi G_phi)` and the original
endpoint-averaged current on oriented positive-axis edges `x -> y=x+e_i`:

\[
 \rho_x={\pi_x^2+m^2\phi_x^2\over2}
 +{1\over4a^2}\sum_{y\sim x}(\phi_y-\phi_x)^2,
 \qquad j_{xy}=-{(\pi_x+\pi_y)(\phi_y-\phi_x)\over2a}.
\]

Set `H[N]=sum N_x rho_x` and `J[u]=sum_edges u_xy j_xy` for real c-number
smearings. These are matter generators, not complete gravitational constraints.

## Theorem 1 — the energy–energy bracket closes exactly

For arbitrary smearings, dimensions, periodic volumes and canonical data,

\[
 \boxed{\{H[N],H[M]\}=J[\beta],\qquad
 \beta_{xy}={M_xN_y-N_xM_y\over a}.}                 \tag{1}
\]

Proof. Collect each undirected gradient edge once:

\[
 H[N]={1\over2}\sum_xN_x(\pi_x^2+m^2\phi_x^2)
       +{1\over4a^2}\sum_{x\to y}(N_x+N_y)(\phi_y-\phi_x)^2.
\]

The onsite mass terms cancel in the bracket. The contribution of one edge is

\[
 {N_xM_y-M_xN_y\over2a^2}
 (\pi_x+\pi_y)(\phi_y-\phi_x)=\beta_{xy}j_{xy}.
\]

Sum over edges. This proves the universal identity without a finite-size
extrapolation. As a sign check, `N=1` gives `beta=-D^+M`, consistent with the
existing energy Ward equation.

## Theorem 2 — locally smeared currents require larger support

Define `A[u]` by

\[
 (A[u]\phi)_x={1\over2a}\sum_i\left[
 u_i(x)(\phi_{x+e_i}-\phi_x)
 +u_i(x-e_i)(\phi_x-\phi_{x-e_i})\right].
\]

Then `J[u]=-pi^T A[u]phi`; canonical differentiation yields

\[
 \boxed{\{J[u],J[v]\}=\pi^T[A[u],A[v]]\phi.}       \tag{2}
\]

Choose smearings along one axis and enough sites to avoid wraparound. Then

\[
 [A[u],A[v]]_{x,x+2e_i}
 ={u_i(x)v_i(x+e_i)-v_i(x)u_i(x+e_i)\over4a^2}.     \tag{3}
\]

This coefficient is generally nonzero. Every original `A[w]` has zero at
that matrix entry. No choice of c-number `w` therefore represents the bracket
as another original `J[w]`, even if `w` depends nonlocally on `u,v`.
Adding original `rho` generators does not help: their quadratic monomials are
`pi*pi` and `phi*phi`, not the missing distance-two `pi*phi` monomial.

The exclusion also covers coefficients depending on matter data continuously
at the zero-field configuration. Scale all matter data by `epsilon`, divide
the putative identity by `epsilon^2`, and take `epsilon -> 0`. All generators
and their bracket are quadratic, so continuity would give precisely the
impossible c-number linear combination above. Singular coefficients are not
excluded, but would not give a regular algebra near the matter vacuum.

More generally, let `E_j=A[u^(j)]` for the unit smearing on the single edge
`j -> j+1` of a straight row. The nested bracket
`C_r=[...[E_0,E_1],...,E_(r-1)]` has

\[
 (C_r)_{0,r}=(2a)^{-r}.                            \tag{4}
\]

For `r=1` this is the edge coefficient. Inductively the only contribution to
`(0,r+1)` is `(C_r)_(0,r)(E_r)_(r,r+1)`; the reversed product has zero row
`0`. Take a sufficiently long row at each step to avoid periodic aliasing.
Thus a volume-uniform, bounded-range space of matter bilinears containing all
the original locally smeared currents cannot be closed under all brackets.

This is not a no-go theorem for nonlinear lattice gravity. New gravitational
counterterms, different currents, additional generators and other regulators
are outside its hypotheses. It identifies the precise shortfall of the fixed
free source at order `g^2`.

At finite volume these quadratic identities also lift to Weyl-ordered
commutators on the common invariant Schwartz core:
`[W(F),W(G)]=i hbar W({F,G})`. The higher odd Moyal terms vanish for quadratic
symbols. No central correction removes the distance-two monomial. This is
not an operator-domain theorem for a nonlinear coupled Hamiltonian.

## Theorem 3 — all admissible fixed-current onsite potentials

Replace the onsite mass term by a `C^1` function `V(phi)`, leaving the current,
canonical kinetic term and nearest-neighbour gradient term unchanged. Require
a momentum Ward identity for arbitrary canonical data on periodic rows of
at least three sites. A necessary and sufficient condition is

\[
 \boxed{V(z)=A z^2/2+Bz+C.}                       \tag{5}
\]

Necessity. The total current is
`P=-sum pi_x(phi_(x+1)-phi_(x-1))/(2a)`. The kinetic and free gradient
contributions to `dot P` vanish. The onsite contribution is

\[
 \dot P\big|_V={1\over2a}\sum_x
 V'(\phi_x)(\phi_{x+1}-\phi_{x-1}).               \tag{6}
\]

Every periodic stress divergence sums to zero, whether local or nonlocal.
Write `f=V'` and choose row data `(x,y,z,z,...,z)`. Equation (6) must give

\[
 f(x)(y-z)+f(y)(z-x)+f(z)(x-y)=0.                 \tag{7}
\]

Setting `x=0,y=1` forces `f(z)=f(0)+(f(1)-f(0))z` for every real `z`.
Integration proves (5). This argument uses no polynomial cutoff. A collinear
configuration embeds the obstruction into the full cubic lattice as well.

Sufficiency. Keep the previously proved full-3D gradient/kinetic stress and
replace the onsite part of each diagonal component by `-V(phi_x)`. The only
potential residual on an edge is

\[
 {1\over a}\left[{V'(x)+V'(y)\over2}(y-x)
                  -(V(y)-V(x))\right],           \tag{8}
\]

which vanishes for (5). All transverse cancellations remain unchanged.
For `V=lambda phi^4/24`, (8) is
`lambda(x+y)(y-x)^3/(24a)` and sums to `-17 lambda/2` on the historical
four-site datum `(0,1,2,4)` at `a=1`. Thus that single negative example is
part of a complete fixed-current onsite-potential classification.

This does not exclude interacting theories with modified currents or
non-onsite interactions. Stability is separate: an onsite potential in (5)
is bounded below for `A>0`, or for `A=B=0`; the algebra also allows unstable
quadratics and linear potentials.

## Reproduction and evidence

```text
python experiments/theory-contracts/matter-current-algebra/current_algebra.py
COUNTS: 22/22 exact checks passed
```

Python 3.11+ and SymPy 1.14 suffice. The source under `free-scalar-3d` is a
required repository input. Costs are fixed-size symbolic algebra: one generic
edge, the actual 27-site periodic source, seven-site current matrices and an
auxiliary degree-six potential census. No random samples, floating arithmetic,
external measurements or fitted parameters are used. The universal statements
come from the displayed proofs, not the finite regressions.

One initial assertion compared expanded and factored SymPy expressions by
structural equality. The recorded exact difference was zero; the checker now
tests the expanded difference. No identity or threshold was weakened.

## Context and next constructive target

The general Leibniz-rule conflict has established treatments, such as
[Kato, Sakamoto and So](https://arxiv.org/abs/0810.2360). That reference supplies
context, not a substitute for (1)–(8); no literature novelty is claimed.
The next construction must cancel the actual matter brackets through
gravitational corrections while retaining a declared locality bound and
consistent Hamiltonian evolution. The companion
[constraint-dressing contract](../constraint-dressing/README.md) supplies
nonlocal classical stabilization with the matched first vertex, a finite
quadratic unitary constraint theorem, and a chosen positive reduced quantum
completion. These do not provide the missing local microscopic TFPT
interaction or a full unreduced Hamiltonian-domain theorem.
