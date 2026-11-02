import type { Metadata } from "next";
import Link from "next/link";
import { pageMetadata } from "@/lib/seo";
import { REPO_URL } from "@/lib/utils";
import summary from "@/lib/research-summary.json";

export const metadata: Metadata = pageMetadata("/replication");

const setup = ["git clone " + REPO_URL + ".git", "cd tfpt", "python3 -m venv .venv", ".venv/bin/pip install -r requirements.txt", ".venv/bin/python verification/verify_quick.py"].join("\n");

export default function ReplicationPage() {
  return <article className="reference-page">
    <header className="reference-header">
      <h1>Reproduce one result, from source to outcome</h1>
      <p>Choose a precise claim, retain its premises and run the calculation that supports it. A useful reproduction records what ran, what it returned and which broader questions it leaves unchanged.</p>
    </header>
    <section className="reference-section" id="start">
      <h2>Start with a claim you can inspect</h2>
      <ol className="reference-rows list-decimal space-y-6 pl-6">
        <li><h3>Choose the statement</h3><p>Open a result and note its claim or finding identifier, assumptions, source revision and verification references. The charge construction or the specified alpha root gives a manageable first example.</p></li>
        <li><h3>Select the appropriate environment</h3><p>The verification page offers browser compatible calculations. Use the repository for modules needing native libraries, interval arithmetic or preserved experimental sources. A successful browser demonstration does not replace a native certificate.</p></li>
        <li><h3>Record the actual outcome</h3><p>Keep the command, tool versions, input, output and any failed assertion. State whether you reproduced an identity, a numerical interval or a conditional construction. Include a counterexample or missing prerequisite when the attempt fails.</p></li>
      </ol>
      <nav className="reference-links" aria-label="Choose a result to reproduce">
        <Link href="/results">Find the claim and its original sources</Link>
        <Link href="/verification#first-check">Open the browser verification tools</Link>
      </nav>
    </section>
    <section className="reference-section" id="python">
      <h2>Run the published Python checks locally</h2>
      <p>From a terminal, clone the public repository and use its documented environment. These commands run from the repository root:</p>
      <pre><code>{setup}</code></pre>
      <p>The concise core check is a starting point. To execute the full registered Python suite in that environment:</p>
      <pre><code>.venv/bin/python verification/run_all.py</code></pre>
      <p>The snapshot registers {summary.counts.registeredScripts.toLocaleString("en-US")} modules, rather than that many checks or independent proofs. Some modules consume experimental sources at their original relative paths. Native interval modules, including v1022, v1025 and v1026, require their stated python-flint/Arb environment.</p>
      <p className="reference-note">These commands are instructions for a reproduction. This page does not report a fresh run or assert that all checks passed on your machine.</p>
      <nav className="reference-links" aria-label="Python source instructions">
        <a href={REPO_URL + "/blob/main/README.md"}>Repository setup instructions</a>
        <a href={REPO_URL + "/blob/main/verification/README.md"}>Verification working directory and module requirements</a>
      </nav>
    </section>
    <section className="reference-section" id="other-tools">
      <h2>Wolfram and Lean cover specific statements</h2>
      <dl className="reference-rows">
        <div><dt>Wolfram</dt><dd>The published record reports 116/116 base checks and 603/603 extension checks. This is a second calculation path for its listed algebraic, identity and lattice results. It is a recorded result with that scope, rather than a new Wolfram execution or an external replication of the whole programme.</dd></div>
        <div><dt>Lean</dt><dd>The formalization covers named mathematical statements, including carrier and charge results. Read each theorem, its imported assumptions and the relevant audit instructions. A scoped formalization does not establish the full Standard Model or certify a physical interpretation.</dd></div>
      </dl>
      <p>Python execution, Wolfram evaluation, Lean elaboration and source consistency audits are separate operations. Report which you actually performed and preserve the corresponding output.</p>
      <nav className="reference-links" aria-label="Inspect the other verification paths">
        <Link href="/verification">Verification paths and their scope</Link>
        <a href={REPO_URL + "/tree/main/experiments/lean4-carrier-rigidity"}>Inspect the Lean carrier project</a>
      </nav>
    </section>
    <section className="reference-section" id="external">
      <h2>Independent reports and disagreements</h2>
      <p>Our public replication register currently contains no published independent reproduction report. This describes the register maintained by the project. Internal Python, Wolfram and Lean work should be assessed separately from a report by an outside researcher.</p>
      <p>A report can confirm a narrow result, reproduce only part of it, dispute an inference or identify a failure. Link to the precise source and explain the boundary of your conclusion. That makes a negative result as useful to the next reader as a successful reproduction.</p>
      <nav className="reference-links" aria-label="Submit or review a reproduction">
        <a href={REPO_URL + "/issues"}>Share a reproduction or failed attempt</a>
        <Link href="/objections">Read the objection record</Link>
      </nav>
    </section>
  </article>;
}
