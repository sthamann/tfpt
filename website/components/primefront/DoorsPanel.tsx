"use client";

import { motion } from "motion/react";

/** Measured endpoints of the λ* target inequality (Teil 75). */
const SAFETY_AT_OMEGA_1 = 273;
const OMEGA_CROSSING = 4.2;

const CHART_W = 220;
const CHART_H = 68;
const OMEGA_MIN = 0.8;
const OMEGA_MAX = 4.8;
const LOG_MIN = Math.log10(0.6);
const LOG_MAX = Math.log10(400);

const xOf = (omega: number) =>
  ((omega - OMEGA_MIN) / (OMEGA_MAX - OMEGA_MIN)) * CHART_W;
const yOf = (safety: number) =>
  CHART_H - ((Math.log10(safety) - LOG_MIN) / (LOG_MAX - LOG_MIN)) * CHART_H;

export function DoorsPanel() {
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-5">
      <p className="mb-3 font-mono text-[10px] uppercase tracking-widest text-amber-700/90">
        Three doors · Teile 73–81
      </p>

      <div className="space-y-2">
        {/* Door A */}
        <Door
          letter="A"
          title="Spectral polarisation"
          verdict="NO-GO"
          tone="rose"
          note="The spectral Dirac phase carries the metaplectic sign datum, but every ε-equivariant spectral functional is exactly re-signing invariant."
        >
          <Meter label="phase carries sign datum" percent={93} tone="rose" />
          <p className="mt-1.5 font-mono text-[10px] text-rose-800/80">
            L² no-go — the spectral world is provably sign-blind. Requirement
            list R1–R5 (Krein quotient, ♭ as null sector).
          </p>
        </Door>

        {/* Door B */}
        <Door
          letter="B"
          title="λ* gets its own calculus"
          verdict="STRUCTURED"
          tone="amber"
          note="Closed form, own functional equation (orbit invariant tanh(σ²ω²/2)), critical width σ_c = √2, convexity."
        >
          <div className="mt-1 flex items-end gap-3">
            <svg
              viewBox={`0 0 ${CHART_W} ${CHART_H}`}
              className="h-16 w-full max-w-[220px]"
              role="img"
              aria-label="λ* safety factor falls from 273 at omega = 1 to 1 at omega = 4.2"
            >
              <line
                x1={0}
                x2={CHART_W}
                y1={yOf(1)}
                y2={yOf(1)}
                stroke="rgba(148,163,184,0.45)"
                strokeWidth={1}
                strokeDasharray="3 3"
              />
              <motion.line
                x1={xOf(1)}
                y1={yOf(SAFETY_AT_OMEGA_1)}
                x2={xOf(OMEGA_CROSSING)}
                y2={yOf(1)}
                stroke="rgba(251,191,36,0.7)"
                strokeWidth={1.5}
                strokeDasharray="4 3"
                initial={{ opacity: 0 }}
                whileInView={{ opacity: 1 }}
                viewport={{ once: true, amount: 0.5 }}
                transition={{ duration: 0.6 }}
              />
              <circle
                cx={xOf(1)}
                cy={yOf(SAFETY_AT_OMEGA_1)}
                r={3.5}
                fill="#fcd34d"
              />
              <circle cx={xOf(OMEGA_CROSSING)} cy={yOf(1)} r={3.5} fill="#fb7185" />
              <text
                x={xOf(1) + 7}
                y={yOf(SAFETY_AT_OMEGA_1) + 4}
                className="fill-amber-800 font-mono"
                fontSize="9"
              >
                273 @ ω=1
              </text>
              <text
                x={xOf(OMEGA_CROSSING) - 4}
                y={yOf(1) - 6}
                textAnchor="end"
                className="fill-rose-800 font-mono"
                fontSize="9"
              >
                1 @ ω=4.2
              </text>
            </svg>
          </div>
          <p className="font-mono text-[10px] text-slate-600">
            Both endpoints measured; the dashed link is schematic. Two named open
            inequalities remain (hull positivity = transport wall; universal
            λ*-vs-A).
          </p>
        </Door>

        {/* Door C */}
        <Door
          letter="C"
          title="A universal recipe and its named lemma"
          verdict="91/91"
          tone="sky"
          note="The hybrid recipe certifies every nontrivial adversarial Weil direction; cost is window-extensive (λ_m ~ m^{5/2}, Eisenstein law)."
        >
          <Meter label="adversarial directions certified" percent={100} tone="sky" />
          <p className="mt-1.5 font-mono text-[10px] text-sky-800/80">
            Named core: the Matching Lemma on the log lattice — window-proved on
            [4, 10⁶] (939 870 clash atoms, 0 violations, exact margin 0.082159).
          </p>
        </Door>
      </div>

      {/* transport ledger */}
      <div className="mt-3 rounded-xl border border-emerald-400/30 bg-emerald-500/10 p-3">
        <p className="font-mono text-[10px] uppercase tracking-wider text-emerald-700/90">
          Transport ledger closes · Teil 79
        </p>
        <p className="mt-1.5 text-center font-mono text-sm text-emerald-800">
          Q_Weil = Q_cert + Δ_arch + Δ₂
        </p>
        <div className="mt-2 grid grid-cols-3 gap-2 text-center font-mono text-[10px]">
          <span className="rounded-md bg-slate-100/60 px-1 py-1 text-slate-600">
            identity ~7e-16
          </span>
          <span className="rounded-md bg-slate-100/60 px-1 py-1 text-slate-600">
            100/100 rows
          </span>
          <span className="rounded-md bg-slate-100/60 px-1 py-1 text-slate-600">
            Δ_pole ≡ Δ_conv ≡ 0
          </span>
        </div>
        <p className="mt-2 text-xs leading-relaxed text-slate-600">
          What is left is one named inequality I5 (prime↔archimedean coupling),
          typed ⟺ Weil positivity ⟺ RH. Equivalence typing, not progress toward
          proving it.
        </p>
      </div>
    </div>
  );
}

const TONE = {
  rose: {
    box: "border-rose-400/30 bg-rose-500/5",
    badge: "border-rose-400/40 bg-rose-500/15 text-rose-800",
    bar: "bg-rose-400/70",
  },
  amber: {
    box: "border-amber-400/30 bg-amber-500/5",
    badge: "border-amber-400/40 bg-amber-500/15 text-amber-800",
    bar: "bg-amber-400/70",
  },
  sky: {
    box: "border-sky-400/30 bg-sky-500/5",
    badge: "border-sky-400/40 bg-sky-500/15 text-sky-800",
    bar: "bg-sky-400/70",
  },
} as const;

function Door({
  letter,
  title,
  verdict,
  tone,
  note,
  children,
}: {
  letter: string;
  title: string;
  verdict: string;
  tone: keyof typeof TONE;
  note: string;
  children: React.ReactNode;
}) {
  const t = TONE[tone];
  return (
    <motion.div
      initial={{ opacity: 0, y: 8 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.3 }}
      transition={{ duration: 0.35 }}
      className={`rounded-xl border p-3 ${t.box}`}
    >
      <div className="flex flex-wrap items-center gap-2">
        <span
          className={`flex h-6 w-6 items-center justify-center rounded-full border font-mono text-[11px] ${t.badge}`}
        >
          {letter}
        </span>
        <span className="min-w-0 flex-1 font-serif text-base text-slate-900">
          {title}
        </span>
        <span className={`rounded-full border px-2 py-0.5 font-mono text-[9px] uppercase tracking-wider ${t.badge}`}>
          {verdict}
        </span>
      </div>
      <p className="mt-1 text-xs leading-relaxed text-slate-600">{note}</p>
      {children}
    </motion.div>
  );
}

function Meter({
  label,
  percent,
  tone,
}: {
  label: string;
  percent: number;
  tone: keyof typeof TONE;
}) {
  return (
    <div className="mt-2">
      <div className="flex items-baseline justify-between font-mono text-[10px] text-slate-600">
        <span>{label}</span>
        <span>{percent}%</span>
      </div>
      <div className="mt-1 h-1.5 overflow-hidden rounded-full bg-slate-200">
        <motion.div
          className={`h-full rounded-full ${TONE[tone].bar}`}
          initial={{ width: 0 }}
          whileInView={{ width: `${percent}%` }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ duration: 0.7, ease: "easeOut" }}
        />
      </div>
    </div>
  );
}
