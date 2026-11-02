import type { Metadata } from "next";
import Link from "next/link";
import { SITE_URL } from "@/lib/utils";
import { groupDecimal } from "@/lib/format-number";
import { frozenRegistry, predictionGroups, predictionById, predictionLabel, shortFrozenValue, type FrozenPrediction } from "@/lib/frozen-predictions";

export const metadata: Metadata = {
  title: "Frozen Prediction Register: Values, Formulas & Conditions",
  description: "The unchanged TFPT register frozen on 9 June 2026: sixteen main values, assigned textures, conditional bands and separately identified diagnostic variants.",
  alternates: { canonical: `${SITE_URL}/predictions` },
};

function RegistryRow({ row, assigned = false }: { row: FrozenPrediction; assigned?: boolean }) {
  return <article id={row.id} className="scroll-mt-24 border-b border-slate-300 py-6">
    <div className="grid gap-2 sm:grid-cols-[minmax(0,1fr)_auto] sm:gap-6">
      <h3 className="font-serif text-xl font-semibold text-slate-950">{predictionLabel(row.id)}</h3>
      <p className="tabular-nums text-lg text-slate-950">{assigned ? "" : "≈ "}{shortFrozenValue(row)}</p>
    </div>
    <p className="mt-2 max-w-3xl text-sm leading-relaxed text-slate-700">{assigned ? "Assigned texture, not a derivation." : row.conditional_on || (row.band_min ? "Conditional on the external reheating input N★ in [50, 60]." : "Recorded as a core numerical readout. Its physical interpretation retains its source conditions.")}</p>
    <details className="mt-3">
      <summary className="cursor-pointer py-2 font-medium text-blue-800">Exact value, formula and registered criterion</summary>
      <dl className="mt-3 grid gap-4 text-sm leading-relaxed sm:grid-cols-[10rem_minmax(0,1fr)]">
        <dt className="font-semibold">Exact frozen {row.band_min ? "band" : "value"}</dt><dd className="break-all font-mono">{row.band_min ? `${groupDecimal(row.band_min)} to ${groupDecimal(row.band_max||"")}` : row.frozen_value && groupDecimal(row.frozen_value)}</dd>
        <dt className="font-semibold">Formula</dt><dd className="break-words font-mono">{row.formula}</dd>
        <dt className="font-semibold">Registered layer</dt><dd>{row.layer || "Conditional band"}</dd>
        <dt className="font-semibold">Named comparison</dt><dd>{row.experiment} <span className="text-slate-600">(wording retained from the frozen register)</span></dd>
        <dt className="font-semibold">Failure criterion</dt><dd>{row.kill_criterion}</dd>
      </dl>
      <Link href={`/falsification#${row.id}`} className="mt-4 inline-block py-2 text-sm text-blue-800 underline underline-offset-4">Read this criterion in context</Link>
    </details>
  </article>;
}

export default function PredictionsPage() {
  return <article className="reference-page">
    <header className="reference-header">
      <h1>The frozen prediction register</h1>
      <p>The formulas and values committed on 9 June 2026. Start with an observable, then open its exact formula, assumptions and failure criterion.</p>
      <p className="reference-note">A formula freeze preserves a dated statement. Measurements already available at that date remain comparisons. Later data test the frozen value; numerical proximity alone does not establish its physical origin.</p>
      <nav className="reference-links" aria-label="Prediction register context"><Link href="/empirical-audit">Compare with dated measurements</Link><Link href="/falsification">What would falsify a statement?</Link><a href="/research/predictions-frozen.json">Download the unchanged register</a></nav>
    </header>
    <nav className="reference-links" aria-label="Register sections"><a href="#main-values">16 main values</a><a href="#assigned">2 assigned textures</a><a href="#bands">2 conditional bands</a><a href="#variants">2 diagnostic variants</a></nav>
    <section id="main-values" className="reference-section" aria-labelledby="main-values-heading">
      <h2 id="main-values-heading">Main registered values</h2>
      <p>These entries retain the register’s core or conditional classification. Source mass ratios and physical measurements require the comparison map stated with the result.</p>
      {predictionGroups.map(group => <section key={group.id} id={group.id} className="mt-9 scroll-mt-24" aria-labelledby={`${group.id}-heading`}>
        <h3 id={`${group.id}-heading`} className="font-serif text-2xl font-semibold text-slate-950">{group.title}</h3>
        <div>{group.ids.map(id => <RegistryRow key={id} row={predictionById(id)} />)}</div>
      </section>)}
    </section>
    <section id="assigned" className="reference-section" aria-labelledby="assigned-heading">
      <h2 id="assigned-heading">Assigned textures</h2>
      <p>The phase and symmetric texture are assignments. They do not count as derivations of the phase or the atmospheric octant.</p>
      {frozenRegistry.assigned_texture_values.map(row => <RegistryRow key={row.id} row={row} assigned />)}
    </section>
    <section id="bands" className="reference-section" aria-labelledby="bands-heading">
      <h2 id="bands-heading">Conditional inflation bands</h2>
      <p>Both bands use the same external reheating input N★. They are correlated readouts, with N★ in [50, 60] specified in the register.</p>
      {frozenRegistry.conditional_bands.map(row => <RegistryRow key={row.id} row={row} />)}
    </section>
    <section id="variants" className="reference-section" aria-labelledby="variants-heading">
      <h2 id="variants-heading">Diagnostic variants</h2>
      <p>These two versions of the solar texture are explicitly excluded from the prediction count. They do not replace the solar prediction of record.</p>
      {frozenRegistry.derived_variants_not_predictions.map(row => <details key={row.id} id={row.id} className="border-b border-slate-300 py-4 scroll-mt-24">
        <summary className="cursor-pointer py-2 font-semibold text-blue-800">{predictionLabel(row.id)}</summary>
        <p className="mt-3 text-sm leading-relaxed">{row.note}</p><p className="mt-3 break-all font-mono text-sm">{groupDecimal(row.value)}</p><p className="mt-3 break-words font-mono text-sm">{row.formula}</p>
      </details>)}
    </section>
    <section className="reference-section"><h2>Follow the statement to its source</h2><p>The historical 27 readout presentation uses a broader scope than this register. Its original documents and claims remain available in the publication set and research atlas.</p><nav className="reference-links" aria-label="Prediction sources"><Link href="/results?topic=topic%3Avalidation">Research findings and history</Link><Link href="/papers">Original publication set</Link><Link href="/empirical-audit">Current dated comparisons</Link></nav></section>
  </article>;
}
