# Round20: positive coupled hopping dynamics and the source/clock extension

2026-09-07. NON-RH. Fixed finite periodic cubic lattice, L>=2, N=L^3.
This is a new declared Hamiltonian, not a microscopic TFPT derivation.
The exact synchronization constraint of Round19 is removed. One full E8
charge module remains at EACH site; the physical space is no longer a
single globally synchronized module.

## 1. Exact Hamiltonian and preserved finite-gauge quotient

Use [local charge transport](../local-charge-transport-round20/PROOF.md) and
the full-frame chart (f,q,h) of [Round19](../cubic-charge-selection-round19/PROOF.md).
Exact frame gauge averaging, link locking and alignment retain q_x=(n_x,0,0)
with n_x in Z^8 independently at every site. A nearest-neighbor gradient
penalty may remain as ENERGY, not as a constraint. Define

    e(n)=n^T G n/2,
    D(n)=(1/N)sum_x e(n_x)+nu sum_(positive edges xy)e(n_x-n_y),
    V(n,phi)=(lambda/N)sum_x e(n_x) phi_x^2,
    X_d=B_delta,eta(g,m)+D+V,      lambda,nu>=0, m>0,
    U_xy,p=T_y,p T_x,p*,          p in {e1,...,e8},
    L_J=J sum_(xy,p)(2-U_xy,p-U_xy,p*),   J>0,
    X=X_d+L_J.                                             (1)

G is the complete pinned E8 Gram form, not the identity. T_x,p uses the
full old cocycle. There are M=24N edge/channel terms INCLUDING periodic
edge multiplicities at L=2. Every term is positive, so

    0<=L_J<=4JM I=96JN I.                                  (2)

The constant 2JM is retained in the physical Hamiltonian and clock energy.
Temporarily factoring its phase in a Dyson estimate does not subtract it
from the model. The hopping term is finite range in the declared local
site net. It commutes with the exact alignment, frame-lock and finite-gauge
projectors. It does NOT preserve the removed synchronization projector.

The diagonal source profile is

    u_n(x)=2lambda e(n_x)/N,
    rho_n=rho_m+u_n phi_x^2/2,
    j_n=j_m,
    tau_n,ii=tau_m,ii-u_n phi_x^2/2.                         (3)

Here n is a configuration index, not a time-independent label under X.
The full Hilbert space is the countable direct sum of the old continuous
base over n, or equivalently its tensor product with l2((Z^8)^N).

## 2. Self-adjointness without false sector conservation

At fixed n, X_d(n) is the positive polynomial Schrodinger operator of
[Round19](../coupled-source-domain-round19/PROOF.md), now with profile (3)
and additional constant positive energy D(n). The same direct-sum proof
gives X_d>=e_m>0 on its exact graph-summable domain. Finite charge support
with compact smooth continuous factors is an operator core.

L_J is bounded self-adjoint at fixed volume. Thus X is self-adjoint on
Dom X_d, with that same operator core, and X>=e_m. The form domain is also
unchanged. This is the bounded-perturbation theorem, not a new assertion
that the interacting evolution is diagonal in n. The latter would be false.
Only the eight total charges sum_x n_x are strongly conserved.

On the unreduced frame space, alignment/gradient are unbounded diagonal
charge energies. The lock and finite gauge penalties are bounded positive
finite-register operators. In the (f,q,h) chart, (1) acts on q and the
continuous variables; these bounded register terms commute with it. Their
exact quotient therefore yields (1), with no finite-register degeneracy
or Jacobian omitted. The selected site net is a different physical theory
from Round19's globally synchronized quotient.

## 3. Complete local source forms survive a bounded hopping perturbation

Use the actual Round18 preconditioned source list

    Q_H(n)=(A tau_n+ell rho_n)/2,
    Q_v(n)=[2ell I-(3/2)d d*]j_m.                           (4)

At each n these are real scalar Weyl quadratics. Their self-adjoint
direct-sum closures are the ones constructed in Round19. With the same
independent site gauge labels c=(r,v), shear r'=bv, v'=0 and weights
rho_i(c)=r_i^2+|v_i|^2+|(bv)_i|^2, define the CLOSED forms

    h(c)=X+g sum_i c_i.Q_i
            +g^2 sum_i rho_i(c) sum_alpha ||Q_i,alpha .||^2
        =h_d(c)+L_J.                                      (5)

The active-source domains are exactly those of h_d(c), since L_J is
bounded. At g=0 there are no source graph conditions. The lower bound
h(c)>=X-N/4 and the graph norm equivalence follow by completing squares
against the SAME positive X. Because L_J is independent of c and time,
the old derivative estimate remains valid:

    E(c)=h(c)+N||.||^2,
    |dE/dt|<=3 E(c).                                      (6)

All-time common-form propagators consequently exist. Equivalently add the
bounded perturbation L_J to the diagonal-sector propagator via its norm-
convergent Dyson series. This also proves strong parameter continuity,
including across inactive source strata: every Dyson term is an integral
of strongly continuous bounded products and its norm is bounded by
(4JM|t-s|)^k/k!. No unbounded charge coefficient is bounded by assumption.
The relevant common-form hypotheses are those reviewed by
[Balmaseda--Lonigro--Perez-Pardo](https://arxiv.org/html/2112.11063v2).

The same determinant-one shear therefore yields a covariant full unitary
group and its self-adjoint generator, with its strong difference-quotient
domain. Continuous gauge test sections still evaluate at c=0, giving the
positive physical generator X. The full off-shell gauge generator itself
is not positive. Bounded hopping does not turn it into a valid square-root
Hamiltonian. Strong finite gauge/lock/alignment reduction commutes with
this source construction; synchronization reduction does not.

## 4. Direct Gaussian dynamics with charge-changing terms

The mass-profile correction is pure trace. The actual TT gradient source
sigma, fast Hessian K_delta, Gaussian center f_delta and zero-point
subtraction are independent of n, exactly as in Round19. Therefore

    J_enc=I_charge tensor J_delta,eta,
    L_J J_enc=J_enc L_J.                                  (7)

First use the proven diagonal-sector direct-J limit, including the arbitrary
nonnegative profile and D(n); it extends to all initial vectors by finite
charge tails. Then add L_J on BOTH Hilbert spaces. In each Dyson term use
(7) and the diagonal propagator intertwining, telescope its finitely many
factors, and apply dominated convergence to the ordered time simplex.
The common factorial majorant makes the entire series uniformly summable
on compact times. This proves the direct-J dynamical limit for the genuinely
charge-mixing parent. It does not claim that a finite initial charge support
stays finite under the exact evolution.

Take eta->0 at fixed delta, then delta->0 at the same fixed lattice.
Both the base and full source-propagator conclusions survive the bounded
perturbation. The bounded-Weyl and local charge readout protocol theorem
extends by the same finite-word telescoping. No simultaneous-parameter,
uniform-volume or operator-norm convergence is asserted. The old tensor
spectators remain; hopping does not project them away.

## 5. Clock and the changed gravity vertex

The common positive bound X>=e_m permits the proper negative-sheet clock
tube and exact half-density construction of Round19, now using X_d+L_J
rather than a diagonal list of X_d(n). In particular

    omega_X=sqrt(12X),   D_X=3^(1/4) X^(-1/4),
    Psi_v(t)=D_X exp(-it omega_X)v,
    ||Psi||_clock^2=||omega_X^(1/2)Psi||^2/6=||v||^2.        (8)

Functional calculus uses X itself; there is no charge-by-charge clock
frequency after hopping. The full gauge clock uses characteristic
transport of the positive base and the proper tube, never sqrt(H_full).
The direct-J clock limit follows from the positive-gap functional-calculus
argument. Readout conjugation by D_X is essential, and spectator clock
energy is still not additive after taking the square root.

There is a substantive LOST shortcut. Let S=sum_a X_gauge,a J_a(n) be the
old scalar gravity dressing generator, with J_a=(rho_n,-j_m). The new
source density does not commute with L_J. On the finite-charge Schwartz
core, for U_g=exp(-igS),

    d/dg [U_g L_J U_g*] at g=0
          =-i[S,L_J]=sum_a X_gauge,a i[L_J,J_a(n)].         (9)

Equation (9) is generally nonzero for lambda>0. Its density component is
the actual hopping energy-exchange term derived in
[the energy balance](../scalar-charge-energy-round20/PROOF.md). The vector
current is charge-independent, so its direct hopping commutator vanishes.
No old force-free/mass-substituted gravity vertex is claimed for the new
moving inhomogeneous charge theory. The full source lift (5) is a declared
covariant completion, not a proof of a conserved nonlinear diffeomorphism
stress tensor. This distinction is required even though the analytic
positivity, reduction and clock results above hold.

The construction supplies local charge dynamics on a common positive parent.
Its microscopic selection, chiral statistics, relativistic stress tensor,
native-net equivalence and continuum remain open. No TOE/T1–T8/RH claim.
