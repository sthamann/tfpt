import Link from "next/link";
import { Math } from "@/components/Math";
import { AlphaExplorer } from "./InteractiveReadouts";
import { AlphaComparison } from "./DerivationFigures";
import styles from "./AlphaDerivation.module.css";

const source = {
  closure: "/documentation?section=section%3A6a757c5701557192653a",
  carrier: "/research/sources/3d71560751889525f0373327.txt",
  transfer: "/research/sources/bccd1d35797f4d0dc5470ebb.txt",
  index: "/research/sources/b2fd6645a9ae63a7e0e8223f.txt",
  circle: "/research/sources/b016474460b2741b2d4ef790.txt",
  grade: "/research/sources/a60e8c86577a5d18e0f6da64.txt",
  proof: "/research/sources/3ccf6cd6ceaf16ffb0706cad.txt",
  measure: "/research/sources/0a7513fbdfbf46c4cb1db1bc.txt",
};

const ingredients = [
  { symbol: String.raw`c_3=\frac1{8\pi}`, meaning: "The P1 boundary normalization. The paper writes 8π as two sheets times the Gauss–Bonnet integral 4π.", scope: "Accepted oriented boundary principle and normalization. Its physical realization remains a separate question.", href: source.closure, label: "Architecture, EM closure" },
  { symbol: String.raw`\varphi_{\rm base}=\frac1{6\pi}=\frac{c_3}{3/4}`, meaning: "The unperturbed seam opening. The denominator 3/4 is the A₃ discriminant norm, paired with the D₅ norm 5/4.", scope: "Exact relation in the named normalization. Why the physical EM response has this additive baseline is part of the source map.", href: source.closure, label: "Architecture, determinant line" },
  { symbol: String.raw`48=3\times16,\quad\delta_{\rm top}=48c_3^4=\frac3{256\pi^4}`, meaning: "Three families of the 16 dimensional even carrier give the admissible count. The four seam factors give the specified topological weight.", scope: "The count and algebra are exact in this carrier branch. Using this weight in the EM response belongs to its stated coupling contract.", href: source.closure, label: "Architecture, contact unit and response" },
  { symbol: String.raw`e^{-2\alpha},\quad 2=d\,\mathrm{SF}=2\times1`, meaning: "Adding αJ to a Euclidean defect action multiplies its relative weight by exp(−αJ). The primitive spectral flow is one on each of two identical sheets.", scope: "Exact reweighting under the stated additive action and index normalization. It specifies a topological coupling, not automatically an energy or heat parameter.", href: source.index, label: "v2.7, defect sector reweighting" },
  { symbol: String.raw`\frac54=B\gamma=\frac32\!\left(\frac39+\frac24\right)=q(D_5)`, meaning: "B is the 3:2 carrier rank ratio; γ is the squared hypercharge trace on the five slots. The same value is the D₅ discriminant norm.", scope: "Exact carrier identity. The marked D₅ grade calculation additionally realizes this power as an actual response in the specified E₈ source.", href: source.carrier, label: "v4.2, charge trace identities" },
  { symbol: String.raw`q(1-q)^{-5/4}`, meaning: "The rank one relative determinant is 1−q. Its chosen inverse susceptibility has power 5/4; the seam opening adds the resulting response with one outer q.", scope: "The determinant identity is proved. The inverse response, the outer q and the physical parameter map must be realized in the same EM channel.", href: source.transfer, label: "v4.2, minimal seam transfer" },
  { symbol: String.raw`M=40+1=41,\quad b_1=\frac{41}{10}`, meaning: "The specified flavour transport lengths sum to 40; one Higgs contribution gives 41. The hypercharge content independently expresses this as the normalized abelian index 10b₁.", scope: "Exact budget and charge trace in the selected three family, one Higgs branch. Root uniqueness itself does not select this budget.", href: source.closure, label: "Architecture, flavour budget and U(1) index" },
  { symbol: String.raw`8b_1=\frac45\,41`, meaning: "Eight times the abelian index equals (4/5) times the budget. The 4/5 is this exact normalization identity; it is not another fitted parameter.", scope: "Coefficient identity. The use of rank(E₈) × b₁ in the local EM functional still has its stated physical interpretation.", href: source.closure, label: "Architecture, Ward reading" },
  { symbol: String.raw`\alpha^3-2c_3^3\alpha^2`, meaning: "The local part of the defined closure. Two names the sheet factor; c₃³ means three seam insertions. Its normalized primitive is α⁴/4 − (2/3)c₃³α³.", scope: "Integrating the supplied derivative is exact. That operation does not derive the derivative from an original coupled EM operator. The cubic moment and exact local normalization need that identification.", href: source.transfer, label: "v4.2, normalized closure potential" },
  { symbol: String.raw`c_3^6\log\!\frac1{\varphi_s}`, meaning: "The transport term uses six seam insertions, associated in the compiler with the C₆ hexagon and six positive A₃ roots. Logarithms enter the determinant and effective action description.", scope: "Specified transport and determinant grammar. A real renormalized local determinant must produce this full logarithmic response, including its measure and variation.", href: source.closure, label: "Architecture, Ward and contact grammar" },
];

export function AlphaDerivation() {
  return <section className={`guide-section ${styles.alpha}`} id="alpha" aria-labelledby="alpha-heading">
    <h2 id="alpha-heading">Where does the number near 137 come from?</h2>
    <p className="guide-lead">Alpha measures electromagnetic coupling strength. Follow how TFPT combines its boundary normalization, carrier charges and a specified defect response into one equation. That equation has a proved unique positive solution, with inverse coupling α⁻¹ ≈ 137.035 999 2168… .</p>
    <p>Alpha is a dimensionless measure of electromagnetic interaction strength. In familiar SI units it combines the elementary charge, the quantum of action and the speed of light:</p>
    <Math block plain="Alpha equals elementary charge squared divided by four pi, vacuum permittivity, reduced Planck constant and the speed of light. It has no units.">{String.raw`\alpha=\frac{e^2}{4\pi\varepsilon_0\hbar c}\approx\frac1{137}`}</Math>
    <p>Writing its inverse gives the number near 137. The comparison here concerns the low energy Thomson limit. Matching a calculated boundary response to that physical observable is a specific part of the task.</p>
    <p>There are three kinds of step below: exact counts and identities, a response calculated under a named contract, and the remaining identification with physical electromagnetism. Keeping those steps visible explains both the number and what its calculation establishes.</p>

    <ol className={styles.sequence}>
      <li>
        <h3>Begin with the boundary and carrier</h3>
        <p>P1 fixes the seam normalization. The marked five slot carrier supplies the 3+2 charge split; its even representation has 16 components. Three family directions then give 48 admissible components. These are internal representation counts.</p>
        <Math block plain="The boundary normalization is one over eight pi. The base opening is one over six pi. Three families of sixteen give the topological weight forty eight times the fourth power of the seam constant.">{String.raw`\begin{aligned}c_3&=\frac1{8\pi},\\\varphi_{\rm base}&=\frac1{6\pi},\\\delta_{\rm top}&=3\cdot16\,c_3^4.\end{aligned}`}</Math>
        <p className={styles.source}><Link href={source.closure}>Original architecture: normalization, carrier count and contact grammar</Link></p>
      </li>
      <li>
        <h3>Let the defect respond to alpha</h3>
        <p>In the original defect sector, an additive action shift αJ changes the relative weight by exp(−αJ). On the stated double cover, primitive spectral flow one per sheet gives J = 2. This is the source of the exponential, including its factor two.</p>
        <Math block plain="The alpha dependent defect weight is the topological weight multiplied by the exponential of minus two alpha.">{String.raw`q(\alpha)=\delta_{\rm top}\,e^{-2\alpha}`}</Math>
        <p>The original circle also determines the single defect line: its winding changes the polarization by a rank one projector Π. Consequently its ordered relative Fredholm determinant is exactly 1−q. The later marked D₅ grade calculation realizes the fractional response (1−uq)<sup>−5/4</sup> in the existing source. The common time diagonal has exponent 2, so the marked measurement matters.</p>
        <Math block plain="The seam opening equals its base plus the defect weight times the inverse determinant response with exponent five quarters.">{String.raw`\varphi_s(\alpha)=\frac1{6\pi}+q(\alpha)\,[1-q(\alpha)]^{-5/4}`}</Math>
        <p>The exponent has an exact charge trace origin: Bγ = (3/2)(5/6) = 5/4. Choosing the EM coupling q(α), the outer factor q and this additive baseline in that same physical channel remains part of the response contract.</p>
        <p className={styles.source}><Link href={source.index}>Original exponential reweighting</Link><Link href={source.circle}>Reconstructed circle defect</Link><Link href={source.grade}>Marked D₅ response proof</Link></p>
      </li>
      <li>
        <h3>Read the shared charge and flavour budget</h3>
        <p>The compiler gives a total flavour transport length of 40. One Higgs contribution makes 41. The same three family charge content gives the normalized U(1) index b₁ = 41/10. This is why the electromagnetic equation reads a budget already present in the matter construction.</p>
        <Math block plain="Forty transport units plus one Higgs give forty one. Eight times b one equals four fifths times forty one.">{String.raw`\begin{aligned}M&=\sum_{f,j}L_{f,j}+N_\Phi\\&=40+1=41,\\8b_1&=8\cdot\frac{41}{10}=\frac45\cdot41.\end{aligned}`}</Math>
        <p>The value 40 is connected to the charge pattern through the stated compiler identity below. Here X = 6Y is integer hypercharge and the trace sums over the sixteen components of one family. The division by three is this compiler relation, rather than an average over three families; the flavour operators and their transport remain its prerequisites.</p>
        <Math block plain="The squared integer hypercharges sum to one hundred twenty. The stated compiler relation divides that trace by three to give the flavour transport budget forty.">{String.raw`\begin{aligned}\operatorname{Tr}X^2&=120,\\\sum_{f,j}L_{f,j}&=\frac{\operatorname{Tr}X^2}{3}=40.\end{aligned}`}</Math>
        <p className={styles.source}><Link href="/explain#budget">Inspect the charge trace and budget identity</Link><Link href="/results?claim=CARRIER.CUTCODE.01">Read its registered statement</Link></p>
        <p className={styles.source}><Link href={source.closure}>Original budget and hypercharge index</Link><Link href="/explain#matter">Follow the charge construction</Link></p>
      </li>
      <li>
        <h3>Assemble the stated electromagnetic closure</h3>
        <p>The closure balances a local cubic term, a quadratic sheet term and a logarithmic transport response. The paper names these the Maxwell moment, Calderón sheet contribution and C₆ transport determinant.</p>
        <Math block plain="F of alpha equals alpha cubed minus twice c three cubed times alpha squared minus four fifths times forty one times c three to the sixth times the logarithm of one over the seam opening. The closure sets F to zero.">{String.raw`\begin{aligned}F(\alpha)&=\alpha^3-2c_3^3\alpha^2\\&\quad-\frac45\,M c_3^6\log\frac1{\varphi_s(\alpha)},\\M&=41,\qquad F(\alpha)=0.\end{aligned}`}</Math>
        <p>The powers of c₃ follow the stated seam insertion grammar: three in the quadratic coefficient, six in the transport coefficient. The logarithm belongs to the determinant description. The carrier identities fix the displayed coefficient values within this closure; they do not alone derive its local functional form.</p>
        <p>The older scalar potential makes the construction explicit: it supplies the local derivative α³−2c₃³α² and integrates the desired response to obtain a stationary action. The present physical question is whether the original local EM operator and its renormalized measure produce this same variation.</p>
        <p className={styles.source}><Link href={source.transfer}>Original definition of the closure potential</Link><Link href={source.measure}>Local measure and Quillen scope</Link></p>
      </li>
      <li>
        <h3>Prove that the equation selects one positive root</h3>
        <p>This is a theorem for the specified function, whose seam opening depends on α. For 0 &lt; α ≤ 2c₃³ the function is negative. Log convexity of the seam response gives strict convexity of F beyond that point. The cubic eventually grows without bound, so F crosses zero exactly once, with positive derivative.</p>
        <p>The argument holds for every positive budget M. It proves uniqueness after the inputs and response are fixed; it does not select 41 in place of another positive budget. An interval enclosure then locates the root.</p>
        <AlphaExplorer />
        <p className={styles.source}><Link href={source.proof}>Read the analytic proof and interval enclosure</Link></p>
      </li>
      <li>
        <h3>Compare the result with measurement</h3>
        <AlphaComparison />
        <p>This dated comparison uses the CODATA 2022 recommended inverse coupling, 137.035 999 177 (21). The closure differs by about 1.9 experimental standard deviations. Alpha had already been measured when the formula was constructed; this comparison is a calculated relation to an existing measurement.</p>
        <p>The mathematical root, the reconstructed circle line, the marked D₅ response and the finite determinant line and KMS results remain achieved. The remaining connection is specific: the original local EM source and operator map must yield the relative real renormalized determinant norm, its coupling and variation, then match the physical Thomson coupling.</p>
        <p className={styles.source}><Link href="/results?search=alpha-exact-coefficients-and-root">Read the current reviewed physical scope</Link><Link href="/empirical-audit">Open the dated empirical comparison</Link></p>
      </li>
    </ol>

    <details className={`guide-details ${styles.ingredients}`}>
      <summary>Trace every ingredient: value, meaning, original source and scope</summary>
      <div className={styles.tableWrap}><table><caption>Provenance of the specified alpha closure</caption><thead><tr><th scope="col">Value</th><th scope="col">What it means</th><th scope="col">Original source</th><th scope="col">What the step establishes</th></tr></thead><tbody>{ingredients.map((i) => <tr key={i.symbol}><th scope="row"><Math ariaLabel={i.symbol}>{i.symbol}</Math></th><td>{i.meaning}</td><td><Link href={i.href}>{i.label}</Link></td><td>{i.scope}</td></tr>)}</tbody></table></div>
    </details>
    <details className={`guide-details ${styles.precision}`}>
      <summary>Inspect the numerical enclosure, full precision and response series</summary>
      <Math block plain="The proved root lies strictly between 0.0072973525622097 and 0.0072973525622100.">{String.raw`\begin{aligned}0.007\,297\,352\,562\,2097&<\alpha_\star,\\\alpha_\star&<0.007\,297\,352\,562\,2100.\end{aligned}`}</Math>
      <p>The original scalar closure gives the following higher precision approximation. These extra digits describe the calculated equation; the displayed interval above states the cited certified enclosure.</p>
      <Math block plain="Calculated inverse alpha is approximately 137.03599921684071250353786030380388037.">{String.raw`\alpha_\star^{-1}\approx137.035\,999\,216\,840\,712\,503\,537\,860\,303\,803\,880\,37`}</Math>
      <Math block plain="The response series starts with q, plus five quarters q squared, plus forty five thirty seconds q cubed.">{String.raw`q(1-q)^{-5/4}=q+\frac54q^2+\frac{45}{32}q^3+\cdots`}</Math>
      <p>The series fixes higher response coefficients once this transfer is specified. The earlier linear, exponential, two defect and resummed calculations retain their own contracts; their similar factors do not identify all their physical actions.</p>
      <p className={styles.source}><Link href="/results?search=alpha-archive-term-provenance">Read the reviewed reconstruction of the original alpha factors</Link></p>
    </details>
  </section>;
}
