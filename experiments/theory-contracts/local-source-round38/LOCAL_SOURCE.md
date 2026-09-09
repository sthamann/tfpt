# An evaluated local source bound on the full cubic rotor lattice

2026-09-07. **NON-RH / unpromoted conditional research theorem.** This is a
finite-time, ambient-volume-independent interval for one physical local
observable of the unchanged parent. It does not calculate a complete 3D
trajectory, remove high fermions, or close a T1-T8 gate.

## 1. Target, preparation, and what changes from Round37

Keep the unrotated U(1) signed-wall Hamiltonian

\[
H=\frac\kappa2\sum_\ell E_\ell^2+
d\Gamma\begin{pmatrix}A+\beta A^2&\eta A\\\eta A&M I\end{pmatrix},
\qquad A_{xy}=aU_{xy},
\tag{1}
\]

with a=1/12, beta=1/4, eta=1/2, kappa=1/100, M=4 and Vmag=0. These are the
declared model choices, not physically selected TFPT constants. Both fermion
species and every rotor flux are retained. Time is in the model's units.

Consider a bulk vertex x of the genuine cubic lattice. Its local neighborhoods
must have the ordinary cubic path incidence: an interior of a sufficiently
large box, the infinite cubic exhaustion, or tori of side at least five suffice.
The special three- and four-step wrapping aliases of smaller tori are NOT used
with the sharp row constant below. The surrounding lattice may otherwise grow
without changing any constant in this calculation.

The reference is still one bare-low fermion per site and E_l=0 everywhere,
q_x=1. Finite local low/high species preparations, including arbitrary complex
superpositions and mixtures with one fermion per site, share this Gauss sector.
The theorem covers this whole family. The evaluated bare result uses initial
p_H,x=0 and p_L,y=1 for all six neighbors. This is not the dressed Haar state,
a selected vacuum, or a complete low-energy spectral subspace.

Round37 supplied a finite-window error plan whose direct state cost was
prohibitive. Here we evaluate the source equation for n_H,x=c_H,x^* c_H,x
directly. No spatial window or electric cutoff is introduced. The tradeoff is
a substantially wider interval than Round37's unexecuted high-precision plan.
The approach is an elementary Duhamel/CAR estimate, not a newly invented
simulation formalism. Strong-operator integral reasoning for unbounded onsite
terms is justified in [Nachtergaele and Sims](https://arxiv.org/html/1410.8174v1).
Connected-cluster simulation is a related established direction, described by
[Wild and Alhambra](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.020340);
we do not claim to have implemented its general algorithm or analytic continuation.

## 2. The exact high-mode equation

Write H=H0+V, retaining every backtrack in

\[
H_0=\frac\kappa2\sum_\ell E_\ell^2+
 \sum_y d_y n_{L,y}+M\sum_y n_{H,y},\qquad d=6\beta a^2=\frac1{96}.
\tag{2}
\]

Here d_y is the actual ambient backtrack coefficient beta a^2 deg_G(y).
At x and its nearest neighbors it equals d. At physical open outer edges
use their original degrees, not six; computational subwindows retain the
ambient backtracks as in Round37. This keeps H0+V exactly the original parent.

V consists of direct transported hoppings and nonbacktracking two-step low
hoppings. Its rotor dependence is multiplication by U(1) transporters, so
[V,U_l]=0 before any cutoff. Let tau_t(B)=e^(itH) B e^(-itH) and tau_t^0 denote
the H0 evolution. Because the high-high block in (1) is just M I, the CAR give

\[
\frac{d}{dt}\tau_t(c_{H,x})
=-iM\tau_t(c_{H,x})-i\eta a\sum_{y\sim x}\tau_t(U_{xy}c_{L,y}).
\tag{3}
\]

Its exact integrated form is

\[
\tau_t(c_{H,x})=e^{-iMt}c_{H,x}
-i\eta a\sum_{y\sim x}\int_0^t e^{-iM(t-s)}
                         \tau_s(B_{xy})ds,
\quad B_{xy}=U_{xy}c_{L,y}.
\tag{4}
\]

These are strong integral identities with bounded sources. Norm
differentiability of arbitrary rotor transporters under E^2 is not assumed.
The c_H and B operators are gauge-covariant, odd intermediate operators, not
physical gauge-invariant initial preparations. Their squared norm gives the
physical, even, gauge-invariant observable n_H,x. Intermediate charged sectors
are allowed algebraically and must not be confused with a new physical vacuum.

Define Y_x(t) by replacing tau_s(B_xy) in (4) with tau_s^0(B_xy), retaining the
entire mass and electric free phases. This is the ONLY approximation at this
stage. The error in that replacement is bounded below; it is not discarded as
an uncontrolled perturbative term.

## 3. Whole-Fock low-row bound and electric phase correction

For the low annihilator, the exact CAR identity is

\[
[V,c_{L,y}]=-\sum_z (A+\beta A^2_{off})_{yz}c_{L,z}
                    -\eta\sum_z A_{yz}c_{H,z}.
\tag{5}
\]

At a fixed gauge configuration a linear combination of annihilators has
operator norm equal to the Euclidean norm of its coefficient row. This follows
from {c(f),c(f)^*}=||f||^2 and (c(f)^*c(f))^2=||f||^2 c(f)^*c(f), on the WHOLE
Fock space. The U(1) coefficients commute, so the same result applies fiberwise,
followed by the supremum over gauge configurations. There is no factor for the
total number of particles or vertices.

In the local cubic row there are six direct low targets, six direct high
targets, six straight distance-two targets with one path each, and twelve
diagonal distance-two targets with two paths each. The direct and distance-two
targets are distinct. Bounding sums of paths to one mode by their absolute
coefficients gives

\[
\|[V,c_{L,y}]\|^2\leq C^2
=6a^2(1+\eta^2)+(6+12\cdot4)\beta^2a^4
=\frac{107}{2048}.
\tag{6}
\]

Flat transporters saturate the row bound; it is not obtained from a numerical
sample of gauge phases. The checker enumerates all 42 local monomials and their
30 mode targets on two actual cubic tori without short path aliases. A bare
matter row dropping the high cross term or A^2 contribution would be wrong.

For a transporter shifting E_l by sigma=+1 or -1, the exact free electric phase is

\[
\tau_s^0(U_l^\sigma)=U_l^\sigma
          e^{i\kappa s(\sigma E_l+1/2)}.
\tag{7}
\]

The inherited full-Fock electric force bound is ||[V,E_l]||<=b=53/288. Integrating
the commutator with exp(i kappa sigma s E_l) gives

\[
\|[V,e^{i\kappa\sigma s E_l}]\|\leq\kappa b|s|.
\tag{8}
\]

Use [V,U_l]=0, (5)-(8), and the scalar low-mode phase e^(-ids) to obtain

\[
\|[V,\tau_s^0(B_{xy})]\|\leq C+\kappa b|s|.
\tag{9}
\]

This is why the unbounded electric energy is not replaced by a fictitious
bounded electric Hamiltonian. Its effect survives explicitly through (7)-(9).
The commutator in (8) is generally nonzero.

## 4. Uniform source defect, with no environmental state vector

Duhamel for the difference between full and free source evolution gives

\[
\|\tau_s(B_{xy})-\tau_s^0(B_{xy})\|
\leq C|s|+\frac{\kappa b}{2}s^2.
\tag{10}
\]

One may first work in any finite volume, where V is bounded, and then use the
local commutator estimate (9) inside the strong integral. Although ||V|| itself
is extensive, it never appears in (10). Equation (4) now yields

\[
\|\tau_t(c_{H,x})-Y_x(t)\|
\leq D(T):=z\eta a\left(\frac C2T^2+\frac{\kappa b}{6}T^3\right),
\quad T=|t|,\ z=6.
\tag{11}
\]

The absolute time integral is conservative; it makes no assumption about
oscillatory cancellation of the source error. For the recorded |t|<=1 domain,
C<0.228574044348872 and D(1)<0.02864843378435. All these bounds are operator
bounds, not estimates on a finite set of prepared vectors. The same derivation
works on subgraphs of the cubic star with degree z<=6 and retained onsite d,
using the same conservative C and b; those are the independent benchmarks.

For finite-volume physical states of the declared class, (11) immediately
controls the Hilbert-Schmidt norm after applying rho^(1/2). Thus arbitrary
mixed or coherent local inputs are covered without multiplying the error by
the number of prepared states. Taking compatible lattice exhaustions preserves
the expectation bound. No continuum or Lorentz-symmetry statement follows.

## 5. Evaluate the source exactly on the specified inputs

Initially the relevant electric links are all in E=0. In (7) this leaves the
scalar phase e^(i kappa s/2). Distinct neighbors produce different shifted
link-flux states, so the B_xy input vectors are mutually orthogonal. They are
also orthogonal to the unshifted c_H,x input vector. These are exact flux
orthogonality statements, not an independence assumption about arbitrary
fermionic phases. For any input density in the class, set

\[
p_H=\langle n_{H,x}\rangle_0,\qquad p_{L,y}=\langle n_{L,y}\rangle_0,
\qquad \Delta=M-d+\kappa/2=\frac{9587}{2400}.
\]

The EXACT norm square of the approximating source is

\[
q(t):=\operatorname{Tr}(\rho Y_x(t)^*Y_x(t))
=p_H+(\eta a)^2\sum_{y\sim x}p_{L,y}
                 \frac{2(1-\cos(\Delta t))}{\Delta^2}.
\tag{12}
\]

The full high occupation is therefore enclosed by the triangle and reverse
triangle inequalities in Hilbert-Schmidt norm:

\[
\boxed{\quad
\max\{0,\sqrt{q(t)}-D(T)\}^{\,2}
\leq\langle n_{H,x}(t)\rangle
\leq\min\{1,(\sqrt{q(t)}+D(T))^2\}.\quad}
\tag{13}
\]

This is not an assertion that q(t) is the exact evolution. Nor does dependence
of q on diagonal marginals make input phases physically irrelevant. Different
coherent inputs with the same marginals may give different actual answers;
the SAME interval, rather than the same predicted exact value, covers them.

For the bare filled reference p_H=0 and all six p_L=1, the actual evaluated,
outward-rounded intervals are:

| Model time | Certified full cubic high occupation |
|---|---|
| 1/100 | [0.00000103570437, 0.00000104736828] |
| 1/10 | [0.00009707552031, 0.00010866560281] |
| 1/2 | [0.00128231410514, 0.00251145919838] |
| 1 | [0.00031949062781, 0.00565070454854] |

The t=1 interval excludes zero and is bounded away from one, uniformly in
ambient volume. It demonstrates finite-time leakage from this NAKED all-low
preparation. It is not a universal obstruction to dressed low-energy effective
theories or a proof about a physical mirror spectrum. The free-source central
quantity at t=1 is about 0.00216436483, but that number alone is NOT the answer.

Unlike an initial derivative, (12) retains the full mass/electric phase and
(13) bounds every omitted source contribution at finite time. The original
t^2 coefficient 1/96 is recovered as t tends to zero. At t=1 that leading
polynomial alone would instead give 1/96 and cannot replace (13).

Cosines are evaluated through an exact rational degree-80 complex exponential
polynomial, with the unitary remainder |Delta t|^81/81!. Square roots are
enclosed by exact integer-square inequalities on a 1e-24 grid. Both the
trigonometric and square-root rounding are propagated outwards. No floating
value or finite reference answer is used to tune the model or the error.

## 6. Independent complete dynamics and what it does not establish

Two auxiliary benchmark geometries are solved in their ENTIRE physical Gauss
sector, with the same parameters and inherited d=1/96 onsite backtracks:

* An edge: two vertices, two fermions, six physical states.
* A six-leaf star: seven vertices, seven fermions, 3,432 physical states and
  64,416 stored Hamiltonian entries.

On these trees Gauss fixes E_l=N_leaf-1 on each edge. Its allowed values happen
to be -1,0,1 because there are only two fermion modes per leaf; this is not an
electric cutoff and no physical tree flux has been omitted. The tree has no
independent cycle rotor. The star is a full interacting benchmark, NOT the full
cubic lattice or a replacement for the analytic volume-uniform proof.

The independent full-parent rational time evolution gives at t=1:

| Complete benchmark | High occupation at the root |
|---|---|
| Edge, bare low input | [0.00036097226121, 0.00036097226122] |
| Six-leaf star, bare low input | [0.00219096851702, 0.00219096851703] |
| Edge, equal low/high root input, Fock-basis coefficient -i | [0.49977067776822, 0.49977067776823] |
| Edge, equal low/high root input, Fock-basis coefficient +i | [0.50058909763542, 0.50058909763543] |

Each answer lies in (13) for its degree and initial marginals. The last two
answers explicitly refute interpreting the phase-insensitive q as a complete
phase-resolved prediction. The source-error intervals remain valid.
The phase labels refer to psi_bare +/- i psi_root_high in the stored Fock basis
with occupied mode indices in increasing order, followed by normalization. A
different local fermion ordering must carry its associated sign conversion.

The tests additionally compare the whole charged source vector
U_(N-1)(t)^* c_H U_N(t) psi to Y_x(t) psi on the edge, with rational evolution
in both charge-covariance sectors and separate polynomial remainders. This is
stronger than only comparing occupations. These intermediate sectors do not
constitute new physical initial-state choices. Further checks cover the CAR
row norm, both transporter orientations, the nonzero electric phase
commutator, exact original-parent gap, all local source kets, Hermiticity,
two Taylor degrees, arbitrary-marginal interval use, pins and artifact replay.

## 7. Costs, claim boundary, and next target

The standalone local readout needs only a few scalar rational computations and
fixed source constants; it stores neither a spatial window nor a parent state
vector. The full certificate build additionally checks cubic incidence and the
benchmark sectors. The star benchmark's degree-100 evolution performs about
12.88 million real integer coefficient visits plus vector operations. Its
big-integer arithmetic is a real cost, not eliminated by the local formula.

There is NO like-for-like speedup claim against Round37's <1e-9 precision plan:
the present t=1 interval is about 0.00533 wide. What is achieved is an actually
evaluated, nontrivial full-cubic interval for ONE source at unit model time,
with all environmental and rotor effects bounded analytically. Neither all
four sources nor a common reduced generator have been solved by this step.

The next concrete target is a second source iteration including low-mode
feedback and electric phase changes, with an explicit residual, to narrow
the unit-time interval and then control the other physical sources. Spectral
mirror elimination, chirality, a selected vacuum and parameters, the continuum
limit, spin-two gravity and the full T1-T8 conjunction remain open. This written
argument and exact checker are not a proof-assistant formalization or external
peer review. No empirical, paper, website, ledger or public TOE promotion follows.
