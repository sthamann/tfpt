# All-observable dynamics of the fixed parent, and its continuity boundary

2026-09-08. **NON-RH / unpromoted mathematical theory experiment.**
This is a model-specific derivation plus executable algebraic controls,
not a proof-assistant certificate, peer-reviewed theorem, continuum QFT,
or solution of T1-T8. No TFPT parameter or preparation selection is added.

## Result and exact scope

For the SAME compact U(1) lattice parent used by `all-electric-majorant`,
the finite-volume Heisenberg maps converge in norm on every bounded local
observable. Their limits extend to a group of *-automorphisms alpha_t of
the full bounded quasi-local rotor/CAR algebra, for every real t. The
volume limit is uniform on compact time intervals. This includes both
fermion species, bounded electric functions and rotor shifts; the old
high-field source is the restriction of this same limit.

There is an important negative result: alpha is NOT point-norm continuous
on that full algebra. The uncut rotor shift U gives an explicit escaping-
flux counterexample, which persists with the original interactions.
An analogous gauge-invariant plaquette Wilson loop witnesses the same
obstruction inside the neutral Gauss sector, not only for charged fields.
The maximal point-norm continuous subalgebra equals that of the free
onsite dynamics. On this proper, invariant C*-subalgebra the restricted
group is C0 and has a dense smooth generator domain. The subalgebra is
not norm dense in the larger algebra and does not contain U.

This resolves the group/composition question for the declared lattice
model with its correct continuity qualification. It does NOT construct
a global Hamiltonian in a selected physical representation, choose a
vacuum, prove positive energy in that representation, or supply the
chirality, continuum, spin-two or compiler-selection bridges.

## 1. The original Hamiltonian and local algebra

Keep a=1/12, eta=1/2, beta=1/4, kappa=1/100, M=4 and Vmag=0.
The onsite energies are epsilon_L=1/96, epsilon_H=4, with ambient degree
six retained at a boundary. H0 also contains kappa sum_l E_l^2/2 on the
FULL integer electric spectrum. V is the original sum of bounded, even
fermionic hopping monomials w U^p c_a^* c_b. No hopping or E branch is
discarded, and no effective Hamiltonian replaces the parent.

For bookkeeping put the three positively oriented links starting at x
and the two fermion modes at x in cell x. The CAR local inclusions are
graded: odd operators at different cells anticommute. Every interaction
is EVEN and therefore commutes with every disjoint local operator,
including odd ones. No three-dimensional Jordan-Wigner replacement by
an ordinary on-site tensor hopping model is assumed.

For finite X, the rotor part is ALL bounded operators on its finite-link
Hilbert space, together with the finite CAR algebra. Let A be the norm
completion of the union of these finite-support algebras. In particular,
local strong operator integrals belong to the chosen local algebra;
membership in a smaller rotor Weyl algebra is not silently presumed.

A hopping footprint includes both fermion endpoints and every vertex of
its one- or two-step transporter. It has at most three cells, diameter
at most two. It can overestimate the actual cell support, which is safe.
The exact complete directed incidence at one cell is:

| Type | Directed terms | Sum of absolute coefficients |
|---|---:|---:|
| nearest L-L | 12 | 1 |
| nearest L-H | 12 | 1/2 |
| nearest H-L | 12 | 1/2 |
| nonbacktracking two-step L-L | 90 | 5/32 |
| total | 126 | J=69/32 |

Here the ninety two-step terms include those whose INTERMEDIATE vertex
is the chosen cell. Omitting that vertex would invalidate this argument.
The counts also follow by translation incidence: the one-step row weight
at one origin is 1, with two vertices per term; the two-step row weight
is 30/576=5/96, with three vertices. Thus J=2+3(5/96).
Every directed monomial is paired with its adjoint, with identical
footprint. Grouping such pairs gives bounded self-adjoint interactions;
using the directed absolute sum is a valid norm upper bound.

Compatible finite volumes retain H0 unchanged and include every original
interaction whose footprint lies inside the volume. For comparison on
all of A, extend each finite-volume evolution by FREE onsite evolution
outside its interacting volume. These extended maps alpha_t^Lambda are
isometric automorphism groups on A, without postulating an infinite sum
Hamiltonian operator. They equal the physical finite-volume maps on
observables supported inside that volume.

## 2. A uniform short-time expansion for ANY bounded local observable

In a finite volume H0 is self-adjoint and V_Lambda is bounded and
self-adjoint. Onsite-conjugated interactions are strongly continuous,
even, bounded, and have unchanged supports and norms. Strong Dyson
integration is legitimate on the separable finite-support Hilbert spaces.
The operator-integration framework and related lattice existence results
are described by [Nachtergaele and Sims, Sections 2-4](https://arxiv.org/html/1410.8174v1).
The graded connected-series estimate and constants below are given
explicitly here rather than assuming their tensor-lattice theorem applies
unchanged to fermions.

Let A_X have support X, s=|X|>=1. In the interaction-picture expansion
each nonzero nested commutator must add a hopping footprint meeting the
union accumulated so far. After j events that union has at most s+2j
cells. Its total incident absolute coupling is at most J(s+2j), by a
union bound. The commutator norm costs a factor two, also for odd A_X
because the Hamiltonian term is even. Therefore the complete n-event
coefficient is bounded by ||A_X|| times

  b_n(s,T) = (2JT)^n/n! product_(j=0..n-1)(s+2j)
           = q^n (s/2)_n/n!,          q=4JT.

This is an arbitrary-order induction, not an extrapolation from the
executed two-event footprint census. It uses no differentiation of an
unbounded electric generator or norm-Taylor expansion of its phases.
It includes ALL commutators, so no separate all-E gap remains here.

For q<1 the series converges absolutely, with total positive bound
(1-q)^(-s/2). Choose h=1/16, giving q(h)=69/128<1. The same h works for
every finite s; the size of s affects polynomial prefactors, not the
convergence radius. Thus large local algebras do not force the group
construction to use a vanishing time step.

Let Z_N^Lambda(t; A_X) denote the free term plus ALL n-event terms n<=N.
The future coefficient ratio is

  b_(n+1)/b_n = 2JT(s+2n)/(n+1).

For s=1 it increases to q; for s>=2 it is constant or decreases to q.
Consequently r_N=max(q,2JT(s+2N)/(N+1)) bounds every future ratio.
For N sufficiently large r_N<1 and the WHOLE tail is bounded by

  ||alpha_t^Lambda(A_X)-Z_N^Lambda(t;A_X)||
      <= ||A_X|| b_N r_N/(1-r_N) = ||A_X|| epsilon_(s,N)(T).

All quantities in the stored short-time certificates are rational.
At h=1/16, s=1, N=32, the bound is approximately 3.00332710e-10.
This is an all-observable existence/control estimate, not a newly
evaluated numerical bulk column and not a replacement error for q50.

Each finite coefficient has support within distance 2n of X. Thus two
volumes containing its radius-(2N+2) neighborhood have identical Z_N,
including for arbitrary initial bounded operators, not just E=0 inputs.
The two-volume norm difference is at most 2||A_X||epsilon_(s,N).
This proves norm convergence, uniform for |t|<=h and on the unit ball
of EACH fixed local algebra. Norm density and finite-volume isometry
extend these short-time maps and their pointwise volume convergence to A.

## 3. All real times, composition and exhaustion independence

Fix t and choose integer m with |t|/m<=h. The finite-volume identity

  alpha_t^Lambda = (alpha_(t/m)^Lambda)^m

and convergence on ALL of A imply pointwise norm convergence of these
finite compositions. Indeed, if T_Lambda,S_Lambda are isometries converging
pointwise to T,S, then

  ||T_Lambda S_Lambda A - T S A||
     <= ||S_Lambda A-SA|| + ||T_Lambda(SA)-T(SA)|| -> 0.

This defines alpha_t for every real t as the original volume limit.
It cannot depend on m, since the finite-volume left side does not.
The same argument for arbitrary t,s gives alpha_t alpha_s=alpha_(t+s).
Norm limits preserve products, adjoints, the identity and norms, and
alpha_(-t) is the inverse. Hence these are *-automorphisms, not merely
positive maps or a semigroup. The argument uses no norm continuity of
the time orbit of a general bounded rotor operator.

For completeness, compact-time uniformity needs more than pointwise
composition: such an orbit need not be norm compact. Use the uniform
unit-ball estimate from Section 2 instead. For |t|<=T choose a fixed
m with T/m<=h. At each of the m steps replace the short-time map on the
current local approximation by its finite Z_N. The support after each
replacement is contained in a FIXED finite enlarged set, independent
of t. Choose successive depths N_j so each relative tail is <=eta_j.
Isometry gives ||A_j||<=(1+eta_j)||A_(j-1)|| and the total approximation
error is at most ||A||[product_j(1+eta_j)-1]. The same finite local
approximation and error apply to every sufficiently large volume and
to the limit. The eta_j can be chosen arbitrarily small. This proves
uniform convergence on [-T,T], without claiming the free orbit is norm
compact, and proves independence of compatible exhaustions.

The previous high-field construction and this one coincide on |t|<=1
because both are norm limits of the same finite-volume parent evolution.
Their quite different upper bounds need not be equally sharp. This
extension changes no prior computed amplitude or record.

## 4. Exact obstruction to point-norm continuity on the full algebra

On one uncut link, E|e>=e|e>, U|e>=|e+1>, and

  alpha_t^0(U)=U exp(i kappa t(E+1/2)).

Take t_m=2 pi/[kappa(2m+1)]. Then t_m->0, and on |m> the last phase
is EXACTLY -1. Therefore ||alpha_(t_m)^0(U)-U||=2. This is an exact
escaping-flux sequence, not a conclusion from a finite electric cutoff.

The interacting correction is small in norm even for this U. From the
complete short-time expansion, for every local A_X,

  ||alpha_t(A_X)-alpha_t^0(A_X)||
    <= ||A_X||[(1-4J|t|)^(-s/2)-1] -> 0.

For U we have s=1. Hence limsup_(t->0)||alpha_t(U)-U||=2 with the
ORIGINAL nonzero hopping and electric couplings. Bounded interactions
do not repair the failure. The executable witness uses pi<4 to bound
the correction by a conservative rational number, while retaining the
exact pi-phase identity for every m.

This does not contradict norm convergence as volume grows: a fixed-time
limit and continuity as time varies are different assertions. Nor does
it contradict strong unitary continuity on a finite-volume Hilbert space.

The issue also survives restriction to physical gauge-invariant observables.
Let p be the oriented current around an elementary plaquette, with
div p=0 and |p|^2=4, and W=U^p its Wilson loop. Choose E=m p and one low
fermion per cell, so the original neutral Gauss law is satisfied; E+p
also satisfies it. The free phase is kappa t(4m+2). At

  t_m^W=pi/[kappa(4m+2)]

the two states have opposite phase and the norm difference is two,
already on that physical sector. The same interacting-correction estimate
with conservative support s=4 tends to zero. Thus the full gauge-invariant
quasi-local algebra also fails point-norm continuity. This is not fixed
by excluding charged single-link operators, and no Gauss-breaking witness
or finite-flux approximation is being used.
The Gauss witnesses here are finite-volume physical vectors in any volume
containing the plaquette. The infinite-volume norm statement concerns
the gauge-invariant subalgebra with its inherited kinematic C*-norm; it
does not select an infinite-volume Gauss representation or assert the
same norm obstruction in every possible representation or quotient.

## 5. The maximal continuous algebra and a legitimate generator domain

Let A_c={A in A: ||alpha_t(A)-A||->0 as t->0}. The perturbation correction
in Section 4 tends to zero for every quasi-local A, by local approximation
and isometry. Consequently

  A_c = {A in A: ||alpha_t^0(A)-A||->0} = A_c^0.

This is an exact characterization from the known FREE onsite group, not
an unexplained deletion of inconvenient observables. A_c is a norm-closed
unital *-subalgebra: the product and adjoint assertions follow from norm
inequalities and the closure assertion from isometry. The group law
makes A_c invariant under every alpha_s. Thus alpha restricted to A_c
is a point-norm continuous C*-dynamical system.

Both local fermion species, local occupations, bounded electric diagonal
functions and finite electric matrix units belong to A_c. Bare U does
not; its finite-flux restrictions converge only strongly, not in norm.
As A_c is closed and proper, it is NOT norm dense in the full algebra A.
No claim that those listed examples alone norm-generate all A_c is made.

A safe dense smooth domain is obtained by time smearing: for A in A_c
and f in C_c^infinity(R), the NORM (Bochner) integral

  A_f = integral f(t) alpha_t(A) dt

lies in every generator domain, with delta^n(A_f)=(-1)^n integral
f^(n)(t) alpha_t(A) dt. Smooth approximate identities show density in
A_c. This supplies actual domain and composition control there. A bounded
formal commutator [H,A] alone is NOT used to assert norm differentiability
or to place every bounded local operator in the generator domain.

Gauge covariance passes from finite volumes to the limits; A_c is gauge
invariant because the gauge action is isometric and commutes with alpha.
The gauge-fixed subalgebra therefore remains invariant as well. Given
an alpha-invariant state on A_c, the usual GNS prescription
U_t pi(A)Omega=pi(alpha_t(A))Omega is isometric, extends to a strongly
continuous unitary group, and implements alpha. This is a CONDITIONAL
representation statement, not a selected TFPT state or a constructed
positive-energy vacuum Hamiltonian.

## Checks, reproduction and remaining obligations

The original cubic rows supply all 126 terms and their adjoint pairs.
Independent translation-incidence arithmetic gives the same J. Actual
connected footprints are enumerated through two events (51 then 3065
classes); these are support/norm controls, not new physical bulk outputs.
Original three-vertex graph monomials independently check the cell adapter.

On the original edge, the executable Hamiltonian uses ALL 16 Fock states
at each of the backgrounds -2,0,3 and the corresponding shifted background.
Gauss fixes the flux for each basis state; these are complete charge
sectors, NOT a flux-cutoff approximation. A rotor U goes between DIFFERENT
backgrounds. Seven observables are tested: low/high annihilators, electric
parity, the zero-electric projection, high occupation, U and U P_(E=0).
For every matrix entry through time degree eight, repeated unsplit
Hamiltonian commutators equal the independent two-sided exponential jets.
Time addition, inverse, adjoint and two nontrivial product identities are
also checked. Complete sparse integer matrices, including their dimensions
and normalization, are retained in validation.json.

These finite checks do not prove an infinite-volume theorem: Sections
1-5 contain that argument. Resource limits in the checkers are not limits
of the induction, the electric spectrum or the mathematical time interval.

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/observable-dynamics/checker.py --output experiments/theory-contracts/observable-dynamics/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/observable-dynamics -p 'test_*.py'
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/observable-dynamics -p 'test_*.py'
```

Next substantive gates: choose/derive a physically appropriate state and
representation rather than assuming one, and investigate the fixed-parent
continuum/chirality/energy requirements. Alternatively, compute a complete
declared source target with its already-derived tail. No new q50 interval,
continuum, spin-two or T1-T8 closure follows from this lattice existence
result. Theory experiments only: no paper, website, ledger, verification,
scorecard, commit or push promotion.
