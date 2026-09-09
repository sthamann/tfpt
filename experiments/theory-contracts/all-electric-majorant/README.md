# All-event convergence of the fixed-parent local high-field source

2026-09-08. **NON-RH / mathematical theory experiment, not a TOE claim.**

This supplies an all-order argument for the M/E source expansion of the
local high annihilator in the SAME compact U(1) lattice parent. It is not
an assertion that the previous finite numerical column already contains
all events. The general argument below, not a finite test count, carries
the statement. Tests check the identities and an independent physical
interaction-depth expansion. No proof-assistant or peer-review certificate
is claimed.

## Precisely fixed model and conclusion

The parameters remain a=1/12, eta=1/2, beta=1/4, kappa=1/100, M=4,
Vmag=0. H0 contains the uncut electric energy kappa sum(E_l²)/2 and
the original onsite fermion energies epsilon_L=1/96, epsilon_H=4.
V contains all directed nearest-neighbor and nonbacktracking two-step
hopping monomials of the original parent. Their norm row sums obey

  mu = max_s sum_(j,p) |w_(s,j,p)| = 77/96,
  S = sum_(monomials meeting a fixed link) |w p_l| = 53/144.

The first high row has absolute weight 1/4. The value S is the complete
absolute incidence sum, NOT the smaller force-operator bound 53/288.
All sums and bounds retain the whole CAR space and all integer fluxes.

For every compatible finite volume, the local high field equals its
M/E source series, absolutely convergent in operator norm for |t|<=1,
with estimates independent of volume and flux. The same source series
constructs the norm limit of this PARTICULAR local high field along
volumes exhausting the cubic lattice, and hence of its high occupation.
This conclusion does not assume a previously constructed thermodynamic
dynamics. It does not construct a global automorphism group on every
rotor/fermion observable, or a continuum/relativistic/gravitational limit.

## 1. Exact normal form for arbitrarily many E events

Use the right-normal rotor convention F(E)U^p=U^p F(E+p). At fixed
simplex intervals u0,...,un, a path integrand has the form

  w i^n exp(i sum_j f_j u_j) U^r exp(i Theta dot E) O
       product_(a=1..k) [1-exp(i kappa sum_(j=1..n) d_aj u_j)],
  Theta = kappa sum_(j=1..n) r_j u_j.

Here O is the LITERAL CAR word with 2k+1 factors, r_j the complete
cumulative currents (including prefixes whose final sum cancels), and
d_aj=r_j dot p_a for intervals before electric event a and zero later.
The last d component is zero after every event. The scalar prefactor is
the actual signed nested-commutator coefficient. The new implementation
stores this raw sign and uses i^n; older files stored its negative and
used -i^n. Tests explicitly compare these conventions.

The initial free field is exp(-i M u0)c_H,0. Its first commutator is
matter-only. The following three identities prove the normal form by
induction, without an upper bound on k:

1. Free evolution maps U^r exp(i Theta E)O to the same word, with
   Theta -> Theta+kappa v r and scalar phase
   exp(i v[kappa |r|²/2+Delta(O)]).
2. The M part of [V,FO]=F[V,O]+[V,F]O acts on EVERY CAR leg. Moving the
   original hopping U^p into right-normal order multiplies the common
   phase by exp(i Theta dot p). Old difference factors do not change.
   The new last interval has zero in all old d rows. Creator legs use
   the transposed original row, reversed current and positive sign;
   annihilator legs use the original row and negative sign.
3. For one original monomial v=w_p U^p B_p,

     [v,U^r exp(i Theta E)]O
       =w_p U^(r+p) exp(i Theta E)[1-exp(i Theta dot p)] B_p O.

   Thus E prepends a creator/annihilator pair and adds exactly ONE new
   scalar difference factor. It neither differentiates nor doubles the
   existing k factors separately. Those factors are independent of E.

Initial flux therefore changes only a common unitary factor. No norm
bound below replaces a full-space operator by its action on E0. In
particular, these bounds can legitimately be used inside a full-Heisenberg
Duhamel identity. They are not estimates of R(t)P_E0 incorrectly applied
to tau(R(t))P_E0.

## 2. Positive moments and their general envelope

Put L_j=|r_j|_1. The first high hop has length one and every later M or E
adds a current of length at most two, so L_j<=2j-1 for EVERY raw path.
Expand the nonnegative polynomial

  product_a sum_j |d_aj| u_j = sum_m c_m product_j u_j^m_j,
  A=sum_m c_m product_j m_j!,
  B=sum_m c_m product_j m_j! sum_j(m_j+1)L_j.

For k=0 the empty product gives A=1 and B=sum L_j. These are the
[Dirichlet simplex moments](https://dlmf.nist.gov/5.14.E2), with the
unused u0 interval carrying exponent zero. The corresponding integrals
are A T^(n+k)/(n+k)! and B T^(n+k+1)/(n+k+1)!.

Since sum m_j=k and sum L_j<=n², every monomial satisfies

  sum_j(m_j+1)L_j <= n²+k(2n-1) = beta_(n,k).

Hence B<=beta_(n,k) A, including A=0. This proof is uniform in n,k,
not an extrapolation from the former k<=3 calculations.

Let a normalized path majorant be

  b_p(T)=|w_p| kappa^k A_p T^(n+k)/(n+k)!.

All literal CAR factors have norm at most one, and all common rotor
factors are unitaries, so this bounds the integrated path operator.
Weights here include their actual 576^-n normalization.

## 3. Both continuations contract together

M has d=2k+1 possible literal legs. Its absolute row sum is at most
d mu, and A does not change except for this hopping weight. Therefore

  sum_(M children) b_child <= b_p mu T (2k+1)/(n+k+1).

For E, use the complete original force incidence on EACH old prefix:

  sum_(p,a,b) |w_(p,a,b)| |r_j dot p| <= S L_j.

This implies A_new<=S B_old after summing E children. The additional
event and difference contribute two powers of T and two factorial
denominators, giving

  sum_(E children) b_child
    <= b_p kappa S T² beta_(n,k)/[(n+k+1)(n+k+2)].

The source starts with M, so n>=k+1. For all such integers,

  (n+k+1)-(2k+1)=n-k>0,
  (n+k+1)(n+k+2)-beta_(n,k)=k²+3n+4k+2>0.

Consequently the COMBINED child sum is bounded by rho(T)b_p, where

  rho(T)=77 T/96 + 53 T²/14400,
  rho(1)=11603/14400=0.805763888888... < 1.

No E branch is omitted to obtain this inequality. The branching count
and growth of CAR degree have already been paid for in the two ratios.

## 4. Identification with the physical finite-volume source

In each finite volume the rotor Hilbert spaces are separable, H0 is
self-adjoint on its natural dense domain, and V is bounded and
self-adjoint. The bounded interaction-picture perturbation is strongly
continuous. The strong Dyson/Duhamel expansion therefore exists. Relevant
operator integration facts are given by
[Nachtergaele and Sims, Section 2](https://arxiv.org/html/1410.8174v1#S2).
This reference supplies the strong-integral framework, not the constants
or model-specific convergence estimate derived here.

At each finite interaction depth, splitting every commutator by the
identities in Section 1 is a finite exact algebraic expansion of that
same Dyson coefficient. No new Hamiltonian or tensor approximation is
introduced. The usual finite-volume Dyson series and the split series
therefore have equal partial coefficients; the uniform majorant proves
absolute convergence of the split series. Their sums coincide with
tau_t^Lambda(c_H,0). Norm differentiation of electric phases is never used.

If Z_N contains the free field plus ALL source words with at most N
events, the simple bound is

  ||tau_t^Lambda(c_H,0)-Z_N^Lambda(t)||
     <= (T/4) rho(T)^N/[1-rho(T)].

A sharper certified version keeps n,k in a small positive recurrence.
Start b_(1,0)=T/4, apply the two exact scalar ratios from Section 3, and
let S_N=sum_k b_(N,k). Then

  epsilon_N(T)=S_N rho(T)/[1-rho(T)]

bounds ALL later events, not merely the next layer. The implementation
records each rational coefficient. At T=1, epsilon_16 is approximately
4.74899e-11, epsilon_24 approximately 2.09058e-16, and epsilon_32
approximately 1.08576e-21. These are estimates for Z_N, NOT achieved
errors of any currently evaluated cubic column.

## 5. Local high-field thermodynamic limit, with an explicit boundary

A path with n events is supported within a radius at most 2n of the
source: each original hopping path has length at most two, and an E
monomial must touch an existing phase-prefix link. Retaining every
prefix is essential to this statement. Free evolution adds no support.

Embed local bounded rotor operators and the CAR algebra by their usual
local inclusions (graded for odd fermionic fields). Compatible volumes
keep the same bulk onsite constants and original monomials; boundary
terms are omitted, not fitted. Volumes containing the radius-(2N+2)
neighborhood have the same Z_N under these embeddings. Each local strong
integral is a bounded operator in that finite-support algebra.
Precisely, the rotor local algebra used here is the algebra of ALL
bounded operators on its finite-link Hilbert space, followed by the
norm completion of these local algebras. Strong integrals need not lie
in a smaller algebra generated only by selected rotor Weyl unitaries;
no invariance or limit theorem for such a smaller algebra is asserted.

For any two such volumes, the previous uniform tail gives

  ||tau_t^Lambda(c_H,0)-tau_t^Lambda'(c_H,0)|| <= 2 epsilon_N(T).

The family is therefore norm Cauchy, uniformly on |t|<=1. It defines a
quasi-local A_H(t), independent of the compatible exhaustion, with norm
at most one. Its occupation A_H(t)^* A_H(t) is positive, bounded by one,
and inherits the corresponding finite-volume limit. This establishes
the local source/occupation limit, not a construction of the full
automorphism group on arbitrary rotor observables or all real times.
It also does not identify the declared parent with the TFPT compiler's
unique dynamical output.

For finitely many translated high fields at the SAME time, use a common
exhaustion. The CAR identities of the finite-volume evolved fields pass
to their norm limits. Likewise the original local gauge covariance passes
to the limit because the gauge action is isometric. Thus the limiting
high occupation remains a gauge-invariant projection, not only a positive
contraction. None of this asserts a composition law on arbitrary rotor
observables that have not been included in the construction.

## Reproduction, checks and remaining work

The independent Hamiltonian check introduces a formal lambda ONLY as
bookkeeping for H0+lambda V. It expands the UNSPLIT rectangular
Liouvillian H_Q X-X H_N simultaneously by lambda and time, and compares
it with the normal-form source. All interaction depths 0..5 and time
powers 0..12 agree exactly, on all six input columns of the 4x6 source
matrix, at flux offsets 0,3,-4. Both sectors are complete; no electric
cutoff is used. The fifth layer includes four-E words. There are
1,1,6,39,263,1801 nonzero whole-operator paths at depths 0..5 after the
safe zero-word rule. Zero action on an initial state is not used to prune
intermediate paths. Complete scaled integer matrices are stored.

Other checks compare the whole commutator on all 16 Fock inputs for words
with up to seventeen literal legs, test actual eight-E normal forms and
their subsequent M step, and compare 256 signed branches with independent
factor multiplication. Removing one branch is detected. Original cubic
row/force sums, historical low-order signed dictionaries, the exact
Dirichlet moments, the general positive polynomial identities and the
complete deterministic replay are checked separately.

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/all-electric-majorant/checker.py --output experiments/theory-contracts/all-electric-majorant/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/all-electric-majorant -p 'test_*.py'
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/all-electric-majorant -p 'test_*.py'
```

The finite code guards (event count, electric count and certificate
depth) are resource limits for executed checks. They do not occur in
the induction proof. Numerical phase polynomials are checked at declared
fluxes; they are NOT claimed to approximate unbounded flux spectra in
operator norm. The mathematical majorant uses exact unitary phases.

Next: evaluate a complete declared source target with this all-event tail,
or extend the constructive dynamics to a generating observable algebra
with domain and composition control. Parameter/vacuum selection, chiral
continuum, universal spin two and T1-T8 remain unclosed. Only local theory
experiments and catalog/continuation notes; no paper, website, ledger,
verification, scorecard, commit or push promotion.
