# A physical cycle resonance: average energy does not control every local readout

2026-09-07. NON-RH, unpromoted conditional research. This is an exact
counterexample to a proposed general inference, not a new TFPT parent or
a refutation of Round31's specifically prepared filled-Haar cubic states.

## 1. A full-rotor physical sector, not an arbitrary Fourier cutoff

Take two sites x,y and two parallel U(1) links oriented x to y. Both links
have full integer electric spectra and electric Hamiltonian
kappa(E1^2+E2^2)/2, with kappa=1/100 and no magnetic potential. Only link 1
carries matter hopping. Use one low/high fermion pair at each site and
the inherited signed-wall functional family

    h(A) = [[A+beta A^2, eta A],[eta A, M I]],
    A(z) = a [[0,z^-1],[z,0]],
    a=1/4, beta=1/4, eta=1/2, c=eta a=1/8.

These are declared diagnostic parameters, not inferred physical constants.
Here A^2=a^2 I. Let n>=400 be an integer and put

    D=kappa(n-1/2), M=D+1/64, Delta=M-1, lambda=1, g=1/2.

Fix one fermion, q_x=1,q_y=0 and the exactly conserved spectator flux
E2=n. The two Gauss operators are

    Gx=E1+E2+Nx-1, Gy=-E1-E2+Ny.

They force E1=-n for either species at x and E1=1-n at y. A hop x to y
raises E1 by one and lowers Nx by one, preserving both constraints. Thus
the physical invariant sector has exactly four states
(low_x,low_y,high_x,high_y). No electric truncation is imposed. Different
n are different allowed cycle-flux sectors, not states illegally inserted
into Round30's one-link sector. Vanishing hopping on link 2 makes E2
conserved; nonzero magnetic or second-link hopping would change the model.

Subtract the initial low_x energy E0=kappa n^2+1/64. The exact reduced
Hamiltonian is

    Hrel = [[0, a, 0, c],
            [a,-D, c, 0],
            [0, c, D, 0],
            [c, 0, 0, 0]].                                   (3)

The electric energy released on the first hop matches the high-sector
cost. Consequently low_x and high_y are resonant despite the large
potential-only band separation. This is an energy-transfer mechanism,
not an inference from a large off-diagonal matrix element alone.

## 2. A rigorous order-one local transition at fixed time

Use the resonant subspace R=(low_x,high_y) and its complement F=(low_y,high_x).
Then

    H_R=c sigma_x, H_F=[[-D,c],[c,D]], H_F^2=(D^2+c^2)I,
    ||H_F^-1||<=1/D, ||C_RF||=a.

Start with low_x. Write the exact evolved vector (r(t),f(t)), with f(0)=0.
Duhamel followed by integration by parts in the fast exponential gives

    ||f(t)|| <= (a/D)( ||r(t)||+||r(0)||+integral_0^t ||r'(u)||du )
             <= (a/D)(2+(c+a)t), t>=0,

because unitarity gives ||r||,||f||<=1 and ||r'||<=c+a. A second Duhamel
bound in R yields

    ||r(T)-exp(-iH_R T)r(0)||
        <= (a^2/D)[2T+(c+a)T^2/2].                            (4)

At the fixed time T=pi/(2c)=4pi, the ideal resonant vector is entirely
high_y. The classical strict bound pi<22/7 gives T<88/7 and reduces the
numerator of (4) to the exact rational upper bound 671/196. Hence

    <N_bare_high_y(T)> >= (1-671/(196D))^2 = p_n.               (5)

The assumed n makes the amplitude lower bound positive before squaring.
It follows that the right hand side tends to one as n and M grow. The
transition is not suppressed by increasing the potential-only gap.

## 3. Neither the readout nor the initial state need use bare band labels

Let Q be the high spectral projector of h(A), P=I-Q, and Qb the bare high
projector. Since ||A||=a, B0=a+beta a^2=17/64 and M>B0. Diagonalizing each
scalar 2x2 block of h(A) gives a mixing angle satisfying

    sin(theta(x)) <= |eta x|/(M-x-beta x^2),
    ||Q-Qb|| <= c/(M-B0) =: q_n = c/(D-1/4).                 (6)

All these projectors preserve the full Gauss constraints. If Pi_y is the
site projector on both species, the local dressed readout Q Pi_y Q obeys

    ||Q Pi_y Q - Qb Pi_y Qb|| <= 2 q_n.

It therefore has expectation at least p_n-2q_n at T for the bare low_x
input. In this two-site matter cell it is still a local gauge-invariant
observable, though it need not be supported on site y alone.

More strongly, prepare the **exactly low** physical initial state

    psi_n=P|low_x>/||P|low_x>||.

Its high occupation is exactly zero. From (6) and q_n<1,
||psi_n-|low_x>||<=sqrt(2)q_n<=2q_n. Unitarity preserves that distance,
so norm-one readouts differ by at most 4q_n for all times. Consequently

    <psi_n(T), Q Pi_y Q psi_n(T)> >= p_n-6q_n -> 1.            (7)

This excludes both a bare-band-label artifact and pre-existing order-one
high population. The excitation comes from locally concentrated electric
energy. The strictly low preparation is different from Round31's filled
constant-Haar construction and carries very large local electric energy.

## 4. Bounded global density can coexist with the resonance

Add empty spectator sites until the total number is N=n^2, connected by
a tree of gauge links to the two-site cell. Put all new fluxes and new
backgrounds to zero, all matter hopping on these links to zero, and retain
the same M at every site. This is a **connected gauge graph with an
inhomogeneous matter hopping graph**, not a homogeneous cubic matter
lattice. The spectator vacuum and zero fluxes are invariant. Equation (3)
and the local measurements are unchanged exactly; no huge N-site matrix
needs to be simulated to establish this tensor-factor restriction.

For the bare low_x preparation, E0/N=1/100+1/(64n^2). For the strictly low
preparation of (7), the cell electric operator is at most kappa n^2, and
||h||<=M+c because the norm of its diagonal part is <=M and its off-block
norm is c. Thus the conserved mean energy obeys

    <H>/N <= 1/100+(M+c)/n^2 -> 1/100.                        (8)

There is exactly one fermion in the entire graph, so the dressed high
number density is always <=1/N, tending to zero even as the local readout
in (7) tends to one. Explicit conservative lower enclosures at T=4pi are:

| n | Declared M | Strictly-low initial state's dressed local readout |
|---|---|---|
| 3200 | 51217/1600 | >0.7738 |
| 6400 | 102417/1600 | >0.8841 |
| 12800 | 204817/1600 | >0.9413 |

At n=12800, (8) is below 0.010000783 per site, while the high density is
at most 1/163840000. These are analytic enclosures, not observed numerical
transition probabilities. The checker uses only rational comparisons.

## 5. Precise obstruction and next premise

A gap of the matter Hamiltonian at fixed gauge coordinates, bounded global
energy per site, and initially zero high occupation do **not**, by
themselves, imply uniform suppression of every local high-sector readout
in this family. A low-only theory that discards this observable as zero
cannot approximate this experiment. This is not a proof that all possible
effective theories fail; a representation retaining the resonant sector
would describe different retained degrees of freedom.

This does not refute the Round31 bounds on volume-averaged high number:
those remain compatible with this example. Nor does the spectator
construction prove an obstruction for every homogeneous interacting 3D
lattice or its special low-energy states. It isolates the missing premise
in a proposed general argument from density alone.

For general nonhomogeneous states, a useful positive target is a bound on
local electric-energy moments or flux tails in the causal neighborhood of
the measured region, and propagation under the actual connected dynamics.
Such a premise would exclude the concentration above. It must be derived
for the claimed state, not inferred from a spatial average. There is also
a clean symmetry-based positive result for the homogeneous family below.

## 6. Positive local population theorem for homogeneous periodic lattices

Take the actual Round31 filled-low construction on a periodic cubic torus,
with every side length >=3, hopping 1/12, beta=1/4, eta=1/2, M>=4,
kappa>0, V_mag=0 and q_x=1 at each site. All electric rotors retain their
full Hilbert spaces, including cycle fluxes. This is a boundary-condition
specialization of the declared lattice family, not the spectator model.

Coordinate translations permute sites and oriented links, hence permute
the gauge coordinates, electric derivatives and fermion generators.
The Hamiltonian and Gauss background are invariant. Functional calculus
makes Q transform covariantly as well. The filled-low Slater vector may
acquire a fermionic permutation sign, but its density matrix, the constant
rotated Haar wave, and the original-frame encoded density matrix are all
translation invariant. Thus the exact evolved density matrix is invariant.

Define the gauge-invariant dressed population assigned to site x by

    n_H,x = dGamma(Q Pi_x Q).

This is a quasilocal readout associated with x, not the bare onsite high
occupation; Q has the spatial decay controlled in Round31. For the finite
lattice, sum_x n_H,x=dGamma(Q^2)=N_H. Transitivity and invariant evolution
therefore give the exact identity, for EVERY site and time,

    <n_H,x(t)> = <N_H(t)>/N = nu_H(t).                        (9)

More generally the expected sum over any set R is |R|nu_H(t). The positive
operator expectation in (9) is uniform locally without assuming independent
sites, truncating fluxes, or approximating the full dynamics.

The inherited filled-state energy calculation applies on this torus:
Tr A=0, Tr A^2=N/24, 3N electric links, and per-link derivative squared
Hilbert-Schmidt cost <=11/384. With delta=M-9/16 it yields

    energy/N <= 1/96+11 kappa/(256 delta^2),
    ebar = 49/96+11 kappa/(256 delta^2),
    <n_H,x(t)> <= min(1, ebar/M,
                     |t| (3/(8delta)) sqrt(6 kappa ebar)).    (10)

These are exactly the inherited density constants, now justified as local
population constants by the new symmetry step, not newly derived density
estimates. At kappa=1/100, the same outward bounds hold for every periodic
volume and site:

| Declared M | Local dressed high population upper bound |
|---|---|
| 4 | min(0.128, 0.0192 abs(t)) |
| 40 | min(0.0128, 0.0017 abs(t)) |
| 400 | min(0.00128, 0.00017 abs(t)) |

The checker verifies translations of both vertices and oriented link
variables on 3x3x3 and 3x3x4 tori, as well as the exact trace/energy costs.
The oriented-link bijections are the covariance witness for arbitrary
gauge coordinates; checking A only at U=1 would not suffice. The proof of
(9) applies to all the stated sizes by the coordinate translation formula.

The resonance example is not translation invariant, so it does not satisfy
this additional hypothesis. Open boxes are not transitive either: (9)
must not silently be transferred to their boundary sites. Finally, small
local high population is still not a comparison of every local observable
between full and low-only dynamics. Virtual interactions, phases and source
corrections can matter even at low population. Establishing that comparison
on the same homogeneous family, with appropriate local energy control and
consistent initial/source data, remains the next substantive step.
