/** Public explanations shared by the topic pages, FAQ and /llms.txt.
 * Mathematical statements and physical identifications keep separate scopes.
 */
export interface TopicLink {
  label: string;
  href: string;
}

export interface TopicSection {
  id: string;
  title: string;
  paragraphs: string[];
  formula?: { tex: string; plain: string };
  sources?: TopicLink[];
}

export interface TopicGuideData {
  id: string;
  slug: string;
  title: string;
  question: string;
  intro: string;
  answer: string;
  claim: string;
  scope: string;
  sections: TopicSection[];
  sources: TopicLink[];
  verification: { description: string; links: TopicLink[] };
  faqs: { question: string; answer: string }[];
}

export const PROJECT_SUMMARY = "Topological Fixed-Point Theory (TFPT) is a research programme by Stefan Hamann and Alessandro Rizzo. It connects a structured oriented boundary source and a marked five slot carrier to E₈ lattice structure, Standard Model representations, flavour relations and numerical readouts. Its mathematical results retain their stated premises. Complete source transports are available in their scopes; identifying and evaluating the full original interacting physical source remains a central research goal.";

const architecture = { label: "Architecture paper and PDF", href: "/papers/architecture-e8" };
const standardModel = { label: "Standard Model paper and PDF", href: "/papers/standard-model" };
const origin = { label: "Origin paper and PDF", href: "/papers/origin-theory" };
const glue = { label: "Original glue theorem and premises", href: "/research/e8-discriminant-glue" };
const alpha = { label: "Original electromagnetic equation", href: "/documentation?section=section%3A6a757c5701557192653a" };
const family = { label: "Original four mark construction", href: "/research/four-mark-divisor" };

export const TOPIC_GUIDES: readonly TopicGuideData[] = [
  {
    id: "alpha",
    slug: "/fine-structure-constant",
    title: "The fine structure constant in TFPT",
    question: "What does TFPT derive about the fine structure constant?",
    intro: "Follow TFPT’s electromagnetic equation from its boundary normalization and charge content to the calculated value of alpha. Inspect every coefficient, vary the trial coupling and compare the root with CODATA.",
    answer: "The fine structure constant α measures electromagnetic interaction strength. A specified TFPT boundary equation has exactly one positive solution, giving α⁻¹ = 137.03599921684… . The root and its uniqueness are mathematical results under the stated inputs. Identifying the whole equation with the physical electromagnetic response and the Thomson coupling remains a separate derivation.",
    claim: "The specified alpha dependent boundary equation has a unique positive simple root with α⁻¹ ≈ 137.03599921684.",
    scope: "This is a result for the stated response function and inputs. It does not by itself establish the original electromagnetic functional or its physical Thomson identification.",
    sections: [
      {
        id: "meaning", title: "What does alpha measure?",
        paragraphs: ["Alpha is dimensionless: its value does not depend on a choice of metres, seconds or another unit system. In SI units, α = e²/(4πε₀ℏc). Here e is the elementary charge, ε₀ the vacuum permittivity, ℏ the reduced Planck constant and c the speed of light.", "The number near 137 is its reciprocal. The comparison on this page concerns the low energy fine structure constant. A coupling quoted at another energy needs the appropriate physical running and matching convention."],
      },
      {
        id: "equation", title: "The equation and its inputs",
        paragraphs: ["Write c₃ = 1/(8π), φbase = 1/(6π), δtop = 48c₃⁴ and q(α) = δtop exp(−2α). The seam response is φs(α) = φbase + q(α)(1 − q(α))^(−5/4). The equation then reads:"],
        formula: { tex: String.raw`F_{U(1)}(\alpha)=\alpha^3-2c_3^3\alpha^2-\frac45\,41c_3^6\log\frac1{\varphi_s(\alpha)}=0`, plain: "The cubic and quadratic terms balance a logarithmic seam response. That response also depends on alpha, so the complete equation is more than a cubic polynomial." },
        sources: [alpha],
      },
      {
        id: "derivation", title: "Where do the coefficients come from?",
        paragraphs: ["The construction supplies a boundary normalization c₃ and a marked five slot carrier. The exponent 5/4 is the D₅ discriminant norm. The admissible count is 48 = 3 × 16, and the declared four seam factors give δtop = 48c₃⁴. The flavour transport budget is 40; one Higgs contribution gives M = 41 and the abelian index b₁ = 41/10. Thus the coefficient (4/5)41 equals 8b₁.", "These are exact identities within the specified construction. Their use together in the same physical electromagnetic response carries additional source and operator premises. The current finite determinant and charged grade results must be retained, while the complete local electromagnetic functional and its normalization still need their own identification."],
        sources: [{ label: "Follow each coefficient and its provenance", href: "/explain#alpha" }, { label: "Current root and physical source assessment", href: "/results?search=alpha-exact-coefficients-and-root" }],
      },
      {
        id: "uniqueness", title: "Why is there only one positive solution?",
        paragraphs: ["The analytic argument first proves that F is negative from zero through α = 2c₃³. Above that point, the logarithm of the positive seam response is strictly convex, making F strictly convex as well. The cubic eventually grows without bound. F therefore crosses zero exactly once, with positive derivative at the crossing.", "An interval calculation brackets that root between 0.0072973525622097 and 0.0072973525622100. The analytic proof supplies global uniqueness; the interval calculation supplies a numerical location. The same uniqueness argument works for every positive budget M, so uniqueness alone does not select M = 41."],
        sources: [{ label: "Read the analytic proof and interval scope", href: "/research/alpha-fixed-point-proof" }],
      },
      {
        id: "measurement", title: "Comparison with CODATA 2022",
        paragraphs: ["The formula gives α⁻¹ = 137.0359992168407… . The CODATA 2022 adjustment gives 137.035999177(21), where the parenthesis means a standard uncertainty of 0.000000021. The difference is about 1.9 times that quoted uncertainty, or about 2.9 × 10⁻¹⁰ of the measured value.", "This is a dated comparison with known data. Alpha was measured before the formula freeze, so later registration does not turn the comparison into a blind prediction. Reproducing the root tests the calculation; establishing its physical origin requires the electromagnetic source map described above."],
        sources: [{ label: "NIST: CODATA 2022 values", href: "https://physics.nist.gov/cuu/pdf/wall_2022.pdf" }, { label: "Registered predictions and comparison categories", href: "/predictions" }],
      },
    ],
    sources: [architecture, alpha, { label: "Analytic positive root proof", href: "/research/sources/3ccf6cd6ceaf16ffb0706cad.txt" }],
    verification: {
      description: "The original v3 module reproduces the root, computes the interval enclosure, checks the inverse budget and compares altered inputs. The separate analytic proof establishes uniqueness on the full positive half line. Downloading a script is distinct from executing it; the reproduction guide explains the runtime and dependencies.",
      links: [{ label: "Download v3_em_alpha.py", href: "/verification/v3_em_alpha.py" }, { label: "Reproduction instructions", href: "/replication" }, { label: "Root result and source record", href: "/results?search=alpha-global-positive-root" }],
    },
    faqs: [
      { question: "Is the TFPT alpha value fitted to CODATA?", answer: "The published equation uses fixed construction inputs and evaluates its root without adjusting a continuous parameter to CODATA. Its agreement is a comparison with previously known data. The physical selection of the equation and all its inputs is a separate question from solving it." },
      { question: "Is the alpha equation just a cubic?", answer: "It contains cubic and quadratic terms, plus a logarithmic response that itself depends on alpha through an exponential. The full function is therefore not a cubic polynomial." },
      { question: "Does the root prove the electromagnetic origin?", answer: "The root and its global uniqueness are established for the specified function. The complete original electromagnetic variation, its real renormalized determinant response and the identification with the physical Thomson coupling retain their own obligations." },
    ],
  },
  {
    id: "e8",
    slug: "/e8-standard-model",
    title: "E₈ and Standard Model structure in TFPT",
    question: "How does TFPT connect E₈ to the Standard Model?",
    intro: "Build the E₈ lattice from D₅ and A₃, then inspect the representations and charges of the marked carrier. Follow the construction through its exact mathematical steps and physical interpretation.",
    answer: "TFPT constructs the E₈ lattice by joining a D₅ carrier lattice and an A₃ family lattice through their matching ℤ₄ discriminant data. Standard Model representations and charges are read from the marked 3+2 carrier and its even exterior representation. The lattice closure is exact under its premises; E₈ itself is not asserted to be the unbroken physical gauge group.",
    claim: "The specified D₅ ⊕ A₃ lattice has an index four even unimodular extension isometric to E₈, with an explicit 240 root certificate.",
    scope: "The lattice theorem and carrier representation do not alone establish a complete interacting chiral Standard Model in physical spacetime. Physical field maps and source premises remain attached to that interpretation.",
    sections: [
      {
        id: "lattice", title: "What is E₈ in this construction?",
        paragraphs: ["A lattice is a discrete set of vectors closed under integer addition. The positive E₈ lattice has eight dimensions, even squared lengths and determinant one. Its 240 shortest nonzero vectors have squared length two. The associated Lie algebra has dimension 248, counting those 240 roots and eight Cartan directions.", "TFPT uses E₈ as a closure and consistency structure. The construction begins with a specified five slot carrier and four marked boundary points, from which its D₅ and A₃ parts are obtained. The eight lattice directions are internal mathematical data; their number does not count physical spacetime dimensions."],
        sources: [architecture],
      },
      {
        id: "glue", title: "How D₅ and A₃ close to E₈",
        paragraphs: ["Each lattice has determinant four and discriminant group ℤ₄. The selected generators have discriminant norms 5/4 and 3/4. Their sum is two, so the diagonal order four glue is isotropic modulo even integers. Adjoining its cosets produces an even lattice of rank eight and determinant one."],
        formula: { tex: String.raw`q(D_5)+q(A_3)=\frac54+\frac34=2,\qquad [E_8:D_5\oplus A_3]=4`, plain: "The two discriminant norms combine to an even norm. The extension contains four cosets of the original direct sum; its determinant is 4 × 4 divided by 4 squared, which equals one." },
        sources: [glue],
      },
      {
        id: "carrier", title: "Where the particle representation enters",
        paragraphs: [String.raw`On a complex five dimensional carrier \(C\), the even exterior representation is \(\Lambda^{\mathrm{even}}C=\Lambda^0C\oplus\Lambda^2C\oplus\Lambda^4C\). Its dimensions are \(1+10+5=16\). This is the D₅ half spinor in the stated Clifford construction. Its identification with one physical fermion family carries the marked carrier and field dictionary.`, "The 3+2 split separates three colour slots and two weak slots. Unitary transformations preserving the split and total determinant form S(U(3) × U(2)), isomorphic to (SU(3) × SU(2) × U(1))/ℤ₆.", String.raw`The remaining block phase has one weight \(x_c\) on each colour slot and one weight \(x_w\) on each weak slot. The total determinant condition makes its generator traceless: \(3x_c+2x_w=0\). The primitive integer pair is \((-2,3)\), up to a common sign. In the stated orientation and charge convention \(X=6Y\), this gives \(Y_c=-1/3\) and \(Y_w=+1/2\). Charges add on exterior states.`],
        formula: { tex: String.raw`Y=\frac16\operatorname{diag}(-2,-2,-2,3,3)`, plain: "Selecting one colour slot and one weak slot gives hypercharge −1/3 + 1/2 = 1/6, as required for the quark doublet representation in this charge convention." },
        sources: [standardModel, { label: "Work through the charges and anomaly check", href: "/explain#matter" }],
      },
      {
        id: "physical-scope", title: "What the lattice result establishes",
        paragraphs: ["An explicit lattice certificate checks the roots, their norms, an integral basis and determinant one. That is stronger than observing that several dimensions add up. The carrier calculation separately gives a charge spectrum whose gauge anomalies cancel in its stated Weyl interpretation.", "These results retain distinct roles. The glue theorem is a lattice statement. Charge assignments and anomaly cancellation are representation and consistency statements. A full physical realization also needs the actual fields, interactions, chiral spectrum and continuum behavior from the same physical source. The current source research tracks those connections separately."],
        sources: [{ label: "Inspect the source and field connections", href: "/explain#source" }, { label: "Result library: glue and its evidence", href: "/results?search=glue" }],
      },
    ],
    sources: [architecture, standardModel, glue],
    verification: {
      description: "The v1 module constructs all 240 roots, checks their squared norms, and certifies an even integral basis with determinant one. The v310 module checks the actual carrier charge list and its anomaly coefficients. These tests have different targets and do not certify a complete physical theory.",
      links: [{ label: "Download v1_e8_glue.py", href: "/verification/v1_e8_glue.py" }, { label: "Download v310_carrier_sm_anomaly.py", href: "/verification/v310_carrier_sm_anomaly.py" }, { label: "Reproduction instructions", href: "/replication" }],
    },
    faqs: [
      { question: "Does TFPT claim E₈ is the Standard Model gauge group?", answer: "E₈ is the internal lattice closure of the specified carrier and family construction. The subgroup preserving the marked 3+2 carrier supplies the Standard Model gauge structure in that construction. E₈ is not identified as the unbroken physical gauge group." },
      { question: "Do E₈'s eight dimensions mean eight spacetime dimensions?", answer: "They are eight lattice directions. Internal lattice rank, field components and physical spacetime dimensions refer to different spaces; moving between them requires an explicit physical map." },
      { question: "Does anomaly cancellation finish the physical derivation?", answer: "It checks consistency of the stated Weyl charge spectrum. The interacting physical source, chiral realization and continuum behavior require their own constructions and premises." },
    ],
  },
  {
    id: "families",
    slug: "/three-fermion-generations",
    title: "Three fermion generations in TFPT",
    question: "Why does TFPT have three fermion generations?",
    intro: "Start with four marked points on one sphere. Follow how the same object produces three cycle directions and a five dimensional function space, then inspect their family and carrier interpretation.",
    answer: "The TFPT family geometry is a sphere with four marked points removed, written ℙ¹ ∖ μ₄. Four loops around the punctures obey one relation, leaving three independent cycle directions: H₁(ℙ¹ ∖ μ₄, ℤ) ≅ ℤ³. Reading these directions as the three physical fermion families is the specified geometric identification; the topology alone does not establish that physical map.",
    claim: "The four puncture family geometry has first homology of rank three and an A₃ residue lattice. The same four point divisor has a five dimensional meromorphic function space.",
    scope: "The ranks three and five are exact invariants of the same specified geometry. Their identification with physical families and carrier modes retains the stated field and source premises; they are not independent experimental confirmations.",
    sections: [
      {
        id: "meaning", title: "What is a fermion generation?",
        paragraphs: ["A generation is one family of quarks and leptons with a common pattern of gauge representations. The familiar charged leptons are the electron, muon and tau, belonging to three families. Repetition of the charge pattern and the different masses and mixing angles are separate questions.", "In TFPT, the five slot carrier supplies one family representation. The family geometry supplies its three cycle directions. The three colour slots inside one carrier and the three family directions have different mathematical roles."],
        sources: [standardModel],
      },
      {
        id: "four-marks", title: "Why are there four marks?",
        paragraphs: [String.raw`The mark count follows in a specified geometric class. Take a sphere that is flat away from its branch points, with every branch point of order \(\mathbb Z_2\). Each point has cone angle \(\pi\), so its angle deficit is also \(\pi\). Gauss–Bonnet requires the deficits to sum to \(2\pi\chi(S^2)=4\pi\). Four such points are therefore required.`, String.raw`This fixes the count under the sphere, flatness and order two branch assumptions. The square arrangement \(\mu_4=\{1,i,-1,-i\}\) uses the separate order four carrier action. The deficit calculation alone leaves the shape parameter of the four marked sphere undetermined; it does not supply that action or the physical source identification.`],
        formula: { tex: String.raw`n\pi=2\pi\chi(S^2)=4\pi\qquad\Longrightarrow\qquad n=4`, plain: "Each order two branch point contributes a deficit of pi. A flat sphere requires a total deficit of four pi, giving four marked points." },
        sources: [{ label: "Original Gauss–Bonnet argument and its geometric assumptions", href: "/documentation?source=verification%2Fv216_marks_gauss_bonnet.py" }],
      },
      {
        id: "count", title: "Four punctures leave three independent loops",
        paragraphs: ["The complex projective line ℙ¹ is topologically a sphere. The four marks μ₄ = {1, i, −1, −i} are the fourth roots of unity. Remove them and draw a small loop around each missing point. Taken together, the four oriented loops bound the remaining punctured surface, so their sum vanishes in first homology. Any three provide an independent basis."],
        formula: { tex: String.raw`\gamma_1+\gamma_2+\gamma_3+\gamma_4=0,\qquad H_1(\mathbb P^1\setminus\mu_4,\mathbb Z)\cong\mathbb Z^3`, plain: "There are four puncture loops and one relation. The resulting cycle space has rank three." },
        sources: [family],
      },
      {
        id: "same-divisor", title: "The same four marks also give the five slot carrier reading",
        paragraphs: [String.raw`Let \(D\) be the divisor consisting of those four points. Riemann–Roch on ℙ¹ gives \(h^0(\mathbb P^1,\mathcal O(D))=5\). This function space allows at most simple poles at the four marks. The cycle space and the function space therefore read the same object in two ways:`],
        formula: { tex: String.raw`\operatorname{rank}H_1(\mathbb P^1\setminus D)=\deg D-1=3,\qquad h^0(\mathbb P^1,\mathcal O(D))=\deg D+1=5`, plain: "For a degree four divisor on the sphere, the cycle count is four minus one and the meromorphic function count is four plus one." },
        sources: [origin, { label: "Original Riemann–Roch and carrier premises", href: "/documentation?evidence=python_verification%3Averification%2Fv189_riemann_roch_carrier.py" }],
      },
      {
        id: "a3", title: "How the family geometry connects to E₈",
        paragraphs: ["The residue construction gives an A₃ root lattice with twelve roots, rank three and determinant four. Its canonical integral pairing is the lattice pairing used in the E₈ glue. This pairing must be distinguished from the analytic Green metric of the marked sphere, which is a characterized deformation.", String.raw`The rotation \(\rho:z\mapsto iz\) acts on these directions. In the cohomology basis \(\omega_k=z^{k-1}dz/(z^4-1)\), for \(k=1,2,3\), its pullback is \(\rho^*\omega_k=i^k\omega_k\). The three eigenvalues are therefore \(\{i,-1,-i\}\). This is the order four Coxeter action of the specified \(A_3\) lattice, preserving its Cartan pairing. It gives an actual action on the three dimensional space, beyond the rank count.`, "The A₃ discriminant group ℤ₄ matches the D₅ carrier discriminant group. Their selected discriminant norms 3/4 and 5/4 sum to two, allowing the index four extension to E₈. This connects the family and carrier structures through actual lattice data.", String.raw`Here \(A_3\) describes the rank three lattice associated with \(\mathfrak{su}(4)\). Its lattice rank, the three cohomology directions and the physical fermion family index have different roles. The stated family dictionary relates their actions; identifying the resulting module with physical families still carries the field and source assumptions.`],
        sources: [architecture, glue, { label: "Original cohomology basis and order four action", href: "/documentation?source=verification%2Fv177_seam_marking_kernel.py" }],
      },
      {
        id: "physical-scope", title: "What remains a physical identification?",
        paragraphs: ["The rank computation answers a precise question about the stated four puncture geometry. To explain the observed generations, the construction must also identify those cycle directions with the actual fermion fields, their group actions and the common physical source. A matching dimension alone does not supply this map.", "The shared divisor therefore unifies two exact mathematical counts, three and five, under the stated geometric carrier reading. The physical interpretation keeps its conditional status. Mass hierarchies, mixing and the interacting chiral realization have further constructions and assumptions; they do not follow from the homology rank alone."],
        sources: [{ label: "Follow the family and field dictionary", href: "/explain#matter" }, { label: "Inspect the common physical source", href: "/explain#source" }],
      },
    ],
    sources: [origin, architecture, standardModel, family],
    verification: {
      description: "The v189 module checks the two divisor invariants and preserves the conditional carrier reading explicitly. The v197 module checks the exterior algebra and half spinor dimensions. These calculations check dimension identities within the stated construction. The representation dictionary is a separate argument, and the physical identification of three families retains its own premises.",
      links: [{ label: "Download v189_riemann_roch_carrier.py", href: "/verification/v189_riemann_roch_carrier.py" }, { label: "Download v197_rr_carrier_clifford_d5.py", href: "/verification/v197_rr_carrier_clifford_d5.py" }, { label: "Reproduction instructions", href: "/replication" }],
    },
    faqs: [
      { question: "Why do four punctures give three families?", answer: "Four loops on the punctured sphere obey one homology relation, so their independent cycle count is three. TFPT reads these three directions as family directions under its stated physical dictionary." },
      { question: "Are the three families the three colours?", answer: "The three colour slots are part of one marked 3+2 carrier. The three family directions belong to the separate cycle space of the punctured sphere. They are different indices and different representations." },
      { question: "Are the counts three and five independent predictions?", answer: "Both follow from the same specified degree four divisor: rank H₁ = 3 and h⁰ = 5. Their shared origin is a unification of mathematical structures, rather than two independent experimental tests." },
    ],
  },
];

export function topicGuide(id: string): TopicGuideData {
  const guide = TOPIC_GUIDES.find((item) => item.id === id);
  if (!guide) throw new Error(`Unknown topic guide: ${id}`);
  return guide;
}
