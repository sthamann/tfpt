# Non-RH TOE research: Round13, weak constraints and exact clock alternatives

Date: 2026-09-06. HEAD and actual remote main were reverified at
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`.
This round is locally integrated research, not a release, commit or push.
Earlier proofs/manifests and concurrent paper/ledger/v472 edits are preserved.
No T1–T8 gate is promoted and no RH or empirical claim is made.

## The decisive change since Round12

The previously open **weak** momentum-deformation question now has a definite
answer for the fixed actual model and seed: smooth time-independent weak
closure fails near a complete regular null torus, already at second order.
This does not follow merely from Round12's strong-conservation obstruction.
The new proof includes the shifted common zero surface and arbitrary smooth
structure functions.

Two constructive alternatives are also fully defined. Exact constraints exist
on small regular phase-space patches. Separately, the already-postulated trace
clock permits exact global classical and spectral-tube quantum relational
constraints while leaving the chosen Hamiltonian and quadratic clock formula
unchanged. Neither alternative is the original global spatial momentum system.

| Contract | Proved result | Boundary |
| --- | --- | --- |
| [Weak homogeneous constraints](weak-constraints-round13/PROOF.md) | A regular rank-three null torus has nonzero averaged forcing after full static-plus-exchange normal form. Even weak preservation of a smooth deformed zero surface is impossible there through order g squared. | Fixed time-independent seed and unchanged Hamiltonian; not a no-go for small flowboxes, added clock variables, singular deformations, or a different parent. |
| [Local constructive constraints](weak-local-construction-round13/PROOF.md) | A parameter-dependent canonical flow constructs exact strongly commuting constraints on a small regular patch of the actual model, with explicit nontrivial 3^3 and 6^3 source/rank witnesses. | No global extension across recurrent tori, preferred gauge interpretation, local spatial current, or quantum implementation is proved. |
| [Clock-assisted joint model](clock-shell-round13/README.md) | Complete classical relational charges and strongly commuting self-adjoint quantum constraints for the unchanged quadratic clock on a specified negative-sheet spectral tube; exact joint physical norm. A free-energy lower bound is uniform in coupling. | Clock, energy zero, sheet and relational momentum prescription remain chosen. The fixed physical initial-data subspace need not be invariant under the old rest-energy evolution. |
| [Covariant unreduced domains](covariant-domain-round13/README.md) | Actual affine characteristic operator, exact kinetic-signature crossing, necessary purely absolutely continuous full-real-line spectrum, and self-adjoint covariant Hermite-Galerkin approximants. | A self-adjoint strong-resolvent limit of those approximants at nonzero coupling is not proved; the full unreduced covariant quantum dynamics remains open. |

## 1. Weak closure: the missing shifted-surface calculation is now done

Allow

    C_i(g)=J0_i+g J1_i+g^2 J2_i+...,
    {C_i(g),H(g)}=M_i^j(g) C_j(g)+O(g^3),

with arbitrary smooth, time-independent corrections and structure functions.
After the common cubic normal form H'=H0+g^2 B+..., regular coordinates
j=J0 describe the deformed zero surface as

    j=g chi1+g^2 chi2+...,
    chi2=(partial_j F1)F1-F2.

The second term is the displacement correction absent from a naive reuse of
the strong-conservation equation. Normal action-coordinate derivatives commute
with the free vector field, including all unoccupied scalar and TT directions.
Weak preservation therefore requires the torus mean of {J0,B} to vanish.

The explicit torus occupies +/-k, +/-l and +/-h, where on side length six
k=(1,1,0), l=(2,5,0), h=(0,0,1). All six actions are one. The three momentum
constraints vanish, and their normal weight determinant is -3 sqrt(3)/4.
An exact enumeration of all 1,365 quartic monomials shows that only the old
charged quartet and its conjugate contribute to the three-phase mean. An
independent standard-library checker instead enumerates all 20,736 ordered
signed quartets: 444 survive phase and lattice-momentum selection, giving
23 distinct monomials, only two of which carry nonzero centered momentum.
Each of those two occurs in 24 permutations. A deliberately wrong conjugate
charge rule produces six spurious charged monomials and is rejected. At
m^2=4/7 the resulting vector is

    (301 sqrt(3)/599040, 0, 0),

not zero. The coefficient stays positive for all finite m^2>=0 and side lengths
divisible by six. Scaling the torus into arbitrarily small neighborhoods of the
origin preserves its regularity and nonzero forcing. Thus this specified weak
completion is ruled out even near the origin, not only for a selected ansatz.

## 2. Local solutions exist, but cannot be silently glued globally

Near a noncritical point, a Hamiltonian characteristic integral constructs a
local coupling-parameter symplectomorphism Phi_g with

    H_g composed with Phi_g=H_0+[H_g(z*)-H_0(z*)].

Then K_i=J0_i composed with Phi_g^-1 commute both with one another and with H_g.
The subtraction fixes the same base point; it is not a change to the physical
Hamiltonian or a chosen vacuum-energy subtraction. The actual regular source
point has rank d(H0,J0)=4 and nonzero first-vertex torque, so this is not a
zero-interaction example. At 6^3 that torque is 9 sqrt(6)/4.

A separate positive Hamiltonian on T*S1 x T*R^3 supplies an exact logical
control: it has a global weak constraint surface even though its strong
defining function has nontrivial monodromy. This confirms why the additional
actual-model argument in section 1 was needed. The local theorem does not
contradict the obstruction on a neighborhood of a complete recurrent torus.

## 3. A joint clock construction with exact domains and normalization

The actual positive Hamiltonian is a sum of the free matter operator and
shifted TT oscillator forms. Their separate form bounds add to

    A_g >= e_* = (sum_k omega_k+sum_alpha r_alpha)/2 > 0,

uniformly in g at fixed nontrivial regulator. This is an unsubtracted energy
bound, not an excitation gap above the interacting ground state.

Classically the full actual reduced flow Phi_g is complete. With the same
postulated C=H_g-p^2/12, p<0, set T=-6q/p. The exact relational charges
J0_i(Phi_g^(-T)z) commute with C and with one another, and recover J0 at g=0
or at the chosen clock origin. They depend on the clock and the full flow.

Quantum mechanically set lambda=E-p^2/12 and

    p_-(E,lambda)=-sqrt(12(E-lambda)),
    w(E,lambda)=6/sqrt(12(E-lambda)).

On I=(-e_*/2,e_*/2), the map Zf=sqrt(w) f(E,p_-) is unitary to L2(I) tensor H,
for any spectral type of A_g. It sends the **unchanged quadratic** C to lambda
multiplication. Thus Z*(I tensor J0_i)Z are precisely defined self-adjoint,
strongly commuting constraints. Joint averaging gives

    eta(f,h)=<(Zf)(0),Pi_0 (Zh)(0)>,
    H_phys=intersection_i ker J0_i.

At the shell w=6/omega, exactly the prior quadratic-clock normalization.
Because Pi_0 and A_g need not commute, the two square-root weights must stay
on their respective sides of Pi_0. The proof and checker explicitly retain
that ordering. The global Fourier normalization of solution readouts is also
declared; no self-adjoint clock-position operator on the restricted tube is
assumed.

The price is a new, generally nonlocal clock-relative momentum prescription.
These are not the old spatial currents, nor a microscopic derivation of the
clock. The original A_g need not preserve the fixed H_phys; its exponential
must not be advertised as an autonomous Hamiltonian on that subspace. Local
observable compression and continuum locality remain separate problems.

## 4. What remains in the unreduced quantum-domain problem

The actual propagation matrix has A^2=0, rank n-1 and affine characteristics.
The full unreduced fiber contains an actual time-dependent quadratic matter
coefficient in addition to its cubic TT interaction. On the checked actual
mode the matter kinetic matrix loses rank at s=32 sqrt(2)/3 for g=1 and then
becomes indefinite. Its different-time Hamiltonians do not commute. Scalar
phases and a bare quadratic-metaplectic argument therefore fail as proposed
shortcuts. For each fixed oscillator power N^k, k>=1, the specific global
linear commutator estimate

    |<f,i[h,N^k]f>| <= C <f,N^k f>

also fails. This does not exclude other coupled-moment estimates or all
possible propagator arguments.

Any genuinely covariant self-adjoint extension must obey a Weyl domain
relation, forcing purely absolutely continuous spectrum R on the full-measure
regular kinematic sector. This does not contradict reduced positivity: the
physical constraint surface is not an ordinary nonzero L2 sector there.

The constructed covariant Galerkin Hamiltonians agree asymptotically with the
entire prescribed Schwartz expression. A self-adjoint strong-resolvent limit
on the same Hilbert space would retain both that expression and covariance.
Existence of this limit at nonzero coupling is the precise open step. Finite
Hermitian matrices, weak convergence, or arbitrary measurable self-adjoint
extensions do not supply it. The additional auxiliary-multiplier domain is
still another obligation.

## T1–T8 and reproduction

T1 dimension/geometry/scale selection, T2 common seam/parent identification,
T4 actual chirality and measure, and T6 physical flavor/analytic operator-family
identification are unchanged. T3/T7 gain exact restricted constraints and a
sharper domain target, not a common local nonlinear quantum gravitational
parent. T5 locality and controlled continuum/Lorentz limits remain open.
T8 gains a conditional joint physical norm, not microscopic state selection
or the complete common SK readout. All eight full gates remain open.

Run `experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/run_round13.py`
from the repository root. Five new mathematical checkers and six unchanged
prerequisites are recorded separately in `ROUND13_VALIDATION.json` and the
four folders' `validation.json` files. `test_round13_runner.py` retains 20
temporary-fixture infrastructure tests; normal and optimized-parent runs are
recorded separately in `ROUND13_RUNNER_VALIDATION.json`. The manifest command
`--check-manifests` checks current hashes, complete inventories and saved-record
consistency, not mathematical truth or a new test execution.

Main and independent reviews read the complete proofs. Separate source-based
checks reproduce actual stresses and normalization. Finite exact algebra,
functional-analytic proofs, conditional constructions and unresolved limits
are kept distinct; there are no floating-point regressions or finite CCR
approximations in the new checks. No aggregate count of physical facts is
inferred from the checker counts or the 1,365-monomial enumeration.

The systematic-debugging workflow caught an initial test-only error: a product
of inverse Jacobians was compared with zero instead of one. Independent
simplification gave exactly one; the assertion was corrected and rerun. This
did not alter the transformation, its Jacobian or the mathematical theorem.

Next decisive work: prove an appropriate strong-resolvent/propagator limit for
the actual unreduced characteristic family, and derive a physical momentum,
clock and local observable prescription from the same microscopic parent.
The restricted constructions here do not choose that prescription for TFPT.
