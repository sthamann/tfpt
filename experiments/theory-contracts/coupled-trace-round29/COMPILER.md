# Simplicity, Noether, and geometry: what actually selects a parent?

2026-09-07. NON-RH research on the **same** scalar/E8 charge model as
[PROOF.md](PROOF.md). The objective is a common microscopic construction,
not eight independently adjustable models presented as T1-T8 closure.
The computations below distinguish equivalent representations from new
physical assumptions. They do not derive the Standard Model or gravity.

## 1. The useful simplification is an operator identity

At the fixed regulator the original interaction satisfies

    Q_u=E_u Q_0 E_u, E_u=exp(-delta u W/2),
    W=sum_x e(n_x) phi_x^2 >=0.

This identity retains the complete hopping operator, its negative loops,
the infinite charge lattice, and continuous scalar variables. The
log-convex positive trace then gives

    exp(-u M) Z(0) <= Z(u) <= Z(0).

The four evaluated u>0 cases in PROOF.md use this simplification. It
avoids demanding a uniformly small conditional Poisson error at every
scalar history. It does not replace a fluctuating interaction with a
chosen background or posit a new positivity theorem for signed weights.

This is a concrete compiler design principle: simplify a representation
by an exact identity or a proved error budget **before** discarding any
state, phase, source, or interaction. A shorter formula by itself has no
such guarantee.

## 2. Noether supplies compatibility, not a unique coupling

Let H(u)=H(0)+uW on the original common Hilbert space. The original local
charge generators commute with W,

    [W,n_x^a]=0, [W,Q^a]=0, Q^a=sum_x n_x^a.

Every nonnegative u therefore preserves the same global U(1)^8 charges.
On the finite-support/Schwartz core, let W_(xy,p) be the actual cocycle
hop moving p from x to y. The contribution to the continuity equation is

    d n_x^a/dt = - I_(xy,p)^a,
    I_(xy,p)^a = i J p^a [W_(xy,p)-W_(xy,p)^*].

Adding uW leaves this **current operator** unchanged. Its expectation
values and time evolution are not unchanged: the state and Hamiltonian
depend on u. Round20 already derives the actual current and the
interaction-energy exchange; those pinned results are not new claims here.
The new checker uses neutral states (p,0,-p), with the third charge outside
the tested edge, in all eight original channels and all 192 local current
components. In particular it retains the first channel's e(p)=2, rather
than replacing all channels by norm-two roots.

The model is not dynamically decoupled. Between (p,0,-p) and (0,p,-p),

    W_before-W_after=e(p)(phi_0^2-phi_1^2),
    <after| i[H_hop,W] |before>
       = -i J phase * e(p)(phi_0^2-phi_1^2) != 0.

At the fixed thermal regulator, Q_0 has no kernel and W is a nonzero
positive operator on the neutral space. The finite expectation proved
in PROOF.md is consequently strictly positive. Hence

    d log Z(u)/du at u=0 = -beta <W>_0 <0.

The different couplings are not identical operators or unitary changes
of representation preserving the same partition function. No auxiliary
spectator system is needed for this underdetermination example.

[Noether's original variational theorems](https://arxiv.org/html/physics/0503066v3)
relate invariance of an action to conservation laws and differential
identities. They do not specify the invariant action or its coupling
coefficients. The u-family above is our explicit application of that
distinction; it is not a claim that Noether proved anything about TFPT.

**Selection test.** A proposed compiler must either derive u in stated
units, prove it redundant while preserving the complete source-dependent
readouts, or retain it honestly as additional physical input. Checking
the same conservation equation at several u values cannot select one.

## 3. An exact geometric representation, with its compulsory measure term

Fourier transformation identifies the onsite charge Hilbert space
ell^2(Z^8) with L^2(T^8). Write n_a=-i partial_(theta_a) and
e(n)=n^t G n/2, with the original det G=1. For the **onsite kinetic
piece** consider

    H_flat= -1/2 partial_phi^2 + c(phi)e(n),
    c(phi)=a_c+u phi^2, a_c>0.

The symbol a_c denotes the onsite charge coefficient (1/N in the
reference), NOT its spatial lattice spacing a=1. The metric

    ds^2 = dphi^2 + c(phi)^(-1) (G^(-1))_ab dtheta_a dtheta_b

has precisely the required principal differential symbol. The eight
torus directions are Fourier-dual **configuration variables**, not eight
new physical spacetime dimensions. This is a representation of existing
degrees of freedom, not a chosen Calabi-Yau compactification.

However, its natural measure and Laplacian are

    sqrt(det g)=c^(-4),
    Delta_g=partial_phi^2 + b partial_phi
              + c G_ab partial_(theta_a) partial_(theta_b),
    b=-4 c'/c.

The unitary from curved to flat measure is U=c^(-2). Conjugating the
actual differential operator gives

    U(-1/2 Delta_g)U^(-1)=H_flat+V_geom,
    V_geom=b'/4+b^2/8
          =-c''/c+3(c'/c)^2
          =-2u/c+12u^2 phi^2/c^2.                      (G1)

Thus the exact geometric representation is

    H_flat=U[-1/2 Delta_g - V_geom]U^(-1),             (G2)

with the original scalar potentials added on both sides. The term
-V_geom is forced by unitary equivalence; it is not a free fit. Simply
replacing H_flat by the pure Laplace-Beltrami operator changes the model.
The checker verifies (G1) on an arbitrary test function and the tests
repeat the computation with independent rational coefficients and a
nontrivial polynomial.

Nor can the discrepancy be removed by an arbitrary constant curvature
ordering. For the nine-dimensional configuration metric,

    R=8 c''/c -26(c'/c)^2,
    V_geom + (xi/2) R
       =(-1+4xi)c''/c +(3-13xi)(c'/c)^2.

At u>0 and a_c>0, vanishing for all phi would require both xi=1/4 and
xi=3/13. No constant xi works. The first choice leaves
-(c'/c)^2/4. For example, at phi=0 the scalar curvature is 16u/a_c;
the warp is genuine geometry, not an unexplained removal of u.

Two tempting geometric selection conditions can also be decided here.
For this ansatz,

    R(0)=16u/a_c, R''(0)=-240u^2/a_c^2.

Requiring a Ricci-flat **configuration** metric forces u=0, since Ricci
flatness requires R(0)=0. Requiring constant scalar curvature also forces
u=0, since R''(0) must vanish. Conversely u=0 gives the flat product.
Thus these particular simplicity conditions eliminate the interaction;
they do not select a distinguished positive u. An imposed value R(0)=R_*
would give u=a_c R_*/16, but R_* is then an extra scale unless derived
independently. These exact exclusions concern this quadratic warped-torus
ansatz only, not all geometric TFPT parents or a Calabi-Yau construction,
and are not physical Einstein field equations.

**Scope.** This is the onsite principal-symbol and measure calculation.
The full model still contains its original cocycle hopping, neutral
sector, spatial charge coupling nu, and scalar gradient potential. No
claim is made that all these terms have become a simple local
Laplace-Beltrami operator, or that this configuration metric is the
physical gravitational field. The construction works for every u>=0,
and so does not select u. It settles the measure correction for this
specific geometric identification, not the global TFPT geometry.

## 4. Einstein's perspective is a conditional bootstrap, not a hidden premise

There is a useful classical organizing idea: matter and gravitational
stress should belong to one self-consistent variational system.
[Deser's explicit self-coupling derivation](https://arxiv.org/html/0910.2975v3)
starts from a free, flat-space, massless symmetric spin-two field, together
with locality/Lorentz and derivative-order assumptions; a first-order
Palatini formulation exposes the classical Einstein self-coupling in a
cubic term. This explains how demanding consistent coupling can reduce
apparent freedom **after** the field content and assumptions are given.

It does not derive that initial spin-two field from the E8 charge
Hamiltonian, establish a quantum continuum limit, select microscopic
couplings, or produce chiral fermions. Covariant conservation of a
chosen matter action is not by itself the Einstein field equation.
Importing the starting spin-two field would be an additional T7 input,
not a completed T7 derivation.

For TFPT the productive test is therefore whether one microscopic
construction generates a common stress tensor and a genuine gapless
spin-two excitation, then whether the same low-energy source functional
has the required universal coupling. A formal quadratic tensor symbol
or an independently postulated Einstein action does not pass that test.

## 5. The common-source compiler gate

For a candidate parent H_q depending on declared compiler data q, first
expose all sources, rather than giving different observables unrelated
prescriptions. A finite-regulator thermal source trace can be defined
from the same transfers. A physical real-time closed-contour functional
would additionally require a derived state and reconstructed dynamics,

    Z_q[J_+,J_-] = Tr(U_q[J_+] rho_q U_q[J_-]^*).

This formula specifies a required common object; Round29 does **not**
construct the missing physical Z_q or rho_q. Its source derivatives must
generate the actual charge currents, matter responses, and total stress,
with symmetry identities proved for the same measure and regulator.

Before calling q a complete compiler, test invariant local deformations
such as uW. If two inequivalent outputs still satisfy every stated
compiler constraint, that constraint set is incomplete. If a proposed
geometric simplification changes the measure, retain the exact Jacobian
or prove a controlled equivalence. If a low-energy limit drops a mode,
bound its effect on these **same** source readouts. This is the operational
content of mathematical economy here; it is not a proof that elegance
selects Nature.

The current T1-T8 requirements split into three dependent tasks:

* **Selection (T1-T2):** derive structure, dimension, seam/representation,
  and compiler rules. The continuous u-family is a concrete unresolved
  selection test, not a reason to fit u from desired predictions.
* **One physical dynamics (T3-T7):** construct the same local/unitary 3+1D
  model, chiral matter and measure, interacting Lorentzian infrared limit,
  all required couplings/textures, and universal quantum spin-two coupling.
  Round29 supplies a controlled interacting finite-regulator trace, not
  any of these full physical theorems.
* **State and readouts (T8):** select the initial state and obtain all
  physical readouts from one closed-contour functional. Declaring beta=1
  in a test does not select a cosmological state.

The immediate next test is a **parameter-selection identity for this
same u-deformation**, with the charge/scalar normalization fixed and the
measure term (G1) retained. It must follow from the compiler's declared
premises and distinguish inequivalent u values. No such identity has
been obtained here. In parallel as a mathematical question, the trace
method still needs improved bounds at fixed strong coupling and uniform
control when the regulators are removed. Neither missing result can be
replaced by the four successful finite-regulator examples.
