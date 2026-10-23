import { papers } from "@/lib/papers";
import { predictions } from "@/lib/predictions";
import { SITE_URL } from "@/lib/utils";
import { SITE_VERSION } from "@/lib/version";

export const collectionJsonLd = {
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "@id": `${SITE_URL}/papers#collection`,
  name: "TFPT research papers",
  url: `${SITE_URL}/papers`,
  description: "Research papers by Stefan Hamann and Alessandro Rizzo on TFPT, E₈, Standard Model structure and the alpha fixed point, with assumptions and research status.",
  inLanguage: "en",
  isPartOf: { "@id": `${SITE_URL}/#website` },
  mainEntity: {
    "@type": "ItemList",
    numberOfItems: papers.length,
    itemListElement: papers.map((paper, index) => ({
      "@type": "ListItem",
      position: index + 1,
      item: {
        "@type": "ScholarlyArticle",
        "@id": `${SITE_URL}/papers/${paper.slug}#article`,
        name: paper.title,
        url: `${SITE_URL}/papers/${paper.slug}`,
      },
    })),
  },
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
