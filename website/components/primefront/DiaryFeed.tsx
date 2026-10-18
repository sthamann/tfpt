"use client";

import {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
  type ReactNode,
} from "react";
import {
  PRIME_FRONT_UPDATES,
  PRIME_FRONT_ARCHIVE_COUNT,
  type PrimeFrontUpdate,
} from "@/lib/primeFront";
import { StatusBadge } from "./StatusBadge";

/* ------------------------------------------------------------------ */
/* Verdict classification (pattern-based; replaces the old 200-entry   */
/* colour map). Every verdict gets exactly one class.                  */
/* ------------------------------------------------------------------ */

type VerdictClass = "win" | "promoted" | "negative" | "open";

const NEGATIVE_RE =
  /DEAD|KILL|DEFLAT|REFUT|FAILS|NO-SIGNAL|DEGENERATE|OUTSIDE/;
const OPEN_RE =
  /RESIST|MISSING|PARTIAL|OPEN|BLOCKED|WILD|VARIES|MIXED|STATUS|RUNNING|TRENDS|HALF-STABLE|MARGINAL|SITS-AT-ZERO|SKELETON|TORSOR/;
const PROMOTED_RE = /PROMOTED|MACHINE-VERIFIED/;

function classify(verdict: string): VerdictClass {
  if (PROMOTED_RE.test(verdict)) return "promoted";
  if (NEGATIVE_RE.test(verdict)) return "negative";
  if (OPEN_RE.test(verdict)) return "open";
  return "win";
}

const CLASS_META: Record<
  VerdictClass,
  { label: string; chip: string; text: string; dot: string }
> = {
  win: {
    label: "Exact / closed",
    chip: "border-sky-400/40 bg-sky-500/10 text-sky-800",
    text: "text-sky-700",
    dot: "bg-sky-400",
  },
  promoted: {
    label: "Promotions",
    chip: "border-emerald-400/40 bg-emerald-500/10 text-emerald-800",
    text: "text-emerald-700",
    dot: "bg-emerald-400",
  },
  negative: {
    label: "Kills / honest negatives",
    chip: "border-rose-400/40 bg-rose-500/10 text-rose-800",
    text: "text-rose-700",
    dot: "bg-rose-400",
  },
  open: {
    label: "Resists / open",
    chip: "border-amber-400/40 bg-amber-500/10 text-amber-800",
    text: "text-amber-800",
    dot: "bg-amber-300",
  },
};

const FILTERS: readonly ("all" | VerdictClass)[] = [
  "all",
  "win",
  "promoted",
  "negative",
  "open",
];

const INITIAL_VISIBLE = 16;
const STEP = 40;

/* ------------------------------------------------------------------ */
/* Fallbacks for entries posted without the new fields.                */
/* ------------------------------------------------------------------ */

function fallbackHeadline(title: string): string {
  const m = title.match(/^[\s\S]{40,240}?[.!?](?=\s)/);
  if (m) return m[0];
  return title.length > 220 ? `${title.slice(0, 200).trimEnd()} …` : title;
}

/* ------------------------------------------------------------------ */
/* Scroll reveal (IntersectionObserver; motion-reduce handled in CSS). */
/* ------------------------------------------------------------------ */

function useInView<T extends HTMLElement>() {
  const ref = useRef<T | null>(null);
  const [inView, setInView] = useState(false);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    if (typeof IntersectionObserver === "undefined") {
      setInView(true);
      return;
    }
    const obs = new IntersectionObserver(
      (entries) => {
        if (entries[0]?.isIntersecting) {
          setInView(true);
          obs.disconnect();
        }
      },
      { rootMargin: "0px 0px -32px 0px", threshold: 0.03 },
    );
    obs.observe(el);
    return () => obs.disconnect();
  }, []);
  return { ref, inView };
}

/* ------------------------------------------------------------------ */

type FeedEntry = PrimeFrontUpdate & { cls: VerdictClass; idx: number };

export function DiaryFeed() {
  const [filter, setFilter] = useState<"all" | VerdictClass>("all");
  const [visibleCount, setVisibleCount] = useState(INITIAL_VISIBLE);
  const [archive, setArchive] = useState<readonly PrimeFrontUpdate[] | null>(
    null,
  );
  const archiveRequested = useRef(false);
  const rootRef = useRef<HTMLDivElement | null>(null);

  /* The older entries live in a separate chunk (lib/primeFrontArchive)
     so they stay out of the route's first-load JS. Fetch them once the
     reader approaches the feed — or on first interaction, whichever
     happens first. */
  const loadArchive = useCallback(() => {
    if (archiveRequested.current) return;
    archiveRequested.current = true;
    import("@/lib/primeFrontArchive")
      .then((m) => setArchive(m.PRIME_FRONT_ARCHIVE))
      .catch(() => {
        archiveRequested.current = false;
      });
  }, []);

  useEffect(() => {
    const el = rootRef.current;
    if (!el) return;
    if (typeof IntersectionObserver === "undefined") {
      loadArchive();
      return;
    }
    const obs = new IntersectionObserver(
      (obsEntries) => {
        if (obsEntries[0]?.isIntersecting) {
          loadArchive();
          obs.disconnect();
        }
      },
      { rootMargin: "1600px 0px" },
    );
    obs.observe(el);
    return () => obs.disconnect();
  }, [loadArchive]);

  const entries = useMemo<FeedEntry[]>(() => {
    const all = archive
      ? [...PRIME_FRONT_UPDATES, ...archive]
      : PRIME_FRONT_UPDATES;
    return all.map((u, idx) => ({
      ...u,
      cls: classify(u.verdict),
      idx,
    }));
  }, [archive]);

  /* Entries not yet downloaded (0 once the archive chunk has arrived). */
  const pendingArchive = archive === null ? PRIME_FRONT_ARCHIVE_COUNT : 0;

  const counts = useMemo(() => {
    const c: Record<"all" | VerdictClass, number> = {
      all: entries.length + pendingArchive,
      win: 0,
      promoted: 0,
      negative: 0,
      open: 0,
    };
    for (const e of entries) c[e.cls] += 1;
    return c;
  }, [entries, pendingArchive]);

  const filtered =
    filter === "all" ? entries : entries.filter((e) => e.cls === filter);
  const visible = filtered.slice(0, visibleCount);

  const groups = useMemo(() => {
    const out: { date: string; items: FeedEntry[] }[] = [];
    for (const e of visible) {
      const last = out[out.length - 1];
      if (last && last.date === e.date) last.items.push(e);
      else out.push({ date: e.date, items: [e] });
    }
    return out;
  }, [visible]);

  const remaining =
    filtered.length -
    visible.length +
    (filter === "all" ? pendingArchive : 0);

  return (
    <div ref={rootRef}>
      <div className="flex flex-wrap items-center gap-2">
        {FILTERS.map((f) => {
          const active = filter === f;
          const meta = f === "all" ? null : CLASS_META[f];
          return (
            <button
              key={f}
              type="button"
              onClick={() => {
                loadArchive();
                setFilter(f);
                setVisibleCount(INITIAL_VISIBLE);
              }}
              aria-pressed={active}
              className={`rounded-full border px-3 py-1 font-mono text-[11px] transition motion-reduce:transition-none ${
                active
                  ? meta
                    ? meta.chip
                    : "border-slate-600/60 bg-slate-800/10 text-slate-900"
                  : "border-slate-300/50 bg-slate-100/40 text-slate-600 hover:border-slate-500 hover:text-slate-800"
              }`}
            >
              {meta ? meta.label : "All runs"}
              <span className="ml-1.5 text-[10px] opacity-70">
                {counts[f]}
                {pendingArchive > 0 && f !== "all" ? "+" : ""}
              </span>
            </button>
          );
        })}
      </div>

      <p className="mt-3 text-sm text-slate-600">
        One entry per completed agent run, newest first. Headlines and key
        facts are distilled from each run&apos;s own record; the full diary
        text of every entry stays available under{" "}
        <span className="text-slate-700">Read the full entry</span>.
      </p>

      <ol className="mt-6 space-y-8">
        {groups.map((g) => (
          <li key={`${g.date}-${g.items[0]?.idx}`}>
            <div className="mb-3 flex items-center gap-3">
              <span
                aria-hidden
                className="h-2 w-2 rounded-full bg-sky-400/80 ring-4 ring-sky-400/10"
              />
              <time
                dateTime={g.date}
                className="font-mono text-xs uppercase tracking-[0.18em] text-slate-600"
              >
                {g.date}
              </time>
              <span className="font-mono text-[10px] text-slate-500">
                {g.items.length} {g.items.length === 1 ? "run" : "runs"}
              </span>
              <span
                aria-hidden
                className="h-px flex-1 bg-gradient-to-r from-slate-300/60 to-transparent"
              />
            </div>
            <ol className="ml-[3px] space-y-3 border-l border-slate-200/70 pl-5 sm:pl-6">
              {g.items.map((e) => (
                <FeedCard key={`${e.date}-${e.idx}`} entry={e} />
              ))}
            </ol>
          </li>
        ))}
      </ol>

      {(remaining > 0 || visibleCount > INITIAL_VISIBLE) && (
        <div className="mt-8 flex flex-wrap items-center gap-3">
          {remaining > 0 && (
            <>
              <button
                type="button"
                onClick={() => {
                  loadArchive();
                  setVisibleCount((c) => c + STEP);
                }}
                className="rounded-full border border-slate-400/60 bg-slate-100/60 px-4 py-1.5 font-mono text-xs text-slate-800 transition hover:border-sky-400/50 hover:text-sky-800 motion-reduce:transition-none"
              >
                Show {Math.min(STEP, remaining)} more
              </button>
              <button
                type="button"
                onClick={() => {
                  loadArchive();
                  setVisibleCount(filtered.length + pendingArchive);
                }}
                className="rounded-full border border-slate-300/50 bg-slate-100/40 px-4 py-1.5 font-mono text-xs text-slate-600 transition hover:border-slate-500 hover:text-slate-800 motion-reduce:transition-none"
              >
                Show all {filtered.length + (filter === "all" ? pendingArchive : 0)}
              </button>
            </>
          )}
          {visibleCount > INITIAL_VISIBLE && (
            <button
              type="button"
              onClick={() => setVisibleCount(INITIAL_VISIBLE)}
              className="rounded-full border border-slate-300/50 bg-slate-100/40 px-4 py-1.5 font-mono text-xs text-slate-600 transition hover:border-slate-500 hover:text-slate-700 motion-reduce:transition-none"
            >
              Collapse
            </button>
          )}
          <span className="font-mono text-[11px] text-slate-500">
            {visible.length} of{" "}
            {filtered.length + (filter === "all" ? pendingArchive : 0)} shown
            {pendingArchive > 0 && " · older runs load automatically"}
          </span>
        </div>
      )}
    </div>
  );
}

/* ------------------------------------------------------------------ */

function FeedCard({ entry }: { entry: FeedEntry }) {
  const [open, setOpen] = useState(false);
  const [mounted, setMounted] = useState(false);
  const { ref, inView } = useInView<HTMLLIElement>();
  const meta = CLASS_META[entry.cls];
  const headline = entry.headline ?? fallbackHeadline(entry.title);
  const hasBody = entry.title.trim().length > headline.trim().length + 10;
  const bodyId = `feed-body-${entry.idx}`;

  return (
    <li
      ref={ref}
      className={`relative rounded-2xl border border-slate-300/45 bg-slate-50/50 p-4 transition duration-500 ease-out motion-reduce:transition-none sm:p-5 ${
        inView ? "translate-y-0 opacity-100" : "translate-y-2 opacity-0"
      }`}
    >
      <span
        aria-hidden
        className={`absolute -left-[27px] top-5 hidden h-1.5 w-1.5 rounded-full sm:block ${meta.dot}`}
      />
      <div className="flex flex-wrap items-center gap-2">
        {entry.part > 0 && (
          <span className="font-mono text-[11px] text-slate-600">
            Teil {entry.part}
          </span>
        )}
        <StatusBadge badge={entry.badge} />
        <span
          className={`ml-auto font-mono text-[10px] font-semibold uppercase tracking-wider ${meta.text}`}
        >
          {entry.verdict}
        </span>
      </div>

      <h3 className="mt-2.5 font-serif text-base leading-snug text-slate-900 sm:text-lg">
        {headline}
      </h3>

      {entry.keyFacts && entry.keyFacts.length > 0 ? (
        <ul className="mt-3 space-y-1.5">
          {entry.keyFacts.map((f, i) => (
            <li
              key={i}
              className="flex gap-2 text-[13px] leading-relaxed text-slate-600"
            >
              <span
                aria-hidden
                className={`mt-[7px] h-1 w-1 shrink-0 rounded-full ${meta.dot} opacity-70`}
              />
              <span className="min-w-0 break-words">{f}</span>
            </li>
          ))}
        </ul>
      ) : (
        <p className="mt-2 text-sm leading-relaxed text-slate-600">
          {entry.summary}
        </p>
      )}

      {hasBody && (
        <>
          {/* The full diary text is mounted only after the first expand, so
              the collapsed bodies stay out of the server-rendered HTML
              (the text itself still ships in this route's JS data). */}
          <div
            id={bodyId}
            className="grid transition-[grid-template-rows] duration-300 ease-out motion-reduce:transition-none"
            style={{ gridTemplateRows: open ? "1fr" : "0fr" }}
          >
            <div className="overflow-hidden">
              {mounted && (
                <div className="mt-3 space-y-3 border-t border-slate-200/60 pt-3">
                  <p className="whitespace-pre-line text-sm leading-relaxed text-slate-700/90">
                    {entry.title}
                  </p>
                  {entry.keyFacts && entry.keyFacts.length > 0 && (
                    <p className="text-[12px] leading-relaxed text-slate-600">
                      {entry.summary}
                    </p>
                  )}
                </div>
              )}
            </div>
          </div>
          <div className="mt-2.5 flex flex-wrap items-center gap-3">
            <button
              type="button"
              onClick={() => {
                setMounted(true);
                setOpen((o) => !o);
              }}
              aria-expanded={open}
              aria-controls={bodyId}
              className="inline-flex items-center gap-1.5 font-mono text-[11px] text-sky-700/90 transition hover:text-sky-800 motion-reduce:transition-none"
            >
              <Chevron open={open} />
              {open ? "Collapse" : "Read the full entry"}
            </button>
            {entry.script && (
              <span className="font-mono text-[10px] text-slate-500">
                {entry.script}
              </span>
            )}
          </div>
        </>
      )}
      {!hasBody && entry.script && (
        <p className="mt-2 font-mono text-[10px] text-slate-500">
          {entry.script}
        </p>
      )}
    </li>
  );
}

function Chevron({ open }: { open: boolean }): ReactNode {
  return (
    <svg
      aria-hidden
      viewBox="0 0 12 12"
      className={`h-3 w-3 transition-transform duration-200 motion-reduce:transition-none ${
        open ? "rotate-90" : ""
      }`}
      fill="none"
      stroke="currentColor"
      strokeWidth="1.5"
    >
      <path d="M4.5 2.5 8 6l-3.5 3.5" strokeLinecap="round" />
    </svg>
  );
}
