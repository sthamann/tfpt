# Sign covariance does not injectively determine seam dynamics

2026-09-18 · NON-RH theory contract · experiment firewall. This folder is a
exact counterexample audit of the reverse implication used in the current
`QGEO.STATE.01` reduction:

```text
[rho, C] = 0  =>  [rho, H] = 0
```

when the state covariance is the zero-temperature sign projector
`C = (I + sgn(H))/2`. The contract verdict is `PARTIAL`: the reverse
implication is **REFUTED** by an exact finite witness, while the forward route
`[rho,H]=0 => [rho,C]=0` and the mark-local implication remain in scope and are
not challenged. No verification, ledger, paper, website, or scorecard status
is changed, and no gate is closed.

## Exact certificate

The checker uses SymPy integers and Gaussian integers only. Set

```text
S = [[0,1],[1,0]],       A = diag(1,2),
H = diag(A,-A) = diag(1,2,-1,-2),
rho = diag(i S, -i S),   C = diag(1,1,0,0).
```

`H` is Hermitian and gapped. `rho` is unitary and has exact order four. With
the antiunitary particle-hole operation `Gamma(X)=J0 conjugate(X) J0`, where
`J0` swaps the two 2-dimensional blocks, the exact relations are

```text
Gamma H Gamma = -H,       Gamma C Gamma = I-C,
Gamma rho Gamma = rho,     [rho,C] = 0,
||[rho,H]||_F^2 = 4.
```

Thus the state projector and its particle-hole symmetry are unchanged while
the dynamics is not invariant. The checker verifies this witness; the general
repair follows analytically. Writing `Q=sgn(H)` and `H=Q|H|`, the hypothesis
`[rho,C]=0` gives `[rho,Q]=0`. Thus `[rho,H]=Q[rho,|H|]`; since a gapped
`H` has `Q^2=I`,

```text
[rho,H] = 0  <=>  [rho, |H|] = 0       (provided [rho,Q]=0).
```

The missing premise is the commutation of `rho` with the positive magnitude
operator, not another sign or character check.

## Exact nonuniqueness at fixed state and clock

For the fixed

```text
rho0 = diag(i,-i,-i,i),       C = diag(1,1,0,0),
H_a = diag(1,a,-1,-a),        a > 0,
```

the cases `a=2` and `a=3` have the same `rho0` and exactly the same sign
projector `C`, but different positive energies and the exact observable ratio
`H_a[1,1]/H_a[0,0] = a` (2 versus 3). More generally, any strictly positive
`H_plus` and `H_minus` in `H=H_plus direct_sum (-H_minus)` produce the same
sign state while retaining arbitrary positive magnitude data. This is state
noninjectivity, not a construction of a competing physical TFPT source.

## Relation to existing contracts

The pinned `v199_seam_state_invariance.py` run was replayed once before this
contract: `4 passed, 0 failed`. It checks the finite carrier-clock setup,
the finite character-block criterion for `H`, and the principal-symbol
commutator. It prints the overstrong sign-projector equivalence without
constructing `C` or testing that equivalence. Its bounded sub-principal
continuum residual remains open. Its exact source hash and the exact `QGEO.STATE.01`
ledger-row hash are checked by `checker.py`.

The positive-temperature/KMS repair is different and is pinned to
`verification/v258_dirac_covariance_induction.py:10-21,149-155`:

```text
C_beta = (I + exp(beta H))^-1,
H = beta^-1 log((I-C_beta) C_beta^-1).
```

For known nonzero `beta` and faithful finite covariance `0<C_beta<I`, this map
is injective and retains the magnitudes. The identity is exact; v258 checks it
numerically. Its tests first prescribe `Dblk` or the mass entries in `Dmass`,
construct `C=kms_cov(D)`, and recover `D` with `induce(C)`. The physical
identification `C_F = P_F C_Sigma P_F` is a recorded conditional statement
(`check(..., True)`), not a construction of an independent raw covariance.

There is a second conditional reconstruction if an actual one-particle
transfer operator is available on the same space. If `0 < T < I` on the
moving sector, a known `tau > 0` satisfies `T = exp(-tau |H|)`, and `T`
commutes with the sign projector `Q=2C-I`, then

```text
H = Q (-log T) / tau
```

reconstructs the gapped operator uniquely on that sector. This is an operator
identity and requires the full transfer operator, not only its population
spectrum. The TFPT rates `6 log(3/2)` and `6 log(3)` can enter such a formula
only after the compiler transfer has independently been identified with this
physical `T`; that identification is not supplied here. A fixed `T=I` sector
is a zero-mode/state case and is outside this sign-projector lemma.

The contract does not refute modular uniqueness for a fixed standard pair, the
full KMS/modular theorem, a full TFPT source, or a continuum construction. It
also does not refute the valid forward implication that an independently
proved mark-local DtN gives `[rho,H]=0` and hence state invariance. It only
removes the reverse inference from state invariance to full dynamics.

## Reproduction

```sh
cd experiments/theory-contracts/seam-state-dynamics-injectivity-20260918
python3 -B checker.py > run_normal.json
python3 -B -OO checker.py > run_optimized.json
cmp run_normal.json run_optimized.json
```

The compact committed certificate is `validation.json`. Expected result:
`status=PASS`, `verdict=PARTIAL`, `reverse_implication=REFUTED`, 25 exact
checks, zero failures, and `closed_gate_ids=[]`.

Primary background references: [Dierckx--Fannes--Pogorzelska](https://arxiv.org/abs/0709.1061)
and [Connes--Rovelli](https://arxiv.org/abs/gr-qc/9406019). This contract adds
no new theorem about those references; it only supplies the finite algebraic
counterexample and records the lost `|H|` premise.
