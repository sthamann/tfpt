import type { Metadata } from "next";
import Link from "next/link";
import { pageMetadata } from "@/lib/seo";
import summary from "@/lib/research-summary.json";

export const metadata: Metadata = pageMetadata("/method");

const assessment = [
  { title: "State the inputs", text: "Begin with the actual structures supplied by P1 and P2, including the boundary assumptions and the marked carrier. A compressed numerical description does not replace these premises." },
  { title: "Separate proof from calculation", text: "A lattice identity, an analytic theorem and a numerical enclosure establish different statements. Inspect the mathematical object, the allowed class and the error control used for the particular result." },
  { title: "Name the physical identification", text: "Reading a representation as particle content, a source response as a measured coupling, or a scale relation as an observable adds a physical connection. Its assumptions remain attached to the result." },
  { title: "Compare with dated observations", text: "Record the experimental quantity, measurement convention, uncertainty and reference date. A formula frozen after an observable was measured is a comparison with known data. A prospective test needs its actual commitment date." },
  { title: "Retain the counterexample", text: "When a construction fails, record exactly which premise or class the counterexample excludes. Preserve the mathematical result that survives and revise the physical connection it no longer supports." },
];

export default function MethodPage() {
  return <article className="reference-page">
    <header className="reference-header">
      <h1>How a TFPT result is assessed</h1>
      <p>Follow the statement from its declared inputs to its mathematical result, physical interpretation and comparison with observation. Each step answers a different question.</p>
    </header>
    <section className="reference-section" id="pipeline">
      <h2>Read the reasoning in order</h2>
      <ol className="reference-rows list-decimal space-y-6 pl-6">
        {assessment.map((step) => <li key={step.title}><h3>{step.title}</h3><p>{step.text}</p></li>)}
      </ol>
      <nav className="reference-links" aria-label="A worked example">
        <Link href="/explain#matter">Work through the charge construction</Link>
        <Link href="/explain#alpha">Follow the alpha equation and its scope</Link>
      </nav>
    </section>
    <section className="reference-section" id="status">
      <h2>Two records, with their original scope</h2>
      <dl className="reference-rows">
        <div><dt>The published claim ledger</dt><dd>The snapshot contains {summary.counts.ledgerActive.toLocaleString("en-US")} active claims. Each row records a claim, its type, dependencies and verification references. The public [E], [C], [O] and [X] markers are a compact display of that more detailed record.</dd></div>
        <div><dt>Source reviewed research findings</dt><dd>The same library includes {summary.counts.reviewedFindings.toLocaleString("en-US")} reviewed findings from later research. Their established, conditional or excluded scope remains distinct from the published ledger. A reviewed finding does not silently promote its parent physical goal.</dd></div>
      </dl>
      <p className="reference-note">Snapshot generated {summary.generatedAt.slice(0, 10)}. Record counts describe coverage. They are separate from executed proof checks, independent replications and experimental confirmations.</p>
      <nav className="reference-links" aria-label="Inspect the records">
        <Link href="/results">Inspect statements, premises and original sources</Link>
        <Link href="/explain#status">Understand the status markers</Link>
      </nav>
    </section>
    <section className="reference-section" id="numbers">
      <h2>What the verification tools establish</h2>
      <p>The Python registry lists {summary.counts.registeredScripts.toLocaleString("en-US")} modules. A module can contain several assertions or numerical tests. Wolfram supplies another calculation path for selected results; Lean formalizes particular mathematical statements under their encoded premises. None of these inventories reports a new execution by itself.</p>
      <p>For a result you intend to use, read the script or theorem statement and its controls, then reproduce that result. A source consistency audit checks the agreement of records and generated pages; it does not run every mathematical proof.</p>
      <nav className="reference-links" aria-label="Reproduce a result"><Link href="/verification">Choose a verification path</Link><Link href="/replication">Reproduce a claim and report the outcome</Link></nav>
    </section>
    <section className="reference-section" id="graveyard">
      <h2>Searches, tests and exclusions</h2>
      <p>Exploration produces candidates before it produces established claims. For a declared test, inspect when its success and failure criteria were written, the alternatives actually tested and the outcome. Preregistration is a property of that dated test, rather than a label applied to all research retrospectively.</p>
      <p>Formula censuses and null models can answer questions within a specified grammar and comparison window. Their score is conditional on that choice. It does not give a calibrated probability that the whole physical theory is correct.</p>
      <nav className="reference-links" aria-label="Tests and corrections">
        <Link href="/falsification">Inspect test targets and failure criteria</Link>
        <Link href="/results?tab=results&status=excluded_scoped">Read scoped exclusions in the result library</Link>
        <Link href="/results?search=metric-dtn-form-bound-needs-transfer-comparison-for-gap">An example: the corrected metric gap argument</Link>
      </nav>
    </section>
    <section className="reference-section" id="red-team">
      <h2>A worked adversarial test: which cuts preserve positivity?</h2>
      <p>Paper 5 tests a condition needed for quantum reconstruction: reflection positivity. In its finite model of sixteen Majorana modes, a reflection divides the observables across a cut. The resulting norm form must be nonnegative to define the reconstructed state space.</p>
      <ol className="reference-rows list-decimal space-y-6 pl-6">
        <li><h3>Add an interaction that can break the condition</h3><p>The test adds the specified quartic interaction and varies the cut. The reflection operator still exists and respects the Hamiltonian, so those checks alone cannot settle positivity.</p></li>
        <li><h3>Keep both the failure and the surviving cuts</h3><p>In the tested model, cuts splitting an interacting quartet into one mode on one side and three on the other produce negative norm directions. Quartet avoiding cuts survive. The later refinement also finds positive symmetric two plus two cuts. Crossing the interaction is therefore insufficient to predict failure; its actual split matters.</p></li>
        <li><h3>Use the failure to constrain the next construction</h3><p>The follow-up tests the stated interacting mark family, both coupling signs and its admissible cuts. On the tested coupling grid, exactly one member and sign survive: the symmetric configuration δ = π/2 with positive coupling. This is a concrete selection result within that finite family.</p></li>
      </ol>
      <p>The result concerns one finite toy model and its specified interaction class. It does not derive the physical seam or complete the interacting continuum construction. The broader OS twistor contract, WOIT.OS.TWISTOR.01, remains open in this paper. A passing test can therefore certify a counterexample or a restricted survivor, rather than confirm the whole theory.</p>
      <nav className="reference-links" aria-label="Original adversarial test and scope">
        <Link href="/documentation?section=section%3A3bc2480a0b64fd3112f1">Read Paper 5, Target G, including the odd split refinement</Link>
        <Link href="/results?search=WOIT.OS.TWISTOR.01">Inspect the parent contract and later results</Link>
      </nav>
    </section>
    <section className="reference-section" id="reverse-audit">
      <h2>Check what the structure leaves unused</h2>
      <p>The safeguards paper also runs a reverse audit. Of the eight E₈ Casimir degrees, its map assigns primary readouts to degrees 2, 8 and 30. The remaining five, 12, 14, 18, 20 and 24, stay visible as structure without a primary readout. This audit records the stated mapping and its unused content; a degree appearing in the map does not by itself derive a physical observable.</p>
      <nav className="reference-links" aria-label="Reverse audit source"><Link href="/documentation?section=section%3A5accfde4a70bd57ce618">Read the safeguards reverse audit</Link></nav>
    </section>
    <section className="reference-section" id="ai">
      <h2>Tools assist the work; sources support the result</h2>
      <p>AI can assist with searches, calculations, code and drafting. The evidence for a result remains its original derivation, explicit assumptions and reproducible checks. A fluent explanation, generated summary or a matching source hash does not substitute for that evidence.</p>
    </section>
  </article>;
}
