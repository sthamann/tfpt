import { CHANGELOG, type ChangelogNode } from "@/lib/changelog";
import type { ChangelogDayEntry, ChangelogIndexEntry, DayMeta } from "@/components/ChangelogBrowser";

function nodesToText(nodes: ChangelogNode[]): string {
  return nodes
    .map((n) => {
      if (n.k === "t" || n.k === "m" || n.k === "c") return n.v ?? "";
      if (n.k === "s") return `[${n.v ?? "O"}]`;
      if ((n.k === "b" || n.k === "i") && n.c) return nodesToText(n.c);
      return "";
    })
    .join("");
}

function collectMarkers(nodes: ChangelogNode[], into: Set<string>): void {
  for (const n of nodes) {
    if (n.k === "s" && n.v) into.add(n.v);
    if ((n.k === "b" || n.k === "i") && n.c) collectMarkers(n.c, into);
  }
}

function hasModuleCode(nodes: ChangelogNode[]): boolean {
  return nodes.some((n) => {
    if (n.k === "c" && n.v && /^v\d+/.test(n.v)) return true;
    if ((n.k === "b" || n.k === "i") && n.c) return hasModuleCode(n.c);
    return false;
  });
}

const EXPERIMENT_RE = /experiments?\s+level\s+only|experiment-level|experiments\//i;
const EDITORIAL_RE = /\beditorial\b/i;

/** Assign an entry to a theory area from its claim ids / keywords. Heuristic
 *  navigational aid (not a load-bearing claim); first match wins. `text` is the
 *  already-lowercased search blob. */
function classifyArea(text: string, tags: string[]): string {
  if (/celest\.|celestial|twistor|\bwp5|bcov|\bwoit\b|costello|burns holograph/.test(text))
    return "celestial";
  if (/seam\.|seam\b|qgeo|pillowcase|\bclock\b|m(?:ö|oe)bius|\bfock\b|orbifold|\bdeck\b|kronheimer|steklov|\bmarks?\b/.test(text))
    return "seam";
  if (/\bp2\.|ax\.p2|\bcarrier\b|g_car|g_\{|partition corollary|deligne|weight[- ]typing/.test(text))
    return "p2";
  if (/alpha\.quillen|em\.ward|fine-structure|quillen|determinant line/.test(text))
    return "em";
  if (/flav\.|fr\.rarekaon|\bckm\b|koide|yukawa|\bpmns\b|lepton|quark|neutrino|\bkaon\b|jarlskog|cabibbo|seesaw|clebsch/.test(text))
    return "flavor";
  if (/cosmo\.|gravit|einstein|\blambda\b|inflation|leptogenesis|axion|n_s|scalaron|entropic|hubble|\bh_?0\b|reheating|running/.test(text))
    return "gravity";
  if (/\bhor\.|horizon|nariai|black[- ]hole|\bbh\b|\beht\b/.test(text))
    return "horizon";
  if (tags.includes("experiment") || /\bfrb\b|pulsar|\brxte\b|\bnicer\b|hfqpo|glitch|\bvela\b|recovery-comb|e8-ladder|efimov|burst/.test(text))
    return "experiment";
  if (tags.includes("editorial") || /registry|manifest|wolfram|website|currency sweep|cross-reference|gitignore|consolidation/.test(text))
    return "infra";
  return "core";
}

/** Extract the enumerator (e.g. "XXIII") that make_changelog_web.py appends to
 *  the date label as "YYYY-MM-DD · XXIII". */
function enumOf(label: string): string {
  const parts = label.split(" \u00b7 ");
  return parts.length > 1 ? parts[parts.length - 1].trim() : "";
}

function clip(s: string, n: number): string {
  const t = s.replace(/\s+/g, " ").trim();
  return t.length > n ? t.slice(0, n).trimEnd() + "\u2026" : t;
}

interface DerivedEntry {
  gi: number;
  date: string;
  label: string;
  enumr: string;
  heading: ChangelogNode[];
  items: ChangelogNode[][];
  anchor: string;
  lead: string;
  text: string;
  tags: string[];
  area: string;
}

function deriveEntry(entry: (typeof CHANGELOG)[number], gi: number): DerivedEntry {
  const allNodes: ChangelogNode[] = [
    ...entry.heading,
    ...entry.items.flat(),
  ];
  const fullText = [entry.heading, ...entry.items]
    .map((nodes) => nodesToText(nodes))
    .join(" ");

  const markers = new Set<string>();
  collectMarkers(allNodes, markers);

  const tags: string[] = [];
  if (hasModuleCode(allNodes)) tags.push("module");
  if (EDITORIAL_RE.test(fullText)) tags.push("editorial");
  if (EXPERIMENT_RE.test(fullText)) tags.push("experiment");
  for (const m of markers) tags.push(m);

  const leadSource =
    entry.heading.length > 0
      ? nodesToText(entry.heading)
      : entry.items.length > 0
        ? nodesToText(entry.items[0])
        : "";

  const text = clip(fullText, 900).toLowerCase();

  return {
    gi,
    date: entry.date,
    label: entry.dateLabel,
    enumr: enumOf(entry.dateLabel),
    heading: entry.heading,
    items: entry.items,
    anchor: `cl-${gi}`,
    lead: clip(leadSource, 220),
    text,
    tags,
    area: classifyArea(text, tags),
  };
}


const derived = CHANGELOG.map((entry, index) => deriveEntry(entry, index));

/** Calendar archives are derived from the canonical generated publication log. */
export const CHANGELOG_DAYS: DayMeta[] = Array.from(
  new Set(derived.map((entry) => entry.date)),
).sort((a, b) => b.localeCompare(a)).map((date) => ({
  date,
  count: derived.filter((entry) => entry.date === date).length,
}));

export const CHANGELOG_MONTHS = Array.from(
  new Set(CHANGELOG_DAYS.map((day) => day.date.slice(0, 7))),
);

export function changelogDayEntries(date: string): ChangelogDayEntry[] {
  return derived.filter((entry) => entry.date === date).map((entry) => ({
    label: entry.label,
    enumr: entry.enumr,
    heading: entry.heading,
    items: entry.items,
    anchor: entry.anchor,
    area: entry.area,
  }));
}

export function changelogSearchIndex(): ChangelogIndexEntry[] {
  return derived.map(({ date, label, enumr, lead, text, anchor, tags, area }) => ({
    date, label, enumr, lead, text, anchor, tags, area,
  }));
}

export function changelogMonthEntries(month: string) {
  return derived.filter((entry) => entry.date.startsWith(month));
}

export function changelogMonthLabel(month: string): string {
  return new Intl.DateTimeFormat("en-US", { month: "long", year: "numeric", timeZone: "UTC" })
    .format(new Date(month + "-01T00:00:00Z"));
}
