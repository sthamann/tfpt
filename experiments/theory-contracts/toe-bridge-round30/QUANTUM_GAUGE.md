# The signed wall with genuinely dynamical compact gauge fields

2026-09-07. NON-RH, unpromoted research. This proves an exact full-Hilbert-
space representation theorem for a declared extension of the signed-wall
family in v1027. It does **not** prove mirror decoupling or a chiral SM.

## 1. Precise input, including what has changed

Let a finite graph carry a compact connected Lie group G on each link,
with normalized Haar measure, and finitely many fermion modes at each
vertex. The kinematic Hilbert space is

    H = L^2(G^edges) tensor F(C^(2d)).                    (1)

There are d low-sector and d auxiliary/mirror fermion modes. Each compact
link retains every electric representation. This is the full rotor
realization, not a finite-dimensional noncommutative quantum-link
truncation. Such a truncation would need a separate theorem.

Let A(U) be a smooth Hermitian gauge-covariant multiplication matrix,
uniformly bounded by L, built from finite-range link transporters. Use
exactly the v1027 polynomial signed-wall family

    h(U) = [ A+beta A^2   eta A ],
           [ eta A       M I   ]
    M=Delta+lambda, beta=lambda g^2, eta=lambda g,
    Delta,lambda>0, g real.

Assume B0=L+beta L^2<M and cL<1, c=beta-eta^2/M>=0. The original
v1027 example Delta=3, lambda=1, g=1/2, L=2 satisfies both. Unlike that
fixed-background calculation, define the **new dynamical extension**

    H = (kappa/2) sum_(link,a) E_(link,a)^2
          + V_mag(U) + dGamma(h(U)), kappa>0,            (2)

with a bounded nonnegative magnetic multiplication potential. Gauge
couplings, fermion content and A are declared; they are not selected by
TFPT in this note. The additive DET-CAR choice of v1027, with its neutral
determinant premise, is retained if these fermions are DET-dressed ones;
the old flat Delta*Q Hamiltonian is not substituted for Delta*N_a.

In the group-element representation link-matrix entries are commuting
scalar multiplication functions, even for nonabelian G. Electric
generators do not commute with them. This distinction is explicit in
[Zohar and Burrello, Sections II and IV](https://arxiv.org/html/1409.3085v2).
The generic noncommuting operator-entry CAR counterexample in v1027
remains correct; it does not exclude this more specific multiplication
algebra. No claim about the chiral fermion measure follows from full-Fock
gauge covariance.

## 2. A global rotation without choosing eigenvectors of A

For real x in [-L,L] set

    D(x)=M-x-beta x^2 >0,
    R(x)=sqrt(D(x)^2+4 eta^2 x^2),
    C(x)=sqrt((R(x)+D(x))/(2R(x))),
    S(x)=2 eta x/sqrt(2R(x)(R(x)+D(x))).

These are smooth real analytic functions on a neighborhood of the
spectral interval. C^2+S^2=1, and S crosses zero continuously at x=0.
Define by finite-dimensional functional calculus

    V(A) = [ C(A)   S(A) ],
           [-S(A)   C(A) ]
    f_+/- (x) = [M+x+beta x^2 +/- R(x)]/2.

Direct multiplication gives

    V(A)^* h(A) V(A) = diag(f_-(A),f_+(A)).             (3)

This is global over all allowed gauge configurations: it never chooses
an individual eigenvector of A. Degeneracies of A and low-sector zeros
do not spoil it. The graph of the low d-dimensional band has the
everywhere invertible C(A) coordinate. There is no claim that its
filled-negative-energy subbundle or a Weyl determinant line is trivial.

The usual scalar signed-wall bounds still hold pointwise:

    f_+(x)>=M, f_-(x)<=B0<M, f_-(x)>=-L,
    sign f_-(x)=sign x, f_-(x)=x+c x^2+O(x^3).

For the lower bound observe
h=diag(A,Delta I)+lambda (gA,I)^*(gA,I)>=-L I.
The sign statement follows from det h(x)=M x(1+cx).
These are frozen-fiber band statements, not full quantum energy bands.

## 3. Full Fock lift and exact electric backreaction

Take the entire exterior algebra, not just its one-particle sector:

    Gamma(V)=direct sum_(n=0)^(2d) wedge^n V,
    (mathcal U Psi)(U)=Gamma(V(A(U))) Psi(U).            (4)

Each fiber is unitary; Haar integration makes mathcal U unitary on (1).
Its transformed creation/annihilation operators satisfy the complete
CAR. The coefficient functions commute with one another and with bare
fermions; no noncommutative-entry CAR shortcut is used. Gauge covariance
of A implies equivariance of V and Gamma(V), so mathcal U commutes with
the **combined** gauge action and preserves every Gauss sector.

For E_a=-i X_a, where X_a is a Haar-skew-adjoint invariant vector field,
define the Hermitian connection

    b_a=-i V^* X_a V,
    B_a=-i Gamma(V)^* X_a Gamma(V)=dGamma(b_a).

Differentiating (4), with all products in their displayed order, gives

    mathcal U^* E_a mathcal U=E_a+B_a,
    mathcal U^* H mathcal U
       = (kappa/2) sum_a (E_a+B_a)^2 + V_mag
                           +dGamma(diag(f_-(A),f_+(A))). (5)

The derivative of B_a and both cross terms belong to the square. The
connection is not an optional fitted correction. Dropping it changes
the electric energy. Its off-diagonal low/high components generally
create high-sector excitations, so (5) is not a free-band diagonalization
of the full quantum problem.

These statements hold first on C^infinity(G^edges) tensor F. The compact-
group electric Laplacian is self-adjoint on its Sobolev H^2 domain and
has compact resolvent; the finite-Fock potential in (2) is bounded.
Bounded perturbation therefore supplies a self-adjoint H on that same
domain. Smooth mathcal U and its inverse preserve H^2. Equation (5)
extends to the self-adjoint operators, not only formal derivatives.
The inherited compact Gauss projection commutes strongly with both;
their physical restrictions retain their ordinary positive norms.

## 4. What survives compression to the empty high sector

Let P be the constant Fock projection onto N_high=0 in the rotated
coordinates and Q=I-P. Since P commutes with the bare E_a, the exact
compressed electric operator is

    P(E_a+B_a)^2P
       = (E_a+P B_a P)^2 + P B_a Q B_a P.               (6)

The second term is nonnegative. With the high Fock vacuum it is

    P B_a Q B_a P=dGamma(b_(a,LH) b_(a,HL)) on F_low.  (7)

This follows directly from CAR: only creating one high fermion and
annihilating it again survives between the empty-high projections.
It is the matrix-valued version of the usual positive Born-Huang
correction; see [the distinction between complete and compressed
channels](https://arxiv.org/html/2608.08668v1#S2).
The derivation (6)-(7) is given here, not imported as a TFPT claim.

Compression is **not** exact elimination. P is generally not reducing
for (5). Replacing full evolution by PHP requires an error theorem;
Section 5a supplies one for the declared finite physical example only.
Even including the positive term in (6) does not make transitions vanish.

A limited but honest full quantum bound is available. For V_mag>=0,

    mathcal U^* H mathcal U +d L >= M N_high.           (8)

Hence any normalized state of expected original energy <=E obeys
<N_high> in its rotated state <=(E+dL)/M. When f_-(A)>=0, dL can be
replaced by zero. This bounds dressed high-sector population, not the
bare mirror response or a many-body gap. The dL cost is extensive; it
does not prove thermodynamic decoupling of a filled Dirac sea.

## 5. Exact quantum-rotor example, including Gauss's law

For a two-vertex link U=e^(i theta), z=U, use

    A(theta)=(1/2)[1 z^-1; z 1], A^2=A,
    Delta=19/12, lambda=g=1, kappa=1, V_mag=0.

These rational parameters are deliberately chosen for exact checks;
they are a different member of the v1027 family, not fitted physical
couplings. Here C=I-A/5, S=3A/5 and the four fiber eigenvalues are
0,5/4,31/12,10/3. All four fermion modes and all 16 Fock states are used.

In order (low_x,low_y,high_x,high_y), the connection at theta=0 is

    b(0)=(1/10)[ 1  0  0 -3;
                 0 -1  3  0;
                 0  3  1  0;
                -3  0  0 -1 ].

For every theta, b_LH b_HL=9I_2/100. Thus the correction to the
compressed Hamiltonian is **9 N_low/200**, including kappa/2=1/2.
The checker records the unweighted geometric term 9 N_low/100 separately.

With E=-i partial_theta and total occupations N_x,N_y, the generators

    G_x=E+N_x-q_x, G_y=-E+N_y-q_y

commute with H and mathcal U. The checker verifies the differential
identity as a Laurent-polynomial equality with an **arbitrary integer**
Fourier label k. There is no electric flux cutoff.

Two finite physical sectors are also exhausted. With external charges
(q_x,q_y)=(1,0), total fermion number is one and Gauss forces fluxes
[0,1,0,1] on four basis states. With (1,1), number is two and the six
states have forced fluxes [0,-1,0,0,1,0]. These are exact constrained
sectors, not a replacement for the full rotor space. They do not describe
an empty-boundary sector with charged particles silently added.

On these sectors the squared Hilbert-Schmidt error made by leaving the
electric energy unrotated is respectively **1/10** and **9/50**. Thus
the omitted connection changes a gauge-invariant physical Hamiltonian,
not only an unphysical coordinate expression. In the one-fermion sector
the characteristic polynomials differ by exactly 31/256; their fourth
spectral moments differ by -31/64. In the two-fermion sector the fourth
moment difference is 1395/32. This excludes merely having written an
isospectral operator in another basis.

## 5a. Controlled elimination in the actual one-fermion Gauss sector

Allow 0<kappa<=1/2, leaving A,Delta,lambda,g unchanged. The exact
one-fermion Gauss Hamiltonian has, after the same rotation, blocks

    L=[5/8+kappa/20, 5/8; 5/8, 5/8+9kappa/20],
    D=[71/24+kappa/20, 3/8; 3/8, 71/24+9kappa/20],
    C=H_HL, C^*C=(9kappa^2/400)I.

Here D>=M I, M=31/12, and 0<=L<=(3/2)I. For real z<=3/2 the
Feshbach self-energy is an exact positive matrix with a uniform bound

    Sigma(z)=C^*(D-z)^(-1)C,
    0<=Sigma(z)<=9kappa^2/[400(M-z)] I
                  <=epsilon I, epsilon=27kappa^2/1300. (11)

Let l_1<=l_2 be the two eigenvalues of L and E_1<=E_2 the two lowest
eigenvalues of the complete four-dimensional physical Hamiltonian. Minmax
gives E_i<=l_i<=3/2. The other two eigenvalues are >=M by principal-block
interlacing. Schur congruence at z<M identifies the number of eigenvalues
below z with the negative index of L-z-Sigma(z). Bound (11), or the
ordered eigenvalues of that Schur matrix, consequently gives

    l_i-epsilon <= E_i <= l_i, i=1,2.                  (12)

The lower endpoints may be replaced by zero if needed. This controls the
effect of the **actual** interband transitions, not only the kinematic
band rotation. At the declared kappa=1/100,

    epsilon=27/13000000 <2.1*10^-6

in this model's energy units. Exact rational Sturm intervals for all
four full roots and both compressed roots independently verify (12).
It is an absolute energy bound, not a percent accuracy on an observed
neutrino mass or a volume-independent mirror-decoupling theorem.

There is also an all-time finite-sector norm estimate. For the natural
low-sector inclusion J, HJ-JL has norm ||C||=3kappa/20. Duhamel gives

    ||exp(-itH)J-J exp(-itL)||<=3kappa |t|/20.          (13)

At kappa=1/100 this is 0.0015 |t|. There is no claim that this growing
bound stays small for arbitrarily long times. Gauss's law, not an
electric truncation, makes this particular physical sector finite.
For the general signed finite-graph problem the high-block threshold
from (8) is only M-dL; an extensive or vanishing threshold does not
support the same elimination estimate. That is a remaining T4 issue.

## 6. Local dynamics and a shared source functional: exact scope

If A is built from bounded finite-range graph hoppings, A^2 only doubles
that range. Original (2), before changing representation, consists of
onsite electric Laplacians and bounded finite-range interactions Phi_Z.
On a bounded-degree lattice with fixed couplings let

    K_mu=sup_x sum_(Z contains x) |Z| ||Phi_Z|| exp(mu diam Z)<infinity.

Pass to the interaction picture of the onsite electric sum. Its unitaries
preserve support and the norm of each bounded Phi_Z. Iterating the
commutator integral then gives, for disjoint bounded **fermion-even**
local observables A_X,B_Y,

    ||[tau_t(A_X),B_Y]||
       <=2||A_X||||B_Y|| |X| exp(-mu dist(X,Y))
                              [exp(2 K_mu |t|)-1].      (9)

One way to see the coefficient is to sum ordered overlapping interaction
paths: their weighted step sum is <=K_mu, their n-fold time simplex is
|t|^n/n!, and each commutator supplies at most a factor two. Triangle
inequality for graph distances supplies exp(-mu dist). This also makes
finite-volume dynamics norm-Cauchy on each fixed local observable at
fixed time as the boundary recedes. The unbounded onsite evolution is
strongly continuous in Hilbert space; (9) does not assert point-norm
continuity on every element of B(L^2(G)) or a continuum velocity bound.
No analogous uniform estimate for the rotated band observables is assumed.

At fixed graph H has a finite heat trace for beta>0. Given beta and
bounded time-dependent sources, the bounded-perturbation Dyson series
defines U_J(t) on this very Hilbert space and

    rho_beta=exp(-beta H)/Tr exp(-beta H),
    Z[J_+,J_-]=Tr(U_(J_+) rho_beta U_(J_-)^*).           (10)

For equal sources Z[J,J]=1. Conjugating H, rho, observables and sources
by the **same** mathcal U leaves (10) unchanged. Transforming only h(U)
does not. Here mathcal U is fixed from the baseline model for all source
histories; a time-dependent re-diagonalization would additionally require
its -i mathcal U^* partial_t mathcal U term.
This is a finite-regulator source-functional construction with
specified beta, not a selection of the cosmological rho_0 of T8.

The missing T4 demands remain substantial: a genuinely chiral content,
local gauge-invariant Weyl measure, uniform interacting mirror decoupling
and index/anomaly control. The current A demonstration is not a Weyl
fermion construction. T5 still needs a nontrivial 3+1D continuum, Lorentz
restoration, confinement and scattering. No source Hessian here has been
identified as the physical spin-two sector of T7. The graph dimension,
field content and couplings have not been derived from T1-T2.
