import { SectionHeader } from "./SectionHeader";

/**
 * The "Rosetta" lexicon: TFPT's discrete-mathematics nomenclature ("compiler",
 * "seam", "deck", "readout", "microcode") mapped heuristically onto standard
 * QFT / mathematical-physics language (Wilsonian RG, path integral, anomalies,
 * index theorems). This is a translation aid for mainstream physicists, not a
 * new claim — every row points to the orthodox concept the TFPT term plays the
 * role of. Recommended by external review (publication-accessibility).
 */
const LEXICON: { term: string; reading: string }[] = [
  {
    term: "Compiler",
    reading:
      "A deterministic boundary → IR map (a fixed renormalization-group endpoint read off by projection), not a parameter fit. ‘Compiles’ = evaluates the unique fixed point.",
  },
  {
    term: "Seam",
    reading:
      "The reflection-positive boundary / holographic screen — a Wilsonian UV boundary CFT (chiral conformal net) whose data the bulk reads off.",
  },
  {
    term: "Carrier (D₅ ⊕ A₃)",
    reading:
      "The boundary field content / chiral algebra: 16 free Majorana fermions, c = 8 = 5 + 3 (a free-fermion conformal net).",
  },
  {
    term: "μ₄ glue / deck",
    reading:
      "An orbifold deck transformation / simple-current (ℤ₄) extension — the standard ‘gauge a discrete symmetry’ / extension operation on a CFT.",
  },
  {
    term: "Clock",
    reading:
      "The Coxeter monodromy element of W(A₃) = S₄ (order h(A₃) = 4) — the orbifold rotation generating the ℤ₄.",
  },
  {
    term: "Audit hull (E₈)",
    reading:
      "An anomaly / consistency lattice — the even unimodular ‘checksum’ that the carrier must embed into. NOT a 4D gauge group (so Coleman–Mandula / Distler–Garibaldi do not apply).",
  },
  {
    term: "Readout / projection",
    reading:
      "An observable extracted as an index or intersection number — the value of an operator after projecting onto the physical sector (a Wilson-line/operator VEV).",
  },
  {
    term: "Microcode",
    reading:
      "The integer charge / index labels (hypercharges, Dynkin indices, Plücker coordinates) — the discrete, RG-invariant quantum numbers.",
  },
  {
    term: "Plücker readout",
    reading:
      "A topological intersection / Schubert index on a Grassmannian — a discrete, scheme-independent number (e.g. cᵤ/c_d = 55/117).",
  },
  {
    term: "Gap (2/3)⁶",
    reading:
      "The spectral gap of the boundary transfer operator = the RG-irrelevance rate of the leading deformation (a Perron–Frobenius subleading eigenvalue).",
  },
  {
    term: "Anchor a = (1,1,2)",
    reading:
      "The minimal generating datum — the role a renormalization scheme’s defining numbers play; its symmetric functions are (|μ₄|, g_car, |ℤ₂|) = (4,5,2).",
  },
  {
    term: "F_transfer",
    reading:
      "The typed RG / threshold-matching functor: compiler source data → physical pole observable, now a runnable solver suite (Koide source→pole v371, η_B Boltzmann v372, axion relic v373, m_p/m_e via QCD/EW v374), each a typed [C] bridge with a kill test, folded into a prediction-observatory CI (v375).",
  },
  {
    term: "v_geo",
    reading:
      "The one dimensionful renormalization condition — a unit choice. After setting ℏ = c = 1 a single scale must still be fixed by hand; the No-Unit Theorem proves a dimensionless compiler cannot produce it.",
  },
  {
    term: "SEAM.EQUIV.01 (keystone)",
    reading:
      "The historical seam/metric keystone: the raw reflection-positive seam state is identified with the holomorphic (E₈)₁ net at τ=i. Its MMST route is [C], closed modulo cited theorems but not solved; the unconditional parent and twistor route remain [O]. The ‘one irreducible postulate’ analogy is scoped to this finite seam/MMST lane, not T1–T8 or a shared 3+1D parent.",
  },
  {
    term: "Rest_TOE / T1–T8",
    reading:
      "The strict physical-completeness matrix, not another name for the finite seam/compiler residual. Round 4 (v1026–v1030) closes only the fixed-M=1, Ny=8 relaxed TEL-B norm below 2.995906 and adds narrow T3/T4/T6–T8 identities/counterbounds. FE-GEN/ALG-EXH, all T1–T8 gates and TFPT.TOE.COMPLETE.01 remain [O], and no shared 3+1D parent exists; v1029 is not a TFPT embedding. The ‘one irreducible postulate’ analogy above is scoped to the historical finite seam/MMST lane.",
  },
];

export function RosettaLexicon() {
  return (
    <section
      id="rosetta"
      className="relative scroll-mt-20 border-t border-slate-200/60 py-20 sm:py-24"
      aria-labelledby="rosetta-heading"
    >
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <SectionHeader
          eyebrow="A translation key"
          title="Compiler-speak → standard physics"
          description="TFPT’s vocabulary comes from discrete mathematics and computer science; a phenomenologist looks for Lagrangians and RG flows. This Rosetta maps each TFPT term onto the orthodox concept it plays the role of — a reading aid, not a new claim."
        />
        <div className="mt-10 overflow-hidden rounded-2xl border border-slate-300/40">
          <table className="w-full border-collapse text-left text-sm">
            <thead>
              <tr className="bg-slate-100/60 text-[11px] uppercase tracking-widest text-blue-700/80">
                <th className="w-1/3 px-4 py-3 font-semibold">TFPT term</th>
                <th className="px-4 py-3 font-semibold">Standard QFT / mathematical reading</th>
              </tr>
            </thead>
            <tbody>
              {LEXICON.map((row, i) => (
                <tr
                  key={row.term}
                  className={i % 2 === 0 ? "bg-slate-50/30" : "bg-slate-100/20"}
                >
                  <td className="px-4 py-3 align-top font-mono text-xs font-semibold text-slate-900">
                    {row.term}
                  </td>
                  <td className="px-4 py-3 align-top leading-relaxed text-slate-700">
                    {row.reading}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p className="mt-5 text-sm leading-relaxed text-slate-600">
          The one honest layer a physicist will scrutinise is{" "}
          <span className="font-mono text-slate-800">F_transfer</span>: the discrete kernel and the
          dimensionless readouts are exact, while the continuous transport that drives the
          source data to the physical pole is the external transfer layer — now a typed, runnable
          solver suite (v371–v375), explicitly{" "}
          <span className="font-mono">[C]</span>, never sold as a derivation.
        </p>
      </div>
    </section>
  );
}
