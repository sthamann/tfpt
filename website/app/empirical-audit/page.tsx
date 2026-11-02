import type { Metadata } from "next";
import Link from "next/link";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { SITE_URL } from "@/lib/utils";
import { formatMeasurement, groupDecimal } from "@/lib/format-number";
import { measurementComparisons as comparisons, measurementCheckedDate as checkedDate, signedSigma } from "@/lib/measurement-comparisons";
import { PredictionBandTests } from "@/components/explain/PredictionOverview";
import { predictionById } from "@/lib/frozen-predictions";

export const metadata: Metadata = {
  title: "Dated Measurement Comparisons: TFPT Empirical Audit",
  description: "Ten frozen TFPT values compared with dated NIST, JUNO, NuFIT, PDG, ACT and Planck results, with normalized differences, original assumptions and primary sources.",
  alternates: { canonical: `${SITE_URL}/empirical-audit` },
};

type Attempt = { kind: string; status?: string; verdictRaw?: string };
type Atlas = { attempts: Attempt[]; coverage: { attemptInventoryDate: string } };
const atlas = JSON.parse(readFileSync(join(process.cwd(), "public/research/semantic-atlas.json"), "utf8")) as Atlas;

function DifferencePlot({ id, title, distance }: { id: string; title: string; distance: number }) {
  const position = (value: number) => 32 + ((value + 2) / 5) * 296;
  return <figure className="my-5 max-w-lg">
    <svg viewBox="0 0 360 116" role="img" aria-labelledby={`${id}-plot-title ${id}-plot-description`} className="block h-auto w-full overflow-visible">
      <title id={`${id}-plot-title`}>{`${title}: frozen value at ${signedSigma(distance)} measurement standard uncertainties`}</title>
      <desc id={`${id}-plot-description`}>The measurement center is zero. The shaded band extends from minus one to plus one stated measurement standard uncertainty. The blue point is the frozen value. No theory uncertainty is included.</desc>
      <rect x={position(-1)} y="39" width={position(1)-position(-1)} height="28" fill="#dbe5ef" />
      <line x1={position(-2)} x2={position(3)} y1="53" y2="53" stroke="#61778c" strokeWidth="1" />
      <line x1={position(0)} x2={position(0)} y1="33" y2="72" stroke="#273e53" strokeWidth="1.5" />
      {[-2,-1,0,1,2,3].map(tick => <g key={tick}>
        <line x1={position(tick)} x2={position(tick)} y1="68" y2="74" stroke="#61778c" />
        <text x={position(tick)} y="91" textAnchor="middle" fill="#364f65" fontSize="13">{tick > 0 ? `+${tick}` : tick === 0 ? "0" : `−${Math.abs(tick)}`}</text>
      </g>)}
      <circle cx={position(distance)} cy="53" r="6" fill="#315b84" stroke="#faf9f6" strokeWidth="2" />
      <text x={position(distance)} y="24" textAnchor="middle" fill="#24466a" fontSize="14" fontWeight="600">{signedSigma(distance)}</text>
      <text x="180" y="113" textAnchor="middle" fill="#465d72" fontSize="12">Difference / stated measurement uncertainty</text>
    </svg>
  </figure>;
}

export default function EmpiricalAuditPage() {
  const historical = atlas.attempts.filter(a => a.kind === "scorecard");
  const statuses = historical.reduce<Record<string, number>>((all, a) => {
    const key = a.status || a.verdictRaw || "unclassified";
    all[key] = (all[key] || 0) + 1;
    return all;
  }, {});
  return <article className="reference-page">
    <header className="reference-header">
      <h1>TFPT against dated measurements</h1>
      <p>Compare ten frozen readouts with named measurements. Each comparison keeps the data release, physical premise and original failure criterion attached.</p>
      <p className="reference-note">Primary sources checked {checkedDate}. The formulas remain those in the register frozen on 9 June 2026. Measurements already available at the freeze retain their comparison status.</p>
      <nav className="reference-links" aria-label="Measurement comparison context"><Link href="/predictions">Read the complete frozen register</Link><Link href="/falsification">Inspect the failure criteria</Link></nav>
    </header>
    <section className="reference-section" aria-labelledby="comparison-heading">
      <h2 id="comparison-heading">How far is each frozen value from the measurement?</h2>
      <p>Every plot uses the same scale: the measured central value is zero, the pale band spans its stated ±1 standard uncertainty, and the blue point marks the frozen readout.</p>
      <p className="reference-note">The distance is (frozen value − measured value) / measurement uncertainty alone. It includes no theory error. These ten distances are not a combined theory significance or a global fit.</p>
      <nav className="reference-links" aria-label="Dated comparisons">{comparisons.map(c => <a key={c.id} href={`#${c.id}`}>{c.title}</a>)}</nav>
      {comparisons.map(c => {
        const row = predictionById(c.id);
        return <section key={c.id} id={c.id} className="scroll-mt-24 border-t border-slate-300 py-8 mt-6" aria-labelledby={`${c.id}-heading`}>
          <div className="grid gap-5 lg:grid-cols-[minmax(0,1fr)_minmax(0,1.15fr)] lg:gap-12">
            <div>
              <h3 id={`${c.id}-heading`} className="font-serif text-2xl font-semibold text-slate-950">{c.title}</h3>
              <p className="mt-3 text-sm leading-relaxed text-slate-700">{c.date}</p>
              <p className="mt-4 text-slate-900"><span className="block text-sm text-slate-600">Selected measurement</span><span className="tabular-nums">{formatMeasurement(c.measured)}</span></p>
              <a href={c.href} target="_blank" rel="noopener noreferrer" className="mt-3 inline-block py-2 text-sm text-blue-800 underline underline-offset-4">{c.source}</a>
            </div>
            <div>
              <DifferencePlot id={c.id} title={c.title} distance={c.sigma} />
              <p className="font-semibold leading-relaxed text-slate-900">{c.result}.</p>
              <p className="mt-2 leading-relaxed text-slate-700">{c.meaning}</p>
            </div>
          </div>
          <details className="mt-5">
            <summary className="cursor-pointer py-2 font-medium text-blue-800">Exact frozen value, assumptions and comparison history</summary>
            <dl className="mt-4 grid gap-4 text-sm leading-relaxed sm:grid-cols-[11rem_minmax(0,1fr)]">
              <dt className="font-semibold">Exact frozen value</dt><dd className="break-all font-mono">{row.frozen_value && groupDecimal(row.frozen_value)}{c.id === "BETA_BIREFRINGENCE_DEG" ? "°" : ""}</dd>
              <dt className="font-semibold">Formula</dt><dd className="break-words font-mono">{row.formula}</dd>
              <dt className="font-semibold">Physical premise</dt><dd>{row.conditional_on || "The frozen numerical readout retains the source and physical transfer conditions of its branch."}</dd>
              <dt className="font-semibold">Committed criterion</dt><dd>{row.kill_criterion}</dd>
              <dt className="font-semibold">Timing and scope</dt><dd>{c.history}</dd>
            </dl>
            <Link href={`/falsification#${c.id}`} className="mt-4 inline-block py-2 text-sm text-blue-800 underline underline-offset-4">Read the criterion in context</Link>
          </details>
        </section>;
      })}
    </section>
    <PredictionBandTests />
    <section className="reference-section" aria-labelledby="register-scope-heading">
      <h2 id="register-scope-heading">Use the right kind of statement</h2>
      <p>The complete register distinguishes main values, assigned textures and conditional inflation bands. Assigned phases are not derivations; the two inflation bands share the external reheating input N★. Their exact values and criteria are kept together on the register page.</p>
      <nav className="reference-links" aria-label="Register classes"><Link href="/predictions#assigned">Assigned textures</Link><Link href="/predictions#bands">Conditional bands</Link></nav>
    </section>
    <section id="searches-heading" className="reference-section" aria-labelledby="search-history-title">
      <h2 id="search-history-title">Historical searches have a separate record</h2>
      <p>The dated search catalogue preserves original attempt metadata. A consistency result, a null and a data limited search answer different questions. Their labels are not new experimental confirmations or source reviewed findings.</p>
      <details className="mt-5">
        <summary className="cursor-pointer py-2 font-medium text-blue-800">Inspect the dated search inventory</summary>
        <p className="mt-4 text-sm leading-relaxed">The inventory dated {new Date(atlas.coverage.attemptInventoryDate).toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric", timeZone: "UTC" })} contains {historical.length} scorecard records. These counts describe that catalogue, not a newly executed suite.</p>
        <dl className="mt-5 flex flex-wrap gap-x-8 gap-y-4">{Object.entries(statuses).map(([status,count]) => <div key={status}><dt className="text-sm text-slate-600">{status.replaceAll("_", " ")}</dt><dd className="tabular-nums text-slate-900">{count}</dd></div>)}</dl>
        <a href="/research/semantic-atlas.json" className="mt-4 inline-block py-2 text-sm text-blue-800 underline underline-offset-4">Download the typed public atlas</a>
      </details>
      <Link href="/results?tab=history" className="mt-4 inline-block py-2 text-blue-800 underline underline-offset-4">Explore the research history</Link>
    </section>
  </article>;
}
