import summary from "@/lib/research-summary.json";
import { PROJECT_SUMMARY, topicGuide } from "@/lib/topic-guides";

/** The visible FAQ and its FAQPage structured data share these exact answers. */
export interface FaqItem {
  q: string;
  a: string;
  sources: { label: string; href: string }[];
}

export const FAQ_ITEMS: FaqItem[] = [
  {
    q: "What is Topological Fixed-Point Theory?",
    a: PROJECT_SUMMARY,
    sources: [{ label: "Work through the construction", href: "/explain" }],
  },
  {
    q: "What does TFPT say about the fine structure constant?",
    a: topicGuide("alpha").answer,
    sources: [{ label: "Equation, root and physical connection", href: "/fine-structure-constant" }, { label: "The analytic root argument", href: "/research/alpha-fixed-point-proof" }],
  },
  {
    q: "Is TFPT a completed physical theory of everything?",
    a: "A completed physical theory of everything has not been established. The mathematical construction already contains precise particle, charge, flavour, quantum and source results. The original source route already reconstructs its state, vacuum and time jointly under its stated hypotheses. A complete interacting physical realization, its chiral and infrared behavior, and universal gravitational coupling retain their own obligations.",
    sources: [{ label: "Physical source and remaining connections", href: "/explain#source" }, { label: "Results in their stated scope", href: "/results" }],
  },
  {
    q: "What role does E₈ play?",
    a: topicGuide("e8").answer,
    sources: [{ label: "E₈ and the Standard Model", href: "/e8-standard-model" }, { label: "The discriminant glue argument", href: "/research/e8-discriminant-glue" }],
  },
  {
    q: "Why does TFPT have three fermion generations?",
    a: topicGuide("families").answer,
    sources: [{ label: "Three fermion generations", href: "/three-fermion-generations" }, { label: "The four mark divisor argument", href: "/research/four-mark-divisor" }],
  },
  {
    q: "Where does experimental input enter?",
    a: "The records distinguish construction inputs from comparisons with measured quantities. Each comparison must state its measurement convention, reference date and uncertainty. Some physical readouts also need declared inputs, such as a dimensional calibration or a cosmological history. Check those dependencies for the particular claim rather than assuming that every displayed number has the same origin.",
    sources: [{ label: "Registered values, assignments and conditional bands", href: "/predictions" }, { label: "How evidence is assessed", href: "/method" }],
  },
  {
    q: "What is actually fitted or supplied?",
    a: "The dimensionless compiler relations are evaluated under their stated inputs, including P1, P2 and the specified mathematical dictionary. Those inputs contain geometric and operator structure, beyond two numerical values. Dimensional quantities require a calibration; conditional physical branches can require additional state, scale or cosmological assumptions. A fixed formula does not derive the physical choice of all its premises.",
    sources: [{ label: "Inspect the starting assumptions", href: "/explain#inputs" }, { label: "Find a result and its premises", href: "/results" }],
  },
  {
    q: "How do you distinguish the results from numerology?",
    a: "Inspect an actual construction: its inputs, allowed operations, derived quantity and counterexamples. The project also records formula censuses and null models. Their outcomes depend on a declared grammar and comparison window; they are not a probability that the full physical theory is true. Reproducing the derivation and testing its physical connection remain separate tasks.",
    sources: [{ label: "Assessment method and test scope", href: "/method" }, { label: "Reproduce a result", href: "/replication" }],
  },
  {
    q: "What could rule out a claim?",
    a: "A counterexample can refute a mathematical statement under its actual premises. A failed calculation can invalidate the result it was meant to reproduce. An observation can exclude a physical readout under its declared conditions. These failures have different scopes: excluding a particular interaction or cosmological branch does not automatically exclude every underlying lattice identity.",
    sources: [{ label: "Targets and failure criteria", href: "/falsification" }, { label: "Recorded exclusions and corrections", href: "/results?tab=results&status=excluded_scoped" }],
  },
  {
    q: "What is still open?",
    a: "The central task is to identify the full original interacting source with its actual field insertions, admissible projection and time, retaining the dynamical bosonic weight and all remaining couplings. Complete reference transport, vacuum reconstruction and the whole classical Clifford transfer are already available in their stated scopes. The next calculation must use that full physical source; a separate choice of vacuum or an optional DET16 parent does not replace it.",
    sources: [{ label: "The common physical source", href: "/explain#source" }, { label: "Current source research", href: "/results?search=source" }],
  },
  {
    q: "What does the latest transfer calculation exclude?",
    a: "For the given unprojected quasifree positive heat source, the complete kernel is calculated. A partition function theorem excludes a literal independent flat factor of dimension greater than two under any unitary field identification that preserves that same transfer and boundary sewing. Physical Gauss projection, dynamical bosons and a general interacting source are outside this theorem. A larger declared interacting source also has nonzero charged transitions carried jointly by fields and environment. Its derivation from the primitive source is still a separate equation.",
    sources: [{ label: "Whole source calculation and scope", href: "/explain#source" }, { label: "Consolidated source results", href: "/results?record=finding%3Ar110-consolidated-source-results-and-atlas-provenance-audit" }],
  },
  {
    q: "Why compare alpha with CODATA at about 1.9 standard deviations?",
    a: "The published formula gives α⁻¹ = 137.0359992168, compared with CODATA 2022 at 137.035999177(21). The difference is about 1.9 standard deviations of that adjustment. Alpha was measured before the formula freeze, so this is a dated comparison with known data. It does not become a blind prediction through later registration.",
    sources: [{ label: "See the comparison and its meaning", href: "/explain#alpha" }, { label: "Prediction categories and freeze date", href: "/predictions" }],
  },
  {
    q: "What do the result counts and status labels mean?",
    a: "The snapshot includes " + summary.counts.ledgerActive.toLocaleString("en-US") + " active published ledger claims and " + summary.counts.reviewedFindings.toLocaleString("en-US") + " source reviewed research findings. These are two records with their own scopes. The [E], [C], [O] and [X] display markers help distinguish established statements, conditional readings, open or supplied inputs, and tests or exclusions. A count is an inventory, rather than that many independent physical confirmations.",
    sources: [{ label: "Read the status definitions", href: "/explain#status" }, { label: "Inspect the result library", href: "/results" }],
  },
];
