# Non-RH TOE research: Round14, a complete finite conditional constraint model

Date: 2026-09-06. Repository HEAD and actual remote main reverified at
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`.
This is local, unpromoted research integration, not a commit, push or public
release. Previous rounds and concurrent paper/ledger/v472 edits are preserved.
No T1–T8 gate, empirical scorecard row, or RH claim is promoted.

## Outcome

One declared finite scalar/TT completion now has a common Hilbert-space
construction for gravity, auxiliary constraints, the trace clock and
homogeneous relational momenta. Self-adjoint generators, exact unitary group
closure, a positive nonzero physical space and its bounded Dirac observables
are constructed together. No unknown interacting Galerkin limit is assumed.

The crucial change is an explicit term in the first-class constraint ideal.
It leaves the already chosen reduced physical Hamiltonian and the whole free
Hamiltonian unchanged, but changes the first off-shell interaction vertex.
Auxiliary gauge-unfixing and the clock/momentum prescriptions are also
declared inputs. Thus this is a solution of a specified finite conditional
quantum model, not of the unchanged old unreduced operator or all T1–T8.

| Contract | New result | Essential boundary |
| --- | --- | --- |
| [First-class completion](firstclass-completion-round14/PROOF.md) | A uniquely self-adjoint completed Hamiltonian has an explicit all-time unitary group, exact strong constraint covariance and precisely the chosen positive reduced dynamics. | A demonstrably nonzero constraint-ideal change alters the first off-shell vertex. Its microscopic TFPT selection is not derived. |
| [Joint gravity/auxiliary/clock model](joint-constraint-model-round14/PROOF.md) | One transported spectral tube and unimodular semidirect group yield an absolutely convergent joint average, positive nonzero physical space and bounded Dirac representatives. | Retains the declared clock sheet, energy convention and relational momenta, not a derived local current or restored homogeneous gravity. |
| [Auxiliary domains and reduction](auxiliary-domain-round14/PROOF.md) | A parameter-dependent metaplectic unitary constructs a self-adjoint completed total Hamiltonian, exact auxiliary propagation, and a separately declared gauge-unfixing with the seed physical norm and dynamics. | Adds primary-momentum-dependent off-surface terms; gauge-unfixing also changes the off-shell Hamiltonian and retained constraint list. It does not solve unchanged-H_sa gravity covariance. |
| [Actual common-domain obstruction](common-domain-round14/PROOF.md) | Self-adjoint realizations of distinct-time actual characteristic fibers cannot share either their operator domain or their absolute-value square-root domain. The obstruction also holds on an open set of regular labels. | Rules out fixed-domain assumptions, not all moving-domain propagators or all strong-resolvent limits. |
| [Actual full-system escape](escape-round14/PROOF.md) | All fourteen TT modes and eight scalar modes give a negative-energy classical orbit with finite-time escape on a stationary off-shell fiber; exact Gaussian states prove two-sided quantum unboundedness. | The escape fiber is not a regular characteristic and is not the full physical constraint surface. No quantum deficiency or Galerkin nonconvergence follows. |
| [Galerkin error control](galerkin-control-round14/PROOF.md) | An exact residual in the three upper physical Hermite shells bounds error against every self-adjoint extension. A separate exactly soluble cubic shows remaining boundary-choice freedom. | The actual residual integral has not been proved to vanish. The soluble boundary model is not the actual Hamiltonian. |

## 1. The constructive solution and its exact price

Use the actual already chosen positive TT/matter operator A_+ and the entire
free nonzero-mode gauge quadratic K_c. The new eliminated Hamiltonian is

    H_first=A_++K_c,
    K_c=-i(bv).partial_r+k(c), c=(r,v),
    H_first-H_sr=-g r.Bcal+g v.B_v.J_v.

The last line is a first-class-ideal term: it vanishes at c=0 and only changes
gauge-direction motion there. Both the full free Hamiltonian and the entire
reduced physical interaction, including its positive g^2 term, are retained.
An actual-source datum gives the nonzero off-shell difference -3 sqrt(2)/128;
the change is not hidden or renamed as equality to H_sr.

The gauge flow is the explicit determinant-one shear

    G_t f(c)=exp(-i integral_0^t k(exp(-s A_c)c)ds) f(exp(-t A_c)c),
    A_c=[[0,b],[0,0]], A_c^2=0, Tr A_c=0.

Time mollification proves its Schwartz core. Joint spectral calculus with
A_+ defines the full self-adjoint sum, including its correct domain where
positive and negative spectral terms can cancel. Constraint group averaging
evaluates c=0, gives the ordinary positive TT/matter norm, and descends exactly
to exp(-it A_+). These are analytic all-Hilbert-space results, not finite
matrix approximations to canonical commutation relations.

The [combined auxiliary proof](auxiliary-domain-round14/COMBINED.md) then uses
W_0=U_g V to construct H_joint=W_0 H_first W_0*, with exact auxiliary and
gravitational constraint propagation on the same transported domains.
Its simultaneous c/eta averaging gives that same physical norm and dynamics.
The auxiliary total before gauge-unfixing does not preserve eta=0; its
secondary quadratic must be removed by the separately declared prescription.

Finally the old quadratic trace clock is added only to A_+, not by taking
the square root of indefinite H_first. With the unitary clock map Z,

    W=W_0 Z*,   C=W (K_c+M_lambda) W*,
    H_ref=L2(c) tensor L2(eta) tensor L2(I_lambda) tensor H_z.

The image is the transported negative-sheet tube characterized by
W_0 A_+ W_0*-P_0^2/12 in I; it is neither the raw A_+ tube nor a bounded
band of the total C spectrum. The single joint constraint representation
includes c, eta, C and the compact group generated by seed homogeneous
momenta. The c/C part is semidirect, not falsely commuting. Its full Haar
integral converges absolutely and gives

    <F(0,0,0), Pi_0 G(0,0,0)>,
    H_phys=ran Pi_0=intersection_i ker J0_i != {0}.

Every bounded physical operator has an explicit transported Dirac
representative. The clock-dependent readouts need not stay in a fixed
Pi_0 subspace; no autonomous restriction of A_+ to that subspace is asserted.
Classical completed Hamiltonian flow is also complete. This is not a theorem
of completeness for every relational momentum gauge flow on the full
off-shell negative sheet.

## 2. Auxiliary completion, with its changed assumptions exposed

The original auxiliary stationary graph is f=-K^-1 s, where the components
of f are actual quadratic matter operators and need not commute. In auxiliary
momentum coordinates eta, define the full direct-integral unitary

    V(eta)=exp(-i eta.f),
    Y=V y V*,
    H_comp=V [A + y.K.y/2] V*.

Here A is the chosen self-adjoint eliminated seed Hamiltonian. For the already
reduced TT/matter seed it is the unique positive operator previously proved.
For the unchanged old full gravity seed, extension covariance and physical
selection remain unproved. For the newly declared H_first they are now
constructed above and in COMBINED.md. The auxiliary joint spectral sum has
its exact multiplier domain; no unwarranted intersection-domain assumption
is made for its indefinite parts.

The Y components strongly commute and are canonically conjugate to eta.
The full auxiliary evolution is exactly Y(t)=Y and eta(t)=eta-t K Y in the
bounded Weyl sense. The correction to the naive shift y-f is necessary:
the actual unprojected source has nonzero commutators. Their connection
corrections are constructed, not omitted.

For A equal to the old H_sr, the eta=0 operator-valued auxiliary Weyl symbol
agrees with the original H_sa. For A=H_first it instead equals H_sa+Delta H,
with Delta H the declared first-class-ideal change above. Both statements
use variables before U_g gravity dressing; after dressing the comparison
is conjugated by U_g as well. The secondary source is unchanged in that
same reference frame. The K-contracted quadratic-source
ordering correction vanishes exactly because only the configuration-only
TT square survives. Individual uncontracted squares need not have zero
ordering correction; the checker detects that distinction.

Off the primary surface, H_comp has additional explicitly defined terms.
It is therefore not the unchanged H_sa on the latter's full Schwartz domain.
The unitary is controlled on compact-eta Schwartz-valued tests and on its
transported operator core; full joint Schwartz invariance is not assumed.

Imposing every original real second-class operator as an annihilation
condition gives only zero, since the primary/secondary commutator contains
the invertible constant K. A nonzero physical space requires a declared
reduction prescription. The constructed gauge-unfixing keeps eta=0 and uses

    H_GU=V A V* = H_comp-Y.K.Y/2.

Abelian group averaging gives the exact seed inner product by evaluation at
eta=0 and descends to exp(-it A). This is an explicit quantization choice,
not automatic equivalence to every possible quantize-first prescription.
Simultaneous gravity dressing transports the construction consistently.
It inherits proven covariance from H_first, but cannot manufacture covariance
for an unspecified extension of the unchanged old H_sr.

## 3. The unchanged actual family has no fixed operator or absolute form domain

For the actual regular L=2 characteristic, h_t=h_0+gt B-t^2/32. Exact Weyl
displacements of full physical Schwartz packets give, at every fixed t,

    ||h_t f_R|| = O(R^5),
    |<f_R,B f_R>| >= c R^6,   c>0,
    ||f_R||=1.

The order-six Hamiltonian contribution cancels between actual scalar kinetic
energy and the actual cubic TT vertex. The surviving B term does not cancel.
Undisplaced TT spectator vertices contribute at most order four; none is
removed from the full model. A second delta-site displacement independently
reproduces the mechanism with a different coefficient.

If two self-adjoint extensions had the same operator domain, the closed graph
theorem would make their graph norms equivalent, contradicting these bounds.
If their Dom(|A|^(1/2)) spaces coincided, the same argument on spectral form
norms, followed by Cauchy–Schwarz, gives the same contradiction. This latter
statement is valid for indefinite operators; no positive Friedrichs form is
assumed. Continuity of the kinetic coefficients extends the result to an open
regular-label neighborhood and a small time interval there.

A separate explicitly solved quadratic family has moving domains and a
unitary propagator on its invariant Schwartz core. It prevents incorrectly
promoting the actual fixed-domain obstruction to a theorem against every
possible time-dependent domain construction.

## 4. Classical escape belongs to the unchanged off-shell model

On r=v=y=0 the actual full physical expression is

    h=T+V2+V3,  T=|p|^2/2, V2>=0 quadratic, V3=g Q.tau cubic.

It does not contain the positive quartic completion term g^2 R. For negative
energy E and outward radial motion, F=|x|^2 satisfies

    F''=10T+2V2-6E,
    F F''-(5/4)(F')^2>0.

Hence F^(-1/4) is concave and the full solution escapes in time at most
4F(0)/F'(0). The exact L=2, m^2=2, g=1 witness gives

    E=-16384, F(0)=8192, F'(0)=32768, T_max<=1.

All fourteen TT and eight scalar coordinates remain present. A second
initially unoccupied TT mode is immediately excited. The proof therefore
does not assume a dynamically invariant one-mode truncation.

The same initial datum in the different positive completed model has energy
180224. Its negative-energy hypothesis fails. This result must not be used
to claim that the positive reduced Hamiltonian has the demonstrated runaway.

Nearby regular characteristic trajectories reach any prescribed finite
radius before time one, with the neighborhood shrinking as the target grows.
This does not prove escape for one fixed regular label. Independently, full
22-coordinate Gaussian packets have exact off-shell expectation

    8 lambda^2-lambda^3/4+91/2

at g=1; the opposite TT displacement reverses the cubic sign. This proves
two-sided lack of semiboundedness, also on frozen regular fibers and the full
minimal operator after parameter localization. It proves neither nonunique
self-adjoint extensions nor their absence.

## 5. A real finite-cutoff error bound, not a projected-equation residual

For compact-parameter, finite-Hermite initial data f, the exact finite
evolution U_N(t) remains in the unchanged minimal test domain. Against ANY
self-adjoint extension H, Duhamel gives

    ||U_N(t)f-exp(-itH)f||
      <= integral_[0,t] ||(I-Pi_N)h Pi_N U_N(s)f|| |ds|.

Since the physical polynomial degree is three, only three top input shells
and three external output shells are needed to evaluate this residual. The
actual vacuum-to-three-creation amplitude includes a nonzero 1/8 coefficient.
Dropping the third shell is therefore an explicitly failed negative control.

The norm integral must itself be bounded rigorously; isolated floating-point
samples do not do that. Its convergence to zero for a dense class at both
signs of time would identify ALL self-adjoint extensions and prove essential
self-adjointness, a stronger result than choosing one covariant limit.

Finite time-Taylor remainder bounds also hold independently of the extension,
but need not tend to zero with order. In an exactly solved, separately labelled
cubic MODEL, all finite derivatives agree while different boundary phases
eventually produce orthogonal packet superpositions. Even exact covariance
and the required purely absolutely continuous full-real-line spectrum do not
select a boundary phase in that MODEL. No actual TFPT deficiency index is
inferred from it.

## Reproduction, integration and the remaining TOE work

Run from the repository root:

    experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/run_round14.py

Seven new checkers, including an independent full-source cross-check, and six
unchanged prerequisites are recorded separately in ROUND14_VALIDATION.json
and six per-contract validation.json files. Twenty temporary-fixture runner
tests run under each of normal and optimized parent settings; their evidence
is ROUND14_RUNNER_VALIDATION.json. Source hashes, complete inventories and
record consistency are checked by run_round14.py --check-manifests.
These metadata checks are not mathematical proof certification. Exact
assertion groups, the uncounted full-system checks and infrastructure tests
are not combined into a fabricated count of proved physical facts.

The proofs received separate complete reviews. Original Ward-source equality
is also checked independently, including all fourteen TT modes and a second
full-model displaced-packet witness. Old proof/manifests are left unchanged.
No paper, website, central ledger or empirical scorecard promotion is part
of this round, and concurrent edits to those surfaces are not overwritten.

T3/T7/T8 gain a common, completely specified finite conditional quantum
construction: domains, constraint group, auxiliary reduction, clock and
positive physical norm now work together. The remaining physical selection
question is whether TFPT derives this completion and its observable algebra.
T1/T2 microscopic geometry and common-parent identification, T4 chirality and
measure, T5 locality and continuum/Lorentz control, and T6 physical flavor are
not thereby solved. No full T1–T8 gate is promoted.

The constructive next dependency is microscopic selection: derive the
constraint-ideal completion, auxiliary reduction, clock/momentum prescription
and physical observable algebra from a single TFPT parent, and prove its
required locality and continuum behavior. If the original first off-shell
vertex is instead nonnegotiable, the unchanged-family moving-domain evolution
or a valid selected limit still needs its own proof. That is a different
Hamiltonian problem; the completion above does not claim to solve it.
