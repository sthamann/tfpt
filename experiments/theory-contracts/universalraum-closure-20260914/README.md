# Universalraum closure checks — 14 September 2026

Theory contract. NON-RH. No promotion to `verification/`, ledger, papers or website. Closes four of the
finite questions left open by
[`universalraum-paired-release-20260914/new-input-audit/singlet_f4.json`](../universalraum-paired-release-20260914/new-input-audit/singlet_f4.json)
(`exact_multiplicity_upper_bound`, `full_non_singlet_comparison`, `CAR_native_phase_equivalence`) and by the
consolidation [`universal_room/TFPT_UNIVERSALRAUM_KONSOLIDIERUNG_2026-09-14_fable.md`](../../../universal_room/TFPT_UNIVERSALRAUM_KONSOLIDIERUNG_2026-09-14_fable.md)
(fork A3 mediator locality, remainder A4). Reuses the Young-orthogonal Schur–Weyl machinery of
[`universalraum-fugen-20260914/clebsch_su4.py`](../universalraum-fugen-20260914/clebsch_su4.py) and the E8 root
helpers of [`universalraum-fugen-20260914/checker.py`](../universalraum-fugen-20260914/checker.py).

Model throughout: `H_C = J Σ_{e∈E(Clebsch)} P⁺_e` on 16 ququarts (40 edges, Clebsch graph (16,5,0,2));
fourth-order coefficient operator `F4` of the reference microscopic candidate,
`H_eff/J + 40 I = H_C/J + (ε²/2) F4 + O(ε⁴)`, `ε = t/Δ`, reference `ε = 1/20`.

## Results

| # | Task | Result | Closes |
|---|---|---|---|
| 1 | `singlet-dense` — full dense `eigh` of the 24 024-dim SU(4)-singlet sector (build 316 s, eigh 1376 s) | E₀/J = 11.045398337068423; E₁/J = 11.561762122802538; gap 0.5163637857341143 J; **first excited level has multiplicity exactly 4**; residuals ≤ 1.7·10⁻¹³; smallest separation between distinct clusters among the lowest 60 levels 4.27·10⁻³ J. All seven lowest clusters are **irreducible representations of Aut(Clebsch) ≅ W(D₅) = 2⁴:S₅ (order 1920)**: 1 (trivial), **4 (standard rep of S₅, χ(01) = +2, 2⁴ acts trivially)**, 20, 5 ([3,2]), 10, 15, 5. No accidental degeneracy. | `exact_multiplicity_upper_bound` (Dublett → Quartett is now an algebraic statement) |
| 2 | `sectors-f4` — lowest 8 levels of **all 64 SU(4) sectors** (Σ dim = 6 952 660, largest 512 512) with first-order F4 correction in both mediator conventions | Bare: singlet ground 11.045398 J, lowest non-singlet = adjoint (5,4,4,3) at 12.133537 J (gap 1.088 J). Corrected at ε = 1/20, global mediators: singlet 11.739759, quartet 12.290877, adjoint 12.818330. Local mediators: singlet 11.960549, quartet 12.447024, adjoint 12.990520. **Singlet stays ground state and the quartet stays first excitation in both conventions.** Singlet-gap coefficient: **+13.9018 ε² (shared mediators) vs −11.9555 ε² (local mediators)** — the A3 decision flips the sign of the leading correction. Max Lanczos residual 2.3·10⁻⁹, F4 Hermiticity defect ≤ 2.6·10⁻¹². | `full_non_singlet_comparison` |
| 3 | `phase-adapter` — Frenkel–Kac cocycle ε(m,n) = (−1)^{mᵀBn} on E8 (cocycle identity, commutator factor and bracket antisymmetry self-tested on 3360 root pairs); native vertex signs ε(α_{s,a}, α_{t,b}) for all 40 edges × 12 ordered colour pairs; gauge problems over F₂ | **Level 1** (site-colour signs η(s,a) only): consistent, rank 45, nullity 19 → every native edge map is exactly the colour antisymmetriser, `K_e†K_e = I − S_e` for all 40 edges simultaneously; hence `H⁽²⁾` and all 160 overlapping-pair F4 terms of the native E8 model coincide with the reference model. **Level 2, shared mediators** (η + one sign per mediator μ ∈ (10,6)): inconsistent, rank 115/124, 156 dependent inconsistent rows; ℤ₂ flux witness on the 6-cycle 0–10–2–12–1–11–0 with colours (0,1). All 40 squares have trivial flux. **Level 2, local mediators** (one sign per edge and colour pair): consistent, rank 285, nullity 19 → exact sign-gauge equivalence of native and reference model. | `CAR_native_phase_equivalence` (tensor layer): **true under local mediators**, false under shared mediators |
| 4 | `locality` — same-label disjoint edge pairs on Clebsch and its ℤ-coverings | Clebsch: 160 overlapping pairs, 60 disjoint same-label pairs (10 labels × C(4,2)). Covering with L copies: overlapping pairs 160 L (extensive), same-label pairs 10·C(4L,2) ~ 8 L² (non-extensive). With |K₄|/J = 4(t/Δ)² per pair, shared mediators give an O(N²) fourth-order energy. | **Fork A3 decided: local mediators** (or cavity scaling t ~ N^{−1/2}, which kills J = 2t²/Δ) |
| 5 | `remainder` — two-bond cluster series (exact 3×3 symmetric block, closed antisymmetric/single-bond forms) | Connected coefficients: symmetric −2 g⁴/Δ³ + 8 g⁶/Δ⁵, antisymmetric +2 g⁴/Δ³ − 12 g⁶/Δ⁵ (g = √2 t); numeric residual after sixth order ≤ 2.7·10⁻⁹ at g = 0.05. Sixth/fourth ratio at t/Δ = 1/20: 2 % (sym), 3 % (asym). Global Schur criterion ‖V‖ < Δ certifies only t/Δ ≲ 1/640; conservative per-site strength at 1/20 is ≈ 1.0 Δ. | `higher_order_bound` **remains open**, now quantified: needs the local Schrieffer–Wolff theorem (Bravyi–DiVincenzo–Loss 2011) with explicit constants |

Joint reading of 3 + 4: the mediator-locality fork (A3) and the phase adapter (A6, tensor layer) are one
question. The ℤ₂ flux that prevents a uniform-sign gauge lives entirely in the *shared-mediator* convention,
and that convention is excluded by extensivity. Under local mediators the native E8 vertex data and the
uniform reference model are the same Hamiltonian to fourth order.

Not closed here (and not claimed): CAR fermionic layer beyond the tensor convention, native TFPT phase
adapter across levels (algebra → microdynamics → state → observation), thermodynamic remainder bound, T1–T8.
A parallel contract [`universalraum-closure-round-20260914/`](../universalraum-closure-round-20260914/)
computes bare non-singlet sectors, the dressed star filter and the T1 selection principle; results are
complementary, not duplicated.

## Files

- `closure_checks.py` — all tasks (`singlet-dense`, `sectors-f4`, `phase-adapter`, `locality`, `remainder`, `all-light`).
- `test_closure.py` — guard tests (graph = fugen edge list; |Aut| = 1920 with 16 translations; Schur–Weyl
  representation irreducible on a small irrep; cocycle identities; native edge map `K†K = I − S`; F₂ solver).
- `validation_singlet_dense.json`, `validation_sectors_f4.json` (checker sha `7d3a989c…`, run 14:13–14:46),
  `validation_phase_adapter.json`, `validation_locality.json`, `validation_remainder.json` (checker sha `0740d2de…`).
  The heavy runs were produced by the earlier checker version; the later edits added the `remainder` task and
  text only, and did not touch the code paths of tasks 1–2.

## Reproduction

```sh
cd experiments/theory-contracts/universalraum-closure-20260914
python3 test_closure.py
python3 closure_checks.py all-light           # phase adapter, locality, remainder (seconds)
python3 closure_checks.py singlet-dense       # ~30 min, ~20 GB RAM (dense 24 024²)
python3 closure_checks.py sectors-f4 --k 8    # ~30 min, all 64 sectors
```

Environment: Python 3.14.3, NumPy 2.4.2 (Accelerate), SciPy 1.17.0, SymPy 1.14.0.
