import Link from "next/link";
import { Math } from "@/components/Math";
import { TOPIC_GUIDES, type TopicGuideData, type TopicLink } from "@/lib/topic-guides";
import { AUTHOR_ENTITIES } from "@/lib/authors";
import { SITE_URL } from "@/lib/utils";
import { EDITORIAL_DATE } from "@/lib/publication";
import type { ReactNode } from "react";
import { ReadingText } from "@/components/ReadingText";

function SourceLinks({ links, label }: { links: readonly TopicLink[]; label: string }) {
  return <nav className="reference-links" aria-label={label}>
    {links.map((link) => /\.(?:txt|py|pdf)(?:$|[?#])/.test(link.href)
      ? <a key={link.href} href={link.href}>{link.label}</a>
      : <Link key={link.href} href={link.href}>{link.label}</Link>)}
  </nav>;
}

export function TopicGuide({ guide, children, contents, sectionContent }: {
  guide: TopicGuideData;
  children?: ReactNode;
  contents?: readonly { id: string; title: string }[];
  sectionContent?: Readonly<Record<string, ReactNode>>;
}) {
  const url = SITE_URL + guide.slug;
  const schema = { "@context": "https://schema.org", "@type": "Article", "@id": url + "#article", url, mainEntityOfPage: url, headline: guide.title, description: guide.answer, inLanguage: "en", author: AUTHOR_ENTITIES, dateModified: EDITORIAL_DATE, about: { "@id": SITE_URL + "/#research-project" }, citation: guide.sources.map(source => source.href.startsWith("http") ? source.href : SITE_URL + source.href) };
  return <article className="reference-page topic-guide">
    <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }} />
    <header className="reference-header">
      <h1>{guide.title}</h1>
      <p>{guide.intro}</p>
      <nav className="topic-contents" aria-label="On this page">
        {(contents ?? guide.sections).map((section) => <a key={section.id} href={`#${section.id}`}>{section.title}</a>)}
        <a href="#verification">Reproduce the calculation</a>
      </nav>
    </header>
    {children ? <div className="topic-experience">{children}</div> : guide.sections.map((section) => <section className="reference-section" id={section.id} key={section.id} aria-labelledby={`${section.id}-heading`}>
      <h2 id={`${section.id}-heading`}>{section.title}</h2>
      {section.paragraphs.map((paragraph) => <p key={paragraph}><ReadingText text={paragraph} /></p>)}
      {section.formula && <Math block plain={section.formula.plain}>{section.formula.tex}</Math>}
      {sectionContent?.[section.id] && <div className="topic-experience">{sectionContent[section.id]}</div>}
      {section.sources && <SourceLinks links={section.sources} label={`Sources for ${section.title}`} />}
    </section>)}
    <section className="reference-section" id="verification" aria-labelledby="verification-heading">
      <h2 id="verification-heading">Reproduce the calculation</h2>
      <p>{guide.answer}</p>
      <p>{guide.verification.description}</p>
      <SourceLinks links={guide.verification.links} label="Verification sources and instructions" />
      <h3 className="mt-8">Read the original argument</h3>
      <SourceLinks links={guide.sources} label="Original papers and source passages" />
    </section>
    <section className="reference-section" aria-labelledby="questions-heading">
      <h2 id="questions-heading">Related questions</h2>
      {guide.faqs.map((item) => <details className="reference-question" key={item.question}>
        <summary className="py-3 font-serif text-xl font-semibold">{item.question}</summary>
        <p>{item.answer}</p>
      </details>)}
    </section>
    <section className="reference-section" aria-labelledby="continue-heading">
      <h2 id="continue-heading">Continue through the construction</h2>
      <SourceLinks links={TOPIC_GUIDES.filter((item) => item.id !== guide.id).map((item) => ({ label: item.title, href: item.slug })).concat([{ label: "The complete connected explanation", href: "/explain" }])} label="Related TFPT explanations" />
    </section>
  </article>;
}
