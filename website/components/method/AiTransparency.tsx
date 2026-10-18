import { REPO_URL } from "@/lib/utils";

/**
 * The AI-transparency statement — sober, factual, no defensiveness. The
 * load-bearing point: nothing depends on trusting an agent, because every
 * finding must pass the deterministic, replayable suite.
 */
export function AiTransparency() {
  return (
    <div className="rounded-2xl border border-slate-300/50 bg-slate-50/60 p-5 sm:p-6">
      <p className="text-sm leading-relaxed text-slate-700 sm:text-[15px]">
        <span className="font-semibold text-slate-900">
          AI agents are used in this project — as instruments.
        </span>{" "}
        They write and run the exploratory probes, draft module code and keep
        the mirrors in sync. They decide nothing. Every finding, positive or
        negative, must pass the same gate: a deterministic verification module
        with named checks, typed status markers and frozen tolerances, replayed
        in full by
      </p>
      <pre className="mt-3 overflow-x-auto rounded-xl border border-slate-200/70 bg-slate-100/60 px-4 py-3 font-mono text-[13px] text-emerald-700">
        <code>python3 verification/run_all.py</code>
      </pre>
      <p className="mt-3 text-sm leading-relaxed text-slate-600 sm:text-[15px]">
        Anyone can replay it — the suite is deterministic (the replay sample
        above is re-certified on every run), the papers and this site are
        generated mirrors of the same ledger, and the{" "}
        <a
          href={REPO_URL}
          target="_blank"
          rel="noopener noreferrer"
          className="text-slate-800 underline decoration-slate-400 underline-offset-2 hover:text-slate-950"
        >
          repository
        </a>{" "}
        contains everything needed to do so. The erratum culture is part of the
        same contract: when the W1 chain misread a convention in its source
        paper, the error was found by the suite&rsquo;s own consistency checks
        and published as a dated erratum the same day (v643) — labels
        corrected, numbers unchanged, nothing quietly rewritten. Tools may
        propose; only the suite disposes.
      </p>
    </div>
  );
}
