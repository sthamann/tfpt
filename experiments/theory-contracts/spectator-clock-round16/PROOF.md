# Round16: the local-parent limit, real spectator energy and the quadratic clock

2026-09-06. Constructive NON-RH research. This extends the **specified**
[Round15 local positive parent](../local-parent-round15/PROOF.md), not the
unchanged microscopic TFPT Hamiltonian. It keeps the quadratic clock constraint
and its group-averaging weight. All lattice sizes below are finite, with a
connected periodic cubic lattice of n>1 sites. Limits and costs are stated
explicitly; no continuum, microscopic clock selection or full TOE is claimed.

## 1. Results and the model actually being compared

Write A=A_+(g) for the chosen scalar/TT Hamiltonian of Round13--15 and let

    d=4n+2,       S=-Delta_y/2 on L2(R^d),
    A_0=A tensor I+I tensor S.                                      (1)

These d surviving coordinates in the Round15 limit are physical free modes.
They have no normalizable state of zero energy. In particular replacing their
energy by zero inside a clock square root is not an exact product-factor trick.
There are instead three precise constructive statements:

* The Round15 sequential quantum limit also intertwines the **quadratic-clock
  square-root dynamics and its positive weighted solution norm**, after the
  same explicitly chosen fast zero-point subtraction.
* Normalized finite-energy spectator packets approximate the A clock, with an
  explicit error bound depending on d, time, their energy and their spatial
  spread. No generalized state is passed off as a normalized vacuum.
* At the limit only, spectator translations admit an exact distributional
  constraint reduction to the A clock. Electing to impose those new constraints
  is an additional model choice, not a gauge symmetry of the finite parent.

The chosen clock remains

    C_X=X-P_q^2/12,       negative P_q sheet,
    omega_X=sqrt(12X),   D_X=sqrt(6) omega_X^(-1/2)
                            =3^(1/4) X^(-1/4).                       (2)

We do not replace C_X by P_q+omega_X. No spatial/matter constraints are added
or identified in this note. If another construction restricts initial data to
a noninvariant charge subspace, the maps here are solution readouts, not an
autonomous clock Hamiltonian on that restricted subspace.

## 2. A uniform positive lower bound already exists before either limit

Use precisely the Round15 notation and its normalized Gaussian isometry:

    B_delta,eta=H_delta,eta-E_fast(delta,eta),
    E_fast=Tr K_delta^(1/2)/(2 sqrt(eta)),
    J_delta,eta^* J_delta,eta=I,
    A_delta=-Delta_(phi,q)/2+V_m(phi)+V_delta(phi,q).       (3)

The frozen fast oscillator, including its complete square, is bounded below
by E_fast+V_delta at each slow configuration. V_delta>=0. Adding the slow
kinetic terms therefore proves the stronger, useful form inequality

    B_delta,eta >= H_m tensor I >= e_m I,
    A_delta >= e_m I,            A_0 >= A tensor I >= e_* I,

    e_m=(1/2) sum_k sqrt(m^2+ell(k)),
    e_TT=sum_(k!=0) sqrt(ell(k)),       e_*=e_m+e_TT.        (4)

The factor in e_TT retains both real TT polarizations. The scalar zero mode
is retained, and contributes zero when m=0. Nevertheless e_m>0 on every
connected nontrivial finite lattice. No simultaneous diagonalization of the
matter kinetic operator with its configuration-dependent fast vacuum is
assumed: the first inequality is a direct inequality of the two summand forms.

At unit spacing, n=8 and m=0 the **original Ward energy** gives

    spec(ell)={0:1,4:3,8:3,12:1},
    e_m=3+3sqrt(2)+sqrt(3),       e_*=9+9sqrt(2)+3sqrt(3),
    d=34.                                                        (5)

Thus gamma=e_m is one common strictly positive bound for the complete
finite-parameter family and both limits. This is an absolute-energy bound,
not an interacting excitation gap. It fails in the excluded n=1,m=0 case.

## 3. Transfer of the actual quantum limit through the clock functions

Round15 proves on every compact smooth slow test function

    ||(B_delta,eta J_delta,eta-J_delta,eta A_delta)psi||
        <= C_delta,psi eta^(1/4)+D_delta,psi eta^(1/2),                (6)

and hence the uncompressed resolvent intertwining at z=+i and -i. It also
proves A_delta -> A_0 by the common-core criterion at fixed finite lattice.
Here we give the functional-calculus step rather than assuming that a
compressed expectation proves the corresponding full dynamics.

Products of resolvents telescope with J between them. Their operator bounds
are uniform, so the two resolvent limits imply

    ||f(B_delta,eta)J_delta,eta v-J_delta,eta f(A_delta)v|| -> 0        (7)

for every f in C_0(R) and every v. Stone--Weierstrass and uniform approximation
justify this passage. The same assertion holds for A_delta,A_0 with J=I.
All spectra lie in [gamma,infinity); clock functions on that half-line may
be extended continuously to the rest of R without affecting any operator.

For f_q(E)=D(E) exp(-iq sqrt(12E)), the decay D(E)=O(E^(-1/4)) makes f_q
belong to C_0 after such an extension. On a bounded q interval the tails
are uniformly small, and on a bounded E interval q -> f_q is uniformly
continuous. A finite q mesh proves that (7) is uniform for |q|<=Q for f_q.

For the unweighted u_q(E)=exp(-iq sqrt(12E)), use the core-energy bounds from
(6): for core psi, ||B_delta,eta J psi|| stays bounded. Consequently the
spectral tail above M is at most const/M in vector norm. The analogous tail
bound holds for A_delta psi. Apply (7) to a continuous compact-energy cutoff
of u_q, send M to infinity and then extend by density and ||J||=1. This gives

    sup_(|q|<=Q) ||exp(-iq omega_B)J v-J exp(-iq omega_A_delta)v|| -> 0,
    sup_(|q|<=Q) ||D_B exp(-iq omega_B)J v
                         -J D_A_delta exp(-iq omega_A_delta)v|| -> 0. (8)

The same two assertions hold as delta->0 with A_delta and A_0. The clock
constraint's own group exp(it C_X) also transfers on product core tests,
because its clock-momentum factor is unchanged; no limiting delta function
is inferred from that fact. The physical shell norm is treated explicitly next.

Equations (6)--(8) prove a **sequential** eta->0 at fixed delta, then delta->0
at fixed lattice. They are strong, uniform on compact clock-time intervals,
not operator-norm convergence or a state/volume-uniform rate. The proof uses
the core-resolvent method discussed in Teschl, Wang, Xie and Zhou,
[On Generalized Strong and Norm Resolvent Convergence, Lemma 2.8](https://arxiv.org/html/2601.10476v1).
We use the explicit uncompressed
intertwining and do not assume an onto inverse for the Gaussian embedding.

## 4. The exact positive clock norm and the norm-preserving embeddings

In a spectral representation of X>=gamma, the negative sheet has

    lambda=E-p_q^2/12,
    p_-(E,lambda)=-sqrt(12(E-lambda)),
    w(E,lambda)=dp_-/dlambda=6/sqrt(12(E-lambda)).                     (9)

For I=(-gamma/2,gamma/2), every E is available at every lambda in I.
Multiplication by sqrt(w) in this change of variables gives the unitary
spectral chart to L2(I,d lambda;H_X). Averaging C_X with dt/(2pi), on
compact smooth lambda tests, evaluates that chart at lambda=0. Thus the
positive physical initial-data norm is ||v||^2 and its solution readout is

    Psi_v(q)=D_X exp(-iq omega_X)v.                                (10)

The clock-position norm at a slice is the weighted Hilbert norm

    K_X=Dom(X^(1/4)),
    ||Psi||_(K_X)^2=(1/6)||omega_X^(1/2)Psi||^2,
    D_X:H_X -> K_X is unitary with these norms.                     (11)

Completeness follows because omega_X^(1/2)/sqrt(6) has a bounded everywhere
defined inverse; (11) defines its domain with its equivalent graph norm.
The quadratic form interpretation includes all v in H_X, without assuming
second q derivatives exist as Hilbert vectors. Distributional solutions and
the original quadratic-clock Jacobian are retained.

For ANY ordinary isometry J:H_A->H_B define

    J^clock=D_B J D_A^(-1): K_A -> K_B.                             (12)

This is an exact isometry at each finite parameter value, not just in the
limit. D_A^(-1) is applied only on K_A; it is not a bounded operator on the
unweighted space. Using (8) and commutation of D_X with omega_X gives

    sup_(|q|<=Q) ||exp(-iq omega_B)J^clock Psi
                   -J^clock exp(-iq omega_A)Psi||_(K_B) -> 0.       (13)

For the eta step use J_delta,eta; for the delta step use the identity on the
common slow space. Composition gives an exact norm-preserving encoding from
K_A0 into the finite parent clock space:

    J_delta,eta^clock,0 = D_B_delta,eta J_delta,eta D_A0^(-1).       (14)

The intermediate D_A_delta factors cancel. The iterated limit of the dynamical
error in (13) is zero. These clock encodings depend on full energy operators and are
not spatially local maps or new canonical coordinate transformations.

This direct spectral derivation is consistent with the original construction
in [Round13](../clock-shell-round13/README.md). General group-averaging context
is Marolf, [Refined Algebraic Quantization: Systems with a single constraint](https://arxiv.org/abs/gr-qc/9508015).
No microscopic TFPT clock is derived
from that reference or from the change of variables.

## 5. Normalized spectators approximate the desired clock, quantitatively

Use momentum coordinates p in R^d and the normalized pure Gaussian

    chi_sigma(p)=(2pi sigma^2)^(-d/4) exp(-|p|^2/(4sigma^2)),
    (I_sigma v)(p)=v chi_sigma(p),       sigma>0.                    (15)

Then ||I_sigma v||=||v||, and

    <S>=d sigma^2/2,
    ||S chi_sigma||=sigma^2 sqrt(d(d+2))/2,
    Var(y_j)=1/(4sigma^2),       sum_j <y_j^2>=d/(4sigma^2).         (16)

For any E>=e_* and s>=0, rationalizing the square root gives

    0<=sqrt(12(E+s))-sqrt(12E)
       =sqrt(12) s/(sqrt(E+s)+sqrt(E)) <= sqrt(3) s/sqrt(e_*).      (17)

The spectral theorem for the commuting factors A and S and
|exp(ia)-exp(ib)|<=|a-b| therefore prove, for every v in H_A,

    sup_(|q|<=Q) ||exp(-iq omega_A0)I_sigma v
                      -I_sigma exp(-iq omega_A)v||
       <= Q sqrt(3) sigma^2 sqrt(d(d+2))/(2sqrt(e_*)) ||v||.         (18)

There is no upper-energy restriction on v in this bound. For a finite mean
energy v the enlarged mean energy is exactly <A>+d sigma^2/2. The comparison
holds for normalized bona fide Hilbert vectors; the packets themselves have
no strong L2 limit as sigma->0. Formula (18) is convergence after changing
embeddings, not construction of a forbidden zero-energy spectator vacuum.

To see the equivalent physical-norm statement, set

    I_sigma^clock=D_A0 I_sigma D_A^(-1).                            (19)

It is an exact isometry K_A->K_A0. Conjugating (18) by the D factors gives
the **same right-hand side** in K_A0 norm for
exp(-iq omega_A0)I_sigma^clock Psi-I_sigma^clock exp(-iq omega_A)Psi,
with ||Psi||_(K_A) in place of ||v||. This is the useful normalized encoding;
the naive unweighted tensor product of slice amplitudes is not an exact
physical-norm isometry.

Indeed, for Psi=D_A v, ||v||=1, the naive product I_sigma Psi has

    ||I_sigma Psi||_(K_A0)^2
      =<v tensor chi_sigma, sqrt(1+S/A)(v tensor chi_sigma)>,
    0<=||I_sigma Psi||_(K_A0)^2-1 <= d sigma^2/(4e_*),              (20)

while, by concavity of (1+x)^(1/4),

    ||I_sigma Psi-I_sigma^clock Psi||_(K_A0)
        <= sigma^2 sqrt(d(d+2))/(8e_*) ||Psi||_(K_A).               (21)

For ordinary unweighted solution readouts, the separate bound

    ||D_A0 exp(-iq omega_A0)I_sigma v
                      -I_sigma D_A exp(-iq omega_A)v||
      <= 3^(1/4) [1/(4e_*^(5/4))+|q|sqrt(3)/e_*^(3/4)]
                    sigma^2 sqrt(d(d+2))/2 ||v||                  (22)

follows by differentiating f_q(E)=3^(1/4)E^(-1/4)exp(-iq sqrt(12E))
and integrating its derivative from E to E+s. This explicitly controls
both the phase and the energy-dependent quadratic-clock shell factor.

For a chosen spectator energy budget epsilon>0 choose

    sigma^2=2epsilon/d.

Then <S>=epsilon and the bound (18) becomes

    Q sqrt(3)/sqrt(e_*) epsilon sqrt(1+2/d),                        (23)

but Var(y_j)=d/(8epsilon) and sum_j<y_j^2>=d^2/(8epsilon).
Small spectator energy thus costs delocalization which grows with n;
these packets are not localized microscopic vacua. On unit-spacing periodic
cubic lattices n=L^3,L>=2, ell<=12 and sum_k ell=6n imply
e_*>=3sqrt(3)n/2 at m=0 (and at least this for m>=0). This is an elementary
finite-size energy estimate, not a continuum theorem: restoring the spacing,
holding volume fixed or subtracting further vacuum energy changes the constants.

For any fixed sigma and finite lattice, (8), (14), (18) and a triangle
inequality compose. After eta->0 then delta->0 the finite-parent clock error
against the target A clock is bounded by (18); subsequently sigma->0 makes
it zero. The physical encoding of the target is exactly

    E_delta,eta,sigma^clock=D_B_delta,eta J_delta,eta I_sigma D_A^(-1),

and has norm one for every parameter. No simultaneous eta(delta,sigma,n)
rate follows: the Round15 residual constants grow with packet support/moments,
delta and volume. Density extends each fixed-packet limit, not a uniform limit
over this changing packet family.

## 6. Why independence does not exactly factor the clock dynamics

The ordinary Hamiltonian A+S has a product Schrödinger evolution. Its clock
Hamiltonian sqrt(12(A+S)) does not split as sqrt(12A)+sqrt(12S). In the A
spectral representation, a spectator momentum s gives the system frequency
sqrt(12(E+s)). For two different system energies, their frequency difference
generally depends on s. Tracing a finite-width spectator packet therefore
does not in general give the pure A clock evolution. This remains true even
though A and S strongly commute; (18) is precisely the error control needed.

Likewise (20) is why merely tensoring a normalized spectator onto the old
clock wavefunction does not retain its exact physical norm. A delta function
at p=0 would make those formal replacements exact, but is not in L2 and is
not the packet (15). Imposing p_j=0 as ordinary operator kernels would give
the zero Hilbert space, because {p=0} has Lebesgue measure zero.

## 7. Optional exact reduction at the limit, with an explicit new choice

The limiting A_0 is invariant under all y translations. Their strongly
commuting self-adjoint generators P_y,j commute with C_A0 and omega_A0.
One may **choose a new constrained limit model** with the constraints

    C_A0=0,        P_y,1=...=P_y,d=0.                              (24)

This choice changes physical content; symmetry alone does not declare a
physical mode to be gauge. There is nevertheless an exact positive reduction,
without a false L2 kernel. In the simultaneous (E,p,p_q) representation use

    lambda=E+|p|^2/2-p_q^2/12,
    w(E,p,lambda)=6/sqrt(12(E+|p|^2/2-lambda)),
    (Z f)(lambda,p,E)=sqrt(w) f(E,p,p_-(E,p,lambda)).                 (25)

On I=(-e_*/2,e_*/2), Z is unitary to
L2(I,d lambda) tensor L2(R^d,dp;H_A). The original joint constraint becomes
M_lambda and the extra momenta become M_pj. For finite sums in these Z coordinates
of compact smooth lambda functions, Schwartz p functions and vectors in H_A, integration by
parts gives absolutely integrable Fourier matrix elements. Averaging with
dt/(2pi) and d^d a/(2pi)^d gives the positive form

    eta(f,h)=< (Zf)(0,0), (Zh)(0,0)>_(H_A).                        (26)

The null quotient completes to H_A, since evaluation is onto. At the shell
w(E,0,0)=6/sqrt(12E), so the quadratic-clock norm and D_A readout are exactly
the original ones. Time translations act by exp(-iq omega_A) on the reduced
data. The ordinary joint L2 kernel is still zero; the construction is a
distributional average on the declared test space. It is separate from the
normalizable approximation (15)--(23), not a claim that their Gaussian
vectors converge to a normalized rigging vector in the old Hilbert space.

The full d-dimensional symmetry in (24) is **not** a symmetry to impose at
finite delta. For an actual nonzero ell=l complement eigenvector with
NN^* eigenvalue mu>0, zero source and coordinate y, the Round15 effective
potential has curvature

    partial_y^2 V_delta=l^2/[l+delta+delta/(delta^2+l)+mu/delta]>0.  (27)

The actual staggered l=8, mu=4 channel has curvature 7008/2231 at delta=1/3.
Thus the corresponding free momentum does not commute with A_delta. All
six homogeneous tensor coordinates already have separate translation
symmetries, but the additional 4(n-1) complement directions do not. A claim
of the entire limit-only gauge reduction on the finite parent is rejected.

## 8. Energy-origin input and exact remaining scope

The construction above uses B=H-E_fast in C_B=B-P_q^2/12. The original
unsubtracted finite parent would instead have C_H=H-P_q^2/12 and a different
clock. Since E_fast diverges and H>=E_fast+gamma,

    ||D_H|| <=3^(1/4)(E_fast+gamma)^(-1/4) ->0.                     (28)

Its normalized slice readout cannot approach the finite nonzero readout
D_A v by the same ordinary isometry. Removing a rapidly rotating overall
clock phase does not by itself repair the energy-dependent square root or
its shell measure. The source-independent subtraction is an explicit
renormalization/clock-origin prescription; it is not derived from TFPT and
is not a harmless constant once the quadratic clock has been fixed.

Nothing here derives the negative sheet, the trace pair, extra constraints,
microscopic state, charged scaling fields, 4D chirality or uniform continuum
locality. The new result is narrower and constructive: actual spectator
energy is either controlled by normalized packets with proved errors and
costs, or removed by a declared **limit-only** distributional constraint
choice; and the existing local-parent quantum limit really passes through
the quadratic clock with its correct norm under its stated energy prescription.

## Reproduction

`checker.py --ward-source /absolute/path/to/free_scalar_ward.py` imports the
original Ward Hamiltonian/source, checks the exact scalar spectrum and positive
lower-bound inputs, the real staggered complement curvature, continuous
Gaussian moments and coordinate widths, shell half densities, weighted norm
and error constants, plus explicit failure controls. Every check uses an
explicit exception, so optimization does not remove it. These finite exact
checks support the analytic proof; they do not numerically certify an
infinite-dimensional limit or create a finite CCR substitute.
