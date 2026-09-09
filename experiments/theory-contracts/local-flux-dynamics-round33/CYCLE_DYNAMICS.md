# Fully evaluated physical cycle dynamics with an unbounded-rotor certificate

2026-09-07. NON-RH / unpromoted. This is a declared three-site periodic
cycle, NOT a three-dimensional cubic torus. It uses the same functional
parent and a=1/12, beta=1/4, eta=1/2, kappa=1/100, M=4, V_mag=0.
The initial state below is stated separately from Round31's dressed
filled-Haar state. No physical parameter or vacuum selection is claimed.

## 1. An infinite physical sector, not the earlier finite Gauss cell

Orient links 0:0->1, 1:1->2, 2:2->0, and use two fermion species at each
site. The mode ordering is low0,low1,low2,high0,high1,high2. A hop along
an oriented link raises its electric flux by one. With q_x=1 and exactly
three fermions, Gauss law reads E_x-E_(x-1)+N_x-1=0. For each occupation
mask m with three set bits and EACH integer k, its complete solution is

    E0=k+1-N0, E1=k+2-N0-N1, E2=k.                           (1)

Thus the physical Hilbert space has 20 matter configurations and an
unbounded cycle label. Start from mask 7 (all three bare low modes filled)
and k=0, so every electric flux is zero. This normalized state is gauge
invariant, with total energy 1/96 and no bare high fermion. It is not the
gauge-dependent spectral-band rotation of the filled-Haar preparation.

The sector is genuinely unbounded under the same parent: from a filled
bare-low state at arbitrary k the sequence

    low0 -> high1, low2 -> low0, high1 -> low2

returns the matter mask to 7 and raises all three electric fluxes by one.
All three hoppings have nonzero parent coefficients and preserve Gauss.
The sequence can be repeated. Its existence establishes an infinite
connected basis graph, not a lower bound on a sum of interfering path
amplitudes. The nonzero Wilson response below is calculated independently.

## 2. Build the full parent BEFORE truncation

The checker expands the actual one-particle matrix

    h(A)=[[A+beta A^2, eta A],[eta A, M I]]

into all its directed monomials and then applies c_target^dagger c_source
with exact fermionic signs. There are 18 directed direct/species terms
and 12 ordered two-step terms. The latter include six backtracking terms.
Every term is checked against (1) before deciding whether its endpoint
survives the electric cutoff |E0|,|E1|,|E2|<=K. This constructs P_K H P_K,
not a new Hamiltonian guessed from a finite rotor.

This order matters. In general,

    P A^2 P = (P A P)^2 + P A (1-P) A P.                     (2)

The last term is positive and records intermediate paths omitted by
cutting A first. A one-edge physical witness uses q=(1,0), one fermion
and fluxes (0,1,0,1). At K=0 only the x states survive. The correct
compressed low_x energy includes beta a^2=1/576; cutting A first gives
A_K=0 and incorrectly removes it. This is a finite-regulator path
correction, not the same approximation as removing high fermions.

Truncated link shifts are partial isometries, not exact rotor unitaries.
No canonical fermion transformation is built from their noncommuting
matrix entries. Bare CAR, the physical positive inner product and the
Gauss restriction are retained throughout.

## 3. Bound all omitted electric sectors, not just two cutoff differences

Separate the parent into

    H0=(kappa/2)sum E_l^2+M N_high+(1/288)N_low,
    H=H0+V.

H0 is diagonal in electric flux and occupation. The bounded V consists
of three link low hoppings, six link species-changing Hermitian hoppings
and three nonbacktracking Hermitian two-step terms. Thus

    ||V|| <= J = 3a(1+2eta)+3 beta a^2 = 97/192.              (3)

In the H0 interaction picture, every term retains its norm and changes
each individual electric flux by at most one. Its matrix coefficients
acquire flux-dependent phases, but the phase factors are unitary and do
not change this support or norm statement. This is why unbounded E^2
does not appear in J.

Starting with zero flux, the Dyson expansions of full evolution and the
compressed P_K H P_K agree through order K. A product of at most K
interactions cannot have an intermediate monomial endpoint outside the
cutoff. Equation (2) is essential: it treats A^2 as a parent monomial
before making that endpoint argument. Each time-ordered n-th term has
norm <=(J T)^n/n!. Consequently, for T=|t|,

    ||U(t)psi0 - U_K(t)psi0|| <= 2 R_(K+1)(JT),
    R_(K+1)(x)=sum_(n>=K+1) x^n/n!
      <= [x^(K+1)/(K+1)!]/[1-x/(K+2)], x<K+2.               (4)

Every bounded norm-one observable therefore has full-versus-cutoff
expectation error at most 4R_(K+1)(JT). This controls the entire infinite
electric tail, not just numerical agreement between K=8 and K=12.
It is a finite-cycle bound: J is extensive on larger graphs, and (4)
must not be advertised as an arbitrary-volume local-observable bound.

The use of quantum-number growth and Hamiltonian truncation is related
to the established framework of [Tong, Albert, McClean, Preskill and Su,
Provably accurate simulation of gauge theories and bosonic systems](https://arxiv.org/abs/2110.06942)
(Quantum 6, 816, 2022). The simple zero-flux, bounded-interaction argument
and the constants in (3)-(4) are derived above for this particular parent;
we do not claim their general results or quantum-computer costs as new.

## 4. Exact arithmetic for the finite real-time calculation

The compressed physical matrix has 40K+8 states: 328 at K=8 and 488 at
K=12. All entries are integers divided by 14400. Subtracting 6I changes
only the overall phase. The centered absolute row sums bound the norm
by 1417/200 at K=8 and 1657/200 at K=12.

The code evaluates the degree-80 exponential polynomial applied to the
initial vector using Gaussian-integer Horner arithmetic with one common
denominator. There is no floating-point eigensolver. The unitary integral
remainder is bounded by ||H_K-6I||^81/81!, below 1e-30 in both cases.
The polynomial norm is independently checked against (1+/-tail)^2.
If its vector error is d, the readout error is <=d(2+d).

Adding this error to 4R_(K+1)(J) gives, before outward interval rounding,

    K=8:  readout error <=2.4891213423e-8,
    K=12: readout error <=9.3081e-14.                         (5)

These absolute bounds apply to every norm-one observable with its correct
compression; the following four are explicitly evaluated at t=1:

| Gauge-invariant readout | Certified full-rotor interval, K=12 |
|---|---|
| Bare high occupation at site 0 | [0.00071934464413, 0.00071934464432] |
| Probability E0=0 | [0.99928328547964, 0.99928328547983] |
| low0^dagger high0 + high0^dagger low0 | [-0.00404633584758, -0.00404633584738] |
| Re(U0 U1 U2), Wilson cycle | [0.00000021720204, 0.00000021720223] |

The first and third are matter readouts; the second and fourth explicitly
test dynamical gauge information. They are not copies of a fixed mean
charge, and the Wilson interval excludes zero. The electric measurement
is a bounded spectral projector, not the unbounded E0^2 operator.
No comparison with experimental data or physical time units is intended.

All six fermion modes are retained. In particular the nonzero high
occupation and interspecies coherence are computed, not set to zero by
definition. A theory which simply freezes this initial bare-low state
would instead give high=0, electric_zero=1, coherence=0 and Wilson=0.
That is a diagnostic of what an effective readout must reproduce, not a
proof that every consistently dressed low-energy theory fails.

## 5. Cost, remaining bridge, and claims not made

At K=12 the sparse centered matrix has 3932 nonzero entries. Each of the
80 Horner steps is a sparse integer matrix-vector operation. Integer bit
sizes grow with degree and the common denominator. This is practical for
this cycle because Gauss leaves only one integer flux and 20 matter masks.
General graph cost still grows exponentially with matter modes and with
the number of independent electric cycles; no efficient generic solver
or large cubic-box numerical result is claimed.

This supplies a reproducible full-dynamics reference with all infinite
electric sectors certified. It is not the desired high-fermion-eliminated
Hamiltonian. Next, a proposed low-only dynamics must reproduce these
matter AND gauge readouts using the same parent and stated preparation,
with consistent virtual/source terms; for the cubic family that comparison
must additionally be local and uniform in volume. Chiral matter, selected
parameters/state, continuum gravity and the complete T1-T8 conjunction
are all outside the proved result. Analytic arguments are not formalized
in a proof assistant or externally peer-reviewed here.

## 6. A constructive next term: the parent already induces Wilson potentials

There is a useful link to the desired low-only description. In the
canonical rotated frame, fix total fermion number equal to the number of
sites and compress to the empty-high sector. All low modes must then be
filled. Round31's determinant connection vanishes, Tr b_LL=0, so the exact
compression is a pure-gauge operator

    H_filled = (kappa/2)sum E_l^2 + Tr f_-(A)
                    +(kappa/2)sum_l Tr(S_l^* S_l).            (6)

This is PHP, not yet an exact elimination of the transitions out of P.
Nevertheless it supplies gauge dynamics from the same parent rather than
adding an independently chosen magnetic action. The scalar low-band
eigenvalue satisfies f^2-(M+x+beta x^2)f+M(x+beta x^2)-eta^2 x^2=0.
Its uniquely determined expansion at x=0 is

    f_-(x)=x+(beta-eta^2/M)x^2-eta^2 x^3/M^2
                 +[-beta eta^2/M^2+eta^2(eta^2-1)/M^3]x^4+O(x^5).

For beta=eta^2=1/4, c4=-(M+3)/(16M^3). Tr A^n is a sum of closed gauge
walks. On a triangle, Tr A^3=6a^3 Re W_triangle, so the leading triangle
potential is -6 eta^2 a^3 Re W_triangle/M^2. On an elementary square,
four starting vertices and two orientations give 8a^4 Re W_square.
The corresponding term is therefore

    -g_square Re W_square,
    g_square = a^4 (M+3)/(2M^3)>0.                           (7)

Up to a constant this is g_square(1-Re W_square), the positive U(1)
plaquette form. At a=1/12, M=4 its coefficient is 7/2654208. On open
simple cubic lattices this is the first flux-dependent term of Tr f_-(A).
Even periodic side lengths >=6 avoid both short winding loops and odd
cycles. The earlier 3-site or size-3 tori have triangular winding loops;
they must not be described as having no earlier loop term.

The Born-Huang term in (6) does not cancel this elementary-square
coefficient at fourth hopping order. Here is the check, including
noncommuting matrix derivatives. Write V(A) as the rotation by theta(A),
with

    theta(A)=u A+v A^2+w A^3+O(A^4),
    u=eta/M, v=eta/M^2,
    w=eta beta/M^2+eta(1-4eta^2/3)/M^3.

The metric is (1/4)Tr[(X_l cos(2theta))^2+(X_l sin(2theta))^2].
With X=X_l A, Y=AX+XA, Z=A^2X+AXA+XA^2, its fourth-order part is

    (v^2+u^4)Tr Y^2 +(2uw-4u^4/3)Tr XZ.

These traces reduce to combinations of Tr A^2 X^2 and Tr AXAX.
They insert the same differentiated link twice; a four-edge elementary
square uses each link once and cannot occur. On an isolated square with
A=a B, the checker finds Tr B^2(X_l B)^2=4 and
Tr B(X_l B)B(X_l B)=-2 for every link and arbitrary holonomies. Thus the
fourth-order metric has no square holonomy. This is a statement about
the leading expansion coefficient; higher orders can generate such
dependence and remain present in the exact formula (6).

Equation (7) is a concrete virtual gauge interaction generated by the
declared signed-wall parent. It is not a derivation of physical SU(3)xSU(2)xU(1),
a selected coupling, the complete magnetic action, or an error-controlled
replacement of (6) by its fourth-order term at the fixed hopping. No
quantitative agreement of this leading term with the bare-prepared
real-time table is asserted: preparation, Born-Huang terms, higher orders
and eliminated-channel memory must all be treated consistently.
