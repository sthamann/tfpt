# Compiler-to-Clifford bridge: recovering structure omitted by the scalar prototype

Date: 2026-09-08. **NON-RH. Exact finite algebra and a formal kinetic-symbol
bridge; not a selected physical bulk, a net-chiral Standard Model or TOE closure.**

## Outcome and correction of scope

The latest `parent-selection-audit` correctly ruled out free Weyl nodes in the
*particular scalar cubic U(1) parent*. It did not exhaust TFPT's foundational
structure. The existing compiler has a selected quadratic form, an order-three
family action and an anchor. These supply a concrete algebraic Clifford frame.
Moreover, `v1027.free_overlap` already contains a stronger **matrix-valued,
vectorlike** free example. It would be wrong to describe TFPT as having only the
scalar hopping structure, or to count that existing example as a new discovery.

This experiment connects these existing ingredients: the sigma-fixed and
sigma-moving planes of the inherited binary quadratic space give commuting
split/quaternion algebras; their products give a Lorentz Clifford frame, whose
Hamiltonian matrices supply precisely the linear symbol needed by the existing
free overlap/signed-wall route. No continuous fitted coefficient enters this
finite construction. The identification with physical spin/transport remains
unproved; discreteness and absence of fitted coefficients do not select a theory.

## Foundational inventory and type discipline

| Existing layer | What is actually available | What must not be inferred |
| --- | --- | --- |
| P1/P2, anchor `(1,1,2)`, E8 closure | Conditional arithmetic/geometric structure and carrier constraints | An unconditional derivation of the seam-to-carrier physical interface |
| `v774`: sigma, Arf form, even five-slot code | Exact binary symplectic/quadratic data | Each Gaussian root class is one physical matter state |
| `v775`: root-class test | The proposed pure code-to-matter assignment fails | That the present algebra repairs that failed assignment |
| `v783`: two-qubit Clifford | Exact finite complex four-dimensional Pauli/Clifford geometry | Physical four-dimensional spacetime or a selected derivative |
| Spin(10) half-spinor `Lambda^even C^5` | Sixteen internal gauge labels per generation | A spacetime two-component Weyl spinor |
| `v252`: finite triple | Internal particle/antiparticle space and finite Yukawa operator | A spacetime differential Dirac operator or derived Yukawa couplings |
| `v975`: dimension selector | Dimension four under stated physical selection axioms | Those axioms or a 4D continuum derived from the compiler |
| `v1027`: signed wall and overlap | Matrix-valued free vectorlike construction, conditional on its inputs | Net chirality, a quantum gauge theory, a selected lattice/ground state |
| Recent scalar U(1) bulk tests | Genuine scoped operator/spectral results | Evidence that this scalar specialization is the physical TFPT parent |

The four-dimensional complex **representation space** below, sixteen-dimensional
real **algebra**, sixteen internal half-spinor labels, three family copies,
particle/antiparticle doubling and Lorentz spin components are different objects.
The same numeral is not an identification map. In particular, the family's
order-three action acquiring a spatial-looking algebraic action is not a theorem
that physical family permutations rotate physical space.

## 1. The inherited binary space already singles out two planes

Use the exact definitions imported read-only from `v774`:

\[
V=\mathbb F_2^4,\quad v=(f_1,f_2,f_3,a),\qquad
b(v,w)=v^T(J-I)w,
\]
\[
\sigma(v)=(f_3,f_1,f_2,a),\quad A=(0,0,0,1),\quad F=(1,1,1,0),
\]
\[
\iota(v)=(f_1,f_2,f_3,a,f_1+f_2+f_3+a),\qquad
q(v)=\frac{\operatorname{wt}\iota(v)}2\pmod2.
\]

The existing frozen selector is sigma-invariance, `q(A)=1`, `q(F)=0`.
It selects one of the sixteen quadratic refinements of `b`, with six zeros
and Arf invariant one. The checker repeats this finite selection.

Because `3=1` in characteristic two, the canonical projectors are

\[
P_0=1+\sigma+\sigma^2,\qquad P_1=\sigma+\sigma^2.
\]

Their images give a **b-orthogonal nondegenerate splitting**

\[
V=V_0\perp V_1,\qquad
V_0=\langle A,F\rangle,\quad
V_1=\{(f_1,f_2,f_3,0):f_1+f_2+f_3=0\}.
\]

On `V0`, the q-values on `(A,F,A+F)` are `(1,0,0)`: Arf zero.
On `V1`, all three nonzero vectors have q-value one: Arf one.
This splitting is intrinsic to the inherited sigma. The signs and ordering of
a basis inside its planes are not claimed to be uniquely physically selected.

## 2. A split plane times a quaternion plane

Choose the explicit ordered cocycle representative

\[
E_vE_w=(-1)^{c(v,w)}E_{v+w},\qquad
c(v,w)=\sum_i v_iw_i+\sum_{i>j}v_iw_j\pmod2.
\]

It obeys `c(v,v)=q(v)` and `c(v,w)+c(w,v)=b(v,w)`.
All 4,096 associativity cells and 256 commutator cells are checked. Choosing
this representative does **not** identify it with TFPT's full charged seam
cocycle. The quadratic form determines a graded algebra isomorphism class,
not an automatic physical operator assignment.

Put `gi=E_ei`, so `gi^2=-1` and distinct generators anticommute. Define

\[
a=g_4,\quad f=g_1g_2g_3,\qquad
u_1=g_1g_2,\quad u_2=g_2g_3,\quad u_3=g_3g_1.
\]

Then `a^2=-1`, `f^2=1`, `af=-fa`. Thus the fixed-plane algebra is `M2(R)`.
The moving-plane units satisfy `ui^2=-1` and `u1 u2=u3` cyclically, so they
generate the quaternions `H`. Both factors commute. Their sixteen product
basis elements are independent, giving

\[
\mathcal A_q\cong M_2(\mathbb R)\otimes\mathbb H\cong M_2(\mathbb H).
\]

The sign `u3=g3 g1=-g1 g3` is essential. Simply permuting binary labels
without lifting their signs gives a wrong algebra automorphism. The signed
sigma lift fixes `a,f` and cycles the three quaternion units.

For direct verification the checker uses

\[
(g_1,g_2,g_3,g_4)=
(iX\otimes1,\ iZ\otimes1,\ iY\otimes X,\ iY\otimes Z).
\]

These matrices reproduce all 256 products and span `M4(C)` after complexification.
An independent real sixteen-dimensional left-regular representation checks the
same quaternion and Clifford identities without these Pauli matrices.

This uses standard mathematics, not a newly invented Clifford classification.
For the quadratic-form/twisted-algebra framework see Elduque and
Rodrigo-Escudero, [Clifford algebras as twisted group algebras and the Arf
invariant](https://arxiv.org/html/1801.07002). The repository-specific contribution
is the application of that framework to its existing sigma/anchor selector and
the explicit connection to its kinetic-symbol route.

## 3. A Lorentz frame and two formal Weyl sectors

With `B=af`, define

\[
\Gamma^0=f,\qquad \Gamma^j=Bu_j\quad(j=1,2,3).
\]

The exact identities are

\[
\{\Gamma^\mu,\Gamma^\nu\}=2\operatorname{diag}(1,-1,-1,-1)^{\mu\nu},
\qquad\Gamma^0\Gamma^1\Gamma^2\Gamma^3=a.
\]

Time gamma is Hermitian and spatial gammas are anti-Hermitian. Set

\[
\alpha_j=\Gamma^0\Gamma^j=-au_j,\qquad
\chi=i\Gamma^0\Gamma^1\Gamma^2\Gamma^3=ia.
\]

Then `alpha_j` and `chi` are Hermitian, `chi^2=1`, `[chi,alpha_j]=0` and
`-i alpha1 alpha2 alpha3=chi`. Both projectors `(1+/-chi)/2` have rank two,
with opposite Weyl orientations. For **formal independent variables** p,

\[
K(p)=\sum_j\alpha_jp_j,\quad K(p)^2=|p|^2I_4,
\]
\[
D(p)=\Gamma^0p_0+\sum_j\Gamma^jp_j,\quad
D(p)^2=(p_0^2-|p|^2)I_4,\quad
\det D(p)=(p_0^2-|p|^2)^2.
\]

This solves the finite algebraic subproblem of producing a full-rank
three-direction Clifford/Weyl **target symbol** from the existing compiler
data. It does not produce translation generators or a physical light cone.
Opposite sectors coexist; no mirror-removal mechanism is proved. The signed
wall's already established low branch
`f_-(x)=x+3x^2/16-x^3/64+O(x^4)` preserves this symbol's linear term under
functional calculus, if this K is supplied as its input.

## 4. Recovering the stronger existing free overlap example

Set `beta=Gamma0` and `gamma_j=-i Gammaj`. These are Hermitian Euclidean
Clifford matrices. In the **existing** `v1027` ansatz use

\[
A(k)=\beta\left[1+\frac{W(k)+i\sum_j\gamma_j\sin k_j}{r(k)}\right],
\quad W=\sum_j(1-\cos k_j)-1,\quad
r^2=\sum_j\sin^2k_j+W^2.
\]

Its linear term at the origin is exactly `sum alpha_j k_j`. For
`xj=1-cos(kj)` in `[0,2]`, the exact identity
`r^2=1+2 sum_{i<j} xi xj` gives `1<=r<=5`. Also
`A^2=2(1+W/r) I`, so zeros require all sines zero and negative W; only
the origin qualifies. All eight corners and 27 non-corner rational
unit-circle points are checked exactly. This is a different, matrix-valued
input from the scalar cubic parent; that parent and its audit stay unchanged.

The prescribed lattice, sin/cos transport and regulator mass one are still
inputs. The construction is free and vectorlike; a finite set of matrix
checks is not a proof of a quantum gauge continuum or a physical vacuum.

## 5. Three controls that prohibit premature physical promotion

**Signature ambiguity.** The same real algebra and same sigma also admit
`E0=f`, `Ej=a uj`, with `{Emu,Enu}=2 delta_munu`. Thus both `Cl(1,3)` and
`Cl(4,0)` appear here (p positive, q negative squares). The finite data alone
do not select a physical real tangent subspace, signature, time orientation
or reflection-positive Euclidean theory. Declaring the anchor to be the
physical oriented four-volume would be an additional interpretation.

**Deck is not chirality.** `a=E_A` anticommutes with f; the central Gaussian
deck scalar `i I` commutes with everything. They are not the same operator.
Likewise no equality between this matrix chi and a pre-existing NS/R state
grading is inferred from their names or orders.

**Internal gauge space is not spatial spin.** The five-slot even-code charge
census agrees exactly with the inherited SM weights: `6Y` values
`(1,-4,2,-3,6,0)` have multiplicities `(6,3,3,2,1,1)`. Three generations
give 48 internal labels, but the `6Y=6` block has dimension three. Any
ordinary spatial spin matrices commuting with hypercharge preserve this
block. Two invertible anticommuting matrices X,Y cannot exist on it:

\[
\det(XY)=\det(-YX)=(-1)^3\det(YX)=-\det(XY)\ne\det(XY).
\]

Consequently a Pauli triple cannot be obtained simply by relabeling those
three families as spin components while maintaining the gauge commutation
condition. An independent spin factor could evade this, but its physical
derivation is precisely not supplied here. This is a scoped representation
obstruction, not a no-go theorem for interacting emergent fermions or larger
spaces. Internal Spin(10) and spacetime spin are distinguished, for example,
in Baez and Huerta's [The Algebra of Grand Unified
Theories](https://arxiv.org/html/0904.1556).

The `v775` failed pure root-class-to-matter dictionary remains failed. None
of these Clifford identities makes mixed Gaussian root classes pure.

## 6. Concrete next physical bridge and acceptance test

The recovered algebra makes the next question narrower. Derive, from the
**same charged seam operators**, a representation of these Clifford factors
and three independent gauge-covariant local transport generators. Their
principal symbol must have the above full rank and must commute with the
intended internal gauge action. It is not enough to assign `p_j` by hand or
tensor on a boundary-invisible spectator spinor. Check seam-generatedness
and the relative commutant of the proposed full parent.

The first candidate should then face, in order: its actual free/interacting
two-point pole and chirality; retained versus removed opposite sector and
anomaly/measure consistency; electric/magnetic coupling selection from the
same source map; reflection/unitarity and a selected state. A surviving
candidate must be the same parent for the remaining T1--T8 obligations,
including the gravitational spin-two response. Neither the finite algebra
nor a free overlap demonstration establishes those obligations.

## Reproduction and scope

From this experiment directory:

```sh
python3 checker.py --output validation.json
python3 -m unittest discover -s . -p test_checker.py -v
python3 -OO -m unittest discover -s . -p test_checker.py -v
```

Eight original verification files are SHA-256 pinned and left unchanged.
`validation.json` pins the checker, these notes and its 18-test suite. The
tests include changed source, quadratic offset, erased cocycle diagonal,
unsigned sigma, reversed quaternion orientation and changed matter charge
controls. Full validation replay is checked in both optimization modes.
See `TEST_RESULTS.md` for measured executions and source regressions.

No verification/ledger/paper/website status is promoted. No T1--T8 problem
is marked closed, no net Weyl matter or full TOE is claimed, no RH work is
included, and no original research parent is modified.
