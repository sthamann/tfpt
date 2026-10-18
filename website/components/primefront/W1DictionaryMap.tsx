"use client";

import { motion, useReducedMotion } from "motion/react";

/**
 * The W1 dictionary: the three layers on which the TFPT window form and
 * Suzuki's screw-function Galerkin matrix are the same object
 * (v630/v631, transported v641, matrix-level v642, theorem-level v643
 * with the same-day convention erratum: eq. (1.3) carries Lerch +1/4,
 * the dictionary is the single scalar +1/D), plus the honest
 * implication map W1 -> W4.
 */

const ROWS = [
  {
    tfpt: "Atom table",
    tfptSub: "positions log n · weights Λ(n)/√n (v563)",
    suzuki: "Prime measure of the screw function",
    suzukiSub: "second derivative of the Λ-term (eq. 1.3)",
    arrow: "literal — identical, atom by atom",
    detail: "one scalar +1/D · 40 atoms (v630, corrected v643)",
    tone: "emerald" as const,
  },
  {
    tfpt: "Archimedean density",
    tfptSub: "e^{−t/2}/(1−e^{−2t}) — the Weil 1952 kernel",
    suzuki: "Smooth layer g″ = +ρ, pole subtracted",
    suzukiSub: "Lerch block (+1/4) collapses to a geometric series",
    arrow: "one scalar: +1/D — derived, not fitted",
    detail:
      "A_arch = −g″_smooth exactly, κ = 0 (v643; the earlier −4D was the g̃-normalization — erratum, numbers transfer verbatim)",
    tone: "sky" as const,
  },
  {
    tfpt: "Rank-one pole term",
    tfptSub: "tracked separately since v591",
    suzuki: "Pole block −2cosh(t/2) inside g",
    suzukiSub: "the s = 0, 1 weights of the explicit formula",
    arrow: "same object, different bookkeeping",
    detail: "the v630 “mystery drift”, resolved (v631)",
    tone: "violet" as const,
  },
];

const TONES = {
  emerald: {
    border: "border-emerald-400/35",
    bg: "bg-emerald-500/[0.07]",
    text: "text-emerald-800",
    line: "stroke-emerald-700/70",
  },
  sky: {
    border: "border-sky-400/35",
    bg: "bg-sky-500/[0.07]",
    text: "text-sky-800",
    line: "stroke-sky-700/70",
  },
  violet: {
    border: "border-violet-400/35",
    bg: "bg-violet-500/[0.07]",
    text: "text-violet-800",
    line: "stroke-violet-700/70",
  },
} as const;

const CHAIN = [
  {
    id: "W1",
    label: "Identify the window form with Suzuki's operator",
    status: "theorem-closed (v643)",
    open: false,
  },
  {
    id: "W2",
    label: "Form density",
    status: "started, not closed (v644)",
    open: true,
  },
  {
    id: "W3",
    label: "Uniform positivity — the RH-hard step",
    status: "open (tool diagnosis v648)",
    open: true,
  },
  {
    id: "W4",
    label: "Continuum passage (classical given W2 + W3)",
    status: "conditional",
    open: true,
  },
];

export function W1DictionaryMap() {
  const reduce = useReducedMotion();
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-4 flex items-baseline justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-sky-700/90">
          The W1 dictionary · TFPT ↔ Suzuki
        </p>
        <span className="font-mono text-[10px] text-slate-600">
          v630 · v631 · v640–v643
        </span>
      </div>

      <div className="space-y-3">
        {ROWS.map((r, i) => {
          const t = TONES[r.tone];
          return (
            <motion.div
              key={r.tfpt}
              initial={reduce ? false : { opacity: 0, y: 10 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.4 }}
              transition={{ duration: 0.45, delay: i * 0.12 }}
              className="grid grid-cols-[1fr_auto_1fr] items-stretch gap-2"
            >
              <div
                className={`rounded-xl border ${t.border} ${t.bg} px-3 py-2.5`}
              >
                <p className={`text-xs font-medium ${t.text}`}>{r.tfpt}</p>
                <p className="mt-0.5 font-mono text-[10px] leading-snug text-slate-600">
                  {r.tfptSub}
                </p>
              </div>
              <div className="flex w-16 flex-col items-center justify-center sm:w-24">
                <svg
                  aria-hidden
                  viewBox="0 0 96 20"
                  className="h-4 w-full"
                  fill="none"
                >
                  <line
                    x1="4"
                    y1="10"
                    x2="84"
                    y2="10"
                    className={t.line}
                    strokeWidth="1.5"
                  />
                  <path
                    d="M80 5l8 5-8 5"
                    className={t.line}
                    strokeWidth="1.5"
                    strokeLinejoin="round"
                  />
                  <path
                    d="M12 5l-8 5 8 5"
                    className={t.line}
                    strokeWidth="1.5"
                    strokeLinejoin="round"
                  />
                </svg>
                <p
                  className={`mt-1 text-center font-mono text-[9px] leading-tight ${t.text}`}
                >
                  {r.arrow}
                </p>
              </div>
              <div
                className={`rounded-xl border ${t.border} ${t.bg} px-3 py-2.5`}
              >
                <p className={`text-xs font-medium ${t.text}`}>{r.suzuki}</p>
                <p className="mt-0.5 font-mono text-[10px] leading-snug text-slate-600">
                  {r.suzukiSub}
                </p>
              </div>
              <p className="col-span-3 -mt-1 text-center font-mono text-[9px] text-slate-600">
                {r.detail}
              </p>
            </motion.div>
          );
        })}
      </div>

      <div className="mt-5 border-t border-slate-200/60 pt-4">
        <p className="font-mono text-[10px] uppercase tracking-widest text-slate-600">
          The honest implication map
        </p>
        <div className="mt-3 flex flex-wrap items-center gap-1.5">
          {CHAIN.map((c, i) => (
            <div key={c.id} className="flex items-center gap-1.5">
              <div
                className={`rounded-lg border px-2.5 py-1.5 ${
                  c.open
                    ? "border-amber-400/30 bg-amber-500/[0.06]"
                    : "border-emerald-400/40 bg-emerald-500/10"
                }`}
              >
                <p
                  className={`font-mono text-[11px] font-semibold ${
                    c.open ? "text-amber-800" : "text-emerald-700"
                  }`}
                >
                  {c.id}
                  <span className="ml-1.5 font-normal normal-case tracking-normal text-slate-600">
                    {c.status}
                  </span>
                </p>
                <p className="mt-0.5 max-w-[180px] text-[10px] leading-snug text-slate-600">
                  {c.label}
                </p>
              </div>
              {i < CHAIN.length - 1 && (
                <span aria-hidden className="font-mono text-slate-500">
                  →
                </span>
              )}
            </div>
          ))}
        </div>
        <p className="mt-3 text-xs leading-relaxed text-slate-600">
          Closing W1 does <strong className="text-slate-700">not</strong> move
          W3. The RH-hard step is untouched — stated in the contract, kept
          explicit here.
        </p>
      </div>
    </div>
  );
}
