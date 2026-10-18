"use client";

import { motion } from "motion/react";
import { cn } from "@/lib/utils";

const TOTAL_DIRECTIONS = 24;
const COVERED_DIRECTIONS = 5;
const HYBRID_DIRECTIONS = 19;

/** Residues mod 8. Twisting absorbs the sign class n ≡ 0,1 (mod 4). */
const RESIDUES = [0, 1, 2, 3, 4, 5, 6, 7] as const;
const ABSORBED = new Set([0, 1, 4, 5]);
const GAP_RESIDUE = 6;

export function ConeCoverage() {
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-sky-700/90">
          Cone coverage · Teil 72 · v540
        </p>
        <span className="font-mono text-[10px] text-slate-600">
          saturates at {COVERED_DIRECTIONS}/{TOTAL_DIRECTIONS}
        </span>
      </div>

      <div className="flex flex-wrap gap-1" aria-hidden>
        {Array.from({ length: TOTAL_DIRECTIONS }, (_, i) => {
          const covered = i < COVERED_DIRECTIONS;
          return (
            <motion.span
              key={i}
              initial={{ opacity: 0, y: 4 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.5 }}
              transition={{ duration: 0.25, delay: i * 0.02 }}
              className={cn(
                "h-6 w-6 rounded-md border",
                covered
                  ? "border-emerald-300/60 bg-emerald-500/30"
                  : "border-slate-300/60 bg-slate-200/60",
              )}
            />
          );
        })}
      </div>
      <p className="mt-2 text-xs leading-relaxed text-slate-600">
        <span className="text-emerald-800">{COVERED_DIRECTIONS} tiles</span> =
        the Weil test directions the guaranteed FE-self-dual cone reaches;{" "}
        <span className="text-slate-700">
          {TOTAL_DIRECTIONS - COVERED_DIRECTIONS} remain
        </span>{" "}
        — for {HYBRID_DIRECTIONS} of the nontrivial ones an explicit
        per-direction hybrid cone exists (T73). The tiles are a count, not an
        ordering.
      </p>

      <div className="mt-4 rounded-xl border border-slate-300/40 bg-slate-100/50 p-3">
        <p className="font-mono text-[10px] uppercase tracking-wider text-slate-600">
          Atoms by residue n mod 8
        </p>
        <div className="mt-2 flex flex-wrap gap-1.5">
          {RESIDUES.map((r) => {
            const isGap = r === GAP_RESIDUE;
            const absorbed = ABSORBED.has(r);
            return (
              <div
                key={r}
                className={cn(
                  "flex h-11 w-11 flex-col items-center justify-center rounded-lg border font-mono",
                  isGap
                    ? "border-amber-300/60 bg-amber-500/20 text-amber-800"
                    : absorbed
                      ? "border-sky-400/40 bg-sky-500/10 text-sky-800"
                      : "border-slate-300/60 bg-slate-200/50 text-slate-600",
                )}
              >
                <span className="text-sm leading-none">{r}</span>
                {isGap && (
                  <span className="mt-0.5 text-[8px] uppercase tracking-wider">
                    λ*
                  </span>
                )}
              </div>
            );
          })}
        </div>
        <ul className="mt-2 space-y-1 font-mono text-[10px] text-slate-600">
          <li>
            <span className="text-sky-700">sky</span> — sign class n ≡ 0,1 mod 4:
            absorbed by twisting (gap −26% mean, −90% max)
          </li>
          <li>
            <span className="text-amber-800">amber</span> — n ≡ 6 mod 8: the
            entire residual distance to the Weil cone, the FE-covariant gap
            functional λ*
          </li>
        </ul>
      </div>

      <p className="mt-3 text-xs leading-relaxed text-slate-600">
        The pin h(0) &gt; 0 blocks every Weil element against every twist, and
        Farkas/LP certificates show no finite signed theta library erases λ*.
        Fence: this is Euler-region positivity (edge L-values), not a
        central-line statement. Not RH evidence.
      </p>
    </div>
  );
}
