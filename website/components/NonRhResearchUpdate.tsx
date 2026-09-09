import Link from "next/link";
import { REPO_URL } from "@/lib/utils";

const SOURCE = `${REPO_URL}/tree/main/experiments/theory-contracts`;
const RESULTS = [
  {
    title: "Charged fields from the source",
    body: "Local fermion fields now have a controlled limit from the original filled QWZ sea, including both adjoints, integer charge and finite-energy dynamics. This is not yet the half-charged E8 spinor field or an identification with the compiler’s sixteen real Majoranas.",
    path: "microscopic-charged-car-limit/README.md",
  },
  {
    title: "Neutral correlations through collisions",
    body: "The original strip’s alternating four-point functions have a full L¹ limit, including colliding endpoints. An improved comparison window leaves the physical source unchanged. Pair-Gram positivity is not a proof of reflection positivity for a complete quantum field theory.",
    path: "microscopic-fourpoint-limit/README.md",
  },
  {
    title: "All-time lattice dynamics",
    body: "A separately declared compact-U(1) model now has dynamics for every bounded local observable and every real time, retaining all electric fluxes. The full bounded algebra is not point-norm continuous; the continuous subalgebra and physical representation must be distinguished.",
    path: "observable-dynamics/README.md",
  },
  {
    title: "A physical neutral ground representation",
    body: "Periodic ground-state limits give a nonnegative physical generator and nonzero Wilson-loop excitation weight in that same compact model. The spectral estimates do not establish a positive mass gap, a particle mass, a unique vacuum or a continuum limit.",
    path: "ground-state-loop-response/README.md",
  },
  {
    title: "Clock and charge constraints",
    body: "The actual low/high hoppings exclude a site-fixed, rotor-independent internal Clock identification. E8 charge signs require an eight-bit refinement and genuine charge carry. Spatial or flux-dressed alternatives remain research questions, not excluded possibilities.",
    path: "clock-rotor-joint-charge/README.md",
  },
  {
    title: "The next source-to-E8 test",
    body: "Construct a renormalized, smeared half-charge field between sectors, with energy bounds, both adjoints and the correct cocycle. A sharp twist has a divergent implementability sum. Eight added copies or a formal charge register would assume the missing microscopic bridge.",
    path: "half-twist-grade-carry/README.md",
  },
];

export function NonRhResearchUpdate() {
  return (
    <section id="research-20260909" aria-labelledby="research-20260909-title" className="scroll-mt-24 border-t border-slate-800/60 py-12 sm:py-16">
      <div className="mx-auto max-w-6xl space-y-6 px-4 sm:px-6 lg:px-8">
        <span id="non-rh-round27" className="block scroll-mt-24" aria-hidden="true" />
        <p className="text-sm font-medium tracking-wide text-blue-300">RESEARCH CONSOLIDATION · 9 SEPTEMBER 2026</p>
        <h2 id="research-20260909-title" className="font-serif text-3xl font-semibold text-slate-50 sm:text-4xl">Source fields and dynamics. The unification bridge remains open.</h2>
        <p className="max-w-4xl text-base leading-relaxed text-slate-300">
          The post-Round27 archive is now brought together in the papers and source map.
          The advances below have different, explicit hypotheses. They are not yet
          one compiler-selected microscopic theory, independently reviewed proofs
          or new empirical predictions.
        </p>
        <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
          {RESULTS.map((result) => (
            <article key={result.path} className="flex flex-col rounded-xl border border-slate-700/60 bg-slate-900/50 p-5">
              <h3 className="text-lg font-semibold text-slate-100">{result.title}</h3>
              <p className="mb-4 mt-3 flex-1 text-base leading-relaxed text-slate-300">{result.body}</p>
              <a href={`${SOURCE}/${result.path}`} className="text-base text-blue-300 underline underline-offset-4" aria-label={`Proof and limits: ${result.title}`}>Proof and limits</a>
            </article>
          ))}
        </div>
        <div className="space-y-3 border-l-2 border-amber-400/60 pl-5 text-base leading-relaxed text-slate-300">
          <p><strong className="text-amber-200">All physical T1–T8 gates remain open.</strong> The shared 3+1D parent, chiral gauge construction, physical continuum, complete couplings, universally coupled quantum gravity and selected initial state are still missing. Separate successful constructions do not establish their common origin.</p>
          <p>The charged-field dependency chain has 131 tests per Python mode, ordinary and optimized. Historical records retain their source hashes and original publication labels. These tests check the written construction; they are not independent proof certificates. The adjacent prime and double-cover studies do not establish RH or a factoring advantage.</p>
        </div>
        <nav aria-label="Consolidated research sources" className="flex flex-wrap gap-x-6 gap-y-3 text-base text-blue-300">
          <a href={`${SOURCE}/RESEARCH_2026-09-09.md`} className="underline underline-offset-4">Full archive and T1–T8 map</a>
          <a href={`${SOURCE}/ROUND27_STATUS.md`} className="underline underline-offset-4">Earlier Round27 record</a>
          <Link href="/papers/research-contracts" className="underline underline-offset-4">Research contracts paper</Link>
          <Link href="/changelog" className="underline underline-offset-4">Publication history</Link>
        </nav>
      </div>
    </section>
  );
}
