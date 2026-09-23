# The family-inner compiler orders and their positive trace lattice

Date: 2026-09-09. This is an exact algebraic result for the pinned compiler
source, not a derivation of a physical state, Hamiltonian, locality or TOE.
The source comparison, including the original marked Construction-A lattice,
is documented separately in [MARKED_BRIDGE.md](MARKED_BRIDGE.md). The exact
identities and finite certificates below are reproduced by
[checker.py](checker.py).

## 1. Fixed data and the meaning of uniqueness

The original real Clifford algebra contains the anchor \(a\) and quaternion
units \(u_1,u_2,u_3\), with

\[
a^2=u_j^2=-1,\qquad [a,u_j]=0,\qquad u_1u_2=u_3
\]

and cyclic variants. Their adjoints are their negatives. Work in the fixed
rational anchor commutant

\[
B=\mathbb Q(a)\langle1,u_1,u_2,u_3\rangle\cong M_2(\mathbb Q(i)),
\qquad D=\mathbb Z[a]\cong\mathbb Z[i].
\]

The original order is the Gaussian Lipschitz order

\[
\mathcal O=D\langle1,u_1,u_2,u_3\rangle.
\]

An *overorder* means a unital subring of this same \(B\), containing
\(\mathcal O\), which is a full, finitely generated integral lattice.
Changing the rational algebra or allowing an infinite denominator
localization is not part of the statement.

The signed family cycle is implemented by

\[
w=\frac{1+u_1+u_2+u_3}{2},\qquad w^*=w^{-1},\qquad w^3=-1.
\]

There are two distinct canonical answers to different selection questions:

\[
\boxed{\mathcal O\subset\mathcal R=\mathcal O[w]\subset\mathcal M},
\qquad
[\mathcal R:\mathcal O]=4,\quad
[\mathcal M:\mathcal R]=4.
\]

The order \(\mathcal R\) is the unique **minimal** extension admitting the
family action by an order unit. The order \(\mathcal M\) is its unique
**maximal** overorder. There are no intermediate orders between them.
Both are adjoint-stable. Thus family-innerness and adjoint-stability alone
do not decide between minimal and maximal completion.

## 2. The minimal unit completion

The Gaussian basis

\[
\mathcal R=D\langle1,u_1,u_2,w\rangle
\]

is the Gaussian extension of the usual Hurwitz quaternion order. Closure
under multiplication and adjoint follows either from the displayed
quaternion relations or the exact basis-product checks. Since
\(u_3=2w-1-u_1-u_2\), its Gaussian index over \(\mathcal O\) is the
ideal index associated with 2; its ordinary integral index is 4.

Suppose an overorder contains a unit \(v\) inducing the same automorphism
on \(B\). Then \(v=cw\), because \(vw^{-1}\) commutes with all of \(B\),
and \(c\in\mathbb Q(i)^\times\). Both \(v^3=-c^3\) and its inverse
belong to the center of the overorder. That center is \(D\): its elements
are algebraic integers in \(\mathbb Q(i)\), whose full integer ring is
\(D\). Hence \(c^3\in D^\times\), so \(c\) and \(c^{-1}\) are integral,
and \(c\in\{1,-1,i,-i\}\). Therefore adjoining any such \(v\) adjoins
exactly \(w\), proving minimality and uniqueness of \(\mathcal R\).

This phase statement concerns the action on the commutant \(B\). In the
full compiler, \(a\) is not central: multiplying \(w\) by \(a\) changes
the signs on the first three Clifford generators. The actual full signed
family lift restricts the ambiguity to \(\pm w\); it gives the same
order \(\mathcal R\).

The word *unit* is essential. Already
\(2w=1+u_1+u_2+u_3\in\mathcal O\) induces the family automorphism by
conjugation in the rational algebra, but its inverse is not in
\(\mathcal O\). It is neither an order unit nor a unitary operation.

## 3. An explicit maximal order and its adjoint

Use the faithful minimal representation

\[
a=iI_2,\quad u_1=\begin{pmatrix}i&0\\0&-i\end{pmatrix},\quad
u_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad u_3=u_1u_2.
\]

Set

\[
\pi=1+i,\quad
P=\begin{pmatrix}1&1/\pi\\0&1/\pi\end{pmatrix},\qquad
\mathcal M=P M_2(D)P^{-1}.
\]

This is a maximal order: \(M_2(D)\) is maximal and conjugation preserves
maximality. In this lattice basis,

\[
P^{-1}u_1P=\begin{pmatrix}i&1+i\\0&-i\end{pmatrix},\quad
P^{-1}u_2P=\begin{pmatrix}1&1-i\\-1-i&-1\end{pmatrix},\quad
P^{-1}wP=\begin{pmatrix}1&1\\-1&0\end{pmatrix}.
\]

Thus \(\mathcal R\subset\mathcal M\). Relative to the four standard
matrix units, the Gaussian coordinate determinants of the bases of
\(\mathcal O\) and \(\mathcal R\) are respectively 4 and 2. Their
integral indices in \(\mathcal M\) are therefore 16 and 4.

The inherited adjoint is not ordinary conjugate transpose in this
nonorthonormal basis. It is

\[
Y\longmapsto H^{-1}Y^*H,\qquad
H=P^*P=\begin{pmatrix}1&(1-i)/2\\(1+i)/2&1\end{pmatrix}.
\]

Here \(\det H=1/2\), while

\[
\pi H=\begin{pmatrix}1+i&1\\i&1+i\end{pmatrix}\in GL_2(D),
\qquad \det(\pi H)=i.
\]

The scalar factor cancels in conjugation. Consequently this adjoint
preserves \(M_2(D)\), and the original adjoint preserves \(\mathcal M\).

An explicit Gaussian basis \(b_{jk}=PE_{jk}P^{-1}\) is

\[
\begin{aligned}
b_{11}&=(1-au_1-u_2+au_3)/2,\\
b_{12}&=((1+a)u_2+(1-a)u_3)/2,\\
b_{21}&=((-1-a)u_1+(-1+a)u_2)/2,\\
b_{22}&=(1+au_1+u_2-au_3)/2.
\end{aligned}
\]

Their matrix-unit multiplication makes the ring structure explicit.

## 4. Unique maximal completion and absence of intermediate orders

In \(P\)-coordinates, \(\pi M_2(D)\subset\mathcal R\). Reduction modulo
\(\pi\) identifies its image with

\[
\mathbb F_2[\bar w]\cong\mathbb F_4\subset M_2(\mathbb F_2),
\quad
\bar w=\begin{pmatrix}1&1\\1&0\end{pmatrix},\quad
\bar w^2+\bar w+I=0.
\]

Indeed \(u_1,u_2\) reduce to scalars, and \(x^2+x+1\) is irreducible
over \(\mathbb F_2\). This describes \(\mathcal R\) as the inverse
image of a nonsplit quadratic field in the residue matrix algebra.

Localize at \(\pi\). Let \(L'\) be any full \(\mathcal R_\pi\)-stable
lattice in the two-dimensional local vector space. Multiplying by a
central power of \(\pi\), arrange \(L'\subset D_\pi^2\) but
\(L'\not\subset\pi D_\pi^2\). Its nonzero reduction is invariant under
\(\bar w\), which has no invariant line. The reduction is therefore
all of \(\mathbb F_2^2\). Nakayama's lemma applied to
\(D_\pi^2/L'\) gives \(L'=D_\pi^2\).

Every maximal order in a split local matrix algebra is the endomorphism
ring of a lattice, up to this scalar homothety. Thus there is only one
maximal order containing \(\mathcal R_\pi\). At other primes the index
4 is invertible, so \(\mathcal R\) already equals \(\mathcal M\)
locally. The local-global equality of lattices proves uniqueness of the
global maximal overorder. These general order/lattice facts are standard;
see [Voight, Quaternion orders, Sections 23.2 and 23.5](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_23).

Any intermediate order reduces modulo \(\pi\mathcal M\) to a subring
between \(\mathbb F_4\) and \(M_2(\mathbb F_2)\). As a left
\(\mathbb F_4\)-vector space its \(\mathbb F_2\)-dimension must be even:
either 2 or 4. Thus it is one of the endpoints. Since every overorder is
contained in a maximal order, \(\mathcal R\) and \(\mathcal M\) exhaust
all overorders of \(\mathcal R\).

## 5. The integral positive cone does not distinguish the orders

Write \(\alpha_j=-au_j\) and
\(X=tI+x\alpha_1+y\alpha_2+z\alpha_3=X^*\). Then

\[
P^{-1}XP=
\begin{pmatrix}
t+x-iy-z&(1-i)(x-iy)\\
(1+i)(iy+z)&t-x+iy+z
\end{pmatrix}.
\]

Gaussian integrality forces \(y\in\mathbb Z\) from the diagonal
imaginary parts, then \(x,z\in\mathbb Z\) from the off-diagonal entries,
and finally \(t\in\mathbb Z\). All three orders already contain these
elements. Hence

\[
\mathcal O\cap\mathcal J=\mathcal R\cap\mathcal J
=\mathcal M\cap\mathcal J=\mathbb Z^4.
\]

Their positive integral points are the same future Lorentz cone points

\[
t\ge\sqrt{x^2+y^2+z^2}.
\]

Their *available operations* differ. For example

\[
q=\frac{(1+a)(1+u_1)}2\in\mathcal M\setminus\mathcal R,
\qquad qq^*=1,\quad q^4=1.
\]

Its conjugation sends \(u_2\mapsto u_3\), \(u_3\mapsto-u_2\). In
the \(P\)-basis it is \(\begin{pmatrix}i&i\\0&1\end{pmatrix}\).
Adjoining this quarter-turn to \(\mathcal R\) generates \(\mathcal M\).
Whether the microscopic source executes it is a genuine discriminator;
merely reproducing positive points cannot answer that question.

## 6. The maximal order carries the \(E_8\) trace lattice

Give \(\mathcal M\) the positive form

\[
\langle A,B\rangle=\operatorname{Re}\operatorname{Tr}_2(AB^*),
\qquad Q(A)=\operatorname{Tr}_2(AA^*).
\]

The trace is the reduced two-dimensional trace, not the doubled trace in
the original complex four-dimensional compiler representation. Since
\(AA^*\in\mathcal M\cap\mathcal J\), its trace is an even integer.
Polarization gives integral pairings. The monomial basis of
\(\mathcal O\) has Gram matrix \(2I_8\); consequently

\[
\det G_{\mathcal M}=\frac{2^8}{[\mathcal M:\mathcal O]^2}
=\frac{256}{16^2}=1.
\]

In the ordered basis
\((b_{11},ab_{11},b_{12},ab_{12},b_{21},ab_{21},b_{22},ab_{22})\),
the exact Gram matrix is

```text
 2  0 -1  1  1  1 -1  0
 0  2 -1 -1 -1  1  0 -1
-1 -1  2  0  0 -1  1  1
 1 -1  0  2  1  0 -1  1
 1 -1  0  1  2  0 -1  1
 1  1 -1  0  0  2 -1 -1
-1  0  1 -1 -1 -1  2  0
 0 -1  1  1  1 -1  0  2
```

Its leading principal minors are \(2,4,4,4,4,4,2,1\). Thus this is a
positive, even, integral, unimodular lattice of rank eight. The checker
also provides a direct certificate identifying its root system: an
integral determinant-one simple-root basis whose Cartan graph has edges
\((0,2),(1,2),(1,6),(2,3),(3,4),(4,5),(5,7)\), the \(E_8\) tree with
arms of lengths 1, 2 and 4. Classification alone is not needed for that
finite certificate.

The lattice carries the inherited markings, not just an abstract metric.
Left multiplication by \(a\) is an integral orthogonal map squaring to
\(-I\). The family map \(A\mapsto wAw^*\) commutes with it and has
characteristic polynomial \((t-1)^4(t^2+t+1)^2\). In the \(P\)-basis its
fixed matrices are
\(\begin{pmatrix}z_1&z_2\\-z_2&z_1-z_2\end{pmatrix}\), with
\(z_1,z_2\in D\). Their integral trace lattice is \(A_2\oplus A_2\),
of determinant 9, with exactly 12 norm-two roots. These are useful
discriminators for a marked comparison: an arbitrary order-three
isometry of an arbitrary \(E_8\) presentation would not suffice.

The root enumeration is exhaustive, not a truncated guess.
\((G^{-1})_{jj}=2\), so Cauchy-Schwarz with the dual basis gives
\(|x_j|\le2\) for every norm-two vector. Exact integer enumeration of
all \(5^8\) possibilities yields 240 roots. Their reduced Gaussian
determinants are \(1,-1,i,-i\), each 24 times, and 0, 144 times.
Thus 96 roots are unitary and 144 have rank one. For the first assertion,
\(AA^*\) has positive eigenvalues of sum 2 and product 1, forcing
\(AA^*=I\).

This trace norm is **not** the multiplicative arithmetic norm
\(\nu(A)=|\det_2 A|^2\). The matrix unit \(b_{12}\) has trace norm 2,
but \(b_{12}^2=0\) and \(\nu(b_{12})=0\). The result is an associative
order with an \(E_8\) Euclidean lattice, not an octonionic composition
algebra or a multiplicative positive-definite \(E_8\) norm.

## 7. What is selected, and what still requires a source theorem

Within the stated family-inner overorders, maximality selects
\(\mathcal M\) uniquely. Equivalently, requiring this inherited trace
lattice to be unimodular selects it: \(\mathcal R\) has trace Gram
determinant 16, whereas \(\mathcal M\) has determinant 1. This equivalence
is a conditional mathematical selection result. It does not establish
that microscopic physical operations must be maximal or unimodular.

The marked lattice connection is stronger than an unmarked \(E_8\)
classification and is treated in [MARKED_BRIDGE.md](MARKED_BRIDGE.md).
Neither connection by itself identifies old Hilbert spaces or supplies
their dynamics. In particular the faithful states

\[
\rho_r=\tfrac12(1+rS/\sqrt3),\quad -1<r<1,\quad
S=\alpha_1+\alpha_2+\alpha_3,
\]

are all normalized, positive, and family-invariant. Likewise
\(H=h_0I+hS\) supplies arbitrary family-compatible selfadjoint generators.
The algebraic identification therefore narrows the missing physical
object to a marked operation/state/process realization; it does not
uniquely validate that realization or close any T1--T8 physical claim.
