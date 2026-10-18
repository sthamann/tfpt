import type { ReactNode } from "react";

/**
 * "Where we are" — a compact three-card status strip (PROVEN / MEASURED /
 * OPEN) so a first-time visitor sees the honest state of the programme
 * before any detail. Server component: no client JS.
 */

function CardIcon({ kind }: { kind: "proven" | "measured" | "open" }): ReactNode {
  const common = {
    viewBox: "0 0 24 24",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: 1.8,
    strokeLinecap: "round" as const,
    strokeLinejoin: "round" as const,
    className: "h-5 w-5",
    "aria-hidden": true,
  };
  switch (kind) {
    case "proven":
      return (
        <svg {...common}>
          <path d="M4 12.5l5 5L20 6.5" />
        </svg>
      );
    case "measured":
      return (
        <svg {...common}>
          <path d="M3 17L17 3l4 4L7 21l-4-4z" />
          <path d="M8 12l1.5 1.5M11 9l1.5 1.5M14 6l1.5 1.5" />
        </svg>
      );
    case "open":
      return (
        <svg {...common}>
          <circle cx="12" cy="12" r="9" strokeDasharray="4 3" />
          <path d="M12 8v5" />
          <circle cx="12" cy="16.2" r="0.4" fill="currentColor" stroke="none" />
        </svg>
      );
  }
}

const CARDS: readonly {
  kind: "proven" | "measured" | "open";
  marker: string;
  border: string;
  chip: string;
  title: string;
  body: ReactNode;
}[] = [
  {
    kind: "proven",
    marker: "PROVEN",
    border: "border-emerald-500/35",
    chip: "border-emerald-400/40 bg-emerald-500/10 text-emerald-800",
    title: "W1 — the identification theorem",
    body: (
      <>
        The TFPT window form <em>is</em>{" "}
        Suzuki&apos;s localized Weil
        operator: a measure-level theorem, machine-verified (v643) after a
        same-day erratum. The dictionary is one scalar, +1/D, with κ = 0
        exactly.
      </>
    ),
  },
  {
    kind: "measured",
    marker: "MEASURED",
    border: "border-sky-500/35",
    chip: "border-sky-400/40 bg-sky-500/10 text-sky-800",
    title: "C = 1 and the chamber",
    body: (
      <>
        The uniform constant C = 1 holds exception-free on all 67 complete
        windows (v618/v619), and every window lands in one Hodge chamber of
        the cover lattice (v627). Measured surfaces — not uniformity proofs.
      </>
    ),
  },
  {
    kind: "open",
    marker: "OPEN",
    border: "border-amber-500/35",
    chip: "border-amber-400/40 bg-amber-500/10 text-amber-800",
    title: "W2 / W3 — the RH-hard part",
    body: (
      <>
        W2 is started, not closed (v644). W3 — uniform positivity, the
        RH-hard step — is open, and closing W1 did not move it. No claim of
        progress toward the Riemann Hypothesis.
      </>
    ),
  },
];

export function WhereWeAre() {
  return (
    <section
      aria-label="Where the programme stands"
      className="mt-6 grid gap-3 sm:grid-cols-3"
    >
      {CARDS.map((c) => (
        <div
          key={c.marker}
          className={`rounded-2xl border bg-slate-50/60 p-4 sm:p-5 ${c.border}`}
        >
          <div className="flex items-center gap-2">
            <span
              className={`inline-flex items-center gap-1.5 rounded-full border px-2.5 py-0.5 font-mono text-[10px] font-semibold uppercase tracking-[0.14em] ${c.chip}`}
            >
              <CardIcon kind={c.kind} />
              {c.marker}
            </span>
          </div>
          <h3 className="mt-3 font-serif text-base font-semibold leading-snug text-slate-900">
            {c.title}
          </h3>
          <p className="mt-1.5 text-[13px] leading-relaxed text-slate-600">
            {c.body}
          </p>
        </div>
      ))}
    </section>
  );
}
