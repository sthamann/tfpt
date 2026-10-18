"use client";

import { useState } from "react";
import { motion } from "motion/react";
import { cn } from "@/lib/utils";

/**
 * The two Gelfand points of the census algebra: the Eisenstein eigenvalue
 * σ₃(p) and the cuspidal eigenvalue a_p (Teil 29 anchors T₃, T₅; a₇ = 24 from
 * the frozen neighbour operator, Teil 31).
 */
const PRIMES = [
  { p: 3, sigma3: 28, ap: -4 },
  { p: 5, sigma3: 126, ap: -2 },
  { p: 7, sigma3: 344, ap: 24 },
] as const;

const LADDER_RUNGS = 9;
const RUNG_GAP = 18;

export function SpectrumLadder() {
  const [idx, setIdx] = useState(0);
  const sel = PRIMES[idx];

  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-4 flex flex-wrap items-center justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-slate-600">
          Gelfand spectrum · what is there vs what is needed
        </p>
        <div className="flex gap-1">
          {PRIMES.map((r, i) => (
            <button
              key={r.p}
              type="button"
              aria-pressed={i === idx}
              onClick={() => setIdx(i)}
              className={cn(
                "rounded-md px-2 py-0.5 font-mono text-[10px] transition",
                i === idx
                  ? "bg-slate-300 text-slate-900"
                  : "bg-slate-200/70 text-slate-600 hover:bg-slate-300/70",
              )}
            >
              p = {r.p}
            </button>
          ))}
        </div>
      </div>

      <div className="grid gap-3 sm:grid-cols-2">
        {/* measured: two points */}
        <div className="rounded-xl border border-sky-400/30 bg-sky-500/5 p-3">
          <p className="font-mono text-[10px] uppercase tracking-wider text-sky-700/90">
            In the suite · two points
          </p>
          <div className="relative mt-4 flex min-h-40 flex-col justify-around gap-4">
            <span
              aria-hidden
              className="absolute inset-y-0 left-6 w-px bg-slate-300/60"
            />
            <SpectrumPoint
              colour="bg-sky-400 border-sky-200/70"
              label="σ₃-system"
              value={sel.sigma3}
              detail="Eisenstein · 5 oldform copies"
            />
            <SpectrumPoint
              colour="bg-rose-400 border-rose-200/70"
              label="a_p-system"
              value={sel.ap}
              detail="cuspidal f₈ · 2 copies"
            />
          </div>
          <p className="mt-1 font-mono text-[10px] text-slate-600">
            dim V = 7 = 5 + 2 · commutative algebra
          </p>
        </div>

        {/* needed: infinitely many */}
        <div className="rounded-xl border border-violet-400/30 bg-violet-500/5 p-3">
          <p className="font-mono text-[10px] uppercase tracking-wider text-violet-700/90">
            Hilbert–Pólya needs · infinitely many
          </p>
          <div className="relative mt-4 h-40 overflow-hidden">
            <span
              aria-hidden
              className="absolute inset-y-0 left-6 w-px bg-slate-300/60"
            />
            <motion.div
              aria-hidden
              className="absolute inset-x-0 top-0"
              animate={{ y: [0, -RUNG_GAP] }}
              transition={{ duration: 2.4, repeat: Infinity, ease: "linear" }}
            >
              {Array.from({ length: LADDER_RUNGS + 2 }, (_, i) => (
                <div
                  key={i}
                  className="flex items-center gap-2"
                  style={{ height: RUNG_GAP }}
                >
                  <span className="ml-[1.3rem] h-1.5 w-1.5 rounded-full bg-violet-300/80" />
                  <span className="h-px flex-1 bg-violet-400/20" />
                </div>
              ))}
            </motion.div>
            <span
              aria-hidden
              className="absolute inset-x-0 top-0 h-10 bg-gradient-to-b from-slate-50 to-transparent"
            />
            <span
              aria-hidden
              className="absolute inset-x-0 bottom-0 h-10 bg-gradient-to-t from-slate-50 to-transparent"
            />
          </div>
          <p className="mt-1 font-mono text-[10px] text-slate-600">
            unbounded / non-commutative · no such operator in the suite
          </p>
        </div>
      </div>

      <p className="mt-3 text-xs leading-relaxed text-slate-600">
        Teil 40, verdict{" "}
        <span className="font-mono text-slate-700">TERRAIN-MAPPED</span>: the
        census operator algebra is commutative with exactly two Gelfand points
        (plus oldform copies). Cartography, not a proof attempt — the July 25
        reframe replaced the hunt for one infinite operator by a family plus a
        relative trace formula.
      </p>
    </div>
  );
}

function SpectrumPoint({
  colour,
  label,
  value,
  detail,
}: {
  colour: string;
  label: string;
  value: number;
  detail: string;
}) {
  return (
    <div className="relative flex items-center gap-3">
      <span
        className={cn(
          "ml-[1.15rem] h-3 w-3 shrink-0 rounded-full border",
          colour,
        )}
      />
      <div className="min-w-0">
        <p className="font-mono text-sm text-slate-900">
          {label} = {value}
        </p>
        <p className="font-mono text-[10px] leading-tight text-slate-600">
          {detail}
        </p>
      </div>
    </div>
  );
}
