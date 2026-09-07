# Round25: uniform finite Euclidean memory for genuinely moving charges

2026-09-07. NON-RH. Use the ORIGINAL g=0 scalar/charge parent, the cell
boundaries and finite Euclidean time regulator of Round24. No torus
averaging, charge truncation, frozen profile, slow-motion assumption or
small-J assumption is made. This is a conditional Gaussian-kernel theorem,
not a real-time theorem for the full interacting charge-history sum.

Throughout a>0, m>0 and u>=0. The positive retained scalar mass is needed
for the positivity margin and the normalized Gaussian comparison below;
the massless case is not included in those statements.

## 1. Dominate every history by one massive temporal Green function

Fix delta>0, T>=3 periodic time slices and any finite integer charge
history n_x(j). In one omitted cell of d=(ell-1)^3 sites, put

    B_j=(-Delta_a+m^2+2u e(n(j)))_FF >= b I,
    b=m^2+12 a^-2 sin^2(pi/(2ell))>0,
    M_jj=2/delta I+delta B_j,
    M_j,j+1=M_j+1,j=-I/delta, including the periodic edge.

Let G=M^-1 and define alpha>0 and q in (0,1) by

    cosh(alpha)=1+delta^2 b/2, q=exp(-alpha).

Then EVERY time block obeys the dimension-free operator-norm estimate

    ||G_jk|| <= g_T(j-k),
    g_T(r)=delta/(2 sinh(alpha))
               * (q^r+q^(T-r))/(1-q^T), 0<=r<T.       (1)

Proof: write M=D-A with D block diagonal and A the nonnegative temporal
adjacency times I/delta. Each ||D_j^-1||<=(2/delta+delta b)^-1. The
block-row norm of D^-1 A is at most 2/(2+delta^2 b)<1. Its Neumann
series converges. Taking norms of each ordered product bounds it by the
scalar walk series for (delta^-1 L_cycle+delta b I)^-1. Summing the
infinite-line solution and its periodic images gives (1). Noncommuting
B_j at different times cause no difficulty: their order is never changed.

This argument requires NO upper bound on charge magnitude, derivative
of a profile, hopping rate J, cell count or spatial volume. Each finite
history has finite matrices; the constants are uniform over such histories.
This avoids a condition-number estimate that deteriorates at large charges.

## 2. A finite-memory approximation with an explicit error

Retain blocks of G at cyclic time distance at most R, 0<=R<floor(T/2),
and set the other blocks to zero; call the symmetric matrix G_R. It is
not assumed positive just because it was obtained by masking G. The
block Schur test and (1) give

    ||G-G_R|| <= tau_R,
    tau_R=delta/sinh(alpha) * q^(R+1)
                          /[(1-q)(1-q^T)].           (2)

There are at most two blocks per nonzero cyclic distance. Equivalently
the omitted residues r=R+1,...,T-R-1 give twice a finite geometric sum;
extending it to infinity yields (2). If R>=floor(T/2), no blocks are
omitted and the error is zero. Do not use an infinite-line kernel without
its periodic images.

For all cells together let C=A_SF, ||C||<=c=6/a^2, and
mathcal C=delta I_T tensor C. The exact and approximated retained kernels
are K=M_SS-mathcal C G mathcal C*, K_R=M_SS-mathcal C G_R mathcal C*.
The cell direct sum does not multiply (2) by the number of cells. Hence

    ||K_R-K|| <= epsilon_R=delta^2 c^2 tau_R,
    K>=delta m^2 I,
    K_R>=delta(m^2-e_R)I, e_R=epsilon_R/delta.         (3)

Choosing R so that e_R<m^2 therefore preserves a positive Euclidean
Gaussian kernel. This gives finite memory in the QUADRATIC SCALAR part,
NOT an instantaneous Hamiltonian or a finite-memory determinant. The
spatial support remains that of the original cell
elimination, at most (3ell-4)a.

For every retained scalar history s, the EXACT eliminated determinant
is used in both weights. If I and I_R are these two unnormalized
conditional weights, their action error satisfies

    |log(I_R(s)/I(s))| <= e_R ||s||_delta^2/2,
    ||s||_delta^2=delta sum_j ||s_j||^2.              (4)

The determinant is not approximated by masking its inverse; the companion
solver evaluates it exactly. Bound (4) grows with total field norm. It is
not a uniform relative bound for arbitrary unbounded fields or a signed
sum over histories.

After additionally integrating the retained scalar variables for ONE
fixed charge history, let Z_R,Z be the corresponding Gaussian factors.
For eta=e_R/m^2<1 and D=T|S|,

    |log(Z_R/Z)| <= D/2 * [-log(1-eta)].             (5)

Indeed the relative kernel perturbation K^-1/2(K_R-K)K^-1/2 has norm
at most eta, so all eigenvalues of K^-1/2 K_R K^-1/2 are in [1-eta,1+eta].
This is an extensive bound (or a bound per space-time coordinate), not a
volume-independent relative partition-function claim. Retained Gaussian
covariances also obey ||K_R^-1-K^-1||<=epsilon_R/
[(delta m^2)^2(1-eta)]. No reflection positivity is inferred for K_R.

## 3. Physical time scale survives regulator refinement

The constants above do not force memory to grow to infinite PHYSICAL
time as delta decreases. At fixed beta=T delta and h=R delta with
0<h<beta/2, along the allowed integer sequences,

    alpha/delta -> sqrt(b),
    lim e_R = c^2/b * exp(-sqrt(b)h)/(1-exp(-sqrt(b)beta)). (6)

Thus a prescribed positive-kernel accuracy can be obtained by a finite
physical memory h, subject to the finite circle length (or by retaining
the whole finite circle). For example b=4, delta=3/4 gives q=1/4 exactly.
At T=9,R=3,c=6,m=1 the bound e_R is strictly below 1/10.

Equation (6) is the limit of the PROVED BOUND, not a construction of the
continuum path integral or its charge sum. It does not justify exchanging
infinite charge sums with time/volume limits. Exponential decay in
Euclidean time does not imply exponential decay in real time: even a
single massive oscillator has oscillatory real-time response.

## 4. Determinant memory is retained, and its mixed response is bounded

The determinant is still a functional of the WHOLE charge history. Its
exact recursive evaluation is not a proof that its temporal dependence
can be discarded. Nevertheless its response to separated changes has a
controlled decay. For scalar stiffness potentials v_i,v_k at time-site
coordinates i=(j,x), k=(l,y), M changes by delta v_i |i><i|, and

    d_i d_k log det M = -delta^2 G_ik G_ki,
    |d_i d_k log det M|<=delta^2 g_T(j-l)^2.          (7)

The inverse derivative identity dG=-G(dM)G proves this for every real
positive physical matrix; no commutation of temporal blocks is used.
For two finite potential changes a_i,a_k whose entire interpolation
rectangle retains the lower bound B_j>=b I, double integration gives

    |log det M_(a_i,a_k)-log det M_(a_i,0)
       -log det M_(0,a_k)+log det M_(0,0)|
         <=delta^2 |a_i a_k| g_T(j-l)^2.             (8)

Positive potential changes automatically meet that hypothesis; signed
physical changes require all interpolated potentials nonnegative.
For two positive changes the mixed log-determinant difference is
nonpositive. The induced charge ACTION contains +1/2 log det M, whereas
the log Gaussian WEIGHT contains -1/2 log det M: their signs differ.

The mixed response decays at twice the Green-function exponential rate,
with its periodic images. It still carries the update magnitudes and
their number on summation. Thus (8) is not a uniform full-history
determinant truncation bound for unbounded charge jumps, nor a solution
of cancellations in the charge-history sum.

## Scope and next obligation

The moving-history SCALAR KERNEL memory is now controlled at the declared
regulator, uniformly over arbitrary charge jumps and density. The
determinant additionally has the magnitude-weighted response bound (8).
No J=O(N^-2) condition enters THIS conditional result. This does not remove
that condition from the different Round24 full-real-time comparison.
Full charge-history dynamics, its cancellations/sign problem, microscopic
selection, full g!=0 gravity, relativistic stress and chiral matter remain
open. No T1-T8/TOE/RH or empirical promotion.

See the [exact determinant/solve algorithm](../history-determinant-solver-round25/PROOF.md)
and the [Round24 original local construction](../local-gaussian-elimination-round24/PROOF.md).
[Molinari](https://arxiv.org/abs/1210.8001) gives primary-source context on
block-matrix inverse decay. Here the bound is derived directly by ordered
walks, using only the lower mass bound, rather than importing a result
requiring a bounded spectral condition number.
