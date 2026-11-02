"use client";

import Link from "next/link";
import { ArrowDown, ArrowRight } from "lucide-react";
import { OutputPlate, MechanismWalkthrough } from "./LearningFigures";

const outcomes = [
  { title: "Particles & charges", short: "Particles", second: "& charges", text: "The representations and charges of one Standard Model family, with a separate geometric construction for three families.", scope: "Representation and charge results", query: "hypercharge", href: "/explain#matter" },
  { title: "Masses & mixing", short: "Masses", second: "& mixing", text: "Relative charged lepton and quark source masses, a common hierarchy and specified constructions for particle mixing.", scope: "Source relations; physical mass transfer has its own conditions", query: "flavor", href: "/explain#flavor" },
  { title: "Electromagnetic coupling", short: "Electromagnetic", second: "coupling α", text: "A fixed boundary equation with one positive root close to the measured electromagnetic coupling. The equation, its root and its physical origin are distinct results.", scope: "Mathematical closure; physical identification remains a separate task", query: "alpha-global-positive-root", href: "/explain#alpha" },
  { title: "Cosmological readouts", short: "Cosmic", second: "patterns", text: "Conditional readouts for the rotation of polarized light, the ordinary matter fraction, early cosmic expansion and the vacuum energy hierarchy.", scope: "Conditional physical readouts and dated predictions", query: "cosmo", href: "/predictions" },
  { title: "Quantum & information structure", short: "Quantum", second: "structure", text: "Exact connections between the E₈ lattice, coding and finite quantum geometry. Source histories can preserve information that a compressed readout loses.", scope: "Scoped mathematical and source reconstruction results", query: "quartic", href: "/explain#quantum" },
  { title: "Clocks & dynamics", short: "Clocks", second: "& dynamics", text: "Related finite clock actions, exact relaxation in the specified transfer model and constructed state and time bridges.", scope: "Operator relations; physical time and a common source remain separate", query: "clock", href: "/explain#clocks" },
];

export function BigPictureHero() {
  return <section className="big-picture-hero learning-hero" aria-labelledby="big-picture-title"><div className="experience-shell big-picture-layout">
    <div className="big-picture-copy"><h1 id="big-picture-title">From a common structure to particles and constants.</h1>
      <p className="big-picture-lead">TFPT studies whether the particle content and constants of nature can be explained together. Its construction already fixes charge assignments, mass relations and a boundary equation for the electromagnetic coupling.</p>
      <p className="big-picture-route">Start with the outputs. Then inspect the actual maps, shared inputs and calculations that connect them.</p>
      <div className="experience-actions"><a href="#outcomes" className="experience-primary">Explore the results <ArrowDown size={18} aria-hidden /></a><a href="#connections" className="experience-secondary">See how it works <ArrowRight size={18} aria-hidden /></a></div>
      <p className="experience-byline">Topological Fixed-Point Theory · Stefan Hamann & Alessandro Rizzo</p>
    </div><OutputPlate/>
  </div></section>;
}

export function OutcomeAtlas() {
  return <section className="experience-shell outcome-atlas" id="outcomes" aria-labelledby="outcome-title">
    <div className="experience-heading"><h2 id="outcome-title">What does the theory determine?</h2><p>Several parts of physics become outputs of the same specified construction. Some are exact mathematical results; others are conditional physical readouts. A complete physical realization remains an open research goal.</p></div>
    <div className="outcome-list">{outcomes.map(item=><article key={item.title}><h3><Link href={item.href}>{item.title} <ArrowRight size={20} aria-hidden /></Link></h3><div><p>{item.text}</p><p className="outcome-scope">{item.scope}. <Link href={`/results?search=${encodeURIComponent(item.query)}`}>Inspect the evidence</Link>.</p></div></article>)}</div>
    <p className="parameter-intro" id="parameter-definition"><strong>“Parameter free” within a specified branch:</strong> no separate fitted number for each output. The starting inputs and any physical calibration conditions remain part of the claim.</p>
    <details className="parameter-meaning"><summary>What does “parameter free” mean here?</summary><p>Within a specified branch, the inputs fix the stated output. A separate fitted number is not supplied for every observable. The boundary normalization, carrier, marking, transport rules and branch choices still belong to the starting construction. Some physical readouts also require scale calibration, mass scheme transfer or cosmological assumptions. Those conditions remain attached to the result.</p><Link className="guide-link" href="/explain#inputs">Inspect the starting inputs</Link><Link className="guide-link" href="/predictions">Distinguish predictions, assigned values and conditional bands</Link></details>
  </section>;
}

export function ConnectionStory() { return <MechanismWalkthrough/>; }

export function MethodAndDiscoveries() {
  return <div className="experience-shell">
    <section className="method-story" id="method-overview"><div className="experience-heading"><h2>How does the construction work?</h2><p>Start with declared inputs, apply explicit maps, then compare the resulting statements with mathematics and measurement.</p></div>
      <ol className="method-path"><li><h3>Specify the starting structure.</h3><p>An oriented boundary and a marked internal carrier. Their normalization and rules are explicit inputs.</p><Link href="/explain#inputs">Starting inputs</Link></li><li><h3>Construct representations and operators.</h3><p>Exterior algebra, lattice matching and transport rules produce the particle sectors and connected readout operators.</p><Link href="/explain#matter">A worked charge example</Link></li><li><h3>Calculate, prove and test.</h3><p>Separate exact identities and numerical outputs from physical assumptions. Compare predictions with data and preserve scoped exclusions.</p><Link href="/verification">Verification and reproduction</Link></li></ol>
      <p className="method-open"><strong>The common physical origin remains the central task.</strong> The constructed pieces do not yet amount to a complete interacting quantum theory in physical spacetime with three spatial dimensions and time. The actual source, state, dynamics and gravity have their own open connections.</p>
    </section>
    <section className="discovery-story" id="discoveries"><div className="experience-heading"><h2>What is remarkable about the connections?</h2><p>The interesting part is where a structure reappears in a different role, through a map that can be checked.</p></div>
      <article><h3>The charge trace also enters the alpha budget.</h3><p>The same family charges participate in the compiler budget used by the electromagnetic equation. The identity retains its flavour transport and Higgs assumptions.</p><Link href="/explain#budget">Trace the connection</Link></article>
      <article><h3>One seed builds several levels of a hierarchy.</h3><p>Fixed powers and rational coefficients connect the charged lepton source masses. The same seed also appears in mixing and other readout branches.</p><Link href="/explain#flavor">See the mass ladder</Link></article>
      <article><h3>The clocks act on one another.</h3><p>The quarter action relabels the five cycle. It is an explicit operator relation, with four actions returning the labels to their starting point.</p><Link href="/explain#clocks">Try the clock action</Link></article>
      <article><h3>A present readout need not contain the whole history.</h3><p>The source construction retains information needed for later responses that a finite compressed readout can lose.</p><Link href="/results?search=memory">Inspect the source and memory results</Link></article>
    </section>
  </div>;
}
