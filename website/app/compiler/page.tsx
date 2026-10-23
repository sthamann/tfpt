import { pageMetadata } from "@/lib/seo";
import type { Metadata } from "next";
import { ExternalLink } from "lucide-react";
import { SITE_URL } from "@/lib/utils";

export const metadata: Metadata = pageMetadata("/compiler");

export default function CompilerPage() {
  return (
    <section className="flex h-[calc(100vh-4rem)] flex-col">
      <div className="flex shrink-0 items-center justify-between gap-4 border-b border-slate-200/60 bg-slate-50/40 px-4 py-2.5 sm:px-6">
        <div className="min-w-0">
          <h1 className="truncate font-serif text-base font-semibold text-slate-900 sm:text-lg">
            The Compiler in Action
          </h1>
          <p className="truncate text-xs text-slate-600">
            Two numbers — <span className="font-mono text-slate-700">c₃ = 1/(8π)</span> and{" "}
            <span className="font-mono text-slate-700">g_car = 5</span> — compile the Standard
            Model, the constants and a 23-readout prediction board.{" "}
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
