# Exact all-length operator structure of the primitive compiler chain

## 1. The alternating source is an existing gamma-matrix chain

Let a_i=i g_i be the four actual Hermitian source generators. In this
source basis a1,a2 are real and a3,a4 imaginary. The on-site unitary
C_minus=a3 a4 obeys C_minus conjugate(a_i) C_minus*=a_i; alternatively
C_plus=a1 a2 obeys C_plus conjugate(a_i) C_plus*=-a_i.
Apply either unitary on the even registers of the alternating open chain.
Every bond, including both orientations, then gives the exact identity

    U_minus H_source U_minus* = 2(n-1)I - (1/2)sum_j Omega_(j,j+1),
    U_plus  H_source U_plus*  = 2(n-1)I + (1/2)sum_j Omega_(j,j+1),
    Omega_(j,j+1)=sum_(mu=1)^4 a_(j,mu) a_(j+1,mu).

The second line matches the h=0 gamma-matrix exchange Hamiltonian with
J=1/2 in Eq. (2) of Siew, Chandrasekharan and Kaul, *Transverse Field
gamma-Matrix Spin Chains* (2024). The constant is our convention. Their
Eq. (4) also gives the staggered chirality sign transformation. This is
an exact operator identification, not merely a common symmetry.
[Primary paper, Eqs. (2)–(4)](https://arxiv.org/pdf/2406.04120).

The proof applies to every open length and to an even bipartite periodic
chain. One must not carry the staggered-sign argument over an odd
periodic cycle without examining its closing bond. No numerical phase
diagram or all-length gap theorem is established by the local identities
here. In particular this is not a newly discovered TFPT-specific chain.

## 2. Two conserved occupations with a correlated hopping sign

Define two independent Pauli triples directly from the original source:

    tau_x=a1, tau_y=a2, tau_z=-i a1 a2,
    sigma_x=tau_z a3, sigma_y=tau_z a4, sigma_z=-i a3 a4.

Each triple has the Pauli multiplication law; the two triples commute.
The checker constructs an explicit on-site unitary putting them in the
standard first/second-qubit basis, not just a formal abstract isomorphism.
The four original directions become

    a=(tau_x,tau_y,tau_z sigma_x,tau_z sigma_y).

Consequently the minus-sign uniform bond has the exact form

    2I - (1/2)[tau_x tau_x' + tau_y tau_y'
          + tau_z tau_z'(sigma_x sigma_x'+sigma_y sigma_y')].

It is two XX-type hopping species, with the sigma hopping multiplied by
the neighboring tau occupation parity. Both totals sum_j tau_z(j) and
sum_j sigma_z(j) are exactly conserved at every length. If occupation
n_tau=(1-tau_z)/2 and similarly for sigma, the tau hopping amplitude is
-1 while the sigma amplitude on j,j+1 is

    -(-1)^(n_tau(j)+n_tau(j+1)).

This supplies exact charge sectors for numerical or analytic work. It
does not decouple the two species.

## 3. A four-step obstruction to simply gauging away the interaction

On three sites consider the configuration square

    (tau=100,sigma=010) -> (010,010) -> (010,001)
                       -> (100,001) -> (100,010).

The four exact hopping amplitudes are -1,+1,-1,-1, whose product is -1.
The second hop changes sign because the first hop changed an occupation
at the shared endpoint. Under arbitrary diagonal phases assigned to the
configurations, phases cancel around a closed loop, so this product is
invariant. Two independent XX species with negative real hopping have
product +1 on this square. Thus no diagonal configuration-phase change
turns this hopping model into those independent chains in the same
occupation graph. This does not exclude non-diagonal dualities, constrained
representations, or more general methods of solving interacting models.

## 4. Spin(4), chirality and what is actually conserved

For all six pairs mu<nu define ell_(mu,nu)=(i/2)a_mu a_nu. Direct bond
identities show that sum_j ell_(mu,nu)(j) commutes with the chain. This is
the actual continuous Spin(4) Lie symmetry; full active U(4) is not
being asserted. The two occupation totals above are Cartan charges.

Chirality chi=a1 a2 a3 a4=-tau_z sigma_z anticommutes with each a_mu.
Each bond changes chirality at both endpoints. The global product of
chiralities is conserved, but the sum of local chiralities is not. Its
global parity is already determined by the two occupation parities.

## 5. What the direct Jordan-Wigner transformation really produces

Use the usual site-parity strings to define 4n Majoranas

    eta_(j,mu)=(product_(k<j) chi_k) a_(j,mu).

They obey canonical anticommutation relations. Since chi_j is the
product of that site's four eta operators,

    a_(j,mu) a_(j+1,mu)
      =eta_(j,mu) chi_j eta_(j+1,mu)
      =(-1)^(mu-1)(product_(nu!=mu) eta_(j,nu)) eta_(j+1,mu),

where the remaining nu are in their original increasing order. Each
exchange term is therefore a genuine **quartic**, not quadratic,
Majorana monomial. Different bond/direction supports are independent
Clifford monomials, so the quartic terms cannot cancel. Gaussian linear
Majorana rotations preserve the exterior degree and cannot remove this
nonzero grade-four interaction. This argument excludes the naive direct
Jordan-Wigner/free-Gaussian interpretation, not every conceivable
nonlinear representation. A separate full-spectrum test can ask the
stronger question about any unconstrained quadratic Fock-space model.

## 6. Genuine free subsectors, with their correct scope

If either species is completely empty or completely filled, its hopping
annihilates the sector and its same-species endpoint parity product is
+1. The other species is then exactly an ordinary open XX chain:

    H_sector=2(n-1)I-sum_j(c_j* c_(j+1)+c_(j+1)* c_j).

Its one-particle energies relative to the constant are
-2 cos(pi k/(n+1)), k=1,...,n; many-particle energies are sums over occupied
modes. The sine-wave formula follows by diagonalizing the open tridiagonal
adjacency matrix. These are exact invariant sectors at every length.

They are not the whole model. Already for three sites their lowest
energy is 4-sqrt(2), above the actual primitive ground 4-sqrt(6). The
checker verifies all four empty/filled-species embeddings explicitly.

## 7. Research significance and boundary

There is now a concrete known-model identification, an explicit local
two-species basis, six continuous symmetry charges and simple solvable
subsectors. The nontrivial component is the joint-occupation sector with
correlated hopping; a tiny gauge-invariant loop exposes it. Literature
on the actual gamma-matrix chain is therefore a relevant next resource,
while a bare claim of two decoupled free chains is not justified.

The register graph, equal primitive couplings and a Hamiltonian/time
interpretation remain conditional inputs. These operator identities do
not select a physical continuum, prove a uniform gap, or close T1-T8.

## 8. Executed verification

The checker passed 141 exact acceptance checks under normal Python and
Python -OO, with byte-identical JSON output. The scoped whitespace check
passed. It verifies original/dependency pins, both source-to-paper signs
on both bond orientations, the explicit local basis, all six symmetry
charges, occupation conservation, the nonremovable configuration-square
sign, canonical Majorana anticommutation and every three-site quartic
bond channel, plus four invariant free-sector embeddings. All numerical
tolerances and eigensolver approximations are absent from these tests.
The arbitrary-length statements follow from the displayed local
identities and ordered parity-string algebra, not from extrapolating a
few finite spectra.
