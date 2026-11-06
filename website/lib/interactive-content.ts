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
    title: "The whole construction",
    question: "How do the different parts of TFPT fit together?",
    summary: "Follow one connected route from a specified boundary source to internal structure, numerical readouts and consistency checks. At each connection, inspect the operation that carries information into the next calculation.",
    steps: [
      {
        title: "Start with the source and its marked geometry",
        body: "The boundary source carries its kernel, state and time. In the stated geometric reduction, four marked points define one divisor: its cycle space has rank three and its meromorphic function space has dimension five.",
      },
      {
        title: "Build the carrier, family and lattice",
        body: "The marked five slot carrier gives sixteen even exterior states. The D₅ carrier and A₃ family lattices join to E₈. Their specified operators then supply charge assignments, clock actions and inputs to a shared small seed.",
      },
      {
        title: "Follow the readouts and check the return path",
        body: "The shared structure enters the alpha equation, flavour relations and conditional cosmological readouts. Compare these outputs with the original inputs and with observations. The return checks constrain consistency within the framework; they do not generate the framework from nothing.",
      },
    ],
    connection: "The chapters share objects and maps: the same carrier, family geometry, lattice norms and seed reappear in different calculations.",
    scope: "Exact mathematics, numerical readouts and physical identifications retain their own premises. Complete transports of a supplied source are available in their scopes; evaluating the full original interacting physical source and its spectrum remains a separate common task.",
    tryThis: "Follow one route from the four marks through E₈ to alpha. At each connection, identify which object or operation is carried forward.",
    links: [
      { href: "/explain", label: "Work through the connected explanation" },
      { href: "/architecture", label: "Inspect the system map and dependencies" },
      { href: "/explain#source", label: "Read the common source route" },
      { href: "/papers/introduction", label: "Open the original reading guide" },
    ],
  },
  {
    id: "alpha",
    title: "The fine structure constant",
    question: "Why does the equation give a number near 137?",
    summary: "Alpha measures electromagnetic interaction strength. The stated TFPT response equation has one positive simple root, whose reciprocal is approximately 137.03599921684.",
    steps: [
      {
        title: "Identify the inputs to the response",
        body: "Begin with the boundary normalization, the D₅ norm of five quarters, the admissible count of forty eight and the matter budget of forty one. Together they define the particular seam response used in the equation.",
      },
      {
        title: "Locate the unique crossing",
        body: "The closure balances cubic and quadratic terms against a logarithmic response that also depends on alpha. The analytic convexity proof gives one positive crossing; the interval calculation locates it numerically.",
      },
      {
        title: "Compare the same physical quantity",
        body: "Take the reciprocal of the root and compare it with the dated low energy alpha measurement, including its uncertainty. A value at another energy requires the appropriate running and matching convention.",
      },
    ],
    connection: "The five quarters comes from the E₈ glue, while the matter budget connects the charge and flavour constructions to the same response equation.",
    scope: "Uniqueness is a theorem for the fixed response and every positive budget. Selecting the physical budget and identifying the full local electromagnetic variation with the renormalized Thomson coupling require the original source and observable map.",
    tryThis: "Move alpha across the root and compare the sign of the closure on either side of the crossing.",
    links: [
      { href: "/fine-structure-constant", label: "Follow the coefficients and their provenance" },
      { href: "/research/alpha-fixed-point-proof", label: "Read the global positive root proof" },
      { href: "/empirical-audit", label: "Inspect dated measurement comparisons" },
    ],
  },
  {
    id: "standard-model",
    title: "One family of matter",
    question: "How do five slots organize matter?",
    summary: "Three colour slots and two weak slots form the marked carrier. Its even selections give sixteen components, organized into six quark and lepton sectors with additive charges.",
    steps: [
      {
        title: "Make an even selection",
        body: "Keep selections of zero, two or four of the five slots. There are one, ten and five choices respectively. In the specified Clifford action, these sixteen states form the D₅ half spinor.",
      },
      {
        title: "Add the occupied slot charges",
        body: "Each colour slot contributes hypercharge minus one third and each weak slot contributes plus one half. One of each gives the quark doublet hypercharge of one sixth. Weak isospin then separates its two electric charges.",
      },
      {
        title: "Check the whole charge spectrum",
        body: "Read all six sectors, their multiplicities and their conjugate field convention. The complete Weyl spectrum has cancelling gauge anomaly coefficients. This tests the consistency of the given representation and charge assignment.",
      },
    ],
    connection: "The carrier supplies the D₅ side of the lattice join and the matter charge traces used by the electromagnetic budget. Its three colour slots are distinct from the three family directions.",
    scope: "The charge reader assumes the marked carrier, normalized hypercharge and even exterior representation. Anomaly cancellation checks that spectrum; a full interacting chiral realization also requires its physical fields, source and continuum construction.",
    tryThis: "Select one colour slot and one weak slot. Then exchange the weak slot and compare the two electric charges.",
    links: [
      { href: "/e8-standard-model#carrier", label: "Operate on the carrier and read its charges" },
      { href: "/explain#matter", label: "Follow the gauge structure and anomaly calculation" },
      { href: "/three-fermion-generations", label: "See where the family index enters" },
      { href: "/papers/standard-model", label: "Read the Standard Model paper" },
    ],
  },
  {
    id: "e8",
    title: "The E₈ lattice",
    question: "How do two lattices become E₈?",
    summary: "A lattice is a regular pattern of points. In E₈, the 240 shortest nonzero vectors from the origin are called roots. This construction joins the carrier and family lattices to build that pattern.",
    steps: [
      {
        title: "Compare the two discriminant forms",
        body: "Both discriminant groups are cyclic of order four. The selected generator norms are five quarters and three quarters. Their sum is two, allowing the diagonal glue subgroup to have even norm.",
      },
      {
        title: "Inspect the four root classes",
        body: "The direct sum contributes fifty two roots. The other three matched cosets add sixty, sixty four and sixty four. Read an actual eight coordinate vector in each class and check that its squared length is two.",
      },
      {
        title: "Check the lattice certificate",
        body: "The extension has index four, dividing the product of the two determinants by sixteen. The resulting determinant is one. Positive definiteness, evenness and rank eight identify E₈, with 240 roots and Lie algebra dimension 248.",
      },
    ],
    connection: "The lattice join uses the carrier and family together. Its discriminant norms also enter the specified boundary response; the eight lattice directions remain internal mathematical data.",
    scope: "This is a lattice theorem for the stated D₅ and A₃ inputs and their compatible glue. Identifying its representations and operators with a physical field theory requires the corresponding field and source dictionary.",
    tryThis: "Select each glue class and compare its root coordinates, squared length and contribution to the total of 240.",
    links: [
      { href: "/e8-standard-model#glue", label: "Build the four root classes" },
      { href: "/research/e8-discriminant-glue", label: "Read the discriminant argument" },
      { href: "/research/four-mark-divisor", label: "Trace the carrier and family to the same divisor" },
    ],
  },
  {
    id: "dynamics",
    title: "Dynamics and time",
    question: "What changes when the system evolves?",
    summary: "A finite transfer can relax toward a stationary direction while other modes decay. Clock actions, this relaxation and coherent quantum evolution describe different operations that must be related through the stated source.",
    steps: [
      {
        title: "Follow the transfer modes",
        body: "The specified family transfer has eigenvalues one, two thirds to the sixth power and one third to the sixth power. Repeated steps preserve the stationary direction while suppressing the other two modes.",
      },
      {
        title: "Separate relaxation from a clock cycle",
        body: "A finite clock returns after a stated number of actions. A decaying transfer mode instead approaches its limit. Coherent unitary evolution changes amplitudes and phases; it is a different operation from applying a positive contraction.",
      },
      {
        title: "Return to the common source",
        body: "The original reconstruction uses the full field correlations and reflection positivity to build a state space and positive energy time together. The operational source already includes its state and time; the physical application keeps the common field map and its hypotheses.",
      },
    ],
    connection: "The clock chapter follows finite symmetry actions. This chapter asks how transfer modes evolve and how those operations connect to the source’s time and field dynamics.",
    scope: "The stated transfer spectrum establishes relaxation for that operator. It neither supplies the full interacting physical Hamiltonian nor assigns seconds to an internal step; the physical source, spectrum and dimensional calibration must support that interpretation.",
    tryThis: "Follow a nonstationary mode through repeated transfer steps, then compare its shrinking amplitude with a clock action that returns to its start.",
    links: [
      { href: "/explain#source", label: "Follow the source, state and time reconstruction" },
      { href: "/explain#clocks", label: "Compare the different clock actions" },
      { href: "/results?record=finding%3Aoriginal-genesis-family-transfer-not-carroll-cycle", label: "Read the family transfer and physical period distinction" },
      { href: "/papers/origin-theory", label: "Read the original transfer argument" },
    ],
  },
  {
    id: "predictions",
    title: "Predictions and tests",
    question: "What can the theory put to the test?",
    summary: "The register frozen on 9 June 2026 contains sixteen main values, two assigned textures and two conditional bands. Each entry keeps its formula, conditions and stated failure criterion.",
    steps: [
      {
        title: "Read the registered statement",
        body: "Choose one observable and inspect its frozen formula, value and conditions. The two assigned textures and two conditional bands have their own categories. The two diagnostic variants are recorded separately from the main predictions.",
      },
      {
        title: "Match the measurement convention",
        body: "Compare the same quantity at the stated scale, in the same units and mass or coupling convention. Keep the observation date and quoted uncertainty visible. Shared formula inputs also mean that several outputs can be correlated.",
      },
      {
        title: "Apply the stated test",
        body: "Read what outcome would exclude the particular formula or physical interpretation. Separate a comparison with data already known when the formula was written from a test against a later observation. Registration preserves that chronology.",
      },
    ],
    connection: "The register collects readouts from alpha, flavour, neutrino, scale and cosmological branches. The common construction explains their dependencies; the empirical audit compares selected outputs with dated measurements.",
    scope: "The register records commitments and categories. Its count is not a count of independent experimental confirmations, and freezing a formula after a quantity was measured does not make that comparison a blind prediction.",
    tryThis: "Choose one registered value, find its physical conditions and failure criterion, then compare it with the corresponding dated measurement.",
    links: [
      { href: "/predictions", label: "Read the complete frozen register" },
      { href: "/empirical-audit", label: "Compare selected values with dated observations" },
      { href: "/falsification", label: "Inspect test targets and failure criteria" },
      { href: "/verification/predictions_frozen.json", label: "Inspect the original structured register" },
    ],
  },
  {
    id: "flavor",
    title: "Flavour and the shared seed",
    question: "Why do the readouts move together?",
    summary: "A common small seed enters the Cabibbo angle, a reactor mixing readout, a boundary phase and a baryon density reading. Changing that seed shows how these specified formulas move together; the charged mass construction also uses its powers.",
    steps: [
      {
        title: "Begin with the common seed",
        body: "The boundary normalization and the admissible count give a seed of approximately 0.053172. Use its stated value as the starting point, then vary it to see which outputs share that input.",
      },
      {
        title: "Follow four responses to one change",
        body: "The Cabibbo readout takes the square root of the seed times one minus the seed. The reactor mixing readout multiplies the seed by a fixed exponential. The boundary phase and baryon density formulas are also proportional to the seed, with their stated physical conditions.",
      },
      {
        title: "Continue into masses and physical comparisons",
        body: "The charged flavour branch adds family operators, transport residues, windings and response coefficients to powers of the same seed. Its source mass ratios require the corresponding physical reader, scale and mass scheme for comparison with measurements.",
      },
    ],
    connection: "Flavour reuses the family geometry and boundary seed. Its specified operators also meet the alpha budget through actual identities, rather than through a coincidental repeated number.",
    scope: "Varying the seed compares the stated formulas; the construction itself fixes its seed. A shared input makes the readouts correlated. The boundary phase and baryon density identifications retain their physical conditions, and source mass comparisons retain their scale and scheme.",
    tryThis: "Move the seed slider and compare the four readouts. Return to the construction value and follow the source links to each formula and its physical conditions.",
    links: [
      { href: "/explain#flavor", label: "Work through the operators and mass ratios" },
      { href: "/explain#budget", label: "Follow the shared matter budget into alpha" },
      { href: "/papers/standard-model", label: "Read the original flavour construction" },
      { href: "/empirical-audit", label: "Inspect the physical mass comparisons" },
    ],
  },
  {
    id: "cosmology",
    title: "Cosmology and scales",
    question: "How do the cosmic readouts connect?",
    summary: "The stated inflation branch puts two observables on one curve. Its mass and vacuum density formulas express dimensionless scale ratios using the boundary normalization and the alpha root.",
    steps: [
      {
        title: "Move along the inflation curve",
        body: "In the specified R + R² branch, N star gives the expansion history input used by both observables. The spectral tilt is one minus two divided by N star; the tensor ratio is twelve divided by its square. Change N star from fifty to sixty and follow both outputs together.",
      },
      {
        title: "Read the scale ratios",
        body: "The scalaron mass relative to the reference scale is the seventh half power of the boundary normalization. The stated vacuum branch uses an exponential of minus twice the inverse alpha, together with its residue factor. These formulas compare scales without assigning units.",
      },
      {
        title: "Keep the gravitational interpretation attached",
        body: "The inverse boundary normalization is eight pi, matching the coefficient used in the conditional Einstein normalization route. Applying that route retains its geometric and field assumptions. A mass in GeV or a duration in seconds also needs a dimensional calibration.",
      },
    ],
    connection: "The inflation observables share N star. The scale formulas reuse the boundary normalization and alpha, connecting the cosmic branches to the same internal construction.",
    scope: "These readouts belong to the stated R + R² and vacuum branches. N star and reheating remain external inputs, while physical gravity and dimensional scales retain their source assumptions and calibration.",
    tryThis: "Move N star between fifty and sixty. Compare how the spectral tilt and tensor ratio travel along the same curve, then inspect the separate scale ratios.",
    links: [
      { href: "/explain#inflation", label: "Read the joint inflation relation" },
      { href: "/explain#cosmology", label: "Follow alpha into the vacuum scale" },
      { href: "/predictions#bands", label: "Inspect the conditional inflation bands" },
      { href: "/papers/horizon-readouts", label: "Read the normalization and scale conditions" },
    ],
  },
  {
    id: "quantum",
    title: "Quantum structure and clocks",
    question: "How do quantum states and clocks connect?",
    summary: "The named mapping turns eight real coordinates into four normalized complex amplitudes for two qubits. Their squared magnitudes give four outcome probabilities. A quarter turn changes the common phase and leaves these probabilities unchanged.",
    steps: [
      {
        title: "Build the finite quantum dictionary",
        body: "With the compiler compatible complex structure, the Gaussian lattice quotient has sixteen classes. In the named chart, the sixty rays are arranged into fifteen orthogonal four ray contexts, matching the stated two qubit stabilizer geometry.",
      },
      {
        title: "Act on the clock labels",
        body: "The quarter action doubles labels modulo five. Its multipliers run through one, two, four and three before returning to one. It therefore changes a five cycle by an order four action, without being a segment of that cycle.",
      },
      {
        title: "Keep the other clock actions distinct",
        body: "The five and six structures meet in the order thirty Coxeter data. Separately, the named G₃₁ compiler combines the quarter and family actions in its order twelve operator. Their explicit actions determine their relationships.",
      },
    ],
    connection: "The finite quantum dictionary and clock operators use the specified E₈ and complex structure. Their relation to relaxation and source time belongs to the separate dynamics path.",
    scope: "The finite correspondence requires the stated lattice, compatible complex structure and explicit chart together. It does not by itself implement a physical quantum instrument, universal quantum computation or a clock period in seconds.",
    tryThis: "Apply the quarter action four times and track the five cycle labels. Compare the returned labels with the separate order thirty and order twelve actions.",
    links: [
      { href: "/explain#quantum", label: "Explore the finite quantum correspondence" },
      { href: "/explain#clocks", label: "Apply the clock actions" },
      { href: "/documentation?section=section%3A6c4044608163b007c4c2", label: "Read the original quantum dictionary" },
      { href: "/documentation?source=verification%2Fv419_seam_galois_carrier.py", label: "Inspect the explicit Galois action" },
    ],
  },
];
