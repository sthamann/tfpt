import { DISCIPLINE } from "@/lib/discipline";

/**
 * The four public status classes and the measured ledger distribution —
 * rendered from the generated discipline stats. The honest headline is that
 * typed-open rows outnumber established ones: statuses are earned, not
 * assumed.
 */

const CLASSES: {
  key: "E" | "C" | "O" | "X";
  label: string;
  desc: string;
  bar: string;
  chip: string;
}[] = [
  {
    key: "E",
    label: "[E] established",
    desc: "Machine-verified exact: identities, lattice facts, formal results, audited numerics. The only class that carries load.",
    bar: "bg-emerald-400/80",
    chip: "text-emerald-800 bg-emerald-500/10 ring-emerald-400/30",
  },
  {
    key: "C",
    label: "[C] conditional",
    desc: "Typed readings and physical identifications — observations that stay observations until a mechanism is proven. Never silently upgraded.",
    bar: "bg-amber-400/80",
    chip: "text-amber-800 bg-amber-500/10 ring-amber-400/30",
  },
  {
    key: "O",
    label: "[O] open",
    desc: "Open gates, premises and research contracts — stated in public with their kill criteria, not hidden in an appendix.",
    bar: "bg-rose-400/80",
    chip: "text-rose-800 bg-rose-500/10 ring-rose-400/30",
  },
  {
    key: "X",
    label: "[X] killed",
    desc: "Falsified or refuted readings, kept in view so they cannot be re-fished. The graveyard above is their showcase.",
    bar: "bg-slate-500/80",
    chip: "text-slate-700 bg-slate-500/10 ring-slate-600/30",
  },
];

export function StatusTypology() {
  const dist = DISCIPLINE.ledger.dist;
  const total = dist.E + dist.C + dist.O + dist.X;
  const pct = (n: number) => (100 * n) / total;

  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-5 sm:p-6">
      <div className="grid gap-5 md:grid-cols-2">
        {CLASSES.map((c) => (
          <div key={c.key} className="flex items-start gap-3">
            <span
              className={`mt-0.5 shrink-0 rounded-full px-2.5 py-0.5 font-mono text-[11px] font-semibold ring-1 ${c.chip}`}
            >
              {c.label}
            </span>
            <p className="text-sm leading-relaxed text-slate-600">{c.desc}</p>
          </div>
        ))}
      </div>

      <div className="mt-6">
        <div className="mb-2 flex items-baseline justify-between">
          <span className="font-mono text-[11px] font-semibold uppercase tracking-widest text-slate-600">
            Measured ledger distribution
          </span>
          <span className="font-mono text-[11px] text-slate-600">
            {total.toLocaleString("en-US")} classified rows (+
            {DISCIPLINE.ledger.dist.AXIOM} declared axioms)
          </span>
        </div>
        <div
          className="flex h-4 w-full overflow-hidden rounded-full ring-1 ring-slate-300/60"
          role="img"
          aria-label={`Ledger status distribution: ${dist.E} established, ${dist.C} conditional, ${dist.O} open, ${dist.X} killed.`}
        >
          {CLASSES.map((c) => (
            <div
              key={c.key}
              className={c.bar}
              style={{ width: `${pct(dist[c.key])}%` }}
            />
          ))}
        </div>
        <div className="mt-2 flex flex-wrap gap-x-5 gap-y-1 font-mono text-[11px] text-slate-600">
          {CLASSES.map((c) => (
            <span key={c.key}>
              {c.label.slice(0, 3)} {dist[c.key]} ·{" "}
              {pct(dist[c.key]).toFixed(0)}%
            </span>
          ))}
        </div>
        <p className="mt-3 text-xs leading-relaxed text-slate-600">
          More rows are typed open or conditional than established — the
          grading is earned per claim, decided by one versioned ledger, and a
          status can only move with new machine evidence.
        </p>
      </div>
    </div>
  );
}
