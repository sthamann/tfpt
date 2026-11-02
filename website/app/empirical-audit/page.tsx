import type { Metadata } from "next";
import Link from "next/link";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { ArrowLeft, ArrowRight, Download, ExternalLink } from "lucide-react";
import { SITE_URL } from "@/lib/utils";
import summary from "@/lib/research-summary.json";

export const metadata: Metadata = {
  title: "TFPT Empirical Audit: Dated Data, Frozen Values & Limits",
  description: "Compare frozen TFPT readouts with dated primary measurements. Inspect the prediction classes, failure criteria and historical search records without conflating numerical agreement with physical validation.",
  alternates: { canonical: `${SITE_URL}/empirical-audit` },
};

type FrozenRow = { id: string; observable: string; formula: string; frozen_value?: string; conditional_on?: string | null; kill_criterion?: string; band_min?: string; band_max?: string };
type Registry = { freeze_date: string; predictions: FrozenRow[]; assigned_texture_values: FrozenRow[]; conditional_bands: FrozenRow[]; derived_variants_not_predictions: FrozenRow[] };
type Attempt = { id: string; titleEN: string; kind: string; status?: string; verdictRaw?: string; domain?: string; reviewState: string };
type Atlas = { attempts: Attempt[]; coverage: { attemptInventoryDate: string } };
const registry = JSON.parse(readFileSync(join(process.cwd(), "public/research/predictions-frozen.json"), "utf8")) as Registry;
const atlas = JSON.parse(readFileSync(join(process.cwd(), "public/research/semantic-atlas.json"), "utf8")) as Atlas;
const frozen = new Map(registry.predictions.map((r) => [r.id, r]));
const checkedDate = "2 November 2026";
const comparisons = [
  {
    id: "ALPHA_INV", title: "Inverse fine structure constant", measured: "137.035999177 ± 0.000000021",
    date: "CODATA 2022 adjustment", result: "1.90 measurement standard uncertainties above the recommended value",
    meaning: "The difference uses the CODATA standard uncertainty alone. It is a numerical comparison, not a combined theory significance or a derivation of the physical coupling.",
    source: "NIST: 2022 CODATA constants", href: "https://physics.nist.gov/cuu/Constants/Table/allascii.txt",
    history: "The CODATA adjustment predates the registry freeze.",
  },
  {
    id: "SIN2_THETA12_SEED", title: "Solar neutrino mixing, sin² θ₁₂", measured: "0.3036 ± 0.0064",
    date: "JUNO 207.2 live days; collaboration preprint, 29 September 2026",
    result: "0.49 measurement standard uncertainties above the JUNO central value",
    meaning: "This comparison uses the normal mass ordering result. The precision does not distinguish the conditional TFPT value from the measured interval.",
    source: "JUNO Collaboration: 207.2 day oscillation analysis", href: "https://arxiv.org/abs/2609.37895",
    history: "The cited collaboration preprint appeared on 29 September 2026. The earlier 59.1 day result, 0.3092 ± 0.0087, was already public on 18 November 2025, before the registry freeze. A prospective test must be assessed against the first public disclosure of the tested value, not its journal date alone.",
  },
  {
    id: "SIN2_THETA13", title: "Reactor neutrino mixing, sin² θ₁₃", measured: "0.02249 ± 0.00057",
    date: "NuFIT 6.1, November 2025 data; normal ordering, IC23 without SK atmospheric data",
    result: "1.08 measurement standard uncertainties above this fit",
    meaning: "The selected fit is stated explicitly because the result depends on ordering and the data combination. The older approximate two sigma label is not used for this comparison.",
    source: "NuFIT 6.1 parameter table", href: "https://www.nu-fit.org/sites/default/files/v61.tbl-parameters.pdf",
    history: "The global fit predates the registry freeze and shares neutrino data with other comparison rows.",
  },
  {
    id: "BETA_BIREFRINGENCE_DEG", title: "Cosmic birefringence, β", measured: "0.215° ± 0.074°",
    date: "ACT DR6 analysis, submitted 17 September 2025; revised 14 April 2026",
    result: "0.37 measurement standard uncertainties above this analysis",
    meaning: "The authors retain unresolved instrumental systematics. The published analysis does not establish a cosmological detection or identify a TFPT mechanism.",
    source: "Diego Palazuelos and Komatsu: ACT DR6", href: "https://arxiv.org/abs/2509.13654",
    history: "This constant rotation comparison is distinct from later searches for anisotropic or time dependent birefringence.",
  },
];

export default function EmpiricalAuditPage() {
  const historical = atlas.attempts.filter((a) => a.kind === "scorecard");
  const statuses = historical.reduce<Record<string, number>>((all, a) => {
    const key = a.status || a.verdictRaw || "unclassified";
    all[key] = (all[key] || 0) + 1;
    return all;
  }, {});
  return (
    <div className="guide-shell py-10 sm:py-16">
      <nav aria-label="Breadcrumb" className="mb-10">
        <Link href="/predictions" className="inline-flex items-center gap-2 text-sm text-blue-700 underline-offset-4 hover:underline focus-visible:outline-2 focus-visible:outline-offset-4">
          <ArrowLeft size={16} aria-hidden /> Predictions and readouts
        </Link>
      </nav>
      <header className="max-w-3xl">
        <h1 className="font-serif text-4xl font-semibold leading-tight text-slate-950 sm:text-6xl">TFPT against the data</h1>
        <p className="mt-6 text-lg leading-relaxed text-slate-700">TFPT has frozen numerical readouts and a record of empirical searches. Here each comparison states the data release, the formula being tested and the conclusion that the evidence supports.</p>
        <p className="mt-4 text-sm leading-relaxed text-slate-600">Primary sources checked {checkedDate}. The selected comparisons below are dated observations, not a new global fit. The scientific inventory was captured {new Date(summary.generatedAt).toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric", timeZone: "UTC" })} at revision <code className="break-all text-xs">{summary.sourceRevision}</code>.</p>
      </header>

      <section aria-labelledby="registry-heading" className="mt-12 border-y border-slate-300 py-7">
        <h2 id="registry-heading" className="font-serif text-2xl font-semibold text-slate-950">What was frozen on 9 June 2026</h2>
        <p className="mt-3 max-w-3xl leading-relaxed text-slate-700">The register contains 16 main values, 2 assigned textures and 2 conditional bands. Two additional variants are explicitly excluded from the prediction count. A freeze preserves the formulas and criteria; it does not turn already available measurements into prospective tests.</p>
        <a href="/research/predictions-frozen.json" className="mt-4 inline-flex items-center gap-2 text-sm font-semibold text-blue-700 underline underline-offset-4"><Download size={16} aria-hidden /> Download the unchanged frozen register</a>
      </section>

      <section aria-labelledby="comparisons-heading" className="mt-12">
        <h2 id="comparisons-heading" className="font-serif text-3xl font-semibold text-slate-950">Four dated comparisons</h2>
        <p className="mt-3 max-w-3xl leading-relaxed text-slate-700">Distances below divide the frozen value minus the measured central value by the stated measurement uncertainty. They use no added theory error and are not a combined probability for TFPT.</p>
        <div className="mt-8 divide-y divide-slate-300 border-y border-slate-300">
          {comparisons.map((c) => {
            const row = frozen.get(c.id)!;
            return <article key={c.id} className="grid gap-5 py-8 lg:grid-cols-[minmax(0,1fr)_minmax(0,1.6fr)] lg:gap-12">
              <div>
                <h3 className="font-serif text-2xl font-semibold leading-snug text-slate-950">{c.title}</h3>
                <p className="mt-3 text-sm leading-relaxed text-slate-600">{c.date}</p>
                <a href={c.href} target="_blank" rel="noopener noreferrer" className="mt-3 inline-flex items-center gap-1.5 text-sm text-blue-700 underline underline-offset-4">{c.source}<ExternalLink size={13} aria-hidden /></a>
              </div>
              <div>
                <dl className="grid gap-4 text-sm sm:grid-cols-2">
                  <div><dt className="text-slate-600">Frozen TFPT value</dt><dd className="mt-1 break-words font-mono text-base text-slate-950">{row.frozen_value}{c.id === "BETA_BIREFRINGENCE_DEG" ? "°" : ""}</dd></div>
                  <div><dt className="text-slate-600">Selected measurement</dt><dd className="mt-1 break-words font-mono text-base text-slate-950">{c.measured}</dd></div>
                </dl>
                <p className="mt-4 font-semibold leading-relaxed text-slate-900">{c.result}.</p>
                <p className="mt-2 leading-relaxed text-slate-700">{c.meaning}</p>
                <details className="mt-4 text-sm">
                  <summary className="cursor-pointer py-2 font-semibold text-blue-700 underline-offset-4 hover:underline focus-visible:outline-2 focus-visible:outline-offset-4">Formula, physical premise and failure criterion</summary>
                  <dl className="mt-3 space-y-3 leading-relaxed text-slate-700">
                    <div><dt className="font-semibold text-slate-900">Formula</dt><dd className="break-words">{row.formula}</dd></div>
                    <div><dt className="font-semibold text-slate-900">Physical premise</dt><dd>{row.conditional_on || "The formula is a core numerical readout in the frozen registry. Physical source selection remains a separate research question."}</dd></div>
                    <div><dt className="font-semibold text-slate-900">Committed criterion</dt><dd>{row.kill_criterion}</dd></div>
                    <div><dt className="font-semibold text-slate-900">Timing and comparison scope</dt><dd>{c.history}</dd></div>
                  </dl>
                </details>
              </div>
            </article>;
          })}
        </div>
      </section>

      <section aria-labelledby="assignments-heading" className="mt-14 grid gap-10 lg:grid-cols-2">
        <div>
          <h2 id="assignments-heading" className="font-serif text-2xl font-semibold text-slate-950">Assignments retain their own status</h2>
          <ul className="mt-4 space-y-5">
            {registry.assigned_texture_values.map((r) => <li key={r.id}><h3 className="font-semibold text-slate-900">{r.observable}</h3><p className="mt-1 text-slate-700">{r.formula}. This is an assigned texture value.</p></li>)}
          </ul>
        </div>
        <div>
          <h2 className="font-serif text-2xl font-semibold text-slate-950">Inflation bands need a reheating input</h2>
          <ul className="mt-4 space-y-5">
            {registry.conditional_bands.map((r) => <li key={r.id}><h3 className="font-semibold text-slate-900">{r.observable}</h3><p className="mt-1 text-slate-700">{r.band_min} to {r.band_max}. {r.formula}.</p></li>)}
          </ul>
          <p className="mt-4 text-sm leading-relaxed text-slate-600">These bands share N* and are correlated. They are not two independent parameters derived by the compiler.</p>
        </div>
      </section>

      <section aria-labelledby="searches-heading" className="mt-14 border-t border-slate-300 pt-8">
        <h2 id="searches-heading" className="font-serif text-3xl font-semibold text-slate-950">The historical search record</h2>
        <p className="mt-4 max-w-3xl leading-relaxed text-slate-700">The source inventory dated {new Date(atlas.coverage.attemptInventoryDate).toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric", timeZone: "UTC" })} retains {historical.length} scorecard records. Their original labels describe different tests and evidence classes. A consistency result, a null and a data limited search answer different questions; none alone establishes the physical theory.</p>
        <dl className="mt-6 flex flex-wrap gap-x-8 gap-y-4">
          {Object.entries(statuses).map(([status, count]) => <div key={status}><dt className="text-sm text-slate-600">{status.replaceAll("_", " ")}</dt><dd className="mt-1 font-mono text-lg text-slate-900">{count}</dd></div>)}
        </dl>
        <p className="mt-6 max-w-3xl text-sm leading-relaxed text-slate-600">The catalogue preserves historical, unreviewed attempt metadata. It is distinct from the current source reviewed findings and from a newly executed verification suite. FRB, GW and EHT searches test specified boundary recovery patterns. Downstream scale and cosmological interfaces retain their additional premises.</p>
        <div className="mt-6 flex flex-wrap gap-5 text-sm font-semibold">
          <Link href="/results" className="inline-flex items-center gap-2 text-blue-700 underline underline-offset-4">Explore findings and research history<ArrowRight size={16} aria-hidden /></Link>
          <a href="/research/semantic-atlas.json" className="inline-flex items-center gap-2 text-blue-700 underline underline-offset-4"><Download size={16} aria-hidden /> Download the typed public Atlas</a>
        </div>
      </section>
    </div>
  );
}
