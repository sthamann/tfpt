# Microscopic neutral four-point limit from the same source

2026-09-09. NON-RH. Written analytic comparison, with finite independent CAR
and full-source checks. This is a four-point result for a specified QWZ
source and its normal-ordered neutral observables, not a charged local
field construction, a new interacting Hamiltonian, or T1--T8/TOE completion.

## 1. The observable and the actual advance

Keep exactly the width-8, mass-1, sector-r=1 QWZ cylinder on 16N one-body
modes, its negative spectral occupation P, and delta=4N^(-3/4). Write

```
t=N delta=4N^(1/4), B_a=ramp+pi Arc_a,
F_a=Phi_(delta,H)(B_a), a in {0,1/N,...,(N-1)/N},
epsilon=(-1,+1,-1,+1),
C_N^circ(a1,a2,a3,a4)
 = exp[-i sum_l epsilon_l Tr(P F_al)]
   det_P(P product_l exp(i epsilon_l F_al) P).
```

All products retain their displayed order. The determinant is taken on
the full occupied source space, not on an edge-only replacement.
For the original U_a=exp(-i ramp) exp(i F_a), the product
U_a1* U_a2 U_a3* U_a4 is exactly the displayed signed-F product.
The outer ramps cancel pair by pair. General neutral but nonalternating
U words do **not** have this cancellation and are not silently identified.
The phase above is the fixed normal-ordering coboundary, not a fitted phase.

Set w_k=exp[-(2pi k/t)^2], H_t=sum_(k>=1) w_k/k, Z_t=exp(H_t/8), and
S_t(d)=sum_(k>=1) w_k exp(2pi i k d)/k. The ordered Current target is

```
K_t(a1,a2,a3,a4)
 = exp[(S_t(a2-a1)-S_t(a3-a1)+S_t(a4-a1)
         +S_t(a3-a2)-S_t(a4-a2)+S_t(a4-a3))/4].
```

The principal new result is an end-point-uniform comparison of the original
source to this whole complex four-point amplitude, after the stronger Z_t^4
normalization. Two auxiliary-window choices below give respectively

```
sup_grid |Z_t^4 C_N^circ - K_t| = O(N^(-3/8)),
sup_grid |Z_t^4 C_N^circ - K_t| = O(N^(-3/4) (log N)^3).
```

The second is the stronger eventual bound. These are asymptotic theorems;
the explicit constants are coarse and not useful small-N error certificates.
Both compare the SAME physical C_N^circ. Only an intermediate proof window
changes. No parameter in the source Hamiltonian or its Gaussian width changes.

## 2. Two honest auxiliary windows

Let floorroot_k and ceilroot_k denote exact integer roots. Define

```
M_pow = min(floor(N/8), floorroot_8(N^3)),
b_N = bit_length(N) = floor(log_2 N)+1,
M_log = min(floor(N/8), floor(sqrt N), 64 ceilroot_4(N) b_N).
```

Both obey 1<=M<=min(N/8,sqrt N). In the first case M~N^(3/8).
In the second the last term is eventually active, giving
M=Theta(N^(1/4) log N). It is not asserted to be active at ordinary small N.
The integer implementation never rounds a floating-point cutoff.

For either choice build the same polarized source isometry J on -M<=j<=M,
using normalized P qtop_j for j>=1 and (I-P) qtop_j otherwise, and set

```
p_j=(2pi j-pi/2)/N, Pcur=1_(j>=1), R=I-JJ*,
Hsharp=J diag(-p_j)J*+RHR,
P_Hsharp=P_H=P, PJ=J Pcur,
Tbar_a=D_N T_a D_N* - pi/(2N) I, D_N[j,j]=exp(i pi j/N),
Fref_a=J Tbar_a J* + R Phi_(delta,Hsharp)(ramp) R.
```

The frozen proofs in `microscopic-energy-linearization`,
`source-current-symbol-match`, and `microscopic-neutral-limit` use the
inequality M<=N/8 for their finite estimates. Their old asymptotic evaluation
M~sqrt N is not reused here. Every M-dependent constant is recomputed below.
The extra sqrt-N cap also permits direct reuse of the frozen `source_strip`
diagnostic without extending that function's declared input domain.

For ANY neutral signed-F word the common R block cancels exactly, including
its normal-ordering phase. Conjugation by D_N and the scalar shift likewise
leave normal-ordered amplitudes unchanged. Thus the complete reference
amplitude is exactly the finite Current amplitude on 2M+1 modes.

## 3. Reparameterized finite estimates

Put d=16N, b=2pi, r0=1-1/49152 and

```
p_*=(2pi M+pi/2)/N, rho_*=2 sin^2(p_*/2),
eta=3 rho_*^8/sqrt(r0)+p_*^3/6,
kappa=2 sqrt(2/pi) eta/delta.
```

The projected residual columns are momentum-orthogonal, so there is no
extra sqrt(M) in ||H-Hsharp||op<=eta. Both operators have exactly the same
spectral sign P. For L unit signed legs, total raw norm is <=Lb and the
complete rotating-history linearization error satisfies

```
I_lin <= kappa sqrt(d) [Lb+(Lb)^2].
```

The fixed normal-order phases coincide leg by leg because
Tr(P Phi_H(B))=Tr(P B)=Tr(P Phi_Hsharp(B)). An estimate of absolute values
alone would not suffice.

The exact sampled symbol and transverse profile proof gives, for every
lattice endpoint, ||J*Fsharp_a J-Tbar_a||op<=eJJ with

```
gamma_*=rho_*^(15/2)/sqrt(2-rho_*), d0=1-pi^2/96,
eJJ=6pi rho_*^2 + 4pi sqrt(2) gamma_*
    +pi^2/(6d0 N^2) [t^2/(4pi^2)+t/(2sqrt(2pi))].
```

The unsmoothed raw reference and actual raw B_a have norm <=b.
For lambda=M/(8N), r=8lambda^2 and s=2r^(15/2), the low-energy inventory
proved in `microscopic-neutral-limit` applies unchanged: below 2lambda
there are only the selected top modes and actual opposite-sign bottom
modes, no bulk or omitted-window mode. The bottom eigenvector differs
from its minus-spin quasimode by <=s, in operator norm over all momenta.
The tilted top-mode removal retains a >0.9 sign-adjusted bulk gap; it does
not assume that an uncorrected bulk bound survives arbitrary compression.

Every raw B_a commutes with Gamma=I_y tensor sigma_x, so the ideal top/bottom
cross matrix is exactly zero. The bottom quasimode's top-two-row tail is
<=r^6. Consequently

```
||E_(2lambda)(Fsharp_a-Fref_a)E_(2lambda)||op <= e,
e=eJJ+2b s+pi(r^6+s)^2.
```

This local estimate is not substituted for the whole history. With
Bdiff=2b, g=exp[-lambda^2/(2delta^2)] and W_L=exp[Lb exp(1/2)+1/2], the
full weighted-frame comparison gives

```
epsilon=e+Bdiff sqrt(d) g,
c=sqrt(d) [e+2Bdiff g],
I_sharp,ref <= Lc+L^2 b sqrt(d) [epsilon+Bdiff W_L exp(-lambda/delta)].
```

This bound explicitly retains excursions into high energies and both
diagonal frames. It follows from the right-evolving Duhamel identity and
||exp(v|Hsharp|)Dref exp(-v|Hsharp|)||op<=b exp(v^2delta^2/2), with v=1/delta.
It is valid for every fixed L; none of the steps assumes L=2.

Finally define

```
Qheat=exp(eta^2/delta^2)
      [sqrt(2pi) N delta+2+16N exp(-1/(32delta^2))],
Aref <= L sqrt[(2+log t)/4+pi^2 Qheat],
Z_t^L <= exp[L(2+log t)/8].
```

The independent vacuum-history comparison, with the triangle inequality
for full histories, proves

```
Z_t^L |C_source^circ-C_ref^circ|
 <= Z_t^L (1+2sqrt(2) Aref) (I_lin+I_sharp,ref).
```

No Fock operator-norm estimate or static-crossblock shortcut appears here.

## 4. Rates, and why the four-point normalization now fits

For M_pow~N^(3/8), p_*=O(N^(-5/8)), hence

```
eta=O(N^(-15/8)), I_lin=O(N^(-5/8)),
eJJ=O(N^(-3/2)), I_sharp,ref=O(N^(-1)),
lambda/delta=Theta(N^(1/8)), Aref=O(N^(1/8)),
Z_t^L=O(N^(L/32)).
```

Thus L=4 gives a source/reference error O(N^(-3/8)); the sharp/reference
part alone is O(N^(-3/4)). The frozen finite-Current Galerkin bound is

```
|C_ref-C_current|
 <= 2L C(t) sqrt(1+L^2 c0 t/4)
    exp[L^2 c0/4-(M+1)/t],
c0=exp(1/(2pi^2))/(2sqrt(2pi)),
C(t)=exp(1/(4pi^2)) [pi/sqrt(6)+sqrt(2+log t)/2].
```

For L=4 and M_pow, its normalized size is
O(N^(1/4) sqrt(log N) exp[-N^(1/8)/4]), which is smaller than any fixed
power. The floor causes no loss since M+1>N^(3/8) once the other cap is inactive.

For the stronger logarithmic window, eventually

```
M=64 ceilroot_4(N) b_N=Theta(N^(1/4) log N),
lambda/delta=M/(8t)>=2b_N>=2 log N,
M/t>=16b_N>=16 log N.
```

Now eta=O(N^(-9/4)(log N)^3) and I_lin=O(N^(-1)(log N)^3).
The profile part of eJJ is O(N^(-3)(log N)^4), below its sampling part
O(N^(-3/2)). The Gaussian tails are superpolynomially small; the weighted
frame tail sqrt(N) exp(-lambda/delta) is O(N^(-3/2)). Therefore
I_sharp,ref=O(N^(-1)), while Aref and Z have the same rates as before.
This gives the stronger L=4 bound O(N^(-3/4)(log N)^3). The normalized
Galerkin contribution is at most O(N^(1/4-16) sqrt(log N)).

More generally the same logarithmic argument controls every fixed neutral
unit signed-F word with

```
Z_t^L |C_source^circ-C_current|=O(N^((L-28)/32)(log N)^3)
```

for even L<28. This is a bounded-order comparison to the smoothed Current,
NOT an assertion of unsmeared point values, L1 limits at all those orders,
or a common field domain. L=28 is a limit of this particular majorant, not
a physical no-go theorem. At general fixed L the normalized logarithmic
Galerkin bound is O(N^(L/32+1/8-16) sqrt(log N)), not the L=4 specialization
displayed above. It remains smaller than the stated comparison rate.

## 5. The full four-point L1 limit, including collisions

The independent `current-fourpoint-limit` proof gives the ordered BCH
formula and convergence in L1(T^4) to

```
K_infinity(a1,a2,a3,a4)
 = exp[(1/4) sum_(i<j) epsilon_i epsilon_j
                Log(1-exp(2pi i(a_j-a_i)))], epsilon=(-,+,-,+).
```

Each ordered pair uses the radial boundary of its own analytic logarithm.
Taking one principal fourth root of a quotient of all factors can change
the phase and is not the definition. At (0,1/4,1/2,3/4) the value is exp(i pi/8).

For completeness, the collision argument is short. Let
v(d)=-log(2|sin pi d|), v_t=G_t*v with the positive circle heat kernel G_t.
Then v_t>=-log 2, so the two like-sign factors have combined modulus <=sqrt(2).
Put h=exp(v/4)=(2|sin pi d|)^(-1/4) and h_t=exp(v_t/4).
Jensen gives h_t<=G_t*h. The four unlike-sign factors form the complete
bipartite graph between the two minus and two plus endpoints. For 1<p<2,
integrating each plus endpoint with Cauchy--Schwarz gives

```
||K_t||_p^p <= 2^(p/2) ||h_t||_(2p)^(4p)
             <= 2^(p/2) ||h||_(2p)^(4p) < infinity,
```

uniformly in t, since p/2<1. Off collisions S_t approaches its ordered
logarithmic boundary value. Uniform Lp bounds and a.e. convergence imply
L1 convergence by uniform integrability. Thus double, triple, and quadruple
collisions are controlled on the full torus, not deleted from the theorem.

To transfer this to the microscopic grid, extend C_N^circ piecewise constantly
in all four endpoints. The unitary Current vacuum word satisfies |K_t|<=Z_t^4;
the logarithmic derivative in any endpoint is bounded by
3pi/2 sum_(k>=1) w_k=O(t). Hence ||partial_a K_t||infty=O(t^(3/2)).
Moving four endpoints by <=1/N costs O(t^(3/2)/N)=O(N^(-5/8)). Together
with Section 4 and the Current L1 theorem this proves

```
Z_t^4 C_N^circ (piecewise constant) -> K_infinity in L1(T^4).
```

This justifies integration against every bounded four-endpoint test function.
No finite numerical quadrature is used to prove integrability.

## 6. Which positivity survives, and which remains unproved

Let V(a,b)=U_a*U_b. More explicitly the pair-created Fock vectors are

```
Psi_N(a,b)=Z_t^2 exp[-i Tr P(F_b-F_a)] Gamma(V(a,b)) Omega_P.
```

The phase multiplies the Fock vector once; it is not put into the one-body
unitary and then raised to the occupied particle number. Their Gram kernel is

```
G_N((a,b),(c,d))=Z_t^4 C_N^circ(b,a,c,d).
```

The reversal (b,a) is essential. Finite G_N is positive semidefinite because
it is a Slater Gram matrix, with the harmless scalar phase and positive
normalization included. Piecewise-constant interpolation preserves this
property. For any bounded pair test f, L1 convergence gives
integral conjugate(f(a,b)) K_infinity(b,a,c,d) f(c,d) >=0.

This is a positive pair-observable form. It is not Osterwalder--Schrader
positivity, spacetime locality, a charged field algebra, or a common
adjoint-closed operator domain. A Gaussian Current can have nontrivial
vertex four-point correlations without acquiring an interacting Hamiltonian.
No Clock/eight-channel tensor identification, 3+1-dimensional parent,
universal gravity coupling, RH implication or TOE closure follows here.

## 7. Reproduction and next acceptance gate

`checker.py` pins the previous microscopic checker transitively and recomputes
all new-window constants. `test_checker.py` independently checks the ordered
CAR amplitude, exact cutoff arithmetic, source sign preservation, symbol
bounds, full four-leg histories, physical ramp cancellation and pair Gram
orientation. Diagnostics include full 16N sources for N=8,16,32 and an
unsymmetrical held-out word at N=24; large-N
rows evaluate analytic majorants only and are labelled as floating evaluations.

The next field-construction gate is not another separated-point fit:
identify compatible charged/zero-mode sectors from the microscopic source
and establish an adjoint-closed common domain, then control genuinely ordered
higher products and their exchange
relations. The logarithmic comparison opens fixed orders up to 26 on the
comparison side, but does not supply those operator or higher-collision
theorems automatically. The target lattice zero-mode representation already
exists in `charged-cocycle-lift`; merely appending it as an independent tensor
factor would not prove the missing microscopic identification.
The parallel Clock/rotor audit addresses a different
common-parent obstruction; its result must not be added to this result as
if the two already shared a physical algebra and state.
