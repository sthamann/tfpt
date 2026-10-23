import { pageMetadata } from "@/lib/seo";
import type { Metadata } from "next";
import { OrientationHero } from "@/components/orientation/OrientationHero";
import { OrientationFrontBox } from "@/components/orientation/OrientationFrontBox";
import { WhatTfptClaims } from "@/components/orientation/WhatTfptClaims";
import { Decoders } from "@/components/orientation/Decoders";
import { StatusMatrix } from "@/components/orientation/StatusMatrix";
import { SeriesMap } from "@/components/orientation/SeriesMap";
import { PublicationOrder } from "@/components/orientation/PublicationOrder";
import { OrientationDownload } from "@/components/orientation/OrientationDownload";
import { RosettaLexicon } from "@/components/RosettaLexicon";
import { SITE_VERSION } from "@/lib/version";
import { SITE_URL } from "@/lib/utils";

export const metadata: Metadata = pageMetadata("/orientation");

const articleJsonLd = {
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  headline: "TFPT in One Map — The Compiler Closure (Introduction)",
  alternateName: "Reading guide, status assessment, and the dependency DAG",
  url: `${SITE_URL}/orientation`,
  inLanguage: "en",
  isPartOf: {
    "@type": "PublicationIssue",
    issueNumber: "0",
    name: `TFPT ${SITE_VERSION} compiler-closure document set`,
  },
  author: [
    { "@type": "Person", name: "Stefan Hamann" },
    { "@type": "Person", name: "Alessandro Rizzo" },
  ],
  abstract:
    `The entry document for the TFPT ${SITE_VERSION} set. It states what TFPT claims and does not claim, the compiler closure from two axioms to E₈, the two engines, the bootstrap loop, and where each load-bearing argument is isolated in the document set.`,
  about: [
    "Compiler closure",
    "Topological Fixed-Point Theory",
    "E8 audit hull",
    "Standard Model",
    "Status discipline",
  ],
  encoding: {
    "@type": "MediaObject",
    contentUrl: `${SITE_URL}/papers/introduction.pdf`,
    encodingFormat: "application/pdf",
  },
};

const breadcrumbJsonLd = {
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  itemListElement: [
    {
      "@type": "ListItem",
      position: 1,
      name: "TFPT",
      item: SITE_URL,
    },
    {
      "@type": "ListItem",
      position: 2,
      name: "Orientation",
      item: `${SITE_URL}/orientation`,
    },
  ],
};

export default function OrientationPage() {
  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(articleJsonLd) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbJsonLd) }}
      />

      <OrientationHero />
      <OrientationFrontBox />
      <WhatTfptClaims />
      <Decoders />
      <StatusMatrix />
      <SeriesMap />
      <PublicationOrder />
      <RosettaLexicon />
      <OrientationDownload />
    </>
  );
}
