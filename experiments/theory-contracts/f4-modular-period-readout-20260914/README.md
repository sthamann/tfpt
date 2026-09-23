# F4 modular period readout: native compiler lane (factorization firewall)

14. September 2026 · **NON-RH** · **experiments/theory-contracts only**.  
Decides whether audited Universalraum / F4 primitives supply a **non-oracular**
`poly(bit_length N)` modular-multiplication and period-readout stack.  
**No promotion** to verification, ledger, papers, or website.

## Firewall

| Allowed | Forbidden |
|---|---|
| Separate arithmetic *specification* from *native gate compilation* | Claim polylog factoring, RH, or P=NP |
| Toy moduli `N=15`, `N=35` with explicit orders | Retry dead quadratic E8 FFT as scalable modmul |
| Asymptotic cost guards vs Shor reference model | Invent a native modmul compiler not present in pinned audits |
| Honest verdict enum scoped to this lane | Treat direct `y ↦ a·y mod N` permutation tables as “compilation” |

## Hypothesis (pre-registered)

Toy modular permutations are easy to **specify**, but no scalable native map from the
fixed **256 / 544**-dimensional audited blocks to `n`-bit modular multiplication exists.
Direct full-permutation construction is an **oracle / encoding assumption**; expected
verdict: **`BLOCKED_MISSING_NATIVE_COMPILER`**, not breakthrough.

## Verified inputs (pinned)

- **r647** (`e8_composite_gauss_probe.py`): `S_N(t)=N^4 gcd(t,N)^4` but **O(N)** moment
  acquisition and **O(N³)** tree contraction; quadratic E8 FFT output uniform at coprime
  ticks; amplified useful ticks remain **N^(1/4)** scale. Verdict already
  `E8_COUNT_FACTOR_EQUIVALENT_NO_FAST_READOUT`.
- **Paired-release audit** (`new-input-audit/check.py`): matter **256D**, closed microscopic
  star **544D**, local F4 columns **832D**; hard tensor-product F4; **no** factor-graph
  configured compilation path for `Z_N` multiplication.

Source SHA-256: `source_manifest.json`.

## Exact models

### Oracle vs native

- **`ORACLE_SPECIFICATION`**: any unitary/permutation/matrix built by tabulating
  `y ↦ (a·y) mod N` (or full modular exponentiation) without deriving it from pinned
  audited gates. The compact arithmetic rule `(N,a)` itself is not expensive; the
  reported `N²` count is only the size of a materialized dense one-hot table, **not**
  a lower bound on reversible modular-arithmetic circuits.
- **`NATIVE_COMPILATION`**: unitary expressed only through the pinned interface:
  4-carrier F4 words, `U0`/record macros, 256/544/832D embeddings — with gate count
  **`poly(bit_length N)`** and **no** explicit `N×N` permutation input.

### Shor reference cost (implementation-only baseline)

Not proved here; standard quantum model from [Shor (1995)](https://arxiv.org/abs/quant-ph/9508027):

- `b = bit_length(N)`; exponent register **O(b²)** qubits.
- **O(b)** controlled modular multiplies for exponentiation, each intended **`poly(b)`** in
  the usual circuit model → overall **`poly(b)`** quantum time **given** native controlled
  modmul + QFT primitives.
- Classical continued-fraction / gcd postprocessing **`poly(b)`**.

This contract asks whether **TFPT audited primitives** supply those native modmul/QFT
blocks. Matching Shor **only after** injecting oracle tables counts as
**`SHOR_IMPLEMENTATION_ONLY`**, not native breakthrough.

### Success / kill

| Outcome | Condition |
|---|---|
| **`NATIVE_POLYLOG_MODMUL_FOUND`** (kill / success) | Documented native compiler + replay checks; modmul gate count **`O(poly(b))`**, no `ORACLE_SPECIFICATION` |
| **`SHOR_IMPLEMENTATION_ONLY`** | Period/order pipeline works only with oracle modmul + standard Shor classical postprocess |
| **`BLOCKED_MISSING_NATIVE_COMPILER`** | No scalable encoding; fixed-dimension obstruction + absent interface |
| **`BLOCKED_ORACLE_ONLY`** | Only oracle permutation path; no audited compilation |

## Toys

| Modulus | Base `a` | Notes |
|---|---|---|
| 15 | 7 | `gcd(a,N)=1`; order and factor demo |
| 35 | 3 | Requested `a=7` already reveals factor 7 by gcd and is not a permutation; the period lane and its oracle table therefore use coprime **`a=3`** (documented) |

## Reproduction

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B checker.py --output validation.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B -OO checker.py --output validation_optimized.json
python3 -B checker.py --replay
```

Normal and `-OO` reports must be byte-identical. `replay.json` records in-memory mutants.

## Claims not made

No new factoring algorithm, no RH statement, no P=NP, no ledger `[E]` upgrade.
