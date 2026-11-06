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
    bytes: 1045066,
    sha256: "4b83eee3b2aa1143a0b2179616fad2d30134affa0a6197b9daf7e966c04c6cd2",
    changelog: "Core chapters of the original introduction; the computational appendix and history remain in the complete edition.",
  },
  "/papers/verification_catalog.pdf": {
    href: "/papers/verification_catalog.pdf",
    ...COMMON,
    bytes: 1474418,
    sha256: "86973714ceaa5ee49d3b5707bdcc091abd8c942976e66b314472c6c174aa8238",
    changelog: "Standalone reference index of registered verification modules and their stated checks.",
  },
  "/papers/introduction.pdf": {
    href: "/papers/introduction.pdf",
    ...COMMON,
    bytes: 3598630,
    sha256:
      "e932e7697ec969bfba995033ce0aa7ce84c2657fb199c201571641a1e8582546",
    changelog:
      "Compiler-closure reading guide: two axioms, the dependency DAG, the predictions and the proof ledger.",
  },
  "/papers/tfpt_1_architecture_e8.pdf": {
    href: "/papers/tfpt_1_architecture_e8.pdf",
    ...COMMON,
    bytes: 1423261,
    sha256:
      "caee883fa856aa65d549bf35b057bd4c4a209e490733c6e32e4c2a41a6c2562f",
    changelog:
      "Architecture: the two axioms, the D₅ × A₃ → E₈ construction, and the EM fixed point with existence + uniqueness.",
  },
  "/papers/tfpt_2_standard_model.pdf": {
    href: "/papers/tfpt_2_standard_model.pdf",
    ...COMMON,
    bytes: 1416134,
    sha256:
      "1e00ebba45c81584f97dd6fca3eaf2d6e1e40531db41e0e29f5566c54bf423f6",
    changelog:
      "The Standard Model in one φ₀-ladder, the flavor residue matrix, and the derived solar angle θ₁₂.",
  },
  "/papers/tfpt_3_e8_audit_bootstrap.pdf": {
    href: "/papers/tfpt_3_e8_audit_bootstrap.pdf",
    ...COMMON,
    bytes: 1365627,
    sha256:
      "d78d5469ac619a8d79c74d0fff3be8a870d1bd8c7484d147b87e1374d6182d8f",
    changelog:
      "The seven E₈ slices as an audit raster, the cascade bridge, and the Möbius bootstrap.",
  },
  "/papers/tfpt_4_frontier.pdf": {
    href: "/papers/tfpt_4_frontier.pdf",
    ...COMMON,
    bytes: 941988,
    sha256:
      "7367a26b4f474dc8290774047e8c135cd5943106be956933ed9cd66277132f42",
    changelog:
      "Honest status of η_B, m_p/m_e, Koide, dark matter and full quantum gravity — not forced onto the ladder.",
  },
  "/papers/tfpt_horizon_readouts.pdf": {
    href: "/papers/tfpt_horizon_readouts.pdf",
    ...COMMON,
    bytes: 932694,
    sha256:
      "c07bf97c326c18eb0d95c496f36e65ead873335fb19dec279987a9e10c238095",
    changelog:
      "Appendix H — the horizon unit system: c₃ = 1/(8π) as the universal horizon thermal code.",
  },
  "/papers/origin_theory.pdf": {
    href: "/papers/origin_theory.pdf",
    ...COMMON,
    bytes: 1231453,
    sha256:
      "79cd9a425b9af2fe9418d3023123654090fc146bac4a56b36a9c0cd93a0df9cf",
    changelog:
      "Origin Theory: the (5,3) skeleton, the triply-forced 8, the order-30 Coxeter cycle, and the gapped unique attractor.",
  },
  "/papers/tfpt_research_contracts.pdf": {
    href: "/papers/tfpt_research_contracts.pdf",
    ...COMMON,
    bytes: 2389016,
    sha256:
      "2ae518ad8adf4a454c3728b56665afa6d23a1c77f9bb90c28fbeb38e2d6144b9",
    changelog:
      "Research contracts separate compiler Rest = v_geo ⊕ G_net ⊕ F_transfer from Rest_TOE. Round 4 (v1026–v1030) closes the relaxed TEL-B norm at fixed M=1, Ny=8: ||R_N||HS < 2.995906 < 3 for every even N≥16, with the former CF/DG estimates discharged for this bound by native v1026 using v1022/v1025. It also adds narrow T3/T4/T6–T8 identities and counterbounds, but closes no T-gate: FE-GEN/ALG-EXH, T1–T8, TFPT.TOE.COMPLETE.01 and the shared complete 3+1D parent remain [O]. The v1029 tensor target requires global zero-mode removal and is not a TFPT embedding. Round 7 (v1031–v1035; 233 typed checks) adds full free quantum/covariant curvature proofs, auxiliary charged corners, the factorized mirror bound and prescribed-source Ward identities. Microscopic TFPT emergence and universal nonlinear interaction remain open; v1033/v1034 require full repository sources. Wave 4: v998–v1001 + lattice-fundamental quasilocal-family amendment + ALPHA relative-det note.",
  },
  "/papers/tfpt_safeguards.pdf": {
    href: "/papers/tfpt_safeguards.pdf",
    ...COMMON,
    bytes: 618075,
    sha256:
      "0388d3faa9aa55fe48cd3d4045b7071322e14b60bbb69c7c7b1470c9b0baef7d",
    changelog:
      "Safeguards: the verification discipline — the status calculus, no-free-pattern + reverse audit (and v431: the 5/8 'overhead' degrees are the forced two-family ladder 6·spine ⊔ det-ladder, not diffuse slack), the over-determination map (v427) with its honest self-correction (v428: the seven arithmetic witnesses compress one (2,3,5)/E₈ object; the genuine multiplication is the input forced four ways + the foreign α⁻¹) and its unconditional floor (v432: ~10⁻¹⁰ from disjoint pieces only, ~20 orders above the v100 conditional; hardened by v436 to an assumption-minimal 1/94,500 ≈ 4.40σ counting floor with a monotone concession ladder), the firewall + No-Unit theorem, frozen predictions + null model, the independent Wolfram and Lean paths, and the red team.",
  },
  "/papers/tfpt_5_redteam.pdf": {
    href: "/papers/tfpt_5_redteam.pdf",
    ...COMMON,
    bytes: 869204,
    sha256:
      "4e17553a3d48151638f134e9e423f226b4ce5b9ba1a56879a0e710788f6bc86c",
    changelog:
      "The adversarial audit: Targets A–E, what survives, what each target reduces to, and the kill tests.",
  },
  "/papers/note_e8_gaussian_code.pdf": {
    href: "/papers/note_e8_gaussian_code.pdf",
    ...COMMON,
    bytes: 370071,
    sha256:
      "644c15043b74931dea8fb572eb8c17c823a0a1674e91eebb79894d78d21dc7bc",
    changelog:
      "Working note N1 — the Gaussian code bridge: E₈ over ℤ[i] via Construction A over the extended Hamming code, the canonical four-bit quotient L/(1+i)L ≅ F₂⁴, and the G₃₁ quartic companion (v689/v690 + 65 Lean theorems).",
  },
  "/papers/changelog.pdf": {
    href: "/papers/changelog.pdf",
    ...COMMON,
    bytes: 1877158,
    sha256:
      "26ec1b9656824b66ea9471468cfff7180ac275d71f7bdf40e8ce62a7143cfcbe",
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
