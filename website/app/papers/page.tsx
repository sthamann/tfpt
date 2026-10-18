import { collectionJsonLd } from "@/lib/structured-data";
import type { Metadata } from "next";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { PapersSection } from "@/components/PapersSection";
import { DownloadsSection } from "@/components/DownloadsSection";
import { SITE_URL } from "@/lib/utils";
import { SITE_VERSION } from "@/lib/version";

export const metadata: Metadata = {
  title: "Papers — TFPT Document Set",
  description:
    `The full TFPT ${SITE_VERSION} document set: reading guide, five core papers, and four companions — architecture, Standard Model, audit & bootstrap, frontier, Red Team, horizon, Origin Theory, research contracts, safeguards.`,
  alternates: { canonical: `${SITE_URL}/papers` },
  openGraph: {
    images: [{ url: `${SITE_URL}/opengraph-image`, width: 1200, height: 630, alt: "TFPT — Topological Fixed-Point Theory" }],
    type: "website",
    title: "Papers — TFPT Document Set",
    description: `The TFPT ${SITE_VERSION} document set: reading guide, five core papers, four companions.`,
    url: `${SITE_URL}/papers`,
    siteName: "TFPT — Topological Fixed-Point Theory",
    locale: "en_US",
  },
};

export default function PapersIndexPage() {
  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(collectionJsonLd) }} />
      <div className="mx-auto max-w-7xl px-4 pt-10 sm:px-6 lg:px-8">
        <Link
          prefetch={false}
          href="/"
          className="inline-flex items-center gap-1.5 text-sm text-slate-600 transition-colors hover:text-slate-800"
        >
          <ArrowLeft size={14} aria-hidden />
          Back to start
        </Link>
      </div>
      <div className="mx-auto mt-8 max-w-7xl px-4 sm:px-6 lg:px-8">
        <Link href="/documentation" className="block rounded-xl border border-blue-200 bg-blue-50 p-5 text-sm leading-relaxed text-blue-900">
          Start with the compact reading guide, open the verification catalog separately,
          or find a topic and its editable sources in the document library →
        </Link>
      </div>
      <PapersSection />
      <DownloadsSection />
    </>
  );
}
