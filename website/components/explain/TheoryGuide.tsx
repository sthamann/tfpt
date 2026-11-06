import Link from "next/link";
import { ChargeExplorer, ClockExplorer } from "./InteractiveReadouts";
import { Math } from "@/components/Math";
import { AbelianBudgetDerivation } from "./AbelianBudgetDerivation";
import { SharedStructureBridge } from "./SharedStructureBridge";
import { SharedSeedDerivation,CosmologyDerivation } from "./ReadoutDerivations";
import { FlavorDerivation } from "./FlavorDerivation";
import { CommonSourcePath } from "./CommonSourcePath";
import { TheoryInputAccount } from "./TheoryInputAccount";
import { GuideNav } from "./GuideNav";
import { StartingStructures } from "./StartingStructures";
import { PatternConnections } from "./PatternConnections";
import { AlphaDerivation } from "./AlphaDerivation";
import { StandardModelDerivationMap } from "./StandardModelDerivationMap";
import { GuidePredictions } from "./GuidePredictions";
import { BootstrapSelection, HorizonAndFrontier } from "./PaperConnections";
import { ContinuousTransfer } from "./ContinuousTransfer";

const evidence = (q: string) => `/results?search=${encodeURIComponent(q)}`;
const areas = [
  { id: "origin", title: "Starting structure", text: "An oriented seam and a five slot carrier. The anchor (1,1,2) compresses several of the same data.", query: "AX.P", href: "#inputs" },
  { id: "lattice", title: "E₈ and consistency", text: "D₅ and A₃ join through matching discriminant data. The bootstrap checks the starting structure within its stated class.", query: "E8", href: "#e8" },
  { id: "matter", title: "Particles and flavour", text: "One family of representations, three family geometry, charge assignments and a common hierarchy of masses and mixings.", query: "flavor", href: "#matter" },
  { id: "electromagnetic", title: "Alpha and the boundary response", text: "Exact coefficients, a reconstructed defect line, a specified response function and its unique positive root.", query: "alpha", href: "#alpha" },
  { id: "time", title: "Clocks, quantum structure and memory", text: "Related finite actions, E₈ coding, a common 4/5/20 object and source histories retaining information beyond a finite readout.", query: "clock", href: "#clocks" },
  { id: "physical", title: "Fields, gravity and the shared source", text: "Local source constructions and conditional gravitational and cosmological channels. A common physical realization remains the goal.", query: "gravity", href: "#source" },
];

export function TheoryMap({ compact = false }: { compact?: boolean }) {
  return <section className="guide-section" aria-labelledby="map-heading" id="theory-map">
    <h2 id="map-heading">Explore the wider construction</h2>
    <p className="guide-lead">Two connected mechanisms run through TFPT: a discrete representation and lattice construction, and a boundary response feeding the constants and scale relations. Their shared inputs make the outputs related.</p>
    <ol className="theory-map">{areas.map((area) => <li key={area.id}>
      <h3 className="mt-2 text-xl"><Link href={compact ? `/explain${area.href}` : area.href}>{area.title}</Link></h3>
      <div><p className="leading-relaxed">{area.text}</p>
      <Link className="guide-link mt-3 inline-block text-sm" href={evidence(area.query)}>Results and sources</Link></div>
    </li>)}</ol>
    <p className="mt-5 text-sm text-slate-600">The bootstrap is a consistency relation. It does not let a consequence prove its own premises. Physical identifications have their own conditions at each connection.</p>
  </section>;
}

function SourceLine({ query, label }: { query: string; label: string }) {
  return <p className="mt-5 text-sm"><Link className="guide-link" href={evidence(query)}>{label} · inspect claims, premises and sources</Link></p>;
}
function Scope({ achieved, given, open }: { achieved: string; given: string; open: string }) {
  return <dl className="scope-list">
    <div><dt>Shown</dt><dd>{achieved}</dd></div><div><dt>Given</dt><dd>{given}</dd></div><div><dt>Physical connection</dt><dd>{open}</dd></div>
  </dl>;
}

export function TheoryGuide() {
  return <article className="guide-shell">
    <header className="guide-introduction">
      <h1>From particle structure to a calculated coupling.</h1>
      <p className="guide-lead">Follow the actual operations, then carry their outputs into the next calculation. Build the carrier representation, compute charges and transport lengths, and see the same lattice norms and matter budget enter alpha. The connected cosmological and quantum examples follow the same discipline.</p><Link className="guide-link inline-flex min-h-11 items-center mt-3" href="/#outcomes">Start with the overall results and connections</Link>
      <nav className="reference-links" aria-label="Understand reading paths"><a href="#standard-model">How the Standard Model is built</a><a href="#flavor">How the masses arise</a><a href="#predictions">Predictions and tests</a><Link href="/interactive">Follow an animated journey</Link></nav>
    </header>
    <p className="figure-note">An accepted starting principle, a mathematical consequence, a physical readout under hypotheses and a measured value play different roles. Each step below says which role its inputs and result have.</p>
    <GuideNav />
    <StartingStructures embedded />
    <StandardModelDerivationMap />
    <section className="guide-section" id="matter">
      <h2>Build the charges of one family</h2><p className="guide-lead">Select one colour slot and one weak slot. Their hypercharges add to 1/6: a quark component. Every even selection has a place in the family.</p>
      <p className="figure-note">Given here: the marked five slot carrier, normalized hypercharge and the even exterior representation. <a className="guide-link" href="#inputs">Inspect the starting inputs</a>.</p>
      <p>The marked split also determines which transformations preserve the interface. Unitary rotations within the three colour slots and within the two weak slots, with total determinant one, form S(U(3) × U(2)). Their Lie algebra is su(3) ⊕ su(2) ⊕ u(1). This is the structure preserving gauge algebra in the stated carrier construction.</p>
      <p>The remaining block phase must be traceless. If its weights are x_c and x_w, then 3x_c + 2x_w = 0. The primitive integer pair is (−2,3), up to the common orientation. In the stated charge convention X = 6Y, that fixes the two slot hypercharges:</p>
      <Math block>{String.raw`Y=\frac16\operatorname{diag}(-2,-2,-2,3,3)`}</Math>
      <p>On an exterior state the occupied slot charges add. That one rule produces the six quark and lepton sectors below. The relation Q_em = T₃ + Y then separates the two components of each weak doublet.</p>
      <ChargeExplorer />
      <details className="guide-details mt-6"><summary>Check the gauge anomalies and the family interpretation</summary>
      <p>The full sixteen component charge list has Tr Y = 0 and Tr Y³ = 0. Its mixed gauge anomaly coefficients also cancel:</p>
      <Math block>{String.raw`\begin{aligned}SU(3)^2U(1):&\quad\frac16-\frac13+\frac16=0,\\SU(2)^2U(1):&\quad\frac14-\frac14=0.\end{aligned}`}</Math>
      <p>Each term includes the appropriate multiplicity and fundamental representation index. This is a consistency check on the given Weyl spectrum. The field interactions and their physical source use the common action and reconstruction route.</p>
      <p><Link className="guide-link" href="/documentation?evidence=python_verification%3Averification%2Fv310_carrier_sm_anomaly.py">Read the actual spectrum and anomaly calculation</Link></p>

      <p className="mt-6">The two weak components then have electric charges 2/3 and −1/3. The other even selections give the conjugate quark and lepton sectors. The subgroup preserving the normalized 3+2 structure supplies the familiar SU(3), SU(2) and U(1) Lie algebra, with its central quotient handled separately.</p>
      <h3 className="mt-8 text-2xl">Where do the three families enter?</h3><p className="mt-3">A sphere with four marked punctures has three independent one cycle directions: a loop around all four punctures gives one relation. Its family lattice is the A₃ side of the construction. Relating those three directions to physical families is part of the specified dictionary. Three colours and three families play different roles.</p>
      <SourceLine query="family" label="Family geometry, representations and anomalies" />
      </details>
    </section>
    <SharedStructureBridge />
    <BootstrapSelection />
    <SharedSeedDerivation />
    <FlavorDerivation />
    <AbelianBudgetDerivation />
    <AlphaDerivation />
    <GuidePredictions />
    <CosmologyDerivation />
    <HorizonAndFrontier />
    <ContinuousTransfer />
    <section className="guide-section" id="clocks">
      <h2>Several clocks, connected by actual actions</h2><p className="guide-lead">The clock network is part of the construction. Each operator acts on a particular space; an order or a recurring number does not identify two operators.</p>
      <ClockExplorer />
      <dl className="scope-list"><div><dt>C₅, C₆, C₃₀</dt><dd>The 5 and 6 structures meet in the order 30 Coxeter data, with the stated cyclotomic decomposition.</dd></div><div><dt>The order 4 action</dt><dd>Its Galois action changes C₅ labels. Four does not divide thirty, so it is not a subcycle of C₃₀.</dd></div><div><dt>G₃₁ compiler clock</dt><dd>The named representation has c = Jσ, σ = c⁴ and J = c⁹. Its operator and its carrier must be retained.</dd></div><div><dt>Relaxation and physical time</dt><dd>The transfer spectrum and its rates are exact in the stated model. A finite cycle, a relaxation step and time in seconds are different objects.</dd></div></dl>
      <SourceLine query="clock" label="Clock relations and scoped exclusions" />
    </section>
    <section className="guide-section" id="quantum">
      <h2>The same structure also carries quantum and information geometry</h2>
      <p className="guide-lead">E₈, the Hamming code, the finite quantum representation and the local source are connected through explicit maps. The recent results extend well beyond a list of numerical constants.</p>
      <p>The interactive gallery below follows the code construction, the Gaussian and quantum dictionary, the actual clock actions, shared operator budgets and later source geometry. Each connection has its own premises and source.</p>
    </section>
    <PatternConnections embedded />
    <section className="guide-section" id="code-families">
      <h2>How the code also carries the family cycle</h2>
      <p className="guide-lead">The Gaussian quotient connects the code and clock pictures. It has four independent binary labels. In a suitable basis, the actual family action cycles F₁ → F₂ → F₃ → F₁ and leaves the anchor A fixed.</p>
      <p>Among its fifteen nonzero root bearing labels, this gives three fixed labels and four cycles of length three. These are classes in the Gaussian quotient L/(1+i)L. They are different from the raw binary codeword fibres used to construct the lattice. The explicit quotient map and its action supply the connection.</p>
      <nav className="reference-links" aria-label="Code and family source"><Link href="/documentation?section=section%3A5d71fdfd1d43434581f5">Read the information layer and family action</Link><Link href="/interactive/quantum">Explore the code and quantum dictionary</Link></nav>
    </section>
    <section className="guide-section" id="source">
      <h2>From connected mathematics to a common physical source</h2><p className="guide-lead">The original papers provide the common reconstruction route, complete reference transport and a geometric action realization. The latest calculations retain this whole-source concatenation and evaluate entire ordered mirror and nonlinear number-source families. The full primitive interacting field integral and its identification with these calculated callers remain the common calculation target.</p>
      <CommonSourcePath/>
      <details className="guide-details mt-7"><summary>Related local Higgs, event and gravitational results</summary>
      <p>Later dynamical Higgs responses and the specified 1+1 dimensional cylinder construction retain their own geometry and premises.</p>
      <h3 className="mt-7 text-2xl">E₈ events and continuous time</h3><p className="mt-3">The original epsilon bracket constrains the Hodge response even for correlated inputs under the stated complete, trace preserving operation assumptions. That finite event response cannot by itself be a continuous evolution beginning at a unitary identity. Event branches, records, additional time branches and their original source realization have to be distinguished.</p>
      <h3 className="mt-7 text-2xl">Gravity, cosmology and units</h3><p className="mt-3">The conditional entanglement and boundary channels connect c₃⁻¹ = 8π to the Einstein normalization; the scale grammar and cosmological branches have explicit readouts. A dimensionless construction still needs dimensional calibration. Applications to local geometry, spin 2 and dynamical gravity retain the hypotheses of the corresponding source and continuum construction.</p>
      <details className="guide-details mt-5"><summary>A later correction to an earlier gap argument</summary><p>The later source review shows that the specified Dirichlet to Neumann form bound alone does not imply the printed transfer gap Δ−2v. A comparison with the actual transfer operator is still required. Earlier broad “gap decoupled” summaries must be read with this correction.</p><Link href={evidence("metric-dtn-form-bound-needs-transfer-comparison-for-gap")}>Read the corrected scope and counterexample</Link></details>
      <SourceLine query="Higgs" label="Local and dynamical Higgs source results" /><SourceLine query="hodge" label="E₈ events, time and records" /><SourceLine query="gravity" label="Gravitational channels and their conditions" />
      </details>
    </section>
    <TheoryInputAccount/>
    <details className="guide-details my-8"><summary>Explore the wider result map</summary><TheoryMap /></details>
    <section className="guide-section" id="status">
      <h2>What does “established” mean here?</h2><p className="guide-lead">Read the precise statement together with its premises. A mathematical result, a numerical calculation and a physical identification answer different questions.</p>
      <dl className="scope-list"><div><dt>[E] Established in its stated scope</dt><dd>The accompanying type distinguishes a formal theorem, lattice result, identity or numerical readout. An [E] marker does not certify all of physics.</dd></div><div><dt>[C] Conditional</dt><dd>A specified physical interpretation or construction depends on named hypotheses. The conditions travel with the result.</dd></div><div><dt>[O] Open or supplied</dt><dd>An unproved connection or declared input. Inputs and research tasks are described separately in the record.</dd></div><div><dt>[X] Test or exclusion</dt><dd>A test has a defined target. A counterexample rules out its stated class, rather than every possible realization.</dd></div></dl>
      <p className="mt-6">The result library preserves the original ledger status and every eligible source reviewed finding, including conditional achievements and negative results. These records are separate from automatically generated, unreviewed paper summaries.</p>
      <Link className="guide-primary mt-6 inline-flex" href="/results">Explore the complete result library</Link>
    </section>
  </article>;
}
