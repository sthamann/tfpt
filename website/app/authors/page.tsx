import Link from "next/link";
import type { Metadata } from "next";
import { AUTHORS, AUTHOR_ENTITIES } from "@/lib/authors";
import { ARCHIVE_RELEASE } from "@/lib/publication";
import { SITE_URL } from "@/lib/utils";

export const metadata: Metadata = {
  title: "TFPT Authors: Stefan Hamann and Alessandro Rizzo",
  description: "Meet the authors of the TFPT publication set. Find their papers, public author identities, original sources and the earlier archived release.",
  alternates: { canonical: `${SITE_URL}/authors` },
  openGraph: { title: "TFPT Authors", description: "Authors, papers and public source records for Topological Fixed-Point Theory.", url: `${SITE_URL}/authors`, type: "website" },
};

export default function AuthorsPage() {
  return <div className="reference-page">
    <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify({ "@context": "https://schema.org", "@type": "CollectionPage", url: `${SITE_URL}/authors`, name: "TFPT authors", about: AUTHOR_ENTITIES }) }} />
    <header className="reference-header"><h1>The authors of TFPT.</h1><p>Stefan Hamann and Alessandro Rizzo are the authors named in the current publication set. Follow their work through the papers, original sources and recorded checks.</p></header>
    <section className="reference-section"><h2>Authors</h2><div className="reference-rows">{AUTHORS.map(author => <article key={author.slug}><h3><Link href={`/authors/${author.slug}`}>{author.name}</Link></h3><p>{author.description}</p><div className="reference-links"><Link href={`/authors/${author.slug}`}>Author and publications</Link>{author.profiles.map(profile => <a key={profile.url} href={profile.url} rel="noopener noreferrer">{profile.label}</a>)}</div></article>)}</div></section>
    <section className="reference-section"><h2>Publications and archive</h2><p>The current TFPT {"publication set"} has its own PDFs, release dates and source fingerprints. The earlier Zenodo deposit records version {ARCHIVE_RELEASE.version}, issued on 25 June 2026 under Stefan Hamann’s name. Its DOI identifies that earlier release.</p><div className="reference-links"><Link href="/papers">Read the current papers</Link><a href={ARCHIVE_RELEASE.url}>Earlier archived release: {ARCHIVE_RELEASE.doi}</a><Link href="/replication">Reproduce a stated result</Link></div></section>
  </div>;
}
