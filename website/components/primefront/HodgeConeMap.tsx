"use client";

import { motion, useReducedMotion } from "motion/react";

/**
 * The Hodge chamber (v627): all 67 complete windows, transported through
 * the exact v624 Lorentz congruence P^T J_det P = J_fix, land in the
 * positive cone of the cover polarization lattice — on one sheet.
 *
 * Schematic cross-section: the J_fix light cone (signature (1,2)) with the
 * 67 window points inside the upper (positive) sheet. Dot positions are a
 * deterministic low-discrepancy scatter — schematic, not data coordinates.
 */

const W = 320;
const H = 230;
const CX = W / 2;
const APEX_Y = 190;

function conePoints(): { x: number; y: number }[] {
  const pts: { x: number; y: number }[] = [];
  const PHI = 0.6180339887;
  for (let i = 0; i < 67; i++) {
    const u = ((i + 1) * PHI) % 1; // horizontal spread
    const v = ((i + 1) * PHI * PHI) % 1; // depth into the cone
    const y = APEX_Y - 26 - v * 120;
    const halfWidth = (APEX_Y - y) * 0.78 - 10;
    const x = CX + (u * 2 - 1) * Math.max(halfWidth, 4);
    pts.push({ x, y });
  }
  return pts;
}

const POINTS = conePoints();

export function HodgeConeMap() {
  const reduce = useReducedMotion();
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-3 flex items-baseline justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-emerald-700/90">
          The positive cone · one sheet
        </p>
        <span className="font-mono text-[10px] text-slate-600">
          v624 · v627
        </span>
      </div>

      <svg
        viewBox={`0 0 ${W} ${H}`}
        role="img"
        aria-label="Schematic light cone of the cover polarization lattice with all 67 complete windows inside the positive sheet"
        className="w-full"
      >
        <defs>
          <linearGradient id="coneFill" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="rgba(16,185,129,0.16)" />
            <stop offset="100%" stopColor="rgba(16,185,129,0.02)" />
          </linearGradient>
        </defs>

        {/* cone boundary lines */}
        <path
          d={`M${CX - (APEX_Y - 20) * 0.78} 20 L${CX} ${APEX_Y} L${
            CX + (APEX_Y - 20) * 0.78
          } 20`}
          fill="url(#coneFill)"
          stroke="rgba(52,211,153,0.45)"
          strokeWidth="1.25"
        />
        {/* mirror sheet, faint */}
        <path
          d={`M${CX - 28} ${H - 4} L${CX} ${APEX_Y} L${CX + 28} ${H - 4}`}
          fill="none"
          stroke="rgba(100,116,139,0.35)"
          strokeWidth="1"
          strokeDasharray="3 4"
        />
        {/* axis */}
        <line
          x1={CX}
          y1="14"
          x2={CX}
          y2={H - 6}
          stroke="rgba(100,116,139,0.25)"
          strokeWidth="1"
          strokeDasharray="2 5"
        />

        {POINTS.map((p, i) => (
          <motion.circle
            key={i}
            cx={p.x}
            cy={p.y}
            r="2.4"
            fill="rgba(110,231,183,0.9)"
            initial={reduce ? false : { opacity: 0, scale: 0 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true, amount: 0.4 }}
            transition={{ duration: 0.3, delay: reduce ? 0 : 0.35 + i * 0.012 }}
          />
        ))}

        <text
          x={CX}
          y={APEX_Y + 16}
          textAnchor="middle"
          className="fill-slate-600"
          fontSize="9"
          fontFamily="var(--font-mono, monospace)"
        >
          det S = 0 (cone boundary)
        </text>
        <text
          x={CX}
          y={30}
          textAnchor="middle"
          className="fill-emerald-800"
          fontSize="9.5"
          fontFamily="var(--font-mono, monospace)"
        >
          67 / 67 complete windows · det S &gt; 0 · min 11.8
        </text>
      </svg>

      <p className="mt-3 text-xs leading-relaxed text-slate-600">
        Transported by the exact integer congruence{" "}
        <span className="font-mono text-slate-700">Pᵀ J_det P = J_fix</span>{" "}
        (det P = −6), every complete window sits inside the positive cone of
        the cover polarization lattice, all on one sheet. Honest typing:
        scrambled combs do <em>not</em> leave the chamber — membership is a
        density-layer statement (v582); the fine C&nbsp;=&nbsp;1 arithmetic
        lives <em>inside</em> the chamber (v637 closes the fine-invariant
        route as an honest negative).
      </p>
    </div>
  );
}
