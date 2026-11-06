"use client";

import { useCallback, useEffect, useId, useMemo, useRef, useState } from "react";
import { C3, E8_ROOTS, FIXED_SEED, alphaRoot, familyTransfer, inner, seedReadouts } from "./mechanisms";
import styles from "./BeginnerExperiments.module.css";

type Comparison = { predicted: number; central: string; uncertaintyMinus: string; date: string; measured: string };
export type BeginnerExperimentsProps = { chapter: string; inverseAlpha: number; comparison?: Comparison; embedded?: boolean };
const colors = ["#84afff", "#71ddc1", "#efa984", "#b9a6ec"];
const svg = (value: number) => Number(value.toFixed(4));
const countBits = (mask: number) => Array.from({ length: 5 }, (_, i) => Number(Boolean(mask & 1 << i))).reduce((a, b) => a + b, 0);
const fraction = (n: number) => { if (!n) return "0"; const gcd = (a: number, b: number): number => b ? gcd(b, a % b) : a; const d = gcd(Math.abs(n), 6); return `${n < 0 ? "−" : "+"}${Math.abs(n) / d}${6 / d === 1 ? "" : `/${6 / d}`}`; };

function useReducedMotion() {
  const [reduced, setReduced] = useState(true);
  useEffect(() => { const media = matchMedia("(prefers-reduced-motion: reduce)"); const update = () => setReduced(media.matches); update(); media.addEventListener("change", update); return () => media.removeEventListener("change", update); }, []);
  return reduced;
}

/** Finite movement between actual data values; no free-running background loop. */
function useNumberMotion(initial: number) {
  const reduced = useReducedMotion(), frame = useRef(0), current = useRef(initial);
  const [value, setState] = useState(initial), [moving, setMoving] = useState(false);
  const set = useCallback((next: number) => { cancelAnimationFrame(frame.current); current.current = next; setState(next); setMoving(false); }, []);
  const stop = useCallback(() => { cancelAnimationFrame(frame.current); setMoving(false); }, []);
  const move = useCallback((target: number, duration = 850, from = current.current) => {
    cancelAnimationFrame(frame.current);
    if (reduced || target === from) { current.current = target; setState(target); setMoving(false); return; }
    const start = performance.now(); current.current = from; setState(from); setMoving(true);
    const draw = (time: number) => {
      const t = Math.min(1, (time - start) / duration), eased = 1 - (1 - t) ** 3;
      current.current = from + (target - from) * eased; setState(current.current);
      if (t < 1) frame.current = requestAnimationFrame(draw); else { current.current = target; setState(target); setMoving(false); }
    };
    frame.current = requestAnimationFrame(draw);
  }, [reduced]);
  useEffect(() => () => cancelAnimationFrame(frame.current), []);
  useEffect(() => { if (reduced) stop(); }, [reduced, stop]);
  return { value, set, move, stop, moving, reduced };
}

function BalanceLesson() {
  const id = useId(), root = useMemo(() => 1 / alphaRoot(), []), motion = useNumberMotion(130);
  const sides = (inverse: number) => {
    const a = 1 / inverse, q = 48 * C3 ** 4 * Math.exp(-2 * a), response = 1 / (6 * Math.PI) + q * (1 - q) ** (-5 / 4);
    return [a ** 3 - 2 * C3 ** 3 * a ** 2, (4 / 5) * 41 * C3 ** 6 * Math.log(1 / response)];
  };
  const [left, right] = sides(motion.value), scale = Math.max(...sides(130), ...sides(145)), balanced = Math.abs(left - right) < 1e-15;
  return <section className={styles.lesson} aria-label="Balance the two sides of the alpha equation">
    <header className={styles.intro}><h2>Make two sides equal</h2><p>Move the slider. It changes the trial coupling, so the two sides of the specified equation change. Find balance when both bars have the same length.</p></header>
    <figure className={styles.stage}><svg viewBox="0 0 640 290" role="img" aria-label={`First side ${left.toExponential(5)}. Second side ${right.toExponential(5)}. ${balanced ? "The sides balance." : "The sides are different."}`}>
      {[{ label: "First side", value: left, y: 78, color: colors[0] }, { label: "Second side", value: right, y: 183, color: colors[1] }].map(row => <g key={row.label}><text x="36" y={row.y - 21} fill="#d4e1f1" fontSize="25">{row.label}</text><rect x="36" y={row.y} width="568" height="30" fill="#223b55" rx="3"/><rect x="36" y={row.y} width={svg(row.value / scale * 568)} height="30" fill={row.color} rx="3"/></g>)}
      <text x="320" y="262" textAnchor="middle" fill="#d4e1f1" fontSize="24">{balanced ? "Equal lengths. The equation balances." : left > right ? "The first side is larger." : "The second side is larger."}</text>
    </svg><figcaption>Both bars use the same fixed scale and the actual equation values.</figcaption></figure>
    <label className={styles.slider} htmlFor={`${id}-balance`}>Trial number <output>{motion.value.toFixed(10)}</output><input id={`${id}-balance`} type="range" min="130" max="145" step=".001" value={motion.value} onChange={event => motion.set(Number(event.target.value))}/></label>
    <div className={styles.controls}><button type="button" onClick={() => motion.move(root)}>Find balance</button>{motion.moving && <button type="button" onClick={motion.stop}>Pause movement</button>}<button type="button" onClick={() => motion.set(130)}>Start again</button></div>
    <div className={styles.result} aria-live="polite"><strong>{balanced ? `The bars balance at ${root.toFixed(10)}` : left > right ? "The first side is larger." : "The second side is larger."}</strong><span>{balanced ? `Alpha is 1 divided by this number: approximately ${(1 / root).toFixed(8)}.` : "Move the trial number, or choose Find balance."}</span></div><details className={styles.details}><summary>See the equation values</summary><p>First side {left.toExponential(5)} · second side {right.toExponential(5)} · difference {Math.abs(left - right).toExponential(3)}.</p></details>
    <p className={styles.note}>This balances the stated mathematical equation. Connecting it to physical electromagnetism is a separate step in the full derivation.</p>
  </section>;
}

function MatterLesson() {
  const [mask, setMask] = useState(0), [before, setBefore] = useState(0);
  const charge = (value: number) => [-2, -2, -2, 3, 3].reduce((sum, q, i) => sum + (value & 1 << i ? q : 0), 0);
  const select = (value: number) => { setBefore(mask); setMask(value); };
  const selected = countBits(mask), even = selected % 2 === 0;
  const contributions = ["−1/3", "−1/3", "−1/3", "1/2", "1/2"].filter((_, i) => Boolean(mask & 1 << i));
  return <section className={styles.lesson} aria-label="Select five slots and add their charges">
    <header className={styles.intro}><h2>Choose slots. Add their numbers.</h2><p>The model supplies five slots. Each selected colour slot adds −1/3; each selected weak slot adds +1/2. Try one of each.</p></header>
    <div className={styles.slotBoard}><div className={styles.slotGroup}><h3>Three colour slots</h3><div>{[0, 1, 2].map(i => <button type="button" key={i} aria-pressed={Boolean(mask & 1 << i)} onClick={() => select(mask ^ 1 << i)}><span className={styles.slotDot}/><strong>Colour {i + 1}</strong><span>−1/3</span></button>)}</div></div><div className={styles.slotGroup}><h3>Two weak slots</h3><div>{[3, 4].map(i => <button type="button" key={i} aria-pressed={Boolean(mask & 1 << i)} onClick={() => select(mask ^ 1 << i)}><span className={styles.slotDot}/><strong>Weak {i - 2}</strong><span>+1/2</span></button>)}</div></div></div>
    <p className={styles.addition} aria-live="polite">{contributions.length ? `${contributions.join(" + ")} = ${fraction(charge(mask)).replace(/^\+/, "")}` : "Choose a slot to begin."}</p><div className={styles.beforeAfter} aria-live="polite"><div><span>Before</span><strong>{fraction(charge(before))}</strong></div><span aria-hidden="true">→</span><div><span>Selected slot charge</span><strong>{fraction(charge(mask))}</strong></div></div>
    <p className={styles.notice} aria-live="polite">{selected} selected · {even ? "an even pattern in the set below" : "an odd pattern, outside the even set shown below"}.</p>
    <div className={styles.patternGroups}>{[0, 2, 4].map(degree => <div key={degree}><h3>{degree} selected · {degree === 0 ? 1 : degree === 2 ? 10 : 5} {degree === 0 ? "pattern" : "patterns"}</h3><div className={styles.patterns}>{Array.from({ length: 32 }, (_, value) => value).filter(value => countBits(value) === degree).map(value => <button type="button" key={value} aria-pressed={value === mask} aria-label={`Select pattern ${Array.from({ length: 5 }, (_, i) => value & 1 << i ? "1" : "0").join("")}`} onClick={() => select(value)}>{Array.from({ length: 5 }, (_, i) => <i key={i} data-selected={Boolean(value & 1 << i)}/>)}</button>)}</div></div>)}</div>
    <p className={styles.note}>One empty pattern + ten pairs + five four-slot patterns = sixteen even choices. These sums are hypercharges in the specified slot dictionary. The full calculation connects them to the particle representations.</p>
  </section>;
}

const rootOrder = [0, 2, 1, 3], rootCounts = [52, 60, 64, 64];
function RootAssemblyLesson() {
  const [built, setBuilt] = useState(0), [auto, setAuto] = useState(false), motion = useNumberMotion(1);
  const points = useMemo(() => {
    const basis = [Array.from({ length: 8 }, (_, i) => .5 * Math.cos(i * Math.PI / 4)), Array.from({ length: 8 }, (_, i) => .5 * Math.sin(i * Math.PI / 4))];
    return E8_ROOTS.map(root => ({ stage: rootOrder.indexOf(root.coset), x: svg(390 + 120 * inner(root.vector, basis[0])), y: svg(210 + 120 * inner(root.vector, basis[1])) }));
  }, []);
  const add = useCallback(() => { if (built >= 4) return; setBuilt(value => value + 1); motion.move(1, 750, 0); }, [built, motion.move]);
  useEffect(() => { if (!auto || motion.moving || built >= 4) return; const timer = setTimeout(add, 260); return () => clearTimeout(timer); }, [auto, built, motion.moving, add]);
  const count = rootCounts.slice(0, built).reduce((sum, value) => sum + value, 0);
  return <section className={styles.lesson} aria-label="Assemble four root groups into E8">
    <header className={styles.intro}><h2>Join four groups of points</h2><p>Build one group at a time. Each dot represents one shortest vector in the eight-coordinate lattice. The four groups together contain 240 vectors.</p></header>
    <figure className={styles.stage}><svg viewBox="0 0 640 420" role="img" aria-label={`${built} of four groups added, representing ${count} of 240 vectors.`}>{rootCounts.map((value, i) => <g key={i}><circle cx="60" cy={60 + i * 100} r="24" fill={built > i ? colors[i] : "#29415c"}/><text x="60" y={68 + i * 100} textAnchor="middle" fill={built > i ? "#112b43" : "#bacde1"} fontSize="23">{value}</text><text x="60" y={104 + i * 100} textAnchor="middle" fill="#bacde1" fontSize="21">Group {i + 1}</text></g>)}{points.filter(point => point.stage < built).map((point, i) => { const p = point.stage === built - 1 ? motion.value : 1; return <circle key={i} cx={svg(60 + (point.x - 60) * p)} cy={svg(60 + point.stage * 100 + (point.y - 60 - point.stage * 100) * p)} r="3.1" fill={colors[point.stage]} opacity={.25 + .75 * p}/>; })}</svg><figcaption>The movement assembles a drawing. The dots are mathematical vectors, rather than moving physical particles. Different vectors can overlap on this flat screen.</figcaption></figure>
    <div className={styles.controls}><button type="button" disabled={built >= 4 || motion.moving} onClick={() => { setAuto(false); add(); }}>Build next group</button><button type="button" onClick={() => { setBuilt(0); motion.set(1); setAuto(true); }}>Replay assembly</button>{auto && built < 4 && <button type="button" onClick={() => setAuto(false)}>Pause after this group</button>}</div>
    <div className={styles.result} aria-live="polite"><strong>{count} of 240 points added</strong><span>{rootCounts.map((value, i) => built > i ? value : "?").join(" + ")}{built === 4 ? " = 240" : ""}</span></div>
    <p className={styles.note}>This is a flat projection of the original E₈ vectors. The full calculation explains why these four particular groups fit into one even lattice with determinant one.</p>
  </section>;
}

function DistributionLesson() {
  const presets = [[1, 0, 0], [.8, .15, .05], [1 / 3, 1 / 3, 1 / 3]], names = ["All weight in bin 1", "Uneven start", "Already equal"];
  const [preset, setPreset] = useState(1), [step, setStep] = useState(0), [auto, setAuto] = useState(false), motion = useNumberMotion(1);
  const cleanDisplayWeight = (value: number) => Math.abs(value) < 1e-12 ? 0 : value;
  const initial = presets[preset], before = familyTransfer(initial, Math.max(0, step - 1)).map(cleanDisplayWeight), after = familyTransfer(initial, step).map(cleanDisplayWeight);
  const values = after.map((value, i) => before[i] + (value - before[i]) * motion.value);
  const advance = useCallback(() => { if (step >= 8) return; setStep(value => value + 1); motion.move(1, 700, 0); }, [step, motion.move]);
  useEffect(() => { if (!auto || motion.moving || step >= 8) return; const timer = setTimeout(advance, 280); return () => clearTimeout(timer); }, [auto, motion.moving, step, advance]);
  const reset = () => { setAuto(false); setStep(0); motion.set(1); };
  return <section className={styles.lesson} aria-label="Redistribute three weights with the actual transfer">
    <header className={styles.intro}><h2>Redistribute a fixed total</h2><p>Choose a starting arrangement, then take one step. The specified transfer brings the three weights closer together while their total stays one.</p></header>
    <div className={styles.choiceRow} role="group" aria-label="Starting distribution">{names.map((name, i) => <button type="button" key={name} aria-pressed={preset === i} onClick={() => { reset(); setPreset(i); }}>{name}</button>)}</div>
    <figure className={styles.stage}><svg viewBox="0 0 640 350" role="img" aria-label={`After ${step} steps, weights ${values.map(value => value.toFixed(6)).join(", ")}. Total one.`}>{values.map((value, i) => <g key={i}><rect x={75 + i * 185} y="45" width="120" height="220" rx="4" fill="#203b55"/><rect x={75 + i * 185} y={svg(265 - value * 220)} width="120" height={svg(value * 220)} rx="3" fill={colors[i]}/><rect x={75 + i * 185} y={svg(265 - before[i] * 220)} width="120" height={svg(before[i] * 220)} fill="none" stroke="#c0d2e5" strokeDasharray="4 5"/><text x={135 + i * 185} y="306" textAnchor="middle" fill="#d4e1f1" fontSize="25">Bin {i + 1}</text><text x={135 + i * 185} y="338" textAnchor="middle" fill="#d4e1f1" fontSize="24">{(value * 100).toFixed(2)}%</text></g>)}</svg><figcaption>Filled bars show the current picture. Dashed outlines show the values before this step. Animation connects the two calculated arrangements.</figcaption></figure>
    <div className={styles.controls}><button type="button" disabled={step >= 8 || motion.moving} onClick={() => { setAuto(false); advance(); }}>One step</button><button type="button" onClick={() => { if (step >= 8) { setStep(0); motion.set(1); } setAuto(true); }}>Run 8 steps</button>{auto && step < 8 && <button type="button" onClick={() => setAuto(false)}>Pause after this step</button>}<button type="button" onClick={reset}>Reset</button></div>
    <div className={styles.result} aria-live="polite"><strong>Step {step} · total {values.reduce((sum, value) => sum + value, 0).toFixed(6)}</strong><span>Before: {before.map(value => value.toFixed(4)).join(" · ")}<br/>After: {after.map(value => value.toFixed(4)).join(" · ")}</span></div>
    <p className={styles.note}>These are mathematical weights updated by the original three-component transfer. A step here does not specify a number of seconds or the full physical dynamics.</p>
  </section>;
}

function SeedLesson() {
  const id = useId(), arrow = useId(), motion = useNumberMotion(FIXED_SEED), values = seedReadouts(motion.value);
  const [target, setTarget] = useState(FIXED_SEED);
  const labels = ["Quark mixing", "Neutrino mixing", "Light rotation", "Ordinary matter"], places = [[125, 100], [515, 100], [125, 305], [515, 305]];
  return <section className={styles.lesson} aria-label="One starting number changes four readouts">
    <header className={styles.intro}><h2>Change one number. Follow four results.</h2><p>Move the starting number in the centre. All four formulas use it, so all four results respond to the same change.</p></header>
    <figure className={styles.stage}><svg viewBox="0 0 640 410" role="img" aria-label={`Starting number ${motion.value.toFixed(8)} gives ${values.map(value => value.toFixed(7)).join(", ")}.`}><defs><marker id={arrow} markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L6,3.5 L0,7" fill="none" stroke="#8ba8cc"/></marker></defs>{places.map(([x, y], i) => <g key={i}><line x1={x < 320 ? 268 : 372} y1={y < 180 ? 170 : 230} x2={x < 320 ? x + 55 : x - 55} y2={y < 180 ? y + 22 : y - 22} stroke="#8ba8cc" strokeWidth="2" markerEnd={`url(#${arrow})`}/><circle cx={x} cy={y} r="56" fill="#1d3853" stroke={colors[i]} strokeWidth="2"/><text x={x} y={y + 8} textAnchor="middle" fill={colors[i]} fontSize="26">{values[i].toFixed(5)}{i === 2 ? "°" : ""}</text><text x={x} y={y < 180 ? y - 66 : y + 76} textAnchor="middle" fill="#d4e1f1" fontSize="23">{labels[i]}</text></g>)}<circle cx="320" cy="200" r="63" fill="#294b76"/><text x="320" y="197" textAnchor="middle" fill="#ffffff" fontSize="27">{motion.value.toFixed(5)}</text><text x="320" y="226" textAnchor="middle" fill="#d4e1f1" fontSize="22">Starting number</text></svg><figcaption>The arrows connect one shared input to four actual formula outputs.</figcaption></figure>
    <label className={styles.slider} htmlFor={`${id}-seed`}>Trial starting number <output>{target.toFixed(8)}</output><input id={`${id}-seed`} type="range" min=".035" max=".07" step=".00001" value={target} onChange={event => { const value = Number(event.target.value); setTarget(value); motion.move(value, 260); }}/></label>
    <div className={styles.controls}><button type="button" onClick={() => { setTarget(FIXED_SEED); motion.move(FIXED_SEED); }}>Restore the fixed starting number</button>{motion.moving && <button type="button" onClick={() => { setTarget(motion.value); motion.stop(); }}>Pause movement</button>}</div>
    <p className={styles.notice}>Fixed TFPT starting number: {FIXED_SEED.toFixed(9)}. The slider explores how the formulas depend on it.</p><p className={styles.note}>The outputs have different meanings and units. The rotation is shown in degrees. Their physical interpretations retain the premises explained in the full calculation.</p>
  </section>;
}

function PredictionLesson({ inverseAlpha, comparison }: { inverseAlpha: number; comparison?: Comparison }) {
  const [stage, setStage] = useState(0), [computed, setComputed] = useState<number | null>(null);
  const central = Number(comparison?.central), uncertainty = Number(comparison?.uncertaintyMinus), predicted = comparison?.predicted ?? inverseAlpha;
  const valid = comparison && Number.isFinite(central) && uncertainty > 0, difference = valid ? (predicted - central) / uncertainty : 0;
  const point = svg(320 + Math.max(-3, Math.min(3, difference)) * 260 / 3);
  return <section className={styles.lesson} aria-label="Calculate a number, inspect its record and compare a measurement">
    <header className={styles.intro}><h2>Put a calculation beside a measurement</h2><p>First calculate the balance point, then inspect the number already recorded by the project. Finally compare it with the dated measurement.</p></header>
    <ol className={styles.reveals}>
      <li><button type="button" onClick={() => { setComputed(1 / alphaRoot()); setStage(value => Math.max(1, value)); }}>Calculate</button><div aria-live="polite"><h3>Calculate the balance number</h3>{stage >= 1 ? <strong>{computed?.toFixed(10)}</strong> : <span>The number appears after calculation.</span>}</div></li>
      <li><button type="button" disabled={stage < 1} onClick={() => setStage(value => Math.max(2, value))}>See the recorded value</button><div aria-live="polite"><h3>Read the existing record</h3>{stage >= 2 ? <strong>{predicted.toFixed(10)}</strong> : <span>The recorded value stays fixed.</span>}</div></li>
      <li><button type="button" disabled={stage < 2 || !valid} onClick={() => setStage(3)}>Compare with measurement</button><div aria-live="polite"><h3>Place them on one scale</h3>{stage >= 3 ? <strong>{difference.toFixed(2)} experimental uncertainty units apart</strong> : <span>The measurement has its own date and uncertainty.</span>}</div></li>
    </ol>
    {stage >= 3 && valid && <><figure className={styles.stage}><svg viewBox="0 0 640 220" role="img" aria-label={`The calculated value lies ${difference.toFixed(2)} standard uncertainties from the measured central value.`}><rect x={svg(320 - 260 / 3)} y="75" width={svg(520 / 3)} height="52" fill="#275c54"/><line x1="60" x2="580" y1="127" y2="127" stroke="#8ba8cc"/>{[-3, -2, -1, 0, 1, 2, 3].map(value => <g key={value}><line x1={svg(320 + value * 260 / 3)} x2={svg(320 + value * 260 / 3)} y1="127" y2="139" stroke="#8ba8cc"/><text x={svg(320 + value * 260 / 3)} y="171" textAnchor="middle" fill="#d4e1f1" fontSize="24">{value > 0 ? "+" : ""}{value}</text></g>)}<line x1="320" x2="320" y1="58" y2="127" stroke={colors[1]} strokeWidth="2"/><text x="320" y="42" fill={colors[1]} textAnchor="middle" fontSize="23">Measured</text><line x1={point} x2={point} y1="58" y2="127" stroke={colors[0]} strokeWidth="2"/><circle cx={point} cy="93" r="7" fill={colors[0]}/><text x={point} y="42" fill={colors[0]} textAnchor="middle" fontSize="23">Calculated</text><text x="320" y="210" textAnchor="middle" fill="#d4e1f1" fontSize="22">One unit = one quoted experimental uncertainty</text></svg><figcaption>The green band spans one quoted uncertainty on either side of the measured central value.</figcaption></figure><div className={styles.result}><strong>Measured: {comparison.measured}</strong><span>{comparison.date}</span></div></>}
    <div className={styles.controls}><button type="button" onClick={() => setStage(0)}>Replay the comparison</button></div><p className={styles.note}>This compares a calculated relation with data that were already known. The recorded number and the measurement retain their original dates and conditions.</p>
  </section>;
}

function CosmosLesson() {
  const id = useId(), motion = useNumberMotion(55), n = motion.value, tilt = 1 - 2 / n, waves = 12 / n ** 2;
  const [target, setTarget] = useState(55);
  const outputs = [{ name: "Pattern tilt", symbol: "nₛ", value: tilt, min: .96, max: 1 - 2 / 60, places: 6 }, { name: "Relative wave strength", symbol: "r", value: waves, min: 12 / 60 ** 2, max: 12 / 50 ** 2, places: 6 }];
  return <section className={styles.lesson} aria-label="One inflation input controls two readouts"><header className={styles.intro}><h2>One choice changes two results</h2><p>The inflation branch uses a supplied value called N. Increase it and the pattern tilt rises while the relative wave strength falls.</p></header>
    <label className={styles.slider} htmlFor={`${id}-n`}>Trial value N <output>{target.toFixed(1)}</output><input id={`${id}-n`} type="range" min="50" max="60" step=".1" value={target} onChange={event => { const value = Number(event.target.value); setTarget(value); motion.move(value, 300); }}/></label>
    <div className={styles.cosmicOutputs}>{outputs.map(output => <div key={output.symbol}><h3>{output.name}</h3><output>{output.value.toFixed(output.places)}</output><svg viewBox="0 0 280 110" role="img" aria-label={`${output.name}, ${output.symbol}, equals ${output.value.toFixed(output.places)}. Scale ${output.min.toFixed(4)} to ${output.max.toFixed(4)}.`}><line x1="30" x2="250" y1="45" y2="45" stroke="#8298af"/><circle cx={svg(30 + (output.value - output.min) / (output.max - output.min) * 220)} cy="45" r="9" fill="#2b57b6"/><text x="30" y="91" fill="#34526f" fontSize="23">{output.min.toFixed(4)}</text><text x="250" y="91" textAnchor="end" fill="#34526f" fontSize="23">{output.max.toFixed(4)}</text></svg><p>{output.symbol} = {output.symbol === "r" ? "12 / N²" : "1 − 2 / N"}</p></div>)}</div>
    <div className={styles.controls}><button type="button" onClick={() => { setTarget(60); motion.move(60, 2000, 50); }}>Play N from 50 to 60</button>{motion.moving && <button type="button" onClick={() => { setTarget(motion.value); motion.stop(); }}>Pause movement</button>}<button type="button" onClick={() => { setTarget(55); motion.move(55); }}>Return to N = 55</button></div>
    <p className={styles.note}>The same input appears in both formulas. The wave readout r is wave power divided by density-fluctuation power. N depends on the stated inflation and reheating history; this control does not derive that external choice. Animation shows formula dependence, rather than time passing in the early universe.</p>
  </section>;
}

function QuantumLesson() {
  const [mode, setMode] = useState("phase"), [turn, setTurn] = useState(0), [clock, setClock] = useState(0), [playing, setPlaying] = useState(false), reduced = useReducedMotion();
  useEffect(() => { if (!playing || reduced) return; const limit = mode === "phase" ? 4 : 30, value = mode === "phase" ? turn : clock; if (value >= limit) { setPlaying(false); return; } const timer = setTimeout(() => mode === "phase" ? setTurn(n => n + 1) : setClock(n => n + 1), mode === "phase" ? 650 : 220); return () => clearTimeout(timer); }, [playing, reduced, mode, turn, clock]);
  const phase = turn % 4, rotation = useNumberMotion(0);
  useEffect(() => rotation.move(turn * 90, 500), [turn, rotation.move]);
  return <section className={styles.lesson} aria-label="Change a common phase while keeping the probabilities fixed"><header className={styles.intro}><h2>Turn the phase. Keep the odds.</h2><p>In this worked state, the two possible outcomes each have a 50% probability. The shared phase is represented by the arrow’s direction. A quarter turn changes that direction for both parts together, leaving those probabilities unchanged.</p></header>
    <div className={styles.choiceRow} role="group" aria-label="Choose the phase or clock example"><button type="button" aria-pressed={mode === "phase"} onClick={() => { setMode("phase"); setPlaying(false); }}>Phase and probability</button><button type="button" aria-pressed={mode === "clocks"} onClick={() => { setMode("clocks"); setPlaying(false); }}>Two clocks</button></div>
    {mode === "phase" ? <><figure className={styles.stage}><svg viewBox="0 0 640 355" role="img" aria-label={`${phase} quarter turns. Shared arrow direction after ${phase} quarter turns. Outcomes 00 and 11 each have probability fifty percent.`}><circle cx="190" cy="165" r="103" fill="none" stroke="#4d6a89"/>{["Start", "¼ turn", "½ turn", "¾ turn"].map((label, i) => { const a = -Math.PI / 2 + i * Math.PI / 2; return <text key={label} x={svg(190 + 132 * Math.cos(a))} y={svg(173 + 132 * Math.sin(a))} textAnchor="middle" fill={phase === i ? colors[1] : "#b7cde4"} fontSize="26">{label}</text>; })}<g transform={`rotate(${svg(rotation.value)} 190 165)`}><line x1="190" y1="165" x2="190" y2="74" stroke={colors[1]} strokeWidth="5"/><circle cx="190" cy="74" r="8" fill={colors[1]}/></g><text x="190" y="334" textAnchor="middle" fill="#d4e1f1" fontSize="22">Shared arrow direction</text>{["00", "11"].map((label, i) => <g key={label}><text x="402" y={75 + i * 125} fill="#d4e1f1" fontSize="24">Outcome {label}</text><rect x="400" y={95 + i * 125} width="190" height="28" fill="#29415d"/><rect x="400" y={95 + i * 125} width="95" height="28" fill={colors[0]}/><text x="400" y={157 + i * 125} fill={colors[0]} fontSize="29">50%</text></g>)}</svg><figcaption>Only the common phase turns. The fixed probability bars describe this particular Bell state.</figcaption></figure><div className={styles.controls}><button type="button" onClick={() => { setPlaying(false); setTurn(n => n + 1); }}>Quarter turn</button><button type="button" disabled={reduced} onClick={() => { setTurn(0); setPlaying(true); }}>Play 4 turns</button>{playing && <button type="button" onClick={() => setPlaying(false)}>Pause</button>}<button type="button" onClick={() => { setPlaying(false); setTurn(0); }}>Reset phase</button></div><p className={styles.notice} aria-live="polite">{phase} quarter turns · the shared arrow changes direction · probabilities stay 50% and 50%.</p></> : <><figure className={styles.stage}><svg viewBox="0 0 640 320" role="img" aria-label={`Combined step ${clock}, five-cycle position ${clock % 5} and six-cycle position ${clock % 6}.`}>{[5, 6].map((count, k) => <g key={count}><circle cx={175 + k * 290} cy="150" r="100" fill="none" stroke="#4d6a89"/>{Array.from({ length: count }, (_, i) => { const a = -Math.PI / 2 + i * 2 * Math.PI / count; return <g key={i}><circle cx={svg(175 + k * 290 + 100 * Math.cos(a))} cy={svg(150 + 100 * Math.sin(a))} r="18" fill={i === clock % count ? colors[1] : "#29415d"}/><text x={svg(175 + k * 290 + 100 * Math.cos(a))} y={svg(157 + 100 * Math.sin(a))} textAnchor="middle" fill={i === clock % count ? "#112b43" : "#d4e1f1"} fontSize="23">{i}</text></g>; })}<text x={175 + k * 290} y="155" textAnchor="middle" fill="#d4e1f1" fontSize="26">{count} positions</text><text x={175 + k * 290} y="295" textAnchor="middle" fill="#b7cde4" fontSize="23">Position {clock % count}</text></g>)}</svg><figcaption>The pair returns after thirty steps because five and six have no common factor.</figcaption></figure><div className={styles.controls}><button type="button" onClick={() => { setPlaying(false); setClock(n => n + 1); }}>Advance one step</button><button type="button" disabled={reduced} onClick={() => { setClock(0); setPlaying(true); }}>Run 30 steps</button>{playing && <button type="button" onClick={() => setPlaying(false)}>Pause</button>}<button type="button" onClick={() => { setPlaying(false); setClock(0); }}>Reset clocks</button></div><p className={styles.notice} aria-live="polite">Step {clock} · {clock > 0 && clock % 30 === 0 ? "Both clocks are back at the start." : `${30 - clock % 30} steps to the next shared return.`}</p></>}
    <p className={styles.note}>The specified mapping from the lattice supplies this quantum example. Clock steps and playback speed here are mathematical illustrations, rather than physical seconds.</p>
  </section>;
}

export function BeginnerExperiments({ chapter, inverseAlpha, comparison, embedded = false }: BeginnerExperimentsProps) {
  return <div className={`${styles.root}${embedded ? ` ${styles.embedded}` : ""}`}>
    {chapter === "alpha" ? <BalanceLesson/> : chapter === "standard-model" ? <MatterLesson/> : chapter === "e8" ? <RootAssemblyLesson/> : chapter === "dynamics" ? <DistributionLesson/> : chapter === "flavor" ? <SeedLesson/> : chapter === "predictions" ? <PredictionLesson inverseAlpha={inverseAlpha} comparison={comparison}/> : chapter === "cosmology" ? <CosmosLesson/> : chapter === "quantum" ? <QuantumLesson/> : null}
  </div>;
}
