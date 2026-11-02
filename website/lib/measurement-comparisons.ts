import "server-only";
import { predictionById } from "./frozen-predictions";

export const measurementCheckedDate = "2 November 2026";
type DatedComparison = {
 id: string; title: string; shortTitle: string; symbol: string; explanation: string;
 central: string; uncertaintyMinus: string; uncertaintyPlus?: string; measured: string;
 date: string; meaning: string; source: string; href: string; history: string;
};
const datedComparisons: DatedComparison[] = [
  {
    id: "ALPHA_INV", central: "137.035999177", uncertaintyMinus: "0.000000021", shortTitle: "Electromagnetic coupling", symbol: "α⁻¹", explanation: "The strength of the electromagnetic interaction.", title: "Inverse fine structure constant", measured: "137.035999177 ± 0.000000021",
    date: "CODATA 2022 adjustment", meaning: "The difference uses the CODATA standard uncertainty alone. It is a numerical comparison, not a combined theory significance or a derivation of the physical coupling.",
    source: "NIST: 2022 CODATA constants", href: "https://physics.nist.gov/cuu/Constants/Table/allascii.txt",
    history: "The CODATA adjustment predates the registry freeze.",
  },
  {
    id: "SIN2_THETA12_SEED", central: "0.3036", uncertaintyMinus: "0.0064", shortTitle: "Solar neutrino mixing", symbol: "sin² θ₁₂", explanation: "How neutrinos mix between the first two states.", title: "Solar neutrino mixing, sin² θ₁₂", measured: "0.3036 ± 0.0064",
    date: "JUNO 207.2 live days; collaboration preprint, 29 September 2026",
    meaning: "This comparison uses the normal mass ordering result. The precision does not distinguish the conditional TFPT value from the measured interval.",
    source: "JUNO Collaboration: 207.2 day oscillation analysis", href: "https://arxiv.org/abs/2609.37895",
    history: "The cited collaboration preprint appeared on 29 September 2026. The earlier 59.1 day result, 0.3092 ± 0.0087, was already public on 18 November 2025, before the registry freeze. A prospective test must be assessed against the first public disclosure of the tested value, not its journal date alone.",
  },
  {
    id: "SIN2_THETA13", central: "0.02249", uncertaintyMinus: "0.00057", shortTitle: "Reactor neutrino mixing", symbol: "sin² θ₁₃", explanation: "A smaller angle in the neutrino mixing pattern.", title: "Reactor neutrino mixing, sin² θ₁₃", measured: "0.02249 ± 0.00057",
    date: "NuFIT 6.1, November 2025 data; normal ordering, IC23 without SK atmospheric data",
    meaning: "The selected fit is stated explicitly because the result depends on ordering and the data combination. The older approximate two sigma label is not used for this comparison.",
    source: "NuFIT 6.1 parameter table", href: "https://www.nu-fit.org/sites/default/files/v61.tbl-parameters.pdf",
    history: "The global fit predates the registry freeze and shares neutrino data with other comparison rows.",
  },
  {
    id: "BETA_BIREFRINGENCE_DEG", central: "0.215", uncertaintyMinus: "0.074", shortTitle: "Cosmic polarization rotation", symbol: "β", explanation: "A conditional rotation of the polarization of ancient light.", title: "Cosmic birefringence, β", measured: "0.215° ± 0.074°",
    date: "ACT DR6 analysis, submitted 17 September 2025; revised 14 April 2026",
    meaning: "The authors retain unresolved instrumental systematics. The published analysis does not establish a cosmological detection or identify a TFPT mechanism.",
    source: "Diego Palazuelos and Komatsu: ACT DR6", href: "https://arxiv.org/abs/2509.13654",
    history: "This constant rotation comparison is distinct from later searches for anisotropic or time dependent birefringence.",
  },
  {
    id: "LAMBDA_C", central: "0.22517", uncertaintyMinus: "0.00068", shortTitle: "Cabibbo quark mixing", symbol: "sin θ₁₂", explanation: "The main angle governing mixing between quark families.",
    title: "Cabibbo quark mixing, sin θ₁₂", measured: "0.22517 ± 0.00068", date: "PDG 2026, CKM review, equation 12.28; issued 1 June 2026",
    meaning: "The global fit reports the standard mixing angle directly. This is not an approximation using the matrix element |Vus|.",
    source: "Particle Data Group 2026: CKM review, Eq. 12.28", href: "https://pdg.lbl.gov/2026/reviews/rpp2026-rev-ckm-matrix.pdf#page=13",
    history: "The global fit predates the registry freeze. Its CKM parameters have shared fit correlations.",
  },
  {
    id: "S23_CKM", central: "0.04189", uncertaintyMinus: "0.00069", uncertaintyPlus: "0.00081", shortTitle: "Second quark mixing angle", symbol: "sin θ₂₃", explanation: "Mixing between the second and third quark families.",
    title: "Quark mixing, sin θ₂₃", measured: "0.04189 +0.00081 / −0.00069", date: "PDG 2026, CKM review, equation 12.28; issued 1 June 2026",
    meaning: "The comparison uses the upper fit uncertainty because the frozen value lies above the central value. The error is asymmetric.",
    source: "Particle Data Group 2026: CKM review, Eq. 12.28", href: "https://pdg.lbl.gov/2026/reviews/rpp2026-rev-ckm-matrix.pdf#page=13",
    history: "The global fit predates the registry freeze. Its CKM parameters have shared fit correlations.",
  },
  {
    id: "S13_CKM", central: "0.003763", uncertaintyMinus: "0.000083", uncertaintyPlus: "0.000088", shortTitle: "Smallest quark mixing angle", symbol: "sin θ₁₃", explanation: "The small mixing between the first and third quark families.",
    title: "Quark mixing, sin θ₁₃", measured: "0.003763 +0.000088 / −0.000083", date: "PDG 2026, CKM review, equation 12.28; issued 1 June 2026",
    meaning: "The comparison uses the upper fit uncertainty because the frozen value lies above the central value. The close central values do not provide an independent fit probability.",
    source: "Particle Data Group 2026: CKM review, Eq. 12.28", href: "https://pdg.lbl.gov/2026/reviews/rpp2026-rev-ckm-matrix.pdf#page=13",
    history: "The global fit predates the registry freeze. Its CKM parameters have shared fit correlations.",
  },
  {
    id: "DELTA_CKM_RAD", central: "1.154", uncertaintyMinus: "0.025", shortTitle: "Quark CP violation phase", symbol: "δCKM (rad)", explanation: "The phase entering quark CP violation.",
    title: "Quark CP phase, δ (radians)", measured: "1.154 ± 0.025 rad", date: "PDG 2026, CKM review, equation 12.28; issued 1 June 2026",
    meaning: "The frozen TFPT formula is explicitly a leading order holonomy readout. Its subleading theory correction is not quantified here; the displayed distance uses only the fit uncertainty.",
    source: "Particle Data Group 2026: CKM review, Eq. 12.28", href: "https://pdg.lbl.gov/2026/reviews/rpp2026-rev-ckm-matrix.pdf#page=13",
    history: "The global fit predates the registry freeze. Its CKM parameters have shared fit correlations.",
  },
  {
    id: "OMEGA_B", central: "0.04821", uncertaintyMinus: "0.00033", shortTitle: "Ordinary matter fraction", symbol: "Ωb", explanation: "The cosmic density fraction in ordinary baryonic matter.",
    title: "Baryon density fraction, Ωb", measured: "0.04821 ± 0.00033", date: "ACT DR6 ΛCDM analysis, revised 24 June 2025; Table 5, P-ACT-LB2 (DESI DR2)",
    meaning: "This uses the directly reported derived Ωb posterior, rather than Ωb h². It is conditional on the named ΛCDM model and P-ACT-LB2 data combination. The frozen value is above its central value by 2.21 stated uncertainties.",
    source: "ACT DR6 power spectra and ΛCDM parameters, Table 5", href: "https://arxiv.org/pdf/2503.14452#page=31",
    history: "The data combination predates the registry freeze. Its cosmological parameters are correlated. The alternative DESI DR1 column gives a different comparison and is not substituted here.",
  },
  {
    id: "RHOL_OVER_MBAR4", central: String(8 * Math.PI * 2.846e-122), uncertaintyMinus: String(8 * Math.PI * .076e-122), shortTitle: "Vacuum energy density", symbol: "ρΛ / M̄⁴", explanation: "The small vacuum energy density relative to the reduced Planck scale.",
    title: "Vacuum energy density, ρΛ / M̄⁴", measured: "(7.153 ± 0.191) × 10⁻¹²¹", date: "Planck 2018 VI, §3.2, after Eq. 13; final revision 9 August 2021",
    meaning: "Planck gives Λ / m_Pl² = (2.846 ± 0.076) × 10⁻¹²². With M̄ = m_Pl / √(8π) and ρΛ = Λ M̄², multiplying by 8π gives this density in the same reduced Planck convention as the frozen output. The comparison retains flat ΛCDM, the physical branch and dimensional calibration premises.",
    source: "Planck 2018 VI: cosmological parameters, §3.2, after Eq. 13", href: "https://arxiv.org/abs/1807.06209",
    history: "The Planck value predates the registry freeze. The TFPT vacuum readout reuses the alpha root, so these are correlated theoretical outputs.",
  },
];

export const measurementComparisons = datedComparisons.map(row => {
 const predicted = Number(predictionById(row.id).frozen_value);
 const measured = Number(row.central);
 const difference = predicted - measured;
 const uncertainty = Number(difference >= 0 ? (row.uncertaintyPlus || row.uncertaintyMinus) : row.uncertaintyMinus);
 const sigma = difference / uncertainty;
 const relative = difference / measured;
 const relativeLabel = Math.abs(relative) < 1e-7
   ? `${(Math.abs(relative) * 1e9).toFixed(2)} parts per billion`
   : `${(Math.abs(relative) * 100).toFixed(Math.abs(relative) < .01 ? 3 : 2)}%`;
 const scopeShort: Record<string,string> = {
 ALPHA_INV: "Specified equation; physical transfer has its own premises",
 SIN2_THETA12_SEED: "Conditional solar texture",
 SIN2_THETA13: "Specified neutrino readout",
 BETA_BIREFRINGENCE_DEG: "Conditional phase; instrumental systematics remain",
 LAMBDA_C: "Standard angle; correlated global fit",
 S23_CKM: "Standard angle; asymmetric fit uncertainty",
 S13_CKM: "Standard angle; asymmetric fit uncertainty",
 DELTA_CKM_RAD: "Leading order; theory correction unquantified",
 OMEGA_B: "Flat ΛCDM; P-ACT-LB2 with DESI DR2",
 RHOL_OVER_MBAR4: "Conditional branch; matched reduced Planck units",
 };
 return { ...row, predicted, sigma, relative, relativeLabel, scopeShort: scopeShort[row.id],
  result: `${Math.abs(sigma).toFixed(2)} measurement standard uncertainties ${sigma >= 0 ? "above" : "below"} the central value` };
});
export type MeasurementComparison = (typeof measurementComparisons)[number];
export function signedSigma(value: number) { return `${value < 0 ? "−" : "+"}${Math.abs(value).toFixed(2)}`; }
export function comparisonFor(id: string) {
 const row = measurementComparisons.find(c => c.id === id);
 if (!row) throw new Error(`Missing measurement comparison: ${id}`);
 return row;
}
