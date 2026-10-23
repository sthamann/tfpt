import type { Metadata } from "next";
import Link from "next/link";
import { papers, STATUS_META, paperLabel } from "@/lib/papers";
import { getReleaseAsset, formatBytes } from "@/lib/release";
import { collectionJsonLd } from "@/lib/structured-data";
import { pageMetadata, PAPER_SEARCH } from "@/lib/seo";

export const metadata: Metadata = pageMetadata("/papers");

export default function PapersIndexPage() {
  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(collectionJsonLd).replace(/</g, "\\u003c") }} />
      <section className="mx-auto max-w-6xl px-4 py-12 sm:px-6 sm:py-16 lg:px-8" aria-labelledby="papers-heading">
        <nav aria-label="Breadcrumb" className="mb-6 text-sm text-slate-600"><Link href="/">TFPT</Link> / Papers</nav>
        <p className="text-sm font-semibold uppercase tracking-wider text-blue-700">Research library</p>
        <h1 id="papers-heading" className="mt-4 font-serif text-4xl font-semibold text-slate-950 sm:text-5xl">TFPT research papers</h1>
        <p className="mt-5 max-w-3xl text-lg leading-relaxed text-slate-700">
          Topological Fixed-Point Theory studies how two starting assumptions connect to E₈,
          Standard Model structure and the fine-structure constant. These papers by Stefan Hamann
          and Alessandro Rizzo document the construction, its checks and the physical interfaces that remain open.
        </p>
        <p className="mt-4 max-w-3xl leading-relaxed text-slate-600">
          Start with the <a className="text-blue-800 underline" href="/papers/introduction_guide.pdf">compact reading guide</a>,
          then choose a topic below. Each paper page provides its abstract, assumptions, contribution,
          limits and citation details. The <Link className="text-blue-800 underline" href="/documentation">document library</Link> connects topics to original sources.
        </p>
        <div className="mt-10 grid gap-5 md:grid-cols-2">
          {papers.map((paper) => {
            const release = getReleaseAsset(paper.pdf);
            return (
              <article key={paper.id} className="flex flex-col rounded-xl border border-slate-200 bg-white p-6">
                <p className="text-xs font-medium text-slate-600">{paperLabel(paper)} · {STATUS_META[paper.status].label}</p>
                <h2 className="mt-3 font-serif text-2xl font-semibold leading-tight text-slate-950">
                  <Link href={`/papers/${paper.slug}`} prefetch={false} className="hover:text-blue-800">{PAPER_SEARCH[paper.slug]?.[0] ?? paper.title}</Link>
                </h2>
                <p className="mt-3 flex-1 text-sm leading-relaxed text-slate-700">{PAPER_SEARCH[paper.slug]?.[1] ?? paper.subtitle}</p>
                <div className="mt-5 flex flex-wrap gap-x-5 gap-y-2 text-sm font-semibold text-blue-800">
                  <Link href={`/papers/${paper.slug}`} prefetch={false}>Read abstract and evidence →</Link>
                  <a href={paper.pdf}>Full PDF{release ? ` (${formatBytes(release.bytes)})` : ""}</a>
                </div>
                {release && <p className="mt-3 text-xs text-slate-500">Release {release.releaseDate} · {release.version}</p>}
              </article>
            );
          })}
        </div>
        <aside className="mt-10 rounded-xl border border-slate-200 bg-slate-50 p-6" aria-labelledby="references-heading">
          <h2 id="references-heading" className="font-serif text-2xl font-semibold text-slate-950">Reference volumes and research status</h2>
          <p className="mt-3 leading-relaxed text-slate-700">The <a href="/papers/verification_catalog.pdf" className="text-blue-800 underline">verification catalog</a> lists the registered checks.
            The <Link href="/changelog" className="text-blue-800 underline">dated changelog</Link> records the publication history.
            Use <Link href="/verification" className="text-blue-800 underline">verification</Link> to reproduce calculations and <Link href="/falsification" className="text-blue-800 underline">falsification</Link> to inspect tests and failure criteria.</p>
        </aside>
      </section>
    </>
  );
}
