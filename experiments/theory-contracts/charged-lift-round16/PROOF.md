# Round16: full neutral-charge lift of the charged seam transporter

Date: 2026-09-06. NON-RH. This constructs an exact unitary equivalence of
charge-shift representations, including the full neutral lattice and its
frozen cocycle. A declared extension of the finite code transporter realizes
that representation with finite-code multiplicity. The added infinite charge
degrees of freedom and their energy are explicit; no microscopic TFPT
selection, spin-field scaling limit, 4D chirality or TOE completion follows.

## 1. Source and outcome

Use precisely the lattice L, neutral sublattice L0', spinor s, ordered basis,
cocycle and finite code transporter of the integrated
[Round15 proof](../matter-geometry-round15/PROOF.md). In particular

    L0'=D5+D3, L=L0'+Zs, s=(1/2)^8,
    b1=2e1, bi=e1+ei (2<=i<=7), b8=s,
    T_p |x>=eps(p,x)|p+x>, T_s^4=T_(4s)!=I.

The finite code transporter T_fin instead obeyed T_fin^4=I. One integer
carry repairs this mismatch on each s-orbit. Seven additional integer
labels retain the whole neutral lattice rather than only one orbit.
The construction below gives an explicit unitary, not an arbitrary
identification of countable-dimensional Hilbert spaces:

    l2(Z^7) tensor l2(Z) tensor C^4  ~=  l2(L),
    carry shift  <->  T_s,
    fourth power <-> T_(4s).

The full cocycle-translated action of every T_p is specified as well.

## 2. Exact splitting of the whole neutral lattice

Define the integer-valued functional on L

    j(x)=4 sum_(i=6)^8 x_i-2 sum_(i=1)^5 x_i.             (1)

For integer E8 vectors it is integral, and for half-integer E8 vectors it
is also integral. It satisfies j(s)=1. Moreover the difference between
j(x) and the old integer grade representative 2 sum_(i<=5)x_i is
4[sum_(i>=6)x_i-sum_(i<=5)x_i], a multiple of four in either case.
Thus j mod4 is exactly the Round15 grade, and

    L0'={x in L: j(x)=0 mod4}.

Let a_i=j(b_i), i=1,...,7. Their exact values are

    a=(-4,-4,-4,-4,-4,2,2),
    k_i=b_i-a_i s, K=ker(j:L->Z).                       (2)

The columns (k1,...,k7,s) are obtained from the old lattice basis by an
integral triangular change of determinant one. Since j(k_i)=0 and j(s)=1,
they prove the exact internal direct sums

    L=K direct_sum Zs,  K=direct_sum_(i=1)^7 Z k_i,
    L0'=K direct_sum Z(4s).                             (3)

In particular 4s is primitive in L0'. Every x has a unique representation

    x=K u+(4m+r)s, u in Z^7, m in Z, r in {0,1,2,3}.   (4)

Here K u means sum_i u_i k_i. Euclidean division with remainder 0<=r<4
is used also for negative j. Formula (3), not a dimension count, ensures
that no neutral charges have been discarded. The chosen complement K is
an explicit arithmetic coordinate choice, not a canonically selected
microscopic subsystem.

## 3. The frozen cocycle is removed from the one-step carry, not deleted

Let G_ij=bi.bj and retain the Round15 cocycle

    eps(p,x)=(-1)^[sum_i n_i(p)n_i(x)G_ii/2
                     +sum_(i>h) n_i(p)n_h(x)G_ih],      (5)

where n are coordinates in the old ordered b-basis. For x=K u+j s these
coordinates are (u1,...,u7,j-a.u). Since all a_i are even and G_8i=1,

    eps(s,x)=(-1)^(j+U), U=sum_i u_i.                   (6)

Define the real unit phase for every integer j, including negative j,

    d(u,j)=(-1)^[j(j-1)/2+j U].                         (7)

It obeys d(u,j+1)=eps(s,x)d(u,j) and d(u,j+4)=d(u,j).
Consequently the map

    Phi |u,m,r> = d(u,4m+r)|K u+(4m+r)s>               (8)

is a unitary onto l2(L): its basis map is bijective by (4) and its phases
have unit modulus. On the covering coordinates define

    C|u,m,r> = |u,m,r+1>        if r<3,
              |u,m+1,0>        if r=3.                 (9)

It is a bilateral permutation unitary and exactly

    Phi C Phi*=T_s, C^4=W_m, Phi W_m Phi*=T_(4s).       (10)

The adjoint decrements r and carries m downward on r=0. There is no cyclic
boundary condition on m. Replacing m by a finite periodic register would
give C^(4N)=I, which contradicts the translation T_(4Ns) on l2(L).

The cocycle has not disappeared from other neutral directions. For v,u in
Z^7 put

    B_K(v,u)=sum_(i=2)^7 v_i u_i
                  +sum_(2<=h<i<=7) v_i u_h mod2,
    V=sum_i v_i.

Since eps(Kv,h s)=1 for every integer h and
T_(h s)=(-1)^[h(h-1)/2] T_s^h, the complete transported representation is

    Phi* T_(Kv+h s) Phi |u,j>
      =(-1)^[h(h-1)/2+B_K(v,u)+(j+h)V]
           |u+v,j+h>.                                (11)

The j shorthand here is equivalent to the carry coordinates (m,r).
Formula (11) determines every neutral and charged lattice shift, including
its phase. In particular the neutral k_i shifts anticommute with C because
k_i.s is odd; deleting the jV factor gives a false representation. The
product and adjoint relations are inherited exactly from the frozen (5),
not replaced by commuting plain translations in all eight directions.

## 4. Lifting the actual finite code transporter

Retain the Round15 finite Fock space, projectors P_r, code P, half-flux
Hamiltonians H_r, arc sign W_A, endpoint pair F, and

    T_fin=sum_r |r+1><r| tensor w_r W_A,
    w_r=I (r even), F (r odd),
    F^2=W_A^2=I, [F,W_A]=0, T_fin^4=I.                 (12)

Let H_r^code be the code fiber in sector r; it has the same positive finite
dimension for all four r. Adjoin an honest l2(Z) winding register and define

    T_lift=sum_r W_m^[r=3] tensor |r+1><r|
                                    tensor w_r W_A.    (13)

This is unitary, preserves the code, has dual grade one, and

    T_lift^4=W_m tensor I.                            (14)

The winding increment does not alter the endpoint-pair or code conditions.
Every projected charged corner is still a unitary between nonzero fibers.

There is a concrete trivialization of those fibers. Set H_0=H_0^code and

    V_r=F^floor(r/2) W_A^(r mod2): H_0 -> H_r^code,
    J|m,r,v>=|m,r,V_r v>.

The parity properties of F and W_A prove that V_r maps the code fibers
onto one another. Direct substitution gives J* T_lift J=C tensor I_H0,
where C now acts only on (m,r). This includes the closing r=3 step, since
V_4=I, so there is no hidden finite-cycle holonomy.

Finally adjoin l2(Z^7), and define

    Omega=(Phi tensor I_H0)(I_(Z^7) tensor J*) .        (15)

This explicit unitary has target l2(L) tensor H_0 and satisfies

    Omega (I_(Z^7) tensor T_lift) Omega*=T_s tensor I_H0.

Conjugating (11) supplies the full lattice translation representation on
the extended microscopic code space, not merely its four grades. However
the new neutral translations are declared operators on the added charge
registers; they are not claimed to be operators generated by the original
QWZ local CAR algebra. The surviving multiplicity H_0 is explicit and is
not collapsed or identified with a preferred TFPT vacuum.

## 5. Charge energy, domains and the cost of the lift

Without an energy on the new registers, the finite microscopic Hamiltonian
would have infinite neutral-charge degeneracy. A specific positive energy
that reproduces the Round15 lattice zero-mode energy is

    E(u,m,r)=|K u+(4m+r)s|^2/2
      = j^2+j(Ku.s)+|Ku|^2/2, j=4m+r.                 (16)

It is a positive definite quadratic form in the eight real coordinates
(u,j), because (k_i,s) is an invertible real basis. Cross terms are
essential: a separate arbitrary m^2 penalty would not equal the frozen
lattice Hamiltonian. The diagonal multiplication operator E is positive
self-adjoint on

    Dom(E)={psi: sum_(u,m,r) E(u,m,r)^2 ||psi_(u,m,r)||^2<infinity}.

It has finite energy multiplicities at fixed finite code size and compact
resolvent. Finite charge support tensor the finite code space is an operator
core. Its unitary group is the exact diagonal phase exp(-itE).

For the microscopic finite cylinder let H_fin^code=direct_sum_r H_r|code,
which is bounded because the cylinder Fock space is finite. Extend it
trivially over u and m. This block-diagonal operator strongly commutes with
E. For any declared scale alpha>0 the sum

    H_ext=alpha E+H_fin^code-E_min I,
    E_min=min spec(H_fin^code),                         (17)

is positive self-adjoint on Dom(E), with the exact product unitary group.
Its compact resolvent follows from the finite code multiplicity and the
bounded perturbation. The charge-sector Hamiltonian is thereby a completely
specified extension, but alpha and this global energy term are new choices;
no physical TFPT scale or microscopic locality is derived.

On the finite-support core, with x=Ku+j s,

    [E,T_lift]=T_lift (x.s+1),
    e^(itE) T_lift e^(-itE)=T_lift e^[it(x.s+1)].         (18)

The first identity uses covering coordinates or the explicit unitary (15).
The second is an all-Hilbert-space bounded-unitary equality. Translation
preserves Dom(E), since |x+s|^2 <= 2|x|^2+4. The energy cost of one charged
step is unbounded as the charge changes; no constant-cost flip is claimed.

The old microscopic Hamiltonian contribution to [H_ext,T_lift] still has
the far-cross-section coefficient and finite endpoint star from Round15,
multiplied by the disorder string and possible winding shift. The additional
alpha E contribution is the unbounded global charge term (18). Therefore
the full new Hamiltonian does not inherit an endpoint-only defect statement.
Nor does the finite transverse-width calculation give point-local or
width-uniform transverse locality.

## 6. Exact gain and remaining physical identification

The fourth-power mismatch is solved as an abstract charged representation:
the full neutral lattice is decomposed, the original cocycle is retained,
and a displayed unitary intertwines every charged and neutral shift. The
finite QWZ/code transporter is extended to that representation with an
explicit finite-code multiplicity and a well-defined positive energy.

The price is an unbounded winding register, seven further independent
integer charge coordinates to retain all of L0', and a newly declared
global energy. None is derived from the finite QWZ degrees of freedom.
The construction does not prove convergence of renormalized endpoint fields,
identify microscopic and normal-ordered edge charge, remove the code
multiplicity, prove a local Gauss realization, or show that the extended
microscopic Hamiltonian becomes the conformal lattice Hamiltonian. Oscillator
vertices, 4D chiral matter, mirror decoupling, flavor and the common gravity
parent remain separate obligations. No T-gate or RH claim is promoted.

## Reproduction

Run `checker.py` from any directory with the project Python environment.
The integrated layout is found relative to this file; an optional
`--contracts-root` selects the known source tree. The fail-closed checker
uses the literal frozen source lambda, retains source hashes, verifies the
integrated predecessor, and checks exact splitting/cocycle/carry/CAR-code
and energy identities including negative controls. Finite fixtures do not
replace the all-lattice and all-Hilbert-space arguments above.
