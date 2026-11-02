import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight, ExternalLink } from "lucide-react";
import { pageMetadata } from "@/lib/seo";
import { CompilerExplorer } from "./CompilerExplorer";
import styles from "./compiler.module.css";

export const metadata: Metadata = pageMetadata("/compiler");

export default function CompilerPage() {
  return <div className={styles.page}>
    <header className={styles.header}>
      <Link href="/explain" className={styles.back}>Back to the worked derivations</Link>
      <h1>Inspect a concrete construction.</h1>
      <p className={styles.lead}>Explore the E₈ lattice: inspect its root coordinates, follow its stated construction and run the lattice check. The system map shows the wider dependencies; the knowledge atlas records the claims and their scope.</p>
    </header>
    <CompilerExplorer />
    <section className={styles.section}>
      <h2>Connect the example to the wider theory.</h2>
      <p>The compiler gives a common mathematical language for lattice structure, clock operations and readouts. Each claimed physical connection has its own premises and evidence.</p>
      <nav className={styles.reading} aria-label="Compiler reading routes">
        <Link href="/papers/architecture-e8"><strong>Architecture and the E₈ construction</strong><span>The inputs, glue and electromagnetic closure <ArrowRight size={17} aria-hidden /></span></Link>
        <Link href="/papers/standard-model"><strong>Representations and flavor</strong><span>The Standard Model readout and its transport layer <ArrowRight size={17} aria-hidden /></span></Link>
        <Link href="/results"><strong>Discoveries with their scope</strong><span>Original claims, reviewed findings and negative results <ArrowRight size={17} aria-hidden /></span></Link>
      </nav>
    </section>
    <section className={styles.section}>
      <h2>The earlier animated machine remains available.</h2>
      <p>Its animation and prediction board are a historical presentation. The current result inventory carries later research and scope corrections.</p>
      <a href="/compiler/index.html?v=4" target="_blank" rel="noopener noreferrer" className={styles.link}>Open the original machine in a separate view <ExternalLink size={16} aria-hidden /></a>
    </section>
  </div>;
}
