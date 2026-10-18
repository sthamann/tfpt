"use client";

import { useEffect, useRef, useState } from "react";
import { Play } from "lucide-react";
import { SectionHeader } from "../SectionHeader";
import { cn, SITE_URL } from "@/lib/utils";

const VIDEO_SRC = "/prime-front/prime-front-explained.mp4";
const POSTER_SRC = "/prime-front/prime-front-explained-poster.jpg";
const CAPTIONS_EN_SRC = "/prime-front/prime-front-explained.en.vtt";
const CAPTIONS_DE_SRC = "/prime-front/prime-front-explained.de.vtt";

/** Chapter markers — seconds match the film's ten frames (STORYBOARD.md). */
const CHAPTERS: { t: number; label: string }[] = [
  { t: 0, label: "The music of the primes" },
  { t: 17, label: "Geometry first (E₈ → ζ)" },
  { t: 31, label: "The W1 theorem" },
  { t: 46, label: "Detector & falsifier" },
  { t: 70, label: "Two surface theorems" },
  { t: 89, label: "The Ihara blueprint (Z1)" },
  { t: 108, label: "The measure from the geometry" },
  { t: 124, label: "The corridor & the 0.53" },
  { t: 144, label: "Honest: no proof" },
  { t: 159, label: "Coda: the regional theorem" },
];

/**
 * The English narration, grouped by chapter. Mirrored from the film's caption
 * track — rendered as visible (collapsible) text so it is accessible to screen
 * readers and indexable (the video pixels are not). Keep in sync with
 * /prime-front/prime-front-explained.en.vtt.
 */
const TRANSCRIPT: { heading: string; body: string }[] = [
  {
    heading: "The music of the primes (0:00)",
    body: "The prime numbers look like randomness. But their distribution follows a hidden orchestra: the zeros of the Riemann zeta function. The Riemann Hypothesis says: all of them lie on one single line. Unproven — for more than one hundred and sixty-five years.",
  },
  {
    heading: "Geometry first (0:17)",
    body: "The TFPT builds the E8 lattice from two axioms. Its counting function already knows the primes: each one acts as its own Hecke check channel. And the zeta function appears as a shadow of this geometry.",
  },
  {
    heading: "The W1 theorem (0:31)",
    body: "From this bookkeeping came a window matrix. And it turned out to be something classical: word for word, Suzuki's localized Weil operator. That is the W1 theorem — machine-verified, with one honestly documented erratum.",
  },
  {
    heading: "Detector & falsifier (0:46)",
    body: "The same window form is a detector. Calibrated on solved worlds: Ramanujan graphs — where the analogue is proven — pass the test. Epstein zeta functions — with genuine zeros off the line — break it, exactly as predicted. And the matched filter makes this constructive: any off-line zero would produce a computable witness. The object is falsifiable.",
  },
  {
    heading: "Two surface theorems (1:10)",
    body: "Two theorems stand on the whole surface. The sign of the determinant: unconditionally proven, on all sixty-seven windows — the century-old zero-free region blocks the only escape route. And the margin: sixty of seventy windows, closed with cited classical results.",
  },
  {
    heading: "The Ihara blueprint (1:29)",
    body: "Then, August third: in the graph laboratory, where the analogue is proven, the target decomposition exists exactly — a sum of squares plus a defect. Our window form is built identically. One part is missing: the engine, Z1. Hilbert–Pólya, in window coordinates.",
  },
  {
    heading: "The measure from the geometry (1:48)",
    body: "And the geometry supplies the measure: the prime atoms can be read off, without circularity, from lattice counting alone. The gamma flow forces their masses to per mille — and their positions. But honestly: as a test bench, not as a generator.",
  },
  {
    heading: "The corridor and the 0.53 (2:04)",
    body: "The state today: every mass lives in a corridor with exactly computable edges. The arithmetic does not choose the edge — it chooses an interior point, at zero point five three. An energy extremum hits it to within per mille. The open question: explain the selection inside the corridor.",
  },
  {
    heading: "Honest: no proof (2:24)",
    body: "No proof of RH. This program says so itself, at every step. But the question has never been this small — and never this precise. Almost nine hundred modules, every number machine-checked. This is the Prime Front.",
  },
  {
    heading: "Coda: the regional theorem and the cofinal problem (2:39)",
    body: "Since then, the sigma chain has turned the finite question into a regional theorem: every matrix whose entry data lie in the certified region is positive definite — a proof object, checkable by a tiny program anyone can run. One construction problem remains: a predefined window sequence, cofinal, staying inside the region. The proof object is ready for audit — the RH quantifier is not.",
  },
];

const fmt = (t: number) => `${Math.floor(t / 60)}:${String(t % 60).padStart(2, "0")}`;

const videoJsonLd = {
  "@context": "https://schema.org",
  "@type": "VideoObject",
  name: "The Prime Front — explained in 3 minutes",
  description:
    "A ~3 minute explainer of TFPT's prime / zeta line, end to end: the Riemann Hypothesis in one image (all zeros on one line), the window matrix born from the E8 bookkeeping and proved identical to Suzuki's Weil operator (the W1 theorem, v643), the calibrated detector / falsifier (Ramanujan passes, Epstein breaks at the predicted 0.803; matched-filter witness for any off-line zero), the two surface theorems (det S > 0 unconditionally on 67/67 windows; the T-B margin closed on 60/70 with cited classics), the Ihara blueprint with the one missing part Z1 (Hilbert–Pólya in window coordinates), the measure and masses forced from pure lattice counting, the corridor with the selection point at 0.53 — and the coda: the sigma chain's regional theorem (every matrix with entry data in the certified region is positive definite, a proof object with a tiny checker) with the one open cofinal construction problem. Honest fence throughout: no claim of progress toward RH — the proof object is ready for audit; the RH quantifier is not.",
  thumbnailUrl: [`${SITE_URL}${POSTER_SRC}`],
  uploadDate: "2026-08-13",
  duration: "PT3M5S",
  contentUrl: `${SITE_URL}${VIDEO_SRC}`,
  inLanguage: "en",
  isFamilyFriendly: true,
  transcript: TRANSCRIPT.map((s) => `${s.heading}\n${s.body}`).join("\n\n"),
  publisher: {
    "@type": "Organization",
    name: "TFPT Collaboration",
    url: SITE_URL,
  },
};

export function PrimeFrontVideo() {
  const ref = useRef<HTMLVideoElement>(null);
  const [started, setStarted] = useState(false);

  // Captions are burned into the video (open captions, English). Browsers
  // remember a user's prior "captions on" preference and would auto-show the
  // <track>, doubling the captions — so default the selectable tracks off;
  // users can still enable one from the native captions menu.
  const disableTracks = () => {
    const v = ref.current;
    if (!v) return;
    for (const t of Array.from(v.textTracks)) t.mode = "disabled";
  };
  useEffect(disableTracks, []);

  const play = () => {
    const v = ref.current;
    if (!v) return;
    setStarted(true);
    void v.play();
  };

  const seek = (t: number) => {
    const v = ref.current;
    if (!v) return;
    v.currentTime = t;
    setStarted(true);
    void v.play();
  };

  return (
    <section
      id="prime-front-video"
      className="relative scroll-mt-20 py-12 sm:py-16"
      aria-labelledby="prime-front-video-heading"
    >
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(videoJsonLd) }}
      />
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <SectionHeader
          id="prime-front-video-heading"
          align="center"
          eyebrow="Watch first"
          title="The Prime Front — in 3 minutes"
          description="The whole prime line as a short film: RH in one image, the window matrix that turned out to be Suzuki's Weil operator, the calibrated detector, the two surface theorems, the Ihara blueprint with its one missing part, the honest state — and the coda: the regional theorem with its one open cofinal construction problem. English captions are burned in; the full transcript is below."
        />

        <figure className="mt-10">
          <div className="relative overflow-hidden border border-slate-300/50 bg-slate-50/60">
            <video
              ref={ref}
              className="aspect-video w-full"
              controls
              playsInline
              preload="none"
              poster={POSTER_SRC}
              aria-label="The Prime Front — explained (English, captioned)"
              onLoadedMetadata={disableTracks}
            >
              <source src={VIDEO_SRC} type="video/mp4" />
              {/* Captions are burned in (open captions); these selectable
                  tracks stay available for users who prefer browser-styled
                  subtitles (or the German translation) and for indexing —
                  not `default`, to avoid double captions. */}
              <track
                kind="subtitles"
                src={CAPTIONS_EN_SRC}
                srcLang="en"
                label="English"
              />
              <track
                kind="subtitles"
                src={CAPTIONS_DE_SRC}
                srcLang="de"
                label="Deutsch"
              />
              Your browser does not support the video tag. You can read the
              full transcript below.
            </video>

            {!started && (
              <button
                type="button"
                onClick={play}
                aria-label="Play the film — The Prime Front, explained"
                className="group absolute inset-0 flex items-center justify-center bg-slate-50/30 transition-colors hover:bg-slate-50/15 focus-visible:outline-none"
              >
                <span className="flex h-20 w-20 items-center justify-center rounded-full border border-sky-400/40 bg-sky-500/20 text-sky-800 ring-1 ring-white/10 transition-transform group-hover:scale-105 group-focus-visible:scale-105">
                  <Play size={34} className="ml-1" aria-hidden />
                </span>
              </button>
            )}
          </div>

          {/* chapter markers */}
          <nav
            aria-label="Video chapters"
            className="mt-4 flex flex-wrap justify-center gap-2"
          >
            {CHAPTERS.map((c) => (
              <button
                key={c.t}
                type="button"
                onClick={() => seek(c.t)}
                className={cn(
                  "inline-flex items-center gap-2 rounded-full border border-slate-300/50 bg-slate-100/60 px-3 py-1.5 text-xs font-medium text-slate-700 transition-colors hover:border-sky-400/40 hover:text-sky-800 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-sky-400/40",
                )}
              >
                <span className="font-mono text-sky-700/80">{fmt(c.t)}</span>
                {c.label}
              </button>
            ))}
          </nav>

          <figcaption className="mt-3 text-center text-xs text-slate-600">
            English narration with English captions burned into the picture;
            selectable English and German subtitle tracks and the full
            transcript below are generated from the same source. Every number
            in the film traces to a named, machine-checked module — and the
            film claims no progress toward RH.
          </figcaption>
        </figure>

        {/* transcript — accessible + indexable */}
        <details className="group mt-8 rounded-2xl border border-slate-300/40 bg-slate-50/40 p-5 sm:p-6">
          <summary className="flex cursor-pointer list-none items-center justify-between text-sm font-semibold text-slate-800 transition-colors hover:text-slate-950">
            <span>Read the transcript</span>
            <span className="text-slate-600 transition-transform group-open:rotate-180">
              ⌄
            </span>
          </summary>
          <div className="prose-tfpt mt-5 space-y-5">
            {TRANSCRIPT.map((s) => (
              <div key={s.heading}>
                <h3 className="font-serif text-base font-semibold text-slate-900">
                  {s.heading}
                </h3>
                <p className="mt-1 text-sm leading-relaxed text-slate-700">
                  {s.body}
                </p>
              </div>
            ))}
          </div>
        </details>
      </div>
    </section>
  );
}
