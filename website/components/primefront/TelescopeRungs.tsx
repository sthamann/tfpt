"use client";

import { motion } from "motion/react";

/**
 * T124 MULTILEVEL.TELESCOPE. The nested level chain D_0 > D_1 > … > D_L is one
 * window form on nested spaces (nesting exact to 2.4e-14), and the rung
 * contributions telescope: Σ δ_l = ε_0 − ε_L (9.2e-10).
 *
 * The drawn chain is ONE admissible chain, built from the measured median
 * falloff 0.316 and the L = 5 ceiling 0.9911 — schematic. The quoted ranges
 * are the probe's numbers.
 */
const RUNG_SHARES = [0.68, 0.215, 0.068, 0.0215, 0.0068] as const;
const REMAINDER = 1 - RUNG_SHARES.reduce((s, r) => s + r, 0);

const LEVELS = 5;
const FRAME_W = 300;
const FRAME_H = 92;

export function TelescopeRungs() {
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-emerald-700/90">
          The level telescope · T124
        </p>
        <span className="font-mono text-[10px] text-slate-600">
          Σ δ_l = ε₀ − ε_L
        </span>
      </div>

      {/* nested spaces: the two-level system is literally one rung */}
      <svg
        viewBox={`0 0 ${FRAME_W} ${FRAME_H}`}
        className="w-full"
        role="img"
        aria-label="Nested level spaces: the coarsest window form sits exactly inside the next finer one, five times over. The two-level system of the previous part is one rung of this ladder."
      >
        {Array.from({ length: LEVELS + 1 }, (_, l) => {
          const inset = l * 7;
          return (
            <motion.rect
              key={l}
              x={10 + inset}
              y={8 + inset * 0.75}
              width={FRAME_W - 20 - inset * 2}
              height={FRAME_H - 30 - inset * 1.5}
              rx={4}
              fill="none"
              stroke={
                l === LEVELS
                  ? "rgba(110,231,183,0.85)"
                  : `rgba(56,189,248,${0.28 + l * 0.07})`
              }
              strokeWidth={l === LEVELS ? 1.6 : 1}
              initial={{ opacity: 0 }}
              whileInView={{ opacity: 1 }}
              viewport={{ once: true, amount: 0.4 }}
              transition={{ duration: 0.3, delay: l * 0.09 }}
            />
          );
        })}
        <text
          x={16}
          y={FRAME_H - 6}
          fontSize="8"
          className="fill-slate-600 font-mono"
        >
          D₀ (coarsest) → D₅ (finest) · nesting exact to 2.4e-14
        </text>
      </svg>

      {/* rung contributions: they telescope to the whole quantity */}
      <p className="mt-3 font-mono text-[10px] uppercase tracking-wider text-slate-600">
        Share of ε₀ carried per rung
      </p>
      <div className="mt-1.5 flex h-3 w-full overflow-hidden rounded-full bg-slate-200/70">
        {RUNG_SHARES.map((share, i) => (
          <motion.div
            key={i}
            className="h-full"
            style={{
              backgroundColor: `rgba(16,185,129,${0.75 - i * 0.11})`,
            }}
            initial={{ width: 0 }}
            whileInView={{ width: `${share * 100}%` }}
            viewport={{ once: true, amount: 0.5 }}
            transition={{ duration: 0.5, delay: 0.5 + i * 0.12, ease: "easeOut" }}
          />
        ))}
        <motion.div
          className="h-full bg-slate-400/60"
          initial={{ width: 0 }}
          whileInView={{ width: `${REMAINDER * 100}%` }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.4, delay: 1.2, ease: "easeOut" }}
        />
      </div>
      <div className="mt-1 flex justify-between font-mono text-[10px] text-slate-600">
        <span>δ₀ · top rung</span>
        <span>δ₄</span>
        <span className="text-slate-500">ε_L</span>
      </div>

      <dl className="mt-4 grid grid-cols-2 gap-2 text-center">
        <Stat
          term="400/400"
          desc="rungs where the certified bound (8R) holds"
        />
        <Stat term="0.27–0.88" desc="share of ε₀ on the top rung" />
        <Stat term="α^−0.080" desc="drift — 7× weaker than T123's" />
        <Stat term="+0.444" desc="of the α^0.5 gap recovered" />
      </dl>

      <p className="mt-3 text-xs leading-relaxed text-slate-600">
        The rung is a <em>maximum</em>, not a minimum, so it needs the form from
        above — exactly where the certified envelope works. Consecutive rungs
        fall by a measured median factor 0.316; at five levels the additive chain
        can reach 0.9911–0.9987 of the whole. The drawn chain is one admissible
        chain built from those two numbers — schematic; the ranges are measured.
        Sandbox; not RH evidence.
      </p>
    </div>
  );
}

function Stat({ term, desc }: { term: string; desc: string }) {
  return (
    <div className="rounded-xl border border-emerald-400/25 bg-emerald-500/[0.07] px-2 py-2">
      <dt className="font-mono text-sm leading-none text-emerald-800">
        {term}
      </dt>
      <dd className="mt-1 text-[10px] leading-tight text-slate-600">{desc}</dd>
    </div>
  );
}
