# Round 9: canonical constraint dressing and finite quadratic quantum completion

## Result

There is an exact, bounded answer for the **equal-time constraint algebra**.
Let the four nonzero-mode vacuum gravity constraints `c_a` commute, and let
`X^a` be gravity gauge coordinates satisfying

```text
{c_a,c_b}=0,       {X^a,c_b}=delta^a_b,
{gravity,matter}=0.
```

For matter currents `J_a` (in the Round-7 convention
`J=(rho,-j_1,-j_2,-j_3)`), put

```text
F_ab := {J_a,J_b}_m.
```

Then the constraints

```text
C_a^(2) = c_a + g J_a - (g^2/2) X^b F_ab                         (1)
```

obey

```text
{C_a^(2),C_b^(2)} = O(g^3)                                      (2)
```

exactly.  This cancels the Round-7 `g^2 {J_a,J_b}` residual.  The same
construction has a formal all-order completion

```text
C_a(g) = exp(g D_S)c_a,
S = -X^b J_b,                 D_S A := {A,S},                    (3)
```

and therefore `{C_a(g),C_b(g)}=0` coefficient by coefficient.

For the actual **finite-volume free scalar**, sections 8–9 strengthen this:
the real-space chart covers every nonzero lattice mode, including
self-conjugate modes, and a decomposable unitary implements the dressing for
every real `g` on one kinematic tensor-product Hilbert space. The dressed
constraints are self-adjoint and strongly commute. This is not merely a
finite-matrix approximation to canonical commutation relations.

Section 7 also constructs a **classical matched-vertex Hamiltonian
completion**. Given the established first-order Ward identity, it preserves
the chosen local first-order stress vertex and supplies `V_2` and all higher
terms through a generally nonlocal dressing. Positivity and the interacting
quantum Hamiltonian domain do not follow from that algebra. Section 10 gives
a **chosen positive reduced quantum completion** by closed quadratic forms;
it retains the first stress vertex but adds a nonlocal second-order term.
Its microscopic derivation and full unreduced quantum matching remain open.

This is a **canonical reparameterization of the decoupled first-class
system**, not a construction of local interacting gravity.  For the current
staggered tensor constraints, every translation-invariant conjugate `X` has
an inverse-gradient pole in the vector sector and an inverse-Laplacian pole
in the scalar sector.  Formula (1) is consequently nonlocal unless the
specific matter bracket supplies enough derivative factors to cancel those
poles.  It does not do so by algebra alone.

The result is non-RH.  It neither proves TOE/T7 closure nor changes any
repository claim.

## 1. Exact second-order proof

All repeated constraint labels are summed.  The Poisson convention is
`{q,p}=1`, and the adjoint convention in (3) is

```text
D_S A = {A,S}.
```

Since `S=-X^bJ_b`, the assumed conjugacy gives

```text
D_S c_a = {c_a,-X^bJ_b} = J_a,                                  (4)
D_S^2 c_a = {J_a,-X^bJ_b} = -X^b F_ab.                          (5)
```

Thus (1) is exactly the Taylor polynomial of (3) through order `g^2`.
It is also useful to verify cancellation without invoking the all-order map.
Write

```text
K_a = -(1/2)X^dF_ad.
```

Matter functions commute with `c` and `X`.  Therefore

```text
{c_a,K_b} = +(1/2)F_ba = -(1/2)F_ab,
{K_a,c_b} = -(1/2)F_ab.
```

Expanding the bracket gives

```text
{C_a^(2),C_b^(2)}
  = g^2 (F_ab + {c_a,K_b} + {K_a,c_b}) + O(g^3)
  = 0 + O(g^3).                                                  (6)
```

This is an identity for any matter Poisson algebra; no commutativity or Ward
assumption on the `J_a` was used.  The displayed `K_a` is the canonical
Lie-series choice, not a uniqueness theorem.  One may add second-order
cocycles whose antisymmetrized gauge derivative vanishes.

The truncation should not be mistaken for an exact solution.  In the
noncommuting example checked below, the `(a,b)=(0,3)` bracket has

```text
[g^3]{C_0^(2),C_3^(2)} = -(X^2 q_1 + X^3)/2 != 0.                (7)
```

The next Taylor term `(g^3/6)D_S^3c_a` cancels all six brackets through
order `g^3`; the checker verifies this independently.

## 2. Formal all-order theorem

Hamiltonian flow is a Poisson automorphism.  Consequently

```text
{exp(gD_S)A, exp(gD_S)B} = exp(gD_S){A,B}.                       (8)
```

Applying (8) to the commuting vacuum constraints proves

```text
{C_a(g),C_b(g)} = exp(gD_S){c_a,c_b} = 0.                        (9)
```

This is an exact formal-power-series statement.  In a finite-dimensional
analytic phase-space patch it is also an ordinary local-in-`g` statement for
as long as the Hamiltonian flow of `S` exists.  No convergence or global-flow
claim is made for the infinite lattice or continuum limit.

The construction is canonically equivalent to the starting system.  In
particular, it does not create a gravity self-interaction, new local
observables, or new physical degrees of freedom.  Its value here is narrower:
it gives an exact algebraic counterterm and identifies what a universal
completion must pay in locality.

## 3. Quantum sign and common ordering

Suppose, only as an algebraic/domain hypothesis, that Hermitian operators on a
common invariant domain satisfy

```text
[X^a,c_b]=i hbar delta^a_b,    [c_a,c_b]=0,
[gravity,matter]=0.
```

Let `S=-X^aJ_a`.  The quantum transformation with the sign matching (3) is

```text
U(g) = exp(i g S/hbar) = exp(-i g X^aJ_a/hbar),
C_hat_a(g) = U(g)c_hat_a U(g)^dagger.                            (10)
```

Indeed,

```text
(i/hbar)[S,c_a] = J_a,
C_hat_a(g)
 = c_a + gJ_a + (i g^2/(2 hbar))X^b[J_a,J_b] + O(g^3).          (11)
```

Thus the ordered quantum second-order term is

```text
K_hat_a = (i/(2 hbar)) X^b[J_a,J_b].                            (12)
```

There is no `X`/matter ordering ambiguity because the two tensor factors
commute.  If the matter currents are Weyl-ordered quadratics, as in the free
scalar witness below, their Moyal series terminates and

```text
[J_a,J_b] = i hbar Op_W(F_ab)
```

exactly.  Equation (12) then reduces to the Weyl quantization of
`-(1/2)X^bF_ab`, with no `hbar^2` remainder.  At all higher orders, the BCH
series of the single generator in (10) is a common ordering prescription.

For arbitrary matter currents these remain operator hypotheses: algebra alone
does not establish self-adjointness or a common domain. Section 9 supplies
these missing facts for the finite-volume, Weyl-quadratic free scalar, using
the real-space chart of section 8. Compatibility with the intended interacting
Hamiltonian is not supplied even in that case.

## 4. Gauge coordinates for the actual complex Fourier constraints

This section avoids treating `c_i=iBp` as if it were a physical real fibre.
Take an unordered, non-self-conjugate Fourier pair `{k,-k}` with `r^2=kappa^T
kappa != 0`, and use normalized real and imaginary coordinates
`q_R,q_I,p_R,p_I`.  Their brackets are

```text
{q_R^A,p_R^B}=delta^AB,   {q_I^A,p_I^B}=delta^AB,
```

with all cross brackets zero.  From the Round-7 definitions

```text
c_0(k)=-s^Tq(k),          c_i(k)=i(Bp(k))_i,
```

the eight real constraints on the pair are

```text
c_0R=-s^Tq_R,             c_0I=-s^Tq_I,
c_VR=-Bp_I,               c_VI= Bp_R.                            (13)
```

For the orthonormal tensor basis used by Round 7,

```text
BB^T = (r^2 I + kappa kappa^T)/2,
(BB^T)^-1 = 2I/r^2 - kappa kappa^T/r^4,
s^Ts = 2r^4,              Bs=0.                                 (14)
```

Put `R=(BB^T)^-1` and `W=RB`.  A commuting conjugate chart is

```text
X_0R = s^Tp_R/(2r^4),     X_0I = s^Tp_I/(2r^4),
X_VR = -Wq_I,             X_VI =  Wq_R.                          (15)
```

Direct multiplication gives

```text
{X_A,c_B}=delta_AB,       {X_A,X_B}=0,       {c_A,c_B}=0.        (16)
```

The checker proves (14)-(16) symbolically for generic `kappa`.  This is a
chart on the stated paired nonzero-mode stratum.  It does not cover `k=0`,
where `B=s=0`, nor does it by itself audit self-conjugate Brillouin-boundary
modes or reciprocal-zone gluing. Section 8 handles those nonzero boundary
modes directly in real space. The removed homogeneous gravity block is still
not a receiver for total matter energy.

## 5. Locality obstruction

The pole orders are already visible in (15):

```text
X_0 ~ (s/r^4)p ~ p/r^2,      X_V ~ (B/r^2)q ~ q/r.               (17)
```

There is also a short regulator-independent proof.  A
translation-invariant finite-range lattice operator has a Fourier symbol that
is a Laurent polynomial in the lattice phases.  It is continuous and bounded
at `k=0`.  The scalar constraint symbol vanishes quadratically there and the
vector constraint symbol vanishes linearly.  If a finite-range conjugate
`X(k)` existed on every punctured neighbourhood of zero, its symbol would
satisfy

```text
X(k) C(k) = 1.                                                   (18)
```

Taking `k -> 0` would give `0=1`, a contradiction.  A finite periodic lattice
with the zero mode deleted admits the Moore-Penrose inverse, but its real-space
kernel spans the lattice; its range is not uniformly finite as volume grows.

Therefore the universal dressing (1) is nonlocal.  A special bracket `F_ab`
can cancel a pole if it contains the corresponding derivative factor.  The
present theorem does not decide that model-specific divisibility question and
does not rule out every other local second-order ansatz.  It does rule out
calling the bare canonical dressing a local gravity interaction.

## 6. A genuinely noncommuting four-current scalar witness

To show that (1) is not being tested only on one nonzero bracket, the checker
uses the established full-3D free-scalar density and three link currents at
one site, with lattice spacing `a=1`:

```text
rho_0 = p_0^2/2 + m^2 q_0^2/2
        + (1/4) sum_i [(q_{+i}-q_0)^2+(q_0-q_{-i})^2],
j_i   = -(p_0+p_{+i})(q_{+i}-q_0)/2,
J     = (rho_0,-j_x,-j_y,-j_z).                                 (19)
```

All six independent entries of `F_ab={J_a,J_b}` are nonzero polynomials.
For the exact rational datum

```text
m^2=2,
(q_0,q_x,q_-x,q_y,q_-y,q_z,q_-z)=(-2,-1,0,1,2,3,4),
(p_0,p_x,p_-x,p_y,p_-y,p_z,p_-z)=(1,2,3,4,5,6,7),
```

the bracket matrix is

```text
F = [[   0, -11/2, -17, -53/2],
     [11/2,     0,  -1,    -2],
     [  17,     1,   0,    -1],
     [53/2,     2,   1,     0]].                                (20)
```

It has determinant `4` and rank `4`.  The checker also proves the four Jacobi
identities symbolically, so (20) comes from one common canonical matter
algebra rather than independently assigned structure constants.  These local
operators are quadratic; the exact Weyl-commutator statement in section 3
therefore applies to this illustration.

This witness is not a common-Hilbert-space gravity construction, a smeared
Dirac algebra, or a substitute for the separate all-lattice current-algebra
analysis.  It establishes exactly the limited fact needed here: all four
matter-current directions can be genuinely coupled by a nondegenerate
Poisson matrix.

## 7. Matched-vertex classical Hamiltonian stabilization

Constraint brackets are only one half of dynamical closure.  Let

```text
H = H_0 + H_m + g V_1 + g^2 V_2 + ...,
{c_a,H_0}=A_a^b c_b.
```

Round 7 establishes the first-order Ward equation

```text
{J_a,H_m}+{c_a,V_1}=A_a^bJ_b.                                  (21)
```

Keeping the same propagation matrix `A`, second order additionally requires

```text
{K_a,H_0+H_m}+{J_a,V_1}+{c_a,V_2}=A_a^bK_b.                     (22)
```

Here `A_a^b` is a fixed c-number matrix/operator on constraint labels, as in
the linear Round-7 propagation equations. A phase-space-dependent `A` would
also have to be transformed in the following conjugation argument.

There is a tautological exact stabilization of the canonical reparameterized
system: transform the whole decoupled Hamiltonian,

```text
H_dress(g)=exp(gD_S)(H_0+H_m).                                  (23)
```

Then (8) gives `{C_a(g),H_dress(g)}=A_a^bC_b(g)`.  But its first-order vertex
is fixed to

```text
[g]H_dress = {H_0+H_m,S}
            = -{H_0,X^a}J_a - X^a{H_m,J_a},                    (24)
```

which is nonlocal through `X` and has not been shown equal, even modulo
constraints, to the Round-7 local `q:tau` coupling.  Equation (23) is thus a
canonical change of variables, not the missing gravitational dynamics.

There is, however, a stronger construction that **does match the prescribed
first vertex**, without claiming locality. Set `H_f=H_0+H_m` and define

```text
W = V_1-D_S H_f,
H_match(g) = exp(gD_S)(H_f+gW).                                 (23a)
```

By the derivation property of Hamiltonian flow,

```text
{c_a,D_S H_f}
 = D_S{c_a,H_f}-{D_S c_a,H_f}
 = A_a^bJ_b-{J_a,H_m}.
```

Subtracting this equality from the first-order Ward identity (21) proves
`{c_a,W}=0` **strongly**, not merely on the vacuum constraint surface.
Consequently (8) gives

```text
{C_a(g),H_match(g)}=A_a^b C_b(g),
[g]H_match=V_1,
V_2 = D_S V_1-(1/2)D_S^2 H_f.                                 (23b)
```

This proves (22) and all subsequent classical stabilization equations at
once. For arbitrary currents it is a formal/local-flow construction. For
the finite quadratic currents of section 9 the dressing flow exists for every
real `g`, so (23a) defines ordinary functions at every coupling parameter.
Completeness in the dressing parameter is **not** global physical-time
existence for the Hamiltonian flow of `H_match`.

The statement is conditional on the exact first Ward identity for the chosen
vertex; it cannot repair a vertex violating (21). With the fixed 3D free
scalar Ward source and Round-7 stress vertex, this is the stated compatible
case. Unlike pure conjugation (23), the invariant remainder `W` may contain
a real TT–matter interaction. Therefore `H_match` must not be described as
unitarily/canonically equivalent to a completely decoupled free Hamiltonian:
it is equivalent to `H_f+gW`, whose interacting physics still requires analysis.

The unavoidable outstanding tests are substantial. The correction is
generally spatially nonlocal through `X`; a finite-range completion has not
been obtained. Neither lower boundedness nor a self-adjoint interacting
quantum Hamiltonian follows from this algebra. For example the perfectly
gauge-invariant physical interaction `W=q u^2` added to two free oscillators
gives, along `q=-g u^2`, zero momenta,

```text
H_f+gW = -g^2 u^4/2+u^2/2 -> -infinity     (g != 0).
```

Thus even exact constraint closure and exact vertex matching do not imply a
stable theory. `hamiltonian_stabilization.py` verifies (21)–(23b) in a canonical
model with a nonzero propagation matrix, two noncommuting currents, and a
nonzero invariant physical vertex. It also verifies that omitting `V_2` fails
and that the energy counterexample above survives. The proof, not this finite
example alone, establishes the general matched-vertex formula.

Section 10 adds an explicit positive reduced completion; it is a further
choice of invariant second-order interaction, not positivity of (23a) alone.

## 8. A real-space chart on every nonzero periodic lattice mode

Let the lattice have `n=L^3` sites, `L>=2`, spacing `a>0`, and periodic shifts
`S_i`. Put `D_i^+=(S_i-I)/a`, `D_i^-=(I-S_i^T)/a`, and
`Delta=sum_i D_i^-D_i^+`. In the orthonormal tensor order
`(11,22,33,23,13,12)`, the real-space scalar row acting on `q` has blocks

```text
A_ii = D_i^-D_i^+ - Delta,
A_ij = sqrt(2) D_i^-D_j^-     (i<j).
```

The vector row acting on `p` has diagonal block `D_i^+` in row `i`, and an
off-diagonal `ij` block contributes `D_j^-/sqrt(2)` to row `i` and
`D_i^-/sqrt(2)` to row `j`. Call this matrix `V`. These are the staggered
scalar and vector constraints in real coordinates. Define

```text
z=(q,p),    Omega=[[0,I],[-I,0]],    c=Cz,    C=diag(A,V),
P0=I_4 tensor (ones(n,n)/n),          G=C C^T,
Gplus=(G+P0)^(-1)-P0,                X=-Gplus C Omega z.          (25)
```

`P0` acts on the four constraint fields, not on matter. The four spatially
constant constraint smearings vanish identically. The full homogeneous
gravity block is excluded as in Round 7; equivalently restrict `z` to
zero-mean `q` and `p` before choosing independent coordinates.

**Proof.** Since `(D_i^+)^T=-D_i^-` and all shifts commute, the diagonal
and off-diagonal terms in `A V^T` cancel. Thus `C Omega C^T=0`. Every block
contains a difference, so `P0 C=0` and `C` also annihilates constant input
tensor fields. In physical-position Fourier coordinates, the scalar Gram
eigenvalue is `s^T s=2r^4`; the vector Gram is
`(r^2 I+kappa kappa^T)/2`, with eigenvalues `r^2,r^2/2,r^2/2` for `r>0`.
Staggering phases are unitary changes of coordinates and do not change these
singular values. Hence the kernel of `G` consists of exactly four means,
including for even `L` and self-conjugate modes. It follows that

```text
Gplus G=I-P0,
{X,c}=I-P0,
{X,X}=0,
P0 X=0.                                                        (26)
```

For the third identity use `Omega^2=-I` and `C Omega C^T=0` in (25).
Choose any real orthonormal basis of `range(I-P0)`. Equations (26) then give
`M=4(n-1)` independent canonical gauge pairs `(X_a,c_a)`. Finite-dimensional
symplectic linear algebra extends them to a Darboux basis, with `2(n-1)`
remaining physical canonical pairs after exclusion of the six homogeneous
gravity pairs. This counting is not the counting of the unreduced `12n`
matrix space, which still contains those six pairs.

`lattice_gauge_chart.py` verifies the complete matrix identities exactly for
`L=2` and `L=3`. The all-volume argument is the proof above, not an
extrapolation from those two sizes. The inverse in (25) remains spatially
nonlocal; this construction does not remove the poles of section 5.

## 9. All-real-coupling quantum theorem for finite quadratic matter

Take the independent nonzero-mode constraints from section 8 and smear the
actual free scalar currents with the same real basis. All `J_a` are then real
Weyl-ordered homogeneous quadratic polynomials in finitely many canonical matter
coordinates. Matter itself may include its homogeneous mode; projecting the
constraint labels does not solve the missing global energy constraint.
Set `hbar=1` in this section. In the Darboux representation use

```text
Hkin = L^2(R^M_X) tensor L^2(R^n_phi) tensor H_TT,
c_a=-i partial/partial X_a,
Q(x)=sum_a x_a J_a,
(U_g psi)(x,phi)=exp(-i g Q(x)) psi(x,phi).                      (27)
```

**Theorem.** For every fixed finite lattice, (27) is a strongly continuous
unitary group for all real `g`. The operators
`C_a(g)=U_g c_a U_g^dagger` are self-adjoint on
`U_g Dom(c_a)` and strongly commute. They have a common invariant core

```text
D=C_c^infinity(R^M_X; Schwartz(R^n_phi)) tensor Schwartz(TT).    (28)
```

Here the first factor denotes smooth compactly supported, Schwartz-valued
functions, not just finite sums of separated `x` and `phi` functions.

**Proof.** For fixed `x`, `Q(x)` is a real quadratic Hamiltonian. Its Weyl
quantization has a unique self-adjoint closure and its evolution is
metaplectic. This standard finite-dimensional input is established in
[Combescure–Robert, *Quadratic Quantum Hamiltonians revisited*, Theorem 4.1,
Remark 4.6 and section 5](https://arxiv.org/html/math-ph/0509027v1).
No positivity of `Q(x)` is required. There is no finite-time blow-up of the
associated linear symplectic flow, even when its norm grows exponentially.

The remaining direct-integral and domain steps are as follows. The quadratic
coefficients depend linearly on `x`; their symplectic flow and its unique
metaplectic lift starting at the identity depend smoothly on `(g,x)`. Thus
`u_g(x)=exp(-igQ(x))` is strongly measurable and pointwise unitary. Integrating
`||u_g(x)psi(x)||^2=||psi(x)||^2` over `x` proves global unitarity and
`U_g U_h=U_(g+h)`. Pointwise strong continuity and the integrable bound
`4||psi(x)||^2` prove strong continuity by dominated convergence.

Metaplectic covariance expresses multiplication and differentiation of
`u_g(x)f` as finite linear combinations of multiplication and differentiation
of `f`. On compact `(g,x)` sets the coefficients are bounded; this gives
locally uniform bounds in every Schwartz seminorm. Differentiation with
respect to `x_a` inserts an integral of a conjugated quadratic `J_a`, hence
again a continuous operator on Schwartz space. Repeating this argument proves
smooth parameter dependence in that space. Consequently `U_g D=D`: support
in `x` is unchanged and both `U_g` and `U_-g` preserve (28).

For completeness, the generator on this domain is not an assumed arbitrary
self-adjoint cubic polynomial. On finite Hermite sums of maximal oscillator
degree `N`, a quadratic operator changes degree by at most two and obeys a
bound of the form

```text
||Q(x)^k f_N|| <= C_K^k product_(j=1..k)(N+2j+1) ||f_N||
```

uniformly for `x` in a compact set `K`. After division by `k!` this has a
positive convergence radius in the evolution parameter. Products of smooth
compact `x` functions and finite Hermite sums are therefore a dense set of
analytic vectors for the symmetric multiplication operator `Q(X)`.
The analytic-vector criterion gives its essential self-adjointness; its
closure is the generator of (27). TT variables are unaffected.

The ordinary momenta `c_a` are self-adjoint and have strongly commuting
spectral projections. The domain (28) is a common core for them. Simultaneous
unitary conjugation transports these spectral projections, their commutation,
and their operator domains. Since `U_g D=D`, it also transports their common
core to the same domain. This proves the theorem, not only a zero formal
commutator on an unspecified domain.

The second-order expansion is precisely (11). All nested matter commutators
remain quadratic; after the first commutator the expressions depend on `X`
but not on `c`, so extra gravitational Moyal derivatives cannot introduce
higher-order ordering corrections. The unitary definition, rather than an
assertion of norm convergence of an unbounded-operator BCH series, supplies
the all-`g` completion. Classically the same completion is global: `X` is
constant along the dressing flow, matter obeys a linear ODE at fixed `X`,
and the remaining `c` equations integrate finite quadratic functions of that
solution on each finite parameter interval.

This theorem concerns a **kinematic Hilbert space and a canonically
reparameterized free system**. It does not construct the physical
interacting-gravity Hilbert space, or prove equivalence of its first
Hamiltonian vertex to the local Round-7 stress coupling. There is no
infinite-volume or continuum implementability assertion.

### A closed-form noncommuting unitary witness

For one matter coordinate `q`, let `p=-i partial_q`,
`J_0=q^2/2`, `J_1=(qp+pq)/2=-i(q partial_q+1/2)`. Then
`[J_0,J_1]=i q^2`. For two gauge coordinates `(x,y)` define

```text
B(g,y)=(1-exp(-2gy))/(4y),      A(g,y)=partial_y B+2gB,
B(g,0)=g/2,                    A(g,0)=g^2/2,
(U_g f)(x,y,q)=exp(-gy/2) exp(-i x B(g,y) q^2) f(x,y,exp(-gy)q).
```

The limits at `y=0` are removable, so these are smooth real functions.
The half-density factor cancels the dilation Jacobian in the norm.
The identity `B(g+h,y)=B(g,y)+exp(-2gy)B(h,y)` gives the group law, and
direct differentiation gives `partial_g U_g=-i(xJ_0+yJ_1)U_g`, `U_0=I`.
The conjugated constraints are

```text
C_x=-i partial_x+B q^2,
C_y=-i partial_y+g J_1+x A q^2,
[C_x,C_y]=i(-A+partial_y B+2gB)q^2=0.                           (29)
```

Without the correction, `[c_x+gJ_0,c_y+gJ_1]=i g^2 q^2`.
`quantum_dressing.py` tests the exact differential-operator identities on an
arbitrary smooth test function, the unitary evolution equation, the group
law, removable limits, the actual intertwining identities `C_a U_g=U_g c_a`,
and the first two expansion coefficients. The
all-volume finite-quadratic theorem rests on the argument above; this
two-current example is an explicit sign, ordering and domain-compatible
witness, not a replacement for that argument.

Audit note: the added `C_y U_g=U_g c_y` regression initially produced two
different unevaluated SymPy `Subs` encodings of the same partial derivative.
The checker now explicitly holds the second argument fixed while composing
the third argument with the `y`-dependent dilation. A separate chain-rule
calculation identified the representation issue; no derivative term was
dropped and the regression still acts on an arbitrary smooth function.

## 10. A chosen positive reduced quantum completion

The negative-energy example in section 7 rules out automatic positivity, not
the existence of every positive higher-order completion. In the finite,
zero-mean gravity target one can explicitly choose such a completion without
changing the reduced first stress vertex.

First verify the reduction used here. For any TT tensor `w`, `Bw=0` and
`t^T w=0` imply `s^T w=0`, `K_p w=w`, and `K_q w=r^2 w`. The real symmetric
free matrices therefore have no cross terms between TT variables and their
orthogonal complement. The chart coordinates and constraints of section 8
annihilate TT directions. Choose the Darboux complement to be the ordinary
TT pairs `(Q_alpha,P_alpha)` with positive frequencies `r_alpha`; all other
gravity directions are the nonzero-mode gauge/constraint pairs. On
`c=X=0` the auxiliary quadratic free Hamiltonian and its first derivatives
vanish. Therefore

```text
(D_S H_f)|_(c=X=0)=0,
W|_(c=X=0)=V_1|_(c=X=0)=sum_alpha Q_alpha tau_alpha,
H_red,0=H_m+sum_alpha(P_alpha^2+r_alpha^2 Q_alpha^2)/2.           (30)
```

Here `tau_alpha` is the real TT projection of the fixed scalar stress, and
`H_m>=0` is the standard finite free matter Hamiltonian (`m^2>=0`). This
reduction does not restore any deleted homogeneous gravity coordinate.

The section `c=X=0` in (30) is the **undressed seed section**. After dressing,
the corresponding section is `X=0, C(g)=0`; there `C(g)=c+gJ`, so the bare
constraint coordinate is `c=-gJ`, not zero. Reduction of the dressed
Hamiltonian means pullback from the seed reduction, not substituting bare
`c=0` into it. This distinction is needed for (34).

**Construction.** With finitely many modes and `r_alpha>0`, choose

```text
L_alpha(g)=Q_alpha+(g/r_alpha^2) tau_alpha,
H_red,+(g)=H_m+sum_alpha[P_alpha^2+r_alpha^2 L_alpha(g)^2]/2.     (31)
```

The precise definition of (31) is by a closed form, not an unproved choice of
self-adjoint domain for a fourth-order differential expression. Each real
`tau_alpha` is a Weyl-quadratic matter operator with a self-adjoint closure,
as in section 9. `Q_alpha` acts on the independent tensor factor, so it
strongly commutes with `tau_alpha`. Joint spectral calculus gives a
self-adjoint `L_alpha(g)`. Different `tau_alpha`, and different `L_alpha`,
need not commute with one another.

On the reduced Hilbert space `L^2(R^(2(n-1))_Q) tensor L^2(R^n_phi)`, define

```text
q_g[psi]=||H_m^(1/2)psi||^2
       +sum_alpha[||P_alpha psi||^2+r_alpha^2||L_alpha(g)psi||^2]/2,
Dom(q_g)=Dom(H_m^(1/2)) intersection
         intersection_alpha (Dom(P_alpha) intersection Dom(L_alpha(g))). (32)
```

This domain is dense because it contains Schwartz space. Every graph norm
in (32) is closed. A sequence Cauchy in `||psi||^2+q_g[psi]` is Cauchy in
each individual graph norm and in the Hilbert norm; the closed operators
therefore have the same Hilbert-space limit, which belongs to the
intersection. Thus the form is closed and nonnegative. The representation
theorem yields a unique nonnegative self-adjoint operator representing this
chosen form, hence unitary physical-time evolution for all real times. The
standard form-to-operator input is stated and proved in
[Sebestyen–Tarcsay, *Basic representation theorems of forms*, Corollary 2.7](https://arxiv.org/html/2505.09588v1).

On the common Schwartz test domain the exact differential expression is

```text
H_red,+(g)=H_red,0+g sum_alpha Q_alpha tau_alpha
                  +(g^2/2)sum_alpha tau_alpha^2/r_alpha^2.     (33)
```

Indeed `Q_alpha` commutes with its matter stress; expanding each square gives
(33) with no discarded ordering correction. Schwartz test functions belong
to each squared-operator domain, so the operator associated with (32) agrees
there with (33). This is exact first-vertex matching on that domain, not a
claim of a coupling-independent full operator domain, analytic perturbation
family, or essential self-adjointness of the formal sum on Schwartz space.

The quartic term has the **specified operator-square ordering**
`tau_alpha^2`, not an unspecified Weyl ordering of the classical quartic
symbol. These can differ by an `hbar^2` scalar. For example, at `hbar=1`,
`D=(up+pu)/2` obeys `D^2=Op_W(u^2 p^2)+I/4`. The checker retains the
`-f/4` term in `D^2 f=-(u^2 f''+2u f'+f/4)`. Positivity of (32) uses the
operator square and does not silently drop that ordering contribution.

Classically choose the gauge-invariant addition

```text
R=(1/2)sum_alpha tau_alpha^2/r_alpha^2,
H_match,+(g)=exp(gD_S)(H_f+gW+g^2R).                           (34)
```

Since `{c_a,R}=0`, the proof of section 7 still gives exact propagation with
the same fixed `A`, and the unreduced first vertex is still `V_1`. Its
reduction is (31). The second vertex in the original coordinates is now
`D_S V_1-D_S^2 H_f/2+R`, an explicitly **chosen additional interaction**,
not a consequence forced by the first Ward identity.

**Limits.** Equations (31)–(34) establish positive self-adjoint dynamics for
this reduced finite-volume completion and exact corresponding classical
constraint propagation. They do not establish a self-adjoint quantization of
the full unreduced `H_match,+` with all off-constraint vertices, nor an
equivalence theorem for a TFPT-derived physical inner product. The inverse
`r_alpha^2` and TT projection are spatially nonlocal; nothing here proves
locality, relativistic causal propagation, a continuum limit, homogeneous
reception, or a unique microscopic origin of `R`. In particular the added
term cannot be advertised as a TFPT prediction.

No ground-state existence, volume-uniform bound, or invariance of Schwartz
space under this interacting evolution is asserted. The unique operator for
the specified form is not a uniqueness theorem for physical completions.

`positive_reduced_hamiltonian.py` verifies the exact operator expansion on
arbitrary smooth functions using two genuinely noncommuting matter stresses,
checks the dilation-ordering terms, exhibits cancellation of the negative
quartic valley, and verifies the free TT splitting algebra on a generic
symbolic TT tensor. The all-mode/domain theorem is the proof above, not a
finite symbolic positivity sample. No finite matrix is used to mimic the CCR.

## 11. Reproduction and evidence boundary

Run from the repository root with a Python environment containing SymPy:

```text
python experiments/theory-contracts/constraint-dressing/checker.py
python experiments/theory-contracts/constraint-dressing/lattice_gauge_chart.py
python experiments/theory-contracts/constraint-dressing/quantum_dressing.py
python experiments/theory-contracts/constraint-dressing/hamiltonian_stabilization.py
python experiments/theory-contracts/constraint-dressing/positive_reduced_hamiltonian.py
```

Observed result:

```text
COUNTS: 38/38 exact checks passed
COUNTS: 12/12 exact real-space chart checks passed
COUNTS: 19/19 exact quantum-dressing checks passed
COUNTS: 19/19 exact Hamiltonian stabilization checks passed
COUNTS: 19/19 exact positive-reduced-Hamiltonian checks passed
VERDICT: ORDER_G2_CANONICAL_CONSTRAINT_CLOSURE_EXACT;
FORMAL_ALL_ORDER_LIE_COMPLETION; INVERSE_DERIVATIVE_LOCALITY_OBSTRUCTION;
NOT_A_LOCAL_GRAVITY_INTERACTION; NON_RH
```

The work was derived against clean TFPT commit
`a21616c41bc9503f5a21ee79c42c4224f6a3d0b0`, matching `origin/main` at the
time of the check.  The prior Round-7 source was
`tex-artefacts/toe_round7_matter_coupling.tex`, the load-bearing regression was
`verification/v1035_matter_coupling.py`, and the full-3D scalar input was the
unpromoted theory contract under
`experiments/theory-contracts/free-scalar-3d/`.

Hard boundaries:

- exact: equal-time order-`g^2` cancellation on every nonzero-mode canonical
  chart satisfying the hypotheses;
- exact formal: all-order first-class completion by one canonical flow;
- exact: paired-real generic Fourier chart and its inverse-derivative poles;
- exact: real-space nonzero-mode chart including self-conjugate lattice modes;
- exact finite quadratic theorem: all-real-`g` unitary dressing, self-adjoint
  strongly commuting constraints and a common invariant core;
- exact classical: matched first-order vertex and all-order constraint
  stabilization, with `V_2=D_S V_1-D_S^2 H_f/2` and fixed propagation matrix;
- exact chosen finite reduced completion: nonnegative self-adjoint quantum
  Hamiltonian from the closed form (32), retaining the first stress vertex;
- exact: full-rank four-current free-scalar Poisson witness;
- not proved: a finite-range/local `K_a` for the specific full lattice current
  algebra;
- not proved: a local microscopic completion, a TFPT derivation of the added
  positive term, or self-adjoint quantization matching all unreduced vertices;
- not proved: a physical interacting-gravity Hilbert space or operator
  realization for arbitrary nonquadratic matter currents;
- not proved: homogeneous-mode reception, nonlinear gravitational interaction,
  Lorentz/Dirac algebra, TOE/T7, infinite-volume or continuum limits, or any
  RH statement.
