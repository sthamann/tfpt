"use client";

import { useState } from "react";
import Link from "next/link";
import { Math } from "@/components/Math";
import styles from "./FlavorDerivation.module.css";

const source = {
  master: "/documentation?section=section%3A70e249c656b3bbd339e9",
  seed: "/documentation?section=section%3A2705ce15584daef708e2",
  residue: "/documentation?section=section%3A7e0600a35f2488ae7d56",
  geometry: "/documentation?section=section%3A26a7469d80cd6b47c2b6",
  leptons: "/documentation?section=section%3Ad9254a3f746aa54dd7bd",
  quarks: "/documentation?section=section%3A115c4091b215e2a670ca",
};

const R = [[1, 3, 0], [1, 5, 2], [2, 5, 3]];
const Q = [[3, 1, 0], [3, 2, 0], [3, 2, 1]];
const K = R.map((row,i)=>row.map((v,j)=>v+Q[i][j]*(j===0?1:-1)));
const L = K.map((row,i)=>row.map((v,j)=>v+Q[i][j]));
const generations = ["First generation", "Second generation", "Third generation"];
const sectorNames = ["Up quarks", "Down quarks", "Charged leptons"];

function Matrix({ name, values, selected, meaning }: {
  name: string; values: number[][]; selected: number; meaning: string;
}) {
  return <figure className={styles.matrixFigure}>
    <figcaption><strong>{name}</strong><span>{meaning}</span></figcaption>
    <table className={styles.matrix} aria-label={`${name}: ${meaning}. Rows are up quarks, down quarks and charged leptons; columns are generations one to three.`}>
      <thead><tr><th scope="col"><span className={styles.srOnly}>Sector</span></th>{[1, 2, 3].map((n) => <th key={n} scope="col" className={selected === n - 1 ? styles.selectedHeading : undefined}>{n}</th>)}</tr></thead>
      <tbody>{values.map((row, i) => <tr key={i}><th scope="row"><span aria-hidden="true">{["u", "d", "e"][i]}</span><span className={styles.srOnly}>{sectorNames[i]}</span></th>{row.map((n, j) => <td key={j} className={selected === j ? styles.selectedCell : undefined}>{n}</td>)}</tr>)}</tbody>
    </table>
  </figure>;
}

function Vector({ values, label }: { values: number[]; label: string }) {
  return <div className={styles.vectorStep}><span>{label}</span><div className={styles.vector} role="math" aria-label={`${label}: ${values.join(", ")}`}>{values.map((n, i) => <span key={i}>{n}</span>)}</div></div>;
}

function Hexagon() {
  const points = Array.from({ length: 6 }, (_, r) => ({
    x: Number((145 + 83 * globalThis.Math.cos(r * globalThis.Math.PI / 3)).toFixed(6)),
    y: Number((112 - 83 * globalThis.Math.sin(r * globalThis.Math.PI / 3)).toFixed(6)),
  }));
  return <figure className={styles.hexagon}>
    <svg viewBox="0 0 310 245" role="img" aria-labelledby="flavor-hexagon-title">
      <title id="flavor-hexagon-title">Six transport residues on a circle. Electron length eight reaches residue two after one full winding; muon length five reaches residue five with no full winding.</title>
      <polygon points={points.map((p) => `${p.x},${p.y}`).join(" ")} fill="none" stroke="currentColor" strokeWidth="1.5" />
      <path d={`M145 112 L${points[2].x} ${points[2].y} M145 112 L${points[5].x} ${points[5].y}`} fill="none" stroke="currentColor" strokeWidth="1" strokeDasharray="4 5" />
      {points.map((p, r) => <g key={r}>
        <circle cx={p.x} cy={p.y} r={r === 2 || r === 5 ? 14 : 5} fill={r === 2 || r === 5 ? "#164c76" : "#f7f4ed"} stroke="currentColor" strokeWidth="1.5" />
        <text x={p.x} y={p.y + (r === 2 || r === 5 ? 5 : -12)} textAnchor="middle" fill={r === 2 || r === 5 ? "#fff" : "currentColor"} fontSize="15">{r}</text>
      </g>)}
      <text x="145" y="117" textAnchor="middle" fill="currentColor" fontSize="18">C₆</text>
      <text x="8" y="17" fill="currentColor" fontSize="16">e: 8 = 6 + 2</text>
      <text x="182" y="235" fill="currentColor" fontSize="16">μ: 5 = 0 + 5</text>
    </svg>
    <figcaption>A full turn supplies the winding. The remaining position supplies the resolvent angle.</figcaption>
  </figure>;
}

function Minor({ columns, values, result }: { columns: string; values: number[]; result: number }) {
  return <figure className={styles.minor}>
    <figcaption>Columns {columns}</figcaption>
    <svg viewBox="0 0 180 120" role="img" aria-label={`Two by two determinant: ${values[0]} times ${values[3]}, minus ${values[1]} times ${values[2]}, equals ${result}.`}>
      <path d="M28 12 V108 M152 12 V108" stroke="currentColor" strokeWidth="1.5" />
      <path d="M63 36 L117 84 M117 36 L63 84" stroke="#9bb3c5" strokeWidth="1.5" />
      {values.map((n, i) => <text key={i} x={i % 2 ? 124 : 56} y={i < 2 ? 33 : 100} textAnchor="middle" fill="currentColor" fontSize="23">{n}</text>)}
    </svg>
    <Math block plain={`${values[0]} × ${values[3]} − ${values[1]} × ${values[2]} = ${result}.`}>{String.raw`${values[0]}\cdot${values[3]}-${values[1]}\cdot${values[2]}=${result}`}</Math>
  </figure>;
}

export function FlavorDerivation() {
  const [generation, setGeneration] = useState(0);
  const basis = [0, 0, 0].map((_, i) => i === generation ? 1 : 0);
  const projected = basis.map((v,i)=>v*(1+(i===0?1:-1)));
  const increment = Q.map(row=>row.reduce((sum,v,i)=>sum+v*projected[i],0));

  return <section id="flavor" className={`guide-section ${styles.flavor}`} aria-labelledby="flavor-heading">
    <h2 id="flavor-heading">How one seed becomes a hierarchy of masses</h2>
    <p className="guide-lead">An electron is much lighter than a muon, and a muon much lighter than a tau. TFPT describes this hierarchy through transport lengths and a finite response. Follow the actual operators, then calculate two lepton ratios and the up to down quark ratio.</p>
    <p>There are two different jobs to do. Integer operators determine the powers of a small common seed. A response calculation determines the coefficient multiplying each power. The dimensionful scale is shared. The same master formula covers all nine charged fermions: the six quarks and the electron, muon and tau. The calculation below follows this documented charged flavour branch in its marked family frame.</p>
    <p className={styles.sources}><a href="#standard-model">Place masses in the Standard Model derivation</a><Link href="/interactive/flavor">Watch the hierarchy form step by step</Link><a href="#predictions">Compare the registered source ratios</a></p>

    <ol className={styles.sequence}>
      <li>
        <h3>Begin with the family anchor and the small seed</h3>
        <p>The four marked boundary points leave three independent cycles: a loop around each point, with one relation between the four loops. In the specified family dictionary, these cycles supply a rank three space. The positive integer anchor a = (1, 1, 2) distributes a total of four across its three marked directions. Up to permutation, it is the only positive integer triple with that total.</p>
        <p>The boundary normalization c₃ and the shared admissible count give the seed. Its baseline factor 4/3 is the halved integrated (E₈)₁ Weyl anomaly in the stated one sided seam construction. Three families of sixteen give the correction count 48.</p>
        <Math block plain="The seed is four thirds of c three plus forty eight times c three to the fourth, with c three equal to one over eight pi. The result is approximately 0.053172.">{String.raw`\begin{aligned}c_3&=\frac1{8\pi},\\\varphi_0&=\frac43c_3+48c_3^4\\&=\frac1{6\pi}+\frac3{256\pi^4}\approx0.053\,172.\end{aligned}`}</Math>
        <p>A further factor of φ₀ suppresses a mass by about nineteen. Which particle receives which power is the next part of the calculation.</p>
        <p className={styles.sources}><Link href={source.master}>Read the seed baseline and master formula</Link><Link href={source.seed}>Follow the shared seed into other observables</Link></p>
      </li>

      <li>
        <h3>Construct the residue, grading and sheet response</h3>
        <p>R records the transport residues for the up quark, down quark and charged lepton sectors. Q is the parabolic family operator. The sheet involution Σ keeps the first marked direction and reverses the other two. These are maps in the specified compiler frame; they are not the physical CKM mixing matrix.</p>
        <div className={styles.matrixRow}>
          <Matrix name="R" values={R} selected={generation} meaning="Transport residues" />
          <Matrix name="Q" values={Q} selected={generation} meaning="Family response" />
          <figure className={styles.sheet}><figcaption><strong>Σ</strong><span>Sheet signs by generation</span></figcaption><div className={styles.signs}>{["+1", "−1", "−1"].map((n, i) => <span key={i} className={generation === i ? styles.selectedCell : undefined}>{n}</span>)}</div><Math plain="Sigma is diagonal, with entries plus one, minus one and minus one.">{String.raw`\Sigma=\operatorname{diag}(1,-1,-1)`}</Math></figure>
        </div>
        <p>Why these operators? The four punctures form a square with D₄ symmetry. Their action on the three independent cycles splits the family space into a line and a plane. The established cusp weights 0, 1/3 and 2/3 become the three grading values 1, 2 and 3 through the rule 3w + 1. The sheet coupling has square 3 on its support. The order three cusp class also supplies the integer lift with det Q = 3.</p>
        <p>In the marked integer frame, the documented budgets, spectra and hierarchy conditions select the displayed normal form. Exhaustive integer enumeration checks uniqueness under those conditions. The result uses this family geometry and its typing, beyond the count of five carrier slots.</p>
        <details className={styles.details}><summary>See the even and odd parts of Q</summary>
          <Math block plain="Conjugating Q by the sheet signs separates an even part with eigenvalues one, two and three, and an odd part whose square is three on its support.">{String.raw`\begin{aligned}Q_+&=\frac{Q+\Sigma Q\Sigma}{2},\\\operatorname{Spec}Q_+&=\{1,2,3\},\\Q_-&=\frac{Q-\Sigma Q\Sigma}{2},\\\chi_{Q_-}(t)&=t(t^2-3).\end{aligned}`}</Math>
          <p>The cusp weights, marked homology frame and discrete normal form are part of this statement. The Q geometry and integer lift are established layers of the documented construction.</p>
        </details>
        <p className={styles.sources}><Link href={source.geometry}>Read the D₄ construction and integer lift</Link><Link href="/verification/v11_unique_KQ.py">Inspect the integer uniqueness calculation</Link></p>
      </li>

      <li>
        <h3>Watch why only the first generation winds</h3>
        <p>The mass powers and transport lengths are two readings of R and Q. Apply the sheet sign before adding Q to obtain K. Add Q once more to obtain L.</p>
        <Math block plain="K equals R plus Q Sigma. L equals K plus Q, which is R plus Q times the identity plus Sigma.">{String.raw`\begin{aligned}K&=R+Q\Sigma,\\L&=K+Q=R+Q(I+\Sigma).\end{aligned}`}</Math>
        <fieldset className={styles.controls}><legend>Send one generation through the projection</legend><div>{generations.map((label, i) => <button key={label} type="button" aria-pressed={generation === i} onClick={() => setGeneration(i)}>{label}</button>)}</div></fieldset>
        <div className={styles.projection}>
          <Vector values={basis} label="Input direction" /><span className={styles.operation}>apply I + Σ</span><Vector values={projected} label="After the sheet projection" /><span className={styles.operation}>apply Q</span><Vector values={increment} label="Added to the residue" />
        </div>
        <p className={styles.live} aria-live="polite" aria-atomic="true">{generation === 0 ? "The first direction survives with weight two. Q sends it to (6, 6, 6), so each sector gains one full six step winding in its first generation." : `The ${generation === 1 ? "second" : "third"} direction cancels: one plus minus one is zero. Q therefore adds no winding to this generation.`}</p>
        <Math block plain="Identity plus Sigma selects twice the first direction. Consequently Q times identity plus Sigma adds six to every entry of the first column and zero elsewhere.">{String.raw`\begin{aligned}I+\Sigma&=2e_1e_1^T,\\Q(I+\Sigma)&=6\,\mathbf1e_1^T,\\L&=R+6\,\mathbf1e_1^T.\end{aligned}`}</Math>
        <div className={styles.matrixRow}><Matrix name="K" values={K} selected={generation} meaning="Powers of φ₀" /><span className={styles.matrixJoin}>L = K + Q</span><Matrix name="L" values={L} selected={generation} meaning="Transport lengths" /></div>
        <p>The column numbers above mean generations. In L, the first column is (7, 7, 8), obtained from (1, 1, 2) by adding six. In K, the lepton row is (5, 3, 2). Those are the three seed powers used below. Matrix entries give these powers; the eigenvalues describe other properties of the operators.</p>
        <p>All nine entries also give a shared transport budget. R contributes 22. L adds six in each of its three first column entries, contributing another eighteen. Equivalently, sum the three sector rows directly:</p>
        <Math block plain="The up row sums to ten, the down row to fourteen, and the lepton row to sixteen. Their total is forty, also equal to the residue total twenty two plus three times six.">{String.raw`\begin{aligned}\sum_{f,j}L_{f,j}&=(7+3+0)\\&\quad +(7+5+2)\\&\quad +(8+5+3)\\&=10+14+16=40\\&=22+3\cdot6.\end{aligned}`}</Math>
        <p>This is a sum of actual transport entries. The electromagnetic budget reuses it alongside an independent calculation from the family charges.</p>
        <p className={styles.sources}><Link href={source.residue}>Read the residue matrix and winding theorem</Link><Link href={source.geometry}>Read K and L as two sheet readings</Link><Link href="/explain#budget">Follow 40 into the electromagnetic budget</Link></p>
      </li>

      <li>
        <h3>Turn lengths into source masses</h3>
        <p>A transport step carries the common factor λY. Its length L supplies the power, and a holonomy response Λ supplies the amplitude. In the closed branch the evaluated response reorganizes the result into a coefficient c and a power K of φ₀.</p>
        <Math block plain="A source mass is the shared scale v geo over square root two, times lambda Y to its transport length, times its response amplitude. In the closed branch this equals the shared scale times pi, times c, times the seed to its K entry.">{String.raw`\begin{aligned}\lambda_Y&=\sqrt{\varphi_0(1-\varphi_0)}\approx0.224\,376,\\\widehat m_{f,j}&=\frac{v_{\rm geo}}{\sqrt2}\lambda_Y^{L_{f,j}}\Lambda_{f,j}\\&=\frac{v_{\rm geo}\pi}{\sqrt2}\,c_{f,j}\varphi_0^{K_{f,j}}.\end{aligned}`}</Math>
        <div className={styles.ladder} aria-label="Lepton transport lengths and seed powers"><div><strong>Electron</strong><span>length 8</span><span>seed power 5</span></div><div><strong>Muon</strong><span>length 5</span><span>seed power 3</span></div><div><strong>Tau</strong><span>length 3</span><span>seed power 2</span></div></div>
        <p>The conversion includes the amplitude calculation. Replacing L by K while keeping the same coefficient would change the formula. The overall scale v<sub>geo</sub> gives masses their units and cancels in the ratios considered here.</p>
        <p className={styles.sources}><Link href={source.master}>Read the transport master formula</Link><Link href={source.quarks}>Read the closed seed ladder</Link></p>
      </li>

      <li>
        <h3>Calculate the three lepton coefficients</h3>
        <p>The finite response distinguishes positions on the six step transport circle. Its distinguished parameter is δ = 1/2: the difference between the D₅ and A₃ gluing norms, 5/4 and 3/4. Evaluating the lepton leg at its specified charge gives the squared resolvent below.</p>
        <Math block plain="Delta is five quarters minus three quarters, or one half. At residue r, the squared response is one divided by five quarters minus cosine of r pi over three.">{String.raw`\begin{aligned}\delta&=\frac54-\frac34=\frac12,\qquad\zeta=e^{i\pi/3},\\A_r&=\left|\frac1{1-\frac12\zeta^r}\right|^2\\&=\frac1{\frac54-\cos(r\pi/3)}.\end{aligned}`}</Math>
        <div className={styles.resolvent}><Hexagon /><div><p>Divide a length by six. The remainder r gives the angle on the circle. Each full winding w contributes the specified gluing factor 4. For the non-anchor leptons, c = 4<sup>w</sup>A<sub>r</sub>.</p><p><strong>Electron:</strong> 8 = 6 × 1 + 2. At residue 2 the cosine is −1/2, so the denominator is 7/4. One winding multiplies its inverse by four.</p><Math block plain="The electron coefficient is four times four sevenths, giving sixteen sevenths.">{String.raw`c_e=4^1\frac1{\frac54+\frac12}=4\cdot\frac47=\frac{16}{7}`}</Math></div></div>
        <p><strong>Muon:</strong> 5 = 6 × 0 + 5. At residue 5 the cosine is +1/2, so the denominator is 3/4. There is no winding factor.</p>
        <Math block plain="The muon coefficient is one divided by three quarters, giving four thirds.">{String.raw`c_\mu=4^0\frac1{\frac54-\frac12}=\frac43`}</Math>
        <p><strong>Tau:</strong> the heaviest lepton is the anchor. The sector product rule fixes its coefficient from the other two. The full exterior, or Dirac spinor, space has dimension 2⁵ = 32, and the family square is 3² = 9.</p>
        <Math block plain="The product of the three lepton coefficients is thirty two ninths. Dividing by the electron and muon coefficients gives the tau coefficient seven sixths.">{String.raw`\begin{aligned}c_ec_\mu c_\tau&=\frac{2^5}{3^2}=\frac{32}{9},\\c_\tau&=\frac{32/9}{(16/7)(4/3)}=\frac76.\end{aligned}`}</Math>
        <p>The product rule and the lepton leg assignments belong to the established response dictionary. The later family monodromy makes the same denominators explicit: det(I − tM₀) = 1 − t³ gives 7/8 and 9/8 at t = ±1/2. These coefficients are calculated within that dictionary, with no individual lepton coefficient fit.</p>
        <p className={styles.sources}><Link href={source.leptons}>Read the resolvent, product rule and monodromy calculation</Link><Link href="/verification/v20_lepton_c_derivation.py">Inspect the rational coefficient calculation</Link></p>
      </li>

      <li>
        <h3>Cancel the shared scale and read two lepton ratios</h3>
        <p>Put the powers (5, 3, 2) together with the coefficients just calculated. Write A for the shared dimensional factor v<sub>geo</sub>π/√2.</p>
        <Math block plain="Electron, muon and tau source masses are A times sixteen sevenths seed to the fifth, four thirds seed cubed, and seven sixths seed squared.">{String.raw`\begin{aligned}\widehat m_e&=A\frac{16}{7}\varphi_0^5,\\\widehat m_\mu&=A\frac43\varphi_0^3,\\\widehat m_\tau&=A\frac76\varphi_0^2.\end{aligned}`}</Math>
        <p>In the electron to muon ratio, A cancels and five minus three leaves two seed powers. In the muon to tau ratio, three minus two leaves one.</p>
        <Math block plain="The electron to muon source mass ratio is twelve sevenths seed squared, approximately 0.00484673. The muon to tau ratio is eight sevenths seed, approximately 0.0607679.">{String.raw`\begin{aligned}\frac{\widehat m_e}{\widehat m_\mu}&=\frac{16/7}{4/3}\varphi_0^{5-3}\\&=\frac{12}{7}\varphi_0^2\approx0.004\,846\,73,\\\frac{\widehat m_\mu}{\widehat m_\tau}&=\frac{4/3}{7/6}\varphi_0^{3-2}\\&=\frac87\varphi_0\approx0.060\,767\,9.\end{aligned}`}</Math>
        <p>The hierarchy now has both parts explained: the integer powers come from K, while the rational coefficients come from the finite lepton response.</p>
      </li>

      <li>
        <h3>Use an oriented area to distinguish up and down</h3>
        <p>Up and down have the same transport length 7 and the same seed power 4. Their common radial hexagon data would give a ratio of one for any purely scalar leg. The quark reader therefore uses the oriented anchor plane, an exterior square response that can distinguish orientation.</p>
        <p>Take the two marked vectors 1 = (1, 1, 1) and a = (1, 1, 2), and let K act on them from the left. The resulting rows are:</p>
        <Math block plain="The all ones row times K is thirteen, eight, four. The anchor row times K is eighteen, eleven, six.">{String.raw`\begin{aligned}\mathbf1^TK&=(13,8,4),\\a^TK&=(18,11,6).\end{aligned}`}</Math>
        <p>Each pair of columns gives an oriented area, calculated as a two by two determinant. These are the three Plücker coordinates of the anchor plane.</p>
        <div className={styles.minors}><Minor columns="1 and 2" values={[13, 8, 18, 11]} result={-1} /><Minor columns="1 and 3" values={[13, 4, 18, 6]} result={6} /><Minor columns="2 and 3" values={[8, 4, 11, 6]} result={4} /></div>
        <p>The magnitude sum in this marked normal frame is |−1| + |6| + |4| = 11. The response denominator ΔQ = 13 also appears as the discriminant 5² − 4 × 3 of Q’s nontrivial quadratic factor. Five carrier slots and three family directions then give:</p>
        <Math block plain="The up to down source mass ratio is five times the sum of the absolute anchor minors, divided by three squared times thirteen. This equals fifty five over one hundred seventeen, approximately 0.470085.">{String.raw`\begin{aligned}\frac{\widehat m_u}{\widehat m_d}&=\frac{c_u}{c_d}\varphi_0^{4-4}\\&=\frac{5\,(1+6+4)}{3^2\cdot13}\\&=\frac{55}{117}\approx0.470\,085.\end{aligned}`}</Math>
        <p>This is the documented exterior readout on the derived discrete selector stratum: det R = 8, Smith normal form (1, 1, 8), grading spectrum (1, 2, 3), and the marked homology normal form with distinct distances (0, 1, 3). These conditions fix the operators used here. The ratio is constant on that stratum and does not require selecting the continuous wall point needed for absolute holonomy amplitudes. The magnitude sum above uses the specified frame; it is not a norm invariant under every possible change of basis.</p>
        <details className={styles.details}><summary>Follow the other two closed quark readouts</summary><p>The anchor power sum 1⁵ + 1⁵ + 2⁵ = 34 and admissible count minus one, 48 − 1 = 47, give the c/s coefficient ratio. The right anchor block of K has minors (12, 12, −2), whose magnitude sum 26 gives the t/b coefficient ratio. The c/s block retains the source’s stated choice of invariant.</p><Math block plain="The charm to strange source ratio is thirty four over forty seven times the inverse seed, approximately 13.605. The top to bottom ratio is three over twenty six times inverse seed squared, approximately 40.8115.">{String.raw`\begin{aligned}\frac{\widehat m_c}{\widehat m_s}&=\frac{34}{47}\varphi_0^{-1}\approx13.605,\\\frac{\widehat m_t}{\widehat m_b}&=\frac3{26}\varphi_0^{-2}\approx40.811\,5.\end{aligned}`}</Math></details>
        <p className={styles.sources}><Link href={source.quarks}>Read the exterior leg and ratio rigidity</Link><Link href="/verification/v37_plucker_anchor.py">Inspect the anchor minors</Link><Link href="/verification/v49_readout_rigidity.py">Inspect the normal form and readout conditions</Link></p>
      </li>

      <li>
        <h3>Carry a source mass into a physical comparison</h3>
        <p>The full matrix also fixes a determinant scaling. The three K row sums are 6, 9 and 10, so the up, down and charged lepton determinants scale with seed powers 6, 9 and 10. Together they give 25. The Q row sums add another 15, recovering the transport budget 40. This fixes the exponent relation; it does not select the remaining absolute quark amplitude anchor.</p>
        <Math block>{String.raw`\begin{aligned}\det M_u&\propto\varphi_0^6,\quad\det M_d\propto\varphi_0^9,\\\det M_e&\propto\varphi_0^{10},\\6+9+10&=25,\quad25+15=40.\end{aligned}`}</Math>
        <p className={styles.sources}><Link href={source.geometry}>Read the determinant and transport identities</Link></p>
        <p>The hats matter. These are source masses in the declared branch. A measured electron pole mass or a quark mass quoted in a renormalization scheme is a particular physical reader of the common renormalized action. The common source construction already supplies the route through its action, field moments, conditional OS/CAR reconstruction and Γ<sub>ren</sub>.</p>
        <div className={styles.handoff} aria-label="Physical comparison route"><span>Source ratio</span><span>Same Γ<sub>ren</sub></span><span>Scale and mass scheme</span><span>Dated measurement</span></div>
        <p>For a numerical comparison, apply the corresponding reader and specify the scale and scheme, especially for quarks. Cancelling v<sub>geo</sub> removes the overall units; it does not remove running or scheme dependence. The dimensionless source relations calculated above remain closed in their stated branch. The absolute amplitude anchor is a separate part of that construction.</p>
        <p className={styles.sources}><Link href={source.quarks}>Read the original source mass scope</Link><Link href="/empirical-audit">Open the dated empirical comparisons</Link><Link href="/results?search=flavor-ratio-closed-absolute-anchor-open">Read the reviewed ratio and amplitude distinction</Link></p>
      </li>
    </ol>
  </section>;
}
