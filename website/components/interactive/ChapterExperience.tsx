"use client";

import { useEffect, useId, useMemo, useRef, useState } from "react";
import Link from "next/link";
import { Math as Formula } from "@/components/Math";
import { AlphaDerivation } from "@/components/explain/AlphaDerivation";
import { BellRayExplorer } from "@/components/explain/BellRayExplorer";
import { ChargeExplorer } from "@/components/explain/InteractiveReadouts";
import { CliffordOperation, MarkedModes } from "@/components/explain/StartingStructures";
import { E8_ROOTS, inner, alphaResidual, alphaRoot, familyTransfer, TRANSFER_RATES, FIXED_SEED, seedReadouts } from "./mechanisms";
import styles from "./ChapterExperience.module.css";

export type InteractivePrediction = {
  id: string;
  observable: string;
  formula: string;
  frozen_value?: string;
  conditional_on?: string | null;
  layer?: string;
  band_min?: string;
  band_max?: string;
  experiment?: string;
  kill_criterion?: string;
};

const ink = ["#b5c7dc", "#66d8be", "#76a7ff", "#eda77e"];
const svgNumber = (value: number) => Number(value.toFixed(4));
const format = (value: number, digits = 6) => value.toLocaleString("en-US", { maximumFractionDigits: digits, minimumFractionDigits: 0 });
function useReducedMotion() {
  const [reduced, setReduced] = useState(true);
  useEffect(() => {
    const media = window.matchMedia("(prefers-reduced-motion: reduce)");
    const update = () => setReduced(media.matches);
    update(); media.addEventListener("change", update);
    return () => media.removeEventListener("change", update);
  }, []);
  return reduced;
}

function RootProjection() {
  const canvas = useRef<HTMLCanvasElement>(null);
  const projected = useRef<{ x: number; y: number; index: number }[]>([]);
  const angle = useRef(.38);
  const [coset, setCoset] = useState(-1);
  const [selected, setSelected] = useState(0);
  const [playing, setPlaying] = useState(true);
  const reduced = useReducedMotion();
  const root = E8_ROOTS[selected];
  const neighbours = useMemo(() => E8_ROOTS.map((r, i) => inner(root.vector, r.vector) === 1 ? i : -1).filter(i => i >= 0), [root]);
  const basis = useMemo(() => [1, 2].flatMap(k => [
    Array.from({ length: 8 }, (_, i) => .5 * Math.cos(2 * Math.PI * k * i / 8)),
    Array.from({ length: 8 }, (_, i) => .5 * Math.sin(2 * Math.PI * k * i / 8)),
  ]), []);
  useEffect(() => {
    const element = canvas.current;
    if (!element) return;
    const context = element.getContext("2d");
    if (!context) return;
    let frame = 0, last = 0, width = 0, height = 0;
    const draw = (time = 0) => {
      if (last && playing && !reduced) angle.current += Math.min(time - last, 40) * .00007;
      last = time;
      const theta = angle.current, c = Math.cos(theta), s = Math.sin(theta);
      context.clearRect(0, 0, width, height);
      const scale = Math.min(width * .32, height * .34);
      projected.current = E8_ROOTS.map((item, index) => ({
        x: width / 2 + scale * (c * inner(item.vector, basis[0]) + s * inner(item.vector, basis[2])),
        y: height / 2 + scale * (c * inner(item.vector, basis[1]) + s * inner(item.vector, basis[3])), index,
      }));
      const origin = projected.current[selected];
      context.strokeStyle = "rgba(132,168,219,.20)"; context.lineWidth = .7;
      for (const i of neighbours) {
        const point = projected.current[i];
        context.beginPath(); context.moveTo(origin.x, origin.y); context.lineTo(point.x, point.y); context.stroke();
      }
      projected.current.forEach((point, i) => {
        const highlighted = coset < 0 || E8_ROOTS[i].coset === coset;
        context.globalAlpha = highlighted ? .92 : .12;
        context.fillStyle = ink[E8_ROOTS[i].coset];
        context.beginPath(); context.arc(point.x, point.y, highlighted ? 3.2 : 2, 0, Math.PI * 2); context.fill();
      });
      context.globalAlpha = 1;
      context.strokeStyle = "#ffffff"; context.lineWidth = 1.8;
      context.beginPath(); context.arc(origin.x, origin.y, 7, 0, Math.PI * 2); context.stroke();
      context.fillStyle = "#a9bfd6"; context.font = "12px system-ui";
      context.fillText("ORTHONORMAL 2D PROJECTION", 20, height - 19);
      if (playing && !reduced && width > 0 && height > 0) frame = requestAnimationFrame(draw);
    };
    const resize = () => {
      cancelAnimationFrame(frame); last = 0;
      const rect = element.getBoundingClientRect(); width = rect.width; height = rect.height;
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      element.width = Math.round(width * dpr); element.height = Math.round(height * dpr);
      context.setTransform(dpr, 0, 0, dpr, 0, 0); draw();
    };
    const observer = new ResizeObserver(resize); observer.observe(element); resize();
    return () => { observer.disconnect(); cancelAnimationFrame(frame); };
  }, [basis, coset, selected, neighbours, playing, reduced]);
  const chooseCoset = (value: number) => {
    setCoset(value);
    if (value >= 0) setSelected(E8_ROOTS.findIndex(item => item.coset === value));
  };
  const next = () => {
    const indices = E8_ROOTS.map((r, i) => coset < 0 || r.coset === coset ? i : -1).filter(i => i >= 0);
    setSelected(indices[(indices.indexOf(selected) + 1) % indices.length]);
  };
  return <section className={styles.apparatus} aria-labelledby="projection-title">
    <header className={styles.introduction}><h2 id="projection-title">Inspect all 240 roots</h2><p>A lattice is a regular pattern of points. A root is one of its shortest nonzero vectors, measured from the origin to a lattice point. Each dot below shows one of E₈’s 240 root vectors, projected from eight coordinates into two.</p><p>The four glue classes are the four groups of vectors joined by this construction. Choose a group, then select a dot or move to the next root. The white ring follows the selected vector; its connecting lines show a precise lattice relationship.</p></header>
    <div className={styles.cosetControls} role="group" aria-label="Highlight an E8 gluing class">
      {[[-1, "All roots", 240], [0, "Class 0", 52], [2, "Class 2", 60], [1, "Class 1", 64], [3, "Class 3", 64]].map(([value, label, count]) => <button key={label} type="button" aria-pressed={coset === value} onClick={() => chooseCoset(Number(value))}><span>{label}</span><strong>{count}</strong></button>)}
    </div>
    <figure className={styles.darkFigure}>
      <canvas ref={canvas} className={styles.rootCanvas} aria-label="Two dimensional projection of all 240 E8 roots. Class controls and the Next root button provide the same selection without pointing." onPointerDown={event => {
        const rect = event.currentTarget.getBoundingClientRect(), x = event.clientX - rect.left, y = event.clientY - rect.top;
        const points = projected.current.filter(point => coset < 0 || E8_ROOTS[point.index].coset === coset);
        const nearest = points.reduce((best, point) => Math.hypot(point.x - x, point.y - y) < Math.hypot(best.x - x, best.y - y) ? point : best, points[0]);
        if (nearest && Math.hypot(nearest.x - x, nearest.y - y) < 30) setSelected(nearest.index);
      }}>All 240 vectors have squared length two. The four cosets contain 52, 60, 64 and 64 roots. Use the controls below to inspect their coordinates.</canvas>
      <figcaption>The projection turns; the lattice stays fixed. Overlapping points are separate roots. Eight lattice directions describe internal geometry, rather than eight spacetime dimensions.</figcaption>
    </figure>
    <div className={styles.toolbar}><button type="button" onClick={next}>Next root</button><button type="button" disabled={reduced} aria-pressed={playing && !reduced} onClick={() => setPlaying(value => !value)}>{playing && !reduced ? "Pause rotation" : "Resume rotation"}</button>{reduced && <span>Rotation paused by your motion preference.</span>}</div>
    <div className={styles.coordinateReadout} aria-live="polite" aria-atomic="true"><p>Selected root · class {root.coset}</p><div className={styles.coordinates}>{root.vector.map((value, i) => <span key={i} data-block={i < 5 ? "carrier" : "family"}><small>{i < 5 ? `D₅ · ${i + 1}` : `A₃ · ${i - 4}`}</small><strong>{value === .5 ? "½" : value === -.5 ? "−½" : value}</strong></span>)}</div><p>Squared length <strong>{inner(root.vector, root.vector)}</strong> · {neighbours.length} neighbours · <span>52 + 60 + 64 + 64 = 240 roots</span></p></div>
    <details className={styles.details}><summary>What exactly has been drawn?</summary><p>The integer roots are ±eᵢ ±eⱼ for i &lt; j. The half integer roots have eight entries ±½ and an even number of minus signs. Two orthonormal projection directions rotate through a four dimensional subspace of the eight coordinate space. Class selection highlights the original D₅ ⊕ D₃ coordinate split, with A₃ isometric to D₃. A line joins the selected root to one of its 56 neighbours whose inner product with it is one. A projection preserves neither every visible distance nor every separation.</p><Formula block>{String.raw`R(E_8)=\{\pm e_i\pm e_j:i<j\}\cup\{\tfrac12(\epsilon_1,\ldots,\epsilon_8):\prod_i\epsilon_i=1\}`}</Formula><Link href="/research/e8-discriminant-glue">Inspect the original lattice certificate</Link></details>
  </section>;
}

function AlphaExperience() {
  const id = useId(), root = useMemo(() => 1 / alphaRoot(), []);
  const [trial, setTrial] = useState(root), [zoom, setZoom] = useState(false);
  const [bracket, setBracket] = useState<[number, number]>([130, 145]);
  const [iterations, setIterations] = useState(0);
  const min = zoom ? 137.03 : 130, max = zoom ? 137.04 : 145;
  const extent = Math.max(Math.abs(alphaResidual(1 / min)), Math.abs(alphaResidual(1 / max))) * 1.12;
  const x = (value: number) => svgNumber(62 + (value - min) / (max - min) * 566);
  const y = (value: number) => svgNumber(154 - alphaResidual(1 / value) / extent * 105);
  const path = Array.from({ length: 181 }, (_, i) => { const a = min + (max - min) * i / 180; return `${i ? "L" : "M"}${x(a)},${y(a)}`; }).join(" ");
  const bisect = () => {
    const mid = (bracket[0] + bracket[1]) / 2;
    setTrial(mid); setIterations(n => n + 1);
    setBracket(alphaResidual(1 / mid) > 0 ? [mid, bracket[1]] : [bracket[0], mid]);
    if (mid < min || mid > max) setZoom(false);
  };
  return <section className={styles.apparatus}>
    <header className={styles.introduction}><h2>Find where the response balances</h2><p>The curve is the specified equation F(α). Move the trial coupling to make its residual zero. All equation inputs stay fixed.</p></header>
    <figure className={styles.darkFigure}><svg viewBox="0 0 700 335" role="img" aria-labelledby={`${id}-plot-title`}><title id={`${id}-plot-title`}>Residual of the specified alpha equation versus inverse alpha</title><line x1="62" y1="154" x2="628" y2="154" stroke="#738ba6"/><text x="27" y="161" fill="#c4d3e4" fontSize="16">0</text><path d={path} stroke="#83adff" strokeWidth="3" fill="none"/>{trial >= min && trial <= max && <><line x1={x(trial)} x2={x(trial)} y1="42" y2="270" stroke="#6bd8bd" strokeDasharray="3 6"/><circle cx={x(trial)} cy={y(trial)} r="7" fill="#6bd8bd" stroke="#0e233a" strokeWidth="2"/></>}<text x="62" y="294" fill="#c4d3e4" fontSize="17">{min}</text><text x="628" y="294" textAnchor="end" fill="#c4d3e4" fontSize="17">{max}</text><text x="62" y="29" fill="#c4d3e4" fontSize="16">F(α), scaled to this interval</text><text x="350" y="320" textAnchor="middle" fill="#c4d3e4" fontSize="16">Trial inverse coupling α⁻¹</text></svg><figcaption>The crossing is a root of this function. Its global uniqueness is proved analytically in the original argument.</figcaption></figure>
    <label className={styles.slider} htmlFor={`${id}-trial`}>Trial inverse coupling <output>{trial.toFixed(10)}</output><input id={`${id}-trial`} type="range" min={min} max={max} step={zoom ? .0000001 : .001} value={trial} onChange={event => setTrial(Number(event.target.value))}/></label>
    <div className={styles.toolbar}><button type="button" onClick={() => setTrial(root)}>Locate calculated root</button><button type="button" aria-pressed={zoom} onClick={() => { setZoom(v => !v); setTrial(root); }}>{zoom ? "Show wider interval" : "Zoom into the root"}</button><button type="button" onClick={bisect}>Bisect the interval</button><button type="button" onClick={() => { setBracket([130, 145]); setIterations(0); setTrial(root); }}>Reset bisection</button></div>
    <dl className={styles.readouts} aria-live="polite"><div><dt>Residual |F(α)|</dt><dd>{Math.abs(alphaResidual(1 / trial)) < 1e-18 ? "< 10⁻¹⁸" : Math.abs(alphaResidual(1 / trial)).toExponential(4)}</dd></div><div><dt>Bisection bracket after {iterations} steps</dt><dd>{bracket[0].toFixed(8)} to {bracket[1].toFixed(8)}</dd></div></dl>
    <p className={styles.scope}>Bisection halves an interval whose endpoints have opposite residual signs. This browser calculation uses ordinary numerical precision. The original analytic proof and certified interval enclosure remain separate evidence.</p>
    <details className={styles.details}><summary>Follow the complete original derivation and every coefficient</summary><div className={styles.originalReader}><AlphaDerivation/></div></details>
  </section>;
}

function MatterExperience() {
  return <section className={styles.apparatus}><header className={styles.introduction}><h2>Build a component of one family</h2><p>Select occupied colour and weak slots. Their charges add. Choose a complete sector to see where it sits in the sixteen component representation.</p></header><div className={styles.legacyReader}><ChargeExplorer/></div><details className={styles.details}><summary>Apply the operations that build the representation</summary><div className={styles.legacyReader}><CliffordOperation/></div><p>Single insertion or removal flips even and odd degree. Quadratic spin generators preserve parity. The even sixteen dimensional subspace is the specified D₅ half spinor.</p></details><details className={styles.details}><summary>Where do the three family directions enter?</summary><div className={styles.legacyReader}><MarkedModes/></div></details></section>;
}

function DynamicsExperience() {
  const id = useId();
  const [first, setFirst] = useState(.8), [split, setSplit] = useState(.75), [step, setStep] = useState(0), [running, setRunning] = useState(false);
  const reduced = useReducedMotion();
  useEffect(() => {
    if (!running || reduced || step >= 8) return;
    const timer = setTimeout(() => setStep(value => value + 1), 950);
    return () => clearTimeout(timer);
  }, [running, reduced, step]);
  const initial = [first, (1 - first) * split, (1 - first) * (1 - split)], current = familyTransfer(initial, step);
  const coefficients = [1 / Math.sqrt(3), (initial[0] - initial[1]) / Math.sqrt(2), (initial[0] + initial[1] - 2 * initial[2]) / Math.sqrt(6)];
  const plotY = (magnitude: number) => svgNumber(42 + Math.min(24, -Math.log10(Math.max(magnitude, 1e-24))) / 24 * 210);
  return <section className={styles.apparatus}><header className={styles.introduction}><h2>Watch a distribution relax</h2><p>Prepare three starting weights, then apply the existing family transfer. The uniform mode stays fixed. Two deviation modes shrink at different rates.</p></header>
    <div className={styles.distributions}>{[{ name: "Starting distribution", values: initial }, { name: `After ${step} transfer ${step === 1 ? "step" : "steps"}`, values: current }].map(row => <div key={row.name}><h3>{row.name}</h3><div className={styles.populationBar} role="img" aria-label={row.values.map((v, i) => `Component ${i + 1}: ${format(v * 100, 4)} percent`).join("; ")}>{row.values.map((v, i) => <span key={i} style={{ width: `${Math.max(0, v) * 100}%`, background: ink[i + 1] }}/>)}</div><p>{row.values.map(v => format(v, 6)).join(" · ")}</p></div>)}</div>
    <div className={styles.twoSliders}><label className={styles.slider} htmlFor={`${id}-first`}>Starting share in component 1 <output>{format(first * 100, 0)}%</output><input id={`${id}-first`} type="range" min="0" max="1" step=".01" value={first} onChange={e => { setFirst(Number(e.target.value)); setStep(0); setRunning(false); }}/></label><label className={styles.slider} htmlFor={`${id}-split`}>Share of the remainder in component 2 <output>{format(split * 100, 0)}%</output><input id={`${id}-split`} type="range" min="0" max="1" step=".01" value={split} onChange={e => { setSplit(Number(e.target.value)); setStep(0); setRunning(false); }}/></label></div>
    <div className={styles.toolbar}><button type="button" disabled={step >= 8} onClick={() => { setRunning(false); setStep(n => Math.min(n + 1, 8)); }}>Apply one step</button><button type="button" disabled={reduced} aria-pressed={running && step < 8 && !reduced} onClick={() => { if (step === 8) { setStep(0); setRunning(true); } else { setRunning(value => !value); } }}>{running && step < 8 ? "Pause steps" : "Play steps"}</button><button type="button" onClick={() => { setStep(0); setRunning(false); }}>Reset steps</button></div>
    <label className={styles.slider} htmlFor={`${id}-step`}>Transfer step <output>{step}</output><input id={`${id}-step`} type="range" min="0" max="8" step="1" value={step} onChange={e => { setStep(Number(e.target.value)); setRunning(false); }}/></label>
    <figure className={styles.darkFigure}><svg viewBox="0 0 700 300" role="img" aria-label="Mode magnitudes versus dimensionless transfer steps on a logarithmic vertical scale. The stationary mode stays fixed; the two deviation modes decay.">{[0, 6, 12, 18, 24].map(exponent => <g key={exponent}><line x1="90" x2="645" y1={42 + exponent / 24 * 210} y2={42 + exponent / 24 * 210} stroke="#354b64"/><text x="72" y={48 + exponent / 24 * 210} fill="#c4d3e4" fontSize="14" textAnchor="end">{exponent ? <>10<tspan baselineShift="super" fontSize=".7em">−{exponent}</tspan></> : "1"}</text></g>)}{TRANSFER_RATES.map((rate, i) => coefficients[i] === 0 ? null : <path key={rate} d={Array.from({ length: 81 }, (_, n) => { const t = n / 10; return `${n ? "L" : "M"}${svgNumber(90 + t / 8 * 555)},${plotY(Math.abs(coefficients[i]) * rate ** t)}`; }).join(" ")} stroke={ink[i + 1]} strokeWidth="2.7" fill="none"/>)}<line x1={90 + step / 8 * 555} x2={90 + step / 8 * 555} y1="32" y2="255" stroke="#ffffff" strokeDasharray="3 5"/>{[0, 2, 4, 6, 8].map(n => <text key={n} x={90 + n / 8 * 555} y="281" fill="#c4d3e4" textAnchor="middle" fontSize="15">{n}</text>)}</svg><figcaption>Mode magnitudes on a logarithmic scale. The continuous lines interpolate the integer step values for reading. A zero initial mode stays zero and lies below the plotted range.</figcaption></figure>
    <dl className={styles.modeReadout} aria-live="polite">{["Stationary mode", "Slower deviation", "Faster deviation"].map((label, i) => <div key={label}><dt><i style={{ background: ink[i + 1] }}/>{label}</dt><dd>{i ? (coefficients[i] * TRANSFER_RATES[i] ** step).toExponential(5) : coefficients[0].toFixed(6)}<small>{i === 0 ? "eigenvalue 1" : i === 1 ? "eigenvalue 64/729" : "eigenvalue 1/729"}</small></dd></div>)}</dl>
    <details className={styles.details}><summary>Inspect the actual transfer and its basis</summary><Formula block>{String.raw`T=\frac13\mathbf1\mathbf1^T+\left(\frac23\right)^6u_2u_2^T+\left(\frac13\right)^6u_3u_3^T`}</Formula><Formula block>{String.raw`u_2=\frac{(1,-1,0)}{\sqrt2},\qquad u_3=\frac{(1,1,-2)}{\sqrt6},\qquad p_n=T^np_0`}</Formula><p>The symmetric three component transfer is the one specified in v221. This apparatus uses its exact spectral decomposition. All three displayed amplitudes use unit length eigenvectors. The stationary amplitude is 1/√3 for a distribution with total weight one; signed deviation amplitudes use the basis shown here.</p><Link href="/documentation?source=verification%2Fv221_seam_qecc.py">Read the original finite transfer</Link></details><p className={styles.scope}>These are dimensionless steps of a specified relaxation operator. The screen’s playback speed is only a reading aid. Coherent quantum evolution, physical seconds and the original interacting field source require their separate maps.</p></section>;
}

const seedLabels = ["Quark mixing λC", "Neutrino mixing sin² θ₁₃", "Cosmic rotation β", "Ordinary matter Ωb"];
const seedFormula = [String.raw`\lambda_C=\sqrt{u(1-u)}`, String.raw`\sin^2\theta_{13}=u e^{-5/6}`, String.raw`\beta_{\mathrm{rad}}=\frac{u}{4\pi}`, String.raw`\Omega_b=\left(1-\frac1{4\pi}\right)u`];
function FlavorExperience() {
  const id = useId(), [seed, setSeed] = useState(FIXED_SEED), [active, setActive] = useState(0);
  const fixed = seedReadouts(FIXED_SEED), values = seedReadouts(seed), min = .035, max = .07;
  const x = (u: number) => svgNumber(90 + (u - min) / (max - min) * 545);
  const y = (ratio: number) => svgNumber(252 - (ratio - .6) / .8 * 210);
  return <section className={styles.apparatus}><header className={styles.introduction}><h2>Change one seed; follow four consequences</h2><p>The four readouts reuse u = φ₀. Move an illustrative trial seed and watch their values change together. The fixed TFPT seed is marked on the graph.</p></header>
    <label className={styles.slider} htmlFor={`${id}-seed`}>Trial shared seed u <output>{seed.toFixed(8)}</output><input id={`${id}-seed`} type="range" min={min} max={max} step=".00001" value={seed} onChange={event => setSeed(Number(event.target.value))}/></label><div className={styles.toolbar}><button type="button" onClick={() => setSeed(FIXED_SEED)}>Restore fixed TFPT seed</button><span>φ₀ = {FIXED_SEED.toFixed(9)}</span></div>
    <figure className={styles.darkFigure}><svg viewBox="0 0 700 320" role="img" aria-label="Four linked readout curves, each divided by its own fixed seed value. A fixed marker shows the TFPT seed; a trial marker follows the slider.">{[.6, .8, 1, 1.2, 1.4].map(v => <g key={v}><line x1="90" x2="635" y1={y(v)} y2={y(v)} stroke="#354b64"/><text x="72" y={y(v) + 5} textAnchor="end" fill="#c4d3e4" fontSize="14">{v.toFixed(1)}×</text></g>)}{fixed.map((reference, index) => <path key={index} d={Array.from({ length: 121 }, (_, n) => { const u = min + (max - min) * n / 120; return `${n ? "L" : "M"}${x(u)},${y(seedReadouts(u)[index] / reference)}`; }).join(" ")} stroke={ink[index]} strokeWidth={active === index ? 3.5 : 1.7} strokeDasharray={index === active ? undefined : `${3 + index * 3} 5`} fill="none" opacity={active === index ? 1 : .5}/>)}<line x1={x(FIXED_SEED)} x2={x(FIXED_SEED)} y1="28" y2="258" stroke="#eda77e" strokeDasharray="4 5"/><line x1={x(seed)} x2={x(seed)} y1="28" y2="258" stroke="#ffffff"/><circle cx={x(seed)} cy={y(values[active] / fixed[active])} r="6" fill={ink[active]} stroke="#ffffff"/><text x="90" y="285" fill="#c4d3e4" fontSize="15">{min}</text><text x="635" y="285" textAnchor="end" fill="#c4d3e4" fontSize="15">{max}</text><text x="350" y="310" textAnchor="middle" fill="#c4d3e4" fontSize="15">Shared seed u · dashed marker: fixed TFPT value</text></svg><figcaption>Vertical scale: each output divided by its value at the fixed seed. Three linear maps overlap on this normalized scale. Quark mixing follows a square root and bends away.</figcaption></figure>
    <div className={styles.outputChoices} role="group" aria-label="Inspect a shared seed readout">{seedLabels.map((label, i) => <button type="button" key={label} onClick={() => setActive(i)} aria-pressed={active === i}><span>{label}</span><strong>{values[i].toFixed(7)}{i === 2 ? "°" : ""}</strong></button>)}</div>
    <div className={styles.working} aria-live="polite"><h3>{seedLabels[active]}</h3><Formula block>{seedFormula[active]}</Formula><p>{["The small seed branch combines complementary weights before taking the square root.", "The fixed exponent is 5/6, the squared hypercharge trace on the five carrier slots. It is not varied by this control.", "Dividing by 4π gives radians. The value displayed in the control is converted to degrees.", "This is the remaining seed budget. Algebraically Ωb + βrad = u; Ωb is distinct from Ωb h²."][active]}</p><p>At the fixed seed: <strong>{fixed[active].toFixed(9)}{active === 2 ? "°" : ""}</strong>. At the trial seed: <strong>{values[active].toFixed(9)}{active === 2 ? "°" : ""}</strong>.</p></div>
    <p className={styles.scope}>The slider is an illustration of dependence, rather than a fit or a replacement for the fixed seed. Each physical readout retains its stated transport, state and cosmological premises. A shared input also makes these outputs correlated.</p><Link className={styles.sourceLink} href="/explain#seed">Follow the original forward and inverse maps</Link>
  </section>;
}

function PhaseRing({ count, position, labels, name }: { count: number; position: number; labels?: number[]; name: string }) {
  const arrow = useId();
  return <svg viewBox="0 0 300 300" role="img" aria-label={`${name}: position ${position}, labels ${(labels ?? Array.from({ length: count }, (_, i) => i)).join(", ")}`}>
    <defs><marker id={arrow} markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L6,3.5 L0,7" fill="none" stroke="#7795b8"/></marker></defs>
    {Array.from({ length: count }, (_, i) => {
      const a = -Math.PI / 2 + i * 2 * Math.PI / count, b = a + 2 * Math.PI / count;
      const x = svgNumber(150 + 100 * Math.cos(a)), y = svgNumber(150 + 100 * Math.sin(a)), u = svgNumber(150 + 100 * Math.cos(b)), v = svgNumber(150 + 100 * Math.sin(b));
      const length = Math.hypot(u - x, v - y), dx = (u - x) / length, dy = (v - y) / length;
      return <g key={i}><line x1={svgNumber(x + dx * 25)} y1={svgNumber(y + dy * 25)} x2={svgNumber(u - dx * 28)} y2={svgNumber(v - dy * 28)} stroke="#7795b8" strokeWidth="1.5" markerEnd={`url(#${arrow})`}/>{position === i && <line x1="150" y1="150" x2={x} y2={y} stroke="#72d9bf" strokeWidth="1.5"/>}<circle cx={x} cy={y} r="20" fill={position === i ? "#72d9bf" : "#18344f"} stroke={position === i ? "#72d9bf" : "#527395"}/><text x={x} y={svgNumber(y + 6)} textAnchor="middle" fill={position === i ? "#0c253b" : "#d6e4f3"} fontSize="18">{labels?.[i] ?? i}</text></g>;
    })}
    <text x="150" y="151" textAnchor="middle" fill="#e2ebf6" fontSize="23">{name}</text><text x="150" y="177" textAnchor="middle" fill="#acc2d9" fontSize="15">{count} positions</text>
  </svg>;
}
function QuantumExperience() {
  const [step, setStep] = useState(0), [power, setPower] = useState(0), [tab, setTab] = useState("ray");
  const multiplier = [1, 2, 4, 3][power];
  return <section className={styles.apparatus}><header className={styles.introduction}><h2>From a binary message to a quantum state</h2><p>In the specified mapping, eight zeros and ones supply eight real coordinates. Pairing them gives four complex amplitudes. Their normalized squared magnitudes give the probabilities of four possible measurement outcomes.</p><p>Apply a quarter turn: it changes one common phase while those probabilities stay fixed. The other tabs let you compare the distinct operations of advancing clock phases and changing their labels.</p></header><div className={styles.tabs} role="group" aria-label="Choose a quantum or clock construction"><button type="button" aria-pressed={tab === "ray"} onClick={() => setTab("ray")}>Construct a quantum ray</button><button type="button" aria-pressed={tab === "phases"} onClick={() => setTab("phases")}>Advance C₅ and C₆</button><button type="button" aria-pressed={tab === "galois"} onClick={() => setTab("galois")}>Apply the C₄ label action</button></div>
    {tab === "ray" ? <><div className={styles.legacyReader}><BellRayExplorer/></div><p className={styles.scope}>The finite dictionary contains sixty rays in fifteen orthogonal four ray contexts. This reader works through one explicit example, including its chart, quarter turn and Pauli operators. The full correspondence and a physical measurement instrument retain their original source premises.</p></> : tab === "phases" ? <><figure className={styles.darkFigure}><div className={styles.phasePair}><PhaseRing count={5} position={step % 5} name="C₅"/><PhaseRing count={6} position={step % 6} name="C₆"/></div><figcaption>Two phase counters with coprime orders. Their pair returns to the starting position after lcm(5, 6) = 30 steps.</figcaption></figure><div className={styles.toolbar}><button type="button" onClick={() => setStep(n => Math.max(0, n - 1))} disabled={step === 0}>Previous phase</button><button type="button" onClick={() => setStep(n => n + 1)}>Advance one phase</button><button type="button" onClick={() => setStep(0)}>Reset phases</button></div><dl className={styles.readouts} aria-live="polite"><div><dt>Combined step</dt><dd>{step}</dd></div><div><dt>C₅ position</dt><dd>{step % 5}</dd></div><div><dt>C₆ position</dt><dd>{step % 6}</dd></div><div><dt>Pair returns</dt><dd>{step > 0 && step % 30 === 0 ? "Both at the origin" : `${30 - step % 30} steps to the next return`}</dd></div></dl></> : <><figure className={styles.darkFigure}><div className={styles.singlePhase}><PhaseRing count={5} position={0} labels={Array.from({ length: 5 }, (_, i) => i * multiplier % 5)} name="C₄ action"/></div><figcaption>Positions stay fixed. Labels change by x ↦ 2x modulo 5, cycling through multipliers 1, 2, 4, 3, 1.</figcaption></figure><div className={styles.toolbar}><button type="button" onClick={() => setPower(n => (n + 1) % 4)}>Apply G</button><button type="button" onClick={() => setPower(0)}>Reset labels</button></div><div className={styles.working} aria-live="polite"><h3>After {power} applications: multiplier {multiplier}</h3><Formula block>{String.raw`G C_5 G^{-1}=C_5^2,\qquad G^4=I`}</Formula><p>The same original edges now advance labels by {multiplier} modulo five. This order four automorphism is not a four step subcycle of a cycle of order thirty.</p></div></>}
    <p className={styles.scope}>These finite actions make the specified clock arithmetic visible. They do not assign seconds, prove a physical recurrence or identify every operator in the quantum source. The G₃₁ compiler clock and coherent evolution retain their own representations.</p><Link className={styles.sourceLink} href="/explain#clocks">Inspect the original actions and source links</Link></section>;
}

function PredictionExperience({ predictions }: { predictions: InteractivePrediction[] }) {
  const id = useId(), [filter, setFilter] = useState("all"), [selectedId, setSelectedId] = useState(predictions[0]?.id ?? "");
  if (!predictions.length) return <section className={styles.apparatus}><h2>Inspect the frozen register</h2><p>The register is available on the original predictions page, including its values, assignments and conditional bands.</p><Link className={styles.sourceLink} href="/predictions">Open the complete frozen register</Link></section>;
  const layer = (row: InteractivePrediction) => row.layer || (row.band_min ? "band" : "unspecified");
  const layerLabels: Record<string, string> = { core: "Core readouts", conditional: "Conditional readouts", assigned: "Assigned textures", band: "Conditional bands", unspecified: "Other registered records" };
  const layerMeaning: Record<string, string> = { core: "A value calculated within the declared compiler construction. Its physical interpretation still carries the original premises.", conditional: "A readout that depends on an additional named physical or geometric identification.", assigned: "A supplied texture or phase branch. Its assigned value keeps that status when compared with observations.", band: "A range obtained while varying a stated external input. The input and range conditions belong to the prediction." };
  const layers = [...new Set(predictions.map(layer))];
  const filtered = predictions.filter(row => filter === "all" || layer(row) === filter);
  const selected = filtered.find(row => row.id === selectedId) ?? filtered[0];
  const sharedVariable = /phi_?0/i.test(selected.formula) ? "phi0" : /N_star/i.test(selected.formula) ? "N_star" : /alpha/i.test(selected.formula) ? "alpha" : null;
  const related = sharedVariable ? predictions.filter(row => row.id !== selected.id && new RegExp(sharedVariable === "phi0" ? "phi_?0" : sharedVariable, "i").test(row.formula)) : [];
  return <section className={styles.apparatus}><header className={styles.introduction}><h2>Follow a registered formula to its conditions</h2><p>Select a record from the original frozen register. Values and formula strings below are supplied by that register. Their categories remain visible.</p></header><div className={styles.filters}><label htmlFor={`${id}-category`}>Type of result<select id={`${id}-category`} value={filter} onChange={e => setFilter(e.target.value)}><option value="all">All result types</option>{layers.map(value => <option key={value} value={value}>{layerLabels[value] ?? value}</option>)}</select></label><label htmlFor={`${id}-record`}>Registered observable<select id={`${id}-record`} value={selected.id} onChange={e => setSelectedId(e.target.value)}>{filtered.map(row => <option value={row.id} key={row.id}>{row.observable}</option>)}</select></label></div>
    <div className={styles.registryRecord} aria-live="polite"><h3>{selected.observable}</h3><p className={styles.layerMeaning}>{layerMeaning[layer(selected)]}</p><dl><div><dt>Original record and layer</dt><dd>{selected.id} · {layer(selected)}</dd></div><div><dt>Frozen value</dt><dd className={styles.exactValue}>{selected.frozen_value ?? (selected.band_min && selected.band_max ? `${selected.band_min} to ${selected.band_max}` : "No scalar value supplied")}</dd></div><div><dt>Original formula</dt><dd>{selected.formula}</dd></div><div><dt>Recorded condition</dt><dd>{selected.conditional_on || "No separate condition string supplied in this record. Its category and original source still apply."}</dd></div>{selected.experiment && <div><dt>Comparison or experiment named in the register</dt><dd>{selected.experiment}</dd></div>}{selected.kill_criterion && <div><dt>Original failure criterion</dt><dd>{selected.kill_criterion}</dd></div>}</dl></div>
    <div className={styles.relationships}><h3>{sharedVariable ? `Other formulas that name ${sharedVariable}` : "Formula relationships"}</h3>{related.length ? <><p>These records explicitly reuse the same named symbol in their frozen formula strings. This is a dependency clue, rather than proof of independent experimental confirmation.</p><div className={styles.relatedRecords}>{related.map(row => <button type="button" key={row.id} onClick={() => { setFilter("all"); setSelectedId(row.id); }}>{row.observable}</button>)}</div></> : <p>No other displayed formula explicitly names the selected symbol. The complete source records contain the full prerequisites and dependencies.</p>}</div><p className={styles.scope}>The register separates predicted readouts, assigned textures and conditional bands. Registration does not make previously known measurements blind tests. The layer names shown here preserve the original data vocabulary.</p><Link className={styles.sourceLink} href="/predictions">Open the original register and freeze policy</Link></section>;
}

export function ChapterExperience({ chapter, predictions = [] }: { chapter: string; predictions?: InteractivePrediction[] }) {
  return <div className={styles.root}>
    {chapter === "alpha" ? <AlphaExperience/> : chapter === "standard-model" ? <MatterExperience/> : chapter === "e8" ? <RootProjection/> : chapter === "dynamics" ? <DynamicsExperience/> : chapter === "predictions" ? <PredictionExperience predictions={predictions}/> : chapter === "flavor" ? <FlavorExperience/> : chapter === "quantum" ? <QuantumExperience/> : null}
  </div>;
}
