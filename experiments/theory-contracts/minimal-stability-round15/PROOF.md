# Sharp minimal-stability selection of the actual finite TT completion

2026-09-06. Non-RH, finite-regulator theorem. This derives a least
stabilizing physical correction under explicit hypotheses; it does not
derive those hypotheses, the microscopic TFPT Hamiltonian, or the Round-14
off-shell constraint-ideal completion from TFPT.

## 1. Result and assumptions

The previously chosen correction is not an arbitrary coefficient within
the following precise class. Fix the existing scalar/TT kinetic energy,
free quadratic energy, and prescribed first-order stress vertex. Permit
only a real scalar-coordinate homogeneous quartic correction at order g².
Then, at every fixed nonzero coupling, the unique pointwise least
classically **or quantum-mechanically** lower-bounded completion is

    R_min(phi) = T(phi)^T L^-1 T(phi)/2.                       (1)

All allowed stabilizing corrections are exactly

    C_4(phi) = R_min(phi) + W_4(phi),  W_4(phi)>=0.            (2)

Thus stability supplies a sharp lower envelope, not uniqueness of every
stable theory. Choosing the least correction eliminates W_4; that last
minimality requirement remains an explicit selection principle.

The hypotheses are important. The theorem does not assume arbitrarily
small g, does not scan amplitudes only in a bounded box, and does not
replace the quantum Hilbert space by a finite matrix. Conversely, it
does not classify momentum-dependent or Q-dependent corrections, changes
to the kinetic metric, higher-degree terms, or unrestricted dependence
on g. Section 6 gives exact counterexamples if these restrictions are
silently dropped.

The input is the same finite connected periodic lattice of n sites,
spacing a>0, m>=0, with all n scalar coordinates and M=2(n-1) retained
nonhomogeneous TT coordinates. Let

    L=diag(ell_alpha),  ell_alpha=r_alpha²>0,
    V_m(phi)=m²||phi||²/2+||D phi||²/2>=0.

The actual Ward stresses give real homogeneous quadratic T_alpha(phi),
independent of scalar momenta and m. This is the trace cancellation proved
in [the actual quantum-domain contract](../local-positive-auxiliary/QUANTUM_DOMAIN.md).
It is essential: replacing these multiplication operators by arbitrary
noncommuting stress operators changes the problem.

For a real homogeneous quartic polynomial C_4, define

    H_C = (||P||²+||pi||²)/2 + V_m(phi)
          + Q^T L Q/2 + g Q^T T(phi) + g² C_4(phi),          (3)
    H_C,min = -Delta_(Q,phi)/2 + V_C(Q,phi)

on C_c^infinity(R^(M+n)), initially as a symmetric differential operator.
The homogeneous-quartic ansatz follows, for example, from requiring a
polynomial correction of degree at most four, invariance under phi -> -phi,
and no additional constant or quadratic term. It also follows from a
quadratic functional of the actual quadratic stresses. These are
restrictions on the admissible completion class, not consequences of
stability alone.

## 2. Sharp equivalence at one fixed nonzero coupling

**Theorem.** For every fixed real g!=0, the following are equivalent:

1. C_4(phi)>=R_min(phi) for every real phi.
2. The complete classical Hamiltonian (3) is nonnegative everywhere.
3. The complete classical Hamiltonian (3) is bounded below.
4. The quantum quadratic form of H_C,min is bounded below on its unit
   vectors in C_c^infinity.
5. That quantum quadratic form is nonnegative.

Under these conditions H_C,min is essentially self-adjoint, its unique
closure is nonnegative, and the classical Hamiltonian flow exists for
all real physical times. The conclusions hold at this fixed finite
regulator; no volume-uniform bound or continuum limit is asserted.

**Classical proof.** Complete the actual TT oscillator square:

    H_C = (||P||²+||pi||²)/2 + V_m(phi)
          +(Q+g L^-1 T)^T L(Q+g L^-1 T)/2
          +g² [C_4(phi)-R_min(phi)].                         (4)

This proves 1=>2=>3. If condition 1 fails at u, write
delta=C_4(u)-R_min(u)<0. For t>0 take

    phi=t u,  Q=-g t² L^-1 T(u),  P=pi=0.

Homogeneity gives the exact energy

    H_C=t² V_m(u)+g² t⁴ delta -> -infinity.                  (5)

The nonnegative quadratic matter potential cannot compensate a negative
quartic defect at arbitrarily large field amplitude. Hence 3=>1.

**Quantum necessity without a spectral cutoff.** Take normalized real
product Gaussians with fixed unit widths, configuration covariance I/2,
zero momentum means, and the same centers (t u,-g t²L^-1T(u)). They are
genuine vectors of L2(R^(M+n)), not finite-dimensional CCR replacements.
For a polynomial of total degree at most four its expectation is exactly

    E_G[V_C]=[V_C+Delta V_C/4+Delta² V_C/32](center).         (6)

The expected kinetic energy is the constant (M+n)/4. The first term of
(6) is (5). The trace correction from g Q.T is at most O(t²), since
Delta_phi T is constant and Q_center=O(t²). The correction from C_4 is
O(t²)+O(1). The free quadratic terms contribute a constant. Therefore

    <G_t,H_C G_t>=g² delta t⁴+O(t²)+O(1) -> -infinity.       (7)

For the actual nonzero-momentum source Delta_phi T_alpha=0, so its cubic
trace correction vanishes exactly, but this extra fact is not needed
for the leading-order argument. Every Gaussian is approximable in the
graph norm of this polynomial differential expression by compactly
supported smooth cutoffs: all derivative and polynomial-weighted tails
decay exponentially. If the form on C_c^infinity had a lower bound, the
same bound would hold on each Gaussian by this graph approximation,
contradicting (7). Thus 4=>1. This also excludes any lower-bounded
self-adjoint extension of the same minimal expression when 1 fails;
it does not calculate deficiency indices or assert that no extension
exists. The implication 1=>5 follows by integration by parts and (4),
and 5=>4 is immediate. QED.

**Existence consequences.** Under 1, V_C is a smooth nonnegative
polynomial. The compact-cutoff proof already supplied in the linked
quantum-domain contract applies verbatim: if (H_C,min^*+1)u=0, elliptic
regularity and a cutoff chi_R give

    ||grad(chi_R u)||²/2 + integral (V_C+1)chi_R²|u|²
       = integral |grad chi_R|² |u|²/2 <= const ||u||²/R².

Thus u=0. The closed symmetric operator A>=0 has closed range A+1,
the zero adjoint kernel makes that range dense, and surjectivity proves
A=A*. This establishes essential self-adjointness, not just a choice
of Friedrichs extension. Polynomial multiplication and differentiation
put Schwartz space in the maximal domain, and its inclusion of the
compact core makes it an operator core. No invariance of Schwartz
under the unitary evolution is needed.

Classically conservation of energy E bounds every canonical momentum
by sqrt(2E). The configuration velocity is precisely that momentum,
so every configuration coordinate stays bounded on a finite time
interval. The polynomial vector field is bounded on the resulting
compact phase-space region. The ordinary continuation theorem therefore
gives existence for all real times, including m=0 without discarding the
uniform scalar. This statement does not require a normalizable massless
ground state.

## 3. What is and is not uniquely selected

Let P_4 be the cone of nonnegative real homogeneous quartic polynomials.
The theorem classifies the entire admissible family as R_min+P_4. In
the pointwise order, R_min is its unique least element and consequently
its only minimal element: every other member has the smaller admissible
element R_min. For example R_min+epsilon (d.phi)^4 is stable for every
epsilon>=0; taking d of zero mean also preserves uniform-scalar shift
invariance. Stability and that symmetry alone therefore do not force
epsilon=0.

For the restricted scalar-coefficient family C_4=kappa R_min, if the
actual source is not identically zero, the exact threshold is kappa>=1.
The full source checker below supplies a nonzero witness, so kappa<1
cannot be rescued by matter mass, a fixed ultraviolet regulator, or
quantum zero-point energy. No perturbative small-g assumption is used.
At g=0 all C_4 drop out and no selection is possible; that degenerate
case is deliberately excluded from the equivalence theorem.

There is also a source-independent variational characterization:

    R_min(phi)=sup_Q {-Q^T LQ/2-Q.T(phi)}.                   (8)

The supremum is attained uniquely at Q=-L^-1 T(phi). Equation (8)
derives the inverse-Laplacian kernel from the already fixed TT stiffness
L and the already fixed source map T; it does not derive either input.
For an independent source j, a quadratic correction j^T A j/2 makes

    Q^T LQ/2+Q.j+j^T A j/2>=0 for all Q,j

if and only if A-L^-1 is positive semidefinite. Thus L^-1 is the unique
least matrix in that stronger, independent-source problem.

For the **actual** source j=T(phi), only
T(phi)^T(A-L^-1)T(phi)>=0 is required. The actual source image is not
assumed to fill source space; matrix positive semidefiniteness is not
a necessary inference. On the actual L=2 lattice nine of fourteen TT
source polynomials vanish identically although all fourteen TT
oscillators are retained. Lowering A on such an invisible direction
leaves the exact scalar correction unchanged. This supplies an actual
counterexample to uniqueness of its matrix representation. The least
**function of phi** remains unique. A further independent-source model
T=(x²,y²), A-I=[[0,1],[1,0]] has an indefinite matrix difference but
T^T(A-I)T=2x²y²>=0. Do not replace positivity on the source image by
a stronger matrix assertion without an explicit hypothesis.

## 4. Exact full-source quantum threshold witness

The checker uses all eight scalar coordinates, all fourteen retained TT
coordinates, and the original staggered Ward frontend on the 2³ torus,
with a=1 and m²=2. Every reconstructed source is compared exactly with
that frontend. For u=delta_000 it proves

    V_m(u)=4,
    R_min(u)=3/256,
    (Delta_phi R_min)(u)=43/144,
    Delta_phi² R_min=43/9.                                 (9)

The three nonzero source values on this datum are 1/4 at the first
polarizations of momenta (0,1,1), (1,0,1), and (1,1,0), each with
ell=8. Other sources can vanish on this datum or identically at this
regulator; none of the fourteen free TT oscillators is dropped.

For C_4=kappa R_min, center unit-width Gaussians at
phi=t u and Q_alpha=-g t²T_alpha(u)/ell_alpha. Formula (6) gives exactly

    <H_kappa> = 3g²(kappa-1)t⁴/256
                +(4+43kappa g²/576)t²
                +91/2+43kappa g²/288.                     (10)

The constant 91/2 includes all 22 configuration kinetic contributions
and every quadratic oscillator Hessian. The checker derives the entire
formula, not only its leading sign, in two ways: direct polynomial
Gaussian contraction and independent contractions of each quadratic
stress Hessian. It includes explicit negative kappa<1 controls and
confirms that kappa=1 removes exactly the destabilizing t⁴ coefficient.

This is an analytic variational certificate for unbounded quantum
expectations when kappa<1. It supplies no finite-matrix approximation to
the interacting spectrum, no convergence rate for a continuum limit,
and no computationally efficient general algorithm for recognizing
nonnegative quartics in an arbitrary number of variables.

## 5. A broader all-coupling statement

Without quartic homogeneity, let C(phi) be real continuous and independent
of g (locally integrable suffices for defining compact-support forms,
but continuity is used here). Keep the same kinetic and other terms.
At each fixed g,

    inf_(Q,P,pi) H_C = V_m(phi)+g²[C(phi)-R_min(phi)].        (11)

Thus the residual in (11), not C>=R_min by itself, is the exact
classical condition for positivity or lower boundedness at that g.

Nevertheless the following stronger demand recovers the same envelope:
if the quantum forms obey one g-independent lower bound for **all real
g**, then C(phi)>=R_min(phi) everywhere. In particular this follows
from nonnegativity for all couplings. Conversely C>=R_min makes all
the forms nonnegative by (4).

To prove necessity, suppose C(u)-R_min(u)<0. Choose one normalized
real compact-support scalar test f localized sufficiently closely to
u. By continuity,

    a_f=<f,C f>-<f,T f>^T L^-1<f,T f>/2<0.

Take a fixed normalized real compact-support TT test h of zero mean
and translate its center to -g L^-1<f,T f>. Its exact total expectation
is b_f,h+g²a_f, with b_f,h independent of g. It tends to minus infinity
as |g| grows, contradicting any uniform lower bound. No interchanging
of coupling and regulator limits is involved. The test f is fixed
after localization; no neglected g-dependent localization cost occurs.

This is stronger than merely asking for a possibly g-dependent lower
bound at every g. Such ordinary per-coupling semiboundedness does not
imply C>=R_min outside the homogeneous-quartic class.

## 6. Exact negative controls against overclaiming

**Matter compensation at fixed coupling.** Let
C=R_min-epsilon V_m with epsilon>0. At any fixed g satisfying
g²epsilon<=1, (4) has residual (1-g²epsilon)V_m>=0, although C<R_min
where V_m>0. The correction now contains a quadratic term and is not
in the theorem's homogeneous-quartic class. This preserves the free
g=0 operator and the first coupling vertex but changes the second-order
quadratic term. The changed hypothesis cannot be hidden.

**Quantum zero-point compensation.** For each fixed phi the shifted
TT oscillator has the same lower bound
E_TT=sum_alpha sqrt(ell_alpha)/2. Integrating that oscillator inequality
over phi and adding the nonnegative scalar kinetic/potential energy
proves A_+>=E_TT as a quadratic-form inequality. Consequently
C=R_min-c with 0<g²c<=E_TT gives a nonnegative quantum operator
A_+-g²c, despite its classical value -g²c at phi=Q=P=pi=0.
It is still semibounded for every g, with a g-dependent lower bound.
This constant correction is outside the homogeneous-quartic class.
Zero-point energy cannot repair the negative leading t⁴ coefficient
of (10), but it can compensate an additive negative constant.

**Higher-order compensation.** C=R_min-a||phi||²+b||phi||^6,
with a,b>0, is smaller than R_min at small nonzero phi yet yields a
classically lower-bounded residual at every fixed g. Completing the
square shows that its potential is bounded below; shifting by that
finite lower bound gives the same unique self-adjointness argument.
This example changes the allowed polynomial degree and cannot refute
the sharp quartic theorem. No claim about all-coupling uniform lower
boundedness is made for it.

**Nonzero-coupling and actual-source controls.** At g=0 the entire
correction is invisible. An identically zero stress witness cannot
establish the threshold kappa>=1. The checker uses the nonzero full
delta-profile witness (9) and separately records the actual nine
identically zero source polynomials instead of counting them as
interaction evidence.

## 7. Interface with the existing construction and remaining scope

The selected least correction is exactly the term in the existing
[local constrained auxiliary realization](../local-positive-auxiliary/README.md)
and [first-class quantum completion](../firstclass-completion-round14/PROOF.md).
No new independent physical model is added. In the restricted class,
the least-stability principle selects the same physical A_+ already
used there, including its complete quantum and classical existence.
It reduces the previously arbitrary positive coefficient to a sharp
endpoint with a proof of necessity. The local auxiliary equations give
one realization of that endpoint; their microscopic selection and
uniqueness do not follow from (1).

The declaration of the admissible correction class and the choice of
the least member are still assumptions. This theorem does not select
the Round-14 changes to the unphysical constraint-ideal dynamics, restore
homogeneous gravity, derive chiral matter or flavor, prove relativistic
locality, or establish a continuum/infinite-volume limit. None of T1--T8
or the full TOE is promoted by this bounded result.

## Reproduction and source context

In the integrated layout run `python3 minimal_stability_check.py`.
Scratch use requires `--contracts-root PATH` pointing to the existing
`experiments/theory-contracts` directory. The checker is fail-closed,
uses exact SymPy arithmetic, prints source hashes, and does not write
the repository. The proofs above establish the all-finite-volume
theorems; the actual L=2 calculations are source and algebra regression
checks, not a proof by sampling field amplitudes.

The nonnegative Schrödinger-operator context is also documented in
Barry Simon's primary article [Schrödinger semigroups](https://doi.org/10.1090/S0273-0979-1982-15041-8)
and its [author-uploaded text](https://www.researchgate.net/publication/243072615_Schrodinger_semigroups).
The only self-adjointness criterion used here is proved explicitly
above and in the existing actual-domain contract. The sharp stability
selection, scaling and Gaussian negative controls are derived here;
no theorem for arbitrary noncommuting stresses is imported.
