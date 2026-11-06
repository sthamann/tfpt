/** Authored reading editions of selected public arguments, not generated claim records. */
export type ResearchBlock =
  | { kind: "paragraph"; text: string }
  | { kind: "formula"; tex: string; plain: string };

export interface ResearchPage {
  slug: string;
  title: string;
  description: string;
  lead: string;
  scope: string;
  sectionIds: string[];
  /** Only a complete replacement of the selected library section may redirect. */
  redirectSectionIds?: string[];
  paper: { title: string; href: string; pdf: string };
  guide: { title: string; href: string };
  sections: { id: string; title: string; blocks: ResearchBlock[] }[];
  sources: { title: string; path: string; lineStart: number; lineEnd: number; href?: string }[];
  scripts: { filename: string; description: string }[];
}

// Pin publication-source links so the cited line ranges remain reproducible.
export const RESEARCH_SOURCE_REVISION = "2925e262855edf188b1e13a0310278066b20454b";
export function researchSourceHref(path: string, lineStart?: number, lineEnd?: number) {
  const anchor = lineStart ? `#L${lineStart}${lineEnd ? `-L${lineEnd}` : ""}` : "";
  return `https://github.com/sthamann/tfpt/blob/${RESEARCH_SOURCE_REVISION}/${path.split("/").map(encodeURIComponent).join("/")}${anchor}`;
}

const p = (text: string): ResearchBlock => ({ kind: "paragraph", text });
const f = (tex: string, plain: string): ResearchBlock => ({ kind: "formula", tex, plain });

export const researchPages: ResearchPage[] = [
  {
    slug: "e8-discriminant-glue",
    title: "The E₈ discriminant glue theorem",
    description: "Read the D₅ and A₃ discriminant argument: norms 5/4 and 3/4, an index 4 even extension, the E₈ lattice and its explicit 240 roots.",
    lead: "The D₅ carrier lattice and the A₃ family lattice have compatible discriminant forms. Their diagonal order 4 glue gives an even unimodular lattice of rank 8. This is the lattice argument behind the TFPT E₈ construction.",
    scope: "A mathematical construction with the stated positive definite D₅ and A₃ root lattices, normalized so roots have squared length 2. Identifying this lattice with a physical gauge theory requires the separate physical interfaces described in the papers.",
    sectionIds: ["section:2befc1b3b29d5cae0f23"],
    redirectSectionIds: ["section:2befc1b3b29d5cae0f23"],
    paper: { title: "E₈ Compiler & the Fine-Structure Constant", href: "/papers/architecture-e8", pdf: "/papers/tfpt_1_architecture_e8.pdf" },
    guide: { title: "E₈ and the Standard Model in TFPT", href: "/e8-standard-model" },
    sections: [
      { id: "discriminant-forms", title: "The two discriminant forms", blocks: [
        p("For an integral lattice L, its discriminant group is L*/L, where L* is the dual lattice. For an even lattice the squared norm defines a quadratic form on this group, valued modulo 2ℤ. Both lattices here have cyclic discriminant group of order 4. Their generating classes have the following norms."),
        f(String.raw`A_{D_5}\cong A_{A_3}\cong\mathbb Z/4\mathbb Z,\qquad \det D_5=\det A_3=4,\qquad q_{D_5}(1)=\frac54,\quad q_{A_3}(1)=\frac34.`, "Both discriminant groups are cyclic of order 4. Their generating norms are five quarters and three quarters."),
        p("In the product discriminant group, the diagonal class (1,1) has norm 2, which is zero modulo 2ℤ. All its multiples also have even norm. The subgroup it generates is therefore isotropic and has order 4. Adjoining the corresponding cosets is the even lattice extension used in the source."),
        f(String.raw`H=\langle(1,1)\rangle,\qquad |H|=4,\qquad q(k,k)=k^2\!\left(\frac54+\frac34\right)=2k^2\equiv0\pmod{2\mathbb Z}.`, "The diagonal subgroup has four elements and its quadratic form vanishes modulo even integers."),
      ] },
      { id: "even-extension", title: "The index 4 extension", blocks: [
        p("Let L₀ = D₅ ⊕ A₃ and let L be the extension associated with H. Its index is 4. The determinant of an overlattice is the original determinant divided by the square of its index, so the extension has determinant 1."),
        f(String.raw`[L:L_0]=4,\qquad \det L=\frac{\det D_5\,\det A_3}{[L:L_0]^2}=\frac{4\cdot4}{4^2}=1,\qquad \operatorname{rank}L=5+3=8.`, "The rank 8 extension is even and unimodular because its determinant is one."),
        p("The positive definite even unimodular lattice of rank 8 is E₈. This identifies the extension. In the source, the order 4 glue is denoted μ₄, whose four elements are {1, i, −1, −i}. The norm identity also appears directly in a spinor root split into five and three coordinates."),
        f(String.raw`\left\|\tfrac12(\pm1)^8\right\|^2=\underbrace{5\cdot\tfrac14}_{D_5}+\underbrace{3\cdot\tfrac14}_{A_3}=\frac54+\frac34=2.`, "A half integer root splits into five coordinates of total norm five quarters and three of total norm three quarters."),
      ] },
      { id: "roots-and-branching", title: "The explicit roots and branching", blocks: [
        p("The cited verification source constructs the roots in standard eight dimensional coordinates. There are 112 integer roots, obtained by choosing two coordinates and independent signs. There are 128 half integer roots, with an even number of minus signs. Every listed vector has squared norm 2."),
        f(String.raw`R(E_8)=\{\pm e_i\pm e_j:i<j\}\ \cup\ \left\{\tfrac12(\epsilon_1,\ldots,\epsilon_8):\epsilon_i\in\{\pm1\},\ \prod_i\epsilon_i=1\right\}.`, "The roots are the signed two coordinate vectors and the half integer vectors with even sign parity."),
        f(String.raw`4\binom82+2^7=112+128=240,\qquad \dim\mathfrak e_8=240+8=248.`, "The construction contains 240 roots and the Lie algebra has dimension 248."),
        p("Under D₅ × A₃, the adjoint decomposes into the two adjoints, a vector product and a pair of conjugate spinor products. The root count differs from the Lie algebra dimension by the eight Cartan directions."),
        f(String.raw`\mathfrak e_8=(45,1)\oplus(1,15)\oplus(10,6)\oplus(16,4)\oplus(\overline{16},\overline4).`, "The five representation blocks have dimensions 45, 15, 60, 64 and 64."),
        f(String.raw`248=45+15+60+64+64,\qquad240=40+12+60+64+64.`, "Removing the five and three Cartan directions gives the corresponding 240 root count."),
        p("The source script also supplies a simple root basis, its integral even Gram matrix, determinant 1 and the coordinates of every root in that basis. Those are the concrete checks cited by this argument; publishing their source does not report a new execution."),
      ] },
    ],
    sources: [{ title: "Original discriminant theorem and branching", path: "documents/tfpt_1_architecture_e8/sections/005-source.tex", lineStart: 166, lineEnd: 229 }],
    scripts: [{ filename: "v1_e8_glue.py", description: "Constructs the 240 roots and checks the simple root lattice certificate, discriminant norms, ranks and glue index." }],
  },
  {
    slug: "four-mark-divisor",
    title: "One four point divisor, a carrier of 5 and a family rank of 3",
    description: "Follow the original Riemann–Roch argument: the same four marked points on the sphere give h⁰ = 5 and homology rank 3, with the Clifford carrier reading.",
    lead: "The pair (5, 3) can be read from one geometric object. Four marked points on the projective line give a five dimensional meromorphic function space and three independent puncture cycles. The original argument then connects the function space to the carrier spinor.",
    scope: "The divisor and its two mathematical invariants are specified. Their arithmetic and the exterior algebra dimension are exact. The identification of the meromorphic modes and their spinor with the physical carrier retains the conditional scope recorded in ARCH.RRCAR.01 and ARCH.RRCAR.02.",
    sectionIds: ["section:584e87a9c163ac38f92f"],
    paper: { title: "Origin Theory: Anchors, Clocks & TFPT Structure", href: "/papers/origin-theory", pdf: "/papers/origin_theory.pdf" },
    guide: { title: "Three fermion generations in TFPT", href: "/three-fermion-generations" },
    sections: [
      { id: "same-divisor", title: "Keep the same four marked points", blocks: [
        p("Take the projective line, topologically a sphere, with the reduced divisor D consisting of the four fourth roots of unity. The degree of D is 4. The cycle and function constructions below use this same D."),
        f(String.raw`D=[1]+[i]+[-1]+[-i],\qquad\deg D=4,\qquad\mu_4=\{1,i,-1,-i\}.`, "The divisor is the sum of the four distinct fourth roots of unity."),
      ] },
      { id: "cycle-side", title: "The cycle side has rank 3", blocks: [
        p("On the punctured sphere, loops around the four punctures have one relation: their oriented sum is zero in first homology. Three independent cycles remain. In the original TFPT reading, this is the family rank."),
        f(String.raw`H_1(\mathbb P^1\setminus\mu_4;\mathbb Z)\cong\mathbb Z^3,\qquad N_{\mathrm{fam}}=\deg D-1=3.`, "Four punctures leave three independent homology cycles."),
      ] },
      { id: "function-side", title: "The function side has dimension 5", blocks: [
        p("The space H⁰(ℙ¹, O(D)) consists of meromorphic functions with at most simple poles at the marked points and no other poles. On the genus zero projective line, Riemann–Roch gives h⁰(O(D)) = deg D + 1 for a divisor of nonnegative degree. Applied to the same four marks, it gives five modes."),
        f(String.raw`C_{\mathrm{car}}=H^0(\mathbb P^1,\mathcal O(D)),\qquad\dim C_{\mathrm{car}}=h^0(\mathcal O(D))=4+1=5=g_{\mathrm{car}}.`, "Riemann–Roch gives a five dimensional function space for this degree 4 divisor."),
        p("Thus the two numbers are tied to one degree. They are two invariants of one object. Their agreement with the carrier and family numbers expresses a shared construction; they do not supply two independent confirmations."),
        f(String.raw`(g_{\mathrm{car}},N_{\mathrm{fam}})=(\deg D+1,\deg D-1)=(5,3).`, "One divisor degree determines both the carrier dimension and the cycle rank."),
      ] },
      { id: "spinor", title: "From five modes to the carrier spinor", blocks: [
        p("The source continues with the standard exterior algebra realization of the D₅ half spinor. For a five dimensional complex mode space, its even exterior powers have degrees 0, 2 and 4. Their dimensions add to 16."),
        f(String.raw`S^+=\Lambda^{\mathrm{even}}C_{\mathrm{car}}=\Lambda^0C_{\mathrm{car}}\oplus\Lambda^2C_{\mathrm{car}}\oplus\Lambda^4C_{\mathrm{car}},`, "The positive half spinor is realized by the even exterior powers of the five dimensional mode space."),
        f(String.raw`\dim S^+=\binom50+\binom52+\binom54=1+10+5=16=2^{5-1}.`, "The even exterior powers contain sixteen components."),
        p("Here 5 is the dimension of the mode space and the rank of D₅; 16 is the dimension of its half spinor representation. The original argument keeps the physical carrier identification conditional. The mathematical dimensions alone do not identify modes with physical particles or derive their dynamics."),
      ] },
    ],
    sources: [{ title: "Original same divisor and carrier argument", path: "documents/origin_theory/sections/001-section-the-whole-integer-skeleton-from-one-pair-gcar-nf.tex", lineStart: 36, lineEnd: 56 }],
    scripts: [
      { filename: "v189_riemann_roch_carrier.py", description: "Checks the two dimension formulas and their agreement with the compiler constants; records the conditional physical carrier identification." },
      { filename: "v197_rr_carrier_clifford_d5.py", description: "Checks the even exterior algebra dimension and the D₅ half spinor dimension chain; retains the physical identification as conditional." },
    ],
  },
  {
    slug: "alpha-fixed-point-proof",
    title: "Why the specified alpha equation has one positive root",
    description: "Read the complete convexity argument for the TFPT alpha equation: domain, log convexity, global existence, uniqueness and the numerical root enclosure.",
    lead: "The specified electromagnetic closure has exactly one positive simple root. The original convexity proof establishes this on the whole positive half line, without a numerical sign scan. It is a theorem about the stated function and its inputs.",
    scope: "Reading edition of EM.FP.POSITIVE_ROOT.CONVEXITY.01, dated 13 October 2026. The contract’s verdict is PARTIAL: the mathematical uniqueness question is settled for the specified function, while physical selection is a separate question. The published ledger classification remains Numerical.",
    sectionIds: ["section:6a757c5701557192653a"],
    paper: { title: "E₈ Compiler & the Fine-Structure Constant", href: "/papers/architecture-e8", pdf: "/papers/tfpt_1_architecture_e8.pdf" },
    guide: { title: "The fine structure constant in TFPT", href: "/fine-structure-constant" },
    sections: [
      { id: "function", title: "Fix the function and inputs", blocks: [
        p("Use c = 1/(8π), p = 1/(6π), d = 48c⁴ and s = 5/4. The physical budget used in the paper is M = 41. The proof below only needs M > 0, so uniqueness itself does not select the value 41."),
        f(String.raw`q(x)=d e^{-2x},\qquad u(x)=q(x)(1-q(x))^{-s},\qquad \varphi(x)=p+u(x),\qquad C=\frac45c^6M>0.`, "The seam response is a positive baseline plus a decaying correction, and C is positive."),
        f(String.raw`F(x)=x^3-2c^3x^2+C\log\varphi(x).`, "The closure is the cubic expression plus the logarithm of the specified seam response."),
        p("This is the same equation as F = x³ − 2c³x² − C log(1/φ) = 0. Because φ depends on x, the complete function is not a cubic polynomial."),
      ] },
      { id: "domain", title: "The function is negative before the cubic turns positive", blocks: [
        p("For x ≥ 0, π > 3 implies c < 1/24, d < 1/6912 < 1/1000 and p < 1/18. Therefore 0 < q ≤ d < 1/1000. Since s = 5/4 < 2, the seam response stays strictly between zero and one."),
        f(String.raw`(1-q)^{-s}<\left(\frac{1000}{999}\right)^2<2,\qquad 0<\varphi(x)<\frac1{18}+\frac1{500}<1.`, "The response is positive and below one, so its logarithm is negative."),
        p("The function is smooth. Set t = 2c³. For 0 < x ≤ t, the cubic part is nonpositive and the logarithmic part is strictly negative. There can be no root in this interval."),
        f(String.raw`F(x)=x^2(x-t)+C\log\varphi(x)<0\qquad(0<x\le t),\qquad F(t)<0.`, "The closure stays negative up to and including t."),
      ] },
      { id: "convexity", title: "The logarithmic response is strictly convex", blocks: [
        p("Put ℓ = log u and w = u/(p + u), so 0 < w < 1. Differentiating the specified response gives exact identities."),
        f(String.raw`\ell'=-2-\frac{2sq}{1-q},\qquad\ell''=\frac{4sq}{(1-q)^2}>0.`, "The second derivative of the logarithm of u is positive."),
        f(String.raw`(\log\varphi)''=w\ell''+w(1-w)(\ell')^2>0.`, "Both contributions to the second derivative of log phi are positive."),
        p("The second identity follows directly by differentiating log(p + exp ℓ). It gives a strict sign for the whole response rather than relying on an estimate that the correction is small."),
      ] },
      { id: "unique-root", title: "Existence, uniqueness and a simple crossing", blocks: [
        p("On x ≥ t, the second derivative of F is strictly positive. As x tends to infinity, φ tends to p > 0, so the logarithm has a finite limit while the cubic tends to infinity. Continuity and F(t) < 0 therefore give a root r > t."),
        f(String.raw`F''(x)=6x-4c^3+C(\log\varphi)''>8c^3>0\qquad(x\ge t).`, "The full closure is strictly convex after t."),
        p("At any root r > t, strict convexity makes the derivative greater than the secant slope from t to r. That slope is positive."),
        f(String.raw`F'(r)>\frac{F(r)-F(t)}{r-t}=\frac{-F(t)}{r-t}>0.`, "Every root crosses with a strictly positive derivative."),
        p("After the first root, the derivative is positive and increasing. A second crossing is impossible. Together with the negative interval before t, this proves exactly one positive root on the whole positive half line. Its positive derivative also proves that it is simple."),
      ] },
      { id: "location", title: "Root location and what the theorem establishes", blocks: [
        p("For M = 41, the original proof reports opposite definite signs from the existing interval implementation F_iv at the following endpoints. Combined with the analytic uniqueness result, this encloses the unique root."),
        f(String.raw`0.0072973525622097<\alpha_\star<0.0072973525622100,\qquad\alpha_\star^{-1}\approx137.0359992168407.`, "The unique root has reciprocal approximately 137.0359992168407."),
        p("The analytic proof, the reported numerical enclosure and a fresh execution are distinct evidence. This page reproduces the argument and cites the existing calculation; it does not report a new run."),
        p("The same proof works for every positive M. The original contract also differentiates the root with respect to M, using its positive derivative at the crossing."),
        f(String.raw`\frac{dr}{dM}=-\frac{(4/5)c^6\log\varphi(r)}{F'(r)}>0.`, "Increasing the positive budget increases its unique positive root."),
        p("The theorem establishes uniqueness for the supplied equation. Deriving its physical electromagnetic response and identifying the result with the renormalized Thomson coupling require the original source and observable map. Those physical obligations are separate from the existence and uniqueness proof."),
      ] },
    ],
    sources: [
      { title: "Original global convexity proof, EM.FP.POSITIVE_ROOT.CONVEXITY.01", path: "experiments/theory-contracts/em-positive-root-convexity-20261013/PROOF.txt", lineStart: 1, lineEnd: 76, href: "/research/sources/3ccf6cd6ceaf16ffb0706cad.txt" },
      { title: "Equation and original manuscript lemma", path: "documents/tfpt_1_architecture_e8/sections/007-source.tex", lineStart: 1, lineEnd: 45 },
    ],
    scripts: [{ filename: "v3_em_alpha.py", description: "Defines the original F and F_iv, computes the root and checks the reported interval bracket and input ablations. Its finite partition is separate from the global analytic convexity proof." }],
  },
];

export function researchPageForSection(sectionId: string) {
  return researchPages.find((page) => page.sectionIds.includes(sectionId));
}

export function researchHrefForSection(sectionId: string) {
  const page = researchPageForSection(sectionId);
  return page ? `/research/${page.slug}` : undefined;
}
