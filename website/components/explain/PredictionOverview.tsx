import Link from "next/link";
import { ArrowDown, ArrowRight } from "lucide-react";
import { comparisonFor, measurementComparisons, signedSigma, type MeasurementComparison } from "@/lib/measurement-comparisons";
import { frozenRegistry, predictionById, predictionLabel, shortFrozenValue } from "@/lib/frozen-predictions";
import { formatMeasurement } from "@/lib/format-number";
import styles from "./PredictionOverview.module.css";

function ReadingValue({ row }: { row: MeasurementComparison }) {
  return <>{shortFrozenValue(predictionById(row.id))}{row.id === "BETA_BIREFRINGENCE_DEG" ? "°" : ""}</>;
}

export function PredictionHeroPlate() {
  const ids = ["ALPHA_INV", "LAMBDA_C", "SIN2_THETA12_SEED", "OMEGA_B"];
  return <figure className={styles.heroPlate} aria-labelledby="prediction-hero-title">
    <h2 id="prediction-hero-title">Predictions, compared with data</h2>
    <p className={styles.heroIntro}>Four examples across particles and cosmology. Each has a fixed output and a named measurement.</p>
    {ids.map(id => { const row = comparisonFor(id); return <a key={id} className={styles.heroRow} href={`#comparison-${id}`}>
      <div><strong>{row.shortTitle}</strong><span>{row.symbol} · TFPT <ReadingValue row={row}/></span></div>
      <div><b>{signedSigma(row.sigma)}σ</b><span>{row.relativeLabel} difference</span></div>
    </a>; })}
    <figcaption>σ is the stated measurement uncertainty. A smaller absolute distance means closer agreement. Source dates and assumptions follow below.</figcaption>
    <a className={styles.heroLink} href="#prediction-accuracy">See all comparisons and testable outputs <ArrowDown size={17} aria-hidden/></a>
  </figure>;
}

function AgreementPlot({ row }: { row: MeasurementComparison }) {
  const x = (v: number) => 24 + (v + 3) * 42;
  return <svg className={styles.plot} viewBox="0 0 300 62" role="img" aria-label={`${row.shortTitle}: TFPT at ${signedSigma(row.sigma)} measurement standard uncertainties. Pale band is minus one to plus one; measurement center is zero.`}>
    <rect x={x(-1)} y="18" width={x(1)-x(-1)} height="22" rx="3" fill="#dce7ed" stroke="#61778c" strokeWidth="0.75"/>
    <line x1={x(-3)} x2={x(3)} y1="29" y2="29" stroke="#8b9cac"/>
    <line x1={x(0)} x2={x(0)} y1="12" y2="45" stroke="#425a6e"/>
    {[-3,-2,-1,0,1,2,3].map(t => <g key={t}><line x1={x(t)} x2={x(t)} y1="42" y2="46" stroke="#8b9cac"/><text x={x(t)} y="59" textAnchor="middle" fill="#4c5d71" fontSize="12">{t > 0 ? `+${t}` : t < 0 ? `−${-t}` : "0"}</text></g>)}
    <circle cx={x(row.sigma)} cy="29" r="5" fill="#294ab6" stroke="#fcfbf8" strokeWidth="1.5"/>
  </svg>;
}

const registerGroups = [
  {title:"Electromagnetism",note:"A fixed root of the specified boundary equation.",ids:["ALPHA_INV"]},
  {title:"Quark mixing",note:"Three angles and a leading order CP phase from the shared flavour construction.",ids:["LAMBDA_C","S23_CKM","S13_CKM","DELTA_CKM_RAD"]},
  {title:"Neutrino mixing",note:"Two numerical readouts, plus the separately assigned atmospheric and CP textures.",ids:["SIN2_THETA12_SEED","SIN2_THETA13","SIN2_THETA23","DELTA_CP_NU_DEG"]},
  {title:"Relative particle masses",note:"These are source scale ratios. A comparison with measured pole or MS̄ masses requires the specified transport and mass scheme.",ids:["MMU_OVER_MTAU","ME_OVER_MMU","MU_OVER_MD","MC_OVER_MS","MT_OVER_MB"]},
  {title:"Cosmic rotation, matter and vacuum",note:"Conditional physical readouts with shared seeds, branch and cosmological assumptions.",ids:["BETA_BIREFRINGENCE_DEG","OMEGA_B","RHOL_OVER_MBAR4"]},
  {title:"Inflation and the next tests",note:"The scalaron scale and two conditional bands. The bands use the external reheating range N★ = 50–60.",ids:["MSCAL_OVER_MBAR","R_TENSOR","N_S"]},
];

export function PredictionOverview({anchored=true}:{anchored?:boolean}) {
  const all = [...frozenRegistry.predictions, ...frozenRegistry.assigned_texture_values, ...frozenRegistry.conditional_bands];
  return <section className={`experience-shell ${styles.overview}`} id={anchored?"prediction-accuracy":undefined} aria-labelledby="prediction-overview-title">
    <header className={styles.heading}><h2 id="prediction-overview-title">What does TFPT predict, and how close are the numbers?</h2><p>Compare the fixed outputs with measurements before following their derivations. The same inputs connect electromagnetic strength, particle mixing and cosmological readouts.</p></header>
    <div className={styles.legend}><span><i/>TFPT output</span><span><i/>Measurement ±1σ</span><span>Zero = measured central value</span></div>
    <p className={styles.note}>Values frozen 9 June 2026; primary sources checked 2 November 2026. Distances use the stated measurement or fit uncertainty, with the corresponding side for asymmetric errors. They include no theory error and are not a combined significance. Known measurements retain their comparison status.</p>
    <div className={styles.columnHeads} aria-hidden><span>Quantity</span><span>TFPT / measured value</span><span>Difference in measurement uncertainties</span></div>
    <div className={styles.comparisons}>{measurementComparisons.map(row => <article key={row.id} id={`comparison-${row.id}`} className={styles.comparison}>
      <div className={styles.quantity}><h3>{row.shortTitle}</h3><p>{row.symbol}</p><p className={styles.scope}>{row.scopeShort}</p></div>
      <div className={styles.values}><p><span>TFPT</span><strong><ReadingValue row={row}/></strong></p><p><span>Measured / fitted</span><strong>{formatMeasurement(row.measured)}</strong></p></div>
      <div className={styles.agreement}><div><strong>{signedSigma(row.sigma)}σ</strong><span>{row.relativeLabel} relative difference</span></div><AgreementPlot row={row}/></div>
      <details className={styles.context}><summary>Meaning, date and source</summary><p>{row.explanation} {row.meaning}</p><p>{row.date}. {row.history}</p><p><strong>Physical premise:</strong> {predictionById(row.id).conditional_on || "The frozen numerical readout retains the source and physical transfer conditions of its branch."}</p><div><a href={row.href} target="_blank" rel="noopener noreferrer">Read the primary measurement</a><Link href={`/empirical-audit#${row.id}`}>Full dated comparison</Link><Link href={`/predictions#${row.id}`}>Formula and failure criterion</Link></div></details>
    </article>)}</div>
    <PredictionBandTests />
    <section className={styles.register} aria-labelledby="register-preview-title"><h3 id="register-preview-title">The wider prediction programme</h3><p>The frozen register contains sixteen main values, two assigned textures and two conditional bands. Explore every entry below. Source mass ratios, assigned textures and conditional bands keep their own comparison requirements.</p>
      {registerGroups.map(group => <details key={group.title} className={styles.registerGroup}><summary>{group.title}<ArrowDown size={17} aria-hidden/></summary><p>{group.note}</p><div>{group.ids.map(id => { const row = all.find(x => x.id === id)!; const measured = measurementComparisons.find(x => x.id === id); const assigned = frozenRegistry.assigned_texture_values.some(x=>x.id===id); return <article key={id} className={styles.registerRow}><div><h4>{predictionLabel(id)}</h4><p>{assigned ? "Assigned texture" : row.band_min ? "Conditional band" : row.layer === "conditional" ? "Conditional readout" : "Fixed numerical readout"}</p></div><strong>{shortFrozenValue(row)}{id === "DELTA_CP_NU_DEG" || id === "BETA_BIREFRINGENCE_DEG" ? "°" : ""}</strong><div>{measured ? <a href={`#comparison-${id}`}>{signedSigma(measured.sigma)}σ in the dated comparison</a> : <span>{group.title === "Relative particle masses" ? "Source to measured mass scheme transfer required" : assigned ? "Test the assigned branch; no independent derivation claimed" : id === "N_S" ? "Upper band edge 2.84 measurement uncertainties below the cited ACT center" : id === "R_TENSOR" ? "The cited upper limit still permits this band" : "Physical scalaron identification required"}</span>}<Link href={`/predictions#${id}`}>Formula, conditions and test <ArrowRight size={14} aria-hidden/></Link></div></article>;})}</div></details>)}
      <p className={styles.note}>The source ratios are not automatically measured pole or MS̄ mass ratios. In particular, a broad historical range is not a current precision match for the charm to strange ratio. The required reader must be applied before reporting a physical accuracy.</p>
      <div className={styles.actions}><Link href="/predictions">Read the complete frozen register <ArrowRight size={17} aria-hidden/></Link><Link href="/empirical-audit">Inspect dated measurements and assumptions</Link><Link href="/falsification">What would rule out each branch?</Link></div>
    </section>
  </section>;
}

export function PredictionBandTests() {
  return <section className={styles.bandTests} aria-labelledby="band-test-title"><h3 id="band-test-title">What remains to be tested, and where is there tension?</h3>
      <article><div><h4>Primordial gravitational waves</h4><p>The conditional inflation branch gives r = 0.00333–0.00480 for N★ = 50–60. The cited BK18 analysis gives r₀․₀₅ &lt; 0.036 at 95% confidence.</p></div><div><p>This limit still permits the whole band. A more sensitive tensor measurement can test it; an upper limit does not measure the predicted value.</p><svg className={styles.bandPlot} viewBox="0 0 400 115" role="img" aria-label="The TFPT tensor band from 0.00333 to 0.0048 is below the BK18 upper limit 0.036 at 95 percent confidence."><line x1="25" x2="375" y1="60" y2="60" stroke="#8b9cac"/><rect x={25+350*.003333333333333333/.04} y="48" width={350*(.0048-.003333333333333333)/.04} height="24" fill="#294ab6"/><line x1="340" x2="340" y1="40" y2="75" stroke="#425a6e" strokeWidth="2"/><text x="60" y="28" textAnchor="middle" fill="#294ab6" fontSize="13">TFPT band</text><text x="340" y="28" textAnchor="middle" fill="#425a6e" fontSize="13">95% upper limit</text>{[0,.01,.02,.03,.04].map(v=><text key={v} x={25+350*v/.04} y="98" textAnchor="middle" fill="#4c5d71" fontSize="12">{v===0?"0":v.toFixed(2)}</text>)}</svg></div><a href="https://arxiv.org/abs/2110.00483" target="_blank" rel="noopener noreferrer">BK18 primary result, 2021</a></article>
      <article><div><h4>The inflation tilt is under tension</h4><p>The same branch gives nₛ = 0.960–0.96667. ACT P-ACT-LB2 with DESI DR2 reports 0.9752 ± 0.0030.</p></div><div><p>The upper edge of the frozen band is 2.84 stated measurement uncertainties below that central value. This is a band comparison at the specified reheating range, with no theory error or global significance assigned.</p><svg className={styles.bandPlot} viewBox="0 0 400 115" role="img" aria-label="TFPT spectral tilt band 0.960 to 0.96667 and ACT measurement 0.9752 plus or minus 0.0030. The one uncertainty measurement interval is above the entire frozen band."><line x1="25" x2="375" y1="60" y2="60" stroke="#8b9cac"/><rect x={25+350*(.960-.95)/.04} y="48" width={350*(.9666666666666667-.960)/.04} height="24" fill="#294ab6"/><rect x={25+350*(.9752-.003-.95)/.04} y="48" width={350*.006/.04} height="24" fill="#dce7ed" stroke="#61778c" strokeWidth="0.75"/><line x1={25+350*(.9752-.95)/.04} x2={25+350*(.9752-.95)/.04} y1="40" y2="79" stroke="#425a6e" strokeWidth="2"/><text x="140" y="28" textAnchor="middle" fill="#294ab6" fontSize="13">TFPT band</text><text x="245" y="28" textAnchor="middle" fill="#425a6e" fontSize="13">ACT ±1σ</text>{[.95,.96,.97,.98,.99].map(v=><text key={v} x={25+350*(v-.95)/.04} y="98" textAnchor="middle" fill="#4c5d71" fontSize="12">{v.toFixed(2)}</text>)}</svg></div><a href="https://arxiv.org/pdf/2503.14452#page=31" target="_blank" rel="noopener noreferrer">ACT DR6 Table 5, revised 24 June 2025</a></article>
      <p className={styles.note}>Neutrino CP phase 240° and atmospheric sin² θ₂₃ = 0.5 are assigned textures in the frozen register. They remain visible as testable branches with their own criteria.</p>
    </section>;
}
