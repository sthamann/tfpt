import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { AUTHORS, authorJsonLd } from "@/lib/authors";
import { papers } from "@/lib/papers";
import { SITE_URL } from "@/lib/utils";

export const dynamicParams = false;
export function generateStaticParams() { return AUTHORS.map(author => ({ slug: author.slug })); }
type Props = { params: Promise<{ slug: string }> };
export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params; const author = AUTHORS.find(author => author.slug === slug);
  if (!author) return {};
  return { title: `${author.name}: TFPT Author and Publications`, description: author.description, alternates: { canonical: `${SITE_URL}/authors/${slug}` }, openGraph: { title: `${author.name}: TFPT Author`, description: author.description, url: `${SITE_URL}/authors/${slug}`, type: "profile", firstName: author.givenName, lastName: author.familyName } };
}
export default async function AuthorPage({ params }: Props) {
  const { slug } = await params; const author = AUTHORS.find(author => author.slug === slug);
  if (!author) notFound();
  const schema = { "@context": "https://schema.org", "@type": "ProfilePage", "@id": `${SITE_URL}/authors/${slug}#profile`, url: `${SITE_URL}/authors/${slug}`, name: `${author.name}: TFPT author`, mainEntity: { ...authorJsonLd(author), description: author.description, subjectOf: papers.map(paper => ({ "@type": "ScholarlyArticle", "@id": `${SITE_URL}/papers/${paper.slug}#article`, name: paper.title, url: `${SITE_URL}/papers/${paper.slug}` })) } };
  return <div className="reference-page"><script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }} />
    <header className="reference-header"><h1>{author.name}</h1><p>{author.description}</p><div className="reference-links"><Link href="/authors">All authors</Link>{author.profiles.map(profile => <a key={profile.url} href={profile.url} rel="noopener noreferrer">{profile.label}</a>)}</div></header>
    <section className="reference-section"><h2>TFPT publications</h2><p>These documents are coauthored with {author.slug === "stefan-hamann" ? "Alessandro Rizzo" : "Stefan Hamann"}. Each paper retains its own assumptions, result scope, PDF release and verification references.</p><div className="reference-rows">{papers.map(paper => <article key={paper.slug}><h3><Link href={`/papers/${paper.slug}`}>{paper.title}</Link></h3><p>{paper.subtitle}</p><div className="reference-links"><Link href={`/papers/${paper.slug}`}>Abstract, sources and citation</Link><a href={paper.pdf}>Read the PDF</a></div></article>)}</div></section>
    <section className="reference-section"><h2>Read and assess the work</h2><p>The research method distinguishes mathematical statements, numerical checks and physical interpretations. Original sources and the status ledger determine the scope of each result.</p><div className="reference-links"><Link href="/method">Research method</Link><Link href="/documentation">Original sources</Link><Link href="/replication">Independent reproduction</Link></div></section>
  </div>;
}
