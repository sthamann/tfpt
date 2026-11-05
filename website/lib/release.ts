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
    bytes: 1032953,
    sha256: "06a1eaf7d04e39c450ebb89e634ca945d3929b3158f60efd1dbbe92542cb9d72",
    changelog: "Core chapters of the original introduction; the computational appendix and history remain in the complete edition.",
  },
  "/papers/verification_catalog.pdf": {
    href: "/papers/verification_catalog.pdf",
    ...COMMON,
    bytes: 1474798,
    sha256: "26f32a791bc94d6146ba52a9ee2a39808a11d4ebbb40fd7450c1e5443148e334",
    changelog: "Standalone reference index of registered verification modules and their stated checks.",
  },
  "/papers/introduction.pdf": {
    href: "/papers/introduction.pdf",
    ...COMMON,
    bytes: 3586972,
    sha256:
      "ed07eed8e12674524b01543a7add6814108c61836148fbdffa79363ae1ecef02",
    changelog:
      "Compiler-closure reading guide: two axioms, the dependency DAG, the predictions and the proof ledger.",
  },
  "/papers/tfpt_1_architecture_e8.pdf": {
    href: "/papers/tfpt_1_architecture_e8.pdf",
    ...COMMON,
    bytes: 1411758,
    sha256:
      "8f8ebd8bbeed52b75358483f74e392f1957d5361c14286aae21ff862ac6978c6",
    changelog:
      "Architecture: the two axioms, the D₅ × A₃ → E₈ construction, and the EM fixed point with existence + uniqueness.",
  },
  "/papers/tfpt_2_standard_model.pdf": {
    href: "/papers/tfpt_2_standard_model.pdf",
    ...COMMON,
    bytes: 1403947,
    sha256:
      "0e3b6ad55fba8252ed3b0cb82dee094f9e37151ac018dd2c6031c5e937cb48a2",
    changelog:
      "The Standard Model in one φ₀-ladder, the flavor residue matrix, and the derived solar angle θ₁₂.",
  },
  "/papers/tfpt_3_e8_audit_bootstrap.pdf": {
    href: "/papers/tfpt_3_e8_audit_bootstrap.pdf",
    ...COMMON,
    bytes: 1365493,
    sha256:
      "a52514576ce36dff9e6baf9cc2d74564b134eb8e07b002ef3f1b1854131f5fbe",
    changelog:
      "The seven E₈ slices as an audit raster, the cascade bridge, and the Möbius bootstrap.",
  },
  "/papers/tfpt_4_frontier.pdf": {
    href: "/papers/tfpt_4_frontier.pdf",
    ...COMMON,
    bytes: 929736,
    sha256:
      "e9d189711019fa44e7aa692d5dc493a8373808cd1edd40ef6a01bd38dd821e63",
    changelog:
      "Honest status of η_B, m_p/m_e, Koide, dark matter and full quantum gravity — not forced onto the ladder.",
  },
  "/papers/tfpt_horizon_readouts.pdf": {
    href: "/papers/tfpt_horizon_readouts.pdf",
    ...COMMON,
    bytes: 932567,
    sha256:
      "3c8e24592ee1f52f016e8dac5c732ece74485ded93612732fbccf9f501e4f1d5",
    changelog:
      "Appendix H — the horizon unit system: c₃ = 1/(8π) as the universal horizon thermal code.",
  },
  "/papers/origin_theory.pdf": {
    href: "/papers/origin_theory.pdf",
    ...COMMON,
    bytes: 1219721,
    sha256:
      "e67757c7c20d615edbd1aaa6e3a0777c68da237a61fc539d52b94274cdca5b54",
    changelog:
      "Origin Theory: the (5,3) skeleton, the triply-forced 8, the order-30 Coxeter cycle, and the gapped unique attractor.",
  },
  "/papers/tfpt_research_contracts.pdf": {
    href: "/papers/tfpt_research_contracts.pdf",
    ...COMMON,
    bytes: 2377929,
    sha256:
      "e0cbfaabca900dbdec60de3e97faf67b935be0ce7315b2b741e0f0f90d258d5f",
    changelog:
      "Research contracts separate compiler Rest = v_geo ⊕ G_net ⊕ F_transfer from Rest_TOE. Round 4 (v1026–v1030) closes the relaxed TEL-B norm at fixed M=1, Ny=8: ||R_N||HS < 2.995906 < 3 for every even N≥16, with the former CF/DG estimates discharged for this bound by native v1026 using v1022/v1025. It also adds narrow T3/T4/T6–T8 identities and counterbounds, but closes no T-gate: FE-GEN/ALG-EXH, T1–T8, TFPT.TOE.COMPLETE.01 and the shared complete 3+1D parent remain [O]. The v1029 tensor target requires global zero-mode removal and is not a TFPT embedding. Round 7 (v1031–v1035; 233 typed checks) adds full free quantum/covariant curvature proofs, auxiliary charged corners, the factorized mirror bound and prescribed-source Ward identities. Microscopic TFPT emergence and universal nonlinear interaction remain open; v1033/v1034 require full repository sources. Wave 4: v998–v1001 + lattice-fundamental quasilocal-family amendment + ALPHA relative-det note.",
  },
  "/papers/tfpt_safeguards.pdf": {
    href: "/papers/tfpt_safeguards.pdf",
    ...COMMON,
    bytes: 617946,
    sha256:
      "c14a6f11415964e0097cef07691bfac5d3c3022f419cd1392ffd512b740c1624",
    changelog:
      "Safeguards: the verification discipline — the status calculus, no-free-pattern + reverse audit (and v431: the 5/8 'overhead' degrees are the forced two-family ladder 6·spine ⊔ det-ladder, not diffuse slack), the over-determination map (v427) with its honest self-correction (v428: the seven arithmetic witnesses compress one (2,3,5)/E₈ object; the genuine multiplication is the input forced four ways + the foreign α⁻¹) and its unconditional floor (v432: ~10⁻¹⁰ from disjoint pieces only, ~20 orders above the v100 conditional; hardened by v436 to an assumption-minimal 1/94,500 ≈ 4.40σ counting floor with a monotone concession ladder), the firewall + No-Unit theorem, frozen predictions + null model, the independent Wolfram and Lean paths, and the red team.",
  },
  "/papers/tfpt_5_redteam.pdf": {
    href: "/papers/tfpt_5_redteam.pdf",
    ...COMMON,
    bytes: 869026,
    sha256:
      "b89c440a6ba6bc36295f01d348cc60524a37a3b137684792d97308ff1fdcc61b",
    changelog:
      "The adversarial audit: Targets A–E, what survives, what each target reduces to, and the kill tests.",
  },
  "/papers/note_e8_gaussian_code.pdf": {
    href: "/papers/note_e8_gaussian_code.pdf",
    ...COMMON,
    bytes: 370071,
    sha256:
      "48ea2533ad079c4fbc410e5811c72f7b0ba47d3c10d913e14fb7b737f04486d9",
    changelog:
      "Working note N1 — the Gaussian code bridge: E₈ over ℤ[i] via Construction A over the extended Hamming code, the canonical four-bit quotient L/(1+i)L ≅ F₂⁴, and the G₃₁ quartic companion (v689/v690 + 65 Lean theorems).",
  },
  "/papers/changelog.pdf": {
    href: "/papers/changelog.pdf",
    ...COMMON,
    bytes: 1875466,
    sha256:
      "f6b6c0617cb7fee1b5d05272ed81e6fd8767a7109421a466e22b3f5f4b2dd5b9",
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
