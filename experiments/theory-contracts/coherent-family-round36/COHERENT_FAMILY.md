# Uniform coherent-family reduction for the fixed physical cycle

**NON-RH / unpromoted conditional theory contract.** This extends the
prepared-state Round35 calculation to one common generator for an entire
specified input subspace. It is not a uniform spatial-lattice result, a
low-energy spectral field theory, or a physical T1-T8 closure.

## 1. A physical input family, not independent fitted initial states

Keep the inherited three-site U(1) cycle, three fermions, q_x=1, a=1/12,
beta=1/4, eta=1/2, kappa=1/100, M=4 and Vmag=0. The Gauss basis remains
(mask,k), with

\[
E_0=k+1-N_0,\quad E_1=k+2-N_0-N_1,\quad E_2=k.
\]

Let W map the standard basis of C^3 into

\[
|7,-1\rangle,\quad |7,0\rangle,\quad |7,+1\rangle.
\tag{1}
\]

Each state has one bare-low fermion per site and no bare-high fermion. The
three states belong to the **same Gauss/background-charge sector**, so their
coherent superpositions are physical. The cycle label is not superselected:
the gauge-invariant Wilson loop changes it, and the parent has virtual paths
connecting it. This is not a superposition of different external charges.

The input is any Wc with c in C^3 and ||c||=1, or W rho W^dagger for **any**
positive semidefinite 3x3 rho of trace one. The theorem covers all complex
coefficients, not only the rational examples evaluated by the standalone
calculator. Initial flux support is |E_l|<=1. Every state in the family has
<E_l^2><=1 and initial energy <=61/2400: W^dagger H_phys W is exactly
diag(61/2400,1/96,61/2400). This is a bounded-energy **preparation subspace**,
not the full spectral subspace below that energy, nor a selected vacuum.

## 2. One shared block space and certified proposal arithmetic

At cutoff K=13, the expanded physical parent has 528 basis states. As before,
expand A^2 monomials before flux compression. Write H=H_K-6I and
Hhat=14400 H. Use the joint block space suggested by

\[
\mathcal K_L(H,W)=\operatorname{span}\{W,HW,\ldots,H^{L-1}W\}.
\tag{2}
\]

The tested L=12,16,20 proposals have 36,48,60 directions. The basis is built
jointly from all three inputs, with repeated orthogonalization against all
earlier directions. Its reduced Hamiltonian has nonzero couplings between
directions descended from different seeds. It is not three separately fitted
one-state models or a direct sum of three independent chains.

Block Krylov methods for several right-hand sides are established; see
[Frommer, Lund and Szyld](https://epubs.siam.org/doi/10.1137/19M1255847).
The defect/Duhamel approach also has established precedent in
[Jawecki, Auzinger and Koch](https://arxiv.org/html/1809.03369v2).
The claims here concern the certified application to this parent and physical
input family, not the invention of either numerical method.

Unlike Round35's single-vector integer construction, the block basis is
**proposed** with 80-digit Decimal arithmetic, then rounded toward zero onto
the grid 1/S, S=10^30. Numerical orthogonality is not accepted as a proof.
Let V denote the resulting rational embedding, with columns stored as
integers divided by S. Check its Gram matrix G=V^dagger V exactly and set

\[
g\geq\|G-I\|,\qquad
g=\max_i\sum_j|G_{ij}-\delta_{ij}|<8\cdot10^{-29}
\tag{3}
\]

for the final model. Thus V has full column rank and ||V||<=sqrt(1+g)<=1+g.
The three input columns and their orthogonality to all later columns are
exact, so VJ=W, GJ=J for J selecting the first three coordinates. An exact
isometry is U=V G^{-1/2}; it also satisfies UJ=W. This is a useful underlying
Hilbert-space interpretation, but the implemented readouts use V with its
controlled roundoff, not an uncomputed matrix square root.

Form a symmetric rational A by rounding V^dagger H V on the same grid,
retaining only entries within the same or neighboring block layers. Set other
entries to zero. This layer truncation is **not assumed exact**: all its
effects, numerical proposal errors and deflation choices are included in the
subsequent exact residual check. Poor proposals cannot gain a small-error
certificate merely by carrying a layer label.

## 3. A uniform operator bound over the whole input space

The common auxiliary evolution is

\[
i\dot y=Ay,\qquad y(0)=Jc.
\tag{4}
\]

A is exactly Hermitian. Define R=HV-VA and upper bounds d_j>=||R e_j||,
computed from exact rational residual columns and outward integer-square-root
bounds. For any c, Duhamel gives

\[
(e^{-itH}W-Ve^{-itA}J)c
=-i\int_0^t e^{-i(t-s)H}R e^{-isA}Jc\,ds.
\tag{5}
\]

There is no initial mismatch because VJ=W exactly. Put B_ij=|A_ij| for i!=j,
B_ii=0. In the interaction picture of diag(A), each remaining phase has
modulus one, yielding

\[
|(e^{-isA})_{ja}|\leq(e^{sB})_{ja}.
\]

For a=0,1,2, enclose

\[
I_{ja}=\int_0^1(e^{sB})_{ja}\,ds
=\sum_{n=0}^{\infty}\frac{(B^n)_{ja}}{(n+1)!},\qquad
e_a=\sum_j d_j I_{ja}.
\tag{6}
\]

Compute the positive series through n=100. With rho the maximum row sum of
B, every remaining entry is bounded by

\[
\frac{\rho^{101}}{102!}\frac1{1-\rho/103}.
\tag{7}
\]

Here rho<9.662, so the tail is valid. All terms are exact rational numbers;
the tail includes every omitted path. For ||c||=1, equations (5)-(6) and
Cauchy-Schwarz imply the **operator** bound

\[
\|e^{-itH}W-Ve^{-itA}J\|
\leq \sqrt{e_0^2+e_1^2+e_2^2}=:\delta,
\quad 0\leq t\leq1.
\tag{8}
\]

This is not a maximum of three sampled errors, and it is not an inference
from three population measurements. It includes arbitrary relative phases
and all input directions. At L20,

\[
\delta<1.051\cdot10^{-18}.
\tag{9}
\]

The tests additionally compare the whole 528x3 embedded evolution matrix
against three independent full-H Horner columns; its Frobenius difference
provides a separate operator-norm check. That reference is not used to
construct A, V, the sources or the residual budget.

## 4. Complex response matrices preserve interference and mixtures

Compile all four original bounded Hermitian sources as O_tilde=V^dagger O V.
Sparse 2O has integer entries, so source numerators are exact integers with
denominator 2S^2. The sources are high occupation at site 0, projector E0=0,
onsite low/high coherence, and the real cycle Wilson loop.

For a time t, the common calculation produces a 3x3 matrix for each source:

\[
M_O(t)=J^\dagger e^{itA}\widetilde Oe^{-itA}J.
\tag{10}
\]

Keep **both real and imaginary off-diagonal entries**. The prediction for
any input density is Tr(rho M_O(t)). Dropping off-diagonal entries replaces
coherent inputs by mixtures and is not allowed by this contract. Once the
four response matrices have been computed, evaluating another rho requires
only a 3x3 trace, not rebuilding or re-evolving the model.

For the exact finite-parent input response M_full and exact auxiliary
evolution, (8) gives

\[
\|M_{\rm full}-M_O\|\leq\delta(2+\delta),\qquad \|O\|\leq1.
\tag{11}
\]

Indeed, the exact full input map has norm one, and the approximate embedded
map differs by at most delta. Expanding the quadratic forms proves (11).
Every positive trace-one rho therefore has an expectation error no larger
than (11). Convexity is sufficient for mixed states; no positivity or
normalization is inferred from a finite sample.

The rational source for identity is G, not exactly I. Its departure is
controlled by (3) and the full-map bound, not silently normalized away. The
exact isometric sources U^dagger O U supply a valid underlying compression;
their difference from the implemented rational sources is already covered
by the direct comparison through V. No complete-positive trace-preserving
channel or arbitrary-input auxiliary theory is asserted from approximate G.

## 5. Polynomial error and the correct full-rotor support margin

Evaluate e^{-itA}J by a degree-80 exact Gaussian-integer polynomial. The
Hermitian unitary remainder satisfies

\[
\|e^{-itA}J-p_{80}(-itA)J\|
\leq\tau=(|t|\|A\|)^{81}/81!.
\tag{12}
\]

This is a bound on the whole matrix action on an isometric input J, not three
scalar error bars promoted without justification. The embedded vector-map
error is D=delta+(1+g)tau and its observable error is D(2+D).

For the full unbounded rotor, the initial support now reaches |E_l|=1.
At cutoff K the interaction-picture Dyson words agree only through order
K-1, **not K**. The initial-subspace operator norm is one and the interaction
norm remains J0=97/192, so at K13

\[
\epsilon(t)\leq4\frac{(J_0t)^{13}}{13!}
 \frac1{1-J_0t/14}+D(2+D).
\tag{13}
\]

The same support argument holds simultaneously on W C^3, including all
coherent inputs; it does not require adding a sqrt(3) factor to the Dyson
bound. K13 was selected to retain the prior distance-12 margin after including
initial k=+-1. It has 528 states instead of Round35's K12/488. Every excluded
integer flux is bounded, not inferred small from comparing two cutoffs.

At t=1, the common family observable error is at most 9.30824711e-14, hence
<9.309e-14. This bound holds for all input density matrices in the family and
all norm-one observables with correctly compressed sources. The four stated
sources are explicitly evaluated. The old k=0 intervals remain identical.

## 6. Evaluated interference witnesses

The following Wilson expectations include the full error (13):

| Initial preparation | Certified real Wilson interval at t=1 |
|---|---|
| k=0 | [0.00000021720204, 0.00000021720223] |
| Equal superposition of k=0,1; relative phase 0 | [0.49994394265919, 0.49994394265938] |
| Equal superposition of k=0,1; relative phase pi | [-0.49994350829306, -0.49994350829286] |
| Equal superposition of k=0,1; relative phase +pi/2 | [0.00749991996345, 0.00749991996365] |
| Equal superposition of k=0,1; relative phase -pi/2 | [-0.00749948559732, -0.00749948559713] |
| Equal incoherent mixture of k=0 and k=1 | [0.00000021718307, 0.00000021718326] |

All these use the same A and same sources. The coherent-plus versus mixture
separation exceeds 0.4999 after error subtraction. Imaginary response entries
are about 0.0074997 and are independently checked with an explicit full
complex superposition, so this is not a real-amplitude-only family test.

The larger contrast is not a newly generated large vacuum Wilson signal:
the initial coherent-plus state already has real Wilson expectation 1/2,
while the initial mixture has zero. It is a diagnostic that preparation and
quantum interference survive the reduction, not a new physical prediction.

L12/36 and L16/48 candidates have uniform vector errors about 1.286e-9 and
2.642e-13; L20/60 has <1.051e-18. Their bounds, not selected observed agreement,
choose the final model. Sixty is not claimed to be a minimal dimension.

## 7. Reproducibility, actual costs and the remaining bridge

The compiled model contains the one 60x60 generator (478 nonzero entries),
four dense source matrices (14,400 integer slots), the input-family contract,
denominators and certified budgets. The current JSON is 949,010 bytes. It
contains no 528-state basis, parent matrix, full states, reference responses
or memory history. A standalone run with a nonexistent parent path is tested.

Budget validity is verified by the separate pinned-parent build and replay;
reading a modified JSON does not certify its assertions. Three Round35 pins,
transitive pins, artifact hashes and the model SHA256 bind the record.
Decimal arithmetic proposes the basis only; accepted Gram, residual, source,
tail and response calculations use exact rational arithmetic. An exact Gram
mutant is rejected even if the proposal procedure had otherwise returned it.

Offline work still uses the full 528-state parent, 31,680 basis integers,
their products, Gram calculations and repeated orthogonalization. Online,
the batch evolves three inputs through the common 60-state generator:
2*80*3*478=229,440 real sparse coefficient visits, plus dense source
contractions. Four response matrices then support arbitrary densities by
3x3 traces. Large integer bit lengths and setup are real costs; no end-to-end
runtime speedup, generic scalability or minimal model size is claimed.

The new result removes dependence on a **single vector** within this declared
three-dimensional preparation space, while retaining all its phases and mixed
states. It does not remove dependence on the choice of preparation **family**.
Global loop-flux states are not spatially local preparations. Block-layer
adjacency is not physical spatial locality, and no volume-uniform lattice
estimate follows from this fixed cycle.

The remaining bridge is a physically local family on the actual 3D lattice,
with uniform spatial-window/flux errors and controlled cost, or a genuine
dressed low-energy spectral reduction with its initial/source corrections.
Physical parameter/state selection, chirality, continuum gravity and the
conjunction T1-T8 remain open. The analytic argument is not formalized in a
proof assistant or independently peer-reviewed here.
