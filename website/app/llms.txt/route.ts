import { papers } from "@/lib/papers";
import { predictions } from "@/lib/predictions";
import { REPO_URL, SITE_URL } from "@/lib/utils";
import { SITE_DATE, SITE_VERSION } from "@/lib/version";
import { PROJECT_SUMMARY, TOPIC_GUIDES } from "@/lib/topic-guides";
import { ARCHIVE_RELEASE, EDITORIAL_DATE } from "@/lib/publication";

/**
 * `/llms.txt` — a machine-readable context file for AI systems (see llmstxt.org).
 *
 * Generated at build time from the site's shared topic explanations,
 * papers, predictions and release metadata. Plain text / markdown an LLM can use to
 * understand and cite TFPT correctly, including the disambiguation from the
 * unrelated Brouwer–Lefschetz fixed-point theory of mathematics.
 */
export const dynamic = "force-static";

function buildLlmsTxt(): string {
  const corePapers = papers.filter((p) => !p.label);
  const companions = papers.filter((p) => p.label);

  const docLine = (p: (typeof papers)[number]) =>
    `- [${p.title}](${SITE_URL}/papers/${p.slug}): ${p.subtitle}. PDF: ${SITE_URL}${p.pdf}`;

  const headlinePredictions = predictions
    .slice(0, 12)
    .map(
      (p) =>
        `- ${p.shortTitle}: ${p.title} (${p.status}; value ${p.numericValue}${p.unit ? ` ${p.unit}` : ""})`,
    )
    .join("\n");

  const topics = TOPIC_GUIDES.map((guide) => `### ${guide.title}
${guide.answer}
Claim: ${guide.claim}
Scope: ${guide.scope}
Explanation: ${SITE_URL}${guide.slug}
Sources: ${guide.sources.map((source) => `${source.label}: ${source.href.startsWith("http") ? source.href : SITE_URL + source.href}`).join("; ")}`).join("\n\n");

  return `# TFPT: Topological Fixed-Point Theory

> ${PROJECT_SUMMARY}

Disambiguation: TFPT here names this physics research programme. Established
topological fixed point theory in mathematics studies subjects including
Brouwer and Lefschetz theorems, degree theory and Nielsen numbers.

Version: ${SITE_VERSION} · Publication release: ${SITE_DATE} · Page updated: ${EDITORIAL_DATE}
Site: ${SITE_URL}
Source code & verification suite: ${REPO_URL}
Earlier archived release: v${ARCHIVE_RELEASE.version}, ${ARCHIVE_RELEASE.date}, ${ARCHIVE_RELEASE.url}
The archive above identifies an earlier release, with ${ARCHIVE_RELEASE.author} as its recorded creator. It is not the DOI of the current v${SITE_VERSION} document set.
Authors: Stefan Hamann, Alessandro Rizzo
License: documents CC-BY; code MPL-2.0

## Core explanations and claim scope
${topics}

## Inputs and physical completion
- P1 supplies a structured oriented reflection positive boundary kernel;
  c3 = 1/(8pi) is its normalization. P2 declares the marked five slot 3+2 readout.
  The principles contain geometric and operator structure beyond two numbers.
- Existing whole source and reference transports, state and vacuum reconstruction,
  and the given classical Clifford field/time kernel retain their stated premises.
  Evaluating the full original interacting physical source and spectrum remains
  distinct from these results. A complete physical theory of everything has not
  been established.
- Dimensional readouts require a declared calibration. Cosmological and other
  conditional branches retain their scale, state and history assumptions.

## Evidence and measurement conventions
- The original status ledger and cited source own a claim's status. The public
  markers [E], [C], [O] and [X] distinguish established statements in scope,
  conditional interpretations, open or supplied inputs, and tests or exclusions.
- Python calculations, Wolfram checks and Lean formalizations have different
  scopes. Inspect the actual statement, premises, dependencies and execution
  evidence. A registered script or a formal source file is not proof that every
  physical claim has been verified, nor that a check has just been rerun.
- The alpha comparison uses CODATA 2022: inverse alpha = 137.035999177(21),
  about 1.9 quoted standard uncertainties from the formula value. This is a
  comparison with known data, not a blind prediction.
- The frozen prediction register separates main values, assigned textures and
  conditional bands. Its ${predictions.length} displayed test surfaces are an
  inventory with individual premises; shared inputs produce correlated readouts.
- A mathematical counterexample, a failed reproduction and a physical exclusion
  have distinct scopes. Apply any no go theorem using its actual hypotheses and
  field identification.

## Key pages
- Overview: ${SITE_URL}
- Full connected explanation: ${SITE_URL}/explain
${TOPIC_GUIDES.map((guide) => `- ${guide.title}: ${SITE_URL}${guide.slug}`).join("\n")}
- Reading guide (start here): ${SITE_URL}/orientation
- How the compiler works: ${SITE_URL}/compiler
- Interactive verification (browser-compatible checks plus pinned native reproduction paths): ${SITE_URL}/verification
- How to falsify TFPT (kill tests): ${SITE_URL}/falsification
- For reviewers: ${SITE_URL}/review
- Questions and answers: ${SITE_URL}/faq
- Selected original arguments: ${SITE_URL}/research
- Authors and publication records: ${SITE_URL}/authors
- Changelog: ${SITE_URL}/changelog

## Documents (authored research document set, v${SITE_VERSION})
${corePapers.map(docLine).join("\n")}
${companions.map(docLine).join("\n")}

## Selected registered readouts
These generated entries retain the data layer's status labels. Consult each
record for its premises, original formula and current comparison; the list is
not a claim of independent blind predictions or complete physical validation.
${headlinePredictions}

## How to cite
Hamann, Stefan & Rizzo, Alessandro (2026). Topological Fixed-Point Theory (TFPT),
v${SITE_VERSION}. ${SITE_URL}. Cite the particular paper and its displayed version
when referring to an argument. The earlier archive DOI above applies to
v${ARCHIVE_RELEASE.version} only.
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
