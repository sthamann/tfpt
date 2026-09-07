# Exact equivariant boundary construction and obstruction

Date: 2026-09-06. Work is confined to the smooth square elliptic boundary.
No repository contract status or physical theory is changed by these results.

## 1. Setup and pullback obstruction

Let E=C/(Z+iZ), let O=0, and let P have order four. Set T=2P and assume
iT != T, the successful affine-clock condition in the preceding surface
audit. Put r(z)=iz+T, s(z)=-z, and L_Q=O_E(Q-O). We have r^4=1,
r^2(z)=-z+(T+iT), and rs=sr. Here r^2 is not s.

For an affine automorphism f(z)=az+b and a degree-zero divisor,

    f^* L_Q = L_(a^(-1)Q)

as line-bundle classes. Indeed f^*(Q-O) is
(a^(-1)(Q-b))-(a^(-1)(-b)), whose Abel sum is a^(-1)Q. Translation
disappears from the degree-zero class, although it still matters in an
actual lift and its phases. Therefore

    r^*L_P = L_(-iP),       s^*L_P = L_(-P).

Neither equals L_P. The second would require 2P=0. The first would imply
iP=-P and therefore iT=T, contrary to the successful-clock assumption.
Consequently L_P has no r-linearization and no s-linearization.

A character twist is a trivial underlying line with a chosen group action.
It cannot change a point of Pic(E), so it cannot repair this obstruction.
In fact the r-invariant subgroup of Pic^0(E) is ker(1+i), of order two;
there is no r-invariant primitive order-four degree-zero line at all.
The s-invariant degree-zero lines are E[2]. Thus L_P^2 becomes
s-invariant, but on the successful fibres it remains non-invariant under r.

The distinction between an invariant class and a linearization is standard;
for finite groups see Galkin--Shinder, Section 2.1, equations (2.1)-(2.2):
[primary paper](https://arxiv.org/pdf/1210.3339).
Our impossibility already occurs before any cocycle obstruction.

## 2. The actual minimal repair

Set L_j=(r^j)^*L_P for j=0,1,2,3 and

    V = direct_sum_(j=0)^3 L_j.

The class orbit is P,-iP,-P,iP. These four points are distinct. Pullback by
r cyclically permutes the four summands. The equality r^4=1 supplies the
closing identification, so this gives a genuine coherent linearization
U:r^*V -> V with U^4=1. It requires no guessed affine phase.

This is the smallest r-stable direct sum containing L_P: each member of its
four-element orbit must occur with the same multiplicity. Furthermore,
Hom(L_j,L_k)=Ext^1(L_j,L_k)=0 for j != k, since the relevant difference is a
nontrivial degree-zero line on an elliptic curve. Its h^0 is zero and
Riemann--Roch gives h^1=0. Consequently cross-extensions do not replace this
minimal direct sum with an indecomposable extension of those same factors.
All four L_j are nontrivial, so H^0(E,V)=H^1(E,V)=0.

For inversion alone, the analogous minimal construction is

    W=L_P direct_sum s^*L_P = L_P direct_sum L_(-P),

of rank two, with the coherent exchange linearization.

V solves the equivariance problem for a specified enlarged boundary bundle.
It does not establish that TFPT selects this bundle or identify it with a
four-dimensional fermion determinant over a configuration space.

## 3. Determinants, fixed-point weights and orientation

The ordinary determinant of V is trivial because

    P-iP-P+iP=0.

Its equivariant determinant is not trivially linearized. The equation
(1-i)z=T has two solutions on E. At either r-fixed point, V is the direct
sum of four copies of the same line fibre, and the induced action is the
four-cycle. Hence its weights are 1,i,-1,-i and its determinant is -1.
Since an action on a trivial line over a connected proper curve is given by
constant scalars, this proves the global equivariant determinant character

    det(V) = O_E with r-character -1.

The conclusion is independent of the particular linearization of this V.
Every bundle automorphism is diagonal on the four pairwise nonisomorphic
summands. At a fixed point any lift is a weighted four-cycle; its fourth
power condition says that the product of the four weights is one. Its
determinant is therefore always -1. In particular twisting the rank-four
bundle by a character i^k multiplies its determinant by i^(4k)=1.

Let chi(r)=i denote the canonical-form character, since r^*dz=i dz. Then

    K_E = O_E tensor chi,       det(V) = O_E tensor chi^2.

These are statements about linearized line bundles. For example K_E tensor
det(V) has character chi^3, not the trivial character. No integer power of
det(V), and no common character twist of V, supplies the missing odd power
of chi. The constant coefficient line C_(chi^(-1)) does give an exact
equivariant trivialization

    K_E tensor C_(chi^(-1)) = O_E,

with invariant generator dz tensor e. This is a constructive twisted
orientation, and does not fix the original class obstruction of L_P.
The same derivative-character construction handles r and s simultaneously
because they commute and define a derivative character on their group.

For inversion alone det(W) has character -1, also the character of K_E.
Thus K_E tensor det(W) is equivariantly trivial under s. This is an actual
rank-two determinant compensation for inversion; W is not r-stable.

These are ordinary bundle determinants. They must not be confused with
det RΓ(E,V), which is canonically C for this acyclic V, or with an analytic
Quillen/Bismut--Freed determinant line in a family.

## 4. Stack descent is available; coarse descent fails

The linearized V is an honest vector bundle on [E/<r>]. At its order-four
stabilizers the fibre representation contains all four characters. Hence
it is not the pullback of an ordinary vector bundle from the coarse
quotient. Character twists permute these weights and cannot make all of
them trivial. Similarly W cannot descend to the coarse pillowcase at its
inversion fixed points, where its weights are +1 and -1.

This is the standard stabilizer descent criterion, Alper Theorem 10.3:
[Good moduli spaces for Artin stacks](https://sites.math.washington.edu/~jarod/papers/gms.pdf).
The bundle construction therefore requires retaining orbifold/stack data,
or an equivalent parabolic formulation, rather than dropping stabilizers.

## 5. What happens to the original cyclic gluing data

Write P=(a,b)/4. The successful condition is that a and b have opposite
parity. The determinant of the pair P,iP modulo four is a^2+b^2, which is
one modulo four. Thus P and iP are a basis of E[4]. In particular

    <L_P> is not r-stable,
    subgroup generated by its r-orbit = Pic^0(E)[4] = (Z/4)^2.

The bundle V has four line summands, but the tensor subgroup generated by
them has sixteen elements. It does not preserve the original order-four
gluing subgroup as a subgroup with an action.

The successful points have two i-orbits, represented by (1,0)/4 and
(1,2)/4. No character twist identifies their marked line bundles. This is
consistent with the two inequivalent P-marked fibres in the surface audit.

## 6. A separate, explicitly solvable theta alternative

The positive-degree line A=O_E(4O) is invariant as a class under r and s,
because r^(-1)O=iT and 4iT=0. This differs from the degree-zero gluing line.
Its section space has dimension four. The theta-group construction is
Mumford, Section 1, especially Proposition 3 and Theorem 2:
[On the Equations Defining Abelian Varieties I](https://pazuki.perso.math.cnrs.fr/index_fichiers/Mumford66.pdf).

On Y^2=X^3-X, take i(X,Y)=(-X,iY) and T=(1,0). In basis (1,X,Y,X^2), an
explicit lift of the affine r is

    R = [[1/2,-1/2,0,1/2], [1,0,0,-1],
         [0,0,-i,0], [1/2,1/2,0,1/2]].

Indeed

    r(X,Y)=((X-1)/(X+1), -2iY/(X+1)^2),
    (R f)(X,Y)=((X+1)^2/2) f(r(X,Y)).

Exact calculation gives R^4=I and

    det(lambda I-R)=(lambda-1)(lambda-i)(lambda+i)^2.

This particular affine-clock representation is not four distinct character
lines. Changing its lift by a character rotates multiplicities, preserving
the pattern (2,1,1,0). It is not the regular representation of the rank-four
degree-zero orbit bundle.

Translation by P does have four distinct projective eigenlines on H^0(A).
But r conjugates this translation to translation by iP. Since the Weil
pairing e_4(P,iP)=i (in the stated oriented convention), their theta lifts
do not commute. In particular the original P-eigenline quartet is sent to
a different eigenline quartet. Thus theta structure supplies a valid
separate construction, not an unproved identification of the gluing line,
Kummer marks and the affine r-clock.

## 7. Relation to the existing TFPT contract

The read-only check of tfpt_research_contracts.tex, section
SEAM.DETLINE.UNIFICATION.01 (starting near line 13616), requires an
isomorphism of the actual determinant lines with connection and matching
bulk holonomy. It explicitly leaves the continuum Bismut--Freed step open.
The present results give an actual boundary bundle and twisted orientation,
plus exact impossibility statements about the rank-one proposal and coarse
descent. They do not supply a bulk Dirac family, analytic normalization,
physical state, chirality, a three-family index, or T1--T8 closure.

The standalone checker in this directory exhausts all sixteen E[4] points,
checks all eight successful primitive points, fixed points, weighted-cycle
determinants, orientation characters and the explicit theta lift. Its finite
arithmetic supports the formulas above; the proofs justify their geometric
interpretation.

