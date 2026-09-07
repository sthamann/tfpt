# Round20: local charge fields, neutral transport and the cost of unfreezing space

2026-09-07. NON-RH. One declared finite periodic cubic lattice, side L>=2,
N=L^3. This supplies actual local charge dynamics by changing Round19's
selection law: global synchronization is no longer an exact constraint.
There is one full E8-metric charge module PER SITE, not one global module.
No microscopic TFPT, fermion, chiral, relativistic or continuum identification
is inferred from the construction.

## 1. Retained frame gauge system; the one constraint that is removed

Use the complete [Round19 frame model](../cubic-charge-selection-round19/PROOF.md),
including its literal even positive unimodular Gram matrix G=B_E8^T B_E8.
Write e(n)=n^T G n/2 and n_s=e8, so e(n_s)=1. Every n in Z^8 is retained.
In the exact kinematic basis chart

    q_x=f_x^-1 F_x,   h_xy=f_x^-1 U_xy f_y,

local finite gauge acts only by left translation on the 24-state frames f_x.
Keep frame alignment q_x,2=q_x,3=0, finite-link lock h_xy=I and the local
gauge projectors A_x. Their positive selection penalty is

    P_rem=mu sum_x[e(q_x,2)+e(q_x,3)]
          +lambda_lock sum_(positive edges xy)(1-delta_(h_xy,I))
          +zeta sum_x(I-A_x),                         (1)

with all three scales positive. Their common kernel has the explicit basis

    J_loc|{n_x}>=24^(-N/2) sum_(f in G24^N)
           |f, F_x=f_x e1 n_x, U_xy=f_x f_y^-1>.       (2)

Unlike Round19, n_x are now INDEPENDENT site labels. The same free-orbit
argument proves that (2) is unitary from tensor_x l2(Z^8) onto ker P_rem.
There is no finite frame multiplicity or holonomy sector. The physical norm
is exactly sum_({n_x})|psi({n_x})|^2. The selection penalty retains a lower
gap min(mu,lambda_lock,zeta), without asserting a gap for interacting matter.

The previous exact gradient constraint is REMOVED. A finite positive
gradient energy will be allowed, but imposing its zero eigenspace would
undo the local dynamics below. The physical charge coordinate count has
changed from 8 to 8N. This is not an unnoticed enlargement or a claim that
one global charge module has acquired independent local coordinates for free.

## 2. An exact all-space local field net and the complete frozen cocycle

Retain the frozen cocycle

    beta(p,n)=sum_a p_a n_a G_aa/2+sum_(a>b)p_a n_b G_ab mod2,
    epsilon(p,n)=(-1)^beta(p,n).

On the physical Hilbert space define the ON-SITE unitary

    T_x,p|...,n_x,...>=epsilon(p,n_x)|...,n_x+p,...>.    (3)

Its full kinematic lift multiplies by epsilon(p,q_x,1), shifts only
F_x by f_x e1 p, and leaves every other site, frame and finite link fixed.
This is gauge invariant, local at site x, and commutes with every exact
selection term (1). It does not commute with the deleted synchronization
condition. Its product/adjoint laws are exact on the full space:

    T_x,p T_x,r=epsilon(p,r)T_x,p+r,
    T_x,p*=epsilon(p,-p)T_x,-p,
    [T_x,p,T_y,r]=0 for x!=y.                          (4)

All eight charge directions and the Gram cross terms survive. At each
site T_x,n_s^4=T_x,4n_s!=I; the frozen grade-plus-integer-carry construction
applies independently at EACH site, with all neutral coordinates intact.
Here "neutral winding" means zero Z4 grade, not zero Z^8 total charge:
T_x,4n_s still changes total charge by the nonzero vector 4n_s. The bond
transport in the next section is neutral in the stronger total-charge sense.

Diagonal local spectral projectors together with all (3) generate the full
site algebra B(l2(E8)): P_n T_(n-m) P_m is a nonzero scalar multiple of
|n><m|. Taking its strong closure supplies every bounded site operator.
Thus for a finite site set S there is an exact faithful field net

    A(S)=B(tensor_(x in S)l2(E8)) tensor I_(S complement),

and disjoint local algebras commute. The dressed lift of its generators
uses only the corresponding frames and electric variables, not a Wilson
line extending across the volume. This is equal-time lattice locality,
not a spacetime causal or relativistic reconstruction theorem.

This field net includes operators charged under the GLOBAL U(1)^8 generated
by total charge. Its neutral subalgebra is smaller. Fixing one total-charge
sector would retain neutral observables and charged corners, not the full
field algebra as operators within that one sector. Only the finite frame
group has been gauged here. The cocycle is not a CAR relation, and the
internal E8 charge lattice is not evidence for fermion statistics or a
nonabelian E8 gauge theory.

## 3. Positive local neutral hopping with nonzero transport

For every positive oriented nearest-neighbor edge x->y and every p in the
eight INTEGER basis vectors P={e1,...,e8}, define

    W_xy,p=T_y,p T_x,p*,
    h_xy,p=J(2I-W_xy,p-W_xy,p*),   J>0,
    H_hop=sum_(positive edges xy,p in P) h_xy,p.       (5)

Each W is a two-site gauge-invariant unitary, W_yx,p=W_xy,p*, and

    h_xy,p=J(I-W_xy,p)*(I-W_xy,p),  0<=h_xy,p<=4J I.

There are M=3N*8 terms, so H_hop is positive and bounded by 96JN I.
The diagonal constant is 2JM=48JN; it is not silently subtracted from a
positive parent. The choice of eight arithmetic generators and their rates
is new dynamical input, not a derived E8-Weyl-invariant or TFPT coupling law.

On a basis configuration, W_xy,p moves n_x->n_x-p, n_y->n_y+p, with phase

    epsilon(p,n_x-p) epsilon(p,n_y).                  (6)

In particular W_xy,p|p,0>=|0,p> with coefficient +1. For L>=3, the two
configurations which differ only by this transfer obey

    <0 at x,p at y|H_hop|p at x,0 at y>=-J.            (7)

At L=2, the two oppositely oriented positive links of the periodic graph
join the same sites, so the full Hamiltonian matrix element is -2J.
This finite-cell multiplicity must not be lost. A single term always gives
-J. Diagonal electric energies cannot cancel (7).

For the complete Hamiltonian below, these finite-support basis states are
in every finite operator-power domain. Thus (7) implies the actual unitary
transition amplitude iJt+O(t^2), or 2iJt+O(t^2) at L=2. This is a nonzero
dynamical transfer, not merely a possible externally applied observable.
From the all-zero configuration, hopping also creates opposite local
charges -p,+p. It is therefore incorrect to keep Round19's zero-charge
product basis vector as an unchanged ground state. No particle-number,
particle/antiparticle or Fock interpretation is inferred from these labels.

The full cocycle affects overlapping interactions. Exact multiplication
gives

    W_xy,p W_xy,r=(-1)^(p^T G r) W_xy,p+r
                =W_xy,r W_xy,p,
    W_xy,p W_yz,r=(-1)^(p^T G r) W_yz,r W_xy,p        (8)

for distinct x,y,z. Replacing all shifts by bare commuting shifts loses the
odd Gram-pairing signs in the second equation. For one fixed p, however,

    W_yz,p W_xy,p=W_xz,p,

by exact cancellation of the intermediate site's unitary and its adjoint.
Repeated nearest-neighbor transfers therefore realize any chosen path,
without a missing cocycle phase. Because the eight p span Z^8 and the
spatial graph is connected, finite transfer words connect every two
integer profiles of the same total charge: eliminate their differences
along any spanning tree, one basis component at a time. This is an
operator-word reachability statement, not a claim that every unitary
matrix element is nonzero at every time in the presence of interference.

## 4. Exact charge continuity and total conservation

Let n_x^a be a site charge coordinate. With Heisenberg convention
dA/dt=i[H,A], define the current from x to y for one bond/channel by

    I_xy,p^a=iJ p^a(W_xy,p-W_xy,p*).                  (9)

It is bounded self-adjoint with norm at most 2J|p^a|. Since
[n_x^a,W_xy,p]=-p^a W_xy,p and
[n_y^a,W_xy,p]=+p^a W_xy,p, the signs are

    dot n_x^a|_(xy,p)=-I_xy,p^a,
    dot n_y^a|_(xy,p)=+I_xy,p^a,
    dot n_x^a=sum_(incoming y->x,p)I_yx,p^a
              -sum_(outgoing x->y,p)I_xy,p^a.         (10)

All diagonal energies commute with n_x. In the normalized state
(|p,0>+i|0,p>)/sqrt(2), the current expectation for this term is Jp^a,
not -Jp^a. Summing (10) cancels every bond exactly.

There is no hidden unbounded-commutator assumption. The commutator for each
n_x^a is a finite sum of bounded shifts, with norm at most 12J for the
chosen basis channels on the cubic graph. The diagonal electric evolution
commutes with n_x. In its interaction picture the hopping and its charge
commutator remain bounded, so the norm-convergent Dyson series yields the
integrated continuity identity on Dom n_x^a and preserves that domain.
The bounded integral extends the charge difference to all vectors. This
justifies (10) as an operator-domain statement, not only a formal core rule.

For total charge Q^a=sum_x n_x^a, every W preserves its eigenvalue. Hence
every exp(i theta.Q), and all joint total-charge spectral projectors,
strongly commute with the full Hamiltonian and its all-time group. This
is exact global charge conservation, not approximate conservation to one
order in J. Individual electric labels are no longer conserved.

## 5. Full positive finite-volume dynamics and cubic covariance

Choose nu>=0 and define the PHYSICAL electric energy

    E_diag=(1/N)sum_x e(n_x)
                +nu sum_(positive edges xy)e(n_x-n_y),
    H_charge=E_diag+H_hop.                             (11)

For fixed finite L, E_diag is a positive self-adjoint diagonal operator,
coercive in all 8N integer coordinates. Its domain is the corresponding
weighted square-summability domain; finite charge support is an operator
core, and its resolvent is compact. Bounded self-adjoint perturbation by
H_hop retains that operator domain and core, compact resolvent, positivity
and an all-time unitary group. No electric cutoff or finite-clock substitute
is used. No uniform thermodynamic gap, unique interacting vacuum or continuum
propagation estimate is claimed.

A full kinematic parent adds (1), uses the diagonal term
(1/N)sum_(x,a)e(q_x,a)+nu sum_(xy)e(q_x,1-q_y,1), and the same lifted hopping.
It is coercive in all 24N integer coordinates before alignment. The finite
frame-projector term and H_hop are bounded at fixed N; the remaining
diagonal terms are unbounded and treated on their actual weighted domain.
All exact selection projectors strongly commute with this parent and
reduce it to (11). This gives one common gauge-invariant local charge
Hamiltonian, not just separately defined operators on a formal quotient.

Under proper spatial cubic rotations the body charges are internal scalars,
n'_x=n_(R^-1 x), as in the declared Round19 frame action. A positive edge
may reverse orientation; then W is replaced by W*, leaving h unchanged.
The Gram energy e(n_x-n_y) is even under that reversal. Consequently the
full Hamiltonian is cubically invariant on the finite periodic graph.
This does not restore the old native oriented-edge observable net or turn
internal charge into spatial spin.

The local density e(n_x) and scalar coupling terms built from it still
commute with frame/lock/alignment. They do NOT commute with H_hop. Therefore
fixed-electric-fiber propagation and force-free source identities from
Round19 cannot be reused unchanged. A common scalar/gravity parent must
include the new charge-energy currents and the source-domain effects of
hopping. These are separate coupled obligations, not erased by positivity
or total-charge conservation.

## 6. Why keeping exact synchronization would forbid this mechanism

Let P_sync project onto the old uniform configurations n_x=n at all sites.
For N>1 an operator omitting one site's charged factor has zero matrix
element between |uniform n> and |uniform m> when n!=m: the untouched site's
charge spectral projections distinguish them. Thus no proper-support
operator can change the old uniform charge while preserving that code.

More specifically, for every nonzero p and every edge x!=y,

    P_sync W_xy,p P_sync=0,
    P_sync H_hop P_sync=48JN P_sync.                   (12)

The transfer produces two unequal endpoint charges, so cannot remain
uniform. The local charged field itself has P_sync T_x,p P_sync=0.
Equation (12) is a COMPRESSION, not an invariant-subspace evolution:
[P_sync,H_hop]!=0. Finite nu leaves this leakage and physical transport;
imposing the old zero-gradient constraint removes it.

Even virtual excursions cannot turn neutral hopping into the old uniform
charge translation. Uniform n has total Q=Nn, and uniform m has Q=Nm.
For n!=m these integer vectors differ. Exact total conservation therefore
gives, for EVERY real t and finite nu,

    <uniform m|exp(-it H_charge)|uniform n>=0.         (13)

The same conclusion holds at every finite perturbative order and for any
additional total-charge-preserving interaction. Higher-order return terms
can change diagonal energies or return amplitudes within a fixed total
sector; (12) alone does not assert that they vanish. Nonneutral global
operations or a different charge reservoir would change the assumptions.

## 7. Constructive advance, costs and reproducibility

The declared finite model now has gauge-invariant ON-SITE charged fields,
nearest-neighbor neutral hopping with a nonzero unitary transition, exact
charge currents/continuity, full E8 lattice/cocycle/carry data, a positive
self-adjoint Hamiltonian, and a faithful local field net on the entire
physical Hilbert space. It is not merely the former globally frozen module.

The price is removing exact spatial synchronization and retaining 8N
physical integer charge coordinates, plus the previously declared full
frame construction. Gradient stiffness is energy, not a retained exact
constraint. The hopping channel set and J, nu, 1/N normalization are new
inputs. The resulting bosonic tensor charge model has not been identified
with propagating chiral Standard Model matter, a microscopic TFPT parent,
Lorentz/continuum physics, complete nonlinear Ward constraints or a TOE.
There is no RH claim.

`checker.py` pins and reruns the complete Round19 charge-selection chain,
then checks exact source cocycles, local gauge lifts, actual periodic-cell
transfer amplitudes and signs, overlapping-bond identities, continuity,
spatial covariance and synchronization failure. Sparse basis actions use
unbounded integer labels and never wrap/truncate a rotor Hilbert space.
Finite fixtures support, but do not replace, the all-size proofs above.
