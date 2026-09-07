# NON-RH Round24: a finite-density preparation and local scalar elimination

2026-09-07. Local research on HEAD and actual remote main
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`, reverified this round.
No commit/push, paper/web release, ledger or empirical promotion.
Earlier local evidence and concurrent paper/ledger/v472 changes remain.

## Finite charge AND scalar density: a controlled family

The [finite-density contract](finite-density-background-round24/PROOF.md)
extends the Round23 dilute comparison to a specified extensive preparation
on the same g=nu=0 parent. Declare lambda_N=N u, u>=0, and shift every
integer charge by the E8 root p=e2. The total physical charge is Np.
Its neutral fluctuations are in the exact ground state of the FULL charge
Hamiltonian, including positive hopping and every integer charge state.

The homogeneous background gives an EXACT mass shift

    m_*^2=m^2+2u e(p), e(p)=1.

Prepare M quanta of the scalar zero mode in this shifted-mass oscillator,
with the other scalar modes in their physical vacuum. M/N may be any
fixed finite density. Other free continuous species remain unrestricted.
The source is not normal ordered and no vacuum energy is subtracted.

For eps=24N^2J<=1/32, the neutral excitation energy E=sum e(n_x) obeys

    ||E chi_J||<=4eps,
    <E>_chi <=2eps(2eta+eta^2), eta=2eps/(1-2eps).

The second-order mean bound and the complete hard-mode covariance give
an explicit residual norm R_N=O(u eps), uniformly in volume at fixed
scalar density. The proof displays every coefficient. At L=5 the
certified hopping endpoint is J=1/12000000; this is the NEUTRAL-sector
gap, not the different Round22 root-sector endpoint.

Both interacting evolutions are kept, without charge or Fock truncation:

    ||(U_original(t)-U_ref(t)) psi||<=min(2,|t|R_N),
    ||(U_original(t)-U_averaged(t)) psi||<=min(2,2|t|R_N).

With the retained common positive lower bound gamma, the corresponding
positive-frequency clock difference is at most
min(2,2|tau|sqrt(3/gamma)R_N). These are uniform on the stated
charge/scalar preparation tensored with the full free-spectator space.
Duhamel and the square-root resolvent are evaluated relative to the
invariant REFERENCE preparation, not an assumed invariant interacting one.

This resolves a finite-density comparison for that family, not general
finite-density dynamics. The coupling path is chosen, not derived.
J still scales at most as N^(-2). Sending eps to zero freezes charge
fluctuations and leaves the mass-shifted Gaussian scalar; it is not a
nontrivial interacting continuum construction or a full-gravity result.

## Local elimination: keep boundary faces, determinant and memory

The [local Gaussian contract](local-gaussian-elimination-round24/PROOF.md)
acts on the ORIGINAL local g=0 parent, not the nonlocal translation
average. Retain the scalar boundary faces of cells of side ell and
integrate their disconnected interiors. Charges and their actual hopping
amplitudes/cocycle remain. At L=9, ell=3, this retains 513 scalar sites and
eliminates 216 in 27 independent eight-site spatial blocks.

For every static integer charge profile, the eliminated scalar stiffness
has the uniform Dirichlet lower bound

    b_*=m^2+12 a^(-2) sin^2(pi/(2ell)).

The exact Schur kernel is positive at Euclidean frequency and has spatial
support diameter at most (3ell-4)a, independent of total volume at fixed
cell size. This construction does not inherit the Round23 global
momentum generator or silently solve the local stress problem.

The charge-dependent determinant is retained as physical output. So is
the frequency dependence. A static low-frequency expansion keeps BOTH
the induced potential and kinetic matrix Z, with remainder bounded by

    omega^4 ||C||^2/[b_*^2(b_*+omega^2)].

For moving charges, the Gaussian integration is still exact PER HISTORY
at the specified finite Euclidean time regulator. Each spatial cell
contains all its temporal coordinates. Determinants and temporal memory
remain; the original charge phases are not converted into probabilities.
The static frequency expansion is not applied to nonstatic histories.

Dense solve cost, storage, and the unsolved infinite charge-history sum
are explicit. Neither a time-local interacting Hamiltonian for arbitrary
moving charges nor an interchange of continuum/volume/history limits
has been established. Full g!=0 gravity is non-Gaussian and not covered.

## Evidence and the remaining mathematical target

Two exact checkers have 33 and 21 groups, with 13 source pins each.
The aggregate separately reruns 23 prerequisite checkers. There are 29
infrastructure/source/semantic fixtures, including six isolated wrong
variants. Normal and optimized checks, analytic review and manifest
consistency are distinct evidence types; finite examples are not a
machine-checked proof of every analytic statement.

See [review](ROUND24_REVIEW.md), [fixture evidence](ROUND24_RUNNER_VALIDATION.json)
and [aggregate evidence](ROUND24_VALIDATION.json). In the research environment:

    python -B experiments/theory-contracts/test_round24_runner.py
    python -B experiments/theory-contracts/run_round24.py
    python -B experiments/theory-contracts/run_round24.py --check-manifests

The next substantive target is a volume-controlled effective dynamics
for genuinely moving, finite-density charges at nonvanishing transport:
retain the induced determinant and bound temporal memory before taking
limits. A static Schur identity or a nearly frozen charge preparation
cannot substitute for that theorem. Microscopic parameter/parent selection,
local relativistic stress, chiral observed matter/flavor, native observable
identification, full gravitational constraints, spectators and external
parameter-fixed predictions remain open. No T1-T8/TOE/RH promotion.
