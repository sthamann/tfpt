import { PublicationArchive } from "@/components/PublicationArchive";
import { pageMetadata } from "@/lib/seo";
import type { Metadata } from "next";
import Link from "next/link";
import {
  ChangelogBrowser,
} from "@/components/ChangelogBrowser";
import {
  CHANGELOG,
  CHANGELOG_COUNT,
  CHANGELOG_MACROS,
} from "@/lib/changelog";
import { REPO_URL } from "@/lib/utils";
import { SITE_VERSION } from "@/lib/version";
import { semanticAtlas } from "@/lib/semantic";
import summary from "@/lib/research-summary.json";
import { permanentRedirect } from "next/navigation";
import { CHANGELOG_DAYS, CHANGELOG_MONTHS, changelogDayEntries, changelogMonthLabel } from "@/lib/changelog-navigation";

const latest = CHANGELOG[0]?.date ?? "";
const earliest = CHANGELOG[CHANGELOG.length - 1]?.date ?? "";

export const metadata: Metadata = pageMetadata("/changelog");

// --------------------------------------------------------------------------
// The current page renders one day. Calendar archives expose every original
// publication entry; the global search index loads only when a filter is used.
// --------------------------------------------------------------------------

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
  const sp = await searchParams;
  if (sp.day && CHANGELOG_DAYS.some((day) => day.date === sp.day)) {
    permanentRedirect("/changelog/" + sp.day);
  }
  const selectedDay = CHANGELOG_DAYS[0]?.date ?? "";
  const dayEntries = changelogDayEntries(selectedDay);

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
          </article>;
        })}
      </div> : <p>No original attempt in this snapshot carries an explicit calendar date. The reviewed questions above remain the entry points to current research.</p>}
    </section>

    <section className="reference-section" id="publication-history">
      <h2>The dated publication log</h2>
      <p>This log covers {earliest} through {latest}: {CHANGELOG_COUNT.toLocaleString("en-US")} entries across {CHANGELOG_DAYS.length.toLocaleString("en-US")} recorded days in the TFPT {SITE_VERSION} publication history. Its source is <code>changelog.tex</code>. Later research can appear in the reviewed snapshot above before a new publication entry is written.</p>
      <p className="reference-note">Original entries retain their dated wording, including statuses and numerical inventories from that period. Use the current result record to inspect subsequent revisions or scope corrections.</p>
      <nav className="reference-links" aria-label="Publication log sources">
        <a href="/papers/changelog.pdf">Read the publication log PDF</a>
        <a href={REPO_URL + "/blob/main/changelog.tex"}>Inspect the original publication source</a>
      </nav>
      <nav className="reference-links" aria-label="Publication history by month">
        {CHANGELOG_MONTHS.map((month) => <Link key={month} href={"/changelog/" + month} prefetch={false}>{changelogMonthLabel(month)}</Link>)}
      </nav>
      <div className="mt-6">
        <ChangelogBrowser
          days={CHANGELOG_DAYS}
          selectedDay={selectedDay}
          entries={dayEntries}
          macros={CHANGELOG_MACROS}
        />
      </div>
    </section>
    <PublicationArchive/>
  </article>;
}
