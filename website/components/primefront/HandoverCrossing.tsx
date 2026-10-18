"use client";

import { motion } from "motion/react";

const VIEW_W = 320;
const VIEW_H = 185;
const PAD_L = 10;
const PAD_R = 10;
const PAD_T = 14;
const PAD_B = 26;

/** Vertical scale in units of μ_k/2 (the flat atom line sits at 1). */
const V_MAX = 4.6;
/** The bare E₋ form is 4–14× μ_k/2; drawn clipped near the top of the frame. */
const BARE_LEVEL = 4.1;

const xOf = (t: number) => PAD_L + t * (VIEW_W - PAD_L - PAD_R);
const yOf = (v: number) =>
  PAD_T + (1 - v / V_MAX) * (VIEW_H - PAD_T - PAD_B);

/** Schematic Schur-profile bounds σ_k(δ); shapes schematic, crossings carry the story. */
const sigmaUpper = (t: number) => 2.75 * Math.exp(-1.45 * t);
const sigmaLower = (t: number) => 2.2 * Math.exp(-1.58 * t);

/** Crossings of the two bounds with μ_k/2 = 1. */
const T_CROSS_LOWER = Math.log(2.2) / 1.58; // ≈ 0.50
const T_CROSS_UPPER = Math.log(2.75) / 1.45; // ≈ 0.70
const T_ANCHOR = (T_CROSS_LOWER + T_CROSS_UPPER) / 2;

function curvePath(fn: (t: number) => number): string {
  const parts: string[] = [];
  for (let t = 0; t <= 1.0001; t += 0.04) {
    parts.push(
      `${t === 0 ? "M" : "L"} ${xOf(t).toFixed(1)} ${yOf(fn(t)).toFixed(1)}`,
    );
  }
  return parts.join(" ");
}

function bandPath(): string {
  const parts: string[] = [];
  for (let t = 0; t <= 1.0001; t += 0.04) {
    parts.push(
      `${t === 0 ? "M" : "L"} ${xOf(t).toFixed(1)} ${yOf(sigmaUpper(t)).toFixed(1)}`,
    );
  }
  for (let t = 1; t >= -0.0001; t -= 0.04) {
    parts.push(
      `L ${xOf(Math.max(t, 0)).toFixed(1)} ${yOf(sigmaLower(Math.max(t, 0))).toFixed(1)}`,
    );
  }
  return parts.join(" ") + " Z";
}

export function HandoverCrossing() {
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-violet-700/90">
          The crossing · σ_k(δ) vs μ_k/2 · T102
        </p>
        <span className="font-mono text-[10px] text-slate-600">
          sandwich holds 16/16 zones
        </span>
      </div>

      <svg
        viewBox={`0 0 ${VIEW_W} ${VIEW_H}`}
        className="w-full"
        role="img"
        aria-label="Sandwich diagram over window depth delta: the falling Schur profile sigma k of delta, bracketed by two bounds, crosses the flat atom line mu k over 2; the handover window 2 w k lands between the two crossings in all 16 zones, and the onset is anchored at that crossing."
      >
        <defs>
          <pattern
            id="pf-hatch-wk"
            width="6"
            height="6"
            patternTransform="rotate(45)"
            patternUnits="userSpaceOnUse"
          >
            <line
              x1="0"
              y1="0"
              x2="0"
              y2="6"
              stroke="rgba(251,191,36,0.35)"
              strokeWidth="1.5"
            />
          </pattern>
        </defs>

        {/* hatched handover window between the two crossings */}
        <motion.g
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.5, delay: 1.5 }}
        >
          <rect
            x={xOf(T_CROSS_LOWER)}
            y={PAD_T + 16}
            width={xOf(T_CROSS_UPPER) - xOf(T_CROSS_LOWER)}
            height={VIEW_H - PAD_T - PAD_B - 16}
            fill="url(#pf-hatch-wk)"
            stroke="rgba(252,211,77,0.4)"
            strokeWidth={1}
          />
          <text
            x={xOf(T_ANCHOR)}
            y={PAD_T + 26}
            textAnchor="middle"
            fontSize="8"
            className="fill-amber-800 font-mono"
          >
            2w_k lands here
          </text>
          <text
            x={xOf(T_ANCHOR)}
            y={PAD_T + 36}
            textAnchor="middle"
            fontSize="7"
            className="fill-amber-800/80 font-mono"
          >
            16/16 · ratio 0.749…0.940
          </text>
        </motion.g>

        {/* bare E₋ level, clipped */}
        <line
          x1={PAD_L}
          x2={VIEW_W - PAD_R}
          y1={yOf(BARE_LEVEL)}
          y2={yOf(BARE_LEVEL)}
          stroke="rgba(148,163,184,0.55)"
          strokeWidth={1}
          strokeDasharray="4 3"
        />
        <text
          x={VIEW_W - PAD_R}
          y={yOf(BARE_LEVEL) - 4}
          textAnchor="end"
          fontSize="8"
          className="fill-slate-600 font-mono"
        >
          bare E₋ form · 2.65…3.52 ≈ 4–14× μ_k/2 (clipped)
        </text>

        {/* dressing arrow: bare → dressed profile */}
        <motion.g
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.4, delay: 1.0 }}
        >
          <line
            x1={xOf(0.08)}
            x2={xOf(0.08)}
            y1={yOf(BARE_LEVEL) + 3}
            y2={yOf(sigmaUpper(0.08)) - 5}
            stroke="rgba(196,181,253,0.75)"
            strokeWidth={1.2}
          />
          <path
            d={`M ${xOf(0.08) - 3} ${yOf(sigmaUpper(0.08)) - 8} L ${xOf(0.08)} ${
              yOf(sigmaUpper(0.08)) - 3
            } L ${xOf(0.08) + 3} ${yOf(sigmaUpper(0.08)) - 8} Z`}
            fill="rgba(196,181,253,0.75)"
          />
          <text
            x={xOf(0.11)}
            y={yOf(3.35)}
            fontSize="8"
            className="fill-violet-800 font-mono"
          >
            Schur dressing against E₀⊕E₊
          </text>
          <text
            x={xOf(0.11)}
            y={yOf(3.35) + 10}
            fontSize="8"
            className="fill-violet-800/80 font-mono"
          >
            takes 35.7%…97.3%
          </text>
        </motion.g>

        {/* sandwich band between the two σ bounds */}
        <motion.path
          d={bandPath()}
          fill="rgba(167,139,250,0.16)"
          stroke="none"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.6, delay: 0.9 }}
        />

        {/* σ bounds — draw sequentially */}
        <motion.path
          d={curvePath(sigmaUpper)}
          fill="none"
          stroke="rgba(196,181,253,0.9)"
          strokeWidth={1.6}
          initial={{ pathLength: 0 }}
          whileInView={{ pathLength: 1 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.8, ease: "easeInOut" }}
        />
        <motion.path
          d={curvePath(sigmaLower)}
          fill="none"
          stroke="rgba(167,139,250,0.65)"
          strokeWidth={1.2}
          initial={{ pathLength: 0 }}
          whileInView={{ pathLength: 1 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.8, delay: 0.35, ease: "easeInOut" }}
        />
        <text
          x={xOf(0.72)}
          y={yOf(sigmaUpper(0.72)) - 14}
          fontSize="8"
          className="fill-violet-800 font-mono"
        >
          Schur profile σ_k(δ)
        </text>

        {/* flat atom line μ_k/2 */}
        <motion.line
          x1={PAD_L}
          x2={VIEW_W - PAD_R}
          y1={yOf(1)}
          y2={yOf(1)}
          stroke="rgba(56,189,248,0.85)"
          strokeWidth={1.6}
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.5, delay: 0.7 }}
        />
        <text
          x={VIEW_W - PAD_R}
          y={yOf(1) + 12}
          textAnchor="end"
          fontSize="8"
          className="fill-sky-700 font-mono"
        >
          atom line μ_k/2
        </text>

        {/* animated marker at the anchored crossing */}
        <motion.g
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.3, delay: 1.9 }}
        >
          <circle
            cx={xOf(T_ANCHOR)}
            cy={yOf(1)}
            r={4.5}
            fill="none"
            stroke="rgba(251,191,36,0.7)"
            strokeWidth={1.2}
            className="animate-ping"
            style={{ transformBox: "fill-box", transformOrigin: "center" }}
          />
          <circle cx={xOf(T_ANCHOR)} cy={yOf(1)} r={3} fill="#fbbf24" />
          <text
            x={xOf(T_ANCHOR)}
            y={VIEW_H - PAD_B - 6}
            textAnchor="middle"
            fontSize="8"
            className="fill-amber-800 font-mono"
          >
            δ_c = 2w_k · anchored · R² 0.968
          </text>
        </motion.g>

        {/* x axis */}
        <line
          x1={PAD_L}
          x2={VIEW_W - PAD_R}
          y1={VIEW_H - PAD_B}
          y2={VIEW_H - PAD_B}
          stroke="rgba(148,163,184,0.35)"
          strokeWidth={1}
        />
        <text
          x={VIEW_W - PAD_R}
          y={VIEW_H - PAD_B + 12}
          textAnchor="end"
          fontSize="8"
          className="fill-slate-600 font-mono"
        >
          window depth δ →
        </text>
        <text
          x={PAD_L}
          y={VIEW_H - PAD_B + 12}
          fontSize="8"
          className="fill-slate-600 font-mono"
        >
          w ~ μ^(−0.563 ± 0.098) · q = −1.84 ± 0.37 (fits)
        </text>
      </svg>

      <p className="mt-3 text-xs leading-relaxed text-slate-600">
        The onset is an <em>anchored</em> crossing of two finite quantities —
        the falling Schur profile σ_k(δ) meets the flat atom line μ_k/2, and
        2w_k lands between the two sandwich crossings in 16/16 zones. Honest
        correction: T96&apos;s essential-singularity reading is compatible but
        no longer singled out. The decomposition with g_k is triply refuted —
        causally impossible, statistically dispensable, and arithmetically
        only a ceiling C_k ≤ g_k·μ_k (the extrapolation violates it from
        k = 69; checked over 18 120 prime-power atoms to n = 200 000) — the
        T101 law C/g was a proxy. Curve shapes are schematic; levels,
        percentages, exponents and the 16/16 bracket are the probe&apos;s
        numbers. Sandbox; not RH evidence.
      </p>
    </div>
  );
}
