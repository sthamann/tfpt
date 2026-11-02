import type { Metadata } from "next";
import Link from "next/link";
import { pageMetadata } from "@/lib/seo";
import { FAQ_ITEMS } from "@/lib/faq";

export const metadata: Metadata = pageMetadata("/faq");

const faqJsonLd = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: FAQ_ITEMS.map((item) => ({
    "@type": "Question",
    name: item.q,
    acceptedAnswer: { "@type": "Answer", text: item.a },
  })),
};

export default function FaqPage() {
  return <article className="reference-page">
    <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqJsonLd).replace(/</g, "\\u003c") }} />
    <header className="reference-header">
      <h1>Questions about TFPT</h1>
      <p>Start with a short answer, then follow the construction or inspect its sources. The mathematical result and its physical interpretation each retain their own scope.</p>
    </header>
    <section className="reference-section" aria-label="Questions and answers">
      {FAQ_ITEMS.map((item) => <details className="reference-question" key={item.q}>
        <summary className="min-h-11 cursor-pointer py-4 font-serif text-xl font-semibold">{item.q}</summary>
        <p>{item.a}</p>
        <nav className="reference-links" aria-label={"Sources for: " + item.q}>
          {item.sources.map((source) => <Link key={source.href} href={source.href}>{source.label}</Link>)}
        </nav>
      </details>)}
    </section>
  </article>;
}
