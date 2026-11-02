"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowRight, RotateCcw } from "lucide-react";
import { Math } from "@/components/Math";
import styles from "./PatternConnections.module.css";

// RM(1,3): evaluations of all affine functions on the eight points of F₂³.
const code = Array.from({ length: 16 }, (_, a) => Array.from({ length: 8 }, (_, x) =>
  ((a & 1) ^ (((a >> 1) & 1) & (x & 1)) ^ (((a >> 2) & 1) & ((x >> 1) & 1)) ^ (((a >> 3) & 1) & ((x >> 2) & 1)))));
const distance = (a: number[], b: number[]) => a.reduce((n, bit, i) => n + Number(bit !== b[i]), 0);
const source = (path: string) => `/documentation?source=${encodeURIComponent(path)}`;

function CodeExperiment() {
  const [word, setWord] = useState(6);
  const [error, setError] = useState<number | null>(2);
  const sent = code[word];
  const received = sent.map((bit, i) => i === error ? 1 - bit : bit);
  const distances = code.map(candidate => distance(candidate, received));
  const nearestDistance = globalThis.Math.min(...distances);
  const nearest = distances.flatMap((d, i) => d === nearestDistance ? [i] : []);
  const recovered = nearest.length === 1 ? code[nearest[0]].join("") : "No unique nearest word";
  return <div className={styles.codeExperiment}>
    <label className={styles.selectLabel}>Choose a valid message
      <select value={word} onChange={e => { setWord(Number(e.target.value)); setError(null); }}>{code.map((bits, i) => <option key={i} value={i}>{bits.join("")}</option>)}</select>
    </label>
    <div className={styles.bitCaption}>Sent word</div>
    <div className={styles.bits} aria-label={`Sent word ${sent.join("")}`}>{sent.map((bit, i) => <span key={i} data-one={bit === 1}>{bit}</span>)}</div>
    <div className={styles.bitCaption}>Change one bit below. The nearest valid word recovers the message.</div>
    <div className={styles.bits}>{received.map((bit, i) => <button key={i} type="button" data-one={bit === 1} data-error={error === i} aria-pressed={error === i} aria-label={`Bit ${i + 1}: ${bit}. ${error === i ? "Undo change" : "Change this bit"}`} onClick={() => setError(error === i ? null : i)}>{bit}</button>)}</div>
    <p className={styles.recovery} aria-live="polite">{error === null ? "The received word is valid." : `Bit ${error + 1} is changed. Only the original word is one bit away.`} <strong>Recovered: {recovered}</strong></p>
    <div className={styles.wordAtlas} aria-label="All sixteen valid words and their distances from the received word">{code.map((bits, i) => <div key={i} data-nearest={nearest.includes(i)}>
      <div className={styles.miniBits} aria-label={bits.join("")}>{bits.map((bit, j) => <span key={j} data-one={bit === 1} />)}</div><span>{distances[i]} {distances[i] === 1 ? "bit" : "bits"} away</span>
    </div>)}</div>
    <p className={styles.caption}>All sixteen valid words are shown. Any two differ in at least four positions, so their one bit neighbourhoods cannot overlap.</p>
    <details><summary>How does this become E₈?</summary><p>Allow every integer vector whose eight parities form one of these words, then rescale by √2. This gives an infinite lattice, rather than just sixteen points.</p><Math block>{String.raw`L=\{x/\sqrt2:x\in\mathbb Z^8,\ x\bmod2\in C\}`}</Math><p>The code is self dual and its word weights are multiples of four. Construction A therefore gives an even unimodular lattice of rank eight, which is E₈. Its shortest vectors number 240: sixteen coordinate vectors and 224 lifts of the fourteen weight four words.</p><p>This is classical binary error correction. The stronger proposal that root operators form the required syndrome algebra was excluded in its stated class.</p><Link href="/results?claim=E8.CODE.01">Code theorem and verification</Link><Link href="/results?claim=E8.SYNDROME.ALGEBRA.01">The stronger proposal and its exclusion</Link></details>
  </div>;
}

function QuantumFigure() {
  return <figure className={styles.quantumFigure}>
    <p>A ray represents one pure quantum state with its overall phase ignored. A basis here contains four mutually orthogonal states. A context names the commuting observables whose joint eigenstates form that basis.</p>
    <div className={styles.flow}><div><strong>E₈ roots</strong><span>Vectors in the same lattice</span></div><ArrowRight aria-hidden/><div><strong>Complex lines</strong><span>Identify v, iv, −v, −iv</span></div><ArrowRight aria-hidden/><div><strong>Quantum rays</strong><span>Apply the specified chart</span></div></div>
    <div className={styles.bases} aria-label="Fifteen orthogonal stabilizer bases, each containing four rays">{Array.from({length:15}, (_, i) => <div key={i}><span>{i + 1}</span>{[0,1,2,3].map(j => <i key={j}/>)}</div>)}</div>
    <figcaption>Each column represents one nonzero Gaussian quotient class: sixteen roots, four phase orbits. In the specified chart, these four rays form the eigenbasis of one Pauli context. The fifteen columns account for all sixty stabilizer rays.</figcaption>
    <details><summary>How does each quotient class become a quantum basis?</summary><Math block>{String.raw`L/(1+i)L\cong\mathbb F_2^4`}</Math><p>With the compiler compatible complex structure J, each of the fifteen nonzero quotient classes contains sixteen roots, giving four Gaussian lines after identifying the four phases. In the specified chart, those four lines form one orthogonal stabilizer basis: the joint eigenstates of a maximal commuting Pauli triple. The fifteen classes map bijectively to the fifteen contexts.</p><p>The projective G₃₁ action matches the two qubit Clifford action in the named representation. Clifford structure alone does not provide universal quantum computation.</p><Link href="/documentation?evidence=python_verification%3Averification%2Fv783_two_qubit_clifford.py">Read the explicit context correspondence</Link></details>
  </figure>;
}

function ClockFigure() {
  const [step, setStep] = useState(0);
  const multiplier = [1, 2, 4, 3][step];
  return <div className={styles.clockFigure}><div className={styles.clockLabels} aria-label={`Galois action: multiply labels by ${multiplier} modulo five`}>{[0,1,2,3,4].map(i => <span key={i}><small>Position {i}</small><strong>{(i * multiplier) % 5}</strong></span>)}</div>
    <div className={styles.actionLine}>{[1,2,4,3,1].map((v,i) => <span key={i} data-active={i === step}>{v}{i < 4 && <ArrowRight aria-hidden/>}</span>)}</div>
    <div className={styles.controls}><button type="button" onClick={() => setStep((step + 1) % 4)}>Apply the quarter action</button><button type="button" onClick={() => setStep(0)} aria-label="Reset clock action"><RotateCcw size={18}/></button><span aria-live="polite">{step} of 4 actions</span></div>
    <p>The action doubles labels modulo five. Four applications return every label. A fourfold action can therefore operate on a five cycle without being a segment of it.</p>
    <Math block>{String.raw`G C_5G^{-1}=C_5^2,\qquad G^4=I`}</Math>
    <details><summary>Where do the other clocks enter?</summary><p>The C₅ and C₆ data meet in the order thirty Coxeter structure. Four does not divide thirty. Separately, the named G₃₁ compiler has c = Jσ, σ = c⁴ and J = c⁹. That order twelve compiler clock is not the regular Springer order twelve element.</p><p>These are actions on specified spaces. A physical duration requires the appropriate source and time dictionary.</p><Link href="/explain#clocks">Explore the full clock network</Link></details>
  </div>;
}

function FlavorFigure() {
  return <figure><div className={styles.operatorBars}>{[["Q",3],["K",4],["R",8],["L",20]].map(([label,n]) => <div key={label}><strong>{label}</strong><div style={{width:`${Number(n)*4}%`}}/><span>det = {n}</span></div>)}</div><figcaption>Four specified operators carry different volume factors. Their determinant product is 1,920.</figcaption><div className={styles.pairedReadouts}><div><span>The same K block</span><Math block>{String.raw`\mathbf1^TK\mathbf1=25`}</Math></div><div><span>At the anchor a = (1,1,2)</span><Math block>{String.raw`a^TKa=41`}</Math></div></div><p>The alpha budget and the flavour operators meet in an actual shared quadratic form. A repeated number becomes informative when the map producing it is specified.</p><details><summary>What does this establish?</summary><p>The operator and anchor identities are exact within the given compiler. Physical masses retain the source scale and transfer conditions. The number 1,920 alone does not prove an isomorphism with a Weyl or horizon action.</p><Link href="/explain#budget">Follow charges into the electromagnetic budget</Link><Link href="/explain#flavor">Follow the mass hierarchy</Link></details></figure>;
}

function InvariantFigure() {
  return <figure><div className={styles.invariants}>{[8,12,20,24].map(d => <div key={d}><span>E₈ root sum</span><strong>F<sub>{d}</sub></strong><ArrowRight aria-hidden/><strong>f<sub>{d}</sub></strong><span>G₃₁ invariant</span></div>)}</div><figcaption>The arrows mean holomorphic restriction in the specified complex structure. The degree records the polynomial order.</figcaption><p>These four restricted polynomials are invariant and algebraically independent. Together with the cited Chevalley theorem, they generate the full G₃₁ invariant ring.</p><details><summary>Why is this more than matching four degrees?</summary><p>The result uses the actual polynomials, invariance under the sixty reflection mirrors and an exact independence check. Vanishing at degrees not divisible by four already follows from the quarter action; that simpler observation is a different claim.</p></details></figure>;
}

function CoverFigure() {
  return <figure><div className={styles.coverTracks} aria-label="Three sheets, each with sixteen lattice sites. The selected lift connects all forty eight sites.">{[0,1,2].map(sheet => <div key={sheet}><span>Sheet {sheet + 1}</span><div>{Array.from({length:16},(_,i) => <i key={i}/>)}</div></div>)}</div><div className={styles.formulaPair}><Math block>{String.raw`y^3=x^4-1`}</Math><Math block>{String.raw`L^4=\mathrm{Deck},\quad L^{12}=I`}</Math></div><figcaption>The selected lift joins the three sheets into one forty eight site cycle. Applying L four times performs the deck action.</figcaption><p>The four marked seam points, a selected μ₃ cover and the NS lift connect geometry to an explicit clock action. The curve has genus three.</p><details><summary>Which assumptions select this construction?</summary><p>The conformal four mark axioms, mark equivalence, uniform monodromy, the specified μ₃ branch and NS lift travel with this result. This genus three cover is distinct from the elliptic curve associated with four branch points.</p></details></figure>;
}

function NativeFigure() {
  return <figure><div className={styles.nativeMap}><div><strong>V₄</strong><span>Take the symmetric fourth power</span></div><ArrowRight aria-hidden/><div><strong>V₅</strong><span>Its P fixed space</span></div><ArrowRight aria-hidden/><div><strong>V₂₀</strong><span>Pair V₅ with conjugate V₄</span></div></div><Math block>{String.raw`V_5=\operatorname{Fix}_P(\operatorname{Sym}^4V_4)`}</Math><Math block>{String.raw`\rho_{20}(g)=\rho_5(g)\otimes\overline{\rho_4(g)}`}</Math><figcaption>The first arrow constructs a fixed space in a symmetric tensor power. The second uses the specified erasure intertwiner for the same group words.</figcaption><p>Here 4, 5 and 20 refer to spaces connected by actual maps. Symmetrization is essential: the full fourth tensor power has a sixteen dimensional fixed space instead.</p><p>The later full field product results reconstruct six complex projective rays and sixty marked flags. Recovering an unmarked geometry and physically selecting a mark are separate statements.</p><Link href="/results?search=native-symmetric-quartic-erasure-common-object">Inspect the quartic maps and premises</Link><Link href="/results?search=intrinsic">Explore later event geometry</Link></figure>;
}

function MemoryFigure() {
  return <figure><svg viewBox="0 0 600 240" role="img" aria-labelledby="memory-figure-title"><title id="memory-figure-title">Different histories can have the same compressed present readout and distinct later responses</title><g fill="none" stroke="currentColor" strokeWidth="2"><path d="M40 50 C130 50 160 120 270 120M40 190 C130 190 160 120 270 120M330 120 C430 120 450 50 560 50M330 120 C430 120 450 190 560 190"/><circle cx="300" cy="120" r="30"/></g><g fill="currentColor" fontSize="19"><text x="35" y="30">History A</text><text x="35" y="222">History B</text><text x="240" y="186">Same readout</text><text x="420" y="30">Later response A</text><text x="420" y="222">Later response B</text></g></svg><figcaption>Logical diagram of information loss under compression. The source retains histories that a present finite readout can identify.</figcaption><p>The source and memory results ask which observables retain enough information to predict later responses. They explain why recovering a matrix from clock fields and identifying a charged twist are different experimental tasks.</p><details><summary>What data distinguish the source?</summary><p>In the specified representation, four actual clock images generate thirty six quadratic directions and an exact response inverse. Charge preserving vacuum words remain twist blind. Eight independent charged response directions, each with its opposite charge and a known time scale, determine the twist. Four generating fields do not mean four measurements.</p></details></figure>;
}

const stories = [
  {id:"code",label:"Error correction",title:"E₈ can be built from a code that repairs a changed bit.",text:"An error correcting code keeps valid messages far enough apart that a damaged message can still be recognized. The extended Hamming code supplies exactly the parity structure used in a construction of E₈.",scope:"Exact code and lattice construction",href:"/documentation?section=section%3A3d2a5b53f3345969fcbc",claim:"E8.CODE.01",Figure:CodeExperiment},
  {id:"quantum",label:"Quantum dictionary",title:"The same lattice has a precise two qubit dictionary.",text:"After choosing the specified complex structure, lattice directions become complex lines. A named chart identifies those lines with a familiar finite quantum geometry.",scope:"Exact finite correspondence with its J and chart",href:"/documentation?section=section%3A6c4044608163b007c4c2",claim:"E8.CLIFFORD2Q.01",Figure:QuantumFigure},
  {id:"clocks",label:"Interlocking clocks",title:"A clock can change how another clock is labelled.",text:"The connection is visible in what the operators do. Try the quarter action on the five cycle labels below.",scope:"Exact actions in the specified representations",href:source("verification/v419_seam_galois_carrier.py"),claim:"SEAM.GALOIS.01",Figure:ClockFigure},
  {id:"flavor",label:"A shared budget",title:"Mass structure and the alpha budget reuse an operator.",text:"The link is stronger than two formulas happening to contain forty one: the same K block evaluates at the same anchor.",scope:"Exact operator identities; physical transfer has its own premises",href:"/documentation?section=section%3A9bab697ba19c86420aea",claim:"FLAV.KQ.01",Figure:FlavorFigure},
  {id:"invariants",label:"Shared invariants",title:"Two symmetry descriptions share a full polynomial dictionary.",text:"An invariant stays unchanged under a group action. Restricting the E₈ root polynomials to the specified complex space produces the basic invariants of G₃₁.",scope:"Invariant ring result under the stated theorem hypotheses",href:"/documentation?section=section%3A83d94e33024ba3df4db8",claim:"E8.QUARTICHALF.01",Figure:InvariantFigure},
  {id:"cover",label:"A lifted seam",title:"A marked boundary leads to a connected clock on a cover.",text:"A cover keeps track of several sheets above the same base. Following a lifted path can change sheets before returning to the starting point.",scope:"Specified conformal seam, cover branch and lift",href:"/documentation?section=section%3A38cc1bfba5161e50d0bb",claim:"QGEO.COVERSEAM.01",Figure:CoverFigure},
  {id:"native",label:"The 4 / 5 / 20 maps",title:"The source connects different response spaces through maps.",text:"Later work follows the native quartic and erasure responses into intrinsic event geometry. The important objects are the fields, their products and their transformation rules.",scope:"Scoped source and event geometry results",href:"/research/sources/319bc0f7a7a5db692a18f6fe.txt",claim:null,Figure:NativeFigure},
  {id:"memory",label:"Source memory",title:"The present readout need not contain the whole process.",text:"Two source histories can look identical after compression while carrying different information for a later response. The observable and the history must therefore be distinguished.",scope:"Source reconstruction in the specified representation",href:"/results?search=memory",claim:null,Figure:MemoryFigure},
];

export function PatternConnections({ embedded = false }: { embedded?: boolean }) {
  const [active,setActive] = useState("code");
  const story = stories.find(s => s.id === active)!;
  const Figure = story.Figure;
  return <section className={`${embedded ? "" : "experience-shell"} ${styles.section}`} id="discoveries" aria-labelledby="pattern-heading">
    <header className={styles.heading}><h2 id="pattern-heading">What else fits together?</h2><p>The lattice can be built from a code. Its complex directions have a quantum dictionary. Its clocks act on one another. Explore the actual connections and what each one establishes.</p></header>
    <div className={styles.layout}><nav className={styles.navigation} aria-label="Connections to explore">{stories.map(s => <button key={s.id} type="button" aria-pressed={active === s.id} aria-controls="pattern-detail" onClick={() => setActive(s.id)}>{s.label}<ArrowRight size={17} aria-hidden/></button>)}</nav>
      <article id="pattern-detail" className={styles.detail} aria-labelledby="pattern-title"><h3 id="pattern-title">{story.title}</h3><p className={styles.lead}>{story.text}</p><Figure key={story.id}/><footer><p>{story.scope}.</p><Link href={story.href}>Read the source and its assumptions <ArrowRight size={16} aria-hidden/></Link>{story.claim && <Link href={`/results?claim=${story.claim}`}>Inspect the original claim</Link>}</footer></article>
    </div>
    <details className={styles.further}><summary>Further results: dynamics, the alpha root and the wider atlas</summary><p>The decoupled DET16 mirror parent has an exact finite volume spectrum and unique product ground state. A specified class of uniformly local Hamiltonians has norm limit dynamics and ground or KMS states. The additional physical spacetime construction keeps its own hypotheses.</p><Link href="/results?claim=CHIRAL4D.MIRROR.DET16.01">Mirror result</Link><Link href="/results?claim=QFT4D.LATTICE.FUNDAMENTAL.01">Local dynamics</Link><p>The specified alpha equation has an analytic global uniqueness proof. That proof works for every positive budget M; selecting the physical budget and identifying the Thomson response are different claims.</p><Link href="/explain#alpha">The complete alpha derivation</Link><Link href="/architecture">Explore all mapped dependencies</Link><Link href="/results">Search the full knowledge atlas</Link></details>
  </section>;
}
