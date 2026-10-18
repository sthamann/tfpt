import type { Metadata } from "next";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { SITE_URL } from "@/lib/utils";
import { SCRIPT_TOTAL } from "@/lib/suite";
import {
  PRIME_FRONT_SECTION_GROUPS,
  PRIME_FRONT_UPDATES,
  PRIME_FRONT_ARCHIVE_COUNT,
} from "@/lib/primeFront";
import { HonestyBanner } from "@/components/primefront/HonestyBanner";
import { StorySixty } from "@/components/primefront/StorySixty";
import { WhereWeAre } from "@/components/primefront/WhereWeAre";
import { DiarySection } from "@/components/primefront/DiarySection";
import { CompilerSchematic } from "@/components/primefront/CompilerSchematic";
import { ShellCensus } from "@/components/primefront/ShellCensus";
import { AperyBridge } from "@/components/primefront/AperyBridge";
import { KillChainTimeline } from "@/components/primefront/KillChainTimeline";
import { PrimeDetector } from "@/components/primefront/PrimeDetector";
import { NeighborStepping } from "@/components/primefront/NeighborStepping";
import { TwoMelodies } from "@/components/primefront/TwoMelodies";
import { CenterAtlas } from "@/components/primefront/CenterAtlas";
import { SpectrumLadder } from "@/components/primefront/SpectrumLadder";
import { WeilArcMap } from "@/components/primefront/WeilArcMap";
import { ModuleLadder } from "@/components/primefront/ModuleLadder";
import { ConeCoverage } from "@/components/primefront/ConeCoverage";
import { DoorsPanel } from "@/components/primefront/DoorsPanel";
import { HeatFamilyBalance } from "@/components/primefront/HeatFamilyBalance";
import { CrossingMap } from "@/components/primefront/CrossingMap";
import { HandoverCrossing } from "@/components/primefront/HandoverCrossing";
import { InstrumentRace } from "@/components/primefront/InstrumentRace";
import { ClosureMapGrid } from "@/components/primefront/ClosureMapGrid";
import { TwoDoorsConvergence } from "@/components/primefront/TwoDoorsConvergence";
import { ReductionCascade } from "@/components/primefront/ReductionCascade";
import { TelescopeRungs } from "@/components/primefront/TelescopeRungs";
import { DiaryFeed } from "@/components/primefront/DiaryFeed";
import { W1DictionaryMap } from "@/components/primefront/W1DictionaryMap";
import { HodgeConeMap } from "@/components/primefront/HodgeConeMap";
import { IharaBlueprintViz } from "@/components/primefront/IharaBlueprintViz";
import { PrimeFrontVideo } from "@/components/primefront/PrimeFrontVideo";
import { TBWindowMap } from "@/components/primefront/TBWindowMap";
import { KorridorViz } from "@/components/primefront/KorridorViz";
import { DeckSectorViz } from "@/components/primefront/DeckSectorViz";
import { StatusBadge } from "@/components/primefront/StatusBadge";
import { VerbatimRecap } from "@/components/primefront/VerbatimRecap";

/** One diary entry per completed agent run (inline feed + lazy archive). */
const DIARY_RUN_COUNT = PRIME_FRONT_UPDATES.length + PRIME_FRONT_ARCHIVE_COUNT;

export const metadata: Metadata = {
  title: "The Prime Front — Research Diary",
  description: `A plain-language research diary of TFPT's prime / zeta line. The story in short: primes → the classical explicit formula → a window matrix built from primes inside the theory's E8 bookkeeping → proved identical to Suzuki's Weil operator (the W1 theorem, v643, machine-verified after a same-day erratum) → one open positivity statement (W3) where everything RH-hard still sits. Also: the uniform constant C = 1, the Lorentz congruence, E8 as a literal error-correcting code, and the G31 reflection group. Machine-verified modules v535–v970 inside a ${SCRIPT_TOTAL}-script suite. No claim of progress toward the Riemann Hypothesis.`,
  keywords: [
    "TFPT prime front",
    "E8 census",
    "Hecke from geometry",
    "Weil structure",
    "relative trace formula",
    "uniform constant C = 1",
    "Lorentz congruence",
    "Hodge chamber",
    "E8 error-correcting code",
    "Shephard-Todd G31",
    "Suzuki screw function",
    "Weil operator W1",
    "zeta research diary",
    "Stefan Hamann",
  ],
  alternates: { canonical: `${SITE_URL}/prime-front` },
  openGraph: {
    images: [{ url: `${SITE_URL}/opengraph-image`, width: 1200, height: 630, alt: "TFPT — Topological Fixed-Point Theory" }],
    type: "article",
    title: "The Prime Front — TFPT research diary",
    description:
      "Primes, the E8 census, and the load-bearing modules v535–v970: Hecke from geometry, the phase-2 certified map, C = 1 exception-free, the Lorentz congruence, the E8 code dictionary, and the Suzuki W1 identification theorem-closed (after a same-day convention erratum). Honest fence: closing W1 does not move W3. No claim of progress toward the Riemann Hypothesis.",
    url: `${SITE_URL}/prime-front`,
    siteName: "TFPT — Topological Fixed-Point Theory",
    locale: "en_US",
  },
  twitter: {
    images: [`${SITE_URL}/opengraph-image`],
    card: "summary_large_image",
    title: "The Prime Front — TFPT",
    description:
      "Research diary of the prime / zeta line. Machine-verified v535–v970: the induction sprint, the phase-2 map, C = 1, the Lorentz bridge, the E8 code, and the Suzuki W1 theorem (erratum-corrected one-scalar dictionary) — with the RH-hard step W3 explicitly open. Not RH evidence.",
  },
};

export default function PrimeFrontPage() {
  return (
    <>
      <section className="relative isolate overflow-hidden pt-12 pb-8 sm:pt-16">
        <div aria-hidden className="absolute inset-0 grid-bg pointer-events-none" />
        <div
          aria-hidden
          className="absolute -top-40 left-1/2 -z-10 h-[520px] w-[1000px] -translate-x-1/2 rounded-full opacity-35 blur-3xl"
          style={{
            background:
              "radial-gradient(closest-side, rgba(56,189,248,0.28), rgba(16,185,129,0.12), transparent)",
          }}
        />
        <div className="relative mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
          <nav aria-label="Breadcrumb" className="mb-6">
            <Link
              prefetch={false}
              href="/"
              className="inline-flex items-center gap-1.5 text-sm text-slate-600 transition-colors hover:text-slate-800"
            >
              <ArrowLeft size={14} aria-hidden />
              Back to overview
            </Link>
          </nav>

          <p className="font-mono text-[11px] uppercase tracking-[0.2em] text-sky-700/90">
            Research diary · {DIARY_RUN_COUNT} agent runs · 6638+ sandbox
            checks · suite {SCRIPT_TOTAL} scripts
          </p>
          <h1 className="mt-3 font-serif text-4xl font-semibold leading-tight text-slate-950 sm:text-5xl md:text-6xl">
            The Prime Front
          </h1>
          <p className="mt-4 max-w-2xl text-base leading-relaxed text-slate-700 sm:text-lg">
            The Prime Front is TFPT&apos;s number-theory line: a research
            diary of how the compiler&apos;s E₈ bookkeeping kept producing
            the classical machinery of primes. One identification is now a
            machine-verified theorem; the RH-hard step is honestly open.
            This page tells the whole story in ordinary language.
          </p>

          <StorySixty />

          <WhereWeAre />

          <div className="mt-6">
            <HonestyBanner />
          </div>

          <BlindPrimeCallout />

          <nav aria-label="On this page" className="mt-8 space-y-3">
            {PRIME_FRONT_SECTION_GROUPS.map((g) => (
              <div
                key={g.label}
                className="flex flex-wrap items-baseline gap-2"
              >
                <span className="w-full font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600 sm:w-44 sm:shrink-0">
                  {g.label}
                </span>
                <span className="flex min-w-0 flex-wrap gap-2">
                  {g.sections.map((s) => (
                    <a
                      key={s.id}
                      href={`#${s.id}`}
                      className="rounded-full border border-slate-300/50 bg-slate-100/40 px-3 py-1 font-mono text-[11px] text-slate-600 transition hover:border-slate-500 hover:text-slate-800"
                    >
                      {s.label}
                    </a>
                  ))}
                </span>
              </div>
            ))}
          </nav>
        </div>
      </section>

      <PrimeFrontVideo />

      <BigPictureSection />

      {/* 01 — Suzuki W1 */}
      <DiarySection
        id="suzuki-w1"
        plain="The matrix this diary builds from primes turned out to be, exactly, the matrix of an operator the number theorist Suzuki had defined independently — and that identification is now a proved, machine-checked theorem."
        eyebrow="01 · The Suzuki identification · v630 / v631 / v640–v644 / v648"
        title="W1 closes as a theorem — after an honest erratum"
        badge="machine-verified"
        visual={<W1DictionaryMap />}
      >
        <p>
          The RH architecture preregistered in v624 (contract
          PRIME.WEIL.OPERATOR.01, citations web-verified: Suzuki
          arXiv:2606.09096 and 2607.24830) starts with W1: identify the TFPT
          window form with the Galerkin matrix of Suzuki&apos;s localized
          Weil operator. First contact (v630):{" "}
          <strong className="font-medium text-emerald-800">
            the atom layers are the same object, literally
          </strong>{" "}
          — positions log n, weights Λ(n)/√n, exact on all 40 atoms — while
          the smooth-layer comparison measured a non-scalar conversion: the
          preregistered residual, with data.
        </p>
        <p>
          Hours later, v631 resolved it: the residual{" "}
          <em>is the zeta pole term</em>, and the follow-up rounds made the
          dictionary sturdy — v640 closed the boundary cells symbolically,
          v641 froze the dictionary and ran it unchanged on three fresh
          windows (a preregistered kill test:{" "}
          <strong className="font-medium text-slate-800">portable</strong>),
          v642 lifted it to the full quadratic form at operator level.
        </p>
        <p>
          <strong className="font-medium text-amber-800">
            Erratum (2026-08-02, corrected the same day):
          </strong>{" "}
          that chain read Suzuki&apos;s eq. (1.3) with Lerch coefficient −1;
          the paper&apos;s own §2.2 data lock +1/4 (v643, check C0.1). All
          the chain&apos;s identities are correct identities of its kernel
          g̃ = g − (5/4)·Lerch, and every measured number transfers verbatim
          via the exact identity cgal(g̃) = −4·cgal(g) — only the labels
          change: Suzuki&apos;s own smooth layer is{" "}
          <span className="font-mono text-slate-800">+ρ</span> (not −4ρ),
          the dictionary is the{" "}
          <strong className="font-medium text-slate-800">
            single scalar +1/D on both layers
          </strong>{" "}
          (sign-compatible with positivity), and the origin constant
          vanishes, κ = 0 exactly.
        </p>
        <p>
          On the corrected reading, v643 proves the{" "}
          <strong className="font-medium text-emerald-800">
            measure-level W1 theorem
          </strong>
          : Suzuki&apos;s L²₀ mean-zero condition is automatic on the u-side
          (the projection lemma — the last named remainder closes), A_arch =
          −g″_smooth exactly at every lag (3.4e−52), and the full form
          equality holds at 1.28e−10 on the common odd sector. v644 starts
          W2 honestly (classical FEM density at rate; Rayleigh–Ritz monotone
          from above on nested spaces; λ_a = 0⁺ within ~1e−9, no sign
          statement; the Mosco remainder named). And v648 types the W3 tool
          diagnosis: the sign-uncertainty toolbox has a real 25-digit
          dictionary to the critical strip, but its mass lever dies at
          d = 1 — while the W3 surface itself is empirically positive on all
          67 complete windows (min λ_min = +8.26e−4).
        </p>
        <p className="text-slate-600">
          The honest map: W1 (theorem-closed) → W2 (started, not closed) →
          W3 (uniform positivity — the RH-hard step, open; the toolbox
          diagnosis closes one candidate route) → W4 (classical given
          W2+W3). Closing W1 does not move W3. No RH claim.
        </p>
      </DiarySection>

      {/* 02 — C = 1 */}
      <DiarySection
        id="uniform-constant"
        plain="One measured constant controls every window with complete data — and the only two exceptions turned out to be missing data, not broken mathematics."
        eyebrow="02 · The uniform constant · v618 / v619"
        title="C = 1, exception-free — and the two violators were the data's edge"
        badge="machine-verified"
      >
        <p>
          The equidistribution conjecture of the theory-open section asks for{" "}
          <span className="font-mono text-slate-800">
            |q_real/q_model| ≤ C·h⁻¹
          </span>{" "}
          uniformly. The measured constant is now frozen:{" "}
          <strong className="font-medium text-emerald-800">C = 1</strong>. On
          the declared surface (69 floor-passed windows, h = 142…1445) the
          model value keeps <em>one</em> sign on the whole ladder — no model
          zero crossing anywhere — and on every lock-sign window{" "}
          <span className="font-mono text-slate-800">eps·h ≤ 0.982</span>,
          with tertile medians 0.61 / 0.45 / 0.39 falling with depth (v618).
        </p>
        <p>
          Exactly two windows violated the bound, and both carried a{" "}
          <span className="font-mono text-slate-800">q_real</span> sign flip.
          v619 found the mechanism, and it is disarmingly concrete: a
          window&apos;s atom demand runs to{" "}
          <span className="font-mono text-slate-800">u ≤ 2α</span>, the
          prime-power data cap sits at{" "}
          <span className="font-mono text-slate-800">U_max = 12.899</span> —
          and the two flip windows are exactly the two whose demand exceeds
          the cap. Injecting the same truncation into healthy windows
          reproduces the flips in sign <em>and</em> magnitude at both scales.
        </p>
        <p>
          On the complete-comb surface — 67 windows — the C = 1 bound holds
          with{" "}
          <strong className="font-medium text-slate-800">
            zero exceptions
          </strong>
          . The “sign-flip windows” are retired as data-boundary artifacts:
          extending the surface needs more prime-power data, not new theory.
          Scrambled combs break the bound by four orders of magnitude — the
          constant is genuine arithmetic placement. No uniformity proof, no
          RH statement.
        </p>
      </DiarySection>

      {/* 03 — Hook */}
      <DiarySection
        id="hook"
        plain="While checking its own bookkeeping, the project kept finding classical prime-number objects; this page asks which of those finds are mechanism and which are coincidence."
        eyebrow="03 · Hook"
        title="What if the bookkeeping secretly speaks number theory?"
        badge="sandbox"
      >
        <p>
          Prime numbers look elementary: indivisible integers. Their global
          pattern is anything but. The Riemann Hypothesis asks for a precise
          spectral order behind that pattern — and this diary does{" "}
          <em>not</em> claim to approach that hypothesis.
        </p>
        <p>
          TFPT is a discrete compiler: two axioms build an E₈ lattice and read
          off Standard-Model structure. While exploring that lattice&apos;s
          shell census, the suite found classical modular objects — thetas,
          Hecke eigenvalues, Apéry congruences — sitting inside compiler-native
          counts. The question became: which of those links are mechanism, and
          which are beautiful coincidence?
        </p>
        <p className="text-slate-600">
          What follows is the arc from first surprise (Teil 11) through a
          four-stage kill of the “archimedean-from-seam” slogan, through Hecke
          from geometry, to the July&nbsp;25 reframe: a{" "}
          <Link
            prefetch={false}
            href="/verification"
            className="text-emerald-700 underline decoration-emerald-400/30 underline-offset-2 hover:text-emerald-800"
          >
            relative-trace identity (v538)
          </Link>
          , a{" "}
          <Link
            prefetch={false}
            href="/verification"
            className="text-emerald-700 underline decoration-emerald-400/30 underline-offset-2 hover:text-emerald-800"
          >
            Weil structure with two named obstructions (v539)
          </Link>
          , an{" "}
          <Link
            prefetch={false}
            href="/verification"
            className="text-emerald-700 underline decoration-emerald-400/30 underline-offset-2 hover:text-emerald-800"
          >
            amplitude route with a positive linear carrier (v540)
          </Link>
          , a{" "}
          <Link
            prefetch={false}
            href="/verification"
            className="text-emerald-700 underline decoration-emerald-400/30 underline-offset-2 hover:text-emerald-800"
          >
            matching-lemma and transport-ledger package with two named limits
            (v541)
          </Link>
          , and the consolidated stand below —{" "}
          <a
            href="#program-status"
            className="text-sky-700 underline decoration-sky-400/30 underline-offset-2 hover:text-sky-800"
          >
            what remains TFPT-specific is exactly one object: I5 — now
            geographically framed
          </a>
          .


        </p>
      </DiarySection>

      {/* 04 — Compiler */}
      <DiarySection
        id="compiler"
        plain="The whole theory starts from two fixed numbers, which force one specific eight-dimensional lattice — everything on this page is read off that lattice."
        eyebrow="04 · The compiler in one picture"
        title="Two axioms, one lattice completion"
        badge="sandbox"
        visual={<CompilerSchematic />}
      >
        <p>
          The discrete compiler starts with two numbers only: the seam constant{" "}
          <span className="font-mono text-slate-800">c₃ = 1/(8π)</span> and the
          carrier rank{" "}
          <span className="font-mono text-slate-800">g_car = 5</span>. From
          those, the theory forces a split{" "}
          <span className="font-mono text-slate-800">D₅ ⊕ A₃</span> completed by
          a four-element glue group{" "}
          <span className="font-mono text-slate-800">μ₄</span> to the unique even
          unimodular lattice in eight dimensions —{" "}
          <span className="font-mono text-slate-800">E₈</span>.
        </p>
        <p>
          Everything on this page is about what that lattice&apos;s point counts
          know — and what they do not know — about primes and L-functions.
          Classical theorems stay classical; the TFPT contribution is the
          in-suite mechanics that make those objects appear from frozen
          geometry.
        </p>
      </DiarySection>

      {/* 05 — Signed census */}
      <DiarySection
        id="census"
        plain="Counting lattice points with signs produces, unexpectedly, a classical formula tied to the Gaussian integers and to pi."
        eyebrow="05 · First discovery · Teil 11"
        title="The signed census: θ₃² · θ₄⁶ as a tensor factor"
        badge="sandbox"
        visual={<ShellCensus />}
      >
        <p>
          Colour every E₈ shell point by its μ₄ “glue class” (four colours).
          Ordinary counting recovers the classical Eisenstein series{" "}
          <span className="font-mono text-slate-800">
            1 + 240 Σ σ₃(n) qⁿ
          </span>
          . The surprise is the <em>signed</em> difference between opposite
          colours:
        </p>
        <p className="rounded-xl border border-slate-300/40 bg-slate-100/50 px-4 py-3 font-mono text-sm text-sky-800">
          Θ₀ − Θ₂ = θ₃(q)² · θ₄(q)⁶
        </p>
        <p>
          Here θ₃² is the theta series of the Gaussian integers ℤ[i] — the
          classical object whose L-value{" "}
          <span className="font-mono text-slate-800">L(1, χ₄) = π/4</span>{" "}
          produces π. It appears as a literal tensor factor of the
          compiler&apos;s signed glue census (classical Jacobi theta algebra;
          the probe content is the in-suite correlation).
        </p>
        <p>
          Three character channels sit on the same shells:{" "}
          <strong className="font-medium text-slate-800">total</strong> (all
          primes, ζ(s)ζ(s−3)),{" "}
          <strong className="font-medium text-slate-800">signed</strong> (entire
          L-series — the glue character kills the pole), and{" "}
          <strong className="font-medium text-slate-800">spinor</strong>{" "}
          (2-adic).
        </p>
      </DiarySection>

      {/* 06 — Bridges */}
      <DiarySection
        id="bridges"
        plain="The same counting reproduces a famous congruence from the proof that zeta(3) is irrational — and look-alike controls fail it."
        eyebrow="06 · Surprise bridges · Teil 12"
        title="The census “knows” the Apéry numbers"
        badge="sandbox"
        visual={<AperyBridge />}
      >
        <p>
          The cuspidal piece of the signed count is the weight-4 form{" "}
          <span className="font-mono text-slate-800">
            f₈ = η(2τ)⁴ η(4τ)⁴
          </span>{" "}
          — classically the Beukers / Ahlgren–Ono form tied to Apéry&apos;s
          proof that ζ(3) is irrational. For every odd prime p ≤ 97 the probe
          checks{" "}
          <span className="font-mono text-slate-800">
            A((p−1)/2) ≡ a_p mod p²
          </span>
          . Via Teil 11, the signed E₈ count at odd prime shells satisfies the
          same congruence. Placebos on nearby eta products fail.
        </p>
        <p className="text-slate-600">
          Beautiful, form-specific, and still sandbox: a correlation inside the
          suite, not a new proof of irrationality.
        </p>
      </DiarySection>

      {/* 07 — Kill chain */}
      <DiarySection
        id="kill-chain"
        plain="The project deliberately tests its own favourite explanations to destruction — and publishes the failures as first-class results."
        eyebrow="07 · Honesty as a method · Teile 14, 19–25"
        title="The kill chain — presented as a feature"
        badge="sandbox"
        visual={<KillChainTimeline />}
      >
        <p>
          An early slogan said the seam&apos;s measured angle 2π was “the
          self-dual temperature.” Teil 14{" "}
          <strong className="font-medium text-rose-800">deflated</strong> that:
          the steps parameter is compiler-specific; the angle is universal
          Bisognano–Wichmann / Unruh conversion.
        </p>
        <p>
          Then the whole “archimedean term from the seam” route was killed in
          four preregistered stages: mode density → interval cut → dictionary →
          scattering phase. Lesson, typed and kept: the seam is a discrete μ₄
          clock, not a hidden Gamma factor. The archimedean piece of the
          explicit formula is treated as a classical externum for recovery
          work.
        </p>
        <p className="text-slate-600">
          Killing your own favourite story on purpose is the method. Null
          results are first-class outcomes.
        </p>
      </DiarySection>

      {/* 08 — Predict */}
      <DiarySection
        id="predict"
        plain="The lattice can say exactly whether a number is prime and what kind of prime it is — but not where the next prime lies; that limit is stated, not hidden."
        eyebrow="08 · Can it predict primes? · Teil 21"
        title="Three honest channels — and one missing operator"
        badge="sandbox"
        visual={<PrimeDetector />}
      >
        <p>
          <strong className="font-medium text-slate-800">(a) Exact geometric
          primality.</strong>{" "}
          n&gt;1 is prime if and only if the E₈ shell at norm 2n has exactly{" "}
          <span className="font-mono text-slate-800">240(1+n³)</span> vectors —
          the classical σ₃ criterion, checked with zero false
          positives/negatives to 10⁴.
        </p>
        <p>
          <strong className="font-medium text-slate-800">(b) Per-prime
          properties.</strong>{" "}
          Glue characters predict arithmetic type: χ₄-fibre ⟺ p = a²+b²
          (100% for p&lt;1000 in the probe). The compiler says what a prime
          does, not where the next one sits.
        </p>
        <p>
          <strong className="font-medium text-slate-800">(c) Positional
          prediction</strong>{" "}
          needs the zero spectrum. Measured budget:{" "}
          <span className="font-mono text-slate-800">x_max ≈ 0.31 · T</span>.
          No continuum Hilbert–Pólya theorem exists in the suite. A zeta-free
          glued truncation candidate now exists at measurement level
          (v716–v721, the moonshot arc) — stated honestly: a measurement,
          not a near miss toward RH.
        </p>
      </DiarySection>

      {/* 09 — Hecke */}
      <DiarySection
        id="hecke"
        plain="The standard machinery of modular forms emerges from stepping between lattice neighbours — the first machine-verified module of this arc."
        eyebrow="09 · The mechanism · Teile 27–32 · v535"
        title="Hecke from geometry — first load-bearing result"
        badge="machine-verified"
        visual={<NeighborStepping />}
      >
        <p>
          Kneser p-neighbours — isotropic lines in E₈/pE₈ — carry the Hecke
          structure of the census. The count of lines is{" "}
          <span className="font-mono text-slate-800">σ₃(p) · #P³(𝔽_p)</span>{" "}
          (enumerated at p = 2, 3, 5, 7: 135 / 1120 / 19656 / 137600).
        </p>
        <p>
          The frozen marked neighbour-sum operator is an affine Hecke element{" "}
          <span className="font-mono text-slate-800">
            ν_p = a · Id + b · T_p
          </span>{" "}
          with <span className="font-mono text-slate-800">b = σ₃(p) + a_p</span>
          . Prime fingerprints fall out of geometry:{" "}
          <span className="font-mono text-emerald-700">
            a₃ = −4, a₅ = −2, a₇ = 24
          </span>
          . Census redundancy is purely 2-adic oldform structure (dim 7 = 5+2);
          recovery is newform projection.
        </p>
        <p>
          Promoted as{" "}
          <span className="font-mono text-emerald-700">
            verification/v535_hecke_from_geometry.py
          </span>{" "}
          (HECKE.GEOM.01, 25/25, AUDIT OK). Classical theorems (Kneser, Hecke,
          Atkin–Lehner, multiplicity one) are classical; the claim is the
          in-suite mechanics. No RH statement. Later joined by v536–v539 — see
          the July&nbsp;25 arc below.
        </p>
      </DiarySection>

      {/* 10 — Eichler */}
      <DiarySection
        id="eichler"
        plain="The lattice count splits into a smooth background plus an interference term, and the interference is exactly the square of a modular coefficient."
        eyebrow="10 · The Eichler layer · Teile 33, 36 · v536"
        title="Smooth background + coherent interference"
        badge="machine-verified"
        visual={<TwoMelodies />}
      >
        <p>
          Once the neighbour operator is frozen, the geometric count splits as
          an elementary Witt piece plus{" "}
          <span className="font-mono text-slate-800">exactly a_p²</span> — like
          a smooth melody with a coherent flicker on top. Two-sided
          confirmation (mod-p geometry on one side, eta-product on the other)
          holds at p ≤ 5; closed forms extend the identity to p ≤ 100.
        </p>
        <p className="text-slate-600">
          Promoted as v536 (Eichler trace layer). Together with v535 and the
          half-integral bridge v537, it becomes one finite relative-trace
          identity — v538.
        </p>
      </DiarySection>

      {/* 11 — Weight drop */}
      <DiarySection
        id="weight-drop"
        plain="The easy half of the connection to zeta closes with classical tools; the hard half — the actual zeros — is untouched, and the page says so."
        eyebrow="11 · Two-channel weight drop · Teile 35, 39"
        title="Abelian channel closed; cuspidal channel remains"
        badge="sandbox"
        visual={<CenterAtlas />}
      >
        <p>
          Rankin–Selberg translates{" "}
          <em>only</em> the abelian shadow into GL(1) products of{" "}
          <span className="font-mono text-slate-800">{"{1, χ₄}"}</span>. The
          centre atlas shows the ξ-line (centre 1/2) is reached exactly by
          weight ≤ 1 theta factors: Mellin(θ₃) → ζ(2s) and{" "}
          <span className="font-mono text-slate-800">
            ζ_ℚ(i) = ζ(s) L(s, χ₄)
          </span>
          . That abelian weight drop is factorisation + Mellin — typed closed.
        </p>
        <p>
          The cuspidal channel — where the{" "}
          <span className="font-mono text-slate-800">a_p</span> live — still
          sits at centre 2 and needs its own bridge. Possessing ζ as a{" "}
          <em>function</em> is not possessing its zeros as a{" "}
          <em>spectrum</em>.
        </p>
      </DiarySection>

      {/* 12 — Stage 4 */}
      <DiarySection
        id="stage-4"
        plain="A map of the terrain shows the finite machine has only a two-point spectrum — far too small for the operator RH would need."
        eyebrow="12 · Stage-4 map · Teil 40"
        title="Two-point spectrum; infinitely many still missing"
        badge="sandbox"
        visual={<SpectrumLadder />}
      >
        <p>
          The operator algebra on the census forms is commutative with a{" "}
          <em>two-point</em> Gelfand spectrum (the σ₃-system and the a_p-system,
          with oldform copies). A Hilbert–Pólya carrier would need an unbounded
          / non-commutative operator with infinitely many eigenvalues.
        </p>
        <p>
          Only two candidate classes remained inside the suite&apos;s early
          vocabulary: seam modular flow, and adelic Bost–Connes-style
          completion. Each has preregistered kills. The July&nbsp;25 reframe
          then changed the game: instead of hunting one infinite operator, the
          diary switched to a <em>family</em> plus a relative trace formula —
          see the next section.
        </p>
        <p className="rounded-xl border border-slate-300/40 bg-slate-100/40 px-4 py-3 text-sm text-slate-600">
          Verdict of the terrain map:{" "}
          <span className="font-mono text-slate-800">TERRAIN-MAPPED</span>.
          Cartography, not a proof attempt. Distance to RH — stated without
          theatre — remains large.
        </p>
      </DiarySection>

      {/* 13 — July 25 arc */}
      <DiarySection
        id="july-25-arc"
        plain="Instead of hunting one infinite operator, the diary switched to a family of values inside a classical trace-formula frame — and isolated exactly two named obstructions."
        eyebrow="13 · The July 25 arc · Teile 51–64 · v538 / v539"
        title="From finite machine to a Weil structure with two named obstructions"
        badge="sandbox"
        visual={<WeilArcMap />}
      >
        <p>
          The day&apos;s reframe: stop asking for one infinite operator. Ask for
          a <strong className="font-medium text-slate-800">family</strong> of
          central values plus a{" "}
          <strong className="font-medium text-slate-800">
            relative trace formula
          </strong>
          . Sandbox Teile&nbsp;51–64 built that map; two pieces graduated into
          the load-bearing suite.
        </p>

        <p>
          <strong className="font-medium text-slate-800">(i) The reframe.</strong>{" "}
          v535, v536 and v537 are three projections of{" "}
          <em>one</em> finite relative-trace identity — promoted as{" "}
          <span className="font-mono text-emerald-700">v538</span>. The
          half-integral object g is literally the quaternary lattice form{" "}
          <span className="font-mono text-slate-800">
            n = (x²+y²)/2 + 2z² + u² + 2w²
          </span>
          .
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            (ii) First non-collapsing infinite carrier.
          </strong>{" "}
          The Waldspurger family kernel K_D (classical Waldspurger periods) has
          rank that grows 8→192 as the discriminant window opens — the
          preregistered “rank saturates” kill did{" "}
          <em>not</em> fire. Its spectrum <em>is</em> the central-value family
          at the GL(2) centre&nbsp;2 — not the ξ-line. This is not RH evidence.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            (iii) Self-generating Hilbert space.
          </strong>{" "}
          The weight |d|<sup>−5/2</sup> is only the critical line of the family
          measure, not a canonical measure. The RTF forces |d|<sup>−1</sup>. At
          that weight, a positive pairing is cutoff-independent and builds its
          own space by GNS:{" "}
          <span className="font-mono text-slate-800">ℓ²(d, b²/|d|)</span>.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            (iv) Both infinities in one object.
          </strong>{" "}
          The double series Z(s,w) packs p-towers (closed Euler factors) and the
          d-family into one bilaterally verified identity (errors down to
          ~8×10<sup>−8</sup>; classical Goldfeld–Hoffstein multiple Dirichlet
          series named classical). Residual probes find only classical GL(1)
          shadows — no new ξ-sector.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            (v) Exact GL(1) core.
          </strong>{" "}
          Inside the positive form, the trivial Sato–Tate isotype is exactly{" "}
          <span className="font-mono text-slate-800">
            G₀ = ζ_p(w−3)² / ζ_p(2w−6)
          </span>
          . Fibre decomposition after character patterns kills twist-mix
          (~10<sup>−16</sup>).
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            (vi) Final linear relation — two obstructions.
          </strong>{" "}
          Machine-checked (and promoted as{" "}
          <span className="font-mono text-emerald-700">v539</span>):
        </p>
        <p className="rounded-xl border border-amber-400/35 bg-amber-500/10 px-4 py-3 font-mono text-sm text-amber-800">
          Q_fam = 2Q_ζ − 2Q_ζ(♭) + Arch + Corr
        </p>
        <p>
          The claim is{" "}
          <em>
            “Weil structure fully identified up to two explicitly isolated
            obstructions”
          </em>{" "}
          — the obstructions are the verified content, not a footnote. Not
          “almost RH.”
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            (vii)–(viii) Progression — see status.
          </strong>{" "}
          Sandbox Teil&nbsp;64 resolves Corr as the det/det₂ Jacobian; the
          categorical minus remains. Teile&nbsp;65–66 close the π-digit front;
          Teil&nbsp;67 takes a first amplitude-Dirac step. Full consolidated
          stand in the next section.
        </p>

        <p className="rounded-xl border border-slate-300/40 bg-slate-100/40 px-4 py-3 text-sm text-slate-600">
          Display markers: sandbox probes stay{" "}
          <span className="font-mono text-amber-800">[sandbox]</span>;
          v538–v541 are{" "}
          <span className="font-mono text-emerald-800">[machine-verified]</span>.
          Ledger fine types live in the verification suite only. No silent
          marker upgrades.
        </p>
      </DiarySection>

      {/* 14 — Program status (consolidated) */}
      <DiarySection
        id="program-status"
        plain="Everything TFPT-specific has been compressed into one remaining object, I5 — provably equivalent to what RH needs, and honestly not proved."
        eyebrow="14 · Where the program stands"
        title="Prime and Riemann Front: From Finite Hecke Structure to an Infinite Stabilized Trace Space"
        badge="sandbox"
        visual={
          <div className="space-y-3">
            <ProgramStatusCallout />
            <ModuleLadder />
          </div>
        }
      >
        <p>
          <strong className="font-medium text-slate-800">
            A single arithmetic machine.
          </strong>{" "}
          Three load-bearing modules are projections of{" "}
          <em>one</em> finite relative-trace identity{" "}
          <span className="font-mono text-emerald-700">[machine-verified · v538]</span>
          . Geometric side (E₈ lattice / glue census) and spectral side (modular
          coefficients / twisted L-values) are computed independently and agree
          exactly on the verified finite modules.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            A canonical infinite state space.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox]</span> A family
          over fundamental discriminants: rank grows without saturation
          (&gt;&nbsp;6000 active discriminants; Hecke integral and exact). The
          Hilbert space is not chosen by hand — a positive pairing produces the
          canonical GNS construction. Independent cutoffs converge
          sub-percent; the prediction chain closes at ~0.09%.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Packing the two infinities.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox]</span> The double
          series Z(s,w) packs two infinite directions — Euler towers over p, and
          the discriminant family — in the classical frame of multiple Dirichlet
          series / relative trace formulas (Goldfeld–Hoffstein named classical).
          Geometric = lattice counting; spectral = L-values × Euler factors.
          Fence: this does <em>not</em> transport to ξ; the system stays at
          weight&nbsp;4. RH concerns GL(1) at Re&nbsp;=&nbsp;1/2.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The Weil structure and its two obstructions.
          </strong>{" "}
          Compared with the Weil structure of the explicit formula (Weil 1952):{" "}
          <span className="font-mono text-emerald-700">
            [machine-verified · v539]
          </span>{" "}
          isolates <em>two</em> discrepancies — an exponential correction factor,
          and a categorical minus tied to the square nature of the family. Both
          isolations are the verified content of v539; neither is a footnote.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Exact determinant stabilization.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T64]</span>{" "}
          exp(−Σ p<sup>−u</sup>) = det(1−K)/det₂(1−K) (Hilbert–Carleman),
          verified ~1.5×10<sup>−16</sup>. In a consistent det₂ formulation the
          correction vanishes identically — it is the regularisation Jacobian of
          the GL(1) transition, not a new object. At u&nbsp;=&nbsp;1/2 the
          ordinary determinant does not exist while det₂ does, so stabilization
          is <em>necessary</em>, not optional: the stabilized transition is the
          only currently identified determinant convention that can reach the
          critical line. This resolves obstruction&nbsp;2 in sandbox; it does
          not rewrite the v539 isolation claim.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The remaining categorical minus.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox]</span> Survives
          every tested canonical projection. Source identified: the channel
          collects even prime powers, bound to the square form of the twist
          family (Waldspurger: L<sub>central</sub> ~ b(d)²) — the construction
          sees the <em>square</em>, not the linear amplitude. Krein signature
          confirms genuine indefiniteness; 32/32 sign characters do not remove
          it selectively. Not a normalisation error, incomplete character sum, or
          regularisation artefact — a categorical feature of the square level.
        </p>

        <p className="rounded-xl border border-violet-400/35 bg-violet-500/10 px-4 py-3 text-sm leading-relaxed text-violet-50 sm:text-base">
          At T86 — 91 probes in — and with seven promoted modules (v535–v541),
          the matching lemma is closed on ALL atom classes (window-certificate
          format,
          modulo proven classics only). What remains TFPT-specific is exactly
          ONE object: I5 in one-family form —{" "}
          <span className="font-mono text-violet-800">
            {"Q_cert + Δ₂ + A_fam − A_shift ≥ 0"}
          </span>{" "}
          — provably equivalent to Weil positivity ⟺ RH.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The remaining mathematical problem — absolute compression.
          </strong>{" "}
          Rest list:{" "}
          <em>(1)</em> I5 in one-family form, typed ⟺ Weil positivity ⟺ RH.
          Matching Lemma: closed on all atom classes (window 10⁶ proved ·
          signed pairing on non-coherent · λ-channel on coherent · 2-line
          exact){" "}
          <span className="font-mono text-amber-800">[sandbox · T86]</span>
          {" / "}
          <span className="font-mono text-emerald-800">
            [machine-verified · v541]
          </span>
          . I5 core = explicit Gaussian-mode family in the one-atom band
          (log&nbsp;2,&nbsp;0.925]; a<sub>neg</sub>&nbsp;=&nbsp;0.7486
          (recalibrated by T93); named target (T); finite-block zone extension
          certified only on an 8-dim window — structurally the wrong instrument
          for the full claim{" "}
          <span className="font-mono text-amber-800">[sandbox · T87–T93]</span>.
          Blind demo: 753/753 primes, zero errors, no division{" "}
          <span className="font-mono text-amber-800">[sandbox · T94]</span>.
          Induction skeleton: identities proved, zones 2–4 closed, zone-5 tip =
          equality problem, asymptotics = one named arithmetic bound (A){" "}
          <span className="font-mono text-amber-800">[sandbox · T99–T101]</span>.
          Milestone at T101: 2428/2428 sandbox checks (3139/3139 at T125).
          Fence: fits/extrapolations marked; geography locates; it does not
          attack; I5 remains ⟺ RH. This is not RH evidence.
        </p>

        <p>
          <strong className="font-medium text-slate-800">Current status.</strong>
        </p>
        <ul className="list-disc space-y-1.5 pl-5 text-sm text-slate-600">
          <li>
            <span className="text-rose-800">Not present:</span> RH proof,
            almost-RH, a zeros operator, a proof of I5.
          </li>
          <li>
            <span className="text-emerald-800">Present:</span> mechanism through
            v541{" "}
            <span className="font-mono text-emerald-800">
              [machine-verified]
            </span>
            ; Matching Lemma closed on all atom classes{" "}
            <span className="font-mono text-amber-800">[sandbox · T86]</span>;
            I5 geography complete{" "}
            <span className="font-mono text-amber-800">[sandbox · T87–T93]</span>
            ; a<sub>neg</sub> recalibrated to 0.7486; blind lattice demo{" "}
            <span className="font-mono text-amber-800">[sandbox · T94]</span>;
            induction skeleton: zones 2–4 closed; asymptotics = arithmetic bound
            (A){" "}
            <span className="font-mono text-amber-800">[sandbox · T99–T101]</span>
            ; I5 in one-family form — the single remaining TFPT-specific object.
          </li>
          <li>
            <span className="text-sky-800">Since then:</span> the induction
            sprint{" "}
            <span className="font-mono text-amber-800">
              [sandbox · T102–T125]
            </span>{" "}
            compressed that named bound from one matrix inequality to one sign
            plus one accounting convention, with certified steps to zone 155,921
            and 400/400 certified rungs, and the finale assembled the whole
            chain end to end on 52 zones — told in{" "}
            <a
              href="#compression"
              className="text-sky-700 underline decoration-sky-400/30 underline-offset-2 hover:text-sky-800"
            >
              sections 22–24
            </a>
            . Series complete: 3139/3139 sandbox checks at T125.
          </li>
        </ul>

        <p>
          <strong className="font-medium text-slate-800">On π — closed.</strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T65–T66]</span>{" "}
          Not the decimal digits of π are the key. Digit probes are closed:
          π digits at prime places are uniform; density-detrended
          cross-correlations null; full placebo battery (e, √2, log&nbsp;2,
          crypto, p±1) plus blind windows — no replication (PI-NULL 16/16;
          FOUR-LEVEL-NULL 23/23). The π spike is classical continued-fraction
          structure (355/113); compiler constant 1/(8π) is not an outlier
          (z&nbsp;=&nbsp;−0.90). Contrast kept: π-driven Cramér randomness
          reproduces prime <em>density</em> perfectly, but only true primes
          track Hardy–Littlewood pair correlation (corr&nbsp;+0.81 vs flat) —
          what makes primes primes is arithmetic, not randomness. The key now
          sits in one-family I5 — not in π digits.
        </p>
      </DiarySection>

      {/* 15 — Amplitude / transport route */}
      <DiarySection
        id="amplitude-route"
        plain="A promising route through squared quantities hits a measured wall, and the wall's exact size is named inside the verified claim."
        eyebrow="15 · The amplitude route · Teile 67–72 · v540"
        title="From the Dirac square root to a positive linear carrier — and the measured wall"
        badge="machine-verified"
        visual={
          <div className="space-y-3">
            <AmplitudeRouteCallout />
            <ConeCoverage />
          </div>
        }
      >
        <p>
          <strong className="font-medium text-slate-800">
            Square level closed — every squaring deletes.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T67–T69]</span>{" "}
          The amplitude Dirac D = [[0,V],[Vᵀ,0]] with D² = family kernel exists
          exactly and is Hecke-equivariant; signs of b(d) are a genuine
          metaplectic residue (52% mixed fibres — Kohnen depth, classical).
          Geometric polarisation b = N₊ − N₋ is exact; Θ = N₊+N₋ is a pure
          Siegel–Weil Eisenstein eigenform (σ₃ eigenvalues, null cusp); the
          family is the difference of two positive counting families
          (b² = Θ² − 4N₊N₋) — yet the minus is polarisation-invariant. By a
          Cauchy–Littlewood lemma, <em>every</em> coefficient bilinear form
          inherits even-k deletion (theorem-like across five channels); at the
          same time the minus is exactly the square-class double-counting of the
          towers (inclusion–exclusion bookkeeping). No full-weight carrier can
          live on the square level.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            A positive linear carrier — plus-only ζ-balance.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T70–T71]</span>{" "}
          The linear positive measure stands: Θ(d) = −48·L(−1,χ_d) exact (Cohen
          1975); full weights [1,1,1,1]; Weil balance{" "}
          <span className="font-mono text-slate-800">
            Q = Q_ζ(g₋) + Q_ζ(g₊)
          </span>{" "}
          is plus-only (~1e-15). The ζ(2s) factor appears only as the squarefree
          sieve of the carrier — bookkeeping, not weight deletion.           Functional
          equation exact:{" "}
          <span className="font-mono text-slate-800">
            {"Λ_Θ(s) = 8^{1−s}Λ_Θ†(5/2−s)"}
          </span>{" "}
          (rel ~1e-40; Fricke closed via Jacobi inversions). Plus survives
          reflection; the mirror family has a rigid sign law. The guaranteed
          cone is FE-selfdual; the Weil cone is not. Overlap 5/24; violations sit
          exactly at the first spectral node. Fence: this is Euler-region
          positivity (absolute convergence), not a central-line statement.
          Classical named: Cohen, Shintani, Siegel–Weil, Jacobi/Fricke, Weil
          1952.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The cone library saturates — one measurable gap.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T72]</span>{" "}
          Twisting absorbs the sign class n&nbsp;≡&nbsp;0,1&nbsp;mod&nbsp;4 (gap
          −26% mean, −90% max), but coverage saturates at 5/24. The pin h(0)&nbsp;&gt;&nbsp;0
          blocks every Weil element against every twist. Final compression: the
          entire residual distance to the Weil cone is the FE-covariant gap
          functional λ* on the atoms n&nbsp;≡&nbsp;6&nbsp;mod&nbsp;8 — no finite
          theta library can erase it (Farkas/LP certificates). Promoted as{" "}
          <span className="font-mono text-emerald-700">v540</span> with λ*
          named inside the claim. The doors that furnish this wall are the next
          section. This is not RH evidence.
        </p>
      </DiarySection>

      {/* 16 — Doors furnished */}
      <DiarySection
        id="doors-furnished"
        plain="The remaining gap gets doors: no-go theorems for what cannot work, a calculus for the gap functional, and one named inequality that would close it."
        eyebrow="16 · The doors get furnished · Teile 73–81"
        title="Two no-go theorems, a λ* calculus, a window proof — and one named inequality"
        badge="sandbox"
        visual={
          <div className="space-y-3">
            <DoorsFurnishedCallout />
            <DoorsPanel />
          </div>
        }
      >
        <p>
          <strong className="font-medium text-slate-800">
            Uniform cone route closed — hybrids live per direction.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T73]</span>{" "}
          Even in the continuum, the direction-uniform cone route is closed
          (sign-constancy lemma; window pin on [0,&nbsp;δ<sub>h</sub>)). But for
          every one of the 19 uncovered Weil directions an explicit,
          verified per-direction hybrid cone exists — the constructive residue
          is a per-test-function certificate machine (HYBRID-GAINS).
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Door A — vacuum structure, spectral no-go.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T74]</span> The
          spectral Dirac phase carries the metaplectic sign datum (~93%) but
          has a Hecke defect. L2 no-go: every ε-equivariant spectral functional
          is exactly re-signing invariant — the spectral world is provably
          sign-blind. The Dirac vacuum sits on the atom of minimal
          Waldspurger-normalised mass. Final Door&nbsp;A requirement list
          R1–R5: the sought polarisation must act coefficient-wise, be
          non-multiplicative in tower depth, non-bilinear, not a support
          reshuffle, and sign-seeing while Euler-compatible — a Krein /
          Gupta–Bleuler <em>quotient</em> in which the ♭-piece is a null/gauge
          sector, not a summand. Classical named: Dirac sea, Krein, Kohnen,
          McKean–Singer.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Door B — λ* gets its own calculus.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T75]</span> The
          gap functional now has closed form, its own functional equation (orbit
          invariant tanh(σ²ω²/2) under positive multipliers ⋊ dilations),
          critical width σ<sub>c</sub>&nbsp;=&nbsp;√2, and convexity (averaging
          lowers; no scale wedge — an earlier fp artefact honestly corrected).
          The target inequality is measured both sides: safety factor 273 at
          ω&nbsp;=&nbsp;1 falling to &lt;&nbsp;1 at ω&nbsp;=&nbsp;4.2. Two named
          open inequalities remain (hull positivity = transport wall;
          universal λ*-vs-A). Classical: Fejér / support functionals, Mellin /
          dilation semigroup.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Door C — a universal recipe, and its named lemma.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T76]</span> The
          hybrid recipe certifies 91/91 nontrivial adversarial Weil directions
          (100%); cost is polynomial / window-extensive (λ<sub>m</sub> ~
          m<sup>5/2</sup> = Eisenstein law). Lattice discreteness is the floor —
          δ<sub>h</sub>&nbsp;→&nbsp;0 does not break S1. Conjecture form with
          named core lemma: the{" "}
          <em>Matching Lemma</em> on the log lattice (a Diophantine divisor-sum
          problem). Implication architecture typed,{" "}
          <em>not claimed</em>: Matching Lemma ⇒ value-side representability ⇒
          [if the value→spectral transport held — the open wall] ⇒ Weil
          positivity. Any RH content would relocate into a universality proof
          plus the transport wall. This is not RH evidence.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Matching Lemma — classically shaped, then window-proved.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T77–T78]</span>{" "}
          T77: classically shaped (Gronwall/Robin; lemma not yet proven). T78
          WINDOW-PROVED (25/25): machine-proved on [4,&nbsp;10⁶] — exact-integer
          inequality chain, full enumeration over 939 870 clash atoms, 0
          violations, exact margin 0.082159; four structure laws at 0
          tolerance. Tail honestly open: Robin 1983 + constants miss by factor
          6.16 — missing residual ingredient named: a correlation lemma
          (thinning × cancellation). T80 RESERVE-PARTIAL: signed envelope
          character-exact; tail closed to ~10²³; last gap confined to the
          χ₋₄-coherent class. Classical: Gronwall 1913, Robin 1983,
          Alaoglu–Erdős, Pólya–Vinogradov, Landau.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Avoidance fails — theorem-shaped.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T81]</span>{" "}
          AVOIDANCE-FAILS (31/31): the same multiplicativity that makes the
          lever exact proves the counter-lever: coherent targets are reachable
          only by coherent rescalings — the freedom does not exist on coherent
          demand. Salvage: T76 recipe already minimally coherent (0 unforced
          keys, 100/100); forced coherent clash closed per certificate (83/90,
          worst ratio 0.18); on avoidant demand the class vanishes identically.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The transport ledger closes — the wall is I5.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T79]</span>{" "}
          LEDGER-CLOSES (22/22):{" "}
          <span className="font-mono text-slate-800">
            {"Q_Weil = Q_cert + Δ_arch + Δ₂"}
          </span>{" "}
          (identity ~7e-16 on 100/100); Δ<sub>pole</sub> ≡ Δ<sub>conv</sub> ≡ 0
          proved; the odd-prime side equals the certified combination exactly.
          The wall is one named inequality I5 (prime↔archimedean coupling),
          typed ⟺ Weil positivity ⟺ RH. Fence: equivalence typing, not progress
          toward proving it. This is not RH evidence. Classical: Weil 1952,
          Guinand, digamma terms.
        </p>

        <p className="rounded-xl border border-slate-300/40 bg-slate-100/40 px-4 py-3 text-sm text-slate-600">
          After T81 the constructive recipe chain saturated. Three new
          perspectives (next section) retype I5 and reopen the Z[i] channel —
          without claiming RH progress.
        </p>
      </DiarySection>

      {/* 17 — Three perspectives */}
      <DiarySection
        id="three-perspectives"
        plain="Three reframes land at once — a term thought external is internal, the wall cuts across the symmetry rather than along it, and the hardest class lives exactly where the compiler is most at home."
        eyebrow="17 · Three new perspectives · Teile 82–84"
        title="The arch term was internal, the wall is transversal, and the last class is the compiler's home"
        badge="sandbox"
        visual={
          <div className="space-y-3">
            <ThreePerspectivesCallout />
            <HeatFamilyBalance />
          </div>
        }
      >
        <p>
          <strong className="font-medium text-slate-800">
            The archimedean term was never external.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T82]</span>{" "}
          ARCH-INTERNAL (22/22): Δ<sub>arch</sub> is exactly the internal
          Γ-difference via Legendre duplication{" "}
          <span className="font-mono text-slate-800">
            {"((2π)^{−s}Γ(s) = ½Γ_R(s)Γ_R(s+1))"}
          </span>
          ; battery 18/18 rel 6.6e-15. The family carries its Γ factor as the
          Mellin signature of its heat-sum nature (verified also outside the
          convergence region). Bonus: the raw heat sum reproduces pole 5/2 and
          residue 8<sup>−3/2</sup> exactly from pure counting. Consequence: I5
          changes type. New form — for all autocorrelations h:
        </p>
        <p className="rounded-xl border border-amber-400/35 bg-amber-500/10 px-4 py-3 font-mono text-sm text-amber-800">
          {"Q_cert(h) + Δ₂(h) + A_fam(h) − A_shift(h) ≥ 0"}
        </p>
        <p>
          Self-consistency of <em>one</em> heat family: atom expansion vs Mellin
          signature of the same theta objects. Nearest classical relative:
          Connes 1999 semi-local trace-formula positivity (named context, not
          used). Fence: type change ≠ proof; I5 remains ⟺ RH. This is not RH
          evidence.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The wall is FE-transversal, not FE-positional.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T83]</span>{" "}
          INVARIANT-NULL (27/27): FE symmetrization is fully absorbed — 5/24 and
          λ* already are the numbers of the symmetric sector (the test region
          was right). Depth find: the product of the two FE reflections
          J₁∘J<sub>1/2</sub> = e<sup>±u</sup> is the unit-line shift — the
          centre delta is literally the transport operator. The value side is
          invariant under the whole infinite-dihedral ladder; the spectral cone
          only under its own reflection. Bonus: explicit-formula null test
          ≤&nbsp;2e-12 validates the whole convention. Classical: Mellin
          involutions, infinite dihedral group.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The last class is the compiler&apos;s home.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T84]</span>{" "}
          LIFT-WORKS-UNANCHORED (29/29): the coherent class equals primitive
          ℤ[i]-norms exactly; Grossencharacter phases replace Mertens divergence
          by L(1,λ)-convergence — the lifted chain never crosses; frontier jumps
          from ~10²³ to ~10<sup>5.9·10¹²</sup>. Circle closes: the last gap sat
          in the ℤ[i] sector — the origin object of the series (μ₄-glue, χ₄,
          θ₃²) — and exactly there the compiler&apos;s own character structure
          supplies the control that is provably impossible over ℚ. T85{" "}
          <span className="font-mono text-amber-800">
            [sandbox · LEMMA-CLOSES-LAMBDA]
          </span>{" "}
          closes the coherent class via the λ-channel (90/90 certificates;
          3.6× window margin). Fence: provably-shaped, not a formal proof; I5
          untouched. Classical: Hecke 1918/1920, Grossencharacter L-functions,
          Landau. This is not RH evidence.
        </p>
      </DiarySection>

      {/* 18 — I5 geography */}
      <DiarySection
        id="i5-geography"
        plain="The remaining object I5 sits precisely between two decades-old research programmes, which frame the same gap from opposite sides."
        eyebrow="18 · I5 geography · Teile 87–101"
        title="The I5 geography: two decades-old programs frame the same gap"
        badge="sandbox"
        visual={
          <div className="space-y-3">
            <I5GeographyCallout />
            <CrossingMap />
          </div>
        }
      >
        <p>
          <strong className="font-medium text-slate-800">
            The Connes dictionary is exact at the core.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T87]</span>{" "}
          DICTIONARY-EXACT-CORE (22/22): Q<sub>cert</sub> atoms equal Connes&apos;
          finite orbit terms (rel&nbsp;6e-16); A<sub>fam</sub> − A<sub>shift</sub>{" "}
          equals Connes&apos; archimedean W<sub>∞</sub> term including the
          principal-value constant (rel&nbsp;3e-23); the internal kernel is
          exactly the Riemann–Siegel phase derivative{" "}
          <span className="font-mono text-slate-800">{"k_ζ = 2θ'_RS"}</span>{" "}
          (rel&nbsp;0.0); the dihedral shift is the scaling group R<sup>*</sup>
          <sub>+</sub> (Weyl commutation exact). Classical: Connes 1999,
          Connes–Consani 2021, Weil, Guinand, Bombieri, Burnol, Yoshida.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Two positivity programs are complementary.
          </strong>{" "}
          Connes–Consani prove positivity <em>before</em> the primes (a
          prime-free Sonin window whose boundary sits exactly at the first
          prime atom u&nbsp;=&nbsp;log&nbsp;2). The compiler proves positivity{" "}
          <em>after</em> the primes (atom certificates). The sectors touch; they
          do not overlap. The I5 coupling lives in the crossing region outside
          both — around t*&nbsp;≈&nbsp;2π. Transferable-shaped: Sonin
          compression (same kernel, same group — verified). Not transferable:
          positivity itself (fence).
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The tight set is eight parametrized curves.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T88]</span>{" "}
          TIGHT-SET-PARAMETRIZED (27/27): band-limited zero plateau (support
          below log&nbsp;2, consistent with the T87 boundary), safe zones, and
          eight nearly vertical tight curves whose spacing follows the Γ-side
          density law (ratio 1.01&nbsp;±&nbsp;0.08 — smooth Γ-density
          description, zero-free; no spectral identification). Zero negatives
          on true autocorrelations (earlier T76 negatives were missing
          arch/p&nbsp;=&nbsp;2 bookkeeping, as the ledger predicted). Validation
          at machine precision (null test 4.3e-13, ledger 1.1e-14). The RH
          content of I5 concentrates on these low-dimensional curves.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The crossing, measured: no sharp wall at log&nbsp;2 — a thin band
            where atom and arch balance, and a 1–4-dimensional residual
            subspace that carries the minimum.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T89]</span>{" "}
          CROSSING-MAPPED (19/19): window compression of the Weil form is
          exactly Bombieri&apos;s classical object (Bombieri 2000 —
          unconditional positivity classically known precisely up to support
          width log&nbsp;2: Yoshida 1992, Bombieri 2000, Connes–Consani 2021).
          Proven zone reproduced (prime side identically zero below log&nbsp;2,
          λ<sub>min</sub>&nbsp;≥&nbsp;0 everywhere). The boundary is{" "}
          <em>not</em> sharp — margin falls smoothly (classical
          band-limitation), no collapse at log&nbsp;2; atom turn-on is
          (a−log&nbsp;2)³-soft. The residual subspace controlled by neither
          program grows softly 0&nbsp;→&nbsp;4 dimensions (of 32) across the
          crossing and carries the global margin minimum — the I5 core, for the
          first time, as a concrete finite-dimensional object per window width.
          The real attackable content is the atom↔arch balance in the thin band
          log&nbsp;2&nbsp;&lt;&nbsp;a&nbsp;≲&nbsp;1.0; the full-form minimum
          lives in the pole-coupled DC direction that Connes–Consani exclude by
          vanishing conditions; the pole-free CC sector keeps measured comfort
          to a&nbsp;≈&nbsp;0.75. Honest self-correction: BOUNDARY-SHARP retyped
          (“small at the boundary” ≠ “collapses at the boundary”). Fence:
          margins beyond the proven zone are measurements; no spectral
          identification. Classical: Weil 1952, Guinand, Yoshida 1992,
          Bombieri 2000/2003, Connes–Consani 2021/2023,
          Connes–Consani–Moscovici, Suzuki.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The residual, dissected: explicit Gaussian modes — and three
            directions under no control.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T90]</span>{" "}
          CORE-DISSECTED (17/17): the 1–4 residual vectors are n-stable across
          the discretisation ladder (angles ≤ 2.1°) and explicit — closed
          Gauss×cos / Gauss×sin fits with 99+% capture, the I5 core as a small
          family of concrete even/odd Gaussian-modulated modes. The coverage
          matrix (certificate extension / Connes–Consani pole vanishing / Sonin
          projection, against ten vectors along the a-ladder) leaves{" "}
          <em>three of ten</em> vectors controlled by no structure at all. That
          decides the core question: the residual is <em>not</em> merely pole
          coupling — pole projection clears only the a&nbsp;=&nbsp;0.75 window;
          from a&nbsp;≈&nbsp;0.85 genuine pole-free atom↔arch content remains,
          and at a&nbsp;=&nbsp;1.2 an odd atom-coupled mode appears that the
          even analyses could not see. Requirement line: an I5 idea must deliver
          positivity for an explicit family of Gaussian-modulated modes in the
          thin band — and it is not reducible to pole cleanup. Classical cited:
          Bombieri, Connes–Consani vanishing, Slepian.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The core, dissected: explicit Gaussian modes; and the band&apos;s
            law: the first prime rescues positivity where the archimedean
            margin ends — with a named, provable-shaped target inequality
            extending the classical zone.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T91]</span>{" "}
          BAND-PARTIAL (19/19, 3/4 closed): the band is the one-atom zone
          log&nbsp;2&nbsp;&lt;&nbsp;a&nbsp;≤&nbsp;0.9253 with inner edge
          a<sub>neg</sub>&nbsp;=&nbsp;0.7486{" "}
          <span className="font-mono text-sky-700">
            (recalibrated by T93; was 0.7410)
          </span>
          . Beyond a<sub>neg</sub> the prime-free margin changes sign and the
          prime atom becomes load-bearing — the first prime rescues positivity
          where the archimedean margin is exhausted (exactly the T89 balance
          point). Atom turn-on law exact (k&nbsp;=&nbsp;2m+1, Beta integrals);
          uncertainty constants decided: a·t<sub>rms</sub>&nbsp;→&nbsp;π
          (Wirtinger) and a·t<sub>cent</sub>&nbsp;→&nbsp;2Si(π)&nbsp;−&nbsp;4/π
          =&nbsp;2.4306. Band and tight curves are two orbit regions of the same
          functional with shared exact scale{" "}
          <span className="font-mono text-slate-800">{"∫k_ζ = 2θ_RS"}</span>.
          Named target (T), for a in the band and ‖f‖&nbsp;=&nbsp;1:{" "}
          <span className="font-mono text-slate-800">
            {"(P_pole + A_arch)(f) ≥ √2·log2·h_f(log2)"}
          </span>{" "}
          — provable-shaped as a zone extension beyond Bombieri&apos;s
          log&nbsp;2 (a self-standing classical target!); RH&nbsp;⇒&nbsp;(T),
          (T)&nbsp;⇏&nbsp;RH. Honest open: the super-exponential λ<sub>pf</sub>{" "}
          rate remains empirical. Classical: Wirtinger/Rayleigh, Beta integrals,
          Lambert-W, Si integral, Bombieri, θ<sub>RS</sub>.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Zone-extension attempt — and the self-check that found the
            checker&apos;s bug.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T92]</span>{" "}
          T-SKELETON (36/36): certified is Q&nbsp;≥&nbsp;6.7e-12&nbsp;&gt;&nbsp;0
          on the 8-dim window subspace over the whole scanned region (error
          certificate, 1057-point covering). The full extension does{" "}
          <em>not</em> stand — λ<sub>min</sub> collapses geometrically (factor
          ~11 per mode); the complement would need ~5000 modes: the finite-block
          route is structurally the wrong instrument. Pearl:{" "}
          <span className="font-mono text-slate-800">
            {"k(0) = −γ − 3log2 − π/2 − log π"}
          </span>{" "}
          exact.{" "}
          <span className="font-mono text-amber-800">[sandbox · T93]</span>{" "}
          MIXED (41/41): T92&apos;s calibration flags against the band map were
          resolved by a third independent implementation — the T89/T91 map
          survives; the only real bug was in the checker (constants imported
          untranslated, accidentally certifying a harder four-atom region); one
          constant precision-improved by ~1% (a<sub>neg</sub>).{" "}
          <em>
            The self-check found the checker&apos;s bug — and
            precision-improved one constant by 1%. The anchor discipline works
            in both directions.
          </em>
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The relay, measured: each prime rescues the direction the previous
            zone exhausts — and arrives before it is needed. The proof target
            shifts from fragile minima to robust counterfactuals.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T95]</span>{" "}
          T-CONTINUUM-NUMERIC (28/28): C1 fully proved — |h<sub>f</sub>
          (log&nbsp;2)|&nbsp;≤&nbsp;1/2 via disjoint support intervals;
          ‖S‖&nbsp;=&nbsp;1/2 exact with characterised eigenspace; atom-extremal
          directions satisfy the target with margin (“the directions that
          maximize the atom cost are provably safe”); continuum margin curve
          positive everywhere; extremizer is not the two-bump — binding
          mechanism is atom rescue. Lower bound open; missing instrument named.{" "}
          <span className="font-mono text-amber-800">[sandbox · T96]</span>{" "}
          EDGE-ARTIFACT + RELAY-CONFIRMED (21/21): the T95 “edge” at α* was a
          map artefact — value exactly reproduced, edge reading withdrawn
          (λ<sub>min</sub>&nbsp;&gt;&nbsp;0 on all [0.38,&nbsp;0.86]; margin
          collapses exponentially, λ&nbsp;∼&nbsp;exp(−49α)).{" "}
          <em>
            Second self-correction of the weekend, same anchor discipline.
          </em>{" "}
          Without the log&nbsp;3-atom, λ<sub>min</sub> crashes to −0.445; the
          loser is the anti-double-bump at distance log&nbsp;3 (alignment
          −0.99); rescue identity to 5e-15. Handover windows all positive:
          +0.025/+0.009/+0.011/+0.007 for the first four atoms. Strategy shift:
          margin problem, not edge problem; numerics exhausted past
          α&nbsp;≈&nbsp;0.55; the counterfactual is the proof target
          (O(0.1)-sizes). Classical: Paley–Wiener, Prolate, Galerkin/Richardson.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The induction takes shape: self-similarity puts the hypothesis
            inside the decomposition; the target is now one scalar inequality
            per zone — and the third self-correction of the weekend replaced a
            circular lemma by an exact identity.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T97]</span>{" "}
          ALIGNMENT-ONLY with certified half-step (105/105): alignment is sharp
          (sign alignment ⟺ coupling window nonempty, without exception); the
          t=0 killer loss on the anti-bump space is proved (
          <span className="font-mono text-slate-800">
            {"k_eff = (1−cos(tu))k(t)"}
          </span>
          , gain ×2–4.8); structure pearl: the E₀ block is literally the same
          form on the smaller window — “the induction hypothesis appears inside
          its own decomposition as self-similarity” (7e-14).{" "}
          <span className="font-mono text-amber-800">[sandbox · T98]</span>{" "}
          LAW-CONFIRMED-MECHANISM-OPEN (44/44): the conjectured one-vector lemma
          was circular (Douglas range inclusion — the law is forced by
          positivity itself); three T97 premises honestly refuted; replacement
          target:{" "}
          <span className="font-mono text-slate-800">
            {"D_k(α) ≤ μ_k/2"}
          </span>{" "}
          — exact scalar inequality, no constant, no vector; holds in all four
          zones, saturates at zone tips. Certificate upgrades: E₋ 43%→93% mean
          (whole zone in 3 of 4) via the probability-measure identity on the
          archimedean wings; E₊ certified for the first time. Skeleton: 8
          pieces proved, 2 certificates, 3 refuted, 3 open. Classical: Douglas
          1966, Schur, Slepian–Pollak–Landau.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Induction closeout (T99–T101).
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T99]</span>{" "}
          DECAY-LAW-FOUND (23/23): exact parity selection rule (
          <span className="font-mono text-slate-800">
            {"J₋Q₋₀J₀ = −Q₋₀"}
          </span>
          ) — the fragile near-null mode is excluded from the binding channel by
          symmetry; recursive inequality with only 1.01–1.20× loss; termination
          is arithmetic (240/240 in ≤&nbsp;4 steps to the classical zone).{" "}
          <span className="font-mono text-amber-800">[sandbox · T100]</span>{" "}
          REMAINDER-CLOSES-ZONES (27/27) — the 100th probe: closure 11/24 →
          24/24 (6/6 in every zone); the drift was a lattice artefact; one lever
          gained 1.7–69× (“the Bessel step threw the induction data away
          twice”); zones 2–4 fully closed; zone-5 tip typed as an equality
          problem (Fredholm shape, simple degeneration). Classical:
          Bessel/Parseval, Slepian, Schur test, Fredholm alternative.{" "}
          <span className="font-mono text-amber-800">[sandbox · T101]</span>{" "}
          CROWDING-TRENDS (31/31) — the fork across 16 zones (n&nbsp;=&nbsp;2..29):
          collapsed law{" "}
          <span className="font-mono text-slate-800">
            {"w_k = 0.0838·(atom gap)/μ_k"}
          </span>{" "}
          (fit) — “the handoff window is the atom spacing divided by the atom
          strength”; primitives flat; D<sub>k</sub>&nbsp;≤&nbsp;μ<sub>k</sub>/2
          holds 64/64 and never fails; only the closing instrument loses (
          <span className="font-mono text-slate-800">{"r ~ exp(−0.16k)"}</span>,
          fit/extrapolation). Core: “The crowding sits in the proof family, not
          in the mathematics it is trying to prove — the most hopeful version of
          the verdict.” Asymptotics would need (A) the arithmetic lower bound of
          the collapsed law [the localized hardness], (B) uniform relative
          margin, (C) a better bulk instrument, (D) a finite check.
        </p>

        <p className="rounded-xl border border-slate-300/40 bg-slate-100/40 px-4 py-3 text-sm text-slate-600">
          The relay induction, audited across 16 zones: the mathematics trends
          self-sustaining — flat primitives, a collapsed one-parameter law for
          the handoff, and a target inequality that never fails; what loses the
          race is the current instrument, and the hardness is localized in one
          arithmetic lower bound. Status: identities proved, zones 2–4 closed,
          zone-5 tip = equality problem, asymptotics = one named arithmetic
          bound (A). I5 remains ⟺ RH; the geography locates where any attack
          must work, it does not perform one. Milestone at T101: 2428/2428
          sandbox checks. All laws marked as fits/extrapolations. This is not RH
          evidence. What happens to that named arithmetic bound over the next
          twenty-three parts is{" "}
          <a
            href="#compression"
            className="text-sky-700 underline decoration-sky-400/30 underline-offset-2 hover:text-sky-800"
          >
            the compression story below
          </a>
          .
        </p>
      </DiarySection>

      {/* 19 — The mechanism (T102) */}
      <DiarySection
        id="mechanism"
        plain="The moment where positivity gets hard is not a mystery: it is an exact crossing of two finite quantities, manufactured by a known coupling."
        eyebrow="19 · The mechanism · Teil 102"
        title="The onset is manufactured — an anchored crossing, not a singularity"
        badge="sandbox"
        visual={<HandoverCrossing />}
      >
        <p>
          <strong className="font-medium text-slate-800">
            The mechanism is exact.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T102]</span>{" "}
          MECHANISM-IDENTIFIED (42/42): the k-th atom acts on the three
          induction blocks E₋/E₀/E₊ as exactly{" "}
          <span className="font-mono text-slate-800">
            diag(−1/2, 0, +1/2)
          </span>
          , so the atom strength μ_k enters the handoff exactly once,
          linearly. A two-sided sandwich over the Schur profile σ_k(δ)
          brackets the handover: 2w_k lands between the two crossings in
          16/16 zones (ratio 0.749…0.940), and the onset is{" "}
          <em>anchored</em> at δ_c = 2w_k (R² 0.968). Honest correction to
          T96: the essential-singularity reading is compatible but no longer
          singled out — the onset is a crossing of two finite quantities.
        </p>
        <p>
          <strong className="font-medium text-slate-800">
            The binding constraint flips.
          </strong>{" "}
          No concentration condition binds: the bare E₋ form is strongly
          positive (2.65…3.52 — that is 4–14× the atom line μ_k/2), and the
          classical ceilings (Cauchy–Schwarz, Landau–Pollak/prolate) are
          saturated near 97%. The onset is manufactured entirely by the{" "}
          <em>Schur dressing against E₀⊕E₊</em> — the coupling to the
          induction hypothesis — which takes 35.7%…97.3% of the bare
          eigenvalue. The window law is a pure μ-power:{" "}
          <span className="font-mono text-slate-800">
            w ~ μ^(−0.563 ± 0.098)
          </span>
          , q = −1.84 ± 0.37 (fits); no log, no g_k.
        </p>
        <p>
          <strong className="font-medium text-slate-800">
            C/g was a proxy — refuted three ways.
          </strong>{" "}
          The T101 decomposition with the atom gap g_k is triply negative:
          causally impossible (Q_(k−1) is blind to the next atom&apos;s
          position), statistically dispensable (a causal law fits better),
          and arithmetically only a ceiling (C_k ≤ g_k·μ_k exactly; the
          16-zone extrapolation violates the ceiling from k = 69 — checked
          over 18 120 prime-power atoms to n = 200 000). The hard core
          localizes to one scalar per zone: a lower bound on σ_k just above
          atom entry. That is a probe-level typing of where the hardness
          sits, not progress on it. Sandbox; not RH evidence. Classical:
          Schur complement, Cauchy–Schwarz, Landau–Pollak/prolate.
        </p>
      </DiarySection>

      {/* 20 — The instrument rebuilt (T101 → T103) */}
      <DiarySection
        id="instrument-race"
        plain="What looked like a mathematical failure was a blunt tool — rebuilding the tool closed most of the map without changing the mathematics."
        eyebrow="20 · The instrument rebuilt · Teile 101 → 103"
        title="The race, rerun: the slope halves and the map jumps to 44/64"
        badge="sandbox"
        visual={
          <div className="space-y-3">
            <InstrumentRace />
            <ClosureMapGrid />
          </div>
        }
      >
        <p>
          <strong className="font-medium text-slate-800">
            T101 lost the race by the instrument, not the math.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T101]</span>{" "}
          Across 16 zones the primitives are flat and the target inequality
          never fails — but the closing instrument&apos;s race quantity r_k
          decays as r ~ exp(−0.1622k) (fit, ± 0.0562): only zone 2 closes
          throughout, 7/64 cells on the zone × wing-fraction map.
        </p>
        <p>
          <strong className="font-medium text-slate-800">
            T103 rebuilds the tool.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T103]</span>{" "}
          INSTRUMENT-IMPROVED (29/29), pure tool-building at door C: the T101
          race curve is first reproduced exactly, then re-run with a
          θ-weighted band sum (certified weights, chain ρ ≤ b_band ≤ b_tail ≤
          b_t99 at 64/64 samples) and full m(Λ) exploitation. The demand
          Λ_ok stays bounded across all 16 zones —{" "}
          <span className="font-mono text-slate-800">0.771…3.640</span>{" "}
          instead of 2.3…376, a reduction of 3.0×…103.4× — at the honest
          price of explicit modes growing 2 → 232. The new race slope is{" "}
          <span className="font-mono text-slate-800">−0.0748 ± 0.0116</span>{" "}
          (fit, 2.2× flatter): r_k falls only 9.33 → 2.70 and{" "}
          <em>never leaves the spectrum</em>. The closure map jumps 7/64 →
          44/64 with one fixed, k-uniform instrument (Λ₀ = 3, r = 2 — no
          zone tuning).
        </p>
        <p>
          <strong className="font-medium text-slate-800">
            Measured verdict: the loss is in the wing, not the bulk.
          </strong>{" "}
          θ-weighting and finite rank are exhausted — the bulk is not
          low-rank (effective rank up to 0.579·dim E₋). What remains is the
          wing slack S = 1 − ρ: the pencil is nearly saturated and S falls
          0.2091 → 0.0392. Named next levers: a wing-adapted
          prolate/Slepian basis, or a Fredholm shape of the equality
          argument. All laws are fits; the tool-problem is half solved, the
          mathematics unchanged. Sandbox; not RH evidence.
        </p>
      </DiarySection>

      {/* 21 — Two doors converge (T102 + T103 → T104) */}
      <DiarySection
        id="two-doors"
        plain="Two independent attacks ended up pointing at the same single object, so the remaining hardness is one scalar per zone, not many."
        eyebrow="21 · Convergence · Teile 102–104"
        title="Two doors, one object: the wing near-null direction"
        badge="sandbox"
        visual={<TwoDoorsConvergence />}
      >
        <p>
          Two independent attacks — door A on the handoff law&apos;s lower
          bound (T102) and door C on the closing instrument (T103) — end
          their day pointing at the <em>same</em> object. T102 finds the
          onset manufactured by the Schur dressing against E₀⊕E₊; T103 finds
          the remaining instrument loss in the wing slack S = 1 − ρ. The
          dressing and the slack are one object seen from two sides: the
          wing near-null direction.
        </p>
        <p>
          The hard core is thereby localized to one scalar per zone — a
          lower bound on the Schur profile σ_k(δ_ref) just above atom entry,
          i.e. quantitative Weil positivity at the atom edge. Provable-shaped
          next to it: resolvent edge-regularity{" "}
          <span className="font-mono text-slate-800">
            σ_k(δ) ≥ σ_k(δ_ref)·(δ/δ_ref)^q_k
          </span>
          .
        </p>
        <p className="rounded-xl border border-slate-300/40 bg-slate-100/40 px-4 py-3 text-sm text-slate-600">
          Result — T104 (SCHUR.PROFILE.BOUND, two independent arms:{" "}
          <span className="font-mono text-slate-700">
            schur_profile_bound_probe.py
          </span>{" "}
          +{" "}
          <span className="font-mono text-slate-700">
            schur_profile_chain_probe.py
          </span>
          ) is CHAIN-PARTIAL: the naive margin route is dead, exact
          spectral-split chains close 16/16 with finite data, and the hard
          core moves to a bare_k lower bound plus the soft dressing scalar L.
          From here the diary runs twenty parts of pure compression on exactly
          that core —{" "}
          <a
            href="#compression"
            className="text-sky-700 underline decoration-sky-400/30 underline-offset-2 hover:text-sky-800"
          >
            the next three sections
          </a>
          . Sandbox; not RH evidence.
        </p>
      </DiarySection>

      {/* 22 — The compression (T105–T112) */}
      <DiarySection
        id="compression"
        plain="Twenty diary parts squeeze one big matrix inequality down to a single boundary value — and a supposed wall turns out to be the measuring grid itself."
        eyebrow="22 · The compression · Teile 105–112"
        title="From one matrix inequality down to one boundary value — then a wall that turned out to be a ruler"
        badge="sandbox"
      >
        <p>
          <strong className="font-medium text-slate-800">
            The bare bound gets a closed form; the avoidance law becomes a
            theorem.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T105]</span>{" "}
          ONE-OF-TWO (28/28): the T104 arm discrepancy dissolves — one currency,
          exact split bare = μ_k/2 + b0 — and three classical steps (Bessel;
          Legendre; Cauchy–Schwarz at the pole pair) collapse into a closed lower
          bound, positive 16/16 at 81.1–92.7% of the measured value, with no
          eigenvalue and no induction data as input. The avoidance law is
          upgraded to a theorem, and an exact parity superselection appears: two
          channels that never mix.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Parity halves the object.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T106]</span>{" "}
          DENSITY-MAPPED (32/32): the Weil pole splits exactly into a positive
          rank-1 lift in the even channel and a negative rank-1 pressure in the
          odd one. The even channel closes 16/16; the odd channel — the one with
          the <em>better</em> density — carries all remaining hardness. Two
          routes are honestly killed on the way (the density chain, invariant
          amplification). What is left is one Loewner statement on half the
          dimensions.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            One scalar, then one number.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T107]</span>{" "}
          SCALAR-TRACTABLE (30/30): the matrix statement becomes exactly one
          scalar ratio{" "}
          <span className="font-mono text-slate-800">r = κ/ε ≤ 1</span>, measured
          r = 0.005…0.18 — two orders of magnitude of room instead of five
          decimal places. The symbol route is structurally dead: the certified
          symbol bound is negative (−2.54…−0.81) where the truth is positive, so
          Grenander–Szegő cannot deliver here in principle.{" "}
          <span className="font-mono text-amber-800">[sandbox · T108]</span>{" "}
          EPSILON-IDENTITY (44/44): ε turns out to be exactly the square of the
          last Cholesky pivot — the classical Szegő–Levinson prediction error —
          so its positivity <em>coincides with</em> the induction&apos;s own
          positivity rather than being an extra demand. (R) drops to two scalars,
          and on eight zones what remains is literally one boundary value of one
          explicit vector.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Both scalars certified; the circle closes on the measured zones.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T109]</span>{" "}
          BOUNDARY-CERTIFIED (29/29): the mechanism is not decay but
          cancellation (the source sits <em>on</em> the boundary), so
          Combes–Thomas is refuted with the exact Green row and replaced by a
          residual certificate that carries the cancellation instead of bounding
          it away; ω is cracked unconditionally by a graded matrix cap. The chain
          closes 16/16 on exactly one strict-margin input, 10²–10⁶ weaker than
          the conclusion.{" "}
          <span className="font-mono text-amber-800">[sandbox · T110]</span>{" "}
          MARGIN-PROPAGATES (28/28): that input propagates — certified base case,
          15 certified handover steps, and the atom entry is structurally free
          (the new atom <em>raises</em> the floor on 15/15). Three sharp gaps
          stay: no reserve, no scalar step law, no k-uniformity.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Then the ladder is driven deep — and the wall is measured, not
            extrapolated.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T111]</span>{" "}
          CROSSING-CONFIRMED (23/23): 199 zones, 117 handovers to n = 521. The
          crossing sits at n* ≈ 462 — an upper bound; T110&apos;s n ≈ 170 was a
          fit artefact — and it splits into three separate walls: the margin wall
          n ≈ 462, a twin-prime ladder wall at 521→523 (purely arithmetic), and a
          requirement wall at n = 727. Decisive detail: the handover mechanism
          itself never fails, 117/117 at retention 1.000000. The chain tears at
          a ratio, never at a step.{" "}
          <span className="font-mono text-amber-800">[sandbox · T112]</span>{" "}
          SCALING-PARTIAL (20/20): rebuilt in a frame whose cell width follows
          the local prime gap, two of the three walls fall structurally — but the
          margin wall is frame-invariant at exponent −0.974. It is the substance
          of the requirement, not the geometry.
        </p>

        <p className="rounded-xl border border-slate-300/40 bg-slate-100/40 px-4 py-3 text-sm text-slate-600">
          Eight parts, one direction: every stage removed something and named
          what was left. The honest state at T112 is a wall that survives every
          reframing — and the next part asks the question that decides its
          status: what currency is it measured in? Sandbox; not RH evidence.
        </p>
      </DiarySection>

      {/* 23 — The certification sprint (T113–T119) */}
      <DiarySection
        id="certification-sprint"
        plain="The compressed claim is then certified step by step, down to extreme depths, with the computer checking every rung."
        eyebrow="23 · The certification sprint · Teile 113–119"
        title="The wall dissolves, the depth explodes, and the last inequality gets a textbook address"
        badge="sandbox"
        visual={<DepthReachCallout />}
      >
        <p>
          <strong className="font-medium text-slate-800">
            The currency question: the wall measures the ruler.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T113]</span>{" "}
          SUBSTANCE-CONFIRMED (27/27): the falling ratio carries the same
          exponent −1.168 ± 0.259 in <em>all five</em> currencies (raw, /λ_max,
          /trace density, /D, /D²), so it cannot be normalised away. But the
          substance is not the expected one. Under refinement there is{" "}
          <em>no plateau</em>: both eigenvalues carry the same power of the cell
          width (D^1.83 and D^1.76). The continuum window form has no gap at all
          — the quantity that was falling measures the{" "}
          <strong className="font-medium text-slate-800">discretization</strong>
          , not the spectrum. And the positive floor survives only as a
          cancellation of relative size ~1e-7, so norm perturbation theory is
          five orders of magnitude too coarse. Consequence: the T109 requirement
          chain was dividing by an artifact.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Remove the division, and the wall dissolves.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T114]</span>{" "}
          WALL-DISSOLVES (22/22): rebuilt without the margin division, the exact
          Schur complement (Albert 1969) certifies 27/27 ladder steps —{" "}
          <strong className="font-medium text-emerald-800">
            eleven of them beyond the old wall, up to n = 1331
          </strong>{" "}
          — and all seven zones where the T109 chain tore, including the wall
          zone n = 449 itself. The exact object is O(0.1) with no cancellation
          (λ_min(S) = 0.068–0.154, i.e. 42–67% of the block scale), while the
          same quantity via the norm bound is negative by a factor 2.4e5–9.6e7:
          an O(1) numerator divided by a 1e-6 artifact floor. Every norm route
          <em>had</em> to fail. From here on chains stop at the compute cap
          (h ≤ 1500), never at a step.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Compression breaks the cap: a certified step at zone 155,921.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T115]</span>{" "}
          TRANSPORT-BLOCKED (26/26), with a large compression gain. Transport
          between the ladder&apos;s non-nested grids certifies only mild
          refinement — and for a principled reason, not a weak bound: on nested
          ladders, where the transport error is exactly zero, the Schur floor
          itself falls like ρ^−1.7, so no bound can undo it. The two-scale
          compression, however, keeps the step bit-exactly margin-free and{" "}
          <strong className="font-medium text-emerald-800">
            certifies a step at n = 155,921
          </strong>{" "}
          (117× deeper than T114), on a fine lattice of 93,470 cells compressed
          to 1490; the longest chain runs 10 steps, 33 certified steps over four
          chains, every certificate 10⁵–10¹¹× above the numerical noise floor.
          The stopper is cost on 3 of 4 chains and a failing step on none. The
          remaining list is the shortest of the series so far: three points, only
          one of them an inequality.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The induction step is a boundary process — and the prime comb refuses
            to be compressed.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T116]</span>{" "}
          RICCATI-PARTIAL (33/33): the global pole rides exactly in a
          12×12+12+1 state (bordered elimination, no truncation anywhere), and
          the Riccati march runs 169,236 prepends to 1,354,088 cells — 903× the
          old cap — at flat cost, 76 µs per step. Declared honestly as a
          cost-geometry demonstration, not a Weil certificate. What breaks is
          unexpected: the full symbol does not decay at all, because every
          incoming cell couples back to every prime power in the window. The
          prime comb is the object that refuses compression. Bonus, and the hinge
          of the next three parts: the one remaining inequality acquires textbook
          shape — ε is the error of a piecewise-constant Galerkin method, and
          classical Aubin–Nitsche duality hits the measured exponent.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Theorem-shaped, and no rate lost.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T117]</span>{" "}
          THEOREM-SHAPED (23/23): the family is exactly nested, so ε is a
          Galerkin best-approximation error of <em>one</em> bilinear form and its
          monotonicity is a theorem rather than a fit; positivity becomes a
          non-membership statement. The direction trap is handled in the open —
          Céa and Aubin–Nitsche give <em>upper</em> bounds — and the two-level
          chain delivers a certified <em>lower</em> bound on 19/19 pairs
          (bound/ε ∈ [0.111, 0.185]) at rate θ&apos; = 1.74 against θ = 1.76: no
          power of D is lost. Self-correction: T116&apos;s factor-120 jumps were
          a sweep artifact — all 23 prime-power entries actually{" "}
          <em>raise</em> ε. What remains is three named analytic lemmas about one
          symbol, each with a classical address, two of them constants rather
          than rates.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Two of three lemmas stand — and the arithmetic half closes as a
            theorem.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T118]</span>{" "}
          TWO-OF-THREE (36/36): the first route is refuted with a reason (the
          exact two-grid symbol is a <em>harmonic</em> mean, which the comb dips
          make vacuous on 14/14 windows), and the rescue is a classical shift
          onto the oscillation Gram, whose symbol is the{" "}
          <em>arithmetic</em> mean of the same aliasing pair — the low-frequency
          negativity is suppressed quadratically instead of poisoning the
          statement. On a 15,680-point FFT lever the certified floor rises
          logarithmically and crosses zero on 3 of 5 zones: the failing windows
          were under-resolved, not obstructed. Saturation turns out to be an
          identity here, so its constant is computed (0.252–0.336) rather than
          assumed.{" "}
          <span className="font-mono text-amber-800">[sandbox · T119]</span>{" "}
          ARITHMETIC-DONE (27/27): the arithmetic half closes as a theorem —
          positivity of the symbol for every cell width below an{" "}
          <em>explicit</em>{" "}
          <span className="font-mono text-slate-800">
            D₀(α) = exp(−(Ξ(α) + B))
          </span>
          , with Ξ the prime-power atom count and B = −1.0474 universal (drift
          ≤ 3.1e-4). The energy route to the remaining statement is proven{" "}
          <em>empty</em> — a tautology — which is what makes that statement
          genuinely new content. And the sharpest identity of the run,{" "}
          <span className="font-mono text-slate-800">κ_end = 1/(1+R)</span>{" "}
          exactly (1.1e-16), reduces everything to one discrete Harnack
          inequality with a classical address.
        </p>

        <p className="rounded-xl border border-slate-300/40 bg-slate-100/40 px-4 py-3 text-sm text-slate-600">
          Worth stating plainly, because it is the load-bearing fence of the
          whole sprint: this chain is classical numerical analysis from end to
          end and{" "}
          <strong className="font-medium text-slate-800">
            contains no zeta input anywhere
          </strong>
          . As a conditional lemma the material is essentially complete — what is
          missing is a proof of the Harnack statement, not a discovery. Sandbox;
          not RH evidence.
        </p>
      </DiarySection>

      {/* 24 — The Harnack pair, the telescope, and the assembly (T120–T125) */}
      <DiarySection
        id="harnack-telescope"
        plain="The final assembly runs the whole chain end to end on 52 zones; what is still missing is uniformity — one sign plus one declared convention."
        eyebrow="24 · The Harnack pair, the telescope, the assembly · Teile 120–125"
        title="Why the last constant is one, why the coupling resists, the direction flip that made the recursion carry — and the finale that composed the whole chain"
        badge="sandbox"
        visual={<TelescopeRungs />}
      >
        <p>
          <strong className="font-medium text-slate-800">
            The Harnack core becomes proof-shaped — at the price of one more
            defect.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T120]</span>{" "}
          HARNACK-EXPLAINED (21/21): the mysterious constant R ≈ 1 is not a
          constant at all but a <em>symmetry</em>. The two increment families are
          the odd and the even half of <em>one</em> sequence, offset by a single
          fine cell — so given one sign on the corner cells their difference is a
          sum over disjoint neighbour pairs, and{" "}
          <span className="font-mono text-slate-800">|R − 1| ≤ 0.04745</span>{" "}
          follows <em>unconditionally</em>, dominating the measurement on
          3112/3112 sign-pure rows. Two negative results count as much: the
          per-cell version of the inequality is provably <em>false</em> (ratios
          up to 4.8e3 — only the summed form holds, which is exactly the form
          proved), and the discrete maximum principle is false too, so the sign
          route is closed and needs a corner-localized decay estimate instead.
          The honest cost: the defect count rises 3 → 4, because in the real
          frame the window grows with the zone, and the unconditional D₀
          criterion then covers exactly 3 of 1492 zones — below the first
          handover the ladder actually uses.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Against the real ladder: a section statement survives where a symbol
            statement dies.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T121]</span>{" "}
          WIDE-RESTRUCTURED (21/21): the chain never needed the symbol to be
          positive — it needs the finite <em>section</em> to be, at the
          frame&apos;s own resolution. Over 16 windows of the real ladder
          (n = 7…283,303) the section is positive 16/16 while the symbol infimum
          is negative on 8 of them; where it is negative the section eigenvalue
          sits on the positive side at 0.64–3.23× its size. The mechanism has a
          classical address (Christoffel functions): a polynomial of that degree
          cannot fit inside one comb dip. The measurement discipline is kept
          explicit — dense rows carry a Cholesky certificate, large rows are
          labelled measurements, because a Ritz value can refute positivity but
          never prove it. The net balance is then computed instead of feared:
          only a poly-log deficit (α^−1.57, uniform in the resolution) rather
          than collapse, decomposed exactly into two repairable steps — and one
          link of the chain is honestly refuted on 42/42 rows.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            Both repairs land: the refuted link was an identity all along.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T122]</span>{" "}
          NET-IMPROVED (20/20): the term that broke T121&apos;s link is not an
          error term but the reflection half of an{" "}
          <strong className="font-medium text-slate-800">isometry</strong> — the
          oscillation block is exactly a compression of one window Toeplitz form.
          From that plus a certified cell envelope and Parseval follows a
          certified band floor, non-vacuous 36/36 up to α = 6.31, where
          T121&apos;s budget tore at 3.45. The structural version of the
          Rayleigh step is <em>sharp</em> (slack 1.00–1.03, drift α^−0.002): no
          α-dependence passes through it any more. Certified deficit halves to
          α^−0.729 and is exactly uniform in the resolution; with the measured
          coupling the balance reads α^−0.113 against the chain&apos;s own
          ceiling α^−0.116 — statistically indistinguishable. The chain closes up
          to its own ceiling as soon as the coupling step stops being a worst
          case.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The coupling resists — structurally, and the reason is the result.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T123]</span>{" "}
          CBS-RESISTS (20/20): the band margin closes almost for free (that
          reduction costs under 1%) and the oscillation block gains{" "}
          <em>uniform</em> certified positivity on every row of the ladder. But
          every certified route to the coupling needs the coarse form from below,
          and there the numbers are brutal: λ_min of the coarse block is
          1.7e-5–2.9e-4, three to five orders below the certified envelope. The
          diagnosis is exact — the near-null direction of the window form is{" "}
          <em>smooth</em>, so it lives in the coarse space, and its eigenvalue
          comes from a cancellation <em>inside</em> the form that no pointwise
          symbol minorant can see. So the worst-case coupling step must stay, and
          the theorem now says why. The entire remaining gap (α^0.5) is that one
          coupling — and it is identified, not estimated: it is the same object
          as the lid the chain throws away, four to eight recursion levels deep.
          Verdict: the two-level argument cannot be tightened. It has to become a
          recursion.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The telescope carries — because the rung is a maximum.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T124]</span>{" "}
          TELESCOPE-CARRIES (28/28): the nested level chain is <em>one</em>{" "}
          window form on nested spaces (nesting exact to 2.4e-14), so the whole
          two-level system of the previous part is literally one rung of a
          ladder, every rung is the saturation identity, and the rungs telescope:
          their sum is the whole quantity (9.2e-10). Then the key of the part —
          the <strong className="font-medium text-slate-800">
            direction flip
          </strong>
          . Read as a residual in the inverse norm, the rung is a{" "}
          <em>maximum</em>, not a minimum: every test vector gives a{" "}
          <em>lower</em> bound, and the denominator wants the form from{" "}
          <em>above</em> — exactly where the certified machinery works. The
          resulting certified rung bound holds on 400/400 rungs with a drift
          seven times weaker than T123&apos;s. T123&apos;s obstruction is still
          there and is now irrelevant: the new bound never forms the object that
          was obstructed. The recursion closes in the right direction, coarse to
          fine, with base case pure semidefiniteness — and the balance moves
          +0.444 of the α^0.5 gap, about nine tenths of the way to the ceiling.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            What that leaves — stated as the diary states it.
          </strong>{" "}
          The coupling defect{" "}
          <em>collapses</em>: it is no longer a quantitative estimate but a sign
          that the coarse-to-fine induction already carries, and three quantities
          (the coarse minimum, its condition number, and the coupling constant)
          leave the chain entirely. One new defect is booked, honestly negative:
          the solution-free version of the rung fails, because the coupling term
          cancels the data instead of perturbing it — so the certified bound
          carries the solution along, on the same bookkeeping standard as the rest
          of the chain. The Harnack pair from T120/T121 is untouched.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            The finale: the chain composes, and the Harnack pair leaves the
            spine.
          </strong>{" "}
          <span className="font-mono text-amber-800">[sandbox · T125]</span>{" "}
          ASSEMBLY-GREEN (34/34): every certificate of the arc mounted on one
          ladder, end to end. All five stages — base Cholesky, telescope rungs, ε
          lower bound, the κ chain, the margin-free handover — complete on 52 of
          52 zones, and 30 of those zones form a run that{" "}
          <em>literally composes</em>: consecutive prime-power atoms on{" "}
          <em>one</em> common resolution, so the new window of a zone{" "}
          <em>is</em> the old window of the next one (an integer identity on
          29/29 pairs), the incoming atom&apos;s block is bit-exactly zero, and
          the output of every step is the input of the next (residual 2.9e-14).
          That is a way <em>around</em> the frame seam rather than through it: no
          two consecutive gap ratios are dyadic, so per-zone frames can never be
          refined onto one another — the run picks one frame for all of it and
          pays with its length. The load-bearing finding is a change of shape:
          the weakest stage of the whole mounting is the κ chain, but that chain
          is the second, independent route — the{" "}
          <strong className="font-medium text-slate-800">
            load-bearing spine is Cholesky-certified on all 52 zones
          </strong>
          , so the Harnack pair no longer carries anything. 430 completed
          Cholesky certificates, 440 identities, the certified margin a factor
          32–8.7e10 above the <em>declared</em> floating-point bound, and the
          base case an <em>equivalence</em> rather than a bridge.
        </p>

        <p>
          <strong className="font-medium text-slate-800">
            And then the accounting.
          </strong>{" "}
          Theorem V-final is printed with line-by-line attribution — 25 lines: 10
          identities, 9 Cholesky certificates, 3 window certificates (all three
          inside the route the spine does not use), and exactly{" "}
          <em>one</em> hypothesis, which is an accounting convention — plus a
          five-point statement of what is <em>not</em> claimed. Of the 31 links
          of the chain, 90.3% are an identity or a completed Cholesky; on the
          spine it is 96.2%, with zero window certificates. The series ledger:
          24 refuted routes across 18 parts, four of them killed by the{" "}
          <em>same</em> cause — a bound that needs the coarse form from below,
          which is why the exit was a direction flip and not a sharper estimate —
          and a seven-station cascade whose last station is new. What remains is
          named as what it is: <em>uniformity</em> in the zone index, not size.
        </p>

        <p className="rounded-xl border border-slate-300/40 bg-slate-100/40 px-4 py-3 text-sm text-slate-600">
          Where the series ends: a finite, machine-certified chain whose
          load-bearing spine is 96.2% identity or Cholesky certificate and
          whose only hypothesis is a declared accounting convention; a relay
          mechanism that never failed a step; and certified single steps as
          deep as zone 155,921. What does not stand is uniformity in the
          zone index — and that, not any missing estimate, is the honest
          distance to any infinite statement. The distance to RH remains
          large. The series completed at 125 parts and 3139/3139 sandbox
          checks; the second phase — &ldquo;the full proof&rdquo;
          (T126–T176) — then closed its measurement programme as planned,
          with the exact cores load-bearing as v562 and the work continuing
          in the backflow rounds of the live feed below. The complete
          end-of-series recap is preserved verbatim behind the expander.
          Sandbox; not RH evidence.
        </p>
        <VerbatimRecap
          id="seriesEnd"
          className="mt-3"
          label="The full end-of-series + phase-2 recap (T125–T176), preserved verbatim"
        />
      </DiarySection>

      {/* 25 — Meaning */}
      <DiarySection
        id="meaning"
        plain="Four honestly calibrated levels of what this could mean — from done-and-verified to dream-not-claimed."
        eyebrow="25 · What would it mean"
        title="Four calibrated levels — with caveats"
        badge="sandbox"
      >
        <ol className="space-y-3">
          <MeaningLevel
            level="Done"
            badge="machine-verified"
            title="Mechanism + finite RTF + Weil structure + amplitude route + proof package"
            body="v535–v537: Hecke, Eichler, half-integral bridge. v538: one finite relative-trace identity. v539: Weil structure fully identified up to two explicitly isolated obstructions. v540: amplitude Dirac + geometric polarisation with the Cohen seed Θ(d) = −48·L(−1,χ_d), the universal even-k deletion as square-class double counting, the positive linear carrier with plus-only ζ-balance, and the exact FE — with the open boundary λ* named inside the claim. v541: the T78–T85 proof package — matching lemma proved exact-integer on [4, 10⁶], transport ledger closes exactly (Δ_pole ≡ Δ_conv ≡ 0 proven), character-exact signed envelope, arch internal via Legendre duplication, coherent class closed by the λ-equivariant CM channel — with the two named limits inside the claim."
          />
          <MeaningLevel
            level="Near"
            badge="sandbox"
            title="I5 geography complete; the induction compressed to one sign plus one convention, and assembled end to end"
            body="After 230 probes (5360/5360 sandbox checks) and the promoted modules v535–v564 plus v569–v570, v573 and v576–v596 of this arc: the matching lemma is closed, the I5 geography is complete, and the induction that would carry I5 is compressed from one matrix inequality (T104) to a sign the coarse-to-fine recursion already carries plus one declared accounting convention (T124/T125) — assembled end to end on 52 zones in the T125 finale, its load-bearing spine 96.2% identity or Cholesky certificate. What remains TFPT-specific is one object, I5 ⟺ Weil positivity ⟺ RH (an equivalence typing, not a proof claim); what is missing is uniformity in the zone index, and the phase-2 measurement programme on it closed as planned (T176; exact cores load-bearing as v562). Not RH evidence."
          >
            <VerbatimRecap
              id="nearLevel"
              className="mt-2"
              label="The full &lsquo;Near&rsquo; status paragraph, preserved verbatim"
            />
          </MeaningLevel>
          <MeaningLevel
            level="Big if"
            badge="sandbox"
            title="A genuinely new functor"
            body="A compiler functor that is Hecke-translating, Euler-preserving, and ξ-carrying without smuggling ζ from outside. Kills are preregistered; classical named pieces stay classical (Weil 1952, Waldspurger, Cohen 1975, Shintani, Cauchy–Littlewood, Hilbert–Carleman det₂, Connes 1999, Connes–Consani 2021 as context)."
          />
          <MeaningLevel
            level="Dream"
            badge="sandbox"
            title="Riemann Hypothesis"
            body="Not claimed. Not evidenced. I5 ⟺ RH is an equivalence typing of the irreducible core — not a proof claim. Crypto unaffected."
          />
        </ol>
      </DiarySection>

      {/* 26 — Prime shadow */}
      <DiarySection
        id="prime-shadow"
        plain="Within TFPT's narrative the direction of explanation is fixed: the geometry comes first, and primes read it out — even zeta appears as the shadow of a counting function."
        eyebrow="26 · The prime shadow · v625"
        title="Primes enter after the geometry — exactly"
        badge="machine-verified"
      >
        <p>
          An external note asked: what if primes are not the origin but the{" "}
          <em>readout</em> — the shadow of the finished geometry in discrete
          arithmetic? The checkable core of that reading is exact, on the
          compiler&apos;s own objects. The E₈ theta function, computed from
          the glue decomposition, <em>is</em> the Eisenstein series{" "}
          <span className="font-mono text-slate-800">Θ_E8 = E₄</span>: shell
          counts{" "}
          <span className="font-mono text-slate-800">r(2n) = 240·σ₃(n)</span>,
          and the first shell is literally 240 — the root count.
        </p>
        <p>
          The “address space” reading is unique factorization, exactly (shell
          counts factor over coprime addresses; the must-fail control shows
          non-coprime does not). The “independent check channels” reading is
          a theorem: the Hecke operators{" "}
          <span className="font-mono text-slate-800">T_p</span> act with
          eigenvalue{" "}
          <span className="font-mono text-slate-800">1 + p³</span> for every
          prime, they <em>commute</em>, and the compiler&apos;s theta is a
          simultaneous eigenvector of all of them. And{" "}
          <span className="font-mono text-slate-800">
            L(E₄, s) = ζ(s)·ζ(s−3)
          </span>
          : the Riemann zeta function appears as the factorized shadow of the
          E₈ counting function.
        </p>
        <p className="text-slate-600">
          Honest scope: these are classical facts (Jacobi, Hecke) — the
          content is that the compiler&apos;s own objects realize them
          verbatim, fixing the direction of explanation inside TFPT&apos;s
          narrative: geometry first, primes as readout. The bolder framings
          (“primes as compiler eigenfrequencies”, “RH as maximal coherence”)
          stay typed hypotheses, not adopted.
        </p>
      </DiarySection>

      {/* 27 — E8 code */}
      <DiarySection
        id="e8-code"
        plain="The E8 lattice literally is an error-correcting code, and the compiler's own symmetries pick out its bits."
        eyebrow="27 · The error-correcting code · v626 / v638"
        title="E8 is literally a code — and the compiler reads its bits"
        badge="machine-verified"
      >
        <p>
          “E₈ is an error-correcting code” is now a theorem in the suite:
          Construction A on the self-dual extended Hamming code{" "}
          <span className="font-mono text-slate-800">[8,4,4]</span> — the
          Reed–Muller code RM(1,3) — yields E₈ exactly (even, unimodular,
          shells 240/2160), and every single-bit error is exhaustively
          correctable: 16×8 corrupted words, a unique nearest codeword every
          time (v626). Round-22 fence: the <em>stronger</em> reading — E₈ as
          an error-correction <em>hull</em>, the 240 root operators plus the
          16 neutral kernels as a twisted group-algebra basis of End(S₊) —
          died as preregistered (SYNDROME-DEAD, v805); the Construction-A
          theorem here is untouched.
        </p>
        <p>
          v638 then made the dictionary compiler-native instead of decorative.
          Stage 1 killed the naive coordinate placement; among all 30
          placements of the code exactly <em>one</em> (up to the anchor
          orientation) carries both compiler symmetries. On that placement
          the code&apos;s coordinates organise as{" "}
          <strong className="font-medium text-slate-800">
            four μ₄ pairs — one bit per pair
          </strong>
          : the family 3-cycle rotates three of the pairs and fixes the
          fourth, the anchor —{" "}
          <span className="font-mono text-slate-800">
            3 families + 1 anchor
          </span>
          , read off the code. The placement reproduces the v629 root
          censuses verbatim, and the syndrome space factors along the same
          structure.
        </p>
        <p className="text-slate-600">
          Compiler ties, typed: 8 = rank, 4 = d = |μ₄|, 16 = the carrier
          half-spinor. Robustness language on this page now has an exact
          anchor — a code with a decoder, not a metaphor.
        </p>
      </DiarySection>

      {/* 28 — Lorentz congruence / Hodge chamber */}
      <DiarySection
        id="hodge-chamber"
        plain="Two programmes that seemed unrelated were computing on the same lattice all along — and every data window lands in one chamber of it."
        eyebrow="28 · One Lorentz lattice · v624 / v627 / v635–v637"
        title="The prime form and the cover lattice are the same geometry"
        badge="machine-verified"
        visual={<HodgeConeMap />}
      >
        <p>
          The surprise of the third external review (v624): an explicit
          integer matrix P with det −6 satisfies{" "}
          <span className="font-mono text-slate-800">
            Pᵀ J_det P = J_fix
          </span>{" "}
          exactly — the prime-front determinant form (det 2) and the cover
          polarization lattice of the geometry program (det 72) are the{" "}
          <em>same</em> rational quadratic form, the cover an index-6
          sublattice. A genuine new bridge between prime analysis and Hodge
          geometry: the two programs this diary has been running were
          computing on one lattice.
        </p>
        <p>
          v627 measured what that buys: transported through the congruence,{" "}
          <strong className="font-medium text-emerald-800">
            all 67 complete windows land in the positive cone
          </strong>{" "}
          of the cover polarization lattice — on one sheet, det S &gt; 0
          everywhere. v635/v636 then closed the “found matrix” worry: P is
          the unique minimal, operator-compatible congruence in its census
          class, and it is <em>constructed</em> from canonical operator data
          (the null-cone rays are exactly ker C_V and fix C_V), not guessed.
        </p>
        <p className="text-slate-600">
          Honesty, twice: chamber membership is a density-layer statement —
          scrambled combs do not leave the chamber (v582) — so the fine
          C&nbsp;=&nbsp;1 arithmetic lives <em>inside</em> the chamber; and
          v637 closed the tempting follow-up as a preregistered negative: the
          fine Hodge-ray invariants do <em>not</em> predict the C = 1 margin
          window-wise beyond the trivial h-trend.
        </p>
      </DiarySection>

      {/* 29 — ST31 */}
      <DiarySection
        id="sixty-lines"
        plain="The quotient of the lattice is a classical sixty-line reflection group — and a tempting numerical coincidence about its size is killed, not celebrated."
        eyebrow="29 · The sixty lines · v633 / v634"
        title="The μ₄ quotient is a classical reflection group — and a numerology is buried"
        badge="machine-verified"
      >
        <p>
          v629 left a sharp positive residue: the μ₄ clock acts freely on the
          240 E₈ roots with exactly 60 orbits — and 60 = D_start, the
          cascade&apos;s starting value. v633 built the quotient properly:
          the 60 orbits are 60 lines in{" "}
          <span className="font-mono text-slate-800">ℤ[i]⁴</span> carrying a
          hermitian form (the “complex E₈”), and the 60 order-2 unitary
          reflections they define generate a group of order{" "}
          <span className="font-mono text-slate-800">46080</span>.
        </p>
        <p>
          v634 identified it: exactly 60 reflections, invariant degrees{" "}
          <span className="font-mono text-slate-800">(8, 12, 20, 24)</span> —
          the Shephard–Todd group{" "}
          <strong className="font-medium text-slate-800">G31</strong>, pinned
          by fingerprints computed, not cited. The compiler sits inside it
          canonically:{" "}
          <span className="font-mono text-emerald-700">
            σ = c⁴, J = c⁹
          </span>{" "}
          — the family 3-cycle and the μ₄ clock are <em>powers of one
          order-12 element</em>, and the μ₄ center is a power of the clock.
        </p>
        <p className="text-slate-600">
          The kill that keeps it honest: |G31| = 46080 = |W(D₅)|·|W(A₃)| —
          the compiler&apos;s glue factors — looks like destiny and is{" "}
          <strong className="font-medium text-rose-800">numerology</strong>.
          The abstract isomorphism dies on cheap invariants, and stronger:
          W(D₅) embeds in <em>no</em> rank-4 group at all, so the order
          coincidence carries no subgroup structure. Also reproduced one
          level deeper: the compiler clock is <em>not</em> the ζ₁₂-regular
          element of G31 (census 19×12 + 3×4) — the v629 kill stands.
        </p>
      </DiarySection>

      <AugustOffensivesSection />

      <FiniteClosureSection />

      <SigmaChainSection />

      <KillAtlasSection />

      <RealRootSignposSection />

      <SvpinKreinSection />

      <CohomSpecSection />

      <ThreeLemmaFormsSection />

      <RoadmapSection />

      <FrontierAuditsSection />

      <UnpricedResolventSection />

      {/* 41 — Live updates */}
      <section
        id="updates"
        aria-labelledby="updates-heading"
        className="scroll-mt-24 border-t border-slate-200/60 py-12 sm:py-16"
      >
        <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
          <div className="flex flex-wrap items-center gap-2">
            <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
              41 · Live updates
            </span>
            <StatusBadge badge="sandbox" />
          </div>
          <h2
            id="updates-heading"
            className="mt-3 font-serif text-2xl font-semibold text-slate-950 sm:text-3xl md:text-4xl"
          >
            Feed — one entry per completed agent run
          </h2>
          <div className="mt-8">
            <DiaryFeed />
          </div>
        </div>
      </section>

      <footer className="border-t border-slate-200/60 py-10">
        <div className="mx-auto max-w-5xl px-4 text-sm text-slate-600 sm:px-6 lg:px-8">
          Numbers and verdicts are taken from{" "}
          <code className="font-mono text-slate-600">experiments/next.txt</code>{" "}
          (2026-07-23 … 2026-08-02 diary and backflow rounds) and the promoted
          modules{" "}
          <code className="font-mono text-slate-600">
            verification/v535_*.py
          </code>{" "}
          …{" "}
          <code className="font-mono text-slate-600">v648_sign_uncertainty.py</code>.
          Exploratory probes live under{" "}
          <code className="font-mono text-slate-600">
            experiments/tfpt-discovery/
          </code>
          .
        </div>
      </footer>
    </>
  );
}

function AugustOffensivesSection() {
  return (
    <section
      id="august-offensives"
      aria-labelledby="august-offensives-heading"
      className="scroll-mt-24 border-t border-slate-200/60 py-12 sm:py-16"
    >
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center gap-2">
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
            30 · The proof offensives of August 3 · v682–v735 + sandbox probes
          </span>
          <StatusBadge badge="machine-verified" />
          <StatusBadge badge="sandbox" />
        </div>
        <h2
          id="august-offensives-heading"
          className="mt-3 font-serif text-2xl font-semibold leading-tight text-slate-950 sm:text-3xl md:text-4xl"
        >
          One day, five offensives — four pictures
        </h2>
        <p className="mt-3 max-w-3xl border-l-2 border-sky-400/40 pl-3 text-[15px] leading-relaxed text-slate-600">
          <span className="font-medium text-sky-700/90">In plain words: </span>
          on August 3 the diary ran five parallel proof offensives against the
          open positivity step — and kept going: fifty-four modules were
          promoted in six rounds (v682–v735), closing the day with the
          moonshot arc measured end to end (glue, state, spectrum, trace
          formula — no theorem, no RH claim) and the keystone round — the
          wall stated in four equivalent languages (moments, state, symbol,
          Hamiltonian) — and the sandbox probes found a
          new geometric picture of how the primes fit into their windows. These four schematics show
          the day&apos;s load-bearing shapes — with the promoted results and
          the still-exploratory ones clearly separated.
        </p>

        <div className="mt-6 max-w-3xl space-y-4 text-base leading-relaxed text-slate-700">
          <p>
            <strong className="font-medium text-emerald-800">
              Promoted (machine-verified):
            </strong>{" "}
            v691 extracted the target factorisation A = B*B + P from the
            Ihara lab — the RH analogue as <em>one operator inequality</em>,
            with the missing ζ-side part named and registered open (Z1). The
            T-B chain (v692 + v693) typed the razor-thin absorption margin as
            a sum of squares and closed it on 60 of 70 complete windows
            unconditionally-modulo-citations, with the exact remainder
            listed window by window.
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              Sandbox (exploration, not promoted):
            </strong>{" "}
            the chain probes measured a <em>just-in-time positivity
            corridor</em> for every prime-power slot — the true mass sits
            inside every corridor at a stable relative position ≈ 0.53 — and
            found the three digamma channels of the arch density realized
            exactly as the deck sectors of the cover lift. Both are search
            surfaces: no claim moves until they are promoted.
          </p>
        </div>

        <div className="mt-8 grid gap-4 lg:grid-cols-2 lg:items-start">
          <IharaBlueprintViz />
          <TBWindowMap />
          <KorridorViz />
          <DeckSectorViz />
        </div>

        <p className="mt-6 max-w-3xl text-sm leading-relaxed text-slate-600">
          Honest fence, as everywhere on this page: the promoted results are
          statements about the declared finite window family and the Ihara
          laboratory — full W3 positivity (the RH-hard step) remains the
          conjecture, PRIME.Z1.OPERATOR.01 remains open (sharpened 2026-08-05
          with the measured qf handover constraints after the closure of
          PRIME.GRAM.DIAGONAL.01, and executed the same day as the v780
          trilogy: the compactness half is measured carried, and the
          selection half — once the one shared open object with
          PRIME.KMS.INDUCTIVE_STATE.02, merged target Z1-COMPACTNESS — was
          finite-level solved in round 23 by Mosco + Friedrichs (v816),
          leaving the sector floor as the single analytic remainder,
          registered as the fenced open contract PRIME.FLOOR.RATIO.01:
          one ratio inequality ρ = τ/τ_pnt &gt; 0 with a measured h^-3/2
          envelope — narrowed in round 24 by the certified floor
          skeleton (v823 Lagrange sum-of-squares + certified fixed pair;
          v824 analytic fixed-pair bound, 0.93–0.97 family exhaustion,
          and the deep tail closed at citation grade for all h at
          T_ver = 3e12, validity horizon α* ≈ 11), depth-hardened
          in round 25 (v829 kill gates survived at full sieve depth
          X = 25.5 with growing margins; v830 Higham-linear budget:
          the α* horizon falls as a float-convention artifact, the
          envelope certified-explicit at 4.335·h^-3/2 on 73/73, the
          alias-phase proof blocker named), and closed on its
          analytic-envelope flank in round 26 (v831: the blocker
          resolves into a typed pair-correlation circularity
          boundary — the amplitudes, not the phases, carry the
          tower gap, and by Guinand the comb&apos;s sqrt-scale
          self-cancellation IS the zero-side floor statement; the
          route is stop-listed and the bridge contract
          PRIME.FLOOR.PAIRCORR.01 [O] registered), with both
          corner-era routes at that wall decided in round 27
          (v835: the character-corner identity is weight-generic
          and the Hjelmslev CP tower strictly projective — but
          comb-blind, so the wall relocates into the
          identification step; v836: the commutant SOS route
          closed definitively by exact certificates; both
          stop-listed), and the wall given its full coordinate
          system in round 28 (v837/v838: the closure quantifier
          measured — no register, compression or state-preserving
          position-dependent carrier identifies, because the
          identity is an EXTREMAL state condition; v839/v840: the
          demand saturates the GUE boundary structurally and the
          bootstrap loop is short — the wall conserves itself
          through the saturation; v841/v842: the route REOPENS
          with the relational input — the identification carrier
          exists, the identified corner&apos;s excess is positive
          on all 67 rungs, and the certified skeleton encloses
          τ_X strictly positively: the wall = the infinite
          quantifier over strictly-positive certified enclosures,
          sharpened demand a uniform lower bound on the excess
          margin), and closed out in round 29 (v843: the margin
          becomes the doubly-derived typed law
          τ = e₁·h^(−3/2)·τ_pnt with the envelope constant
          reproduced exactly across both coordinate systems, the
          tower giving scale not recursion, the excess a growing
          cancellation — the wall self-similar at cell level —
          and the finite-table limit kernel-checked in Lean:
          ExcessSkeleton.lean proves pointwise_pos_not_uniform
          and carries UniformMarginBound as the single named
          hypothesis; the quantifier now sits on the one scalar
          series e₁ ≥ 4.335), and consolidated in round 30
          (v846/v847: the three candidate proof architectures are
          decided — the relational Schur–Gram dies structurally at
          the forced Cauchy–Schwarz price and the price is
          geometry-independent (the unitary spectral mother gains
          20–33× at symbol grade but never at Gram grade:
          harvesting interference is Fejér–Riesz of the total
          symbol, i.e. the positivity itself), the sign-register
          wedge lift exists as exact algebra but the frame-uniform
          law dies on the commutant uniformity wall, and the
          completed-cell cone transport breaks at the n = 2 cell —
          the arithmetic sits IN the violations; v848: the
          continuum extraction chain is COMPLETE — cofinal finite
          positivity, cofinal in the mesh-refinement order,
          ⇒ Weil positivity ⇒ the target, theorem-grade
          modulo named citations, with no Mosco compactness, no
          uniform δ and no diagonal argument in the implication,
          so the wall is exactly hypothesis (H), registered
          PRIME.EXTRACTION.CHAIN.01 [O]) —
          battery-relative, and
          still no positivity theorem on V_∞), and
          nothing here is a claim of progress toward the Riemann
          Hypothesis.
        </p>
      </div>
    </section>
  );
}

function FiniteClosureSection() {
  return (
    <section
      id="finite-closure"
      aria-labelledby="finite-closure-heading"
      className="scroll-mt-24 border-t border-slate-200/60 py-12 sm:py-16"
    >
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center gap-2">
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
            31 · The finite closure and the phase architecture · v905–v911 +
            sandbox probes
          </span>
          <StatusBadge badge="machine-verified" />
          <StatusBadge badge="sandbox" />
        </div>
        <h2
          id="finite-closure-heading"
          className="mt-3 font-serif text-2xl font-semibold leading-tight text-slate-950 sm:text-3xl md:text-4xl"
        >
          The finite wall closes — and gets a price tag
        </h2>
        <p className="mt-3 max-w-3xl border-l-2 border-sky-400/40 pl-3 text-[15px] leading-relaxed text-slate-600">
          <span className="font-medium text-sky-700/90">In plain words: </span>
          the reflux rounds sixty-four through seventy-one finish the{" "}
          <em>finite</em> surface of the wall end-form: every reachable wall
          face on the deployed ladder is now certified from cited inputs, the
          zero supply that certification consumes is measured and priced, and
          the sandbox probes map the <em>phase architecture</em> behind the
          wall — with the promoted results and the still-exploratory ones
          clearly separated, as always.
        </p>

        <div className="mt-6 max-w-3xl space-y-4 text-base leading-relaxed text-slate-700">
          <p>
            <strong className="font-medium text-emerald-800">
              Promoted (machine-verified):
            </strong>{" "}
            <em>the finite wall closure</em> (v909): the composed census B ∧
            W1 ∧ W2 holds on 39/39 matched surface + 8/8 deep rungs — the
            B-half via the interval-certified floor min c_B = 0.5523 (v905),
            the W1 face via one exact measure inequality (the two +8..+9 dex
            composition gaps of earlier rounds dissolve into a single Loewner
            step) plus <em>verified zeros as exact data</em> at the named
            j = 16 seat, and the W2 face via the recomposed certificate paid
            by a 20,000,000-ordinate certified cache (Odlyzko + LMFDB/Platt,
            every ordinate below the Platt–Trudgian height 3·10¹² — cited,
            never assumed). The honest typing is frozen and non-negotiable:
            W1 and W2 are <em>algorithmically independent evaluations of the
            same localized Weil form</em> — a strong mutual crosscheck, not
            two independent proofs; positivity is certified on a finite
            family of Galerkin sections <em>along the measured critical
            direction</em>, never uniformly. And <em>the transfer law</em>{" "}
            (v910): the zero-cutoff height the certificate actually consumes
            grows as T_req ~ h^2.8, and its ratio to the window&apos;s own
            spectral reach π/D <em>grows</em> too (+0.897 dex per ln h) —
            the zero supply is an <em>external battery</em>, not a local
            sampling law. The whole census compresses into one statement:
            zeros certified up to T plus the unconditional tail envelope
            imply the wall for all deployed h ≤ H(T), with H measured at
            254 / 1256 / 2806 for the three historic cache heights. The
            finite engine does not scale by buying zeros; H(T) is the
            measuring rod any future analytic per-window bound has to beat.
            (The seam-side row of the same promotion, v911, closes the
            wiring-selector contract as a freedom theorem — pure-I is a
            deployment representative, not a compiler theorem; it lives in
            the research-contracts companion.)
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              Sandbox (exploration, not promoted):
            </strong>{" "}
            the phase architecture. The <em>Euler phase identity</em>: the
            wall read is exactly the derivative of a completed unitary Euler
            phase — warded on three levels, with the honest verdict that the
            bare identity is a coordinate change (it survives all five
            falsifying worlds, as predicted); the discriminating content
            sits in the <em>grouping</em>: of the five Euler grouping axioms
            G1–G5, G2&apos;s parameter-free weight law is the one measured
            structure that separates the true prime comb from every control
            world. The <em>Krein index census</em>: the deployed phase is
            not a generalized Schur function of finite negative index — the
            index grows proportionally with resolution (slope +0.997, no
            saturation), the half-gap shift removes zero negative
            directions, and the cosh control shares the full index
            signature: verdict WALLPAPER, the route buried by its own
            pre-frozen kill criterion. And the <em>Zolotarev compression</em>:
            one global fixed eight-pole rational filter certifies all 68
            ladder steps (per-rung optimum three to five poles), compressing
            the old degree-119 certificate into eight resolvents — the
            ONEBADMODE certificate becomes finitely many determinant-phase
            values, with the honest caveat that the filter&apos;s
            observer-complexity grade sits far above the half-gap class.
            All three are frozen sandbox probes: no claim moves until they
            are promoted.
          </p>
        </div>

        <p className="mt-6 max-w-3xl text-sm leading-relaxed text-slate-600">
          Honest fence, as everywhere on this page: the finite closure is a
          statement about the deployed finite ladder from cited inputs — a
          finite verified-zero sum can never prove RH, the all-h and
          all-direction objects (the UNIF-PATH caveat) stay open, the
          registered ½ stays underived, and the transfer law itself says the
          finite engine cannot reach deeper rungs by buying more zeros. This
          page is research documentation, not a claim of progress toward the
          Riemann Hypothesis.
        </p>
      </div>
    </section>
  );
}

function SigmaChainSection() {
  return (
    <section
      id="sigma-chain"
      aria-labelledby="sigma-chain-heading"
      className="scroll-mt-24 border-t border-slate-200/60 py-12 sm:py-16"
    >
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center gap-2">
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
            32 · The σ chain and the regional theorem · sandbox probes
          </span>
          <StatusBadge badge="sandbox" />
        </div>
        <h2
          id="sigma-chain-heading"
          className="mt-3 font-serif text-2xl font-semibold leading-tight text-slate-950 sm:text-3xl md:text-4xl"
        >
          The last cap becomes a derived chain — and seals as a theorem
          package
        </h2>
        <p className="mt-3 max-w-3xl border-l-2 border-sky-400/40 pl-3 text-[15px] leading-relaxed text-slate-600">
          <span className="font-medium text-sky-700/90">In plain words: </span>
          the σ-chain rounds (freeze rounds seventy-three through
          seventy-five, plus the next morning&apos;s package round) replace
          the program&apos;s last attractive cap by a <em>derived</em>,
          exact-rational certificate chain, lift it to class level, compress
          it into a sealed three-part theorem package with its own tiny
          independent checker — and measure the third level, the quantifier,
          to its endform. Everything in this chapter is sandbox: frozen
          preregistered probes in the experiments tree, no promotion, no
          marker moves — v911 was the newest promoted module at this
          chapter&apos;s freeze.
        </p>

        <div className="mt-6 max-w-3xl space-y-4 text-base leading-relaxed text-slate-700">
          <p>
            <strong className="font-medium text-amber-800">
              The σ identity, and the chain (Level 1):
            </strong>{" "}
            the wall&apos;s decisive ratio is exactly its own Schur quotient,{" "}
            <span className="font-mono text-emerald-700">σ = 1 − s/n</span>{" "}
            (warded at 3.8×10⁻¹⁵) — so <em>any</em> cap on σ is the open half
            restated, mechanism-importing. The preceding round&apos;s
            attractive σ ≤ 0.665 closure is dismantled <em>by provenance</em>:
            its constant is the probe&apos;s own margin convention, and its
            numerical match with a measure-side 0.665 is a{" "}
            <em>proven coincidence</em> — two 0.665s with disjoint
            provenances. The cap is replaced by a derived per-cell chain
            (n &gt; 0 ∧ certified ordered co-block floors ∧ Gauss–Radau
            moment bound, every inequality exact-rational): σ ≤ 0.727, hence
            M ≻ 0, on <strong className="font-medium text-slate-900">151/151
            built wall-legal cells plus 59/59 deep steps</strong> to h = 6344
            (worst margin 0.2124) — the first wall-positivity chain with{" "}
            <em>no member in the cancellation currency</em>: the margins are
            O(1), not 10⁻⁴-grade near-cancellations, and every relocation
            screen passes flat.
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The class theorem, sealed (Level 2):
            </strong>{" "}
            the <em>joint</em> Radau relation lifts definiteness from the
            cells to the class of all data sharing the certified floors —
            inf λ₁ = +0.008 over the entire class, against −574 admitted
            without the relation. The optimization is then compressed into a
            machine-verifiable <em>SOS proof object</em>: 1111 exact rational
            sum-of-squares certificates (closed-form Markov–Lukács Grams,
            PSD by structure, zero numerical error), census 151/151 at
            η = 0.273. And the morning&apos;s round seals it as a{" "}
            <strong className="font-medium text-slate-900">three-part
            theorem package</strong>: a purely symbolic relation certificate
            (no numeric input anywhere), the positivity certificate
            re-verified digit-identically against the stored proof object,
            and an honestly typed coverage certificate — full coverage of
            the 151 built cell regions with explicit rational moment
            neighborhoods, with the class box, the h &gt; 1450 flank and the
            all-h quantifier explicitly <em>not</em> covered. The audit
            entry point is a 202-line stdlib-only checker (imports exactly
            json / sys / hashlib / fractions / itertools, AST-gated) that
            re-proves the whole theorem in two seconds — and it has teeth:
            all three doctored packages die at exactly the named barrier.
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The endform of the quantifier (Level 3):
            </strong>{" "}
            the legality frontier is the quantifier&apos;s likely final
            address. h = 8003 turned out to be a hole, not a wall — the
            legal sub-ladder extends to{" "}
            <span className="font-mono text-emerald-700">h = 8204</span> —
            but every built cell beyond is negative: the frozen enum returns,
            for the first time, a measured <em>termination signal</em> of
            the built horizon, with the sign living in the{" "}
            <em>seat-to-bulk coupling</em> over a stably positive arch
            baseline (and the seat itself migrating). The smooth, prime-free
            world is illegal at −10⁴ against ±10⁻¹⁰ of truth: frontier
            legality is a prime effect. Behind the frontier, the deep rate:
            the one-atom shape limit is exact (moment-shape collapse at
            R² 0.9999, the atom identity literal), but the collapse is
            measured <em>unfinished</em> — its driver is a cancellation of
            giants (median factor 10⁵), and the direct reading closes
            razor-thin at{" "}
            <span className="font-mono text-emerald-700">+0.0104</span>,
            typed as an <em>irreducible measurement</em> that no certified
            constant can move. Of the three named missing bounds, B3 is now{" "}
            <em>Lipschitz-certified</em> (a 400-bit interval proof object),
            B2 <em>proved-conditional</em> (the deficit growth is
            self-limiting against an h-stationary cap), and B1 is reduced to
            one measured scalar t &gt; 4/5 — whose carrier is, once again,
            the arithmetic AR–OSC cancellation.
          </p>
          <p>
            <strong className="font-medium text-rose-800">
              The closed no-gos:
            </strong>{" "}
            the Pick / one-bad-atom compression is DEAD (a symbolically
            exact 2ε/y² high-pole blindness lemma — permanent); the
            finite-gap reference route is ILLDEFINED (the wall&apos;s
            spectral gap set is scattered, not banded — the class object
            does not exist for it); and the morning&apos;s fast kill test
            closes the multiplicative shell architecture, JCONTRACT-DEAD:
            0/27 shells are J-contractive, all 162 truth points non-PSD,
            and the full shell grouping produces no new positive defect
            structure — the elementary route closed early and cheap, before
            any large program was built on it.
          </p>
        </div>

        <p className="mt-6 max-w-3xl text-sm leading-relaxed text-slate-600">
          Honest fence, and the closing map in its frozen form: the finite
          theory is complete and machine-verified; the class theorem is a
          machine-verifiable proof object; <em>the quantifier is RH</em> —
          whose content now has one name in every coordinate system tested,
          the arithmetic coupling — and whose next honest move is a
          construction question, the cofinal corridor (the window
          family&apos;s deep extension, cofinal in the mesh-refinement
          order the extraction chain needs), not another bound. What
          stands is a regional finite positivity theorem plus a single
          open cofinal construction problem — not almost-RH. All of it is sandbox: no
          claim moves until it is promoted, and nothing here is a claim of
          progress toward the Riemann Hypothesis.
        </p>
      </div>
    </section>
  );
}

function KillAtlasSection() {
  return (
    <section
      id="kill-atlas"
      aria-labelledby="kill-atlas-heading"
      className="scroll-mt-24 border-t border-slate-200/60 py-12 sm:py-16"
    >
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center gap-2">
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
            33 · The kill atlas and the Obstruction Completeness Theorem ·
            sandbox probes
          </span>
          <StatusBadge badge="sandbox" />
        </div>
        <h2
          id="kill-atlas-heading"
          className="mt-3 font-serif text-2xl font-semibold leading-tight text-slate-950 sm:text-3xl md:text-4xl"
        >
          The whole campaign becomes one falsifiable object — and one named
          endpoint
        </h2>
        <p className="mt-3 max-w-3xl border-l-2 border-sky-400/40 pl-3 text-[15px] leading-relaxed text-slate-600">
          <span className="font-medium text-sky-700/90">In plain words: </span>
          four consolidation rounds (discovery freeze rounds seventy-nine
          through eighty-two, 2026-08-14) audit the entire RH campaign into
          one machine-refutable map, adjudicate every remaining candidate
          sign source, and consolidate the endpoint as a named,
          finite-rung theorem about the <em>obstruction</em> — not about
          RH. Everything in this chapter is sandbox: four frozen probes in
          the experiments tree, no promotion, no marker moves — v913 was
          the newest promoted module at the freeze; the suite stood at 906
          (954 today, after the v914/v915 promotion of chapters 37–39, the v916/v917 Epstein detection-arc promotion of 2026-08-16, the v918–v921 prime-front theorem-arc promotion of 2026-08-18, the v922–v925 spectral-balance/edge arc and v926–v930 endgame-arc promotions of 2026-08-19, the v931–v935 triple-cofinal-arc and v936–v941 post-bughunt-arc promotions of 2026-08-20, the v942–v948 mechanism-arc promotion of 2026-08-21, the v949–v954 Bughunt-X-arc promotion of 2026-08-22, the v955/v956 integrable-dictionary-arc promotion of 2026-08-24, the v958 bordered-dictionary-arc and v959 coupled-tau-terminal-arc promotions of 2026-08-24/25, and the v960/v961 wave-4 surface-closure/orientation promotions of 2026-08-25).
        </p>

        <div className="mt-6 max-w-3xl space-y-4 text-base leading-relaxed text-slate-700">
          <p>
            <strong className="font-medium text-amber-800">
              The map as one object (round 79, 43/43):
            </strong>{" "}
            the RH implication chain is reconstructed explicitly as an
            11-node, 10-edge DAG with{" "}
            <strong className="font-medium text-slate-900">
              exactly one open edge, E4
            </strong>{" "}
            — positivity at every rung of one sign-independently
            predeclared family, cofinal in the mesh-refinement order — and
            the honest non-proven list carries the four classical
            citations as an executable gate, not prose. The 50-route kill
            atlas assigns every killed route of the campaign to exactly
            one edge (17 on E4, 21 on the finite scalar edge, 8 past the
            wall, 2 off-chain), every verdict token grep-verified inside
            its own artifact. Six coordinate systems — τ &gt; 0, n − q &gt;
            0, σ &lt; 1, the anti-cancellation scalar, the P_err budget,
            v913&apos;s (L) — are pinned as <em>one and the same edge</em>:
            twenty notes of localization work sharpened the edge&apos;s
            type and closed the second open edge, but{" "}
            <em>did not move it</em>.
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The external proposal is coordinate system #7 (round 80,
              35/35, SAT-DISGUISE):
            </strong>{" "}
            the reviewer-proposed &quot;signed projection alignment&quot;
            closure of E4 is exact algebra — verified with{" "}
            <em>zero residual in exact fractions</em> — and empty: the
            projection is the identity, so the alignment-looking term
            vanishes identically, the ellipse inequality is s ≥ 0
            verbatim, and the &quot;optimal signed profile&quot; is
            B-independent, carrying zero arithmetic. The θ-average is the
            already-priced mean route; the proposed selection rule is
            exactly the sign-mined index whose non-noninterference is
            kernel-checked in Lean; and the small-rank premise is refuted
            by measurement (stable rank grows 110 → 1595). As candidate
            #19 it fails the frozen gate: it separates without
            independently orienting — its readout <em>is</em> the wall
            scalar.
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The candidate map completes (round 81, 33/33):
            </strong>{" "}
            the five formerly untested classes all fail with exact killing
            numbers — the Euler/G2 weight law separates but does not
            orient; every Krein contractor certificate is the wall sign
            renamed (margin exactly s/n); the named unconditional
            ordinate-position types are empty, with the required ordinate
            precision priced at{" "}
            <strong className="font-medium text-slate-900">
              ~1% of the mean zero spacing
            </strong>{" "}
            on the 2×10⁷-ordinate certified cache; the minimal alignment
            statement MIN-U2 is <em>beyond-classical</em> (restricted to
            the deployed windows it already excludes off-line zeros below
            every classical zero-free width); and every enumerated global
            source-profile inequality dies on the downward-closure lemma.
            Final tally:{" "}
            <strong className="font-medium text-slate-900">
              24 candidate sign sources, 0 pass, 19 fail, no
              blanket-untested class left.
            </strong>{" "}
            (Completeness over the corpus vocabulary — the round-108 audit,
            chapter 39, names five classes outside it, unpriced:
            ergodic/measure-rigidity transfer, o-minimal counting,
            bigger-group representation positivity,
            GMC/Fyodorov–Hiary–Keating, and higher-order Fourier
            uniformity of Möbius.)
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The bird&apos;s-eye round (round 82, 35/35):
            </strong>{" "}
            the three degrees of freedom every route held fixed are
            adjudicated. <em>Shape:</em> five structurally different
            admissible window families decay far shallower than the
            deployed one (exponents −0.46…−1.09 against −3.379) — the
            maneuver exists but buys nothing: single-window ladders fail
            the density leg, mesh-dense families inherit the saturation by
            an exact Schur bound, and the localization is shape-invariant
            (square shapes push the whole unconditional content into
            off-line exclusion below classical widths, 5/5
            beyond-classical). The hardness is RH&apos;s, not the
            program&apos;s. <em>Direction:</em> the existence route closes
            permanently at the border-membership step in exact fractions —
            a positive extension always exists, and &quot;the arithmetic
            one is it&quot; is the open edge verbatim.{" "}
            <em>Bootstrap:</em> still dead — T_req ~ h^4.77, the
            cache&apos;s τ-coverage ends at h ≈ 36, and height, not
            precision, is the deficit.
          </p>
          <p>
            <strong className="font-medium text-emerald-800">
              The Obstruction Completeness Theorem:
            </strong>{" "}
            (i) the DAG has exactly one open edge; (ii) the candidate map
            is complete and fully adjudicated; (iii) the missing input is
            exactly characterized — signed, alignment-carrying,
            unconditional, sub-spacing (~1%), minimal form MIN-U2
            beyond-classical; (iv) the characterization is
            shape-independent — with the existence direction closed and
            the bootstrap dead. Finite-rung; atlas completeness is
            editorial completeness over the named routes, typed as such;
            the counter-evidence is carried unsmoothed (NO-WITNESS stands:
            all certified reads positive to h = 12632, deepest
            2.796×10⁻¹⁵, decay flattening).
          </p>
        </div>

        <p className="mt-6 max-w-3xl text-sm leading-relaxed text-slate-600">
          Honest fence: this theorem turns &quot;why does RH not fall to
          this program?&quot; into a machine-checked statement with an
          exact domain of validity. It says nothing about the truth,
          provability or falsity of the Riemann Hypothesis and is not
          evidence in either direction — a no-go about the <em>type</em> of
          the missing input is not evidence about its <em>existence</em>,
          and it is emphatically not a statement that RH is unprovable.
          All of it is sandbox: no claim moves until it is promoted, and
          nothing here is a claim of progress toward the Riemann
          Hypothesis.
        </p>
      </div>
    </section>
  );
}

function RealRootSignposSection() {
  return (
    <section
      id="realroot-signpos"
      aria-labelledby="realroot-signpos-heading"
      className="scroll-mt-24 border-t border-slate-200/60 py-12 sm:py-16"
    >
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center gap-2">
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
            34 · The real-root architecture, the Parity Lemma, and the
            sign-position predictor · sandbox probes
          </span>
          <StatusBadge badge="sandbox" />
        </div>
        <h2
          id="realroot-signpos-heading"
          className="mt-3 font-serif text-2xl font-semibold leading-tight text-slate-950 sm:text-3xl md:text-4xl"
        >
          The missing object gets its most concrete form yet — and stays
          exactly as open
        </h2>
        <p className="mt-3 max-w-3xl border-l-2 border-sky-400/40 pl-3 text-[15px] leading-relaxed text-slate-600">
          <span className="font-medium text-sky-700/90">In plain words: </span>
          six discovery freeze rounds (rounds eighty-three through
          eighty-eight, 2026-08-14) attack the one direction the
          Obstruction Completeness Theorem leaves untyped —{" "}
          <em>constructing</em> the missing object rather than bounding it.
          Everything in this chapter is sandbox: ten frozen probes in the
          experiments tree, no promotion, no marker moves — the suite stays
          at 906. One convention: an adversarial bughunt round corrected
          three MAJOR misstatements in the round-83/84 records; the frozen
          probes and notes are not retro-edited — the correction is the
          record — and this chapter carries only the corrected numbers.
        </p>

        <div className="mt-6 max-w-3xl space-y-4 text-base leading-relaxed text-slate-700">
          <p>
            <strong className="font-medium text-amber-800">
              The real-root architecture (round 83, three lanes: 16/16 +
              4/4 + 20/20):
            </strong>{" "}
            the first route of the campaign to genuinely leave the kill
            atlas — source-only <em>self-adjoint</em> operators, real
            spectra by construction, no wall positivity, no zero data
            consumed, the limit identified via the trace formula. Lane one
            reads the census fully real (41/41 at x = 13) with all six
            trace rows converging, at the honest price that the minimizer
            exists only at internal precision ~e^(−4πx). The corrected
            zero-tracking read is <em>stronger</em> than first recorded:
            first-zero deviation −8.4×10⁻¹⁶ at x = 8 and 13 (exactly the
            cache&apos;s own float64 quantization of γ₁), mean displacement
            0.0 at float64 resolution. Lane two proves the structural
            point:{" "}
            <strong className="font-medium text-slate-900">
              the surviving convergence statement alone implies Weil
              positivity
            </strong>{" "}
            — full RH strength. Lane three <em>proves</em> a Nyquist
            density obstruction for its mesh family (constant density ℓ/2π
            against Ξ&apos;s log density — a constant cannot equal a
            non-constant). Three lanes, one recorded conflict, frozen for
            an arbiter.
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The arbiter (round 84, 17/17, REALROOT-DEPTH-UNDECIDED):
            </strong>{" "}
            the conflict resolves <em>by mechanism</em> — different
            operator families, not different sums, not a bug. A new deep
            rung x = 21 (λ_min = 1.25×10⁻⁹³): the mesh family&apos;s band
            count grows with the uniform Nyquist density while the
            extremal family stays <em>exactly</em> on the Ξ census —
            (0,30) = 3, (0,60) = 13, (0,100) = 29 — with all 50 excess
            zeros exiled to the band edge. But the{" "}
            <strong className="font-medium text-slate-900">
              Z1-transfer identity
            </strong>{" "}
            names the catch: the Galerkin matrix <em>is</em> the Gram
            matrix of zero evaluations — source-only in input,
            zero-measure in content. No finite rung can verify the
            architecture, only falsify it; the surviving lemma carries
            full RH strength.
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The TPL round (round 85, three lanes: 7/7 + 32/32 + 9/9):
            </strong>{" "}
            energy sign and zero census are locally independent
            observables (off-line quartets flip λ_min without moving the
            count — Rouché); the ARCH block <em>is</em> the smooth zero
            density exactly, so the entire positivity is supplied by the
            prime block alone;{" "}
            <strong className="font-medium text-slate-900">
              the Parity Lemma
            </strong>
            : the persistence statement is — with no analysis — a finite
            combinatorial statement about the sign pattern of one explicit
            matrix&apos;s ground eigenvector, and the <em>number</em> of
            sign changes is forced by a counting law (one fixed factor
            e^(−11) per forced skip, constant over 23 decades) — only the{" "}
            <em>positions</em> remain open, from the prime block alone.
            Simultaneously the devil&apos;s advocate convicts the
            route&apos;s measured support as circular: the recorded counts
            are the smooth Riemann–von Mangoldt values to &lt; 1, the
            instrument transcribes any fed measure (including a prime-free
            world), and outrunning classical verification would need
            dps ~ 2×10¹².
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The simplicity round (round 86, 22/22) and the bughunt
              (round 87, 24/24):
            </strong>{" "}
            the one principle that threads everything is{" "}
            <strong className="font-medium text-slate-900">
              Gram transcription
            </strong>{" "}
            — TFPT&apos;s positivity is always Gram positivity of node
            evaluations, a theorem exactly where the nodes are compiler
            data; the arithmetic seam is the single place whose nodes are
            not. One-axiom and fixed-point readings refuted against
            pre-registered bars; the order split (position first-order,
            reality second-order) mechanically explains why all 24
            candidate sign sources died. Tested simplicity adds nothing
            beyond the OCT — it explains why the OCT looks as it does. The
            bughunt: nine findings (3 MAJOR / 6 MINOR / 0 FATAL), no
            verdict flips, the honest zero-tracking claim <em>stronger</em>{" "}
            than published, and nine hardcoded pass-gates convicted across
            the corpus — an N/N tally is not, by itself, evidence that N
            things were tested.
          </p>
          <p>
            <strong className="font-medium text-emerald-800">
              The sign-position round (round 88, 19/19,
              SIGNPOS-PREDICTOR-EXACT):
            </strong>{" "}
            a source-only predictor of the sign-change positions — the
            parity of a rounded band-limited prime phase at the Nyquist
            lattice — is{" "}
            <strong className="font-medium text-slate-900">
              exact at all 79 reachable lattice points
            </strong>{" "}
            (x = 3/5/8/13), with arithmetic load exactly 4: the density
            alone fails at exactly four points and the prime-node comb
            repairs precisely those four; a scramble control fails 6/11.
            The catch, named precisely: exactness for all x is
            half-integer rounding-margin control of one explicit
            band-limited function of the primes (measured minimum margin
            0.0317) — verbatim the same RH-hard seat, relocated for the
            third time. Gantmacher–Krein is structurally dead, the
            position map is rigid, the positions are K-stable in the
            deployed band.
          </p>
        </div>

        <p className="mt-6 max-w-3xl text-sm leading-relaxed text-slate-600">
          Honest fence: the wall route is closed as a theorem (chapter 33);
          the only escape architecture is adjudicated DEPTH-UNDECIDED with
          its measured support convicted circular; and the missing object
          now has its most concrete form ever — eigenvector sign-change
          positions, equivalently rounding margins of a band-limited prime
          function — carrying full RH strength in every coordinate system.
          The predictor is a finite measurement, not an all-x statement.
          RH is neither proven nor disproven here; what is documented is
          the complete map of why. All of it is sandbox: no claim moves
          until it is promoted, and nothing here is a claim of progress
          toward the Riemann Hypothesis.{" "}
          <strong className="font-medium text-amber-800/90">
            Correction of record (round 97, 2026-08-15, chapter 37):
          </strong>{" "}
          the predictor&apos;s exactness holds at x ≤ 13 only — its
          operative extension is measured false from x = 21 onward (567
          τ-screened counterexamples to the cache edge x = 890; the
          round-88 exactness was a small-x accident of the margin budget,
          by an arithmetic-free mechanism). TPL(i) itself is untouched:
          the eigenvector truth side is unmeasured beyond x = 13, and the
          finite claim as published (exact at 79 points, x ≤ 13) remains
          factually true.
        </p>
      </div>
    </section>
  );
}

function SvpinKreinSection() {
  return (
    <section
      id="svpin-krein"
      aria-labelledby="svpin-krein-heading"
      className="scroll-mt-24 border-t border-slate-200/60 py-12 sm:py-16"
    >
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center gap-2">
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
            35 · The Stieltjes–Vitali pin route and the Krein screw-function
            carrier · sandbox probes
          </span>
          <StatusBadge badge="sandbox" />
        </div>
        <h2
          id="svpin-krein-heading"
          className="mt-3 font-serif text-2xl font-semibold leading-tight text-slate-950 sm:text-3xl md:text-4xl"
        >
          Countable pins, a carrier that sees the primes — and the same
          single input at the bottom
        </h2>
        <p className="mt-3 max-w-3xl border-l-2 border-sky-400/40 pl-3 text-[15px] leading-relaxed text-slate-600">
          <span className="font-medium text-sky-700/90">In plain words: </span>
          two closing discovery freeze rounds (rounds eighty-nine and
          ninety, 2026-08-14) take the <em>resolvent</em> direction to its
          endpoint: an externally proposed reduction of the whole trace
          problem to countably many safe scalars, and the construction of
          the one carrier the corpus did not have. Everything in this
          chapter is sandbox: two frozen probes in the experiments tree,
          no promotion, no marker moves — the suite stood at 906 at the freeze (954 today). No RH
          claim in any direction.
        </p>

        <div className="mt-6 max-w-3xl space-y-4 text-base leading-relaxed text-slate-700">
          <p>
            <strong className="font-medium text-amber-800">
              The Stieltjes–Vitali pin route (round 89, externally
              proposed, 17/17, SVPIN-ROUTE-OPEN):
            </strong>{" "}
            replace the full semilocal trace convergence by countably many
            positive resolvent scalars in the absolutely convergent Euler
            half-plane — then Herglotz compactness (one pin suffices),
            Vitali on the pins accumulating at the interior point i, the
            identity theorem, and the pole contradiction give (SV) ⟹ RH.
            The skeleton is{" "}
            <strong className="font-medium text-slate-900">
              sound gate by gate
            </strong>{" "}
            (the one named condition is the CF realness hypothesis) — and
            the named non-gap is stated as bluntly as the probe states it:
            the chain moves the <em>entire</em> burden into (SV) itself.
            The finite pre-check converges on all 16 frozen σ values
            (measured drop 2.6 against the a-priori Riemann–von Mangoldt
            model 2.4); the mesh-CF control is{" "}
            <em>poisoned through the same pins</em> (overshoot growing
            like log x — the wrong limit, measured); all four world
            controls separate; and the τ-screen shows 0/16 relocations —
            no disguise.
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The honest weight (round 89, Z1-typed):
            </strong>{" "}
            on the extremal family the measured pin convergence{" "}
            <em>is</em> the transcription of cache partial sums (rel
            ~10⁻¹²) — instrument consistency, never source-side content —
            and the naive Suzuki spectral readout is dead (a form-spectrum
            ladder, not the ordinates). The route is the{" "}
            <strong className="font-medium text-slate-900">
              second architecture of the campaign to survive every gate
            </strong>
            , and its reduction — countably many safe scalars in place of
            a test-class quantification — is the logically sharpest open
            target of the program. The priced remaining task was exactly
            one: the Krein inverse-spectral realization of Suzuki&apos;s
            screw function.
          </p>
          <p>
            <strong className="font-medium text-emerald-800">
              The Krein carrier (round 90, 22/22, SUZKREIN-CARRIER-OPEN):
            </strong>{" "}
            the priced ingredient, built. The screw function is extracted
            corpus-exactly (the normalization <em>derived</em>, not
            fitted; the classical Krein accelerant hypothesis{" "}
            <em>certified</em>, not assumed), the Levinson/Szegő solve{" "}
            <em>is</em> the discrete Gelfand–Levitan equation, and{" "}
            <strong className="font-medium text-slate-900">
              the realized Hamiltonian sees the primes
            </strong>
            : coefficient spikes at r = log q for q = 2, 3, 4, 5, 7
            (contrast 2.8–5.2). All 16 frozen σ rows converge truth-tight
            under a measured Weyl-disk contraction law R ~ e^(−(σ+1.36)L),
            and the disk center <em>resums the missing tail</em> (beating
            the truncated source sum by ×600 at σ = 0.6). It is{" "}
            <strong className="font-medium text-slate-900">
              the first pin carrier to pass the Z1 screen
            </strong>{" "}
            — no zero-cache transcription (minimum relative deviation
            8.5×10⁻³ against the bar 10⁻⁶) — and the controls die at the
            positivity level itself: the prime-free smooth accelerant{" "}
            <em>loses screw positivity</em> at finite window depth — the
            true primes are necessary for it.
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The repriced lemma, and its honest price:
            </strong>{" "}
            the literal trace-class norm of the pin contract is measured
            flat — the correct currency is Weyl-disk contraction — and the
            minimal missing lemma is stated exactly: uniform disk
            contraction of the Krein realization on σ ≥ 1/2 + ε,{" "}
            <em>given</em> positivity of every finite section of the
            accelerant. And that hypothesis{" "}
            <strong className="font-medium text-slate-900">
              is localized Weil positivity itself
            </strong>
            : the carrier localizes the remaining task (one contraction
            rate for one explicit canonical system) and replaces the wrong
            currency by the right one — it does not remove the input.
          </p>
        </div>

        <p className="mt-6 max-w-3xl text-sm leading-relaxed text-slate-600">
          Honest fence: the day&apos;s arc is complete — the wall route
          closed as a theorem (chapter 33), the real-root architecture
          adjudicated with its support convicted circular (chapter 34),
          the pin route as the sharpest reduction, and the Krein carrier
          as the first non-transcribing host — and at the bottom of every
          route, machine-verified, sits the same single input: Weil
          positivity, in one currency or another. The two open lemmata are
          precisely stated (Weyl-disk contraction of one explicit
          canonical system — round 90 stated it with a σ ↓ 1/2 uniformity
          that round 92 showed not load-bearing; the adjective is retired
          of record with round 109, chapter 39 — and the sign-change
          positions of one explicit ground eigenvector). The carrier&apos;s convergence is a finite
          measurement of a lemma, not its proof. RH is neither proven nor
          disproven here. All of it is sandbox: no claim moves until it is
          promoted, and nothing here is a claim of progress toward the
          Riemann Hypothesis.
        </p>
      </div>
    </section>
  );
}

function CohomSpecSection() {
  return (
    <section
      id="cohomspec"
      aria-labelledby="cohomspec-heading"
      className="scroll-mt-24 border-t border-slate-200/60 py-12 sm:py-16"
    >
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center gap-2">
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
            36 · What any cohomology for Spec ℤ must supply · sandbox
            probes
          </span>
          <StatusBadge badge="sandbox" />
        </div>
        <h2
          id="cohomspec-heading"
          className="mt-3 font-serif text-2xl font-semibold leading-tight text-slate-950 sm:text-3xl md:text-4xl"
        >
          The cohomological specification sheet — the missing theorem,
          stated as a testable interface
        </h2>
        <p className="mt-3 max-w-3xl border-l-2 border-sky-400/40 pl-3 text-[15px] leading-relaxed text-slate-600">
          <span className="font-medium text-sky-700/90">In plain words: </span>
          three closing discovery freeze rounds (rounds ninety-one,
          ninety-two and the specification round, 2026-08-15) compile the
          campaign&apos;s machine-checked characterization of the one
          missing input into a requirements document aimed at the
          geometric programs — Deninger&apos;s conjectural cohomology for
          Spec ℤ and the Connes–Consani scaling site. Everything in this
          chapter is sandbox: four frozen probes in the experiments tree,
          no promotion, no marker moves — the suite stood at 906 at the freeze (954 today). No RH
          claim in any direction.
        </p>

        <div className="mt-6 max-w-3xl space-y-4 text-base leading-relaxed text-slate-700">
          <p>
            <strong className="font-medium text-amber-800">
              The patterns round (round 91, two honest negatives):
            </strong>{" "}
            the program&apos;s first magnetar giant-flare QPO bed is{" "}
            <strong className="font-medium text-slate-900">NULL</strong>{" "}
            (SGR 1806−20 and SGR 1900+14 against the geometric 3/2
            ladder: Fisher-joint p = 0.3584 under a 20000-draw null with
            a 17-base look-elsewhere battery), and the LEE-controlled
            scan for an unclaimed dimensionless observable is{" "}
            <strong className="font-medium text-slate-900">
              SCAN-UNDECIDABLE
            </strong>{" "}
            with the structural finding as the content: the compiler
            vocabulary is <em>saturated</em> at today&apos;s tolerances —
            even the positive controls have cheaper accidental hits than
            the corpus expressions — so new predictions provably cannot
            come from numeric scanning; they must be derived theory-side.
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The Verblunsky round (round 92, 23/23,
              VERBLUNSKY-NO-INVARIANT):
            </strong>{" "}
            the sought packet-wise invariance mechanism of the screw
            coordinate is cleanly killed — a complete prime packet is a
            high-rank <em>indefinite</em> Toeplitz update (displacement
            rank two), the induced coefficient step is prior-state
            dependent (×316), and the true packet stream itself exits the
            Schur disk after p = 2/3/5/7 and only re-enters through later
            packets: the rescue is collective, not local. What the round
            pins on the way is load-bearing for the sheet: the{" "}
            <strong className="font-medium text-slate-900">
              Euler–Pick criterion
            </strong>{" "}
            (RH ⟺ explicit Pick matrices built from ξ′/ξ(1/2+σ) at σ =
            1+1/r stay positive semidefinite for every N; the source-only
            falsification ladder reads λ_min = 4.59×10⁻² down to
            2.44×10⁻⁶² at N = 12, all positive) and the{" "}
            <strong className="font-medium text-slate-900">
              (AC) identity
            </strong>
            : Euler–Pick positivity <em>is</em> Weil positivity on
            exponential autocorrelations, by identity.
          </p>
          <p>
            <strong className="font-medium text-emerald-800">
              The specification sheet (cohomspec_probe.py, 20/20,
              COHOMSPEC-COMPILED):
            </strong>{" "}
            seven numbered properties any candidate &quot;Weil pairing
            with structural positivity&quot; must have, each grounded by
            grep ward or recomputation in its owning frozen artifact. It
            must produce the signed, alignment-carrying, unconditional,
            sub-spacing ordinate-position input of the one open edge; it
            must be shape-independent (deployed decay exponent −3.379,
            recomputed); it cannot be a magnitude, density or existence
            statement (Littlewood floor 214.7/1527.1; the existence
            direction closed at border membership, det M = s·det B exact);
            its Gram form on exponential autocorrelations{" "}
            <strong className="font-medium text-slate-900">
              must be the Euler–Pick matrices
            </strong>{" "}
            — a proposed cohomological trace formula can be tested against
            this interface today, at any finite N, by machine; its
            positivity must die on the control worlds exactly as measured
            (the prime-free world at window depth r = 0.264 by a support
            error, the weight-scrambled world at r = 0.744 — the pairing
            must consume the exact prime support and the exact log
            p/p^(m/2) weights); and it must not be the wall scalar
            renamed (the τ-screen that killed fifteen routes).
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The function-field precedent, mapped to where it breaks:
            </strong>{" "}
            in Weil&apos;s proof the pairing is the intersection pairing
            on the surface C × C, the positivity is the
            Castelnuovo–Severi/Hodge-index inequality, and Frobenius
            supplies the cycle. For Spec ℤ, verified against the current
            literature: Deninger&apos;s dynamical Lefschetz trace formula
            is now <em>proved</em> on the smooth-foliation side
            (Álvarez López–Kordyukov 2024) but no arithmetic dynamical
            system realizing Spec ℤ has been constructed; Connes–Consani
            have Riemann–Roch on the periodic orbits of the scaling site
            (2017) but not on its <em>square</em> — exactly the surface
            substitute whose Hodge-index inequality would be the
            structural positivity — while their semilocal/prolate line
            (2021–2023) supplies the archimedean-place positivity and
            reduces RH to an Euler-factor property, and the 2026 extremal
            construction leaves open precisely the convergence this
            corpus adjudicated REALROOT-DEPTH-UNDECIDED.
          </p>
        </div>

        <p className="mt-6 max-w-3xl text-sm leading-relaxed text-slate-600">
          Honest fence: the specification sheet is a requirements document
          derived from machine-checked no-gos. It proves nothing about
          Deninger&apos;s program or Connes–Consani, asserts no defect and
          no progress of either, and claims no progress on the Riemann
          Hypothesis in any direction. Whether any cohomological theory
          can meet the specification is open, and the standing
          counter-evidence (NO-WITNESS: all certified reads positive to
          h = 12632) travels with every property. What it adds is
          precision: a testable interface where there was an analogy. All
          of it is sandbox: no claim moves until it is promoted.
        </p>
      </div>
    </section>
  );
}

function ThreeLemmaFormsSection() {
  return (
    <section
      id="three-lemma-forms"
      aria-labelledby="three-lemma-forms-heading"
      className="scroll-mt-24 border-t border-slate-200/60 py-12 sm:py-16"
    >
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center gap-2">
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
            37 · The three lemma forms and the certified instruments ·
            sandbox probes
          </span>
          <StatusBadge badge="sandbox" />
        </div>
        <h2
          id="three-lemma-forms-heading"
          className="mt-3 font-serif text-2xl font-semibold leading-tight text-slate-950 sm:text-3xl md:text-4xl"
        >
          The instrument tier — three RH-sufficient lemma forms, two
          certified falsification instruments, and a correction of record
        </h2>
        <p className="mt-3 max-w-3xl border-l-2 border-sky-400/40 pl-3 text-[15px] leading-relaxed text-slate-600">
          <span className="font-medium text-sky-700/90">In plain words: </span>
          nine discovery freeze rounds (rounds ninety-three and
          ninety-five through one-hundred-two, 2026-08-15, several as
          concurrent lanes) finish the campaign&apos;s instrument tier
          and, in one case, correct its own published record. Everything
          in this chapter was frozen as sandbox: eight frozen probes plus
          a Lean formalization round in the experiments tree, no promotion
          at the freeze, no marker moves — the suite stood at 906 at the
          freeze. Promotion of record (2026-08-15): the certified
          Euler–Pick floors of rounds 95 and 100 have since been promoted
          into the load-bearing suite as v915_eulerpick_certified_floors.py
          (the N ≤ 3 floors and all cited-bound wards recomputed at every
          suite run, the cap-10¹³ N = 4 intervals pinned from the
          run-of-record with the split disclosed, and the chapter-39 reach
          cap typed in verbatim); the suite stands at 954 (after the later v916/v917 Epstein detection-arc, v918–v921 theorem-arc, v922–v925 spectral-balance/edge arc, v926–v930 endgame-arc, v931–v935 triple-cofinal-arc, v936–v941 post-bughunt-arc, v942–v948 mechanism-arc, v949–v954 Bughunt-X-arc, v955/v956 integrable-dictionary-arc, v958/v959 bordered- and coupled-tau-arc, and v960/v961 wave-4 promotions). Everything else
          in this chapter remains sandbox. No RH claim in any direction.
        </p>

        <div className="mt-6 max-w-3xl space-y-4 text-base leading-relaxed text-slate-700">
          <p>
            <strong className="font-medium text-amber-800">
              The correction of record (round 97, 13/13,
              SP-OPERATIVE-FALSIFIED):
            </strong>{" "}
            the round-88 sign-position predictor (chapter 34) was priced
            against the full classical exponential-sum arsenal — and the
            measurement overtook the pricing. Extending the census from
            79 points (x ≤ 13) to 18798 points (x ≤ 890, the cache edge)
            shows the <em>operative</em> form{" "}
            <strong className="font-medium text-slate-900">
              false from x = 21 onward, with 567 τ-screened
              counterexamples
            </strong>
            : the round-88 exactness was a small-x accident of the margin
            budget, by an arithmetic-free mechanism (the Fejér
            taper&apos;s tracking-variance floor, rms → 1/(2π) = 0.159,
            against the 0.5 budget — no taper in this family survives).
            The pricing itself: the best unconditional bound misses the
            budget by ×8.2, and even RH gives only 1.015 at the deepest
            rung; the prefix/exceptional-set salvage is dead in-window.
            The fence: what died is the deployed source-side approximant,
            not TPL(i) itself — the eigenvector truth side is unmeasured
            beyond x = 13, and the published finite claim remains
            factually true. Frozen probes and notes are not retro-edited;
            the correction is the record.
          </p>
          <p>
            <strong className="font-medium text-emerald-800">
              The two certified falsification instruments:
            </strong>{" "}
            the Euler–Pick ladder is rebuilt to certified standard (round
            95, 31/31: N ≤ 3 with outward-rounded interval floors, decay
            measured generic, detection law N* = 6.1 + 1.95·log₁₀(1/δ),
            γ-blind beyond γ ≈ 50) and then extended (round 100, 22/22):{" "}
            <strong className="font-medium text-slate-900">
              λ_min(𝒫₄) ∈ [8.28×10⁻¹⁵, 1.38×10⁻¹⁴] certified positive at
              sieve cap 10¹³
            </strong>
            , with π(10¹³) = 346,065,536,839 reproduced exactly as the
            hard external ward, Nair&apos;s ψ(x) ≥ (x−2)·ln 2 unblocking
            the a-priori certificate, and the knowledge wall corrected to
            N = 5 — beyond the verified-zeros range, no sieve of any size
            helps. These four certified floors are now load-bearing:
            v915_eulerpick_certified_floors.py recomputes the N ≤ 3 floors
            and every cited-bound ward at each suite run and pins the
            cap-10¹³ N = 4 intervals from the run-of-record, with the
            recompute/pin split disclosed in the module and the ledger
            row. And the Hausdorff safe-point round (round 102, 40/40)
            builds{" "}
            <strong className="font-medium text-slate-900">
              the cheapest certified RH-consequence instrument in the
              corpus
            </strong>
            : the equivalence skeleton sound, certified depth 86 (5290
            cells) with γ*-reach 189 at a = 256 and 563 on the a = 1024
            arm — versus Euler–Pick&apos;s certified N = 3 at γ ~ 5–8 —
            replicated across three source-only carriers with no zero
            cache anywhere in construction. The detector is honestly
            priced: ~1/δ reach below γ₁, provably blind above — made
            concrete by a located Epstein witness zero (ρ ≈ 0.697 +
            36.374i, RH-for-Q provably false, the Q Pascal field
            positive to depth 100 exactly as the phase model predicts;
            correction of record, round 123 / v916: that zero was never
            γ-minimal — the located off-line census of ξ_Q holds four
            pairs below 45, and the γ-minimal driver 0.9330+15.6682i
            carries 26× its excess).
            Honestly NOT-WORLD-NEW: Zhang (arXiv:2303.09396) has the
            identical criterion at the central point; the novelty is the
            safe-point shift, the source-only decoder, and the certified
            conditioning. Both channels are open and empty — a single
            certified negative would be an RH-disproof candidate — with the
            round-108 reach cap (chapter 39): both instruments are
            disproof-sound but reach-capped far below Platt–Trudgian&apos;s
            3.0×10¹² (Euler–Pick sees off-line zeros only at γ ≈ 5–8; the
            Hausdorff field is provably blind above γ₁ = 14.13), so
            &quot;open and empty&quot; is a theorem given the cited inputs,
            not live falsification power.
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The interface and the kernel (rounds 98 and 99):
            </strong>{" "}
            the one external published RH reduction —
            Connes–Consani–Moscovici&apos;s P(n) property — is
            adjudicated: its published local terms reproduce the corpus
            Euler–Pick matrices{" "}
            <strong className="font-medium text-slate-900">
              entrywise
            </strong>{" "}
            (ξ′/ξ to rel 2.3×10⁻⁵⁰), all six prime-bearing Galerkin
            sections are positive (a new finite instrument; a certified
            negative would have refuted RH), and the honest comparison is
            an identity: P(n) <em>is</em> localized Weil positivity in
            the corpus&apos;s measured currency — so any semilocal
            prolate candidate is finitely testable against this interface
            today. And 27 theorems of the reduction chain are now
            kernel-checked in Lean 4 (axioms exactly
            propext/Classical.choice/Quot.sound): the Euler–Pick forward
            PSD direction at the SV nodes for every N, the δ₁ no-go, the
            full Parity Lemma under one named simplicity hypothesis, and
            the SV skeleton with its honesty lock
            skeleton_not_unconditional — an instance with RH = False,
            showing the packaging alone yields nothing.
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The mechanism rounds (93, 96, 101):
            </strong>{" "}
            round 92&apos;s exit/re-entry is fully explained as support
            bookkeeping (COLLECTIVE-IS-SUPPORT: an exact causal onset
            bound plus ~2 measured lags; the completed stream&apos;s
            max|α| constant at 0.184; mass-without-atoms dies at the
            identical lag — in-window survival requires the exact
            arithmetic weights). The rigidity round answers the inverse
            problem: screw positivity to depth r pins the measure onto
            the prime comb exponentially tightly —{" "}
            <strong className="font-medium text-slate-900">
              all 17 adversarial impostors die
            </strong>
            , and the moduli law c_mod = 1.073 is conditioning-priced:
            rigidity is the conditioning cost up to an O(1) factor, not a
            new arithmetic-free law. The α-induction round sets a
            positivity depth record (r = 9.0, both meshes) with an exact
            kick law (deviation ≤ 2.8×10⁻¹⁶) and the finding that{" "}
            <strong className="font-medium text-slate-900">
              prime arrivals stabilize
            </strong>{" "}
            — the naive atoms-push-down picture is wrong; the wall
            relocates into the certificate, and the named open piece (a
            source-certified energy floor with κ₊ &lt; 1/2) <em>is</em>{" "}
            localized positivity.
          </p>
        </div>

        <p className="mt-6 max-w-3xl text-sm leading-relaxed text-slate-600">
          Honest fence (wording corrected of record by the round-108
          logic audit and the round-109 bughunt, chapter 39): the one
          open input now holds three RH-sufficient lemma forms —
          Weyl-disk contraction of one explicit canonical system
          (pointwise at the pins, per the round-92 correction; the stale
          adjective &quot;uniform&quot; is retired), the sign positions
          of one explicit ground eigenvector, and Hausdorff cell
          positivity of one explicit Pascal field. Of the three, the
          Hausdorff form is a proven RH-equivalence; the Weyl-disk and
          sign-position forms are one-sided pendants (their converses
          are the round-90 open lemma and the
          CF-realness/Connes-§6.6 hypotheses), every mutual equivalence
          routes through RH, transfer between forms is none, and
          certified regions are form-local. Around them: three agreeing
          source-only carriers, two certified falsification instruments,
          the rigidity law, and 27 kernel-checked theorems. At the
          bottom, unchanged: localized Weil positivity. The certified
          instruments are falsification channels, not evidence — their
          certified slices sit in territory classical zero verification
          closed long ago, and their blindness laws are measured and
          carried. RH is neither proven nor disproven; all of it is
          sandbox: no claim moves until it is promoted.
        </p>
      </div>
    </section>
  );
}

function RoadmapSection() {
  return (
    <section
      id="roadmap"
      aria-labelledby="roadmap-heading"
      className="scroll-mt-24 border-t border-slate-200/60 py-12 sm:py-16"
    >
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center gap-2">
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
            38 · The roadmap · sandbox probes
          </span>
          <StatusBadge badge="sandbox" />
        </div>
        <h2
          id="roadmap-heading"
          className="mt-3 font-serif text-2xl font-semibold leading-tight text-slate-950 sm:text-3xl md:text-4xl"
        >
          The road from here — a machine-gated path to a complete proof
        </h2>
        <p className="mt-3 max-w-3xl border-l-2 border-sky-400/40 pl-3 text-[15px] leading-relaxed text-slate-600">
          <span className="font-medium text-sky-700/90">In plain words: </span>
          three discovery freeze rounds (rounds one-hundred-three through
          one-hundred-five, 2026-08-15) compile the campaign&apos;s complete
          machine-checked map into the one artifact it never produced: a
          staged, milestone-gated research roadmap from today&apos;s frozen
          state to a complete RH proof, in which every stage is falsifiable
          against the corpus&apos;s own instruments. The fences come first:
          a roadmap is not progress on RH, no stage is claimed started, and
          the mathematics of Stages 1–2 does not yet exist. Everything here
          was frozen as sandbox — three frozen probes, no promotion at the
          freeze, no marker moves; the suite stood at 906 at the freeze.
          Promotion of record (2026-08-15): the round-103 Form-A theorem
          (extended by round 106, chapter 39) has since been promoted as
          v914_pascal_region_theorem.py, and the certified Euler–Pick
          floors it consumes as Stage-0/1b acceptance values as
          v915_eulerpick_certified_floors.py; the suite stands at 952. The
          roadmap itself remains sandbox.
        </p>

        <div className="mt-6 max-w-3xl space-y-4 text-base leading-relaxed text-slate-700">
          <p>
            <strong className="font-medium text-emerald-800">
              The two feeder rounds:
            </strong>{" "}
            the Form-A round (round 103, MOONSHOT-PARTIAL) proves, from
            cited inputs alone (Platt–Trudgian 2021 + Rosser 1941 + the
            classical γ₁ isolation — no zero table, no zeta evaluator),{" "}
            <strong className="font-medium text-slate-900">
              the largest positivity region of the campaign: C_(n,k)(256)
              &gt; 0 for every n ≥ 0 and every k ≤ 10¹⁹
            </strong>{" "}
            — ten quintillion complete k-columns, with the scope inside the
            theorem: it touches the k → ∞ quantifier nowhere and proves
            nothing about RH; its three suggested proof routes die with
            named mechanisms (the Laguerre sign obstruction on the prime
            side; pure-point Szegő entropy −∞; nonuniform asymptotic-a
            transport). The theorem is now load-bearing as
            v914_pascal_region_theorem.py, which recomputes the complete
            four-region partition at every suite run. The class round (round 104, 23/23,
            LEVINSON-ADJUDICATED) prices the last unexamined classical
            theorem type — positive proportion on the line
            (Selberg/Levinson/Conrey up to PRZZ&apos;s κ &gt; 0.417293) —
            as structurally useless at every published constant: a
            proportion theorem must come within 1 − κ* &lt; 4.8×10⁻³ of{" "}
            <em>all</em> zeros (κ*_ledger = 0.9952/0.9983/0.9988, lower
            bounds) before it can feed the wall.{" "}
            <strong className="font-medium text-slate-900">
              The atlas tally moves 24 → 25 candidates, 0 PASS
            </strong>{" "}
            — every named unconditional classical theorem type about zero
            positions is now formally priced.
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The roadmap (round 105, roadmap_probe.py, 29/29,
              ROADMAP-COMPILED):
            </strong>{" "}
            <strong className="font-medium text-slate-900">Stage 0</strong>{" "}
            (done, frozen): the atlas at 25/0, one open edge E4, the three
            lemma forms (each RH-sufficient; only the Hausdorff form a
            proven equivalence — the rounds-108/109 correction of record,
            chapter 39), two certified instruments with
            open-and-empty channels, the k ≤ 10¹⁹ theorem (re-derived
            inside the probe from the cited constants), the rigidity law,
            the specification sheet, 27 kernel theorems.{" "}
            <strong className="font-medium text-slate-900">Stage 1</strong>{" "}
            (open — new mathematics): structural positivity of Hodge-index
            type for Spec ℤ; the verified literature state: Deninger&apos;s
            trace formula is proved for smooth foliated flows
            (arXiv:2402.06671) but has no arithmetic host, and
            Connes–Consani have Riemann–Roch on the scaling site and for ℤ
            but not on its square. Milestone 1a — an arithmetic dynamical
            system hosting the proven trace formula — acceptance gate: it
            must reproduce the (AC)/Euler–Pick interface at the 16 frozen
            σ, checkable by machine in minutes. Milestone 1b — Riemann–Roch
            on the square of the scaling site — acceptance gate: the
            intersection pairing on exponential autocorrelations must
            reproduce the certified 𝒫_N ladder (N ≤ 4 frozen floors).{" "}
            <strong className="font-medium text-slate-900">Stage 2</strong>{" "}
            (open — new mathematics): the Hodge-index/Castelnuovo analog on
            the Stage-1 substrate; gates: fail the surrogates exactly at r
            = 0.264/0.744, be signed and alignment-carrying (v913 class),
            survive the τ-screen (bands 0.30/0.70), reproduce the certified
            Hausdorff cells (depth 86) and strictly extend the k ≤ 10¹⁹
            reach.{" "}
            <strong className="font-medium text-slate-900">Stage 3</strong>{" "}
            (conditional-complete — assembly the machine already holds):
            from the index inequality to localized Weil positivity in any
            one lemma form, then v848&apos;s extraction chain, v912&apos;s
            rate theorem, the Lean kernel tier (sv_implies_rh with its
            honesty lock), the SVPIN skeleton, the Hausdorff equivalence,
            and the CCM same-currency interface — with the round-108 fence
            (chapter 39): the only kernel-checked end-to-end extraction
            accepts only the wall form H_cof, which none of the three entry
            forms produces without RH; the per-form descents are
            probe-gated plus classical, and the weakest link is the
            Stage-2→3 interface itself — finite acceptance gates (cells
            n + k ≤ 86) against infinite-quantifier entry forms, a jump no
            corpus machinery bridges (v912 bridges convergence, not
            positivity).
          </p>
          <p>
            <strong className="font-medium text-amber-800">
              The falsification spine (parallel, permanent):
            </strong>{" "}
            the two certified instruments keep running as standing disproof
            channels — Euler–Pick N ≤ 4 and the Hausdorff field at depth 86,
            both open and empty; a single certified negative anywhere would
            be an RH-disproof candidate. The round-108 reach cap travels
            with the headline (chapter 39): both instruments are
            disproof-sound but reach-capped far below Platt–Trudgian&apos;s
            3.0×10¹² (γ ≈ 5–8 and γ₁ = 14.13 respectively), so &quot;open
            and empty&quot; is a theorem given the cited inputs, not an
            observation — the certified ranges carry zero live
            falsification power. The extension walls are knowledge
            walls, not compute walls: N = 5 needs ψ-knowledge beyond 10¹⁹
            (the floor exceeds λ₅ by 4.7×10⁵ at any sieve cap), and the
            Form-A n = 0 mechanism exhausts at k ≈ 1.405×10¹⁹ — relocated
            by round 106&apos;s stronger mechanism to k ≈ 7.44×10²¹
            (chapter 39).
          </p>
        </div>

        <p className="mt-6 max-w-3xl text-sm leading-relaxed text-slate-600">
          Honest fence: a roadmap is not progress on RH; no stage is claimed
          started; Stages 1–2 require mathematics that does not yet exist,
          and the corpus proves interfaces and obstructions, never
          existence. No timeline is promised. The roadmap&apos;s value is
          exactly that every step is falsifiable and interface-defined: any
          candidate, from anyone, anywhere, can be adjudicated against
          frozen machine gates in minutes. RH is neither proven nor
          disproven; all of it is sandbox — no claim moves until it is
          promoted.
        </p>
      </div>
    </section>
  );
}

function FrontierAuditsSection() {
  return (
    <section
      id="frontier-audits"
      aria-labelledby="frontier-audits-heading"
      className="scroll-mt-24 border-t border-slate-200/60 py-12 sm:py-16"
    >
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center gap-2">
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
            39 · The frontier extension, the code reading, and the audits ·
            sandbox probes
          </span>
          <StatusBadge badge="sandbox" />
        </div>
        <h2
          id="frontier-audits-heading"
          className="mt-3 font-serif text-2xl font-semibold leading-tight text-slate-950 sm:text-3xl md:text-4xl"
        >
          The campaign audited — the corrections of record, a 530× frontier
          extension, and the code reading vindicated
        </h2>
        <p className="mt-3 max-w-3xl border-l-2 border-sky-400/40 pl-3 text-[15px] leading-relaxed text-slate-600">
          <span className="font-medium text-sky-700/90">In plain words: </span>
          four discovery freeze rounds (rounds one-hundred-six through
          one-hundred-nine, 2026-08-15, concurrent lanes) extend the
          roadmap&apos;s frontier, adjudicate the program&apos;s founding
          intuition under its own name, and then audit the campaign&apos;s
          own headlines. This is first of all a corrections chapter: the
          round-108 logic audit and the round-109 bughunt (the first
          adversarial audit of rounds 86–105) independently convicted the
          published &quot;three equivalent lemma forms&quot; language and
          two related headlines; the corrected wordings are carried in
          chapters 37 and 38. No number was wrong, no verdict flips.
          Everything here was frozen as sandbox: four frozen probes, no
          promotion at the freeze, no marker moves — the suite stood at
          906 at the freeze. Promotion of record (2026-08-15): the
          round-106 frontier extension below — with the round-103 base
          theorem and the HSW attribution resolved from the paper itself
          (Cor. 1.2 is the N(t) bound used; Cor. 1.4 is the companion S(t)
          bound, not used) — has since been promoted as
          v914_pascal_region_theorem.py, and the certified Euler–Pick
          floors as v915_eulerpick_certified_floors.py; the suite stands
          at 914. The audits and the code reading remain sandbox. No RH
          claim in any direction.
        </p>

        <div className="mt-6 max-w-3xl space-y-4 text-base leading-relaxed text-slate-700">
          <p>
            <strong className="font-medium text-amber-800">
              The corrections of record (round 108,
              bigpicture_logic_probe.py, 31/31, BIGPICTURE-FINDINGS(3);
              round 109, bughunt2_r86_r105_probe.py, 30/30,
              BUGHUNT2-FINDINGS(7, max MAJOR): 1 MAJOR / 6 MINOR / 0
              FATAL):
            </strong>{" "}
            &quot;three equivalent lemma forms&quot; overstated the machine
            record. The honest table: the{" "}
            <strong className="font-medium text-slate-900">
              Hausdorff form is a genuine proven RH-equivalence
            </strong>{" "}
            (its continuation chain independently re-derived gap-free in
            round 109), while the Weyl-disk and sign-position forms are{" "}
            <strong className="font-medium text-slate-900">
              one-sided pendants
            </strong>{" "}
            — form ⇒ RH established, RH ⇒ form open (the round-90 lemma and
            the CF-realness/Connes-§6.6 hypotheses respectively). Every
            mutual equivalence that holds routes <em>through</em> RH — no
            direct form-to-form edge exists — and{" "}
            <strong className="font-medium text-slate-900">
              transfer is none
            </strong>
            , demonstrated by an explicit counterexample world: an off-line
            quadruple at γ = 20 keeps <em>every</em> Hausdorff cell
            positive (n + k ≤ 50) while the Euler–Pick section fires at
            N = 12 (certified negative pivot at 200 dps).{" "}
            <strong className="font-medium text-slate-900">
              Certified regions are form-local
            </strong>
            : the k ≤ 10¹⁹/7.4×10²¹ Form-A theorems imply nothing about
            screw sections or Weyl disks, and their zero-location content
            sits below γ₁ = 14.13, where Platt–Trudgian is infinitely
            stronger. Two further headlines gained fences (carried in
            chapter 38): Stage 3&apos;s &quot;conditional-complete&quot;
            (the kernel-checked extraction accepts only H_cof, which no
            entry form produces — the weakest link is the finite-gates
            versus infinite-quantifier interface itself) and the
            falsification spine (both instruments disproof-sound but
            reach-capped — &quot;open and empty&quot; is a theorem given
            the cited inputs). The audit also names the five classes the
            atlas leaves unpriced (ergodic/measure-rigidity transfer,
            o-minimal counting, bigger-group representation positivity,
            GMC/Fyodorov–Hiary–Keating, higher-order Fourier uniformity of
            Möbius — chapter 33&apos;s completeness is vocabulary-relative)
            and the minor fixes now carried on the surfaces: the stale
            &quot;uniform&quot; adjective in Form B&apos;s name (pointwise
            at the pins suffices, per round 92) and the screwind mesh
            ladder misattribution (0.207 was the δ = 0.008 value; the true
            δ = 0.012 sup is 0.2219; MESH-DAMPED stands). Against all
            that, the load-bearing re-derivations are clean: the round-103
            theorem re-proved end to end with an own implementation, the
            N = 4 certification re-derived, the Hausdorff continuation
            gap-free, the Lean theorems saying exactly what round 99
            claims, all 16 in-scope probes re-run green —{" "}
            <strong className="font-medium text-slate-900">
              no round verdict flips
            </strong>
            .
          </p>
          <p>
            <strong className="font-medium text-emerald-800">
              The frontier extension (round 106, moonshot_o3_probe.py,
              16/16, MOONSHOT3-EXTENDED):
            </strong>{" "}
            the round-103 theorem extends 530-fold —{" "}
            <strong className="font-medium text-slate-900">
              C_(n,k)(256) &gt; 0 for every n ≥ 0 and every k ≤
              7,444,682,106,464,286,365,865
            </strong>{" "}
            (≈ 7.44×10²¹), from Platt–Trudgian 2021 plus the{" "}
            <em>corrected</em> Hasanalizade–Shen–Wong zero-counting bound
            (JNT 235 (2022) Cor. 1.2 — the attribution flag resolved from
            the paper at promotion: Cor. 1.2 is the N(t) bound used,
            Cor. 1.4 the companion S(t) bound; the commissioned S(T)
            constants honestly replaced — their Cheng–Graham input was
            later identified as invalid). The theorem is now load-bearing
            as v914_pascal_region_theorem.py (the 33-cell frontier pinned
            from the run-of-record, a six-cell full-packet subsample
            including the worst cell recomputed at every suite run). The
            general law is derived:{" "}
            <strong className="font-medium text-slate-900">
              k_front(T) = λ·T²/(a − ½) with λ∞ = 0.226987
            </strong>{" "}
            — verification height buys quadratically many columns — and
            the frontier is mechanism-exact (the next 2×10⁻⁶ relative step
            fails). New exact structure travels with it: the two-variable
            generating function in closed form with a pole-divisor
            RH-<em>equivalence</em> (not a proof), total sign-regularity
            in the reversed-k orientation, the fixed-N
            eventual-positivity theorem — and two measured warnings:{" "}
            <strong className="font-medium text-slate-900">
              Hankel positivity alone is not Form A
            </strong>{" "}
            (the uniform measure on [2,3] has every Hankel matrix positive
            definite yet C_(0,1) = −3/2 — the localizers are load-bearing)
            and the downward transport is not sign-closed (eventual
            fixed-N positivity cannot be propagated down to a = 256).
          </p>
          <p>
            <strong className="font-medium text-emerald-800">
              The code reading vindicated (round 107,
              code_synthesis_probe.py, 18/18,
              CODE-READING-TRUE-DECODING-DIRECTION):
            </strong>{" "}
            the program&apos;s founding intuition — the primes as an
            error-correcting code — got its first formal adjudication
            under that name, and it is{" "}
            <strong className="font-medium text-slate-900">
              true as measured structure
            </strong>
            : the primes are the unique codeword of an error-correcting
            code in the compiler&apos;s own Gram grammar (minimum distance
            the round-96 rigidity law, re-measured independently to four
            digits; decoding radius the exact impostor exits; rate → 0) —
            the{" "}
            <strong className="font-medium text-slate-900">
              same grammar as the compiler&apos;s E8 code layer
            </strong>{" "}
            ([8,4,4] self-dual, rebuilt exactly in-probe), but a different
            dual type. The decisive number:{" "}
            <strong className="font-medium text-slate-900">
              the dual rank grows with slope 1.0000
            </strong>{" "}
            (the binding check index never stabilizes; a non-codeword
            passes every bounded-depth check family bit-exactly below its
            defect), and the adversarial local-testability gap → 0. The
            honest close: the code runs in the <em>decoding</em> direction
            (finite checks ⇒ identification) while RH needs the{" "}
            <em>encoding</em> direction (codeword ⇒ all checks) — the
            quantifier does not compress, and the reason is now a measured
            number.
          </p>
        </div>

        <p className="mt-6 max-w-3xl text-sm leading-relaxed text-slate-600">
          Honest fence: the corrections change no number and flip no
          verdict — they grade the record&apos;s own language against the
          machine state, per the standing correction-of-record convention
          (frozen probes and notes are not retro-edited; the correction is
          the record). The frontier theorem is a finite certificate from
          cited inputs and touches the k → ∞ quantifier nowhere; the code
          reading is structure, not progress. RH is neither proven nor
          disproven; all of it is sandbox — no claim moves until it is
          promoted.
        </p>
      </div>
    </section>
  );
}

function UnpricedResolventSection() {
  return (
    <section
      id="unpriced-resolvent"
      aria-labelledby="unpriced-resolvent-heading"
      className="scroll-mt-24 border-t border-slate-200/60 py-12 sm:py-16"
    >
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center gap-2">
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
            40 · The vocabulary boundary priced, and the resolvent closure ·
            sandbox probes
          </span>
          <StatusBadge badge="sandbox" />
        </div>
        <h2
          id="unpriced-resolvent-heading"
          className="mt-3 font-serif text-2xl font-semibold leading-tight text-slate-950 sm:text-3xl md:text-4xl"
        >
          The atlas at 30 candidates, 0 pass — and the CCM operator is the
          corpus&apos;s own record family
        </h2>
        <p className="mt-3 max-w-3xl border-l-2 border-sky-400/40 pl-3 text-[15px] leading-relaxed text-slate-600">
          <span className="font-medium text-sky-700/90">In plain words: </span>
          two discovery freeze rounds (rounds one-hundred-eleven and
          one-hundred-twelve, 2026-08-15, concurrent lanes) close the two
          flanks the audits left open: the five argument classes named as
          genuinely outside the atlas enumeration are all adjudicated and
          killed, and the constructive resolvent-closure architecture is
          built and adjudicated — with the striking identification that the
          operator of the new Connes–Consani–Moscovici paper
          (arXiv:2511.22755) is, mode for mode, an object this diary had
          already built and frozen as its round-89 record. Everything here
          is sandbox: two frozen probes, no promotion, no marker moves —
          the suite stood at 906 at these rounds&apos; freeze (954 today,
          after the v914/v915 and later promotions through v961). No RH claim in
          any direction.
        </p>

        <div className="mt-6 max-w-3xl space-y-4 text-base leading-relaxed text-slate-700">
          <p>
            <strong className="font-medium text-amber-800">
              The unpriced classes adjudicated (round 111,
              unpriced_classes_probe.py, 26/26, UNPRICED-ADJUDICATED —
              tally 25 → 30, 0 PASS):
            </strong>{" "}
            all five classes outside the original enumeration are priced
            and killed; none survives as an open lever. The headline is{" "}
            <strong className="font-medium text-slate-900">
              Zagier&apos;s published horocycle RH-equivalence
            </strong>{" "}
            (Zagier 1979/81; Sarnak 1981; Verjovsky 1994) — a published
            RH-equivalence never adjudicated until now: the instrument
            measures the deep-window error exponent at{" "}
            <strong className="font-medium text-slate-900">0.7451</strong>{" "}
            (the RH-range 3/4 in the classically verified region), and
            planted-zero synthetic worlds recover the exact affine law{" "}
            <strong className="font-medium text-slate-900">
              θ = 1 − Θ/2 to sup Re ρ
            </strong>{" "}
            (|dev| ≤ 0.0029) — the horocycle rate <em>is</em> the emptied
            zero-free/density currency, and the rigidity technology that
            would improve it is rate-free (Ratner) or non-horospherical
            (the 2023 effective results explicitly exclude the
            horospherical case, which the modular horocycle is; the
            classical spectral 1/2 has stood since 1981). The other four:
            o-minimal counting is{" "}
            <em>inapplicable by type</em> (ζ&apos;s zero set is infinite,
            o-minimal sets have finitely many components; Masser 2011
            counts rational points on the graph — count currency,
            position-free, unsigned); bigger-group representation
            positivity has its <em>host gap confirmed</em> (λ ≥ 1/4 with
            positive multiplicity forces the line — the Selberg-zeta
            precedent — but λ = 1/5 yields a real pair exactly, and at the
            arithmetic quotients the 1/4 gap is Selberg&apos;s own open
            conjecture, Kim–Sarnak deficit 49/4096 exact);
            GMC/Fyodorov–Hiary–Keating is <em>magnitude-law-only</em> (the
            randomized Euler product carries zero signed alignment
            observable — iid phases have zero signed expectation and a
            flip-invariant law); and higher-order Fourier uniformity is{" "}
            <em>cancellation-only and ineffective</em> (the entire content
            sits in Siegel–Walfisz-ineffective constants; the sharpest
            signed corollary of |X| ≤ env is X ≥ −env).{" "}
            <strong className="font-medium text-slate-900">
              The atlas stands at 30 candidates, 0 pass, with the
              vocabulary boundary itself now adjudicated — every named
              argument class inside and outside the original enumeration is
              formally priced.
            </strong>
          </p>
          <p>
            <strong className="font-medium text-emerald-800">
              The resolvent closure adjudicated (round 112,
              resolvent_closure_probe.py, 36/36, RESOLVENT-TRANSCRIPTION +
              CROSSCARRIER-BOUNDS + JENSEN-NO-DICTIONARY):
            </strong>{" "}
            the identification first —{" "}
            <strong className="font-medium text-slate-900">
              arXiv:2511.22755&apos;s operator (CCM&apos;s det_reg
              construction) is, mode for mode, the corpus&apos;s own
              round-89 record extremal family
            </strong>
            : kernel to 10⁻⁶⁸, spectrum equal to the record zeros (10/10,
            rel 2.7×10⁻⁸), their det_reg formula executable as a rank-one
            determinant identity to 10⁻⁷⁵ — the corpus had independently
            built CCM&apos;s operator before their paper. The
            groundspace-block variant{" "}
            <strong className="font-medium text-slate-900">
              eliminates CCM&apos;s simplicity and evenness hypotheses at
              construction level
            </strong>{" "}
            (basis-rotation-invariant to 1.5×10⁻¹⁶, stable where the
            simple selection swings O(1); the exterior-determinant
            identity to 5.2×10⁻¹⁵; the remaining realness step is the
            named block-CCM lemma, finite-dimensional and ζ-free). The
            pins converge 16/16 —{" "}
            <strong className="font-medium text-slate-900">
              but the Z1 screen fires
            </strong>
            : band pins equal cache partial sums to rel 7.7×10⁻¹² — the
            round-89 transcription conviction, inherited by the literal
            CCM carrier; side by side, the Krein benchmark extrapolates
            genuinely (2.9×10⁻⁴) while the CCM carrier band-transcribes
            (1.3×10⁻¹) —{" "}
            <strong className="font-medium text-slate-900">
              the Krein carrier remains the only non-transcribing attack
              surface in the corpus
            </strong>
            . The cross-carrier test: 17/17 operator moments are monotone
            lower bounds of the Hausdorff moments, the deficit exactly the
            RvM band tail (median ratio 0.786) — one object only in the
            limit. The Jensen hyperbolicity wedge (arXiv:2608.08682) is
            verified verbatim but typed NO-DICTIONARY — its only corpus
            bridge is alternating-signed, so by form-locality it adds no
            unconditional Hausdorff cells. The architecture&apos;s selling
            point is verified as logic and priced: one Stieltjes
            representation would generate all three positivity families at
            once, while finite certificates are form-local — correct, and
            precisely therefore worthless without a non-transcribing
            carrier. The remaining theorem is doubly named:{" "}
            <strong className="font-medium text-slate-900">
              CCM&apos;s own §7–8 prolate approximation — equivalently the
              round-90 Weyl-disk contraction, pointwise at the pins
            </strong>
            .
          </p>
        </div>

        <p className="mt-6 max-w-3xl text-sm leading-relaxed text-slate-600">
          Honest fence: the identification is a finite mode-for-mode
          certification at the built rungs, never a claim about the limit;
          the transcription conviction types the finite ladder, not
          CCM&apos;s theorem; and the killed classes are priced against
          the corpus&apos;s own measured budget, with every citation
          verified against its source. RH is neither proven nor disproven;
          all of it is sandbox — no claim moves until it is promoted.
        </p>
      </div>
    </section>
  );
}

function BigPictureSection() {
  return (
    <section
      id="big-picture"
      aria-labelledby="big-picture-heading"
      className="scroll-mt-24 border-t border-slate-200/60 py-12 sm:py-16"
    >
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center gap-2">
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
            00 · Start here
          </span>
          <StatusBadge badge="sandbox" />
        </div>
        <h2
          id="big-picture-heading"
          className="mt-3 font-serif text-2xl font-semibold leading-tight text-slate-950 sm:text-3xl md:text-4xl"
        >
          The big picture, in plain words
        </h2>
        <p className="mt-4 max-w-3xl text-base leading-relaxed text-slate-700">
          The rest of this page is a diary, written as the work happened, in the
          language of the work. This section says the same thing in ordinary
          words. Every number below is copied from the diary. Every limit is
          named.
        </p>

        <div className="mt-8 grid gap-4 lg:grid-cols-2">
          <article className="rounded-2xl border border-sky-400/30 bg-sky-500/[0.07] p-5 sm:p-6">
            <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-sky-700/90">
              What we are trying to do
            </p>
            <h3 className="mt-2 font-serif text-xl text-sky-50">
              A relay that has to work forever
            </h3>
            <div className="mt-3 space-y-3 text-sm leading-relaxed text-slate-700">
              <p>
                There is one quantity in this story that must never go negative.
                It is assembled out of the prime numbers, one prime at a time.
              </p>
              <p>
                Picture a bridge built span by span. Each new span has to carry
                the load the previous one can no longer hold. Each prime is a
                span. The handover from one span to the next is the whole
                question: does it keep working, prime after prime, without end?
              </p>
              <p>
                If it does, a classical statement called{" "}
                <strong className="font-medium text-slate-900">
                  Weil positivity
                </strong>{" "}
                holds — and that statement is equivalent to the Riemann
                Hypothesis. So this is where the difficulty of the Riemann
                question actually sits, in the form the diary can touch. We do
                not prove it. We test the relay span by span, and we write down
                precisely what a proof would still need.
              </p>
            </div>
          </article>

          <article className="rounded-2xl border border-emerald-400/30 bg-emerald-500/[0.07] p-5 sm:p-6">
            <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-emerald-700/90">
              What actually works today
            </p>
            <h3 className="mt-2 font-serif text-xl text-emerald-50">
              The mechanism has never failed a step
            </h3>
            <div className="mt-3 space-y-3 text-sm leading-relaxed text-slate-700">
              <p>
                Every handover that has been checked, checks out. 117 of 117 in
                the deep ladder{" "}
                <span className="font-mono text-amber-800">[T111]</span>, 400 of
                400 rungs of the nested ladder{" "}
                <span className="font-mono text-amber-800">[T124]</span>, and a
                single certified step as deep as{" "}
                <strong className="font-medium text-emerald-800">
                  zone 155,921
                </strong>{" "}
                <span className="font-mono text-amber-800">[T115]</span>.
              </p>
              <p>
                When a chain of steps stops, it stops because the computer runs
                out of budget — never because a step failed.
              </p>
              <p>
                It did not always look like that. For a while there seemed to be
                a wall near zone 462{" "}
                <span className="font-mono text-amber-800">[T111]</span>. Then
                T113 showed the wall was measuring our own grid rather than the
                mathematics, and T114 removed the division that produced it. The
                wall dissolved, and eleven steps opened up beyond it at once.
              </p>
            </div>
          </article>
        </div>

        <div className="mt-8 grid gap-4 lg:grid-cols-2 lg:items-start">
          <div className="space-y-3 text-base leading-relaxed text-slate-700">
            <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
              The great compression
            </p>
            <h3 className="font-serif text-xl text-slate-950">
              One huge inequality, squeezed down to two small ones
            </h3>
            <p className="text-sm">
              At T104 the thing left to prove was a{" "}
              <strong className="font-medium text-slate-900">
                matrix inequality
              </strong>
              : a statement about every direction of a large window at once.
              Twenty-one parts later the load-bearing part of it is one sign and
              one accounting convention.
            </p>
            <p className="text-sm">
              Nothing was assumed away on the route. At each stage the older,
              bigger statement was shown to <em>follow</em> from the smaller one
              — and several times a step of our own was refuted and replaced,
              which is why the list is shorter and not longer.
            </p>
            <p className="text-sm text-slate-600">
              What is left today: on the load-bearing spine, one <em>sign</em>{" "}
              that the induction already carries on its own plus one declared{" "}
              <strong className="font-medium text-slate-800">
                accounting convention
              </strong>{" "}
              <span className="font-mono text-amber-800">[T124, T125]</span>. The{" "}
              <strong className="font-medium text-slate-800">
                Harnack pair
              </strong>{" "}
              — two statements that hold on every window measured so far —
              survives as a second, independent route and no longer holds the
              spine up. Neither is proved. Both now have classical addresses.
            </p>
          </div>
          <ReductionCascade />
        </div>

        <aside className="mt-8 rounded-2xl border border-rose-400/35 bg-rose-500/[0.08] p-5 sm:p-6">
          <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-rose-700">
            The honest box — what this is not
          </p>
          <ul className="mt-3 space-y-2.5 text-sm leading-relaxed text-slate-700">
            <li>
              <strong className="font-medium text-rose-800">
                No zeta input anywhere.
              </strong>{" "}
              The chain is classical numerical analysis from end to end. The
              zeta function is never fed in, so nothing here can be a
              circular re-derivation of it.
            </li>
            <li>
              <strong className="font-medium text-rose-800">
                No infinite statement.
              </strong>{" "}
              Every certificate is a finite computation on a finite window. An
              infinite claim would need the two open statements — that is the
              whole point of naming them.
            </li>
            <li>
              <strong className="font-medium text-rose-800">
                A measured ladder is not all zones.
              </strong>{" "}
              Where this page says “certified”, it means the zones that were
              actually run. Trends beyond them are labelled as fits or
              extrapolations, never as results.
            </li>
            <li>
              <strong className="font-medium text-rose-800">
                Sandbox, not verified physics.
              </strong>{" "}
              This entire diary is exploratory. Only the promoted modules{" "}
              <Link
                prefetch={false}
                href="/verification"
                className="font-mono text-emerald-700 underline decoration-emerald-400/40 underline-offset-2 hover:text-emerald-800"
              >
                v535–v970 (this front)
              </Link>{" "}
              are machine-verified and cited in the papers. Sandbox probes never
              move a status marker.
            </li>
            <li>
              <strong className="font-medium text-rose-800">
                Not RH, and not almost-RH.
              </strong>{" "}
              “I5 ⟺ RH” is a <em>typing</em> of what the remaining core is
              equivalent to — not a proof claim and not a measure of distance.
              No progress toward the Riemann Hypothesis is claimed. Cryptography
              is unaffected.
            </li>
          </ul>
        </aside>

        <div className="mt-8">
          <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-600">
            Where it stands now
          </p>
          <dl className="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-4">
            <BigPictureStat
              term={`${DIARY_RUN_COUNT}`}
              desc="agent runs in the diary — series complete at 125 parts, phase 2's measurement programme closed, backflow rounds ongoing"
              tone="sky"
            />
            <BigPictureStat
              term="6638+"
              desc="sandbox checks logged across the diary's probes, all passing"
              tone="amber"
            />
            <BigPictureStat
              term="v535–v970"
              desc={`machine-verified modules of this front, inside the ${SCRIPT_TOTAL}-script suite (all green)`}
              tone="emerald"
            />
            <BigPictureStat
              term="96.2%"
              desc="of the load-bearing spine is an identity or a Cholesky certificate (T125 finale)"
              tone="violet"
            />
          </dl>
          <p className="mt-4 max-w-3xl text-sm leading-relaxed text-slate-600">
            The chain is written as a{" "}
            <strong className="font-medium text-slate-800">
              conditional theorem
            </strong>
            : everything after the word “suppose” is proved or certified. The
            finale{" "}
            <span className="font-mono text-slate-700">
              grand_assembly_probe.py
            </span>{" "}
            assembled it end to end on 52 zones and changed what has to be
            supposed:{" "}
            <strong className="font-medium text-slate-800">
              the series is complete, and the chain&apos;s spine needs no Harnack
              pair
            </strong>{" "}
            — that pair survives only as a second, independent route, and the one
            hypothesis the spine still carries is a declared accounting
            convention. What is missing for any infinite statement is uniformity
            in the zone index, not size — and that is now the program: the
            series is complete, and a second phase (T126+) attacks the two
            remaining genuinely new inequalities, the direction lemma and the
            zone-uniform seam floor. Sandbox; not RH evidence.
          </p>
        </div>
      </div>
    </section>
  );
}

const BIG_PICTURE_TONE = {
  sky: "border-sky-400/30 bg-sky-500/[0.08] text-sky-800",
  amber: "border-amber-400/30 bg-amber-500/[0.08] text-amber-800",
  emerald: "border-emerald-400/30 bg-emerald-500/[0.08] text-emerald-800",
  violet: "border-violet-400/30 bg-violet-500/[0.08] text-violet-800",
} as const;

function BigPictureStat({
  term,
  desc,
  tone,
}: {
  term: string;
  desc: string;
  tone: keyof typeof BIG_PICTURE_TONE;
}) {
  return (
    <div className={`rounded-xl border px-3 py-3 ${BIG_PICTURE_TONE[tone]}`}>
      <dt className="font-mono text-xl leading-none">{term}</dt>
      <dd className="mt-1.5 text-[11px] leading-tight text-slate-600">
        {desc}
      </dd>
    </div>
  );
}

function ProgramStatusCallout() {
  return (
    <aside className="rounded-2xl border border-violet-400/35 bg-violet-500/10 p-5 sm:p-6">
      <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-violet-700/90">
        Strongest current sentence
      </p>
      <p className="mt-3 font-serif text-lg leading-relaxed text-violet-50 sm:text-xl">
        After the T102–T176 sprint (its identity cores promoted module by
        module), what remains TFPT-specific is exactly one object: I5 — and the
        induction that would carry it is now
        a conditional theorem, assembled end to end on 52 zones (T125), whose
        load-bearing spine is 96.2% identity or Cholesky certificate, whose only
        hypothesis is a declared accounting convention, and whose seam
        architecture is finished (T126): both remaining inequalities are
        proof-shaped (T127), three of the four resulting points stand at their
        preregistered bars (T128 · THREE-OF-FOUR), the kappa law that T128
        preregistered falls once on 331 fresh transports while the theorem
        underneath it stands (T129 · KAPPA-WILD), the graded-to-uniform
        bridge stands as an identity — 84 pairs, zero overshoot, both deep
        seams carried to positive fine floors — while the curvature bound is
        reduced to a uniform bound on one exponent (T130 · ONE-OF-TWO), and
        the self-supply loop is built one number short of closed: the
        epsilon-to-floor sandwich and sign constancy via Perron–Frobenius
        are theorems, and M25 reduces to positivity of the pole-free
        section with nine decades of slack (T131 · SUPPLY-PARTIAL). The phase
        then reversed direction: that identity block is now load-bearing v542
        (nine per-instance identities and theorems, nothing uniform), the
        Beurling–Deny triad became an operator discriminator for the seam DtN
        (T132 · SPECTRUM-ONLY), and a certificate audit hardened v379 to an
        exact positive-mixture Gram certificate (T133 · MIXED). T134 (PARTIAL)
        then closed the existence half of the pole-free floor — all Cholesky
        pivots positive on 79/79 windows, every cheap lower-bound route
        failing by sign, not size, with the one surviving opening named (an
        M-matrix question) — and T135 (BOUNDED-STATE) found the bounded
        faithful seam state the Weil window provably lacks (m_cert = 12, from
        the pre-declared set, with the honest caveats stated). T136
        (ONE-CARRIES) then closed one item of that M-matrix question outright —
        Varga&apos;s regular splitting makes the Jacobi radius an identity and
        Collatz–Wielandt bounds it a priori, sharp to 1.00–1.03 on 900/900 — with
        the exact bookkeeping putting the whole degradation in the margin and M17
        closing negatively; and T137 (BOTH-RESIST) made the long-lag support an
        explicit arithmetic stripe set and certified the entire absolute-value
        envelope family DEAD (ρ(|E|) ≥ 1.32 from below on 35/35), leaving one
        named residue: a sign-preserving bound. Thirteen of those statements are
        now load-bearing as v543 and v544.
      </p>
      <ul className="mt-4 space-y-2 text-xs leading-relaxed text-slate-600">
        <li>
          <strong className="font-medium text-slate-800">
            The mechanism never failed.
          </strong>{" "}
          Every certified handover step holds — 117/117 on the deep ladder at
          retention 1.000000 (T111), 400/400 rungs of the nested ladder (T124).
          Chains stop at the compute budget, never at a step (T114 onward).
        </li>
        <li>
          <strong className="font-medium text-slate-800">
            Depth reached, certified.
          </strong>{" "}
          Margin-free steps up to n = 1331 (T114) and a single certified step at
          n = 155,921 (T115); a boundary march to 1.35 million cells at flat cost
          (T116, declared a cost-geometry demonstration, not a Weil certificate).
        </li>
        <li>
          <strong className="font-medium text-slate-800">
            The wall was a ruler.
          </strong>{" "}
          The apparent margin wall near zone 462 (T111) is currency-invariant
          (T113) but measures the discretization, not the spectrum — and it
          dissolves once the artifact division is removed (T114).
        </li>
        <li>
          <strong className="font-medium text-slate-800">
            What is left, named.
          </strong>{" "}
          On the spine: one sign the coarse-to-fine induction already carries
          plus one declared accounting convention (T124/T125). The Harnack pair
          (T120/T121, unconditional |R − 1| ≤ 0.047 plus a section statement) is
          a second, independent route and no longer load-bearing. Honestly booked
          against it: the solution-free version of the rung fails, the
          unconditional D₀ criterion covers only the first three zones (T120),
          and uniformity in the zone index is open (T125).
        </li>
        <li>
          <strong className="font-medium text-slate-800">
            Series balance — complete.
          </strong>{" "}
          125 parts, 3139/3139 sandbox checks, seven promoted modules; the finale{" "}
          <span className="font-mono text-slate-700">
            grand_assembly_probe.py
          </span>{" "}
          (ASSEMBLY-GREEN, 34/34) assembled the chain end to end — 52 zones, 430
          completed Cholesky certificates, 24 refuted routes and a seven-station
          cascade booked. The mandate T ≤ 125 is fulfilled; the next step is a
          decision about extraction, not another probe. The full sprint is told
          in{" "}
          <a
            href="#compression"
            className="text-sky-700 underline decoration-sky-400/30 underline-offset-2 hover:text-sky-800"
          >
            sections 22–24
          </a>
          . Not almost-RH. This is not RH evidence.
        </li>
        <li>
          <strong className="font-medium text-slate-800">
            Phase 2: the full proof.
          </strong>{" "}
          The first post-series probe (T126 · SEAMS-CERTIFIED, 31/31)
          finished the seam architecture and left exactly two genuinely new
          inequalities — the direction lemma (U3) and the zone-uniform seam
          floor (U5). The phase then worked them down round by round
          (T127–T176), promoted every identity core module by module
          (v542–v562), and closed its measurement programme as planned:
          R1 stands classified as a near-degeneracy, not a size. The full
          phase-2 narrative — every probe, every honest break — is
          preserved verbatim behind the expander. Sandbox; not RH evidence.
          <VerbatimRecap
            id="phase2FullProof"
            className="mt-2"
            label="The full phase-2 recap (T126–T176), preserved verbatim"
          />
        </li>
      </ul>
    </aside>
  );
}

/** Depth reach of the certified chain across the sprint. Numbers from T110–T116. */
const DEPTH_REACH = [
  { part: "T110", label: "certified handover steps", value: "15" },
  { part: "T111", label: "handovers, retention 1.000000", value: "117/117" },
  { part: "T114", label: "deepest certified zone", value: "n = 1331" },
  { part: "T115", label: "deepest certified zone", value: "n = 155,921" },
  { part: "T116", label: "boundary march, flat cost", value: "1.35M cells" },
] as const;

function DepthReachCallout() {
  return (
    <aside className="rounded-2xl border border-emerald-400/35 bg-emerald-500/10 p-5 sm:p-6">
      <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-emerald-700/90">
        Depth reach · what the chain certified, part by part
      </p>
      <dl className="mt-4 space-y-2.5">
        {DEPTH_REACH.map((d) => (
          <div
            key={`${d.part}-${d.value}`}
            className="flex flex-wrap items-baseline gap-x-2 border-b border-emerald-400/15 pb-2 last:border-0 last:pb-0"
          >
            <dt className="font-mono text-[11px] text-emerald-800">{d.part}</dt>
            <dd className="font-mono text-sm text-emerald-50">{d.value}</dd>
            <dd className="min-w-0 flex-1 text-right text-[11px] text-slate-600">
              {d.label}
            </dd>
          </div>
        ))}
      </dl>
      <p className="mt-4 text-xs leading-relaxed text-slate-600">
        Chains stop at the compute budget, never at a step. T116&apos;s march is
        a cost-geometry demonstration, not a Weil certificate — declared as such
        in the probe. Sandbox; not RH evidence.
      </p>
    </aside>
  );
}

function AmplitudeRouteCallout() {
  return (
    <aside className="rounded-2xl border border-sky-400/35 bg-sky-500/10 p-5 sm:p-6">
      <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-sky-700/90">
        Transport compressed · v540
      </p>
      <p className="mt-3 font-serif text-lg leading-relaxed text-sky-50 sm:text-xl">
        The transport problem, compressed to a single measurable object: the
        FE-covariant gap functional λ* on the atoms n&nbsp;≡&nbsp;6&nbsp;mod&nbsp;8.
      </p>
      <p className="mt-4 text-xs leading-relaxed text-slate-600">
        Square closed → linear plus-carrier stands → cone library saturates at
        5/24. Euler-region positivity ≠ central-line claim. This is not RH
        evidence.
      </p>
    </aside>
  );
}

function DoorsFurnishedCallout() {
  return (
    <aside className="rounded-2xl border border-amber-400/35 bg-amber-500/10 p-5 sm:p-6">
      <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-amber-700/90">
        The wall, named
      </p>
      <p className="mt-3 font-serif text-lg leading-relaxed text-amber-50 sm:text-xl">
        The wall is no longer a metaphor: it is one named inequality —
        provably equivalent to RH. Everything else on the route is either
        proved or classically provable-shaped.
      </p>
      <p className="mt-4 text-xs leading-relaxed text-slate-600">
        After T81 the recipe chain saturated. Three new perspectives (next)
        retype I5 without claiming RH progress.
      </p>
    </aside>
  );
}

function ThreePerspectivesCallout() {
  return (
    <aside className="rounded-2xl border border-sky-400/35 bg-sky-500/10 p-5 sm:p-6">
      <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-sky-700/90">
        New I5 form — fence
      </p>
      <p className="mt-3 font-mono text-sm leading-relaxed text-sky-800">
        {"Q_cert(h) + Δ₂(h) + A_fam(h) − A_shift(h) ≥ 0"}
      </p>
      <p className="mt-3 font-serif text-base leading-relaxed text-sky-50">
        Self-consistency of one heat family. Type change ≠ proof; I5 remains ⟺
        RH. Coherent class closed via λ-channel.
      </p>
      <p className="mt-4 text-xs leading-relaxed text-slate-600">
        T86{" "}
        <span className="font-mono text-amber-800">
          [sandbox · LEMMA-FULLY-CLOSED]
        </span>
        : all atom classes covered. Geography next. This is not RH evidence.
      </p>
    </aside>
  );
}

function BlindPrimeCallout() {
  return (
    <aside className="mt-8 rounded-2xl border border-emerald-400/40 bg-emerald-500/10 p-5 sm:p-6">
      <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-emerald-700/90">
        Blind demo · T94 · sandbox
      </p>
      <p className="mt-3 font-serif text-xl leading-relaxed text-emerald-50 sm:text-2xl">
        753/753 primes predicted — zero errors, no division.
      </p>
      <p className="mt-3 text-sm leading-relaxed text-slate-700">
        All primes in the never-seen window [1,000,001–1,010,000], from pure
        lattice counting (Jacobi 1834: odd n prime ⟺ r₄(n)&nbsp;=&nbsp;8(n+1)),
        with an AST-enforced prediction path containing no divisibility tests.
        Predictions committed by MD5 before any truth was computed. Honesty: a
        sieve is ~820× faster — structure completeness, not algorithmic
        progress. Spectral prediction (zeros&nbsp;→&nbsp;primes) remains bound
        to I5/RH.
      </p>
    </aside>
  );
}

function I5GeographyCallout() {
  return (
    <aside className="rounded-2xl border border-violet-400/35 bg-violet-500/10 p-5 sm:p-6">
      <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-violet-700/90">
        Geography — not an attack
      </p>
      <p className="mt-3 font-serif text-lg leading-relaxed text-violet-50 sm:text-xl">
        Identities proved; zones 2–4 closed; zone-5 tip = equality; asymptotics
        = one named arithmetic bound (A).
      </p>
      <p className="mt-4 text-xs leading-relaxed text-slate-600">
        I5 remains ⟺ RH; the geography locates where any attack must work, it
        does not perform one. 2428/2428 sandbox checks at T101 (5360/5360
        today). This is not RH evidence.
      </p>
    </aside>
  );
}

function MeaningLevel({
  level,
  badge,
  title,
  body,
  children,
}: {
  level: string;
  badge: "sandbox" | "machine-verified";
  title: string;
  body: string;
  children?: React.ReactNode;
}) {
  return (
    <li className="rounded-2xl border border-slate-300/45 bg-slate-50/40 p-4">
      <div className="flex flex-wrap items-center gap-2">
        <span className="font-mono text-[10px] uppercase tracking-widest text-slate-600">
          {level}
        </span>
        <StatusBadge badge={badge} />
      </div>
      <h3 className="mt-1 font-serif text-lg text-slate-900">{title}</h3>
      <p className="mt-1 text-sm leading-relaxed text-slate-600">{body}</p>
      {children}
    </li>
  );
}
