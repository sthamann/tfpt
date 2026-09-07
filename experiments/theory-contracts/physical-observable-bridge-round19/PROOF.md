# Round19: a physical observable bridge, with a finite-range gravity subalgebra

2026-09-07. NON-RH, fixed finite periodic lattice. This separates three
questions that need different answers: changing only gauge labels does not
change the physical base algebra; some genuine native gravitational
derivative observables have finite-range representatives; and the local
positive parent approximates finite protocols made from these observables.
None of this identifies the whole old native field net with the new one.

## 1. Exact quotient algebra through the gauge preconditioning

Use the actual operators and model of
[Round18](../preconditioned-local-parent-round18/PROOF.md). Write H_B for
the positive physical base Hilbert space and B=B_delta,eta for its specified
self-adjoint generator. Let d=4(n-1) first, before the optional four extra
mean gauge pairs. The old and preconditioned constraint labels obey

    c=P c_tilde,  X_tilde=P X,  P=ell^2 on each mean-zero field,
    (T F)(c_tilde)=(det P)^(1/2) F(P c_tilde).             (1)

The physical reduction of continuous compactly supported H_B-valued tests
is E F=F(0); its null space is precisely ker E. For any bounded O on H_B,
the fiberwise operator I tensor O preserves this test space and ker E, and

    E (I tensor O)F=O EF.                                (2)

Thus O -> [I tensor O] is an isometric unital *-representation of the
ENTIRE bounded physical algebra B(H_B) on the completed quotient. Products,
adjoints and norms are preserved, not merely individual expectation values.
Surjectivity of E follows by F(c)=a(c)v with a(0)=1.

With both gauge Haar measures normalized independently as du/(2pi)^d,
E_new T=(det P)^(1/2) E_old. Transporting the old Haar measure instead
multiplies the new physical inner product by (det P)^(-1); equivalently
use the normalized evaluation (det P)^(-1/2) E_new. With this explicit
choice the induced physical unitary I_phys is the identity on H_B and

    I_phys O_old=O_new I_phys,    I_phys B_old=B_new I_phys. (3)

The two B's in (3) are the SAME chosen base. The old global and the new
cellwise higher-order stabilizers are different off shell, so (3) is NOT
an intertwining of their full unreduced generators by T. Their exact
quotient dynamics both equal exp(-itB), which suffices for (3).

For the all-site Round18 model, adjoining a test factor a_mean with
a_mean(0)=1 adds the four evaluation maps. The completed quotient remains
H_B, and (2) holds unchanged. The mean constraints are the declared extra
pure-gauge constraints; their off-shell dynamics need not decouple.

On H_B=L2(R^(35n)), let A_B(R) be the bounded local algebra acting on the
canonical pairs in a finite site region R and trivially on its complement.
The quotient maps in (2)--(3) preserve this declared local net EXACTLY.
No ell^(-1) acts on these physical fields. This is locality relative to
the local positive BASE variables, not automatically the original gravity
variables or the final TT-only tensor factor. Those distinctions are
addressed constructively below.

## 2. A polynomial TT filter in the actual native stencils

Keep the Round18 real adjoints, tensor order (11,22,33,23,13,12), scalar
row A, vector row V, d=(D_i^+) and trace column t. In this section all
scalar Laplacians act componentwise on tensor or vector spaces. Recall

    A A*=2ell^2,  A V*=0,  V V*=(ell I+d d*)/2,
    (d d*)^2=ell d d*,  Vt=d,  At=2ell.                  (4)

For ell>0 the orthogonal TT projector can equally be written

    P_TT=I-V*(V V*)^(-1)V-A*(2ell^2)^(-1)A.              (5)

Indeed range A* and range V* are orthogonal, of dimensions one and three
per nonzero momentum. Their joint orthogonal complement has dimension two.
It agrees with ker V intersection ker t*: the component of t orthogonal
to range V* is A*/ell. This last identity also follows directly from the
native shifts, A*=ell t-V*d. There are no missing staggered phases.

Define on the FULL site tensor space the following polynomial matrix:

    R=ell^2 I_6-2ell V*V+V*d d*V-(1/2)A*A.              (6)

By (4), (V V*)^(-1)=2ell^(-1)I-ell^(-2)d d*. Equations
(5)--(6) prove the all-volume identities

    R=ell^2 P_0,  R*=R,  R^2=ell^2 R,
    R V*=0,  R A*=0,  R t=0,                            (7)

where P_0 is P_TT on all nonzero modes and zero on all six tensor means.
At zero momentum (6) is exactly zero. Thus (7) includes the means, not
an implicit inverse at zero. R is nonzero on every retained TT mode,
with eigenvalue ell^2 and rank 2(n-1).

Every term of (6) has a bounded stencil. A safe universal bound is graph
radius four from the labeled tensor site's center, using the actual
staggered component labels. No support radius grows with volume. The
companion checker additionally reconstructs the unaliased Laurent stencil,
so wrapping on L=2 or L=3 cannot fake a support certificate.

R is a FOUR-derivative TT-filtered tensor readout. We do not call it an
identified Riemann/Weyl curvature tensor or assert a minimal derivative
order. It is a concrete way to remove TT inverse kernels from a nontrivial
algebra of gravitational observables. Continuum results relating compact
linearized observables to curvature provide motivation only, not a premise
for this lattice proof: [Froeb--Hack--Higuchi,
Compactly supported linearised observables](https://arxiv.org/abs/1703.01158).

## 3. Native gauge-invariant bounded observables and their exact quotient

In the original mean-zero gravity phase space the constraints are Aq=0
and Vp=0. Their gauge directions shift p by range A* and q by range V*.
For real tensor test vectors f,h set

    L(f,h)=<f,Rq>+<h,Rp>,   W_R(f,h)=exp(i L(f,h)).       (8)

These are ordinary exponentials of real linear canonical fields. Each L
has its standard self-adjoint closure and the W's form the regular Weyl
representation; there is no finite-dimensional approximation to the CCR.
Equations (7) show that they strongly commute with all linear constraint
Weyl groups. Moreover they commute with all original Darboux gauge
coordinates X: X_H=-(2ell^2)^(-1)Ap and X_v=(V V*)^(-1)Vq.
Both commutations follow from the exact linear symplectic pairings, hence
hold for the exponentials and not just a formal common-domain bracket.

The reduced representatives are

    L_phys(f,h)=<f,ell^2 q_TT>+<h,ell^2 p_TT>,            (9)

acting on the original TT factor, identity on every scalar or other
spectator factor. Their symplectic pairing is exactly

    sigma_R((f,h),(f',h'))=<f,R^2 h'>-<h,R^2 f'>,
    W_R(f,h)W_R(f',h')=exp(-i sigma_R/2)
                              W_R(f+f',h+h').           (10)

The same pairing holds before and after reduction because
R P_0 R=R^2. Therefore the native gauge-invariant Weyl algebra generated
by (8) and its reduced representation are linked by a *-homomorphism
which preserves the complete Weyl relations. Compactly supported f,h
have actual native support inside their fixed R-neighborhoods. Disjoint
such enlarged neighborhoods commute at equal time. This is a genuine
finite-range native observable SUBALGEBRA, not a gauge-fixing declaration.

On a fixed finite lattice these readouts generate the entire TT Weyl
algebra GLOBALLY: any TT smearing u equals R(ell_nonzero^(-2)u).
This statement does not preserve localization of the smearing. Recovering
q_TT,p_TT from Rq,Rp requires ell_nonzero^(-2), with norm ell_min^(-2).
The map is not a uniformly local or uniformly conditioned net inverse.
In particular a delta-site TT-projected potential still has an inverse
kernel. The four-derivative filter does not establish a local canonical
TT potential field. The extra all-site tensor means and complement modes
of the parent are annihilated by R, not interpreted as gauge modes there.

The ACTUAL Ward sources obey tau=sigma+t h with
h_x=(pi_x^2-m^2 phi_x^2)/2. Thus

    R tau=R sigma,                                      (11)

exactly, including zero modes and all quantum orderings (these source
components are multiplication/diagonal momentum squares). In particular
the readout source has no pi dependence. The checker imports the literal
Ward frontend and tests (11), nonzero response and rejection of an
anisotropic kinetic-source alteration. No arbitrary replacement source
is fitted to make the filter work.

## 4. Gravity dressing, clock readouts and the optional momentum quotient

The original scalar gravity dressing is, in the X representation,

    U_g=exp(-ig sum_a X_a J_a),                          (12)

where the actual J_a are finite scalar-matter Weyl quadratics. It acts as
the identity on TT. This is the all-real-coupling unitary established in
[the original quantum dressing](../constraint-dressing/README.md), Section 9.
Equivalently, (7)--(8) commute both with X and with each scalar J. Hence

    U_g W_R(f,h) U_g*=W_R(f,h)                           (13)

EXACTLY for every coupling, not only at first order. The TT derivative
subalgebra remains native finite range through THIS gravity dressing.
The subsequent characteristic straightening S_loc and clock transport
are different operations and need not fix it.

For scalar Weyls the corresponding native representative U_g W_scalar U_g*
generally depends on the nonlocal X. Their abstract physical algebra is
still identified by (2), but their dressed native support is not proved
local. Nor does (13) cover arbitrary auxiliary source dressings, nonlinear
gravitational matter sources, or the undeclared full diffeomorphism group.

Retain B>=e_m>0 and use the exact negative-sheet clock tube and
half-density unitary Z from [Round16](../clock-vertex-round16/PROOF.md).
For W=S_loc Z* (and any explicitly retained common extra transports),

    W* C_loc W=K_c+lambda,
    O_D=W(I tensor O)W*.                                (14)

For every bounded O on H_B, (14) is a bounded operator of the same norm,
strongly commuting with the clock constraint and the spectral c constraints
in this reference representation. It induces precisely O on the joint
physical quotient. Products and adjoints are again exact. Its original
variable support is not inferred from this unitary transport, which uses
full characteristic dynamics and a spectral clock chart.

For clarity about what a clock reading measures, set omega=sqrt(12B) and
D=sqrt(6) omega^(-1/2). The reference shell readout is

    chi_v(t)=D exp(-i omega t)v.                         (15)

Equip ran D=Dom(omega^(1/2)) with the complete weighted norm
||chi||_clock=||D^(-1)chi||. Then (15) is an onto isometry from H_B onto
that readout Hilbert space for every fixed t. It is not an isometry for
the ordinary unweighted L2 norm. The operator representing O on readings
at t is D exp(-i omega t) O exp(+i omega t) D^(-1), bounded in this
weighted norm, with norm ||O||. No commutation of O with B is required.
This states the half-density convention explicitly and does not multiply
delta distributions by a merely measurable S_loc.

If the OPTIONAL homogeneous relational constraints are also imposed, the
physical space is ran Pi_0, not H_B. The preceding local-net claim must
then be restricted: bounded operators commuting with Pi_0 restrict
multiplicatively, and all operators in the corner Pi_0 B(H_B) Pi_0 have
the transported representatives (14). But O -> Pi_0 O Pi_0 on the whole
unprojected algebra is NOT a *-homomorphism. A site Weyl need not preserve
ran Pi_0, and compact averaging may spread its support. The checker gives
an explicit commuting-observable compression counterexample. No full local
net theorem is claimed for this extra projected theory or for the genuine
translation quotient, which is a different choice.

## 5. Bare local Weyls asymptotically respect the actual Gaussian encoding

The exact local parent from [Round15](../local-parent-round15/PROOF.md) has
slow x=(phi,q), fast a, and the normalized embedding

    (J_delta,eta psi)(x,a)=psi(x) chi_eta(a-f_delta(x)),
    chi_eta(b)=det(Omega_eta/pi)^(1/4) exp(-b.Omega_eta.b/2),
    Omega_eta=sqrt(eta) K_delta^(1/2)>0.                 (16)

Here f_delta is the actual degree-at-most-two displaced minimum and K_delta
is source independent. They are generally nonlocal functions of x; that
fact is not removed. Define a slow Weyl with real coordinate smear u and
translation y by the convention

    [W(u,y)psi](x)=exp(i u.(x+y/2)) psi(x+y),            (17)

and let W_parent be the BARE same operation on x, identity on a. It has
exact finite support when u,y do. Configuration multipliers (y=0)
intertwine J exactly. For general y put
Delta f(x,y)=f_delta(x+y)-f_delta(x). Gaussian integration gives

    <chi_eta(. -f_delta(x)),chi_eta(. -f_delta(x+y))>
      =exp[-sqrt(eta) Delta f.K_delta^(1/2).Delta f/4],

    ||(W_parent J-J W)psi||^2
      =2 integral dx |psi(x+y)|^2
           (1-exp[-sqrt(eta) Delta f.K_delta^(1/2).Delta f/4]). (18)

The phase cancels from the norm. The positive integrand tends pointwise to
zero for fixed delta,x,y and is bounded by 2|psi(x+y)|^2. Dominated
convergence proves

    ||(W_parent J_delta,eta-J_delta,eta W)psi|| ->0       (19)

for EVERY slow Hilbert vector, without a moment or smoothness assumption.
For vectors with finite integral of |psi(x+y)|^2 Delta f.K_delta^(1/2).Delta f,
1-exp(-z)<=z gives the explicit O(eta^(1/4)) norm bound. For a pure tensor
translation Delta f is constant in x because f is affine in q; a scalar
translation generally has a linear phi-dependent difference. These are
fixed-delta, fixed-operation statements, not uniform estimates on all
states, large translations or growing lattices.

At finite eta, (18) is nonzero whenever Delta f differs from zero on a set
where the state is nonzero. The bare operation therefore does NOT preserve
the encoded range exactly. The exact encoded Weyl needs a compensating
fast displacement f(x+y)-f(x), usually nonlocal. Both the nonzero defect
and the asymptotic local-operation theorem are essential to the result.

## 6. A complete finite readout-protocol convergence theorem

At fixed delta the input dynamical theorem gives, for every psi,

    ||(exp(-it B_delta,eta)J_delta,eta
                       -J_delta,eta exp(-it A_delta))psi|| ->0, (20)

uniformly for t in compact intervals. For any fixed finite word made from
the unitaries (17), their adjoints and finitely many time propagations,
equations (19)--(20), telescoping the word one factor at a time, imply

    ||Protocol_parent J_delta,eta psi
                    -J_delta,eta Protocol_delta psi|| ->0.    (21)

Every factor has norm one, so each telescope term is one of the proved
strong intertwinings evaluated on a fixed slow vector. The same result
holds for a finite linear combination of such words, with its finite
coefficient bound. If finite sequences of durations range in a fixed compact
set, continuity of the limiting unitary orbit and finite epsilon nets give
uniformity; no infinite-duration or infinitely many readout limit is taken.

For any two initial vectors, isometry of J and Cauchy--Schwarz turn (21)
into convergence of the corresponding matrix elements. Finite products of
bounded readouts interspersed with evolution, not just single compressed
Hamiltonian expectations, are thus controlled. Spectral projections,
unbounded detector moments, operator-norm convergence and arbitrary Borel
functions are not inferred from finite Weyl words without extra estimates.

Next take delta->0 at the SAME fixed lattice. The original strong unitary
limit is A_delta -> A_0=A_+ tensor I+I tensor S_extra. Select only scalar
Weyls and the gravitational Weyls W_R from (8), both of which are fixed
operators independent of delta,eta. Since R kills all complement and mean
tensor modes, these operate as their scalar/TT representative tensor the
identity on the 4n+2 extra tensor modes. A second bounded-word telescoping
argument therefore gives the sequential limit of all these matrix elements
to the corresponding protocol for A_+ and its physical observable algebra.

Explicitly take initial product states psi tensor chi_extra with any
normalized chi_extra. Extra free evolutions in a word combine into
exp(-i S_extra sum_j t_j). For general transition amplitudes this factor
remains and is not zero-energy-normalized away. For EXPECTATION/CORRELATION
protocols of the usual Heisenberg form, total forward minus backward time
is zero, so the extra factor cancels exactly. Equivalently one can trace
the independent extra factor and obtain the same TT/matter correlation.
An arbitrary transition word with nonzero net duration requires retaining
its explicit spectator amplitude. This exception prevents confusing an
autonomous subsystem readout with removal of extra physical states.

Thus local bare scalar and native finite-range derivative-gravity readouts
of the positive parent recover a nontrivial physical TT/matter observable
algebra and its finite dynamical protocols. The preparation J is still
nonlocal and the sequential auxiliary limit still singular; this theorem
does not provide local state preparation or a uniform causal bound.

The same bounded-word proof applies to the reduced clock propagations
exp(-it sqrt(12B_delta,eta)) whenever the positive-base lower bound is kept:
the core/resolvent intertwining and tight spectral cutoff argument from
Round15 apply to this bounded continuous spectral function as well. Its
uniform compact-time version follows by a compact spectral cutoff before
removing the uniformly small state-dependent tail. This is the UNPROJECTED
reduced clock dynamics; the optional Pi_0 restrictions and the absolute
spectator clock-energy convention still require their own stated conditions.
In particular sqrt(12(A_+ + S_extra)) does NOT split into independent
subsystem clock generators. The preceding TT-only correlation conclusion
does not automatically apply to clock time; removing this spectator clock
energy needs the separate normalized low-energy spectator approximation
of Round16 in its stated order.

## 7. Tensor charge extension and remaining boundary

If a coupled positive base has sectors indexed by a countable charge set,
uses the SAME J as I_charge tensor J_delta,eta, and has the sectorwise
dynamical convergence proved in the companion coupling construction, then
bounded unitary charge shifts commute with J exactly. The proof of (21)
extends to mixed finite words of those shifts, scalar/filtered-gravity
Weyls and sector-dependent dynamics. Prove it first on finite charge
support; any fixed finite shift word visits finitely many sectors. The
uniform norm bound on each factor then extends the result to all square
summable charge superpositions by a finite-support tail estimate. This is
a conditional observable corollary, not a second proof of the companion
coupled Hamiltonian or a superselection prescription.
If a charge shift changes the system energy, its clock-reading representative
also needs the corresponding D factors in (15); it is not the naive same-weight
charge shift on unweighted shell wavefunctions.

The results here eliminate a specific overly broad obstruction: nonlocal
gauge-label preconditioning does not force every physical observable to
be nonlocal. They supply an exact quotient algebra, actual local native
gravitational derivative observables, and controlled finite local readout
protocols approaching the retained positive TT/matter model. Still open
are a full native interacting local observable net, local preparations,
uniform volume/continuum bounds, relativistic propagation, a preferred
metric and model parameters, and the additional matter/sector/measure
contracts. Neither finite stencil identities nor positive abstract
quotients prove a full TOE, T1--T8 closure, or anything about RH.

## Reproduction

The checker independently reconstructs the native matrices and universal
Laurent stencil, checks the literal Ward response, and tests the exact
Gaussian overlap, Weyl signs, quotient normalization, clock weight and
compression counterexamples. Its exact algebraic checks are regressions
for the displayed all-volume proof, not numerical evolution or finite CCR.
