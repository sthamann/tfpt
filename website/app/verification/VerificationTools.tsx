"use client";

import { useEffect, useState } from "react";
import dynamic from "next/dynamic";
import { Play, FileCode2 } from "lucide-react";
import { useReproducer } from "@/components/Reproducer";
import styles from "./verification.module.css";

const Archive = dynamic(() => import("./VerificationArchive"), {
  loading: () => <p role="status">Loading the technical overview…</p>,
});
const Graph = dynamic(() => import("@/components/VerificationDag").then(module => module.VerificationDag), {
  loading: () => <p role="status">Loading the dependency graph…</p>,
});

export function VerificationTools({ mode }: { mode: "check" | "archive" | "graph" }) {
  const { open } = useReproducer();
  const [expanded, setExpanded] = useState(false);

  useEffect(() => {
    if (mode === "check") return;
    const followAnchor = () => {
      const id = window.location.hash.slice(1);
      const graphTarget = ["dag", "dependency-graph"].includes(id);
      const archiveTarget = ["open-gates", "research-20260909", "research-20260909-title", "non-rh-round27", "technical-archive"].includes(id);
      if ((mode === "graph" && graphTarget) || (mode === "archive" && archiveTarget)) setExpanded(true);
    };
    followAnchor();
    window.addEventListener("hashchange", followAnchor);
    return () => window.removeEventListener("hashchange", followAnchor);
  }, [mode]);

  if (mode === "check") return (
    <div className={styles.check}>
      <dl><div><dt>Question</dt><dd>Does the explicit construction give the even, unimodular E₈ lattice?</dd></div><div><dt>What is tested</dt><dd>Shared ℤ₄ discriminant data; glue norms 5/4 + 3/4 = 2; 240 roots of squared length 2; an integral, even basis with determinant 1.</dd></div></dl>
      <div className={styles.actions}>
        <button className={styles.primary} type="button" onClick={() => open("v1_e8_glue.py")}><Play size={16} aria-hidden /> Run the lattice check</button>
        <a href="/verification/v1_e8_glue.py" className={styles.secondary}><FileCode2 size={17} aria-hidden /> Read the Python source</a>
      </div>
      <p className={styles.note}>Python runs in your browser using Pyodide. The first run downloads the runtime. Its output appears in the existing verification viewer, including any failure and the local reproduction command.</p>
    </div>
  );

  return <details className={styles.archive} open={expanded} onToggle={event => setExpanded(event.currentTarget.open)}>
    <summary>{mode === "graph" ? "Explore the complete dependency graph" : "Open the script index, figures and research details"}</summary>
    {expanded && <div className={`${styles.archiveBody} ${mode === "graph" ? styles.graph : ""}`}>{mode === "graph" ? <Graph /> : <Archive />}</div>}
  </details>;
}
