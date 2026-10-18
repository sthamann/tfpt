"use client";

import { motion, useReducedMotion } from "motion/react";

/**
 * The just-in-time positivity corridor (sandbox exploration, chain_* probes,
 * 2026-08-03 — NOT promoted): for each prime-power slot the previous section
 * leaves a closed interval [w_lo, w_hi] of admissible atom masses (the
 * resolvent / Levinson edge formula, machine-verified as an identity in the
 * probe), and the TRUE mass Λ(n)/√n sits strictly inside it — at a stable
 * relative position ≈ 0.53 with a slow log-n drift (corr ≈ −0.68).
 *
 * Schematic: corridor bands and mass dots use the probes' reported summary
 * statistics (pooled median 0.529, IQR [0.511, 0.559]) with a deterministic
 * jitter — representative rendering, not data coordinates.
 */

const W = 340;
const H = 240;
const PAD_L = 34;
const PAD_R = 12;
const TOP = 30;
const BOTTOM = 200;

/** Prime-power slots by log n (the atom positions of the window form). */
const SLOTS = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 19, 23, 27, 32, 41, 53, 64, 81, 101];

const LOG_MIN = Math.log(2);
const LOG_MAX = Math.log(101);

type Slot = {
  x: number;
  yLo: number;
  yHi: number;
  yMass: number;
  n: number;
};

function buildSlots(): Slot[] {
  return SLOTS.map((n, i) => {
    const t = (Math.log(n) - LOG_MIN) / (LOG_MAX - LOG_MIN);
    const x = PAD_L + t * (W - PAD_L - PAD_R);
    // Deterministic jitter (golden-ratio scatter), scaled to the IQR width.
    const jitter = ((((i + 1) * 0.6180339887) % 1) - 0.5) * 0.048;
    // Median 0.529 with the measured negative log-n drift (corr ≈ −0.68).
    const pos = 0.556 - 0.055 * t + jitter;
    // Corridor band: schematic height, mildly narrowing with depth.
    const half = 46 - 14 * t;
    const yMid = TOP + 62 + t * 44;
    const yLo = yMid + half;
    const yHi = yMid - half;
    const yMass = yLo - pos * (yLo - yHi);
    return { x, yLo, yHi, yMass, n };
  });
}

const DATA = buildSlots();

export function KorridorViz() {
  const reduce = useReducedMotion();
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-3 flex items-baseline justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-amber-700/90">
          The positivity corridor · per prime-power slot
        </p>
        <span className="font-mono text-[10px] text-slate-600">
          chain_* probes · sandbox
        </span>
      </div>

      <svg
        viewBox={`0 0 ${W} ${H}`}
        role="img"
        aria-label="Schematic corridors of admissible atom masses per prime-power slot, with the true mass sitting near relative position 0.53 inside every corridor"
        className="w-full"
      >
        {/* axis */}
        <line
          x1={PAD_L - 6}
          y1={BOTTOM}
          x2={W - PAD_R}
          y2={BOTTOM}
          stroke="rgba(100,116,139,0.35)"
          strokeWidth="1"
        />
        <text
          x={(PAD_L + W - PAD_R) / 2}
          y={BOTTOM + 14}
          textAnchor="middle"
          className="fill-slate-600"
          fontSize="8.5"
          fontFamily="var(--font-mono, monospace)"
        >
          slot position log n (prime powers 2 … 101)
        </text>

        {/* corridor bands */}
        {DATA.map((s, i) => (
          <motion.line
            key={`band-${s.n}`}
            x1={s.x}
            y1={s.yLo}
            x2={s.x}
            y2={s.yHi}
            stroke="rgba(251,191,36,0.28)"
            strokeWidth="7"
            strokeLinecap="round"
            initial={reduce ? false : { opacity: 0, scaleY: 0.4 }}
            whileInView={{ opacity: 1, scaleY: 1 }}
            viewport={{ once: true, amount: 0.4 }}
            transition={{ duration: 0.35, delay: reduce ? 0 : i * 0.035 }}
            style={{ transformOrigin: `${s.x}px ${(s.yLo + s.yHi) / 2}px` }}
          />
        ))}

        {/* closed-formula edges */}
        {DATA.map((s) => (
          <g key={`edges-${s.n}`}>
            <line
              x1={s.x - 5}
              y1={s.yLo}
              x2={s.x + 5}
              y2={s.yLo}
              stroke="rgba(251,191,36,0.75)"
              strokeWidth="1.4"
            />
            <line
              x1={s.x - 5}
              y1={s.yHi}
              x2={s.x + 5}
              y2={s.yHi}
              stroke="rgba(251,191,36,0.75)"
              strokeWidth="1.4"
            />
          </g>
        ))}

        {/* median guide through the mass dots */}
        <motion.path
          d={`M${DATA.map((s) => `${s.x} ${s.yMass}`).join(" L")}`}
          fill="none"
          stroke="rgba(56,189,248,0.35)"
          strokeWidth="1"
          strokeDasharray="3 4"
          initial={reduce ? false : { pathLength: 0 }}
          whileInView={{ pathLength: 1 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 1.1, delay: reduce ? 0 : 0.5 }}
        />

        {/* the true masses */}
        {DATA.map((s, i) => (
          <motion.circle
            key={`mass-${s.n}`}
            cx={s.x}
            cy={s.yMass}
            r="2.6"
            fill="rgba(125,211,252,0.95)"
            initial={reduce ? false : { opacity: 0, scale: 0 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true, amount: 0.4 }}
            transition={{ duration: 0.3, delay: reduce ? 0 : 0.25 + i * 0.035 }}
          />
        ))}

        {/* legend */}
        <text
          x={PAD_L - 2}
          y={16}
          className="fill-amber-800"
          fontSize="9"
          fontFamily="var(--font-mono, monospace)"
        >
          corridor [w_lo, w_hi] · closed edge formula
        </text>
        <text
          x={PAD_L - 2}
          y={27}
          className="fill-sky-800"
          fontSize="9"
          fontFamily="var(--font-mono, monospace)"
        >
          true mass Λ(n)/√n · pos ≈ 0.53, log-n drift
        </text>
      </svg>

      <p className="mt-3 text-xs leading-relaxed text-slate-600">
        <strong className="font-medium text-amber-800">
          Sandbox exploration — not promoted:
        </strong>{" "}
        the corridor edges come from a closed resolvent identity
        (machine-verified in the probe); the true mass lies{" "}
        <em>inside every corridor measured</em>, at relative position with
        pooled median{" "}
        <span className="font-mono text-slate-700">0.529</span>, IQR{" "}
        <span className="font-mono text-slate-700">[0.511, 0.559]</span>, and
        a slow negative log-n drift (corr ≈{" "}
        <span className="font-mono text-slate-700">−0.68</span>). No closed
        law for the position yet — that is the open question, stated as such.
      </p>
    </div>
  );
}
