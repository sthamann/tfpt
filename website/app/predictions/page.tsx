import { predictionsJsonLd } from "@/lib/structured-data";
import type { Metadata } from "next";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { PredictionsSection } from "@/components/PredictionsSection";
import { SITE_URL } from "@/lib/utils";

export const metadata: Metadata = {
  title: "Predictions — 27 Status-Graded Test Surfaces",
  description:
    "The TFPT prediction surface: 27 status-graded, falsifiable test surfaces — frozen pre-data where applicable, each with a kill condition and a ledger marker.",
  alternates: { canonical: `${SITE_URL}/predictions` },
  openGraph: {
    images: [{ url: `${SITE_URL}/opengraph-image`, width: 1200, height: 630, alt: "TFPT — Topological Fixed-Point Theory" }],
    type: "website",
    title: "Predictions — TFPT",
    description:
      "27 status-graded, falsifiable test surfaces from the TFPT compiler closure.",
    url: `${SITE_URL}/predictions`,
    siteName: "TFPT — Topological Fixed-Point Theory",
    locale: "en_US",
  },
};

export default function PredictionsPage() {
  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(predictionsJsonLd) }} />
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
      <PredictionsSection />
    </>
  );
}
