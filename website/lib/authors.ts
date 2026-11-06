import { SITE_URL } from "@/lib/utils";

/** Identities recorded in the manuscripts and the archived release metadata. */
export const AUTHORS = [
  {
    slug: "stefan-hamann",
    name: "Stefan Hamann",
    familyName: "Hamann",
    givenName: "Stefan",
    description: "Stefan Hamann is a coauthor of the TFPT publication set and maintains the public TFPT repository. His earlier TFPT release is recorded in the Zenodo archive.",
    profiles: [
      { label: "Personal website", url: "https://stefan-hamann.de/" },
      { label: "ORCID 0009-0001-2596-109X", url: "https://orcid.org/0009-0001-2596-109X" },
      { label: "GitHub", url: "https://github.com/sthamann" },
    ],
  },
  {
    slug: "alessandro-rizzo",
    name: "Alessandro Rizzo",
    familyName: "Rizzo",
    givenName: "Alessandro",
    description: "Alessandro Rizzo is a coauthor of the current TFPT publication set with Stefan Hamann. The papers below document their shared mathematical constructions, calculations and physical research questions.",
    profiles: [],
  },
] as const;

export function authorJsonLd(author: (typeof AUTHORS)[number]) {
  return {
    "@type": "Person",
    "@id": `${SITE_URL}/authors/${author.slug}#person`,
    name: author.name,
    givenName: author.givenName,
    familyName: author.familyName,
    url: `${SITE_URL}/authors/${author.slug}`,
    sameAs: author.profiles.map((profile) => profile.url),
  };
}

export const AUTHOR_ENTITIES = AUTHORS.map(authorJsonLd);
