import type { MetadataRoute } from "next";
import { papers } from "@/lib/papers";
import { RELEASE_ASSETS } from "@/lib/release";
import { SITE_DATE } from "@/lib/version";
import { SITE_URL } from "@/lib/utils";
import { AUTHORS } from "@/lib/authors";
import { TOPIC_GUIDES } from "@/lib/topic-guides";
import { researchPages } from "@/lib/research-pages";
import { CHANGELOG_DAYS, CHANGELOG_MONTHS } from "@/lib/changelog-navigation";
import { EDITORIAL_DATE } from "@/lib/publication";
import { INTERACTIVE_CHAPTERS } from "@/lib/interactive-content";

/**
 * Sitemap priority by asset path.
 *
 * The introduction (the reading guide) and the five core documents carry the
 * load-bearing arguments and rank highest; the four companions (Appendix H,
 * Origin Theory, research contracts, safeguards) sit just below.
 */
function priorityForAsset(href: string): number {
  if (href === "/papers/introduction.pdf") return 0.7;
  if (href.startsWith("/papers/")) return 0.65;
  return 0.5;
}

export default function sitemap(): MetadataRoute.Sitemap {
  // Tie lastmod to the released content version (lib/version.ts, generated from
  // tex-artefacts/version.tex) rather than the build timestamp, so crawlers see
  // a meaningful "last changed" date instead of "today" on every deploy.
  const lastModified = new Date(SITE_DATE);

  // Only canonical, crawlable routes — no in-page fragment anchors (#overview,
  // …): search engines drop URL fragments and fold them into the page URL.
  const pages: MetadataRoute.Sitemap = [
    { url: `${SITE_URL}/licensing`, lastModified, changeFrequency: "yearly", priority: 0.3 },
    { url: `${SITE_URL}/empirical-audit`, lastModified: new Date("2026-11-02"), changeFrequency: "monthly", priority: 0.85 },
    { url: `${SITE_URL}/explain`, lastModified: new Date("2026-11-02"), changeFrequency: "monthly", priority: 0.95 },
    { url: `${SITE_URL}/results`, lastModified: new Date("2026-11-02"), changeFrequency: "weekly", priority: 0.9 },
    { url: `${SITE_URL}/documentation`, lastModified, changeFrequency: "monthly", priority: 0.8 },
    {
      url: SITE_URL,
      lastModified,
      changeFrequency: "weekly",
      priority: 1.0,
    },
    {
      url: `${SITE_URL}/orientation`,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.95,
    },
    {
      url: `${SITE_URL}/compiler`,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.85,
    },
    {
      url: `${SITE_URL}/verification`,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.85,
    },
    {
      url: `${SITE_URL}/falsification`,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.85,
    },
    {
      url: `${SITE_URL}/method`,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.85,
    },
    {
      url: `${SITE_URL}/review`,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.8,
    },
    {
      url: `${SITE_URL}/objections`,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.7,
    },
    {
      url: `${SITE_URL}/replication`,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.7,
    },
    {
      url: `${SITE_URL}/papers`,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.85,
    },
    {
      url: `${SITE_URL}/predictions`,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.8,
    },
    {
      url: `${SITE_URL}/architecture`,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.75,
    },
    {
      url: `${SITE_URL}/faq`,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.7,
    },
    {
      url: `${SITE_URL}/changelog`,
      lastModified,
      changeFrequency: "weekly",
      priority: 0.6,
    },
  ];

  const paperPages: MetadataRoute.Sitemap = papers.map((p) => ({
    url: `${SITE_URL}/papers/${p.slug}`,
    lastModified,
    changeFrequency: "monthly",
    priority: 0.85,
  }));

  // Single source of truth for every released PDF asset (papers + predictions
  // + auxiliary documents). New entries only need to be added in
  // `lib/release.ts` — they appear in the sitemap automatically.
  const releaseFiles: MetadataRoute.Sitemap = Object.values(RELEASE_ASSETS).map(
    (asset) => ({
      url: `${SITE_URL}${asset.href}`,
      lastModified: new Date(asset.releaseDate),
      changeFrequency: "monthly",
      priority: priorityForAsset(asset.href),
    }),
  );

  // These visible editorial pages changed independently of the PDF release.
  const updatedPages = new Set([SITE_URL, ...["papers", "faq", "orientation", "predictions", "verification", "review", "architecture", "compiler", "documentation", "empirical-audit", "method", "replication", "falsification", "changelog"].map((path) => `${SITE_URL}/${path}`)]);
  const editedPages = new Set(["", "/faq", "/orientation", "/documentation", "/changelog"].map(path => SITE_URL + path));
  const additions: MetadataRoute.Sitemap = [
    ...INTERACTIVE_CHAPTERS.map(chapter => ({url: `${SITE_URL}/interactive${chapter.id === "overview" ? "" : `/${chapter.id}`}`, lastModified: new Date(EDITORIAL_DATE), changeFrequency: "monthly" as const, priority: chapter.id === "overview" ? 0.95 : 0.85})),
    ...TOPIC_GUIDES.map(guide => ({ url: SITE_URL + guide.slug, lastModified: new Date(EDITORIAL_DATE), changeFrequency: "monthly" as const, priority: 0.9 })),
    ...["/research", "/authors", ...AUTHORS.map(author => `/authors/${author.slug}`), ...researchPages.map(page => `/research/${page.slug}`)].map(path => ({ url: SITE_URL + path, lastModified: new Date(EDITORIAL_DATE), changeFrequency: "monthly" as const, priority: 0.8 })),
    ...[...CHANGELOG_MONTHS, ...CHANGELOG_DAYS.map(day => day.date)].map(period => ({ url: `${SITE_URL}/changelog/${period}`, lastModified: new Date(EDITORIAL_DATE), changeFrequency: "monthly" as const, priority: 0.4 })),
  ];
  return [...pages.map((page) => editedPages.has(page.url)
    ? { ...page, lastModified: new Date(EDITORIAL_DATE) }
    : updatedPages.has(page.url) ? { ...page, lastModified: new Date("2026-11-02") } : page),
    ...paperPages.map(page => ({ ...page, lastModified: new Date(EDITORIAL_DATE) })), ...releaseFiles, ...additions];
}
