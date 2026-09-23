# Conditional selection and a symmetric local quartic representative

20 September 2026 · UR.SOURCE.BOUNDARY_SELECTION.01 · PARTIAL.

This continues the user-supplied local edge-reconstruction candidate, retained
verbatim in INPUT.txt as a reported proposal. The exact lattice calculations
below were independently executed. The continuum bosonization assumptions
remain explicit; no interacting QWZ scaling theorem or P1/P2 origin is claimed.

## 1. Fixed source class and correctly typed coordinates

The candidate has eight right complex channels plus one auxiliary right and
one auxiliary left channel on the SAME edge. Its statistical form is

    K=diag(1,1,1,1,1,1,1,1,1,-1),    B(p,q)=p^T K q.

The physical source-number functional used in the proposal is q(p)=sum p_i.
It is not identified with Standard Model hypercharge. The fixed glue character
is i^(h.p), with h=(2,2,2,2,2,0,0,0,3,3).

The existing D5+A3 dictionary has D5 on coordinates 1--5, with color 1--3 and
weak 4--5; A3 family occupies 6--8. Coordinate 9 is auxiliary right and 10
auxiliary left. The first three plus signs in the supplied n are COLOR
coordinates. Recalling only that a family rank also equals three would give
the wrong dictionary. A3 rank-three coordinates are not themselves three
space dimensions or already three physical propagating fermion species.

The source class, number functional, glue character and identification of
these coordinates with actual microscopic channels are additional assumptions.
They are the conditional inputs of this audit, not conclusions from P1/P2.

## 2. The special null vector is constrained, but minimality alone is not enough

An integral vector n is characteristic for K exactly when all ten entries are
odd: B(p,p)=B(p,n) mod 2 for every integral p. For a nonzero characteristic
null vector,

    sum_(i<=9) n_i^2 = n_10^2 >=9,
    ||n||_Euclidean^2 = 2 n_10^2 >=18.

Thus the smallest Euclidean norm is 18. It occurs precisely when n_10=+/-3
and n_1,...,n_9 are signs. Fix the positive orientation n_10=3. Number
neutrality then requires exactly three plus signs among the first nine
entries. There are C(9,3)=84 choices, one orbit if all nine right channels
may be permuted. This is a constrained minimality theorem in the stated
microscopic basis, not an unconditional physical minimization principle.

For primitive characteristic null n the quotient

    (n^perp intersect Z^(9,1))/Z n

is positive, even, unimodular of rank eight. Conversely, evenness of this
quotient forces n to be characteristic: reduction of n^perp modulo two
surjects onto the kernel of B(n,.) modulo two (use a primitive dual u with
B(n,u)=1). The norm-parity functional must be that same nonzero linear
functional. For our candidate the explicit whole-lattice basis below
proves the quotient directly, without relying only on a dimension count.
The ordinary neutral null z=e9-e10 is noncharacteristic and leaves I8.

Evenness is an input that distinguishes the desired bosonic low-energy edge
from a fermionic one. The existence of a primitive neutral null cosine alone
does not supply that input. Nor does relevance at an energy matrix built
after selecting n turn this reasoning into native source selection.

## 3. The fixed oriented glue resolves a real ambiguity

Let e be 1 when n9=+1 and 0 otherwise. On the 84 minimal neutral candidates,

    h.n = 2e (mod 4).

Glue invariance therefore forces n9=-1 and leaves C(8,3)=56 possibilities.
Under S5 on the carrier and S3 on the family they form four orbits indexed
by k=0,1,2,3 plus signs in the first five coordinates.

If one additionally requires THE COUPLING VECTOR to be invariant under
within-block permutations S3_color x S2_weak x S3_family, only two remain:

    n_C=(+,+,+,-,-,-,-,-,-,3),
    n_F=(-,-,-,-,-,+,+,+,-,3).

This permutation requirement is a declared symmetry condition, not the full
native C/J action. The two null directions have B(n_C,n_F)=-12; they cannot
be simultaneously treated as mutually null commuting pinning directions.

Their quotients are abstractly E8, but their ORIENTED graded dictionaries
differ. Put a=(n1,...,n8) and, for p in E8=D8 union (s+D8), s=(1/2)^8,

    k_a(p)=a.p/2,
    T_a(p)=(p,-k_a(p),k_a(p)),
    F_n(p)=T_a(p)-(p1/n1)n.

This is integral on E8, orthogonal to n, and preserves inner products.
The required target character is g(p)=2 sum_(i<=5) p_i modulo four.
For n_C one has h.n_C=8 and

    h.F_C(p)=g(p)-8p1 = g(p) (mod 4).

For n_F, h.n_F=-4 and n1=-1, hence

    h.F_F(p)=g(p)-4p1.

The latter agrees on all integer D8 charges but changes every half-integral
spinor character by a minus sign. In particular s has phase i for n_C and
-i for n_F. Rephasing a vertex does not change its eigenvalue under G, and
adding an integral multiple of n changes h.p by zero modulo four. Fixing
the oriented D8/spinor dictionary therefore selects n_C from these two.

This is the strengthened CONDITIONAL selection: characteristic + neutral +
minimal + stated block invariance + the fixed oriented glue dictionary.
Without block invariance, matching the spinor orientation leaves 25 of the
56 minimal candidates (k=1 or 3), not one. Changing the target identification
or reversing its orientation changes the question. The proposal explicitly
does not yet identify G with physical J; this calculation cannot silently
upgrade that missing identification.

## 4. An exact symmetric replacement for the chosen energy matrix

The submitted representative uses F_C(p)=T_a(p)-p1 n, so it singles out the
first original color coordinate. Its timelike unit vector is n-e1.
There is a simpler representative using the ALREADY DISTINGUISHED auxiliary
right channel, without picking one of the eight original channels.

From now on n=n_C, a=(1,1,1,-1,-1,-1,-1,-1), and set

    e_R=-e9,                 m=n+e9,
    B(e_R,e_R)=1,           B(m,m)=-1,
    B(e_R,m)=0,             n=e_R+m,
    F_aux(p)=T_a(p)-k_a(p)n.                                  (1)

For integer D8 vectors, k_a is integer; for s+D8 it is half-integer. In
both cases F_aux is integral. Its ninth coordinate vanishes, and it is
orthogonal to m. Also B(F_aux(p),F_aux(q))=p.q.

Let beta_1,...,beta_8 be the standard E8 root basis specified in checker.py,
with Euclidean determinant -1 and Gram matrix G. Define

    W_aux=[F_aux(beta_1),...,F_aux(beta_8),e_R,m].

The executed exact calculation gives

    det W_aux=+/-1,
    W_aux^T K W_aux=G direct_sum diag(1,-1).                   (2)

Thus the entire integral local operator lattice is retained. The positive
energy matrix can be written WITHOUT an unexplained ten-dimensional fit:

    V_aux = K+2 K m m^T K
          = W_aux^(-T) (G direct_sum I2) W_aux^(-1).          (3)

Its eigenvalues are 1 (eight times), 17+12 sqrt(2), 17-12 sqrt(2), all
positive. Unlike the first-coordinate construction, this matrix preserves
S3_color x S2_weak x S3_family. It does so together with n, q and h.
It is still a CHOSEN energy matrix compatible with those data, not a unique
Hamiltonian inferred from them.

The choice changes dimensions of operators carrying a massive component.
In particular z=e9-e10 now has dimension 9, rather than the input's 4.
Both choices give Delta(n)=1; the free starting metric gives Delta(n)=9
and Delta(z)=1. Equal energy-matrix eigenvalues do not justify copying all
individual operator dimensions between the two realizations.

In the field coordinates phi=W_aux chi, the continuum quadratic theory
is the E8 sector plus an ordinary right/left pair. The interaction
cos(n^T K phi) becomes cos(chi_R-chi_L). At this designated free-fermion
bosonization point it is a Dirac mass term. Consequently the proposed
continuum Hamiltonian has the same conditional factorization

    H=H_(E8,1)+H_massive_Dirac.

The original fermion cocycles and spin structure must be transported with
the integral basis change. No enlargement of the Hilbert space by arbitrary
bosonic sectors is licensed. This uses the standard continuum mechanism of
[Cano et al.](https://arxiv.org/abs/1310.5708), not a new microscopic lattice
existence theorem or an operator derived directly from a QWZ hopping term.

## 5. The local spinor becomes a quartic composite

The fixed weight s maps under (1) to

    b_aux=F_aux(s)=(1,1,1,0,0,0,0,0,0,1).

Hence the local vertex is proportional, with the inherited Klein factors,
to the product of the three right color fermions and the auxiliary left
fermion, in the charge convention of INPUT.txt. It has four distinct
fermion factors; there is no vanishing same-point square of one fermion.

At the free original energy matrix its conformal dimensions are (3/2,1/2):
total dimension 2 and spin 1. At (3) it has (1,0): it is a pure chiral
weight-one E8 current and commutes with the massive factor. This is an
internal D8 spinor CURRENT, a bosonic local operator. It is not a proof of
a 3+1-dimensional Weyl fermion or of spacetime spin-statistics.

For every E8 vector,

    q(F_aux(p))=sum p_i,
    h.F_aux(p)=g(p)-8 k_a(p)=g(p) (mod 4).                     (4)

The checker executes (2)--(4) on all 240 roots and all 57,600 ordered root
pairings using exact integer arithmetic. These are metric/charge/grade
checks, not a new replay of the attachment's entire cocycle phase table.
The integral lattice isometry allows the known compatible cocycle to be
transported; its identification with native C/J actions remains separate.

The quartic representative differs from the supplied pure representative
b_old=(0,0,0,1,1,1,1,1,1,-2) by exactly n:

    b_aux=b_old+n,
    2 b_aux=T_a(2s)+n=F_aux(2s).

The D8 dictionary must transform as well. Integer carry is preserved in the
same local lattice, rather than stored in a new two-state counter. The
standard level-one current identities then hold on the common continuum
vacuum: ||V_(b,-r)Omega||²=r for r>0; V_(b,-1)^2 Omega=0 while
V_(b,-3)V_(b,-1)Omega is the nonzero weight-four doubled-charge state, up
to the fixed cocycle phase. This follows from b²=2 and the lattice-vertex
operator product, not from a new finite QWZ simulation.

## 6. A genuine open interval for the relevant-null selection test

At (3), write any integral vector as (r,A,B) in E8 direct_sum I_(1,1).
Its dimension is Delta_0=(r²+A²+B²)/2. If it is null, r²+A²-B²=0, so
Delta_0=B². For a nonzero relevant null vector Delta_0<2, |B|=1. Evenness
and positivity of E8 then force r=0, |A|=1. Number neutrality becomes
A=B, because q(e_R)=-1 and q(m)=+1. Thus the only neutral relevant nulls
are +/-n. Every other nonzero neutral null has Delta_0>=4.

This is not limited to one numerical matrix. Keep the E8 block and deform
only the pair's positive energy matrix by the Lorentz boost metric

    M_eta=[[cosh(2eta),sinh(2eta)],
           [sinh(2eta),cosh(2eta)]].

In these coordinates the null-vector scaling dimension is

    Delta_eta = [r²+cosh(2eta)(A²+B²)+2sinh(2eta)AB]/2.

Since M_eta has eigenvalues exp(+/-2eta),

    exp(-2|eta|) Delta_0 <= Delta_eta <= exp(2|eta|) Delta_0.

Therefore for |eta| < log(2)/2, n stays relevant and every other neutral
null stays irrelevant. In the smaller closed interval
|eta|<=log(3/2)/2, their dimensions are respectively at most 3/2 and at
least 8/3. The strict selection has a finite margin.

This is a uniform scaling-dimension statement over the infinite integral
class of neutral self-null cosines. It is not a stability theorem against
all perturbations, an RG derivation from the free QWZ point, or a proof
that any lattice Hamiltonian realizes this continuum family. The massive
pair away from eta=0 is a sine-Gordon interaction, not the free Dirac
factorization of the special point. Independent positive velocities and
the boost parameter remain continuous choices.

## 7. What the source still has to produce

The original compiler already supplies the D5+A3 glue data and the desired
oriented spinor class. This audit shows how those data can distinguish
local null-coupling candidates IF realized on the specified channel lattice.
The missing source map is now more precise:

1. Produce the eight channels and the extra local R/L pair with this actual
   number/grading representation, rather than eight copies inserted by hand.
2. Derive the even-quotient/minimal-coupling condition and the physical block
   symmetry, or another actual selector giving the same n and phase basin.
3. Obtain a microscopic interaction whose effective energy lies in the
   specified reconstruction regime, with momentum-compatible cosine.
4. Intertwine the native C,J actions, the state and common time with this
   reconstructed field dictionary. A post-hoc lattice conjugation supplies
   a representation, not that physical intertwiner.

The one-copy QWZ edge has only one chiral complex channel; its rank-one
current obstruction was already documented in compiler-source-channel-gate
and source-rg-clock-bridge. It is not newly discovered here and does not
refute the explicitly enlarged eight-channel candidate. Neither candidate
by itself supplies a dynamical 3+1D geometry, chirality, or spin-two sector.
