# A certified small time-local auxiliary realization of the physical cycle

Status: **NON-RH, conditional theory contract, not promoted**. No T1-T8 gate
is closed. This is a prepared-state numerical model reduction of the existing
Hamiltonian, not a derived low-energy spectral field theory.

## 1. Target, inherited model and the distinction from Round34

Round34 gave a closed retained-amplitude equation with memory, reconstructing
the high sector at the readout. Its K12 implementation still compiled 463 high
components into 49,375 memory integers and 926,000 source integers. The target
here is a genuinely smaller **online** time-local calculation, retaining the
same initial preparation and the same four physical observables.

Keep the Round33 three-site cycle, U(1) Gauss sector with three fermions and
background q_x=1, a=1/12, beta=1/4, eta=1/2, kappa=1/100, M=4 and Vmag=0.
The initial vector is the bare-filled state (mask=7,k=0), not a dressed vacuum.
The initial energy is 1/96. All parameters and preparation are conditional
choices inherited from that benchmark, not physically selected compiler outputs.

Compress the already expanded parent to |E_l|<=12; it has 488 physical states
and 3,932 nonzero Hamiltonian entries. H below denotes its **centered** physical
matrix H_K-6I. Its integer representative is Hhat=14400 H. A global phase
e^{-6it} does not affect any reported expectation. Parent monomials are
expanded before flux compression; no truncated-shift unitarity is used.

The new model uses a different subspace from Round34's bare-low P:

\[
\mathcal K_m=\operatorname{span}\{\psi_0,H\psi_0,\ldots,H^{m-1}\psi_0\}.
\tag{1}
\]

It includes high-occupation configurations. Indeed, the second orthogonal
direction is entirely in the bare-high sector, and its first coupling squared
is exactly 1/96 before controlled rounding. Thus this construction does not
evade Round34's same-P obstruction by claiming high particles have vanished.
It encodes their relevant response in auxiliary coordinates.

Krylov/Lanczos model reduction and defect-based error bounds are established
numerical methods. See [Jawecki, Auzinger and Koch, sections 1-2](https://arxiv.org/html/1809.03369v2).
The contribution here is the parent-specific certified realization, with
unchanged preparation, four compressed physical sources, full-rotor error,
exact construction and independently runnable artifact. It is not a new
projection principle or a new physical law.

## 2. Exactly orthogonal integer construction

Let v_j be integer representatives of the orthogonal Krylov directions,
h_j=v_j^T v_j>0, and u_j=v_j/sqrt(h_j). Start with v_0=psi_0 and form

\[
\alpha_j=\frac{v_j^T\widehat H v_j}{h_j},\quad
\beta_j=\frac{v_{j-1}^T\widehat H v_j}{h_{j-1}},
\]

\[
w=\widehat H v_j-\alpha_j v_j-\beta_j v_{j-1}.
\tag{2}
\]

Clear the rational denominators in w and divide its integer entries by their
positive greatest common divisor. The result is v_{j+1}. Every new vector is
checked against **all** earlier vectors for exact orthogonality. A premature
zero residual is rejected for the requested dimension; it is not divided by
zero or silently replaced by noise. For the tested m=12,16,20, it is nonzero.

The matrix U=(u_0,...,u_{m-1}) is exactly isometric. Hermiticity and (2) imply
T=U^T H U is real symmetric tridiagonal. All entries beyond its first
off-diagonals are checked to vanish by integer dot products. The physical
inner product remains positive, and all basis directions belong to the
physical Gauss sector.

To avoid uncontrolled floating square roots, set S=10^30 and round toward
zero on its reciprocal grid:

\[
\widetilde U_{ij}=S^{-1}\operatorname{sgn}(v_{j,i})
\left\lfloor\frac{S|v_{j,i}|}{\sqrt{h_j}}\right\rfloor,
\qquad A_{ij}=S^{-1}\operatorname{trunc}(S T_{ij}).
\tag{3}
\]

For off-diagonal T, the square root is computed by integer square-root bounds
on (v_i^T Hhat v_j)^2 S^2/(14400^2 h_i h_j), not by a floating eigensolver.
The same rounded off-diagonal entry is used on both sides, so A is **exactly
Hermitian**. Each entry in (3) has error less than S^{-1}, and

\[
\|\widetilde U-U\|\leq \epsilon_U:=\sqrt{488m}/S,
\qquad \|\widetilde U\|\leq1+\epsilon_U.
\tag{4}
\]

The first column is exactly psi_0, since that vector has a single unit entry.
The reduced initial condition is exactly y(0)=e_0. No discarded initial slip
or fit to the original trajectory is involved.

## 3. The small evolution and a rigorous residual bound

The online evolution is the time-local equation

\[
i\dot y=Ay,\qquad y(0)=e_0.
\tag{5}
\]

It is exactly unitary on the m-dimensional auxiliary Hilbert space. Calculate
the residual of its rational embedding against the original finite parent:

\[
R=H\widetilde U-\widetilde U A,\qquad r_j=R e_j.
\tag{6}
\]

Every entry of (6) is an exact rational with denominator 14400 S^2. Each
column norm is enclosed from above with integer square roots. Duhamel's
formula gives, for 0<=t<=1,

\[
\|e^{-itH}\psi_0-\widetilde U e^{-itA}e_0\|
\leq\|\psi_0-\widetilde Ue_0\|
 +\sum_j\|r_j\|\int_0^t|y_j(s)|\,ds.
\tag{7}
\]

There is an important distinction: ||R|| is **not** small. At m20 the last
column has norm about 3.5203. A bound t||R|| alone is useless for this task.
The argument instead bounds how little amplitude reaches that column from
the fixed initial e_0 during the stated interval.

Split A into its diagonal and off-diagonal part, and let B have entries
B_ij=|A_ij| for i!=j and zero diagonal. In the diagonal interaction picture
all phase factors have modulus one. Termwise integration of the Dyson series
therefore yields the componentwise bound

\[
|y_{m-1}(s)|\leq (e^{sB})_{m-1,0},\qquad
I_m:=\int_0^1|y_{m-1}(s)|ds
\leq\sum_{n=0}^\infty\frac{(B^n)_{m-1,0}}{(n+1)!}.
\tag{8}
\]

Because B is a nearest-neighbor chain, the terms vanish for n<m-1. Compute
the nonnegative series through n=80 in exact rational arithmetic. If rho is
the maximum row sum of B (also an operator-norm bound), its remaining tail is

\[
\sum_{n=81}^\infty\frac{(B^n)_{m-1,0}}{(n+1)!}
\leq\frac{\rho^{81}}{82!}\frac1{1-\rho/83}.
\tag{9}
\]

Here rho<7.903, so this is valid. It includes every omitted path and is not an
asymptotic first-term residual estimate. Other components obey |y_j(s)|<=1
by the exact unitarity of (5). Thus the uniform-on-[0,1] bound used is

\[
\delta_m=\sum_{j<m-1}\|r_j\|+\|r_{m-1}\| I_m.
\tag{10}
\]

The initial mismatch in (7) is exactly zero. At m20 the bound has
sum_{j<19}||r_j||<4.626e-28 and I_20<9.426e-20, giving

\[
\delta_{20}<3.32\cdot10^{-19}.
\tag{11}
\]

The computed rational upper bound is stored in the certificate. Tests compare
the **whole embedded vector** against the independent full-H Horner solver,
not just a few observables. The direct solver is a test oracle, never an input
to construction, error estimation or standalone evolution.

## 4. Compress the physical sources, not just the Hamiltonian

For each original bounded Hermitian physical observable O, prepare

\[
\widetilde O=\widetilde U^T O\widetilde U.
\tag{12}
\]

The exact isometric interpretation is O_eff=U^T O U. Its norm is <=1, and its
positive projectors remain positive compressions. The rational matrix in (12)
approximates O_eff with error at most epsilon_U(2+epsilon_U). Rather than add
this error twice, the reported certificate compares the physical state directly
to the rational embedded vector in (7); that already includes embedding/source
roundoff. In particular, the rational image of the identity is
U_tilde^T U_tilde, not exactly I. This tiny difference is bounded, not ignored.

The four O are the same high occupation at site 0, projector E0=0, Hermitian
onsite low/high coherence, and real cycle Wilson operator. All have full-space
norm <=1. Their sparse 2O matrices have integer entries. Consequently (12) is
stored with the common denominator 2S^2, with no intermediate observable
rounding. Online readout is simply y^dagger O_tilde y. It does **not** construct
488-component vectors or access the parent, eliminated block, memory histories
or reference values. The independent tests verify equality with the full
embedded readout for arbitrary construction data and the computed state.

This directly fixes the source-omission error exposed in Round34. It does not
assume small high occupation makes those terms negligible. The second
auxiliary direction is already entirely a high-occupation direction.

## 5. Polynomial evaluation and all omitted electric fluxes

Equation (5) is evaluated by a degree-80 exact Gaussian-integer Horner series.
For any rational t in [0,1], the time numerator scales A's integer entries,
and the time denominator scales its common denominator. In particular, odd
parent numerators are never integer-divided when checking t=1/2.
The reduced Hermitian matrix gives the unitary remainder

\[
\tau_{80}(t)\leq (|t|\|A\|)^{81}/81!.
\tag{13}
\]

The polynomial norm is checked against (1+-tau)^2. Combining (4), (10) and (13),
the finite-parent-to-computed-embedded-vector error is at most
d=delta_m+(1+epsilon_U)tau. For a norm-one observable, the expectation error
is at most d(2+d), even though the embedded polynomial need not be normalized.

Finally reuse the Round33 full-rotor Dyson bound for its specified zero-flux
initial support. With J=97/192,

\[
\epsilon_O(t)\leq
4\frac{(Jt)^{13}}{13!}\frac1{1-Jt/14}+d(2+d).
\tag{14}
\]

The electric term covers **all** excluded integer fluxes, not just two cutoffs.
At m20 and t=1 the rounded error upper bound is 9.30810332e-14, hence <9.309e-14.
It is slightly larger than the earlier certificate's rounded bound because
this round explicitly adds a nonzero model-reduction error. Nevertheless all
four outward-rounded intervals are **identical** to the frozen reference:

| Observable | Certified full-rotor interval at t=1 |
|---|---|
| High occupation site 0 | [0.00071934464413, 0.00071934464432] |
| Probability E0=0 | [0.99928328547964, 0.99928328547983] |
| Onsite species coherence | [-0.00404633584758, -0.00404633584738] |
| Real Wilson cycle | [0.00000021720204, 0.00000021720223] |

The scan m=12,16,20 gives vector-defect bounds about 2.717e-10, 5.785e-14,
and 3.319e-19 respectively. The first two yield overlapping but wider
certificates. This is not a proof that dimension 20 is minimal, either within
all Krylov choices or among other effective descriptions. Reference values are
read only after the model has been built and evaluated, solely for comparison.

## 6. Standalone artifact, costs and proof boundaries

The m20 compiled JSON contains a 20-dimensional initial state specification,
58 nonzero tridiagonal Hamiltonian integers, 1,600 dense source integers for
the four 20x20 observables, common denominators, certified scalar error budgets,
scope and provenance. It contains **no parent matrix, Krylov basis, high-state
vectors, memory/source-history kernels or benchmark answers**. The current
pretty-printed artifact is 109,937 bytes. The standalone command is tested
with a nonexistent parent-repository path.

Reading the JSON's budgets is not itself a fresh proof of them. Verification
of their validity requires the pinned-parent build and deterministic replay.
An arbitrary modified JSON is not authenticated or certified merely because
the standalone calculator can read it. The validation binds the compiled
artifact by SHA256; source-pin and Hermiticity/preparation mutants are tested.

Offline construction still uses the full 488-state cutoff parent. It stores
488m integer basis entries, their products and rounded copies; at m20 the
largest primitive basis entry has 3,969 bits. Exact orthogonality/tridiagonality
and all four source matrices are compiled with full-parent access. These costs
and the preparation dependence are not hidden in a fictitious small theory.

Online, the degree-80 evolution performs 80 complex sparse steps with 58
coefficient positions each: 2*80*58=9,280 real coefficient visits, compared
with 2*80*3932=629,120 in the old full-H evolution. But reduced entries
have a 10^30 denominator instead of 14400, hence much larger integer operands;
four dense source contractions cost O(4m^2). Fewer state components or coefficient
visits are **not** an end-to-end wall-time or bit-complexity speedup claim.
One-time setup is not amortized by assertion. The bound and artifact apply to
the declared preparation and 0<=t<=1, not arbitrary states or long times.

The old bare-low P was not kept as the new state space, so the exact same-P
unitarity obstruction remains valid. No decay of the full memory kernel is
assumed or proved. The result is a controlled finite-time auxiliary realization,
not high-band spectral elimination. Auxiliary chain locality is locality in
a Krylov index, **not physical spatial locality**. No volume-uniform cubic
comparison, chiral measure, selected vacuum/couplings, continuum limit,
graviton or complete T1-T8 solution follows. The analytic bounds are not
formalized in a proof assistant or independently peer-reviewed here.

The next substantive bridge is a preparation family and physically local
subspace with uniform error and controlled cost, or an independently certified
dressed low-energy Hamiltonian with its initial/source corrections. This small
standalone reference makes such candidates testable without claiming that an
efficient numerical representation is itself a theory of everything.
