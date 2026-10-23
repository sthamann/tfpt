import type { Metadata } from "next";
import { SITE_URL } from "@/lib/utils";

// Search descriptions summarize published scope; they do not change claim status.
export const PAGE_SEARCH = {
  "/": [
    "Topological Fixed-Point Theory (TFPT): Research & Papers",
    "Explore TFPT by Stefan Hamann and Alessandro Rizzo: E₈ mathematics, the alpha fixed point, research papers, reproducible checks and open physical questions."
  ],
  "/papers": [
    "Research Papers: E₈, Alpha & the Standard Model",
    "Read the TFPT papers on E₈, the fine-structure constant and Standard Model structure. Open each abstract, inspect its assumptions or download the full PDF."
  ],
  "/verification": [
    "Verification: Python, Wolfram, Lean & Claim Status",
    "Reproduce TFPT calculations with Python, inspect Wolfram and Lean checks, and trace each result to its inputs, source paper and recorded claim status."
  ],
  "/orientation": [
    "What Is TFPT? Assumptions, Results & Reading Guide",
    "Start with Topological Fixed-Point Theory: its two inputs, E₈ construction, alpha equation, research papers and the physical questions that remain open."
  ],
  "/tour": [
    "TFPT Explained: A Guided Tour of the Research",
    "Follow TFPT from its two starting assumptions through E₈ and the alpha fixed point to testable readouts. See what is established and how to check it."
  ],
  "/compiler": [
    "Interactive Compiler: From TFPT Inputs to E₈",
    "Explore how TFPT connects its seam constant and carrier rank to E₈ and Standard Model readouts. An interactive explanation with the assumptions visible."
  ],
  "/falsification": [
    "Falsification: How to Test TFPT Predictions",
    "Inspect the tests that can challenge TFPT: the alpha equation, neutrino mixing, inflation and other readouts, with their assumptions and failure criteria."
  ],
  "/method": [
    "Research Method: Sources, Controls & Verification",
    "See how TFPT tracks assumptions, checks calculations, records failed approaches and separates exact mathematics from conditional physical interpretations."
  ],
  "/review": [
    "Review TFPT: Claims, Evidence & Open Questions",
    "A starting point for reviewing TFPT: the core claims, original assumptions, reproducible calculations, falsification tests and unresolved physical interfaces."
  ],
  "/objections": [
    "TFPT Objections: Evidence, Replies & Status",
    "Review objections to TFPT and follow each reply to its evidence. Covers E₈, physical interpretation, experimental inputs and the remaining research questions."
  ],
  "/replication": [
    "Replication: Reproduce TFPT & Report Results",
    "Find the TFPT code, documents and reproduction steps. See the current replication status and how independent checks can confirm or challenge a result."
  ],
  "/predictions": [
    "TFPT Predictions: Alpha, Neutrinos & Cosmology",
    "Explore TFPT readouts for the fine-structure constant, neutrinos and cosmology. Each entry states its value, assumptions, status and experimental comparison."
  ],
  "/architecture": [
    "TFPT Architecture: E₈, Clocks & Physical Interfaces",
    "Trace the TFPT architecture from seam and carrier inputs to E₈, clocks, Standard Model readouts and conditional gravity interfaces, with sources and status."
  ],
  "/faq": [
    "TFPT FAQ: E₈, the Alpha Equation & Open Questions",
    "What is TFPT? Why does it use E₈? Is its alpha value a fit? Read direct answers about the research programme, its assumptions, evidence and open questions."
  ],
  "/changelog": [
    "Research Changelog: Dated TFPT Updates",
    "Follow dated changes to TFPT papers, calculations and claim status. Historical entries retain their original scope and link to the publication record."
  ],
  "/documentation": [
    "Document Library: TFPT Topics & Original Sources",
    "Find TFPT papers by topic, open the reading guide and trace arguments to original LaTeX sources, verification scripts, claim status and formal references."
  ]
} as const;

export const PAPER_SEARCH: Record<string, readonly [string, string]> = {
  "introduction": [
    "TFPT Reading Guide: Theory, Results & Open Questions",
    "An introduction to TFPT, its assumptions, E₈ compiler and physical readouts. Includes the status assessment, dependency map and routes through the papers."
  ],
  "architecture-e8": [
    "E₈ Compiler & the Fine-Structure Constant",
    "The TFPT architecture paper: seam and carrier inputs, the D₅ and A₃ lattice construction, E₈ closure and the alpha fixed-point equation, with explicit assumptions."
  ],
  "standard-model": [
    "Standard Model Structure & Flavor in TFPT",
    "Read the TFPT paper on Standard Model representations, hypercharge, families and flavor readouts. Inspect the construction, physical assumptions and open transfers."
  ],
  "e8-audit-bootstrap": [
    "E₈ Lattice Audit & Bootstrap",
    "Explore the TFPT E₈ audit and bootstrap: lattice closure, branching checks and consistency relations. The paper states the assumptions and comparison classes."
  ],
  "frontier": [
    "Open Physical Questions in TFPT",
    "The TFPT frontier paper documents conditional physical interfaces and remaining derivations. Follow the assumptions, research contracts and explicit open questions."
  ],
  "redteam": [
    "TFPT Red Team: Objections & Adversarial Checks",
    "Read the adversarial audit of TFPT: counterexamples, failed approaches, physical interface checks and the limits of the mathematical and numerical results."
  ],
  "horizon-readouts": [
    "Horizon Temperatures & the TFPT Unit System",
    "Appendix H compares black-hole, de Sitter and Unruh temperature formulas through a shared normalization. Physical interpretations and open search proposals are marked."
  ],
  "origin-theory": [
    "Origin Theory: Anchors, Clocks & TFPT Structure",
    "Explore the Origin Theory synthesis: anchors, interlocking clocks, E₈ and the shared numerical structure. Physical source selection retains its stated assumptions."
  ],
  "research-contracts": [
    "TFPT Research Contracts & Remaining Interfaces",
    "Inspect the TFPT research contracts for physical interfaces, including assumptions, verification links, scoped results and the remaining conditions for completion."
  ],
  "safeguards": [
    "TFPT Safeguards: Status, Controls & Numerology",
    "How TFPT records assumptions, controls, claim status and failed approaches. Read the safeguards paper and inspect the limits of its mathematical conclusions."
  ],
  "e8-gaussian-code": [
    "E₈, Gaussian Integers & the Hamming Code",
    "A working note on E₈ over Gaussian integers, the extended Hamming code and a four-bit information layer. An algebraic result with its scope stated explicitly."
  ]
};

export function pageMetadata(route: keyof typeof PAGE_SEARCH): Metadata {
  const [title, description] = PAGE_SEARCH[route];
  const url = route === "/" ? SITE_URL : SITE_URL + route;
  return {
    title: route === "/" ? { absolute: title } : title, description,
    alternates: { canonical: url },
    openGraph: {
      type: "website", title, description, url,
      siteName: "Topological Fixed-Point Theory (TFPT)", locale: "en_US",
      images: [{ url: SITE_URL + "/opengraph-image", width: 1200, height: 630, alt: "Topological Fixed-Point Theory (TFPT)" }],
    },
    twitter: { card: "summary_large_image", title, description, images: [SITE_URL + "/opengraph-image"] },
  };
}
