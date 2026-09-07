<div align="center">

# TFPT

### Can the structure of fundamental physics be compiled from one discrete seed and π?

<a href="assets/readme/00_hero.png"><img src="assets/readme/00_hero.png" alt="TFPT: one seed a=(1,1,2)+π → E8 consistency hull → Standard Model, α⁻¹=137.0359992, gravity, cosmology → 27 falsifiable predictions, 3 verification engines" width="880"></a>

**TFPT is a falsifiable, machine-checked framework that reconstructs major dimensionless structures
of particle physics, gravity and cosmology from `a = (1, 1, 2)` and `π`** — a *candidate*
parameter-free compiler for the dimensionless skeleton of fundamental physics.

<p>
  <a href="https://github.com/sthamann/tfpt/actions/workflows/verify.yml"><img alt="Core Verification" src="https://github.com/sthamann/tfpt/actions/workflows/verify.yml/badge.svg"></a>
  <a href="https://github.com/sthamann/tfpt/actions/workflows/audit.yml"><img alt="Sync Audit" src="https://github.com/sthamann/tfpt/actions/workflows/audit.yml/badge.svg"></a>
  <a href="https://github.com/sthamann/tfpt/actions/workflows/lean.yml"><img alt="Lean Proofs" src="https://github.com/sthamann/tfpt/actions/workflows/lean.yml/badge.svg"></a>
  <br>
  <img alt="Version 5.4" src="https://img.shields.io/badge/version-5.4-6e56cf">
  <img alt="Predictions" src="https://img.shields.io/badge/predictions-27_falsifiable-db2777">
  <img alt="Engines" src="https://img.shields.io/badge/verification-Python_·_Wolfram_·_Lean-16a34a">
  <a href="https://doi.org/10.5281/zenodo.21128999"><img alt="DOI" src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21128999-3b82f6"></a>
  <a href="https://www.fixpoint-theory.com"><img alt="Website" src="https://img.shields.io/badge/website-fixpoint--theory.com-2563eb"></a>
</p>

**[▶︎ Understand it in five and a half minutes](https://www.fixpoint-theory.com/#intro-video)** ·
**[⚡ Run the verifier](#run-the-verifier)** ·
**[📄 Read the theory](docs/THEORY.md)**

</div>

This repository contains the complete TFPT compiler-closure document set, **27 status-graded,
falsifiable test surfaces**
(the 16-entry core registry frozen before the data), three independent
verification engines (Python + Wolfram + Lean), and a versioned status ledger that types every
claim — including its **explicit open problems and falsification criteria**.

## Non-RH research update — 7 September 2026

The [research contracts through Round27](experiments/theory-contracts/ROUND27_STATUS.md)
now accompany the updated papers and [public research overview](https://www.fixpoint-theory.com/verification#non-rh-round27).
The latest finite-regulator result removes an artificial charge factor from
the signed-history error bounds, improves certified charge/hop cutoffs, and
supplies a nonzero quadratic-memory cutoff after the signed sum. It does
not evaluate the complete interacting partition or close the physical
T1–T8 gates. Earlier round records retain their original local-only wording
as historical provenance; this integration ships the archive without
rewriting those source-pinned snapshots.

## Video

[![TFPT in 5½ minutes](website/public/intro/tfpt-intro-poster.jpeg)](https://www.fixpoint-theory.com/#intro-video)

The 5½-minute film — updated 2026-08-31: compiler, alpha fixed point, dual status card, the August structural wave, falsification discipline, live predictions.

---

## Start here

Different readers want different proof. Pick your route:

| I am… | Start with |
|---|---|
| a **physicist** | [`docs/FOR_PHYSICISTS.md`](docs/FOR_PHYSICISTS.md) — the assumptions, the derivation, the open interfaces |
| a **mathematician** | [`docs/FOR_MATHEMATICIANS.md`](docs/FOR_MATHEMATICIANS.md) — the `E8` closure and the formal certificates |
| here to **verify the claims** | [Run the 30-second verifier](#run-the-verifier), then [`docs/VERIFICATION.md`](docs/VERIFICATION.md) |
| here for the **intuition** | [the 5½-minute film](https://www.fixpoint-theory.com/#intro-video) |
| here to **falsify it** | [`docs/FALSIFICATION.md`](docs/FALSIFICATION.md) — the kill tests |

---

## Run the verifier

Re-derive TFPT's headline claims from the two axioms, in about a second:

<p align="center"><img src="assets/readme/verify-demo.gif" alt="./verify re-derives the E8 closure, α⁻¹ = 137.0359992 and 3 generations from a=(1,1,2)+π" width="760"></p>

```bash
git clone https://github.com/sthamann/tfpt && cd tfpt
pip install -r requirements.txt

./verify            # ~1s    : the core claim, re-derived from the axioms
./verify --full     # ~4-5h  : the entire Python suite, 1028 modules (ALL CHECKS PASSED)
./verify --release  #         : documents + suite + website + sync audit
```

No local toolchain? `docker run --rm ghcr.io/sthamann/tfpt:latest`. The three independent engines
are one flag away: `./verify --wolfram`, `./verify --lean`, `./verify --audit`. Full detail in
[`docs/VERIFICATION.md`](docs/VERIFICATION.md).

Strict TOE status (2026-09-05): v1026–v1030 narrow only TEL-B/T2, T4 and T6–T8
subgates. The relaxed TEL-B norm theorem is uniform for even N≥16, but every T1–T8
gate remains `[O]`, and a shared 3+1D parent is still missing.

Round 7 (`v1031`–`v1035`, including the round-6 quantum prerequisite) adds
233 typed checks and full proofs in the contracts paper: a zero-mean free
Weyl/Fock curvature field with helicities ±2; auxiliary Z4 flux-register corners
with a twist-weight/parity obstruction; the **factorized** mirror lower gap
`1+sqrt(3)/2`; and physical-Fourier Ward propagation for **prescribed** sources.
These are not a common-parent derivation, microscopic MMST, an interacting
mirror-gap theorem or universal nonlinear gravity. Every T1–T8 gate stays `[O]`.
Run each `verification/v1031_*.py` through `v1035_*.py` locally with the repository
dependencies. The source-auditing v1033/v1034 require a full checkout, not Pyodide.

Portability amendment (2026-09-06): v1033 now treats the degenerate QWZ zero
space without an eigensolver-selected vacuum. It reports a fixed-particle
ground-space mixture and bounds over all pure fillings; the corrected numeric
interpretation is explicit in the contracts paper. The 233-check count and
open gates do not change. A separate [free 3D scalar theory contract](experiments/theory-contracts/free-scalar-3d/README.md)
gives the complete local symmetric-stress derivation and 68 exact checks,
including its finite-volume Weyl operator lift. It is unpromoted and does not
solve interacting matter or nonlinear gravity.

For the full native certificate chain (including the interval inputs), run
`v1022_telb_round3_certificates.py`, `v1025_telb_c1_c2a_certificates.py` and
`v1026_telb_round4_closure.py` from `verification/` in the environment installed
from `requirements.txt` (`python-flint==0.9.0`). The browser reproducer explicitly
excludes these three modules; it does not replace their native certificates.

---

## The five results — and their honest status

Not everything below has the same epistemic status, and saying so is the point:

| Claim | Result | Status |
|---|---|---|
| `E8` closure | `(D5 ⊕ A3) + μ4 ≅ E8`, 240 roots, glue index 4 | **Exact** — machine-proven lattice identity `[E]` |
| Number of generations | `N_fam = 3` | **Exact within the compiler** `[E]` |
| Fine-structure constant | `α⁻¹ = 137.0359992` | **Exact numerical identity** — unique Ward root, interval-verified `[E]` (1.9σ from CODATA-2022) |
| Physical origin of the seam | `SEAM.EQUIV.01` | **Open** — the MMST route is closed *modulo a cited theorem* (`SEAM.EQUIV.MMST.01` `[C]`); the parent claim is not proven end-to-end `[O]` |
| Cosmic birefringence | `β = φ₀/(4π) ≈ 0.2424°` | **Falsifiable prediction** — decided by CMB polarimetry `[X]` |

Markers: `[E]` exact/machine-proven · `[C]` conditional · `[O]` open/axiom · `[X]` kill test. The
authoritative per-claim status is [`verification/status_ledger.csv`](verification/status_ledger.csv)
— **the ledger wins**. Full matrix and marker system in [`docs/CLAIMS.md`](docs/CLAIMS.md).

---

## What is genuinely open

The discrete/algebraic compiler is closed (`[E]`). Within that compiler lane, the historical
residual is **three named interface problems** (the seam interface carries two routes):

| Interface | Question | Status |
|---|---|---|
| `v_geo` | the one metrology unit (`= 1/√G`); No-Unit Thm: a scale-invariant seam has no compiler scale; interface structurally closed as an R+ scale torsor in calibration form (v725) | primitive `[O]` |
| `SEAM.EQUIV.01` | the raw seam *is* the holomorphic `(E8)₁` net (parent target; closed if either route closes) | `[O]` as an unconditional claim |
| `SEAM.EQUIV.MMST.01` | the MMST route: lattice + S3 stack + Lean, scaling limit cited | `[C]` — closed modulo cited theorems |
| `SEAM.EQUIV.TWISTOR.01` | the twistor route: the open Costello–Li construction (prepared by `CELEST.SEAM.01`) | `[O]` |
| `F_transfer` | one functor, four typed interfaces (Koide, `η_B`, axion, `m_p/m_e`) | `[C]` |

(Route split 2026-07-22 — an ID restructuring, no status change in substance: the statements
previously attached to "`SEAM.EQUIV.01` closed modulo a cited theorem" now live on the MMST route ID.)

This compiler accounting is not the physical TOE accounting. `TFPT.TOE.COMPLETE.01` is the AND of
eight independent gates T1–T8; all eight remain `[O]`. Round 4 proves the relaxed uniform TEL-B
norm and adds scoped algebraic/constraint results, but makes no aggregate marker move.
No single shared 3+1D parent currently satisfies T3–T8.
The complete gate matrix and remaining obligations are in
[`tfpt_research_contracts.tex`](tfpt_research_contracts.tex) and
[`docs/OPEN_PROBLEMS.md`](docs/OPEN_PROBLEMS.md).

---

## How to falsify TFPT

The predictions are frozen ([`predictions_frozen.json`](verification/predictions_frozen.json),
2026-06-09) and locked to their formulas on every run — the freeze protects **future**
measurements; for historically known observables the honest statistics caveat is in
[`docs/FALSIFICATION.md`](docs/FALSIFICATION.md) (contract `PRED.JOINTLIKELIHOOD.01`). A
confirmed measurement outside a window kills the claim:

| Observable | TFPT frozen value | Decided by |
|---|---|---|
| Leptonic CP phase | `δ_PMNS = 240°` (Galois-locked) | DUNE, Hyper-K |
| Cosmic birefringence | `β ≈ 0.2424°` | CMB polarimetry |
| Reactor angle | `sin²θ₁₃ = 0.02311` *(now ~2.0σ tension)* | JUNO |

All kill tests, the null model (200,000 look-alikes score ≤ 5/13; TFPT 13/13 — under its
declared null model; see the statistics caveat there), and the live
scorecard: [`docs/FALSIFICATION.md`](docs/FALSIFICATION.md) ·
[fixpoint-theory.com/falsification](https://www.fixpoint-theory.com/falsification).

---

## Try to break TFPT

For a fundamental-physics theory, **openly invited criticism is a trust signal**. The most valuable
contributions, in order of impact:

1. **Reproduce or falsify a frozen prediction.**
2. **Find a circular dependency** — a "derived" quantity that used its own target.
3. **Identify an unstated physical assumption** doing load-bearing work.
4. **Challenge a claimed uniqueness result** (the `E8` glue, the `α⁻¹` root).
5. **Close or kill one compiler interface or one T1–T8 completeness gate.**

Ready-made [issue templates](.github/ISSUE_TEMPLATE) exist for exactly these: *claim challenge*,
*reproduction failure*, *mathematical counterexample*, *physical interpretation*, *prediction
update*, and *documentation*. This repository is meant to be a scientific discussion space, not
just an archive.

---

## Repository structure

```
├── verify                 # the one-command verifier (quick / --full / --release)
├── README.md              # you are here
├── docs/                  # THEORY · CLAIMS · OPEN_PROBLEMS · FALSIFICATION
│                          # VERIFICATION · FOR_PHYSICISTS · FOR_MATHEMATICIANS
├── verification/          # 1028 registered modules, run_all.py, the status ledger,
│                          # the Wolfram second path, the red-team layer
├── experiments/           # research explorations + the Lean 4 proofs (not claims until promoted)
├── rh/                    # the consolidated RH-program workspace (inventory, Lean pilot, paper,
│                          # run_rh.py suite — gated by build.sh audit; no RH claim)
├── website/               # the public mirror (fixpoint-theory.com), kept byte-identical by the audit
├── *.tex                  # the 12 published theory documents + the repo-only prime-front
│                          # research documentation (see docs/THEORY.md)
└── build.sh               # the build + sync pipeline (notes · gen · website · audit · release)
```

> _Disambiguation:_ this is the **physics** theory TFPT (a compiler closure for the Standard Model).
> It is not the unrelated Brouwer–Lefschetz "topological fixed point theory" of mathematics.

---

## Citation & license

```bibtex
@misc{hamann2026tfpt,
  title  = {Topological Fixed-Point Theory (TFPT): Two Axioms, One Compiler,
            the Standard-Model Skeleton Derived},
  author = {Hamann, Stefan and Rizzo, Alessandro},
  year   = {2026},
  note   = {Version 5.4},
  doi    = {10.5281/zenodo.21128999},
  url    = {https://doi.org/10.5281/zenodo.21128999}
}
```

- **Website (interactive):** <https://www.fixpoint-theory.com> — reading guide, compiler walkthrough,
  in-browser reproducer for every script.
- **Archived deposit (DOI):** <https://doi.org/10.5281/zenodo.21128999> (Zenodo, v5.4);
  concept DOI for all versions: <https://doi.org/10.5281/zenodo.18328333>.
- **AI/agent context:** <https://www.fixpoint-theory.com/llms.txt>

*Claim discipline: nothing in this repository is marked closed that is not machine-verified, and no
dimensionful quantity is claimed as a derivation from pure numbers.*
