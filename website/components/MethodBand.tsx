import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { DISCIPLINE } from "@/lib/discipline";

const fmt = (n: number) => n.toLocaleString("en-US");

/**
 * Compact pointer band to /method — three measured discipline numbers
 * (generated from the suite, certified by v649) and the one-line claim.
 */
export function MethodBand() {
  const stats = [
    {
      value: fmt(DISCIPLINE.ledger.killRows),
      label: "documented kills & honest negatives",
    },
    {
      value: fmt(DISCIPLINE.suite.mustfailOccurrences),
      label: "must-fail / negative controls",
    },
    {
      value: `${DISCIPLINE.replay.passed}/${DISCIPLINE.replay.total}`,
      label: "deterministic replay sample",
    },
  ];

  return (
    <section
      id="method-band"
      aria-labelledby="method-band-heading"
      className="relative scroll-mt-20 py-10 sm:py-12"
    >
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <div className="rounded-2xl border border-emerald-400/20 bg-gradient-to-br from-emerald-500/[0.07] via-slate-50/70 to-slate-50/90 p-5 sm:p-6">
          <div className="flex flex-col gap-5 lg:flex-row lg:items-center lg:justify-between">
            <div className="min-w-0">
              <p className="font-mono text-[10px] font-semibold uppercase tracking-[0.2em] text-emerald-700">
                Method
              </p>
              <h2
                id="method-band-heading"
                className="mt-1.5 font-serif text-lg font-semibold text-slate-950 sm:text-xl"
              >
                How we keep ourselves honest
              </h2>
              <p className="mt-1 max-w-xl text-sm leading-relaxed text-slate-600">
                Sandbox firewall, kill criteria before execution, one ledger,
                generated mirrors — and the process discipline itself measured
                and certified by the suite (v649). The numbers are censuses,
                not slogans.
              </p>
            </div>
            <div className="flex shrink-0 flex-col gap-4 sm:flex-row sm:items-center">
              <dl className="flex gap-6">
                {stats.map((s) => (
                  <div key={s.label} className="min-w-0">
                    <dt className="sr-only">{s.label}</dt>
                    <dd className="font-mono text-2xl font-semibold text-slate-950">
                      {s.value}
                    </dd>
                    <dd className="mt-0.5 max-w-[9rem] text-[11px] leading-snug text-slate-600">
                      {s.label}
                    </dd>
                  </div>
                ))}
              </dl>
              <Link
                prefetch={false}
                href="/method"
                className="inline-flex items-center gap-1.5 self-start whitespace-nowrap rounded-full border border-emerald-400/30 bg-emerald-500/10 px-4 py-2 text-sm font-semibold text-emerald-800 transition-colors hover:bg-emerald-500/20 hover:text-emerald-800 sm:self-center"
              >
                The verification framework
                <ArrowRight size={14} aria-hidden />
              </Link>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
