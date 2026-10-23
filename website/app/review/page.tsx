import { pageMetadata } from "@/lib/seo";
import type { Metadata } from "next";
import Link from "next/link";
import {
  ArrowLeft,
  ArrowRight,
  CheckCircle2,
  CircleDot,
  FlaskConical,
  ShieldAlert,
  Target,
  XCircle,
} from "lucide-react";
import { SCRIPT_TOTAL } from "@/lib/suite";
import { SITE_VERSION } from "@/lib/version";
import { REPO_URL, SITE_URL } from "@/lib/utils";

export const metadata: Metadata = pageMetadata("/review");

interface Block {
  icon: React.ReactNode;
  kicker: string;
  title: string;
  body: React.ReactNode;
  tone: string;
}

const BLOCKS: Block[] = [
  {
    icon: <Target size={18} aria-hidden />,
    kicker: "1 · The claim",
    title: "What TFPT claims",
    tone: "border-blue-400/30 bg-blue-500/[0.05]",
    body: (
      <>
        A two-input discrete compiler whose algebraic kernel derives the{" "}
        <strong className="text-slate-900">Standard-Model skeleton</strong> — the
        gauge group, three families, hypercharge and the flavor invariants — and
        several dimensionless readouts (α⁻¹, the neutrino angles, β_rad). It is
        built only from two axioms: the seam constant{" "}
        <span className="font-mono">c₃ = 1/(8π)</span> and the carrier rank{" "}
        <span className="font-mono">g_car = 5</span>. E₈ is the compiler&rsquo;s
        internal audit lattice, not a physical gauge group.
      </>
    ),
  },
  {
    icon: <XCircle size={18} aria-hidden />,
    kicker: "2 · The non-claims",
    title: "What TFPT does not claim",
    tone: "border-slate-500/30 bg-slate-500/[0.05]",
    body: (
      <>
        It is <strong className="text-slate-900">not</strong> an E₈ gauge theory
        (so the Distler–Garibaldi / Coleman–Mandula no-gos do not apply), and{" "}
        <strong className="text-slate-900">not</strong> a certified strict
        physical theory of everything end-to-end — the keystone SEAM.EQUIV.01 is
        closed only on its MMST route (SEAM.EQUIV.MMST.01), modulo a cited
        published theorem (the cited continuum scaling-limit existence, v336;
        extension leg on the peer-reviewed crossed-product package, realisation
        at invariant level, v469; the twistor route SEAM.EQUIV.TWISTOR.01 and
        the unconditional parent stay [O]). The classical covariant field equation carries no free dimensionless Newton coupling under the named QFT/entanglement premises [C],
        and the ambient, non-perturbative quantum-gravity measure is discharged as
        a redundancy [C] (a certification object, not missing dynamics), not an
        open hole. The absolute mass scale is a single declared dimensionful
        anchor (v_geo), and{" "}
        <span className="font-mono">m_p/m_e</span> is explicitly not claimed as a
        compiler power. No experimental value is ever used as an input — only as
        a comparison row.
      </>
    ),
  },
  {
    icon: <ShieldAlert size={18} aria-hidden />,
    kicker: "3 · The kill conditions",
    title: "What would kill it",
    tone: "border-rose-400/30 bg-rose-500/[0.05]",
    body: (
      <>
        Any single one of: the α fixed-point equation{" "}
        <span className="font-mono">F_U(1)(α) = 0</span> failing or admitting a
        second admissible root; a robust neutron-EDM signal (θ_eff = 0 is
        structural); a second light seam-even Higgs doublet (N_Φ = 1); a robust
        tensor ratio <span className="font-mono">r ≳ 0.01</span>; a robust{" "}
        <span className="font-mono">w ≠ −1</span>; a JUNO solar angle clearly away
        from 0.307; or any verification script failing to reproduce its claim.{" "}
        <Link prefetch={false} href="/falsification" className="font-semibold text-blue-700 hover:text-blue-800">
          The full kill board →
        </Link>
      </>
    ),
  },
  {
    icon: <CheckCircle2 size={18} aria-hidden />,
    kicker: "4 · The evidence",
    title: "What is machine-checked",
    tone: "border-emerald-400/30 bg-emerald-500/[0.05]",
    body: (
      <>
        Every exact identity, lattice/Lie theorem and numerical fixed point is
        re-derived from the two axioms by{" "}
        <strong className="text-slate-900">{SCRIPT_TOTAL} Python checks</strong>{" "}
        (<span className="font-mono">run_all.py</span> ends ALL CHECKS PASSED),
        mirrored on an independent Wolfram path, and the carrier algebra is
        formalised in Lean 4 with{" "}
        <span className="font-mono">0 sorry</span>. Every claim is typed in a
        single versioned ledger — if the prose and the ledger disagree, the
        ledger wins.{" "}
        <Link prefetch={false} href="/verification" className="font-semibold text-blue-700 hover:text-blue-800">
          The verification stack →
        </Link>
      </>
    ),
  },
  {
    icon: <CircleDot size={18} aria-hidden />,
    kicker: "5 · The residual",
    title: "What remains open",
    tone: "border-amber-400/30 bg-amber-500/[0.05]",
    body: (
      <>
        The compiler residual has exactly three named interfaces, none hidden:{" "}
        <span className="font-mono">v_geo</span> (one dimensionful scale anchor,
        the same nature as 1/G, [O]), <span className="font-mono">G_net</span> (the
        seam-net metric inclusion — algebra discharged to [E]; the seam keystone now
        [C], closed modulo cited theorems), and <span className="font-mono">F_transfer</span>{" "}
        (the source→pole/relic/cosmology transport — Koide, η_B, the axion relic,
        m_p/m_e are its four instances, now runnable typed solvers v371–v375 [C]).
        Beside that compiler residual sits Rest_TOE: every T1–T8 gate and
        TFPT.TOE.COMPLETE.01 remains [O], and no shared 3+1D parent has been
        constructed. Within the historical finite boundary-net/MMST lane, the
        listed Dirac, cutoff, gauging and glue data reduce to the same{" "}
        <span className="font-mono">G_net</span> premise via the Modular Spectral
        Closure (v258–v261); this is not a strict-TOE closure. That
        premise is now closed modulo cited theorems via the Seam Equivalence Theorem{" "}
        <span className="font-mono">SEAM.EQUIV.01</span> (the raw RP seam IS the
        holomorphic (E₈)₁ net at τ=i): the target net is pinned at every computable
        level by an explicit lattice model (v367/v368) and the S3 closure stack
        (v376–v379, ground-state witnesses v489/v490), Lean-pinned (FORM.SEAM.MMST.01) to the published MMST/Adamo
        theorems, leaving [O] = the cited continuum scaling-limit existence only
        (v336; extension leg on the peer-reviewed crossed-product package,
        realisation at invariant level, v469; stays [O]); its conformal-deck
        face QGEO.SYM.01 is a corollary. Round 4 (v1026–v1030) closes the fixed-M=1,
        Ny=8 relaxed TEL-B norm ||R_N||HS &lt; 2.995906 &lt; 3 for every even N≥16;
        native v1026 uses v1022/v1025 for the former CF/DG estimates. The other
        modules add narrow T3/T4/T6–T8 identities and counterbounds. FE-GEN/ALG-EXH,
        every T1–T8 gate and the shared 3+1D parent remain [O]; v1029 requires global
        zero-mode removal and is not a TFPT embedding. These native certificates are
        not browser certificates. The
        step-by-step reduction lives on the{" "}
        <Link prefetch={false} href="/changelog" className="font-semibold text-blue-700 hover:text-blue-800">
          changelog
        </Link>
        .{" "}
        <Link prefetch={false} href="/verification#open-gates" className="font-semibold text-blue-700 hover:text-blue-800">
          The open residual →
        </Link>
      </>
    ),
  },
  {
    icon: <FlaskConical size={18} aria-hidden />,
    kicker: "6 · The five-minute test",
    title: "Reproduce one result in five minutes",
    tone: "border-violet-400/30 bg-violet-500/[0.05]",
    body: (
      <>
        Open the dependency graph and click the{" "}
        <span className="font-mono">α⁻¹</span> node: the real Python runs in your
        browser (via Pyodide / WebAssembly) and re-derives{" "}
        <span className="font-mono">α⁻¹ = 137.0359992…</span> as the unique root
        of the parameter-free cubic — no install, no fit.{" "}
        <Link prefetch={false} href="/verification#dag" className="font-semibold text-blue-700 hover:text-blue-800">
          Run it now →
        </Link>{" "}
        Or clone the repository and run the whole suite locally.
      </>
    ),
  },
];

export default function ReviewPage() {
  return (
    <>
      <section className="relative isolate overflow-hidden pt-12 pb-8 sm:pt-16">
        <div aria-hidden className="absolute inset-0 grid-bg pointer-events-none" />
        <div
          aria-hidden
          className="absolute -top-40 left-1/2 -z-10 h-[500px] w-[1000px] -translate-x-1/2 rounded-full opacity-30 blur-3xl"
          style={{
            background:
              "radial-gradient(closest-side, rgba(99,102,241,0.4), rgba(16,185,129,0.2), transparent)",
          }}
        />
        <div className="relative mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
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
          <span className="inline-flex items-center gap-2 rounded-full border border-blue-400/20 bg-blue-500/10 px-4 py-1.5 text-xs font-medium tracking-wider text-blue-800">
            <span className="uppercase">For the skeptical reviewer</span>
          </span>
          <h1 className="mt-6 font-serif text-4xl font-semibold leading-tight text-slate-950 sm:text-5xl md:text-6xl">
            Read this <span className="text-gradient-blue">first</span>.
          </h1>
          <p className="mt-4 max-w-2xl text-base leading-relaxed text-slate-700 sm:text-lg">
            If the claim &ldquo;a derived Standard-Model skeleton&rdquo; set off
            an alarm, good — keep it on. This page is the five-minute orientation:
            what is claimed, what is <em>not</em>, what would falsify it, what is
            machine-checked, what is still open, and how to reproduce one result
            yourself. Nothing here is sold; a typed claim stack is dissected.
          </p>
        </div>
      </section>

      <section className="relative py-8 sm:py-12">
        <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
          <ol className="grid gap-4">
            {BLOCKS.map((b) => (
              <li key={b.kicker}>
                <article className={`rounded-2xl border p-5 sm:p-6 ${b.tone}`}>
                  <div className="flex items-center gap-2 text-slate-800">
                    {b.icon}
                    <span className="text-[10px] font-semibold uppercase tracking-widest text-slate-600">
                      {b.kicker}
                    </span>
                  </div>
                  <h2 className="mt-2 font-serif text-xl font-semibold text-slate-950">
                    {b.title}
                  </h2>
                  <p className="mt-2 text-sm leading-relaxed text-slate-700">{b.body}</p>
                </article>
              </li>
            ))}
          </ol>

          <div className="mt-8 flex flex-wrap gap-3">
            <Link
              prefetch={false}
              href="/verification"
              className="inline-flex items-center gap-2 rounded-full bg-blue-700 px-5 py-2.5 text-sm font-semibold text-white shadow-lg shadow-blue-500/20 transition-transform hover:scale-105"
            >
              Verification stack
              <ArrowRight size={15} aria-hidden />
            </Link>
            <Link
              prefetch={false}
              href="/falsification"
              className="inline-flex items-center gap-2 rounded-full border border-rose-400/40 bg-rose-500/10 px-5 py-2.5 text-sm font-semibold text-rose-800 transition-colors hover:bg-rose-500/20"
            >
              How to kill it
            </Link>
            <Link
              prefetch={false}
              href="/objections"
              className="inline-flex items-center gap-2 rounded-full border border-slate-400/60 bg-slate-100/60 px-5 py-2.5 text-sm font-semibold text-slate-900 transition-colors hover:bg-slate-200/80"
            >
              Objection ledger
            </Link>
            <Link
              prefetch={false}
              href={`${REPO_URL}/issues`}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 rounded-full border border-slate-400/60 bg-slate-100/60 px-5 py-2.5 text-sm font-semibold text-slate-900 transition-colors hover:bg-slate-200/80"
            >
              Open an issue
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
