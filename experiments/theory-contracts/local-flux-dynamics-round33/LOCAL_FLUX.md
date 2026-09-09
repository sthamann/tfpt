# Local electric control in the declared cubic family

2026-09-07. NON-RH / unpromoted. The parent is the original, unrotated
Round30 Hamiltonian, specialized as in Round31/32 to U(1), nearest-neighbor
A with hopping a=1/12, beta=1/4, eta=1/2, M>=4, kappa>0 and V_mag=0.
The full rotor Hilbert spaces and both fermion species are retained.
These model choices are not physical constants selected by TFPT.

## 1. A bounded force despite unbounded electric energy

For a link l write F_l=i[H,E_l]. Electric energies, M N_high, and the
backtracking part of beta A^2 commute with E_l. The remaining terms are
bounded, even, gauge-invariant fermion hoppings multiplied by unitary
link transporters. A Hermitian hopping between two distinct fermion modes
has norm one on the whole Fock space, not a norm growing with its size.
Its electric derivative has the same norm when the transporter contains
the link once, with exponent +1 or -1.

Per link the direct terms have norm sum a+2 eta a. A graph of degree at
most z has at most 2(z-1) nonbacktracking unoriented length-two paths
containing that link. Each contributes beta a^2; reverse paths form the
Hermitian conjugate, and backtracking has zero electric derivative.
Triangle inequality therefore gives the volume-independent bound

    ||F_l|| <= b_z = a(1+2 eta)+2(z-1) beta a^2.

For cubic boxes or tori (sides >=3), z=6 and b_6=53/288. For the separate
three-site cycle below, z=2 and b_2=49/288. These are conservative whole-
Fock force bounds from actual monomials. They do not replace the distinct
Schatten projector-derivative constants of Round31 without further proof.
For example, a force norm is not automatically a Sylvester source trace norm.

The bounded commutator gives, for every finite-electric-form-energy state,

    ||E_l exp(-itH)psi|| <= ||E_l psi|| + b_z |t|.              (1)

One obtains (1) on the finite-flux smooth core from the integral identity
for E_l U(t)-U(t) E_l and extends it by closure. In finite volume H is a
bounded perturbation of the electric Laplacian plus bounded fermionic
onsite terms; its commutator with E_l is bounded. This justifies domain
invariance used in the identity. For mixed states replace vector norms
by Hilbert-Schmidt norms of E_l rho^(1/2). No factor of total volume
occurs. No assumption about translation invariance during evolution is
needed if the initial bound is already uniform link by link.

## 2. Supply the initial moment for the actual filled-Haar state

For the inherited dressed filled-low Haar state, Round31 proved for every
cubic link

    <E_l^2(0)> = Tr(S_l^*S_l) <= 11/[384 delta^2],
    delta=M-9/16.

Its initial state and q_x=1 backgrounds are unchanged in this statement.
Combining with (1) yields

    <E_l^2(t)> <= (sqrt(11/384)/delta + (53/288)|t|)^2.        (2)

The checker replaces sqrt(11/384) by the outward rational upper bound
17/100. This is a local-energy premise derived for the stated preparation,
not extracted from a global average. It also holds near open boundaries
because their degrees and initial derivative costs are no larger.

For a specified set L of r links and integer K>=0, the commuting electric
spectral projections and Markov/union bounds give

    Prob(exists l in L: |E_l(t)|>K)
      <= min(1, r (sigma0+b_6 |t|)^2/(K+1)^2),               (3)

where sigma0=17/(100 delta). This excludes the concentrated initial-flux
sequence used in Round32's obstruction: that sequence does not satisfy
the small per-link initial moment assumed in (2).

## 3. What a local electric cutoff does to the dynamics

Let P_K impose |E_l|<=K only on the r specified links; all other rotors
remain untruncated. P_K commutes with the U(1) Gauss constraints and with
the diagonal unbounded electric Hamiltonian. Define H_K=P_K H P_K on
ran P_K by its self-adjoint compression. This must be the compression
of the complete parent, not a polynomial rebuilt from truncated link
operators. The distinction is explicit in CYCLE_DYNAMICS.md.

Only bounded terms involving the selected links contribute to P_K H Q_K.
Their total norm is <=r b_6 by the same path count. For a pure initial
state with the uniform moment sigma0, use normalized initial data
P_K psi/||P_K psi|| in the compressed dynamics. Set T=|t| and
p0=r sigma0^2/(K+1)^2<1. Projected Duhamel and (3) give

    ||P_K U(t)psi - exp(-itH_K)P_K psi||
      <= r b_6 sqrt(r)/(K+1) (sigma0 T+b_6 T^2/2).

Adding the final Q_K component and the initial normalization change
(1-sqrt(1-p))<=p<=p0 proves the full vector error bound

    d_K(T) = sqrt(r)/(K+1) [sigma0+b_6 T
                       +r b_6(sigma0 T+b_6 T^2/2)] + p0.     (4)

Every norm-one bounded observable then has expectation error <=min(2,2d_K).
Purification gives the corresponding mixed-state statement. This is a
comparison with a specified projected initial state, not an unannounced
change of preparation. The checker uses an integer upper bound on sqrt(r)
to retain exact rational acceptance arithmetic.

For r=6, M=400, kappa=1/100, T=1 and K=4096, the recorded union flux tail
is below 1.217e-8 and the conservative observable comparison is below
0.000420. The moment and force bounds, rather than kappa-independent
physical claims, determine these numbers. The r-link cutoff comparison
is uniform in the rest of the lattice's size, but leaves that rest fully
dynamical and infinite dimensional. It is NOT yet a finite-window solver.

## 4. Exact scope of the new local result

Equations (2)-(4) establish a previously missing local electric moment,
its propagation and a controlled partial electric truncation. They do
not remove high fermions, establish a many-body gap, or prove that a
Schrieffer-Wolff remainder is small on every linked cluster. A locality
bound is additionally needed to replace the rest of the infinite lattice
by a finite spatial window. We do not import one without deriving its
constants for this parent. Gauge observables involving unbounded E_l^2
are not covered by the norm-one observable guarantee in (4).

For the finite connected cycle, a bounded-interaction Dyson argument
below is far sharper than the moment-only cutoff estimate and permits
an actual fully evaluated real-time calculation.
