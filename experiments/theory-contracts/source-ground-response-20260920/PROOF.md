# Charged response on every actual ground of the assigned boundary

**UR.SOURCE.GROUND_RESPONSE.01 — PARTIAL — 20 September 2026**

## 1. Scope and inherited results

The previous pair-transfer contract compared a controlled source pair space
with the native empty-reference N=2 sector. It explicitly left open whether a
different demonstrated vacuum/GNS map could recover the interacting native
ground response. Here we test the entire actual ground space of the SAME
assigned massless boundary Hamiltonian, with the SAME nonlinear dressed
vertices. This is a new state comparison, not a repetition of the already
refuted linear Gaussian CAR identification.

The boundary remains conditional: Gamma=Z^10, K=diag(1^9,-1),
a=(1,1,1,-1,-1,-1,-1,-1), e_R=-e9, m=(a,0,3),
F(r)=(r-(a.r)a/2,0,-a.r), Vaux=K+2Kmm^T K. Its compact Hamiltonian is

    H_s = L0 + Lbar0 - Q/4,       q(v)=sum_j v_j.

We retain the original odd fields p_i=F(r_i)+e_R, r_i=FW_i/2, i=1,...,64,
with their actual cocycle and adjoints. Their positive kinetic norm is three.
No pinning cosine or new interaction is turned on. The lattice, Vaux and
their microscopic selection are not derived here from P1/P2.

The unmodified target is H_nat=Delta Nb+g sum_A(b_A^dagger P_A+h.c.),
at g/Delta=1/20, without mu N. Its certified unique ground has N=64.
The existing native results give, for each canonical fermion:

    Z_- = nu in (0.96107325,0.9736610625), Z_+=1-nu;
    m0=1, m1=0;
    0.007737 < e_low/Delta < 2403745/61508688;
    all addition energies /Delta > 82409/250000;
    all other removal energies /Delta > 94909/250000.

The low removal pole has strictly positive residue, in fact >0.88007628.
The native equation-of-motion and pole-consolidation checkers were rerun
here, with 831 and 81 controls, byte-identical to their stored certificates.
The expensive underlying full ground-state enumeration was NOT rerun. Its
theorem and bounds are inherited, with pinned sources; neither the source
ground argument below nor a short checker replaces that earlier proof.

The two E8 ground states themselves were already proved in
half-charge-energy-bridge and explicitly reproduced in
UR.SOURCE.CHARGED_TIME.01. They are not claimed as new. The earlier parity
and W-bright-space obstruction in universalraum-source-equivalence-decision
is also retained as an existing result, not re-counted as this contribution.

## 2. Entire ground space, with no hidden extra sectors

The exact orthogonal decomposition is

    Gamma = F(E8) direct_sum Z e_R direct_sum Z m.

The checker proves that integer images of D8 simple generators and
s=(1/2,...,1/2), together with e_R,m, generate all Z^10: their integer
Hermite normal form is I10. It checks the metric and original charge map.
Thus every momentum has unique form k=F(r)+x e_R+y m, with r in E8,
x,y integral. Its energy, before nonnegative oscillator integers, is

    E(k)=r.r/2 - sum(r)/4 + x^2/2+x/4 + y^2/2-y/4.       (1)

For integer r_j, the contribution r_j(2r_j-1)/4 is nonnegative and
vanishes only at zero. For half-integer r_j=n+1/2, it equals n(2n+1)/4,
nonnegative for all integral n, vanishing only at n=0. The E8 parity
condition admits both r=0 and r=s and no other equality cases. The
spectator terms vanish only at x=y=0. Hence the full ground space is

    G_s = span{|0>,|F(s)>}.                              (2)

Its full Gamma gap is 1/4, witnessed by -e_R or m. This incorporates the
previous E8 gap 1/2 and the two already present spectator directions.
The positivity proof is for all lattice points, not a finite box census.

Every source ground density matrix is allowed below. Write its populations
t and 1-t in (2), and allow any offdiagonal entry compatible with positivity.
No physical mechanism selecting t, the coherence or Vaux is asserted.

## 3. The actual nonlinear fields on both ground states

The original native weight array gives exactly

    q(p_i):  -3 (15 fields), -1 (35), +1 (13), +3 (1).

Use the plus sign for the p_i vertex, mapped to native f_i^dagger; its
adjoint has momentum -p_i and is mapped to f_i. Since

    (F(s),p_i)_V = (q_i+1)/2,

the exact lowest addition/removal energies on the two grounds are

| initial ground | addition | removal |
|---|---:|---:|
| 0 | (6-q)/4 | (6+q)/4 |
| F(s) | (8+q)/4 | (4-q)/4 |

All are strictly positive. On a highest-weight lattice state |k>, at
unit cylinder position, the creation-oscillator part of V_p is

    epsilon(p,k) exp(sum_(n>=1) p.a_-n/n) |k+p>.

The phase has unit modulus. The oscillator norm generating function is

    sum_(n>=0) c_n z^n = exp(3 sum_(j>=1) z^j/j)
                       = (1-z)^(-3),
    c_n=(n+1)(n+2)/2 >0.                               (3)

This is an exact convergent generating function, not an oscillator
truncation. The underlying lattice OPE and adjoint/cocycle conventions are
standard; see Anagiannis et al., Appendix B, equations B.2-B.6 and the
adjoint footnote ([primary source](https://arxiv.org/html/2009.00186v1#A2)).
The specific charge census, energies and comparison here are calculations
on the pinned TFPT fields, not conclusions supplied by that paper.

Two-point matrix elements cannot detect coherences between the grounds:
p_i-p_j=F(r_i-r_j), whereas r_i-r_j has integral coordinates and s has
half-integral coordinates. Thus p_i-p_j is never +F(s) or -F(s). Diagonal
two-point observables have zero net momentum; offdiagonal ones also cannot
connect the two grounds. The checker verifies all 2016 distinct pairs.
Anomalous same-sign pairs carry nonzero e_R charge and also do not connect
the grounds. We have not assumed an incoherent mixture to discard terms.

## 4. A finite, adjoint-preserving response

A raw field at a point is distributional. To state finite weights without
quietly identifying V_p(r)^dagger with V_-p(r), use an explicit symmetric
heat regularization:

    B_i^+ = c_i exp(-epsilon H_s) V_p_i(1) exp(-epsilon H_s),
    B_i^- = (B_i^+)^dagger,             epsilon>0.       (4)

These formulae may be read as regulated matrix elements on the ground
space and its finite-energy descendants. Their norms converge by (3).
One and the same c_i is used for the operator and its actual adjoint,
chosen so that the sum of the two ground response weights is one. This
normalizes the tested state expectation; it does NOT establish CAR as an
operator identity. Epsilon is an explicitly chosen probe resolution, not
an inverse physical temperature or a source-derived coupling.

Let rho=exp(-2epsilon), and E_(a,+/-) denote the four table entries.
The two normalized spectral measures are exactly

    dnu_+/- (E) = c_i^2 sum_(a=0,s) t_a
        sum_(n>=0) c_n exp[-2epsilon(E_(a,+/-)+n)]
        delta_(E_(a,+/-)+n)(dE).                       (5)

Their Euclidean time response follows by an additional exp(-tau E);
real time by exp(-itE). The oscillator factor is
(1-rho exp(-tau))^(-3). Thus both real and Euclidean times are derived
from the same positive measures, with the actual adjoint retained.

## 5. The 35-field test covers every source ground state

For q=-1, BOTH rows of the table are identical:

    addition energies = 7/4+n,
    removal energies  = 5/4+n,          n=0,1,2,... .   (6)

Every residue in (6) is positive for finite epsilon. Populations and
coherences have disappeared. The response matrix is scalar on this
35-dimensional block, so an allowed basis change within it cannot help.

Suppose a positive common time calibration multiplies source energies
by lambda in native Delta units. Equality of positive spectral measures
requires the lowest source removal pole to be the known native low pole.
Therefore

    (5/4)lambda < 2403745/61508688.

The source then has a nonzero addition pole at

    (7/4)lambda < 3365243/61508688
                 = 0.054711669349...,

whereas EVERY native addition energy is >0.329636. The intervals are
disjoint by more than 0.27492433 in native Delta units. Equivalently,

    source addition/removal threshold ratio = 7/5 = 1.4;
    native ratio > 8.4349537399....                    (7)

Independently, the source second removal pole is at (9/4)lambda,
strictly below 0.070343575, while every other native removal energy
is >0.379636. It too has nonzero weight for every finite epsilon.
The epsilon=infinity endpoint would discard the positive addition weight
and does not match the native state. These are spectral-support proofs;
no finite sampling of time is used.

Changing the global energy zero cannot change these excitation energies.
Adding a chemical-potential term can change them, but it changes the
Hamiltonian and potentially its ground selection. The native target is
the fixed no-mu Hamiltonian. Such a new term is outside this identification.

The threshold contradiction also applies to any readout that retains these
same nonzero lowest poles. Arbitrary frequency-selective readouts that
delete poles are not covered; their field products, charged adjoints and
physical selection would have to be derived separately.

## 6. Why equal integrated weights can give a misleading match

Let x=exp(-epsilon/2). Apart from their common oscillator factor, (5) has

    w_+(q)=t x^(6-q)+(1-t)x^(8+q),
    w_-(q)=t x^(6+q)+(1-t)x^(4-q).                     (8)

For q=-1, w_+=x^7, w_-=x^5 irrespective of t. Hence the common removal
weight, if all 64 modes are to match, must be nu=1/(1+x^2). The condition
w_-(q)=x^(-2)w_+(q) has exact difference

    (2t-1)[x^(6+q)-x^(4-q)].                           (9)

Because 0<x<1 and some q!=-1 are present, it forces t=1/2. Conversely
t=1/2 gives the same nu for all 64 modes. Ground coherences remain
unfixed by this two-point calculation. Both balanced pure superpositions
and balanced mixtures are admitted here; their higher responses need not
agree and their physical preparation has not been supplied.

Thus one CAN fit the native integrated addition/removal weights by choosing

    t=1/2, epsilon=log(nu/(1-nu)).                      (10)

This is an explicit fit to a target occupation, not a derived source rule.
It does not pass the common-time test (7). A second exact diagnostic is the
signed first spectral moment in the q=-1 block. From (3), the oscillator
mean is 3rho/(1-rho), so

    m1_source = (1-nu)(7/4+3rho/(1-rho))
                  -nu(5/4+3rho/(1-rho))
              = -1/2-3(nu-1/2)^2 <0,                 (11)

where rho=((1-nu)/nu)^2 follows from the same heat readout. For the native
occupation interval this lies between -1.173065 and -1.137765 in source
units. The native first moment is exactly zero. A positive time scaling
preserves the mismatch. Even without fitting the native occupation, (11)
is strictly negative for every finite positive epsilon.

Spectral moment sum rules from equations of motion are established tools;
see Freericks and Turkowski ([primary source](https://arxiv.org/abs/0907.1284)).
The native zero first moment is independently derived in the pinned TFPT
native charged-response calculation. The cited paper does not prove it
for this model, nor the new boundary comparison.

## 7. Correlation, decision, and remaining origin question

The new static-register contract UR.SOURCE.STATIC_REGISTER.01 was read and
its checker rerun: all 49 recorded requirements, including 21 algebraic
controls, 12 source pins and 16 manifest checks, reproduced byte for byte.
Its conclusion distinguishes real reduced correlations from a closed
non-Gaussian matter Hamiltonian. It does not prove that all source states
are Gaussian, and it is not needed as a premise for (6)-(11).

The sector reconstruction preserves the same charged fields and the same
assigned H. It therefore also preserves this obstruction. Relabeling
sectors cannot move the poles. The earlier successful W tensor and pair
state/time identities remain correct under their fixed lattice vacuum;
they did not assert the native N=64 vacuum map tested here.

The tested repair — choose any actual ground of this existing boundary,
keep its dressed fields and assigned time, and recover the unchanged
native ground response — is REFUTED in the precise readout class above.
The broader contract is PARTIAL, not a general refutation of TFPT or of
all nonlinear source maps. The elementary CAR obstruction was already
known; (7) is a response obstruction even after relaxing to normalized
state responses and admitting every source ground.

The remaining source derivation must alter the charged energy/field map
itself and simultaneously supply a state. Matching W, choosing a ground
superposition or fitting a two-point occupation does not accomplish that.
A proposed new source-derived interaction or field map can be tested with
the actual native N=63/64/65 thresholds above before computing elaborate
many-body dynamics. No new source interaction is invented here.

No T1-T8 gate is closed. No 3+1D, flavor, alpha or gravity transfer is
derived. The normal and optimized exact checkers agree; the analytic
infinite-lattice and spectral arguments are written out, not formalized
in a proof assistant. No independent agent review is claimed for this
new contract.
