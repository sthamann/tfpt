# Fifth-order electric sources with a sixth-order ideal remainder

2026-09-07. **NON-RH / conditional, unpromoted theory experiment.**
Three further one-electric sources and the first two-electric source are
evaluated for the unchanged compact U(1) parent. The ideal source now
matches through fifth time order; its omitted-electric bound begins at
sixth order. The separately bounded finite-configuration approximation
does NOT acquire fifth-order exactness. No full gauge solution or T1-T8
closure is claimed.

## 1. Unchanged parent, initial class and exact branch partition

Keep

\[
H=H_E+d\Gamma(h),\qquad H_E=\frac\kappa2\sum_\ell E_\ell^2,
\qquad h=\begin{pmatrix}A+\beta A^2&\eta A\\\eta A&MI\end{pmatrix},
\quad A_{xy}=aU_{xy},                                           \tag{1}
\]

with a=1/12, eta=1/2, beta=1/4, kappa=1/100, M=4 and Vmag=0.
The free generator H0 retains the original low onsite backtracks
d=1/96, the high mass, and the full electric energy. V contains the
remaining original direct and nonbacktracking two-step monomials. All
couplings are declared assumptions, not parameters selected by TFPT.

The physical readout is n_H,0. The initial class has E=0 and exactly one
L/H fermion per site, arbitrary coherent/mixed/entangled species states
on a finite patch, and bare-low filling elsewhere. The fixed physical
Gauss background is one per site. This round does not introduce a dressed
vacuum, rotate fields, remove the low backtracks, or replace the cubic
parent by a tree. Independent finite graphs below are controls, not the
source of the three-dimensional result.

For a gauge coefficient F and a CAR word O, use the exact split

\[
[V,FO]=F[V,O]+[V,F]O.                                        \tag{2}
\]

Label these branches M and E respectively. The first interaction on
c_H,0 is M. Round43's exact matter row P_infinity sums all purely M
branches, while Round44 evaluates it with a separate configuration-exit
certificate. The retained ideal source is now

\[
\begin{split}
Z_{45}=P_\infty+C_{ME}+C_{MEM}+C_{MME}
 +C_{MEMM}+C_{MMEM}+C_{MMME}+C_{MEE}.                         \tag{3}
\end{split}
\]

Each displayed electric source is freely propagated with ALL its mass
and electric phases, not replaced by its leading time coefficient.
MEMM, MMEM and MMME have four interactions and one phase difference;
MEE has three interactions and two phase differences. All four first
contribute at time order five. MEME and MMEE, later first-electric
branches, and propagation of the new terms remain in the explicit bound.
Equation (3) is not an all-order electric resummation.

The estimates use strong integral identities, not operator-norm
differentiation of unbounded rotor generators. In finite ambient volumes
H0 is self-adjoint and V is bounded. For background on this distinction,
see [Nachtergaele and Sims, On the dynamics of lattice systems with
unbounded on-site terms in the Hamiltonian](https://arxiv.org/html/1410.8174v1). The branch formulas,
constants and computations below are model-specific work, not results
asserted by that reference. The omitted-source bounds are uniform in
ambient volume and initial flux. Expectation bounds pass to compatible
thermodynamic limits where the dynamics exists; a continuum construction
is not supplied here.

## 2. Phases and signs of the four new sources

Let epsilon_L=d, epsilon_H=M. A path has cumulative integer link currents
r_j during free intervals s_j; s_0 is its initial high-source interval.
For n interactions define the oriented simplex integral

\[
J_n(f;t)=\int_{s_j\ge0,\,\sum_{j=0}^n s_j=t}
 \exp\!\left(i\sum_{j=0}^n f_js_j\right)\,ds_1\cdots ds_n   \tag{4}
\]

for positive t, with the oriented continuation for negative t. On
nonzero initial electric flux E, add kappa r_j dot E to every branch's
j-th frequency, j>=1. This common addition leaves every electric phase
difference unchanged. The final frequency is always
kappa |r_n|^2/2 plus the free CAR word energy.

The implementation stores weights as integers over 576^n and frequencies
as integers over 2400. Its signed weight w is the negative of the raw
nested-commutator coefficient, including the negative initial
annihilator row. The source prefactor is therefore -i^n w: +w for ME,
+i w for the three-interaction sources, and -w for the new four-interaction
sources. Confusing stored weights with raw commutator coefficients would
reverse the fifth-order correction.

### 2.1 Append M to MEM or MME

Take the two old frequency lists f_0,f_1, prefixes r1,r2,r3 and word
O=c_a^dagger c_b c_y. Apply the derivation [V,O] to each of its three
legs. The creator uses the TRANSPOSED hopping row and positive sign;
each annihilator uses the stored row and negative sign. Let the selected
leg shift be p4, r4=r3+p4, and O' its updated word. Both new lists are

\[
f'_\nu=\left(f_{\nu,0},
 f_{\nu,1}+\kappa r_1\!\cdot p_4,
 f_{\nu,2}+\kappa r_2\!\cdot p_4,
 f_{\nu,3}+\kappa r_3\!\cdot p_4,
 \frac\kappa2|r_4|^2+\Delta(O')\right),\quad \nu=0,1,          \tag{5}
\]

where Delta(c_a^dagger c_b c_y)=epsilon_a-epsilon_b-epsilon_y.
The old electric difference vector acquires a zero final component.
Multiply its stored weight by the new hopping weight and leg sign.
The contribution is -w [J4(f'_0)-J4(f'_1)] U^r4 O'. Both the
transposed creator transport and the shift of ALL earlier frequencies
are essential.

### 2.2 MMME

After three M steps let the modes be j1,j2,j3, with prefixes r1,r2,r3.
A force monomial w4 U^p4 c_a^dagger c_b gives r4=r3+p4 and
O=c_a^dagger c_b c_j3. Its first list is

\[
\begin{split}
f_{0,0}&=-M,\\
f_{0,k}&=\frac\kappa2(2r_k\!\cdot r_3-|r_k|^2)-\epsilon_{j_k},
 \quad k=1,2,3,\\
f_{0,4}&=\frac\kappa2|r_4|^2+\Delta(O),\\
f_1-f_0&=\kappa(0,r_1\!\cdot p_4,r_2\!\cdot p_4,r_3\!\cdot p_4,0).
\end{split}                                                     \tag{6}
\]

Its stored weight is +g w2 w3 w4, g=eta a. Its contribution has the
same -w [J4(f0)-J4(f1)] convention as (5). The force census inspects
the UNION of all three prefix supports, including currents subsequently
cancelled by later hops. Testing only the final current loses terms.

### 2.3 MEE: keep the literal five-factor word

Start with an ME path, prefixes r1,r2, old word c_a^dagger c_b c_y,
and frequencies (-M,alpha0,gamma). The next force monomial
w3 U^p3 c_u^dagger c_v yields r3=r2+p3 and the LITERAL word

\[
O_5=c_u^\dagger c_v c_a^\dagger c_b c_y.                      \tag{7}
\]

It is not an already normal-ordered quintic. Set

\[
\begin{split}
f&=(-M,\alpha_0,\gamma,\kappa|r_3|^2/2+
 \epsilon_u-\epsilon_v+\epsilon_a-\epsilon_b-\epsilon_y),\\
d_1&=(r_1\!\cdot p_2,0,0),\qquad
d_2=(r_1\!\cdot p_3,r_2\!\cdot p_3,0),\\
\delta_i&=\kappa(0,d_i).
\end{split}
\]

\[
C_{MEE,p}=i w\{J_3(f)-J_3(f+\delta_1)-J_3(f+\delta_2)
                 +J_3(f+\delta_1+\delta_2)\}\,U^{r_3}O_5.     \tag{8}
\]

Here w is the old stored ME weight times w3. The two differences factor
pointwise into (1-exp(i delta1 dot s))(1-exp(i delta2 dot s)). The exact
CAR identity

\[
O_5=\delta_{va}c_u^\dagger c_b c_y
       -c_u^\dagger c_a^\dagger c_v c_b c_y                   \tag{9}
\]

includes a cubic contraction. The evaluator applies the literal ordering
in (7), so both pieces are automatically retained. A separate all-mask
Fock test checks (9); dropping the contraction is not allowed.

## 3. Exact cubic census and symmetry restoration

All first high-source orientations are related by proper rotations of
the unchanged cubic parent. Enumerate one first current along the x
axis, with its actual sign. Restore its six images by

\[
(x,y,z)\longmapsto \text{coordinates with }
 x_{axis}=s x,\quad x_{axis+1}=s y,\quad x_{axis+2}=z,
\quad axis=0,1,2,\ s=\pm1,                                  \tag{10}
\]

where subscripts are cyclic. Each map has determinant +1. Link endpoint
ordering and current signs are transformed together. Dot products and
scalar frequency kernels are invariant. No rotational symmetry of the
USER'S INITIAL STATE is assumed: all six images are evaluated on that
same state and their contributions are added before taking squared norms.

The full raw census is

| Source | Raw paths |
|---|---:|
| MEMM | 2199312 |
| MMEM | 1852848 |
| MMME | 941664 |
| MEE | 6936 |
| Total | 5000760 |

Norm weights are accumulated on this FULL-Fock raw census before using
any zero rule specific to the initial subspace. Both (7) and cubic words
end in two annihilators. Identical modes kill the word identically;
different modes at the same site kill it only on the exactly-one/site
initial class. After the norm census, apply these zero rules and
canonicalize these last two annihilators with their CAR sign. Collect
equal word/current/frequency records exactly, with no magnitude pruning.
Simplex symmetry permits sorting frequencies within each J_n.

For the representative direction this gives 826407 one-E groups and
2854 two-E groups. At t=1 they produce respectively 241623 and 828
nonzero word/current coefficients, using 1102 and 141 frequency kernels.
The common response streams 1449738 one-E images and 4968 two-E images
into actual physical output vectors. Equal final mask/current states
are collected before the Gram matrix is formed. Retaining only
representative probabilities would lose interference and is not used.

At degree 80 the scalar Taylor remainder for (4) is bounded by

\[
\frac{T^n}{n!}\frac{(T\max_j|f_j|)^{81}}{81!},\quad T=|t|.    \tag{11}
\]

The absolute signed-group weights and all six images are included in
the arithmetic error. At t=1 the new one-E and two-E amplitude errors
are below 5.972e-51 and 2.289e-51. This evaluation error applies on E0
inputs: no finite polynomial is claimed to approximate an unbounded-E
phase in whole-spectrum operator norm. The mathematical remainder in
the next section is a different, flux-uniform estimate.

## 4. Derive the new sixth-order remainder without dropping branches

Use the pinned full-Fock row and electric commutator bounds

\[
C_L=\sqrt{107/2048},\quad C_H=\sqrt{1/96},\quad b=53/288,
\qquad \|[V,e^{i\theta\cdot E}]\|\le b|\theta|_1.             \tag{12}
\]

For a literal word, the product rule gives ||[V,O]|| no greater than
the sum of the appropriate C_species over ALL its factors, including
all five factors of (7). This bound does not require normal ordering.

For an n=4 one-E path let d=(f1-f0)/kappa after excluding the initial
zero component, and ell_j=|r_j|_1. Define

\[
m_1=\sum_j|d_j|,\qquad
e_1=m_1\sum_j\ell_j+\sum_j|d_j|\ell_j.                       \tag{13}
\]

For an n=3 two-E path put a_j=|d1_j|, b_j=|d2_j| and

\[
\begin{split}
m_2={}&(\sum a)(\sum b)+\sum ab,\\
e_2={}&(\sum a)(\sum b)(\sum\ell)+(\sum ab)(\sum\ell)\\
 &+(\sum a\ell)(\sum b)+(\sum b\ell)(\sum a)
       +2\sum ab\ell.                                      \tag{14}
\end{split}
\]

These are simplex moments, not fitted error factors. In general

\[
\int_{\sum_{j=0}^q s_j=T}\prod s_j^{\alpha_j}\,ds
 =\frac{\prod\alpha_j!}{(q+\sum\alpha_j)!}
     T^{q+\sum\alpha_j}.                                    \tag{15}
\]

After one extra Duhamel integral, the one-E matter remainder uses a
first moment on the five-simplex; the two-E matter remainder uses a
second moment on the four-simplex. Both have denominator 6! and power
T^6. One further electric commutator multiplies by kappa b sum ell_j s_j,
giving second and third moments respectively, denominator 7! and T^7.
Three repeated indices in (14) have factorial weight six; two repeated
indices weight two; three distinct indices weight one.

Exact raw-path sums A_i=sum |w| m_i sum_word C and B_i=sum |w| e_i give

\[
\begin{aligned}
A_1&=\frac{75222083}{31850496}C_L+
        \frac{3186533}{3981312}C_H,&
B_1&=\frac{117262271}{11943936},\\
A_2&=\frac{8927}{20736}C_L+\frac{323}{3456}C_H,&
B_2&=\frac{77543}{110592}.                                   \tag{16}
\end{aligned}
\]

The unexpanded propagations of the new terms are therefore bounded by

\[
R_{1M}=\frac{\kappa A_1T^6}{6!},\quad
R_{1E}=\frac{\kappa^2bB_1T^7}{7!},\quad
R_{2M}=\frac{\kappa^2A_2T^6}{6!},\quad
R_{2E}=\frac{\kappa^3bB_2T^7}{7!}.                            \tag{17}
\]

For an original cubic subgraph with z first neighbors, use z/6 times
these conservative full-cubic constants. A reduced finite-graph census
does not replace (16). The declared numerical domain is |t|<=1,
1<=z<=6. There is no extensive norm of V in (17).

Let E3 be Round40's first-electric branch after three matter steps;
let R3M and R3E be Round42's further matter and electric propagation of
MEM/MME, and let R_MEE,old be its first double-electric remainder. The
three replaced budgets cover disjoint newly evaluated branches:

\[
\boxed{
D_{45}=D_{43}-E_3-R_{3M}-R_{MEE,old}
                +R_{1M}+R_{1E}+R_{2M}+R_{2E}.}              \tag{18}
\]

R3E is RETAINED: it covers MEME and MMEE and starts at order six.
The first-electric levels from four matter steps onward are also
retained, with their infinite tail certificate inherited from Round43.
Purely M propagation is still P_infinity. Thus no unexpanded branch is
silently removed and

\[
\|\tau_t(c_{H,0})-Z_{45}(t)\|\le D_{45}(T)=O(T^6).           \tag{19}
\]

At T=1 in the cubic interior:

| Bound component | Approximate amplitude upper bound |
|---|---:|
| Previous D43 | 3.463893107534404e-5 |
| New R1M | 8.632173714888443e-6 |
| New R1E | 3.584789663316531e-8 |
| New R2M | 1.499188736866721e-8 |
| New R2E | 2.560187261353297e-11 |
| Complete D45, including retained old branches | 1.128347545208343e-5 |

The theoretical electric upper bound decreases by about 67.4%. This
is not a measured reduction in the exact error, nor is a positive
remainder upper bound a lower bound on unavoidable error.

## 5. Same-source physical readouts and independent full-parent checks

Reuse Round44's depth-six auxiliary configuration set, with 46874
particle/current/species states and ALL 652522 outgoing configuration
rows. Its unchanged all-exit certificate is included. In particular,
epsilon_aux(t=1) is below 1.315e-7; at shorter times it may begin at
order t^4. Equation (19) does NOT claim that this finite configuration
approximation exactly reproduces fifth-order three-dimensional jets.

For the computed common source Z_tilde form
q=||Z_tilde Psi||^2, adding linear, cubic and literal five-factor
amplitudes before squaring. The physical occupation is enclosed in

\[
\left[\max(0,\sqrt q-\varepsilon)^2,
       \min(1,(\sqrt q+\varepsilon)^2)\right],\quad
\varepsilon=D_{45}+\epsilon_{aux}+\epsilon_{electric,num}.    \tag{20}
\]

All arithmetic is rational, with outward square-root/Taylor enclosures.
The response uses one common patch basis, retains off-diagonal entries,
and supports positive normalized mixed input densities via the inherited
Gram interface. The implemented patch interface has at most three
prepared sites (dimension eight); the rest of the cubic lattice remains
bare filled, not removed.

At t=1 the actual full-cubic bare-low result is

**[0.00219685812592, 0.00219899873816]**.

The previous Round44 interval was
[0.00219466789203, 0.00220118831043]. The new interval is more than
three times narrower, with both source and configuration errors included.

For neighboring-site states (LL-iHH)/sqrt2 and (LL+iHH)/sqrt2,
bare filling elsewhere, the new t=0.3 results are

| Preparation | Certified high-occupation interval |
|---|---|
| Minus phase | [0.50034548173813, 0.50034550547455] |
| Plus phase | [0.50034542873258, 0.50034545246899] |

The exact rational interval gap exceeds 2.926e-8. Both preparations have
identical one-site density matrices I/2 and initial E0, so the separated
readouts detect correlations. This extends the previous certified time
0.2 to 0.3 under the same assumptions. At t=1 their intervals are
[0.50087779544505, 0.50091011044334] and
[0.50087947351658, 0.50091178856899], which STILL OVERLAP.
No new t=0.5 result is claimed by this round.

Independent checks use the FULL physical parent on an edge and on a
four-cycle, not its split-source generator. All four exactly-one/site
E0 edge columns match the ideal source's time coefficients through
order five. Omitting MEE leaves orders zero through four unchanged but
fails at order five. A separate finite-time physical-sector calculation
checks bare and both Bell preparations on each graph: all six certified
full-parent intervals at t=1 lie inside (20). The edge physical sector
has dimension six; the cycle calculation has 2310 physical states and
includes its certified omitted winding tails. These finite controls
check the implementation, not a transfer of their physics to the bulk.

## 6. Correlation hierarchy: a sufficient ceiling, not a closure theorem

M acts by a bilinear CAR derivation and preserves word degree. Each E
prepends a creator/annihilator pair. A retained sector with at most k
electric events therefore has literal degree at most 2k+1. Normal
ordering produces words of that degree and lower; (9) exhibits the
first contraction explicitly.

On the exactly-one/site initial class, a nonzero normal-ordered word
has at most one annihilator per site. For two terms of degrees d,d', a
nonzero Gram cross term requires the SAME final flux and site-charge
pattern q. Let C be the support of nonzero q. A neutral spectator site
costs at least two fermion factors. Each charged site costs at least
|q_x| factors, so the union of the two supports obeys

\[
|S\cup S'|\le |C|+\frac{d-\sum|q_x|}{2}
                     +\frac{d'-\sum|q_x|}{2}
             \le\frac{d+d'}2.                              \tag{21}
\]

Consequently linear/quintic cross terms require at most three-site
species densities, cubic/quintic at most four-site, and quintic/quintic
at most five-site. More generally a bounded-k electric source has a
sufficient (2k+1)-site reduced-density ceiling under this initial-class
restriction. This is not a truncation of the exact initial-state
correlations, nor an exact finite hierarchy for the full dynamics.

The cubic MEE fifth-order coefficient has 1596 nonzero normal-ordered
quintic terms after initial-class zero rules. Its charge/flux-compatible
support pairs reach five sites. However this candidate-support census
does NOT prove irreducible five-site dependence of the final readout:
remaining cancellations in the Gram observable have not been excluded.
The record explicitly sets
`irreducible_five_site_readout_dependence_proved=false`.

## 7. Reproducibility, real costs and the next acceptance gate

The deterministic record pins Round44 and the transitive parent chain;
it hashes the checker, tests and both documents. Twenty regression tests
cover the independent full-parent fifth jets; necessity of MEE; literal
CAR contractions; exact phases, large initial flux and negative time;
complete raw norm census; prefix cancellation; independent simplex
moments; symmetry restoration against unreduced preceding cubic sources;
projection AFTER the full norm census; direct charged Fock Gram columns;
mixed three-site preparations; all retained error parts; the sufficient
correlation ceiling; actual bulk intervals and their nonseparation
boundary; six finite-parent enclosures; guards and deterministic replay.

The 5000760 raw paths, 829261 representative groups, exact-integer
denominators, 46874-state auxiliary matrix and 652522 exit rows are real
costs. At t=1 the four patch-basis columns contain respectively 127533,
180991, 130768 and 182601 nonzero collected electric outputs. Symmetry
restoration and arithmetic are not free; no end-to-end speedup is claimed.
The validation record does not freeze machine-dependent runtimes.

The next acceptance gate is to propagate or resum the now-explicit
cubic and five-factor sources without losing the M/E partition,
contractions, mixed-state interference or a volume/flux-uniform bound.
At least MEME and MMEE remain omitted. The new one-E matter propagation
bound R1M is still a major component; enlarging only the auxiliary
configuration set cannot remove it. Another useful independent gate is
a physical observable beyond n_H,0. None of these steps by itself
selects the parameters/preparation, establishes a chiral continuum or
universal spin-two sector, or solves all T1-T8 obligations.

This round changes only its theory-experiment files and the experiment
catalog/continuation notes. No paper, website, verification result,
ledger, scorecard, proof-assistant result or peer-review status is
promoted. No observational dataset is used.
