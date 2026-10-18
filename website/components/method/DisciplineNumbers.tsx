import { DISCIPLINE } from "@/lib/discipline";

/**
 * The measured discipline numbers (D1–D6 of META.DISCIPLINE.01), rendered
 * from the generated lib/discipline.ts — no hand-maintained figures. Each
 * card names the census it comes from; v649 re-certifies the bars on every
 * suite run.
 */

const fmt = (n: number) => n.toLocaleString("en-US");

export function DisciplineNumbers() {
  const d = DISCIPLINE;
  const cards: { value: string; label: string; note: string }[] = [
    {
      value: fmt(d.suite.modules),
      label: "verification modules",
      note: "one file per claim cluster; every module carries checks",
    },
    {
      value: fmt(d.suite.checkSites),
      label: "machine checks (static call sites)",
      note: "python3 verification/run_all.py replays all of them",
    },
    {
      value: fmt(d.suite.mustfailOccurrences),
      label: "must-fail / negative controls",
      note: `across ${fmt(d.suite.mustfailModules)} modules — scrambles, kill tests, controls that must break`,
    },
    {
      value: fmt(d.ledger.killRows),
      label: "documented kills & honest negatives",
      note: `ledger rows recording killed, retyped or ill-posed hypotheses (of ${fmt(d.ledger.rows)} total)`,
    },
    {
      value: `${fmt(d.contracts.ledgerRows)} / ${fmt(d.contracts.withKillCriteria)}`,
      label: "research contracts / with kill criteria",
      note: "preregistered lemma chains; kill criteria named before execution",
    },
    {
      value: `${d.replay.passed}/${d.replay.total}`,
      label: "deterministic replay sample",
      note: "declared modules run twice — identical output (v55…v648, incl. v634/v643/v648)",
    },
    {
      value: fmt(d.lean.modules),
      label: "Lean 4 proof modules",
      note: "committed formal certificates (git ls-files; no sorry)",
    },
    {
      value: fmt(d.anchors.recomputed),
      label: "classical anchors recomputed",
      note: "Jacobi · Construction A · Shephard–Todd · Suzuki · completed-ζ, checked against the literature",
    },
  ];

  return (
    <div>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {cards.map((c) => (
          <div
            key={c.label}
            className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-5"
          >
            <div className="font-mono text-3xl font-semibold tracking-tight text-slate-950">
              {c.value}
            </div>
            <div className="mt-1.5 text-sm font-semibold text-slate-800">
              {c.label}
            </div>
            <p className="mt-1.5 text-xs leading-relaxed text-slate-600">
              {c.note}
            </p>
          </div>
        ))}
      </div>
      <p className="mt-4 text-xs leading-relaxed text-slate-600">
        Every number on this page is generated from the repository by{" "}
        <code className="text-slate-600">
          verification/make_discipline_stats.py
        </code>{" "}
        and certified as frozen minimum bars by{" "}
        <code className="text-slate-600">v649_discipline_audit.py</code>{" "}
        (claim <code className="text-slate-600">META.DISCIPLINE.01</code>) on
        every suite run. Nothing here is typed in by hand.
      </p>
    </div>
  );
}
