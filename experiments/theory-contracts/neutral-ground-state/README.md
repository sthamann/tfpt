# Neutral ground-state representations of the fixed parent

2026-09-08. **NON-RH / unpromoted mathematical theory experiment.**
General existence argument with exact finite controls; no proof-assistant
certificate, unique vacuum, numerical infinite-lattice ground state or TOE.

## What is established, and what is not selected

The SAME uncut compact U(1) parent admits locally normal, translation-
invariant neutral ground cluster states obtained from periodic finite-volume
ground states. Each supplies a strongly continuous unitary implementation
of the already-constructed dynamics. On the cyclic Hilbert space of the
neutral physical observable algebra its generator is nonnegative and
annihilates the cyclic vector. This is an existence construction, not an
assumption of a previously supplied invariant state.

The construction uses the variational ground-state prescription and a
subsequence of periodic volumes. Neither uniqueness nor independence of
boundary prescription or subsequence is shown. No assertion that TFPT's
compiler selects this prescription or one particular state is made.
Positive energy on the charged field algebra, a bulk spectral gap, purity,
Lorentz symmetry, chirality, continuum dynamics and spin two remain open.

The old preparation with one low fermion per cell and E=0 is NOT a ground
state. A bounded local gauge-invariant unitary strictly lowers its energy.
It is also not stationary. Consequently the old q49/q50 readouts remain
responses from that specified preparation, not vacuum predictions.

## 1. Fixed Hamiltonian, neutral sector and finite-volume existence

Retain a=1/12, eta=1/2, beta=1/4, kappa=1/100, M=4, Vmag=0,
epsilon_L=1/96 and the full integer electric spectrum. Use cubic tori of
side L>=5, without magnetic or hopping modifications. One cell owns its
two fermion modes and three positively oriented outgoing links. A torus
has N=L^3 cells and 3N links. Its original Gauss generators are

  G_x = n_L,x+n_H,x-1 + div_x E.

On the joint neutral sector G_x=0, summing Gauss over the torus gives
N_L+N_H=N. This is a physical restriction, not a chemical-potential fit.
The E=0, all-low product vector belongs to this sector, so it is nonempty.

H0=kappa sum E_l^2/2+epsilon_L N_L+M N_H is self-adjoint with compact
resolvent on each finite torus: below any finite electric energy there
are finitely many integer flux vectors, and the fermionic space is finite.
The original interaction V is bounded and self-adjoint. Every hopping
commutes with all G_x, so the neutral sector reduces H0 and H=H0+V.
Bounded perturbation preserves self-adjointness, a lower bound and compact
resolvent, also on this reducing subspace. Thus the neutral Hamiltonian
has a lowest eigenvalue and a nonzero finite-dimensional ground eigenspace,
WITHOUT imposing an electric cutoff.

Let rho_L be the normalized spectral projection onto that ground eigenspace.
It is a normal, stationary neutral state. The projector commutes with the
torus translations because the original Hamiltonian and neutral restriction
do. No unique eigenvector or symmetry-breaking choice is presumed.

## 2. Uniform coercivity and the missing regularity estimate

For one directed hopping T=U^p c_a^*c_b with distinct modes a,b,

  T^2=(T^*)^2=0,
  (T+T^*)^2=n_a(1-n_b)+n_b(1-n_a).

Hence ||T+T^*||=1 on the whole Fock/rotor space. A Hermitian pair with
coefficient w costs |w|, not twice that value. There are, per torus cell,
three nearest-neighbor edge groups of weight a(1+2eta)=1/6 and fifteen
two-step pairs of weight beta a^2=1/576. Therefore

  ||V_L|| <= v N,      v=1/2+15/576=101/192.

The operator inequality and variational product-state upper bound in the
neutral sector are

  H_L >= epsilon_L N + kappa sum E_l^2/2 +(M-epsilon_L)N_H-vN,
  E0,L <= epsilon_L N.

In rho_L these imply

  kappa/2 <sum E_l^2> +(M-epsilon_L)<N_H> <= vN.

Translation invariance converts this global estimate into a uniform LOCAL
bound, without replacing an extensive bound by an unproved local one:

  <sum_(a=1..3) E_(x,a)^2> <= 2v/kappa = 2525/24,
  <n_H,x> <= v/(M-epsilon_L) = 101/766.

These bounds are deliberately conservative. They are not predictions
for the actual ground-state densities. The energy lower bound per cell
epsilon_L-v=-33/64 establishes stability of the neutral finite-volume
family; it is not a negative-energy excitation in the eventual GNS space.

## 3. Locally normal subsequential thermodynamic states

Identify each fixed finite cell box X with the corresponding interior of
large tori. Its reduced density matrices rho_(L,X) have local electric
second moment at most C|X|, C=2525/24. Let P_R be the finite-rank projection
onto |E_l|<=R on its 3|X| owned links, with all local fermions retained.
Then

  Tr rho_(L,X)(1-P_R) <= C|X|/(R+1)^2.

P_R has rank 4^|X|(2R+1)^(3|X|). The projection is a compactness device,
NOT a modified Hamiltonian or simulated flux truncation. The trace-norm
distance between rho and P_R rho P_R tends uniformly to zero; for example
the elementary bound 2 sqrt(p)+p suffices, where p=Tr rho(1-P_R).
The projected matrices lie in a bounded finite-dimensional set.
Thus the local density matrices form a relatively compact trace-norm set.

Take nested finite boxes exhausting the lattice and a diagonal subsequence
L_j so the reductions converge in trace norm on every box. Their limits
are positive, trace one and consistent under partial trace. They define
a locally normal state omega on the FULL bounded quasi-local rotor/CAR
algebra of `observable-dynamics`, not merely on its norm-continuous part.
This avoids relying on sequential weak-* compactness of a nonseparable
full B(H) algebra or on a possibly singular weak-* limit.

Translation symmetry and neutrality pass on fixed local bounded operators.
For each local gauge unitary exp(i theta G_x), omega(exp(i theta G_x))=1.
The electric moment bound passes by finite spectral truncations and lower
semicontinuity; equality or convergence of the unbounded energy moments
is NOT assumed. An infinite-volume ground energy density has not been
numerically evaluated or obtained by exchanging unbounded limits.

## 4. Same dynamics, stationarity and strong GNS implementation

The existing dynamics proof also applies to these periodic approximants.
The incidence and support-CARDINALITY bounds are identical. For an interior
observable, every fixed connected coefficient agrees with the infinite
lattice once its entire neighborhood lies away from the torus seam.
Wrap-around couplings never enter those coefficients. The uniform tails
and the already-proved finite-step composition argument give convergence
to the SAME alpha_t, uniformly on compact time intervals. No new bulk
dynamics or periodic long-range interaction is introduced in the limit.

One may extend a torus density to the quasi-local cell algebra by an even
product density outside its cell box; fixed interior reductions do not
depend on this extension. Neutrality is needed only on fixed interior
Gauss operators before taking the limit. Boundary embeddings are not
claimed to preserve an infinite-lattice Gauss constraint at the seam.

Finite-volume stationarity, local trace-norm convergence and norm convergence
of alpha_t^L(A) imply omega(alpha_t(A))=omega(A). For quasi-local evolved
operators use a fixed local norm approximation first, rather than evaluating
an unknown state on a moving infinite-support object.

In the GNS representation define

  U_t pi(A)Omega = pi(alpha_t(A))Omega.

Stationarity and the group law make this a unitary group on the cyclic
space. Crucially it is STRONGLY continuous even on the full field algebra:
for local A, alpha_t(A)-alpha_t^0(A) tends to zero in norm by the earlier
connected-series bound, while alpha_t^0(A) is strongly continuous on its
finite-support Hilbert space. Local normality therefore gives continuity
of omega(A^*alpha_t(A)) at zero. The identity

  ||(U_t-I)pi(A)Omega||^2
    =2 omega(A^*A)-2 Re omega(A^*alpha_t(A))

proves strong continuity on a dense set, hence everywhere. Stone's theorem
provides a self-adjoint generator K. This does NOT turn the earlier
operator-NORM continuity failure of U or Wilson loops into a false success:
strong continuity in a state representation is a different property.

For the operator-algebra/GNS framework see
[Rainer Verch, Lecture Notes, Section 1](https://arxiv.org/html/2507.00900v1).
The local regularity estimate and same-parent state construction above
are the additional model-specific inputs supplied here.

## 5. Positive energy on the physical observable space, not all charges

Let B_phys be the norm closure of bounded LOCAL gauge-invariant observables.
It includes local Wilson loops, bounded electric functions, occupations
and gauge-invariant matter transporters. It need not be restricted to A_c.
Every original hopping and the free evolution preserve gauge invariance.
Consequently every finite connected source coefficient starting from a
physical local observable is again physical and local. The finite-step
approximation tower retains that property, so B_phys is invariant under
alpha without a norm-continuity assumption for gauge orbits of arbitrary B(H).

For local A in B_phys and large tori, A preserves the complete neutral Gauss
sector. If rho_L is supported on its lowest energy E0,L, then

  f_(L,A)(t)=rho_L(A^*alpha_t^L(A))
            = integral_[0,infinity) exp(i t lambda) d mu_(L,A)(lambda),
  mu_(L,A)(R)=rho_L(A^*A) <= ||A||^2.

This follows directly from the spectral theorem for H_L-E0,L on the
neutral sector, and remains true for a degenerate ground mixture. The
functions converge to f_A(t)=omega(A^*alpha_t(A)); the latter is continuous
by Section 4. Positive definiteness and nonnegative spectral support pass
to the limit. For example test against inverse Fourier transforms of
smooth compactly supported functions of lambda in (-infinity,0); their
integrals vanish at every L and pass by the uniform bound on |f_(L,A)|.
The explicit exp(+it lambda) convention here fixes the energy sign.

Consequently the GNS generator on H_phys=closure(pi(B_phys)Omega) obeys

  K_phys >= 0,       K_phys Omega=0.

No norm-generator assumption for Wilson loops is used in this spectral
argument. Local Gauss unitaries fix Omega and commute with B_phys, hence
act identically on H_phys. The constructed space is physically neutral.
The generator is a GNS energy relative to its ground state, not a proven
convergent operator sum of the infinite unrenormalized energy density.

Charged fields can leave the neutral sector. Minimizing only inside that
sector does NOT imply positive energy for those other sectors. Thus K on
the full field GNS space is self-adjoint, but K>=0 there is not asserted.
Nor is a positive GAP, a unique zero eigenvector or a relativistic vacuum
inferred from K_phys>=0.

## 6. Exact rejection of the old preparation as a vacuum

Let Omega_bare be the all-low E=0 product vector. Its finite-torus mean
energy is N/96. H produces 6N mutually orthogonal high-particle/low-hole
states, each with hopping amplitude magnitude 1/24. Thus

  Var_(Omega_bare)(H)=6N(1/24)^2=N/96 > 0.

Nonstationarity also has a strictly local witness: the t^2 coefficient of
the high occupation at an interior site is 6(1/24)^2=1/96, although its
initial value is zero. The full cubic first action is executed on 125
cells/375 links, with all 6000 original directed hopping monomials.

More strongly, pick one directed nearest L-to-H transporter T with
chi=T Omega_bare normalized. It is gauge invariant and preserves the
neutral sector. The actual two-vector compression of the FULL Hamiltonian
onto Omega_bare,chi is

  [ E_bare,       w          ]
  [ w,            E_bare+D  ],
  w=1/24,    D=M-epsilon_L+kappa/2=9587/2400.

For the normalized vector proportional to Omega_bare-(w/D)chi, the energy
decrease is EXACTLY

  dE=w^2 D/(D^2+w^2)=239675/551523414
     approximately 0.0004345690389855325.

This vector is obtained by the bounded local gauge-invariant unitary
exp[-theta(T-T^*)], tan(theta)=w/D. Other original hopping terms have zero
matrix elements within these two vectors; they have not been removed
from the Hamiltonian. The exact cubic execution checks this compression.
Therefore the bare infinite product state fails the local ground-state
variational condition as well as stationarity.
These energy comparisons are quadratic-form calculations on vectors with
finite electric support. They do not place the rotor-containing unitary
in a norm-generator domain or differentiate its time orbit in operator norm.

On even tori, place this rotation on a perfect matching of disjoint edges.
The rotations are even and commute on disjoint supports. Unused links stay
in E=0; any hopping that uses one has zero expectation. A nonbacktracking
two-step path cannot use two matching edges, so its expectation also
vanishes, without deleting it from H. The energy density of this explicit
variational family is

  epsilon_L-dE/2 = 90003169/8824374624
                 approximately 0.0101993821471739.

An independent four-cell/two-dimer control retains all cross-dimer and
two-step interactions and checks this cancellation exactly. This is a
trial-state upper bound, NOT the exact ground energy or a state-selection
theorem. The compactness proof needs only the weaker bare upper bound.

## 7. A fully certified finite ground-state control

The complete neutral sector of the original edge has six states; Gauss
fixes their electric values, with no imposed flux cutoff. Its original
6x6 integer Hamiltonian is reconstructed. All six eigenvalues are isolated
by exact characteristic-polynomial arithmetic and independently bracketed
by rational LDL inertia at both endpoints.

The lowest energy is enclosed near 0.01996381643983592, below the bare
edge energy 1/48. A rational ground-ray approximation and a spectral
leakage certificate give true edge-ground intervals approximately

  high density:             [0.0001089054888, 0.0001089109378],
  electric second moment:   [0.0002176950225, 0.0002177004715].

These displayed intervals are rounded outwards; the exact rational
endpoints in validation.json are authoritative. The ray's weight outside
the true edge ground is at most 1.86e-18. Its coefficients, norms, energies,
all eigenvalue intervals and inertia pivots are stored for full replay.
No finite-edge gap, state vector or density is promoted to the cubic bulk.
In particular no finite-volume torus ground state has been diagonalized.

There is also a concrete check of the charged/neutral distinction: removing
the root low fermion maps this six-state neutral sector to the complete
four-state charged sector. The true neutral edge ground has a strictly
negative value of <c_L^*(H_charged-E0)c_L>, certified using the rational
ground ray, its spectral error bound and the full charged Hamiltonian.
Thus positive neutral-ground energy cannot simply be extended to the
charged field algebra, even on the original edge. This is not claimed
as a computed sign for the unknown full-cubic ground state.

## Reproduction and remaining work

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/neutral-ground-state/checker.py --output experiments/theory-contracts/neutral-ground-state/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/neutral-ground-state -p 'test_*.py'
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/neutral-ground-state -p 'test_*.py'
```

Finite controls check the constants, original Hamiltonian, variational
witnesses and spectra. The infinite-volume argument is in Sections 1-5;
it is not replaced by finite tests or Boolean fields in a result record.
The subsequence construction does not give an algorithmic convergence
rate, an explicit bulk state or uniqueness. Next: control the state/phase
and its excitations, test charged-sector stability separately, and justify
any compiler/vacuum selection before pursuing continuum and chiral claims.
Existing q50 remains unchanged and is not a vacuum readout. Theory
experiments only; no paper, website, ledger, verification, scorecard,
commit or push promotion and no T1-T8 completion claim.
