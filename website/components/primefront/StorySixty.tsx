import type { ReactNode } from "react";

/**
 * "The story in 60 seconds" — five pictogram steps a first-time visitor can
 * scan before any detail arrives. Server component: no client JS, no motion.
 * Status labels are honest: only step 4 is a machine-verified theorem; the
 * last step is explicitly open.
 */

type StepTone = "classical" | "measured" | "theorem" | "open";

const TONE: Record<
  StepTone,
  { label: string; chip: string; icon: string; ring: string }
> = {
  classical: {
    label: "classical",
    chip: "border-slate-500/40 bg-slate-500/10 text-slate-700",
    icon: "text-slate-700",
    ring: "border-slate-400/50",
  },
  measured: {
    label: "measured",
    chip: "border-sky-400/40 bg-sky-500/10 text-sky-800",
    icon: "text-sky-700",
    ring: "border-sky-500/40",
  },
  theorem: {
    label: "theorem · machine-verified",
    chip: "border-emerald-400/40 bg-emerald-500/10 text-emerald-800",
    icon: "text-emerald-700",
    ring: "border-emerald-500/40",
  },
  open: {
    label: "open",
    chip: "border-amber-400/40 bg-amber-500/10 text-amber-800",
    icon: "text-amber-700",
    ring: "border-amber-500/40",
  },
};

function StepIcon({ kind }: { kind: string }): ReactNode {
  const common = {
    viewBox: "0 0 32 32",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: 1.6,
    strokeLinecap: "round" as const,
    strokeLinejoin: "round" as const,
    className: "h-8 w-8",
    "aria-hidden": true,
  };
  switch (kind) {
    case "primes":
      // number line with irregular prime ticks
      return (
        <svg {...common}>
          <path d="M2 22h28" />
          <path d="M5 22v-7M8 22v-9M13 22v-8M18 22v-10M25 22v-9" />
          <circle cx="5" cy="12" r="1.2" fill="currentColor" stroke="none" />
          <circle cx="8" cy="10" r="1.2" fill="currentColor" stroke="none" />
          <circle cx="13" cy="11" r="1.2" fill="currentColor" stroke="none" />
          <circle cx="18" cy="9" r="1.2" fill="currentColor" stroke="none" />
          <circle cx="25" cy="10" r="1.2" fill="currentColor" stroke="none" />
        </svg>
      );
    case "formula":
      // two sides of one identity, linked
      return (
        <svg {...common}>
          <rect x="3" y="8" width="10" height="16" rx="2" />
          <rect x="19" y="8" width="10" height="16" rx="2" />
          <path d="M13 14h6M13 18h6" />
        </svg>
      );
    case "window":
      // a finite window matrix
      return (
        <svg {...common}>
          <rect x="5" y="5" width="22" height="22" rx="2" />
          <path d="M5 12.3h22M5 19.6h22M12.3 5v22M19.6 5v22" />
        </svg>
      );
    case "equals":
      // the identification
      return (
        <svg {...common}>
          <circle cx="16" cy="16" r="12" />
          <path d="M10.5 13h11M10.5 19h11" />
        </svg>
      );
    case "gap":
      // one open inequality — a gap in the arc
      return (
        <svg {...common}>
          <path d="M27.2 12.5A12 12 0 1 0 28 16" />
          <path d="M23 7l6 6M29 7l-6 6" strokeWidth={1.3} />
        </svg>
      );
    default:
      return null;
  }
}

const STEPS: readonly {
  icon: string;
  tone: StepTone;
  title: string;
  text: ReactNode;
}[] = [
  {
    icon: "primes",
    tone: "classical",
    title: "Primes",
    text: (
      <>
        Prime numbers look random. The Riemann Hypothesis asks whether a
        hidden spectrum orders them.
      </>
    ),
  },
  {
    icon: "formula",
    tone: "classical",
    title: "The explicit formula",
    text: (
      <>
        A classical identity (Weil) turns that question into one quantity,
        built prime by prime, that must never go negative.
      </>
    ),
  },
  {
    icon: "window",
    tone: "measured",
    title: "The window form",
    text: (
      <>
        TFPT&apos;s lattice bookkeeping produces exactly that quantity on
        finite windows — a matrix built from primes, tested window by window.
      </>
    ),
  },
  {
    icon: "equals",
    tone: "theorem",
    title: "= Suzuki's operator",
    text: (
      <>
        That window matrix <em>is</em>{" "}
        the matrix of Suzuki&apos;s Weil
        operator — proved as a machine-verified theorem (v643), after a
        same-day erratum.
      </>
    ),
  },
  {
    icon: "gap",
    tone: "open",
    title: "One open inequality",
    text: (
      <>
        Everything RH-hard now sits in one open positivity statement (W3).
        It is open — and no progress toward RH is claimed.
      </>
    ),
  },
];

export function StorySixty() {
  return (
    <section
      aria-label="The story in 60 seconds"
      className="mt-10 rounded-2xl border border-slate-300/50 bg-slate-50/60 p-5 sm:p-6"
    >
      <p className="font-mono text-[10px] font-semibold uppercase tracking-[0.2em] text-sky-700">
        The story in 60 seconds
      </p>
      <ol className="mt-4 grid gap-4 sm:grid-cols-2 lg:grid-cols-5">
        {STEPS.map((s, i) => {
          const tone = TONE[s.tone];
          return (
            <li key={s.title} className="relative flex flex-col">
              <div
                className={`flex h-14 w-14 items-center justify-center rounded-xl border bg-slate-100/60 ${tone.ring} ${tone.icon}`}
              >
                <StepIcon kind={s.icon} />
              </div>
              {i < STEPS.length - 1 && (
                <span
                  aria-hidden
                  className="absolute left-[64px] top-[27px] hidden h-px w-[calc(100%-76px)] bg-gradient-to-r from-slate-400/60 to-transparent lg:block"
                />
              )}
              <p className="mt-3 flex flex-wrap items-center gap-x-2 gap-y-1">
                <span className="font-serif text-[15px] font-semibold leading-snug text-slate-900">
                  <span className="mr-1.5 font-mono text-[11px] text-slate-600">
                    {i + 1}
                  </span>
                  {s.title}
                </span>
              </p>
              <span
                className={`mt-1 w-fit rounded-full border px-2 py-px font-mono text-[9px] uppercase tracking-wider ${tone.chip}`}
              >
                {tone.label}
              </span>
              <p className="mt-2 text-[13px] leading-relaxed text-slate-600">
                {s.text}
              </p>
            </li>
          );
        })}
      </ol>
      <p className="mt-4 border-t border-slate-200/60 pt-3 text-xs leading-relaxed text-slate-600">
        Steps 1–2 are classical mathematics. Step 3 is measured inside the
        suite; step 4 is machine-verified (v535–v648, all green); step 5 is
        honestly open. Everything below tells this story in full detail.
      </p>
    </section>
  );
}
