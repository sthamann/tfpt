import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { SectionHeader } from "./SectionHeader";

/**
 * The 2026-08 geometric-realization arc: the conformal seam axioms force a
 * concrete algebraic curve (the μ₃-cover y³ = x⁴ − 1), and the seam's kernel
 * structure is recovered on it exactly. Every step mirrors a ledger row
 * (QGEO.SEAMFORCE.01 / NCENSUS / SEAMID / COVERSEAM / ORBCAS / E8.INCIDENCE);
 * the bedrock premise itself (GATE.QGEO / QGEO.SYM.01) stays open and is said
 * so explicitly. Static SVG — no motion, safe under prefers-reduced-motion.
 */

const MARKER_TONE: Record<string, string> = {
  "[E]": "text-emerald-800 bg-emerald-500/15 ring-emerald-400/30",
  "[E]/[C]": "text-amber-800 bg-amber-500/15 ring-amber-400/30",
  "[O]": "text-rose-800 bg-rose-500/15 ring-rose-400/30",
};

interface Step {
  marker: string;
  title: string;
  body: string;
  refs: string;
}

const STEPS: Step[] = [
  {
    marker: "[E]/[C]",
    title: "The axioms force the cover",
    body: "ℤ₄-Möbius rigidity pins the four marks to μ₄, and the conformal seam axioms force the μ₃-cover — the genus-3 curve y³ = x⁴ − 1, up to the conjugate sheet. The seam is no longer a template: it has one concrete shape.",
    refs: "v617",
  },
  {
    marker: "[E]/[C]",
    title: "N = 3 is pinned",
    body: "A census of cyclic covers: the seam admits only N ∈ {3, 5} as primitive orders, and the compiler's own 3-adic constants (27, 81) pin N = 3 — conditional on the compiler anchor, typed as such.",
    refs: "v620",
  },
  {
    marker: "[E]",
    title: "The physical seam is the conformal seam",
    body: "The chiral seam kernel equals the antiperiodic (NS) mode sum on the 16-site circle exactly — the periodic (Ramond) sum fails as a must-fail control — and the mark-bond midpoints land literally on μ₄ = {1, i, −1, −i}.",
    refs: "v622",
  },
  {
    marker: "[E]/[C]",
    title: "The covered seam and its ℤ₃ orbifold",
    body: "Lifted to the cover, the seam is one 48-site NS circle; the lifted clock has exact order 12 with L⁴ = deck — the relation r⁴ = ω becomes lattice combinatorics. The deck classes carry the ℤ₃-twist Casimir data exactly, the interacting orbifold slice stands at the abelian vertex level (twist weight 1/36 from three exact routes, crossing symmetry-protected), and the twist sector is reflection positive under the parafermionic Klein pairing (η = (1,1) unique, N-stable).",
    refs: "v623 · v628 · v639 · v645",
  },
];

/** Site/mark coordinates for the seam-circle panel (angles in degrees). */
const seamSites = Array.from({ length: 16 }, (_, a) => {
  const t = ((2 * a + 1) * Math.PI) / 16;
  return { x: 150 + 62 * Math.cos(t), y: 128 - 62 * Math.sin(t) };
});
const seamMarks = [0, 90, 180, 270].map((deg) => {
  const t = (deg * Math.PI) / 180;
  return { x: 150 + 62 * Math.cos(t), y: 128 - 62 * Math.sin(t) };
});

/** Root ring for the E₈ panel: two rings suggesting the 240-root system. */
const rootRingOuter = Array.from({ length: 24 }, (_, k) => {
  const t = (k * 2 * Math.PI) / 24;
  return { x: 810 + 64 * Math.cos(t), y: 128 - 64 * Math.sin(t) };
});
const rootRingInner = Array.from({ length: 12 }, (_, k) => {
  const t = (k * 2 * Math.PI) / 12 + Math.PI / 12;
  return { x: 810 + 36 * Math.cos(t), y: 128 - 36 * Math.sin(t) };
});

function ArcMap() {
  return (
    <svg
      viewBox="0 0 960 264"
      role="img"
      aria-label="Map of the geometric arc: the seam circle with four μ₄ marks, forced μ₃-cover to the genus-3 curve y³ = x⁴ − 1 carrying the 48-site covered seam, and the E₈ root system with its 60 μ₄-clock orbits."
      className="w-full"
    >
      {/* ── Panel 1: the seam ───────────────────────────────────────── */}
      <circle cx="150" cy="128" r="62" fill="none" stroke="#475569" strokeWidth="1.5" />
      {seamSites.map((p, i) => (
        <circle key={`s${i}`} cx={p.x} cy={p.y} r="2.4" fill="#526278" />
      ))}
      {seamMarks.map((p, i) => (
        <rect
          key={`m${i}`}
          x={p.x - 4}
          y={p.y - 4}
          width="8"
          height="8"
          transform={`rotate(45 ${p.x} ${p.y})`}
          fill="#f1f5f9"
          stroke="#93c5fd"
          strokeWidth="1.5"
        />
      ))}
      <text x="150" y="34" textAnchor="middle" fill="#cbd5e1" fontSize="13" fontFamily="var(--font-mono, monospace)">
        ℙ¹ ∖ μ₄ — the seam
      </text>
      <text x="150" y="222" textAnchor="middle" fill="#64748b" fontSize="11" fontFamily="var(--font-mono, monospace)">
        16 sites · marks on μ₄ (v622)
      </text>

      {/* ── Arrow 1 ─────────────────────────────────────────────────── */}
      <line x1="236" y1="128" x2="330" y2="128" stroke="#475569" strokeWidth="1.5" markerEnd="url(#geo-arrow)" />
      <text x="284" y="112" textAnchor="middle" fill="#93c5fd" fontSize="11" fontFamily="var(--font-mono, monospace)">
        μ₃-cover — forced
      </text>
      <text x="284" y="150" textAnchor="middle" fill="#64748b" fontSize="10" fontFamily="var(--font-mono, monospace)">
        v617 · N = 3 (v620)
      </text>

      {/* ── Panel 2: the curve (three sheets over the base circle) ──── */}
      {[-26, 0, 26].map((dy, i) => (
        <ellipse
          key={`sheet${i}`}
          cx="480"
          cy={128 + dy}
          rx="78"
          ry="18"
          fill="none"
          stroke={i === 1 ? "#67e8f9" : "#475569"}
          strokeWidth="1.5"
        />
      ))}
      {/* branch lines through the sheets at the four mark positions */}
      {[-58, -20, 20, 58].map((dx, i) => (
        <line
          key={`br${i}`}
          x1={480 + dx}
          y1={128 - 26 - 14}
          x2={480 + dx}
          y2={128 + 26 + 14}
          stroke="#334155"
          strokeWidth="1"
          strokeDasharray="3 3"
        />
      ))}
      <text x="480" y="34" textAnchor="middle" fill="#cbd5e1" fontSize="13" fontFamily="var(--font-mono, monospace)">
        y³ = x⁴ − 1 — genus 3
      </text>
      <text x="480" y="222" textAnchor="middle" fill="#64748b" fontSize="11" fontFamily="var(--font-mono, monospace)">
        48-site covered seam · clock order 12, L⁴ = deck (v623)
      </text>

      {/* ── Arrow 2 ─────────────────────────────────────────────────── */}
      <line x1="578" y1="128" x2="672" y2="128" stroke="#475569" strokeWidth="1.5" markerEnd="url(#geo-arrow)" />
      <text x="626" y="112" textAnchor="middle" fill="#93c5fd" fontSize="11" fontFamily="var(--font-mono, monospace)">
        readout
      </text>

      {/* ── Panel 3: E₈ ─────────────────────────────────────────────── */}
      {rootRingOuter.map((p, i) => (
        <circle key={`o${i}`} cx={p.x} cy={p.y} r="2.4" fill="#6ee7b7" />
      ))}
      {rootRingInner.map((p, i) => (
        <circle key={`i${i}`} cx={p.x} cy={p.y} r="2" fill="#475569" />
      ))}
      <text x="810" y="132" textAnchor="middle" fill="#263b53" fontSize="15" fontFamily="var(--font-serif, serif)">
        E₈
      </text>
      <text x="810" y="34" textAnchor="middle" fill="#cbd5e1" fontSize="13" fontFamily="var(--font-mono, monospace)">
        240 roots
      </text>
      <text x="810" y="222" textAnchor="middle" fill="#64748b" fontSize="11" fontFamily="var(--font-mono, monospace)">
        μ₄ quotient: 60 ℤ[i]-lines — the ST31 system (v629 · v633 · v634)
      </text>

      <defs>
        <marker id="geo-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
          <path d="M0,0 L8,4 L0,8 Z" fill="#475569" />
        </marker>
      </defs>
    </svg>
  );
}

export function GeometryArc() {
  return (
    <section
      id="geometry"
      className="relative scroll-mt-20 border-t border-slate-200/60 py-14 sm:py-16"
      aria-labelledby="geometry-heading"
    >
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <SectionHeader
          id="geometry-heading"
          eyebrow="The geometric realization"
          title="The seam now has a shape: one curve, forced"
          description="Until mid-2026 the seam was an axiomatized boundary. A chain of machine-checked steps now realizes it geometrically: the seam axioms force one concrete algebraic curve, and the seam's kernel structure is recovered on it exactly. The bedrock premise itself stays open — these are exact slices that narrow it."
        />

        <div className="mt-8 overflow-x-auto border border-slate-300/40 bg-slate-50/40 p-4 sm:p-6">
          <div className="min-w-[640px]">
            <ArcMap />
          </div>
        </div>

        <ol className="mt-6 grid gap-3 sm:grid-cols-2">
          {STEPS.map((s) => (
            <li
              key={s.title}
              className="flex flex-col border border-slate-300/40 bg-slate-50/40 p-4"
            >
              <div className="flex flex-wrap items-center gap-2">
                <span
                  className={`rounded-sm px-1.5 py-0.5 font-mono text-[10px] font-semibold ring-1 ${
                    MARKER_TONE[s.marker] ?? MARKER_TONE["[E]"]
                  }`}
                >
                  {s.marker}
                </span>
                <h3 className="font-serif text-base font-semibold text-slate-950">
                  {s.title}
                </h3>
                <span className="ml-auto font-mono text-[10px] text-slate-600">
                  {s.refs}
                </span>
              </div>
              <p className="mt-2 text-sm leading-relaxed text-slate-700">
                {s.body}
              </p>
            </li>
          ))}
        </ol>

        <div className="mt-6 flex flex-col gap-3 border border-rose-500/20 bg-rose-500/[0.04] px-4 py-3 sm:flex-row sm:items-center sm:justify-between sm:px-5">
          <p className="text-xs leading-relaxed text-slate-700">
            <span
              className={`mr-2 rounded-sm px-1.5 py-0.5 font-mono text-[10px] font-semibold ring-1 ${MARKER_TONE["[O]"]}`}
            >
              [O]
            </span>
            <span className="font-semibold text-slate-800">Not claimed closed:</span>{" "}
            the seam-realization bedrock (GATE.QGEO / QGEO.SYM.01) is still open. The
            parafermionic RP twist of the ℤ₃ orbifold (v639) is since resolved at the
            lattice OS level (v645: mirror × charge conjugation, η = (1,1) unique); the
            named residues — the continuum orbifold statement and the N_fam = 3 anchor —
            are tracked in the ledger, not hidden.
          </p>
          <Link
            prefetch={false}
            href="/verification#open-gates"
            className="inline-flex flex-none items-center gap-1.5 text-xs font-semibold text-blue-700 transition-colors hover:text-blue-800"
          >
            The open gates
            <ArrowRight size={13} aria-hidden />
          </Link>
        </div>
      </div>
    </section>
  );
}
