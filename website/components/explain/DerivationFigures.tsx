import Link from "next/link";
import { groupDecimal, readingNumber } from "@/lib/format-number";

export function BudgetBridge() {
  return <section className="budget-bridge" id="budget" aria-label="How the charge trace connects to the electromagnetic budget">
    <h2>The same charges enter the electromagnetic budget.</h2>
    <p>Sum the squared integer hypercharges X = 6Y over all sixteen components. The result is 120. The compiler connects this trace to its flavour budget and the stated single Higgs contribution.</p>
    <ol className="budget-chain">
      <li><span className="budget-value">120</span><span>Tr X² on one family</span><small>Exact charge trace</small></li>
      <li><span className="budget-operation">Compiler relation</span><span className="budget-value">40</span><span>ΣL = (Tr X²)/3</span><small>The flavour budget, with its transport rules</small></li>
      <li><span className="budget-operation">+ 1</span><span className="budget-value">41</span><span>M = 10b₁</span><small>With one Higgs contribution</small></li>
    </ol>
    <p className="figure-note">The factor 1/3 is the stated compiler relation. It is not an average over three families. The individual flavour operators and the Higgs content remain part of the construction.</p>
    <div className="budget-next"><p><strong>Where does 41 go next?</strong> Into the specified electromagnetic boundary equation. Solving that fixed equation gives α⁻¹ = 137.035 999 2168… . Its identification with nature’s electromagnetic response is a further physical question.</p><Link className="guide-link" href="/explain#alpha">Follow the equation and data comparison</Link></div>
    <Link className="guide-link figure-source" href="/results?search=CARRIER.CUTCODE.01">Charge trace and compiler identity: original statement and evidence</Link>
  </section>;
}

export function AlphaComparison() {
  const prediction = 137.0359992168407;
  const measured = 137.035999177;
  const sigma = 0.000000021;
  const z = (prediction - measured) / sigma;
  const x = 60 + (z + 3) / 6 * 480;
  return <figure className="comparison-figure">
    <h3>How close is the calculated value to the measurement?</h3>
    <div className="comparison-values"><div><span>Calculated closure root</span><strong>{groupDecimal("137.0359992168")}…</strong></div><div><span>CODATA 2022 recommended value</span><strong>{groupDecimal("137.035999177")} (21)</strong></div></div>
    <svg viewBox="0 0 600 150" role="img" aria-label="Comparison in units of experimental standard uncertainty. CODATA is centered at zero with a shaded plus or minus one sigma interval. The calculated root lies about 1.90 sigma higher.">
      <rect x="220" y="34" width="160" height="42" fill="#dbece7" />
      <line x1="60" y1="76" x2="540" y2="76" stroke="#718096" />
      {[-3, -2, -1, 0, 1, 2, 3].map(tick => <g key={tick}><line x1={300 + tick * 80} y1="76" x2={300 + tick * 80} y2="83" stroke="#718096" /><text x={300 + tick * 80} y="110" textAnchor="middle" fontSize="22" fill="#334155">{tick > 0 ? "+" : ""}{tick}</text></g>)}
      <line x1="300" y1="26" x2="300" y2="76" stroke="#176b58" strokeWidth="2" />
      <line x1={x.toFixed(3)} y1="26" x2={x.toFixed(3)} y2="76" stroke="#263e88" strokeWidth="2" />
      <circle cx={x.toFixed(3)} cy="48" r="7" fill="#263e88" />
      <text x="300" y="145" textAnchor="middle" fontSize="21" fill="#334155">Difference in experimental standard uncertainties (σ)</text>
    </svg>
    <figcaption><span className="comparison-legend"><span><i className="measurement-key" /> CODATA ±1σ</span><span><i className="calculation-key" /> Calculated root</span></span><strong>{z.toFixed(2)}σ above the CODATA recommended value.</strong> This dated comparison uses the experimental uncertainty. The measured value was known before the formula freeze.</figcaption>
    <a className="guide-link figure-source" href="https://physics.nist.gov/cuu/pdf/RevModPhys.97.025002.pdf" target="_blank" rel="noopener noreferrer">NIST: CODATA 2022 recommended values, published 2025</a>
  </figure>;
}

export function LeptonLadder() {
  const seed = 1 / (6 * Math.PI) + 3 / (256 * Math.PI ** 4);
  const rows = [
    { label: "Electron", symbol: "e", coefficient: "16/7", power: 5, ratio: ((16 / 7) / (7 / 6)) * seed ** 3 },
    { label: "Muon", symbol: "μ", coefficient: "4/3", power: 3, ratio: (8 / 7) * seed },
    { label: "Tau", symbol: "τ", coefficient: "7/6", power: 2, ratio: 1 },
  ];
  return <figure className="lepton-figure">
    <h3>One small seed, three levels of the mass ladder.</h3>
    <p>The charged lepton branch has source amplitudes proportional to c × φ₀ᵏ. The common scale cancels when the tau source mass is set to one.</p>
    <svg viewBox="0 0 600 200" role="img" aria-label="Relative source masses on a logarithmic scale: electron about 0.0002945, muon about 0.06077, tau one. These are compiler source ratios, not pole mass measurements.">
      {[0.0001, 0.001, 0.01, 0.1, 1].map(value => { const x = 60 + (Math.log10(value) + 4) * 120; return <g key={value}><line x1={x} y1="25" x2={x} y2="127" stroke="#d5dce3" /><text x={x} y="151" textAnchor="middle" fontSize="22" fill="#334155">{value}</text></g>; })}
      {rows.map((row, i) => { const x = 60 + (Math.log10(row.ratio) + 4) * 120; return <g key={row.symbol}><line x1="60" y1={40 + i * 35} x2={x.toFixed(3)} y2={40 + i * 35} stroke="#263e88" strokeWidth="2" /><circle cx={x.toFixed(3)} cy={40 + i * 35} r="6" fill="#263e88" /><text x={(x - 13).toFixed(3)} y={46 + i * 35} textAnchor="end" fontSize="24" fill="#172554">{row.symbol}</text></g>; })}
      <text x="300" y="190" textAnchor="middle" fontSize="22" fill="#334155">Relative source mass · logarithmic scale · τ = 1</text>
    </svg>
    <table className="figure-table"><caption>Fixed lepton source branch</caption><thead><tr><th>Lepton</th><th>Source amplitude</th><th>Ratio to τ</th></tr></thead><tbody>{rows.map(row => <tr key={row.symbol}><th>{row.label}</th><td>({row.coefficient}) φ₀<sup>{row.power}</sup></td><td>{row.ratio === 1 ? "1" : readingNumber(row.ratio,5)}</td></tr>)}</tbody></table>
    <figcaption>The rational coefficients follow the stated resolvent and product rule, with the assigned lepton legs. Absolute calibration and transfer to observed mass schemes remain separate. The dimensionless source relations are already worked out.</figcaption>
    <Link className="guide-link figure-source" href="/results?search=lepton">Lepton amplitudes, source ratios and their conditions</Link>
  </figure>;
}
