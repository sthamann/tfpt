"use client";

import { useState } from "react";
import Link from "next/link";
import { Check, Copy } from "lucide-react";
import { SCRIPT_TOTAL } from "@/lib/suite";
import { cn } from "@/lib/utils";

const REPRO_LINE = "python run_all.py → ALL CHECKS PASSED";
const REPRO_COPY = "python run_all.py";

/**
 * The anti-slop strip: machine-checked counts + copyable repro one-liner.
 * Intended as the hero visual — lab-notebook, not marketing glow.
 */
export function ProofStrip({ className }: { className?: string }) {
  const [copied, setCopied] = useState(false);

  const copy = async () => {
    try {
      await navigator.clipboard.writeText(REPRO_COPY);
      setCopied(true);
      window.setTimeout(() => setCopied(false), 1600);
    } catch {
      /* clipboard may be denied; the line remains selectable */
    }
  };

  return (
    <div
      className={cn(
        "w-full max-w-3xl border border-slate-400/50 bg-slate-50/80 text-left",
        className,
      )}
    >
      <div className="border-b border-slate-300/60 px-3 py-2 font-mono text-[11px] leading-relaxed tracking-wide text-slate-700 sm:px-4 sm:text-xs">
        <span className="text-emerald-700/90">{SCRIPT_TOTAL}</span>
        {" machine-checked modules · Wolfram mirror · Lean carrier · "}
        <span className="text-amber-800/90">0 external replications yet</span>
      </div>
      <div className="flex flex-col gap-2 px-3 py-2.5 sm:flex-row sm:items-center sm:justify-between sm:px-4">
        <button
          type="button"
          onClick={copy}
          title="Copy: python run_all.py"
          className="group flex min-h-8 min-w-0 items-center gap-2 text-left font-mono text-[11px] text-slate-800 transition-colors hover:text-slate-950 sm:text-xs"
        >
          <span className="truncate">{REPRO_LINE}</span>
          {copied ? (
            <Check size={13} className="flex-none text-emerald-700" aria-hidden />
          ) : (
            <Copy
              size={13}
              className="flex-none text-slate-600 group-hover:text-slate-700"
              aria-hidden
            />
          )}
          <span className="sr-only">
            {copied ? "Copied" : "Copy run command"}
          </span>
        </button>
        <Link
          prefetch={false}
          href="/replication"
          className="inline-flex min-h-8 flex-none items-center font-mono text-[10px] uppercase tracking-widest text-slate-600 underline decoration-slate-300 underline-offset-2 hover:text-slate-800"
        >
          Replication status →
        </Link>
      </div>
    </div>
  );
}
