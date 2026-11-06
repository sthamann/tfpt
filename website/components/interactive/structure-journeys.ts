import { bitCount, chargeSectors, evenMasks } from "@/lib/carrier";
import { E8_ROOTS, inner } from "./mechanisms";
import { easeJourney, journeyColors, type DrawKit, type JourneySpec } from "./chapter-journey-types";

const carrierSource = "/documentation?evidence=python_verification%3Averification%2Fv197_rr_carrier_clifford_d5.py";
const spectrumSource = "/documentation?evidence=python_verification%3Averification%2Fv310_carrier_sm_anomaly.py";
const glueSource = "/research/e8-discriminant-glue";
const rootSource = "/documentation?evidence=python_verification%3Averification%2Fv1_e8_glue.py";

/** The source's simple root basis, also used by v1_e8_glue.py. */
const simpleRoots = [
  [.5, -.5, -.5, -.5, -.5, -.5, -.5, .5],
  [1, 1, 0, 0, 0, 0, 0, 0],
  [-1, 1, 0, 0, 0, 0, 0, 0],
  [0, -1, 1, 0, 0, 0, 0, 0],
  [0, 0, -1, 1, 0, 0, 0, 0],
  [0, 0, 0, -1, 1, 0, 0, 0],
  [0, 0, 0, 0, -1, 1, 0, 0],
  [0, 0, 0, 0, 0, -1, 1, 0],
];
const gram = simpleRoots.map(a => simpleRoots.map(b => inner(a, b)));
function determinant(matrix: number[][]) {
  const m = matrix.map(row => [...row]); let previous = 1;
  // This positive definite Gram matrix has nonzero leading principal minors.
  for (let k = 0; k < m.length - 1; k++) {
    const pivot = m[k][k];
    for (let i = k + 1; i < m.length; i++) for (let j = k + 1; j < m.length; j++) m[i][j] = (m[i][j] * pivot - m[i][k] * m[k][j]) / previous;
    for (let i = k + 1; i < m.length; i++) m[i][k] = 0;
    previous = pivot;
  }
  return m[m.length - 1][m.length - 1];
}
const gramDeterminant = determinant(gram);
const chargeTraceTerms = chargeSectors.map(row => row.multiplicity * row.x ** 2);
const traceX2 = chargeTraceTerms.reduce((sum, value) => sum + value, 0);
const rootCounts = [0, 2, 1, 3].map(coset => E8_ROOTS.filter(root => root.coset === coset).length);

export const STRUCTURE_JOURNEYS: Record<string, JourneySpec> = {
  "standard-model": {
    name: "From five slots to the charge budget",
    steps: [
      {
        short: "Five marked slots", title: "Start with three colour slots and two weak slots",
        body: "The construction supplies five internal slots, marked as a group of three and a group of two. The marking tells us which transformations must preserve each group.",
        input: "The specified five dimensional complex carrier with its marked 3+2 split.",
        operation: "Keep the three colour directions and two weak directions as separate blocks.",
        output: "A carrier C⁵ = C³ ⊕ C² with a fixed marking.",
        formula: String.raw`C=\mathbb C^3\oplus\mathbb C^2,\qquad\dim C=3+2=5`,
        detail: "The five directions are internal carrier slots. They are not five spacetime directions. The marked carrier and its physical identification belong to the stated TFPT construction; this journey begins with them.",
        href: "/explain#inputs", from: [], additional: "The marked five dimensional carrier and the stated unitary structure are supplied inputs to this chapter.",
      },
      {
        short: "Count even choices", title: "Keep selections of zero, two or four slots",
        body: "An exterior basis state records which slots are occupied. Keeping even selections leaves one empty choice, ten pairs and five choices of four slots.",
        input: "The five distinct slots from the first step.",
        operation: "Enumerate each subset and retain subsets with even size.",
        output: "The three counts are 1, 10 and 5.",
        formula: String.raw`\binom50=1,\qquad\binom52=10,\qquad\binom54=5`,
        detail: "These are subsets of labelled slots. The empty selection is one basis state. In the specified exterior and Clifford construction, even parity selects one half spinor; particle meaning requires the actual carrier dictionary.",
        href: carrierSource, from: [0],
      },
      {
        short: "Sixteen components", title: "Combine the even selections into one representation",
        body: "Put the three even degrees together. Their dimensions add to sixteen. With the specified Clifford action, this is the D₅ half spinor used for one family.",
        input: "One empty state, ten degree two states and five degree four states.",
        operation: "Take the direct sum of the three even exterior powers.",
        output: "S⁺ has sixteen components.",
        formula: String.raw`S^+=\Lambda^0C\oplus\Lambda^2C\oplus\Lambda^4C,\qquad\dim S^+=1+10+5=16`,
        detail: "The standard insertion and removal operators give the Clifford action. Their quadratic generators preserve even parity and realize the spin action of so(10). This action supplies the representation statement. Identifying its components with physical fermion fields retains the marked carrier and source premises.",
        href: carrierSource, from: [1],
      },
      {
        short: "Fix slot charges", title: "Use the marked split to fix the relative slot charges",
        body: "Give every colour slot the same block phase weight and every weak slot another. Total determinant one makes the generator traceless. The primitive integer weights are −2 and +3 in the stated orientation.",
        input: "The marked 3+2 carrier, its block preserving unitary transformations and the charge convention X = 6Y.",
        operation: "Solve 3x_c + 2x_w = 0 and choose the primitive integer pair in the stated orientation; divide by six.",
        output: "Each colour slot carries Y = −1/3 and each weak slot Y = +1/2.",
        formula: String.raw`3x_c+2x_w=0,\quad(x_c,x_w)=(-2,3),\quad Y=\tfrac16\operatorname{diag}(-2,-2,-2,3,3)`,
        detail: "Transformations preserving the split and total determinant form S(U(3) × U(2)), with the stated Standard Model central quotient. The trace equation fixes the relative block weights. The common orientation and X = 6Y convention remain explicit. This branch reuses the marked slots directly; the number sixteen alone does not fix an operator.",
        href: "/explain#matter", from: [0], additional: "Use the stated orientation and normalized charge convention X = 6Y.",
      },
      {
        short: "Add selected charges", title: "Calculate the charge of an actual selection",
        body: "Select one colour slot and one weak slot. A charge operator on an exterior product adds the occupied slot charges, giving −1/3 + 1/2 = 1/6.",
        input: "An even degree two state with one colour slot and one weak slot occupied, and the charge operator from the previous branch.",
        operation: "Add the two occupied slot hypercharges.",
        output: "This component has hypercharge Y = 1/6.",
        formula: String.raw`Y(c_i\wedge w_a)=Y_c+Y_w=-\frac13+\frac12=\frac16`,
        detail: "There are three choices of colour slot and two choices of weak slot, giving six such components. Hypercharge Y and electric charge are distinct: electric charge additionally uses Q_em = T₃ + Y. The chosen weak component matters for that second operation.",
        href: "/explain#matter", from: [2, 3],
      },
      {
        short: "Six charge sectors", title: "Apply the same rule to all sixteen states",
        body: "Group every even selection by its colour and weak occupations. The six groups contain 1, 3, 6, 1, 2 and 3 components, with the same charge pattern used in the original spectrum.",
        input: "All sixteen even selections and the normalized slot charge operator.",
        operation: "For every mask, count occupied colour and weak slots, add their charges, and group equivalent occupation types.",
        output: "The groups are νᶜ, uᶜ, Q, eᶜ, L and dᶜ, with sixteen components in total.",
        formula: String.raw`\begin{aligned}&(\nu^c,u^c,Q,e^c,L,d^c):\\Y&=(0,-\tfrac23,\tfrac16,1,-\tfrac12,\tfrac13),\\n&=(1,3,6,1,2,3)\end{aligned}`,
        detail: "The superscript c denotes the conjugate field convention. This specified sixteen component family includes the neutral singlet. The colour and weak representations accompany the charges in the original dictionary. Anomaly cancellation checks this stated Weyl spectrum; its interacting physical realization has additional source obligations.",
        href: spectrumSource, from: [2, 3],
      },
      {
        short: "Trace 120 → 10/3", title: "Square the charges and count every component",
        body: "For integer charge X = 6Y, multiply each sector’s X² by its number of components. The six contributions add to 120. Dividing by 6² converts the result to the hypercharge trace 10/3.",
        input: "The six sector multiplicities and integer charges X = (0, −4, 1, 6, −3, 2).",
        operation: "Sum nX², then divide by 36 to obtain the trace of Y² on one family.",
        output: `Tr X² = ${traceX2}; Tr Y² = 10/3 on the sixteen component family.`,
        formula: String.raw`\operatorname{Tr}_{16}X^2=0+48+6+36+18+12=120,\qquad\operatorname{Tr}_{16}Y^2=\frac{120}{36}=\frac{10}{3}`,
        detail: "This is a trace over the full one-family representation, including multiplicities. The divisor 36 comes from X = 6Y. It is separate from the compiler identity ΣL = Tr X²/3 = 40, which also requires the actual flavour transport operators.",
        href: "/explain#budget", from: [5],
      },
      {
        short: "Weighted budget 41", title: "Apply the stated field weights and normalization",
        body: "Three Weyl families contribute 20/3. One complex Higgs doublet contributes 1/6. Their sum is 41/6; the carrier normalization then gives b₁ = 41/10, or a budget of 41 in tenths.",
        input: "The one-family charge trace, three Weyl families, one complex Higgs doublet and the stated carrier normalization.",
        operation: "Apply one loop weights 2/3 for Weyl fermions and 1/3 for the complex scalar, then multiply by 3/5.",
        output: "b₁ = 4 + 1/10 = 41/10; M = 10b₁ = 40 + 1 = 41.",
        formula: String.raw`b_Y=\frac23\cdot3\cdot\frac{10}{3}+\frac13\cdot2\left(\frac12\right)^2=\frac{41}{6},\quad k_Y=\frac{5/6}{1/2}=\frac53,\quad b_1=\frac35b_Y=\frac{41}{10}`,
        detail: "The five-slot traces Tr Y² = 5/6 and Tr T₃² = 1/2 give k_Y = 5/3. After normalization, the fermions contribute 4 and the Higgs 1/10. Three families and the Higgs content are supplied here; they do not follow just from the preceding one-family trace. Using this coefficient in the original local electromagnetic variation retains its further physical source identification.",
        href: "/explain#budget", from: [3, 6], additional: "Supply three Weyl families, one complex Higgs doublet and the stated one loop field weights.",
      },
    ],
  },
  e8: {
    name: "From two lattices to the E₈ certificate",
    steps: [
      {
        short: "Ranks 5 + 3", title: "Start with the two specified root lattices",
        body: "The carrier side supplies D₅ and the family side supplies A₃. Their ranks are five and three. Keep both integral pairings: joining their eight directions requires more than adding the counts.",
        input: "The positive definite D₅ and A₃ root lattices with their standard integral forms, normalized so roots have squared length two.",
        operation: "Form their orthogonal direct sum.",
        output: "L₀ = D₅ ⊕ A₃ has rank eight and determinant 4 × 4 = 16.",
        formula: String.raw`L_0=D_5\oplus A_3,\qquad\operatorname{rank}L_0=5+3=8,\qquad\det L_0=4\cdot4=16`,
        detail: "D₅ is the stated carrier root lattice. A₃ is the family residue lattice, with its integral Cartan pairing. Its pairing is distinct from the analytic Green metric between marked points. These are internal lattice directions, rather than a count of physical spacetime dimensions.",
        href: "/papers/architecture-e8", from: [], additional: "Begin with the specified positive root lattices and their actual integral pairings.",
      },
      {
        short: "5/4 + 3/4 = 2", title: "Compare the two discriminant norms",
        body: "The selected generating classes have squared norms 5/4 and 3/4. They add to two. This is the compatibility needed for the chosen pair of classes to have even total norm.",
        input: "The two lattice forms and their chosen generating classes in the dual lattices modulo the original lattices.",
        operation: "Evaluate the discriminant quadratic forms and add the generating norms.",
        output: "q_D(1) + q_A(1) = 5/4 + 3/4 = 2.",
        formula: String.raw`q_{D_5}(1)=\frac54,\qquad q_{A_3}(1)=\frac34,\qquad q_{D_5}(1)+q_{A_3}(1)=2`,
        detail: "The discriminant form is valued modulo even integers. In the standard coordinate split, five entries of magnitude 1/2 contribute 5/4 and three contribute 3/4. This norm identity is a compatibility condition within the actual lattice construction.",
        href: glueSource, from: [0],
      },
      {
        short: "Match four classes", title: "Pair the two cyclic groups of four classes",
        body: "Each lattice has discriminant group ℤ₄. Pair corresponding classes to make the diagonal subgroup generated by (1,1). Its four elements all have even total norm.",
        input: "The two cyclic discriminant groups and the compatible generating norms.",
        operation: "Match k on one side with k on the other, for k = 0, 1, 2, 3.",
        output: "H = ⟨(1,1)⟩ has order four and is isotropic for the discriminant form.",
        formula: String.raw`A_{D_5}\cong A_{A_3}\cong\mathbb Z_4,\qquad H=\langle(1,1)\rangle,\qquad q(k,k)=2k^2\equiv0\pmod{2\mathbb Z}`,
        detail: "A Smith form calculation gives the cyclic group of order four for each Cartan matrix. Isotropic here means that the total discriminant norm is zero modulo even integers, permitting an even extension. The generator labels are a convention; exchanging labels 1 and 3 does not create new particle species.",
        href: glueSource, from: [0, 1],
      },
      {
        short: "Index 4 → det 1", title: "Adjoin the four matched cosets",
        body: "The matching subgroup adds four cosets to the original direct sum. The extension has index four. Divide the old determinant by the square of that index: 16/16 = 1.",
        input: "The rank eight direct sum with determinant sixteen and the isotropic subgroup H of order four.",
        operation: "Take the associated even overlattice and apply the determinant versus index formula.",
        output: "The new lattice is even, positive definite, rank eight and unimodular.",
        formula: String.raw`[L:L_0]=4,\qquad\det L=\frac{\det L_0}{[L:L_0]^2}=\frac{16}{4^2}=1`,
        detail: "Unimodular means determinant one. Evenness comes from the isotropic glue, while positivity and rank come from the original Euclidean lattice. These hypotheses together identify the positive even unimodular lattice of rank eight. The following explicit vectors make the construction inspectable.",
        href: glueSource, from: [0, 2],
      },
      {
        short: "52 + 60 integers", title: "Construct the two groups of integer roots",
        body: "In the five plus three coordinate chart, integer roots have two nonzero entries, each ±1. Keeping both entries in one block gives 52 roots. Placing one in each block gives another 60.",
        input: "The even extension and its standard five plus three Euclidean coordinate realization, with A₃ represented isometrically by D₃.",
        operation: "Enumerate the signed pairs within blocks and across the block boundary.",
        output: `The integer groups contain ${rootCounts[0]} and ${rootCounts[1]} roots, totalling 112.`,
        formula: String.raw`4\binom52+4\binom32=40+12=52,\qquad4\cdot5\cdot3=60,\qquad52+60=112`,
        detail: "Within a block, choose two positions and two independent signs. Across blocks, choose one of five positions, one of three positions and four sign pairs. These are the norm two vectors in classes 0 and 2 of the stated coordinate realization.",
        href: rootSource, from: [0, 2, 3], additional: "Use the standard five plus three coordinate chart, with the isometry A₃ ≅ D₃.",
      },
      {
        short: "64 + 64 halves", title: "Add the two groups of half integer roots",
        body: "The remaining roots have eight entries ±1/2 and an even total number of minus signs. Either both blocks have even sign parity or both have odd parity. Each choice gives 64 roots.",
        input: "The same coordinate extension and its two matched spinor cosets.",
        operation: "Enumerate five-sign and three-sign blocks with matching parity.",
        output: `The half integer groups contain ${rootCounts[2]} and ${rootCounts[3]} roots, totalling 128.`,
        formula: String.raw`2^4\cdot2^2=64\ \text{for each parity pair},\qquad64+64=128`,
        detail: "Fixing parity leaves sixteen possible sign choices in the five-coordinate block and four in the three-coordinate block. Matching even with even and odd with odd gives an even total sign parity. The labels of classes 1 and 3 can be exchanged with the generator convention.",
        href: rootSource, from: [2, 4],
      },
      {
        short: "240 roots, norm 2", title: "Combine the actual vectors and check their lengths",
        body: "The 112 integer roots and 128 half integer roots are distinct. Every integer root has squared length 1 + 1; every half integer root has squared length eight times one quarter.",
        input: "The two enumerated integer groups and two enumerated half integer groups.",
        operation: "Join the lists, remove no vectors, and evaluate each vector’s Euclidean squared norm.",
        output: `${E8_ROOTS.length} distinct roots, each with squared length two.`,
        formula: String.raw`52+60+64+64=240,\qquad1^2+1^2=2,\qquad8\left(\frac12\right)^2=2`,
        detail: "The diagram projects actual eight-coordinate vectors onto the screen, so distinct roots can overlap in the picture. The original verification also checks all roots in the explicit simple root basis. A numerical match of counts alone would not provide that lattice certificate.",
        href: rootSource, from: [4, 5],
      },
      {
        short: "The E₈ certificate", title: "Check the basis, evenness and determinant together",
        body: "Take the original eight simple roots and form their Gram matrix. Its entries are integral, its diagonal entries are even and its determinant is one. The full source certificate puts every constructed root in this basis.",
        input: "The positive rank eight extension, determinant one and the constructed list of roots.",
        operation: "Form the simple root Gram matrix and check the original lattice certificate.",
        output: `The E₈ lattice: rank 8, even, determinant ${gramDeterminant}; its Lie algebra has 240 + 8 = 248 dimensions.`,
        formula: String.raw`G_{ij}=a_i\cdot a_j,\qquad G_{ii}=2,\quad\det G=1,\qquad\dim\mathfrak e_8=240+8=248`,
        detail: "The glyph uses the actual Gram entries of the source basis, with diagonal entries two and linked entries minus one. The source additionally checks that each of the 240 vectors has integer coordinates in that basis. This is a lattice and representation result. Identifying E₈ as an unbroken physical gauge group is not a claim of this construction; physical field and interaction maps retain their separate premises.",
        href: rootSource, from: [0, 3, 6],
      },
    ],
  },
};

function drawMask(mask: number, x: number, y: number, kit: DrawKit, size = 2.6) {
  for (let i = 0; i < 5; i++) kit.dot(x + (i - 2) * (size * 2 + 2), y, size, mask & 1 << i ? i < 3 ? journeyColors[0] : journeyColors[1] : "#263b51", "#66819e");
}

function drawCoordinates(vector: number[], y: number, kit: DrawKit) {
  vector.forEach((value, i) => kit.text(value === .5 ? "½" : value === -.5 ? "−½" : String(value).replace("-", "−"), (i - 3.5) * 19, y, 14, i < 5 ? journeyColors[0] : journeyColors[1]));
  kit.line(19, y - 13, 19, y + 5, "#526b85", true);
}

function drawMatter(index: number, kit: DrawKit, p: number) {
  const { text, dot, line, bar } = kit;
  const alpha = kit.ctx.globalAlpha;
  if (index === 0) {
    [-72, -36, 0, 44, 80].forEach((x, i) => { dot(x, -8, 11, i < 3 ? journeyColors[0] : journeyColors[1]); text(i < 3 ? "c" : "w", x, -8, 13, "#10273e", 600); });
    line(-84, 15, 12, 15); line(32, 15, 92, 15); text("3", -36, 40, 26); text("+", 19, 40, 22); text("2", 62, 40, 26);
  } else if (index === 1) {
    let position = 0;
    [0, 2, 4].forEach((degree, col) => {
      const masks = evenMasks.filter(mask => bitCount(mask) === degree), x = (col - 1) * 66;
      text(`${degree} slots`, x, -48, 13);
      masks.forEach((mask, row) => { kit.ctx.globalAlpha = alpha * (position++ < Math.ceil(p * 16) ? 1 : .15); drawMask(mask, x, (row - (masks.length - 1) / 2) * 8, kit, 2); });
      kit.ctx.globalAlpha = alpha; text(String(masks.length), x, 43, 22);
    });
  } else if (index === 2) {
    evenMasks.forEach((mask, i) => dot(-12 + i % 4 * 23, -35 + Math.floor(i / 4) * 24, 5.2, i < Math.ceil(p * 16) ? journeyColors[bitCount(mask) === 0 ? 2 : bitCount(mask) === 2 ? 0 : 1] : "#294057"));
    text("16", -66, 12, 35);
  } else if (index === 3) {
    [-2, -2, -2, 3, 3].forEach((value, i) => { const x = [-72, -36, 0, 44, 80][i]; dot(x, -27, 13, i < 3 ? journeyColors[0] : journeyColors[1]); text(value < 0 ? "−2" : "+3", x, -27, 13, "#10273e", 600); });
    text("3(−2) + 2(3) = 0", 0, 14, 17); text("Y = X ÷ 6", 0, 43, 22);
  } else if (index === 4) {
    const mask = p < .35 ? 1 : 9;
    drawMask(mask, 0, -32, kit, 7);
    text(p < .35 ? "−1/3" : "−1/3 + 1/2", 0, 8, 21);
    text(p < .35 ? "−1/3" : "1/6", 0, 38, 32, journeyColors[1]);
  } else if (index === 5) {
    chargeSectors.forEach((row, i) => { const x = -77 + i * 31; const height = row.multiplicity / 6 * 58; bar(x - 9, 25 - height, 18, height, p, journeyColors[i % journeyColors.length]); text(String(row.multiplicity), x, 18 - height, 14); text(row.label, x, 46, 14); });
  } else if (index === 6) {
    chargeSectors.forEach((row, i) => { const x = -77 + i * 31, contribution = chargeTraceTerms[i], height = contribution / 48 * 44; bar(x - 9, 10 - height, 18, height, p, journeyColors[i % journeyColors.length]); text(String(contribution), x, 3 - height, 12); });
    text(`${traceX2} ÷ 36 = 10/3`, 0, 44, 20);
  } else if (index === 7) {
    for (let i = 0; i < 41; i++) dot(-64 + i % 9 * 16, -42 + Math.floor(i / 9) * 17, 4, i < Math.ceil(p * 41) ? i === 40 ? journeyColors[2] : journeyColors[0] : "#294057");
    text("40 + 1 = 41", 0, 43, 22);
  }
}

function drawLattice(index: number, kit: DrawKit, p: number) {
  const { text, dot, line, ctx } = kit;
  const alpha = ctx.globalAlpha;
  if (index === 0) {
    for (let i = 0; i < 5; i++) dot(-45, -40 + i * 20, 4.5, journeyColors[0]);
    for (let i = 0; i < 3; i++) dot(45, -20 + i * 20, 4.5, journeyColors[1]);
    text("D₅", -76, 5, 20); text("A₃", 77, 5, 20); text("+", 0, 4, 24); text("= 8", 0, 43, 22);
  } else if (index === 1) {
    for (let i = 0; i < 8; i++) { ctx.fillStyle = i < Math.ceil(p * 8) ? i < 5 ? journeyColors[0] : journeyColors[1] : "#294057"; ctx.fillRect(-70 + i * 18, -21, 14, 29); }
    text("5/4", -30, -38, 21, journeyColors[0]); text("3/4", 47, -38, 21, journeyColors[1]); text("= 2", 0, 38, 30);
  } else if (index === 2) {
    for (let i = 0; i < 4; i++) { const y = -44 + i * 29; dot(-56, y, 11, journeyColors[0]); dot(56, y, 11, journeyColors[1]); text(String(i), -56, y, 14, "#10273e", 600); text(String(i), 56, y, 14, "#10273e", 600); if (p >= i / 4) line(-40, y, -40 + 80 * Math.min(1, Math.max(0, p * 4 - i)), y, journeyColors[2]); }
  } else if (index === 3) {
    text("4 × 4", 0, -32, 25); line(-52, -15, 52, -15); text("4²", 0, 12, 25); text("= 1", 0, 39, 29, journeyColors[1]);
  } else if (index === 4 || index === 5) {
    const cosets = index === 4 ? [0, 2] : [1, 3];
    cosets.forEach((coset, i) => { const root = E8_ROOTS.find(value => value.coset === coset)!; ctx.globalAlpha = alpha * (p < i * .35 ? .18 : 1); drawCoordinates(root.vector, -28 + i * 38, kit); });
    ctx.globalAlpha = alpha;
    text(index === 4 ? `${rootCounts[0]} + ${rootCounts[1]} = 112` : `${rootCounts[2]} + ${rootCounts[3]} = 128`, 0, 44, 19);
  } else if (index === 6) {
    const xBasis = Array.from({ length: 8 }, (_, i) => .5 * Math.cos(i * Math.PI / 4));
    const yBasis = Array.from({ length: 8 }, (_, i) => .5 * Math.sin(i * Math.PI / 4));
    E8_ROOTS.slice(0, Math.ceil(p * E8_ROOTS.length)).forEach(root => dot(inner(root.vector, xBasis) * 54, inner(root.vector, yBasis) * 24 - 10, 1.6, journeyColors[[0, 2, 1, 3].indexOf(root.coset)]));
    text("240 roots · length² 2", 0, 44, 17);
  } else if (index === 7) {
    gram.forEach((row, i) => row.forEach((value, j) => { ctx.fillStyle = value === 2 ? journeyColors[0] : value === -1 ? journeyColors[1] : "#294057"; ctx.globalAlpha = alpha * (i * 8 + j < Math.ceil(p * 64) ? 1 : .15); ctx.fillRect(-65 + j * 9, -45 + i * 9, 6, 6); }));
    ctx.globalAlpha = alpha; text("det", 67, -13, 17); text(String(gramDeterminant), 67, 20, 32, journeyColors[1]); text("rank 8 · even · det 1", 0, 44, 16);
  }
}

/** Draw one authored operation in the engine's local 200 × 115 region. */
export function drawStructureStep(chapter: string, index: number, kit: DrawKit): void {
  kit.ctx.save();
  const progress = easeJourney(kit.progress);
  if (chapter === "standard-model") drawMatter(index, kit, progress);
  else if (chapter === "e8") drawLattice(index, kit, progress);
  kit.ctx.restore();
}
