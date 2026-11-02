import Link from "next/link";
import { ChargeExplorer, ClockExplorer } from "./InteractiveReadouts";
import { Math } from "@/components/Math";
import { BudgetBridge, LeptonLadder } from "./DerivationFigures";
import { GuideNav } from "./GuideNav";
import { AlphaDerivation } from "./AlphaDerivation";

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
      <h1>Work one connection all the way through.</h1>
      <p className="guide-lead">Build one family of charges. Follow its charge trace into the compiler budget and the specified alpha equation.</p><Link className="guide-link inline-flex min-h-11 items-center mt-3" href="/#outcomes">Start with the overall results and connections</Link>
    </header>
    <GuideNav />
    <section className="guide-section" id="matter">
      <h2>Build the charges of one family</h2><p className="guide-lead">Select one colour slot and one weak slot. Their hypercharges add to 1/6: a quark component. Every even selection has a place in the family.</p>
      <p className="figure-note">Given here: the marked five slot carrier, normalized hypercharge and the even exterior representation. <a className="guide-link" href="#inputs">Inspect the starting inputs</a>.</p>
      <ChargeExplorer />
      <details className="guide-details mt-6"><summary>Gauge structure and the three families</summary>
      <p className="mt-6">The two weak components then have electric charges 2/3 and −1/3. The other even selections give the conjugate quark and lepton sectors. The subgroup preserving the normalized 3+2 structure supplies the familiar SU(3), SU(2) and U(1) Lie algebra, with its central quotient handled separately.</p>
      <h3 className="mt-8 text-2xl">Where do the three families enter?</h3><p className="mt-3">A sphere with four marked punctures has three independent one cycle directions: a loop around all four punctures gives one relation. Its family lattice is the A₃ side of the construction. Relating those three directions to physical families is part of the specified dictionary. Three colours and three families play different roles.</p>
      <SourceLine query="family" label="Family geometry, representations and anomalies" />
      </details>
    </section>
    <BudgetBridge />
    <AlphaDerivation />
    <section className="guide-section" id="inputs">
      <h2>First, what is supplied?</h2>
      <p className="guide-lead">A seam is the oriented boundary structure used to define a response. A carrier is the internal space on which the algebra acts. A compiler is the collection of specified mathematical maps taking these data to representations, operators and numerical readouts.</p>
      <div className="grid gap-8 sm:grid-cols-2"><div><h3 className="text-2xl">Boundary normalization</h3><p className="mt-3">P1 specifies a primitive boundary kernel, winding and the normalization c₃ = 1/(8π). It carries geometric and positivity assumptions, beyond the decimal value.</p></div><div><h3 className="text-2xl">Five slot carrier</h3><p className="mt-3">P2 supplies the five dimensional carrier and its 3+2 interface. These are internal degrees of freedom, not five spatial dimensions.</p></div></div>
      <p className="mt-6">The anchor a = (1,1,2), four marked points and the bootstrap reveal rigidity within explicitly defined classes. Compressing the inputs does not remove the need to explain their physical realization.</p>
      <SourceLine query="AX.P" label="P1, P2 and the anchor" />
    </section>
    <section className="guide-section" id="e8">
      <h2>Why E₈ appears</h2><p className="guide-lead">The carrier and family sides have compatible lattice data. The matching is an operation that can be checked.</p>
      <ol className="guide-steps"><li><strong>Build the two sides.</strong> D₅ has rank 5; A₃ has rank 3. Each has discriminant group ℤ₄.</li><li><strong>Check the glue.</strong> The two discriminant norms add to 5/4 + 3/4 = 2. The index 4 extension has determinant (4 × 4)/4² = 1.</li><li><strong>Identify the result.</strong> The positive even unimodular lattice of rank 8 is E₈, with 240 roots. Its Lie algebra has dimension 248.</li></ol>
      <Scope achieved="A lattice construction under the specified glue data." given="The carrier, family lattice, matching and positive lattice setting." open="E₈ is the closure and consistency object here. Its appearance does not by itself identify E₈ as the unbroken physical gauge group." />
      <SourceLine query="glue" label="The lattice and bootstrap results" />
    </section>
    <section className="guide-section" id="flavor">
      <h2>A common ladder for masses and mixing</h2><p className="guide-lead">The charged flavour construction already contains fixed word lengths, amplitudes and mass ratios. Its achievements should stay visible alongside the remaining source and scale questions.</p>
      <div className="formula-sequence"><Math block>{String.raw`\varphi_0=\frac1{6\pi}+\frac3{256\pi^4}`}</Math><Math block>{String.raw`\lambda_Y=\sqrt{\varphi_0(1-\varphi_0)}`}</Math><Math block>{String.raw`\widehat m_{f,j}=\frac{v_{\rm geo}}{\sqrt2}\lambda_Y^{L_{f,j}}\Lambda_{f,j}`}</Math></div>
      <LeptonLadder />
      <ol className="guide-steps"><li><strong>One seed:</strong> φ₀ ≈ 0.053172 gives λY ≈ 0.224376. Powers of a number smaller than one produce a hierarchy.</li><li><strong>Fixed steps:</strong> the residue and winding operators supply L = R + 6W, with det R = 8. The exponent for each component is a compiler output.</li><li><strong>Closed readouts:</strong> charged lepton amplitudes and quark ratios are worked out. For example, the derived selector stratum gives cᵤ/c_d = 55/117.</li><li><strong>Shared dependencies:</strong> the same seed enters mixing, the boundary response and conditional cosmological readouts. These are correlated theoretical outputs.</li></ol>
      <Scope achieved="The stated charged flavour branch, lepton amplitudes and quark ratio readouts; explicit mixing and neutrino constructions with individual statuses." given="The residue/transport construction, its selected stratum and source scale conventions." open="Absolute calibration, transfer to observed mass schemes and the full common physical source remain distinct from the closed dimensionless relations. Neutrino candidates retain their own assumptions and history." />
      <SourceLine query="flavor-ratio-closed" label="Closed flavour ratios and the remaining absolute anchor" />
      <Link className="guide-link inline-block mt-3" href="/predictions">Compare the registered textures, bands and later candidates</Link>
    </section>
    <section className="guide-section" id="clocks">
      <h2>Several clocks, connected by actual actions</h2><p className="guide-lead">The clock network is part of the construction. Each operator acts on a particular space; an order or a recurring number does not identify two operators.</p>
      <ClockExplorer />
      <dl className="scope-list"><div><dt>C₅, C₆, C₃₀</dt><dd>The 5 and 6 structures meet in the order 30 Coxeter data, with the stated cyclotomic decomposition.</dd></div><div><dt>The order 4 action</dt><dd>Its Galois action changes C₅ labels. Four does not divide thirty, so it is not a subcycle of C₃₀.</dd></div><div><dt>G₃₁ compiler clock</dt><dd>The named representation has c = Jσ, σ = c⁴ and J = c⁹. Its operator and its carrier must be retained.</dd></div><div><dt>Relaxation and physical time</dt><dd>The transfer spectrum and its rates are exact in the stated model. A finite cycle, a relaxation step and time in seconds are different objects.</dd></div></dl>
      <SourceLine query="clock" label="Clock relations and scoped exclusions" />
    </section>
    <section className="guide-section" id="quantum">
      <h2>The same structure also carries quantum and information geometry</h2>
      <p className="guide-lead">E₈, the Hamming code, the finite quantum representation and the local source are connected through explicit maps. The recent results extend well beyond a list of numerical constants.</p>
      <ul className="guide-steps"><li><strong>Coding and quantum geometry:</strong> Construction A on the extended Hamming code gives E₈. With the specified complex structure, Gaussian lines connect to the named two qubit stabilizer geometry.</li><li><strong>A common 4/5/20 object:</strong> native quartic and erasure intertwiners connect these representations. The numbers name actual spaces and maps, not three physical dimensions.</li><li><strong>Intrinsic event geometry:</strong> full field products reconstruct six complex projective rays and the associated sixty marked flags. The unmarked geometry and a physically selected mark are distinct results.</li><li><strong>Source and memory:</strong> the existing local E₈ current construction has modes, charged sectors and exterior paths. A finite compressed readout can lose information needed for later responses; the source history retains it.</li></ul>
      <SourceLine query="quartic" label="The native source and intrinsic geometry" /><SourceLine query="memory" label="Histories, exterior response and reconstruction" />
    </section>
    <section className="guide-section" id="source">
      <h2>From connected mathematics to a common physical source</h2><p className="guide-lead">The current work asks whether one original process supplies the fields, state, time, admissible events and gravitational response together. The constructed pieces remain available while that joint identification is tested.</p>
      <h3 className="mt-7 text-2xl">Local fields and the Higgs source</h3><p className="mt-3">Source, state and time bridges have been worked out in specified representations. Recent results construct dynamical and local Higgs source responses, including a local causal net in the given 1+1 dimensional cylinder. This does not turn that supplied geometry into physical 3+1 dimensional spacetime.</p>
      <h3 className="mt-7 text-2xl">E₈ events and continuous time</h3><p className="mt-3">The original epsilon bracket constrains the Hodge response even for correlated inputs under the stated complete, trace preserving operation assumptions. That finite event response cannot by itself be a continuous evolution beginning at a unitary identity. Event branches, records, additional time branches and their original source realization have to be distinguished.</p>
      <h3 className="mt-7 text-2xl">Gravity, cosmology and units</h3><p className="mt-3">The conditional entanglement and boundary channels connect c₃⁻¹ = 8π to the Einstein normalization; the scale grammar and cosmological branches have explicit readouts. A dimensionless construction still needs dimensional calibration. The common local geometry, spin 2 and dynamical source remain separate obligations.</p>
      <details className="guide-details mt-5"><summary>A later correction to an earlier gap argument</summary><p>The later source review shows that the specified Dirichlet to Neumann form bound alone does not imply the printed transfer gap Δ−2v. A comparison with the actual transfer operator is still required. Earlier broad “gap decoupled” summaries must be read with this correction.</p><Link href={evidence("metric-dtn-form-bound-needs-transfer-comparison-for-gap")}>Read the corrected scope and counterexample</Link></details>
      <SourceLine query="Higgs" label="Local and dynamical Higgs source results" /><SourceLine query="hodge" label="E₈ events, time and records" /><SourceLine query="gravity" label="Gravitational channels and their conditions" />
    </section>
    <TheoryMap />
    <section className="guide-section" id="status">
      <h2>What does “established” mean here?</h2><p className="guide-lead">Read the precise statement together with its premises. A mathematical result, a numerical calculation and a physical identification answer different questions.</p>
      <dl className="scope-list"><div><dt>[E] Established in its stated scope</dt><dd>The accompanying type distinguishes a formal theorem, lattice result, identity or numerical readout. An [E] marker does not certify all of physics.</dd></div><div><dt>[C] Conditional</dt><dd>A specified physical interpretation or construction depends on named hypotheses. The conditions travel with the result.</dd></div><div><dt>[O] Open or supplied</dt><dd>An unproved connection or declared input. Inputs and research tasks are described separately in the record.</dd></div><div><dt>[X] Test or exclusion</dt><dd>A test has a defined target. A counterexample rules out its stated class, rather than every possible realization.</dd></div></dl>
      <p className="mt-6">The result library preserves the original ledger status and every eligible source reviewed finding, including conditional achievements and negative results. These records are separate from automatically generated, unreviewed paper summaries.</p>
      <Link className="guide-primary mt-6 inline-flex" href="/results">Explore the complete result library</Link>
    </section>
  </article>;
}
