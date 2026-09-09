# What is genuinely open

> The honest frontier. If you want to *close* one of these, see the "Try to break TFPT" section
> of the [README](../README.md#try-to-break-tfpt) and open a claim challenge.

## Current research frontier — 9 September 2026

**All T1–T8 remain open.** The [consolidation and acceptance map](../experiments/theory-contracts/RESEARCH_2026-09-09.md)
supersedes older summaries as the current research entry point. New progress:
integer charged fields from the actual filled QWZ sea, neutral four-point
collision control, full dynamics and neutral ground-state representations
for a separate compact-U(1) test parent, and exact Clock/cocycle restrictions.

The first missing T2 step is now a renormalized, smeared **half-charge
inter-sector field** with source energy and adjoint control, followed by
source-derived eight-channel E8 and family/Clock identification. Neutral
determinants, integer CAR fields and a formal E8 charge lattice are not
interchangeable proofs of that step. For T3–T8 the same selected 3+1D parent
is still missing. The prototype's scalar momentum symbol cannot acquire a
Weyl node by scalar retuning alone. Wilson spectral bounds do not prove a
mass gap, and periodic ground-state cluster points do not select a unique state.

**Reading older seam reductions below:** “closed modulo cited theorems”
describes a conditional target-net route. It does not mean that the actual
microscopic charged seam has been identified, nor that only invoking a
continuum theorem would complete T2. The original source hypotheses and
the physical source-to-target bridge must both be discharged.

## Earlier status and conditional compiler accounting

> **Strict TOE status (2026-09-05).** `TFPT.TOE.COMPLETE.01` and every physical gate T1–T8
> remain open (`[O]`). Round 4 (`v1026`–`v1030`) proves the relaxed uniform TEL-B norm
> below 2.995906 for all even N≥16 and adds scoped algebraic/constraint results.
> Microscopic one-edge FE-GEN/ALG-EXH, the chiral dynamical-gauge construction,
> physical mass generation, the collective spin-2 embedding and global state selection
> remain unproved; no parent marker moves. A single shared 3+1D parent satisfying T3–T8 is still
> missing.
>
> Round 7 (`v1031`–`v1035`) adds a positive local covariant **free** curvature
> field of helicities ±2, not its microscopic TFPT embedding. Auxiliary charged
> corners still have the quarter-twist mismatch `h=1/4 != h_lambda=1`;
> the onsite mirror gap `1+sqrt(3)/2` is factorized, not an interacting gap theorem.
> Prescribed-source linear Ward propagation does not settle dynamical quantum
> matter, universal nonlinear coupling or the removed homogeneous block.

**Compiler residual (historical v5.4 view, scope-corrected 2026-09-05).** The
discrete/algebraic compiler is closed (`[E]`). Within that compiler accounting, the residual is
**three named interface problems** — not a diffuse list:

| Interface | Question | Status |
|---|---|---|
| `v_geo` | the one metrology unit (`=1/√G = m/μ`); No-Unit Thm: no compiler scale | primitive `[O]` |
| `G_net` | `SEAM.EQUIV.01`: the raw seam *is* the holomorphic `(E8)₁` net | `[C]` — closed modulo a cited theorem |
| `F_transfer` | one functor, four typed interfaces (Koide, `η_B`, axion, `m_p/m_e`) | `[C]` |

The remaining distance *within this compiler-residual accounting* is therefore not a list but
**one metrology unit** (`v_geo`, the No-Unit
Theorem, `v153`/`v364`) plus the **typed `F_transfer` interfaces** (Koide, `η_B`, axion, `m_p/m_e`
— deliberately `[C]`, never compiler outputs), above the **cited-theorem ceiling** on the seam
(`SEAM.EQUIV.01` closed modulo MMST + OS reconstruction, Lean `FORM.SEAM.MMST.01`) and with
**`QG.AMB.01` a `[C]` redundancy** (`v369`). The central theorem reads as a clean simple-current
extension, `(D₅)₁⊗(A₃)₁ ⋊ ⟨(1,1)⟩ ≅ (E₈)₁` (index 4, c = 8, μ = 1 ⇒ holomorphic ⇒ E₈, `v154`).

---

## Deep dive — parameter-free gravity, the all-orders perturbative leg, and `SEAM.EQUIV.01`

**Gravity: a *conditional* entanglement-thermodynamic route, with the 8π coefficient multiply
matched.** What is actually established (honest typing, 2026-08-27 review round): (a) multiple
*consistent* `8π` coefficient matches — the thermodynamic origin `2π/η` coincides with the
geometric one `|Z₂|·2π·χ` via `|μ₄| = |Z₂|·χ(S²) = 4`, so `c₃` is triply over-determined
(anchor, geometry, thermodynamics, `v358`/`v359`); (b) a **conditional** local
entanglement-thermodynamic GR route — the entanglement-equilibrium derivation (Jacobson 2015,
arXiv:1505.04753) yields the *semiclassical* Einstein equation under its specific assumptions
(small geodesic balls, locally maximally symmetric vacuum, first-order variation, conformal
matter; the nonconformal case needs an extra conjecture, cf. Casini–Galante–Myers
arXiv:1601.00528), and with TFPT's atoms both coefficients come out fixed — `c₃⁻¹ = 8π` and `Λ`
from `α` (`ρ_Λ = (3/4π²)e^{−2α⁻¹}`, `v60`), with the Einstein tensor forced by Lovelock so
matter conservation is an output (`v359`); (c) an `R+R²` effective structure. **What does NOT
follow from this route** (explicitly, per `GRAV.NONCIRCULAR.01` and `QFT4D.OS.RECON.01` in
`tfpt_research_contracts`): a quantized dynamical metric, the nonperturbative state/path-integral
structure, black-hole unitarity, global solutions/boundary conditions — and the *existence of
the 4D QFT whose entanglement is being varied*, which the derivation assumes (the CHM ball
modular Hamiltonian and the Bisognano–Wichmann boost enter as **inputs**; the chain is
conditional on the 4D package and must never be cited as evidence *for* it). The residual is
therefore *not* only the equation-of-state fork and the unit `v_geo` — those are the residuals
*within* the conditional route; the route's own hypotheses are the larger open item. An
**external candidate** for the missing action level — Bianconi's entropic action, *Gravity from
entropy*, PRD 111, 066001 (2025) — is quantified in `v473`: her free constant is pinned exactly
(`β′_B = c₃/6 = 1/(48π)`), her emergent `Λ` reproduces the `v60` branch with the exact target
`Tr Q² = 32c₃⁴`, and the `R²` sector misses the TFPT Starobinsky coefficient by exactly `3(8π)⁹ ≈ 10¹³`
(pre-registered kill test) — nothing closes, the typing stays `[O]`. The operator level is executed in
`v474`: the D₅ Clifford/spinor structure exhibited on the carrier Fock space `Λ•ℂ⁵` (ten exact gammas,
the 45-dim `so(10)` preserving the 16-dim even subspace), the Hodge fold identified as the `5 → 5̄`
conjugation (her `1+5+10` becomes the GUT `16 = 1+5̄+10`), and the `Q`-target decided — integer supports
exactly `{|ℤ₂|, rank E₈, 2^g_car}` with minimal uniform `q = c₃²`; the naive pair-block (`10`) reading is
killed. The `R²` kill test itself is executed in `v475`: with exact tensorial factors (vacuum action
`3βR + (17/24)β²R²` on the maximally symmetric background) the raw entropic scalaron comes out
**trans-Planckian** (`m² = 4608π²/17 M̄²`, ≈ 51.7 M̄), so the light-trace-mode reading is dead and
KMS-spectral renormalisation is the only surviving `R²` route; the Lorentzian-positivity caveat now has
an explicit timelike witness (`1 − αv² ≤ 0`). The compression conjecture (AP2) is made well-posed in
`v476`: the literal operator-side reading is ill-posed on a pure bulk, the state-side reading (build
`Δ_Σ` from the compressed relative metric) is forced, and the mismatch between the readings is exactly
second order in the cross-cut correlations and gap-suppressed — AP2 itself stays `[O]`. The surviving
`R²` route is typed as ONE moment condition in `v477`: the entropic action is the flat scale-integral of
relative heat-kernel actions, and demanding `m² = c₃⁷M̄²` forces exactly `μ₂/μ₁² = (72/17)(8π)⁹` — with
the closure identity `(4608π²/17)/((72/17)(8π)⁹) = c₃⁷` holding identically, the 13 orders are a
scale-measure datum which TFPT's own KMS moment (`v36` `f₀`) fixes correctly; zero new dials,
consistency not derivation `[C]`. First steps on the two remaining legs are in `v478`: the compressed
critical state's modular data flows to the CHM/Bisognano–Wichmann geometric form (`c_est → 1` at 2×10⁻⁴,
CHM parabola, even bands exactly zero) — meeting TFPT's Einstein-derivation input (`v323`/`v358`) — and
the measure condition reduces to one exact KMS time `t₀ = ln(72/17) + 9ln(8π) = 30.461` (the `h(E₈) = 30`
near-miss explicitly declined); both legs stay `[O]`. The global measure (`QG.AMB.01`) is now a
**`[C]` redundancy** (`v369`): a certification object rather than missing dynamics, conditional on
`SEAM.EQUIV.01` and Bisognano–Wichmann.

**The perturbative 4D leg: a local perturbative construction under the EG/BRST hypotheses**
(not "full 4D physics" — the binding phrasing rule of `QFT4D.OS.RECON.01`). The matter+gauge
`S_pert` is a typed Epstein–Glaser/BRST contract (`v381`, `QFT4D.EG.ALLORDER.01`): dimension-4
power-counting ⇒ a finite counterterm space, BRST nilpotency `s²=0` for the carrier
`su(3)×su(2)`, and the seam gap ⇒ the adiabatic limit, with all-order `T_n` existence and the
Slavnov–Taylor identity imported. The massless-sector weak adiabatic limit is the cited Duch
theorem (arXiv:1801.10147), whose hypotheses must still be verified for the concrete TFPT model
— a seam-transfer gap does not substitute for the IR structure of massless photons/gluons; and
even full EG/BRST success yields none of: confinement/hadron spectrum, the Yang–Mills mass gap,
asymptotic charged states in QED, the nonperturbative Higgs vacuum, a controlled full S-matrix
(the
`R²/Weyl²` Stelle ghost is fenced out as the resummed entire form factor, `v304`/`v370`/`v380`). The
EM-Ward functional origin — *why exactly that* `F_U(1)` — is named as the tracked target
`ALPHA.QUILLEN.EXACT.01` (`v382`), a face of `SEAM.EQUIV.01`; the `α⁻¹` value itself stays `[E]`. Four
honest steps narrow that target without closing it: a solvable 4D model reaches the `a₄` heat-kernel
order (`v433`); the matter factor `b₁` is the `U(1)_Y` `a₄` coefficient via the `β = a₄` theorem,
collapsing the three residuals to one `[C]` (the seam `F`-normalisation) + one `[O]` (`v434`); and a
`π`-power test isolates the cubic `α³` as the *unique* metric-independent (`π⁰`) topological rung, whose
coefficient is a conditional integer Chern–Simons level (`v435`). A fifth step (`v470`) upgrades both
leftovers: the `α³` level **equals the computed bulk Chern invariant** `|C| = 1` of the same p+ip collar
that realises S3, and the seam `F`-normalisation is retyped as the **affine embedding index**
`k_Y = tr(Y²)/tr(T3²) = 5/3` (Ginsparg 1987; `(3/5)·(41/6) = 41/10 = b₁` exactly). A sixth step (`v472`)
exhibits the bridge lemma at the finite level. What stays `[O]` is the **continuum** ζ-det identification
on the abstract seam (= the `SEAM.EQUIV.01` face), so `ALPHA.QUILLEN.EXACT.01` stays `[O]`.

**One principle behind "parameter-free", and the shape of what's left.** A bird's-eye synthesis
shows every TFPT sector is the *same* object — a gapped operator with a unique attractor (the physics)
and a spectral gap (the reason there is no free dial); so "parameter-freeness is a theorem" is **one**
spectral-gap statement, theory-wide, not a list of coincidences (`v383`). Precision (2026-08-27, per
`DYN.MARKOV.EMBED.01`): the shared shape is a universal *contraction class* — shared gap and
multiplier — not one physical clock (`v723`/`v724`/`v777`). The `v384` residual-matrix statement
("every open item is an external math proof, theorem-forbidden, or external physics") applies to the
*compiler-internal* residual matrix as scoped in `v384` — it does **not** mean the physics
construction is done. The contract scope fence in `tfpt_research_contracts` (ledger wins) honestly
lists as open: the interacting reflection positivity, mirror decoupling, the internal `SU(2)` as a
genuine gauge action, both helicities in the shared microscopic parent (the independent free
curvature target now has helicities ±2), local 4D matter fields, EWSB, confinement — now registered as
the named contracts `SEAM.BULK4D.RECON.01`, `QFT4D.OS.RECON.01`, `CHIRAL4D.NOMIRROR.01`,
`DYN.UNITARY.DILATION.01` under the top-level rule `DIMENSION.UPLIFT.FIREWALL.01` (no 1+1D theorem
closes a 3+1D claim).

**The TFPT4D master route (2026-08-27, master-route wave).** The 4D contracts above are now
organized into **one constructive route** (the "master route" programme section in
`tfpt_research_contracts`): the working hypothesis is that TFPT is not missing twenty independent
formulas but *one* growth principle — the unique local, reflection-positive, approximately
quantum-Markovian 4D completion of the seam algebra, anomaly-free, with exactly one relevant
dimensionful direction (= the `v_geo` calibration torsor, `ANCHOR.VGEO.02`). New rows: the
**conditional 4D dimension selector** `DIMENSION.SELECTOR.4D.01` `[C]` (machine-checked, `v975`:
`d = 4` unique + minimal + overdetermined under {`d > 2`, dimensionless YM coupling, real SD/ASD
2-form split, Weyl chirality}; `μ₄` enters nowhere — axiom provenance from the compiler is the
registered open half); the **seam-gap compression** `SEAM.SIMPLECURRENT.GENERATOR.01` `[O]` (one
simple-current generator instead of 128 current controls); the **explicit finite 4D lattice
action** `TFPT4D.LATTICE.ACTION.01` `[O]` (Wilson + Ginsparg–Wilson + one relevant `Φ` sector +
seam/topological module, seven machine-checkable finite gates T1–T7); the **determinant-line
unification hypothesis** `SEAM.DETLINE.UNIFICATION.01` `[O]` (`Res_seam det D₄D ≅ det D_seam`
with connection — would unify seam extension, anomaly freedom, generation index and CP
orientation); and the **generating-functional contract** `FTRANSFER.GENERATING.01` `[O]` (all four
`F_transfer` bridges from one `W[J] = log Z[J]`; the `FR.TRANSFER.01` guard stays binding).
Everything constructive stays `[O]` with registered kill criteria; RH and `PRIME.*` remain
separate programmes (a green RH probe is neither necessary nor sufficient for the 4D physics).

**`SEAM.EQUIV.01` is closed modulo a cited theorem.** The explicit lattice model (`v367`/`v368`) and
the S3 closure stack pin the target at every computable level — central charge `c=8` (`v376`), the
`(E8)₁` character with 248 currents and one primary (`v377`), genus-one torus GSD = 1 (`v378`) and
reflection positivity (`v379`) — and it is Lean-formalised as `FORM.SEAM.MMST.01`: the collar's MMST
hypotheses are kernel-proved, the MMST scaling-limit and Adamo–Moriwaki–Tanimoto OS-reconstruction
theorems enter as named cited axioms, and the `#print axioms` check is clean. The *only* residual that
stays `[O]` is the abstract continuum existence of the scaling limit (exactly those two cited published
theorems, `v336`). The post-F **G-block** narrows that residual on six more fronts (`v454`–`v464`,
`v469`), re-founding the `128`-spinor extension on 1995–2001 peer-reviewed subfactor theory (the
Longo–Rehren locality integer `h_s = 16/16 = 1 ∈ ℤ`) and reducing the realisation axiom to invariants
(R1′: quasi-free `[C]` + gap `[E]` + class D + `c₋ = 8` `[E]`, computed FHS `|C| = 1`, `ν = 16`, the
Kitaev 16-fold-way class whose edge *is* the bosonic `(E8)₁` state). Across the whole G-block the
residual is now *entirely certification* — a named, hypothesis-audited package of published theorems with
no open internal mechanism — yet `SEAM.EQUIV.01` stays `[O]` because it still rests on cited
continuum-existence theorems we do not re-prove. `QGEO.SYM.01` is its **corollary** (`v335`, Lean
`FORM.QGEO.BW.01`). `QG.AMB.01` is gap-decoupled from the general Euclidean-QG conformal-factor problem
(margin `Δ_eff ≈ 1.648 > 0`, `v76`/`v330`).

---

## Historical reduction (how we got here)

<details>
<summary><b>The full reduction chain and the forward plan</b></summary>

- **One condition, not many** (`v234`/`v235`): the whole *structural* residual — the metric inclusion
  `G_net`, the carrier `P2` and red-team Target A — is a single condition, *"the seam carries no
  nontrivial abelian sector"*, with three provably-equivalent faces that all force `E8`: holomorphy
  (`μ`-index 1), a homology-sphere seam link (`Γ` perfect `⟺ 2I`, `v232`), and exactly one 1-dim irrep
  (`v219`) — all equal `#(mark-1) = |H₁| = 1`, true only for `E8`. In abelian Chern–Simons language it is
  the single integer step `holomorphic ⟺ det K = 1`; the extension tower `D₅⊕A₃ (16) → D₈ (4) → E₈ (1)`
  is anyon condensation, i.e. the Kitaev `E8` quantum-Hall state.
- **Gravity** (`v358`/`v359`, historical wording — see the conditional typing in the deep dive above
  and `GRAV.NONCIRCULAR.01`): the entanglement first law, *under the Jacobson entanglement-equilibrium
  hypotheses*, gives the covariant Einstein equation `G_ab + Λ g_ab = c₃⁻¹ T_ab` with **both**
  coefficients fixed, and the **thermodynamic** origin of `c₃` **coincides** with the **geometric**
  one via `|μ₄| = |Z₂|·χ(S²) = 4`. So `c₃` is **triply over-determined** (anchor, geometry,
  thermodynamics). Within the conditional route the residual is the equation-of-state interpretive
  fork and the one unit `v_geo`; the route's own 4D-QFT hypotheses are the larger open item.
- **The central theorem**: `1/(8π)` from the seam-determinant replica — structure closed, the
  Fursaev–Solodukhin factor machine-derived (`v90`), the mechanism exhibited at the gapped-model level
  (`v150`), the Calderón transfer answered (`v151`), the `q(A₃)` normalisation identified as the one
  dimensionful anchor in disguise (`v152`), and the whole chain exercised numerically on the discretized
  collar with the seam's own kernel and real replica sheets (`v471`).
- **Ambient QG measure** (`QG.AMB.01` / `G_metric`) — reframed as a **`[C]` redundancy** (`v369`).
- **Absolute amplitude normalisation** (`U_point`) — an anchor; the quark *ratios* are closed.
- **Frontier interfaces** (`m_p/m_e`, `η_B`, Koide, axion relic) — deliberately typed as interfaces,
  never quoted as compiler outputs.

**Forward plan v2 (2026-06-23) — all five tracks done.** Track 1 (`v367`/`v368` + S3 stack `v376`–`v379`):
an explicit gapped p+ip lattice model (numerical Chern `|C|=1`, `c_-=8`) pins the `(E8)₁` target at every
computable level; only the cited MMST continuum scaling limit stays external. Track 2 (`v369`): the ambient
QG measure is reframed as a **holographic redundancy**. Track 3 (`v371`–`v374`): the four `F_transfer`
interfaces promoted to typed runnable solvers. Track 4 (`v375`): a status-typed CI over the frozen
prediction registry with a live JUNO/NuFIT/ACT/BK18 scorecard. Plus `v380`: the KMS Entire Hessian — the
Stelle ghost is exactly a finite Seeley–DeWitt truncation.

A development timeline of all 472 modules is in [`introduction.tex`](../introduction.tex) (and on the
website verification page).

</details>
