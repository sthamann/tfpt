# Round21: the exact boundary of an additive charge momentum repair

2026-09-07. NON-RH. This is a new obstruction for the moving E8 charge
model, distinct from Round12's gravity resonance obstruction. It excludes
a stated class of repairs, NOT every mixed scalar/charge/gravity momentum.

## 1. The scalar total momentum and its actual force

Use the actual free-scalar Ward stencil and the input Hamiltonian

    H_sc=H_m+D(n)+(lambda/N)sum_x e(n_x)phi_x^2+L_J,
    P_m,i=sum_x j_m,i(x)=-sum_x pi_x D_i^c phi_x,
    D_i^c phi_x=(phi_(x+ei)-phi_(x-ei))/(2a).

Fields in the last product are at distinct sites, or cancel at L=2, so
the displayed ordering agrees with Weyl ordering. At finite periodic
volume the divergence of EVERY periodic stress stencil sums to zero.
Round20's local scalar force therefore gives

    i[H_sc,P_m,i]=F_i(n,phi),
    F_i=-sum_x (u_(x+ei)-u_x)phi_x phi_(x+ei)/(2a),
    u_x=2lambda e(n_x)/N.                               (1)

L_J and D commute with P_m. This formula is an exact operator polynomial
on finite-charge scalar-Schwartz vectors, not a frozen-charge dynamical
approximation. For L>=3 and lambda>0 it is nonzero: choose n_0=p with
e(p)=1, all other charges zero, phi_0=phi_ei=t, all other phi zero. Then

    F_i=lambda t^2/(Na).                               (2)

This is a polynomial evaluation witness, not a normalizable position
eigenstate. A nonzero multiplication polynomial acts nontrivially on
Schwartz vectors. The witness also exists in EVERY fixed total-charge
sector Q: put the compensating charge Q-p at a third site where phi=0.
In particular the neutral sector does not evade the obstruction.
At L=2, P_m=0 and the two opposite edge occurrences
cancel in the total force, so this particular obstruction does NOT apply.
A uniform energy profile also removes (1) at that instant, but hopping
does not in general preserve the uniform-profile subspace.

## 2. No charge-only momentum can cancel this force, at any J

Suppose P=P_m+P_c, where P_c acts only on the charge factor. P_c may be
nonlocal, depend on lambda,J, and have arbitrary charge matrix elements;
it need not be a polynomial or a short-range hopping sum. Assume its
products with H_sc are defined on a common core containing the charge
basis tensored with scalar Schwartz vectors. This regularity assumption
is essential; singular domain constructions are not covered.

Taking the (n,n) charge matrix element of i[H_sc,P] gives

    <n|i[H_sc,P]|n>=F_i(n,phi)+i[L_J,P_c]_(n,n) I_scalar. (3)

Indeed [D,P_c]_(n,n)=0, [V,P_c]_(n,n)=0 and [H_m,P_c]=0.
The last term in (3) is independent of phi and pi, whereas (2) is a
nonconstant quadratic. No value of that scalar can cancel (2) as an
operator. Thus there is NO conserved P of this additive form for the
full independent-site charge Hilbert space, L>=3, lambda>0, at ANY finite
J>=0 and ANY diagonal D. This is not a failed finite ansatz search.

It also applies if P_c acts on independent spectator factors and their
Hamiltonian is scalar-independent: the extra diagonal commutator is then
an operator on those factors, still independent of scalar fields. It does
NOT apply to a correction containing scalar operators, to the full
interacting gravitational B, or to a weak constraint-surface identity.
It does NOT assert the absence of every conserved operator (H itself is
conserved). A regular completion of the full theory whose scalar/charge
decoupling limit has this additive form would nevertheless fail this
necessary test in that limit.

A stress-only repair retaining P_m has the same problem: the integral
of its added periodic divergence is zero and cannot remove (1). Simply
calling a charge energy current a momentum current does not change (3).

## 3. Why a literal infinitesimal translation of integer occupations fails

There is a second elementary, independent boundary. For a charge-diagonal
observable A_x (n_x^a or e(n_x)) and an operator K with all required basis
matrix elements and products defined,

    <n|i[K,A_x]|n>=0.                                   (4)

But the diagonal matrix element of D_i^c A_x can be nonzero. Therefore
i[K,A_x]=D_i^c A_x cannot hold on that basis core. Giving integer occupation
operators the literal continuum infinitesimal translation law is already
incompatible with their pure-point representation. This does not forbid
charge transport: its correct time derivative from Round20 is an
OFF-DIAGONAL hopping current, not a diagonal spatial finite difference.

More generally, a strongly continuous one-parameter unitary group that
normalizes the full atomic diagonal charge algebra cannot continuously
permute its minimal projections. The image of each rank-one projection
must be another such projection. Near t=0, strong continuity tested on
its basis vector forces that projection to stay fixed (the alternatives
are orthogonal); the group law and connectedness then fix it for all t.
Hence the induced automorphism on this diagonal algebra is trivial.
This statement concerns the charge factor, not an assumed atomic algebra
of all continuous gravitational and scalar variables.

## 4. The symmetry that DOES survive, and the available escape

Simultaneously permuting all lattice fields and charges by one site is an
exact finite cyclic symmetry of the source-free uniform-coefficient
parent. D,V and the positive-edge inventory permute into themselves;
the cocycle is identical at every site. No charge profile is frozen under
this transformation. The full uniform source-free B is also translation
covariant. There is consequently an exact crystal-momentum label.

For a translation unitary T with T^L=I, its spectral projectors and one
bounded logarithm are

    Pi_k=(1/L)sum_(r=0)^(L-1) exp(-2pi i kr/L) T^r,
    P_cr=(1/a)sum_k theta_k Pi_k,
    theta_k=principal representative of 2pi k/L,
    T=exp(i a P_cr),   ||P_cr||<=pi/a.                  (5)

Strong commutation of T with the Hamiltonian gives that of P_cr. This is
not the old centered P_m plus a charge-only term. Fractional translations
generated by this logarithm need not normalize the occupation algebra;
indeed they cannot do so nontrivially by section 3. Formula (5) uses global
translations and does not furnish a local infinitesimal action, local
stress tensor, additive unwrapped continuum momentum or Lorentz symmetry.
Even the Nyquist branch choice is an input, not an extra physical result.

Thus a genuine next solution must either construct a MIXED momentum with
a different action on the occupation algebra, or change the carrier,
interaction/product, or continuum limit and prove the new properties.
Neither changing a name nor unitary dressing of the failed commutator
does this. This is consistent with, but not deduced from, the distinct
lattice Leibniz obstruction studied by
[Kato, Sakamoto and So](https://arxiv.org/abs/0803.3121v3).
Their locality/product hypotheses are not imported as a universal no-go
for TFPT. The independent proof here is (1)–(4).

## 5. Evidence and costs

The checker hashes and imports the actual Ward source, derives all three
local force components, the full L=3 periodic total momentum and its
nonzero E8 witness, and treats the L=2 cancellation separately. Exact
symbolic charge-block tests illustrate the universal matrix-element
proof without mistaking a finite matrix test for that proof. Finite
cyclic translation/projector tests are separate from momentum closure.
No numerical parameter fitting, cut-off charge Hilbert space or empirical
data are used. This narrows the missing stress construction; no T1–T8,
TOE, RH or experimental status is promoted.

## 6. Stronger result: a resonant obstruction to ANY regular first correction

There is also an obstruction beyond the charge-only ansatz, with different
hypotheses. Set J=0 and decouple gravity, at L=3, a=1, N=27, m>0. Write
H(lambda)=H_0+lambda V_1, H_0=H_m+D and
V_1=N^(-1)sum_x e(n_x)phi_x^2. Suppose a time-independent conserved family

    P(lambda)=P_0+lambda P_1+o(lambda),
    P_0=P_m,1+P_c,0,

is differentiable in the relevant commutator matrix elements on a common
core containing finite-charge oscillator eigenvectors. P_c,0 is charge-only
and commutes with D. P_1 may be ANY mixed operator with these matrix
elements, not merely a polynomial, quadratic, diagonal or local correction.
At first order conservation requires

    i[H_0,P_1]=-i[V_1,P_0].                              (6)

Fix n_0=p, e(p)=1, and all other charges zero. The actual cubic Laplacian
has orthonormal real modes

    C_x=sqrt(2/N) cos(2pi x_1/3),
    S_x=sqrt(2/N) sin(2pi x_1/3),
    omega=sqrt(m^2+3),  d=sin(2pi/3)=sqrt(3)/2.

They share the same frequency; all other scalar oscillators are in their
vacuum. Let |C> and |S> excite respectively one C or S quantum, with the
SAME fixed charge configuration. Both are genuine eigenvectors of H_0
at energy E_vac+omega+D(n). Therefore the |C>,|S> matrix element of the
left side of (6) is ZERO for every allowed P_1, including one mixing
charge configurations or independent spectator eigenstates.

The right side is not zero. P_m restricted to these two states is
d[[0,-i],[i,0]]. Since C_0=sqrt(2/N), S_0=0, the two diagonal matrix
elements of V_1 differ by 2/(N^2 omega). All other-mode vacuum terms are
equal and cancel; cross terms leave the selected subspace. P_m itself
preserves that subspace, so no missing intermediate states enter its
commutator. Also <n|[V_1,P_c,0]|n>=0. Consequently

    <C|i[V_1,P_0]|S>=2d/(N^2 omega)
       =sqrt(3)/(729 sqrt(m^2+3)) != 0.                 (7)

Independently the force polynomial (1), restricted to the C,S modes and
divided by lambda, is 4d Q_C Q_S/N^2. The exact oscillator matrix element
<1,0|Q_C Q_S|0,1>=1/(2omega) gives the SAME result (7).
The checker applies the untruncated oscillator creation/annihilation
rules, including intermediate states outside the selected two states.
It does not substitute a two-state truncated canonical commutator.

For an arbitrary total-charge sector Q, put Q-p at r=(0,1,0).
This site has the same C,S phase as 0; the coefficient in (7) is multiplied
by 1+e(Q-p)>0. The neutral choice has multiplier 2. Thus superselection
of total charge does not remove this resonant obstruction either.

Equation (7) rules out every such regular first-order deformation of
the stated seed at J=0, even with mixed P_1. In particular it rules out a
family jointly regular down to J=lambda=0 with that free limit. It does
NOT prove that no mixed momentum exists at a fixed nonzero J, that no
different zeroth-order generator works, or that a singular/nonperturbative
branch, changed interaction, full dynamical gravity or continuum limit
is impossible. Those are genuine alternative research targets, not
solutions supplied by this obstruction. The L=3 quantum resonance and
lambda coupling here are distinct from Round12's classical L=6,
order-g^2 scalar–TT resonance; neither result is silently substituted
for the other.
