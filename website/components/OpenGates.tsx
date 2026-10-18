"use client";

import { motion } from "motion/react";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { SectionHeader } from "./SectionHeader";
import { Math } from "./Math";
import { FTransferDynamics } from "./FTransferDynamics";

interface Gate {
  tag: string;
  marker: string;
  title: string;
  body: string;
  formula?: string;
  tone: string;
}

const GATES: Gate[] = [
  {
    tag: "Interface 1",
    marker: "[O]",
    title: "v_geo — the one scale anchor",
    body: "Quark ratios are closed (Readout Rigidity, c_u/c_d = 55/117); only the absolute scale v_geo remains. CLOSED METROLOGY STRUCTURE (R₊ unit torsor; one dimensionful calibration necessary by dimensional analysis — the No-Unit theorem v153/v725): the same unit as gravity's 1/G, over-determined to 0.11% by gravity vs dark energy (v274). A unit, not a gap; display stays [O], no physical [E]. The interface is structurally closed as an R₊ scale torsor in calibration form (v725: complete export table, dimension-matrix rank 1, all conditions λ-homogeneous; one external reference selects the point, everything else is prediction) — no scale derivation; the one remaining dimensionless ratio is named: H_EW = ln(M̄_Pl/v_EW) = 37.1776. Unit choice closed; dimensionless hierarchies (M_Pl/v_EW, M_R/M_scal, Λ_QCD/v_EW, T_reh/M_scal) remain predictive obligations.",
    formula: "\\det R = 8,\\ \\operatorname{Spec}(Q_+)=\\{1,2,3\\};\\ U_{\\mathrm{point}} \\to v_{\\mathrm{geo}}",
    tone: "border-amber-400/30 bg-amber-500/5",
  },
  {
    tag: "Interface 2",
    marker: "[E] target · [C] seam",
    title: "G_net — the metric-sector inclusion",
    body: "The (E₈)₁ target is closed [E] (v154/v175). The seam coupling SEAM.EQUIV.01 is closed modulo cited theorems: the lattice model (v367/v368) + the S3 stack pin it at every computable level (c = 8, the (E₈)₁ character, torus GSD = 1, RP; v376–v379, ground-state witnesses v489/v490), Lean-pinned (FORM.SEAM.MMST.01). Residual [O] = the cited MMST continuum-existence only (v336; extension leg on the peer-reviewed crossed-product package, realisation at invariant level, v469; stays [O]). First exact index/arithmetic witnesses (2026-08-03): the NS/R grading is the parity character of E8(Z[i])/(1+i) = F₂⁴ — the Ramond projection is (1+i)-adic (v722) — and the Pimsner–Popa/Watatani index is exactly 4 on the CAR ladder with μ₄ derived from the clock (v726); the Q-system identification stays the registered open half (GNET.RAMIFIED.01).",
    formula: "[\\,(E_8)_1 : (D_5)_1\\times(A_3)_1\\,] = 4 = |\\mu_4| \\Rightarrow \\text{holomorphic } c = 8",
    tone: "border-amber-400/30 bg-amber-500/5",
  },
  {
    tag: "Interface 3",
    marker: "[C]",
    title: "F_transfer — one typed runnable solver suite",
    body: "One typed, runnable solver suite — Koide (v371), η_B (v372), axion relic (v373), m_p/m_e (v374) — each with a kill test, folded into a prediction-observatory CI (v375). A guard (v187) keeps them [C] bridges, never compiler outputs. The external-clock typing is now confirmed from the inside: both thermal-time routes for internalizing the four clocks are machine-killed (v723 STT-KILLED, v724 T3B-DEAD) — the anchor census sharpens to {one unit (v_geo-class), one angle θᵢ, one lattice O(1) C_p} — and the frozen external-clock contract is now EXECUTED on its expected K1 kill (v777, NO-COMMON-CONNECTION: no common continuous clock exists; the fibered functor with the constant seam cocycle {0, ±Δ²/2} survives). The coset assignment of the fibered functor's clock fibers is now a theorem from KMS/modular typing (v792, KMS-COSET-THEOREM: S = −(ln λ)²/2 from the time-1 holonomy multiplier; blind protocol, exact unblinding). Honest residual (wave 3, FTRANSFER.SK.RHO0.01 [O]; mechanism executed wave 4, v1000): cosmological transfers need the pair (S, ρ₀), not W[J] alone — FTRANSFER.GENERATING.01 covers equilibrium correlators; KMS/FDT ~10⁻¹⁷, ρ₀-contrast 3.550×10⁻³ vs static 10⁻¹⁶; the typed candidate is θ_i = 3π/5 unique in the μ₄ lift [C] (no cosmological solve).",
    tone: "border-slate-500/30 bg-slate-500/5",
  },
];

const RESIDUAL: { label: string; marker: string; blurb: string; tone: string }[] = [
  {
    label: "v_geo",
    marker: "[O]",
    blurb: "Closed metrology structure (R₊ unit torsor; one dimensionful calibration necessary by dimensional analysis — No-Unit v153/v725), over-determined (gravity = dark energy = M̄_Pl to 0.11%, v274); the same unit as gravity's 1/G. Display stays [O], no physical [E].",
    tone: "from-amber-500/15 to-amber-500/[0.03] border-amber-400/30",
  },
  {
    label: "G_net",
    marker: "[E] target · [C] seam",
    blurb: "Metric inclusion: the (E₈)₁ target is closed and pinned at every computable level (lattice v367/v368 + S3 stack v376–v379, ground-state witnesses v489/v490); the seam coupling SEAM.EQUIV.01 now carries two named routes (route split 2026-07-22, no status change in substance): the MMST route SEAM.EQUIV.MMST.01 is closed modulo cited theorems (Lean FORM.SEAM.MMST.01), residual [O] = the cited MMST continuum existence only (v336; extension leg crossed-product certified, v469); the twistor route SEAM.EQUIV.TWISTOR.01 (Costello–Li construction, prepared by CELEST.SEAM.01) is [O]; the parent closes if either route closes and stays [O] as an unconditional claim.",
    tone: "from-amber-500/15 to-amber-500/[0.03] border-amber-400/30",
  },
  {
    label: "F_transfer",
    marker: "[C]",
    blurb: "One typed runnable solver suite (v371–v374) + a prediction-observatory CI (v375), each with a kill test — bridges, never primitive outputs.",
    tone: "from-slate-500/15 to-slate-500/[0.03] border-slate-500/30",
  },
];

/** The three provably-equivalent faces of the single structural condition (v234). */
const FACES: { face: string; statement: string }[] = [
  { face: "AQFT", statement: "boundary net holomorphic (μ-index 1)" },
  { face: "Geometry", statement: "seam link a homology 3-sphere (Γ perfect ⟺ 2I)" },
  { face: "Rep theory", statement: "exactly one 1-dim irrep (no abelian charge)" },
];

function ResidualTreemap() {
  return (
    <figure
      className="mt-8 rounded-2xl border border-slate-300/40 bg-slate-50/30 p-4 sm:p-5"
      aria-label="The complete open residual: compiler Rest = v_geo ⊕ G_net ⊕ F_transfer, beside Rest_TOE"
    >
      <figcaption className="mb-3 text-center font-mono text-sm text-slate-700">
        Rest = <span className="text-amber-800">v_geo</span> ⊕{" "}
        <span className="text-amber-800">G_net</span> ⊕{" "}
        <span className="text-slate-800">F_transfer</span>
        <span className="block mt-1 text-[11px] font-sans text-slate-600">
          compiler rest · beside it Rest_TOE (ten named [O] contracts / eight TFPT.TOE.COMPLETE.01 gates; nothing claimed closed)
        </span>
      </figcaption>
      <div className="grid gap-3 sm:grid-cols-3">
        {RESIDUAL.map((r) => (
          <div
            key={r.label}
            className={`flex flex-col gap-2 rounded-xl border bg-gradient-to-br p-4 ${r.tone}`}
          >
            <div className="flex items-center justify-between gap-2">
              <span className="font-mono text-base font-semibold text-slate-950">
                {r.label}
              </span>
              <span className="rounded-full bg-slate-100/60 px-2 py-0.5 font-mono text-[10px] font-semibold text-slate-700 ring-1 ring-slate-400/40">
                {r.marker}
              </span>
            </div>
            <p className="text-xs leading-relaxed text-slate-700">{r.blurb}</p>
          </div>
        ))}
      </div>
    </figure>
  );
}

/**
 * The historical finite seam/compiler closing condition (v234/v235) has three
 * provably-equivalent faces, all forcing E₈. This is not the strict physical TOE
 * residual: T1–T8 remain separate [O] gates. The sprint-by-sprint reduction
 * history lives on /changelog and in the research contracts.
 */
function ClosingCondition() {
  return (
    <figure className="mt-8 rounded-2xl border border-emerald-400/25 bg-emerald-500/[0.04] p-5 sm:p-6">
      <figcaption className="text-sm font-semibold text-emerald-800">
        The historical finite seam/compiler residual is{" "}
        <span className="underline decoration-emerald-400/40 underline-offset-4">
          one condition
        </span>{" "}
        — the seam carries no nontrivial abelian sector
      </figcaption>
      <p className="mt-2 text-sm leading-relaxed text-slate-700">
        The metric inclusion (G_net), the carrier P2 and red-team Target A are not
        three gates but three faces of a single condition — and all three force E₈:
      </p>
      <div className="mt-4 grid gap-3 sm:grid-cols-3">
        {FACES.map((f) => (
          <div
            key={f.face}
            className="rounded-xl border border-slate-300/40 bg-slate-50/40 p-3"
          >
            <div className="font-mono text-[11px] font-semibold uppercase tracking-wider text-emerald-700/80">
              {f.face}
            </div>
            <div className="mt-1 text-xs leading-relaxed text-slate-700">
              {f.statement}
            </div>
          </div>
        ))}
      </div>
      <div className="mt-4 overflow-x-auto rounded-lg border border-slate-300/40 bg-slate-50/50 p-2.5">
        <Math
          block
          plain="The seam has exactly one one-dimensional representation (a trivial abelianisation, a homology-sphere link) if and only if it is E₈ — equivalently, the K-matrix has determinant one."
        >
          {"\\#(\\text{1-dim irreps}) = |\\Gamma^{\\mathrm{ab}}| = |H_1(S^3/\\Gamma)| = 1 \\iff E_8 \\iff |\\det K| = 1"}
        </Math>
      </div>
      <p className="mt-4 text-sm leading-relaxed text-slate-700">
        <span className="font-semibold text-emerald-800">In short.</span> Within the historical finite
        boundary-net/MMST lane, the Modular Spectral Closure (v258–v261) reduces the listed Dirac,
        cutoff, gauging and glue data to this one premise, so{" "}
        <span className="font-mono text-emerald-800">SEAM.EQUIV.01</span> is{" "}
        <span className="text-emerald-800">closed modulo cited theorems</span>: the explicit lattice model
        (v367/v368) and the S3 stack (v376–v379, ground-state witnesses v489/v490) pin the target at every computable level, Lean-pinned
        (FORM.SEAM.MMST.01) to the published MMST/Adamo theorems — the only residual{" "}
        <span className="text-amber-800">[O]</span> is their abstract continuum-existence (v336; its 128-spinor
        extension leg is certified at net level by the peer-reviewed crossed-product package v469, LR/Böckenhauer/KLM,
        with AGT/AMT an independent second witness; stays [O]). The ambient
        measure QG.AMB.01 is a <span className="text-amber-800">[C] redundancy</span> (v369/v379) — a
        certification object, not missing dynamics — and perturbative spin-2 graviton unitarity is
        established (the Stelle ghost is a truncation artefact, v304/v370/v380).
      </p>
      <details className="group mt-3 rounded-lg border border-slate-300/40 bg-slate-50/40">
        <summary className="cursor-pointer list-none px-3 py-2 text-xs font-semibold text-slate-800 transition-colors hover:text-slate-950 [&::-webkit-details-marker]:hidden">
          <span className="text-blue-700 group-open:hidden">＋ </span>
          <span className="hidden text-blue-700 group-open:inline">－ </span>
          The full argument (Modular Spectral Closure · the QG-decoupling theorem · the 4D-QFT fork)
        </summary>
        <div className="space-y-2 px-3 pb-3 text-xs leading-relaxed text-slate-600">
          <p>
            <span className="font-semibold text-slate-700">Modular Spectral Closure (v258–v261).</span> The
            finite Dirac is a covariance induction of the seam KMS state, the spectral-action cutoff <em>is</em>{" "}
            that KMS weight (f₂/f₀ = 1), and seam, carrier-16 and E₈ live on one Kummer/K3 surface — so Dirac,
            cutoff, gauging, glue and orientability are readouts of one seam state. QGEO.SYM.01 is then a
            corollary (a conformal net&apos;s vacuum is rotation-invariant by axiom, v335).
          </p>
          <p>
            <span className="font-semibold text-slate-700">Seam keystone.</span> The keystone&apos;s residual is
            a composition of standard cited theorems (OS/clustering, the Kitaev free-fermion classification,
            the AQFT stack) over established TFPT facts — Lean-pinned to those named steps plus the derived gap
            Δ = 6·ln(3/2) ≈ 2.43 &gt; 0, with no further finite MMST/compiler assumption in that lane.
            The strict physical TOE obligations remain separate. Its two heavy legs are
            literature-anchored (v336): the MMST continuum scaling limit and the Adamo–Moriwaki–Tanimoto OS
            reconstruction, with (E₈)₁ inside their range (c=8, rank 8, 16 Majoranas) — and the 128-spinor
            extension leg is now certified at net level by the peer-reviewed crossed-product package (v469,
            LR/Böckenhauer/KLM), with the AGT/AMT route demoted to an independent second witness; stays [O].
          </p>
          <p>
            <span className="font-semibold text-slate-700">QG decoupling is a theorem (v337).</span> Every
            readout factors through the gapped admissible spectrum (χ = 729/665, margin 1.648 &gt; 0), so TFPT
            provably does not need the ambient measure.
          </p>
          <p>
            <span className="font-semibold text-slate-700">4D-QFT fork (v265).</span> Finite boundary-net/MMST
            lane — closed modulo cited theorems; ambient QG — discharged as redundancy [C]; 4D GUT — not claimed (E₈ is the
            audit hull, not a 4D gauge group); optional UV branch — carrier-native Pati–Salam, falsifiable by
            thresholds and proton decay. The sprint-by-sprint reduction (v234 → v302) is on the{" "}
            <Link prefetch={false} href="/changelog" className="text-blue-700 underline-offset-2 hover:underline">
              changelog
            </Link>
            .
          </p>
          <p>
            <span className="font-semibold text-amber-800">Strict TOE scope.</span> Round 4
            (v1026–v1030) closes the relaxed TEL-B norm at fixed M=1, Ny=8:
            ||R_N||HS &lt; 2.995906 &lt; 3 for every even N≥16. Native v1026 uses
            v1022/v1025 to discharge the former CF/DG estimates for this bound; the
            other modules add only narrow T3/T4/T6–T8 identities and counterbounds.
            FE-GEN/ALG-EXH, every T1–T8 gate and TFPT.TOE.COMPLETE.01 remain [O],
            and a shared 3+1D parent is still absent. The v1029 tensor target requires
            global zero-mode removal and is not a TFPT embedding.
            Round 7 (v1031–v1035) quantizes this free target and constructs a
            positive local covariant curvature field with helicities ±2. It also
            gives auxiliary flux-register charged corners, the factorized onsite
            mirror bound 1+√3/2, and linear Ward propagation for prescribed sources.
            The quarter twist has h=1/4, not hλ=1; the mirror bound is not an
            interacting hopping theorem; universal quantum coupling remains open.
          </p>
        </div>
      </details>
    </figure>
  );
}

/**
 * Trust section: what is still open. The historical finite seam/compiler residual
 * has one structural condition (no abelian sector ⟹ E₈), plus the scale and typed
 * transfer interfaces. Rest_TOE and T1–T8 remain a separate open matrix.
 */
export function OpenGates() {
  return (
    <section
      id="open-gates"
      className="relative scroll-mt-20 py-20 sm:py-24"
      aria-labelledby="open-gates-heading"
    >
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <SectionHeader
          eyebrow="Honest boundaries"
          title="What is still open?"
          description="After the compiler closure the live compiler residual is Rest = v_geo ⊕ G_net ⊕ F_transfer. Beside it sits the strict-physical-TOE accounting Rest_TOE: every T1–T8 gate and TFPT.TOE.COMPLETE.01 remains [O], and the shared 3+1D parent is absent. The one-condition/E₈ reduction applies only to the historical finite seam/compiler and boundary-net/MMST lane. Round 4 (v1026–v1030) closes the fixed-M=1, Ny=8 relaxed TEL-B norm below 2.995906 and adds narrow T3/T4/T6–T8 results; FE-GEN/ALG-EXH and all full gates stay open. Round 7 (v1031–v1035) quantizes the zero-mean target and constructs a free covariant helicity-±2 curvature field, auxiliary charged corners, a factorized mirror bound and prescribed-source Ward propagation. This is not a microscopic TFPT embedding or universal nonlinear coupling."
        />

        <ClosingCondition />

        <ResidualTreemap />

        <div className="mt-10 grid gap-5 lg:grid-cols-3">
          {GATES.map((g, i) => (
            <motion.article
              key={g.title}
              initial={{ opacity: 0, y: 16 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.05 }}
              transition={{ duration: 0.55, delay: i * 0.08 }}
              className={`flex flex-col rounded-2xl border p-6 ${g.tone}`}
            >
              <div className="flex items-center gap-2">
                <span className="rounded-full border border-slate-400/40 bg-slate-100/50 px-2.5 py-0.5 text-[10px] font-semibold uppercase tracking-widest text-slate-700">
                  {g.tag}
                </span>
                <span className="rounded-full bg-rose-500/15 px-2 py-0.5 font-mono text-[10px] font-semibold text-rose-800 ring-1 ring-rose-400/30">
                  {g.marker}
                </span>
              </div>
              <h3 className="mt-3 font-serif text-base font-semibold text-slate-950">
                {g.title}
              </h3>
              <p className="mt-2 flex-1 text-sm leading-relaxed text-slate-700">
                {g.body}
              </p>
              {g.formula && (
                <div className="mt-3 overflow-x-auto rounded-lg border border-slate-300/40 bg-slate-50/40 p-2.5">
                  <Math block>{g.formula}</Math>
                </div>
              )}
            </motion.article>
          ))}
        </div>

        <FTransferDynamics />

        <div className="mt-6 flex flex-wrap items-center gap-3 text-sm text-slate-600">
          <span>The gates are written up as numbered research contracts.</span>
          <Link
            prefetch={false}
            href="/papers/research-contracts"
            className="inline-flex items-center gap-1.5 font-semibold text-blue-700 transition-colors hover:text-blue-800"
          >
            Read the contracts
            <ArrowRight size={14} aria-hidden />
          </Link>
        </div>
      </div>
    </section>
  );
}
