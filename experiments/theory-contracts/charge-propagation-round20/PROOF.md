# Round20: bounded charge flow and finite-volume propagation certificates

2026-09-07. NON-RH. The model and local cocycle shifts are precisely those
of [the transport parent](../local-charge-transport-round20/PROOF.md) and
[the coupled domain theorem](../hopping-source-domain-round20/PROOF.md).
No finite rotor cutoff, Fock-particle identification or relativistic
Lieb--Robinson conclusion is used. Unless stated otherwise, t is generated
by X, not by the nonlinear square-root clock Hamiltonian.

## 1. Local and regional continuity are genuine operator statements

Let U_xy,p=T_y,p T_x,p* move p from x to y and let
L_J=J sum_(xy,p)(2-U-U*). The diagonal part X_d commutes strongly with
all charge coordinates. On finite charge support,

    [n_x^a,U_xy,p]=-p^a U_xy,p,
    I_xy^a=iJ sum_p p^a(U_xy,p-U_xy,p*),
    d n_x^a/dt=sum_(y->x) I_yx^a-sum_(x->y) I_xy^a.       (1)

With the eight coordinate generators p=e_b, only p=e_a contributes to
I^a on each edge. Thus ||I_xy^a||<=2J, independently of occupation, scalar
state, mass profile or the coupling lambda. Current is bounded although
n_x, e(n_x), and the scalar Hamiltonian are not.

For a set S of sites write Q_S^a=sum_(x in S)n_x^a. Internal edges cancel
exactly, including periodic multiplicities; let |boundary S| count actual
positive-edge occurrences crossing the cut. Then

    ||i[X,Q_S^a]||<=2J |boundary S|,
    ||exp(itX)Q_S^a exp(-itX)-Q_S^a||
                  <=2J |boundary S| |t|.                 (2)

The difference in (2) is the bounded extension of the difference of
unbounded operators on Dom Q_S^a. Here is the domain argument: X_d
strongly commutes with Q_S^a, and in its interaction picture the bounded
hopping has the same bounded Q_S commutator. Its Dyson series preserves
Dom Q_S in graph norm on compact times. Differentiation and integration
give (2), first on the graph core and then by closure. For S equal to the
whole lattice the boundary is empty; exp(itX) commutes with every spectral
projection of the eight total charges. This is stronger than a vanishing
formal expectation on a few test vectors.

## 2. All-order charge-configuration selection and an explicit tail

Let P_n denote the projection onto a charge configuration n, with the
entire continuous scalar/gravity space left untouched. Define d(n,m) as
the minimum number of allowed neutral nearest-neighbor coordinate transfers
taking n to m; put d=infinity when the total charges differ. This is an
integer-flow distance, not the Euclidean distance between arbitrary
quantum states. Every hop changes one component by -1,+1 at its endpoints.

Separate L_J=2JM I+K, M=24N, K=-J sum(U+U*), so ||K||<=2JM.
Only for estimating amplitudes, factor the harmless phase of 2JM. The
physical energy origin remains unchanged. In the X_d interaction picture
every K(t) still moves charge by precisely one allowed transfer, since
X_d is block diagonal in charge. Therefore for k<d(n,m),

    P_m K(t_k)...K(t_1)P_n=0.                            (3)

The norm-convergent Dyson series proves

    ||P_m exp(-itX)P_n||
       <=min(1, sum_(k>=d) a^k/k!)
       <=min(1, exp(a) a^d/d!),  a=2JM|t|,               (4)

when d is finite, and the amplitude is exactly zero for differing totals.
For the second inequality use (d+j)!>=d! j! and sum over j. It also holds
for a target set at distance at least d, with its joint orthogonal projection:
the bound is on the whole operator product, not a sum of uncontrolled
individual final-state probabilities.

For a unit charge displaced through graph distance r with other charges
unchanged, d=r: at least r signed edge transfers are needed, and a shortest
path realizes them. With a fixed species p, the projective phases telescope
along a path, U_yz,p U_xy,p=U_xz,p, so this elementary upper construction is
not lost to an invented commuting-shift approximation.

The constant a grows with N. Equation (4) is a rigorous FINITE-VOLUME
transition bound, not a uniform light cone. Equation (2) is a boundary-rate
bound on charge transfer, not an information-speed bound for all observables.
The full base B has unbounded intersite continuous-field interactions;
results covering unbounded ON-SITE terms and bounded interactions do not
automatically apply to it. See the precise scope of
[Nachtergaele--Sims](https://arxiv.org/abs/1410.8174).

## 3. A nonzero neighboring transport probability, with L=2 handled

Take n with one basis charge p at x and zero elsewhere, and m with that
charge at a neighboring y. The inherited cocycle gives

    <m|U_xy,p|n>=1.

For L>=3 exactly one positive-edge term or its adjoint produces this
neighboring transition. The full X matrix element is -J times the identity
on continuous fields. For a normalized continuous Schwartz vector psi,

    ||P_m exp(-itX)(|n> tensor psi)||^2=J^2 t^2+o(t^2).   (5)

The strong first-order expansion is valid because this vector is in Dom X;
its projection onto m kills the zeroth-order term and the entire diagonal
generator. Other channels are distinct final charge configurations.

At L=2 the positive-axis periodic-edge inventory has two reversed edges
between each such neighboring pair. Their relevant transfer operators are
identical, not independent probabilities. Their amplitudes add to -2J,
and (5) becomes 4J^2t^2+o(t^2). Generally the coefficient is the squared
modulus of the SUM of coinciding directed-channel amplitudes. An experiment
that declares a simple undirected graph instead would be a different
Hamiltonian normalization; it must not silently replace the periodic one.

The zero charge PROFILE is no longer a stationary basis state: hopping
also creates adjacent (-p,+p) configurations of total zero. This is a
neutral dipole process on the integer rotor carrier, not yet a particle/
antiparticle Fock construction. Exact total-charge conservation does not
mean every local charge occupation is conserved.

## 4. Synchronization is incompatible with this transport

In the old exact synchronized subspace every site has the same n. A local
transfer leaves that subspace; its compressed hopping is only 2JM times
identity, and compression does not define an invariant dynamical restriction.
Moreover two different uniform profiles have total charges Nn and Nm.
All neutral transport conserves total charge, so NO perturbative order or
virtual neutral hopping can produce a uniform n->m transition for n!=m.
The new local theory necessarily has many site configurations, not the old
single global module with a secretly local charged operator.

## 5. The square-root clock has a different, but bounded, charge response

The coupled clock uses K=sqrt(12X), not X. A positive lower bound X>=gamma>0
and the bounded commutator C=[X,Q_S^a] give the resolvent identity

    [sqrt(X),Q_S^a]=(1/pi) integral_0^infinity
               t^(1/2)(X+t)^(-1) C (X+t)^(-1) dt.

The operator-norm integral converges, since
integral_0^infinity t^(1/2)/(gamma+t)^2 dt=pi/(2sqrt(gamma)).
Prove the identity first with bounded spectral/resolvent regularizations
on the common charge graph core and pass by this integrable bound; the
bounded commutator criterion then preserves Dom Q_S under the clock group.
Consequently

    ||[K,Q_S^a]|| <=sqrt(3/gamma) * 2J|boundary S|,
    ||exp(itK)Q_S^a exp(-itK)-Q_S^a||
             <=sqrt(3/gamma) * 2J|boundary S| |t|.         (6)

One may take gamma=e_m. This is a bound on normalized physical initial
data; clock-slice amplitudes additionally require the D_X weights.
The resolvents in (6) are not local operators. Thus (6) is NOT a local
clock-current formula and does not transfer the distance-d Taylor-order
claim (3) to clock time. Even a positive tridiagonal matrix has, in general,
a nonzero distance-two matrix entry in its square root. The checker gives
an exact three-coordinate functional-calculus counterexample, not a finite
CCR approximation to the actual theory.

The [checker](checker.py) verifies exact graph multiplicities, path lengths,
cut cancellations, cocycle transition phases and the factorial inequality.
It is a regression for the preceding all-volume operator argument, not a
finite-state simulation or empirical transport measurement. Microscopic
couplings, spin/statistics, chirality, full stress and continuum are open.
