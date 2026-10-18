"use client";

import { motion, useReducedMotion } from "motion/react";

/**
 * The T-B closure map (v692 + v693 — machine-verified): the absorption
 * margin of the load-bearing 2×2 lock block, typed as transverse zero mass
 * (a sum of squares, v692), closes on 60 of the 70 complete family windows
 * unconditionally-modulo-citations once the strongest published explicit
 * zero-density bounds are built in (v693). The remainder is exact: nine
 * windows with certificate height T* ≈ 1–3e13 plus the deepest window
 * h = 5690 at T* = 8.5e14.
 *
 * Tile layout is schematic (70 tiles, ordered shallow → deep); the
 * closed/open split and the T* heights are the module's reported census.
 */

const COLS = 10;
const TOTAL = 70;
// The ten open windows sit at the deep end of the family census.
const OPEN_FROM = 60;
const DEEPEST = 69; // h = 5690, T* = 8.5e14

function tileMeta(i: number): {
  cls: string;
  title: string;
} {
  if (i === DEEPEST) {
    return {
      cls: "border-rose-400/50 bg-rose-500/25",
      title: "open: h = 5690 — closes at certificate height T* = 8.5e14",
    };
  }
  if (i >= OPEN_FROM) {
    return {
      cls: "border-amber-400/40 bg-amber-500/20",
      title: "open: closes at certificate height T* ≈ 1–3e13",
    };
  }
  return {
    cls: "border-emerald-400/30 bg-emerald-500/25",
    title: "closed unconditionally-modulo-citations (v693)",
  };
}

export function TBWindowMap() {
  const reduce = useReducedMotion();
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-3 flex items-baseline justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-emerald-700/90">
          The T-B closure map · 70 complete windows
        </p>
        <span className="font-mono text-[10px] text-slate-600">
          v692 · v693
        </span>
      </div>

      <div
        role="img"
        aria-label="70 window tiles: 60 closed unconditionally-modulo-citations, nine open at certificate height about 1e13 to 3e13, one deepest window h equals 5690 at 8.5e14"
        className="grid gap-1"
        style={{ gridTemplateColumns: `repeat(${COLS}, minmax(0, 1fr))` }}
      >
        {Array.from({ length: TOTAL }, (_, i) => {
          const m = tileMeta(i);
          return (
            <motion.div
              key={i}
              title={m.title}
              className={`aspect-square rounded-[3px] border ${m.cls}`}
              initial={reduce ? false : { opacity: 0, scale: 0.5 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true, amount: 0.3 }}
              transition={{
                duration: 0.25,
                delay: reduce ? 0 : (i >= OPEN_FROM ? 0.9 : 0) + i * 0.012,
              }}
            />
          );
        })}
      </div>

      <div className="mt-3 flex flex-wrap gap-x-4 gap-y-1 font-mono text-[10px] text-slate-600">
        <span className="inline-flex items-center gap-1.5">
          <span className="h-2.5 w-2.5 rounded-[2px] border border-emerald-400/30 bg-emerald-500/25" />
          60 closed · unconditionally-modulo-citations
        </span>
        <span className="inline-flex items-center gap-1.5">
          <span className="h-2.5 w-2.5 rounded-[2px] border border-amber-400/40 bg-amber-500/20" />
          9 open · T* ≈ 1–3e13
        </span>
        <span className="inline-flex items-center gap-1.5">
          <span className="h-2.5 w-2.5 rounded-[2px] border border-rose-400/50 bg-rose-500/25" />
          h = 5690 · T* = 8.5e14
        </span>
      </div>

      <p className="mt-3 text-xs leading-relaxed text-slate-600">
        <strong className="font-medium text-emerald-800">
          Machine-verified (v692 + v693, 12 checks):
        </strong>{" "}
        v692 types the razor-thin T-B margin as{" "}
        <em>transverse zero mass</em> — a sum of squares via the identity{" "}
        <span className="font-mono text-slate-700">
          det(G_Z + P) = det G_Z + c_P(s⊥ᵀG_Z s⊥)
        </span>{" "}
        — and v693 builds in the cited explicit bounds (Platt–Trudgian 3e12,
        Hasanalizade–Shen–Wong, the explicit Ingham-form zero density
        arXiv:2507.15184): the penalty drops ×6.5–14.4 and 60/70 windows
        close, each open window carrying its exact certificate height T*.
        Honest scope: this closes the <em>lock-block determinant</em> on the
        declared finite family — full W3 positivity remains the conjecture;
        no RH statement.
      </p>
    </div>
  );
}
