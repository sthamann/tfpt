import type { Metadata } from "next";
import Link from "next/link";
import { readFileSync } from "node:fs";
import path from "node:path";
import { ArrowRight, BookOpen, Download, FileCode2, Network } from "lucide-react";
import { REPO_URL, SITE_URL } from "@/lib/utils";

export const dynamic = "force-static";
export const metadata: Metadata = {
  title: "Document library and source registry",
  description: "Find TFPT topics, modular LaTeX sources, verification scripts, and explicit Lean and Wolfram references in one documented source registry.",
  alternates: { canonical: `${SITE_URL}/documentation` },
};

type Document = { id: string; entry_point: string; canonical_source: string; role: string; title: string; topic_ids?: string[]; ordered_section_ids: string[] };
type Topic = { id: string; title: string };
type Registry = { documents: Document[]; topics: Topic[]; sources: unknown[]; sections: unknown[]; reverse_indexes: { by_topic?: Record<string, unknown[]> } };

export default function DocumentationPage() {
  const registry: Registry = JSON.parse(readFileSync(path.join(process.cwd(), "public/documentation/registry.json"), "utf8"));
  const active = registry.documents.filter((document) => document.role === "active");
  return (
    <div className="mx-auto max-w-7xl px-4 py-16 sm:px-6 lg:px-8">
      <div className="max-w-3xl">
        <p className="text-sm font-semibold uppercase tracking-widest text-blue-700">TFPT document library</p>
        <h1 className="mt-4 font-serif text-4xl font-semibold tracking-tight text-slate-950 sm:text-5xl">Find the argument. Follow its sources.</h1>
        <p className="mt-6 text-lg leading-relaxed text-slate-600">Read a compact guide, open a particular document, or trace a topic to the LaTeX module and verification sources that discuss it.</p>
      </div>
      <section aria-labelledby="reading-editions" className="mt-12 grid gap-5 md:grid-cols-3">
        <h2 id="reading-editions" className="sr-only">Reading editions</h2>
        {[
          { title: "Compact reading guide", href: "/papers/introduction_guide.pdf", icon: BookOpen, description: "The introduction’s core chapters, with its computational reference appendix and dated history available separately." },
          { title: "Verification catalog", href: "/papers/verification_catalog.pdf", icon: Network, description: "The complete registered module index as a separate reference volume. Descriptions retain their stated scope." },
          { title: "Complete document set", href: "/papers", icon: Download, description: "The original complete PDFs, research contracts and publication history remain available under their established names." },
        ].map(({ title, href, icon: Icon, description }) => (
          <Link key={href} href={href} prefetch={false} className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition hover:border-blue-300 hover:shadow-md">
            <Icon size={25} className="text-blue-700" aria-hidden />
            <h3 className="mt-5 font-serif text-xl font-semibold text-slate-950">{title}</h3>
            <p className="mt-3 text-sm leading-relaxed text-slate-600">{description}</p>
            <span className="mt-5 inline-flex items-center gap-2 text-sm font-semibold text-blue-700">Open <ArrowRight size={15} aria-hidden /></span>
          </Link>
        ))}
      </section>
      <section aria-labelledby="registry-heading" className="mt-16 rounded-2xl border border-slate-200 bg-slate-50 p-6 sm:p-8">
        <h2 id="registry-heading" className="font-serif text-2xl font-semibold text-slate-950">One source registry</h2>
        <p className="mt-4 max-w-4xl leading-relaxed text-slate-600">The registry inventories {registry.sources.length} authored LaTeX source files, {registry.documents.length} document entry points and {registry.sections.length} section records. It connects physical source locations, topics, Python checks, ledger claims, and explicit Lean or Wolfram references. Historical and generated material is identified separately.</p>
        <p className="mt-3 max-w-4xl text-sm leading-relaxed text-slate-600">A citation identifies a source; it does not establish that source’s mathematical or physical conclusion. Suggested topic matches are navigation hints. Original statements, assumptions and the status ledger remain authoritative.</p>
        <div className="mt-6 flex flex-wrap gap-3">
          {[
            { href: `${REPO_URL}/blob/main/docs/registry/INDEX.md`, label: "Browse the registry" },
            { href: "/documentation/registry.json", label: "Download JSON" },
            { href: `${REPO_URL}/blob/main/docs/LATEX_MAINTENANCE.md`, label: "Maintenance guide" },
          ].map(({ href, label }) => <a key={href} href={href} className="rounded-lg border border-slate-300 bg-white px-4 py-2 text-sm font-semibold text-slate-700 hover:border-blue-400 hover:text-blue-800">{label}</a>)}
        </div>
      </section>
      <section aria-labelledby="topics-heading" className="mt-16">
        <h2 id="topics-heading" className="font-serif text-2xl font-semibold text-slate-950">Navigate by topic</h2>
        <p className="mt-3 text-slate-600">Topic suggestions help locate relevant sections. Consult each registry record for explicit evidence links and its original scope.</p>
        <div className="mt-6 flex flex-wrap gap-3">{registry.topics.map((topic) => <a key={topic.id} href={`${REPO_URL}/blob/main/docs/registry/topics/${topic.id}.md`} className="rounded-full border border-slate-200 bg-white px-4 py-2 text-sm text-slate-700 hover:border-blue-300 hover:text-blue-800">{topic.title}</a>)}</div>
      </section>
      <section aria-labelledby="sources-heading" className="mt-16">
        <h2 id="sources-heading" className="font-serif text-2xl font-semibold text-slate-950">Active documents and editable sources</h2>
        <div className="mt-6 divide-y divide-slate-200 rounded-2xl border border-slate-200 bg-white">{active.map((document) => <a key={document.id} href={`${REPO_URL}/blob/main/${document.canonical_source}`} className="flex items-start gap-4 p-5 transition hover:bg-slate-50"><FileCode2 size={20} className="mt-1 shrink-0 text-blue-700" aria-hidden /><div><h3 className="font-semibold text-slate-900">{document.title}</h3><p className="mt-1 break-all font-mono text-xs leading-relaxed text-slate-500">{document.canonical_source}</p><p className="mt-2 text-xs text-slate-500">{document.ordered_section_ids.length} section records · entry point {document.entry_point}</p></div><ArrowRight size={16} className="ml-auto mt-1 shrink-0 text-slate-400" aria-hidden /></a>)}</div>
      </section>
    </div>
  );
}
