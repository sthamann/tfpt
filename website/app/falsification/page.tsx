import type { Metadata } from "next";
import Link from "next/link";
import { SITE_URL } from "@/lib/utils";
import { frozenRegistry, predictionGroups, predictionById, predictionLabel, type FrozenPrediction } from "@/lib/frozen-predictions";

export const metadata: Metadata = {
  title: "Failure Criteria: What Would Falsify Each TFPT Statement?",
  description: "Read the exact frozen failure criteria for TFPT statements with their assumptions. Distinguish a mathematical counterexample, a failed physical branch and the remaining goal of a complete theory.",
  alternates: { canonical: `${SITE_URL}/falsification` },
};

function CriterionRow({ row }: { row: FrozenPrediction }) {
  return <article id={row.id} className="scroll-mt-24 border-b border-slate-300 py-6">
    <h3 className="font-serif text-xl font-semibold text-slate-950">{predictionLabel(row.id)}</h3>
    <p className="mt-3 max-w-3xl leading-relaxed text-slate-800">{row.kill_criterion}</p>
    <details className="mt-3">
      <summary className="cursor-pointer py-2 font-medium text-blue-800">Assumptions and scope of this criterion</summary>
      <p className="mt-3 max-w-3xl text-sm leading-relaxed">{row.conditional_on || (row.band_min ? "The formula uses an external reheating input N★ in [50, 60]." : row.layer === "assigned" ? "This is an assigned texture. Its failure tests the assigned branch." : "The registry classifies this as a core numerical readout. An empirical test still needs the stated physical observable and comparison convention.")}</p>
      <p className="mt-3 max-w-3xl text-sm leading-relaxed">The criterion above is reproduced verbatim from the register frozen on 9 June 2026. Conditions such as combined error, transport corrections and subleading budgets remain part of that statement. This page does not replace them with measurement uncertainty alone.</p>
      <nav className="reference-links" aria-label={`${predictionLabel(row.id)} context`}><Link href={`/predictions#${row.id}`}>Exact formula and frozen value</Link><Link href="/results?topic=topic%3Avalidation">Read the research context</Link></nav>
    </details>
  </article>;
}

export default function FalsificationPage() {
  return <article className="reference-page">
    <header className="reference-header">
      <h1>What would falsify each statement?</h1>
      <p>A failed comparison bears on the statement that connects a formula to an observable. Read the committed failure criterion together with that statement’s assumptions and scope.</p>
      <nav className="reference-links" aria-label="Failure criteria context"><Link href="/predictions">The frozen register</Link><Link href="/empirical-audit">Dated measurement comparisons</Link><a href="/research/predictions-frozen.json">Read the original criteria</a></nav>
    </header>
    <section id="kill-criteria" className="reference-section" aria-labelledby="scope-heading">
      <span id="kill-criteria-section" className="scroll-mt-24" />
      <h2 id="scope-heading">Three different ways a statement can fail</h2>
      <dl className="reference-rows">
        <div><dt>Mathematical counterexample</dt><dd>An error in a proof or an explicit counterexample under the same hypotheses refutes that mathematical statement. For example, a lattice construction must actually satisfy the evenness, determinant and root conditions it asserts. <Link href="/verification">Inspect and run the lattice check.</Link></dd></div>
        <div><dt>Conditional physical failure</dt><dd>A measurement satisfying a committed failure criterion rules out the associated physical readout or branch under its stated assumptions. It does not erase separate lattice identities or prove that every other branch fails.</dd></div>
        <div><dt>The full physical goal</dt><dd>A common source for the mathematical pieces, physical observables, dynamics, spacetime and gravity is still a research task. A successful numerical comparison does not establish that complete construction. <Link href="/results">Follow the current questions and findings.</Link></dd></div>
      </dl>
    </section>
    <section id="kill-board" className="reference-section" aria-labelledby="criteria-heading">
      <span id="kill-board-section" className="scroll-mt-24" />
      <h2 id="criteria-heading">The sixteen registered criteria</h2>
      <p>These are the original criteria, grouped by observable. Their wording has not been updated to match later measurements.</p>
      <nav className="reference-links" aria-label="Failure criteria groups">{predictionGroups.map(group => <a key={group.id} href={`#${group.id}`}>{group.title}</a>)}</nav>
      {predictionGroups.map(group => <section key={group.id} id={group.id} className="mt-9 scroll-mt-24" aria-labelledby={`${group.id}-heading`}>
        <h3 id={`${group.id}-heading`} className="font-serif text-2xl font-semibold text-slate-950">{group.title}</h3>
        {group.ids.map(id => <CriterionRow key={id} row={predictionById(id)} />)}
      </section>)}
    </section>
    <section id="textures-and-bands" className="reference-section" aria-labelledby="textures-heading">
      <h2 id="textures-heading">Assigned textures and conditional bands</h2>
      <p>These four entries retain their separate register classes. A failed texture or reheating dependent branch has that scope.</p>
      {[...frozenRegistry.assigned_texture_values, ...frozenRegistry.conditional_bands].map(row => <CriterionRow key={row.id} row={row} />)}
    </section>
    <section id="no-knobs" className="reference-section" aria-labelledby="inputs-heading">
      <span id="no-knobs-section" className="scroll-mt-24" />
      <h2 id="inputs-heading">Keep the assumptions fixed</h2>
      <p>Apply each comparison to the declared equation, branch and measurement convention. Source mass ratios require their transport map; inflation bands require a reheating input. A revised formula is a new statement with its own history, rather than a replacement for the frozen test.</p>
      <nav className="reference-links" aria-label="Inputs and method"><Link href="/explain#inputs">Starting assumptions</Link><Link href="/method">Sources, controls and review</Link><Link href="/predictions#variants">Why the solar variants are not new predictions</Link></nav>
    </section>
    <section id="confrontation" className="reference-section" aria-labelledby="comparison-heading">
      <span id="confrontation-table-section" className="scroll-mt-24" />
      <h2 id="comparison-heading">Compare with data, then return to the criterion</h2>
      <p>The empirical audit gives four dated comparisons with named primary sources. Its measurement uncertainty distances are descriptive; a register criterion that specifies combined error or a correction budget needs that additional information before a failure verdict.</p>
      <nav className="reference-links" aria-label="Comparison and historical sources"><Link href="/empirical-audit">Open the dated empirical audit</Link><Link href="/papers">Historical 27 readout publication surface</Link><Link href="/results?topic=topic%3Avalidation">Reviewed results and recorded exclusions</Link></nav>
    </section>
  </article>;
}
