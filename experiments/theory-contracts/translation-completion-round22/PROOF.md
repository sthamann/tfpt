# Round22: positive continuous-translation completion of the common parent

2026-09-07. NON-RH. This is an explicitly CHANGED Hamiltonian on the SAME
full physical scalar/gravity/auxiliary/E8-charge Hilbert space of Round20.
It constructs a conserved continuous GLOBAL momentum. It is not a local
relativistic stress tensor, a derivation of microscopic TFPT, or a claim
that the unchanged interaction has passed the companion obstruction.

## 1. A continuous translation group with no extra degrees of freedom

Fix an ODD cubic side L>=3, N=L^3, signed Fourier labels
k_i in {-h,...,h}, h=(L-1)/2. Every one of the 35 canonical pairs/site of
the actual local parent is included. On these continuous variables define

    K_cont,i=sum_(species alpha,k) k_i a_alpha,k* a_alpha,k.

Unit-frequency reference oscillators suffice to define this operator.
It is the generator of spatial rotations of each real cosine/sine
canonical pair, independent of a common reference frequency on that
pair. It therefore also commutes with the physical scalar free Hamiltonian.
The three K_cont components are self-adjoint, strongly commute, and have
integer joint spectrum. Their unitary action linearly transforms ALL
continuous coordinates and momenta, preserving real fields and Schwartz
space. At a lattice step it is the actual spatial permutation. Odd L
avoids assuming a continuous real Nyquist convention for an even lattice.

On the entire infinite E8 charge carrier, let T_c,i translate all site
charges by one lattice step. Its N JOINT character projectors Pi_k have
infinite ranks; they are NOT a charge truncation. With the convention
T_c,i Pi_k=exp(-2pi i k_i/L)Pi_k, define

    K_c,i=sum_k k_i Pi_k,
    K_i=K_cont,i+K_c,i,
    U(theta)=exp(i sum_i theta_i K_i), theta in [0,2pi)^3. (1)

K_i are self-adjoint commuting sums on separate factors. U is a strongly
continuous representation of the three-torus, and U(-2pi e_i/L) is the
original simultaneous one-site translation. All eight total charges
commute strongly with U. The E8 Gram form, cocycle, frames and physical
charge multiplicities are not changed; no new field is added.

The old centered scalar momentum is NOT K_cont: its sin weights have been
replaced by signed Fourier labels. K_c is a bounded global translation
logarithm, not a local occupation derivative. Fractional U rotations need
not preserve the diagonal occupation algebra, consistently with Round21.
Physical momentum units are P_i=2pi K_i/(La).

## 2. Average the actual whole positive parent, not an isolated vertex

Let X=B_delta,eta(g,m)+D+V+L_J be the actual Round20 positive parent,
X>=e_m>0 for m>0. Here g,lambda,nu,J,delta,eta have their original
allowed ranges. Before its prescribed source-independent subtraction,

    q_X(psi)+E_fast||psi||^2=sum_z ||A_z psi||^2.       (2)

The A_z are the actual kinetic, mass, gradient and auxiliary-square
factors from the 35-pair parent, plus the full E8 charge factors and
sqrt(J)(I-U_e). For example, with B_E8*B_E8=G, charge-scalar factors can
be written sqrt(lambda/(2N))(B_E8 n_x)_a phi_x. The auxiliary residual
D E-Nu-h-g sigma(phi) is at most quadratic in continuous fields; the
other continuous factors are linear. No second positive model is appended.

Use the dense invariant core C of finite charge support with continuous
Schwartz factors. Define on C

    q_av(psi)=integral_T3 q_X(U(theta)*psi) dtheta/(2pi)^3. (3)

It follows immediately that q_av>=e_m||psi||^2. Averaging the ENTIRE
square is essential: changing a cubic term while keeping its old quartic
completion would not justify this lower bound. The constant E_fast is
averaged with weight one, neither multiplied by the number of samples
nor changed by a charge- or state-dependent subtraction. The constant
48NJ remains in physical hopping energy.

All charge-only D,L_J commute with K_c and are unchanged by (3). All
translation-invariant continuous quadratic terms are also unchanged.
Nonlinear gravity/scalar and scalar/charge interactions generally change,
already at their FIRST nonzero coupling order. In the gravity-decoupled
scalar/charge input, (3) changes only V and preserves H_m+D+L_J exactly.

## 3. A finite sum-of-squares algorithm and the quantum domain

The operation is finite and explicit at fixed L. Write on C

    U(theta) A_z U(theta)*=sum_r exp(i r.theta) B_z,r.

There are finitely many integer r. A charge operator has frequencies
k-l from its finite Pi_k/Pi_l decomposition, hence |r_i|<=2h regardless
of the size of an integer charge. Each continuous linear factor has
frequencies at most h; quadratic auxiliary factors have at most 2h.
The largest combined factors in (2) have |r_i|<=3h. Thus Parseval gives

    q_av(psi)+E_fast||psi||^2=sum_(z,r)||B_z,r psi||^2. (4)

This is a constructive finite Fourier-factor prescription, retaining all
charge configurations. Every B_z,r is closable: it is a finite sum of
polynomial differential operators and charge operators with finite
translation-projector insertions. Their adjoints are defined on C, which
they preserve. The finite sum of their squared graph norms is a closable
positive form on C. We choose its closure and subtract E_fast. Its
Friedrichs operator X_av is self-adjoint, X_av>=e_m, and has all-time
unitary dynamics. C is its FORM core by construction. We do not assert
essential self-adjointness of the new expression on an old operator core
or equality of its operator domain with Dom X.

This also gives a simple exact finite quadrature. Set M=6h+1. Every
frequency difference in a squared factor has |d_i|<=6h<M. Hence

    q_av(psi)=(1/M^3) sum_(j in {0,...,M-1}^3)
                    q_X(U(2pi j/M)*psi),              (5)

on C. No nonzero allowed frequency is a multiple of M. At L=3, M=7:
343 conjugated copies with weights 1/343 suffice EXACTLY. The old
three-point spatial sampling is NOT enough: it preserves frequency 3
and therefore retains precisely the unwanted reciprocal-lattice terms.
The equality (5) relies on the actual finite polynomial degree of (2),
not a claim that this quadrature works for every unbounded operator.

The raw number of Fourier blocks per square is at most (6h+1)^3; each
charge projector is itself a finite sum of N spatial translations.
The algorithm can be expensive and spatially global. It does not solve
the infinite-dimensional time evolution efficiently or provide a
volume-uniform domain/numerical error estimate.

## 4. Exact conserved total momentum, including full base and clock

U(alpha) C=C and the Haar shift in (3) gives q_av(U(alpha)psi)=q_av(psi).
This identity extends to the closed form and its domain; the associated
operator X_av consequently commutes strongly with U and the joint
spectral measure of K. Thus all three total momenta are exactly conserved,
not just at first perturbative order. Total U(1)^8 charge remains conserved.
The positive spectral gap gives sqrt(12X_av) and the old type of weighted
physical clock construction; K also commutes strongly with this square
root. This is a statement about the NEW positive base and its clock,
not about the old full off-shell constraint generator.

Kinematic finite-frame reduction is already taken in the physical Hilbert
space and is not undone. A corresponding action on its selected code is
obtained through the existing exact isometry; no native finite-range lift
of fractional translations is asserted. The native local observable net
and the old Gaussian/constraint-source limiting theorems are NOT
automatically inherited by X_av. They must be rederived for the changed
interactions before any such additional claim can be made.

## 5. A nontrivial retained interaction and a precisely removed one

In the certified charge band of the other two contracts, K_c chi_k=k chi_k.
For a scalar one-quantum exchange k,q -> l,r, averaging the original V
retains its exact matrix element if the SIGNED, unwrapped vectors obey

    k+q=l+r,

and removes it otherwise. The original lattice coupling only required
this equality modulo L. For the two actual positive-J resonances:

- Channel A has k+q=l+r=(1,-1,0), so its nonzero matrix element survives.
- Channel B has k+q=(-1,-2,0), l+r=(2,1,0), so its nonzero OLD matrix
  element is set to zero by (3). It differed by (3,3,0), not by zero.

There is therefore real scalar/charge exchange in X_av; this is not an
averaging that deletes the entire interaction. But it is demonstrably a
different Hamiltonian at order lambda, not a repair of the same one by
renaming its momentum. The checker enumerates all L=3 lowest-band,
scalar-number-preserving k,q,r channels: 19^3=6859 have no wrap and remain;
27^3-19^3=12824 wrapped channels are removed. This is a bounded sector
inventory, not the count of all vertices or a proof of continuum behavior.

## 6. What has and has not been solved

For the declared changed common parent, positivity, a closed quantum
realization, all-time dynamics, total charge and continuous global
momentum conservation are constructed on the same untruncated carrier.
They evade the original-model no-go because both its seed and its
interaction are changed explicitly. Existing scalar/gravity degrees of
freedom, including spectators, are retained rather than solved away.

The price is spatial NONLOCALITY and loss of the prescribed original first
vertices. A conserved global momentum does not yield a local symmetric
energy-momentum tensor, local gravity constraints, causal propagation,
Lorentz symmetry or a relativistic continuum. No parameter or interaction
selection by microscopic TFPT has been established. The old Gaussian
encoding and full source/observable-net limits remain unproved for X_av.
No T1–T8/TOE/RH or empirical promotion. This is a tested research alternative,
not an automatic replacement of the repository's current physical model.
