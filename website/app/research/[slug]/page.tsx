import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Math } from "@/components/Math";
import { researchPages, researchSourceHref, RESEARCH_SOURCE_REVISION } from "@/lib/research-pages";
import { SITE_URL } from "@/lib/utils";
import { AUTHOR_ENTITIES } from "@/lib/authors";
import { EDITORIAL_DATE } from "@/lib/publication";

interface ResearchPageProps { params: Promise<{ slug: string }> }

export function generateStaticParams() {
  return researchPages.map((page) => ({ slug: page.slug }));
}

export const dynamicParams = false;

export async function generateMetadata({ params }: ResearchPageProps): Promise<Metadata> {
  const { slug } = await params;
  const page = researchPages.find((entry) => entry.slug === slug);
  if (!page) return {};
  const url = `${SITE_URL}/research/${page.slug}`;
  return {
    title: page.title,
    description: page.description,
    alternates: { canonical: url },
    openGraph: { type: "article", title: page.title, description: page.description, url, locale: "en_US" },
    twitter: { card: "summary_large_image", title: page.title, description: page.description },
  };
}

export default async function ResearchArgumentPage({ params }: ResearchPageProps) {
  const { slug } = await params;
  const page = researchPages.find((entry) => entry.slug === slug);
  if (!page) notFound();

  return <article className="reference-page">
    <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify({ "@context": "https://schema.org", "@type": "Article", "@id": `${SITE_URL}/research/${page.slug}#article`, url: `${SITE_URL}/research/${page.slug}`, mainEntityOfPage: `${SITE_URL}/research/${page.slug}`, headline: page.title, description: page.description, inLanguage: "en", author: AUTHOR_ENTITIES, dateModified: EDITORIAL_DATE, citation: page.sources.map(source => source.href ?? researchSourceHref(source.path, source.lineStart, source.lineEnd)) }) }} />
    <header className="reference-header">
      <nav className="reference-links" aria-label="Research navigation"><Link href="/research">All selected arguments</Link><Link href={page.guide.href}>{page.guide.title}</Link></nav>
      <h1>{page.title}</h1>
      <p>{page.lead}</p>
    </header>
    <section className="reference-section" id="scope">
      <h2>Statement and assumptions</h2>
      <p>{page.scope}</p>
      <nav className="reference-links" aria-label="Argument sections">{page.sections.map((section) => <a key={section.id} href={`#${section.id}`}>{section.title}</a>)}<a href="#original-sources">Original sources</a></nav>
    </section>
    {page.sections.map((section) => <section className="reference-section" id={section.id} key={section.id}>
      <h2>{section.title}</h2>
      {section.blocks.map((block, index) => block.kind === "formula"
        ? <Math key={index} block plain={block.plain}>{block.tex}</Math>
        : <p key={index}>{block.text}</p>)}
    </section>)}
    <section className="reference-section" id="original-sources">
      <h2>Read the original sources</h2>
      <p>This reading edition follows the original arguments below. The paper and its surrounding sections retain the full publication context.</p>
      <div className="reference-rows">
        {page.sources.map((source) => <article key={source.path}>
          <h3><a href={source.href ?? researchSourceHref(source.path, source.lineStart, source.lineEnd)}>{source.title}</a></h3>
          <p className="reference-source-path">{source.path} · original lines {source.lineStart} to {source.lineEnd}</p>
        </article>)}
      </div>
      <div className="reference-links"><Link href={page.paper.href}>{page.paper.title}</Link><a href={page.paper.pdf}>Read the complete PDF</a>{page.sectionIds.map((id) => <Link key={id} href={`/documentation?${new URLSearchParams({ section: id, view: "library" })}`}>Inspect the original library record</Link>)}</div>
      <details><summary>Source version</summary><p className="reference-note">Publication source links are pinned to repository revision {RESEARCH_SOURCE_REVISION}. A linked scientific source excerpt carries its own original fingerprint, line range and recorded publication scope.</p></details>
    </section>
    <section className="reference-section" id="verification-sources">
      <h2>Inspect the cited verification code</h2>
      <p>The following scripts support the particular calculations described here. A citation identifies a source; a new execution needs its own result.</p>
      <div className="reference-rows">
        {page.scripts.map((script) => <article key={script.filename}>
          <h3><a href={researchSourceHref(`verification/${script.filename}`)}>{script.filename}</a></h3>
          <p>{script.description}</p>
          <div className="reference-links"><Link href={`/verification?moduleQuery=${encodeURIComponent(script.filename)}#module-catalog`}>Find the verification module</Link><Link href={`/documentation?source=${encodeURIComponent(`verification/${script.filename}`)}`}>Follow its paper citations</Link></div>
        </article>)}
      </div>
      <nav className="reference-links" aria-label="Research context"><Link href={page.guide.href}>{page.guide.title}</Link><Link href="/results">Statements and physical scope in the atlas</Link><Link href="/research">Read another argument</Link></nav>
    </section>
  </article>;
}
