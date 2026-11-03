import Link from "next/link";
import { researchInventory } from "@/lib/research";

export function ResearchSnapshot() {
  const data = researchInventory();
  const c = data.meta.counts;
  return <section className="guide-section" aria-labelledby="snapshot-heading">
    <h2 id="snapshot-heading">What has been achieved, and what comes next?</h2>
    <p className="guide-lead">The result library brings the published claim ledger together with later source reviewed research. Each achievement retains its assumptions and its exact scope.</p>
    <dl className="scope-list"><div><dt>Established structure</dt><dd>The E₈ glue, the carrier and charge construction, charged flavour relations, the specified alpha root, finite quantum geometry and explicit source response results.</dd></div>
      <div><dt>Connected recent results</dt><dd>The common 4/5/20 structure, intrinsic event geometry, complete reference transport, source memory, local Higgs responses and full field and time maps in the specified source classes.</dd></div>
      <div><dt>Common source route</dt><dd>A complete operational source supplies its field moments, vacuum and time together. The geometric action route and the whole classical Clifford transfer are available. The remaining physical task is to identify the full original interacting source on the same admissible fields and projection.</dd></div>
    </dl>
    <p className="mt-5"><Link className="guide-link" href="/explain#source">Follow the common source route and its original theorem</Link></p>
    <details className="guide-details mt-7"><summary>Latest source results: the whole kernel, its limits and the environment</summary>
      <p>The source review retains the complete field, reference and time maps. For the stated smooth classical background, the full Clifford transfer is calculated through exterior powers of its one particle heat operator. Its vacuum and every ordered field response belong to that same construction.</p>
      <p>A spectral theorem excludes a literal independent flat mirror factor of dimension greater than two inside this unprojected quasifree heat source, even after a nonlinear unitary change of field coordinates. Physical Gauss projection and the full interacting source lie outside that exclusion. DET16 is a candidate comparison, not a requirement for every TFPT completion.</p>
      <p>A larger declared interacting source has a nonzero ordered transition in which the environment carries the compensating charge. Its direct vertex is not an elementary CAR field, and that calculation does not yet identify it with the primitive TFPT source. The consolidated result keeps this remaining equation explicit.</p>
      <div className="flex flex-wrap gap-4"><Link className="guide-link" href="/explain#source">Read the source construction and its scope</Link><Link className="guide-link" href="/results?search=r109">Environment and charged responses</Link><Link className="guide-link" href="/results?record=finding%3Ar110-consolidated-source-results-and-atlas-provenance-audit">Read the consolidated source results</Link></div>
    </details>
    <p className="mt-6 text-sm text-slate-600">Snapshot {data.meta.generatedAt.slice(0,10)}: {c.ledgerActive} active ledger claims and {c.reviewedFindings} scientific research findings. Includes scoped exclusions and corrections. The {c.registeredScripts} registered scripts are a separate inventory, not a new full suite run.</p>
    <div className="mt-6 flex flex-wrap gap-3"><Link className="guide-primary" href="/results">Read the complete result library</Link><Link className="readout-button" href="/explain#status">Understand the status labels</Link><Link className="readout-button" href="/verification">Reproduce a calculation</Link></div>
  </section>;
}

export function PredictionRegistryGuide() {
  const { predictions: r } = researchInventory();
  const groups = [
    { title: "Main registered values", entries: r.predictions, note: "Read the layer and conditions of each entry. A known measured value and a future independent test have different histories." },
    { title: "Assigned texture values", entries: r.assigned_texture_values, note: "These are assigned texture branches in this frozen register, not an additional derivation of their physical selection." },
    { title: "Conditional bands", entries: r.conditional_bands, note: "The bands retain their external inputs, including the declared reheating range." },
    { title: "Derived variants, not new predictions", entries: r.derived_variants_not_predictions, note: "Alternative evaluations of a registered texture do not create extra independent predictions." },
  ];
  return <section className="guide-section" id="registered-values">
    <h2>Which kind of prediction are you reading?</h2>
    <p className="guide-lead">The register was frozen on {r.freeze_date}. It contains 16 main entries, two assigned textures and two conditional bands. Two further variants are explicitly not new predictions. The broader experimental test surface is a different count.</p>
    <ol className="guide-steps"><li><strong>Before the formula:</strong> identify which measurements were already available.</li><li><strong>At the freeze:</strong> retain the exact formula, value, conditions and timestamp.</li><li><strong>After the freeze:</strong> compare independent later data with the committed statement and its declared failure criterion.</li></ol>
    <p className="mb-6">Alpha and the mixing angles were already measured. A later precision measurement can test a frozen value without making the earlier numerical agreement a blind discovery. Sigma values describe dated comparisons, not a probability that the theory is true.</p>
    {groups.map(group => <details key={group.title} className="guide-details my-3"><summary>{group.title} · {group.entries.length}</summary><p>{group.note}</p>
      <div className="divide-y divide-slate-200">{group.entries.map(entry => <div key={entry.id} className="py-4"><h3 className="text-xl">{entry.observable}</h3><p className="break-words">{entry.formula}{entry.frozen_value ? ` = ${entry.frozen_value}` : ""}</p><p className="text-sm">{entry.layer ? `Register layer: ${entry.layer}. ` : ""}{entry.conditional_on}</p>{entry.experiment && <p className="text-sm">Experiment in the frozen record: {entry.experiment}</p>}{entry.kill_criterion && <p className="text-sm">Failure criterion: {entry.kill_criterion}</p>}</div>)}</div>
    </details>)}
    <p className="mt-5 text-sm">Newer neutrino candidates, including the alternative phase near 287.7°, retain their own derivation and mechanism status. They do not silently replace the registered 240° texture or its history.</p>
    <div className="mt-5 flex flex-wrap gap-4 text-sm"><a className="guide-link" href="/research/predictions-frozen.json">Read the exact frozen JSON</a><Link className="guide-link" href="/results?search=neutrino">Inspect the neutrino results</Link><Link className="guide-link" href="/explain#alpha">Follow the alpha derivation</Link></div>
  </section>;
}
