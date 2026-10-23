import { pageMetadata } from "@/lib/seo";
import type { Metadata } from "next";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { HostileRefereeFAQ } from "@/components/HostileRefereeFAQ";
import { FAQ_ITEMS } from "@/lib/faq";
import { SITE_URL } from "@/lib/utils";

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
  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(faqJsonLd) }}
      />

      <section className="relative isolate overflow-hidden pt-12 pb-8 sm:pt-16">
        <div aria-hidden className="absolute inset-0 grid-bg pointer-events-none" />
        <div
          aria-hidden
          className="absolute -top-40 left-1/2 -z-10 h-[460px] w-[1000px] -translate-x-1/2 rounded-full opacity-30 blur-3xl"
          style={{
            background:
              "radial-gradient(closest-side, rgba(244,63,94,0.3), rgba(99,102,241,0.25), transparent)",
          }}
        />
        <div className="relative mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
          <nav aria-label="Breadcrumb" className="mb-6">
            <Link
              prefetch={false}
              href="/"
              className="inline-flex items-center gap-1.5 text-sm text-slate-600 transition-colors hover:text-slate-800"
            >
              <ArrowLeft size={14} />
              Back to overview
            </Link>
          </nav>
          <span className="inline-flex items-center gap-2 rounded-full border border-rose-400/20 bg-rose-500/10 px-4 py-1.5 text-xs font-medium tracking-wider text-rose-800">
            <span className="uppercase">Hostile-referee FAQ</span>
          </span>
          <h1 className="mt-6 font-serif text-4xl font-semibold leading-tight text-slate-950 sm:text-5xl">
            The sharpest objections, <span className="text-gradient-blue">answered</span>.
          </h1>
          <p className="mt-4 max-w-2xl text-base leading-relaxed text-slate-700">
            A theory at this scope deserves an adversary, not a cheerleader.
            These are the first questions a sceptical physicist asks — E₈,
            &ldquo;Standard Model derived&rdquo;, &ldquo;zero fitted
            constants&rdquo; — answered with the status discipline that backs
            them.
          </p>
        </div>
      </section>

      <section className="relative py-8 sm:py-12">
        <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
          <HostileRefereeFAQ />
        </div>
      </section>
    </>
  );
}
