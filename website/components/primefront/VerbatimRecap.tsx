"use client";

import { useState, type ComponentType } from "react";

/**
 * Collapsed expander for the page's very long "preserved verbatim" recap
 * paragraphs. The texts live in `verbatimRecaps.tsx`, which is loaded with
 * a dynamic import() on first expand — so the ~160 KB of historical status
 * prose stays out of the server-rendered HTML and the route's first-load
 * JavaScript while remaining one click away, word for word.
 */
const RECAPS = {
  sprintPhase2: () =>
    import("./verbatimRecaps").then((m) => m.SprintPhase2Recap),
  seriesEnd: () => import("./verbatimRecaps").then((m) => m.SeriesEndRecap),
  nearLevel: () => import("./verbatimRecaps").then((m) => m.NearLevelRecap),
  phase2FullProof: () =>
    import("./verbatimRecaps").then((m) => m.Phase2FullProofRecap),
} as const;

export type VerbatimRecapId = keyof typeof RECAPS;

const TONES = {
  slate: "text-slate-600 hover:text-slate-800",
  amber: "text-amber-700/80 hover:text-amber-800",
} as const;

export function VerbatimRecap({
  id,
  label,
  tone = "slate",
  className,
}: {
  id: VerbatimRecapId;
  label: string;
  tone?: keyof typeof TONES;
  className?: string;
}) {
  const [open, setOpen] = useState(false);
  const [Recap, setRecap] = useState<ComponentType | null>(null);
  const [failed, setFailed] = useState(false);
  const regionId = `verbatim-recap-${id}`;

  const toggle = () => {
    const next = !open;
    setOpen(next);
    if (next && !Recap) {
      setFailed(false);
      RECAPS[id]()
        .then((C) => setRecap(() => C))
        .catch(() => setFailed(true));
    }
  };

  return (
    <div className={className}>
      <button
        type="button"
        onClick={toggle}
        aria-expanded={open}
        aria-controls={regionId}
        className={`inline-flex items-baseline gap-1.5 text-left font-mono text-[11px] uppercase tracking-[0.18em] transition-colors motion-reduce:transition-none ${TONES[tone]}`}
      >
        <span
          aria-hidden
          className={`inline-block transition-transform motion-reduce:transition-none ${
            open ? "rotate-90" : ""
          }`}
        >
          ▸
        </span>
        {label}
      </button>
      {open && (
        <div id={regionId}>
          {failed ? (
            <p className="mt-3 font-mono text-[11px] text-rose-700/80">
              The preserved text could not be loaded — please try again.
            </p>
          ) : Recap ? (
            <Recap />
          ) : (
            <p className="mt-3 font-mono text-[11px] text-slate-600">
              Loading the preserved text…
            </p>
          )}
        </div>
      )}
    </div>
  );
}
