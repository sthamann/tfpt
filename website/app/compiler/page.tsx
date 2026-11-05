import type { Metadata } from "next";
import { ExternalLink } from "lucide-react";
import { SITE_URL } from "@/lib/utils";

export const metadata: Metadata = {
  title: "Compiler in Action: Shared Geometry and Standard-Model Structure",
  description:
    "An interactive walkthrough of the TFPT numerical compiler. The displayed c₃ normalization and carrier rank belong to a structured boundary source and declared physical readout with existing conditional reductions. Explore E₈ closure, constant relations, flavor and the 23-readout board, and test the stated numerical contract with ablations.",
  keywords: [
    "TFPT compiler",
    "interactive Standard Model",
    "E8 audit hull",
    "c3 = 1/(8π)",
    "g_car = 5",
    "fine-structure constant 137",
    "ablation console",
    "TFPT machine",
    "Stefan Hamann",
    "Alessandro Rizzo",
  ],
  alternates: { canonical: `${SITE_URL}/compiler` },
  openGraph: {
    images: [{ url: `${SITE_URL}/opengraph-image`, width: 1200, height: 630, alt: "TFPT — Topological Fixed-Point Theory" }],
    type: "website",
    title: "The Compiler in Action — TFPT",
    description:
      "Explore the numerical TFPT compiler: c₃ normalization, carrier, E₈ closure and a 23-readout board. The structured physical source retains its stated premises.",
    url: `${SITE_URL}/compiler`,
    siteName: "TFPT — Topological Fixed-Point Theory",
    locale: "en_US",
  },
  twitter: {
    images: [`${SITE_URL}/opengraph-image`],
    card: "summary_large_image",
    title: "The Compiler in Action — TFPT",
    description:
      "Explore shared numerical data and E₈ compiler closure, with an interactive ablation console and stated source scope.",
  },
};

export default function CompilerPage() {
  return (
    <section className="flex h-[calc(100vh-4rem)] flex-col">
      <div className="flex shrink-0 items-center justify-between gap-4 border-b border-slate-200/60 bg-slate-50/40 px-4 py-2.5 sm:px-6">
        <div className="min-w-0">
          <h1 className="truncate font-serif text-base font-semibold text-slate-900 sm:text-lg">
            The Compiler in Action
          </h1>
          <p className="truncate text-xs text-slate-600">
            Displayed numerical readouts: <span className="font-mono text-slate-700">c₃ = 1/(8π)</span> and{" "}
            <span className="font-mono text-slate-700">g_car = 5</span>. Explore the numerical compiler
            and its 23-readout board under the stated source premises.{" "}
            <span className="hidden sm:inline">Click any part of the machine to inspect it.</span>
          </p>
        </div>
        <a
          href="/compiler/index.html?v=4"
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex shrink-0 items-center gap-1.5 rounded-full border border-slate-300/60 bg-slate-900/5 px-3 py-1.5 text-xs font-medium text-slate-800 transition-colors hover:bg-slate-900/5 hover:text-slate-950"
        >
          <ExternalLink size={13} aria-hidden />
          Full screen
        </a>
      </div>
      <iframe
        src="/compiler/index.html?v=4"
        title="TFPT Machine — the compiler in action: from one edge to the Standard Model"
        loading="lazy"
        className="w-full flex-1 border-0 bg-[#080c18]"
      />
    </section>
  );
}
