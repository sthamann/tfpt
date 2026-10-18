import { papers } from "@/lib/papers";
import { predictions } from "@/lib/predictions";
import { SITE_URL } from "@/lib/utils";
import { SITE_VERSION } from "@/lib/version";

export const collectionJsonLd = {
  "@context": "https://schema.org",
  "@type": "Collection",
  name: `TFPT ${SITE_VERSION} Compiler-Closure Document Set`,
  url: `${SITE_URL}/papers`,
  description:
    `The TFPT ${SITE_VERSION} document set: the introduction reading guide, the architecture and E₈ compiler, the Standard Model, the E₈ audit and bootstrap, the honest frontier, the adversarial Red-Team audit, and the four companions — Appendix H (horizon), the Origin Theory synthesis, the research contracts, and the safeguards discipline.`,
  hasPart: papers.map((p) => ({
    "@type": "ScholarlyArticle",
    name: p.title,
    headline: p.title,
    alternateName: p.subtitle,
    abstract: p.abstract,
    url: `${SITE_URL}/papers/${p.slug}`,
    inLanguage: "en",
    author: [
      { "@type": "Person", name: "Stefan Hamann" },
      { "@type": "Person", name: "Alessandro Rizzo" },
    ],
    isPartOf: {
      "@type": "PublicationIssue",
      name: `TFPT ${SITE_VERSION} compiler-closure document set`,
      issueNumber: String(p.number),
    },
    encoding: {
      "@type": "MediaObject",
      contentUrl: `${SITE_URL}${p.pdf}`,
      encodingFormat: "application/pdf",
    },
  })),
};

export const predictionsJsonLd = {
  "@context": "https://schema.org",
  "@type": "Dataset",
  name: "TFPT prediction surface",
  description:
    "Falsifiable predictions of the TFPT compiler closure: α⁻¹(0), the solar angle sin²θ₁₂ = 1/3 − φ₀/2, sin²θ₁₃, the inflation tensor ratio r, n_s, A_s, the strong-CP null θ_eff = 0, cosmic birefringence β, Ω_b, η_B, the axion window, and the flavor invariants (det R = 8).",
  url: `${SITE_URL}/predictions`,
  creator: [
    { "@type": "Person", name: "Stefan Hamann" },
    { "@type": "Person", name: "Alessandro Rizzo" },
  ],
  keywords: predictions.map((p) => p.shortTitle).join(", "),
  variableMeasured: predictions.map((p) => ({
    "@type": "PropertyValue",
    name: p.shortTitle,
    description: p.title,
    value: p.numericValue,
    unitText: p.unit,
  })),
};
