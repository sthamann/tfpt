"use client";

import { motion } from "motion/react";

/** Reflections of the infinite-dihedral ladder the value side is invariant under. */
const VALUE_REFLECTIONS = ["J₁", "J½", "J₁", "J½", "J₁", "…"] as const;

export function HeatFamilyBalance() {
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <p className="mb-3 font-mono text-[10px] uppercase tracking-widest text-sky-700/90">
        Three perspectives · Teile 82–84
      </p>

      {/* T82 — the arch term moves inside */}
      <div className="rounded-xl border border-slate-300/40 bg-slate-100/50 p-3">
        <p className="font-mono text-[10px] uppercase tracking-wider text-slate-600">
          T82 · the archimedean term was never external
        </p>

        <div className="mt-3 space-y-2">
          <TermRow
            caption="before — arch as an outside object"
            terms={[
              { label: "Q_cert", tone: "in" },
              { label: "Δ₂", tone: "in" },
              { label: "Δ_arch", tone: "out" },
            ]}
          />
          <div className="text-center font-mono text-[10px] text-slate-500">
            Legendre duplication · (2π)⁻ˢΓ(s) = ½Γ_R(s)Γ_R(s+1) · rel 6.6e-15
          </div>
          <TermRow
            caption="after — one heat family, arch inside"
            terms={[
              { label: "Q_cert", tone: "in" },
              { label: "Δ₂", tone: "in" },
              { label: "A_fam", tone: "in" },
              { label: "− A_shift", tone: "in" },
            ]}
          />
        </div>

        <p className="mt-3 rounded-lg border border-amber-400/35 bg-amber-500/10 px-3 py-2 text-center font-mono text-xs text-amber-800">
          Q_cert(h) + Δ₂(h) + A_fam(h) − A_shift(h) ≥ 0
        </p>
      </div>

      {/* T83 — FE-transversal */}
      <div className="mt-2 rounded-xl border border-slate-300/40 bg-slate-100/50 p-3">
        <p className="font-mono text-[10px] uppercase tracking-wider text-slate-600">
          T83 · the wall is FE-transversal, not FE-positional
        </p>
        <div className="mt-2 space-y-1.5">
          <div className="flex items-center gap-1.5">
            <span className="w-20 shrink-0 font-mono text-[10px] text-sky-700">
              value side
            </span>
            {VALUE_REFLECTIONS.map((r, i) => (
              <motion.span
                key={i}
                initial={{ opacity: 0 }}
                whileInView={{ opacity: 1 }}
                viewport={{ once: true, amount: 0.5 }}
                transition={{ duration: 0.2, delay: i * 0.08 }}
                className="rounded border border-sky-400/40 bg-sky-500/10 px-1.5 py-0.5 font-mono text-[10px] text-sky-800"
              >
                {r}
              </motion.span>
            ))}
          </div>
          <div className="flex items-center gap-1.5">
            <span className="w-20 shrink-0 font-mono text-[10px] text-rose-700">
              spectral cone
            </span>
            <span className="rounded border border-rose-400/40 bg-rose-500/10 px-1.5 py-0.5 font-mono text-[10px] text-rose-800">
              J₁
            </span>
            <span className="font-mono text-[10px] text-slate-500">
              — its own reflection only
            </span>
          </div>
        </div>
        <p className="mt-2 text-xs leading-relaxed text-slate-600">
          The product of the two FE reflections J₁∘J½ = e<sup>±u</sup> is the
          unit-line shift — the centre delta is literally the transport
          operator. Explicit-formula null test ≤ 2e-12.
        </p>
      </div>

      {/* T84 — the Z[i] home */}
      <div className="mt-2 rounded-xl border border-slate-300/40 bg-slate-100/50 p-3">
        <p className="font-mono text-[10px] uppercase tracking-wider text-slate-600">
          T84 · the last class is the compiler&apos;s home
        </p>
        <div className="mt-2 flex flex-wrap items-center gap-2 font-mono text-[10px]">
          <span className="rounded-md border border-violet-400/40 bg-violet-500/10 px-2 py-1 text-violet-800">
            coherent class = primitive ℤ[i]-norms
          </span>
          <span className="text-slate-500">→</span>
          <span className="rounded-md border border-slate-400/60 bg-slate-200/60 px-2 py-1 text-slate-700">
            Mertens divergence
          </span>
          <span className="text-slate-500">→</span>
          <span className="rounded-md border border-emerald-400/40 bg-emerald-500/10 px-2 py-1 text-emerald-800">
            L(1, λ) convergence
          </span>
        </div>
        <div className="mt-2 flex items-center gap-2 font-mono text-[10px] text-slate-600">
          <span>frontier</span>
          <span className="rounded bg-slate-200/70 px-1.5 py-0.5 text-slate-700">
            ~10²³
          </span>
          <motion.span
            aria-hidden
            initial={{ width: 0 }}
            whileInView={{ width: "3rem" }}
            viewport={{ once: true, amount: 0.5 }}
            transition={{ duration: 0.6 }}
            className="h-px bg-gradient-to-r from-slate-400 to-emerald-300/70"
          />
          <span className="rounded bg-emerald-500/15 px-1.5 py-0.5 text-emerald-800">
            ~10<sup>5.9·10¹²</sup>
          </span>
        </div>
      </div>

      <p className="mt-3 text-xs leading-relaxed text-slate-600">
        Type change ≠ proof; I5 remains ⟺ RH. T85/T86 close the coherent and
        non-coherent classes in provably-shaped form; the core checks are
        promoted as v541. Not RH evidence.
      </p>
    </div>
  );
}

function TermRow({
  caption,
  terms,
}: {
  caption: string;
  terms: { label: string; tone: "in" | "out" }[];
}) {
  return (
    <div>
      <p className="font-mono text-[9px] uppercase tracking-wider text-slate-500">
        {caption}
      </p>
      <div className="mt-1 flex flex-wrap items-center gap-1.5 rounded-lg border border-slate-300/40 bg-slate-50/50 p-2">
        {terms.map((t, i) => (
          <motion.span
            key={t.label}
            initial={{ opacity: 0, y: t.tone === "out" ? -6 : 4 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, amount: 0.5 }}
            transition={{ duration: 0.3, delay: i * 0.08 }}
            className={
              t.tone === "in"
                ? "rounded-md border border-sky-400/40 bg-sky-500/10 px-2 py-1 font-mono text-[11px] text-sky-800"
                : "rounded-md border border-dashed border-slate-500/60 bg-slate-200/50 px-2 py-1 font-mono text-[11px] text-slate-600"
            }
          >
            {t.label}
          </motion.span>
        ))}
      </div>
    </div>
  );
}
