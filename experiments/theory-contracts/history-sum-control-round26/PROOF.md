# Round26: an absolutely convergent summed history with certified finite tails

2026-09-07. NON-RH. Fix a finite periodic spatial lattice L>=3, N=L^3,
a,m>0, u,nu>=0, J>=0, delta>0, integer T>=3, beta=T delta. Work in the
NEUTRAL total-charge sector of the original g=0 scalar/charge model.
Every local charge is still an arbitrary element of Z^8. Other free
species factor unchanged. This is the specified Euclidean time regulator,
not the exact unsliced heat operator or a real-time reconstruction.

## 1. Specify the positive transfer operator, including its normalization

Let K_phi=sum pi_x^2/2, A(n)=-Delta_a+m^2+2u diag(e(n_x)), and

    V(n,phi)=D(n)+phi^T A(n)phi/2,
    D(n)=sum_x e(n_x)/N+nu sum_edges e(n_x-n_y),
    A_sign=sum_(directed edge/channel hops) W_e,
    r=48N, kappa=rJ, H_hop=kappa I-J A_sign.

The r terms are the original monomial unitaries with cocycle signs, with
both directions present. No hopping constant is subtracted. Define

    Q_delta=exp(-delta V/2)
               [exp(-delta K_phi) tensor exp(-delta H_hop)]
             exp(-delta V/2),
    Z_T=Tr_neutral Q_delta^T.                       (1)

The middle factors act on different tensor factors and commute. Thus
Q_delta is positive. It is trace class: 0<=exp(-delta H_hop)<=I bounds it
above by its charge-diagonal Gaussian counterpart, whose trace is finite
by the positive scalar mass and coercive charge energy. Traces and
compression inequalities below therefore apply to actual operators.

Resolving the charges between transfers and integrating all scalar
coordinates gives exactly the Round24/25 matrix
delta^-1 L_time tensor I+delta blockdiag A(n(j)), with the ordinary
free-particle Gaussian normalization. Denote the positive scalar factor
for a history by Z_phi[n], and its zero-charge value by Z_phi,0>0.
The nonnegative added scalar potential gives 0<Z_phi[n]<=Z_phi,0 directly
in the finite Gaussian integral. Define Theta(s)=Tr_neutral exp(-sD).

The actual Gram matrix has ||G^-1||_infinity=31, hence

    D(n)>=a_c ||n||_2^2, a_c=1/(62N),
    Theta(s)<=(1+sqrt(pi/(s a_c)))^(8N)=:Theta_bound(s). (2)

Use ||G^-1||_2<=||G^-1||_infinity for the first estimate and the decreasing
Gaussian integral bound on each integer coordinate for the second.
Dropping neutrality and the nonnegative nu term only enlarges this bound.

## 2. Absolute convergence and a nonzero denominator despite cancellations

Replace each signed hop by its unsigned translation ONLY to construct
a comparison operator A_+. It has r unit-weight outgoing and incoming
steps. U_delta=exp(-delta kappa) exp(delta J A_+) has nonnegative entries,
row/column sum one and operator norm one. Expanding the exponentials in
words gives entrywise |exp(-delta H_hop)_(n',n)|<=U_delta(n',n).

For closed histories, the absolute sum (even with individual hop words
resolved) is therefore at most

    Z_abs,T <= Z_phi,0 Theta(beta).                 (3)

To justify the charge trace bound, apply Schatten Holder to products of
exp(-s_j D) and norm-one unsigned shifts, with sum s_j=beta. The heat
factors have norms ||exp(-s_j D)||_(beta/s_j)
=Theta(beta)^(s_j/beta). Summing words contributes exp(beta kappa),
which cancels the retained exp(-beta kappa). The positive comparison
allows Tonelli; (3) then gives absolute convergence of the signed sum.
This includes all integer charge configurations and all word lengths.

For a LOWER bound, compress Q_delta to the all-zero charge vector Omega.
Since <Omega|A_sign|Omega>=0, scalar spectral Jensen gives
<Omega|exp(delta J A_sign)|Omega>>=1. The compression is therefore at
least exp(-delta kappa) times the free scalar transfer Q_phi,0.
Schatten-T compression monotonicity gives

    Z_T>=exp(-beta kappa) Z_phi,0>0,
    Z_abs,T/Z_T<=exp(beta kappa) Theta(beta)=:C_sign. (4)

This is a finite, generally enormous cancellation budget, not absence
of a sign problem or a useful volume-uniform average sign. It does not
need small J. The zero-charge compression is a variational comparison,
not a projection used to define the interacting dynamics. Nonneutral
sectors need a different lower reference and are not asserted in (4).

## 3. Improve the conditional scalar normalization bound before summing

For the retained scalar kernel, positivity of the full spatial stiffness
and minimization over fast variables give the STRONGER lower bound

    K>= (delta^-1 L_time+delta m^2 I_T) tensor I_S.   (5)

The temporal form has no retained/fast cross term. Its fast contribution
is nonnegative during the minimization, which proves (5). Consequently

    Tr K^-1 <= |S| T g_m(0),
    g_m(0)=delta/(2sinh(alpha_m))*(1+q_m^T)/(1-q_m^T),
    cosh(alpha_m)=1+delta^2 m^2/2, q_m=exp(-alpha_m).

Let epsilon=||K_R-K|| be bounded as in Round25 and eta=epsilon/(delta m^2)<1.
For X=K^-1/2(K_R-K)K^-1/2, ||X||_1<=epsilon Tr K^-1. Since
|log(1+x)|<=|x|/(1-eta) for |x|<=eta, the conditional scalar factors obey

    |log(Z_phi,R[n]/Z_phi[n])| <=
      B_R=epsilon |S| T g_m(0)/(2(1-eta)),
    |Z_phi,R[n]/Z_phi[n]-1|<=a_R=exp(B_R)-1.         (6)

The exact eliminated determinant stays in both factors. This trace bound
avoids a spurious linear divergence in T from counting all temporal modes
with the same worst coercivity constant. At fixed beta and epsilon=delta e,
the prefactor delta T g_m(0) tends to beta coth(beta m/2)/(2m).
The bound remains extensive in |S|. It is not a uniform thermodynamic bound.

Combining (3),(4),(6) gives an ACTUAL SUMMED partition estimate

    |Z_T,R/Z_T-1|<=a_R C_sign.                      (7)

If rho=a_R C_sign<1, the approximate summed partition stays positive.
For a bounded self-adjoint charge observable O(n) inserted at one time,
||O||<=1, the normalized expectation difference is at most

    2 rho/(1-rho).                                 (8)

The exact expectation is bounded by one because Q_delta^T is positive;
the numerator error is bounded by the same absolute sum. Equation (8)
is NOT asserted for arbitrary signed multi-time functions or scalar
observables whose Gaussian insertion has not been controlled. No
reflection positivity or Hamiltonian for K_R is inferred.

## 4. Finite charge and hop-order tails, without a truncated Hamiltonian

Discard histories with any sampled charge profile ||n(j)||_infinity>K.
With a union over T slices, splitting off half of that slice's heat
factor and using Holder on the rest bounds the omitted absolute weight by

    E_charge <= Z_phi,0 T exp[-delta a_c(K+1)^2/2]
                             Theta(beta-delta/2).   (9)

The split-off factor has norm at most the displayed exponential. The
remaining heat times sum to beta-delta/2; unsigned hop norms and the
retained hopping constant cancel as before. This bound deteriorates under
time refinement at fixed K; no uniform fixed-charge-box limit is claimed.

Resolve exp(delta J A_sign) in words at each slice, and omit histories
whose TOTAL number of elementary hops exceeds P. With theta=beta kappa,

    E_hops <= Z_phi,0 Theta(beta) p_P(theta),
    p_P(theta)=exp(-theta) sum_(r>P) theta^r/r!.

For P+2>theta the geometric majorant gives

    p_P(theta)<=exp(-theta) theta^(P+1)/(P+1)!
                                      /(1-theta/(P+2)). (10)

The total order, multinomial allocation to slices and the factor exp(-theta)
must all be retained. This is a convergent all-J expansion at fixed N,beta,
not a small-J perturbative assertion. The corresponding RELATIVE hop bound
after (4) is Theta(beta) times the right side without exp(-theta).

Let the finite word/charge sum also use the controlled scalar memory
approximation if desired. A combined certified relative error is

    rho <= exp(theta)[T exp(-delta a_c(K+1)^2/2)
                        Theta(beta-delta/2)+a_R Theta(beta)]
           +Theta(beta) theta^(P+1)/(P+1)!/(1-theta/(P+2)). (11)

Full memory makes a_R=0. Then finite K and P can reach any prescribed
error at fixed regulator. For nonzero memory removal, (11) may certify
nothing useful because C_sign is large; that is reported, not hidden.
The finite sum is an approximation to the unbounded theory with a proved
tail, NOT a replacement of its Hamiltonian by a finite charge register.

## 5. Constructive algorithm and explicit limitations

Enumerate starting charge profiles in [-K,K]^(8N), elementary words up
to total length P, and their allocations among T slices. Require total
neutrality, closure and the charge box at the sampled slice boundaries.
Do NOT reject intermediate charges inside an exponential word merely
because they leave that box: only the sampled-boundary tail was proved.
Intermediate word coordinates may reach K+P. Each accepted scalar history
is a positive finite Gaussian integral, computable by the Round25 solver
and a retained scalar solve; all original phases multiply its weight.

A naive candidate-count envelope is

    (2K+1)^(8N) sum_(r=0)^P (48N)^r binomial(T+r-1,r). (12)

This is not efficient in N,P,K. Exact algebraic determinants and bounded
transcendental evaluation need their own precision costs. The implemented
rational planner certifies (9),(10) using pi<4, e<3 and e>2; it reports
cutoffs and a work envelope, NOT an executed full partition sum. Physical
word and scalar-kernel regressions are separate from this global bound.

Thus absolute convergence, a positive denominator and certified finite
summation errors are established for the declared finite neutral Euclidean
regulator. Efficient cancellation control, a volume-uniform interacting
limit, real-time reconstruction, full g!=0 gravity and observed chiral
matter remain open. No T1-T8/TOE/RH or empirical promotion.
