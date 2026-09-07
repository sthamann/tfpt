# NON-RH Round18: a finite-range full completion in a declared new field chart

2026-09-06. Local research on repository base
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`, also actual remote main at
the start of this round. No commit, push, paper/web release, ledger promotion
or empirical change. Existing research and concurrent paper/ledger/v472
changes are preserved.

## Main constructive result: full finite-range generator, with a precise price

The [preconditioned parent](preconditioned-local-parent-round18/PROOF.md)
supplies a full finite-range source-stabilized Hamiltonian expression with
a controlled self-adjoint realization, all-time unitary group, exact
constraint covariance and positive physical reduction. This is stronger
than locality of only the positive base in Round17.

The construction fixes the finite cubic lattice and declares NEW independent
gauge-field pairs at each site. On the old mean-zero chart, the canonical
preconditioning is

    c=ell^2 c_tilde,        X_tilde=ell^2 X,       ell=-Delta.

It cancels the inverse spatial operators in the actual linear sources:

    Q_tilde,H=(A tau+ell rho)/2,
    Q_tilde,v=-[2ell I-(3/2)d d*] Jv,
    c.Q=c_tilde.Q_tilde.

Every density here is the retained Ward density, current or stress. The
preconditioned free constraint energy also becomes a polynomial stencil.
Four additional mean gauge pairs supply ordinary independent site fields;
they are NOT physical homogeneous gravity or dynamically decoupled off shell.
Their first-class reduction adds no physical states.

Together with the existing local 35-pair/site positive base B, the full
generator uses 39 canonical pairs per site before the clock and separate
old gauge auxiliaries. It replaces the global square by

    g^2 sum_i rho_i(c_tilde) sum_alpha Q_tilde,i,alpha^2,
    rho_i=r_tilde,i^2+|v_tilde,i|^2+|(b v_tilde)_i|^2.

All terms have spatial support bounded independently of lattice size in
these declared fields. Operator-square ordering is retained; the actual
sources still do not commute. The full constraint generator is not positive;
its c_tilde=0 reduction is exactly B with the ordinary positive physical norm.

This is NOT a local identification with the original native gravitational
observable net: c_tilde=ell^(-2)c is nonlocal. The inverse norm is
ell_min^(-2), and the chart condition number grows with box size. The
kinematic change of variables and the constant gauge-Haar determinant are
explicitly accounted for. Bounded spatial range is not Lorentz covariance,
a cutoff-independent propagation bound or a relativistic continuum theorem.

The old global square is CHANGED, not rewritten. The linear source vertex
is exact on the old mean-zero chart; the complete old TT-plus-constraint
first dressed vertex returns only after the sequential base limits and the
same old gravity dressing. That dressing need not preserve this new locality.
There is no claim of all-order equality to the old completion.

## The analytic step that makes local block stabilization work

The [cellwise stability theorem](local-source-stability-round18/PROOF.md)
handles a difficulty hidden by the old global weight: some source
coefficients can vanish while others remain active. For the actual shear
r'=bv, v'=0, the added transport square in rho_i makes its active set
invariant and gives |rho_i'|<=rho_i.

On precisely the active source graph domains, the forms are closed and
satisfy h>=B-N/4 and an all-time energy bound exp(3|t-s|). A common form-core
and weak-uniqueness argument prove strong continuity even across changing
activity strata, including the physical zero fiber. No source graph condition
is imposed where its coefficient is zero.

This yields the full covariant unitary group and positive reduction, and
extends Round17's ORIGINAL Gaussian source embedding through the sequential
eta then delta limits. The quadratic clock construction also applies with
its proper tube, energy subtraction and norm weights. Finite-parameter
constraint-clock equivalence is not finite-parameter physical clock-dynamics
equivalence. All 4n+2 physical spectator modes remain accounted for.

The old Darboux chart alone would still fail locality: an actual L=3
coefficient linking Bcal_000 to pi_111^2 is -11/648. The preconditioning is
therefore substantive additional input, not a relabeling of local blocks.

## Exact auxiliary readouts are possible, but noiseless source energy is not

The [auxiliary-source result](auxiliary-source-obstruction-round18/PROOF.md)
constructs an explicit positive coherent-state isometry with mutually
commuting readout multipliers and exactly the original first source moments.
It computes their nonnegative extra squared-source energy.

More generally, for any isometry J and commuting readouts Ra with
J*RaJ=Qa, the leakage forms n_a=||(I-JJ*)RaJ psi||^2 satisfy

    n_a+n_b >= |<psi,[Qa,Qb]psi>|.

For an explicitly normalized Gaussian family in the ACTUAL Ward source,

    |<[Q0,Q1]>|=(t^2+10)/1024.

Thus such a register replacement cannot retain both all source moments
and the unchanged squared-source energy without leakage. A single constant
energy subtraction cannot remove this unbounded defect. This excludes
that exact commuting-register shortcut, NOT the new local parent, which
retains noncommuting source operators and changes the completion. The
coherent dilation itself is a readout construction, not a proved Hamiltonian
dilation. Positive static Gaussian elimination and undressed source-copy
constraints have separate, explicitly scoped sign/commutator checks.

## The charge parent now extends across the whole 3D lattice

The [electric Hodge parent](charge-hodge-round18/PROOF.md) keeps every link
and the entire E8 charge metric, adding local electric divergence and curl
constraints with a positive local penalty. Their exact integral kernel is
three constant oriented flux vectors: Z^24, not merely a numerical rank.

At L=3, the Gauss-only 440 integer coordinates reduce to 24. The penalty
has a volume-independent nonzero lower bound 2 Delta at its declared
normalization. Physical norm, the full three-copy charge energy, cocycle
and nontrivial spinor fourth powers are explicit. Charged harmonic shifts
must act on every parallel link in their direction; they are not local fields.

Selecting one rank-eight charge lattice by the obvious synchronization
violates a proper cubic rotation. Cubic averaging instead kills all harmonic
fluxes. More generally a cubic-invariant real linear kernel, with rotations
acting trivially internally, has dimension divisible by three. This is a
bounded linear/quadratic selection obstruction, not a no-go for nonlinear
orientational sectors or additional matter. Electric curl is a NEW imposed
constraint, not magnetic flatness or a derived Maxwell/chiral sector.

## Remaining physical obligations and reproduction

A local finite-regulator generator has now been constructed in its declared
new fields. The missing task is its microscopic selection and identification
with the required TFPT observable net, coupled to a selected charged/chiral
sector and a controlled relativistic continuum limit. The charge construction
is still separate. Their juxtaposition is not one interacting 3+1D TOE.
Flavor, measure and the original conjunctive T1--T8 obligations are not
promoted; there is no RH claim.

`run_round18.py` executes four new checkers and five unchanged prerequisites.
New exact groups, source provenance and inherited predecessor checks remain
separately typed. Twenty isolated runner fixtures are executed normally and
with an optimized parent interpreter. See the
[internal review](ROUND18_REVIEW.md), [aggregate validation](ROUND18_VALIDATION.json)
and [runner evidence](ROUND18_RUNNER_VALIDATION.json).
`run_round18.py --check-manifests` checks current source hashes, inventories
and recorded-success consistency; it does not certify the analytic proofs.
Prior Round10--17 evidence is retained and its manifests are checked separately.
