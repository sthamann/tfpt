# Ground-state coercivity and nontrivial low-energy Wilson response

2026-09-08. **NON-RH / unpromoted mathematical theory experiment.**
Same full compact-U(1) rotor/CAR parent and parameters as
`neutral-ground-state`; no electric cutoff, new magnetic term, chemical
potential, fitted input, selected vacuum or T1-T8 completion.

The result is a stronger ground-state estimate and a spectral-moment
constraint in the already constructed symmetric periodic ground-state
representations. It is NOT a computation of a gap, a proof of gaplessness,
a phase identification or a continuum construction. The infinite-volume
reasoning below is not replaced by the finite execution checks.

## 1. Exact low/high matrix structure of the original Hamiltonian

On a cubic torus of side L>=5 let A_U be the Hermitian covariant nearest-
neighbor adjacency matrix, with unitary link entries. Its operator entries
are functions of the mutually commuting U(1) link coordinates. Electric
operators remain fully dynamical; no link configuration is frozen in H.
With low and high annihilator columns l,d, the EXACT matter Hamiltonian is

  H_m = l^* h_l l + M d^*d + w(d^* A_U l + l^* A_U d),
  h_l = a A_U + beta a^2 A_U^2,
  a=1/12, beta=1/4, w=eta a=1/24, M=4.

The diagonal backtracks in A_U^2 are the existing epsilon_L=1/96 onsite
term; all original nonbacktracking two-step terms are present. The checker
compares the full Laurent-monomial matrices on L=5 and, in tests, L=6.
The trace here is the finite SITE-MATRIX trace, not a Hilbert-space trace:

  ||A_U|| <= 6,     Tr A_U^2=6N,
  h_l <= R I,       R=6a+36 beta a^2=9/16,
  Tr h_l=epsilon_L N,       N=L^3.

The norm bound is pointwise in gauge coordinates, hence an operator bound
on the uncut rotor Hilbert space. It is not a numerical phase sample.

## 2. Holes remove the spurious extensive interaction cost

Define holes b_x=l_x^*. Their number N_b=N-N_L equals N_H in the neutral
Gauss sector. CAR and commutation of the gauge coefficients with matter
give, as exact operators,

  l^* h_l l = Tr h_l - b^* h_l^T b,
  l^* A_U^2 l = 6N - b^*(A_U^2)^T b <= 6N.

Transposition is on site indices; the transposed Hermitian matrix remains
positive when the original matrix is positive, since its coefficients
belong to a commuting gauge-coordinate algebra. This step would not be
automatic for noncommuting matrix-valued gauge entries. The hole Gram
term is positive, not discarded through an unjustified occupancy guess.

For ANY scalar t>0, completing the square gives

  0 <= t sum_x (d_x+(w/t)(A_U l)_x)^*
                 (d_x+(w/t)(A_U l)_x),

and hence the original cross term is bounded below by

  w(d^*A_U l+l^*A_U d) >= -t N_H - (w^2/t) l^*A_U^2 l
                       >= -t N_H - cN/t,
  c=6w^2=1/96.

Let D=M-R=55/16. In the neutral sector the FULL Hamiltonian satisfies

  H >= epsilon_L N + (kappa/2) sum_links E_l^2
                   + (D-t) N_H - cN/t,       kappa=1/100.       (1)

This is an operator/form inequality, not a Schrieffer-Wolff approximation.
The checking identity before inequalities holds on all 256 Fock masks of
the original ambient-degree-six plaquette and arbitrary integer flux.
The executable tests use three very different backgrounds and two t
choices, retaining every nearest, two-step and diagonal term.

At t=D, (1) and the old bare variational bound imply

  E0,L/N >= epsilon_L-c/D=13/1760,
  <sum_three_outgoing E_(x,a)^2> <= 2c/(kappa D)=20/33.

Translation invariance of the normalized ground-space projector is used
to obtain the LOCAL bound. The old bound 2525/24 was valid but far looser.
At t=D/2, dropping the electric term and using the same upper energy gives

  <n_H,x> <= 4c/D^2=32/9075, approximately 0.003526170799.

These are upper bounds, NOT computed ground-state densities. In particular
the spectral meaning of D is only this coercivity inequality; D or M must
not be relabeled as the physical many-body gap.

## 3. Dimer improvement and symmetric thermodynamic states

The previously verified disjoint matching trial state lowers the energy
by g=239675/551523414 per dimer. Pair successive x coordinates on every
row. For all L, including odd L, the number of dimers per site is

  m_L/N=floor(L/2)/L.

Thus E0,L/N <= epsilon_L-[floor(L/2)/L]g. The finite-volume electric
estimate is C_L=20/33-[2 floor(L/2)/L]g/kappa, with thermodynamic limit

  C_* = 20/33-g/kappa = 1706590130/3033378777
      approximately 0.5626037021620528.                         (2)

Odd volumes approach the same bound with excess g/(kappa L). No assumption
that the trial state IS a ground state enters this argument. The limiting
energy-density brackets for finite-volume ground energies are

  13/1760 <= liminf E0,L/N <= limsup E0,L/N
            <= epsilon_L-g/2 approximately 0.0101993821471739.

Existence of an actual limit of energy densities is not proved here.

The finite-volume normalized ground-space projectors inherit translations,
coordinate permutations and lattice reflections. The checker verifies
these transformations on all 6000 original directed hopping monomials of
the L=5 torus. The corresponding fermion permutation is implemented by
second quantization; no choice of signs for ground vectors is needed.
Reflections reverse oriented E and permutations exchange axes, so

  <E_l>=0,       <E_l^2> <= C_L/3

on each torus. These are symmetries of the prescribed density, not a proof
that every pure ground state has them. The earlier local trace-norm
compactness construction applies with the stronger bound. First electric
moments pass by uniform second-moment control; second moments pass only as
upper bounds by lower semicontinuity. The resulting symmetric periodic
cluster states carry the same dynamics and nonnegative physical GNS K.
See the model-specific construction in `neutral-ground-state/README.md`.
The general GNS/spectral framework is described by
[Rainer Verch, Lecture Notes, Section 1](https://arxiv.org/html/2507.00900v1).

## 4. An exact Wilson-loop energy identity, with full electric domain

For an oriented elementary plaquette set W=product_l U_l^(p_l), with
p_l=+1 or -1 on its four boundary links and zero elsewhere. Define
S=sum_l p_l E_l. Gauss commutes with W. Also W commutes with ALL of H_m,
because its gauge factors and all those of H_m are mutually commuting
link-coordinate functions, and W contains no matter operators. However
W does NOT commute with the electric Hamiltonian:

  W^* H W - H = kappa(S+2),
  [H,W] = kappa W(S+2).                                       (3)

Equation (3) holds on the full finite-volume electric domain. Integer flux
translation preserves that domain. Since H is a bounded perturbation of
H0, a finite-volume ground vector is in it; W times that vector is also
in it. This is NOT differentiation in the operator-norm generator domain
of W, which the predecessor analysis explicitly showed to be unavailable.

Let mu_L be the positive spectral measure of W acting on the neutral
ground projector, for H_L-E0,L. Its total mass is one. In the convention
rho_L(W^*alpha_t(W))=integral exp(+it lambda) dmu_L(lambda), (3) gives

  supp mu_L subset [0,infinity),
  m1,L = integral lambda dmu_L = kappa <S+2> = 2kappa=1/50,
  m2,L = integral lambda^2 dmu_L = kappa^2 <(S+2)^2>.

From <S>=0 and S^2 <=4 sum_boundary E_l^2,

  m2,L <= kappa^2(16 C_L/3+4).                                (4)

All four electric operators commute, so the quadratic Cauchy inequality
is also a joint spectral/form inequality. The independent full-H control
checks (3) on every plaquette Fock mask at three unrestricted integer
backgrounds. It does not diagonalize a truncated plaquette Hamiltonian.
An additional full-cubic control on 125 sites/375 links retains all 6000
original terms, including those leaving the selected plaquette. It checks
three Fock inputs (neutral and charged), with loop backgrounds 0,-7,+11.
A second-size regression repeats this on 216 sites/648 links with all
10368 terms. These are exact H actions, not torus ground diagonalizations.

## 5. Nonzero physical excitation weight survives the infinite limit

Previous compact-time convergence of the same dynamics and local state
convergence give convergence of the correlation functions of W. The
limiting correlation is continuous by the existing strong GNS result.
Equivalently the finite positive measures converge weakly to the spectral
measure mu of pi(W)Omega for the physical generator K. Tightness also
follows directly from the uniform second-moment bound.

It is essential not to exchange unbounded moments without control:

  integral_(lambda>R) lambda dmu_L <= (sup_L m2,L)/R.

Thus the FIRST moment is uniformly integrable and passes with equality.
The SECOND moment passes only by lower semicontinuity and (4):

  m1=1/50,       m2 <= M2=kappa^2(16 C_*/3+4).

Now apply Cauchy-Schwarz solely on the POSITIVE spectral axis:

  mu((0,infinity)) >= m1^2/M2
                   = 9100136331/15926496851
                   approximately 0.5713834257549624.           (5)

The measure therefore has nonzero excitation content even if the ground
space is degenerate. Its positive support obeys

  inf supp(mu|_(0,infinity)) <= B=M2/m1
       =15926496851/455006816550
       approximately 0.03500276539098807.                      (6)

Precisely, every interval (0,B+epsilon), epsilon>0, has positive spectral
weight. An atom at B, an eigenvector at the infimum or a discrete particle
branch is NOT asserted. Since mu is a K spectral measure, the infimum of
the positive spectrum of K is at most B as well. This permits a zero gap;
it is NOT a positive lower gap bound.

A more robust finite-window statement follows without resolving a pole:
for R=2B, splitting the first moment at R and using its second-moment tail,

  mu((0,R]) >= (m1-M2/R)/R = m1^2/(4 M2),
  R approximately 0.07000553078197614,
  mu((0,R]) >= approximately 0.1428458564387406.                 (7)

These are dimensionless original-Hamiltonian energy units, NOT eV and not
a new experimental particle-mass prediction. The simpler bare-trial bound
alone would give B<=179/4950 approximately 0.03616161616.

### Why subtracting only the vacuum would have been insufficient

The vector (W-omega(W))Omega is orthogonal to Omega but may retain OTHER
zero-energy components. With K=diag(0,0,10) and a unit vector carrying
weights 0.6,0.3,0.1, centering against the first basis vector leaves a
Rayleigh quotient 2.5 although the true positive gap is 10. The ratio of
the second and first moments instead returns 10. Equations (5)-(7) handle
the whole zero eigenspace without assuming uniqueness. This counterexample
is a regression test, not an alternative physical parent.

The available moments are compatible BOTH with a gapped two-atom measure
at 0 and B (positive weight m1^2/M2), and a gapless uniform measure on
[0,2m1] (second moment 4m1^2/3<M2). These measures illustrate the remaining
inference boundary; neither is asserted to be the actual Wilson spectrum.

## 6. Winding flux is not an exact extra conservation law here

Let F_x be the sum of oriented electric fields crossing one periodic
x cut. An original LH transporter across that cut changes F_x by one
while preserving every local Gauss constraint. Its nonzero coefficient
in H is w=1/24. The full-cubic bare-state action verifies this matrix
element on 125 sites/375 links, so [F_x,H] is genuinely nonzero.

Thus exact electric-plane-flux superselection from a matter-free theory
cannot simply be imported to protect a massless mode in this parent.
This statement does not exclude emergent/approximate conservation or
classify a phase. Nor does (3) supply a separately derived effective
magnetic plaquette Hamiltonian. Integrating out matter with a controlled
remainder, if used later, remains a separate obligation.

## Reproduction and next discriminant

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/ground-state-loop-response/checker.py --output experiments/theory-contracts/ground-state-loop-response/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/ground-state-loop-response -p 'test_*.py'
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/ground-state-loop-response -p 'test_*.py'
```

The finite tests check exact algebra, cubic symmetry, loop domains via
uncut actions, source pins and failed inferences. They are not a proof-
assistant certificate for the general thermodynamic argument. No bulk
ground vector, dispersion relation or gap has been numerically computed.

The next discriminant is a LOWER spectral bound or long-distance connected
Wilson/electric correlations for these same symmetric ground states. That
would begin to separate a gapped phase from a gapless one. Neither the
heavy mass M=4, gauge invariance alone nor a centered-vacuum trial vector
can supply that missing result. Uniqueness/compiler selection, chirality,
continuum Lorentz symmetry and spin-two gravity remain open. Only local
theory experiments and their catalog/notes are updated; no paper, website,
verification, ledger, scorecard, commit, push or RH promotion.
