import { pageMetadata } from "@/lib/seo";
import type { Metadata } from "next";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { SectionHeader } from "@/components/SectionHeader";
import { MethodPipeline } from "@/components/method/MethodPipeline";
import { DisciplineNumbers } from "@/components/method/DisciplineNumbers";
import { Graveyard } from "@/components/method/Graveyard";
import { FalsifyList } from "@/components/method/FalsifyList";
import { StatusTypology } from "@/components/method/StatusTypology";
import { AiTransparency } from "@/components/method/AiTransparency";
import { DISCIPLINE } from "@/lib/discipline";
import { SITE_VERSION } from "@/lib/version";
import { SITE_URL } from "@/lib/utils";

export const metadata: Metadata = pageMetadata("/method");

const articleJsonLd = {
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  headline: "Method — The TFPT verification framework",
  url: `${SITE_URL}/method`,
  inLanguage: "en",
  isPartOf: {
    "@type": "PublicationIssue",
    name: `TFPT ${SITE_VERSION} compiler-closure document set`,
  },
  author: [
    { "@type": "Person", name: "Stefan Hamann" },
    { "@type": "Person", name: "Alessandro Rizzo" },
  ],
  abstract:
    "The scientific process behind TFPT: exploratory work is firewalled in a sandbox, probes declare kill criteria before running, surviving results are promoted into a deterministic verification suite, one status ledger is the single source of truth, and papers and website are generated mirrors. The process discipline itself is measured and certified by a suite module (v649, META.DISCIPLINE.01).",
  about: [
    "Verification",
    "Falsifiability",
    "Preregistration",
    "Reproducibility",
    "Topological Fixed-Point Theory",
  ],
};

const fmt = (n: number) => n.toLocaleString("en-US");

export default function MethodPage() {
  const d = DISCIPLINE;
  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(articleJsonLd) }}
      />

      {/* ── Hero ─────────────────────────────────────────────────────── */}
      <section className="relative isolate overflow-hidden pt-12 pb-12 sm:pt-16">
        <div aria-hidden className="absolute inset-0 grid-bg pointer-events-none" />
        <div
          aria-hidden
          className="absolute -top-40 left-1/2 -z-10 h-[500px] w-[1000px] -translate-x-1/2 rounded-full opacity-30 blur-3xl"
          style={{
            background:
              "radial-gradient(closest-side, rgba(52,211,153,0.35), rgba(96,165,250,0.2), transparent)",
          }}
        />
        <div className="relative mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
          <nav aria-label="Breadcrumb" className="mb-6">
            <Link
              prefetch={false}
              href="/"
              className="inline-flex items-center gap-1.5 text-sm text-slate-600 transition-colors hover:text-slate-800"
            >
              <ArrowLeft size={14} />
              Back to overview
            </Link>
          </nav>
          <span className="inline-flex items-center gap-2 rounded-full border border-emerald-400/20 bg-emerald-500/10 px-4 py-1.5 text-xs font-medium tracking-wider text-emerald-800">
            <span className="uppercase">Method · the verification framework</span>
          </span>
          <h1 className="mt-6 font-serif text-4xl font-semibold leading-tight text-slate-950 sm:text-5xl md:text-6xl">
            Every claim is machine-checked.
            <br />
            Every temptation is{" "}
            <span className="text-emerald-700">promoted with controls</span> —
            or <span className="text-rose-700">buried in public</span>.
          </h1>
          <p className="mt-4 max-w-2xl text-base leading-relaxed text-slate-700">
            A project built around exact integer and lattice identities has to
            answer one suspicion before any other:{" "}
            <em>how is this not numerology?</em> This page is the answer — not
            as a promise, but as measured process discipline: a sandbox
            firewall, kill criteria declared before execution, a deterministic
            suite, one versioned ledger, and a public graveyard of the
            coincidences that did not survive.
          </p>
          <p className="mt-3 max-w-2xl text-sm leading-relaxed text-slate-600">
            The discipline itself is a suite claim: module{" "}
            <code className="text-slate-700">v649_discipline_audit.py</code>{" "}
            (<code className="text-slate-700">META.DISCIPLINE.01</code>) parses
            the repository on every run and fails if any census below
            regresses.
          </p>
        </div>
      </section>

      {/* ── The pipeline ─────────────────────────────────────────────── */}
      <section
        id="pipeline"
        className="relative scroll-mt-20 py-12 sm:py-14"
        aria-labelledby="pipeline-heading"
      >
        <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
          <SectionHeader
            id="pipeline-heading"
            eyebrow="The pipeline"
            title="From sandbox to claim — one direction, one gate"
            description="Nothing becomes a claim by being written down. Exploration lives in experiments/ behind a firewall; a probe must declare its kill criteria before it runs; only what survives is promoted into the verification suite; the ledger decides every status; papers and website are generated mirrors that an audit checks against the ledger."
          />
          <div className="mt-8">
            <MethodPipeline />
          </div>
          <div className="mt-6 grid gap-4 text-sm leading-relaxed text-slate-600 md:grid-cols-3">
            <p>
              <span className="font-semibold text-slate-800">
                The firewall.
              </span>{" "}
              Results in <code className="text-slate-700">experiments/</code>{" "}
              are search surfaces, not claims — they cannot be cited by a
              paper, cannot move a status, and are labelled sandbox on this
              site until promoted.
            </p>
            <p>
              <span className="font-semibold text-slate-800">
                The one gate.
              </span>{" "}
              Promotion means: a{" "}
              <code className="text-slate-700">verification/vN_*.py</code>{" "}
              module with named checks and frozen tolerances, a ledger row, a
              citation in a paper body, and a green{" "}
              <code className="text-slate-700">run_all.py</code>. A finding
              that skips any of these does not exist.
            </p>
            <p>
              <span className="font-semibold text-slate-800">
                The mirrors.
              </span>{" "}
              The script index, the changelog, the maps and the numbers on
              this page are generated files.{" "}
              <code className="text-slate-700">bash build.sh audit</code>{" "}
              fails if any mirror drifts from its source.
            </p>
          </div>
        </div>
      </section>

      {/* ── The numbers ──────────────────────────────────────────────── */}
      <section
        id="numbers"
        className="relative scroll-mt-20 border-t border-slate-200/60 py-12 sm:py-14"
        aria-labelledby="numbers-heading"
      >
        <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
          <SectionHeader
            id="numbers-heading"
            eyebrow="The numbers"
            title="Discipline, measured"
            description="These are not marketing figures. They are censuses computed from the repository itself — the ledger, the module sources, the contracts paper, the Lean tree — regenerated by the build and frozen as minimum bars inside the suite."
          />
          <div className="mt-8">
            <DisciplineNumbers />
          </div>
        </div>
      </section>

      {/* ── The graveyard ────────────────────────────────────────────── */}
      <section
        id="graveyard"
        className="relative scroll-mt-20 border-t border-slate-200/60 py-12 sm:py-14"
        aria-labelledby="graveyard-heading"
      >
        <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
          <SectionHeader
            id="graveyard-heading"
            eyebrow="Buried coincidences"
            title="The graveyard"
            description={`A confirmation-bias generator keeps every coincidence it finds. This project has buried ${fmt(d.ledger.killRows)} of its own readings — killed, retyped or retired in the open, each with the module that did it. Seven of the most tempting ones:`}
          />
          <div className="mt-8">
            <Graveyard />
          </div>
        </div>
      </section>

      {/* ── What would falsify this ──────────────────────────────────── */}
      <section
        id="falsify"
        className="relative scroll-mt-20 border-t border-slate-200/60 py-12 sm:py-14"
        aria-labelledby="falsify-heading"
      >
        <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
          <SectionHeader
            id="falsify-heading"
            eyebrow="Standing kill criteria"
            title="What would falsify this"
            description={`${fmt(d.contracts.ledgerRows)} contract rows are open in the ledger, ${fmt(d.contracts.withKillCriteria)} with kill criteria named before execution. These are the ways the construction dies — committed in advance, not negotiated afterwards.`}
          />
          <div className="mt-8">
            <FalsifyList />
          </div>
        </div>
      </section>

      {/* ── Status honesty ───────────────────────────────────────────── */}
      <section
        id="status"
        className="relative scroll-mt-20 border-t border-slate-200/60 py-12 sm:py-14"
        aria-labelledby="status-heading"
      >
        <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
          <SectionHeader
            id="status-heading"
            eyebrow="Status honesty"
            title="Four classes, one ledger, no silent upgrades"
            description="Every claim carries a display marker decided by the status ledger. The distribution below is measured from the ledger — and it is deliberately not flattering."
          />
          <div className="mt-8">
            <StatusTypology />
          </div>
        </div>
      </section>

      {/* ── AI transparency ──────────────────────────────────────────── */}
      <section
        id="ai"
        className="relative scroll-mt-20 border-t border-slate-200/60 py-12 pb-20 sm:py-14"
        aria-labelledby="ai-heading"
      >
        <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
          <SectionHeader
            id="ai-heading"
            eyebrow="AI transparency"
            title="Instruments, not authorities"
            description="The role of AI agents in this project, stated plainly — and why the trust model does not depend on them."
          />
          <div className="mt-8">
            <AiTransparency />
          </div>
        </div>
      </section>
    </>
  );
}
