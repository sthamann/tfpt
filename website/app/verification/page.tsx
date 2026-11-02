import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import foundation from "@/lib/foundation-index.json";
import { ModuleCatalog } from "@/components/verification/ModuleCatalog";
import { pageMetadata } from "@/lib/seo";
import { REPO_URL } from "@/lib/utils";
import summary from "@/lib/research-summary.json";
import { VerificationTools } from "./VerificationTools";
import styles from "./verification.module.css";

export const metadata: Metadata = pageMetadata("/verification");

export default async function VerificationPage({ searchParams }: { searchParams: Promise<Record<string, string | string[] | undefined>> }) {
  const params = await searchParams;
  const single = (value: string | string[] | undefined) => typeof value === "string" ? value : "";
  return (
    <div className={`reference-page ${styles.page}`}>
      <header className={styles.header}>
        <Link href="/explain" className={styles.back}>Back to the connections</Link>
        <h1>Follow a result back to its evidence.</h1>
        <p className={styles.lead}>Choose a result, inspect its assumptions, then run the calculation that supports it. Each check answers a specific question. The original status and the scope of that answer stay attached.</p>
        <nav className={styles.actions} aria-label="Verification sections">
          <a href="#first-check" className={styles.primary}>Try one check <ArrowRight size={17} aria-hidden /></a>
          <a href="#module-catalog" className={styles.secondary}>Find a verification module</a>
          <a href="#reproduce" className={styles.textLink}>Reproduce locally</a>
          <a href="#dag" className={styles.textLink}>All technical tools</a>
        </nav>
      </header>
      <section id="first-check" className={styles.section}>
        <div className={styles.sectionIntro}>
          <h2>Start with the E₈ construction.</h2>
          <p>The first module builds the lattice explicitly. It checks the glue, constructs its 240 roots and tests the lattice basis. You can read the source before running it.</p>
        </div>
        <VerificationTools mode="check" />
        <p className={styles.note}>This is a mathematical lattice check. Identifying that lattice with a physical system requires additional arguments and retains its own status.</p>
      </section>
      <section id="module-catalog" className={styles.section}>
        <div className={styles.sectionIntro}><h2>Find the source behind a check.</h2></div>
        <ModuleCatalog modules={foundation.modules} query={single(params.moduleQuery)} cluster={single(params.moduleCluster)} requestedPage={single(params.catalogPage)} />
      </section>
      <section className={styles.section}>
        <div className={styles.sectionIntro}>
          <h2>Different evidence answers different questions.</h2>
          <p>A numerical calculation, a formal theorem and an experimental comparison carry different kinds of information. Follow the source appropriate to the claim.</p>
        </div>
        <dl className={styles.evidence}>
          <div><dt>Python calculations</dt><dd>Inspect the algorithm, its inputs and its negative controls. Run a browser compatible module here, or use the repository for the complete environment.<a href={`${REPO_URL}/tree/main/verification`} className={styles.textLink}>Browse Python sources</a></dd></div>
          <div><dt>Formal mathematics</dt><dd>Read the actual Lean statement and its assumptions. The carrier formalization has a defined mathematical scope.<a href={`${REPO_URL}/tree/main/experiments/lean4-carrier-rigidity`} className={styles.textLink}>Inspect the Lean formalization</a></dd></div>
          <div><dt>Independent implementation</dt><dd>The Wolfram implementation checks algebraic results through a separate computational path. The recorded runs report 116/116 base checks and 603/603 extension checks. This is distinct from external experimental replication.<a href={`${REPO_URL}/tree/main/verification/wolfram`} className={styles.textLink}>Read the Wolfram implementation</a></dd></div>
          <div><dt>Physical comparison</dt><dd>Read each prediction with its freeze, conditions and failure criterion. A passing mathematical check does not decide the experimental comparison.<Link href="/predictions" className={styles.textLink}>Open the prediction register</Link></dd></div>
        </dl>
      </section>
      <section id="reproduce" className={styles.section}>
        <div className={styles.sectionIntro}>
          <h2>Run the same check on your machine.</h2>
          <p>From a checkout of the repository, install its Python requirements and run the first lattice module. The complete suite is a separate step.</p>
        </div>
        <div className={styles.commands}>
          <div><h3>Set up the repository</h3><pre><code>{`git clone ${REPO_URL}.git\ncd tfpt\npython3 -m venv .venv\n.venv/bin/pip install -r requirements.txt`}</code></pre></div>
          <div><h3>Check the E₈ lattice</h3><pre><code>.venv/bin/python verification/v1_e8_glue.py</code></pre><p>Read the individual checks and the final pass or fail result.</p></div>
          <div><h3>Run the registered suite</h3><pre><code>cd verification{`\n`}../.venv/bin/python run_all.py</code></pre><p>The full suite uses the dependencies and source context documented in the repository.</p></div>
        </div>
        <a className={styles.textLink} href={`${REPO_URL}#build-and-maintain`}>Repository setup and maintenance instructions</a>
      </section>
      <section className={styles.section}>
        <div className={styles.sectionIntro}>
          <h2>Read the current claim beside its source.</h2>
          <p>The research snapshot dated {summary.generatedAt.slice(0, 10)} includes the active ledger, reviewed findings and registered scripts. It records source coverage and stated scope; it is not a new execution of every proof or calculation.</p>
        </div>
        <div className={styles.actions}>
          <Link href="/results" className={styles.primary}>Find a result and its premises <ArrowRight size={17} aria-hidden /></Link>
          <a href="/research/status-ledger.csv" className={styles.secondary}>Download the ledger</a>
          <a href="/research/coverage.json" className={styles.textLink}>Inspect snapshot coverage</a>
        </div>
      </section>
      <section id="dag" className={styles.section}>
        <div className={styles.sectionIntro}>
          <h2>Trace the dependencies.</h2>
          <p>Select a node to inspect its inputs, outputs, scope and verification scripts. Browser compatible checks open the same verification viewer; native certificates provide their local command.</p>
        </div>
        <div id="dependency-graph"><VerificationTools mode="graph" /></div>
      </section>
      <section id="technical-archive" className={styles.section}>
        <div className={styles.sectionIntro}>
          <h2>Keep the detailed research in reach.</h2>
          <p>The script index, figures and detailed research interfaces remain available below. This older technical overview preserves its original statements; use the current result inventory to follow later scope corrections.</p>
        </div>
        <VerificationTools mode="archive" />
      </section>
      <nav className={styles.next} aria-label="Continue reading"><Link href="/compiler" className={styles.textLink}>See how the construction connects <ArrowRight size={17} aria-hidden /></Link><Link href="/results" className={styles.textLink}>Explore the discoveries <ArrowRight size={17} aria-hidden /></Link></nav>
    </div>
  );
}
