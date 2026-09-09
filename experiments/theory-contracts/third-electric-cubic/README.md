# Third electric source: full cubic census and both new boundary terms

2026-09-08. **NON-RH / conditional same-parent theory experiment.**

This evaluates the MEEE source on the original full cubic U(1) parent,
with its unchanged couplings and bare-low E0 preparation. It does not
alter or depend on the unfinished Round50 combined numerical column.
It pins the completed seventh-frontier edge experiment and, transitively,
the original Round49 sources and Hamiltonian.

## Exact construction and complete raw census

Apply one complete electric force difference to every original MEE seed.
Use all original hopping monomials meeting any of its three spectral
prefixes. Prepend c_a^* c_b and retain eight signed simplex branches:
the old four with the new final full energy, plus the same four shifted
by (0,24 r_i dot p,0), with opposite signs. No phase or current is fitted.
The source has four interaction events and three electric differences,
so its first possible time power is seven.

The full cubic census contains 441456 raw paths, of which 346236 are zero
as WHOLE Fock operators. Only 4980 raw paths act nontrivially on the bare
preparation. These are different tests: all raw and nonzero-operator norm
moments are accumulated BEFORE the preparation-specific final action.
The original complete force scan independently checks the indexed census.

## Seven-leg operator control

The new literal pattern is (+,-,+,-,+,-,-). A complete CAR monomial maps
each occupation basis vector either to zero or to exactly one basis
vector with coefficient of modulus one. Consistent initial occupation
requirements define its domain. Different domain vectors have different
images because each mode has a fixed net toggle. Thus every nonzero
literal word is a partial isometry of norm one, including words with
repeated modes; inconsistent requirements give the zero operator.

For the original matter commutator, Leibniz and the inherited full-Fock
row bounds give

  ||[V,L_word]|| <= sum_(j=1..7) C_(species_j),
  C_L=sqrt(107/2048), C_H=sqrt(1/96).

No tensor-to-Fock isometry or initial-null pruning is needed. The regression
exhausts all 4^7 literal mode words and all 16 occupations in a four-mode
Fock space to check the zero rule and partial-isometry structure. This is
a finite implementation check accompanying the general argument above,
not a formal proof-assistant certificate.

## Exact phase moments and the fourth-E remainder

For k difference vectors d_ai and current lengths L_i, expand the positive
polynomial product_a sum_i |d_ai|u_i. A monomial c product_i u_i^m_i has
Dirichlet weight c product_i m_i!. Therefore

  A_k=sum_m c_m product_i m_i!,
  B_k=sum_m c_m product_i m_i! sum_i(m_i+1)L_i.

The corresponding simplex integrals are A_k T^(n+k)/(n+k)! and
B_k T^(n+k+1)/(n+k+1)!. This is a direct specialization of the
[Dirichlet integral, DLMF 5.14.2](https://dlmf.nist.gov/5.14.E2), with the
unlisted interval u0 carrying exponent zero. The polynomial implementation
is independent of Round50's subset recurrence and is checked against
complete assignments and the older one-/two-difference formulas.

Sum the nonzero-operator A_3 and B_3 moments with absolute original
weights divided by 576^4, retaining all 128 species patterns. Let

  A_C=sum_sigma a_sigma sum_j C_(sigma_j), B=sum_sigma b_sigma.

Using the inherited strong full-H Duhamel identity and electric force
bound 53/288, the two disjoint outgoing branches of the new leaf obey

  R_MEEEM = kappa^3 A_C T8/8!,
  R_MEEEE = kappa^4 (53/288) B T9/9!,  kappa=1/100.

The outer full-H propagator already includes all later M/E events. The
fourth electric event is explicitly retained, not removed because the
source compiler stopped at three. Strong-dynamics and infinite-volume
assumptions are inherited conditions, not re-proved here.

At T=1 the old MEEE boundary is 5.131814689917804e-12. Its two replacements
are 6.903852888826482e-13 and 8.322343755687405e-16. Their sum is
6.912175232582170e-13. This is a replacement for ONE branch of an otherwise
unchanged source expansion. Other seventh-order families remain, so no
global O(t8) claim follows. It must never be attached to an unchanged
combined probability as if the new MEEE amplitude were absent.

### Positive E transport without a new raw-path expansion

A further bound applies to the two original families (n,k)=(3,2) and
(4,1), where n is event count and k electric count. For one fixed link,
sum absolute original hopping weights times the link-current incidence,
resolved by the species of the newly prepended pair. The exact matrices
are

  F = [[29/144,1/12],[1/12,0]],
  G = [[17/72,1/12],[1/12,0]],

where G has one additional factor equal to the total hopping-current
length. In F_LL, the two directed nearest-neighbor terms contribute
96/576 and the twenty two-step terms contribute 20/576. The cross-species
entries each have two terms of weight 24/576. G doubles only the two-step
contribution. These incidence sums are not the sharper operator force
norm 53/288. The regression checks both matrices from the actual original
rows for translated links, every axis, and both current orientations.

Let b_sigma be the old positive phase-gradient moment. Prefix currents
obey L_i<=2i-1. For each old polynomial monomial with exponents m_i,
sum_i m_i=k, set S=sum_i(m_i+1)L_i. Its second length moment is
S²+sum_i(m_i+1)L_i², bounded by
(sum_i L_i+(k+1)L_max)S. Adding the new last-interval contribution and
using |r_final+p|<=L_final+|p| gives the componentwise transport

  a'_(alpha,beta,sigma) <= F_(alpha,beta) b_sigma,
  b'_(alpha,beta,sigma) <= [C_nk F_(alpha,beta)+G_(alpha,beta)] b_sigma,
  C_nk = n²+(k+2)(2n-1).

Thus C_32=29 and C_41=37. The inequality
sum_h |w_h| |r_i dot p_h| <= F L_i, separately for each species pair,
is just the triangle inequality over link incidences. The G version
controls the additional |p_h| factor. This supplies all terms in the
new Dirichlet moments; it omits no extra electric boundary.

The complete measured MEEE moment tensors lie below these independent
upper tensors component by component. Further explicit original cubic
one-E path controls verify the (4,1) transport. This gives conservative
M/E boundary replacements for MEMME, MMEME and MMMEE without pretending
to have executed their new full raw census or combined readout. Whole
operator zero seeds can be excluded here because left multiplication
by the electric bilinear preserves the zero operator. Initial-state
zeros cannot be excluded. No global time-order promotion follows.

## Numerical and independent physical checks

Only after the norm census, apply complete literal words to bare-low E0
and group the exact signed physical-output/frequency keys. Integrate all
scalar simplex kernels by the pinned rational degree-80 compiler with
its explicit numerical tail. Restore all six original cubic rotations
with the fermionic cocycle and sum amplitudes before squaring.

The resulting `isolated_source_squared_norm` is the norm of this ONE
source column, NOT the occupation probability of the complete theory.
In particular it omits all interference with the old source and the
pending second-M column. The complete changed physical readout has not
been computed by this experiment.

On the original physical edge, all four E0 input columns of the MEEE
order-seven matrix agree with the independently Hamiltonian-checked
frontier record. There are 216 raw edge paths and no lower-order source
terms. A missing signed phase branch is detected. Small nonzero cubic
controls compare literal simplex sums against the grouped compiler.
Every grouped output also obeys the original charged Gauss constraint,
div(current)+occupation_change=-delta_root. The test checks all 2355
nonzero frequency groups independently of the coefficient compilation.

## Reproduction and firewall

From the repository root:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/third-electric-cubic/checker.py --output experiments/theory-contracts/third-electric-cubic/validation.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/third-electric-cubic -p 'test_*.py'
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/third-electric-cubic -p 'test_*.py'
```

Success verdict: `FULL_CUBIC_MEEE_CENSUS_AND_ISOLATED_SOURCE_EVALUATED`.
The record includes all moments, exact isolated-column norm, numerical
tail and costs. It is not a complete-source or TOE success marker.

Parameters/preparation, all-order electric dynamics, the chiral continuum,
universal spin two and T1-T8 remain open. Local theory-contract work only:
no empirical scorecard, paper, website, verification, ledger, commit, push
or external/formal certification is included.
