# The same Bell block does not have a branch-independent bare refinement

12 September 2026. NON-RH. Conditional finite-dimensional model only.
Companion executable: `ternary.py`. Original source and note are hash-pinned;
neither original file was edited or executed as a module.

## Outcome in simple language

Expanding the left, middle, or right part of the same three-factor block
produces three different encodings. At local dimension four their overlaps
are exactly 17/20, not one. A phase or a logical change of basis cannot make
them identical. Keeping all three bare encodings in one common linear space
requires twelve dimensions, not four.

One can explicitly change the five-factor physical state to move between
the encodings. This is an available mathematical recoupling, not yet a
source-selected rule. Crucially, the fixed equal-weight Bell Hamiltonian
distinguishes the middle expansion from the two end expansions: its energy
expectation is larger by 9/40 for every logical input. No unitary preserving
that Hamiltonian can identify the middle and left encodings. Left and right
can instead be exchanged by physical chain reflection, which swaps the
marked endpoints.

This rules out a precise proposed shortcut, not all refinements, tensor
networks, Hamiltonians, or physical models. In particular, a different
encoding, a dressed low-energy band, or a coherently averaged tree rule is
not excluded. None is uniquely derived here from TFPT's original source.

## 1. Fixed model and factor labels

Let each factor have dimension d>1. Odd factors carry the fundamental
representation of U(d), even factors its conjugate. With

    Phi = d^(-1/2) sum_a |a,a>,
    Z = (Phi_12 tensor I_3 + I_1 tensor Phi_23)/sqrt(2(1+1/d)),

Z is the previously derived three-factor ground isometry. In the chosen
basis its entries are real, so conjugate(Z)=Z, but its placement on a
conjugate factor is retained explicitly. The three maps C^d -> (C^d)^tensor5
are

    L = (Z tensor I tensor I) Z,
    M = (I tensor conjugate(Z) tensor I) Z,
    R = (I tensor I tensor Z) Z.

This compares maps into the **same five labeled physical factors**. It is
not merely comparing unlabeled abstract Hilbert spaces of equal dimension.

## 2. General analytic contraction proof

Write an unnormalized diagram (ij)(kl);m for the map that contracts equal
output indices in pairs ij and kl and puts the logical input at output m.
Use output positions one through five:

    A=(12)(34);5, B=(14)(23);5, C=(12)(45);3,
    D=(23)(45);1, E=(25)(34);1.

The component formula

    Z_(ijk),a = (delta_ij delta_ka + delta_ia delta_jk)/sqrt(2(d+1))

directly gives

    L=(A+B+C+D)/[2(d+1)],
    M=(A+B+D+E)/[2(d+1)],
    R=(A+C+D+E)/[2(d+1)].

The Gram matrix of the five diagrams is the following scalar matrix
tensor I_d:

             [ d^2  d    d    1    d   ]
             [ d    d^2  1    d    1   ]
    G(d) =   [ d    1    d^2  d    1   ].
             [ 1    d    d    d^2  d   ]
             [ d    1    1    d    d^2 ]

To obtain an entry, identify indices forced equal by the two diagrams.
The logical input indices are always connected; every other connected
component contributes a free sum of d values. Thus entries are exactly
d^2, d, or 1. This proves the formula for every integer d>1; the finite
controls below are independent corroboration, not interpolation.

Consequently

    L*L=M*M=R*R=I,
    L*M=L*R=M*R=q_d I,
    q_d=(3d+5)/[4(d+1)],
    1-q_d=(d-1)/[4(d+1)]>0.

All adjoint-reversed overlaps have the same value.

## 3. Exact geometric consequences

The block Gram of the joined map [L M R] is

    ((1-q_d)I_3 + q_d 1_3 1_3^T) tensor I_d.

Its eigenvalues are 1+2q_d with multiplicity d and 1-q_d with multiplicity
2d. Both are positive. Hence the span of the three bare ranges has dimension
3d. This is the minimum linear space containing these specified ranges,
not a lower bound on every possible physical description or new encoding.

The ranges are pairwise distinct and have zero pairwise intersection. For
example Lx=Ry implies x=q_d y and y=q_d x, hence x=y=0. If a logical unitary
V satisfied L=RV, then L*R=V* would be unitary, contradicting q_d<1. Thus
neither a logical basis transformation nor global phase repairs the maps.

For every logical vector psi,

    ||(L-R)psi||^2 = (d-1)/[2(d+1)] ||psi||^2,
    ||(I-LL*)R psi||^2 = (1-q_d^2)||psi||^2.

| d | q_d | minimum common bare span | squared map mismatch | cross-range projection leakage |
|---|---|---|---|---|
| 2 | 11/12 | 6 | 1/6 | 23/144 |
| 3 | 7/8 | 9 | 1/4 | 15/64 |
| 4 | 17/20 | 12 | 3/10 | 111/400 |

At d=4 the joined Gram eigenvalues are 27/10 (multiplicity4) and 3/20
(multiplicity8). Projection leakage is a statement about changing these
encodings; it is not independently a physical dynamical loss rate.

## 4. Ambient recoupling exists, but it is not a logical phase

Let Delta=L-R. Since Delta*Delta=2(1-q_d)I, the operator

    U_LR = I - Delta Delta*/(1-q_d)

is a Hermitian unitary on the five-factor physical space: it is the
reflection I-2P_Delta. Direct contraction proves

    U_LR L=R, U_LR R=L, U_LR M=M.

It is the identity on the orthogonal complement of the Delta range. All
three encodings intertwine the same fundamental U(d) representation;
therefore Delta Delta* and U_LR commute with the global U(d) action.
No group-action incompatibility prevents this physical recoupling.

More generally the same construction swaps any two branches and fixes the
third. On the 3d-dimensional joined range these swaps implement permutations
of three independent encodings; on its orthogonal complement they are the
identity. This supplies finite three-branch recoupling, not all-level
associativity or a proof of coherence for overlapping larger refinements.

One may also define the coherent tree average

    T=(L+M+R)/sqrt(3(1+2q_d)),     T*T=I.

That is a valid new encoding. Choosing it is an additional rule, and its
agreement with further refinements or a physical parent has not been proved.

## 5. The fixed physical Hamiltonian distinguishes the trees

Keep the specified equal-weight five-site Bell parent

    H = sum_(j=1)^4 (I-P_(j,j+1)).

This is the existing conditional Bell interaction extended to four adjacent
edges, with no counterterm or reweighted middle link. In the five-diagram
coordinates its action is

         [ 2     -2/d   -1/d    0      -1/d ]
         [-1/d    3      0      0       0   ]
    h =  [-1/d    0      2     -1/d     0   ].
         [ 0     -1/d   -1/d    2      -2/d ]
         [ 0      0      0     -1/d     3   ]

This coordinate matrix need not be Hermitian in the Euclidean coordinate
metric because the diagrams are not orthonormal; the physical metric is G.
The checker independently applies each actual adjacent Bell projector to
all five finite diagram matrices and verifies the coefficient action.

For the specific Householder from section4 one obtains

    (U_LR H L - H R)* (U_LR H L - H R)
        = (d-1)/[2d^2(d+1)] I.

At d=4 this is 3/160 I, nonzero on every logical input. The simple
representation-preserving reflection is therefore not Hamiltonian-preserving.

This does **not** imply that no H-preserving L-to-R map exists: spatial chain
reflection Pi, reversing all five factors, exchanges L and R and fixes M.
It sends each P_(j,j+1) to P_(5-j,6-j), so Pi H Pi*=H. It also exchanges
the marked left and right endpoints and their observables.

The middle branch has a stronger obstruction. Full scalar compressions are

    L*HL=R*HR = [(d-1)(9d+10)]/[4d(d+1)] I,
    M*HM     = [(d-1)(5d+6)]/[2d(d+1)] I.

The middle-minus-left energy is

    (d-1)(d+2)/[4d(d+1)] > 0.

At d=4 the energies are 69/40 and 39/20, separated by 9/40. These are
expectations throughout the code subspaces, not assertions that the codes
are eigenspaces of H. If an ambient unitary V commuted with H and obeyed
V L=M Q for any logical unitary Q, their energy compressions would have to
agree. The different scalars make that impossible. Thus **no**
H-preserving ambient unitary identifies left and middle bare refinements
for this fixed equal-weight parent, even allowing a logical basis change.

The obstruction may be evaded only by changing some premise, such as the
encoding, parent, retained subspace, weights, or meaning of physical
identification. Such a changed construction needs a separate derivation.

## 6. Scope, verification, and debug disclosure

No original TFPT spacetime factorization, full active U(d), physical Bell
links, clock calibration, or continuum has been derived. The result concerns
the explicit conditional finite model in `interaction/COMPOSITION.md`.
No T1-T8 status is advanced; no RH mechanism is proposed.

The checker derives the general overlap and energy formulas symbolically
and independently checks d=2,3,4 using sparse physical matrices. All guards
are explicit exceptions. No dense d^5-by-d^5 Hamiltonian is diagonalized.

During construction, two symbolic checks compared factored and expanded
denominators structurally. Systematic debugging showed exact difference
zero and a deliberately shifted negative control -I. Both checks now test
the exact algebraic difference. An initial provisional energy-defect norm
omitted a factor d+1; a full diagram derivation corrected it before recording
the result, and independent physical-projector contractions corroborate
the corrected formula. No threshold or assumption was relaxed.

Final receipt: 211 exact checks in normal and `-OO` runs. The subprocess
comparison confirms byte-identical JSON outputs. Only the new
`ternary.py` and this note were edited by this worker.
