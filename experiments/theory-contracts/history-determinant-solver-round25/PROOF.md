# Round25: exact linear-time block elimination for the original charge history

2026-09-07. NON-RH. This supplies an executable exact-arithmetic solver
for a given charge history at the Round24 finite time regulator. It does
not enumerate or sample the infinite charge histories, change their
cocycle signs, or claim a bit-complexity/physics breakthrough.

## 1. Open-chain factorization retains every time-dependent block

In one omitted cell, let d=(ell-1)^3, t=1/delta, T>=3 and
A_j=2t I+delta B_j, B_j>=b I. Remove only the wraparound temporal
off-diagonal blocks -tI from M, leaving the diagonal unchanged. Call
the open matrix O. It is positive and at least delta b I because its
time Laplacian retains Dirichlet endpoint diagonals.

Its exact block LDL* pivots are

    D_0=A_0,
    D_j=A_j-t^2 D_(j-1)^-1, j=1,...,T-1.           (1)

Every pivot is positive (indeed >=delta b I by Schur minimization).
The subdiagonal of L is -t D_(j-1)^-1. Block multiplication proves
O=L diag(D_j) L*. Therefore det O=product_j det D_j. To solve O x=f,

    y_0=f_0, y_j=f_j+t D_(j-1)^-1 y_(j-1),
    z_j=D_j^-1 y_j,
    x_(T-1)=z_(T-1), x_j=z_j+t D_j^-1 x_(j+1).    (2)

The order is essential for matrices B_j that do not commute in time.
The implementation uses exact rational/symbolic algebra in the checks;
a floating-point stability/error theorem is not supplied.

## 2. Restore periodic time exactly, not approximately

Let U inject two d-dimensional vectors at time 0 and T-1, and

    R=[[0,-tI],[-tI,0]], F=O^-1 U, Q=U*F,
    H=I_(2d)+R Q.

Then M=O+U R U*, and the determinant lemma and an explicit multiplication
give

    det M=(product_j det D_j) det H,
    M^-1 f=O^-1 f-F H^-1 R U* O^-1 f.              (3)

Both M and O are positive, so H is invertible and det H>0. H need not
be symmetric: do not silently replace RQ by QR inside the solve or take
individual logarithms of unexamined eigenvalues. The determinant ratio
is included in the scalar Gaussian factor det(M)^(-1/2), along with
the original (2pi) normalization. Ignoring the periodic correction gives
a different determinant and response even for constant charges.

For a retained source f=mathcal C* s, (3) computes the exact induced
action s*M_SS*s/2-f*M^-1*f/2. No full Td-by-Td inverse is required.
The [finite-memory theorem](../moving-history-memory-round25/PROOF.md)
can then bound a temporal truncation while keeping this determinant.

## 3. Actual charge updates include decreases as well as increases

At a fixed time slice, a physical hop can change two scalar diagonal
entries by delta times 2u times the signed energy differences. If V is
this small diagonal matrix and E injects the affected coordinates, then

    M_new=M+E V E*,
    det M_new/det M=det(I+V E* M^-1 E).             (4)

Negative entries in V are not clipped. The final charge energies remain
nonnegative, so the new physical matrix is positive and the determinant
ratio remains positive. Formula (4) neither changes nor incorporates
the separate projective hopping amplitude; that original phase must be
multiplied exactly as before.

The regression uses actual E8 root p=e2 and the old neutral hop action:
(2p,0,-2p) -> (p,p,-2p). A compensating retained-site charge keeps total
charge zero. The affected fast-site energy differences are -3 and +1,
so for u=1 the stiffness update is (-6,+2), NOT two positive increments.
The old cocycle phase and conservation are checked, and a dense direct
determinant is compared to (4). Reversing the hop reciprocates the ratio.

## 4. Cost, verification and boundaries

Factorization, the 2d endpoint right-hand sides and their small correction
cost O(T d^3) arithmetic operations per spatial cell. A new single right-
hand side costs O(T d^2) after factorization; storage is O(T d^2).
For (L/ell)^3 cells multiply these costs by the cell count. These improve
the generic dense O(T^3 d^3) arithmetic count of Round24 without changing
the exact time-regulator problem. Computing all entries of M^-1 still has
quadratic output size in T and is not claimed linear-time.

Exact rational bit lengths grow with T and charge magnitude; arithmetic
operation count is not a bit-complexity or fixed-precision stability bound.
The checker compares the recursive output to separately assembled dense
matrices, determinants and solves, including noncommuting physical blocks,
periodic closure and signed physical charge updates. Synthetic band
examples supplement, not replace, the actual eight-site scalar cell.

This solves the conditional finite-history Gaussian algebra, not the
infinite charge-history sum, sign cancellations, real-time unitary
evolution or a continuum limit. All g!=0 non-Gaussian gravitational
terms remain outside the construction. No T1-T8/TOE/RH promotion.
