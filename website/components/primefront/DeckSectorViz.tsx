"use client";

import { motion, useReducedMotion } from "motion/react";

/**
 * The deck-sector split of the arch density (sandbox exploration,
 * chain_deck_sector_probe.py, 2026-08-03 — NOT promoted): the three digamma
 * channels of the zeta arch density — arguments 1/12, 5/12, 3/4 on the ζ₁₂
 * grid — arise exactly as the tower traces of the three deck sectors of the
 * v623 cover lift (48-site NS circle), with deck charges {1/6, 1/2, 5/6} ==
 * the v628 deck-class twists. The three channels sum to the arch density
 * with the global scalar forced to 1.
 */

const W = 340;
const H = 250;

// Circle panel geometry.
const CX = 88;
const CY = 96;
const R = 62;

// The three digamma arguments as points on the ζ₁₂ circle.
const CHANNELS = [
  {
    frac: 1 / 12,
    label: "1/12",
    twist: "ν = 1/6",
    b: 0.5,
    color: "rgba(52,211,153,0.9)",
    stroke: "rgba(52,211,153,0.75)",
  },
  {
    frac: 5 / 12,
    label: "5/12",
    twist: "ν = 5/6",
    b: 2.5,
    color: "rgba(56,189,248,0.9)",
    stroke: "rgba(56,189,248,0.75)",
  },
  {
    frac: 3 / 4,
    label: "3/4",
    twist: "ν = 1/2",
    b: 4.5,
    color: "rgba(251,191,36,0.9)",
    stroke: "rgba(251,191,36,0.75)",
  },
] as const;

function circlePos(frac: number, r: number = R) {
  const a = -Math.PI / 2 + 2 * Math.PI * frac;
  return { x: CX + r * Math.cos(a), y: CY + r * Math.sin(a) };
}

// Curve panel geometry: T_b(t) = e^{-b t} / (1 - e^{-6t}) on t ∈ [0.35, 2.2],
// and the arch density rho(t) = e^{-t/2}/(1 - e^{-2t}) = sum of the three.
const PX0 = 178;
const PX1 = 330;
const PY0 = 178;
const PY1 = 34;
const T_MIN = 0.35;
const T_MAX = 2.2;
const V_MAX = 1.45;

function towerTrace(b: number, t: number) {
  return Math.exp(-b * t) / (1 - Math.exp(-6 * t));
}

function archDensity(t: number) {
  return Math.exp(-t / 2) / (1 - Math.exp(-2 * t));
}

function curvePath(f: (t: number) => number): string {
  const pts: string[] = [];
  const N = 44;
  for (let i = 0; i <= N; i++) {
    const t = T_MIN + ((T_MAX - T_MIN) * i) / N;
    const v = Math.min(f(t), V_MAX);
    const x = PX0 + ((t - T_MIN) / (T_MAX - T_MIN)) * (PX1 - PX0);
    const y = PY0 - (v / V_MAX) * (PY0 - PY1);
    pts.push(`${x.toFixed(1)} ${y.toFixed(1)}`);
  }
  return `M${pts.join(" L")}`;
}

export function DeckSectorViz() {
  const reduce = useReducedMotion();
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-3 flex items-baseline justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-amber-700/90">
          Three deck sectors · one arch density
        </p>
        <span className="font-mono text-[10px] text-slate-600">
          chain_deck_sector · sandbox
        </span>
      </div>

      <svg
        viewBox={`0 0 ${W} ${H}`}
        role="img"
        aria-label="The three digamma channels of the zeta arch density at arguments 1/12, 5/12 and 3/4 on the zeta-12 circle, summing exactly to the arch density"
        className="w-full"
      >
        {/* ζ₁₂ circle with 12 ticks */}
        <circle
          cx={CX}
          cy={CY}
          r={R}
          fill="none"
          stroke="rgba(100,116,139,0.35)"
          strokeWidth="1"
        />
        {Array.from({ length: 12 }, (_, k) => {
          const outer = circlePos(k / 12, R);
          const inner = circlePos(k / 12, R - 5);
          return (
            <line
              key={k}
              x1={inner.x}
              y1={inner.y}
              x2={outer.x}
              y2={outer.y}
              stroke="rgba(100,116,139,0.45)"
              strokeWidth="1"
            />
          );
        })}
        <text
          x={CX}
          y={CY + 4}
          textAnchor="middle"
          className="fill-slate-600"
          fontSize="9"
          fontFamily="var(--font-mono, monospace)"
        >
          ζ₁₂ grid
        </text>

        {/* the three channel points + twist labels */}
        {CHANNELS.map((c, i) => {
          const p = circlePos(c.frac);
          const lbl = circlePos(c.frac, R + 17);
          return (
            <g key={c.label}>
              <motion.circle
                cx={p.x}
                cy={p.y}
                r="4.4"
                fill={c.color}
                initial={reduce ? false : { opacity: 0, scale: 0 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true, amount: 0.4 }}
                transition={{ duration: 0.35, delay: reduce ? 0 : 0.2 + i * 0.25 }}
              />
              <text
                x={lbl.x}
                y={lbl.y - 2}
                textAnchor="middle"
                fill={c.color}
                fontSize="9"
                fontFamily="var(--font-mono, monospace)"
              >
                {c.label}
              </text>
              <text
                x={lbl.x}
                y={lbl.y + 8}
                textAnchor="middle"
                className="fill-slate-600"
                fontSize="8"
                fontFamily="var(--font-mono, monospace)"
              >
                {c.twist}
              </text>
            </g>
          );
        })}

        {/* channel curves */}
        {CHANNELS.map((c, i) => (
          <motion.path
            key={`curve-${c.label}`}
            d={curvePath((t) => towerTrace(c.b, t))}
            fill="none"
            stroke={c.stroke}
            strokeWidth="1.3"
            initial={reduce ? false : { pathLength: 0 }}
            whileInView={{ pathLength: 1 }}
            viewport={{ once: true, amount: 0.4 }}
            transition={{ duration: 0.8, delay: reduce ? 0 : 0.25 + i * 0.25 }}
          />
        ))}

        {/* the arch density = exact sum */}
        <motion.path
          d={curvePath(archDensity)}
          fill="none"
          stroke="rgba(226,232,240,0.9)"
          strokeWidth="1.8"
          strokeDasharray="5 3"
          initial={reduce ? false : { pathLength: 0 }}
          whileInView={{ pathLength: 1 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.9, delay: reduce ? 0 : 1.1 }}
        />

        {/* curve panel labels */}
        <text
          x={PX0 + 2}
          y={PY1 - 8}
          className="fill-slate-800"
          fontSize="9"
          fontFamily="var(--font-mono, monospace)"
        >
          Σ channels = arch density ρ(t) · scalar forced to 1
        </text>
        <line
          x1={PX0}
          y1={PY0 + 4}
          x2={PX1}
          y2={PY0 + 4}
          stroke="rgba(100,116,139,0.35)"
          strokeWidth="1"
        />
        <text
          x={(PX0 + PX1) / 2}
          y={PY0 + 16}
          textAnchor="middle"
          className="fill-slate-600"
          fontSize="8.5"
          fontFamily="var(--font-mono, monospace)"
        >
          tower traces T_b(t), b ∈ {"{1/2, 5/2, 9/2}"}
        </text>

        {/* deck-sector legend */}
        <text
          x={CX}
          y={CY + R + 36}
          textAnchor="middle"
          className="fill-slate-600"
          fontSize="8.5"
          fontFamily="var(--font-mono, monospace)"
        >
          deck sectors m mod 12 ∈ {"{1, 5, 9}"}
        </text>
        <text
          x={CX}
          y={CY + R + 48}
          textAnchor="middle"
          className="fill-slate-600"
          fontSize="8.5"
          fontFamily="var(--font-mono, monospace)"
        >
          twists {"{1/6, 1/2, 5/6}"} = v628
        </text>
      </svg>

      <p className="mt-3 text-xs leading-relaxed text-slate-600">
        <strong className="font-medium text-amber-800">
          Sandbox exploration — not promoted:
        </strong>{" "}
        the three digamma channels of the arch density (arguments{" "}
        <span className="font-mono text-slate-700">1/12, 5/12, 3/4</span> on
        the ζ₁₂ grid) are exactly the tower traces of the three deck sectors
        of the v623 cover lift, carrying the v628 twist classes{" "}
        <span className="font-mono text-slate-700">{"{1/6, 1/2, 5/6}"}</span>{" "}
        — with the global scalar forced to 1 and the wrong twist set{" "}
        <span className="font-mono text-slate-700">{"{1/4, 1/2, 3/4}"}</span>{" "}
        failing as demanded (≥ 30% off). A geometric anchor for the arch
        layer, not a positivity statement.
      </p>
    </div>
  );
}
