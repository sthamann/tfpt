# Round18: exact source dilation, its unavoidable noise, and auxiliary limits

2026-09-06. NON-RH, unpromoted finite-lattice research. This examines an
EXACT auxiliary replacement of the Round17 source-square completion. It
constructs a positive isometric commuting-readout dilation of the actual
quadratic sources, and computes why its energy is not the original energy.
It excludes two precisely specified shortcuts, not all local quantum parents.

## 1. Actual source and a normalized state witness

Keep the actual Ward source and the Round17 conventions, including all
scalar sites, the trace subtraction, ordering and noncommuting currents.
On the L=2 lattice, spacing one, mass squared two, take the normalized real
mode (-1)^(x1+x2)/sqrt(8). With symmetric tensor coordinates ordered
(11,22,33,23,13,12), set

    s=(4,4,8,0,0,4sqrt(2)), ell=8,
    Bv=[[5,-3,0],[-3,5,0],[0,0,8]]/32,
    Q0=OpW(s.tau/(s.s)+rho/16),
    (Q1,Q2,Q3)=OpW(Bv current).

The current convention here incorporates Jv=-current, hence agrees with
Q=(Bcal,-Bv Jv). Q3 happens to vanish in this fiber and is retained as zero.
These real Weyl quadratics have their self-adjoint metaplectic closures.
Schwartz space is a common invariant expression core for every product
used below; no finite-dimensional CCR model is substituted.

Let z=(phi,pi) in R^16, Omega=[[0,I],[-I,0]], and q_a(z) their classical
quadratic symbols. Quadratic Weyl calculus is exact at the commutator level:

    [Qa,Qb]=i OpW({q_a,q_b}).                            (1)

For the normalized eight-coordinate Gaussian centered at phi_000=t,
all other fields and all momenta zero, with covariance I_16/2, the checker
computes directly from the imported Ward source

    <[Q0,Q1]>/i = -(t^2+10)/1024.                       (2)

The polynomial bracket contains -phi_000^2/1024 and its centered Gaussian
expectation is -5/512. Equation (2), not merely a nonzero formal bracket,
provides an explicit normalized scalar-sector Hilbert vector for every real t.
Other scalar/TT/fast factors can be tensored with normalized domain vectors.
No membership in an additional homogeneous projected sector is inferred.

## 2. A quantitative obstruction to noiseless commuting registers

Let J:H->K be any isometry, P=JJ*, and Ra mutually strongly commuting
self-adjoint auxiliary readouts. Assume on the target common Schwartz core

    J psi in intersection Dom Ra,    J* Ra J psi=Qa psi. (3)

Only these first-moment identities are assumed. Define leakage vectors and
their nonnegative quadratic forms by

    La psi=(I-P)Ra J psi,
    n_a[psi]=||La psi||^2
            =||Ra J psi||^2-||Qa psi||^2.               (4)

The last equality is orthogonal decomposition, not a formal subtraction of
unbounded operators. Strong commutation implies that the joint spectral
integral <Ra Jpsi,Rb Jpsi> is real: its integrand is r_a r_b times a positive
measure and is integrable by Cauchy--Schwarz. Decomposing with P gives

    <psi,[Qa,Qb]psi>
       = -<La psi,Lb psi>+<Lb psi,La psi>.

Therefore

    |<[Qa,Qb]>| <= 2 sqrt(n_a n_b) <= n_a+n_b.           (5)

In particular, exact source intertwining Ra J=J Qa for all a is impossible
for the actual source: it would force both n0 and n1 to vanish, contradicting
(2). More generally preserving all first moments AND the total squared-source
energy sum ||Ra Jpsi||^2=sum ||Qa psi||^2 for every core state is impossible,
because the sum of the nonnegative n_a would vanish.

For any fixed nonzero Round17 fiber weight w=|g||c|, (2)--(5) imply

    w^2 sum_a n_a[psi_t] >= w^2 (t^2+10)/1024.           (6)

Thus the excess cannot be repaired by one finite state-independent energy
subtraction. The bound is about exact first-moment matching; approximate
or biased readouts require separate error terms and are not ruled out.

This elementary dilation argument belongs to the setting of joint-measurement
noise, for context see [Ozawa, 2003](https://arxiv.org/html/quant-ph/0310070v1).
Equations (3)--(6) are proved here under their explicit unbiased-compression
hypotheses, not quoted as a universal measurement-error inequality.

## 3. A constructive commuting dilation with the exact extra term

For d scalar canonical pairs define normalized coherent states

    chi_(q,p)(x)=pi^(-d/4) exp(-|x-q|^2/2+i p.(x-q/2)),
    (J psi)(z)=(2pi)^(-d/2)<chi_z,psi>.

Plancherel integration over p followed by Gaussian integration over q gives
J*J=I. Thus K=L2(R^(2d),dz) has an ordinary positive norm. It is an enlarged
readout Hilbert space; J is not onto K. For real polynomial f, multiplication
M_f has its maximal self-adjoint domain and all such multipliers strongly
commute. The coherent resolution gives

    J* M_exp(i t.z) J=exp(-|t|^2/4) exp(i t.Z),
    J* M_f J=OpW(exp(Delta_z/4) f)                       (7)

on Schwartz tests. The first identity follows by completing the Gaussian
square in the coherent kernel; differentiating in t proves the second for
polynomials. All moments in question are finite on Schwartz vectors.
This is the coherent-state/anti-Wick relation; see also
[Amour--Nourrigat, 2018](https://arxiv.org/abs/1806.04898).

For q_a(z)=z^T H_a z/2 with real symmetric H_a, choose

    f_a=q_a-Tr(H_a)/4,       Ra=M_(f_a).

Equation (7) proves exact first-moment matching J*RaJ=Qa for every source,
without replacing the noncommuting target Qa by commuting target operators.
The commuting READOUTS live on K and the target range is not invariant.

Since the heat series truncates at order two on a quartic polynomial,

    exp(Delta/4) f_a^2
        =q_a^2+|H_a z|^2/2+Tr(H_a^2)/8,
    symbol_W(Qa^2)=q_a^2+Tr((Omega H_a)^2)/8.

Consequently the exact excess form in (4) is represented on Schwartz by

    N_a=OpW(|H_a z|^2/2)
             +[Tr(H_a^2)-Tr((Omega H_a)^2)] I/8.        (8)

Its first term is a sum of squares of real linear canonical operators,
and its constant is nonnegative: the Frobenius bound gives
|Tr((Omega H_a)^2)|<=Tr(H_a^2). This also verifies positivity independently
of (4). A nonzero H_a produces a nonconstant quadratic excess. There is
no claim that a universal constant removes the defect or that compression
of exp(-it sum Ra^2) equals exp(-it sum Qa^2).

This construction is a complete finite-regulator answer for simultaneous
first-moment source readouts with positive norm. It is NOT a Hamiltonian
dilation of the unchanged source-square dynamics. It supplies an explicit
alternative if the extra second-order interaction sum N_a is accepted as
new physical input. Neither locality of the multipliers' labels nor the
positive norm establishes native 3+1D observable locality.

## 4. Why two simpler auxiliary proposals fail in their stated classes

### Positive Gaussian static elimination

For real classical source j and ordinary auxiliary coordinates a, let

    W(j,a)=j^T C j/2+a^T K a/2+a^T L j,       K>0.

The exact minimum is attained at a=-K^-1 L j and equals

    min_a W=j^T(C-L^T K^-1 L)j/2.                       (9)

With C=0 the induced contribution is negative semidefinite, not the
positive source square needed for stabilization. If W itself is a positive
quadratic form, its Schur complement must be nonnegative; the required bare
contact C is then already part of the parent. The Round15 local positive
base explicitly has such a bare source contact and is NOT excluded by (9).
This is not a no-go for nonlinear fields, constraints, derivative couplings
or quantum energy contributions. A Euclidean imaginary-field integral is
not silently interpreted as a real positive Hamiltonian in (9).

### Undressed source-copy constraints

For auxiliary commuting coordinates y_a, the tentative constraints
T_a=y_a-Qa have

    [T_a,T_b]=[Qa,Qb] != 0.                              (10)

They are not a commuting first-class family merely because y_a commute.
The weaker compression allowance is precisely the noisy case (3)--(8).
Genuine conversion can add connection or nonlinear corrections, as in
[Batalin--Lavrov, 2015/2016](https://arxiv.org/abs/1505.03601), but those
corrections and their locality/domain properties must actually be built.
The existing nonlocal gravity dressing is not a free local replacement.

## 5. What this changes in the search

An exact source-register localization of the old global completion cannot
simultaneously keep commuting registers, every source, squared energy and
the positive isometric encoding with no leakage. Keeping noncommuting LOCAL
sources and changing the higher-order completion, as in the companion
[block stability construction](../local-source-stability-round18/PROOF.md),
does not make those assumptions and is not excluded.

The new preconditioned local-field parent is likewise a different off-shell
completion, not a counterexample to this exact-dilation bound. The abelian
charge fluxes of Round17 already commute, so its rotor energy construction
also does not contradict this result. No full-TFPT no-go, microscopic
selection, chirality, continuum, T1--T8 or RH claim follows.

The checker evaluates the actual source bracket on normalized coherent
states, the exact anti-Wick excess for all retained sources, and separately
labelled finite matrix/completing-square controls. It does not turn finite
algebra into certification of arbitrary unbounded-operator statements.
