import { pageMetadata } from "@/lib/seo";
import type { Metadata } from "next";
import Link from "next/link";
import { ArrowLeft, ArrowUpRight } from "lucide-react";
import { SectionHeader } from "@/components/SectionHeader";
import { FAQ_ITEMS } from "@/lib/faq";
import { SITE_VERSION } from "@/lib/version";
import { REPO_URL, SITE_URL } from "@/lib/utils";

export const metadata: Metadata = pageMetadata("/objections");

type Status = "Answered" | "Conditional" | "Open";

const STATUS_META: Record<Status, { tone: string }> = {
  Answered: { tone: "bg-emerald-500/15 text-emerald-800 ring-emerald-400/30" },
  Conditional: { tone: "bg-amber-500/15 text-amber-800 ring-amber-400/30" },
  Open: { tone: "bg-rose-500/15 text-rose-800 ring-rose-400/30" },
};

/**
 * Status classification for each FAQ objection, in the same order as
 * lib/faq.ts (the single source for the objection text itself — the short
 * answer below is derived from it). The classification only types where each
 * answer already lands; it introduces no new claim.
 */
const META: { status: Status; where: string; whereHref: string; stillOpen: string }[] = [
  { status: "Answered", where: "FAQ · Doc 1", whereHref: "/faq", stillOpen: "No" },
  { status: "Answered", where: "FAQ · Verification", whereHref: "/verification", stillOpen: "No" },
  { status: "Conditional", where: "FAQ · Open gates", whereHref: "/verification#open-gates", stillOpen: "Conditional layer (declared)" },
  { status: "Answered", where: "FAQ · Verification", whereHref: "/verification", stillOpen: "No (conditional ≤ 10⁻³⁰·⁷; unconditional ≈ 4.40σ, v436)" },
  { status: "Answered", where: "Falsification", whereHref: "/falsification", stillOpen: "By design" },
  { status: "Open", where: "Open gates · Research contracts", whereHref: "/verification#open-gates", stillOpen: "Yes — 3 named interfaces" },
  { status: "Answered", where: "FAQ · α comparator", whereHref: "/faq", stillOpen: "No" },
];

/**
 * A concise ledger summary derived from the full FAQ answer: the leading
 * sentence(s), capped at ~200 characters. A sentence boundary is `.`/`!`/`?`
 * followed by whitespace + a capital letter (or end of string), so periods
 * inside decimals ("137.0359992168") or dotted tokens ("QGEO.SYM.01") never
 * split, and a bare one-word opener like "No." is extended into the next
 * sentence rather than shown alone.
 */
function shortAnswer(a: string): string {
  const MIN_LEN = 24;
  const MAX_LEN = 200;
  const boundary = /[.!?](?=\s+[A-Z(]|\s*$)/g;

  let cut = a.length;
  let m: RegExpExecArray | null;
  while ((m = boundary.exec(a)) !== null) {
    const end = m.index + 1;
    if (end >= MIN_LEN) {
      cut = end;
      break;
    }
  }

  const s = a.slice(0, cut).trim();
  if (s.length > MAX_LEN) {
    return s.slice(0, MAX_LEN).replace(/\s+\S*$/, "").trimEnd() + "…";
  }
  return s;
}

const ROWS = FAQ_ITEMS.map((item, i) => ({
  objection: item.q,
  answer: shortAnswer(item.a),
  ...(META[i] ?? {
    status: "Answered" as Status,
    where: "FAQ",
    whereHref: "/faq",
    stillOpen: "No",
  }),
}));

export default function ObjectionsPage() {
  return (
    <>
      <section className="relative isolate overflow-hidden pt-12 pb-8 sm:pt-16">
        <div aria-hidden className="absolute inset-0 grid-bg pointer-events-none" />
        <div
          aria-hidden
          className="absolute -top-40 left-1/2 -z-10 h-[500px] w-[1000px] -translate-x-1/2 rounded-full opacity-30 blur-3xl"
          style={{
            background:
              "radial-gradient(closest-side, rgba(168,85,247,0.35), rgba(99,102,241,0.2), transparent)",
          }}
        />
        <div className="relative mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
          <nav aria-label="Breadcrumb" className="mb-6">
            <Link
              prefetch={false}
              href="/"
              className="inline-flex items-center gap-1.5 text-sm text-slate-600 transition-colors hover:text-slate-800"
            >
              <ArrowLeft size={14} />
              Back to overview
            </Link>
          </nav>
          <span className="inline-flex items-center gap-2 rounded-full border border-violet-400/20 bg-violet-500/10 px-4 py-1.5 text-xs font-medium tracking-wider text-violet-800">
            <span className="uppercase">Public objection ledger</span>
          </span>
          <h1 className="mt-6 font-serif text-4xl font-semibold leading-tight text-slate-950 sm:text-5xl md:text-6xl">
            The sharpest <span className="text-gradient-blue">objections</span>, tracked.
          </h1>
          <p className="mt-4 max-w-2xl text-base leading-relaxed text-slate-700 sm:text-lg">
            A ledger, not a brochure: every recurring objection with its answer
            status, where it is addressed, and whether anything stays open. The
            full answers live in the hostile-referee FAQ; disagreements belong in
            the issue tracker.
          </p>
        </div>
      </section>

      <section
        id="ledger"
        className="relative scroll-mt-20 py-8 sm:py-12"
        aria-labelledby="ledger-heading"
      >
        <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
          <SectionHeader
            id="ledger-heading"
            eyebrow="The ledger"
            title="Objection · status · where · still open?"
            description="Each row links to where the objection is addressed in depth. Status is honest: most are answered, the parameter question is conditional on the declared layer, and the residual is genuinely open."
          />

          <div className="mt-8 overflow-hidden rounded-2xl border border-slate-300/40">
            <div className="overflow-x-auto formula-scroll">
              <table className="w-full min-w-[860px] border-separate border-spacing-0 text-left text-sm">
                <thead>
                  <tr>
                    {["Objection", "Short answer", "Status", "Where", "Still open?"].map((h) => (
                      <th
                        key={h}
                        scope="col"
                        className="border-b border-slate-200/60 bg-slate-50/60 px-4 py-3 text-[10px] font-semibold uppercase tracking-widest text-slate-700"
                      >
                        {h}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {ROWS.map((row) => (
                    <tr key={row.objection} className="hover:bg-slate-100/30">
                      <td className="border-b border-slate-200/60 px-4 py-3 align-top text-xs font-semibold leading-relaxed text-slate-900">
                        {row.objection}
                      </td>
                      <td className="border-b border-slate-200/60 px-4 py-3 align-top text-xs leading-relaxed text-slate-700">
                        {row.answer}
                      </td>
                      <td className="border-b border-slate-200/60 px-4 py-3 align-top">
                        <span
                          className={`inline-block rounded-full px-2.5 py-0.5 text-[10px] font-semibold uppercase tracking-wider ring-1 ${STATUS_META[row.status].tone}`}
                        >
                          {row.status}
                        </span>
                      </td>
                      <td className="border-b border-slate-200/60 px-4 py-3 align-top text-xs">
                        <Link
                          prefetch={false}
                          href={row.whereHref}
                          className="font-semibold text-blue-700 transition-colors hover:text-blue-800"
                        >
                          {row.where}
                        </Link>
                      </td>
                      <td className="border-b border-slate-200/60 px-4 py-3 align-top text-xs leading-relaxed text-slate-700">
                        {row.stillOpen}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          <div className="mt-6 flex flex-wrap gap-3">
            <Link
              prefetch={false}
              href="/faq"
              className="inline-flex items-center gap-2 rounded-full bg-blue-700 px-5 py-2.5 text-sm font-semibold text-white shadow-lg shadow-blue-500/20 transition-transform hover:scale-105"
            >
              Full answers — hostile-referee FAQ
            </Link>
            <Link
              prefetch={false}
              href={`${REPO_URL}/issues`}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 rounded-full border border-slate-400/60 bg-slate-100/60 px-5 py-2.5 text-sm font-semibold text-slate-900 transition-colors hover:bg-slate-200/80"
            >
              Raise a new objection
              <ArrowUpRight size={14} aria-hidden />
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
