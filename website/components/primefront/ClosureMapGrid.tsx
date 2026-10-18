"use client";

import { motion } from "motion/react";

const ZONES = 16;
const FRACTIONS = 4;

const CELL = 16;
const GAP = 3;
const PAD_L = 22;
const PAD_T = 12;
const VIEW_W = PAD_L + ZONES * (CELL + GAP) - GAP + 4;
const VIEW_H = PAD_T + FRACTIONS * (CELL + GAP) - GAP + 18;

/**
 * T101 instrument: 7/64 closed — zone 2 closes throughout (the only zone that
 * does); the placement of the remaining 3 cells is schematic, the count exact.
 */
const OLD_CLOSED = new Set([
  "2-0",
  "2-1",
  "2-2",
  "2-3",
  "3-0",
  "3-1",
  "4-0",
]);

/** Extra fractions closed per zone above zone 9 (schematic placement, exact total 44). */
const NEW_EXTRA_BY_ZONE: Record<number, number> = { 10: 3, 11: 2, 12: 2, 13: 1 };

/**
 * T103 instrument (one fixed k-uniform choice: Λ₀ = 3, r = 2): 44/64 closed.
 * Per-cell placement is schematic; the counts 7 → 44 are the probe's numbers.
 */
const isNewClosed = (zone: number, fraction: number) =>
  zone <= 9 || fraction < (NEW_EXTRA_BY_ZONE[zone] ?? 0);

const xOf = (zone: number) => PAD_L + (zone - 1) * (CELL + GAP);
const yOf = (fraction: number) => PAD_T + fraction * (CELL + GAP);

const ROW_LABELS = ["¼", "½", "¾", "1"] as const;
const COL_TICKS = [1, 4, 8, 12, 16] as const;

type CellState = "old" | "new" | "open";

function cellState(zone: number, fraction: number): CellState {
  if (OLD_CLOSED.has(`${zone}-${fraction}`)) return "old";
  if (isNewClosed(zone, fraction)) return "new";
  return "open";
}

const CELLS: { zone: number; fraction: number; state: CellState }[] = [];
for (let zone = 1; zone <= ZONES; zone++) {
  for (let fraction = 0; fraction < FRACTIONS; fraction++) {
    CELLS.push({ zone, fraction, state: cellState(zone, fraction) });
  }
}

const NEW_CELLS = CELLS.filter((c) => c.state === "new");

export function ClosureMapGrid() {
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-emerald-700/90">
          Closure map · 16 zones × 4 wing fractions · T103
        </p>
        <span className="font-mono text-[10px] text-slate-600">
          7/64{" "}
          <span aria-hidden className="text-slate-500">
            →
          </span>{" "}
          <motion.span
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true, amount: 0.5 }}
            transition={{ duration: 0.4, delay: 1.0 }}
            className="text-emerald-700"
          >
            44/64
          </motion.span>
        </span>
      </div>

      <svg
        viewBox={`0 0 ${VIEW_W} ${VIEW_H}`}
        className="w-full"
        role="img"
        aria-label="Closure map over 16 zones and 4 wing fractions: with the old T101 instrument 7 of 64 cells close; with the fixed k-uniform T103 instrument (Lambda zero equals 3, r equals 2) 44 of 64 cells close. Cell placement is schematic, counts exact."
      >
        {/* open cells — static background */}
        {CELLS.filter((c) => c.state === "open").map((c) => (
          <rect
            key={`${c.zone}-${c.fraction}`}
            x={xOf(c.zone)}
            y={yOf(c.fraction)}
            width={CELL}
            height={CELL}
            rx={3}
            fill="rgba(30,41,59,0.5)"
            stroke="rgba(71,85,105,0.5)"
            strokeWidth={1}
          />
        ))}

        {/* T101 cells — light up first */}
        {CELLS.filter((c) => c.state === "old").map((c, i) => (
          <motion.rect
            key={`${c.zone}-${c.fraction}`}
            x={xOf(c.zone)}
            y={yOf(c.fraction)}
            width={CELL}
            height={CELL}
            rx={3}
            fill="rgba(16,185,129,0.5)"
            stroke="rgba(110,231,183,0.85)"
            strokeWidth={1.2}
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true, amount: 0.4 }}
            transition={{ duration: 0.3, delay: i * 0.07 }}
          />
        ))}

        {/* T103 cells — cascade in after */}
        {NEW_CELLS.map((c, i) => (
          <motion.rect
            key={`${c.zone}-${c.fraction}`}
            x={xOf(c.zone)}
            y={yOf(c.fraction)}
            width={CELL}
            height={CELL}
            rx={3}
            fill="rgba(16,185,129,0.24)"
            stroke="rgba(52,211,153,0.5)"
            strokeWidth={1}
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true, amount: 0.4 }}
            transition={{ duration: 0.25, delay: 0.9 + i * 0.035 }}
          />
        ))}

        {/* row labels — wing fraction */}
        {ROW_LABELS.map((label, f) => (
          <text
            key={label}
            x={PAD_L - 6}
            y={yOf(f) + CELL / 2 + 3}
            textAnchor="end"
            fontSize="8"
            className="fill-slate-600 font-mono"
          >
            {label}
          </text>
        ))}

        {/* column ticks — zones */}
        {COL_TICKS.map((zone) => (
          <text
            key={zone}
            x={xOf(zone) + CELL / 2}
            y={VIEW_H - 4}
            textAnchor="middle"
            fontSize="8"
            className="fill-slate-600 font-mono"
          >
            {zone}
          </text>
        ))}
        <text
          x={PAD_L - 6}
          y={VIEW_H - 4}
          textAnchor="end"
          fontSize="7"
          className="fill-slate-500 font-mono"
        >
          zone
        </text>
      </svg>

      <div className="mt-2 flex flex-wrap gap-x-4 gap-y-1 font-mono text-[10px] text-slate-600">
        <span>
          <span
            aria-hidden
            className="mr-1.5 inline-block h-2.5 w-2.5 rounded-sm border border-emerald-300/85 bg-emerald-500/50 align-middle"
          />
          closed at T101 (7)
        </span>
        <span>
          <span
            aria-hidden
            className="mr-1.5 inline-block h-2.5 w-2.5 rounded-sm border border-emerald-400/50 bg-emerald-500/25 align-middle"
          />
          newly closed at T103 (+37)
        </span>
        <span>
          <span
            aria-hidden
            className="mr-1.5 inline-block h-2.5 w-2.5 rounded-sm border border-slate-400 bg-slate-200/60 align-middle"
          />
          open (20)
        </span>
      </div>

      <p className="mt-3 text-xs leading-relaxed text-slate-600">
        One fixed, k-uniform instrument (Λ₀ = 3, r = 2 — no zone tuning) jumps
        the closure map from 7/64 to 44/64. Which cells are drawn closed is
        schematic (only the zone-2 column of T101 is placed as measured); the
        counts are exact. The remaining loss sits in the wing slack
        S = 1 − ρ, not the bulk. Sandbox; not RH evidence.
      </p>
    </div>
  );
}
