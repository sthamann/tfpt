# Fixed-word matter resummation with controlled electric leakage

2026-09-07. **NON-RH / conditional, unpromoted theory experiment.**
The further matter propagation of Round45's four newest electric sources
has a self-adjoint auxiliary representation. It is now evaluated on the
complete edge parent and bounded for the cubic target. The NEW cubic
resummed readout has NOT been evaluated. The global ideal remainder is
still sixth order, not seventh, and full electric dynamics and T1-T8
remain open.

## 1. Same parent, a precisely specified new target

The parent remains H=H_E+dGamma(h), with

\[
H_E=\frac\kappa2\sum E_\ell^2,\qquad
h=\begin{pmatrix}A+\beta A^2&\eta A\\\eta A&MI\end{pmatrix},
\quad A_{xy}=aU_{xy}.                                      \tag{1}
\]

Keep a=1/12, eta=1/2, beta=1/4, kappa=1/100, M=4, Vmag=0 and
the original low onsite backtracks d=1/96. Initial physical states have
E0 and exactly one L/H fermion per site; a finite species patch may be
coherent, mixed or entangled, with bare-low filling elsewhere. These
couplings and preparations are assumptions, not selections from TFPT.

Use the same exact branch split [V,FO]=F[V,O]+[V,F]O, labelled M and E.
Replace only the FINAL free propagator of each Round45 leaf
MEMM, MMEM, MMME and MEE by all its subsequent M propagation. Write
these replacements as C_hat and define

\[
Z_{46}=P_\infty+C_{ME}+C_{MEM}+C_{MME}
 +\widehat C_{MEMM}+\widehat C_{MMEM}
 +\widehat C_{MMME}+\widehat C_{MEE}.                         \tag{2}
\]

Each hat includes the original leaf plus any number of M events AFTER
it. Earlier branches are unchanged. This disjoint branch partition does
not double-count MEM or the lower free sources. It does not resum every
possible one-E history, nor E events occurring during the new propagation.
MEME, MMEE and first-E events after four or more initial M events remain
in their inherited bounds.

## 2. A self-adjoint lift for every fixed literal word

Let I=(i1,...,id) label a literal CAR word O_I with fixed creator pattern
epsilon_l in {0,1}. Work in the FULL ordered tensor index space, before
any antisymmetry or CAR quotient. The bilinear derivation satisfies

\[
[d\Gamma(h),O_I]=\sum_J\mathcal L_{IJ}O_J,\qquad
\mathcal L=\sum_{l:\epsilon_l=1}h_l^T
                   -\sum_{l:\epsilon_l=0}h_l.              \tag{3}
\]

The transpose on a creator also reverses its gauge transport. In
particular, the cubic pattern is (+,-,-); the literal five-factor
pattern is (+,-,+,-,-), not (+,+,-,-,-). The latter would lose the
contraction in c_u^dagger c_v c_a^dagger c_b c_y.

For a gauge-operator-valued ROW F, its free-electric-plus-M evolution is

\[
\dot F=iH_EF-iF K_d,\qquad
K_d=H_E I-\mathcal L
 =H_E I-\sum_{creators}h_l^T+\sum_{annihilators}h_l.          \tag{4}
\]

Thus for an initial row or a time-dependent injection S,

\[
F(t)=e^{iH_Et}F(0)e^{-iK_dt}
 +\int_0^t e^{iH_E(t-s)}S(s)e^{-iK_d(t-s)}\,ds.             \tag{5}
\]

K_d is a real diagonal self-adjoint electric/onsite operator plus a
bounded symmetric hopping operator. Negative creator contributions
do not make it non-Hermitian. The generator is bounded below for fixed
d; no bound on the complete electric spectrum is imposed. Equation (5)
is a strong integral identity. For the relevant unbounded-generator
framework, see [Nachtergaele and Sims, On the dynamics of lattice systems
with unbounded on-site terms in the Hamiltonian](https://arxiv.org/html/1410.8174v1).
The signed tensor lift and estimates here are model-specific derivations,
not a claim that this reference solves the present model.

This lift is not the full physical Hamiltonian: the omitted [V,F]O
branch is generally nonzero. Its CAR reconstruction is also NOT an
isometry, as the explicit counterexample below shows.

## 3. Exact edge evaluation keeps intermediate electric fields

The finite benchmark is the unchanged original edge parent, with both
species and the same ambient onsite d=1/96. Its full physical N=2
Gauss sector has dimension six. The auxiliary tensor spaces are NOT
those six physical states.

Define signed auxiliary charge

\[
q_I(x)=\#\{\text{annihilator legs at }x\}
          -\#\{\text{creator legs at }x\}.                  \tag{6}
\]

It always has total charge one, but individual sites may have negative
charge or charge greater than two. It must not be constrained like
physical fermion occupation. For a fixed auxiliary background B with
B0+B1=1 and edge orientation 0->1,

\[
E_I=q_I(1)-B_1,\qquad R_B=-B_1.                            \tag{7}
\]

The source word's gauge shift is r_I=-q_I(1), so E_I+r_I=R_B,
independent of I. Restricting (5) to this charge background gives a
finite row equation

\[
\dot G_B=iG_BL_B+S_B(t),\quad
L_B=H_E(R_B)I-K_{d,B}.                                    \tag{8}
\]

Its diagonal is kappa(R_B^2-E_I^2)/2+Delta(O_I). Its creator off-diagonal
is +h^T and its annihilator off-diagonal is -h. The implemented check
E_I-E_J=p_IJ verifies every original transport. Only final indices with
E_I=0 are extracted for the physical initial class. Intermediate
coefficients must be evaluated at E_I, not silently at zero.

For d=3 there are four backgrounds B1=-1,...,2, each with 64 literal
word states; selected E0 word counts are 8,24,24,8. For d=5 there are
six backgrounds B1=-2,...,3, each with 1024 states; selected counts are
32,160,320,320,160,32. All these tensor states are retained. There is
no edge electric cutoff: Gauss law fixes its finite allowed current
for each tensor word and background.

For a raw n-interaction leaf, its last free interval has frequency
f_n=H_E(E+r)-H_E(E)+Delta(O). Removing that interval from the scalar
simplex produces the exact forcing

\[
S_p(t)=-i^n w_p\sum_\nu\sigma_\nu
 J_{n-1}(f_{\nu,0}(E),...,f_{\nu,n-1}(E);t).                \tag{9}
\]

All previous phase prefixes are retained; each earlier frequency receives
kappa r_j dot E_I. The final frequency is independently checked against
the diagonal of (8). The source is evaluated from the RAW paths, not
Round45's initial-space-pruned coefficient records.

Write G_q=i^q v_q/(14400^q q!) and let H_m be the complete homogeneous
polynomial in the integer early frequencies (in units 1/14400). The
integer recurrence is

\[
v_{q+1}=v_qL_{B,int}
 -25^n\sum_{p,\nu}\sigma_\nu w_{p,int}
 H_{q-n+1}(f_{\nu,early,int}),                              \tag{10}
\]

with H_m=0 for m<0. It resums ALL later M paths within the lifted
generator. The finite-degree numerical approximation and its tail
are a separate issue, not a truncation by number of hopping events.

The executed degree is 100. For each raw branch let R bound both the
Hermitian norm of L_B and all its early scalar frequencies. The
matrix-valued n-simplex Taylor remainder through total degree N is

\[
|w|\frac{T^n}{n!}\frac{(RT)^{N-n+1}}{(N-n+1)!}.             \tag{11}
\]

This follows by scaling the simplex to unit size: its integrand is a
unitary exponential with generator a convex combination of L_B and
the real scalar frequencies. Sum absolute branch weights, multiply
each background's row error by sqrt(number of selected words), and
sum backgrounds. This explicitly converts a finite tensor row error
to a coefficient l1 error. It does not assume norm-equal CAR reconstruction.
At t=1 the cubic and five-factor errors are below 1.633e-66 and
3.809e-48 respectively.

## 4. Two essential counterchecks

### A tensor row is not a volume-uniform isometry

On a bare-low, exactly-one/site state with N sites, take the cubic row

\[
Q_N=\sum_{z\ne0}c_{L,z}^\dagger c_{L,z}c_{L,0}.
\]

Its coefficient l2 norm is sqrt(N-1), whereas
||Q_N Psi||=N-1. The ratio grows like sqrt(N-1), also on the same E0
initial class. Round43's special linear two-column isometry therefore
cannot be copied to cubic or quintic sources. Tests reproduce the
counterexample for N=2,4,8. This kills that shortcut, not the lift (5).

The safe reconstruction is ||sum F_I O_I|| <= sum ||F_I||. For the
local seeds here the l1 mass is bounded independently of ambient
volume by their finite raw seed census and the hopping estimates below.

### Initial null words must survive until after propagation

Two distinct annihilators at the same site kill the exactly-one/site
initial class, but not the whole Fock space. Their subsequent matter
commutator need not kill that class. Pruning these words before (5)
therefore changes the result. A mutant applying Round45's free-source
initial zero rule BEFORE resummation yields a different edge Gram
matrix. The new compiler retains all 238 raw cubic and 36 raw two-E
edge leaf paths. Literal CAR contractions and cancellations are handled
only by the actual final physical operator action.

Round45's pruning was correct for its freely propagated sources;
this does not retroactively invalidate that round or its bounds.

## 5. A volume- and flux-uniform bound on resummed electric leakage

For a single original cubic hopping row the maximum absolute weight
and length-weighted weight are

\[
\mu=77/96,\qquad j=41/48.                                  \tag{12}
\]

The low row has direct plus cross weight 3/4 and nonbacktracking
two-step weight 5/96. Counting those two-step lengths twice gives
3/4+10/96=41/48. The high row is smaller. For d literal legs put
lambda=d mu and nu=d j. Dropping hopping signs gives a positive
path envelope with mass at most exp(lambda u).

For an M suffix of duration u, the weighted integral of its added
current lengths is at most

\[
\frac{\nu u^2}{2}e^{\lambda u}.                            \tag{13}
\]

Indeed, in an m-hop path, inserting a length-weighted hop in any one
of m slots replaces one factor lambda by nu. The total remaining
free time after a marked hop has simplex mean u/2. Summing
m nu lambda^(m-1) u^m/m! times u/2 gives (13). The signs and electric
phases can reduce this envelope, but cannot increase it. No diagonal
electric-energy norm or extensive many-body V norm enters.

Use Round45's full raw seed moments B1,B2 and the scalar moments

\[
S_1=\frac{A_{1,L}+A_{1,H}}3=\frac{1243387}{1179648},\qquad
S_2=\frac{A_{2,L}+A_{2,H}}5=\frac{2173}{20736}.              \tag{14}
\]

Here A_{k,L/H} are the RATIONAL coefficients of C_L/C_H in Round45's
CAR bound, not the values containing the square roots. Every path
has d factors, hence summing those species counts and dividing by d
gives sum |w| times the scalar phase-difference moment.

For one-E leaves n=4,d=3; for the two-E leaf n=3,d=5. In both cases
n+k=5 and the last entry of every old phase-difference vector is zero.
The extra electric force bounds the source by kappa b times its
electric-phase gradient. At fixed seed times its norm envelope is

\[
\kappa^{k+1}b |w|\prod_{a=1}^k(|d_a|\cdot s)
 e^{\lambda u}\left(\sum_j|r_j|_1s_j+\frac{\nu u^2}{2}\right).
                                                                    \tag{15}
\]

There is one more outer full-H Duhamel integral. For the old-prefix
part, multiplication by u^m gives simplex moment weights one or m+1,
depending on whether the old gradient already contains u. Bounding
both by m+1 is conservative. The extra u^2/2 from (13) gives
binomial(m+2,2). Thus the complete leakage after the resummed leaf is

\[
\boxed{
\mathcal E_k(T)\le\kappa^{k+1}b\left[
 B_k T^7\sum_{m\ge0}\frac{(m+1)(\lambda T)^m}{(m+7)!}
 +\nu S_k T^8\sum_{m\ge0}
       \frac{\binom{m+2}{2}(\lambda T)^m}{(m+8)!}\right].}    \tag{16}
\]

The two old differences are retained as factors during the suffix
expansion; an M step shifts both branches' older frequencies equally.
They are not replaced by unrelated absolute phases. The new currents
in (13) are also retained in the bound, rather than reusing the old
electric gradient unchanged.

Both positive series are evaluated through m=24 with rational upper
tails. For a_m=binomial(m+p,p)x^m/(m+q)!, the consecutive ratio is
x(m+p+1)/((m+1)(m+q+1)), which decreases with m. Its value at the
first omitted term is below one in the declared domain |t|<=1.
The resulting geometric tail is an outward certificate, not a fit
to any physical residual. For a cubic subgraph with z first neighbors,
multiply (16) by z/6, still using full-cubic constants.

## 6. The new branch partition and its actual scope

Let R1M,R1E,R2M,R2E be Round45's four unexpanded leaf propagation
budgets. Replace ALL FOUR, not merely their matter parts:

\[
D_{46}=D_{45}-R_{1M}-R_{1E}-R_{2M}-R_{2E}
                    +\mathcal E_1+\mathcal E_2.             \tag{17}
\]

The full-H propagation after each new electric leakage preserves
operator norms. The old MEME/MMEE remainder and all later first-E
branches remain unchanged. At t=1, z=6:

| Component | Approximate amplitude upper bound |
|---|---:|
| Previous D45 | 1.128347545208343e-5 |
| Retained older branches | 2.600436351320539e-6 |
| Cubic resummed-leaf electric leakage | 7.276627161966979e-8 |
| Five-factor resummed-leaf electric leakage | 9.375618339384865e-11 |
| Complete D46 | 2.673296379123602e-6 |

This new IDEAL TARGET bound is more than four times smaller. It is
NOT a new computed three-dimensional occupation interval. The new
leakage starts at t^7, but the retained older branches start at t^6,
so D46 is still O(t^6). The independently verified suffix jets through
order seven are NOT a claim of matching the full Hamiltonian through
order seven. Full-parent fifth-order matching is preserved via the
unchanged lower source coefficients.

For any actually compiled common source, reconstruct its full Gram
before squaring and use the familiar physical occupation enclosure

\[
\left[\max(0,\sqrt q-\epsilon)^2,
       \min(1,(\sqrt q+\epsilon)^2)\right],\qquad
q=\|\widetilde Z_{46}\Psi\|^2,
\quad\epsilon=D_{46}+\epsilon_{num}+\epsilon_{configuration}.\tag{18}
\]

This round evaluates (18) on the complete EDGE, with no edge
configuration projection. At t=1:

| Edge preparation | New certified high occupation |
|---|---|
| Bare-low | [0.00036095532874, 0.00036098918920] |
| (LL-iHH)/sqrt2 | [0.49999679150340, 0.49999805170416] |
| (LL+iHH)/sqrt2 | [0.49999850068624, 0.49999976088915] |

All three contain the independently evolved full physical six-state
Hamiltonian results. The two Bell intervals are now separated at t=1
by more than 4.489e-7, despite identical one-site densities. This is an
EDGE correlation witness, not a bulk t=1 witness. The latest actually
executed bulk result remains Round45, where its Bell intervals at t=1
still overlap. A new bulk execution would have to supply its own
configuration-exit and CAR reconstruction certificate for the hats;
it cannot simply replace D45 by D46 around the old numerical center.

## 7. Reproduction, costs and next gate

Twenty regression tests check all literal cubic and five-factor words
against the original full-Fock commutator on every edge mask; signed
creator transports, Hermiticity and Gauss backgrounds; the no-M limit
against independent scalar simplexes; independent explicitly appended
M paths through seventh order; the unchanged fifth-order coefficients;
premature initial-null pruning; the nonisometry counterexample; hopping
and length bounds; positive series and their tails; simplex moments;
the exact retained-branch partition; independent polynomial degrees;
negative time and zero; common mixed patches; domain/phase/pin guards;
the actual edge readouts and bulk nonexecution boundary; and replay.

Real costs include four 64-state and six 1024-state auxiliary matrices,
238 and 36 raw seed paths, all 1088 extracted word/current records,
and exact degree-100 integer arithmetic. The original physical edge
problem itself has only six states. This is a test of a transferable
fixed-degree construction, NOT an edge speedup claim. No all-cubic
tensor graph or cubic numerical cost certificate is pretended to exist.

The next acceptance gate is an actual cubic execution of the lifted
inhomogeneous sources, with signed-current configuration exits and a
volume-safe coefficient-to-CAR error bound. The naive two-column l2
reconstruction and initial-null pruning are now explicitly excluded.
After that, the still dominant older first-E and MEME/MMEE branches
must be evaluated or resummed; an independent observable beyond n_H,0
remains useful. Neither this algorithm nor its bound selects the
physical vacuum/parameters, builds a chiral continuum or establishes
universal spin-two dynamics.

Only local theory-experiment files and catalog/continuation notes
change. No paper, website, verification result, ledger, scorecard,
proof-assistant result or peer-review status is promoted. No empirical
dataset, commit or push is part of this round.
