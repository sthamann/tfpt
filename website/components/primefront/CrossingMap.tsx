"use client";

import { motion } from "motion/react";

const LOG2 = Math.log(2);
const LOG4 = Math.log(4);
/** Outer edge of the one-atom zone (T91, Lambert-W form): a* = 0.9253 < log 3. */
const BAND_END = 0.9253;

const VIEW_W = 320;
const AXIS_Y = 96;
const BAND_H = 16;
const PAD_L = 6;
const PAD_R = 6;

const xOf = (a: number) =>
  PAD_L + (a / LOG4) * (VIEW_W - PAD_L - PAD_R);

/** dim_REST grows softly 0 → 4 (of 32); step positions across the crossing are schematic. */
const REST_STEPS = [
  { a: 0.45, dim: 0 },
  { a: 0.78, dim: 1 },
  { a: 0.92, dim: 2 },
  { a: 1.08, dim: 3 },
  { a: 1.26, dim: 4 },
];

const MARKERS = [
  {
    a: 0.7486,
    label: "0.7486",
    note: "sign change — prime atom becomes load-bearing (T91; a_neg recalibrated by T93)",
  },
  { a: 0.85, label: "0.85", note: "pole-free atom↔arch content remains (T90)" },
  { a: 1.2, label: "1.2", note: "odd atom-coupled mode (T90)" },
];

const MAX_DIM = 4;
const REST_TOP = 12;
const REST_BOTTOM = 62;

export function CrossingMap() {
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-violet-700/90">
          Crossing map · support width a · Teile 87–93
        </p>
        <span className="font-mono text-[10px] text-slate-600">
          λ_min ≥ 0 on all 16 windows
        </span>
      </div>

      <svg
        viewBox={`0 0 ${VIEW_W} 140`}
        className="w-full"
        role="img"
        aria-label="Map of the I5 crossing region over support width a: proven zone up to log 2, thin attackable band up to 1.0, classical band-limitation beyond, with the residual subspace dimension growing from 0 to 4."
      >
        {/* residual dimension steps */}
        {REST_STEPS.map((s, i) => {
          const h = (s.dim / MAX_DIM) * (REST_BOTTOM - REST_TOP);
          const w = 26;
          return (
            <g key={s.a}>
              <motion.rect
                x={xOf(s.a) - w / 2}
                y={REST_BOTTOM - h}
                width={w}
                height={Math.max(h, 1)}
                rx={3}
                fill="rgba(167,139,250,0.35)"
                stroke="rgba(196,181,253,0.55)"
                strokeWidth={1}
                initial={{ opacity: 0, scaleY: 0 }}
                whileInView={{ opacity: 1, scaleY: 1 }}
                viewport={{ once: true, amount: 0.4 }}
                transition={{ duration: 0.45, delay: i * 0.1 }}
                style={{ transformOrigin: `0px ${REST_BOTTOM}px` }}
              />
              <text
                x={xOf(s.a)}
                y={REST_BOTTOM - h - 4}
                textAnchor="middle"
                fontSize="9"
                className="fill-violet-800 font-mono"
              >
                {s.dim}
              </text>
            </g>
          );
        })}
        <text x={PAD_L} y={REST_TOP - 3} fontSize="8" className="fill-slate-600 font-mono">
          dim residual (of 32)
        </text>

        {/* zone bands */}
        <rect
          x={xOf(0)}
          y={AXIS_Y - BAND_H}
          width={xOf(LOG2) - xOf(0)}
          height={BAND_H}
          rx={3}
          fill="rgba(16,185,129,0.22)"
          stroke="rgba(52,211,153,0.5)"
          strokeWidth={1}
        />
        <rect
          x={xOf(LOG2)}
          y={AXIS_Y - BAND_H}
          width={xOf(BAND_END) - xOf(LOG2)}
          height={BAND_H}
          rx={3}
          fill="rgba(251,191,36,0.22)"
          stroke="rgba(252,211,77,0.55)"
          strokeWidth={1}
        />
        <rect
          x={xOf(BAND_END)}
          y={AXIS_Y - BAND_H}
          width={xOf(LOG4) - xOf(BAND_END)}
          height={BAND_H}
          rx={3}
          fill="rgba(71,85,105,0.35)"
          stroke="rgba(100,116,139,0.5)"
          strokeWidth={1}
        />

        {/* axis ticks */}
        {([
          { a: LOG2, label: "log 2", anchor: "middle" },
          { a: BAND_END, label: "a* 0.9253", anchor: "middle" },
          { a: LOG4, label: "log 4", anchor: "end" },
        ] as const).map((t) => (
          <g key={t.label}>
            <line
              x1={xOf(t.a)}
              x2={xOf(t.a)}
              y1={REST_TOP}
              y2={AXIS_Y + 4}
              stroke="rgba(148,163,184,0.35)"
              strokeWidth={1}
              strokeDasharray="2 3"
            />
            <text
              x={xOf(t.a)}
              y={AXIS_Y + 14}
              textAnchor={t.anchor}
              fontSize="9"
              className="fill-slate-600 font-mono"
            >
              {t.label}
            </text>
          </g>
        ))}

        {/* measured markers */}
        {MARKERS.map((m, i) => (
          <g key={m.label}>
            <circle cx={xOf(m.a)} cy={AXIS_Y - BAND_H / 2} r={3} fill="#f8fafc" />
            <text
              x={xOf(m.a)}
              y={AXIS_Y + (i % 2 === 0 ? 25 : 34)}
              textAnchor="middle"
              fontSize="8"
              className="fill-slate-600 font-mono"
            >
              {m.label}
            </text>
          </g>
        ))}
      </svg>

      <ul className="mt-2 space-y-1 font-mono text-[10px] text-slate-600">
        <li>
          <span className="text-emerald-700">green</span> — proven zone a ≤ log 2:
          prime side identically zero; classical unconditional positivity
          (Yoshida, Bombieri, Connes–Consani)
        </li>
        <li>
          <span className="text-amber-800">amber</span> — the thin band
          log 2 &lt; a ≤ a* = 0.9253: the real attackable content, atom↔arch
          balance; a* &lt; log 3, so the whole band is a one-atom zone (T91)
        </li>
        <li>
          <span className="text-slate-700">slate</span> — beyond a*: further
          prime atoms enter and the deep near-zeros are classical
          band-limitation, no crossing content
        </li>
      </ul>

      <div className="mt-3 grid gap-2 sm:grid-cols-3">
        {MARKERS.map((m) => (
          <div
            key={m.a}
            className="rounded-lg border border-slate-300/40 bg-slate-100/50 px-2 py-1.5"
          >
            <p className="font-mono text-[11px] text-slate-800">a = {m.label}</p>
            <p className="text-[10px] leading-tight text-slate-600">{m.note}</p>
          </div>
        ))}
      </div>

      <p className="mt-3 text-xs leading-relaxed text-slate-600">
        The boundary is not sharp — the margin falls smoothly and the atom
        turn-on is (a − log 2)³-soft. T90 dissects the residual: the 1–4 vectors
        are n-stable (≤ 2.1°) and explicit (Gauss×cos / Gauss×sin, 99+%
        capture), and 3 of 10 tracked vectors sit under no control at all. T91
        adds the inner edge: at a<sub>neg</sub> = 0.7486 (recalibrated by T93;
        was 0.7410) the pole+arch margin is exhausted and the prime atom at
        u = log 2 turns load-bearing — the same point the T89 balance found.
        Step positions above are schematic; the dimensions and the marked
        widths are measured. Geography locates where an attack must work — it
        does not perform one. Not RH evidence.
      </p>
    </div>
  );
}
