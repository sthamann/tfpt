# Round17: exact source intertwining and source-stabilized adiabatic dynamics

2026-09-06. NON-RH constructive research. All statements fix the finite lattice
and the explicit [Round15 local-parent family](../local-parent-round15/PROOF.md).
They preserve the literal Weyl-quadratic matter sources; no commuting-source
replacement, finite CCR model, microscopic selection or continuum limit is used.

## 1. Result and exact hypotheses

Let x=(phi,q) in R^(7n) denote all slow coordinates, a in R^(28n) the added
fast coordinates, and use the original definitions

    B_delta,eta=H_delta,eta-E_fast(delta,eta),
    A_delta=-Delta_x/2+V_m(phi)+V_delta(x),
    (J_delta,eta psi)(x,a)=psi(x) chi_eta(a-f_delta(x)),
    chi_eta(b)=det(Omega_eta/pi)^(1/4) exp(-b^T Omega_eta b/2),
    Omega_eta=sqrt(eta) K_delta^(1/2).                         (1)

K_delta>0 is independent of x and f_delta is a real polynomial of degree at
most two. J is an exact ordinary isometry. The fast zero-point subtraction
is explicit input, not a clock-origin derivation. The actual matter sources
Q_alpha=(Bcal,-B_v J_v) are the self-adjoint closures of real homogeneous
Weyl quadratics on scalar coordinates, extended by identity on all other
coordinates. In particular the Q_alpha generally do not commute.

For fixed delta>0, any scalar source and any compact smooth slow psi,

    ||(Q_alpha J-J Q_alpha)psi||
          <= C_1 eta^(1/4)+C_2 eta^(1/2),
    ||(Q_alpha Q_beta J-J Q_alpha Q_beta)psi||
          <= sum_(k=1)^4 C_k eta^(k/4).                       (2)

The second statement includes every **ordered** pair, in particular Q_alpha^2.
The finite constants below are computable from the actual source coefficients,
K_delta, f_delta and the compact test. No invariance of evolved Schwartz or
compact support is needed.

More importantly, (2) does close the dynamical bridge. For a nonzero affine
constraint characteristic c(t)=exp(t A_c)c0, let h_B(t) and h_delta(t) be the
closed forms

    h_X(t)[u]=q_X[u]+g sum_alpha c_alpha(t)<u,Q_alpha u>
                        +g^2|c(t)|^2 sum_alpha ||Q_alpha u||^2.    (3)

Their unitary propagators obey the **full, uncompressed** limit

    sup_(|t|<=T) ||V_B(t,0)J_delta,eta psi
                          -J_delta,eta V_delta(t,0)psi|| ->0     (4)

for every slow Hilbert vector. The limit is eta->0 at fixed delta, lattice,
g and c0!=0. The analogous delta->0 result holds with A_delta replaced by
A_0=A_+ tensor I+I tensor(-Delta_extra/2), retaining all 4n+2 spectators.
At c0=0 or g=0, the source terms vanish and the original Round15 result applies.
No uniform limit in a varying c0, delta, volume or state family is asserted.

The missing common **form** core is proved here. We do not assume the fourth-
order expression in (3) is essentially self-adjoint on compact tests, or that
static resolvent convergence alone establishes a nonautonomous limit.

## 2. Gaussian directional derivatives, with all constants and powers

For fast-space vectors d_1,...,d_k, Fourier transformation of chi_eta makes
the differentiation norm a Gaussian momentum moment. The momentum covariance
is Omega_eta/2. Wick's formula and
|d_i^T Omega_eta d_j|<=sqrt(d_i^T Omega_eta d_i d_j^T Omega_eta d_j) give

    ||(d_1.grad_a)...(d_k.grad_a)chi_eta||_a
       <= M_k eta^(k/4) product_j ||K_delta^(1/4)d_j||,
    M_k=sqrt((2k-1)!!)/2^(k/2),                  M_0=1.          (5)

There are (2k-1)!! Gaussian pairings, including coincident directions. This
bound is valid for arbitrary nonorthogonal directions and every fast dimension;
dimension dependence is contained in the displayed K-weighted vectors.

For an ordered list I=(i_1,...,i_r) of slow derivative indices, including
repetitions, let P_(1,2)(I) be its partitions into singleton/pair blocks. Set
d_{i}=partial_i f_delta and d_{ij}=partial_i partial_j f_delta. Since all
third derivatives of f vanish, the exact chain rule is

    partial_I chi_eta(a-f_delta(x))
       =sum_(pi in P_(1,2)(I)) (-1)^|pi|
          [product_(B in pi) d_B.grad_a] chi_eta(a-f_delta(x)).   (6)

Derivatives in a commute; sources need not. Formula (6) includes derivatives
of the x-dependent first derivatives of f through its pair blocks.
For a compact set C in slow space define

    F_C=max_(x in C, |B|=1,2) ||K_delta^(1/4)d_B(x)||,
    G_r(C,eta)=sum_(pi in P_(1,2)({1,...,r}))
                       M_|pi| eta^(|pi|/4) F_C^|pi|.           (7)

Then sup_C ||partial_I chi_eta||_a<=G_r. The partition multiplicities for
r=1,2,3,4 give explicitly

    G_1=M_1 F eta^(1/4),
    G_2=M_1 F eta^(1/4)+M_2 F^2 eta^(1/2),
    G_3=3M_2 F^2 eta^(1/2)+M_3 F^3 eta^(3/4),
    G_4=3M_2 F^2 eta^(1/2)+6M_3 F^3 eta^(3/4)+M_4 F^4 eta.       (8)

For eta<=1 these are bounded by finite constants times eta^(1/4), but the
more precise powers in (8) matter when a particular first derivative vanishes.
Small eta broadens the fast coordinate Gaussian; it is its momentum/slow
derivative norm that becomes small. A falsely narrowing Gaussian would reverse
these powers and fail (2).

## 3. Exact differential source intertwining, including ordered squares

A Weyl quadratic has differential form

    Q=sum_(|beta|<=2) a_beta(x) partial_x^beta,                 (9)

where second-order coefficients are constant, first-order coefficients are
linear, and zeroth-order coefficients are quadratic plus the Weyl constant.
Every ordered product Q_alpha Q_beta is a differential operator of order
at most four with polynomial coefficients; they include the ordering terms
from differentiating the coefficients of Q_beta. No classical-square
substitution is made.

For ANY such polynomial differential operator P of order m<=4, the product
rule gives the exact identity on compact smooth psi

    (P J-J P)psi
      =sum_beta a_beta(x) sum_(0<nu<=beta) binom(beta,nu)
             (partial^(beta-nu)psi)(partial^nu chi_eta).      (10)

Consequently, if supp(psi) is contained in C,

    ||(P J-J P)psi||
      <=sum_beta ||a_beta||_(infinity,C)
          sum_(0<nu<=beta) binom(beta,nu)
                  ||partial^(beta-nu)psi||_x G_|nu|(C,eta).   (11)

This proves (2) simultaneously for all actual sources and all ordered pairs.
Their number at fixed lattice is finite. It also proves (2) for sources
with added real constants, although the present input is the original one.

For each positive eta, J psi is compact in x and smooth Gaussian-times-
polynomial in a after any finite sequence of the displayed derivatives.
It therefore lies in Dom Q_alpha Q_beta and Dom B_delta,eta. Cutoffs in a
and the already established source/Schrodinger cores identify these expressions
with their closed operators. The self-adjoint form representative of (3) acts
on J psi by B J psi+g c.Q J psi+g^2|c|^2 sum Q_alpha^2 J psi: integration by
parts against the full form domain proves this domain inclusion.

Combining (11) with the original Round15 B residual yields, uniformly on
compact c/time sets and compact smooth psi,

    ||(h_B(t)J-J h_delta(t))psi||
       <= sum_(k=1)^4 C_(k,delta,psi,g,c,T) eta^(k/4).          (12)

Here h_delta(t)psi denotes its actual fourth-order expression, which is in
L2. Compact smooth tests belong to its representing operator domain; that
inclusion does not assert they are its operator core.

## 4. A common form core without a fourth-order operator-core assumption

Let A=-Delta_x/2+V(x) be any one of A_delta or A_0, with smooth V>=0.
For all the actual sources define

    D=Dom(A^(1/2)) intersection (intersection_alpha Dom Q_alpha),
    ||u||_D^2=||u||^2+q_A[u]+sum_alpha ||Q_alpha u||^2.          (13)

It is a dense Hilbert space. We prove C_c^infinity is dense in this norm.

First take radial cutoffs chi_R equal to one on |x|<=R and zero for |x|>=2R,
with derivatives of order j bounded by C_j R^(-j). Since u is in H1,
chi_R u->u in H1 and in ||sqrt(V).|| by dominated convergence. The quadratic
source commutator has only the terms

    [Q,chi_R]u = constant*(partial chi_R)(partial u)
               +constant*(partial^2 chi_R)u
               +linear(x)*(partial chi_R)u.                 (14)

The first two vanish by the H1 bound and R^(-1),R^(-2). On the annulus,
|linear(x) partial chi_R| is uniformly bounded, so the last term vanishes
by the escaping L2 tail of u. Thus all Q graph norms converge as well.
Distributional identification with the self-adjoint Q is legitimate: compact
cutoffs approximate Schwartz in its graph norm, while Schwartz is its known
core, so C_c^infinity is also a core for each individual Q.

Next mollify the compact H1 vector chi_R u with a compact smooth convolution
kernel. The constant second-derivative part of Q commutes with convolution.
For a linear first-order coefficient the commutator is an O(epsilon) bounded
convolution acting on grad(chi_R u). Quadratic multiplication commutes up to
O(epsilon)||chi_R u|| on the enlarged compact support. Hence

    Q[(chi_R u)*rho_epsilon]-(Q chi_R u)*rho_epsilon ->0

in L2, for every source. The H1 convergence and boundedness of V on that compact
set also give A-form convergence. First taking epsilon->0, then R->infinity,
proves the required common form-core statement. It works even if the sources'
second-order coefficient matrices are individually degenerate or indefinite.

## 5. Compactness and the actual varying-space lower bound

For the original fast oscillator decomposition, B>=A_delta tensor I as
quadratic forms on the full (x,a) space. Indeed the fast Hamiltonian minus
E_fast is pointwise bounded below by V_delta(x), and the complete slow
kinetic and V_m terms remain. Thus q_B controls

    (1/2) sum_i ||partial_i Psi||^2
                    +||sqrt(V_m+V_delta)Psi||^2.             (15)

It does not impose a uniform fast-coordinate confinement as eta->0.
Nevertheless it supplies precisely the needed **projected** compactness.
Suppose Psi_eta has uniformly bounded norm, B form and all Q graph norms,
and J_eta^* Psi_eta converges weakly to u. Write u_eta=J_eta^*Psi_eta.
For every compact slow set C,

    partial_i u_eta=J_eta^*(partial_i Psi_eta)
              +integral da (partial_i chi_eta) Psi_eta,
    ||last term||_(L2(C))<=C_C eta^(1/4)||Psi_eta||.           (16)

There is no assertion of a global uniform bound on that last coefficient:
partial_i f is linear and may be unbounded in x. Compact exhaustion and weak
lower semicontinuity in (15) imply u is in Dom(A_delta^(1/2)) and

    q_A_delta[u]<=liminf_eta q_B[Psi_eta].                    (17)

For the potential part, multiplication by sqrt(V_m+V_delta) commutes with
J^*, a pointwise contraction in a; for the gradient part use (16) on increasing
compact regions. Their joint lower bound follows by first restricting both
nonnegative contributions to one region, then exhausting the full space.

For any z in C_c^infinity, the adjoint form of (2) gives

    <Q_alpha z,u_eta>=<J z,Q_alpha Psi_eta>+o(1).             (18)

The Q errors vanish against bounded Psi_eta. Weak compactness of
J^* Q_alpha Psi_eta and (18) identify its weak limit as Q_alpha u.
Each Q is self-adjoint on its known domain, so distributional membership in
its maximal L2 domain is genuine membership in Dom Q, not a guessed extension.
The same reasoning works in time-integrated weak L2 spaces. In particular,
uniform energy bounds give limiting u in L_infinity([-T,T];D).

For completeness this proves a precise generalized **form/Mosco** statement.
At fixed c!=0,g!=0 put w=|g||c| and l_alpha=g c_alpha/(2w). Then

    h_X(c)[u]+||u||^2
       =q_X[u]+sum_alpha ||w Q_alpha u+l_alpha u||^2
                                      +(3/4)||u||^2,         (19)

since sum l_alpha^2=1/4. Formula (19), (17),(18) and weak lower semicontinuity
show the lower bound for every sequence with J^*Psi_eta weakly convergent
and bounded positive form. Recovery holds for compact smooth z with Psi_eta=Jz
by (1),(2) and the exact Round15 compressed B form. For general u in D,
use the common form core in Section 4 and a diagonal approximation. This is
an explicit lower-bound/recovery statement for the embeddings J; it does not
require J to be onto or an inverse on the entire fast Hilbert space.

## 6. Full nonautonomous characteristic convergence

Fix g!=0,c0!=0 and a compact time interval. The characteristic never crosses
zero, so w(t) has a positive minimum. Each (3) has a complete common form
domain (for its own fixed eta) and smooth time coefficients. The exact bounds
of the vertex-preserving construction apply to every base X>=0:

    q_X+(w^2/2)sum ||Q_alpha u||^2+(1/2)||u||^2
        <= h_X(t)[u]+||u||^2,
    |partial_t(h_X(t)[u]+||u||^2)|
        <=5||A_c|| (h_X(t)[u]+||u||^2).                       (20)

They give the unique common-form propagator and its energy estimate, as in
Assumption 3.8 and Theorem 3.10 of
[Balmaseda, Lonigro and Perez-Pardo](https://arxiv.org/html/2112.11063v2).
The dense complete common form space, positive norm and smooth coefficients
are explicitly verified here; no shared operator domain is required.

Start with compact smooth psi and let Psi_eta(t)=V_B(t,0)J psi. Its initial
(20) energy is uniformly bounded by (2) and the Round15 B residual. The energy
estimate therefore bounds q_B[Psi_eta(t)] and each ||Q_alpha Psi_eta(t)||
uniformly on the interval. The corresponding projected vectors u_eta(t)=J^*
Psi_eta(t) have weakly convergent subsequences, with limit u in L_infinity(D)
by Section 5. For each compact smooth test z,

    i partial_t <z,u_eta(t)>=<h_B(t)Jz,Psi_eta(t)>
                         =<h_delta(t)z,u_eta(t)>+o(1),       (21)

where the last error is uniform on the time interval by (12). The norms
||h_B(t)Jz|| are uniformly bounded, so these scalar amplitudes are uniformly
equicontinuous. A countable dense test set and diagonal compactness give a
weakly continuous limiting u with the initial value psi.

The limit of (21) is initially tested on C_c^infinity. Section 4 and the
uniform D bound extend it to every fixed z in D. The resulting equation is
the weak common-form Schrodinger equation, with

    u in L2([-T,T];D),       partial_t u in L2([-T,T];D*).     (22)

Its solution is unique. One may either use the common-form theorem just
cited, or use the Hilbert-triple energy identity: temporal mollification and
duality give d||u||^2/dt=2Re<partial_t u,u>=0 for a solution with Hermitian
h_delta(t). Applied to the difference of two solutions with the same initial
data, this identity gives uniqueness. The Hilbert-triple representative is
strongly continuous in H; no smoothness of an evolved Schwartz vector is
inferred. Consequently u(t)=V_delta(t,0)psi, with unchanged norm ||psi||.

Finally,

    ||Psi_eta(t)-J V_delta(t,0)psi||^2
       =2||psi||^2-2Re<V_delta(t,0)psi,u_eta(t)> ->0.          (23)

All subsequences have the same limit, so convergence holds for the original
family. Uniform weak convergence against a dense test set, followed by a
finite net along the continuous limiting orbit, makes (23) uniform on the
compact time interval. Approximate arbitrary Hilbert initial data by compact
smooth psi and use the two unitary propagators and ||J||=1 to obtain (4).
This proves vanishing **uncompressed leakage**, not just convergence after
applying J^*. It does not assume essential self-adjointness of a fourth-order
minimal expression or apply Duhamel to an unproved invariant core.

## 7. The following delta limit also retains the actual sources

At fixed finite lattice, V_m+V_delta is a nonnegative polynomial potential
converging uniformly on compact x sets to the total potential of A_0 (called
V_0, already including V_m, in the Round15 local-parent proof). All source operators Q_alpha
are independent of delta. Replace J by identity and B by A_delta in the
argument above. The potential convergence and fixed positive kinetic energy
give the version of (17) by compact exhaustion. Source graph compactness is
ordinary weak closedness. The source terms in the test residual are identical,
and the remaining A_delta-A_0 residual vanishes on C_c^infinity. The same form
core and weak uniqueness prove

    sup_(|t|<=T)||V_delta(t,0)psi-V_0(t,0)psi|| ->0.           (24)

The target still includes the real 4n+2 free tensor spectators. Since the
Q_alpha act only on the scalar factor, (24) is compatible with that tensor
splitting, but neither their clock energy nor their physical content is deleted.
Equations (4),(24) are sequential eta->0 then delta->0. Even though the source
residual has explicit powers, the nonautonomous convergence proof is strong
and statewise; it supplies no universal rate for the interacting dynamics,
no arbitrary simultaneous eta=delta choice and no uniform volume estimate.

## 8. Costs, actual-source tests and claim boundary

For a compact test of derivative order at most four, (7),(11) give finite
constants from the K_delta-weighted first/second derivatives of f_delta, the
source coefficients and finitely many Sobolev norms. K_delta is 28n dimensional
(28-by-28 Fourier blocks), f_delta contains the nonlocal screened source kernel,
and both the coefficients and source count grow with lattice/stiffness data.
No polynomial-cost many-body simulation or bounded-cost continuum follows.

The checker imports the actual L2 Ward stress/energy/current, constructs the
literal four sources of the normalized (pi,pi,0) mode with all eight scalar
coordinates, verifies a nonzero Poisson/Weyl commutator and the original
operator-square ordering constants, and tests the exact differential/Gaussian
identities through fourth order. The fourth source in this particular mode
vanishes identically and is retained as a zero member, not invented as a
nonzero excitation. Generic polynomial-source tests are marked
as algebra controls, not substituted for the actual-source regression.

This result supplies the source-intertwining and characteristic-dynamics
bridge for the explicitly chosen source-stabilized extension of the local
parent. It does not identify that extension with the original microscopic
TFPT model, remove its new source-square terms or fast vacuum subtraction,
derive the clock, prove relativistic locality, select charged matter, or close
the full T1--T8 contracts. The proof concerns the declared positive form
realizations, not uniqueness of every extension of their formal expressions.
