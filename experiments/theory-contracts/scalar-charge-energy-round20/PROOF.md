# Round20: scalar–charge energy exchange and local energy balance

2026-09-07. NON-RH. The positive parent X=X_d+L_J is specified in
[the hopping-domain proof](../hopping-source-domain-round20/PROOF.md).
This derives its actual new energy-exchange term and a local energy-current
identity. It does not claim a complete relativistic stress tensor.

## 1. Exact shift calculus with the original charge cocycle

For an oriented hop e=(x,y,p), let s_e be the integer configuration change
n_x->n_x-p, n_y->n_y+p. Write U_e for the FULL projective shift, including
its n-dependent cocycle phase. If F(n,phi) is a real diagonal multiplication
polynomial and Delta_e F=F(n+s_e,phi)-F(n,phi), then

    F U_e=U_e F(n+s_e,phi),
    i[L_J,F]=iJ sum_e [U_e Delta_e F+U_e* Delta_-e F].     (1)

The coefficient sits to the RIGHT of the shift. Moving it to the left
without shifting its argument gives a different operator. The right-hand
side is symmetric on the finite-charge Schwartz core because
(U_e Delta_e F)*=-U_e* Delta_-e F. Cocycle phases do not cancel between
different overlapping hops and must not be replaced by commuting shifts.

For one edge,

    Delta_e e(n_x)=-n_x^T G p+e(p),
    Delta_e e(n_y)= n_y^T G p+e(p),
    Delta_e [e(n_x)+e(n_y)]=(n_y-n_x)^T G p+2e(p),
    Delta_e e(n_x-n_y)=-2(n_x-n_y)^T G p+4e(p).          (2)

Thus total integer charge is conserved but diagonal charge ENERGY generally
is not: it exchanges with hopping and scalar interaction energy. Neighboring
gradient-penalty bonds also change when one endpoint changes; they are not
omitted from D(n+s_e)-D(n).

## 2. The actual scalar Ward source gains a quantum transfer term

First isolate the scalar/charge input Hamiltonian

    H_sc=H_m+D(n)+(lambda/N)sum_x e(n_x)phi_x^2+L_J,
    rho_sc(x)=rho_m(x)+(lambda/N)e(n_x)phi_x^2,
    u_x=2lambda e(n_x)/N.                                (3)

H_m and rho_m,j_m,tau_m are EXACTLY the original free-scalar Ward functions,
with the repaired diagonal stress. D is charge diagonal. For a frozen n,
Round19's mass-profile computation applies. But n is now an operator moved
by L_J. Since L_J commutes with phi,pi but not e(n_x), the full equation is

    d rho_sc(x)/dt+sum_i D_i^- j_m,i(x)
        =S_x,   S_x=(lambda/N)phi_x^2 i[L_J,e(n_x)].      (4)

Equation (1) makes S_x completely explicit and local: only hops touching x
contribute. It vanishes at J=0 or lambda=0, not for generic moving charge.
Calling u_x a static external coefficient after adding hopping would
incorrectly omit (4). The added source is energy exchanged with the charge/
hopping sector, not a violation of total energy conservation.

The scalar momentum input obeys

    d j_m,i(x)/dt+Div_i tau_n(x)
       =-(u_(x+ei)-u_x)phi_x phi_(x+ei)/(2a).             (5)

There is no direct hopping commutator with j_m, because it has no charge
dependence. Equations (4),(5) are equal-time operator identities on the
finite-charge scalar Schwartz core: the continuous quadratics use exact
Weyl quantization and the discrete shifts are exact unitaries. They are
not continuum Poisson approximations to quantum charge transport.

When full gravitational/auxiliary interactions in B are added, (4) receives
the additional i[B-H_m,rho_sc] term. It is accounted for by the complete
energy-current construction below. The free scalar Ward expressions alone
are not claimed to be the total interacting gravitational stress tensor.

## 3. Exact cancellation in the coupled energy budget

Put V=(lambda/N)sum e(n_x)phi_x^2. The transfer parts of the scalar energy
and diagonal charge energy are respectively i[L_J,V] and i[L_J,D]. The
corresponding derivative of the hopping energy is

    d L_J/dt=i[X_d,L_J]=-i[L_J,D+V],                      (6)

because B acts only on continuous variables and commutes with bare charge
shifts. Equations (4),(6) therefore cancel in the total energy budget,
including the gradient penalty D and the scalar-dependent transition cost.
No scalar mass is retuned by hand during the motion.

Individual hopping bond energies need not commute: if edges share exactly
one site and p^T G r is odd, their transfer operators anticommute. Therefore
bond-by-bond energy balance also contains hopping--hopping currents. The
checker exhibits this with the ACTUAL off-diagonal entries of G. A model
using eight independent commuting shifts would miss these currents despite
having the right total integer charge count.

## 4. Full local energy continuity, including its operator-domain meaning

Before the prescribed fast zero-point subtraction, all displayed terms of
X are positive local kinetic squares, multiplication squares, diagonal
charge/gradient terms or bounded positive hopping terms. Index them by z
(site, edge, tensor component or local auxiliary block), and write

    X+E_fast I=sum_z h_z.

This is an exact finite sum of closed positive forms. Constant allocation
of E_fast has no effect on any current. On the common dense space of
finite charge support with continuous Schwartz functions, every h_z and
every finite product is defined. Define

    J_(z->w)=i[h_z,h_w],   J_(w->z)=-J_(z->w).

Then the EXACT core identity is

    i[X,h_z]+sum_w J_(z->w)=0.                           (7)

Terms with disjoint support commute, so each nonzero current is supported
on the union of two overlapping finite supports. Each local term has a
bounded spatial radius independent of N, hence so does this current
construction. Summing over a set of energy nodes leaves only currents
crossing its boundary. Grouping nodes into cells is an explicit finite
redistribution of energy; it need not produce the original free-scalar
stress stencil. The full construction includes scalar/charge exchange,
gradient-penalty changes and overlapping-bond projective hopping currents.

There is a precise weak dynamical interpretation without assuming that
Schwartz space is invariant under every unbounded evolution. Put
A=X+E_fast+1>=1. Each positive form q_z is bounded by q_A. For
psi in Dom A^(3/2), exp(-itX)psi stays in that domain. The map
A^(1/2)exp(-itX)psi is differentiable, so q_z(psi(t)) is differentiable and
its derivative is the weak commutator of X with q_z. This defines the
closed summed flux in (7) along such trajectories and conserves total
energy exactly. On the common core it is the displayed finite sum of local
commutators. We do not separately assert that every unbounded individual
current has a bounded closure or a state-independent expectation for all
finite-energy vectors. The bounded charge-current theorem is stronger in
that respect and is proved separately.
The bounded-readout Gaussian limit does not, by itself, prove convergence
of these unbounded energy currents; additional moment estimates would be
needed for that separate limiting assertion.

Thus the result is a full local ENERGY balance for the specified model,
with a common-core identity and qualified weak evolution, not a proof of
a conserved symmetric relativistic energy-momentum tensor. Discrete cubic
translations do not by themselves supply an infinitesimal local momentum
generator. Equation (5) must still be completed by an appropriate dynamical
charge/gravity stress construction before that larger claim can be made.

## 5. Evidence and remaining scope

The checker imports the actual scalar Ward source, derives the precise
dynamic transfer residual, and uses exact infinite-lattice shift actions
on finite-support vectors to test energy exchange, operator ordering and
noncommuting neighboring bond currents. A finite-support test vector is
not a truncated Hilbert space: shifts are allowed to leave its support.

The coupling, synchronization relaxation and hopping channels are chosen.
There is no derivation of spin/statistics, chiral matter, a Standard Model
spectrum, uniform propagation speed, full nonlinear gravity or a continuum.
No T1–T8/TOE/RH or experimental status is promoted.
