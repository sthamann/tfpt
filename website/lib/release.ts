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
    bytes: 1049690,
    sha256: "9ef5b6e6a1305c7c7c5390492fd9093264e1ea72e5b83d03a4c29e8c5c8c16f5",
    changelog: "Core chapters of the original introduction; the computational appendix and history remain in the complete edition.",
  },
  "/papers/verification_catalog.pdf": {
    href: "/papers/verification_catalog.pdf",
    ...COMMON,
    bytes: 1493672,
    sha256: "7c70ef0c24989e011fe7db4161f51014859ae9a169a07a4a29a9f6f22efaf883",
    changelog: "Standalone reference index of registered verification modules and their stated checks.",
  },
  "/papers/introduction.pdf": {
    href: "/papers/introduction.pdf",
    ...COMMON,
    bytes: 3639371,
    sha256:
      "c637d98d8bb089c120398ea8c06ab5c12f90120026daaafd5519e291ca585073",
    changelog:
      "Compiler-closure reading guide: two axioms, the dependency DAG, the predictions and the proof ledger.",
  },
  "/papers/tfpt_1_architecture_e8.pdf": {
    href: "/papers/tfpt_1_architecture_e8.pdf",
    ...COMMON,
    bytes: 1431100,
    sha256:
      "f384fe6b6a11fc6925c5ff2953586eef144b2315a88a960dc3927d935fbb361a",
    changelog:
      "Architecture: the two axioms, the D₅ × A₃ → E₈ construction, and the EM fixed point with existence + uniqueness.",
  },
  "/papers/tfpt_2_standard_model.pdf": {
    href: "/papers/tfpt_2_standard_model.pdf",
    ...COMMON,
    bytes: 1424077,
    sha256:
      "e4363db6c6149c87417d91b8d36a0e2c74fe6f25416a1fe8c18e988b8efa4503",
    changelog:
      "The Standard Model in one φ₀-ladder, the flavor residue matrix, and the derived solar angle θ₁₂.",
  },
  "/papers/tfpt_3_e8_audit_bootstrap.pdf": {
    href: "/papers/tfpt_3_e8_audit_bootstrap.pdf",
    ...COMMON,
    bytes: 1372346,
    sha256:
      "bce7cca546b8fb3183ac733a978666211ead53bf1ab23da2e78a59f14238b6e2",
    changelog:
      "The seven E₈ slices as an audit raster, the cascade bridge, and the Möbius bootstrap.",
  },
  "/papers/tfpt_4_frontier.pdf": {
    href: "/papers/tfpt_4_frontier.pdf",
    ...COMMON,
    bytes: 945760,
    sha256:
      "65002d03b940ee748cf86cadfa99dc4189b86eb0625742583c45fb66212271c5",
    changelog:
      "Honest status of η_B, m_p/m_e, Koide, dark matter and full quantum gravity — not forced onto the ladder.",
  },
  "/papers/tfpt_horizon_readouts.pdf": {
    href: "/papers/tfpt_horizon_readouts.pdf",
    ...COMMON,
    bytes: 936299,
    sha256:
      "cc679cfd15b089dc95199b3ee23cbac965757f612a94197f6ffbd8a60aa97a93",
    changelog:
      "Appendix H — the horizon unit system: c₃ = 1/(8π) as the universal horizon thermal code.",
  },
  "/papers/origin_theory.pdf": {
    href: "/papers/origin_theory.pdf",
    ...COMMON,
    bytes: 1236572,
    sha256:
      "219ef2de6787fa8d912dc98ea88c8b51e578d7048ea48cac7f319cbd153723d4",
    changelog:
      "Origin Theory: the (5,3) skeleton, the triply-forced 8, the order-30 Coxeter cycle, and the gapped unique attractor.",
  },
  "/papers/tfpt_research_contracts.pdf": {
    href: "/papers/tfpt_research_contracts.pdf",
    ...COMMON,
    bytes: 2406184,
    sha256:
      "2db4d59d408226da3e350cb17759c5d2e8999795fccb19e2cac30b00c0566467",
    changelog:
      "Research contracts separate compiler Rest = v_geo ⊕ G_net ⊕ F_transfer from Rest_TOE. Round 4 (v1026–v1030) closes the relaxed TEL-B norm at fixed M=1, Ny=8: ||R_N||HS < 2.995906 < 3 for every even N≥16, with the former CF/DG estimates discharged for this bound by native v1026 using v1022/v1025. It also adds narrow T3/T4/T6–T8 identities and counterbounds, but closes no T-gate: FE-GEN/ALG-EXH, T1–T8, TFPT.TOE.COMPLETE.01 and the shared complete 3+1D parent remain [O]. The v1029 tensor target requires global zero-mode removal and is not a TFPT embedding. Round 7 (v1031–v1035; 233 typed checks) adds full free quantum/covariant curvature proofs, auxiliary charged corners, the factorized mirror bound and prescribed-source Ward identities. Microscopic TFPT emergence and universal nonlinear interaction remain open; v1033/v1034 require full repository sources. Wave 4: v998–v1001 + lattice-fundamental quasilocal-family amendment + ALPHA relative-det note.",
  },
  "/papers/tfpt_safeguards.pdf": {
    href: "/papers/tfpt_safeguards.pdf",
    ...COMMON,
    bytes: 620136,
    sha256:
      "6b67ec04d36c7c0efd51b8257e6ac6782b8457aa014e29e3f3c901854ae4c10d",
    changelog:
      "Safeguards: the verification discipline — the status calculus, no-free-pattern + reverse audit (and v431: the 5/8 'overhead' degrees are the forced two-family ladder 6·spine ⊔ det-ladder, not diffuse slack), the over-determination map (v427) with its honest self-correction (v428: the seven arithmetic witnesses compress one (2,3,5)/E₈ object; the genuine multiplication is the input forced four ways + the foreign α⁻¹) and its unconditional floor (v432: ~10⁻¹⁰ from disjoint pieces only, ~20 orders above the v100 conditional; hardened by v436 to an assumption-minimal 1/94,500 ≈ 4.40σ counting floor with a monotone concession ladder), the firewall + No-Unit theorem, frozen predictions + null model, the independent Wolfram and Lean paths, and the red team.",
  },
  "/papers/tfpt_5_redteam.pdf": {
    href: "/papers/tfpt_5_redteam.pdf",
    ...COMMON,
    bytes: 872377,
    sha256:
      "2d5e31554109df50cce8450fb76e97cdaf6b7992c2b9458d0ab0acad4217bbb5",
    changelog:
      "The adversarial audit: Targets A–E, what survives, what each target reduces to, and the kill tests.",
  },
  "/papers/note_e8_gaussian_code.pdf": {
    href: "/papers/note_e8_gaussian_code.pdf",
    ...COMMON,
    bytes: 370071,
    sha256:
      "a1e2054744e0b90863a51e6bb9964d03e1f037cff8cc4f436a86c92d4e891125",
    changelog:
      "Working note N1 — the Gaussian code bridge: E₈ over ℤ[i] via Construction A over the extended Hamming code, the canonical four-bit quotient L/(1+i)L ≅ F₂⁴, and the G₃₁ quartic companion (v689/v690 + 65 Lean theorems).",
  },
  "/papers/changelog.pdf": {
    href: "/papers/changelog.pdf",
    ...COMMON,
    bytes: 1877136,
    sha256:
      "01b64663b9081e2bb8889efc50d20d3f3a08fa44269498a1051796affc4b1b90",
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
