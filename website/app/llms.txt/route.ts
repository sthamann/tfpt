import { papers } from "@/lib/papers";
import { predictions } from "@/lib/predictions";
import { REPO_URL, SITE_URL } from "@/lib/utils";
import { SITE_DATE, SITE_VERSION } from "@/lib/version";

/**
 * `/llms.txt` — a machine-readable context file for AI systems (see llmstxt.org).
 *
 * Generated at build time from the same data layer that drives the site
 * (papers, predictions, version), so it never drifts from the published
 * content. Plain text / markdown: a quick, parseable overview an LLM can use to
 * understand and cite TFPT correctly, including the disambiguation from the
 * unrelated Brouwer–Lefschetz fixed-point theory of mathematics.
 */
export const dynamic = "force-static";

function buildLlmsTxt(): string {
  const corePapers = papers.filter((p) => !p.label);
  const companions = papers.filter((p) => p.label);

  const docLine = (p: (typeof papers)[number]) =>
    `- [${p.title}](${SITE_URL}/papers/${p.slug}) — ${p.subtitle}. PDF: ${SITE_URL}${p.pdf}`;

  const headlinePredictions = predictions
    .slice(0, 12)
    .map(
      (p) =>
        `- ${p.shortTitle} — ${p.title} (${p.status}; value ${p.numericValue}${p.unit ? ` ${p.unit}` : ""})`,
    )
    .join("\n");

  return `# TFPT — Topological Fixed-Point Theory

> Topological Fixed-Point Theory (TFPT) is a theoretical-physics framework
> by Stefan Hamann and Alessandro Rizzo. P1 supplies a structured primitive
> reflection-positive boundary kernel; c3 = 1/(8pi) is its normalization.
> P2 declares the physical five-slot 3+2 readout. Their shared four-mark
> geometry, anchor and finite W-bridge provide existing conditional reductions.
> The compiler closes D5 plus A3 to E8 and supplies Standard-Model structure,
> flavor and alpha relations under stated premises. The operational source
> already contains state and time. Full physical source identification and
> readout completion remain separate from finite compiler closure.
> ${predictions.length} status-graded falsifiable test surfaces are listed.

Disambiguation: this is the physics theory "TFPT" (compiler closure for the
Standard Model). It is NOT the established Brouwer–Lefschetz "topological fixed
point theory" of mathematics (Nielsen/Lefschetz numbers, degree theory).

Version: ${SITE_VERSION} · Last updated: ${SITE_DATE}
Site: ${SITE_URL}
Source code & verification suite: ${REPO_URL}
Archived deposit (DOI): https://doi.org/10.5281/zenodo.20846087
Authors: Stefan Hamann, Alessandro Rizzo
License: documents CC-BY; code MPL-2.0

## What TFPT claims
- The Standard Model gauge group (SU(3)×SU(2)×U(1))/Z6, hypercharge, and exactly
  three families follow in the declared carrier and marked source construction.
- alpha^-1 = 137.0359992 is the unique positive root of a parameter-free self-consistent closure equation
  boundary Ward identity (a fixed point, with proven existence and uniqueness),
  not a fit.
- The strong-CP angle closes structurally: theta_eff = 0.
- Flavor: integer lattice operators with det(Q,K,R,L) = (3,4,8,20), product
  1920 = |W(D5)|; charged-lepton coefficients (16/7, 4/3, 7/6) exactly.
- Cosmology read-outs: Omega_b, the Starobinsky scalaron mass, Lambda ~ e^(-2/alpha),
  cosmic birefringence beta = phi0/(4pi) ≈ 0.2424°.
- Every load-bearing claim is machine-checked: an independent Python suite, a
  Wolfram mirror, and a Lean 4 carrier-rigidity proof, all tracked in a versioned
  status ledger.

## What TFPT does NOT claim
- E8 is the compiler's internal bookkeeping (an audit hull), NOT an unbroken
  physical gauge group; the Distler–Garibaldi and Coleman–Mandula no-go results
  do not apply.
- No certified strict Theory of Everything; no dimensionful constant is claimed
  as a derivation from pure numbers (one metrology unit, v_geo, stays open).
- Round 4 (v1026-v1030) closes the relaxed TEL-B norm at fixed M=1, Ny=8:
  ||R_N||HS < 2.995906 < 3 for every even N>=16. Native v1026 uses v1022/v1025
  to discharge the former CF/DG estimates for this bound. The remaining modules
  add narrow T3/T4/T6-T8 identities and counterbounds. FE-GEN/ALG-EXH, every
  T1-T8 gate, TFPT.TOE.COMPLETE.01 and the shared 3+1D parent remain [O]. The
  v1029 tensor target requires global zero-mode removal and is not a TFPT embedding.

## Key pages
- Overview: ${SITE_URL}
- Reading guide (start here): ${SITE_URL}/orientation
- How the compiler works: ${SITE_URL}/compiler
- Interactive verification (browser-compatible checks plus pinned native reproduction paths): ${SITE_URL}/verification
- How to falsify TFPT (kill tests): ${SITE_URL}/falsification
- For reviewers: ${SITE_URL}/review
- Hostile-referee FAQ: ${SITE_URL}/faq
- Changelog: ${SITE_URL}/changelog

## Documents (peer-review-style document set, v${SITE_VERSION})
${corePapers.map(docLine).join("\n")}
${companions.map(docLine).join("\n")}

## Headline predictions (status-graded)
${headlinePredictions}

## How to cite
Hamann, Stefan & Rizzo, Alessandro (2026). Topological Fixed-Point Theory (TFPT),
v${SITE_VERSION}. ${SITE_URL} · DOI: 10.5281/zenodo.20846087
`;
}

export function GET(): Response {
  return new Response(buildLlmsTxt(), {
    headers: {
      "content-type": "text/plain; charset=utf-8",
      "cache-control": "public, max-age=3600, s-maxage=86400",
    },
  });
}
