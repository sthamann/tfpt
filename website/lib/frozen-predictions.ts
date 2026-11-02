import "server-only";
import { readingNumber } from "./format-number";
import { readFileSync } from "node:fs";
import { join } from "node:path";

export type FrozenPrediction = {
  id: string;
  observable: string;
  formula: string;
  frozen_value?: string;
  layer?: string;
  conditional_on?: string | null;
  experiment?: string;
  kill_criterion?: string;
  band_min?: string;
  band_max?: string;
};
export type FrozenVariant = { id: string; formula: string; value: string; note: string };
type FrozenRegistry = {
  registry: string;
  freeze_date: string;
  policy: string;
  predictions: FrozenPrediction[];
  assigned_texture_values: FrozenPrediction[];
  conditional_bands: FrozenPrediction[];
  derived_variants_not_predictions: FrozenVariant[];
};

// Preserve the registry's exact strings. Display labels below are navigation aids.
export const frozenRegistry = JSON.parse(
  readFileSync(join(process.cwd(), "public/research/predictions-frozen.json"), "utf8"),
) as FrozenRegistry;

export const predictionGroups = [
  { id: "electromagnetism", title: "Electromagnetism and cosmic rotation", ids: ["ALPHA_INV", "BETA_BIREFRINGENCE_DEG"], topic: "validation" },
  { id: "mixing", title: "Particle mixing", ids: ["SIN2_THETA12_SEED", "SIN2_THETA13", "LAMBDA_C", "S23_CKM", "S13_CKM", "DELTA_CKM_RAD"], topic: "flavor" },
  { id: "masses", title: "Relative particle masses", ids: ["MMU_OVER_MTAU", "ME_OVER_MMU", "MU_OVER_MD", "MC_OVER_MS", "MT_OVER_MB"], topic: "flavor" },
  { id: "cosmology", title: "Cosmological readouts", ids: ["OMEGA_B", "MSCAL_OVER_MBAR", "RHOL_OVER_MBAR4"], topic: "cosmology" },
] as const;

const labels: Record<string, string> = {
  ALPHA_INV: "Inverse fine structure constant, α⁻¹",
  BETA_BIREFRINGENCE_DEG: "Cosmic birefringence, β (degrees)",
  SIN2_THETA12_SEED: "Solar neutrino mixing, sin² θ₁₂",
  SIN2_THETA13: "Reactor neutrino mixing, sin² θ₁₃",
  LAMBDA_C: "Cabibbo mixing, λC",
  S23_CKM: "Quark mixing, s₂₃",
  S13_CKM: "Quark mixing, s₁₃",
  DELTA_CKM_RAD: "Quark CP phase, δ (radians)",
  MMU_OVER_MTAU: "Muon to tau source mass ratio",
  ME_OVER_MMU: "Electron to muon source mass ratio",
  MU_OVER_MD: "Up to down quark mass ratio",
  MC_OVER_MS: "Charm to strange quark mass ratio",
  MT_OVER_MB: "Top to bottom quark mass ratio",
  OMEGA_B: "Baryon density, Ωb",
  MSCAL_OVER_MBAR: "Scalaron mass ratio, Mscal / M̄",
  RHOL_OVER_MBAR4: "Vacuum energy density, ρΛ / M̄⁴",
  DELTA_CP_NU_DEG: "Neutrino CP phase (degrees)",
  SIN2_THETA23: "Atmospheric neutrino mixing, sin² θ₂₃",
  R_TENSOR: "Tensor to scalar ratio, r",
  N_S: "Spectral tilt, ns",
  SIN2_THETA12_SEAM: "Leading epsilon solar texture variant",
  SIN2_THETA12_NONLIN: "Nonlinear solar texture variant",
};
export function predictionLabel(id: string) { return labels[id] || id; }
export function predictionById(id: string) {
  const row = frozenRegistry.predictions.find((entry) => entry.id === id);
  if (!row) throw new Error(`Missing frozen prediction: ${id}`);
  return row;
}
export function shortFrozenValue(row: FrozenPrediction) {
  if (row.band_min && row.band_max) return `${readingNumber(row.band_min,5)} to ${readingNumber(row.band_max,5)}`;
  return row.frozen_value ? readingNumber(row.frozen_value, row.id === "ALPHA_INV" ? 13 : 7) : "Not specified";
}
