# Relative determinant: exact closure and obstructions

Date: 2026-09-06. Bounded independent mathematical follow-up to
the user-supplied CY proposal. Integrated as unpromoted research; no claim of analytic
determinant matching, no physical chirality or TOE closure.

## 1. Setup and determinant convention

Let `f:S -> P1` be the smooth minimal rational elliptic surface attached to
`y^2+xy+ty=x^3+tx^2`, with zero section `O`, order-four section `P`, and a
chosen smooth fibre `F`. The prior audit established `K_S=-F`,
`O^2=P^2=-1`, `P.O=0`, `P.F=O.F=1`, and the frame lattice
`L={O,F}^perp = E8(-1)`. Its restriction to smooth fibres factors through
`L/(D5(-1)+A3(-1)) = Z4`. Put

\[
D_P=P-O-F,\qquad D_P^2=-2,\qquad
\mathcal O_S(D_P)|_F=L_P=\mathcal O_F(P-O).
\]

We use the algebraic convention
`lambda(V)=det R Gamma(V)=tensor_q det H^q(V)^{(-1)^q}`.
Some analytic authors use its dual. All subsequent signs refer to this
declared convention. Determinants are graded lines when needed; the usual
Koszul signs are retained by the determinant functor.

## 2. An exact cohomology theorem for every nontrivial frame coset

**Proposition.** Suppose `D in L` has nontrivial restriction to a smooth
fibre. Write `D^2=-2m`. For every integer `q`,

\[
h^0(S,\mathcal O(D+qF))=h^2(S,\mathcal O(D+qF))=0,
\quad \chi(S,\mathcal O(D+qF))=1-m,
\quad h^1(S,\mathcal O(D+qF))=m-1.
\]

**Proof.** The fibre class is nef. Every effective divisor `A` with
`A.F=0` has only vertical components: a horizontal irreducible component
has strictly positive degree over the base and hence positive intersection
with `F`. Every vertical divisor restricts trivially to a smooth fibre.
Components in other fibres are disjoint; the whole chosen smooth fibre
has trivial normal bundle. If `D+qF` were effective, its restriction would
therefore be trivial, contradicting the hypothesis. Thus `h0=0`.
Serre duality identifies `h2(O(D+qF))` with
`h0(O(-D-(q+1)F))`; the same argument, with inverse nontrivial restriction,
gives zero. Surface Riemann--Roch, `chi(O_S)=1`, `K=-F`, `D.F=F^2=0`,
then gives `chi=1+D^2/2=1-m`. This proves the assertion.

Consequently, whenever `n` is not divisible by four,

\[
h^\bullet(S,\mathcal O(nD_P+qF))=(0,n^2-1,0).
\]

| Divisor | Restriction to F | Surface cohomology (h0,h1,h2) |
| --- | --- | --- |
| D_P | L_P | (0,0,0) |
| 2D_P | L_P^2 | (0,3,0) |
| 3D_P | L_P^3 | (0,8,0) |
| 5D_P | L_P | (0,24,0) |

In particular, **the identical boundary line `L_P` does not determine the
surface cohomology**. The nontriviality hypothesis is essential: this
table must not be extrapolated to multiples divisible by four.

There is a useful localization statement. Nontrivial torsion sections
remain nontrivial on every smooth fibre (over the smooth base, torsion is
finite etale). Therefore `f_*O(D)=0`: its generic rank is zero, and direct
image of a line bundle to the integral base is torsion-free. The sheaf
`R^1 f_*O(D)` has generic rank zero and is a torsion sheaf supported on
the three singular fibres. Leray gives

\[
H^1(S,\mathcal O(D))=H^0(\mathbb P^1,R^1f_*\mathcal O(D)),
\qquad \operatorname{length} R^1f_*\mathcal O(D)=m-1.
\]

This determines its total length, not its distribution among the three
fibres or its module structure. These are coherent cohomology groups,
not automatically physical particle states.

## 3. What the relative determinant actually closes

Choose an isomorphism `O(-F) ~= K_S` and the corresponding anticanonical
section `s`. The divisor sequence is

\[
0\longrightarrow V K_S\xrightarrow{\ s\ }V
\longrightarrow i_*(V|_F)\longrightarrow0.
\]

For nontrivial degree-zero `V|_F`, `R Gamma(F,V|_F)=0`. Indeed a nonzero
section of a degree-zero line on an elliptic curve would have no zeros
and trivialize it; genus-one Riemann--Roch gives `h1=h0=0`.
Thus multiplication by `s` is a quasi-isomorphism on global sections and
induces

\[
\lambda_S(VK_S)\xrightarrow{\sim}\lambda_S(V),\qquad
\lambda_F(V|_F)=\lambda_S(V)\lambda_S(VK_S)^{-1}\xrightarrow{\sim}\mathbb C.
\]

This is an actual algebraic closure of the *relative* line. It identifies
the two bulk determinants; it does not identify either bulk determinant
with the boundary determinant. For `V=O(D_P)` both bulk complexes happen
to be acyclic. For `V=O(5D_P)` they both have 24-dimensional H1 and the
same relative cancellation holds.

The assertion extends to perfect families over a base when every boundary
fibre is acyclic: derived base change and Nakayama give zero boundary
pushforward, hence its canonical determinant trivialization. This says
nothing yet about a Quillen metric or connection.

There is also a normalization issue: using the ideal inclusion
`O(-F) -> O_S` is intrinsic to the divisor, whereas expressing its source
as `K_S` requires the chosen identification. Replacing `s` by `c s`
changes the induced determinant map by `c^{chi(S,V)}`. For `5D_P` the
exponent is `-24`. The relative exact-sequence map retains this dependence;
it is not a canonically fixed absolute normalization after forgetting `s`.

**Concrete family counterexample to deleting the extra factor.** Fix S
and F and take `B=P1`, `M=O_B(1)`,

\[
\mathcal V=\mathcal O_S(5D_P)\boxtimes M
\quad\text{on }S\times B.
\]

The boundary family is `L_P boxtimes M` and is acyclic, so its determinant
is `O_B`. But both surface pushforwards have only
`R^1 ~= H^1(S,O(5D_P)) tensor M`, of rank 24. Consequently

\[
\lambda_{S/B}(\mathcal V)\simeq\mathcal O_B(-24),\qquad
\lambda_{S/B}(\mathcal V K_{S/B})\simeq\mathcal O_B(-24),\qquad
\lambda_{F/B}(\mathcal V|_{F\times B})\simeq\mathcal O_B.
\]

Constant one-dimensional vector-space factors are suppressed in these
isomorphism classes. Degree distinguishes the lines: the proposed equality
of a single bulk determinant with the boundary line is false even as an
algebraic line bundle over this elementary family.
This is a family obtained by a parameter-line twist, not a new geometric
modulus of S. A proposed functorial identity must respect such twists;
excluding them requires an explicit framing/rigidification condition.

## 4. Serre duality: a product, and a square for self-dual bundles

For a vector bundle V on a smooth proper complex surface, Serre duality
gives `H^q(VK) ~= H^{2-q}(V^vee)^vee`. Taking alternating determinants,

\[
\lambda_S(VK_S)\simeq\lambda_S(V^\vee)^{-1},
\qquad
\boxed{\lambda_F(V|_F)\simeq\lambda_S(V)\otimes\lambda_S(V^\vee).}
\]

The inverse in the first formula comes from dualization; dimension two
contributes an even degree shift. It is easy to get this sign wrong.
Relative Serre duality gives the same identity over a smooth proper
surface family, using the *relative* canonical bundle.

An actual chosen self-duality `V ~= V^vee` gives
`lambda_F(V|F) ~= lambda_S(V)^2`, not cancellation. If the boundary is
acyclic it produces a specified square trivialization. A square
trivialization is not a specified section of its square root: already
on one complex line, `v -> -v` preserves its square while exchanging
the two normalized roots. Global two-torsion and equivariant characters
must also be checked. No automatic Pfaffian or analytic norm is inferred.

There is one honest special cancellation: for the hyperbolic double
`H(V)=V direct_sum V^vee`, multiplicativity identifies
`lambda_S(H(V))` with `lambda_F(V|F)` via the above formula. In the
acyclic boundary case this bulk determinant is algebraically trivialized
(relative to the divisor/duality data). This construction doubles the
bundle; it does not produce a chiral family or a Quillen isometry.

## 5. CM orbit bundle: pairing, zero modes, and a determinant character

Now work on a selected `F=E_i` with `a(z)=iz` and an order-four P whose
`T=2P` satisfies `iT != T`, as on the two surviving CM fibres in the audit.
Pullback acts by `a^* L_P=L_{-iP}`. Set

\[
L_j=(a^j)^*L_P,\quad j\in\mathbb Z/4,
\qquad W=\bigoplus_{j=0}^3L_j.
\]

The four line classes are distinct and nontrivial. Opposite lines satisfy
`L_{j+2} ~= L_j^vee`. Thus `h0(W)=h1(W)=0`, and the ordinary and
equivariant Dolbeault indices of W both vanish. Taking four orbit summands
cannot turn these acyclic lines into three chiral zero modes.

There is a genuine equivariant construction: `a^*W -> W` cyclically
reindexes the summands, and its fourth power is identity. Rigidify the
degree-zero lines at the fixed origin. The inverse-pair identifications
are then unique as rigidified line isomorphisms. They give the symmetric,
nondegenerate pairing

\[
B(u,v)=u_0v_2+u_2v_0+u_1v_3+u_3v_1,
\]

which is invariant under the cyclic lift. At the origin the lift has
the regular four-cycle representation, with eigencharacters
`1, chi, chi^2, chi^3`, where `chi(a)=i`. Its determinant is `-1`.
Although `det W` is ordinarily trivial, its natural equivariant
determinant carries the nontrivial sign character.

This sign cannot be removed by tensoring W with a constant Z4 character:
the determinant changes by its fourth power, which is 1. More generally,
because the four L_j are distinct, an equivariant isomorphism must cycle
them with four scalar factors whose product is 1. Its determinant at the
origin is again -1. Hence this honest order-four orbit lift admits no
invariant trivialization of its determinant. Allowing a projective lift
whose fourth power is -I would change the problem, not solve the same one.

The invariant symmetric pairing above therefore gives an O(4)-type
structure with orientation character; it is not automatically an
equivariantly oriented SO(4) or SU(4) structure. A nondegenerate invariant
alternating pairing is impossible for this regular representation: its
one-dimensional eigencharacters 1 and -1 would each have to pair with
themselves. With the holomorphic line splitting, cyclic invariance of the
only possible opposite-summand alternating pairings forces their
coefficients to vanish.

For the affine clock `r(z)=iz+T`, pullback on degree-zero line *classes*
is the same. Cyclic induction still works, but rigidifications and the
pairing must be transported using an actual chosen fixed point/line
isomorphism. The linear-clock calculation is not a silent construction
of a global automorphism of S.

**A tempting three-dimensional space is also nonchiral.** Since the
off-diagonal Hom lines are nontrivial, the different coefficient bundle
`End_0(W)` has `h0=h1=3`. This is not the cohomology of W. With pullback
character convention `a^*dz=i dz`, equivariant Serre duality gives

\[
H^0(End_0W)=\chi+\chi^2+\chi^3,
\quad H^1(End_0W)=1+\chi+\chi^2,
\quad \operatorname{ind}_{\mathbb Z_4}=\chi^{-1}-1.
\]

The nonequivariant index is zero. The invariant sector has index -1,
not three; replacing pullback by the inverse action conjugates the
characters. Omitting the canonical-form character would miscount this
sector. This remains a mathematical Dolbeault statement on F, not a
four-dimensional matter-spectrum derivation.

## 6. Acyclicity does not flatten a Quillen connection

Here is a concrete independent counterexample. Keep an elliptic curve E
and its flat metric fixed. Let `Ehat=Pic^0(E)` and let `Poin` be the
rigidified Poincare line on `E x Ehat`, with its standard unitary family
connection. On `U=Ehat minus {O}`, every fibre line is nontrivial degree
zero and acyclic. Thus `det R pi_*Poin|_U` is canonically trivial as an
algebraic line.

Nevertheless, the local family index/Quillen curvature formula is
nonzero. Choose normalized one-forms `a,b` on E and `alpha,beta` on
Ehat with `integral_E a wedge b=1` and represent

\[
c_1(Poin)=a\wedge\beta-b\wedge\alpha.
\]

Since the relative tangent metric is flat,

\[
c_1(\lambda,\|\cdot\|_Q)
=\pi_*\frac{c_1(Poin)^2}{2}
=-\alpha\wedge\beta\ne0
\]

in the declared algebraic determinant convention (dual determinant
convention reverses the sign). Here `c1(lambda,||.||_Q)` denotes the
normalized Chern curvature form, avoiding an extra sign convention for
the unnormalized curvature operator. Restricting the constant nonzero form to U
does not kill it. There is no contradiction: the trivial line on U can
have a nonconstant Quillen norm and a curved connection. Small
contractible loops with nonintegral enclosed normalized area have
nontrivial holonomy. Thus even local holonomy triviality does not follow
from the absence of zero modes.

This is a counterexample to the *general inference*, not a computed
curvature for the proposed TFPT determinant. The fourth-torsion locus
of a fixed E is discrete, so the Poincare example must not be reported
as a continuous deformation staying inside that fixed torsion locus.
The actual varying elliptic/surface/connection family still has to be
specified and its metric anomaly and holonomies computed.

## 7. What is closed and the next discriminating computation

Closed algebraically: frame-bundle cohomology, singular-fibre support of
the bulk cohomology, the exact relative determinant trivialization in
the acyclic boundary case, the duality product formula, and an explicit
paired rank-four orbit bundle with its unavoidable determinant character.

Ruled out: recovering a single bulk determinant from the boundary torsion
class alone; turning the four nontrivial degree-zero orbit lines into
three Dolbeault zero modes; inferring a parallel Quillen trivialization
from acyclicity; discarding the orientation character in the orbit lift.

Next discriminating data: specify the actual family of coefficient
bundles/operators and the lift of the clock. If bulk states are intended,
compute the modules `R^1f_*O(D)` on the three singular fibres and their
symmetry action; their total length is already constrained above. Then
compare the exact-sequence determinant isomorphism with the chosen
analytic metrics/connections. These are new required calculations,
not supplied by the cohomology identities.

## Sources and verification scope

- [Stacks, determinants of perfect complexes, tag 0FJI](https://stacks.math.columbia.edu/tag/0FJI):
  determinant functor and canonical trivialization for acyclic complexes.
- [Stacks, derived duality, tag 0B6I](https://stacks.math.columbia.edu/tag/0B6I),
  together with the smooth surface dualizing complex `K_S[2]`:
  the Serre-duality input used in the explicit sign computation.
- [Stacks, Grothendieck--Riemann--Roch, tag 02UO](https://stacks.math.columbia.edu/tag/02UO):
  its smooth proper surface-to-a-point specialization yields the Euler
  formula used above by expanding the Chern character and Todd class.
- [Freed, On Determinant Line Bundles, Theorems 1.30--1.31 and section 4](https://people.math.harvard.edu/~dafr/detsur.pdf):
  curvature, holonomy, and elliptic-curve determinant families. His
  Fredholm determinant convention is dual to the algebraic convention
  declared above; signs are translated accordingly.
- [Freed, Determinant Line Bundles Revisited](https://arxiv.org/abs/dg-ga/9505002):
  geometric determinant connections and holonomy.

All propositions specific to the marked surface/orbit above are derived
in this note. The companion checker verifies intersection arithmetic,
Riemann--Roch consequences, finite torsion orbits, representation
characters, pairing invariance and the exterior-algebra curvature
calculation. It is not a computer proof of Serre duality, Riemann--Roch,
cohomological base change or the analytic family index theorem.

