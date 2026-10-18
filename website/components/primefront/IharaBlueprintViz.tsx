"use client";

import { motion, useReducedMotion } from "motion/react";

/**
 * The Hecke-SOS blueprint (v691, PRIME.HECKESOS.01 — machine-verified):
 * in the Ihara lab the target factorisation A = B*B + P exists exactly —
 * B the Chebyshev columns of the Hecke operator, P the closed defect Gram,
 * and P ⪰ 0 ⟺ Ramanujan. On the ζ side the same shape is assembled, but
 * the geometric operator Z1 whose polynomial traces are the window moments
 * is the named missing part (PRIME.Z1.OPERATOR.01, OPEN).
 */

const REVEAL = {
  initial: { opacity: 0, y: 8 },
  whileInView: { opacity: 1, y: 0 },
  viewport: { once: true, amount: 0.35 },
} as const;

function Box({
  children,
  tone,
  delay,
  reduce,
  dashed,
  pulse,
}: {
  children: React.ReactNode;
  tone: string;
  delay: number;
  reduce: boolean | null;
  dashed?: boolean;
  pulse?: boolean;
}) {
  return (
    <motion.div
      {...(reduce ? {} : REVEAL)}
      transition={{ duration: 0.45, delay: reduce ? 0 : delay }}
      className={`rounded-lg border px-3 py-2 text-center font-mono text-[11px] leading-snug ${
        dashed ? "border-dashed" : ""
      } ${pulse ? "animate-pulse" : ""} ${tone}`}
    >
      {children}
    </motion.div>
  );
}

function PlusSign({ delay, reduce }: { delay: number; reduce: boolean | null }) {
  return (
    <motion.div
      {...(reduce ? {} : REVEAL)}
      transition={{ duration: 0.3, delay: reduce ? 0 : delay }}
      className="text-center font-mono text-sm text-slate-600"
    >
      +
    </motion.div>
  );
}

export function IharaBlueprintViz() {
  const reduce = useReducedMotion();
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <div className="mb-3 flex items-baseline justify-between gap-2">
        <p className="font-mono text-[10px] uppercase tracking-widest text-emerald-700/90">
          The blueprint · A = B*B + P
        </p>
        <span className="font-mono text-[10px] text-slate-600">v691</span>
      </div>

      <div className="grid grid-cols-2 gap-3">
        {/* Ihara lab column — proved */}
        <div className="space-y-2">
          <p className="text-center font-mono text-[10px] uppercase tracking-widest text-emerald-700/80">
            Ihara lab · exists exactly
          </p>
          <Box
            tone="border-slate-400/60 bg-slate-100/60 text-slate-800"
            delay={0.1}
            reduce={reduce}
          >
            A — the window form
          </Box>
          <motion.div
            {...(reduce ? {} : REVEAL)}
            transition={{ duration: 0.3, delay: reduce ? 0 : 0.25 }}
            className="text-center font-mono text-sm text-slate-600"
          >
            =
          </motion.div>
          <Box
            tone="border-emerald-400/40 bg-emerald-500/10 text-emerald-800"
            delay={0.4}
            reduce={reduce}
          >
            B*B — Chebyshev columns of the Hecke operator
            <span className="mt-1 block text-[9px] text-emerald-700/70">
              recursion · no Cholesky · no spectrum
            </span>
          </Box>
          <PlusSign delay={0.55} reduce={reduce} />
          <Box
            tone="border-emerald-400/40 bg-emerald-500/10 text-emerald-800"
            delay={0.7}
            reduce={reduce}
          >
            P — closed defect Gram
            <span className="mt-1 block text-[9px] text-emerald-700/70">
              P ⪰ 0 ⟺ Ramanujan
            </span>
          </Box>
        </div>

        {/* ζ column — the missing part */}
        <div className="space-y-2">
          <p className="text-center font-mono text-[10px] uppercase tracking-widest text-sky-700/80">
            ζ deployment · same shape
          </p>
          <Box
            tone="border-slate-400/60 bg-slate-100/60 text-slate-800"
            delay={0.9}
            reduce={reduce}
          >
            deployed window form
            <span className="mt-1 block text-[9px] text-slate-600">
              = the sine/defect half of the canonical split
            </span>
          </Box>
          <motion.div
            {...(reduce ? {} : REVEAL)}
            transition={{ duration: 0.3, delay: reduce ? 0 : 1.0 }}
            className="text-center font-mono text-sm text-slate-600"
          >
            =
          </motion.div>
          <Box
            tone="border-sky-400/40 bg-sky-500/10 text-sky-800"
            delay={1.15}
            reduce={reduce}
          >
            cos half — unconditionally SOS
          </Box>
          <PlusSign delay={1.3} reduce={reduce} />
          <Box
            tone="border-amber-400/50 bg-amber-500/10 text-amber-800"
            delay={1.45}
            reduce={reduce}
            dashed
            pulse={!reduce}
          >
            Z1 = ?
            <span className="mt-1 block text-[9px] text-amber-700/80">
              a self-adjoint geometric operator whose polynomial traces are
              the window moments — OPEN
            </span>
          </Box>
        </div>
      </div>

      <p className="mt-4 text-xs leading-relaxed text-slate-600">
        <strong className="font-medium text-emerald-800">
          Machine-verified (v691, 27 checks):
        </strong>{" "}
        on a proven RH analogue (the Ihara zeta of Ramanujan graphs) the
        target factorisation exists <em>exactly</em>, and the RH analogue is
        one operator inequality: P ⪰ 0 ⟺ Ramanujan. The deployed ζ window
        form is exactly the sine/defect half of the canonical cos/sin split.
        What the ζ column is missing is <em>named</em>, not hidden: the
        operator Z1 (Hilbert–Pólya type) — registered OPEN as
        PRIME.Z1.OPERATOR.01. The v695–v698 series records its ground
        (measure, canonical operator, masses, positions); the v713–v721
        montage and moonshot arc now record a <em>measured</em> truncation
        candidate (glue, state, spectrum, trace formula) — measurements, not
        theorems; the continuum Sätze stay named open and the contract stays
        open (sharpened 2026-08-05 after the diagonal-Gram closure: the
        bulk + boundary/threshold form with the measured qf handover
        constraints). No RH statement.
      </p>
    </div>
  );
}
