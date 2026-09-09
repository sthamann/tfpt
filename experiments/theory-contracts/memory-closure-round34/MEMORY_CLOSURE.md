# Exact retained-amplitude memory dynamics with physical source reconstruction

Status: **conditional non-RH theory contract, not promoted**. This calculation
continues the specific three-site cycle of Round33. It is not a derivation of
the Standard Model, a physical vacuum, a continuum limit, or a complete TOE.
In particular, the retained projector below is a **bare occupation projector**,
not a low-energy spectral projector. The exact elimination is a reformulation
with explicit memory and source costs, not an efficiency claim.

## 1. Unchanged parent, preparation, and domains

Use the Round33 compact U(1) cycle with three sites, six fermion modes, three
fermions, background charge q_x=1 and parameters

\[
a=1/12,\quad \beta=1/4,\quad \eta=1/2,\quad
\kappa=1/100,\quad M=4,\quad V_{\rm mag}=0.
\]

These are inherited conditional model parameters, not newly selected physical
constants. A Gauss basis is (mask,k), with three occupied modes and k an arbitrary
integer. The electric fields are

\[
E_0=k+1-N_0,\quad E_1=k+2-N_0-N_1,\quad E_2=k.
\]

Let P select mask=7: all three bare low modes occupied, all bare high modes
empty. Q=1-P. The initial vector is exactly |mask=7,k=0>, so q(0)=0.
This is the Round33 bare-filled, zero-flux preparation, **not** the earlier
dressed Haar preparation. No renormalization of P psi(t) is performed.

Write the physical Hamiltonian on P H direct-sum Q H as

\[
H=\begin{pmatrix}L&C^\dagger\\C&D\end{pmatrix}.
\tag{1}
\]

On P, L is diagonal, with L(k)=3k^2/200+1/96. In particular, direct bare-low
evolution has no Wilson hopping; that effect must come from virtual departures.
The electric and mass operators commute with P. The remaining fixed-cycle
hopping operator is bounded by the Round33 estimate J=97/192. Consequently
C is bounded, and L and D are self-adjoint on their respective electric
domains: each is an electric diagonal operator plus a bounded Hermitian
perturbation. All blocks are taken inside the physical Gauss sector.

The flux cutoff means |E_l|<=K on every link, not an independent arbitrary
restriction on k. At K>=1 there are 40K+8 full components: 2K+1 retained and
38K+7 eliminated. The parent monomials are expanded **before** compression,
as in Round33. In particular P_cut A^2 P_cut is not replaced by
(P_cut A P_cut)^2. No truncated rotor unitarity is assumed.

## 2. Exact closed equation and existence

With p=P psi and q=Q psi, the block equations imply

\[
q(t)=-i\int_0^t e^{-iD(t-s)}C p(s)\,ds,
\tag{2}
\]

and therefore the closed equation

\[
\dot p(t)=-iLp(t)-\int_0^t K(t-s)p(s)\,ds,
\qquad K(u)=C^\dagger e^{-iDu}C.
\tag{3}
\]

Only retained amplitudes are evolution unknowns in (3). Eliminated dynamics
remain in K; they have not disappeared from the information or cost budget.
The construction is the established Feshbach projection method. For a primary
discussion of projected-amplitude memory equations, see
[Chruscinski and Kossakowski, equations (5)-(11)](https://arxiv.org/html/1302.6218v3).
Their environment tensor-product application is not being imported as a
TFPT physical identification. Equations (1)-(3) here follow directly from the
physical-sector blocks just defined.

For the unbounded full rotor, read (3) in mild form using e^{-iLt}. Since
||K(u)||<=||C||^2, iteration of the double Duhamel integral is bounded on a
finite interval by the convergent series
sum_n ||C||^{2n} T^{2n}/(2n)!. This gives existence and uniqueness of a
continuous mild p(t), with (2) reconstructing the unique full unitary solution.
No norm-convergent Taylor expansion of the **unbounded** full H is asserted.
The finite-cutoff polynomial computation below is separately certified against
the full rotor by the inherited bounded-interaction Dyson argument.

For a different initial preparation with q(0) nonzero, (2) also contains
e^{-iDt}q(0), and (3) contains -i C^dagger e^{-iDt}q(0). Those initial-source
terms are not silently dropped; that different preparation is not evaluated
in this round.

## 3. Source reconstruction is part of the theory

For any bounded Hermitian observable O, define

\[
R_p(t)=\int_0^t e^{-iD(t-s)}C p(s)\,ds.
\]

The unchanged full expectation is the retained-history functional

\[
\langle O\rangle_t=p(t)^\dagger O_{PP}p(t)
 +2\Re\{-i p(t)^\dagger O_{PQ}R_p(t)\}
 +R_p(t)^\dagger O_{QQ}R_p(t).
\tag{4}
\]

It contains the cross source O_PQ e^{-iDu} C and the bilocal source
C^dagger e^{iDu} O_QQ e^{-iDv} C. Keeping (3) while using only O_PP generally
does not reproduce the experiment. Normalizing p after projection would
instead condition on finding no high particle and change the protocol.

The code uses a factorized implementation of (4): parent-derived source maps
reconstruct q **at the readout**, then the unchanged Round33 physical observable
definitions are applied. The 463 high components at K12 remain explicitly
present at this stage. This is not an observable-only contraction that has
eliminated their readout cost.

The four observables are the high-mode number at site 0, the projector E0=0,
the Hermitian onsite low/high species coherence, and the real full-cycle Wilson
loop. All have norm at most one in the full physical Hilbert space. No error
bound for an unbounded E^2 observable is inferred from these estimates.

## 4. Compiling and solving the memory equation without a full-state propagator

For each finite cutoff, let h=14400 and Hhat=h(H-6I). The global centering phase
has no effect on any reported expectation. The hats below denote the blocks of
this integer matrix. The compilation, independent of any reference trajectory,
forms

\[
B_r=\widehat D^r\widehat C,\qquad
K_r=\widehat C^T\widehat D^r\widehat C.
\tag{5}
\]

Every integer K_r is symmetric. To degree N=80, B_0,...,B_79 and
K_0,...,K_78 are sufficient. Let p_n=P Hhat^n psi_0. Eliminating the high block
from the power recurrence gives

\[
p_0=\psi_0,\quad p_1=\widehat Lp_0,\qquad
p_{n+1}=\widehat Lp_n+\sum_{r=0}^{n-1}K_r p_{n-1-r}.
\tag{6}
\]

This recurrence takes only Lhat, the precompiled K_r, the retained initial
index and the requested degree. It does not take Dhat, Chat, a high-state
trajectory, the original full propagator, or the benchmark values. An independent
test compares it to direct powers of an unrelated non-diagonal block matrix.

Induction on the full block recurrence gives

\[
q_n=\sum_{r=0}^{n-1}B_r p_{n-1-r}.
\tag{7}
\]

At t=1 the low polynomial is sum_n (-i)^n p_n/(h^n n!). The high readout is

\[
q^{[N]}(1)=\sum_{r=0}^{N-1}B_r
 \sum_{j=0}^{N-1-r}\frac{(-i)^{r+j+1}}{h^{r+j+1}(r+j+1)!}p_j.
\tag{8}
\]

The total degree r+j+1 is truncated at N. Multiplying separately truncated
series without this restriction would not give the same polynomial. Exact
integer numerators use the common denominator h^N N!, with no floating-point
state evolution. Equations (6)-(8) prove equality to the degree-N full-H
exponential polynomial. The tests independently check equality of **every real
and imaginary component**, at both K8 and K12, against Round33's full-state
Horner implementation. That implementation is never used by the memory solver.

The minimum supported degree N=2 needs only K0 and B0,B1. Its dedicated
regression guards against trying to access the not-yet-compiled K1.

## 5. Certification against all integer electric fluxes

For the Hermitian finite matrix, its maximum absolute row sum R bounds its
operator norm. The integral remainder for the unitary exponential gives

\[
\delta_N=R^{N+1}/(N+1)!.
\tag{9}
\]

Here R=1417/200 for K8 and 1657/200 for K12, and delta_80<10^{-30}.
The exact reconstructed polynomial norm is checked against (1+-delta_N)^2.
For a norm-one O, its finite-polynomial expectation error is at most
delta_N(2+delta_N).

The full/cut interaction-picture Dyson words agree through order K for the
unchanged zero-flux initial vector. Each hopping monomial changes each link
flux by at most one, and the interaction bound is J=97/192. Round33 proves

\[
R_{K+1}(x)\leq
\frac{x^{K+1}}{(K+1)!}\frac1{1-x/(K+2)},\qquad x=97/192,
\]

and a full-rotor norm-one observable error at most 4 R_{K+1}(x). Consequently
the memory/source answer has error

\[
\epsilon_K=4R_{K+1}(97/192)+\delta_{80}(2+\delta_{80}).
\tag{10}
\]

At K12 this is at most 9.3081e-14. The bound includes all excluded electric
fluxes, not just a comparison of two finite cutoffs. It applies to the specified
initial zero-flux support; general retained initial states require their own
distance-to-boundary estimate. No uniform-in-time or volume limit follows.

All four resulting intervals are exactly identical, endpoint for endpoint, to
the frozen Round33 certificate. The benchmark is read **after** evolution and
source evaluation and is used only for a fail-closed comparison. Changing a
benchmark endpoint cannot retune the answer; a regression requires rejection.

For a concrete source-omission diagnostic, the full Wilson value is positive,
in [0.00000021720204, 0.00000021720223]. Full minus the unnormalized bare-P-only
Wilson readout lies in [0.00008580171746, 0.00008580171785]. Subtracting these
certified intervals encloses the P-only answer in
[-0.00008558451581, -0.00008558451523], strictly negative. Omitting the source
reconstruction therefore gives the wrong sign in this actual gauge observable,
even though the eliminated total probability is small. This is not a comparison
to a properly dressed effective observable, which remains a separate task.

## 6. Why an autonomous Hamiltonian on this same bare subspace is not exact

Consider the compressed propagator G(t)=P exp(-itH) P acting on the same P
with the unchanged preparation map. On finite-support domain vectors,

\[
G(0)=I,\quad G'(0)=-iL,\quad G''(0)=-L^2-C^\dagger C.
\tag{11}
\]

An exponential exp(-itA) with a time-independent linear A would require A=L
from the first derivative, but its second derivative would be -L^2. Since
C is nonzero, it cannot equal G(t) for all initial vectors and all times.
In particular, no autonomous Hermitian operator on this same bare subspace
reproduces the compressed amplitudes exactly.

For the actual initial vector, the exact physical K(0) diagonal is 1/96:

\[
\|p(t)\|^2=1-t^2/96+O(t^3),\qquad
\left.\frac{d^2}{dt^2}\|p(t)\|^2\right|_{0}=-1/48.
\tag{12}
\]

At t=1 the full-rotor survival interval is
[0.99784311496210, 0.99784311496230]. The complement is physical probability
in the eliminated bare-occupation sector, not a numerical normalization error.

This is a restricted obstruction. It does **not** rule out a dressed encoding,
a time-dependent non-Hermitian generator, auxiliary variables, an energy-window
effective Hamiltonian with a controlled error, or an effective theory for fewer
specified observables. In particular it is not a no-go for spectral mirror
decoupling or a proof against any T1-T8 solution.

## 7. The virtual Wilson term appears in the same memory kernel

The physical zeroth moment C^dagger C is diagonal, equal to 1/96 at interior
retained k and 1/192 at the cutoff endpoints. In the first centered moment,

\[
\langle k+1|C^\dagger(D-6I)C|k\rangle
=-3\eta^2a^3=-1/2304.
\tag{13}
\]

It is independent of k for every allowed adjacent pair. The three routes are
the cyclic rotations of low0 -> high1, low2 -> low0, high1 -> low2. Fermion
antisymmetry supplies the negative sign. The scalar centering cannot change
this off-diagonal coefficient because C^dagger C has no off-diagonal entries.

The stationary Schur expression L-C^dagger(D-E)^{-1}C connects this path to
the leading virtual term. With the one-high intermediate mass denominator
expanded in the large-M regime, its cubic hopping contribution is

\[
-\frac{3\eta^2a^3}{M^2}(W+W^\dagger)
=-\frac{6\eta^2a^3}{M^2}\Re W.
\tag{14}
\]

This agrees with the leading triangle term already identified in Round33's
filled-band compression. Equation (13) is exact; equation (14) is only the
leading hopping/large-mass connection, **not** a certified static approximation
to all four t=1 readouts. The full memory calculation keeps higher moments,
the electric dynamics, and the original preparation. A square in three spatial
dimensions is not identified with this three-site triangle.

## 8. Finite-cycle memory does not have an automatic decay tail

For the actual retained initial basis vector, put c=C|k=0> and
k_c(t)=<c,e^{-iDt}c>. At a finite cutoff, resolve the distinct eigenvalues
lambda of D with spectral weights w_lambda=||Pi_lambda c||^2. Then

\[
k_c(t)=\sum_\lambda w_\lambda e^{-i\lambda t},\quad
\sum_\lambda w_\lambda=1/96,
\]

and direct integration of the finite sum gives

\[
\lim_{T\to\infty}\frac1T\int_0^T|k_c(t)|^2\,dt
=\sum_\lambda w_\lambda^2
\geq \frac{(1/96)^2}{\dim Q}.
\tag{15}
\]

At K12 the rational lower bound is 1/4267008. This is a **long-time averaged
square**, not a pointwise lower bound on the kernel. It nevertheless excludes
decay to zero and absolute integrability of this nonzero kernel entry: the
entry is bounded and |k_c|^2 <= (1/96)|k_c|. Degeneracies only increase the
possible lower bound by reducing the number of distinct contributing weights.

The uncut three-site rotor also has compact resolvent in Q: the electric
diagonal grows quadratically with |k| with finite matter multiplicity, and its
remaining perturbation is bounded. Its spectral weights form a countable
absolutely summable sequence. Uniform approximation by finite spectral sums
then gives the same mean-square identity, with a strictly positive sum of
squares for c nonzero. No numeric finite-dimensional lower bound is carried
over to the uncut space. Thus the full **fixed spatial cycle** likewise has no
automatic norm-decaying memory tail. This statement does not concern a
thermodynamic or continuum bath limit.

A short history window, a Markov approximation, or exponential norm decay is
therefore not justified by the mass gap alone in this example. Oscillatory
cancellations and dressed low-energy approximations may still give accurate
finite-time effective descriptions; they need their own bounds. Degree 80
in this work truncates a certified polynomial, **not** the duration of memory.

## 9. Cost, provenance, and the remaining bridge

At K12 only 25 retained components occur per jet in (6), but the compilation
uses the 463-dimensional eliminated block. It stores 79 dense 25x25 memory
matrices (49,375 integer slots) and 80 dense 463x25 source maps (926,000 integer
slots). Integers grow with polynomial degree; these counts are not byte counts.
The implementation also retains parent blocks, 81 retained jets, and both
cutoffs in caches. At K8 the corresponding counts are 17, 311, 22,831 and
422,960. No memory reduction or runtime speedup over Round33 is claimed.

In arithmetic-operation terms, dense memory convolution costs O(N^2 p^2).
Source integration costs O(N^2 p), and source contraction O(N q p). Offline
sparse-D source compilation costs O(N nnz(D) p), in addition to cross
contractions and hashing. Bit complexity is larger because the operands are
arbitrary-precision integers. Constructing a full parent is acceptable for
this small benchmark, not a scalable three-dimensional solution.

Three SHA256 pins fix the Round33 checker, dynamical proof and validation;
transitive provenance is checked too. Production certification rechecks pins
even when kernels or solutions are cached. The output records separate kernel
and source digests and hashes of this round's four source artifacts. Tests run
normally and under -OO, without relying on removable Python assertions.

The conditional benchmark now has an actually evaluated closed memory
description with unchanged physical sources and preparation. Still open are
a controlled, simpler low-energy approximation to this description; a uniform
local-readout comparison in a genuine three-dimensional dynamical lattice;
spatial-window and flux tails in that comparison; selected physical couplings,
state, chiral measure and continuum physics. No physical T1-T8 gate is promoted.
