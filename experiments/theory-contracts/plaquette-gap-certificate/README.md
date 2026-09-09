# Uncut plaquette and coupled-cube gaps, with a failed global extension

2026-09-08. **NON-RH / unpromoted mathematical theory experiment.**

For the original SINGLE-PLAQUETTE spatial restriction, the complete neutral
Hamiltonian has a unique ground state and a strictly positive first gap,
enclosed approximately by

  0.0195776909527 <= gap <= 0.0204013098746.                    (1)

The authoritative rational endpoints are in Section 5 and validation.json;
the decimals in (1) are rounded outwards. All integer electric fluxes and
all neutral fermion configurations are included in this statement. There
is no finite-flux diagonalization or discarded electric tail.
Section 5b extends the same method to the coupled three-dimensional cube:
eight sites, twelve edges, five uncut integer flux directions, and a unique
neutral ground state with gap between 0.0177576051837 and 0.0221667420299.

This is NOT the gap of the full cubic lattice. The plaquette retains the
original ambient-degree-six onsite/backtrack coefficient and every hopping
whose complete path lies on its four edges. Couplings leaving this spatial
restriction are absent, explicitly. Its gap must not be promoted to a bulk
gap. A separate exact full-cubic variational counterexample below shows
why the particular bare-sector proof does not extend uniformly in volume.

## 1. Complete neutral space, including the infinite electric direction

Use four sites with directed edges 0->1->2->3->0, low/high fermions on
each site, and the unchanged parameters

  a=1/12, eta=1/2, beta=1/4, kappa=1/100, M=4,
  w=eta*a=1/24, epsilon_L=1/96, Vmag=0.

The original restriction has 24 directed nearest-neighbor terms and eight
directed two-step terms. Both two-step routes to opposite corners remain
distinct, with their original link products. Ambient backtracks stay at
degree six, not at the plaquette's actual degree two.

Neutral Gauss requires four fermions in eight modes. For an occupation
mask m let q_x=n_L,x+n_H,x-1. With arbitrary k in Z and E_3=k, all solutions
of q_x+E_x-E_(x-1)=0 are exactly

  E_0=k-q_0, E_1=k-q_0-q_1, E_2=k-q_0-q_1-q_2, E_3=k.

Thus the complete physical basis is the 70 masks in C(8,4), each times
ALL k in Z. The free diagonal energy grows quadratically with |k|. Its
resolvent is compact; the original hopping is bounded and self-adjoint.
Consequently the full neutral Hamiltonian is self-adjoint, bounded below
and compact-resolvent, with discrete eigenvalues lambda_0<=lambda_1<=...
counted with multiplicity. No assumption of nondegeneracy is made yet.

The executed basis checks cover 210 inputs and all 2130 nonzero outputs
at k=-3,0,4. Regression controls also use k=+-1,000,000. These are checks
of the complete formula and uncut original actions, NOT a definition of
a finite electric Hilbert space. Every H output changes k by at most one.

## 2. An infinite-rank P/Q split with a controlled Q block

Let P be the projection onto N_H=0 INSIDE the neutral sector. Then all
four low modes are filled and Gauss makes all four E equal to k. Hence
P is infinite-rank, isomorphic to l2(Z), and

  A=P H P,       A|k>=(e_b+2 kappa k^2)|k>,       e_b=1/24.

Low-to-low hops annihilate P by Pauli exclusion. Write Q=1-P, C=Q H Q,
B=Q H P. Each P basis vector has exactly eight distinct LH outputs in Q,
each with coefficient magnitude w. The output sets for different k are
orthogonal: equal output fermions identify the oriented hop, and its
electric translation is injective. Therefore, as operators on ALL P,

  B^*B=8w^2 P=c P,       c=1/72.                             (2)

P and Q commute with the free electric/onsite part and preserve its
domain; B is bounded. The block operator and its quadratic-form Schur
completion are therefore well defined despite the infinite rank of P.

The previously established hole completion applies to this geometry. Its
low one-particle block is

  h_l=a A_U+beta a^2 A_U^2+4 beta a^2 I,
  h_l<=r I,       r=2a+8 beta a^2=13/72,
  Tr h_l=e_b,    Tr A_U^2=8.

The extra diagonal 4 beta a^2 retains the omitted-neighbor backtracks;
it is not a new parameter. Set d=M-r=275/72. Neutrality gives N_holes=N_H,
so for every t>0 the exact square-completion bound is

  H >= e_b + (kappa/2) sum E_l^2 + (d-t) N_H - c/t.

On Q, N_H>=1. Choose the AUXILIARY INEQUALITY parameter t=1/8<d, yielding

  C >= q Q,       q=e_b+d-t-c/t=29/8.                         (3)

The electric term was only bounded below by zero, not truncated in H.
The all-Fock square identity is checked independently on 256 inputs.
This establishes a Q threshold for this spatial restriction; it is not
an assertion that the physical first excitation costs q or M.

## 3. Lower eigenvalue bounds without a flux cutoff

The block-elimination framework is the Feshbach-Schur method; see
[Dusson, Sigal and Stamm (2021), Section 1](https://arxiv.org/html/2105.02058).
Here P is infinite-rank and A unbounded, so we explicitly use the following
quadratic-form completion rather than silently invoking a finite-rank
perturbation theorem. For lambda<q,

  S(lambda)=A-lambda-B^*(C-lambda)^(-1)B,
  A-lambda-c/(q-lambda) <= S(lambda) <= A-lambda.              (4)

The form of H-lambda on u in P and v in Q equals

  <u,S(lambda)u>
    + ||(C-lambda)^(1/2)[v+(C-lambda)^(-1)Bu]||^2.

The triangular substitution is invertible on the form domain: B is
bounded, C-lambda is positive with bounded inverse, and its inverse times
B maps into the C domain. Thus the negative index of H-lambda equals
that of S(lambda). Both relevant negative indices are finite.

Let p_j be the ordered eigenvalues of A, so p_0=e_b, p_1=p_2=e_b+1/50,
p_3=p_4=e_b+4/50, etc. For every p_j<q, minmax on the P subspace gives
lambda_j<=p_j. Define the conservative rational lower bound

  ell_j=p_j-c/(q-p_j).                                      (5)

For lambda<ell_j, (4) implies that S(lambda) has at most j negative
eigenvalues: its j-th eigenvalue is bounded below by
p_j-lambda-c/(q-lambda)>0. Therefore lambda_j>=ell_j. In particular,

  lambda_0 >= 13/344,
  lambda_1,lambda_2 >= 12351/213800,
  lambda_3 >= 24741/210200.

This argument bounds the FULL compact-resolvent problem with all k in Z.
It does not set a finite matrix's eigenvalues equal to the true spectrum.
An independent rational six-dimensional block example tests the sign and
ordering of (4)-(5) against exact root isolation and LDL inertia. That
example is only an algebra regression, not an additional physical model.

## 4. Better upper bounds from original one-hop trial vectors

For k=0,-1,+1 define p_k=|all-low,E=k>, b_k=Bp_k, and

  d_k=<b_k,(H-p_k_energy)b_k>/<b_k,b_k>.

The notation p_k_energy denotes e_b+k^2/50, not the vector. Applying the
FULL original plaquette H gives, for these three k,

  <b_k,b_k>=1/72,       d_k=57497/14400,
  v_k=p_k-b_k/d_k.

Each trial vector has nine components and lives in the complete domain.
They are mutually orthogonal. The original Hamiltonian, not a truncated
effective Hamiltonian, gives their Gram and energy matrices, in order
k=0,-1,+1:

  G=(3308785009/3305905009) I,

  H_trial = [ 3032799409/79341720216, -2500/3305905009, -2500/3305905009;
             -2500/3305905009, 115525405333/1983543005400, 0;
             -2500/3305905009, 0, 115525405333/1983543005400 ].

Nonzero off-diagonal elements are retained. These are variational matrix
elements of dressed winding states, not an independently justified magnetic
effective Hamiltonian or exact eigenvectors.

For a subspace of dimension r=1,2,3, the elementary inequality
2 Re(H_ij x_i^*x_j)<=|H_ij|(|x_i|^2+|x_j|^2) gives the upper quotient

  u_(r-1)=max_(i<r) [H_ii+sum_(j<r,j!=i)|H_ij|]/G_ii.

Minmax on these actual subspaces proves

  lambda_0 <= u_0=3032799409/79410840216,
  lambda_1,lambda_2 <= u_1=u_2=115526905333/1985271005400.

The state vectors' electric support is finite as for any variational test
vector. That does NOT truncate the Hamiltonian or the complementary space;
the lower bounds in Section 3 cover the whole missing space exactly.

## 5. Certified conclusions for the neutral single plaquette

Combining the lower and upper bounds yields

  13/344 <= lambda_0 <= 3032799409/79410840216,
  12351/213800 <= lambda_1 <= 115526905333/1985271005400,

  5193605841619/265281838096575
    <= lambda_1-lambda_0
    <= 217698943193/10670831654025.                            (6)

The lower endpoint is strictly positive. Hence lambda_0 has multiplicity
ONE; this is a conclusion, not a vacuum-uniqueness assumption. The first
gap lies in the outward-rounded interval (1), in original model units.

There are exactly THREE eigenvalues counting multiplicity below 11/120:
u_2<11/120<ell_3. The first two excited levels are not proved exactly
degenerate; symmetry alone is not used to infer such degeneracy.

Nothing in this section proves a uniform gap in larger spatial regions,
an infinite-lattice gap or a unique TFPT-selected vacuum. In particular
the new statement is not a reversal of the predecessor's still-open
bulk-gap status.

## 5b. The same proof also works on a genuinely three-dimensional cell

This is not just a collection of decoupled faces. Take the original cube
with eight vertices (0 or 1 in each coordinate), twelve edges and all SIX
faces. Retain all 120 original directed monomials with paths inside the
cube, including paths that meet at shared face edges or vertices, and the
ambient-degree-six onsite terms. Only paths leaving the cube are absent.
This is still a finite spatial restriction, not the infinite cubic lattice.

There are C(16,8)=12870 neutral-total-number fermion masks. Pick a spanning
tree: its seven edges are determined by Gauss once the five chord fluxes
are specified. Given arbitrary integer chord fluxes and any such mask,
solve the tree edges from the leaves inwards. Every value stays integer,
and the root equation follows from total charge zero. This is a bijective
parameterization of the complete neutral space by those 12870 masks times
Z^5. The checker verifies Gauss on every mask; tests verify original H
closure with multiple nonzero five-component flux backgrounds. It does
not replace any of the five integer directions by a finite window.

In P, all low modes are filled and E is an integer divergence-free flow.
Any nonzero such flow contains a directed cycle after orienting edges by
their flux signs. The cube graph is bipartite and its shortest cycle has
four edges. Consequently sum E_l^2>=sum |E_l|>=4. A unit face circulation
saturates the bound. Thus A=P H P has a UNIQUE minimum at E=0, with

  p_0=8epsilon_L=1/12,       p_1=p_0+2kappa=p_0+1/50.

No full enumeration of the infinite P spectrum is required. Its electric
energy confines all five independent integer directions, ensuring compact
resolvent also for this full physical cube problem.

The exact row/Gram calculations now give

  h_l <= (3a+12 beta a^2)I=(13/48)I,
  Tr A_U^2=24,       B^*B=(24w^2)P=(1/24)P.

Using t=1/4 in the same positive-square inequality yields

  Q H Q >= q Q,       q=1/12+M-13/48-1/4-(1/24)/(1/4)
                       =163/48.

Hence Section 3 applies with e_b=1/12, c=1/24 and this q. The original-H
one-hop trial construction for E=0 and a single unit face circulation has
24 Q outputs per P input, cost 898/225, and the exact two-vector matrices

  G=(6468107/6451232)I,
  H_trial=[5659907/77414784, -625/825757696;
           -625/825757696, 180306317/1935369600].

This gives full-space bounds

  15/212 <= lambda_0 <= 5659907/77617284,
  35827/395100 <= lambda_1 <= 5769849019/62093827200,

  22690215757/1277774537850
    <= gap_cube
    <= 72950146007/3290972841600,

or, rounded outwards,

  0.0177576051837 <= gap_cube <= 0.0221667420299.

The strict lower bound again implies a unique neutral ground state for
this complete uncut cell. The six face degrees of freedom are coupled;
five independent electric cycles remain, not six independent plaquette
Hamiltonians. External-cube couplings and a volume-uniform gap are NOT
covered. This extension tests that the local argument survives an actual
three-dimensional cell, without claiming that it survives arbitrary size.

## 6. Why this bare P/Q proof cannot simply scale to the cubic bulk

On a cubic torus of N sites, define P_N again by N_H=0 in the neutral
sector. It contains all divergence-free electric configurations, not just
the zero-flux vector. Its minimum energy is epsilon_L N. The same argument
for actual LH outputs gives

  B_N^*B_N=(N/96)P_N.

The bulk hole bound has D=55/16, c_site=1/96. For 0<t<D, its estimate on Q_N is

  Q_N H Q_N >= epsilon_L N + [D-t-c_site N/t]Q_N.

A positive bracket is possible only if t(D-t)>c_site N, hence only if

  N<D^2/(4c_site)=9075/32 approximately 283.59375.

The criterion passes N=216 (L=6), fails N=343 (L=7), and is not a
volume-uniform proof. Failure of an estimate is not by itself a spectral
counterexample, so we separately construct one to the stronger proposed
claim Q_N H Q_N>=epsilon_L N+positive_constant.

### An actual Q_N state below the bare P_N minimum

On an even cubic torus, pick a perfect matching with N/2 edges. On one
edge use the single LH-excited state chi=T Omega_bare, with exactly one
high fermion. Its energy cost above bare is

  d_anchor=M-epsilon_L+kappa/2=9587/2400.

On every OTHER matching edge use the previously verified two-state dimer
rotation, lowering the energy by

  g=239675/551523414 per dimer.

All components have at least one high fermion, so the product lies
entirely in Q_N and is still exactly Gauss neutral. All unused links remain
at E=0. A hopping containing an unused link has zero expectation by flux
orthogonality. No nonbacktracking two-step path uses two matching edges,
because matching edges have disjoint endpoints. Thus ALL original cross
and two-step terms are retained but have zero expectation. The exact
full-H variational energy is

  E_Q_trial=epsilon_L N+d_anchor-(N/2-1)g.                    (7)

At L=28, N=21952, this gives

  E_Q_trial-epsilon_L N=-170930754997/220609365600
                       approximately -0.7748118695328863.

Therefore inf spec(Q_N H Q_N) is actually below the bare P_N minimum for
this finite cubic volume. This is stronger than a failed norm estimate.
The L=28 value uses exact matching-factorization arithmetic, NOT an
enumerated 2^10975-component state or a numerical large-volume ground state.

The local identities behind (7) are independently executed with one
anchored pair and two dressed pairs in the FULL L=5 cubic parent: 125
sites, 375 links and all 6000 terms. Its four-component vector lies wholly
in Q, and its original-H energy is epsilon_L N+d_anchor-2g. The tests repeat
this with all 10368 terms at L=6. No couplings outside the selected matching
edges are removed in these cubic controls.

### What this counterexample does NOT imply

Equation (7) lies ABOVE the all-dressed matching trial energy by the fixed
positive amount d_anchor+g. It is below the BARE reference, not below the
true ground state. It neither proves negative physical GNS energy nor
closes the bulk gap to zero. The bulk's previously constructed nonnegative
physical energy and Wilson spectral bounds remain unchanged.

The obstruction is specifically the attempted globally empty-high P/Q
separation measured against the undressed extensive reference. A valid
volume-uniform route needs control relative to the interacting state,
for example dressed local projections/connected-cluster estimates, or a
different genuinely volume-uniform lower spectral argument. This work does
not claim that any such replacement has already been constructed.

## Reproduction and research boundary

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/plaquette-gap-certificate/checker.py --output experiments/theory-contracts/plaquette-gap-certificate/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/plaquette-gap-certificate -p 'test_*.py'
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/plaquette-gap-certificate -p 'test_*.py'
```

The spectral results rest on the explicit full-space proofs in Sections
1-5b plus exact model-specific constants and variational controls. Finite
tests are not a proof-assistant certificate or independent mathematical
peer review. The positive finite-region gap and the exact failed global
bare-sector extension are different conclusions with different scopes.

Only local theory experiments and their catalog/working notes are updated.
No paper, website, verification, ledger, scorecard, commit, push or RH
promotion. Bulk phase and gap, vacuum selection, chirality, continuum
Lorentz symmetry and spin-two gravity remain open; T1-T8 are not completed.
