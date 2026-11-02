import Link from "next/link";
import { ArrowDown, ArrowRight } from "lucide-react";
import { MechanismWalkthrough } from "./LearningFigures";

import { PredictionHeroPlate } from "./PredictionOverview";
import predictionStyles from "./PredictionOverview.module.css";

const outcomes = [
  { title: "Particles & charges", short: "Particles", second: "& charges", text: "The representations and charges of one Standard Model family, with a separate geometric construction for three families.", scope: "Representation and charge results", query: "hypercharge", href: "/explain#matter" },
  { title: "Masses & mixing", short: "Masses", second: "& mixing", text: "Relative charged lepton and quark source masses, a common hierarchy and specified constructions for particle mixing.", scope: "Source relations; physical mass transfer has its own conditions", query: "flavor", href: "/explain#flavor" },
  { title: "Electromagnetic coupling", short: "Electromagnetic", second: "coupling α", text: "A fixed boundary equation with one positive root close to the measured electromagnetic coupling. The equation, its root and its physical origin are distinct results.", scope: "Mathematical closure; physical identification remains a separate task", query: "alpha-global-positive-root", href: "/explain#alpha" },
  { title: "Cosmological readouts", short: "Cosmic", second: "patterns", text: "Conditional readouts for the rotation of polarized light, the ordinary matter fraction, early cosmic expansion and the vacuum energy hierarchy.", scope: "Conditional physical readouts and dated predictions", query: "cosmo", href: "/predictions" },
  { title: "Quantum & information structure", short: "Quantum", second: "structure", text: "Exact connections between the E₈ lattice, coding and finite quantum geometry. Source histories can preserve information that a compressed readout loses.", scope: "Scoped mathematical and source reconstruction results", query: "quartic", href: "/explain#quantum" },
  { title: "Clocks & dynamics", short: "Clocks", second: "& dynamics", text: "Related finite clock actions, exact relaxation in the specified transfer model and constructed state and time bridges.", scope: "Operator relations; physical time and a common source remain separate", query: "clock", href: "/explain#clocks" },
];

export function BigPictureHero() {
  return <section className="big-picture-hero learning-hero" aria-labelledby="big-picture-title"><div className={`experience-shell big-picture-layout ${predictionStyles.heroGrid}`}>
    <div className={predictionStyles.heroIntroCopy}><h1 id="big-picture-title">From a common structure to particles and constants.</h1>
      <p className="big-picture-lead">TFPT connects particle charges, mass relations, mixing angles and cosmological readouts through one specified construction. Start with its numerical predictions and their comparison with data, then follow the shared ingredients.</p>
    </div><PredictionHeroPlate/><div className={predictionStyles.heroNext}>
      <div className="experience-actions"><a href="#prediction-accuracy" className="experience-primary">Predictions and accuracy <ArrowDown size={18} aria-hidden /></a><a href="#inputs" className="experience-secondary">See how it works <ArrowRight size={18} aria-hidden /></a></div>
      <p className="experience-byline">Topological Fixed-Point Theory · Stefan Hamann & Alessandro Rizzo</p>
    </div>
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
