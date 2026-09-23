# Actual source transport, integer carry and its locality boundary

20 September 2026 · UR.SOURCE.DRIVEN_CARRY.01 · experiments only.

This is a written conditional mathematical derivation, accompanied by exact
finite identities, independently checked estimates and numerical evolution.
It is not a formal proof-assistant certificate or a physical TFPT completion.
The precise source is the pinned `verification/v1033_charged_disorder.py`.
The regional-charge prerequisite is `source-edge-charge-transport/PROOF.md`.
`FLUX_PROOF_REVIEW.txt` gives the detailed linear-drive argument; this file
collects its consequences, the additional energy estimate and the boundaries.

## 1. Question, extra input and stopping criterion

The previous half-sector calculation compared different filled ground states.
The missing execution question was whether one actual unitary history carries
half a regional charge and then another half, without reoccupying the sea at
the zero crossing. We answer that question for a specified external probe.

Fix width W=8, mass M=1, circumference N>=32, and natural hopping units hbar=1.
In the fixed periodic Fourier basis prescribe

    h_N(f) = direct_sum_j h(2 pi (j-f)/N),       j=0,...,N-1,
    f(s) = 1/4 + s,                            0<=s<=1,
    i partial_s U(s) = T h_N(f(s)) U(s),        U(0)=I.

The covariance is Gamma(s)=U(s)P_(1/4)U(s)*; initially all 8N negative
one-body modes are filled. No projection, filling reset or bath acts during
the evolution. The full finite Fock evolution is the number-preserving second
quantization of U. Its total particle number is exactly 8N.

**Extra input:** the uniform time-dependent Peierls phase and the duration T
are prescribed externally. They are not selected by P1/P2, and this result
does not derive the free QWZ realization itself from the compiler.

Success means controlling the actual full-sea evolution and its charge carry.
We stop short of identifying this global history with a local half-spinor
field, with eight selected species, or with an actual C/J-equivariant field.

## 2. Why the closing gap does not invalidate this particular transport

In the exact SX eigenbasis, ordered plus then minus, the source block is

    h(p) = [[-sin(p) I, D(rho)], [D(rho)*, sin(p) I]],
    D(rho)=rho I-S_upper,           rho=1-cos(p).

The checker verifies this identity from the imported primitive hopping
matrices; it does not replace them by an unrelated continuum Dirac model.
Also det D=rho^8. At p=0 there are exactly two zero modes, one on each edge,
and seven negative/seven positive massive modes. For every p the other
fourteen energies have absolute value at least one. This follows by singular
value perturbation from the seven nonzero singular values of S_upper and
sin(p)^2+(1-rho)^2=1; see the prerequisite proof.

The small singular lines of D*D and DD* are real analytic near rho=0, since
their zero eigenvalues are simple. Their signed coupling is

    d(rho)=rho^8 a(rho),                a(0) != 0,

with a analytic. The exact two-edge block is [[-sin p,d],[d,sin p]]. Its
geometric top and bottom eigenlines continue smoothly through zero. Their
mixing angle has order theta=O(p^15), hence theta'=O(p^14).

Only j=1 crosses zero during this drive. There track

    P_cross(p)=P_mass^-(p)+P_top(p)

through the crossing; in every other block track P_-(p). This defines a
commuting rank-8N projector P_tr(s), with the actual initial covariance.
At the half endpoint P_tr(1/2)=P_(3/4). At the full endpoint it is exactly

    P_tr(1)=P_(5/4)+|top,j=1><top,j=1|-|bottom,j=1><bottom,j=1|.    (1)

Thus it is an excited filled configuration after the crossing, not a new
ground state. The branch labels are fixed by the geometric edge profiles.

For each needed smooth branch put K_p=[partial_p P,P]. Solve

    [h,X_p]=K_p.

Between selected and unselected massive components this is a uniformly
gapped Sylvester equation, read on projectors rather than arbitrary bases
inside degenerate bands. The only small denominator is the two-edge gap.
There the numerator is O(p^14), the denominator has a simple zero, and
X_p=O(p^13), partial_p X_p=O(p^12). The derivatives of the real singular
vectors have zero diagonal overlap; they do not introduce an O(p) matrix
element between the orthogonal plus/minus edge frames.

Consequently finite constants A,B,D exist, independent of N and T, with

    ||X_p||<=A,   ||partial_p X_p||<=B,   ||K_p||<=D.

Use the analytic top branch only near zero; elsewhere the negative spectral
cut is uniformly gapped on a compact momentum set. No assertion about
following the top branch through degeneracies at unrelated momenta is needed.

Let U_A be the Kato intertwiner with generator -iT h+K_s. Because
partial_s p=-2pi/N, partial_s X_s=(2pi/N)^2 partial_p X_p. Integrating the
derivative of U_A* X_s U bounds the difference from the true evolution.
For each 16-dimensional covariance block,

    ||Gamma_j-P_tr,j|| <= e_N,
    e_N = 8pi A/(NT)+8pi^2(B+DA)/(N^2 T).                         (2)

Summing the trace norms, or adding Hilbert--Schmidt norms in quadrature,
gives, also at the half endpoint,

    ||Gamma-P_tr||_1 <= 16 N e_N = O(1/T),
    ||Gamma-P_tr||_2 <= 4 sqrt(N) e_N = O(1/(T sqrt(N))).          (3)

For clarity, a uniform chart cover can be specified explicitly. On
|p|<=1/4, rho<=1/32, the second singular value is >=31/32, the small one
is <=rho^8, and the small edge energies have magnitude <0.26. Thus the
analytic two-edge projector is separated from all massive modes by >1/2
throughout this closed chart. The analytic singular-line construction and
the removable p^13 quotient give bounded X_p and its first derivative on
that chart. On the complementary chart |p|>=1/8 (modulo 2pi), the entire
negative/positive cut has minimum absolute energy >=sin(1/8): for rho>=1
use the bound 1, and for rho<=1 use |sin p|. The Riesz projector on a fixed
contour around the negative spectrum therefore has bounded derivatives.
Its offdiagonal commutator solution is the gapped Sylvester inverse, bounded
by the cut gap, with bounded derivative. On overlaps the unique
offdiagonal solution agrees. The continued crossing projector is needed
only in the first chart, since its entire momentum path lies there for
N>=32. This supplies the uniform constants without treating internal
massive-band degeneracies as simple eigenvalues.

The constants are proved finite, not interval-enclosed or optimized. The
mechanism is an instance of gapless adiabatic control with a bounded
commutator solution, not a new general adiabatic theorem. Compare
[Avron--Elgart](https://arxiv.org/abs/math-ph/9805022). A conventional minimum
gap estimate would be invalid at the actual zero crossing.

For f=1/4+F(s) with fixed C2 profile and bounded F',F'', the same integration
includes an additional p'' X_p term of order 1/N; (3) still holds with a
profile-dependent constant. Numerical controls also use
F(s)=s-sin(2pi s)/(2pi), whose endpoint velocities vanish.

## 3. The charge is measured on the original full source

Let T_cut project onto transverse rows y>=4, including all circumference
positions and both spin components. At each endpoint define the existing
Gaussian time average A_f with delta=4 N^(-3/4):

    (A_f)_ab=(T_cut)_ab exp[-(e_a-e_b)^2/(2 delta^2)],
    C_top(f)=dGamma(A_f)-Tr(T_cut P_(1/4)).                       (4)

The reference is the same initial raw density at both endpoints. It is NOT
Tr(A_f P_(1/4)), and the half endpoint uses A_(3/4), not A_(5/4).
Since 0<=A_f<=I, any covariance trace error in (3) bounds the charge-mean
error. When P commutes with h_f, Tr(A_f P)=Tr(T_cut P).

The prior full-sea estimate gives

    Tr[T_cut(P_(3/4)-P_(1/4))]=1/2+O(N^-1).                      (5)

For a full flux period the momenta are relabeled j->j-1, hence

    Tr[T_cut(P_(5/4)-P_(1/4))]=0                                (6)

exactly. The extra top particle and bottom hole in (1) have regional
weights 1+O(N^-16) and O(N^-16). Equations (1)--(6) therefore imply

    <C_top(3/4)>_evolved = 1/2+O(N^-1)+O(T^-1),
    <C_top(5/4)>_evolved = 1+O(N^-16)+O(T^-1).                   (7)

These are also the raw regional-charge means up to the same bounds. The
unfiltered regional number has large sea fluctuations; filtering is needed
for the following concentration statement.

For a Slater covariance C and a positive contraction A,

    Var_C(dGamma(A))=Tr[C A^2-C A C A].

The trace inequality yields

    |Var_C-Var_P|<=3||C-P||_1.                                  (8)

The prerequisite bounds the ground-state filtered variance by a quantity
B_N->0. For the particle-hole target (1), the existing geometric estimates
give ||(A-1)u_top||+||A u_bottom||=O(N^-8). Commuting dGamma(A) through the
two CAR operators shows that its centered second moment is bounded by
(sqrt(B_N)+O(N^-8))^2. Combining with (3),(8), the actual evolved variance
also tends to zero whenever T->infinity. The limit is a sharp regional
charge on these states, not only a half-integer mean of an uncontrolled
fluctuating distribution. The two complementary filtered charges sum
exactly to dGamma(I)-8N at each N.

## 4. Source energy and fixed low-energy excitations

Trace control alone must not be promoted to energy-graph control. Here the
stronger Hilbert--Schmidt estimate in (3) supplies that missing bound.
At either endpoint let P=P_tr, K=N h_f/(2pi), and let Psi have covariance
Gamma. P commutes with K even at the full endpoint where it is excited.
Let H_P=dGamma(K)-Tr(PK). Put eta=||Gamma-P||_2. For equal-rank projections,

    |<H_P>|=|Tr K(Gamma-P)| <= ||K|| eta^2,
    Var(H_P)=1/2 ||[K,Gamma]||_2^2 <=2||K||^2 eta^2.             (9)

The first inequality uses the two diagonal population deficits relative to
P, whose sum is eta^2; it is stronger than a linear trace-norm estimate.
Because ||K||=O(N), (3),(9) imply

    ||H_P Psi||=O(sqrt(N)/T+T^-2).                              (10)

The overlap of two Slater determinants is the product of the cosines of
their principal angles. After one overall phase is chosen,

    ||Psi-Omega_tr|| <= eta = O(1/(T sqrt(N))).                  (11)

Thus **T=N^(3/4)** simultaneously provides:

    trace covariance error       O(N^-3/4),
    Slater-state norm error      O(N^-5/4),
    endpoint energy-graph error  O(N^-1/4),
    fixed edge dynamical phase   O(T/N)=O(N^-1/4).               (12)

Choosing only T=sqrt(N) suffices for charge convergence but (10) would not
prove energy-graph convergence. This distinction is retained.

For any fixed finite collection of low-energy edge creation/annihilation
operators, the one-body intertwiner error is O(1/(NT)); its rescaled-energy
norm is O(1/T). Real normalized edge eigenvectors have zero diagonal Berry
connection. Their O(1/N) energies give the last bound in (12). CAR
commutation then extends (10)--(12), with constants depending on the chosen
finite core, to its transported particle/hole states. The filtered charge
acts on each fixed edge excitation with its original +1/-1 action, by the
geometric A_f estimates. This realizes the oriented charge carry on those
cores up to one common vacuum phase; it does not fix a multi-species cocycle.

At the full endpoint the target energy above its actual instantaneous sea,
in K units, is N/pi times its positive small edge energy at p=-pi/(2N),
which tends to 1/2. No infinite-energy defect is hidden in the full-cycle
charge. This is a one-copy particle-plus-hole energy, not a mass formula.

## 5. Two forward operations are not an inverse pair

The final Hamiltonian is statically large-gauge equivalent to the initial
one. The actually evolved state instead approaches (1); its covariance
distance from the final instantaneous sea tends to sqrt(2). At finite N
the tracked final determinant is exactly orthogonal to that sea.

Writing U_1=U(T/2,0) and U_2=U(T,T/2), the forward composition U_2 U_1
has the whole-charge effect (7). U_1* U_1 returns the original covariance
exactly. It would be an error to identify the forward second leg with
U_1* merely because the background labels close modulo one flux period.
On the source the second leg retains an occupation history.

Eight independent copies would give the vector (1,...,1)=2s with
s=(1/2,...,1/2). This tensor-product consequence does not select eight
species, derive an E8 field algebra, or establish the actual C/J action.

## 6. Locality, gauge and original-principle boundary

Every instantaneous h_N(f) uses the original local hopping blocks, but the
probe acts on all circumference links. This is an extended operation. A
static transformation between uniform and seam gauges does not identify
their time-dependent evolutions without the scalar term:

    if psi'=G(t)psi, then H'=G H G*+i dot(G)G*.

Deleting that term silently changes the experiment. The result is not a
seam-only instantaneous twist operator or a localized field insertion.
The duration diverges in hopping units; in the rescaled clock K=N h/(2pi)
it is 2pi T/N. Neither clock conversion changes the spatial support.

Flux-driven charge transport is established physics; see
[Laughlin](https://doi.org/10.1103/PhysRevB.23.5632) and the original
[QWZ model](https://arxiv.org/abs/cond-mat/0505308). The work here is the
source-specific full-sea and energy/carry check against the TFPT attachment.

The remaining first field implication is explicit: construct a localized,
charged, smeared source operator with both adjoints and a nonzero continuum
limit, reproducing this carry, the required products/cocycle and the actual
symmetries under the same physical clock. A global spectral-flow unitary
does not supply its oscillator dressing or its local operator products.
The P1/P2 origin of the physical source and probe also remains open.
