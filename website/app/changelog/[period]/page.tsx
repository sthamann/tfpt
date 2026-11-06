import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ChangelogBrowser } from "@/components/ChangelogBrowser";
import { CHANGELOG_MACROS } from "@/lib/changelog";
import {
  CHANGELOG_DAYS,
  CHANGELOG_MONTHS,
  changelogDayEntries,
  changelogMonthEntries,
  changelogMonthLabel,
} from "@/lib/changelog-navigation";
import { SITE_URL } from "@/lib/utils";

type Props = { params: Promise<{ period: string }> };

export const dynamicParams = false;

export function generateStaticParams() {
  return [
    ...CHANGELOG_MONTHS.map((period) => ({ period })),
    ...CHANGELOG_DAYS.map(({ date: period }) => ({ period })),
  ];
}

function periodLabel(period: string) {
  if (CHANGELOG_MONTHS.includes(period)) return changelogMonthLabel(period);
  if (CHANGELOG_DAYS.some((day) => day.date === period)) return period;
  return null;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { period } = await params;
  const label = periodLabel(period);
  if (!label) return {};
  const title = `TFPT Publication History: ${label}`;
  const description = `Read the original TFPT publication entries for ${label}, with their dated wording, mathematical expressions and recorded status markers.`;
  const url = `${SITE_URL}/changelog/${period}`;
  return {
    title,
    description,
    alternates: { canonical: url },
    openGraph: { title, description, url, type: "website" },
    twitter: { title, description, card: "summary_large_image" },
  };
}

export default async function ChangelogArchivePage({ params }: Props) {
  const { period } = await params;
  const label = periodLabel(period);
  if (!label) notFound();
  const isMonth = CHANGELOG_MONTHS.includes(period);
  const month = period.slice(0, 7);
  const monthIndex = CHANGELOG_MONTHS.indexOf(month);
  const olderMonth = CHANGELOG_MONTHS[monthIndex + 1];
  const newerMonth = monthIndex > 0 ? CHANGELOG_MONTHS[monthIndex - 1] : undefined;
  const days = CHANGELOG_DAYS.filter((day) => day.date.startsWith(month));

  return <article className="reference-page">
    <header className="reference-header">
      <h1>Publication history: {label}</h1>
      <p>Original publication entries retain their wording and recorded status. Follow the current research history for later findings and revisions.</p>
      <nav className="reference-links" aria-label="Publication archive navigation">
        <Link href="/changelog">Current research and publication history</Link>
        {!isMonth && <Link href={"/changelog/" + month}>{changelogMonthLabel(month)}</Link>}
        <a href="/papers/changelog.pdf">Complete publication log PDF</a>
      </nav>
    </header>

    {isMonth ? <section className="reference-section">
      <h2>Recorded days in {label}</h2>
      <p>{changelogMonthEntries(month).length.toLocaleString("en-US")} publication entries across {days.length} recorded days. Open a day to read its complete original entries and formulas.</p>
      <div className="reference-rows">
        {days.map((day) => <article key={day.date}>
          <h3><Link href={"/changelog/" + day.date} prefetch={false}><time dateTime={day.date}>{day.date}</time></Link></h3>
          <p>{day.count} {day.count === 1 ? "publication entry" : "publication entries"}</p>
          <ul>
            {changelogMonthEntries(month).filter((entry) => entry.date === day.date).map((entry) => <li key={entry.anchor}>
              <Link href={`/changelog/${day.date}#${entry.anchor}`} prefetch={false}>{entry.lead || entry.label}</Link>
            </li>)}
          </ul>
        </article>)}
      </div>
      <nav className="reference-links" aria-label="Adjacent publication months">
        {olderMonth && <Link href={"/changelog/" + olderMonth} prefetch={false}>Older: {changelogMonthLabel(olderMonth)}</Link>}
        {newerMonth && <Link href={"/changelog/" + newerMonth} prefetch={false}>Newer: {changelogMonthLabel(newerMonth)}</Link>}
      </nav>
    </section> : <section className="reference-section" aria-label={"Publication entries for " + period}>
      <ChangelogBrowser days={CHANGELOG_DAYS} selectedDay={period} entries={changelogDayEntries(period)} macros={CHANGELOG_MACROS} />
    </section>}
  </article>;
}
