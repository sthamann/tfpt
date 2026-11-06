/**
 * Release metadata for the published PDFs. The version, release date, byte
 * size, and SHA-256 hash are written here so reviewers can verify integrity
 * and tell two snapshots apart without opening the file.
 *
 * To regenerate these values after a re-build:
 *
 *   npm run release:write   (rewrites bytes + sha256 in place)
 *
 * which invokes scripts/release-hashes.mjs against website/public.
 */

export interface ReleaseAsset {
  /** Path under /public, including the leading slash. */
  href: string;
  /** Series version this snapshot was built against. */
  version: string;
  /** ISO-8601 release date for the artifact. */
  releaseDate: string;
  /** Byte size of the PDF (raw bytes). */
  bytes: number;
  /** SHA-256 hash of the PDF, lowercase hex. */
  sha256: string;
  /** Optional changelog entry — short, one-line. */
  changelog?: string;
}

const COMMON = {
  version: "TFPT 5.4",
  releaseDate: "2026-11-06",
};

export const RELEASE_ASSETS: Record<string, ReleaseAsset> = {
  "/papers/introduction_guide.pdf": {
    href: "/papers/introduction_guide.pdf",
    ...COMMON,
    bytes: 1049686,
    sha256: "9a827699fc5d3487da752ea0443f585d6ecffeb20b105a951d12ff08cad926cd",
    changelog: "Core chapters of the original introduction; the computational appendix and history remain in the complete edition.",
  },
  "/papers/verification_catalog.pdf": {
    href: "/papers/verification_catalog.pdf",
    ...COMMON,
    bytes: 1493381,
    sha256: "a91c636b49a6bd2019a2e5aedb7f6ae85ca88f13dcdc18eadcc1bc790fbc2fca",
    changelog: "Standalone reference index of registered verification modules and their stated checks.",
  },
  "/papers/introduction.pdf": {
    href: "/papers/introduction.pdf",
    ...COMMON,
    bytes: 3639402,
    sha256:
      "bd629972952e625f47914fe4d2437aa8e3d90c4100496301785a3f052fb280a1",
    changelog:
      "Compiler-closure reading guide: two axioms, the dependency DAG, the predictions and the proof ledger.",
  },
  "/papers/tfpt_1_architecture_e8.pdf": {
    href: "/papers/tfpt_1_architecture_e8.pdf",
    ...COMMON,
    bytes: 1431103,
    sha256:
      "859440023a75d9ad630cb5fad9e96bb9a89d6f7678ab81642be9769c80968e9e",
    changelog:
      "Architecture: the two axioms, the D₅ × A₃ → E₈ construction, and the EM fixed point with existence + uniqueness.",
  },
  "/papers/tfpt_2_standard_model.pdf": {
    href: "/papers/tfpt_2_standard_model.pdf",
    ...COMMON,
    bytes: 1423780,
    sha256:
      "639a72170dc6977a866e056d8888ca3251bd71f5c52018b208567f5d6e7e2066",
    changelog:
      "The Standard Model in one φ₀-ladder, the flavor residue matrix, and the derived solar angle θ₁₂.",
  },
  "/papers/tfpt_3_e8_audit_bootstrap.pdf": {
    href: "/papers/tfpt_3_e8_audit_bootstrap.pdf",
    ...COMMON,
    bytes: 1372063,
    sha256:
      "8e069dc9aba7e2f3b17b21f5ff7e83076acbd43dfb61e2f9b09633af2e0e9a93",
    changelog:
      "The seven E₈ slices as an audit raster, the cascade bridge, and the Möbius bootstrap.",
  },
  "/papers/tfpt_4_frontier.pdf": {
    href: "/papers/tfpt_4_frontier.pdf",
    ...COMMON,
    bytes: 945778,
    sha256:
      "2bd91460398b2ffa14654408801d6078cc2c6698e923457a459f44e1e3e485ac",
    changelog:
      "Honest status of η_B, m_p/m_e, Koide, dark matter and full quantum gravity — not forced onto the ladder.",
  },
  "/papers/tfpt_horizon_readouts.pdf": {
    href: "/papers/tfpt_horizon_readouts.pdf",
    ...COMMON,
    bytes: 936079,
    sha256:
      "3ba5be01adc4868461ba69db5e6de22a733f854d1d6b0979d7c74c3962817e5a",
    changelog:
      "Appendix H — the horizon unit system: c₃ = 1/(8π) as the universal horizon thermal code.",
  },
  "/papers/origin_theory.pdf": {
    href: "/papers/origin_theory.pdf",
    ...COMMON,
    bytes: 1236565,
    sha256:
      "6c97f961f655c876b94681376fb634a7d321edd67935f758d69e5e2b57d1d222",
    changelog:
      "Origin Theory: the (5,3) skeleton, the triply-forced 8, the order-30 Coxeter cycle, and the gapped unique attractor.",
  },
  "/papers/tfpt_research_contracts.pdf": {
    href: "/papers/tfpt_research_contracts.pdf",
    ...COMMON,
    bytes: 2406175,
    sha256:
      "58f7fb30442c170af1e232850b06331dc75015eeb94810dc8229479b6528ad98",
    changelog:
      "Research contracts separate compiler Rest = v_geo ⊕ G_net ⊕ F_transfer from Rest_TOE. Round 4 (v1026–v1030) closes the relaxed TEL-B norm at fixed M=1, Ny=8: ||R_N||HS < 2.995906 < 3 for every even N≥16, with the former CF/DG estimates discharged for this bound by native v1026 using v1022/v1025. It also adds narrow T3/T4/T6–T8 identities and counterbounds, but closes no T-gate: FE-GEN/ALG-EXH, T1–T8, TFPT.TOE.COMPLETE.01 and the shared complete 3+1D parent remain [O]. The v1029 tensor target requires global zero-mode removal and is not a TFPT embedding. Round 7 (v1031–v1035; 233 typed checks) adds full free quantum/covariant curvature proofs, auxiliary charged corners, the factorized mirror bound and prescribed-source Ward identities. Microscopic TFPT emergence and universal nonlinear interaction remain open; v1033/v1034 require full repository sources. Wave 4: v998–v1001 + lattice-fundamental quasilocal-family amendment + ALPHA relative-det note.",
  },
  "/papers/tfpt_safeguards.pdf": {
    href: "/papers/tfpt_safeguards.pdf",
    ...COMMON,
    bytes: 619840,
    sha256:
      "e60b4835937eb34019e86944fce46151d140a87b7f930eb2f498191afe1a05de",
    changelog:
      "Safeguards: the verification discipline — the status calculus, no-free-pattern + reverse audit (and v431: the 5/8 'overhead' degrees are the forced two-family ladder 6·spine ⊔ det-ladder, not diffuse slack), the over-determination map (v427) with its honest self-correction (v428: the seven arithmetic witnesses compress one (2,3,5)/E₈ object; the genuine multiplication is the input forced four ways + the foreign α⁻¹) and its unconditional floor (v432: ~10⁻¹⁰ from disjoint pieces only, ~20 orders above the v100 conditional; hardened by v436 to an assumption-minimal 1/94,500 ≈ 4.40σ counting floor with a monotone concession ladder), the firewall + No-Unit theorem, frozen predictions + null model, the independent Wolfram and Lean paths, and the red team.",
  },
  "/papers/tfpt_5_redteam.pdf": {
    href: "/papers/tfpt_5_redteam.pdf",
    ...COMMON,
    bytes: 872084,
    sha256:
      "45eacb7f4868808beef17a2bbcd7735d025d63e526f84056c8f1c49462cf90be",
    changelog:
      "The adversarial audit: Targets A–E, what survives, what each target reduces to, and the kill tests.",
  },
  "/papers/note_e8_gaussian_code.pdf": {
    href: "/papers/note_e8_gaussian_code.pdf",
    ...COMMON,
    bytes: 374396,
    sha256:
      "0483ce5385d5f5ca963560e55409dd6c9296e57f416756f5bcf73849f27433e8",
    changelog:
      "Working note N1 — the Gaussian code bridge: E₈ over ℤ[i] via Construction A over the extended Hamming code, the canonical four-bit quotient L/(1+i)L ≅ F₂⁴, and the G₃₁ quartic companion (v689/v690 + 65 Lean theorems).",
  },
  "/papers/changelog.pdf": {
    href: "/papers/changelog.pdf",
    ...COMMON,
    bytes: 1892849,
    sha256:
      "f81c7264e9c07b0b8e548126e8fd7d8a75e8abb96fa6f47fb712272acfc0260c",
    changelog:
      "The canonical dated changelog of every change to the theory, the suite, the papers and the website.",
  },
};

export function getReleaseAsset(href: string): ReleaseAsset | undefined {
  return RELEASE_ASSETS[href];
}

export function formatBytes(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(0)} KB`;
  return `${(bytes / (1024 * 1024)).toFixed(2)} MB`;
}

export function formatHashShort(sha256: string): string {
  return `${sha256.slice(0, 8)}…${sha256.slice(-4)}`;
}
