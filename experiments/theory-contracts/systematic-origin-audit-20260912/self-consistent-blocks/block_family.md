# An exact two-coordinate block for the changing compiler interaction

The previous primitive ground encoding need not be held fixed when new
couplings are generated. For the specified three-register family, the
entire required readjustment fits inside **two real multiplicity
coordinates, each carrying the same four-dimensional logical factor**.
This is an exact finite invariant enclosure, not a numerical truncation.

## 1. Actual source and declared family

Use the original four Clifford generators g_i and Hermitian a_i=i g_i.
On a dual pair put S_i=a_i tensor conjugate(a_i) and

    h4=sum_i (I-S_i)/2,
    h10=sum_i (I-S_i)/2 + sum_(i<j)(I-S_i S_j)/2
       =5h4-h4^2.

The last equality is checked directly from the ten source words. Let H
be the sum of h4 on edges 12 and 23 of V tensor bar(V) tensor V, and T
the corresponding sum of h10. The same-copy outer interaction is

    N=sum_i a_i tensor I tensor a_i.

The changing parent studied here is H(u,v)=H+uT+vN, with real u,v. This
is a declared finite family motivated by earlier perturbative terms;
it is not asserted to contain every operator generated at every scale.
In particular the same-copy outer term is not a dual Bell projector.

## 2. Rational common hull and minimality

Let Phi=(1/2)sum_a |aa>, V0=Phi_12 tensor I, W0=I tensor Phi_23, and

    B=V0+W0, C=(4I-H)B, J=[B,C].

The exact Gram is

    J*J = [[5/2,6],[6,15]] tensor I4.

Its two-coordinate determinant is 3/2, hence J has rank eight. Direct
64-dimensional matrix multiplication gives

    H J=J(M4 tensor I4),  M4=[[4,-6],[-1,4]],
    T J=J(M10 tensor I4), M10=[[4,-12],[0,9]],
    N J=J(MN tensor I4),  MN=[[-4,-12],[2,6]].

These coordinate matrices are self-adjoint in the stated Gram, not in
the Euclidean metric. The tests verify both closure and the metric
identity K M=M^T K, preventing a false Hermiticity assumption.

Define orthonormal maps

    G_minus=(B+C/sqrt(6))/(sqrt(3)+sqrt(2)),
    G_plus =(B-C/sqrt(6))/(sqrt(3)-sqrt(2)).

G_minus is exactly the earlier primitive G, not a substituted candidate.
The maps have H energies 4-sqrt(6) and 4+sqrt(6). Crucially

    N G_minus=G_minus-G_plus.

Thus the original G and one application of N already span the entire
eight-dimensional enclosure. Since that enclosure is invariant under
all three operators, it is the **smallest common invariant hull** of the
original logical ground space. Its logical degeneracy is not removed.

## 3. Exact changing ground equation inside the hull

In the orthonormal [G_minus,G_plus] coordinates,

    H(u,v) = [[c-sqrt(6)(1+u), -(u+2v)/2],
              [-(u+2v)/2, c+sqrt(6)(1+u)]] tensor I4,
    c=4+13u/2+v.

The two energy branches, each fourfold, are exactly

    E_plus/minus=c +/- sqrt(24(u+1)^2+(u+2v)^2)/2.

This supplies a two-component eigenvector equation for an adjusted
encoding G(u,v)=x G_minus+y G_plus, with |x|^2+|y|^2=1. The old G
remains an eigen-encoding **if and only if u+2v=0**. Along that line it
is the lower hull branch for u>-1, the upper branch for u<-1; both
branches coincide at u=-1,v=1/2. That point is the only degeneracy of
the two-coordinate matrix. It need not be a global physical ground.

Writing delta=sqrt(6)(1+u), q=(u+2v)/2 and r=sqrt(delta^2+q^2), an
explicit normalized lower-branch vector near the primitive point is

    x=sqrt((r+delta)/(2r)),
    y=q/sqrt(2r(r+delta)).

It is valid where r>0 and r+delta>0. The other coordinate chart covers
the remaining nondegenerate points. At u=v=0 it gives x=1,y=0 exactly.
This formula states an exact hull eigenvector, not an independent
claim that the selected branch stays lowest among all 64 states.

## 4. A controlled neighborhood where it really is the global ground

At u=v=0 the omitted spectrum starts at energy 2, while E0=4-sqrt(6).
The full gap is g=sqrt(6)-2. Each ten-word pair term has spectrum in
[0,6], so 0<=T<=12I and ||T-6I||<=6. The same-copy outer term has norm
||N||=4. Removing the harmless scalar 6uI gives the sharper bound

    ||u(T-6I)+vN|| <= 6|u|+4|v|.

By the finite-dimensional min-max eigenvalue bound, the four lowest
states remain isolated, with gap at least

    sqrt(6)-2-12|u|-8|v|.

Because the exact common hull contains the original ground and is
reducing for every H(u,v), its lower fourfold branch is the actual
global ground whenever

    12|u|+8|v| < sqrt(6)-2.

This is a sufficient local neighborhood, not a sharp phase diagram.
Outside it the hull is still exactly invariant, but a different
symmetry sector may become lower. Claiming a global ground there
requires comparing the omitted sectors.

## 5. What this adds and what it does not

The generated couplings do not require freezing a now-inappropriate
ground map, and they do not force a large block eigensolver at this
step. Their self-consistent finite-block response is an explicit
two-coordinate rotation. Both the original four-dimensional logical
factor and the exact source operator definitions are retained.

This is not yet a self-consistent renormalization fixed point. Boundary
channels must be recomputed for G(u,v); new inter-block virtual processes
can still produce other couplings, ranges and higher-body terms. The
physical register/graph/time selection, uniform long-chain control and
all T1-T8 closures remain unproved. No RH, factoring or complexity claim
is made by this finite result.

## 6. Executed verification

The checker passed 40 exact checks in normal Python and Python -OO,
with byte-identical JSON output. Tests include the source and dependency
pins, the explicit ten-word polynomial, common-hull rank and minimality,
full physical intertwining for symbolic u,v, the correct Gram metric,
the previous-G equality, branch discriminant and full unperturbed
characteristic polynomial. No numerical diagonalization or tolerance is
used in these acceptance checks.

One implementation check initially compared characteristic polynomials
with different SymPy symbol assumptions despite identical printed
variable names. It was corrected by using the polynomial's own generator;
a changed-polynomial negative control confirms the correction does not
weaken the spectral acceptance.
