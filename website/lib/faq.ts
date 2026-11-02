import summary from "@/lib/research-summary.json";

/** The visible FAQ and its FAQPage structured data share these exact answers. */
export interface FaqItem {
  q: string;
  a: string;
  sources: { label: string; href: string }[];
}

export const FAQ_ITEMS: FaqItem[] = [
  {
    q: "What is Topological Fixed-Point Theory?",
    a: "TFPT is a research programme by Stefan Hamann and Alessandro Rizzo. It connects an oriented boundary structure and a five slot carrier to representations, E₈ lattice structure, flavour relations and numerical readouts. Its mathematical results retain their assumptions. Connecting the whole construction to one physical source remains a separate research goal.",
    sources: [{ label: "Work through the construction", href: "/explain" }],
  },
  {
    q: "What does TFPT say about the fine structure constant?",
    a: "A specified boundary equation has a unique positive root giving α⁻¹ ≈ 137.03599921684. The equation includes an alpha dependent response, so the complete function is more than a cubic polynomial. Its mathematical root and the derivation of its actual electromagnetic origin are separate statements.",
    sources: [{ label: "Equation, root and physical connection", href: "/explain#alpha" }, { label: "The analytic root result", href: "/results?search=alpha-global-positive-root" }],
  },
  {
    q: "Is TFPT a completed physical theory of everything?",
    a: "A completed physical theory of everything has not been established. The mathematical construction already contains precise particle, charge, flavour, quantum and source results. A common local physical realization, the actual observables and events, physical spacetime and gravity still have distinct obligations. A solved subproblem retains its value while its parent goal remains open.",
    sources: [{ label: "Physical source and remaining connections", href: "/explain#source" }, { label: "Results in their stated scope", href: "/results" }],
  },
  {
    q: "What role does E₈ play?",
    a: "E₈ appears as the positive even unimodular lattice obtained from the specified carrier and family glue. It is a closure and consistency object. This construction does not identify E₈ itself as the unbroken physical gauge group. The particle representations and their physical interpretation need their own explicit maps and premises.",
    sources: [{ label: "Follow the lattice construction", href: "/explain#e8" }, { label: "Lattice results and sources", href: "/results?search=glue" }],
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
    a: "The central question is the common original physical source: how its local fields, state, time, admissible events and gravitational response are realized together. Later research supplies local source constructions, intrinsic event geometry and explicit response results under named premises. These achievements narrow the remaining connection without establishing physical 3+1 dimensional spacetime or a complete gravitational theory.",
    sources: [{ label: "The common physical source", href: "/explain#source" }, { label: "Current source research", href: "/results?search=source" }],
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
