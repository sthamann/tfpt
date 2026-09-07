import Link from "next/link";
import { REPO_URL } from "@/lib/utils";

const SOURCE = `${REPO_URL}/tree/main/experiments/theory-contracts`;

export function NonRhResearchUpdate() {
  return (
    <section id="non-rh-round27" aria-labelledby="non-rh-round27-title" className="scroll-mt-24 border-t border-slate-800/60 py-12 sm:py-16">
      <div className="mx-auto max-w-6xl space-y-6 px-4 sm:px-6 lg:px-8">
        <p className="text-sm font-medium tracking-wide text-blue-300">NON-RH RESEARCH · 7 SEPTEMBER 2026 · ROUND 27</p>
        <h2 id="non-rh-round27-title" className="font-serif text-3xl font-semibold text-slate-50 sm:text-4xl">Stronger error control. Physical completion still open.</h2>
        <p className="max-w-4xl text-base leading-relaxed text-slate-300">
          The research archive now includes the positive-parent, constraint-domain,
          charge-transport and signed-history work through Round 27. These are
          mathematical results under stated assumptions, not a derived common
          microscopic theory or new empirical predictions.
        </p>
        <div className="grid gap-5 md:grid-cols-3">
          <article className="rounded-xl border border-slate-700/60 bg-slate-900/50 p-5">
            <h3 className="text-lg font-semibold text-slate-100">One full reference</h3>
            <p className="mt-3 text-base leading-relaxed text-slate-300">Keeping all constant charge profiles removes an artificial extra charge factor from the sign, memory and hopping error bounds. The original E8 phases and scalar determinants remain. An exponential volume-dependent sign bound still remains.</p>
          </article>
          <article className="rounded-xl border border-slate-700/60 bg-slate-900/50 p-5">
            <h3 className="text-lg font-semibold text-slate-100">Smaller certified cutoffs</h3>
            <p className="mt-3 text-base leading-relaxed text-slate-300">At N=27, T=3, β=1 and J=0.1, the charge cutoff falls from 4096 to 2670 and total hopping order from 962 to 354, for less than 1% omission error. The full partition has not been evaluated.</p>
          </article>
          <article className="rounded-xl border border-slate-700/60 bg-slate-900/50 p-5">
            <h3 className="text-lg font-semibold text-slate-100">A nonzero memory cutoff</h3>
            <p className="mt-3 text-base leading-relaxed text-slate-300">A specified weak-hopping example on 729 sites retains 25 of 33 quadratic time offsets. Its summed memory-error bound is at most 0.2045%, with combined omission error below 1%. The full determinant remains a full-history function.</p>
          </article>
        </div>
        <div className="space-y-3 border-l-2 border-amber-400/60 pl-5 text-base leading-relaxed text-slate-300">
          <p><strong className="text-amber-200">What this does not solve:</strong> practical charge summation, an efficient sign cure, an interacting continuum and real-time reconstruction, a shared microscopic parent, chiral completion or gravity. All physical T1–T8 gates remain open.</p>
          <p>Two checkers contain 23 and 25 exact groups with 18 source pins each. There are 37 isolated regression fixtures and 29 prerequisite reruns. Test counts are not independent proof certificates; numerical evaluation error of a future full sum requires an additional budget.</p>
        </div>
        <nav aria-label="Round 27 research sources" className="flex flex-wrap gap-x-6 gap-y-3 text-base text-blue-300">
          <a href={`${SOURCE}/ROUND27_STATUS.md`} className="underline underline-offset-4">Results and limits</a>
          <a href={`${SOURCE}/full-reference-control-round27/PROOF.md`} className="underline underline-offset-4">Full-reference proof</a>
          <a href={`${SOURCE}/reference-tail-planner-round27/PROOF.md`} className="underline underline-offset-4">Certified examples</a>
          <Link href="/papers/research-contracts" className="underline underline-offset-4">Research contracts paper</Link>
        </nav>
      </div>
    </section>
  );
}
