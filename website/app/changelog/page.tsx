import { PublicationArchive } from "@/components/PublicationArchive";
import { pageMetadata } from "@/lib/seo";
import type { Metadata } from "next";
import Link from "next/link";
import {
  ChangelogBrowser,
  type ChangelogDayEntry,
  type ChangelogIndexEntry,
  type DayMeta,
} from "@/components/ChangelogBrowser";
import {
  CHANGELOG,
  CHANGELOG_COUNT,
  CHANGELOG_MACROS,
  type ChangelogNode,
} from "@/lib/changelog";
import { REPO_URL } from "@/lib/utils";
import { SITE_VERSION } from "@/lib/version";
import { semanticAtlas } from "@/lib/semantic";
import summary from "@/lib/research-summary.json";

const latest = CHANGELOG[0]?.date ?? "";
const earliest = CHANGELOG[CHANGELOG.length - 1]?.date ?? "";

export const metadata: Metadata = pageMetadata("/changelog");

// --------------------------------------------------------------------------
// Server-side derivation of the browsing data. The full CHANGELOG (node trees,
// ~2 MB) stays server-only; the client receives the tiny day list, a compact
// searchable index and just the selected day's full entries.
// --------------------------------------------------------------------------

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

/** Calendar dates come only from the attempt metadata, never an identifier or filename. */
function recordedDate(value: string | null): string | null {
  const match = value?.match(/^(\d{4})-?(\d{2})-?(\d{2})(?:T.*)?$/);
  if (!match) return null;
  const iso = [match[1], match[2], match[3]].join("-");
  const parsed = new Date(iso + "T00:00:00Z");
  return Number.isFinite(parsed.getTime()) && parsed.toISOString().slice(0, 10) === iso ? iso : null;
}

export default async function ChangelogPage({
  searchParams,
}: {
  searchParams: Promise<{ day?: string }>;
}) {
  const derived = CHANGELOG.map((e, i) => deriveEntry(e, i));

  // Day list (newest first, CHANGELOG order preserved), with per-day counts.
  const days: DayMeta[] = [];
  const dayPos = new Map<string, number>();
  for (const e of derived) {
    const at = dayPos.get(e.date);
    if (at === undefined) {
      dayPos.set(e.date, days.length);
      days.push({ date: e.date, count: 1 });
    } else {
      days[at].count += 1;
    }
  }

  const sp = await searchParams;
  const selectedDay =
    sp.day && dayPos.has(sp.day) ? sp.day : days[0]?.date ?? "";

  const dayEntries: ChangelogDayEntry[] = derived
    .filter((e) => e.date === selectedDay)
    .map((e) => ({
      label: e.label,
      enumr: e.enumr,
      heading: e.heading,
      items: e.items,
      anchor: e.anchor,
      area: e.area,
    }));

  const index: ChangelogIndexEntry[] = derived.map((e) => ({
    date: e.date,
    label: e.label,
    enumr: e.enumr,
    lead: e.lead,
    text: e.text,
    anchor: e.anchor,
    tags: e.tags,
    area: e.area,
  }));

  const atlas = semanticAtlas();
  const currentQuestions = [
    "problem:atlas-clock-defect-and-operational-reconstruction",
    "problem:automated-operator-source-synthesis",
    "problem:marked-seam-monodromy-and-lattice-lifts",
  ].flatMap((id) => {
    const question = atlas.problems.find((item) => item.id === id);
    return question ? [question] : [];
  });
  const datedAttempts = atlas.attempts.flatMap((attempt) => {
    const date = recordedDate(attempt.date);
    return date ? [{ ...attempt, recordedDate: date }] : [];
  }).sort((a, b) => b.recordedDate.localeCompare(a.recordedDate) || a.id.localeCompare(b.id)).slice(0, 8);

  return <article className="reference-page">
    <header className="reference-header">
      <h1>Research and publication history</h1>
      <p>Follow the current research snapshot alongside the dated publication log. An original attempt, a reviewed finding and a published change are distinct records, each with its own date and scope.</p>
    </header>

    <section className="reference-section" id="research-snapshot">
      <h2>The current research snapshot</h2>
      <p>The snapshot generated <time dateTime={summary.generatedAt}>{summary.generatedAt.slice(0, 10)}</time> contains {summary.counts.reviewedFindings.toLocaleString("en-US")} source reviewed findings and {summary.counts.ledgerActive.toLocaleString("en-US")} active published ledger claims. These records retain their original premises and status. The snapshot date describes this export; it does not date every discovery.</p>
      <p className="reference-note">{summary.counts.findingStatuses.established_scoped.toLocaleString("en-US")} findings established in scope, {summary.counts.findingStatuses.conditional.toLocaleString("en-US")} conditional findings and {summary.counts.findingStatuses.excluded_scoped.toLocaleString("en-US")} scoped exclusions. The inventory is separate from a fresh verification run.</p>
      <div className="reference-rows">
        {currentQuestions.map((question) => {
          const related = question.findingIds.slice(-2).flatMap((id) => {
            const finding = atlas.findings.find((item) => item.id === id);
            return finding ? [finding] : [];
          });
          return <article key={question.id}>
            <h3><Link href={"/results?question=" + encodeURIComponent(question.id)}>{question.titleEN}</Link></h3>
            <p>{question.questionEN}</p>
            <nav className="reference-links" aria-label={"Reviewed entry points for " + question.titleEN}>
              {related.map((finding) => <Link key={finding.id} href={"/results?record=" + encodeURIComponent(finding.id)}>{finding.titleEN}</Link>)}
            </nav>
            <PublicationArchive/>
  </article>;
        })}
      </div>
      <nav className="reference-links" aria-label="Research snapshot sources">
        <Link href="/results">Explore the questions and reviewed results</Link>
        <a href="/research/coverage.json">Inspect the snapshot coverage record</a>
      </nav>
    </section>

    <section className="reference-section" id="dated-attempts">
      <h2>Recent dated attempt records</h2>
      <p>These dates are stored on the original attempt records. Related findings may have been reviewed later. The date of an attempt is not assigned to every result connected to it.</p>
      <p className="reference-note">Recorded verdicts describe historical attempts. A reported PASS is separate from a reviewed theorem, a fresh run or completion of the parent physical goal.</p>
      {datedAttempts.length ? <div className="reference-rows">
        {datedAttempts.map((attempt) => {
          const related = attempt.reviewedFindingIds.slice(-2).flatMap((id) => {
            const finding = atlas.findings.find((item) => item.id === id);
            return finding ? [finding] : [];
          });
          return <article key={attempt.id}>
            <p className="reference-note">Recorded attempt date: <time dateTime={attempt.recordedDate}>{attempt.recordedDate}</time></p>
            <h3>{attempt.titleEN.replace(/[-_]\d{8}$/, "").replace(/[-_]/g, " ")}</h3>
            <nav className="reference-links" aria-label={"Evidence for " + attempt.titleEN}>
              <Link href={"/results?tab=history&search=" + encodeURIComponent(attempt.id)}>Read the historical record and original sources</Link>
              {related.map((finding) => <Link key={finding.id} href={"/results?record=" + encodeURIComponent(finding.id)}>{finding.titleEN}</Link>)}
            </nav>
            <PublicationArchive/>
  </article>;
        })}
      </div> : <p>No original attempt in this snapshot carries an explicit calendar date. The reviewed questions above remain the entry points to current research.</p>}
    </section>

    <section className="reference-section" id="publication-history">
      <h2>The dated publication log</h2>
      <p>This log covers {earliest} through {latest}: {CHANGELOG_COUNT.toLocaleString("en-US")} entries across {days.length.toLocaleString("en-US")} recorded days in the TFPT {SITE_VERSION} publication history. Its source is <code>changelog.tex</code>. Later research can appear in the reviewed snapshot above before a new publication entry is written.</p>
      <p className="reference-note">Original entries retain their dated wording, including statuses and numerical inventories from that period. Use the current result record to inspect subsequent revisions or scope corrections.</p>
      <nav className="reference-links" aria-label="Publication log sources">
        <a href="/papers/changelog.pdf">Read the publication log PDF</a>
        <a href={REPO_URL + "/blob/main/changelog.tex"}>Inspect the original publication source</a>
      </nav>
      <details open={Boolean(sp.day)} className="mt-6">
        <summary>Browse the original publication entries by day</summary>
        <ChangelogBrowser
          days={days}
          index={index}
          selectedDay={selectedDay}
          entries={dayEntries}
          macros={CHANGELOG_MACROS}
        />
      </details>
    </section>
    <PublicationArchive/>
  </article>;
}
