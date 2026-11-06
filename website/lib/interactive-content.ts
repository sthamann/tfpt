/** Authored introductions to the existing public construction readers.
 * The linked originals own their scientific statements and assumptions.
 * Prediction counts follow public/verification/predictions_frozen.json.
 */
export type InteractiveChapterId =
  | "overview"
  | "alpha"
  | "standard-model"
  | "e8"
  | "dynamics"
  | "predictions"
  | "flavor"
  | "cosmology"
  | "quantum";

export interface InteractiveStep {
  readonly title: string;
  readonly body: string;
}

export interface InteractiveChapter {
  readonly id: InteractiveChapterId;
  readonly title: string;
  readonly question: string;
  readonly summary: string;
  readonly steps: readonly [InteractiveStep, InteractiveStep, InteractiveStep];
  readonly connection: string;
  readonly scope: string;
  readonly tryThis: string;
  readonly links: readonly { readonly href: string; readonly label: string }[];
}

export const INTERACTIVE_CHAPTERS: readonly InteractiveChapter[] = [
  {
    id: "overview",
    title: "How the pieces connect",
    question: "What connects the parts of TFPT?",
    summary: "Start with a boundary rule and five internal places. Follow how their structure organizes matter, builds the E₈ pattern and supplies numbers to compare with observations.",
    steps: [
      {
        title: "Start with the given rules",
        body: "A boundary rule describes how a change in one place affects another. Five labelled internal places supply the other starting structure.",
      },
      {
        title: "Follow what is shared",
        body: "The stated four mark geometry links the family and carrier counts. Those structures organize matter choices and join into the E₈ pattern.",
      },
      {
        title: "Compare the results",
        body: "Follow the shared structure into alpha, particle mixing and cosmic readouts. Compare each result with its source conditions and the relevant observation.",
      },
    ],
    connection: "The pictures follow reused objects and rules. A connection means that one calculation carries a specific result into another.",
    scope: "Exact mathematics, numerical readouts and physical identifications retain their own premises. Complete transports of a supplied source are available in their scopes; evaluating the full original interacting physical source and its spectrum remains a separate common task.",
    tryThis: "Start the visual journey. At each scene, point to what is being reused in the next scene.",
    links: [
      { href: "/explain", label: "Work through the connected explanation" },
      { href: "/architecture", label: "Inspect the system map and dependencies" },
      { href: "/explain#source", label: "Read the common source route" },
      { href: "/papers/introduction", label: "Open the original reading guide" },
    ],
  },
  {
    id: "alpha",
    title: "Finding the alpha number",
    question: "Can you find the number near 137?",
    summary: "Alpha tells us how strongly light and charged particles interact. One divided by alpha is near 137. Find the trial number where the two calculated sides balance.",
    steps: [
      {
        title: "Choose a trial number",
        body: "Move the slider. The two displayed sides are calculated from the same trial value.",
      },
      {
        title: "Find the balance",
        body: "Watch the gap between the sides. Find balance locates the value where the gap closes.",
      },
      {
        title: "Compare the number",
        body: "The result near 137 is inverse alpha. The dated measurement and its uncertainty provide the next comparison.",
      },
    ],
    connection: "The two sides reuse ingredients from the matter and E₈ constructions. Finding their balance calculates the number for those supplied ingredients.",
    scope: "Uniqueness is a theorem for the fixed response and every positive budget. Selecting the physical budget and identifying the full local electromagnetic variation with the renormalized Thomson coupling require the original source and observable map.",
    tryThis: "Move the trial number and compare the two sides. Press Find balance to locate where they meet.",
    links: [
      { href: "/fine-structure-constant", label: "Follow the coefficients and their provenance" },
      { href: "/research/alpha-fixed-point-proof", label: "Read the global positive root proof" },
      { href: "/empirical-audit", label: "Inspect dated measurement comparisons" },
    ],
  },
  {
    id: "standard-model",
    title: "Building a family of matter",
    question: "How do five places organize matter?",
    summary: "Turn five internal places on or off. Keep choices with zero, two or four occupied places. Their charges add, producing sixteen components grouped into one family in this construction.",
    steps: [
      {
        title: "Choose the occupied places",
        body: "The five places are internal labels. Three have colour labels and two have weak labels. Each toggle changes which places are occupied.",
      },
      {
        title: "Keep the even choices",
        body: "Keep zero, two or four occupied places. There are one, ten and five such choices, giving sixteen in total.",
      },
      {
        title: "Add their charges",
        body: "The display adds the charge contributions of the occupied places. Compare the sum before and after changing your selection.",
      },
    ],
    connection: "These five internal places supply the carrier used by the E₈ and alpha calculations. The three colour labels and the three family directions have different jobs.",
    scope: "The charge reader assumes the marked carrier, normalized hypercharge and even exterior representation. Anomaly cancellation checks that spectrum; a full interacting chiral realization also requires its physical fields, source and continuum construction.",
    tryThis: "Turn on one colour place and one weak place. Compare their added charge, then explore the other allowed choices.",
    links: [
      { href: "/e8-standard-model#carrier", label: "Operate on the carrier and read its charges" },
      { href: "/explain#matter", label: "Follow the gauge structure and anomaly calculation" },
      { href: "/three-fermion-generations", label: "See where the family index enters" },
      { href: "/papers/standard-model", label: "Read the Standard Model paper" },
    ],
  },
  {
    id: "e8",
    title: "Building the E₈ pattern",
    question: "How do four groups build E₈?",
    summary: "Build the pattern from groups of 52, 60, 64 and 64 points. Each point represents one of E₈’s shortest nonzero vectors, called roots.",
    steps: [
      {
        title: "Begin with the first group",
        body: "Add the first fifty two roots. They come from the two starting patterns, with forty on the carrier side and twelve on the family side.",
      },
      {
        title: "Add the missing groups",
        body: "Add sixty mixed roots, then two groups of sixty four. The running total reaches 240.",
      },
      {
        title: "Look at the same pattern again",
        body: "Replay the additions. Each group shows another part of the same fixed E₈ pattern.",
      },
    ],
    connection: "The carrier and family supply two starting patterns. The four groups show how their specified join builds the E₈ pattern.",
    scope: "This is a lattice theorem for the stated D₅ and A₃ inputs and their compatible glue. Identifying its representations and operators with a physical field theory requires the corresponding field and source dictionary.",
    tryThis: "Press Build next group until all 240 roots appear. Use Replay to watch the four additions again.",
    links: [
      { href: "/e8-standard-model#glue", label: "Build the four root classes" },
      { href: "/research/e8-discriminant-glue", label: "Read the discriminant argument" },
      { href: "/research/four-mark-divisor", label: "Trace the carrier and family to the same divisor" },
    ],
  },
  {
    id: "dynamics",
    title: "Watching three shares settle",
    question: "What happens after one more step?",
    summary: "Put a total share of one across three bins. Each step redistributes it using the fixed rule. The shares settle toward equality while their total stays one.",
    steps: [
      {
        title: "Choose a starting distribution",
        body: "A preset divides the total share among three bins. Read the three starting amounts and check that they add to one.",
      },
      {
        title: "Apply the rule once",
        body: "One step redistributes the shares using the specified rule. Compare the new bin amounts with the starting ones.",
      },
      {
        title: "Repeat the same rule",
        body: "Run eight steps. The differences shrink toward equal thirds while the total remains one.",
      },
    ],
    connection: "This example shows what the specified redistribution rule does. The clock example instead follows positions around a returning cycle.",
    scope: "The stated transfer spectrum establishes relaxation for that operator. It neither supplies the full interacting physical Hamiltonian nor assigns seconds to an internal step; the physical source, spectrum and dimensional calibration must support that interpretation.",
    tryThis: "Choose a starting preset. Press One step, then Run 8 steps, and compare the three shares with their unchanged total.",
    links: [
      { href: "/explain#source", label: "Follow the source, state and time reconstruction" },
      { href: "/explain#clocks", label: "Compare the different clock actions" },
      { href: "/results?record=finding%3Aoriginal-genesis-family-transfer-not-carroll-cycle", label: "Read the family transfer and physical period distinction" },
      { href: "/papers/origin-theory", label: "Read the original transfer argument" },
    ],
  },
  {
    id: "predictions",
    title: "Checking a calculated number",
    question: "How do we check a calculated number?",
    summary: "Reveal the calculation, its recorded number and a dated measurement. Compare the values and the measurement uncertainty while keeping the formula’s conditions visible.",
    steps: [
      {
        title: "Calculate",
        body: "Reveal the published rule and its supplied inputs. They determine the number shown by this example.",
      },
      {
        title: "Record",
        body: "Reveal the registered result. Its date and stated conditions stay attached to that number.",
      },
      {
        title: "Compare",
        body: "Reveal the dated measurement and its uncertainty. Compare the same quantity; keep a known data comparison distinct from a later prospective test.",
      },
    ],
    connection: "The register preserves what was calculated and when. The dated measurement supplies a separate observation for the comparison.",
    scope: "The register records commitments and categories. Its count is not a count of independent experimental confirmations, and freezing a formula after a quantity was measured does not make that comparison a blind prediction.",
    tryThis: "Choose Calculate, See the recorded value and Compare with measurement in order. Identify the calculated number, the measurement and its stated uncertainty.",
    links: [
      { href: "/predictions", label: "Read the complete frozen register" },
      { href: "/empirical-audit", label: "Compare selected values with dated observations" },
      { href: "/falsification", label: "Inspect test targets and failure criteria" },
      { href: "/verification/predictions_frozen.json", label: "Inspect the original structured register" },
    ],
  },
  {
    id: "flavor",
    title: "One input, four results",
    question: "Why do four numbers move together?",
    summary: "Move one small input and watch four numbers change. Each follows its own rule, but all four calculations use the same input.",
    steps: [
      {
        title: "Begin with the shared input",
        body: "The construction supplies a small number called the seed. Start at its marked value.",
      },
      {
        title: "Change it once",
        body: "Move the seed slider. All four displayed results are recalculated from that one change.",
      },
      {
        title: "Compare the four responses",
        body: "Each result uses its own rule. The slider shows their dependence; the marked construction value gives the quoted TFPT results.",
      },
    ],
    connection: "The shared input connects particle mixing with the stated cosmic readouts. The detailed mass construction also uses its powers, with additional family rules and coefficients.",
    scope: "Varying the seed compares the stated formulas; the construction itself fixes its seed. A shared input makes the readouts correlated. The boundary phase and baryon density identifications retain their physical conditions, and source mass comparisons retain their scale and scheme.",
    tryThis: "Move the shared seed slider and compare all four numbers. Follow how each responds to the same change.",
    links: [
      { href: "/explain#flavor", label: "Work through the operators and mass ratios" },
      { href: "/explain#budget", label: "Follow the shared matter budget into alpha" },
      { href: "/papers/standard-model", label: "Read the original flavour construction" },
      { href: "/empirical-audit", label: "Inspect the physical mass comparisons" },
    ],
  },
  {
    id: "cosmology",
    title: "Two connected cosmic results",
    question: "How does one input move both results?",
    summary: "In the stated early universe scenario, N measures an interval of expansion. Move it to see the pattern tilt rise while the relative gravitational wave strength falls.",
    steps: [
      {
        title: "Choose the expansion input",
        body: "Set N star between fifty and sixty. It describes the amount of expansion used by the stated early Universe branch.",
      },
      {
        title: "Read the density result",
        body: "The first number describes how the power of early density fluctuations changes with size.",
      },
      {
        title: "Read the wave result",
        body: "The second compares gravitational wave power with density fluctuation power. Both numbers must use the same N star.",
      },
    ],
    connection: "Both results use the same amount of expansion. One calculated curve fixes their positions together.",
    scope: "These readouts belong to the stated R + R² and vacuum branches. N star and reheating remain external inputs, while physical gravity and dimensional scales retain their source assumptions and calibration.",
    tryThis: "Move N star from fifty to sixty. Compare how the two displayed results change together.",
    links: [
      { href: "/explain#inflation", label: "Read the joint inflation relation" },
      { href: "/explain#cosmology", label: "Follow alpha into the vacuum scale" },
      { href: "/predictions#bands", label: "Inspect the conditional inflation bands" },
      { href: "/papers/horizon-readouts", label: "Read the normalization and scale conditions" },
    ],
  },
  {
    id: "quantum",
    title: "Turning a quantum state",
    question: "What changes when the phase turns?",
    summary: "Turn the phase wheel. In this worked state, two outcomes each stay at 50%. Then advance the five and six position clocks to see when they return together.",
    steps: [
      {
        title: "Read the two outcomes",
        body: "This worked state has two equally likely outcomes. Each has probability fifty percent.",
      },
      {
        title: "Turn the common phase",
        body: "A quarter turn changes the state’s common phase. The two probabilities stay at fifty percent through all four turns.",
      },
      {
        title: "Compare two returning clocks",
        body: "Advance the five position and six position clocks together. After thirty steps, both are back at their starting positions.",
      },
    ],
    connection: "The worked state uses the specified mapping from E₈ coordinates. The clock comparison separately shows how finite return counts work.",
    scope: "The finite correspondence requires the stated lattice, compatible complex structure and explicit chart together. It does not by itself implement a physical quantum instrument, universal quantum computation or a clock period in seconds.",
    tryThis: "Press Quarter turn and watch the two probabilities. Then advance the five and six position clocks until both return after thirty steps.",
    links: [
      { href: "/explain#quantum", label: "Explore the finite quantum correspondence" },
      { href: "/explain#clocks", label: "Apply the clock actions" },
      { href: "/documentation?section=section%3A6c4044608163b007c4c2", label: "Read the original quantum dictionary" },
      { href: "/documentation?source=verification%2Fv419_seam_galois_carrier.py", label: "Inspect the explicit Galois action" },
    ],
  },
];
