# Origin, E8 cascade and dynamics: the common composition question

2026-09-08. Research synthesis at repository HEAD b803b7e5, with the named
uncommitted compiler/charge/field experiments explicitly included. Three
parallel read-only research lanes were independently checked and combined
with a new actual-source neutral-pair computation. No T1--T8, TOE or RH
completion is claimed. Paper, website and proof ledger remain unchanged.

## Main conclusion

The strongest simple common principle to investigate is **composition
with its state and phases retained**. The old cascade, the finite compiler,
charge-cocycle algebra, neutral fields and arithmetic correspondences all
contain exact composition laws. They do not yet form one derived physical
system. The missing bridge is not another attractive numerical constant:
it is a source-preserving identification of their operations and states.

This is a proposed research direction, not a new axiom already proved to
select the world. A compact statement can hide strong assumptions. The
[Origin Story](../../../origin_theory.tex) at lines 1509--1538 already
proposes one stable fixed point, but its word "admissible" includes
unitarity, finite entropy, anomaly-free chiral matter, lattice closure,
Hawking--Einstein compatibility, primitive seam transport and PF selection.
Those obligations cannot all be counted as outputs of the short slogan.

Similarly, [the compiler uniqueness record](../../../tfpt_research_contracts.tex)
at lines 5846--5861 explicitly says uniqueness up to **nonunique**
isomorphism, with automorphism group C6, not a strict terminal object.
Finite uniqueness does not select a vacuum, spacetime derivative, or a
four-dimensional interacting theory.

## 1. A genuine algebraic simplification: reflection relates the two pairs

In the existing eight real E8 coordinates, let

    R(x1,x2,...,x7,x8)=(x2,x1,...,x8,x7).

R preserves the lattice and metric, commutes with the actual family cycle
sigma, reverses the Gaussian deck J to J^(-1)=-J, and fixes the compiler
quotient L/(1+J)L pointwise. The exact four-section census in
[charged-cocycle-lift](../charged-cocycle-lift/README.md) has permutations

    J: (0 3)(1 2),    R: (0 1)(2 3).

Thus the two unordered deck-paired Clifford splittings belong to **one
orbit if deck-orientation reversal is allowed**. They are not unrelated
algebraic choices. This is a smaller and more informative residual than
simply recording two unexplained alternatives.

The lift must retain signs. For the actual ordered parity cocycle c,
define the quadratic phase

    p_R(x)=sum_(i>k) [c(R e_i,R e_k)+c(e_i,e_k)] x_i x_k mod 2.

Because R preserves the quadratic form, the cocycle difference is an
alternating symmetric bilinear form, hence the displayed polarization
identity gives delta p_R = c(Rx,Ry)+c(x,y). All 65,536 cells are checked.
The unsigned cocycle differs in 30,720 cells. Adding a linear character
with binary mask 42, 84, 170 or 212 gives coherent lifts satisfying

    Rhat^2=1, [Rhat,sigmahat]=0, Rhat Jhat=Jhat^(-1) Rhat.

These phases refer to the already declared target charge algebra, not an
identified microscopic seam field. Their parity formula extends to its
integer lattice zero modes; the metric isometry preserves their quadratic
energy. It does not settle the physical status of R.

**Decisive boundary:** R does not preserve the marked standard D5+D3
carrier. It sends e1+e5 to e2+e6, changing the inherited grade from 0 to 2,
although it fixes s=(1/2)^8. Therefore the two choices cannot yet be
declared gauge-equivalent for the full physically marked construction.
Next: reconstruct orientation and the carrier marking from the same
microscopic state and charged local operators, then classify R there.

## 2. What the old logarithmic E8 cascade really says

The inspected sources are:

- [V1.06, 01.09.2025](../../../_archive/paper-latex/old/paper_v1_06_01_09_2025.tex),
  lines 650--699: claimed orbit chain and curvature/physical-window normalization.
- [V2 text](/Users/stefanhamann/Projekte/tfpt-theoryv2/latex/tffpt-theory-fullv2.tex:1173),
  lines 1173--1222: explicitly adopted 5/6 discrete closure and structural postulate.
- [Historical normalization program](/Users/stefanhamann/Projekte/tfpt-theoryv2/E8ChainSolver/e8_orbit_engine/src/e8_orbit_engine/fit.py:15),
  lines 15--68: takes gamma0=0.834 as input.
- [Historical graph construction](/Users/stefanhamann/Projekte/tfpt-theoryv2/E8ChainSolver/e8_orbit_engine/src/e8_orbit_engine/chain_search.py:62),
  lines 62--142: approximate graph based on dimensions, heights and label distance,
  not a verified orbit-closure Hasse graph.
- [Current cascade chapter](../../../tfpt_3_e8_audit_bootstrap.tex),
  lines 11948--11971 and 12143--12177, and its arithmetic checker
  [v5](../../../verification/v5_e8_cascade.py).

The inner formula is

    D_n=60-2n, n=0,...,26,
    gamma_n=lambda log(D_n/D_(n+1)), n=0,...,25.

It telescopes exactly. More generally tau(a,b)=log(a/b) satisfies
tau(a,c)=tau(a,b)+tau(b,c). This permits subdivision without changing the
scalar endpoint transfer exp(-lambda tau). That is the useful simple
structure. Identifying log D with physical entropy would require an
additional state-space identification: D is a centralizer dimension,
not automatically a count of accessible physical microstates.

### Source discrepancies that must be corrected before promotion

The current chapter uses gamma(0) both for the first inner 60->58 step
and for the historical 248->60 normalization. Their ratios are 30/29 and
62/15, so these definitions cannot both hold for nonzero lambda. Use a
separate gamma_pre if preserving the historical convention.

V1.06 has gamma_pre approximately 0.834, whereas V2 adopts 5/6 and obtains
lambda=0.5872331908. Its code inserts that target; v5 checks arithmetic,
not the orbit-closure chain, the optimization problem, or uniqueness of
lambda. Curvature on the pure inner ladder is S(lambda)=lambda^2 C,
C>0; without explicit additional constraints its minimum is lambda=0.
This does not refute a constrained optimization theorem, but the inspected
implementation does not supply one. The current "curvature-extremum,
no fit" statement is therefore not certified by its cited checker.

Index conventions also differ. The V2 displayed formula uses D_n/58
after the pre-step; consistently adjoining that pre-step to every inner
step instead uses D_n/60. With the V2 lambda:

| Quantity | Value |
| --- | ---: |
| Inner ladder (8/60)^lambda | 0.3062915264 |
| Text-indexed pre-step plus (8/58)^lambda | 0.1357903473 |
| Consistently composed full 248->8 chain, 31^(-lambda) | 0.1331137487 |

These differences are recorded, not silently reconciled. None of these
small suppression factors generates a Planck-to-IR hierarchy by itself;
the chapter explicitly retains calibrated block normalizations.

### A sharp finite-prime-support boundary

All scalar rung ratios and their inverses use only primes <=31. Their
products cannot introduce 37 or any larger prime. The consistently
composed full chain even collapses to 248/8=31; its scalar endpoint loses
the intermediate decomposition. Repeating the same finite scalar ladder
does not create an all-prime system. Richer operators could, but would
need a construction rather than an inserted list of primes.

## 3. The arithmetic comparison is exact, but its physical clock is missing

The existing [Gaussian rank-four submodule QSM](../../tfpt-discovery/census_qsm_normflow_probe.py)
uses injective endomorphisms, q(A)=Norm det A, and

    mu_A delta_K=delta_(AK), H_index delta_K=log[M:K] delta_K,
    [H_index,mu_A]=log q(A) mu_A.

Its partition function is the classical product
Z(s)=product_(j=0..3) zeta_Q(i)(s-j), Re(s)>4. It is insensitive to the
E8 Hermitian form at fixed free module rank. The thermodynamic abscissa
4 is not an RH critical line.

New independent exact calculation: compute the formal Dirichlet log
directly from hnf_cell_counts(200), without prime decomposition in that
calculation. Against the Euler-product comparison it gives

    ell(p^k)=(1+chi_-4(p)^k)(1+p^k+p^(2k)+p^(3k))/k,
    ell(n)=0 for n not a prime power.

All 199 coefficients agree; all 139 non-prime powers vanish. In
particular raw counts at 10,26,65 are 4680,71400,1485120, but all three
connected coefficients are zero. This is a discriminating comparator,
not a new physical derivation or a proof based on finitely many n.

### Direct physical-clock countercheck

The tempting identification with the existing charge-zero-mode dilation
fails already before taking a limit. On ell^2(L), let V_2|q>=|2q> and
H_0|q>=||q||^2/2 |q>. Then

    [H_0,V_2]=3 V_2 H_0,

not c log(256) V_2. The index of 2L in L is 256, but the energy shifts
at q=0,alpha,2alpha for a root alpha are 0,3,12. At the vacuum alone a
nonzero constant logarithmic shift is impossible because V_2 fixes it.
Thus the current quadratic charge Hamiltonian is not the index clock.
This excludes that direct identification only; it does not exclude a
different derived correspondence on the same eventual physical parent.

## 4. Link to the new neutral field computation

The accompanying [neutral-pair experiment](../neutral-pair-composition/README.md)
computes the full complex Slater determinant, proves cancellation of the
common external ramp, and controls its connected leakage-log series.
At N=64 the half-arc overlap is 0.684686, the tested bottom-mode error
is 1.01e-5, but the top-mode error is still about 1.04 (Frobenius norm).
There is no claimed local-field or full determinant-factorization limit.

The relevant commonality is composition, not equality of these three
objects. Neutral unitary pairs obey W_ab W_bc=W_ac; their expectations
need not multiply. Absolute determinants of finite unitaries have modulus
one, so their modulus cannot serve as a nontrivial index degree either.
Keep the state, compression, complex phase and proper-range embeddings
distinct. The positive leakage log does not by itself supply the signed
arithmetic trace information; its mixed-channel test is proved in the
neutral-pair note.

Classical examples show what a *real* bridge must contain:
[Moller--Pohl](https://arxiv.org/abs/1103.5235) constructs a specific
geodesic symbolic dynamics and transfer family whose Fredholm determinant
is Selberg zeta. That is not an identification with Riemann zeta or TFPT.
[Connes--Consani--Marcolli](https://arxiv.org/abs/math/0703392) formulates
an adelic trace pairing whose required positivity is equivalent to RH;
constructing the pairing does not prove that positivity.

## 5. Prioritized next proof, mapped back to TOE

1. **Same-parent field/state gate:** control the full complex neutral
   determinant, endpoint normalization and smeared limit, then identify
   the carrier marking and charge-cocycle phase microscopically. This is
   relevant to the shared T1/T2/T3/T8 substrate, not a closure of any of them.
2. **Same-parent dynamics gate:** derive a multiplicative correspondence
   degree from actual source operations and test its commutator with the
   already selected physical generator. The direct V_2 identification
   above fails. Do not repair it by defining a different clock and calling
   it the original dynamics. Relevant to T4 and the RH interface.
3. **Arithmetic generatedness gate, conditional on 2:** produce a new
   degree with prime 37 from the construction, without putting 37 into its
   generator list; then prove unbounded generation, local factors and
   mixed connected cancellation. This is a first kill test, not an RH
   acceptance test. All-place trace, pole terms and positivity remain.

The gauge measure (T5), flavor mechanism (T6), and gravitational spin-2
reconstruction (T7) receive no independent solution from these identities.
They must eventually be tested on the same selected parent and state.
The value of the simplicity perspective is to remove redundant choices
and reject false identifications early, while keeping the remaining
physical selection problem explicit.

## Reproduction and test boundary

`python3 checker.py --output validation.json` reproduces the exact finite
record and labeled floating cascade values. Ten tests pass in normal
and -OO modes. The independent Dirichlet exponential test uses a
nonmultiplicative sequence, so it is not a replay of the Euler target.
Inherited source files are hash-pinned and unchanged.

An initial -OO import failed because the old census hashes __doc__. A
first metadata restoration also failed because this Python's default AST
parse inherited optimization. The final adapter restores only the pinned
source description from an explicitly unoptimized syntax tree; executable
code and assertions still use the requested interpreter mode. This was
diagnosed using the systematic-debugging skill; no physics or old source
was changed to make the checks pass.
