# NON-RH Round16: the original vertex and clock together, with two further bridges

2026-09-06. Local research integration on repository base
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`, also the actual remote main
verified at the start of this round. Earlier research artifacts and concurrent
paper/ledger/v472 edits are preserved. No commit, push, public release,
empirical scorecard change or full T1--T8 promotion in this round.

## Main result: the Round15 clock compatibility gap has a constructive answer

The [joint vertex/clock proof](clock-vertex-round16/PROOF.md) now retains the
ACTUAL Round15 generator H_vp, its original first dressed interaction vertex,
and the unchanged quadratic clock H_vp-P_0^2/12 in one quantum construction.
It includes the declared auxiliary gauge-unfixing, spectral relational
homogeneous momenta, exact joint constraint group and positive physical norm.
It does not exchange H_vp for the different Round14 off-shell expression.

The key is an explicit measurable unitary built from the already controlled
characteristic propagators. For a=bv!=0 set

    tau(c)=r.a/|a|^2,      c_perp=(r-tau(c)a,v),
    S(c)=V_c_perp(tau(c),0) exp(+i tau(c) A_+).

Propagator composition proves, as equality of full unitary groups and domains,

    H_vp=S(K_c+A_+)S*.

This is a representation of the SAME H_vp, not deletion of its interaction.
The zero-velocity subspace has positive codimension and measure zero. S is
unitary on the full kinematic L2 space, but is not assumed continuous at that
subspace. Crucially tau(delta c)=tau(c), so S(delta c)->I strongly for almost
every fixed direction. A dominated-convergence argument gives exactly the
previous Gaussian mean-square physical trace. An explicit scalar countermodel
rejects replacing that argument by unrestricted pointwise continuity.

With B=S A_+ S* and K_tilde=S K_c S*, the proper reducing clock tube is
P_0<0 and B-P_0^2/12 in (-e_*/2,e_*/2). B and K_tilde strongly commute;
B is NOT the instantaneous operator h(c), and K_tilde is NOT bare K_c.
The full clock operator is self-adjoint on its joint spectral multiplier
domain even though H_vp is unbounded below. No square root of H_vp is taken.

The common unitary W=U_g V_aux S Z* transports all domains and spectral
constraints at once. It yields the reference generator K_c+lambda, and
an absolutely convergent joint Haar average with physical norm

    <F(0,0,0), Pi_0 G(0,0,0)>.

No product of delta(c) with a merely measurable S is used. The quadratic
clock's half-density remains sqrt(6/omega), omega=sqrt(12A_+). Pi_0 need
not commute with A_+; the resulting clock-dependent readouts are not falsely
called an autonomous restriction to ran Pi_0.

The price remains the Round15 higher-order operator-square prescription,
the clock and negative sheet, energy zero, auxiliary gauge-unfixing and
relational momentum choices. Computing S uses full interacting propagation
for potentially arbitrarily large orbit time near bv=0. There is no local
or bounded-cost formula and no complete classical counterpart asserted here.

## The local-parent limit also works through the quadratic clock

The [spectator/clock proof](spectator-clock-round16/PROOF.md) supplies an
additional interface, not a claim that the local parent is already a lift
of the complete H_vp constraint model.

After the explicitly specified fast zero-point subtraction, the entire
finite-parameter parent family has the common lower bound e_m>0. This lets
the Round15 uncompressed quantum limit pass through both sqrt(12X) clock
dynamics and the inverse-quarter-power shell weight. An exact isometry
between weighted clock-slice spaces is

    J_clock=D_B J D_A^(-1),       D_X=3^(1/4) X^(-1/4).

It is norm preserving at finite parameters; dynamical intertwining is a
strong limit, uniform on compact clock-time intervals. The sequential
order remains eta->0 at fixed delta, then delta->0 at fixed finite lattice.
No simultaneous or volume-uniform limit is inferred.

The 4n+2 surviving free tensor coordinates are not dropped. For d=4n+2,
normalized Gaussian spectator momenta of variance sigma^2 per coordinate
give a genuine Hilbert-space approximation to the desired A_+ clock:

    error <= Q sqrt(3) sigma^2 sqrt(d(d+2))/(2sqrt(e_*)) ||v||,
    <S_extra>=d sigma^2/2,        sum <y_j^2>=d/(4sigma^2).

At fixed spectator energy epsilon, sigma^2=2epsilon/d and the total spatial
second moment is d^2/(8epsilon). The approximation therefore pays for low
energy with delocalization; it does not manufacture a normalizable zero-energy
vacuum. Independence of ordinary Hamiltonians does not factor their clock
square root. The correct weighted embedding and its error are proved too.

An OPTIONAL exact distributional reduction can impose spectator momenta zero
on the limiting free-spectator model. This is an additional constraint choice,
not a consequence of calling a symmetry gauge. It cannot be applied unchanged
at finite delta: an actual complement mode has nonzero restoring curvature.
Without the fast-energy subtraction even the clock shell weight has a
different limit. Its energy-origin prescription is physically consequential.

## The charged shift now carries the full neutral charge, not just its grade

The [charged-lift proof](charged-lift-round16/PROOF.md) solves the algebraic
mismatch T_s^4=T_(4s)!=I versus the finite code's T_fin^4=I by an explicit
covering representation, including the complete frozen lattice and cocycle.

For s=(1/2)^8 define

    j(x)=4 sum_(i=6)^8 x_i-2 sum_(i=1)^5 x_i,
    K=ker j,       L=K direct_sum Zs,
    L0'=K direct_sum Z(4s).

An explicit integral basis identifies every charge uniquely with
(u,m,r) in Z^7 x Z x {0,1,2,3}, x=Ku+(4m+r)s. A displayed cocycle phase
gives a unitary from this full covering space onto l2(L). A charged step
increments r, and r=3 carries m forward. Its fourth power is the neutral
winding shift, precisely as required by T_(4s), rather than the identity.
Every other neutral and charged translation also has its explicit cocycle
phase; replacing all directions by commuting plain shifts is rejected.

The actual finite QWZ code transporter admits this lift with its code
multiplicity retained. The positive diagonal charge energy is exactly
|Ku+(4m+r)s|^2/2, including its cross terms. With the bounded finite-cylinder
code Hamiltonian it defines a positive self-adjoint extended Hamiltonian.

This ADDS an unbounded winding register, seven neutral charge labels and a
declared global energy scale. They have not been derived from local QWZ
fermions. Charged step energy is unbounded, and the older transverse-cut
defect remains. The lift is not the missing microscopic spin-field scaling
limit, local charge generation, oscillator vertex theory or 4D chirality.

## Verification and actual remaining obligation

Run from the repository root:

    experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/run_round16.py

The runner separates three new checkers from six unchanged prerequisite
runs. Their exact group counts and any source checks are recorded with
commands, transcripts, interpreter versions and input/artifact hashes in
ROUND16_VALIDATION.json and the per-folder validation.json files.
Twenty isolated infrastructure fixtures run in normal and optimized parent
environments; children always have assertions enabled. These are regression
checks, not machine certification of the infinite-dimensional proofs.
The independent internal review is documented in [ROUND16_REVIEW.md](ROUND16_REVIEW.md),
not represented as external peer review. The runner's --check-manifests
only checks inventory, hashes and successful-record consistency.

The finite vertex/clock compatibility problem is now constructively solved
for the declared model. The common microscopic TFPT parent remains unproved:
one must still derive the prescriptions and local observable algebra,
identify the charged scaling fields, lift the local-parent limit to the full
constraint structure, and establish the chiral/flavor/measure and uniform
relativistic continuum properties on that same object. Three mathematical
bridges are not silently added together and called a full TOE. T1--T8 remain
open as complete physical contracts. RH is out of scope.
