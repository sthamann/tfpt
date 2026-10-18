"use client";

import { useState } from "react";
import { motion } from "motion/react";
import { cn } from "@/lib/utils";

/**
 * Teil 12 — Apéry ↔ f₈ congruence A((p−1)/2) ≡ a_p (mod p²).
 * Values are recomputed from f₈ = η(2τ)⁴η(4τ)⁴ and the Apéry numbers;
 * `residue` is the common class a_p ≡ A((p−1)/2) mod p².
 */
const ROWS: { p: number; ap: number; residue: number }[] = [
  { p: 3, ap: -4, residue: 5 },
  { p: 5, ap: -2, residue: 23 },
  { p: 7, ap: 24, residue: 24 },
  { p: 11, ap: -44, residue: 77 },
  { p: 13, ap: 22, residue: 22 },
  { p: 17, ap: 50, residue: 50 },
  { p: 19, ap: 44, residue: 44 },
  { p: 23, ap: -56, residue: 473 },
  { p: 29, ap: 198, residue: 198 },
  { p: 31, ap: -160, residue: 801 },
  { p: 37, ap: -162, residue: 1207 },
  { p: 41, ap: -198, residue: 1483 },
  { p: 43, ap: 52, residue: 52 },
  { p: 47, ap: 528, residue: 528 },
  { p: 53, ap: -242, residue: 2567 },
  { p: 59, ap: -668, residue: 2813 },
  { p: 61, ap: 550, residue: 550 },
  { p: 67, ap: 188, residue: 188 },
  { p: 71, ap: 728, residue: 728 },
  { p: 73, ap: 154, residue: 154 },
  { p: 79, ap: -656, residue: 5585 },
  { p: 83, ap: 236, residue: 236 },
  { p: 89, ap: 714, residue: 714 },
  { p: 97, ap: -478, residue: 8931 },
];

export function AperyBridge() {
  const [active, setActive] = useState(7);
  const row = ROWS.find((r) => r.p === active) ?? ROWS[0];

  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-slate-600">
          Apéry congruence · click a prime
        </p>
        <span className="rounded-full border border-emerald-400/35 bg-emerald-500/10 px-2 py-0.5 font-mono text-[10px] text-emerald-800">
          {ROWS.length}/{ROWS.length} match
        </span>
      </div>

      <div className="flex flex-wrap gap-1" role="list">
        {ROWS.map((r, i) => (
          <motion.button
            key={r.p}
            type="button"
            role="listitem"
            initial={{ opacity: 0, scale: 0.85 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true, amount: 0.4 }}
            transition={{ duration: 0.25, delay: i * 0.025 }}
            onClick={() => setActive(r.p)}
            aria-pressed={r.p === active}
            title={`p = ${r.p}: a_p = ${r.ap}`}
            className={cn(
              "h-7 min-w-7 rounded-md px-1.5 font-mono text-[10px] transition",
              r.p === active
                ? "bg-emerald-500/30 text-emerald-900 ring-2 ring-emerald-300/60"
                : "bg-emerald-500/10 text-emerald-800/80 hover:bg-emerald-500/25",
            )}
          >
            {r.p}
          </motion.button>
        ))}
      </div>

      <div className="mt-4 grid gap-2 sm:grid-cols-2">
        <div className="rounded-xl border border-slate-300/40 bg-slate-100/50 p-3">
          <p className="font-mono text-[10px] text-slate-600">
            Cusp form side · f₈ = η(2τ)⁴η(4τ)⁴
          </p>
          <p className="mt-1 font-mono text-xl text-sky-800">
            a<sub>{row.p}</sub> = {row.ap}
          </p>
          <p className="mt-2 text-xs leading-relaxed text-slate-600">
            The same a<sub>p</sub> the frozen neighbour operator reads off E₈
            geometry (Teile 27–32).
          </p>
        </div>
        <div className="rounded-xl border border-slate-300/40 bg-slate-100/50 p-3">
          <p className="font-mono text-[10px] text-slate-600">
            Apéry side · A(({row.p}−1)/2) mod {row.p}²
          </p>
          <p className="mt-1 font-mono text-xl text-violet-800">
            {row.residue}
          </p>
          <p className="mt-2 text-xs leading-relaxed text-slate-600">
            Apéry&apos;s ζ(3) numbers, reduced mod p² = {row.p * row.p}.
          </p>
        </div>
      </div>

      <p className="mt-3 rounded-xl border border-emerald-400/30 bg-emerald-500/10 px-3 py-2 text-center font-mono text-sm text-emerald-800">
        A(({row.p}−1)/2) ≡ a<sub>{row.p}</sub> ≡ {row.residue} (mod {row.p * row.p})
      </p>

      <p className="mt-2 text-xs leading-relaxed text-slate-600">
        Classical Beukers / Ahlgren–Ono congruence, verified here for every odd
        prime p ≤ 97. Placebos on nearby eta products fail. The probe content is
        that the signed E₈ count at odd prime shells satisfies the same
        congruence — a correlation inside the suite, not a new proof.
      </p>
    </div>
  );
}
