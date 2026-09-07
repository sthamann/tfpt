# Finite reference frames: complete relational algebra and an exact locality boundary

Date: 2026-09-06. Unpromoted non-RH research. The result is a conditional
finite-group construction for the actual chosen reduced Hamiltonian A=H_+.
It neither derives a spatial reference system from TFPT nor supplies its
continuous gravitational momentum constraints.

## 1. What the preceding invariant-sector construction does not provide

Round11 proves that finite lattice translations U_a strongly commute with A,
so Pi_inv=|Gamma|^-1 sum_a U_a defines a consistent invariant sector.
This does **not** make Pi_inv O_X Pi_inv a faithful copy of the original
local observable algebra. Compression is in general not multiplicative.

For example take three spins, cyclic translation and its invariant projector
Pi. Operators X_0 and Z_1 on different sites commute before compression, but

    [Pi X_0 Pi, Pi Z_1 Pi]
       = -(2i/9) Pi (Y_0+Y_1+Y_2) Pi != 0.               (1)

Within the invariant sector every compressed X_j equals the compressed
average of the three X operators, and similarly for Z. Equation (1) is a
finite tensor-algebra counterexample, not a finite-matrix approximation to
bosonic canonical commutators or a simulation of H_+.

There is also a general exact support statement. On the finite scalar site
tensor product, a bounded scalar operator supported in a proper subset X
and invariant under every transitive lattice translation must be scalar.
Indeed for each site j choose a translation a with j outside aX. Invariance
places O in the algebra supported on aX, so it commutes with every bounded
operator at j. The site algebras generate the full tensor-product algebra;
its commutant is scalar. This statement is about strictly supported scalar
operators which are themselves invariant, not every operator that might
preserve a chosen subspace or involve TT variables.

## 2. An explicit reference system repairs the algebraic identification

Let Gamma be a finite group, N=|Gamma|, and U its genuine unitary representation
on the system Hilbert space H. For TFPT's specified regulator Gamma is the
finite periodic translation group, acting by coordinate pullbacks, not by
the failed centered-difference infinitesimal generator. Add the ideal reference
space H_R=l^2(Gamma), with orthonormal |a> and left regular action
L_b|a>=|ba>. Impose invariance under W_b=L_b tensor U_b.

Define the isometry V:H -> H_R tensor H by

    V psi = N^(-1/2) sum_a |a> tensor U_a psi.             (2)

Its range is exactly the invariant subspace. Directly,

    V^*V=I, W_b V=V,
    VV^* = N^-1 sum_b W_b =: Pi_diag.                    (3)

For the last equality the (a,c) block of each side is N^-1 U_(ac^-1).
In particular the physical space with a reference is isomorphic to the
**whole** H, not merely the smaller invariant sector H_inv of the original
system alone. For an abelian group the reference supplies the opposite
character to each system character. This is finite quasimomentum compensation,
not an identified physical gravitational momentum receiver.

For any bounded system operator O define

    Rel(O) = sum_a |a><a| tensor U_a O U_a^*.              (4)

Then Rel is unital, norm preserving and a *-homomorphism:

    Rel(O_1 O_2)=Rel(O_1)Rel(O_2),
    W_b Rel(O) W_b^*=Rel(O),
    Rel(O)V=VO, V^*Rel(O)V=O.                            (5)

Consequently the algebras Rel(A_X), restricted to ran(V), reproduce the
original subsystem algebras, including their products and equal-time
commutation. Every bounded operator on ran(V) has such a representative.
On the **full kinematical space**, however, Rel(B(H)) need not be the whole
invariant operator algebra; additional regular-representation sectors exist.
The claim of surjectivity is only after restriction to ran(V).

The reference has N mutually orthogonal coordinate states. N is both the
dimension used and a necessary dimension for this particular perfect sharp
frame with N perfectly distinguishable positions. No dimension lower bound
for every imperfect reference model or implementation complexity claim is made.

## 3. States, readouts and conditional clock

For any trace-class system state rho, rho_phys=V rho V^* is invariant and

    tr(rho_phys Rel(O))=tr(rho O).                        (6)

The reference has uniform diagonal position probability 1/N, yet the joint
state retains all relational information. At the level of a pure state,
projection onto any |a> followed by U_a^* recovers psi after normalization.
This is a mathematical conditional-state statement, not a gauge-invariant
operation selecting an absolute coordinate.

Assume A is self-adjoint, bounded below, and strongly commutes with each U_a,
as proved for the chosen H_+. The operator I_R tensor A is self-adjoint on
the finite direct sum of D(A), commutes with every W_a, and obeys

    (I_R tensor A)V=VA,
    exp(-it(I_R tensor A))V=V exp(-itA).                 (7)

Its restriction to ran(V) is therefore the unique transported A with domain
V D(A). This solves the reference-extended finite dynamics with a specified
physical Hilbert space, not the unreduced original gravity/auxiliary operator.

If A>=epsilon>0, the postulated clock C=A-P_Q^2/12 of Round11 can be added.
The finite diagonal group average and its convergent clock averaging commute.
The physical completion is H, with the same shell weight 6/sqrt(12E) and
positive clock generator sqrt(12A). It is not H_inv: the reference has allowed
all original finite translation characters. The global clock constraint,
energy zero and time orientation remain extra assumptions.

## 4. Exact dynamics of the relational local net

Because U_a commutes with A, (4) gives the strong bounded-operator identity

    exp(it(I_R tensor A)) Rel(O) exp(-it(I_R tensor A))
                    = Rel(exp(itA) O exp(-itA)).          (8)

Thus every bounded commutator, its norm, every state expectation and every
well-defined weak time derivative are preserved when both the Hamiltonian
and the observable net are transported. In particular

    V^* [Rel(O_X,t),Rel(O_Y)] V = [O_X(t),O_Y].           (9)

Apply this to the bounded scalar Weyl translations in
`../reduced-locality-round11/PROOF.md`. Their nonzero first-time-order remote
response is unchanged. Adding a nondynamical perfect reference **does not
cancel it**. It makes the local-algebra identification explicit, precisely
so that an unchanged response cannot be mistaken for a locality repair.

This remains conditional on assigning these relational operations the same
physical locality labels. They are globally controlled operators on the
unconstrained reference/system description, and they share one reference.
An implementation using genuinely local rods, signals and measurements would
be an additional dynamical construction whose operations must be specified.

## 5. A finite reference kinetic energy is exactly tractable

Allow any self-adjoint H_R on l^2(Gamma) which commutes with the left regular
action, and use the noninteracting extension

    H_ext = H_R tensor I + I_R tensor A.                 (10)

H_R is bounded because the reference is finite. Put h_ab=<a|H_R|b>.
Left invariance gives h_ab=h_(e,a^-1 b), and compression gives

    B=V^*(H_R tensor I)V = sum_c h_(e,c) U_c,
    H_phys=A+B on D(A).                                 (11)

B is bounded self-adjoint, commutes strongly with A and is positive if H_R
is positive. For a lattice reference graph Laplacian this is, for example,

    B=kappa sum_j (2I-U_(e_j)-U_(-e_j)), kappa>=0.        (12)

This is an explicit finite quasimomentum-dependent energy, not the old local
momentum density. Each U translates the entire configuration. The bounded
perturbation theorem supplies self-adjointness of A+B on the same domain;
if B>=0 the old lower bound epsilon survives. The clock construction then
uses A+B. This choice changes the physical Hamiltonian and its energy data.

## 6. No bounded reference-only energy can erase the actual remote vertex

There is a sharper statement for (10), even allowing arbitrary finite H_R.
On the strict cubic 6^3 witness let X=(0,0,0), Y=(0,0,3), and
phi_0(x)=f(x_1 mod 3), f=(1,-1,0). Round11 establishes

    h_XY := partial_X partial_Y R(phi_0)
          = -1762469675117/170400029184000 != 0.          (13)

Stress is quadratic and its mixed derivative sigma_XY vanishes identically
at this separation. R is homogeneous quartic. For nonzero Weyl displacements
a,b the polynomial

    Delta_Y^b Delta_X^a V_g(t phi_0)

has leading coefficient g^2 a b h_XY t^2; its remaining powers in t are at
most one. The local matter term and q-sigma term have zero mixed finite
difference here. For fixed g,a,b all nonzero, the resulting multiplication
operator is unbounded. Its product with a Weyl unitary is still unbounded
on the Schwartz domain. Normalized compactly supported smooth packets moved
along t phi_0 exhibit this growth and have finite energy at each finite t.
Their energies are not uniformly bounded as t grows. No additional no-go
restricted to a fixed low-energy state set is inferred from this argument.

By contrast any bounded B satisfies

    ||[[B,T_X(a)],T_Y(b)]|| <= 4 ||B||.                  (14)

Therefore adding (11) cannot make the complete remote double commutator
vanish on all states. This excludes a cancellation by **reference-only
finite kinetic energy in this specified additive extension**, not by every
possible dynamical reference or interaction. Field-dependent reference
couplings, infinite-dimensional physical reference fields, and different
local operation assignments are outside this theorem.

## 7. Context and exact regressions

Finite regular-representation references and relational quantities are a
standard framework, not a new derivation of quantum gravity. Primary context:
[de la Hamette and Galley, Quantum reference frames for general symmetry groups](https://arxiv.org/abs/2004.14292)
and [Krumm, Hoehn and Mueller, Quantum reference frame transformations as symmetries](https://arxiv.org/abs/2011.01951).
Equations (2)-(14) are proved directly here for the present conditional model.

`reference_frame_checker.py` checks a full finite cyclic frame construction,
its physical-space identification, products, commutators, state readout,
dynamics and reference kinetic energy, plus the nonmultiplicative-compression
counterexample. It also recomputes the actual cubic scalar witness and its
quartic scaling from the Round11 source implementation. The finite spin
example checks group/algebra identities; it is not claimed to model the
scalar field, a continuum limit, or empirical physics.

Independent review checked the full proof, particularly the possibly
nonabelian compression in (11) and the precise all-state scope of (14),
and reran all 35 exact check groups successfully.
