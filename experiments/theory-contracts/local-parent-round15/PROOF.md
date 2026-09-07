# Round15: a local positive dynamical family with a controlled quantum TT limit

Unpromoted non-RH research, 2026-09-06. This constructs a new family of local
Hamiltonians, not a proof that TFPT selects it or that the old reduced scalar
observable net has become causal. All statements below fix the finite periodic
staggered lattice before taking the two auxiliary limits.

## 1. Result

There is an explicit real, finite-range, translation-invariant Hamiltonian on
**35 canonical pairs per lattice site**, with positive kinetic energy and a
nonnegative multiplication potential. Its quantum realization is uniquely
self-adjoint and has the ordinary positive Hilbert-space norm. No gauge
constraint, negative-norm mode, or instantaneous multiplier is imposed in this
new model. All 28 auxiliary pairs per site are genuine physical oscillators.

For fixed stiffness parameter delta>0, a normalized displaced Gaussian embeds
the seven-field slow Hilbert space isometrically in the full theory. After
subtracting a specified source-independent oscillator zero-point energy,
the full unitary evolution converges on these encoded states as the auxiliary
mass eta tends to zero. The limiting slow Hamiltonian is derived exactly.
Taking delta to zero afterwards gives the chosen positive scalar/TT dynamics
**tensored with 4n+2 additional free tensor-coordinate modes**, where n is the
number of sites. The TT/matter factor, including its quartic term, has the
original canonical norm and unitary evolution. The extra factor is not a gauge
quotient and has no normalizable zero-energy vector.

This is a constructive local dynamical approximation to the specified finite
model, with strong quantum dynamical convergence, not merely a static KKT
representation. It pays for that result with extra physical modes, a singular
parameter limit, a diverging bare source contact, and an explicit divergent
energy subtraction. None of those costs is a derived TFPT prescription.

## 2. Actual local operators and source

Use the six orthonormal symmetric-tensor components (11,22,33,23,13,12), the
Round7 staggered masks, and the local operators of Round10:

    ell = -Delta,       D D* = ell I_6,
    N = [V*, t],        t = (1,1,1,0,0,0)^T.

D maps 18 oriented link fields to six tensor fields. N maps three staggered
vector fields and one scalar trace field to tensors. All are finite-range;
ell commutes with N, and stars are adjoints in the actual real lattice inner
products. In physical-position Fourier coordinates N=[B^T,t] up to a harmless
unitary vector phase, with

    B B^T = (ell I + kappa kappa^T)/2,
    B t = kappa,       det(N* N)=ell^3/2  (ell>0).

For each nonzero momentum P=I-N(N*N)^(-1)N* is the rank-two TT projector.
Write P_0 for this projector on nonzero modes and zero on the whole homogeneous
tensor sector. P_0 is used only to describe the derived limit; it is not an
input coupling in the local Hamiltonian.

The actual Ward frontend has

    tau_ii(x) = (pi_x^2-m^2 phi_x^2)/2 + sigma_ii(phi;x),
    tau_ij(x) = sigma_ij(phi;x), i!=j.

Thus sigma is the local, configuration-only, quadratic gradient-stress
representative, with exactly the original staggered source placements.
P_0 tau=P_0 sigma. Choosing sigma, rather than the full momentum-dependent tau,
is part of this new finite-parameter family: trace responses at finite delta
are not claimed to equal those of the old source. In the target TT limit the
sources agree exactly. The checker imports the original Ward formulas and
checks this decomposition at every tensor component and all eight L=2 sites,
and checks a nonzero normalized actual TT polynomial.

## 3. A genuinely dynamical, local, positive Hamiltonian

Let x=(phi,q) be unconstrained slow coordinates: one scalar and all six real
tensor components at every site. Their momenta are (pi,p). Add fast coordinates
a=(E,u,h): E has 18 components, u has four, and h has six. Every fast coordinate
has its own canonical momentum p_a. No means are deleted. For delta,eta>0 set

    M_delta = delta I_6 + delta^(-1) ell I_6,
    H_delta,eta = (||pi||^2+||p||^2)/2 + V_m(phi)
                 + ||p_a||^2/(2 eta) + W_delta(phi,q,E,u,h),

    W_delta = ||D* q+E||^2/2 + delta ||u||^2/2
              + <h,M_delta h>/2
              + ||D E-Nu-h-g sigma(phi)||^2/(2 delta).       (1)

V_m is the exact free-scalar gradient/mass potential, m^2>=0. Every term in
(1) is nonnegative. h's gradient energy is local: <h,ell h>=||D*h||^2.
The last square is also a finite-range local interaction; expanding it
does not introduce any inverse spatial operator. Its bare source contact is
g^2||sigma||^2/(2 delta), which diverges as delta tends to zero.

All 35n coordinate-momentum pairs have nonsingular positive kinetic Hessian.
There are no primary or secondary gauge constraints. Hamilton's equations
are ordinary local polynomial differential equations, with the matter
backreaction fixed by differentiation of the same potential. In particular
no unpreserved guessed Gauss law is imposed. Nonnegative conserved energy
bounds all velocities at each fixed delta,eta; on any finite time interval
coordinates are bounded by their initial values plus this velocity bound.
The smooth finite-dimensional vector field therefore has complete classical
flow. This elementary completeness argument needs no confining potential.

Quantize on L2(R^(35n)) with p=-i partial and the displayed multiplication
potential. A constant linear rescaling makes the kinetic energy an ordinary
Laplacian. The standard essential-self-adjointness theorem for a smooth
nonnegative Schrödinger potential applies on C_c^infinity. Equivalently the
usual cutoff energy proof has zero lower-bound defect here. The closure is
the unique nonnegative self-adjoint Hamiltonian; its unitary group exists
for all times. This is not a finite-matrix approximation to the CCR.

## 4. Exact elimination at finite delta, including the zero mode

Shift only for calculation F=E+D*q and put

    j = ell q+g sigma(phi),
    L_delta = ell I_6 + delta I_6
              + delta^(-1) N N* + M_delta^(-1),
    R_delta = L_delta^(-1).                              (2)

The occurrence of inverses in (2) describes the result of eliminating
fields, not the local parent couplings in (1). Introduce lambda=R_delta j.
The unique minimizer over fast coordinates is

    E_* = D*(lambda-q),
    u_* = -delta^(-1) N* lambda,
    h_* = -M_delta^(-1) lambda.                          (3)

Indeed the residual at (3) is -delta lambda. The four positive contributions
at this point sum to <lambda,L_delta lambda>/2. Consequently

    min_a W_delta = <j,R_delta j>/2 =: V_delta(x),
    W_delta(x,a)=V_delta(x)+(a-f_delta(x))^T
                           K_delta(a-f_delta(x))/2,       (4)

where f_delta=(E_*,u_*,h_*) and the source-independent fast Hessian is

    C=[D,-N,-I_6],
    K_delta=diag(I_18,delta I_4,M_delta)+delta^(-1) C*C>0. (5)

All these identities are exact on the full finite real lattice, including
homogeneous fields. In particular there is no inverse of ell at its zero.
f_delta is a polynomial of degree at most two in x.

On a Fourier fiber with ell=l>0 set

    a_delta(l)=l+delta+delta/(delta^2+l).

Then R_delta=(a_delta(l) I+delta^(-1)NN*)^(-1). It has eigenvalue
1/a_delta(l) on TT, and eigenvalues 1/(a_delta(l)+mu/delta) on the four
complement directions, where mu>0 ranges over the nonzero eigenvalues of NN*.
At l=0, N=[0,t]; R_delta has eigenvalue delta/(delta^2+1) on the five
traceless means and delta/(delta^2+4) on the trace mean. Therefore

    R_delta --> R_0 := P_0 ell_nonzero^(-1)              (6)

in matrix norm at each fixed finite lattice. All six homogeneous source
components disappear in this limit; this is dynamically implemented by the
h family, rather than omitted by an unsatisfied homogeneous Gauss law.

An explicit finite-lattice bound for 0<delta<=1 is

    ||R_delta-R_0|| <= delta C_L,
    C_L=max(1, max_(l>0) (1+l^(-1))/l^2,
                  max_(l>0,mu>0) mu^(-1)).              (7)

The first bound follows by subtracting the two TT reciprocals; the second
and third follow from positivity of the corresponding denominators. C_L
is not uniform in growing volumes. Since j is quadratic at most, (7) gives
an explicit pointwise error <=delta C_L||j(x)||^2/2 in the effective
potential. The sign of the full kernel difference is not asserted: TT
eigenvalues approach from below, while complement/zero eigenvalues are
positive and approach zero.

## 5. The entire desired positive square, not just its quartic term

Define on the seven-field slow space

    A_delta=-Delta_x/2+V_m(phi)+<j,R_delta j>/2.

Each A_delta is the uniquely self-adjoint nonnegative Schrödinger operator
on its C_c^infinity core. By (6), its limiting multiplication potential is

    V_0 = V_m + <ell P_0 q+g P_0 sigma,
                    ell_nonzero^(-1)(ell P_0 q+g P_0 sigma)>/2
        = V_m + <q_TT,ell q_TT>/2 + g<q_TT,sigma>
                 + g^2<sigma,P_0 ell_nonzero^(-1)sigma>/2. (8)

This is exactly the full chosen positive TT/matter potential. The q-dependent
quadratic and cubic terms are recovered together with the g^2 term; keeping
the old q terms unchanged while screening only the positive quartic would
not preserve positivity at large scalar amplitudes.

An orthogonal canonical splitting of the 6n q coordinates gives 2(n-1) TT
coordinates and 4n+2 complement/homogeneous coordinates q_extra. Thus

    A_0 = A_+ tensor I + I tensor (-Delta_q_extra/2).    (9)

The second factor is actual extra free physical content, not gauge. The
isometry psi -> psi tensor chi, with any normalized chi in its L2 space,
preserves the TT/matter norm. Its evolved range is not fixed unless chi is
an eigenvector, but after tracing out the independent extra factor the
TT/matter evolution is exactly exp(-it A_+) for every initial product state.
There is no L2 zero-energy chi. Imposing p_extra=0 as an ordinary kernel
would erase the entire state space and is not done.

On every C_c^infinity test function, A_delta psi -> A_0 psi by polynomial
coefficient convergence on the compact support. The same core criterion
proved below gives strong resolvent and strong unitary convergence, uniform
for time in compact intervals. This is a fixed-regulator limit, not a
continuum or infinite-volume theorem.

## 6. Positive quantum encoding and a computed adiabatic residual

Fix delta>0 for this section. Put d_f=28n, K=K_delta, f=f_delta and

    Omega_eta=sqrt(eta) K^(1/2),
    chi_eta(b)=det(Omega_eta/pi)^(1/4)
                         exp(-b^T Omega_eta b/2),
    E_fast(delta,eta)=Tr K^(1/2)/(2 sqrt(eta)),
    (J_delta,eta psi)(x,a)=psi(x) chi_eta(a-f(x)).       (10)

The Gaussian is normalized for each x, hence J*J=I exactly. The frozen fast
operator has ground eigenvalue E_fast independent of x, so (4) implies

    H_delta,eta-E_fast >= 0                             (11)

as quadratic forms. The inequality retains the positive slow kinetic energy.
The energy subtraction in (11) is explicit and divergent; this argument does
not justify changing the TFPT clock's already fixed absolute energy origin.

For real normalized chi, <chi,partial_i chi>=0. Direct Gaussian integration
gives the **exact** compressed quadratic form

    <J psi,(H_delta,eta-E_fast)J psi>
      = <psi,A_delta psi>
        + sqrt(eta)/4 integral |psi(x)|^2
                 sum_i (partial_i f)^T K^(1/2)(partial_i f) dx. (12)

The added term is nonnegative and generally nonzero. A claim of exact finite
eta quantum elimination would miss it. Because f is degree <=2 it is a
quadratic multiplication correction, with coefficients computed from the
same actual source and K. No source-dependent Jacobian is introduced.

There is also an operator, rather than merely form, estimate. Let
B_eta=H_delta,eta-E_fast. For psi in C_c^infinity(R^(7n)),

    (B_eta J-J A_delta)psi
        = -sum_i (partial_i psi)(partial_i chi_eta)
          -psi sum_i partial_i^2 chi_eta/2.             (13)

The derivatives include f(x) through b=a-f(x). If d_i=partial_i f and
e_i=partial_i^2 f, exact Gaussian moments imply

    ||partial_i chi_eta||_a
        = eta^(1/4) (d_i^T K^(1/2)d_i/2)^(1/2),
    ||partial_i^2 chi_eta||_a
        <= eta^(1/4)(e_i^T K^(1/2)e_i/2)^(1/2)
           +sqrt(3 eta)/2 d_i^T K^(1/2)d_i.             (14)

For the second line the quadratic Gaussian term has norm sqrt(3) s/2,
where s=d_i^T Omega_eta d_i; the odd e_i term and even quadratic term are
in fact orthogonal, so the displayed triangle bound is conservative.
Together (13)-(14) give computable finite constants on the compact support:

    ||(B_eta J-J A_delta)psi||
       <= C_(delta,psi) eta^(1/4)+D_(delta,psi) sqrt(eta) -->0. (15)

J psi belongs to Dom B_eta: it is smooth, compact in x and Gaussian in a,
and its displayed operator image is square-integrable. Cutoffs in a and the
Schrödinger operator core justify the equality with the unique closure.

### Why this proves convergence of the full unitary dynamics

Here is a direct core/resolvent argument, so no invariance of the interacting
Schwartz space, uniform operator-domain assumption, or formal Born-Oppenheimer
series is needed. For z nonreal and h=(A_delta-z)psi, psi in C_c^infinity,

    (B_eta-z)^(-1)J h - J(A_delta-z)^(-1)h
      = -(B_eta-z)^(-1)(B_eta J-J A_delta)psi.           (16)

Its norm tends to zero by (15) and the self-adjoint resolvent bound. Such h
are dense because C_c^infinity is a core. The uniform operator bound extends
(16) to every slow h; both z and its conjugate are allowed. Products of
resolvents and Stone-Weierstrass then give the same intertwining limit for
every continuous function vanishing at infinity.

For core psi, ||B_eta J psi|| stays bounded by (15). A spectral cutoff at
|E|<=M therefore leaves a tail <=constant/M, uniformly for small eta.
The analogous bound holds for A_delta psi. Apply the continuous functional
calculus result to a cut-off exp(-itE), then send M to infinity. This proves

    ||exp(-it B_eta)J_delta,eta psi
                -J_delta,eta exp(-it A_delta)psi|| -->0. (17)

It holds for all slow psi by density and the isometry. On core states the
two time-dependent expressions have uniformly bounded time derivatives;
a finite time mesh upgrades convergence to uniformity on each compact time
interval. Density extends that uniform statement to every slow state.
Thus leakage out of the encoded evolving sector vanishes in norm, not only
in compressed expectations. This is strong, not operator-norm convergence
uniform over all states, and no state-independent convergence rate follows.

The argument is a direct instance of the standard core-intertwining method;
see Teschl, Wang, Xie and Zhou, [On Generalized Strong and Norm Resolvent
Convergence](https://arxiv.org/html/2601.10476v1), Lemma 2.8, for primary
operator-theoretic context. Equations (13)-(17), including the stronger
uncompressed intertwining, are proved here for the present Gaussian encoding.

## 7. Limit order, observable locality, and the price paid

The proved limit is eta->0 at fixed delta, followed by delta->0 at fixed
lattice. Equations (7), (14), and (15) expose the constants for a quantitative
finite-state calculation. They do not license an arbitrary simultaneous
choice eta=delta or a volume-independent error bound. A diagonal sequence
can be selected for any countable dense set of core states and compact time
intervals; that existence statement is not an efficient universal algorithm.

The local Hamiltonian uses 35n pairs, including 28n added oscillator pairs.
Dense exact elimination of K is dimension 28n; its translation invariance
permits 28-by-28 Fourier blocks and O(n log n) Fourier transforms for classical
coefficient operations. This does not make the quantum Hilbert space finite
or provide a polynomial-cost interacting many-body simulation. The fast
frequencies are sqrt(lambda_j(K_delta)/eta); the energy subtracted in (10)
and the stiffness scales diverge in the relevant limits. The smallest
nonzero spatial eigenvalues also enter (7), so no bounded-cost continuum
parent has been demonstrated.

There is no conflict with the healthy Schur sign obstruction. Expansion of
the last square in (1) contains the positive bare contact
g^2||sigma||^2/(2 delta); elimination subtracts an ordinary negative Schur
term from this divergent contact. The net positive inverse-gradient kernel
arises only in a singular family, exactly outside the bounded-contact
uniform no-go hypotheses. Nor is E being called a Maxwell electric field:
E here is a canonical coordinate with its own momentum and is not constrained
by Gauss law. A fixed finite delta model has no new gauge symmetry.

At finite parameters the canonical scalar operations are local on the full
tensor-product space, but the low-fast-energy encoding J is not local:
f_delta contains R_delta. A scalar momentum shift on an encoded state does
not in general preserve its displaced auxiliary vacuum. Exactly,

    J* (-i partial_i) J = -i partial_i,
    J* (-partial_i^2/2) J = -partial_i^2/2
                +sqrt(eta) (partial_i f)^T K^(1/2)(partial_i f)/4.

The first compressed equality does not make the encoding a local algebra
homomorphism. Encoded scalar Weyl operations require the accompanying
spatially extended change in the auxiliary displacement. As delta->0 the
derived TT scalar response is precisely the already proved nonlocal response,
not its cancellation. Finite interaction range on an oscillator lattice does
not itself imply relativistic microcausality or a volume/energy-uniform
Lieb-Robinson bound, and no such bound is asserted.

Lastly the extra tensor free modes in (9) carry physical energy. Inserting
this enlarged model into the Round14 trace-clock square root would generally
change the clock readout. Tensor-factor independence is not permission to
erase their energy or declare them gauge. The construction solves a controlled
local dynamical representation problem, not the microscopic completion
selection, chiral content, gravity constraint algebra or full T1-T8 problem.

## Reproduction

`checker.py --ward-source /absolute/path/to/free_scalar_ward.py` runs exact
SymPy checks of the original scalar source, the actual staggered fiber
matrices, all 28 fast coordinates, the positive Hessian and minimizer,
the complete TT/zero-mode kernel limits, the sign-control mutation, and the
continuous Gaussian norm, residual and nonzero compression correction.
The finite checks support the explicit all-lattice algebra and analytic
proof; they do not numerically certify an infinite-dimensional limit.
