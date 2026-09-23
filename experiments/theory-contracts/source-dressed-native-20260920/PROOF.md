# Dressed native tensor, faithful pair jets and the source-time gate

**UR.SOURCE.DRESSED_NATIVE.01 — PARTIAL — 20 September 2026**

## Decision and provenance

The requested outcome is a common physical source of the interlocked TFPT
construction. This contract tests the alternative F(E8) field dictionary left
open by the preceding common-T(D8) grading obstruction. It uses the existing
ten-channel lattice and its two already specified energies; it introduces no
new Hamiltonian, mediator, vacuum or gauge field.

The first unproved physical premise remains the ten-channel boundary itself.
The actual QWZ source has a controlled single chiral edge limit; neither ten
channels nor the reconstructed energy Vaux has been derived from P1/P2.
Full P1 contains more than a sign projector. Nothing here is a no-go theorem
for full P1 or TFPT.

The exact question is whether the original native 64-CAR/60-CCR tensor and
Hamiltonian can be identified with local odd fields in this boundary while
preserving the actual group action, charges, products, states and time.
The tensor identification succeeds. The literal CAR/CCR and same-time
Hamiltonian identification fails. Tracking the lost states gives a more
precise result: the full native exterior-square representation injects into
second-order antisymmetric field-product coefficients, while only its
60-dimensional coupling image survives the coincident product.

This is not the previous E6 cubic calculation repeated. That contract fixed
a bosonic current tensor. Here the native 60 by 2016 W, inherited odd grading,
both native group representations and the whole pair-state map are compared.

## 1. Fixed lattice, fields and energies

Let Gamma=Z^10 with K=diag(1^9,-1), B(x,y)=x^T K y. Put

    a=(1,1,1,-1,-1,-1,-1,-1), n=(a,-1,3),
    e_R=-e9, m=n-e_R=(a,0,3), g=K n,
    F(r)=(r-(a.r)a/2,0,-a.r).

The inherited unimodular decomposition is

    Gamma = F(E8) orthogonal-sum Z e_R orthogonal-sum Z m,
    F(r).F(s)=r.s, e_R^2=1, m^2=-1.

Original number and hypercharge are

    q(x)=sum x_i,
    Y=(-1/3,-1/3,-1/3,1/2,1/2,0,0,0,1,1).

For x=F(r)+A e_R+B m one has exactly

    g(x)=A-B, q(x)=sum r-g(x), Y(x)=Y8.r-g(x).

The source-native doubled weight arrays FW and BW are rebuilt from the
unchanged native_source.py prefix, including all six original guards. Write
r_i=FW_i/2 and s_A=BW_A/2. These are the native (bar16,bar4) and (10,6)
weights, with r_i^2=s_A^2=2. No conjugation of just the family factor is used.

Choose the existing minimal right-moving odd pair dressing:

    p_i=F(r_i)+e_R, b_A=F(s_A)+2 e_R.

These are integral, have squared norms 3 and 6, and g charges 1 and 2.
They are local odd/even fields in the SAME Gamma, under the F action.
They are not the former T-action c-spinors and do not evade that action's
central-character obstruction by renaming it.

Use a consistent Gamma cocycle

    epsilon(x,y)=(-1)^(sum_(i>j) x_i y_j).

It is bilinear and therefore associative. Its commutator is
(-1)^[B(x,y)+B(x,x)B(y,y)], the required graded lattice sign. A different
cohomologous convention only rephases fields; no microscopic phase
normalization is newly derived here.

The two PRE-EXISTING generalized metrics are V0=I and
Vaux=K+2 K m m^T K. They are not passive versions of the same energy.
At Vaux, F(E8) and e_R are right-moving, m is left-moving. Thus the p_i
fields have (h,hbar)=(3/2,0), and b_A have (3,0). Full F(E8) root currents
have weight one only in this selected reconstruction. No mass term is
turned on in this conformal test.

## 2. The exact native W is an equivariant local product tensor

For all 2016 unordered native fermion pairs, the exponent B(p_i,p_j) is

| Exponent | Number of pairs |
|---|---:|
| 0 | 480 |
| 1 | 1120 |
| 2 | 416 |

Exactly the 480 exponent-zero pairs obey p_i+p_j=b_A for a native mediator
row. The local vertex product at Vaux is

    V_p(z)V_q(0)=epsilon(p,q) z^(p.q)
        exp[sum_(l>=1) z^l p.a_(-l)/l] |p+q>.

All products here are right-moving. This is the standard lattice-vertex
framework, not a new mechanism; see Anagiannis et al., Appendix B,
[arXiv:2009.00186](https://arxiv.org/pdf/2009.00186). The odd-lattice sign
used here was specified and checked explicitly above.

One consistent sign per fermion, mediator and product-group root is enough
to identify the complete source tensor with W. The checker solves 2032
linear equations over F2 in 176 signs, with rank167. These include:

- all 480 nonzero tensor signs, with all remaining tensor entries zero;
- all root actions on the 64 fields from the original five-qubit and
  three-qubit Jordan-Wigner constructions;
- all induced root actions on the 60 mediators, reconstructed from W;
- the same root-current sign for both representations.

All 40 D5 and 12 D3 roots are used, together with their actual Cartan
weights. This is an intertwiner of the actual group representations, not
an inference from equal dimensions. The sign freedom is a basis convention,
not 480 independently adjusted coupling constants. Flipping a single
relative W sign makes even the smaller tensor-only sign system inconsistent.

In the resulting bases, define Psi_i and Phi_A as the rephased vertices.
The coincident normal product is exactly

    :Psi_i Psi_j: = sum_A W_(A,ij) Phi_A.                 (1)

Since WW^T=8I60,

    sum_(i<j) W_(A,ij) :Psi_i Psi_j: = 8 Phi_A.          (2)

Equation (1) is the promised positive source-field identification of the
native tensor, conditional on this boundary and current realization.
It does not identify a coefficient in an autonomous Hamiltonian.

## 3. The native dark pair space is present in field jets

Ordering one field at z and one at zero without antisymmetrizing their
LABELS is not a G-equivariant map from Lambda^2 F. It would falsely suggest
additional pair directions at weight four. The correct exterior map is

    A_ij(z) = [Psi_i(z)Psi_j(0)-Psi_j(z)Psi_i(0)]/2,
    A_ij(z)|0> = sum_(k>=0) z^k C_k(i wedge j).

For lambda=p_i.p_j the cocycle gives

    A_ij(z)|0> = epsilon_ij z^lambda /2
       [exp(E_i(z))+(-1)^lambda exp(E_j(z))] |p_i+p_j>,
    E_i(z)=sum_(l>=1) z^l p_i.a_(-l)/l.                (3)

Up to the already fixed nonzero basis phases, the coefficients are:

- lambda=0: C0=|b_A>, C1=(b_A.a_-1)|b_A>/2;
  C2=[b_A.a_-2+(p_i.a_-1)^2+(p_j.a_-1)^2]|b_A>/4.
- lambda=1: C0=C1=0,
  C2=[(p_i-p_j).a_-1]|p_i+p_j>/2.
- lambda=2: C0=C1=0, C2=|p_i+p_j>.

In particular C1=(L_-1/2)C0 on the whole exterior square: it cannot
restore a direction killed by C0. Every C2 state has conformal weight5.

All 2016 pairs are partitioned by their actual total lattice momentum.
Different momenta have independent Heisenberg Fock sectors. The complete
exact fiber calculation gives:

| lambda | Fibers | Pairs per fiber | rank C0 | cumulative rank C0,C1 | rank C2 alone |
|---|---:|---:|---:|---:|---:|
| 0 | 60 | 8 | 1 | 1 | 8 |
| 1 | 480 | 2 | 0 | 0 | 2 |
| 1 | 40 | 4 | 0 | 0 | 4 |
| 2 | 416 | 1 | 0 | 0 | 1 |

For lambda0 the quadratic oscillator coefficient distinguishes all eight
pairs; for lambda1 the difference vectors have the stated full row rank.
The checker evaluates these rational ranks in the complete oscillator
coefficient basis, including the a_-2 terms. Positive Heisenberg Fock
norms ensure that these are actual independent states, not formal symbols
that disappear in a further lattice-VOA quotient.

Consequently

    rank C0=60, rank(C0,C1)=60, rank C2=2016,
    dim ker W=1956, C2 restricted to ker W is injective. (4)

Thus the native pair representation has a faithful equivariant realization
as second-order local product coefficients. Its 1956 dark directions first
occur at weight5, two units above the weight3 coincident coupling image.
They were lost by coincidence, not by the absence of all corresponding
operators from the source theory. This is an exact finite pair-sector map,
not a construction of the full native Fock algebra or a spacetime spectrum.

## 4. Why this is not the native CAR/CCR Hamiltonian

Two elementary tests already decide the literal identification.

First, with the adjoint normalized to positive vacuum norm,

    Psi_i(z) Psi_i^dagger(0)
      = z^-3 [1+z j_i(0)+z^2 (:j_i^2:+partial j_i)(0)/2+...]. (5)

The field has a third-order pole and operator-valued singular coefficients.
Distinct i,j with p_i.p_j=2 have a noncentral double pole in the mixed
adjoint product. These are not canonical fermion-field relations. Choosing
the first creation mode gives a positive one-particle Gram, but does not
remove the extra operators from its anticommutators on other states.

Second, in the native Fock space a normalized bright fermion pair
P_A^dagger|vac>/sqrt8 and b_A^dagger|vac> are independent, orthogonal states.
Under the literal field map (2) their images are sqrt8 Phi_A|0> and
Phi_A|0>. Their source Gram is

    [[8,sqrt8],[sqrt8,1]], with determinant zero,         (6)

whereas the native Gram is I2. No rephasing or invertible two-state basis
change repairs that rank loss. The other 1956 coincident pair directions
are zero. C2 restores pair information, but changes the map and its energy
by two units on the dark kernel. It supplies no independent canonical
mediator and does not turn (1) into 60 independent CCR oscillators.

Therefore the native H=Delta N_b+g_coupling sum(b_A^dagger P_A+h.c.) and
its vacuum theorem cannot be transported through this field assignment.
The abstract native theorem is not refuted. A different, explicitly proven
state/operator/time embedding could still change this conclusion.

This also has an exhaustive metric bound within the stated Gaussian class.
Every local vertex with the same F(E8) root charge is

    x=F(r)+A e_R+B m, A,B integral.

Odd parity means A+B odd. For every boost of the orthogonal pair preserving
the full weight-one E8 current block,

    Delta_eta(x)=1+[(A+B)^2 e^(2eta)+(A-B)^2 e^(-2eta)]/4
               >=1+|A^2-B^2|/2 >=3/2.                (7)

The first inequality is AM-GM; the final nonzero odd integer follows from
A+B odd. There is no cutoff or sampled-eta extrapolation. A descendant
cannot lower this bound. Thus changing only that pair energy cannot make
these local odd root fields weight-one-half free fermions. The statement
does not exclude non-Gaussian phases or other charged sectors.

## 5. Charge, time and correlation with the other lane

The odd dressing shifts both original q and original Y by -1 per fermion
and -2 per mediator. It supplies correct parity and the actual native
internal G representation, but is not an unchanged identification of the
native E8 Cartan hypercharges with the original charged-source Y.
Writing Y_E8=Y+g makes the difference explicit. If g is physically gauged,
these lifts agree on neutral observables; proving that gauging and its
charged field sectors is additional work. Gauge neutrality of Phi^dagger
Psi Psi by itself supplies neither its amplitude nor a Hamiltonian.

At Vaux the corresponding conformal energies obey h_b=h_i+h_j=3 on
every W vertex. At the actual original free comparison V0, however,

    Delta0(p_i)=3/2+(a.r_i)^2: 56 at5/2, 8 at21/2;
    Delta0(b_A)=3+(a.s_A)^2: 30 at3, 30 at7.

For the 480 supported vertices the offset

    Delta0(b_A)-Delta0(p_i)-Delta0(p_j)
      =2(a.r_i)(a.r_j)

is -18 for15, -6 for90, -2 for225, and +2 for150. None vanishes.
The quarter-charge term from the previous charged-time audit cancels from
this difference because q_b=q_i+q_j. Retaining that term therefore cannot
turn V0 into Vaux or restore resonance. Applying
H(V)=L0(V)+Lbar0(V)-Qq/4 to this ten-channel comparison is conditional on the same earlier boundary
premise; it is not a new derivation of source time from P1.

In the selected Vaux theory C0 and C2 at a fixed total charge still differ
in energy by2, even after the quarter-charge shift. A chemical-potential
relabeling cannot change their local products or the Gram-rank defect.

The newly delivered other-lane contract UR.SOURCE.CHARGED_LIFT.01 has been
read and its 33-control checker reproduced byte for byte. It proves that
every integral additive lift of the neutral quotient is F(r)+(lambda.r)n,
lambda in E8. The common T(D8) action would require lambda=a/2 outside E8.
Its even-neighbor repair changes the local field algebra and removes the
original odd local fields. The present F-dressed fields do not contradict
that result: they use the permitted F action and the native s multiplet,
with their explicit additional odd pair component.

Together the two lanes separate three issues that previously looked like
one: the neutral E8 quotient, the charged group action, and the physical
product/state/time realization. The first two can agree in a selected
dictionary while the third still differs.

## Scope, checks and next source obligation

Exact arithmetic checks W, the full marked group action, complete pair
fibers, both energy assignments, and all source pins. Normal and -OO
executions must produce byte-identical certificates. General bound(7),
the vertex formula and the interpretation of the Gram defect are written
arguments, not consequences of a large check count. No independent agent
review or proof-assistant verification is claimed.

The next derivation must provide a common charged operator/state/time map
from the original source. It must either justify independent native CAR/CCR
degrees of freedom with their Hamiltonian, or derive the dynamics of the
composite/derivative fields actually present. In the latter case native
Fock vacuum and mass claims require a new derivation. The known Gaussian
source closure does not manufacture the missing elementary interaction.
This result does not authorize another fitted oscillator or a metric change
described as a passive dictionary.

No T1-T8 gate, 3+1D fermion theory, gravity, physical vacuum or complete
TFPT solution is established. Papers, ledger and empirical scorecard are
unchanged. This is a theory contract under the experiments firewall.
