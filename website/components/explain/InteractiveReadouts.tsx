"use client";

import { useState } from "react";
import Link from "next/link";
import { CarrierFigure } from "./CarrierFigure";
import { chargeSectors } from "@/lib/carrier";

const fraction = (n: number, d = 6): string => {
  if (!n) return "0";
  const gcd = (a: number, b: number): number => b ? gcd(b, a % b) : a;
  const g = gcd(Math.abs(n), d);
  return `${n < 0 ? "−" : ""}${Math.abs(n) / g}${d / g === 1 ? "" : `/${d / g}`}`;
};
const sectors: Record<string, [string, string, number]> = {
  "0,0": ["νᶜ", "Neutrino singlet", 1], "2,0": ["uᶜ", "Conjugate up quark", 3],
  "1,1": ["Q", "Quark doublet", 6], "0,2": ["eᶜ", "Conjugate charged lepton", 1],
  "3,1": ["L", "Lepton doublet", 2], "2,2": ["dᶜ", "Conjugate down quark", 3],
};
export function ChargeExplorer() {
  const [mask, setMask] = useState(9);
  const c = [0, 1, 2].filter(i => mask & (1 << i)).length;
  const w = [3, 4].filter(i => mask & (1 << i)).length;
  const y = -2 * c + 3 * w;
  const t = 3 * (Number(Boolean(mask & 8)) - Number(Boolean(mask & 16)));
  const sector = sectors[`${c},${w}`];
  return <div className="readout-box">
    <div className="charge-composition"><div><div className="grid gap-7 sm:grid-cols-2 lg:grid-cols-1">
      {[[0, 1, 2], [3, 4]].map((indices, group) => <div key={group}>
        <p className="font-medium text-slate-950">{group ? "Two weak slots · Y = +1/2 each" : "Three colour slots · Y = −1/3 each"}</p>
        <div className="mt-3 flex flex-wrap gap-2" role="group" aria-label={group ? "Select weak slots" : "Select colour slots"}>
          {indices.map(i => <button type="button" key={i} aria-pressed={Boolean(mask & (1 << i))}
            onClick={() => setMask(mask ^ (1 << i))} className={`readout-button ${mask & (1 << i) ? "is-selected" : ""}`}>
            {i < 3 ? `Colour ${i + 1}` : i === 3 ? "Weak +" : "Weak −"}
          </button>)}
        </div>
      </div>)}
    </div>
    <div className="my-6 border-y border-slate-300 py-5" aria-live="polite" aria-atomic="true">
      <p className="font-serif text-2xl text-slate-950">Y = {c} × (−1/3) + {w} × (1/2) = {fraction(y)}</p>
      {sector ? <><p className="mt-3 font-medium">{sector[0]} · {sector[1]} · {sector[2]} {sector[2] === 1 ? "component" : "components"}</p>
        <p className="mt-2">Electric charge Qₑ = T₃ + Y = {fraction(t)} + ({fraction(y)}) = {fraction(t + y)}</p></>
        : <p className="mt-3">This selection has odd exterior degree. It belongs to the other half spinor, outside the S⁺ family displayed here.</p>}
      <p className="mt-2 text-sm text-slate-600">Exterior degree {c + w} · {sector ? "in S⁺ = Λ⁰ ⊕ Λ² ⊕ Λ⁴" : "outside S⁺"}</p>
    </div>
    <p className="mb-3 text-sm text-slate-700">Choose a sector, or select the slots above.</p>
    <div className="flex flex-wrap gap-2">{[[0,"νᶜ"],[3,"uᶜ"],[9,"Q"],[24,"eᶜ"],[15,"L"],[27,"dᶜ"]].map(([value, label]) =>
      <button type="button" key={value} onClick={() => setMask(Number(value))} className="readout-button" aria-label={`Show ${label} sector`}>{label}</button>)}</div>
    </div><CarrierFigure selectedMask={mask} /></div>
    <p className="mt-5 text-sm">{sector ? "The outlined selection locates this component in the whole family." : "No cell is outlined because this odd selection belongs to the other half spinor."} The superscript c denotes the conjugate field convention.</p>
    <details className="guide-details mt-5"><summary>See how the whole family contributes 120</summary>
      <p>For X = 6Y, each sector contributes its number of components times X². Changing the selected component above highlights its sector here. The full family sum stays fixed.</p>
      <div className="figure-table-scroll" role="region" aria-label="Charge trace table" tabIndex={0}><table className="figure-table"><caption>Tr X² over all sixteen components</caption><thead><tr><th>Sector</th><th>Components</th><th>X = 6Y</th><th>Contribution</th></tr></thead><tbody>{chargeSectors.map(row => <tr key={row.label} className={sector?.[0] === row.label ? "is-current" : undefined}><th>{row.label}</th><td>{row.multiplicity}</td><td>{row.x}</td><td>{row.multiplicity} × {row.x < 0 ? `(${row.x})` : row.x}² = {row.contribution}</td></tr>)}</tbody><tfoot><tr><th>Total</th><td>16</td><td /><td>120</td></tr></tfoot></table></div>
    </details>
    <details className="guide-details mt-5"><summary>What is assumed in this demonstration?</summary>
      <p>This reader starts with the five dimensional carrier, its 3+2 marking, the normalized hypercharge operator and the even exterior representation. It demonstrates the charge readout. The source and physical selection of that marking are separate questions.</p>
      <Link href="/results?search=hypercharge">Inspect the charge claims and their inputs</Link>
    </details>
  </div>;
}

const c3 = 1 / (8 * Math.PI);
function F(a: number) {
  const q = 48 * c3 ** 4 * Math.exp(-2 * a);
  const phi = 1 / (6 * Math.PI) + q * (1 - q) ** (-5 / 4);
  return a ** 3 - 2 * c3 ** 3 * a ** 2 - (4 / 5) * 41 * c3 ** 6 * Math.log(1 / phi);
}
export function AlphaExplorer() {
  const [inverse, setInverse] = useState(137.0359992168407);
  const [zoom, setZoom] = useState(false);
  const min = zoom ? 137.03 : 130, max = zoom ? 137.04 : 145;
  const extent = Math.max(Math.abs(F(1 / min)), Math.abs(F(1 / max))) * 1.14;
  const path = Array.from({ length: 161 }, (_, i) => {
    const x = min + (max - min) * i / 160;
    return `${i ? "L" : "M"}${(50 + i * 3.125).toFixed(4)},${(105 - F(1 / x) / extent * 75).toFixed(4)}`;
  }).join(" ");
  const dotX = 50 + (inverse - min) / (max - min) * 500;
  const dotY = 105 - F(1 / inverse) / extent * 75;
  return <div className="readout-box">
    <p className="text-sm text-slate-600">The function is fixed. The slider changes the trial value, not the equation.</p>
    <svg viewBox="0 0 600 250" className="alpha-residual-chart" role="img" aria-labelledby="alpha-chart-title alpha-chart-description">
      <title id="alpha-chart-title">Residual of the specified electromagnetic equation</title>
      <desc id="alpha-chart-description">The horizontal axis is inverse alpha. The curve crosses zero near 137.0359992168. This plot illustrates a root and does not prove global uniqueness or physical identification.</desc>
      <line x1="50" y1="105" x2="550" y2="105" stroke="#94a3b8" />
      <path d={path} fill="none" stroke="#1d4ed8" strokeWidth="2.5" />
      <circle cx={dotX.toFixed(4)} cy={dotY.toFixed(4)} r="5" fill="#1e3a8a" />
      <text x="50" y="202" fontSize="24" fill="#334155">{min}</text><text x="550" y="202" textAnchor="end" fontSize="24" fill="#334155">{max}</text>
      <text x="300" y="238" textAnchor="middle" fontSize="24" fill="#334155">Inverse alpha</text><text x="16" y="112" fontSize="24" fill="#334155">0</text>
      <text x="50" y="24" fontSize="24" fill="#334155">F(α), scaled</text>
    </svg>
    <label htmlFor="alpha-trial" className="mt-4 block font-medium">Trial α⁻¹ = <output className="tabular-nums">{inverse.toFixed(10)}</output></label>
    <input id="alpha-trial" type="range" className="my-4 w-full accent-blue-800" min={min} max={max} step={zoom ? 0.0000001 : 0.001} value={inverse} onChange={e => setInverse(Number(e.target.value))} />
    <div className="flex flex-wrap gap-3">
      <button type="button" className="readout-button" onClick={() => { setInverse(137.0359992168407); }}>Locate the calculated root</button>
      <button type="button" className="readout-button" aria-pressed={zoom} onClick={() => { setZoom(!zoom); setInverse(137.0359992168407); }}>{zoom ? "Show wider interval" : "Zoom into the root"}</button>
    </div>
    <p className="mt-4 text-sm" aria-live="polite">Residual |F(α)| {Math.abs(F(1 / inverse)) < 1e-18 ? "< 10⁻¹⁸" : `≈ ${Math.abs(F(1 / inverse)).toExponential(3)}`}. This display uses ordinary browser arithmetic; the source proof and interval enclosure are separate evidence.</p>
  </div>;
}

export function ClockExplorer() {
  const [power, setPower] = useState(0);
  const multiplier = [1, 2, 4, 3][power];
  return <div className="readout-box">
    <p className="font-medium">A quarter action changes the labels of the five cycle.</p>
    <div className="clock-action-layout"><svg viewBox="0 0 340 290" role="img" aria-label={`Five cycle after ${power} applications of G. Labels clockwise are ${[0,1,2,3,4].map(i=>i*multiplier%5).join(', ')}. The arrows connect successive original positions.`}>
      <defs><marker id="finite-clock-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#64748b" /></marker></defs>
      {[0,1,2,3,4].map(i => {const a=-Math.PI/2+i*2*Math.PI/5,b=a+2*Math.PI/5;const x=170+104*Math.cos(a),y=140+104*Math.sin(a),u=170+104*Math.cos(b),v=140+104*Math.sin(b),len=Math.hypot(u-x,v-y);return <g key={i}><line x1={(x+26*(u-x)/len).toFixed(3)} y1={(y+26*(v-y)/len).toFixed(3)} x2={(u-29*(u-x)/len).toFixed(3)} y2={(v-29*(v-y)/len).toFixed(3)} stroke="#64748b" strokeWidth="1.5" markerEnd="url(#finite-clock-arrow)" /><circle cx={x.toFixed(3)} cy={y.toFixed(3)} r="23" fill="#eef3fa" stroke="#263e88" /><text x={x.toFixed(3)} y={(y+8).toFixed(3)} textAnchor="middle" fontSize="25" fill="#172554">{i*multiplier%5}</text></g>})}
    </svg><div><p className="text-2xl font-serif">C₅ → G C₅ G⁻¹ = C₅²</p><p className="mt-4">The original cycle steps by 1. After relabeling, the same arrows step by {multiplier} modulo 5.</p><p className="mt-4" aria-live="polite">{power === 0 ? "Original labeling" : `After ${power} ${power === 1 ? "application" : "applications"}`} · multiplier {multiplier}</p><div className="clock-powers" aria-label="Four actions restore the original labels">{[1,2,4,3,1].map((value,i)=><span key={i} className={i===power?"is-current":undefined}>{value}{i<4&&<span aria-hidden> → </span>}</span>)}</div></div></div>
    <button type="button" className="readout-button" onClick={() => setPower((power + 1) % 4)}>Apply G · step {power + 1} of 4</button>
    <p className="mt-4">Labels are multiplied by 2 modulo 5. Four applications return to the original labels. This illustrates G C₅ G⁻¹ = C₅² and G⁴ = I on the five cycle.</p>
    <p className="mt-3 text-sm text-slate-600">The Galois action is distinct from the C₃₀ rotation and from the named G₃₁ compiler operator. This finite action does not set a duration in seconds.</p>
  </div>;
}
