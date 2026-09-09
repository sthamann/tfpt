# Geometric control of the existing dynamical signed-wall family

2026-09-07. NON-RH / unpromoted research. This extends Round30's declared
compact-rotor family. It proves conditional, volume-independent **per-link
Fock bounds**, spatial projector bounds and a **finite-time high-density
bound**. It does not prove a many-body mirror spectral gap, a chiral measure,
the physical Standard Model or any full T1-T8 gate.

The geometric motivation is the tangent/normal splitting in
[Sochi, Sections 3.6 and 3.9](https://arxiv.org/html/1609.02868v1).
For quantum subspaces the precise objects are spectral projectors, not an
asserted physical surface. The projector/metric formalism is standard;
see [Mera and Ozawa, Section II](https://arxiv.org/html/2103.11583v3#S2) and
[Graf and Piechon](https://arxiv.org/html/2102.09899v2).
The estimates below are derived here for the specified family, not quoted
from those papers as TFPT results.

## 1. Hypotheses and the first useful geometric object

For each finite graph keep the full Hilbert space

    L^2(G^edges, Haar) tensor F(C^(2d))

and Round30's h(A), V(A), electric generators and self-adjoint Hamiltonian.
G is compact and connected; every electric representation is retained.
Write P(U)=V(U) diag(I_d,0) V(U)^* and Q=1-P. Assume uniformly

    spectrum(h_L) subset [a,b], spectrum(h_H) subset [b+delta,infinity),
    delta>0,     h_L=P h P on ran P, h_H=Q h Q on ran Q.            (1)

For the signed-wall family one may take a=-L, b=B0=L+beta L^2,
delta=M-B0, with all the other Round30 assumptions retained. This is a
**fiber** separation, not the full electric Hamiltonian's many-body gap.
All bounds on derivatives below are supremums over gauge configurations.
The derivative X_a is a declared real invariant electric direction on a
link; for coordinate formulas use partial derivatives. No commutation of
distinct nonabelian invariant vector fields is assumed.

Define the subbundle second fundamental form in the trivial ambient
fermion bundle by

    S_a=Q (X_a P) P.                                            (2)

Differentiating P^2=P gives P(X_a P)P=Q(X_a P)Q=0, hence
X_a P=S_a+S_a^*. If w and v are the low and high column frames of V,
then S_a=v(v^* X_a w)w^*. Thus S_a and b_(a,HL)=-i v^* X_a w have
identical nonzero singular values. In particular

    w^* S_a^* S_a w=(X_a w)^* Q (X_a w)=b_(a,LH)b_(a,HL).        (3)

This is an actual operator identity underlying the Born-Huang term. The
positive trace metric is g_ab=Re Tr(S_a^* S_b); the antisymmetric part
encodes the projected curvature. It is geometry of **gauge-parameter
dependent quantum states**, not yet a metric on spacetime.

## 2. Sylvester equation in three norms, with no dimension factor

Differentiate [h,P]=0 and take the Q-P block:

    h_H S_a-S_a h_L=-Q(X_a h)P.                                 (4)

Put T_a=Q(X_a h)P. The unique solution of (4), using (1), is

    S_a=-integral_0^infinity exp[-t(h_H-b)] T_a exp[t(h_L-b)] dt. (5)

Both the convergence and the sign follow directly by differentiating the
integrand. Its norm is at most exp(-delta*t)||T_a||_p for each Schatten
norm p=1,2,infinity, since ||AXB||_p<=||A||||X||_p||B||. Therefore

    ||S_a||_p <= ||Q(X_a h)P||_p/delta <= ||X_a h||_p/delta.     (6)

The constant is independent of total matrix dimension. Degeneracies
inside either band do not matter. A vanishing band separation does.
These are finite-graph theorems with uniform constants where the stated
hypotheses are uniform, not a choice of infinite-volume Fock representation.

## 3. Exact entire-Fock norms: locality survives second quantization

Let b_a^off have just the low-high and high-low blocks of b_a. Its
one-particle eigenvalues are +sigma_j, -sigma_j and possible zeros,
where sigma_j are the singular values of S_a. On the entire exterior
algebra dGamma(b_a^off) has every subset sum of these eigenvalues. Thus

    ||dGamma(b_a^off)|| = sum_j sigma_j = ||S_a||_1.              (7)

This is not the generally much worse bound d||b_a^off||. For
N_H=dGamma(diag(0,I_d)), the Hermitian current i[B_a,N_H] has the same
norm: its off-diagonal blocks differ by unit complex phases only.
Consequently, if ||X_a h||_1<=D1_a,

    ||i[B_a,N_H]|| <= D1_a/delta =: g_a.                         (8)

On the empty-high Fock space the geometric correction is positive and

    ||(kappa/2)dGamma(b_LH b_HL)||
       =(kappa/2)Tr(S_a^* S_a)
       <=kappa D2_a^2/(2 delta^2),  D2_a=||X_a h||_2.           (9)

Equation (9) is a bound for a single link/direction; summing all links
still gives an extensive operator. These constants are local if X_a h
has uniformly bounded support and coefficients. Derivatives of spectral
projectors need not have finite rank or strictly finite support.

For Round30's exact four-mode rotor: sigma_1=sigma_2=3/10,
||dGamma(b^off)||=||i[B,N_H]||=3/5, and Tr(S^*S)=9/50.
The checker exhausts all 16 Fock eigenvalues and verifies the trace cost
on the doubly occupied low state. One cannot use 9/100 as the whole
low-Fock geometric norm. The pointwise derivative cost is ||Xh||_2^2=3;
delta=4/3 gives the valid, conservative bound 27/16 on ||S||_2^2.

## 4. Spatial locality of the projector and its link derivative

Assume h has graph range R, fixed internal dimension per site, and

    Jrow = sup_x sum_y ||h_xy|| < infinity                       (10)

uniformly over graphs and gauge configurations. Choose mu>0 with

    Jrow (exp(mu R)-1) <= delta/4.                               (11)

Use the rectangular low-band contour Gamma with real sides
a-delta/2 and b+delta/2, imaginary sides +/-delta/2. Its distance
from the spectrum is at least rho=delta/2 and its length is
ell=2(b-a+2delta), independent of volume.

Here is the weighted-resolvent argument explicitly. Conjugate h by the
diagonal weight exp(mu f(x)) for any 1-Lipschitz distance function f.
The perturbation's block row and column sums are at most the left side
of (11); the column bound follows from Hermiticity before weighting and
the same absolute entry estimate. The Schur norm bound and resolvent
Neumann series give, for z on Gamma,

    ||(z-h)^(-1)_xy|| <= (2/rho) exp(-mu dist(x,y)).              (12)

The Riesz formulas P=(1/2pi i) integral_Gamma (z-h)^(-1) dz and
X_a P=(1/2pi i) integral_Gamma (z-h)^(-1)(X_a h)(z-h)^(-1) dz
therefore imply

    ||P_xy|| <= ell/(pi rho) exp(-mu dist(x,y)),                  (13)

    ||(X_a P)_xy|| <= 2 ell C_a/(pi rho^2)
       *exp[-mu(dist(x,Z_a)+dist(y,Z_a))],                       (14)

where both indices of X_a h are supported in the finite set Z_a and
C_a=sum_(u,v in Z_a)||(X_a h)_uv||. All constants are uniform under
the declared local bounds. Formula (14) establishes a genuinely local
origin for the changing subspace, not merely a fixed-background norm.

On polynomial-growth lattices, these tails are summable. In particular
Q Pi_x Q, with Pi_x the fixed on-site projector, gives a positive
quasilocal high-density decomposition: sum_x Q Pi_x Q=Q. Its fermionic
second quantization approximates local observables in norm. To see this,
write Q Pi_x Q=A_x A_x^*, truncate the finitely many columns A_x outside
a ball, and use
||AA^*-CC^*||_1<=(||A||_2+||C||_2)||A-C||_2 and the exponential
column tails. Finally ||dGamma(K)||<=||K||_1 for Hermitian K.
No sufficiently fast volume growth is silently replaced by polynomial
growth. No continuum velocity bound follows when lattice spacing changes.

## 5. Full electric dynamics: an energy-density theorem

In the rotated representation let D_a=E_a+B_a and

    H'=H_el'+Vmag+dGamma(h_L,h_H),
    H_el'=(kappa/2)sum_a D_a^2.                                 (15)

On the smooth core, and by quadratic-form extension for finite-energy
states, J_a=i[D_a,N_H]=i[B_a,N_H] is bounded by (8). The commutator is

    d <N_H>/dt=(kappa/2)sum_a <D_a J_a+J_a D_a>.                 (16)

Cauchy-Schwarz first in Hilbert space and then in a yields

    |d<N_H>/dt| <= sqrt(2 kappa <H_el'> sum_a g_a^2).            (17)

The integrated estimate holds for all finite times; the derivative can
be read almost everywhere for finite-form-energy states. The same
inequality holds for mixed states by the Hilbert-Schmidt form of
Cauchy-Schwarz. Restricting to an invariant Gauss sector preserves it.

Let n be the number of sites, d<=m n the number of low modes,
#electric directions<=c_E n, g_a<=g, and <H'>/n<=e. Because Vmag>=0
and dGamma(h_L,h_H)>=-dL, energy conservation gives

    <H_el'(t)>/n <= e+mL =: ebar.

Writing nu_H=<N_H>/n, (17) implies

    |nu_H(t)-nu_H(0)| <= |t| g sqrt(2 kappa c_E ebar).           (18)

This is volume-independent. Round30 equation (8) ALREADY supplied the
static inequality H'+dL>=M N_H. After division by n it gives

    nu_H(t) <= (e+mL)/M = ebar/M.                               (18a)

Thus volume-independent density suppression is not first discovered by
renaming the old occupation bound. The new contributions are the local
Schatten/full-Fock control, the finite-time rate (18), spatial decay and
the explicit uniform-energy Gauss state below. Both bounds must be kept.
For a family with fixed L,beta,eta,D1 and
M increasing, delta=M-B0 increases and g<=D1/delta. If initial energy
density stays uniformly bounded and nu_H(0)=0, high-sector population
density tends to zero uniformly over all finite volumes and bounded time
intervals as M tends to infinity. This is a **population-density
decoupling limit**, not spectral mirror decoupling at finite physical M.
No convergence of the full many-body wavefunction, no approximation of
all low-sector dynamics and no unique physical state is asserted.

## 6. A connected family and an explicit Gauss state

Take connected open U(1) chains, one low and one high fermion per vertex,
nearest-neighbor hopping A_(x,x+1)=U_x/4 and its adjoint, beta=1/4,
eta=1/2, lambda=1, Delta=M-1, M>=4, Vmag=0. This is the same signed-wall
functional family; the chain, parameters and backgrounds are declared,
not derived from TFPT's compiler. Put X=X_a A for a single link. Then

    L=1/2, B0=9/16, delta=M-9/16,
    ||X||_1=1/2, ||X||_2^2=1/8,
    X_a h=[X+beta(AX+XA), eta X; eta X,0].                      (19)

The Schatten triangle and ideal properties yield

    D1 <= (1+2 beta L+2|eta|)||X||_1 =9/8,
    D2^2 <= [(1+2 beta L)^2+2 eta^2]||X||_2^2 =33/128.          (20)

At M=4: delta=55/16, g<=18/55, and the per-link whole-low-Fock
geometric energy is at most 33 kappa/3025, at **every** chain length.
The derivative occupies at most four sites. Algebraic checks for
n=2,3,4,8,16,32 have squared Hilbert-Schmidt costs
3/16, 385/2048, 193/1024, 193/1024, 193/1024, 193/1024 respectively.
They are regressions; (19)-(20), not that finite list, establish uniformity.
For (11) one may take R=2, Jrow=77/16, mu=1/16 at M=4:
exp(1/8)<=8/7 gives Jrow(exp(1/8)-1)<=11/16<55/64.
Here Jrow<=M+(1+|eta|)L+beta L^2 bounds physical-site 2x2 blocks.
The smaller 17/4 scalar-orbital row bound does not bound those blocks;
the regression suite explicitly rejects that substitution.

There is also an explicit initial state, so an energy premise need not
remain merely hypothetical in this family. In the **rotated** frame take
the constant normalized Haar rotor wave times the Slater state with all
low modes filled and no high mode. Set the background charge q_x=1 at
each vertex. The zero-flux filled state satisfies both signs of each link
Gauss law; the equivariant full rotation maps it to an original-frame
physical state. These are stated backgrounds, not a neutral empty vacuum.

For the canonical V(A)=[C,S;-S,C],

    Tr b_LL=-i Tr(C X_a C+S X_a S)
           =-(i/2) X_a Tr(C^2+S^2)=0.                          (21)

Thus on the constant filled-low state the electric expectation per link
is exactly (kappa/2)Tr(S_a^*S_a). Meanwhile f_-(A)<=A+beta A^2,
Tr A=0, and Tr A^2=(n-1)/8. Consequently its total energy density obeys

    e <= 1/32 + 33 kappa/(256 delta^2),
    ebar <= 17/32 + 33 kappa/(256 delta^2).                      (22)

Combining (18), c_E<=1 and (20) supplies the explicit uniform bound

    Ebar=17/32+33 kappa/(256 delta^2),
    nu_H(t) <= min{1, Ebar/M,
                   |t| (9/(8 delta))*sqrt(2 kappa Ebar)}.      (23)

At kappa=1/100 rational upper bounds on the coefficient of |t| are
17/500 for M=4, 3/1000 for M=40, and 3/10000 for M=400. These are
upper bounds on **expected high occupation per site in model units**,
not measured probabilities, masses or percentages of all TOE problems.
The inherited static caps are less than 0.133, 0.0133 and 0.00133,
respectively, at those same parameters, and are stronger at late times.
This static energy argument does not alone control virtual low-sector
energy shifts or local-observable errors. The state is chosen and
explicit, not selected by cosmology or shown to be the ground state.

### 6a. Explicit three-dimensional boxes with physical cycle fluxes

The same construction extends to connected open hypercubic boxes in a
declared spatial dimension s_dim, with hopping 1/(4 s_dim) and at most
2 s_dim nearest neighbors. This is a choice of dimension, not T1's missing
dimension selection. L=1/2 and delta=M-9/16 are unchanged, whereas

    c_E<=s_dim, D1<=9/(8 s_dim), D2^2<=33/(128 s_dim^2),
    Tr A^2/n<=1/(8 s_dim),
    e<=1/(32 s_dim)+33 kappa/(256 s_dim delta^2).                 (23a)

These follow by the same local matrix calculation and counting unoriented
edges (each contributes two entries to Tr A^2). Equations (17)-(18a)
apply without further approximation. The filled-low q_x=1 Haar state and
the zero determinant connection (21) remain exactly the same construction.

For s_dim=3 this is an explicit local Hamiltonian on three-dimensional
spatial boxes with continuous unitary time, full U(1) electric rotors and
the declared signed-wall matter. It is **not** chiral SM matter, not a
Lorentz-invariant continuum and not a TFPT-selected 3+1D completion.
Vmag=0 is still the stated choice; no Yang-Mills magnetic dynamics is
silently supplied. The local constants now read

    D1<=3/8, D2^2<=11/384,
    Ebar=49/96+11 kappa/(256 delta^2),
    nu_H(t)<=min{1,Ebar/M, |t| (3/(8 delta))*sqrt(6 kappa Ebar)}. (23b)

At kappa=1/100 exact rational comparisons certify

    M=4:   nu_H(t)<=min(0.128,   0.0192 |t|),
    M=40:  nu_H(t)<=min(0.0128,  0.0017 |t|),
    M=400: nu_H(t)<=min(0.00128, 0.00017|t|).                    (23c)

These bounds hold for every finite box size, not just tested volumes.
Regressions use 2x2x2, 2x3x2 and 3x3x3 boxes. Their graph cycle ranks
are 5, 9 and 28. Unlike open chains, the Gauss constraints therefore leave
unbounded independent electric circulation sectors. An explicit plaquette
flow k around four edges has zero divergence for **every integer k** and
electric norm squared 4 k^2. The checker verifies that polynomial identity.
No enumeration or cutoff of these physical flux sectors enters (23b).

## 7. Two obstructions that the geometric bound does not erase

### 7.1 Unbounded electric flux

In the Round30 four-mode example, on a constant low vector times the
rotor Fourier wave exp(i k theta), the off-band electric action has norm

    ||H'_HL on that input fiber||=3 kappa(2|k|+1)/20.            (24)

The checker verifies its full Laurent matrix for an arbitrary integer k.
The fiber gap and all geometric matrices stay fixed while (24) diverges.
Thus (6) does not imply a bounded small Hamiltonian perturbation on the
unrestricted rotor Hilbert space. The fixed-background one-fermion Gauss
sector of Round30 has forced finite fluxes; it is **not** this arbitrary-k
example. Equation (24) rejects a full-Hilbert-space inference without
misrepresenting the smaller physical sector. Equations (17)-(23) expressly
retain the necessary energy control.

### 7.2 Global overlap versus local occupation

For Round30's actual one-fermion Gauss cell with any normalized initial
low vector, C=H_HL satisfies C^*C=9 kappa^2 I/400. Analytic finite-matrix
evolution gives p(t)=||Q exp(-itH)psi||^2=9 kappa^2 t^2/400+O(t^3),
so p(t)>0 at sufficiently small nonzero times. For n **independent**
copies, full dynamics and the all-low projector factorize exactly:

    probability(all cells low)=(1-p(t))^n,
    expected high occupation per cell=p(t).                    (25)

For any fixed such t, the first quantity tends to zero. The vector-norm
distance to any all-low state is at least sqrt[1-(1-p(t))^n]. This is a
counterexample to inferring uniform global overlap from small local
leakage; it is not a claim that a connected chiral theory is a product.
It does not contradict a local spectral gap or equations (18)-(23).

## 8. Intrinsic curvature is not automatically a graviton

With b=-i V^*dV, the full connection satisfies db+i b wedge b=0.
For a low frame w the projected connection a=-i w^*dw satisfies

    da+i a wedge a=-i (dw)^* Q wedge dw.                        (26)

Thus projected curvature can be nonzero in a flat full frame. The
checker verifies both identities in an explicitly separate two-coordinate
SU(2) frame, obtaining F_uv=sin(2u). This is a mathematical diagnostic,
not another TFPT sector. No spacetime metric, dynamical spin-two pole,
two helicities or universal matter coupling has been produced.

## 9. Exact remaining proof boundary

The new local/Fock bounds, spatial projector estimate and explicit
finite-time large-M population theorem address a real part of T3/T4.
They do not show the volume-independent interacting **spectral** mirror
gap or a local chiral Weyl measure. The physical parameter M is not
selected, and no low-sector effective dynamics error theorem on connected
large graphs has been proved. That is the next concrete step: retain
virtual high-sector terms and compare gauge-invariant local observables
at finite energy density, with constants uniform in graph size.

T1/T2 reconstruction, T5 continuum, T6 mass/coupling selection, T7 quantum
gravity and T8 canonical state remain separate obligations of the same
parent. Nothing here turns an internal geometric identity into their
completion. Tests certify the displayed finite identities and arithmetic;
the analytic arguments are not proof-assistant or external-review certified.
