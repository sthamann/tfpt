# Round22: a controlled moving-charge band on the full E8 carrier

2026-09-07. NON-RH. This uses the actual Round20 Hamiltonian, with the
explicit allowed choice nu=0, total charge p=e2 of energy e(p)=1, and a
fixed odd cubic lattice. The concrete momentum test uses L=3, N=27.
No charge cutoff, frozen-position approximation or new hopping law is used.

## 1. An isolated eigenspace before hopping

On the full fixed-total-charge space use

    D=(1/N)sum_x e(n_x),  H_c(J)=D+48NJ I+J K,
    K=-sum_(positive edges,8 basis channels)(U_e+U_e*),
    ||K||<=b=48N.

The physical constant 48NJ is retained; only the resolvent calculation
uses H_tilde=D+JK. D has compact resolvent and its original diagonal
domain; K is bounded and self-adjoint. All cocycle signs are unchanged.

The positive even E8 lattice has e(n) an integer, zero only at n=0.
Thus in total charge p, the minimum is e0=1/N, attained exactly by the N
configurations |x> having p at x and zero elsewhere. Every other
configuration has D>=2/N. The gap is exactly Delta=1/N: p=e2 can be
split into e3 and e2-e3 at distinct sites, both of energy one.
This argument includes all integer configurations, not an enumerated box.

On this eigenspace, the FULL K compresses to negative cubic adjacency.
Only the p basis channel can move |x> to another one-charge configuration;
its actual cocycle coefficient is +1. All seven other channels and all
dipole-producing terms still act into the complementary Hilbert space.
They are not erased from H_c. On |k>=N^(-1/2)sum_x exp(2pi i k.x/L)|x>,

    <k|K|k>=-2 sum_i cos(2pi k_i/L).                    (1)

The one-charge eigenspace is NOT invariant under full hopping. The
checker explicitly retains its nonzero leakage into higher configurations.

## 2. Exact eigenvectors at genuinely positive hopping

Fix a joint character k of all three charge translations. At J=0, e0
is a simple isolated eigenvalue in that character space. On the circle
|z-e0|=Delta/2, the resolvent norm is at most 2/Delta. Set

    eps=J b/Delta=48N^2 J,    0<=eps<=1/32.             (2)

The resolvent identity/Neumann series gives an analytic rank-one Riesz
projection P_k(J) and

    ||P_k(J)-P_k(0)||<=rho=2eps/(1-2eps).

Projection rank stays one because rho<1. Choose the normalized vector
chi_k(J)=P_k(J)|k>/||P_k(J)|k>|| with positive overlap. Then

    ||chi_k(J)-|k>||<=dvec=2rho=4eps/(1-2eps)<=2/15.   (3)

These are exact eigenvectors in the infinite charge Hilbert space,
analytic in J. They belong to Dom D, since H_tilde is a bounded
perturbation of D. The whole lowest cluster has N eigenvalues, one per
translation character, and remains separated from the rest by at least
Delta-2Jb. Proper cubic rotations intertwine the character spaces, so
E_k(J)=E_(Rk)(J) EXACTLY, not just to first order.

For clarity, the elementary Neumann proof is all that is used here.
General isolated-eigenvalue perturbation theory is discussed by
[Wahl](https://arxiv.org/abs/1910.08460). No weighted/random-operator result
from that paper is assumed for this model.

## 3. Dispersion with an explicit error, not a projected surrogate

Let epsilon_k be the eigenvalue of H_tilde. Bounded perturbation gives
|epsilon_k-e0|<=Jb. Eliminating the complement of |k> within its character
space is legitimate: its compressed operator minus epsilon_k is bounded
below by Delta-2Jb. The exact Schur equation therefore yields

    |E_k(J)-[e0+48NJ-2J sum_i cos(2pi k_i/L)]|
       <=J^2 b^2/(Delta-2Jb).                          (4)

This quantifies an actual moving-charge band with all virtual charge
configurations retained. It is not an efficient full eigenvector solver,
a quasiparticle interpretation for every charge state, or a uniform
continuum dispersion theorem. The bound (2) scales as N^(-2); the
absolute constant 48NJ remains part of all physical energies and clocks.

There is also a directly certified NONFLAT band, not just a formal slope.
For L=3 and 0<J<=Delta/(4b^2)=1/181398528, the error in (4) is at most
J/2. The shell-3 and shell-0 eigenvalues therefore differ by at least
9J-2(J/2)=8J>0. This smaller interval is contained in (2). On the larger
interval (2), the coarse error bound alone is not claimed to resolve every
band splitting; exact cubic equalities and the form-factor bound still hold.

## 4. A nonzero interaction form factor despite its unbounded source

For an integer wave vector h define the diagonal, generally unbounded
operator

    F_h=sum_x exp(2pi i h.x/L) e(n_x).

Pointwise |F_h(n)|<=sum_x e(n_x)=N D(n), so Dom D is sufficient.
At J=0, if h=l-k modulo L, <l|F_h|k>=1. The eigenvector equation gives

    ||D chi_k||<=|epsilon_k|+Jb<=1/N+2Jb,
    ||F_h chi_k||<=1+2eps,   ||F_h*|l>||=1.

Using (3) on the two sides, WITH this graph bound rather than pretending
F_h is bounded, gives

    |<chi_l|F_h|chi_k>-1|
       <=dvec(2+2eps)<=11/40,
    |<chi_l|F_h|chi_k>|>=29/40.                         (5)

For N=27 the explicit certified positive interval is

    0<J<=1/1119744.

It is conservative and in the declared dimensionless energy units.
No empirical value of J is inferred. Formula (5) is uniform in the finite
list k,l but not in N. It supplies the NONZERO exact matrix element needed
by the companion positive-J resonance proof, instead of extrapolating a
truncated charge calculation to an infinite Hilbert space.

## 5. Scope and reproducibility

The checker applies the full projective hopping inventory to a genuine
finite-support input vector without wrapping output charges, reconstructs
the one-charge compression and its leakage, verifies the full cubic
Fourier dispersion, and checks every rational resolvent/form-factor bound.
An analytic argument, not the finite examples, proves all-charge isolation.
This establishes a finite-volume band and a certified interaction window
for nu=0 and total root charge p. Larger J, arbitrary nu, the neutral
sector, full gravity, chirality and a relativistic continuum are not
automatically covered. No T1–T8/TOE/RH or empirical promotion.
