# Exact full-reference budgets and a nonzero memory truncation

2026-09-07. NON-RH. This is an executable bound planner for the analytic
statement in [full-reference control](../full-reference-control-round27/PROOF.md).
It does NOT execute the complete interacting partition sum.

## Rational certification

The implementation uses only integers and fractions for certificates:

    exp(theta) <= 3^ceil(theta),
    exp(-d) <= 2^-floor(d),
    Theta(s) <= [1+2 ceil sqrt(1/(s a_c))]^(8N),
    Theta(s)^(1/T) <= ceil_integer_Tth_root(Theta_upper(s)),
    exp(B)-1 <= B/(1-B),  0<=B<1.

The last inequality follows term by term from 1/k!<=1. Integer-root
rounding is upwards. The planner searches the smallest nonnegative K
and P passing these particular monotone conservative tail predicates;
it does not claim that physically necessary cutoffs are minimal.
The admissibility P+2>theta is checked before evaluating the geometric
tail. Charge and hopping receive half the budget remaining after the
supplied certified memory error. Gaussian/transcendental evaluation
roundoff, if a partition sum were later executed, requires its own budget.

## Like-for-like original comparison case

At N=27,T=3,beta=1,J=1/10, theta=648/5, tolerance=1/100, full memory:

    Round26 published planner: K=4096, P=962.
    Round27 exact-bound planner: K=2670, P=354.

Both bound omission error only; neither computes Z. Round26 used doubling
for K and steps of 64 for P, while Round27 refines to the first admissible
integer. The checker additionally compares the OLD inequalities at their
own first passing integers K=4035,P=956, separating proof improvement from
search-grid improvement. The old rational Theta(beta) envelope is 83^216 (415 digits)
and is entirely absent from the new sign/memory and hopping estimates.
This refers to the certified envelope, not a measured physical entropy.

For the deliberately naive candidate enumeration envelope

    (2K+1)^(8N) sum_(k<=P) (48N)^k binomial(T+k-1,k),

the conservative decimal-digit upper bound drops from 3846 to 1912.
That is still prohibitively large. These are upper counts of a naive
scheme, neither a runtime measurement nor a necessary complexity lower
bound. Faster regroupings are not excluded by these counts.

## Genuine finite-memory witness on the original lattice

Take L=9,N=729, cells ell=3, a=1,m^2=1, arbitrary u,nu>=0, g=0.
There are 27 disconnected scalar interiors of 8 sites, with 513 retained
sites and 216 eliminated sites, exactly the geometry of Round25.
Choose T=33, delta=3/4, beta=99/4 and J=1/866052, so theta=1.
This is a declared weak-total-hopping example, not an all-J practical
solver and not a fitted physical coupling.

The cell Dirichlet gap is b=m^2+12 sin^2(pi/6)=4. Hence q_b=1/4 solves
q_b+q_b^-1=2+delta^2 b exactly. Use c=6 and the Round25 cyclic tail

    tau_R=delta q_b^(R+1)/[sinh(alpha_b)(1-q_b)(1-q_b^T)],
    epsilon_R=delta^2 c^2 tau_R, eta_R=epsilon_R/(delta m^2).

For the retained temporal inverse trace, q_0=1/2 corresponds to a lower
mass squared 8/9<=1, so its explicit diagonal Green function is an upper
bound on g_m(0). This comparison is rigorous, not a floating approximation
to the irrational exact q_m. Retain the FULL fast determinant unchanged.

For R=12<floor(T/2)=16 the exact rational certificate gives

    rho_memory <= 0.002045 < 1/300,
    eta_R<1, B_R<1.

The displayed decimal is rounded upwards; the executable comparisons use
fractions. The quadratic memory retains 2R+1=25 of 33 cyclic time offsets
and discards 8. Thus this is a nonzero memory truncation that survives
the complete signed history sum. It is not merely a positive conditional
kernel. R=11 fails the chosen 1/300 memory subbudget using this bound;
that is not a physical impossibility statement about R=11.

For the same parameters the combined planner supplies K=12235,P=5
and verifies rho_charge+rho_hops+rho_memory<1/100. Those K and P apply
to sampled boundary charges and TOTAL word order respectively. The
candidate-envelope digit upper bound is 25624: the charge enumeration
remains far beyond an executed calculation even though the memory and
word budgets are small.

The complete fast determinant is still a full-history function. Reducing
the quadratic memory does not make the full statistical weight Markovian
or remove all temporal dependence. No approximate positive transfer,
efficient sign sampler, continuum or real-time theorem follows.

## Cost and verification

The executable integer search is a certificate calculator, not the
solver being bounded. Per-history Gaussian evaluation still uses the
Round25 block solver (fixed cell size: O(T d^3) arithmetic, O(T d^2)
storage); bit complexity, stability and the number of histories remain
separate. Exact checks of root ceilings, minimum predicates, factorial
tails, comparison inequalities, source pins and false-execution flags
are run again with optimization enabled. No mathematical claim is
established solely by test counts. All previous round files are immutable.
