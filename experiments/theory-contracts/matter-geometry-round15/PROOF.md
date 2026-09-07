# Round15: exact eight-channel charged-sector and GSO bridge

Date: 2026-09-06. NON-RH, local research construction. Locally integrated research;
no public release, empirical claim, or 3+1D chirality theorem is made here.

## Result and provenance

The frozen D5+A3 charge can be realized in eight, not nine, orthonormal
bosonic current coordinates. An explicit A3=D3 isometry sends it to the
positive Spin(16) spinor weight. The four original glue sectors become the
two NS-even and two Ramond-positive-chirality branches, with an explicit
internal order-four charge. An integral lattice basis supplies a cocycle and
nonzero charged operators on one common charge Hilbert space. This solves
the charge-coordinate and abstract GSO identification, not the microscopic
QWZ spin-field scaling limit.

A separate finite microscopic construction supplies a code-compatible
half-flux transporter on the source QWZ hopping. It changes the prescribed
seam coupling from Z to Z^2 and adds an explicit code projector and endpoint
fermion pair. Its four charged corners are nonzero and its commutator has a
defect on the far endpoint cross-section. It is not identified with the conformal vertex.

The inputs are the literal OMEGA_S, OMEGA_F and LAM coordinates of
`verification/v983_simple_current_generator.py`, the QWZ builder in
`verification/v988_psi_lambda_reduction.py`, and the Round7 charged-disorder
proof. That proof correctly identified the uniform quarter-flux weight
mismatch. Nothing below changes its result for the unchanged uniform Z
hopping. The classical E8/free-fermion construction is not new physics;
the source-specific isometry, grade and finite code map are made explicit.
Primary context: [Goddard--Olive--Schwimmer, The heterotic string and a
fermionic construction of the E8 Kac-Moody algebra](https://doi.org/10.1016/0370-2693(85)90387-9).
All finite arithmetic and operator identities used below are proved here.

## 1. The exact A3 to D3 isometry

For y in R^4 with sum(y)=0, set

    B y = ((y1+y2-y3-y4)/2,
           (y1-y2+y3-y4)/2,
           (y1-y2-y3+y4)/2).

Then B B^T=I_3 and B^T B=I_4-J_4/4. Thus B is an isometry on the
trace-zero plane; its inverse there is B^T. For integral trace-zero y,
By=(y1+y2,y1+y3,y1+y4) is integral with even coordinate sum 2y1.
Conversely for z in Z^3 with even sum, B^T z is integral with zero sum.
Consequently B(A3)=D3 exactly, not just at the level of a root census.

The source omega_f=(3,-1,-1,-1)/4 maps to (1,1,1)/2. Leaving the five
D5 coordinates unchanged gives an isometry U of the rank-eight spaces:

    U(L0)=D5 direct_sum D3,
    U(lambda)=s=(1,1,1,1,1,1,1,1)/2,
    |s|^2/2=1.

No ninth fermion or diagonal-U(1) quotient is needed in this realization.
This is a change of bosonic current coordinates, not an asserted onsite
CAR change of variables in the old QWZ model.

## 2. All four sectors, including the full order-four grade

Write L0'=D5+D3 and L=L0'+Zs. Since 2s=(1,...,1) has odd sums in both
blocks, while an integer D8 vector has either even-even or odd-odd block
sums,

    D8=L0' disjoint_union (L0'+2s),
    L=D8 disjoint_union (D8+s).

The second expression is the positive E8 lattice: all coordinates are
integral or all half-integral, and their total sum is even. The proof is
valid for every lattice vector, not a bounded coordinate search.

For every x in L define

    r(x)=2 sum_(i=1)^5 x_i mod 4.

This is integer valued modulo four, additive, vanishes precisely on L0',
and r(s)=5=1 mod4. Its four fibers are exactly L0'+r s. Define the unitary
internal grade Q|x>=i^r(x)|x>. Then Q^4=1.

The fermionic boundary monodromy of e^(i x.phi) in any of the eight complex
fermions is exp(2 pi i x_j)=(-1)^r(x). Only the parity of r specifies the
spin structure. The full order-four grade is an internal D5-center charge;
it is not the uniform boundary phase i^r. In particular r=0 and r=2 have
the same spin structure, as do r=1 and r=3. This exact distinction is the
reason that the old quarter-flux implementation could not be the frozen
lambda merely by an orthogonal relabeling.

At norm two, the integer roots are ±e_i±e_j. The 40 roots internal to the
first block and 12 internal to the last block have grade zero. The 5*3*4=60
mixed roots have grade two. The 128 half roots are (±1/2)^8 with an even
number of minus signs. If n5 is the number of first-block minus signs,

    r=5-2 n5 mod4.

Even n5 gives grade one and odd n5 grade three. Total even parity forces
matching parity in the last block. There are 16*4=64 roots of each grade.
Thus the source census [52,64,60,64] is recovered with an explicit map of
every root, not merely matching dimensions.

## 3. A genuine GSO projector on the abstract charge sectors

For the NS charge space use integer x and retain even total charge. For the
Ramond charge space write x=n+s with n integral and retain even sum(n).
These are respectively D8 and D8+s. In the Ramond zero-mode Clifford
module of eight complex fermions, use x_j=1/2-n_j with n_j=0,1. The GSO
projector is

    P_R=(1+(-1)^N)/2.

Its rank is 128. On its image the exact grade is

    Q_R=i (-1)^N5,

and the two projectors (1±(-1)^N5)P_R/2 have ranks 64 each. On the NS
charge space Q_NS=(-1)^sum_(i≤5) x_i, giving grades zero and two. In other
words O+S is now a specified direct sum of charge/Fock sectors with a
specified projector, rather than a coefficientwise character sum.

This supplies a chosen abstract fermionic realization of the sourced E8
lattice. It does not identify absolute lattice-site occupation with the
normal-ordered edge charge, nor derive a microscopic GSO constraint from
TFPT dynamics. Those are additional identifications.

## 4. Cocycle and charged corners on one common Hilbert space

An explicit Z-basis of L is

    b1=2e1,  bj=e1+ej (j=2,...,7),  b8=s.

The determinant of its 8 by 8 column matrix is one. Every basis vector is
in L, whose index/covolume computation from L0' gives covolume one, so it
is a full basis. Let G_ij=bi.bj: it is integral with even diagonal. For
p=sum m_i bi and q=sum n_i bi define

    eps(p,q)=(-1)^[sum_i m_i n_i G_ii/2
                       +sum_(i>j) m_i n_j G_ij].

The exponent is integral and bilinear. Hence eps is a normalized
two-cocycle; direct subtraction of its two exponents gives

    eps(p,q)/eps(q,p)=(-1)^(p.q),
    eps(p,p)=(-1)^(|p|^2/2).

On l2(L) define the bounded unitary

    T_p |q> = eps(p,q)|p+q>.

It has a nonzero corner from every grade r to r+r(p), norm one on that
whole corner, and Q T_s Q*=i T_s. Its product is
T_p T_q=eps(p,q)T_(p+q). In particular T_s is not a formal symbol or a
sectorwise operator with zero charged corners.

The Hilbert adjoint is T_p*=eps(p,-p) T_(-p); its cocycle phase is retained,
not silently identified with T_(-p). Tensoring with the eight-boson oscillator
Fock completion gives the explicit diagonal conformal Hamiltonian
L0=|p|^2/2+sum_(j,n>0) n N_(j,n), with its weighted square-summability
domain in the occupation/charge basis. It is positive self-adjoint, with
finite energy multiplicities and an exact all-time diagonal unitary group.
These are statements about the constructed lattice model, not its QWZ limit.

Crucially, simple-current order four is an order in L/L0', not an operator
equation T_s^4=1. Here eps(s,s)=-1 and

    T_s^4=T_(4s) != 1.

The latter returns to the same grade while changing the actual charge.
Equating a finite flux register's fourth power to a vertex's fourth power
would lose precisely this neutral-lattice charge data.

Tensoring with the algebraic eight-boson oscillator Fock space gives the
usual explicit formal vertex

    V_p(z)=exp(sum_(n>0) p.a_-n z^n/n)
           T_p z^(p.a_0)
           exp(-sum_(n>0) p.a_n z^-n/n).

The oscillator commutator produces (z-w)^(p.q); the displayed cocycle
cancels its integer exchange sign. Thus the formal fields of the even
lattice are bosonically local. The leading state coefficient of V_s applied
to the vacuum has energy |s|^2/2=1. This is an algebraic vertex/Fock construction, not an analytic
convergence theorem for unsmeared QWZ operators. No boundedness of V_s(z)
or uniform scaling estimate is inferred from boundedness of T_s.

## 5. A finite QWZ half-flux transporter preserving an explicit code

Let h(k) be the literal source QWZ builder, and use eight identical complex
copies. The following is an explicitly changed microscopic candidate:

    h_r^half = h(k=2r),
    H = sum_r |r><r| tensor dGamma(h_r^half).

The seam coupling is Z^2, not Z. Let A be an arc starting just after the
seam, u_A=-1 on A and +1 outside, and W_A=Gamma(u_A). Then W_A^2=1,
and h_(r+1)^half-u_A h_r^half u_A* is supported only on the opposite
endpoint cross-section: the longitudinal bonds from x=ell to x=ell+1
at every transverse y, in every copy. This follows from the same literal
hopping calculation as Round7. It is not a single pointlike bond in the
two-dimensional cylinder.

Let N5 count all finite-site occupations in the first five copies and N
all occupations. The new code projector is

    P = sum_r |r><r| tensor [(1+(-1)^N)/2
                       * indicator[(-1)^N5=(-1)^floor(r/2)]].

The indicator and parity factors act on the same Fock space and commute. Both
commute with H. This is a declared finite code constraint, not yet the
edge-vacuum GSO projector of Section 3.

Choose one orbital just outside A at the far endpoint in a first-block
copy and one in a last-block copy. Their Majoranas gamma_5 and gamma_3
obey {gamma_5,gamma_3}=0. The local even operator

    F=i gamma_5 gamma_3

is Hermitian unitary, flips (-1)^N5, preserves (-1)^N, and commutes with
W_A because both orbitals are outside A. Set w_r=1 for even r and F for
odd r, and define

    T = sum_r |r+1><r| tensor w_r W_A.

Each w_r W_A is unitary. The parity condition floor(r/2) changes exactly
on the two odd-r steps, where F flips it. Hence T P=P T, every
P_(r+1) P T P P_r corner is nonzero with norm one, T^2=X^2 tensor F,
and T^4=1. Also Z T Z*=iT, while total fermion parity commutes with T.
The bare X W_A fails code preservation on the odd-r steps; the endpoint
pair is necessary for this particular code.

Finally, in each corner the commutator decomposes as

    H_(r+1) w_r W_A - w_r W_A H_r
      = [H_(r+1),w_r] W_A
          +w_r [H_(r+1)-W_A H_r W_A*] W_A.

The second bracket lives on that entire far endpoint cross-section. Because H is finite
range and F is supported at that endpoint, the first bracket lives on
the finite star of its two orbitals. More precisely, the commutator is a
coefficient supported on the far cross-section and the finite star of F,
multiplied by the displayed disorder string;
the entire commutator is not an operator with endpoint-only support after
the string is forgotten. The transporter therefore has an
exact endpoint-cross-section defect; it is not an arbitrary block shift.
This support statement concerns the commutator before applying the global
code projector. No local Gauss-law realization of that global projector
is claimed. At the fixed source width Ny=8 the cross-section has finite
transverse extent. No point-local or width-uniform transverse support bound,
nor locality conclusion in a joint transverse/scaling limit, follows.

## 6. What this does and does not solve

Constructed from exact sourced charge data: the rank-eight isometry, all
four charge sectors, the genuine internal Z4 grade, abstract GSO projector,
an explicit cocycle and nonzero charged charge-lattice operators. Constructed
as a declared microscopic modification: one eight-copy half-flux QWZ
Hamiltonian, invariant finite code and local-defect charged transporter.

Still required for identification with the TFPT seam: derive the changed
Z^2 coupling and code from the same microscopic parent, match finite-site
charge to edge charge, prove a renormalized spin-field scaling limit with
the specified cocycle, and prove that the code-projected microscopic local
algebra exhausts the E8 algebra. The finite T is not T_s or V_s, as its
fourth-power relation already shows. There is no identification with the
separate Round14 gravity/clock model, no 4D anomaly/measure or mirror theorem,
no selected generation count, no neutrino mass texture and no RH claim.

## Reproduction

Run `eight_channel_bridge_check.py --repo /absolute/path/to/tfpt-theoryv4`.
The checker uses exact rational arithmetic for the lattice/cocycle/CAR code,
imports the literal source lambda coordinates and QWZ builder, and keeps
floating source-matrix comparisons separately labelled. Exhausted finite
root/cocycle fixtures are regressions; the all-lattice arguments above are
the proofs. No repository or source file is written by the checker.
