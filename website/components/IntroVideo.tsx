"use client";

import { getImageProps } from "next/image";
import { useEffect, useRef, useState } from "react";
import { Play } from "lucide-react";
import { SectionHeader } from "./SectionHeader";
import { cn, SITE_URL } from "@/lib/utils";

const VIDEO_SRC = "/intro/tfpt-intro.mp4";
const POSTER_SRC = "/intro/tfpt-intro-poster.jpeg";
const CAPTIONS_SRC = "/intro/tfpt-intro.en.vtt";

/** Chapter markers — rounded display seconds match the film's six scene starts. */
const CHAPTERS: { t: number; label: string }[] = [
  { t: 0, label: "Compiler" },
  { t: 39, label: "Alpha fixed point" },
  { t: 83, label: "Dual status" },
  { t: 140, label: "August structural wave" },
  { t: 231, label: "Falsification" },
  { t: 269, label: "Predictions" },
];

/**
 * The transcript, grouped by chapter. Mirrored from the video's caption track
 * (tfpt-intro.en.vtt). Rendered as visible (collapsible) text so it is accessible to
 * screen readers and indexable by search/answer engines (the video pixels are
 * not). Keep in sync with /intro/tfpt-intro.en.vtt.
 */
const POSTER_URL = getImageProps({ src: POSTER_SRC, alt: "TFPT film preview", width: 540, height: 304, quality: 75 }).props.src;

const TRANSCRIPT: { heading: string; body: string }[] = [
  {
    heading: "Compiler (0:00)",
    body: "What if the laws of nature are not a list of fitted constants but the output of a tiny compiler? Topological Fixed-Point Theory begins with two declared axioms. The boundary constant c₃ equals one over eight pi and a five slot carrier. From them, it builds D₅ plus A₃, joins the two through a cyclic μ₄ glue and reaches E₈. Then it reads off the discrete standard model structure, the gauge group, three families, hypercharges, and the flavor operators together with dimensionless fixed point readouts. The claim is not that every physical detail is solved, it is narrower and testable. A small machine constructs a large rigid skeleton then names every bridge it still needs.",
  },
  {
    heading: "Alpha fixed point (0:39)",
    body: "The flagship line is alpha inverse, 137.0359992168. The verifier finds it as the unique positive stationary root of the boundary U(1) Ward identity. It is not fitted to the measured value, mutate the permitted terms and the root does not survive. E₈ is the checksum behind the discrete construction, 240 roots lock the D₅ and A₃ sectors into one even, unimodular rank eight lattice. At the time of this recording, 1012 machine-checked verification modules tested this architecture, its numerical identities, its reductions and its failures; the live total is shown on the verification page. Every load-bearing claim has a script and a claim identifier. The status ledger, not the rhetoric, decides whether a line is exact, conditional, open or a kill test.",
  },
  {
    heading: "Dual status (1:23)",
    body: "That discipline forces two status cards to sit side by side. The first is the compiler rest. It has three named interfaces. v_geo, the one dimensionful calibration that pure numbers cannot supply. G_net, the seam-to-E₈ net identification, conditionally closed on its MMST route, but open as an unconditional parent claim. And F_transfer, the typed interfaces that carry selected compiler structures into masses, QCD, baryogenesis and cosmology. Beside it sits a stricter card, the physical theory of everything rest. Its master contract is the AND of eight gates. None is fully closed. They demand the seam continuum, a complete three plus one dimensional local quantum theory, a chiral measure and uniform mirror gap, controlled infrared physics, internally fixed couplings and neutrino dynamics, emergent gravity and the physical state. So the honest sentence is precise. TFPT closes a discrete compiler. It does not yet certify a strict physical theory of everything.",
  },
  {
    heading: "August structural wave (2:20)",
    body: "The August wave did not erase that frontier. It compressed it. First, the seam boundary theory was reduced to one external charged scaling limit theorem. Five supporting lemmas were proved in-house. The cross product step, a uniform growth bound, the first telescoping estimate, the integer D₅ plus A₃ pairings and the order-four outer action. The remaining analytic target is isolated in a 20 plus page memorandum and a send-ready specialist package. Second, the DET16 mirror mechanism is exact on the full 2¹⁶ cluster. A rank one projector, a gap exactly equal to one and all 45 Spin(10) commutators vanishing. A cited stability theorem now supplies a volume uniform finite chain leg. The full dynamical four-dimensional claim remains conditional. Third, the first 3+1-dimensional lattice scaffold now lets gauge content, a chiral wall mirror gapping and the seam clock coexist. The Hamiltonian-class dynamics has a Lieb–Robinson bound, a norm-convergent time evolution, a gauge-invariant quasilocal algebra and ground and thermal states. Phase uniqueness, the limiting gap and infrared universality remain open. Finally, the finite axiom core premises now derive in-house. The remainder is zero modulo the same external MMST identification. P2 remains typed as an axiom and the genuine four-dimensional functional is still a gate. The gain is not a victory slogan, it is convergence. Many vague gaps have become one external theorem, one physical unit and a short list of explicit four-dimensional obligations.",
  },
  {
    heading: "Falsification (3:51)",
    body: "A serious compiler must also record what does not compile. The number-preserving Casimir projector does not isolate the mirror state, its multiplicities explode instead. Eight preregistered Schur-texture constructions all fail because the even seam data forces the wrong degeneracy and the naive extension of the alpha grammar to the strong and weak couplings fails in all 64 tested conventions while the U(1) control survives. These routes are not quietly deleted, they become permanent constraints. The future mechanism must evade the exact reason each one died. That is how the project protects itself from numerology. A failed pattern is evidence, not decoration.",
  },
  {
    heading: "Predictions (4:29)",
    body: "The newest neutrino chain shows how the live frontier is meant to work. As a candidate, it gives a normal-ordering mass sum near 0.0599 electron volts, a leptonic CP phase near 287.7 degrees and a pentagon-class misalignment with phase 288 degrees and angle two pi over 35. At finite level, all three mixing angles land within 0.56 sigma. But the mechanism that turns the seam operator into the flavor operator is still open. There is no seesaw closure. The labels stay candidate and numerical, not exact physics. DESI can press on the mass floor. DUNE can separate 287.7 degrees from the older 240 degree branch. JUNO can test the reactor-angle structure. So is reality compiled? We still do not know. What exists now is more disciplined than an answer by proclamation. A machine-checked compiler with a sharpened map of what remains. Every closed line has a proof object. Every gap has a name. Every prediction has a kill switch.",
  },
];

const fmt = (t: number) => `${Math.floor(t / 60)}:${String(t % 60).padStart(2, "0")}`;

const videoJsonLd = {
  "@context": "https://schema.org",
  "@type": "VideoObject",
  name: "TFPT — Is reality compiled?",
  description:
    "A film on Topological Fixed-Point Theory as a machine-checked discrete compiler, not a completed Theory of Everything. Six scenes cover the two-axiom compiler to E₈, the stationary alpha fixed point, the separate compiler and strict-physical-TOE status cards, the August structural wave, permanently recorded falsifications, and candidate neutrino predictions with DESI, DUNE, and JUNO kill switches.",
  thumbnailUrl: [`${SITE_URL}${POSTER_SRC}`],
  uploadDate: "2026-08-31",
  duration: "PT5M29S",
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

export function IntroVideo() {
  const ref = useRef<HTMLVideoElement>(null);
  const [started, setStarted] = useState(false);

  // Captions are burned into the video (open captions). Browsers remember a
  // user's prior "captions on" preference and would auto-show the <track>,
  // doubling the captions — so default the selectable track off; users can still
  // enable it from the native captions menu.
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
      id="intro-video"
      className="relative scroll-mt-20 py-12 sm:py-16"
      aria-labelledby="intro-video-heading"
    >
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(videoJsonLd) }}
      />
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <SectionHeader
          id="intro-video-heading"
          align="center"
          eyebrow="Start here"
          title="Is reality compiled?"
          description="A 5:29 film on TFPT's machine-checked discrete compiler, its separate open physical-TOE gates, the August structural wave, documented falsifications, and candidate predictions with live kill switches."
        />

        <figure className="mt-10">
          <div className="relative overflow-hidden border border-slate-300/50 bg-slate-50/60">
            <video
              ref={ref}
              className="aspect-video w-full"
              controls
              playsInline
              preload="none"
              poster={POSTER_URL}
              aria-label="TFPT — Is reality compiled? (English, with subtitles)"
              onLoadedMetadata={disableTracks}
            >
              <source src={VIDEO_SRC} type="video/mp4" />
              {/* Captions are burned in (open captions); this selectable track
                  stays available for users who prefer browser-styled subtitles
                  and for indexing — not `default`, to avoid double captions. */}
              <track
                kind="subtitles"
                src={CAPTIONS_SRC}
                srcLang="en"
                label="English"
              />
              Your browser does not support the video tag. You can read the full
              transcript below.
            </video>

            {!started && (
              <button
                type="button"
                onClick={play}
                aria-label="Play the film — Is reality compiled?"
                className="group absolute inset-0 flex items-center justify-center bg-slate-50/30 transition-colors hover:bg-slate-50/15 focus-visible:outline-none"
              >
                <span className="flex h-20 w-20 items-center justify-center rounded-full border border-blue-400/40 bg-blue-500/20 text-blue-800 ring-1 ring-white/10 transition-transform group-hover:scale-105 group-focus-visible:scale-105">
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
                  "inline-flex items-center gap-2 rounded-full border border-slate-300/50 bg-slate-100/60 px-3 py-1.5 text-xs font-medium text-slate-700 transition-colors hover:border-blue-400/40 hover:text-blue-800 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-400/40",
                )}
              >
                <span className="font-mono text-blue-800">{fmt(c.t)}</span>
                {c.label}
              </button>
            ))}
          </nav>

          <figcaption className="mt-3 text-center text-xs text-slate-600">
            English captions burned into the picture (silent track); a selectable
            subtitle track and the full transcript below are generated from the
            same source.
          </figcaption>
        </figure>

        {/* transcript — accessible + indexable */}
        <details className="group mt-8 rounded-2xl border border-slate-300/40 bg-slate-50/40 p-5 sm:p-6">
          <summary className="flex cursor-pointer list-none items-center justify-between text-sm font-semibold text-slate-800 transition-colors hover:text-slate-950">
            <span>Read the full transcript</span>
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
