# Honest simultaneous clock and inversion action

Date: 2026-09-06. Exact boundary geometry only; no TOE or RH claim.

## Result

The rank-four orbit bundle V does admit the full simultaneous action of
G=<r,s>=C4 x C2. There are exactly two isomorphism classes of such
linearizations on the fixed underlying holomorphic bundle. They arise from
the two descents of L_P through a specific free degree-two isogeny. Both
have determinant character (r,s)=(-1,+1), both fail ordinary coarse
Kummer descent, and neither changes the degree-zero line obstruction found
in Round10. The construction and phase relations are explicit below.

## 1. The group and the stabilizer of the line class

On E=C/(Z+iZ), let r(z)=iz+T, s(z)=-z, T=2P, with iT != T. Put
D=T+iT=(1+i)/2 modulo the lattice, and h(z)=z+D. Then

    r^4=s^2=h^2=1,   rs=sr,   h=r^2 s.

The nonzero translation h has no fixed point. G is the direct product of
<r> and K=<h>. The derivative character is chi(r)=i, chi(s)=-1,
chi(h)=1. Pullback on degree-zero lines is inverse derivative, so the
stabilizer of L_P=O(P-O) inside G is exactly K. Its orbit is
L_P,L_(-iP),L_(-P),L_(iP).

The original line remains non-linearizable under r and s individually;
induction changes the bundle, not that conclusion.

## 2. Actual induction, including the cocycle

Translation acts trivially on Pic^0(E), so h^*L_P is isomorphic to L_P.
Choose any isomorphism. Its square is a nonzero constant because E is
connected and proper. Rescaling by a square root makes the square identity.
There are exactly two inequivalent choices, differing by the sign character
of K. Equivalently they are the two lines M_+,M_- on E'=E/K with
q^*M_± isomorphic to L_P, where q:E->E' is the free degree-two quotient.

Given either K-linearization phi, define

    V=direct_sum_(j=0)^3 (r^j)^*L_P.

Use the canonical cyclic pullback identification for the r-action U. For
h use the pulled-back isomorphism (r^j)^*phi on the jth summand. Naturality
of pullback and commutativity of r and h give UH=HU. Coherence gives
U^4=H^2=1. Therefore

    S_action=U^2 H

obeys S_action^2=1, commutes with U, and covers s=r^2h. This is an honest
G-linearization, not a projective representation. In particular setting
S_action=U^2 would cover the wrong base map, because r^2 != s.

The descent principle for a line and its chosen lifts is described in
[Mumford, Section 1, pp. 290-291](https://pazuki.perso.math.cnrs.fr/index_fichiers/Mumford66.pdf).
For finite-group equivariant line bundles and character choices see
[Galkin--Shinder, Section 2.1](https://arxiv.org/pdf/1210.3339).
The direct pullback argument above proves the needed special case without
assuming a general obstruction class vanishes.

## 3. Exact flat lift, showing why bare signs are insufficient

Use holonomy coordinates p=(a,b)/4 with

    f(z+1)=i^a f(z),   f(z+i)=i^b f(z).

The divisor point convention is P=(b-ia)/4, up to simultaneous inversion.
Successful points have a,b of opposite parity, and D=(1+i)/2 in all cases.
Let zeta8=exp(pi i/4). Extending the holonomy character from the lattice
Lambda to Lambda'=Lambda+ZD requires

    c0=rho'(D),   c0^2=rho(1+i)=i^(a+b).

Hence c0=epsilon*zeta8^(a+b), epsilon=±1. These are primitive eighth roots
because a+b is odd. Both descended lines M_± have exact order eight:
their holonomy at D has order eight and all holonomies have order dividing
eight. They differ by the unique nontrivial line in ker(q^*:Pic^0(E')->Pic^0(E)).
As a complex torus E' is again square; after scaling its lattice, q is the
degree-two isogeny [1-i]. None of this supplies a preferred epsilon.

Let R(x,y)=(-y,x), p_j=(R^T)^j p, and use integer representatives
p_j=(a_j,b_j) without reducing them modulo four. Define

    c_(j+1)=c_j i^(-a_j),
    (H_j f)(z)=c_j^(-1) f(z+D).

Then c_j^2=i^(a_j+b_j), c_4=c_0, and H_j^2=1. The needed cross-relation
is nontrivial on the universal cover: RD-D=(-1,0). Thus

    f(Rz+RD+T)=i^(-a_j) f(Rz+D+T),

and exactly the recursion for c_j gives H_(j+1) U_j=U_j H_j. This explicitly
cancels the otherwise present projective commutator. The naive choice
c_j=1 fails H_j^2=1 because rho_j(1+i)=±i.

## 4. Classification of the two choices

The four underlying line summands are pairwise nonisomorphic, and their
cross-Hom spaces vanish. Every bundle automorphism is therefore diagonal
with constant nonzero entries. Every r-linearization of V can be brought
to the canonical cycle by such a diagonal change. Once this is done, the
commutation relation with r forces all four residual h-normalization
ratios to be equal. Squaring h makes that common ratio ±1. The two signs
cannot be conjugated into one another by a remaining diagonal
r-equivariant automorphism, which is scalar on all four summands.
Thus there are exactly two G-linearizations up to isomorphism.

Write a G-character as gamma(r)=i^k, gamma(s)=(-1)^ell. Its restriction to
K is gamma(h)=(-1)^(k+ell). Character twists with k+ell even preserve the
linearization isomorphism class; those with k+ell odd exchange the two.
There are four characters of each kind. This also explains why the
derivative-character twist, (k,ell)=(1,1), does not pick a new matter bundle.

## 5. Determinant and orientation, with both generators

The ordinary determinant of V is O_E since its four Picard classes sum to
zero. At either r-fixed point the action cyclically permutes its four line
fibres. Its determinant is -1. At each s-fixed point inversion exchanges
the classes j and j+2; there are two weighted two-cycles. Each has
determinant -1 because s^2=1, so the total determinant is +1. Therefore

    det(V):  r -> -1,  s -> +1,  h -> +1,
    det(V) is equivariantly isomorphic to K_E^2.

These characters are independent of epsilon. A common character twist
of the rank-four V multiplies its determinant by gamma^4=1 and does not
alter them. The canonical-form character remains chi=(i,-1). The
coefficient line C_(chi^(-1)) supplies the genuine simultaneous twisted
orientation dz tensor e. In contrast no integer power of det(V) cancels
chi, since all such powers have r-character ±1.

This is an ordinary bundle determinant; it does not equal an analytic
fermion determinant over a configuration family. The four lines are
acyclic, so det RΓ(E,V) is canonically the determinant of a zero complex.

## 6. Exact descent boundary

V descends through the free quotient by K as a bundle on E'; this is
ordinary effective descent. The residual C4 action is retained. V also
defines a bundle on [E/G] and on the Kummer stack [E/<s>].

It does not descend as an ordinary vector bundle to the coarse Kummer
P1: at every inversion fixed point the stabilizer weights are +1,+1,-1,-1.
Either epsilon and any common character twist preserve that multiset.
Likewise at an order-four fixed point the weights of the corresponding
generator are all four fourth roots, so ordinary coarse descent through
the full group is impossible. The full quotient has orbifold signature
(4,4,2). The order-four fixed points form two size-two G-orbits; the four
inversion fixed points form one size-four G-orbit.

The relevant exact criterion is trivial stabilizer action on fibres:
[Alper, Theorem 10.3](https://www.numdam.org/item/10.5802/aif.2833.pdf).
Keeping stack/orbifold data is a concrete condition on this construction.

## 7. Joint-character refinement of the specified flat operator

This subsection refines, and does not contradict, Round10's equality of the
four r-character spectra. On a Fourier orbit seeded by
w0=4(n,m)+(a,b), the preceding formulas give

    H=eta I,   eta=epsilon*(-1)^(n+m).

Hence the full G-character with r-eigenvalue i^k and s-eigenvalue sigma
occurs precisely when eta=sigma*(-1)^k. Within a fixed K-character the
four r-sectors are still unitarily isospectral. The two K-characters split
the momentum lattice by the parity of n+m.

For p=(1,0), the squared-frequency minima for even and odd n+m are
1/16 and 9/16. Thus the gaps of the chosen flat Laplacian are pi^2/(4A)
and 9*pi^2/(4A). The second value follows directly: even parity allows
(n,m)=(0,0), whereas odd parity is minimized by (-1,0).

For p=(1,2), both parity classes have minimum 5/16, and the map
(n,m)->(n,-m-1) preserves the exact norm while reversing parity. It proves
that the two parity-restricted spectra, including all multiplicities, are
identical. Epsilon only exchanges the K-character labels.

These are choices of sector and a specific flat boundary operator. No
chirality, particle masses, physical projections or TFPT selection follows
from this arithmetic. The rank-four block construction has no holomorphic
zero modes and retains the determinant-line/connection gaps already stated.

## Reproduction

Run test_joint_equivariance.py with Python and SymPy. It exhausts finite
torsion/group data, checks lift/cocycle recursions, matrices for both choices
and several complete Fourier orbits, and includes wrong-lift controls. The
all-mode and geometric statements rest on the proofs above, not on finite
spectral samples. No repository files are imported or written by the checker.
