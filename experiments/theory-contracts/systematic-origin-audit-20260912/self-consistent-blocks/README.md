# Exact local readjustment, first-stage uniform energy control, and the time gap

12 September 2026. NON-RH. This continues the primitive block work without
assuming that a fixed block encoding or a weak-link hierarchy reproduces itself.
All results concern an explicitly stipulated compiler-based model, not a
selected physical TFPT theory.

## 1. The changing block is exactly a two-coordinate problem

The previous second-order calculation generated a ten-word pair term and a
same-copy next-neighbor term. On three alternating registers, define

    H(u,v)=H4(12)+H4(23)+u[H10(12)+H10(23)]+v N13,
    H10=5H4-H4^2,
    N13=sum_i a_i tensor I tensor a_i,   a_i=i g_i.

The smallest common invariant space containing the previous ground encoding
has dimension eight: two multiplicity coordinates, each carrying the original
four-dimensional logical factor. This enclosure is exact, not an approximate
choice of eight states. With orthonormal embeddings G_minus and G_plus,

    H(u,v)|hull = (m I2 - a sigma_z - b sigma_x) tensor I4,
    m=4+13u/2+v,   a=sqrt(6)(1+u),   b=(u+2v)/2.

The two energies are m+-r, where r=sqrt(a^2+b^2). Near the original point,
the adjusted lower-branch embedding is

    G(u,v)=cos(theta) G_minus + sin(theta) G_plus,
    cos(2theta)=a/r,   sin(2theta)=b/r.

Thus the local readjustment needs a single mixing angle. The old encoding
remains an eigen-encoding exactly on u+2v=0; it is the lower branch there
if u>-1. The positive couplings generated earlier do not lie on that line.

The lower branch is guaranteed to be the ground space of the full
64-dimensional block, rather than just of the hull, whenever

    12|u|+8|v| < sqrt(6)-2.

This follows by centering the ten-word interaction and applying an eigenvalue
perturbation bound. It is sufficient, not a complete phase diagram. Outside
it the hull remains invariant, but another sector could have lower energy.
See [block_family.md](block_family.md) for the exact Gram, action matrices,
minimality proof, and branch construction.

The two coordinates here are multiplicity coordinates of a finite block.
They have not been identified with physical spacetime coordinates or a new
fundamental qubit of nature.

## 2. The entire adjusted boundary map is explicit

The main checker independently reconstructs both embeddings from the original
source and evaluates all sixteen compiler words on both ends. No word is mixed
into another direction. If its original Clifford degree is k, the adjusted
boundary compression multiplies it by lambda_k:

| degree k | lambda_k(u,v) |
|---|---|
| 0 | 1 |
| 1 and 3 | (sqrt(6)/4) a/r |
| 2 | 7/12 + b/(12r) |
| 4 | 1/2 + b/(2r) |

These follow from exact two-coordinate response matrices, not a fitted
interpolation. At u=v=0 they reproduce the preceding full sixteen-word map.
For u>-1 close to zero,

    theta=(u+2v)/(4sqrt(6))+O((|u|+|v|)^2).

The primitive degree-one transport changes only at second order in the small
mixing angle, while degree-two and degree-four transport already change at
first order. A moving state therefore does not imply the same first-order
change in every observable. Degrees refer to the original compiler word basis,
not automatically to physical spacetime tensor types or Lorentz chirality.

Along the leading normalized couplings from the previous calculation,

    u=(16B/3)epsilon+O(epsilon^2),
    v=(8C/3)epsilon+O(epsilon^2),
    B=34101sqrt(6)/822272, C=9sqrt(6)/512,

the angle slope is exactly 16185/205568. This is the tangent of the truncated
local-family response; it is not an exact repeated RG flow of the original
microscopic Hamiltonian.

## 3. Complete second-order first step on any finite open chain

Let N nonoverlapping original trimers form an alternating chain with weak
interblock links epsilon. Write e0=4-sqrt(6), and retain the exact constants

    A=927307sqrt(6)/6167040,
    B=34101sqrt(6)/822272,
    C=9sqrt(6)/512.

On the logical chain define H4,e and H10,e on each nearest-neighbor edge.
Define N_j on blocks j and j+2 with identity on the middle block; both outside
factors have the same orientation. Even starting blocks use the complex
conjugate version of the previously computed same-copy term.

The entire canonical second-order first-step polynomial is

    H_eff,N^(2) = N e0 I
      +(N-1)[(5/4)epsilon-(A+6B)epsilon^2] I
      +[(3/8)epsilon-2B epsilon^2] sum_edges H4,e
      +2B epsilon^2 sum_edges H10,e
      +C epsilon^2 sum_(j=1)^(N-2) N_j.

Why this is complete at this order, for every finite N:

1. Both perturbations on one edge give the already computed two-block term.
2. Perturbations on adjacent edges give the already computed shared-middle
   term. Only the shared block may be excited between the two operations.
3. Two disjoint edges cannot contribute: an excitation created on one edge
   cannot be removed by an operation on the disjoint edge before projection
   onto the tensor-product ground space. A ground-only intermediate state
   is excluded by the reduced resolvent.

These exhaust all ordered pairs of edges. The all-N statement is a support
and projector argument using the exact two- and three-block coefficients,
not an extrapolation from numerical chain lengths. It assumes open chains
of complete trimers; other boundaries must be treated explicitly.

### A length-independent ground-energy error per block

Treat a trimer as one 64-dimensional site. Its shifted onsite operator is
positive with a fourfold zero eigenspace, gap Delta=sqrt(6)-2 and norm
2sqrt(6)=(6+2sqrt(6))Delta. Onsite terms act on disjoint factors. Each weak
edge operator has norm 4 and the chain degree is at most two, hence the local
perturbation strength is at most 8, independently of N.

These properties meet the local many-body SW hypotheses. Theorems 1 and 3
of [Bravyi–DiVincenzo–Loss, §4](https://arxiv.org/pdf/1105.0675) imply constants
c,epsilon_*>0 independent of N such that, for |epsilon|<epsilon_*,

    |E_min(H_micro,N)-E_min(H_eff,N^(2))| <= c N |epsilon|^3.

This gives a uniform ground-energy error per block. Numerical values of c
and epsilon_* have not been extracted. The theorem is applied analytically;
the finite scripts do not prove it. This does not give a uniform isolated
4^N-dimensional perturbed band, ground-state fidelity, a complete spectrum,
or reduced real-time accuracy. Computing E_min of the effective chain is
itself still a separate many-body problem.

## 4. Why a second iteration is not yet controlled

Microscopic links with pattern 1,1,epsilon yield logical nearest-neighbor
links all of order epsilon after the first blocking. New logical triples
therefore have both internal couplings and external links on the same scale.
Dividing the whole Hamiltonian by epsilon cannot create a new weak-link ratio.

There is also inherited truncation error. Before normalization it is of
third order. After division by the leading coupling it is second order.
If a second weak-link parameter is also epsilon, this unknown contribution
is the same order as the second-stage correction one is trying to determine.
A ground-energy bound alone does not supply the state or interaction-norm
control needed to perform that step.

An acceptable repeated construction must therefore either supply an actual
second scale hierarchy, with its source justification and accumulated error,
or provide a genuinely nonperturbative reduction. An exact local G(u,v) is a
useful ingredient, but neither creates the hierarchy nor removes the omitted
first-stage terms. No extra hierarchy is silently imposed here.

## 5. The anchor is not the physical time direction

The original source constructs Lorentz gamma matrices with

    gamma0=f=g1g2g3,
    a_source=g4=gamma0 gamma1 gamma2 gamma3.

Thus i a_source is chirality in that frame. The source simultaneously admits
an equally family-covariant Euclidean frame. An explicit boost changes gamma0
while preserving the anchor. This proves neither physical signature nor clock
selection. The four original comparison directions have not been identified
as a physical Lorentz four-vector.

A narrow mathematical obstruction clarifies the issue: a fixed real
quadratic form invariant under all Lorentz rotations and boosts is a multiple
of the indefinite metric eta. If it is also positive semidefinite, it must
vanish. This is not a no-go theorem for positive energy or relativistic physics.

Given a unit timelike observer vector n, a simple positive construction is

    Q_n(x)=2(n dot x)^2-x dot x,
    G_n=2 eta n n^T eta-eta.

It is Euclidean in the observer's rest frame and satisfies
Q_(Lambda n)(Lambda x)=Q_n(x). The observer and compared vector must both
transform. Its physical source realization remains missing: a formal gamma
matrix is not yet a physical timelike field or a generator of evolution.
See [frame_time.md](frame_time.md); `observer_form.py` now persists the exact
source-frame, boost, invariant-form, and observer-form checks independently.

## 6. Evidence and next acceptance

Run `python3 -B run_checks.py` for three source-pinned checkers, each replayed
normally and under `-OO`. The adjusted ground and transport calculations
are exact symbolic identities. Symbolic equality is checked by an exact
simplified residual, including a small-nonzero negative control; it is not
replaced by a numerical tolerance. `verification.json` records hashes and
outputs. Earlier primitive results are replayed separately.

The next decisive acceptance is a source-justified or nonperturbative second
step with observable and accumulated-error control, alongside an operational
identification of time/observer structure. All T1–T8 completion claims remain
false. No RH, factoring, P versus NP, or Hylæan capability claim is made.

### Subsequent uniform-coupling test

The [uniform-chain continuation](../uniform-chain/README.md) now gives an
all-length variational obstruction to reusing the fixed tensor-G encoding
at equal couplings. It also identifies the exact known gamma-chain model
and a dimer comparison parent. These later results do not invalidate the
weak-link calculation above; they delimit its extrapolation to the uniform
chain. The source selection and physical-time obligations remain open.
