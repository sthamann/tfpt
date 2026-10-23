import { pageMetadata } from "@/lib/seo";
import { predictionsJsonLd } from "@/lib/structured-data";
import type { Metadata } from "next";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { PredictionsSection } from "@/components/PredictionsSection";
import { SITE_URL } from "@/lib/utils";

export const metadata: Metadata = pageMetadata("/predictions");

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
