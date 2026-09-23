# Exact dynamical closure by retaining the pairing multiplicity

12 September 2026. NON-RH. Conditional five-site Bell model only.
Companion: `hull.py`. No original source, parent, weight, or physical factor
is changed. The enlargement is of the retained description inside the
already specified d^5-dimensional physical space.

## Outcome

There is an exact finite repair of the previous Hamiltonian leakage:
retain all five pairing configurations rather than the three chosen
refinement branches. For local dimension four this is a **20-dimensional
invariant space**, with an explicitly isometric encoding and a Hermitian
effective Hamiltonian that reproduces its physical evolution exactly.

This is the smallest H-invariant space containing the specified bare
branches; the left branch alone already forces all20 dimensions. The middle
branch and the coherent symmetric average each need12 dimensions, namely
the reflection-even sector. The average itself is not an energy eigenstate.

The repair is for the specified Bell Hamiltonian, not arbitrary physical
operations. One original local compiler generator already leaves the
20-dimensional space. Hence retaining pairing multiplicity solves this
finite dynamical closure problem, not universal observable closure, a
source-selection problem, continuum consistency, or any T1-T8 obligation.

## 1. Same five diagrams and same fixed parent

Use the previous unnormalized diagram maps C^d -> (C^d)^tensor5:

    A=(12)(34);5, B=(14)(23);5, C=(12)(45);3,
    D=(23)(45);1, E=(25)(34);1.

Here each pair imposes equality of its output indices, and the unpaired
site carries the logical input. Write the joined physical map as

    Dcal=[A B C D E].

The source-pinned diagram Gram and fixed equal-weight Hamiltonian action
satisfy

    Dcal* Dcal = G tensor I_d,
    H_physical Dcal = Dcal (h tensor I_d),
    H_physical = sum_(j=1)^4 (I-P_(j,j+1)),

with

         [ d^2  d    d    1    d   ]
         [ d    d^2  1    d    1   ]
    G =  [ d    1    d^2  d    1   ],
         [ 1    d    d    d^2  d   ]
         [ d    1    1    d    d^2 ]

         [ 2     -2/d   -1/d    0      -1/d ]
         [-1/d    3      0      0       0   ]
    h =  [-1/d    0      2     -1/d     0   ].
         [ 0     -1/d   -1/d    2      -2/d ]
         [ 0      0      0     -1/d     3   ]

The coefficient matrix h is not Euclidean-Hermitian, because these
diagrams are not orthonormal. It obeys the correct identity G h=h* G.

The leading principal minors of G are

    d^2,
    d^2(d-1)(d+1),
    d^2(d-1)^2(d+1)^2,
    (d-1)^4(d+1)^4,
    (d-1)^4(d+1)^4(d^2-2).

All are strictly positive for integer d>=2. Thus Dcal has rank5d; no
diagram multiplicity can be silently identified with another.

The local Bell-projector contraction rule reconnects a pair of adjacent
sites, with coefficient1 if the pair already occurs and coefficient1/d
otherwise. Each reconnection is again one of these five diagrams. Thus the
span is closed under the individual adjacent Bell projectors and their
generated algebra; the executable independently verifies the full fixed H
action using actual physical matrices at d=2,3,4.

## 2. Reflection decomposition and complete hull polynomial

Spatial reversal exchanges A with D and B with E, leaving C fixed.
Use the even basis (A+D,B+E,C) and odd basis (A-D,B-E). Then h decomposes as

    h_even = [[2,-3/d,-1/d],[-1/d,3,0],[-2/d,0,2]],
    h_odd  = [[2,-1/d],[-1/d,3]].

The sectors have physical dimensions3d and2d. The full five-multiplicity
characteristic polynomial is the product

    chi_even(E)=E^3-7E^2+(16-5/d^2)E-12+12/d^2,
    chi_odd(E)=E^2-5E+6-1/d^2.

The complete spectrum on the retained physical hull repeats each
multiplicity-space eigenvalue d times. This is a complete spectrum of this
invariant hull, not automatically the complete d^5-dimensional spectrum.

At d=4, independent exact factorization gives

    chi_h(E)=(4E-9)(4E^2-19E+20)(16E^2-80E+95)/256.

The five distinct energies in the retained hull are

    even: (19-sqrt41)/8, 9/4, (19+sqrt41)/8;
    odd:  (10-sqrt5)/4, (10+sqrt5)/4.

Each is fourfold. The lowest retained energy is (19-sqrt41)/8; no claim
about every outside representation sector follows from this calculation.

## 3. Minimal dynamical hulls, not just a convenient enlargement

Ignoring the common nonzero normalization, the previous L,M,R coefficient
vectors are respectively

    l=(1,1,1,1,0), m=(1,1,0,1,1), r=(1,0,1,1,1).

The Krylov matrix [l,hl,h^2l,h^3l,h^4l] has determinant

    -2(d+1)(d^2+4)/d^9,

which never vanishes for integer d>=2. L alone therefore generates all
five diagram multiplicities. Reflection gives the same result for R.
Consequently the smallest H-invariant hull of span{L,M,R} is exactly5d.

M is entirely even, with coordinates (1,1,0). Its three-column even Krylov
determinant is

    2(d+1)(d+4)/d^3 != 0.

The sum L+M+R is even with coordinates (3,2,2). Its corresponding
determinant is

    2(d+1)(14d+19)/d^3 != 0.

Both therefore fill the three-multiplicity even sector and neither is an
energy eigenvector. In particular coherent symmetrization does not make
the original d-dimensional code invariant under this H.

| Initial retained object | Minimal H-invariant dimension | d=4 |
|---|---|---|
| L alone | 5d | 20 |
| R alone | 5d | 20 |
| M alone | 3d | 12 |
| coherent average L+M+R | 3d | 12 |
| joint bare span of L,M,R | 5d | 20 |

The original joint bare span has dimension3d but is **not** the full even
sector: it contains two even multiplicities and one odd multiplicity.
Thus its dimension12 at d=4 must not be confused with the different,
invariant12-dimensional even hull of M or of the average.

## 4. Explicit isometric repair and exact intertwining

Since G is positive, choose the upper Cholesky factor C with G=C* C and
define

    J = Dcal (C^-1 tensor I_d),
    K = C h C^-1.

Then

    J*J=I_(5d), K*=K,
    H_physical J = J (K tensor I_d).

The last identity is actual operator intertwining, not matching spectra.
It implies for every real time t

    exp(-it H_physical) J = J exp(-it (K tensor I_d)).

No projection leakage occurs for that evolution. The entire diagram range
is invariant, so its orthogonal projector commutes with the selfadjoint
physical H. This repairs precisely the finite closure problem without
changing the parent, adding a compensating interaction, or inventing new
physical factors.

Cholesky orthonormalization is a convenient coordinate choice, not a
physical uniqueness principle. Any other orthonormalization gives a
unitarily equivalent K. The global U(d) representation on the retained
space is I_5 tensor U: the five-fold multiplicity carries the nontrivial
pairing dynamics, while this full-symmetry Hamiltonian acts as identity on
the d-dimensional fundamental label. It does not derive a nontrivial
logical four-state Hamiltonian by renaming multiplicity evolution.

## 5. The repair does not preserve unrestricted local compiler access

An exact extra control uses the actual source generator

    g1=i(X tensor I_2)

from the pinned compiler, applied to the first of the five d=4 factors.
It is unitary on the full physical space. Set O=g1 tensor I_(4^4),
M=G tensor I_4, and B=Dcal* O Dcal. Its off-hull leakage Gram, on the
unnormalized diagram coordinates, is

    R=M-B* M^-1 B != 0.

The checker verifies this exactly. The corresponding total squared
leakage summed over an orthonormal20-state hull basis is

    Tr(M^-1 R)=896/75 > 0.

This is a summed norm, not a per-state probability or a dynamical rate;
nonzero trace proves failure of invariance but does not claim every input
leaks. It is already enough to reject "the20-dimensional repair preserves
all source-marked local operations."

More generally, independent full matrix algebras M_d on all five factors
generate M_(d^5). Their only common invariant subspaces are zero and the
whole physical space. Thus no proper retained hull can preserve that
unrestricted operation set. A reduced theory must state which operations
are retained, compressed, or represented through a changed access map.
The Bell-Hamiltonian repair by itself does not supply such a universal map.

## 6. Verification and limits

The general proof uses exact Gram minors, reflection blocks and nonvanishing
Krylov determinants. Independent d=2,3,4 controls form the actual physical
diagram maps, compute exact Cholesky encodings, and verify J*J=I as well as
H_physical J=J(K tensor I_d) with the original local Bell-projector helper.
The local marked-operation control is actual d=4 source data, not a random
unitary. No full d^5-by-d^5 matrix diagonalization is used.

During implementation, systematic debugging isolated three implementation
issues: characteristic-polynomial generators dropped a real-symbol
assumption; the original projector helper accepted d columns rather than
5d; and a matrix-only simplifier was passed a scalar. The fixes canonicalize
the polynomial variable, apply the unchanged helper in d-column blocks,
and use scalar simplification. No mathematical target was relaxed; a
shifted-polynomial negative control remains present.

Final receipt:86 exact checks in normal and `-OO` runs; subprocess comparison
confirms byte-identical JSON. Only the new hull.py and this note were edited. The
original conditional carrier, graph, full U(d) symmetry, energy unit, and
physical interpretation are still premises. No all-level refinement law,
continuum, gravity, matter selection, or T1-T8 completion is inferred.
