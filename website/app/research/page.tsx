import type { Metadata } from "next";
import Link from "next/link";
import { researchPages } from "@/lib/research-pages";
import { SITE_URL } from "@/lib/utils";

const title = "TFPT Research Arguments: E₈, Alpha & the Four Mark Divisor";
const description = "Read selected original TFPT arguments in full: the E₈ discriminant glue, the shared four point divisor and the global alpha root proof, with formulas and sources.";
export const metadata: Metadata = {
  title,
  description,
  alternates: { canonical: `${SITE_URL}/research` },
  openGraph: { type: "website", title, description, url: `${SITE_URL}/research` },
  twitter: { card: "summary_large_image", title, description },
};

export default function ResearchPage() {
  return <article className="reference-page">
    <header className="reference-header">
      <h1>Read the mathematical arguments.</h1>
      <p>Three selected TFPT arguments, with the definitions, formulas and reasoning on the page. Each reading edition keeps the original assumptions and links directly to its paper, source lines and cited verification code.</p>
    </header>
    <section className="reference-section" aria-label="Selected original arguments">
      <div className="reference-rows">
        {researchPages.map((page) => <article key={page.slug}>
          <h2><Link href={`/research/${page.slug}`}>{page.title}</Link></h2>
          <p>{page.lead}</p>
          <div className="reference-links"><Link href={`/research/${page.slug}`}>Read the argument</Link><Link href={page.guide.href}>Read the topic guide</Link></div>
        </article>)}
      </div>
    </section>
    <section className="reference-section">
      <h2>Continue into the original documents</h2>
      <p>These pages select complete arguments from a larger publication set. The source library retains the remaining sections, evidence links and document filters. The knowledge atlas follows each result into its recorded assumptions and physical scope.</p>
      <nav className="reference-links" aria-label="Continue reading"><Link href="/documentation">Search the full source library</Link><Link href="/papers">Read the papers</Link><Link href="/results">Inspect the knowledge atlas</Link></nav>
    </section>
  </article>;
}
