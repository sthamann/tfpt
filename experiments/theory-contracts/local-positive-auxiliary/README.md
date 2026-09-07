# Round 10: local constrained realization of the positive TT completion

## Result and scope

For the fixed finite periodic staggered lattice, the chosen term

\[
R[\tau]=\tfrac12\langle\tau,P_{\rm TT}(-\Delta)^{-1}\tau\rangle
\]

has an exact realization by **local, real, nondynamical constrained
auxiliaries**. The local equations accept the unprojected stress tensor; the
TT projector appears only after solving those equations. On the constraint
surface, the *full* TT-plus-stress potential is a positive square before
elimination. The static auxiliaries have no time derivatives. The subsequent
[finite second-class embedding](SECOND_CLASS.md) introduces canonical
auxiliary pairs and then removes every one by its regular constraints.
A full first-class gravity/matter mode count is not established.

In contrast, ordinary unconstrained minimization of healthy real Gaussian
auxiliaries induces a negative Schur term. This sign obstruction is exact;
with a bounded volume-independent local source contact it also excludes a
positive inverse-gradient-squared pole on arbitrarily large lattices.

The construction here starts as a local static variational parent for the
chosen reduced completion; [SECOND_CLASS.md](SECOND_CLASS.md) completes its
finite auxiliary classical stabilization. It is not a local relativistic theory,
not a first-class Dirac realization of the enlarged variables, and not a
derivation of the chosen completion from TFPT. The finite-volume exclusion
of homogeneous gravity remains explicit. No RH assertion is involved.

## 1. Fixed lattice operators and source

Use the orthonormal tensor order `(11,22,33,23,13,12)` and the masks of
Round 7. The scalar lattice operator is
`ell=-Delta=sum_i (D_i^+)^T D_i^+`, acting identically on each tensor
component. Its nonzero Fourier eigenvalue is
`r^2=sum_i kappa_i^2`, `kappa_i=2 sin(a k_i/2)/a`.

Let `V` be the local staggered tensor divergence already used for the vacuum
vector constraint. Its diagonal component blocks are `D_i^+`, and its
off-diagonal blocks are `D_j^-/sqrt(2)` in row `i`. Put

\[
t=(1,1,1,0,0,0)^T,\qquad N(v,\chi)=V^\dagger v+t\chi.
\]

`N` has only first-order difference blocks and an onsite trace block.
On each nonzero momentum, `ker N^dagger=ker V intersect ker t^dagger`
is exactly the two-dimensional TT space. Denote its orthogonal projector
by `P`. No local formula for `P` is assumed.

Introduce 18 real fields `E_(i,A)`, one oriented link field for each of the
six tensor components `A`. The link in direction `i` has the tensor mask
with bit `i` flipped. Let `D` be its componentwise staggered divergence into
the six tensor components. This is a first-order local operator and

\[
D D^\dagger=\ell I_6.
\tag{1}
\]

Tensor indices and space are implicit in inner products. All shifts commute,
so `ell` commutes with `V,N,P` on the nonzero-mode space. The same assertions
hold in physical-position Fourier coordinates: `V=i B`, with

\[
BB^T=(r^2I+\kappa\kappa^T)/2,\quad Bt=\kappa.
\]

After a harmless unitary phase of the three `v` variables one may use
`N=[B^T,t]` for a fibre calculation. Then

\[
\det(N^TN)=r^6/2>0,\qquad
P=I-N(N^TN)^{-1}N^T,\qquad \operatorname{rank}P=2.
\tag{2}
\]

All real-space placements are inherited from the explicit Round-7 masks;
the checker also verifies generic Laurent-symbol phase conjugacy. Boundary
and self-conjugate modes have `r>0` unless the whole momentum is zero.

## 2. Exact positive constrained static realization

For a real *unprojected* source tensor `tau`, minimize

\[
\frac12\|E\|^2
\quad\hbox{subject to}\quad
D E-V^\dagger v-t\chi=g\tau.
\tag{3}
\]

The fields `v` (three components) and `chi` (one component) are free slack
variables with no energy. The constraint and its source contain no TT
projection or inverse spatial operator. For now work at nonzero momentum;
section 4 gives the exact homogeneous compatibility condition.

Use the multiplier functional

\[
\mathcal F=\tfrac12\|E\|^2
-\langle\lambda,D E-Nu-g\tau\rangle,\qquad u=(v,\chi).
\]

Its stationary equations are

\[
E=D^\dagger\lambda,\qquad N^\dagger\lambda=0,\qquad
\ell\lambda-Nu=g\tau.
\tag{4}
\]

The multiplier becomes TT as a consequence of *local* equations
`V lambda=0`, `t^dagger lambda=0`. Applying `P` to the last equation gives

\[
\lambda_* =g\ell^{-1}P\tau,\quad
E_* =gD^\dagger\ell^{-1}P\tau,\quad
u_*=-g(N^\dagger N)^{-1}N^\dagger\tau.
\tag{5}
\]

The resulting minimum is

\[
\min_{(3)}\tfrac12\|E\|^2
=\tfrac{g^2}{2}\langle\tau,P\ell^{-1}\tau\rangle=g^2R[\tau].
\tag{6}
\]

This is constrained minimization over positive `E` energy. It is a saddle
in the multiplier, not minimization of a positive quadratic form over all
displayed fields. At a nonzero momentum, the symmetric KKT matrix in
`(E,u,lambda)` has inertia `(22 positive, 6 negative, 0 zero)`: eliminate
the positive 18-dimensional `E` block, then split the multiplier into four
`range N` and two TT directions. Each `u/range N` block has one sign of
each kind; the two TT multiplier directions are negative. The sign is not
hidden inside a purported healthy propagating scalar.

### The constrained fibre has many configurations but one minimizing E

Equation (3) is equivalent to `P D E=gP tau`. At nonzero momentum this has
two independent conditions on 18 `E` components, so its affine tangent
space is 16-dimensional. Every allowed field is uniquely

\[
E=E_*+\eta,\qquad P D\eta=0,
\qquad \langle E_*,\eta\rangle=0.
\]

Consequently its energy is `g^2 R+||eta||^2/2`. The minimizing `E` is unique;
the entire constraint surface is not a unique field configuration. In
particular `ker D` is contained in those tangent directions. Equation (4),
not the source constraint alone, sets them to zero. No dynamics is assigned
to these directions here. Adding canonical partners and kinetic terms
would require a new constraint and physical-degree-of-freedom count.

## 3. Positivity of the complete coupled potential before elimination

Let the existing gravity field `q` be TT and have zero mean. Its free
potential is `||D^dagger q||^2/2`, because (1) gives the ordinary
`sum_alpha r_alpha^2 Q_alpha^2/2`. On (3), local summation by parts and
`Vq=t^dagger q=0` imply

\[
g\langle q,\tau\rangle=\langle D^\dagger q,E\rangle.
\]

Thus the full constrained Hamiltonian functional

\[
H_{\rm loc}=H_m+\tfrac12\|p\|^2+
\tfrac12\|D^\dagger q\|^2+g\langle q,\tau\rangle+
\tfrac12\|E\|^2
\]

obeys the identity

\[
H_{\rm loc}|_{(3)}
=H_m+\tfrac12\|p\|^2+\tfrac12\|D^\dagger q+E\|^2\ge0.
\tag{7}
\]

Minimizing over `E,u` produces exactly the positive reduced Hamiltonian of
Round 9. More precisely,

\[
H_{\rm loc}|_{(3)}=H_{\rm red,+}+\tfrac12\|\eta\|^2.
\tag{8}
\]

The old TT oscillator coordinates remain in `q,p`; they have not been
integrated out and then reintroduced as a second copy. The new fields have
no time derivatives. A first-order variational action can use the original
matter and TT symplectic terms, `-H_loc`, and a local multiplier for (3).
Its auxiliary Euler equations are algebraic in time and elliptic in space.
Eliminating them preserves those original symplectic terms. This is an
exact finite static/auxiliary construction; it does not by itself classify
all its Dirac constraints or establish relativistic causal propagation. The
subsequent finite auxiliary-only classification is provided in
[SECOND_CLASS.md](SECOND_CLASS.md); it does not restore the original
unreduced gravity gauge sector.

## 4. Homogeneous compatibility and the precise optional slack

At `k=0`, `D=V=0`, whereas the trace column `t` survives. Therefore (3)
requires

\[
\overline\tau-\tfrac13t(t^T\overline\tau)=0.
\tag{9}
\]

There are exactly five missing traceless homogeneous source directions.
The trace mean is absorbed by `chi`; the three homogeneous `v` components
are null variables. This count differs from simply declaring all six
means incompatible.

To match the existing completion, which deletes homogeneous gravity and
its entire source contribution to `R`, one may either state that all of
(3) is on the nonzero-mode quotient, or give a fully local constraint
description with an additional traceless tensor `h`:

\[
D E-Nu-h=g\tau,\qquad D_i^+h=0\;(i=1,2,3),\qquad t^Th=0.
\tag{10}
\]

The last constraints are local and first order. They allow exactly five
spatially constant real slack parameters; minimization chooses
`h=-g trfree(mean tau)` and `mean chi=-g(t^T mean tau)/3`. Their energy is
zero. They implement deletion/bookkeeping of the homogeneous source, not
homogeneous gravitational reception or physical energy storage. Because
`q` is zero mean, (7) is unchanged. The homogeneous `E` is unconstrained
but minimized to zero; homogeneous `v` can be fixed to zero without
changing any value. A local constraint description of constant fields is
not a claim that a causal local evolution has solved their global value.

## 5. Ordinary healthy Schur elimination: exact sign and locality bounds

For real unconstrained auxiliary coordinates `a` and an independent real
source vector `j`, consider

\[
H(a,j)=H_{\rm seed}(j)+\tfrac12a^TKa+g a^TBj+
\tfrac{g^2}{2}j^TAj,\qquad K>0.
\]

Completing the square proves

\[
\min_aH=H_{\rm seed}+
\tfrac{g^2}{2}j^T(A-B^TK^{-1}B)j.
\tag{11}
\]

Without a direct `A` term, the induced correction is negative semidefinite.
Its rank is at most the number of coupled auxiliary directions. A rank-two
TT inverse-Laplacian residue requires at least two coupled directions;
with a uniformly positive auxiliary gap and bounded local couplings it
cannot have any inverse-Laplacian pole at all. If additional positive
kinetic energies make those directions physical oscillators, the required
gapless modes would be additional propagating content. They do not repair
the wrong induced sign.

More generally, for a fixed finite-range, translation-invariant parent with
finitely many species and volume-independent bounded coefficients, `A(k)`
is bounded near `k=0` and

\[
A(k)-B(k)^\dagger K(k)^{-1}B(k)\le A(k).
\]

Along a fixed direction the target has two positive eigenvalues `1/r^2`.
It cannot satisfy this bound as `r` tends to zero. Thus a bounded local
contact does not evade the sign problem uniformly over growing volumes.
The statement is about an identity for independent sources; it does not
assert that every arbitrary nonlinear matter parent is of this form.
For a source coupled linearly to general stable auxiliaries, ordinary
second-order perturbation about a stationary minimum has the same negative
Hessian susceptibility. A direct higher-order source interaction is an
extra assumption.

### Why a fixed finite-volume overclaim would be wrong

There is a scalar-channel counterexample to a stronger claim that no
finite-volume local Schur realization with a bare contact is possible.
Write `l=r^2` and choose

\[
K(l)=l(d l-1),\quad B(l)=d l-1,\quad A=d.
\]

Then `A-B^2/K=1/l` exactly, and `K>0` on a fixed retained spectrum if
`d>1/l_min`. These are finite-degree local symbols. But `K<0` for
`0<l<1/d`, so health fails on sufficiently large volumes unless `d` grows
with volume. The bare positive source contact has paid the diverging cost.
This example is not a construction of the full TT projector kernel; it
prevents extending (11)'s uniform obstruction to an unrestricted
finite-volume statement with arbitrary regulator-dependent contacts.

## 6. Actual scalar stress, quantum scope, and next dynamical obligation

The actual free-scalar stress has the form

\[
\tau_{ii}(x)=\tfrac12\pi_x^2-\tfrac12m^2\phi_x^2+
\sigma_{ii}(\phi),\qquad \tau_{ij}(x)=\sigma_{ij}(\phi)\;(i\ne j).
\]

Every real TT smearing kills the common diagonal kinetic and mass term.
Thus the actual `tau_alpha` are quadratic multiplication operators in
`phi`, and **all these TT stress operators strongly commute**. This is
narrower than the earlier general quadratic theorem, whose witness permits
noncommuting stresses. There is no noncommuting-stress Gauss-law no-go for
this particular TT source. Using the full unprojected stress in (3) is
legitimate; its common trace is absorbed by `chi` locally. Equivalently one
may use the local `sigma(phi)` after changing only the trace slack.

For this actual scalar input the elimination and (7) are pointwise
identities of multiplication potentials; the positive reduced
Schrodinger form already established in Round 9 applies. This is stronger
than a c-number external-source witness, but does not establish an
unreduced physical Dirac inner product, gauge algebra, or a self-adjoint
local enlarged Hamiltonian on all auxiliary variables.

Even with commuting TT source charges, a naive new Abelian Gauss generator
`G=div E-g tau(phi)` is not preserved by unchanged free matter dynamics:
`{G,H_m}=-g{tau,H_m}` is generically nonzero. In the simple quadratic test
`tau=phi^2/2`, `H_m=pi^2/2`, this is `-g phi pi`, nonzero on `G=0`.
Additional local couplings, constraints or multiplier equations are needed
if the nondynamical saddle is to become a first-class gauge theory.
Equally, the current TT restriction of `q,p` is a reduced description;
this artifact does not restore the entire unreduced gravitational sector.

Real unconstrained Euclidean Gaussian integration also has the Schur sign:
the integral of `exp(-a^T K a/2+g a^Tj)` generates
`exp(+g^2 j^T K^-1 j/2)`. The desired positive action term uses an imaginary
coupling `i g a^Tj`, or a constrained/multiplier formulation. Neither is a
positive real auxiliary oscillator minimization. Maxwell theory provides
the standard distinction: its time component is a Lagrange multiplier
enforcing Gauss' law, while the electric energy is nonnegative; see
[Tong, QFT, section 6.2](https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S6.html).
This reference is context for the distinction, not a proof that the tensor
system here inherits Maxwell's gauge dynamics.

## Reproduction and evidence boundary

Run `python3 local_auxiliary_checker.py` in this directory. The checker has
no repository imports and uses only exact SymPy operations. It checks the
Schur signs and finite-volume escape, generic TT rank/projectors, local
staggered phase symbols, constrained stationary solution and orthogonality,
the complete positive potential identity, a non-minimizing divergence-null
direction, the homogeneous count and slack, and the matter-stabilization
mutant. The universal sign, minimization, and degree-of-freedom arguments
are the proofs above, not extrapolations from matrix samples.

Audited source locations:

- `experiments/theory-contracts/constraint-dressing/README.md`, section 10
  (positive reduced form, source ordering, inverse `r_alpha^2`);
- `experiments/theory-contracts/free-scalar-3d/README.md`, equations R8.1–R8.3
  (common trace kinetic term and local configuration-only remainder);
- `verification/v1035_matter_coupling.py`, `tensor_data`
  (the actual `B,t,Kp,Kq` matrices and tensor normalization).

This folder is integrated as unpromoted research. The constructive conclusion is a local
static constrained representation with a nonnegative coupled energy, plus
explicit obstructions to reinterpreting it as an unconstrained healthy
oscillator parent. The remaining task is a dynamically consistent local
constraint realization, with its homogeneous sector and physical mode
count derived rather than assumed.


## Completed finite auxiliary stabilization

[SECOND_CLASS.md](SECOND_CLASS.md) gives an exact Hamiltonian realization
of the newly added auxiliaries as **second-class**, not first-class gauge,
variables. Its invertible KKT Hessian gives 56 second-class constraints
removing 28 added canonical pairs per retained real nonzero mode.
Seed Dirac brackets remain canonical even for the actual noncommuting
unprojected stress. All preservation multipliers are fixed, and the
finite constrained measure has no source-dependent auxiliary Jacobian.
The reduced Hamiltonian and its all-time classical flow are the same
positive completion. This classifies the auxiliaries, not the full
gravitational constraint system or the deleted homogeneous sector.

## Actual reduced quantum domain and vacuum

[QUANTUM_DOMAIN.md](QUANTUM_DOMAIN.md) treats the actual scalar stress as a
multiplication potential, rather than arbitrary Weyl-quadratic stresses.
It proves essential self-adjointness on compactly supported smooth test
functions and a Schwartz operator core. At fixed finite volume, positive
mass gives a unique ground state and compact resolvent. With mass zero and
the uniform scalar retained, the free uniform coordinate forbids an L2
ground state. These statements do not
supply an unreduced auxiliary physical Hilbert space or a TFPT initial-state
selection. See also the separate [CY boundary work](../cy-seam-round10/README.md);
no common microscopic parent joining these constructions is proved.

Reproduce all three distinct aspects with `local_auxiliary_checker.py`,
`second_class_checker.py`, and `quantum_domain_check.py`. The last keeps the
initially vanishing L=2 axial TT witness as a degeneracy control and requires
two nonzero, degree-two, normalized real TT witnesses on L=3. This prevents
trivial zero polynomials from passing as meaningful quantum-source tests.
