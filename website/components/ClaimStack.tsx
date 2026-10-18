"use client";

import { motion } from "motion/react";
import Link from "next/link";
import { ArrowDown, ArrowRight } from "lucide-react";
import { SectionHeader } from "./SectionHeader";
import { cn } from "@/lib/utils";

/**
 * The Claim Stack — the single most important credibility graphic.
 *
 * It makes the [E]/[C]/[O] separation structural: a reader physically cannot
 * read a conditional claim as if it were exact, because the layers are
 * stacked, typed and colour+text coded. Each layer carries its status marker,
 * a one-line kill condition, and a link to where it is derived/verified.
 *
 * Every fact here mirrors content that already lives in the documents and the
 * ledger (no new claims are introduced); the scripts are reached through the
 * /verification dependency graph rather than re-listed here.
 */
interface Layer {
  key: string;
  marker: "[E]" | "[C]" | "[O]";
  kicker: string;
  title: string;
  items: string[];
  kill: string;
  link: { href: string; label: string };
  tone: string;
  markerTone: string;
}

const LAYERS: Layer[] = [
  {
    key: "inputs",
    marker: "[O]",
    kicker: "Declared inputs",
    title: "Two axioms — the only dials",
    items: [
      "c₃ = 1/(8π) — the seam constant",
      "g_car = 5 — the carrier rank",
      "Both reduce to the anchor a = (1,1,2) + π; nothing else is free",
      "Under the named glue architecture, three independent selectors force one boundary degree d = 4 — the two inputs reduce to d = 4 plus π, conditional (v624)",
    ],
    kill: "A fourth chiral generation (N_fam ≠ 3) or a different carrier rank breaks the compiler at the source.",
    link: { href: "/orientation", label: "How the two inputs close" },
    tone: "border-sky-400/30 bg-sky-500/[0.06]",
    markerTone: "bg-sky-500/15 text-sky-800 ring-sky-400/30",
  },
  {
    key: "exact",
    marker: "[E]",
    kicker: "Exact kernel",
    title: "E₈ glue, carrier traces, identities",
    items: [
      "D₅ ⊕ A₃ + μ₄ ⇒ E₈ — a Lie/lattice theorem",
      "Gauge group, 3 families, hypercharge — Lean-formalised",
      "Flavor operator ladder, det R = 8, θ_QCD = 0",
    ],
    kill: "Any failure of the E₈ glue identities or the Lean-checked carrier rigidity.",
    link: { href: "/verification", label: "Run the proofs in your browser" },
    tone: "border-emerald-400/30 bg-emerald-500/[0.06]",
    markerTone: "bg-emerald-500/15 text-emerald-800 ring-emerald-400/30",
  },
  {
    key: "numerical",
    marker: "[E]",
    kicker: "Numerical fixed points",
    title: "α⁻¹, sin²θ₁₂, sin²θ₁₃, β_rad",
    items: [
      "α⁻¹ = 137.0359992 — unique cubic root, 1.9σ from CODATA-2022",
      "sin²θ₁₂ = 1/3 − φ₀/2 = 0.3067 — frozen JUNO prediction",
      "β_rad = φ₀/(4π) = 0.2424° — within 0.4σ of ACT DR6",
      "sin²θ₁₃ = 0.0231 — the honest stress: ~2.0σ from current global fits, the largest single pull (named and tracked)",
    ],
    kill: "A unique-root failure for α, or JUNO landing clearly off 0.3067 at high significance.",
    link: { href: "/predictions", label: "The prediction surface" },
    tone: "border-teal-400/30 bg-teal-500/[0.06]",
    markerTone: "bg-teal-500/15 text-teal-800 ring-teal-400/30",
  },
  {
    key: "conditional",
    marker: "[C]",
    kicker: "Conditional physics",
    title: "Masses, inflation, cosmology transfer",
    items: [
      "Absolute masses via the declared QCD / EW scheme layer",
      "Starobinsky R²: n_s, r, A_s over the frozen N⋆ band",
      "η_B, axion relic — typed F_transfer downstream bridges",
    ],
    kill: "A robust r ≳ 0.01 kills the R² branch; a transfer that misses its target demotes that bridge — the kernel is untouched.",
    link: { href: "/papers/frontier", label: "The honest frontier" },
    tone: "border-amber-400/30 bg-amber-500/[0.06]",
    markerTone: "bg-amber-500/15 text-amber-800 ring-amber-400/30",
  },
  {
    key: "open",
    marker: "[O]",
    kicker: "Open interfaces",
    title: "v_geo · G_net · F_transfer · Rest_TOE",
    items: [
      "v_geo — one dimensionful scale anchor (metrology primitive) [O]",
      "G_net — metric-sector inclusion (algebra [E]; seam coupling [C] closed modulo cited theorems, v367/v368 + v376–v379, ground-state witnesses v489/v490; crossed-product certified extension (v469))",
      "F_transfer — typed runnable solver suite (v371–v375), each with a kill test [C]",
      "Rest_TOE / T1–T8 — named AND TFPT.TOE.COMPLETE.01 [O] (ten-component rest; not a closure)",
    ],
    kill: "Compiler scope: v_geo is the [O] unit while G_net and F_transfer are status-typed contracts. Strict scope: Round 4 (v1026–v1030) closes only the fixed-M=1, Ny=8 relaxed TEL-B norm below 2.995906 and adds narrow identities/counterbounds. FE-GEN/ALG-EXH, every T1–T8 gate and TFPT.TOE.COMPLETE.01 remain [O], with no shared 3+1D parent; v1029 is not a TFPT embedding.",
    link: { href: "/verification#open-gates", label: "The research contracts" },
    tone: "border-rose-400/30 bg-rose-500/[0.06]",
    markerTone: "bg-rose-500/15 text-rose-800 ring-rose-400/30",
  },
];

export function ClaimStack() {
  return (
    <section
      id="claim-stack"
      className="relative scroll-mt-20 py-14 sm:py-16"
      aria-labelledby="claim-stack-heading"
    >
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <SectionHeader
          id="claim-stack-heading"
          eyebrow="The claim stack"
          title="One stack, five honestly-typed layers"
          description="Read top to bottom: declared inputs → exact kernel → numerical fixed points → conditional physics → open interfaces. Each layer states its marker and how it fails."
        />

        <ol className="mt-8 flex flex-col gap-2" aria-label="The TFPT claim stack, from declared inputs to open interfaces">
          {LAYERS.map((layer, i) => (
            <li key={layer.key}>
              <motion.article
                initial={{ opacity: 0, y: 12 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, amount: 0.1 }}
                transition={{ duration: 0.4, delay: i * 0.04 }}
                className={cn(
                  "border p-4 sm:p-5",
                  layer.tone,
                )}
              >
                <div className="flex flex-wrap items-center gap-2">
                  <span
                    className={cn(
                      "rounded-full px-2 py-0.5 font-mono text-[11px] font-semibold ring-1",
                      layer.markerTone,
                    )}
                  >
                    {layer.marker}
                  </span>
                  <span className="text-[10px] font-semibold uppercase tracking-widest text-slate-600">
                    {layer.kicker}
                  </span>
                </div>

                <div className="mt-2 grid gap-4 md:grid-cols-[minmax(0,1fr)_minmax(0,1.05fr)]">
                  <div>
                    <h3 className="font-serif text-lg font-semibold text-slate-950">
                      {layer.title}
                    </h3>
                    <ul className="mt-2 space-y-1.5">
                      {layer.items.map((it) => (
                        <li
                          key={it}
                          className="flex gap-2 text-sm leading-relaxed text-slate-700"
                        >
                          <span aria-hidden className="mt-2 h-1 w-1 flex-none rounded-full bg-slate-500" />
                          {it}
                        </li>
                      ))}
                    </ul>
                  </div>

                  <div className="flex flex-col justify-between gap-3 rounded-xl border border-slate-300/40 bg-slate-50/40 p-4">
                    <div>
                      <div className="text-[10px] font-semibold uppercase tracking-widest text-rose-700/80">
                        How it fails
                      </div>
                      <p className="mt-1 text-xs leading-relaxed text-slate-700">
                        {layer.kill}
                      </p>
                    </div>
                    <Link
                      prefetch={false}
                      href={layer.link.href}
                      className="inline-flex w-fit items-center gap-1.5 text-xs font-semibold text-blue-700 transition-colors hover:text-blue-800"
                    >
                      {layer.link.label}
                      <ArrowRight size={13} aria-hidden />
                    </Link>
                  </div>
                </div>
              </motion.article>

              {i < LAYERS.length - 1 && (
                <div className="flex justify-center py-1" aria-hidden>
                  <ArrowDown size={16} className="text-slate-500" />
                </div>
              )}
            </li>
          ))}
        </ol>
      </div>
    </section>
  );
}
