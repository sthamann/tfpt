# Virtual Hamiltonian and observable reduction in the physical Gauss cell

2026-09-07. NON-RH, unpromoted conditional research. All energies and times
are in the declared model units, with hbar=1. This is the actual Round30
one-fermion Gauss sector, not an arbitrary electric-flux cutoff.

## 1. Fixed input and the remaining coupling

Use the pinned Round30 fixture, kappa=1/100 and backgrounds (q_x,q_y)=(1,0).
Gauss law forces the four electric fluxes (0,1,0,1). Write V0=V(z=1) and

    H = V0^* (h(z=1) + kappa diag(0,1,0,1)/2) V0
      = H0 + B,
    H0 = diag(L,D), B = [[0,C^*],[C,0]].

The positive electric compression gives D >= (31/12)I and L <= (3/2)I.
Thus gamma=13/12 separates these ordered blocks. Direct calculation gives
C^*C=(9 kappa^2/400)I, hence c=||B||=||C||=3/2000.
This gamma is a bound for this physical four-dimensional Hamiltonian's
diagonal blocks. It is not a many-body or continuum mirror-gap theorem.

## 2. Exact Sylvester solution and controlled virtual term

Solve D X-X L=C. Ordered spectra give the convergent integral

    X = integral_0^infinity exp(-u(D-a)) C exp(u(L-a)) du,
    ||X|| <= c/gamma = b = 9/6500,

with a between the spectra (the integrand is independent of a). The exact
rational solution is

    X = [[2616759, 6113709],[-6092541,-2614491]] / 7749971776.

Set S=[[0,X^*],[-X,0]], so S^*=-S, ||S||=||X|| and [H0,S]=-B.
Our convention is ad_S(A)=[A,S]. Expanding exp(-S)H exp(S) and using that
last identity at every order yields the absolutely convergent identity

    exp(-S)H exp(S)
      = H0 + sum_{k>=1} k/(k+1)! ad_S^k(B)
      = H2 + R_H,
    H2 = H0 + [B,S]/2.

In particular its low block is

    L2 = L - (C^*X + X^*C)/2.

The high block is D+(CX^*+XC^*)/2. Both are Hermitian and the second-order
Hamiltonian is block diagonal. The virtual term is nonzero and retained.
Since ||ad_S(A)||<=2b||A||, the omitted Hamiltonian obeys

    ||R_H|| <= c (exp(2b)-1-2b)
             <= 2 c b^2/(1-2b)
             = 243/42133000000 < 5.768e-9 =: numerical upper enclosure.

In the sequel epsilon_H denotes the exact fraction, not its decimal.
The rational comparison follows from 2b<1 and 1/k!<=1/2 for k>=2.
It deliberately uses the cancellation with H0; estimating each uncancelled
H0 commutator separately would lose this sharper bound.

Unitary Duhamel gives, for every real t,

    ||exp(-itH)-exp(S)exp(-itH2)exp(-S)|| <= |t| epsilon_H.       (1)

The diagonal correction has norm <=cb, leaving an ordered gap at least
gamma-2cb>0. Weyl's inequality therefore matches the two low eigenvalues
of H with those of L2 to absolute error <=epsilon_H. Independent rational
Sturm isolations in the checker improve the two particular enclosures to
1.39e-13 and 2.138e-12. The analytic bound, not those particular small
errors, is the reusable statement.

This uses the Schrieffer-Wolff idea, but is derived here with these explicit
matrices and remainders. Background: Bravyi, DiVincenzo and Loss,
[Schrieffer-Wolff transformation for quantum many-body systems](https://arxiv.org/abs/1105.0675)
(2011). Their bounded-spin many-body results are not automatically results
for unbounded electric rotors or this project's physical continuum.

## 3. The observable and preparation must travel with the Hamiltonian

Let J embed the two low coordinates and W=exp(S)J. For any normalized low
vector psi, prepare the original physical state V0 W psi. For an original
observable O_original, use O=V0^* O_original V0 in the present frame and

    O_low = J^* exp(-S) O exp(S) J,
    O2 = J^*(O+[O,S]+[[O,S],S]/2)J.

For ||O||<=1 the omitted source terms obey

    ||O_low-O2|| <= (2b)^3/[6(1-2b)]
                  = 243/68466125000 = epsilon_O.

This follows from the same commutator series and 1/k!<=1/6 for k>=3.
Equation (1) now gives the expectation comparison

    | <exp(-itH)W psi, O exp(-itH)W psi>
      - <exp(-itL2)psi, O2 exp(-itL2)psi> |
        <= 2 |t| epsilon_H + epsilon_O.                        (2)

At |t|=1 the right hand side is 4131/273864500000 < 1.509e-8.
No state-normalization approximation is hidden: W is exactly isometric.
O2 need not be exactly a positive contraction, but is within epsilon_O of
one whenever the original observable is a positive contraction.

For the gauge-invariant site occupation Ny=diag(0,1,0,1), the checker records
the complete rational L2 and O2 matrices. In particular the correction to
the (0,0) entry of the compressed readout is nonzero. Its magnitude minus
epsilon_O is over 1000 times the bound in (2) at t=1. Thus retaining only
the Hamiltonian correction while silently using the bare compressed
readout fails even at t=0 for the encoded preparation.

Conversely, (2) is NOT a tiny-error guarantee for the old undressed input
J psi. Its transformed boundary data are exp(-S)J psi and generally contain
a high component of order b. For an unchanged arbitrary initial state,
(1) remains valid if BOTH blocks of H2, the entire transformed initial
state, and the entire transformed observable are retained. That is an
accurate block dynamics representation, not a low-only theory. One must
either control the initial slip or justify the encoded preparation.

## 4. Independent rational real-time check

The checker does not accept floating-point diagonalization as evidence for
(2). For an anti-Hermitian matrix A, a Taylor polynomial P_m(A) has the
unitary integral remainder bound

    ||exp(A)-P_m(A)|| <= ||A||^(m+1)/(m+1)!.

Absolute row/column sums supply rational norm enclosures. Degrees 8,36,36
for S,-iH,-iL2 give exact Gaussian-rational matrices. With
F=P_36(-iH) P_8(S)J, compare the full 2x2 source matrix

    F^* O F - P_36(-iL2)^* O2 P_36(-iL2).

Its rational absolute-row upper bound, plus all polynomial tail budgets,
bounds the error uniformly over every normalized low psi at t=1. The
result is at most 361297/250000000000000 = 1.445188e-9. The separately
bounded Taylor contribution is below 1e-18. This is an enclosure, not a
measured probability or a claim that the true error saturates it.

The source matrix is expanded to canonical Gaussian-rational entries
before checking Hermiticity: unevaluated but equal conjugate products
must not be confused with an actual non-Hermitian remainder.

## 5. What is and is not solved

This supplies a reproducible, source-consistent finite-cell effective
Hamiltonian, local readout, encoding, energy bound and real-time bound.
It improves the earlier bare-compression/Feshbach calculation without
changing its underlying physical Gauss cell. It does not derive that cell
or its parameters from the complete TFPT compiler, make it chiral, select
its state, or extend (2) uniformly to all interacting lattice volumes.
The global-density shortcut for that last extension is examined separately
in [LOCAL_ENERGY.md](LOCAL_ENERGY.md).
