# Round24: exact spatially local elimination with retained memory and determinant

2026-09-07. NON-RH. This acts on the ORIGINAL local g=0 scalar/charge
parent, not the globally averaged alternative. Here g denotes gravity;
write lambda_N=N u, u>=0. All integer charge variables and their original
hopping/cocycle are retained. Only selected continuous SCALAR coordinates
are integrated out. Other free continuous species factor unchanged.

## 1. Keep the cell boundaries: an exact finite-range construction

Let ell>=2 divide L and keep every site having at least one coordinate
equal to zero modulo ell. Call this retained set S. The omitted F is
a union of DISCONNECTED interior cubes, each of side ell-1. There are
(L/ell)^3 cubes, each with (ell-1)^3 scalar variables. No new variables
are introduced. For L=9, ell=3, N=729, this retains 513 and removes 216
scalar coordinates. It does not remove 216 charge modules.

For a static charge profile n, the scalar stiffness is

    A=-Delta_a+m^2 I+2u diag(e(n_x)) >=m^2 I.

In particular its diagonal contains the full 6/a^2, EVEN at an omitted
site next to S. A_FF is a Dirichlet block, not the graph Laplacian obtained
by deleting its boundary edges. Its exact uniform lower bound is

    A_FF>=b_* I,
    b_*=m^2+12 a^-2 sin^2(pi/(2ell)).                (1)

The potential is nonnegative for every integer charge magnitude. The
Dirichlet box eigenvalues prove (1), not an enumerated charge box.

At Euclidean frequency omega, put B=A_FF and C=A_SF. Gaussian elimination
is EXACT and gives the retained kernel

    K_eff(omega)=A_SS+omega^2 I-C(B+omega^2 I)^(-1)C*,
    K_eff(omega)>=(m^2+omega^2)I.                    (2)

The inequality follows by minimizing the full positive form over F.
The correction connects two retained sites only when they border the
SAME omitted cube. Its support diameter is at most (3ell-4)a (the old
nearest-neighbor part is also retained). This is finite spatial range
independent of total L at fixed ell,a, not a polynomial tail from global
momentum filtering. Keeping only isolated coarse points would not give
this disconnected-interior argument; the retained boundary faces matter.

## 2. The determinant and the time dependence are physical output

For a finite positive Gaussian block matrix M with retained vector s,

    integral df exp[-(s,f)^T M(s,f)/2]
       =(2pi)^(dim F/2) det(M_FF)^(-1/2)
             exp[-s^T(M_SS-M_SF M_FF^-1 M_FS)s/2].   (3)

The determinant depends on the charge profile. The derivative of LOG det
with respect to a diagonal matrix entry is (M_FF^-1)_(x,x)>0 (a physical
potential with an additional delta coefficient carries that factor too).
The determinant CANNOT be dropped
as a source-independent normalization, absorbed into the preassigned
E_fast, or replaced by a fitted mass term. Both the covariance kernel
and this induced charge weight are part of the exact elimination.

For a static profile, a controlled local-in-time approximation is available:

    K_eff(omega)=K_0+omega^2 Z+R(omega),
    K_0=A_SS-CB^-1 C* >=m^2 I,
    Z=I+CB^-2 C* >=I,
    R(omega)=-omega^4 C B^-2(B+omega^2 I)^(-1) C*,
    ||R(omega)||<=omega^4 ||C||^2/[b_*^2(b_*+omega^2)]. (4)

This identity holds for all real Euclidean omega; a small relative error
requires low frequency. It keeps the induced kinetic matrix Z, not just
the static Schur complement. The two-derivative model has a positive
canonical realization using Z^(1/2) and Z^-1/2 K_0 Z^-1/2, but it is an
APPROXIMATION to the frequency-dependent kernel. Spatial locality of every
canonical square root is not automatically inferred from finite-range Z.

At real spectral frequency E with E^2<b_*, continuation of the finite
matrix identity gives K_eff(-E^2)=K_0-E^2 Z+R_E, where
||R_E||<=E^4 ||C||^2/[b_*^2(b_*-E^2)]. This is a kernel/resolvent-level
estimate below the eliminated threshold, not a full nonlinear scattering
or real-time norm error theorem. The bound ||C||<=6/a^2 may be used.

## 3. Moving charges: exact at the specified Euclidean time regulator

Do not replace positive hopping by a frozen charge profile. At a finite
Euclidean time slicing, resolve the ORIGINAL hopping factors in the
integer charge basis. For ANY resulting charge history n_x(j), the scalar
integral remains Gaussian. With time step delta>0 and periodic time index j,
its matrix is

    M[n]=delta^-1 Delta_time,positive tensor I
             +delta blockdiag_j[-Delta_a+m^2+2u e(n_x(j))].

Temporal edges join only the same spatial site. Hence M_FF[n] is still
block diagonal by SPATIAL cube, each block now including every time slice,
and M_FF[n]>=delta b_* I. Equation (3) integrates each cube EXACTLY for
that history, retaining all temporal memory, charge-dependent determinants
and the full original transition amplitudes/cocycle signs outside it.
Arbitrarily large integer charges only raise the scalar diagonal; they
are not cut off or wrapped into a finite register.

In the resulting action, retained sites at different times couple only
if they border the same cube. Determinants are also products over cubes,
but depend on their complete charge histories. These statements do NOT
make the charge path sum a positive probability measure: original hopping
phases remain. Nor does the finite-matrix identity justify interchanging
infinite history sums with time/volume limits without further estimates.

For nonstatic histories the scalar block is not diagonal in temporal
Fourier frequency. Formula (4) is NOT silently applied to those histories.
The exact memory kernel is the available result; a time-local approximation
for genuinely moving, finite-density charges needs its own control.

## 4. Cost and claim boundary

At T time slices, each omitted block has dimension T(ell-1)^3. A generic
dense exact solve costs O(T^3(ell-1)^9) per cube and stores O(T^2(ell-1)^6)
entries; spatial cube count is (L/ell)^3. This does not solve the infinite
charge-history sum, its sign problem, or a thermodynamic/continuum limit.
Sparse methods can improve implementation cost but are not assumed here.

This is constructive scalar elimination preserving finite spatial support,
with a positive kernel, the indispensable determinant, exact time-regulator
history treatment and a controlled STATIC low-frequency truncation. It
does not supply a local-in-time Hamiltonian for all moving charges for
free, nor recover the Round22 continuous additive momentum. The original
discrete symmetries remain the starting point.

The [finite-density preparation result](../finite-density-background-round24/PROOF.md)
controls one extensive-charge/extensive-scalar family with a nonzero mass
shift; it is not substituted for the missing general history estimates.
Full g!=0 gravity makes the scalar action non-Gaussian and is NOT integrated
by (3). No chiral/TOE/T1-T8/RH or empirical promotion.

For background, [Dusson-Sigal-Stamm](https://arxiv.org/abs/2105.02058)
discuss Schur/Feshbach maps. Here the block identities and constants are
derived directly for the stated scalar lattice; that paper's spectral
perturbation results are not assumed to solve the interacting charge problem.
