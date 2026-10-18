"use client";

import { motion } from "motion/react";

/**
 * The reduction cascade T104 → T125: what the "one remaining object" was at each
 * stage. Part numbers and named objects are literal (experiments/next.txt);
 * the bar widths are schematic — they order the stages, they do not measure them.
 */
const STAGES = [
  {
    part: "T104",
    object: "one matrix inequality",
    detail:
      "A Loewner statement on the full window — 16 zones, every dimension.",
    width: 100,
  },
  {
    part: "T106",
    object: "half the dimensions",
    detail:
      "The parity split closes the even channel 16/16; only the odd channel is left.",
    width: 62,
  },
  {
    part: "T107",
    object: "one scalar ratio",
    detail: "r = κ/ε ≤ 1, measured r = 0.005…0.18 — two orders of room.",
    width: 40,
  },
  {
    part: "T108–T109",
    object: "one boundary value",
    detail:
      "ε becomes an exact identity (the last Cholesky pivot); what is left is one number of one explicit vector.",
    width: 26,
  },
  {
    part: "T115–T117",
    object: "one textbook inequality",
    detail:
      "The Szegő–Levinson prediction error, read as a Galerkin error — a classical address, not a new object.",
    width: 16,
  },
  {
    part: "T124",
    object: "a Harnack pair + one sign",
    detail:
      "Two window-certified statements, plus a sign the coarse-to-fine induction already carries.",
    width: 9,
  },
  {
    part: "T125",
    object: "one sign + one convention",
    detail:
      "Assembled on 52 zones: the load-bearing spine needs the sign on one finite matrix plus a declared accounting convention — the Harnack pair survives as a second, independent route.",
    width: 5,
  },
] as const;

export function ReductionCascade() {
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-4 flex flex-wrap items-center justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-sky-700/90">
          The reduction cascade · what is still missing, per stage
        </p>
        <span className="font-mono text-[10px] text-slate-600">
          T104 → T125
        </span>
      </div>

      <ol className="space-y-3">
        {STAGES.map((s, i) => (
          <li key={s.part}>
            <div className="flex flex-wrap items-baseline gap-x-2 gap-y-0.5">
              <span className="font-mono text-[11px] text-sky-800">
                {s.part}
              </span>
              <span className="text-sm font-medium text-slate-900">
                {s.object}
              </span>
            </div>
            <div className="mt-1.5 h-2 overflow-hidden rounded-full bg-slate-200/70">
              <motion.div
                className="h-full rounded-full bg-gradient-to-r from-sky-500/70 via-emerald-400/60 to-emerald-300/70"
                initial={{ width: 0 }}
                whileInView={{ width: `${s.width}%` }}
                viewport={{ once: true, amount: 0.4 }}
                transition={{ duration: 0.55, delay: i * 0.12, ease: "easeOut" }}
              />
            </div>
            <p className="mt-1 text-xs leading-relaxed text-slate-600">
              {s.detail}
            </p>
          </li>
        ))}
      </ol>

      <p className="mt-4 text-xs leading-relaxed text-slate-600">
        Each stage removed something and named what was left. The bar lengths are
        schematic — they show the order of the steps, not a measured size. Part
        numbers and objects are taken literally from the diary. Nothing here is
        a proof of the last step. Sandbox; not RH evidence.
      </p>
    </div>
  );
}
