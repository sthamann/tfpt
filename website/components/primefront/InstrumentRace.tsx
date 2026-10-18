"use client";

import { motion } from "motion/react";

const VIEW_W = 320;
const VIEW_H = 170;
const PAD_L = 8;
const PAD_R = 40;
const PAD_T = 12;
const PAD_B = 22;

const ZONES = 16;

/** Race quantity r_k: measured endpoints 9.33 → 2.70 (T103). */
const R_START = 9.33;
const R_END_NEW = 2.7;
/** Endpoint-anchored decay for the drawn curve; the fitted slope is −0.0748 ± 0.0116. */
const NEW_SLOPE = Math.log(R_START / R_END_NEW) / (ZONES - 1);
/** Fitted slope of the T101 two-factor chain: −0.1622 ± 0.0562. */
const OLD_SLOPE = 0.1622;
/**
 * Schematic spectrum floor, drawn so the old curve exits exactly at zone 3
 * (T101: only zone 2 closes throughout; 7/64). The floor shape is schematic;
 * the two slopes and the endpoints 9.33 → 2.70 are the measured/fitted values.
 */
const FLOOR_SLOPE = 0.075;
const FLOOR_START = R_START / Math.exp((OLD_SLOPE - FLOOR_SLOPE) * 2);

const R_MIN = 0.72;
const R_MAX = 10.8;

const xOf = (k: number) =>
  PAD_L + ((k - 1) / (ZONES - 1)) * (VIEW_W - PAD_L - PAD_R);
const yOf = (r: number) => {
  const lo = Math.log(R_MIN);
  const hi = Math.log(R_MAX);
  return (
    PAD_T + (1 - (Math.log(r) - lo) / (hi - lo)) * (VIEW_H - PAD_T - PAD_B)
  );
};

const rNew = (k: number) => R_START * Math.exp(-NEW_SLOPE * (k - 1));
const rOld = (k: number) => R_START * Math.exp(-OLD_SLOPE * (k - 1));
const floorOf = (k: number) => FLOOR_START * Math.exp(-FLOOR_SLOPE * (k - 1));

function curvePath(fn: (k: number) => number): string {
  const parts: string[] = [];
  for (let k = 1; k <= ZONES; k += 0.5) {
    parts.push(
      `${k === 1 ? "M" : "L"} ${xOf(k).toFixed(1)} ${yOf(fn(k)).toFixed(1)}`,
    );
  }
  return parts.join(" ");
}

function spectrumBandPath(): string {
  const parts: string[] = [
    `M ${xOf(1).toFixed(1)} ${PAD_T}`,
    `L ${xOf(ZONES).toFixed(1)} ${PAD_T}`,
  ];
  for (let k = ZONES; k >= 1; k -= 0.5) {
    parts.push(`L ${xOf(k).toFixed(1)} ${yOf(floorOf(k)).toFixed(1)}`);
  }
  return parts.join(" ") + " Z";
}

const AXIS_TICKS = [1, 4, 8, 12, 16] as const;
/** Old curve meets the schematic floor at zone 3 by construction. */
const EXIT_ZONE = 3;

export function InstrumentRace() {
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-emerald-700/90">
          The race r_k · 16 zones · T101 → T103
        </p>
        <span className="font-mono text-[10px] text-slate-600">
          log scale · slopes are fits
        </span>
      </div>

      <svg
        viewBox={`0 0 ${VIEW_W} ${VIEW_H}`}
        className="w-full"
        role="img"
        aria-label="Race quantity r_k over 16 zones on a log scale: the old T101 instrument decays with slope minus 0.1622 and leaves the schematic spectrum band at zone 3; the new m(Lambda) instrument of T103 decays with slope minus 0.0748, falls only from 9.33 to 2.70 and never leaves the spectrum."
      >
        {/* schematic spectrum band */}
        <path
          d={spectrumBandPath()}
          fill="rgba(56,189,248,0.07)"
          stroke="none"
        />
        <path
          d={curvePath(floorOf)}
          fill="none"
          stroke="rgba(100,116,139,0.6)"
          strokeWidth={1}
          strokeDasharray="3 3"
        />
        <text
          x={xOf(11)}
          y={yOf(floorOf(11)) + 11}
          fontSize="8"
          className="fill-slate-600 font-mono"
        >
          spectrum edge (schematic)
        </text>

        {/* old instrument — draws first */}
        <motion.path
          d={curvePath(rOld)}
          fill="none"
          stroke="rgba(251,113,133,0.85)"
          strokeWidth={1.6}
          initial={{ pathLength: 0 }}
          whileInView={{ pathLength: 1 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 1.0, ease: "easeInOut" }}
        />
        {/* exit marker at zone 3 */}
        <motion.g
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.3, delay: 0.55 }}
        >
          <circle
            cx={xOf(EXIT_ZONE)}
            cy={yOf(rOld(EXIT_ZONE))}
            r={3.5}
            fill="none"
            stroke="#fb7185"
            strokeWidth={1.4}
          />
          <text
            x={xOf(EXIT_ZONE) + 6}
            y={yOf(rOld(EXIT_ZONE)) - 5}
            fontSize="8"
            className="fill-rose-700 font-mono"
          >
            leaves the spectrum at zone 3
          </text>
        </motion.g>
        <text
          x={xOf(10.5)}
          y={yOf(rOld(10.5)) + 12}
          fontSize="8"
          className="fill-rose-700/90 font-mono"
        >
          old · slope −0.1622 ± 0.0562
        </text>

        {/* new m(Λ) instrument — draws second */}
        <motion.path
          d={curvePath(rNew)}
          fill="none"
          stroke="rgba(52,211,153,0.95)"
          strokeWidth={2}
          initial={{ pathLength: 0 }}
          whileInView={{ pathLength: 1 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 1.0, delay: 1.05, ease: "easeInOut" }}
        />
        <motion.g
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.3, delay: 2.0 }}
        >
          <circle
            cx={xOf(ZONES)}
            cy={yOf(R_END_NEW)}
            r={2.5}
            fill="#34d399"
          />
          <text
            x={xOf(ZONES) + 5}
            y={yOf(R_END_NEW) + 3}
            fontSize="9"
            className="fill-emerald-700 font-mono"
          >
            2.70
          </text>
        </motion.g>
        <text
          x={xOf(1) + 4}
          y={yOf(R_START) - 4}
          fontSize="9"
          className="fill-slate-700 font-mono"
        >
          9.33
        </text>
        <text
          x={xOf(5.5)}
          y={yOf(rNew(5.5)) - 6}
          fontSize="8"
          className="fill-emerald-700/90 font-mono"
        >
          new m(Λ) · slope −0.0748 ± 0.0116
        </text>

        {/* x axis */}
        <line
          x1={PAD_L}
          x2={VIEW_W - PAD_R}
          y1={VIEW_H - PAD_B}
          y2={VIEW_H - PAD_B}
          stroke="rgba(148,163,184,0.35)"
          strokeWidth={1}
        />
        {AXIS_TICKS.map((k) => (
          <text
            key={k}
            x={xOf(k)}
            y={VIEW_H - PAD_B + 12}
            textAnchor="middle"
            fontSize="8"
            className="fill-slate-600 font-mono"
          >
            {k}
          </text>
        ))}
        <text
          x={VIEW_W - PAD_R}
          y={VIEW_H - PAD_B + 12}
          textAnchor="start"
          fontSize="8"
          className="fill-slate-500 font-mono"
        >
          {" "}
          zone
        </text>
      </svg>

      <div className="mt-3 grid gap-2 sm:grid-cols-3">
        <div className="rounded-lg border border-emerald-400/30 bg-emerald-500/10 px-2 py-1.5 text-center">
          <p className="font-serif text-lg text-emerald-800">3.0× – 103.4×</p>
          <p className="text-[10px] leading-tight text-slate-600">
            demand reduction across the 64 samples
          </p>
        </div>
        <div className="rounded-lg border border-slate-300/40 bg-slate-100/50 px-2 py-1.5 text-center">
          <p className="font-mono text-sm text-slate-800">
            Λ_ok 0.77…3.64
          </p>
          <p className="text-[10px] leading-tight text-slate-600">
            bounded over all 16 zones (was 2.3…376)
          </p>
        </div>
        <div className="rounded-lg border border-slate-300/40 bg-slate-100/50 px-2 py-1.5 text-center">
          <p className="font-mono text-sm text-slate-800">modes 2 → 232</p>
          <p className="text-[10px] leading-tight text-slate-600">
            honest price: explicit modes grow
          </p>
        </div>
      </div>

      <p className="mt-3 text-xs leading-relaxed text-slate-600">
        The race quantity r_k must stay inside the spectrum for a zone to
        close. The old two-factor chain (T101) decays as r ~ exp(−0.1622k)
        (fit) and only zone 2 survives throughout (7/64). The θ-weighted
        m(Λ) instrument (T103) halves the slope to −0.0748 ± 0.0116 (fit):
        r_k falls only 9.33 → 2.70 and never leaves the spectrum. Curve
        shapes and the spectrum edge are schematic exponentials; slopes,
        endpoints and the reduction factors are the probe&apos;s numbers.
        Sandbox; not RH evidence.
      </p>
    </div>
  );
}
