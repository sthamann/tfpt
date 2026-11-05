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
  releaseDate: "2026-11-05",
};

export const RELEASE_ASSETS: Record<string, ReleaseAsset> = {
  "/papers/introduction_guide.pdf": {
    href: "/papers/introduction_guide.pdf",
    ...COMMON,
    bytes: 1013629,
    sha256: "2fcd4436e4d5b03c35521656dfe31c7f6c97fe09cfc032efe9c61ec6de26c4c1",
    changelog: "Core chapters of the original introduction; the computational appendix and history remain in the complete edition.",
  },
  "/papers/verification_catalog.pdf": {
    href: "/papers/verification_catalog.pdf",
    ...COMMON,
    bytes: 1474815,
    sha256: "0f6dd5a77e328471f7b1697937ca6f49788285498a1e51a2418614e2e13caf6c",
    changelog: "Standalone reference index of registered verification modules and their stated checks.",
  },
  "/papers/introduction.pdf": {
    href: "/papers/introduction.pdf",
    ...COMMON,
    bytes: 3566341,
    sha256:
      "6ce7f0edf0db2086dd77fd7708e8e6bdbbdfd6c100e0ed4b8c5f7c52f9eaf280",
    changelog:
      "Compiler-closure reading guide: two axioms, the dependency DAG, the predictions and the proof ledger.",
  },
  "/papers/tfpt_1_architecture_e8.pdf": {
    href: "/papers/tfpt_1_architecture_e8.pdf",
    ...COMMON,
    bytes: 1392953,
    sha256:
      "b038f277fbad8dcd4f0ad86713b86d82c4e7065779f1f5e224434e68791c5011",
    changelog:
      "Architecture: the two axioms, the D₅ × A₃ → E₈ construction, and the EM fixed point with existence + uniqueness.",
  },
  "/papers/tfpt_2_standard_model.pdf": {
    href: "/papers/tfpt_2_standard_model.pdf",
    ...COMMON,
    bytes: 1384855,
    sha256:
      "5ca3ef6796307d5cd5402b7654a933c3de6356657dbfeaff3b9c25f97ce4494f",
    changelog:
      "The Standard Model in one φ₀-ladder, the flavor residue matrix, and the derived solar angle θ₁₂.",
  },
  "/papers/tfpt_3_e8_audit_bootstrap.pdf": {
    href: "/papers/tfpt_3_e8_audit_bootstrap.pdf",
    ...COMMON,
    bytes: 1365510,
    sha256:
      "c6dfce446255f035fbe9c598aa66e59c32a5cf3f6fef03c4b26b22cf84c2af4c",
    changelog:
      "The seven E₈ slices as an audit raster, the cascade bridge, and the Möbius bootstrap.",
  },
  "/papers/tfpt_4_frontier.pdf": {
    href: "/papers/tfpt_4_frontier.pdf",
    ...COMMON,
    bytes: 909058,
    sha256:
      "a355dfdf8b7e70e047aaf074cf25edca8d9f39dda99e4447be8613e8a77e4321",
    changelog:
      "Honest status of η_B, m_p/m_e, Koide, dark matter and full quantum gravity — not forced onto the ladder.",
  },
  "/papers/tfpt_horizon_readouts.pdf": {
    href: "/papers/tfpt_horizon_readouts.pdf",
    ...COMMON,
    bytes: 932570,
    sha256:
      "935fb488437d47bda2d0233e0684a585e273211909296e85721f5e7ef396eb06",
    changelog:
      "Appendix H — the horizon unit system: c₃ = 1/(8π) as the universal horizon thermal code.",
  },
  "/papers/origin_theory.pdf": {
    href: "/papers/origin_theory.pdf",
    ...COMMON,
    bytes: 1198974,
    sha256:
      "b05ff185fb0bbe789e5064be91a6dc89bb8678266fe90db75729f73e9773541a",
    changelog:
      "Origin Theory: the (5,3) skeleton, the triply-forced 8, the order-30 Coxeter cycle, and the gapped unique attractor.",
  },
  "/papers/tfpt_research_contracts.pdf": {
    href: "/papers/tfpt_research_contracts.pdf",
    ...COMMON,
    bytes: 2360389,
    sha256:
      "4d077f8585d04375ab6115295ada8cf9c8c9db7012b4af9d164dc6b22b643e5e",
    changelog:
      "Research contracts separate compiler Rest = v_geo ⊕ G_net ⊕ F_transfer from Rest_TOE. Round 4 (v1026–v1030) closes the relaxed TEL-B norm at fixed M=1, Ny=8: ||R_N||HS < 2.995906 < 3 for every even N≥16, with the former CF/DG estimates discharged for this bound by native v1026 using v1022/v1025. It also adds narrow T3/T4/T6–T8 identities and counterbounds, but closes no T-gate: FE-GEN/ALG-EXH, T1–T8, TFPT.TOE.COMPLETE.01 and the shared complete 3+1D parent remain [O]. The v1029 tensor target requires global zero-mode removal and is not a TFPT embedding. Round 7 (v1031–v1035; 233 typed checks) adds full free quantum/covariant curvature proofs, auxiliary charged corners, the factorized mirror bound and prescribed-source Ward identities. Microscopic TFPT emergence and universal nonlinear interaction remain open; v1033/v1034 require full repository sources. Wave 4: v998–v1001 + lattice-fundamental quasilocal-family amendment + ALPHA relative-det note.",
  },
  "/papers/tfpt_safeguards.pdf": {
    href: "/papers/tfpt_safeguards.pdf",
    ...COMMON,
    bytes: 617946,
    sha256:
      "35d517aac75573dde55a2bbc4044977440fa4b7ecdd3f6d92348736714570412",
    changelog:
      "Safeguards: the verification discipline — the status calculus, no-free-pattern + reverse audit (and v431: the 5/8 'overhead' degrees are the forced two-family ladder 6·spine ⊔ det-ladder, not diffuse slack), the over-determination map (v427) with its honest self-correction (v428: the seven arithmetic witnesses compress one (2,3,5)/E₈ object; the genuine multiplication is the input forced four ways + the foreign α⁻¹) and its unconditional floor (v432: ~10⁻¹⁰ from disjoint pieces only, ~20 orders above the v100 conditional; hardened by v436 to an assumption-minimal 1/94,500 ≈ 4.40σ counting floor with a monotone concession ladder), the firewall + No-Unit theorem, frozen predictions + null model, the independent Wolfram and Lean paths, and the red team.",
  },
  "/papers/tfpt_5_redteam.pdf": {
    href: "/papers/tfpt_5_redteam.pdf",
    ...COMMON,
    bytes: 869025,
    sha256:
      "e5e062c58d41f384b69954be82fdaf2b87fa09b4e500cc8f5240424c6f793960",
    changelog:
      "The adversarial audit: Targets A–E, what survives, what each target reduces to, and the kill tests.",
  },
  "/papers/note_e8_gaussian_code.pdf": {
    href: "/papers/note_e8_gaussian_code.pdf",
    ...COMMON,
    bytes: 370071,
    sha256:
      "40438e7e98cbfd5611f5697d8a91afbcc34c35d0eea8e2821cb1e5a4844bdd12",
    changelog:
      "Working note N1 — the Gaussian code bridge: E₈ over ℤ[i] via Construction A over the extended Hamming code, the canonical four-bit quotient L/(1+i)L ≅ F₂⁴, and the G₃₁ quartic companion (v689/v690 + 65 Lean theorems).",
  },
  "/papers/changelog.pdf": {
    href: "/papers/changelog.pdf",
    ...COMMON,
    bytes: 1875344,
    sha256:
      "ef0912da3ae99276770e5b0380283c015ec1daef970510f15bed51ad91c44230",
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
