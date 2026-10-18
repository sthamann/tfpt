/**
 * Buried coincidences — the graveyard. Each card names a numerically
 * tempting reading and the module that killed it. This is the strongest
 * anti-numerology evidence the project has: the temptations were tested
 * and published as negatives, not quietly adopted.
 */

const GRAVES: {
  title: string;
  tempting: string;
  died: string;
  refs: string;
}[] = [
  {
    title: "|G31| = |W(D₅)| · |W(A₃)|",
    tempting:
      "The sixty-line reflection group has order 46080 = 1920 · 24 — exactly the product of the two compiler Weyl groups. It looked like the glue theorem written as group theory.",
    died:
      "Killed three ways: G31 is not isomorphic to the product (centers 4 vs 1), is no direct or semidirect product in either order (Lagrange kill), and W(D₅) does not even embed in any rank-4 unitary group. The order coincidence carries no structure.",
    refs: "v634",
  },
  {
    title: "The pₙ = 2 + 2ⁿ bytecode reading",
    tempting:
      "The anchor's power sums looked like they might be literal code operations in the Reed–Muller dictionary — 'the compiler numbers are code words'.",
    died:
      "0/11 natural code families reproduce the sequence; 18, 27, 81 have no code reading at all. The bingo is buried in public; only the σ-selected anchor decomposition survives as an exact statement.",
    refs: "v646",
  },
  {
    title: "The compiler clock as a square: c = w²",
    tempting:
      "The regular 24-element w satisfies w⁶ = ±J, so the order-12 compiler clock looked like its square — one clock, one origin.",
    died:
      "Killed by a parity theorem: 12-cycles of any square arise in pairs from 24-cycles, and the clock's census 19×12 + 3×4 has odd counts — impossible even in S₂₄₀. A power-census scan over all 46080 elements confirms it.",
    refs: "v647",
  },
  
  {
    title: "The naive 48 × 5 incidence on the E₈ roots",
    tempting:
      "240 = 48 · 5 — the seam sites times the carrier slots. An external review proposed building the roots canonically as (cover modes) × (carrier slots).",
    died:
      "The canonical order-12 element does not act freely (census 19×12 + 3×4, not 20 free orbits) — the construction fails at the first hurdle. The positive residue is sharp and smaller: the μ₄ clock alone acts freely with exactly 60 orbits.",
    refs: "v629",
  },
  {
    title: "The external review's B-test",
    tempting:
      "A follow-up test proposed by an external review looked like an independent check of the anchor bytecode.",
    died:
      "Machine-checked and found ill-posed as stated — recorded as such in the module instead of being silently reinterpreted until it passed.",
    refs: "v624",
  },
  
];

export function Graveyard() {
  return (
    <div className="grid gap-4 md:grid-cols-2">
      {GRAVES.map((g) => (
        <article
          key={g.title}
          className="flex flex-col rounded-2xl border border-rose-500/20 bg-slate-50/60 p-5"
        >
          <div className="flex items-start justify-between gap-3">
            <h3 className="font-mono text-sm font-semibold text-rose-800">
              {g.title}
            </h3>
            <span className="shrink-0 rounded-full bg-rose-500/10 px-2.5 py-0.5 font-mono text-[10px] font-semibold uppercase tracking-widest text-rose-700 ring-1 ring-rose-400/30">
              buried
            </span>
          </div>
          <p className="mt-3 text-sm leading-relaxed text-slate-700">
            <span className="font-semibold text-slate-800">
              What was tempting.{" "}
            </span>
            {g.tempting}
          </p>
          <p className="mt-2 text-sm leading-relaxed text-slate-600">
            <span className="font-semibold text-rose-800">How it died. </span>
            {g.died}
          </p>
          <div className="mt-auto pt-3 font-mono text-[11px] text-slate-600">
            evidence: {g.refs}
          </div>
        </article>
      ))}
    </div>
  );
}
